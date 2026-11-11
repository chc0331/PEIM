import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_concept_graph as exporter


CURRICULUM = """<a id="course-test"></a>

## 학습 과목

### 기존 단원

- [x] [A](../wiki/concepts/a.md) · [수행 기록](progress.md) <!-- topic-id:a -->

### 사진 대조 후 추가한 기초 학습 목표

- [ ] [B](../wiki/concepts/b.md) <!-- goal-id:b -->
"""


class ConceptGraphExportTests(unittest.TestCase):
    def test_public_snapshot_excludes_nonconcept_nodes_and_private_fields(self):
        graph = {
            "nodes": [
                {"id": "a", "label": "데이터 거버넌스", "source_file": "wiki/concepts/data-governance.md", "file_type": "concept", "evidence": "raw/private.md", "description": "데이터 관리 원칙"},
                {"id": "b", "label": "메타데이터", "source_file": "wiki/concepts/data-governance.md", "file_type": "concept"},
                {"id": "c", "label": "기출", "source_file": "wiki/questions/exam.md", "description": "study/private.md"},
            ],
            "links": [
                {"source": "a", "target": "b", "relation": "references", "confidence": "EXTRACTED", "description": "raw/private.md"},
                {"source": "a", "target": "c", "relation": "references", "confidence": "EXTRACTED"},
            ],
        }
        text = exporter.public_graph(graph, "2026-11-05", {"데이터 거버넌스": "wiki/concepts/data-governance.md"})
        result = json.loads(text)
        self.assertEqual([node["id"] for node in result["nodes"]], ["a", "b"])
        self.assertEqual([(edge["source"], edge["target"]) for edge in result["edges"]], [("a", "b")])
        for private in ("raw/", "study/", "evidence", "wiki/questions/", "private.md"):
            self.assertNotIn(private, text)

    def test_private_text_in_concept_description_is_rejected(self):
        graph = {"nodes": [{"id": "a", "label": "개념", "source_file": "wiki/concepts/a.md", "description": "study/progress.md"}], "links": []}
        with self.assertRaisesRegex(ValueError, "개인 기록"):
            exporter.public_graph(graph, "2026-11-05", {"개념": "wiki/concepts/a.md"})

    def test_reference_to_concept_document_opens_its_own_neighborhood(self):
        graph = {
            "nodes": [
                {"id": "a", "label": "A", "file_type": "concept", "source_file": "wiki/concepts/a.md"},
                {"id": "ref", "label": "B", "file_type": "document", "source_file": "wiki/concepts/a.md"},
                {"id": "b", "label": "B", "file_type": "document", "source_file": "wiki/concepts/b.md"},
                {"id": "c", "label": "C", "file_type": "concept", "source_file": "wiki/concepts/b.md"},
                {"id": "question", "label": "제140회 문제", "file_type": "document", "source_file": "wiki/concepts/a.md"},
            ],
            "links": [
                {"source": "a", "target": "ref", "relation": "references"},
                {"source": "b", "target": "c", "relation": "references"},
                {"source": "a", "target": "question", "relation": "references"},
            ],
        }
        result = json.loads(exporter.public_graph(graph, "2026-11-05", {"A": "wiki/concepts/a.md", "B": "wiki/concepts/b.md"}))
        self.assertEqual({node["id"] for node in result["nodes"]}, {"a", "b", "c"})
        self.assertEqual([(edge["source"], edge["target"]) for edge in result["edges"]], [("a", "b"), ("b", "c")])

    def test_overview_includes_the_canonical_node_for_each_concept_document(self):
        graph = {
            "nodes": [
                {"id": "a", "label": "A", "file_type": "concept", "source_file": "wiki/concepts/a.md"},
                {"id": "b-ref", "label": "B", "file_type": "document", "source_file": "wiki/concepts/a.md"},
                {"id": "b", "label": "B", "file_type": "document", "source_file": "wiki/concepts/b.md"},
                {"id": "detail", "label": "B detail", "file_type": "concept", "source_file": "wiki/concepts/b.md"},
                {"id": "c", "label": "C", "file_type": "concept", "source_file": "wiki/concepts/c.md"},
            ],
            "links": [{"source": "a", "target": "b-ref", "relation": "references"}],
        }
        titles = {"A": "wiki/concepts/a.md", "B": "wiki/concepts/b.md", "C": "wiki/concepts/c.md"}
        result = json.loads(exporter.public_graph(graph, "2026-11-10", titles))
        self.assertEqual(set(result["topic_ids"]), {"a", "b", "c"})
        self.assertEqual(len(result["topic_ids"]), 3)

    def test_classification_exports_course_topics_methods_and_unclassified(self):
        titles = {ident.upper(): f"wiki/concepts/{ident}.md" for ident in "abcd"}
        graph = {
            "nodes": [
                {"id": label.lower(), "label": label, "file_type": "concept", "source_file": source}
                for label, source in titles.items()
            ],
            "links": [],
        }
        classification = exporter.read_classification(CURRICULUM, {
            "additional_units": {"course-test": ["추가 단원"]},
            "placements": {"course-test": {"추가 단원": [titles["B"]]}},
            "study_methods": [titles["C"]],
        })
        text = exporter.public_graph(graph, "2026-11-10", titles, classification=classification)
        hierarchy = json.loads(text)["hierarchy"]
        self.assertEqual(hierarchy["courses"], [{
            "id": "course-test", "label": "학습 과목",
            "units": [
                {"id": "course-test-unit-1", "label": "기존 단원", "topic_ids": ["a"]},
                {"id": "course-test-unit-2", "label": "추가 단원", "topic_ids": ["b"]},
            ],
        }])
        self.assertEqual(hierarchy["study_methods"], ["c"])
        self.assertEqual(hierarchy["unclassified"], ["d"])
        self.assertNotIn("progress.md", text)
        self.assertNotIn("topic-id", text)

    def test_classification_rejects_duplicate_and_unknown_wiki_references(self):
        snapshot = {"nodes": [{"id": "a", "source_file": "wiki/concepts/a.md"}], "topic_ids": ["a"]}
        for source, error in [
            ("wiki/concepts/a.md", "대표 배치 중복"),
            ("wiki/concepts/missing.md", "공개 주제를 찾지 못했습니다"),
        ]:
            with self.subTest(source=source):
                classification = exporter.read_classification(CURRICULUM, {
                    "placements": {"course-test": {"기존 단원": [source]}},
                })
                with self.assertRaisesRegex(ValueError, error):
                    exporter.topic_hierarchy(snapshot, classification)
        with self.assertRaisesRegex(ValueError, "대표 배치의 단원을 찾지 못했습니다"):
            exporter.read_classification(CURRICULUM, {"placements": {"course-test": {"없는 단원": []}}})

    def test_stale_graph_does_not_create_site(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            output = root / "published"
            with patch.object(exporter, "status", return_value={"status": "갱신 필요"}):
                with self.assertRaisesRegex(ValueError, "그래프 갱신"):
                    exporter.export(root, output)
            self.assertFalse(output.exists())

    def test_export_to_source_and_separate_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            site = root / "site" / "concept-graph"
            site.mkdir(parents=True)
            for name in exporter.SITE_FILES:
                (site / name).write_text(f"existing {name}", encoding="utf-8")
            graph_dir = root / "graphify-out"
            graph_dir.mkdir()
            graph = {
                "nodes": [{"id": "a", "label": "A", "file_type": "concept", "source_file": "wiki/concepts/a.md"}],
                "links": [],
            }
            (graph_dir / "graph.json").write_text(json.dumps(graph), encoding="utf-8")
            (root / "study").mkdir()
            (root / "study/curriculum.md").write_text(CURRICULUM, encoding="utf-8")
            (root / "docs").mkdir()
            (root / "docs/concept-graph-placements.json").write_text("{}", encoding="utf-8")
            state = {"status": "ready", "nodes": 1, "edges": 0, "built_at": "2026-11-10"}
            docs = {"wiki/concepts/a.md": {"meta": {"title": "A", "type": "concept"}}}
            with patch.object(exporter, "SITE_SOURCE", site), \
                 patch.object(exporter, "status", return_value=state), \
                 patch.object(exporter, "lint", return_value=(docs, {})):
                exporter.export(root, site)
                self.assertEqual((site / "index.html").read_text(), "existing index.html")
                snapshot = json.loads((site / "graph-data.json").read_text())
                self.assertEqual(snapshot["nodes"][0]["label"], "A")
                self.assertEqual(snapshot["hierarchy"]["courses"][0]["units"][0]["topic_ids"], ["a"])

                separate = root / "separate"
                exporter.export(root, separate)
                self.assertEqual((separate / "app.js").read_text(), "existing app.js")
                self.assertEqual((separate / "graph-data.json").read_text(), (site / "graph-data.json").read_text())

                with self.assertRaisesRegex(ValueError, "프로젝트 루트"):
                    exporter.export(root, root)


if __name__ == "__main__":
    unittest.main()
