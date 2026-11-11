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
COURSE_ANCHOR = re.compile(r'<a id="(course-[a-z0-9-]+)"></a>')
TOPIC_MARKER = re.compile(r"<!-- topic-id:[a-z0-9-]+ -->")
TOPIC_LINK = re.compile(r"\]\(\.\./(wiki/concepts/[a-z0-9-]+\.md)\)")


def read_classification(curriculum, additions):
    """Read course headings, unit headings and topic links from the curriculum."""
    courses = {}
    course = pending_course_id = unit = None
    for line in curriculum.splitlines():
        if anchor := COURSE_ANCHOR.fullmatch(line.strip()):
            pending_course_id = anchor[1]
        elif line.startswith("## "):
            course = None
            unit = None
            if pending_course_id:
                if pending_course_id in courses:
                    raise ValueError(f"커리큘럼 과목 ID 중복: {pending_course_id}")
                course = {"id": pending_course_id, "label": line[3:].strip(), "units": {}}
                courses[pending_course_id] = course
                pending_course_id = None
        elif course and line.startswith("### "):
            unit = line[4:].strip()
        elif marker := TOPIC_MARKER.search(line):
            sources = TOPIC_LINK.findall(line)
            if not course or not unit or len(sources) != 1:
                raise ValueError(f"커리큘럼 과목·단원 또는 위키 링크를 확인하세요: {marker[0]}")
            course["units"].setdefault(unit, []).append(sources[0])

    if not courses:
        raise ValueError("커리큘럼에서 학습 과목을 찾지 못했습니다")
    for course_id, labels in additions.get("additional_units", {}).items():
        if course_id not in courses:
            raise ValueError(f"추가 단원의 과목을 찾지 못했습니다: {course_id}")
        units = courses[course_id]["units"]
        for label in labels:
            if label in units:
                raise ValueError(f"추가 단원 중복: {course_id} / {label}")
            units[label] = []

    for course_id, placements in additions.get("placements", {}).items():
        if course_id not in courses:
            raise ValueError(f"대표 배치의 과목을 찾지 못했습니다: {course_id}")
        units = courses[course_id]["units"]
        for label, sources in placements.items():
            if label not in units:
                raise ValueError(f"대표 배치의 단원을 찾지 못했습니다: {course_id} / {label}")
            units[label].extend(sources)

    return {"courses": list(courses.values()), "study_methods": additions.get("study_methods", [])}


def topic_hierarchy(snapshot, classification):
    files_by_id = {node["id"]: node["source_file"] for node in snapshot["nodes"]}
    topics_by_file = {files_by_id[ident]: ident for ident in snapshot["topic_ids"]}
    if len(topics_by_file) != len(snapshot["topic_ids"]):
        raise ValueError("같은 위키 문서에 대표 주제가 여러 개 있습니다")
    assigned = set()

    def assign(sources):
        topic_ids = []
        for source in sources:
            if source not in topics_by_file:
                raise ValueError(f"대표 배치에서 공개 주제를 찾지 못했습니다: {source}")
            if source in assigned:
                raise ValueError(f"대표 배치 중복: {source}")
            assigned.add(source)
            topic_ids.append(topics_by_file[source])
        return topic_ids

    courses = []
    for course in classification["courses"]:
        course_id = course["id"]
        units = [
            {"id": f"{course_id}-unit-{index}", "label": label, "topic_ids": assign(sources)}
            for index, (label, sources) in enumerate(course["units"].items(), start=1)
        ]
        courses.append({"id": course_id, "label": course["label"], "units": units})
    methods = assign(classification["study_methods"])
    return {
        "courses": courses,
        "study_methods": methods,
        "unclassified": [ident for source, ident in topics_by_file.items() if source not in assigned],
    }


def public_graph(graph, built_at, concept_titles, *, classification=None):
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
        "topic_ids": [item["id"] for _, item in sorted(canonical.items()) if item["id"] in ids],
    }
    if classification is not None:
        result["hierarchy"] = topic_hierarchy(result, classification)
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
    classification = read_classification(
        (root / "study/curriculum.md").read_text(encoding="utf-8"),
        json.loads((root / "docs/concept-graph-placements.json").read_text(encoding="utf-8")),
    )
    data = public_graph(graph, state["built_at"], concept_titles, classification=classification)
    output = output.resolve()
    if output == root.resolve():
        raise ValueError("출력 위치는 프로젝트 루트가 아니어야 합니다")
    output.mkdir(parents=True, exist_ok=True)
    if output != SITE_SOURCE.resolve():
        for name in SITE_FILES:
            shutil.copyfile(SITE_SOURCE / name, output / name)
    (output / "graph-data.json").write_text(data, encoding="utf-8")
    result = json.loads(data)
    return {"output": str(output), "nodes": len(result["nodes"]), "edges": len(result["edges"])}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="공개 사이트 파일을 저장할 디렉터리")
    args = parser.parse_args()
    print(json.dumps(export(ROOT, args.output), ensure_ascii=False))
