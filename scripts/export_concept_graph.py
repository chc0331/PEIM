"""Export a reviewed, concept-only snapshot for the public GitHub Pages site."""

import argparse
import json
from pathlib import Path
import re
import shutil

from wiki import lint, status


ROOT = Path(__file__).resolve().parents[1]
SITE_SOURCE = ROOT / "site/concept-graph"
SITE_FILES = ("index.html", "style.css", "app.js", ".nojekyll")
CONCEPT_PATH = re.compile(r"wiki/concepts/[a-z0-9-]+\.md\Z")
PRIVATE_TEXT = re.compile(r"raw/|study/|graphify-out/|/Users/|file://|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", re.I)


def public_graph(graph, built_at, concept_titles):
    """Keep only fields and edges required to browse concept documents."""
    canonical = {}
    for item in graph["nodes"]:
        source = item.get("source_file", "")
        label = item.get("label", "")
        if source == concept_titles.get(label) and item.get("file_type") in ("concept", "document"):
            previous = canonical.get(label)
            if previous is None or (item["file_type"] == "document" and previous["file_type"] != "document"):
                canonical[label] = item
    remap = {}
    nodes = []
    for item in graph["nodes"]:
        source = item.get("source_file", "")
        if not source.startswith("wiki/concepts/"):
            continue
        if not CONCEPT_PATH.fullmatch(source):
            raise ValueError(f"허용되지 않은 개념 문서 경로: {source}")
        if item.get("file_type") == "document":
            target = canonical.get(item["label"])
            if target is None:
                continue  # cited source or exam question, not a concept document
            if target["id"] != item["id"]:
                remap[item["id"]] = target["id"]
                continue
        nodes.append({
            "id": item["id"],
            "label": item["label"],
            "aliases": item.get("aliases") or [],
            "description": item.get("description") or "",
            "file_type": item.get("file_type") or "concept",
            "document_status": item.get("document_status") or "미검증",
            "review_status": item.get("review_status") or "",
            "source_file": source,
            "source_location": item.get("source_location") or "",
        })
    if not nodes:
        raise ValueError("공개할 개념 노드가 없습니다")
    ids = {item["id"] for item in nodes}
    if len(ids) != len(nodes):
        raise ValueError("개념 노드 ID가 중복되었습니다")
    edges = []
    seen_edges = set()
    for item in graph["links"]:
        source = remap.get(item["source"], item["source"])
        target = remap.get(item["target"], item["target"])
        if source not in ids or target not in ids or source == target:
            continue
        key = (source, target, item.get("relation") or "related_to", item.get("confidence") or "AMBIGUOUS")
        if key not in seen_edges:
            edges.append({"source": key[0], "target": key[1], "relation": key[2], "confidence": key[3]})
            seen_edges.add(key)
    result = {
        "built_at": built_at,
        "nodes": nodes,
        "edges": edges,
    }
    serialized = json.dumps(result, ensure_ascii=False, separators=(",", ":"))
    if PRIVATE_TEXT.search(serialized):
        raise ValueError("공개 데이터에 개인 기록·원자료 경로 또는 이메일이 포함되었습니다")
    return serialized + "\n"


def export(root, output):
    state = status(root)
    if state.get("status") != "ready":
        raise ValueError("그래프 갱신이 필요합니다. wiki.py prepare/accept/build를 완료하세요")
    graph = json.loads((root / "graphify-out/graph.json").read_text(encoding="utf-8"))
    if len(graph["nodes"]) != state["nodes"] or len(graph["links"]) != state["edges"]:
        raise ValueError("그래프 파일과 빌드 상태의 노드·관계 수가 다릅니다")
    docs, _ = lint(root)
    concept_titles = {doc["meta"]["title"]: path for path, doc in docs.items() if doc["meta"]["type"] == "concept"}
    data = public_graph(graph, state["built_at"], concept_titles)
    output = output.resolve()
    if output == root.resolve() or output == SITE_SOURCE.resolve():
        raise ValueError("출력 위치는 프로젝트 루트와 사이트 원본 폴더가 아니어야 합니다")
    output.mkdir(parents=True, exist_ok=True)
    for name in SITE_FILES:
        shutil.copyfile(SITE_SOURCE / name, output / name)
    (output / "graph-data.json").write_text(data, encoding="utf-8")
    result = json.loads(data)
    return {"output": str(output), "nodes": len(result["nodes"]), "edges": len(result["edges"])}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="공개 사이트 저장소의 루트 경로")
    args = parser.parse_args()
    print(json.dumps(export(ROOT, args.output), ensure_ascii=False))
