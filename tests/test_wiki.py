import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import yaml

spec = importlib.util.spec_from_file_location("wiki", Path(__file__).resolve().parents[1] / "scripts/wiki.py")
wiki = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wiki)


class WikiLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for folder in ("raw", "study/reviews", "wiki/concepts", "wiki/sources", "wiki/questions", "wiki/comparisons", "graphify-out"):
            (self.root / folder).mkdir(parents=True, exist_ok=True)
        (self.root / wiki.SPEC).parent.mkdir(parents=True)
        (self.root / wiki.SPEC).write_text("test extraction contract")
        (self.root / "wiki/log.md").write_text("# Log\n")
        (self.root / "raw/original.md").write_text("preserve original")
        (self.root / "study/reviews/private.md").write_text("student wrong answer; score: 5")
        self.doc("a", "회상 연습", ["Active recall", "인출 연습"])
        self.doc("b", "답안 훈련", ["Answer practice"])

    def doc(self, ident, title, aliases=None, status="미검증", body="Test training document."):
        meta = {"id": "concept-" + ident, "title": title, "aliases": aliases or [], "type": "concept", "domains": ["test"], "sources": [], "status": status, "updated": "2026-09-06"}
        p = self.root / f"wiki/concepts/{ident}.md"
        p.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n# " + title + "\n" + body, encoding="utf-8")
        return p

    def extraction(self, wanted=None, old=False):
        wanted = wanted or ["a", "b"]
        nodes = []
        for ident in wanted:
            name = f"wiki/concepts/{ident}.md"
            nodes.append({"id": f"wiki_concepts_{ident}_entity", "label": f"{'Old' if old else 'New'} {ident}", "file_type": "concept", "source_file": name, "source_location": "line 1"})
        edges = []
        if "a" in wanted:
            edges.append({"source": "wiki_concepts_a_entity", "target": "wiki_concepts_b_entity", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": "wiki/concepts/a.md", "source_location": "line 1", "weight": 1.0})
        return {"nodes": nodes, "edges": edges, "hyperedges": [], "input_tokens": None, "output_tokens": None}

    def accept(self, extraction):
        p = self.root / "graphify-out/test-extraction.json"
        wiki.write_json(p, extraction)
        return wiki.accept(self.root, p, self.root / "graphify-out/extraction-request.json")

    def initial(self):
        wiki.prepare(self.root)
        self.accept(self.extraction(old=True))
        wiki.build(self.root)

    def test_prepare_is_idempotent_and_excludes_personal_data(self):
        first = wiki.prepare(self.root)
        self.assertEqual(len(first["semantic_pending"]), 2)
        before = (self.root / "wiki/log.md").read_bytes()
        second = wiki.prepare(self.root)
        self.assertEqual(second["changed"], [])
        self.assertEqual(before, (self.root / "wiki/log.md").read_bytes())
        request = wiki.read_json(self.root / "graphify-out/extraction-request.json")
        self.assertTrue(all(n.startswith("wiki/concepts/") for n in request["files"]))
        self.assertNotIn("score", (self.root / "wiki/index.md").read_text())

    def test_aliases_return_same_page(self):
        self.assertEqual(wiki.search(self.root, "회상 연습")[0]["path"], wiki.search(self.root, "ACTIVE RECALL")[0]["path"])
        self.assertEqual(wiki.search(self.root, "인출 연습")[0]["path"], "wiki/concepts/a.md")

    def test_duplicate_alias_and_broken_link_rejected(self):
        self.doc("c", "Different", ["Active recall"])
        with self.assertRaisesRegex(ValueError, "별칭 중복"):
            wiki.lint(self.root)
        (self.root / "wiki/concepts/c.md").unlink()
        self.doc("b", "답안 훈련", body="[missing](missing.md)")
        with self.assertRaisesRegex(ValueError, "끊어진 링크"):
            wiki.lint(self.root)

    def test_existing_raw_cannot_be_modified_or_deleted(self):
        wiki.prepare(self.root)
        p = self.root / "raw/original.md"
        p.write_text("changed")
        with self.assertRaisesRegex(ValueError, "원자료 변경"):
            wiki.prepare(self.root)
        p.unlink()
        with self.assertRaisesRegex(ValueError, "원자료 변경"):
            wiki.lint(self.root)

    def test_missing_evidence_cannot_be_marked_verified(self):
        self.doc("a", "회상 연습", status="출처 확인")
        with self.assertRaisesRegex(ValueError, "근거 없음"):
            wiki.lint(self.root)

    def test_official_question_requires_traceable_number_and_page(self):
        path = self.root / "wiki/questions/exam.md"
        meta = {"id": "question-exam", "title": "공식 문제", "aliases": [], "type": "question",
                "question_kind": "공식 기출", "domains": ["test"], "sources": [{"path": "raw/original.md", "locator": "PDF p. 1"}],
                "status": "출처 확인", "updated": "2026-11-01"}

        def save(body='\n<a id="q1"></a>\n'):
            path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n" + body)

        save()
        with self.assertRaisesRegex(ValueError, "회차·교시"):
            wiki.lint(self.root)
        meta.update(exam_round=140, exam_session=1, questions=[{"number": 1, "pdf_pages": [1]}])
        save()
        wiki.lint(self.root)
        meta["questions"][0]["pdf_pages"] = []
        save()
        with self.assertRaisesRegex(ValueError, "문항 번호·페이지"):
            wiki.lint(self.root)
        meta["questions"][0]["pdf_pages"] = [1]
        save("missing anchor")
        with self.assertRaisesRegex(ValueError, "본문 위치"):
            wiki.lint(self.root)
        meta["questions"].append({"number": 1, "pdf_pages": [2]})
        save()
        with self.assertRaisesRegex(ValueError, "중복·누락"):
            wiki.lint(self.root)

    def test_conflicting_status_is_preserved(self):
        self.doc("a", "회상 연습", status="상충", body="Source one and source two disagree. Do not resolve automatically.")
        wiki.prepare(self.root)
        self.accept(self.extraction())
        self.assertEqual(wiki.read_json(self.root / "graphify-out/semantic-cache.json")["wiki/concepts/a.md"]["nodes"][0]["document_status"], "상충")

    def test_concept_alias_merge_keeps_all_evidence_and_question_nodes(self):
        docs = wiki.pages(self.root)
        nodes = [
            {"id": "canonical", "label": "회상 연습", "file_type": "concept", "source_file": "wiki/concepts/a.md", "source_location": "정의"},
            {"id": "mention", "label": "Active recall", "file_type": "concept", "source_file": "wiki/questions/exam.md", "source_location": "문항 q1 / PDF p.1"},
            {"id": "question", "label": "회상 연습", "file_type": "document", "source_file": "wiki/questions/exam.md"},
        ]
        edges = [{"source": "question", "target": "mention"}]
        merged, rewritten, _ = wiki.merge_concepts(nodes, edges, docs)
        self.assertEqual({n["id"] for n in merged}, {"canonical", "question"})
        self.assertEqual(rewritten, [{"source": "question", "target": "canonical"}])
        concept = next(n for n in merged if n["id"] == "canonical")
        self.assertEqual(len(concept["evidence"]), 2)
        self.assertEqual(wiki.merge_concepts(list(reversed(nodes)), edges, docs)[2]["mention"], "canonical")

    def test_stale_receipt_and_missing_output_rejected(self):
        wiki.prepare(self.root)
        self.doc("a", "회상 연습", body="changed while agent was extracting")
        with self.assertRaisesRegex(ValueError, "추출 이후 문서 변경"):
            self.accept(self.extraction())
        wiki.prepare(self.root)
        with self.assertRaisesRegex(ValueError, "추출 누락"):
            self.accept(self.extraction(["b"]))
        self.assertFalse((self.root / "graphify-out/semantic-cache.json").exists())

    def test_private_extraction_is_rejected(self):
        wiki.prepare(self.root)
        data = self.extraction()
        data["nodes"][0]["source_file"] = "study/reviews/private.md"
        with self.assertRaisesRegex(ValueError, "허용되지 않은"):
            self.accept(data)

    def test_incremental_update_deletion_and_direction(self):
        self.initial()
        first = wiki.read_json(self.root / "graphify-out/graph.json")
        self.assertTrue(first["directed"])
        self.assertEqual(len(first["nodes"]), 2)
        edge = first.get("links", first.get("edges"))[0]
        labels = {n["id"]: n["label"] for n in first["nodes"]}
        self.assertEqual(labels[edge["source"]], "Old a")
        self.assertEqual(labels[edge["target"]], "Old b")
        self.doc("a", "회상 연습", body="new content")
        self.assertEqual(wiki.status(self.root)["status"], "갱신 필요")
        self.assertEqual(wiki.prepare(self.root)["semantic_pending"], ["wiki/concepts/a.md"])
        self.accept(self.extraction(["a"]))
        wiki.build(self.root)
        graph = wiki.read_json(self.root / "graphify-out/graph.json")
        self.assertEqual({n["label"] for n in graph["nodes"]}, {"New a", "Old b"})
        (self.root / "wiki/concepts/b.md").unlink()
        self.assertEqual(wiki.prepare(self.root)["semantic_pending"], [])
        wiki.build(self.root)
        graph = wiki.read_json(self.root / "graphify-out/graph.json")
        self.assertEqual([n["label"] for n in graph["nodes"]], ["New a"])
        self.assertEqual(graph.get("links", graph.get("edges")), [])
        self.assertEqual(wiki.status(self.root)["status"], "ready")
        self.assertEqual(len(wiki.read_json(self.root / "graphify-out/semantic-cache.json")), 1)

    def test_failed_build_keeps_previous_graph_and_marks_stale(self):
        self.initial()
        before = (self.root / "graphify-out/graph.json").read_bytes()
        with patch("graphify.exporters.html.to_html", side_effect=RuntimeError("renderer failure")):
            with patch("sys.argv", ["wiki", "--root", str(self.root), "build"]):
                self.assertEqual(wiki.main(), 1)
        self.assertEqual(before, (self.root / "graphify-out/graph.json").read_bytes())
        self.assertEqual(wiki.status(self.root)["status"], "갱신 필요")
        self.assertTrue(wiki.search(self.root, "회상"))
        wiki.build(self.root)
        self.assertEqual(wiki.status(self.root)["status"], "ready")

    def test_no_change_reuses_extraction_and_does_not_grow_graph(self):
        self.initial()
        state = wiki.status(self.root)
        self.assertEqual(wiki.prepare(self.root)["semantic_pending"], [])
        wiki.build(self.root)
        self.assertEqual(wiki.status(self.root)["nodes"], state["nodes"])
        self.assertEqual(wiki.status(self.root)["edges"], state["edges"])
        report = (self.root / "graphify-out/GRAPH_REPORT.md").read_text()
        self.assertNotIn("0 input", report)
        self.assertIn("미측정", report)


if __name__ == "__main__":
    unittest.main()
