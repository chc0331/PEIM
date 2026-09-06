#!/usr/bin/env python3
"""Local wiki checks and a content-addressed, session-mediated Graphify bridge."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unicodedata
from datetime import datetime
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = {"sources": "source", "concepts": "concept", "comparisons": "comparison", "questions": "question"}
STATES = {"미검증", "출처 확인", "상충", "구버전"}
SPEC = ".codex/skills/graphify/references/extraction-spec.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")


def read_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else ({} if default is None else default)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def normalize(value):
    return re.sub(r"[\s_-]+", "", unicodedata.normalize("NFKC", str(value)).casefold())


def relative(root, value):
    p = Path(value)
    p = p if p.is_absolute() else root / p
    return p.resolve().relative_to(root.resolve()).as_posix()


def pages(root):
    result = {}
    for folder in SECTIONS:
        for p in sorted((root / "wiki" / folder).rglob("*.md")):
            if p.is_symlink():
                raise ValueError(f"심볼릭 링크는 위키 입력에서 제외: {p}")
            text = p.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
            if not match:
                raise ValueError(f"문서 메타데이터 없음: {p}")
            meta = yaml.safe_load(match[1])
            if not isinstance(meta, dict):
                raise ValueError(f"잘못된 메타데이터: {p}")
            result[p.relative_to(root).as_posix()] = {"meta": meta, "text": text, "hash": digest(p)}
    return result


def lint(root):
    docs = pages(root)
    ids, aliases, errors = {}, {}, []
    for name, doc in docs.items():
        m = doc["meta"]
        for key in ("id", "title", "aliases", "type", "domains", "sources", "status", "updated"):
            if key not in m:
                errors.append(f"{name}: {key} 누락")
        ident = m.get("id", "")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(ident)) or ident in ids:
            errors.append(f"{name}: 잘못되거나 중복된 ID {ident}")
        ids[ident] = name
        if m.get("type") != SECTIONS[name.split("/")[1]] or m.get("status") not in STATES:
            errors.append(f"{name}: 문서 유형 또는 검증 상태 오류")
        for key in ("aliases", "domains", "sources"):
            if not isinstance(m.get(key), list):
                errors.append(f"{name}: {key}는 목록이어야 함")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(m.get("updated", ""))):
            errors.append(f"{name}: 갱신일 형식 오류")
        for alias in [m.get("title", ""), *(m.get("aliases") or [])]:
            key = normalize(alias)
            if key in aliases and aliases[key] != name:
                errors.append(f"별칭 중복: {alias}: {aliases[key]} / {name}")
            aliases[key] = name
        if any(k in m for k in ("score", "mastery", "student_answer")):
            errors.append(f"{name}: 개인 수행 기록은 study에 저장")
        if m.get("type") == "question" and m.get("question_kind") not in ("공식 기출", "훈련 문제"):
            errors.append(f"{name}: 공식 기출/훈련 문제 구분 필요")
        if m.get("status") == "출처 확인" and not m.get("sources"):
            errors.append(f"{name}: 출처 확인 상태에 근거 없음")
    for name, doc in docs.items():
        m = doc["meta"]
        for source in m.get("sources", []):
            if not isinstance(source, dict) or not (source.get("id") or source.get("path")):
                errors.append(f"{name}: 출처 ID 또는 보관 경로 필요")
                continue
            if source.get("id") and source["id"] not in ids:
                errors.append(f"{name}: 없는 출처 ID {source['id']}")
            if source.get("path"):
                p = relative(root, source["path"])
                if not p.startswith("raw/") or not (root / p).is_file():
                    errors.append(f"{name}: 없는 원자료 {p}")
        if m.get("type") == "source":
            if not str(m.get("source_url", "")).startswith(("https://", "http://")):
                errors.append(f"{name}: 출처 원문 URL 필요")
            if not any(s.get("path") for s in m.get("sources", []) if isinstance(s, dict)):
                errors.append(f"{name}: 출처 참조 원자료 필요")
        # The project deliberately uses ordinary relative Markdown links.
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", doc["text"]):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            target = target.strip("<>").split("#")[0]
            p = (root / name).parent / target
            if not p.exists():
                errors.append(f"{name}: 끊어진 링크 {target}")
        if "[[" in doc["text"]:
            errors.append(f"{name}: 이 프로젝트는 일반 Markdown 링크를 사용")
    raw_hashes = {p.relative_to(root).as_posix(): digest(p) for p in sorted((root / "raw").rglob("*")) if p.is_file()}
    saved = read_json(root / "study/.maintenance.json").get("raw_hashes", {})
    for name, h in saved.items():
        if raw_hashes.get(name) != h:
            errors.append(f"원자료 변경/삭제 감지: {name}; 새 버전으로 보관할 것")
    if errors:
        raise ValueError("\n".join(errors))
    return docs, raw_hashes


def mark_stale(root, reason):
    out = root / "graphify-out"
    out.mkdir(exist_ok=True)
    (out / ".needs_update").write_text(reason + "\n", encoding="utf-8")


def cache_valid(entry, doc, contract):
    return entry.get("hash") == doc["hash"] and entry.get("contract") == contract


def prepare(root):
    docs, raw_hashes = lint(root)
    state_path = root / "study/.maintenance.json"
    state = read_json(state_path)
    hashes = {n: d["hash"] for n, d in docs.items()}
    before = state.get("wiki_hashes", {})
    changed = sorted(n for n in hashes if before.get(n) != hashes[n])
    deleted = sorted(set(before) - set(hashes))
    lines = ["# 학습 위키", "", "출처 확인은 학습 완료가 아닙니다. 개인 진도는 [학습 현황](../study/progress.md)을 확인하세요.", ""]
    for folder, kind in SECTIONS.items():
        lines += [f"## {folder}", ""]
        for name, d in docs.items():
            m = d["meta"]
            if m["type"] == kind:
                lines.append(f"- [{m['title']}]({name.removeprefix('wiki/')}) — {m['status']}; {', '.join(m['domains'])}")
        if not any(d["meta"]["type"] == kind for d in docs.values()):
            lines.append("아직 등록된 문서가 없습니다.")
        lines.append("")
    (root / "wiki/index.md").write_text("\n".join(lines), encoding="utf-8")
    if changed or deleted or state.get("raw_hashes") != raw_hashes:
        with (root / "wiki/log.md").open("a", encoding="utf-8") as f:
            f.write(f"\n## [{now()}] sync\n\n")
            for n in changed:
                f.write(f"- 반영: [{docs[n]['meta']['title']}]({n.removeprefix('wiki/')})\n")
            for n in deleted:
                f.write(f"- 삭제 반영: `{n}`\n")
            f.write("- 학습 숙련도는 자동 변경하지 않음. 문서 의미·상충 검토는 강사가 수행.\n")
    write_json(state_path, {"wiki_hashes": hashes, "raw_hashes": raw_hashes})
    cache = read_json(root / "graphify-out/semantic-cache.json")
    contract = digest(root / SPEC)
    pending = {n: d["hash"] for n, d in docs.items() if not cache_valid(cache.get(n, {}), d, contract)}
    request = {"files": pending, "all_files": hashes, "contract": contract,
               "instruction": "Read only files listed in files. Use the installed extraction specification. No external API. Return standard Graphify JSON; never invent missing output."}
    write_json(root / "graphify-out/extraction-request.json", request)
    if pending or read_json(root / "graphify-out/state.json").get("files") != hashes:
        mark_stale(root, "문서 변경: 의미 추출 또는 그래프 재생성 필요")
    return {"documents": len(docs), "changed": changed, "deleted": deleted, "semantic_pending": list(pending)}


def accept(root, extraction_path, request_path):
    from graphify.validate import validate_extraction
    docs, _ = lint(root)
    request = read_json(request_path)
    wanted = request.get("files", {})
    if not wanted:
        raise ValueError("추출 요청에 파일이 없음")
    contract = digest(root / SPEC)
    if request.get("contract", contract) != contract:
        raise ValueError("추출 규칙 변경: 다시 prepare 후 추출")
    for name, h in wanted.items():
        if name not in docs or docs[name]["hash"] != h:
            raise ValueError(f"추출 이후 문서 변경/삭제: {name}")
    extraction = read_json(extraction_path)
    cache = read_json(root / "graphify-out/semantic-cache.json")
    for key in ("nodes", "edges", "hyperedges"):
        if not isinstance(extraction.get(key, []), list):
            raise ValueError(f"잘못된 추출 형식: {key}")
        for item in extraction.get(key, []):
            name = relative(root, item.get("source_file", ""))
            if name not in wanted:
                raise ValueError(f"허용되지 않은 추출 출처: {name}")
            item["source_file"] = name
    old_nodes = [node for n, e in cache.items() if n in docs and n not in wanted and cache_valid(e, docs[n], contract) for node in e["nodes"]]
    errors = validate_extraction({**extraction, "nodes": old_nodes + extraction.get("nodes", [])})
    if errors:
        raise ValueError("Graphify 추출 검증 실패: " + "; ".join(errors[:10]))
    for name in wanted:
        nodes = [n for n in extraction.get("nodes", []) if n["source_file"] == name]
        if not nodes:
            raise ValueError(f"추출 누락: {name}; 완료 처리하지 않음")
    updates = {}
    for name in wanted:
        m = docs[name]["meta"]
        entry = {"hash": wanted[name], "contract": contract}
        for key in ("nodes", "edges", "hyperedges"):
            entry[key] = [item for item in extraction.get(key, []) if item["source_file"] == name]
        for node in entry["nodes"]:
            node["document_id"] = m["id"]
            node["document_status"] = m["status"]
            node["source_url"] = m.get("source_url")
            node["wiki_sources"] = m["sources"]
        updates[name] = entry
    cache.update(updates)
    write_json(root / "graphify-out/semantic-cache.json", cache)
    mark_stale(root, "추출 수락됨: build 실행 필요")
    return {"accepted": len(updates)}


def build(root):
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all, label_communities_by_hub
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.export import to_json
    from graphify.exporters.html import to_html
    from graphify.report import generate
    docs, _ = lint(root)
    cache = read_json(root / "graphify-out/semantic-cache.json")
    contract = digest(root / SPEC)
    pending = [n for n, d in docs.items() if not cache_valid(cache.get(n, {}), d, contract)]
    if pending:
        raise ValueError("의미 추출 필요: " + ", ".join(pending))
    current = {n: cache[n] for n in docs}
    nodes = [v for e in current.values() for v in e["nodes"]]
    node_ids = {n["id"] for n in nodes}
    edges = [v for e in current.values() for v in e["edges"] if v["source"] in node_ids and v["target"] in node_ids]
    hyperedges = [v for e in current.values() for v in e.get("hyperedges", []) if all(n in node_ids for n in v["nodes"])]
    G = build_from_json({"nodes": nodes, "edges": edges, "hyperedges": hyperedges}, directed=True, root=root)
    # Graphify can coalesce a document node and same-named concept into one ID.
    # A page referring to that concept must not become a spurious self-reference.
    G.remove_edges_from([(u, v) for u, v in G.edges() if u == v])
    communities = cluster(G)
    labels = label_communities_by_hub(G, communities)
    questions = suggest_questions(G, communities, labels)
    report = generate(G, communities, score_all(G.to_undirected(), communities), labels, god_nodes(G), surprising_connections(G, communities),
                      {"total_files": len(docs), "total_words": sum(len(d['text'].split()) for d in docs.values())},
                      {"input": 0, "output": 0}, str(root), suggested_questions=questions)
    # Upstream report accepts numeric counters only. Never present placeholders as measured usage.
    report = re.sub(r"(?ms)^## Token [^\n]*\n.*?(?=^## |\Z)", "## Token Usage\n\n세션 의미 추출 토큰 수는 제공되지 않아 미측정입니다. 0 또는 무료라는 뜻이 아닙니다.\n\n", report)
    report = re.sub(r"(?m)^- Token cost:.*$", "- Token cost: 미측정 (세션 사용량 미제공; 0 또는 무료를 뜻하지 않음)", report)
    report = re.sub(r"(?m)^- Verdict:.*$", "- 활용성: 실제 질의 사례로 검증하며 토큰 절감률은 미측정", report)
    report = "# 학습 그래프 안내\n\n관계 추출·중심성은 사실 검증, 출제 빈도, 학습 숙련도를 뜻하지 않습니다.\n\n" + report
    report += "\n## 위키와 원출처 탐색\n\n"
    for name, d in docs.items():
        report += f"- [{d['meta']['title']}](../{name}) — {d['meta']['status']}\n"
    out = root / "graphify-out"
    out.mkdir(exist_ok=True)
    # Build all outputs before publishing; failures leave the previous graph usable.
    with tempfile.TemporaryDirectory(prefix=".build-", dir=out) as temp:
        stage = Path(temp)
        to_json(G, communities, str(stage / "graph.json"), force=True, community_labels=labels)
        to_html(G, communities, str(stage / "graph.html"), community_labels=labels, learning_overlay={})
        html_path = stage / "graph.html"
        html = re.sub(r"<title>.*?</title>", "<title>정보관리기술사 학습 그래프</title>", html_path.read_text(encoding="utf-8"))
        # Keep the native Graphify view; make its existing source field navigable.
        source_field = '<div class="field">Source: ${esc(n._source_file || \'-\')}</div>'
        source_link = '<div class="field">Source: <a style="color:#9dccff" target="_blank" rel="noopener" href="../${(n._source_file || \'\').split(\'/\').map(encodeURIComponent).join(\'/\')}">${esc(n._source_file || \'-\')}</a></div>'
        if source_field not in html:
            raise ValueError("Graphify HTML 형식 변경: 출처 링크 연동 재검증 필요")
        html_path.write_text(html.replace(source_field, source_link), encoding="utf-8")
        (stage / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
        for name in ("graph.json", "graph.html", "GRAPH_REPORT.md"):
            if not (stage / name).is_file():
                raise ValueError(f"Graphify 출력 누락: {name}")
        backup = out / "last-good"
        backup.mkdir(exist_ok=True)
        for name in ("graph.json", "graph.html", "GRAPH_REPORT.md", "state.json"):
            if (out / name).exists():
                shutil.copy2(out / name, backup / name)
        published = []
        try:
            for name in ("graph.json", "graph.html", "GRAPH_REPORT.md"):
                os.replace(stage / name, out / name)
                published.append(name)
        except OSError:
            for name in published:
                if (backup / name).exists():
                    shutil.copy2(backup / name, out / name)
                else:
                    (out / name).unlink(missing_ok=True)
            raise
    write_json(out / "semantic-cache.json", current)
    write_json(out / "state.json", {"status": "ready", "built_at": now(), "files": {n: d["hash"] for n, d in docs.items()},
                                  "contract": contract, "nodes": len(G), "edges": G.number_of_edges(), "token_usage": None})
    (out / ".graphify_python").write_text(str(root / ".venv/bin/python"), encoding="utf-8")
    (out / ".needs_update").unlink(missing_ok=True)
    return {"status": "ready", "nodes": len(G), "edges": G.number_of_edges()}


def status(root):
    docs, _ = lint(root)
    state = read_json(root / "graphify-out/state.json")
    fresh = state.get("files") == {n: d["hash"] for n, d in docs.items()} and state.get("contract") == digest(root / SPEC)
    fresh = fresh and all((root / "graphify-out" / n).is_file() for n in ("graph.json", "graph.html", "GRAPH_REPORT.md"))
    fresh = fresh and not (root / "graphify-out/.needs_update").exists()
    return {**state, "status": "ready" if fresh else "갱신 필요"}


def search(root, query):
    result = []
    q = normalize(query)
    for name, d in pages(root).items():
        m = d["meta"]
        words = [m["id"], m["title"], *m["aliases"]]
        score = 2 if any(q == normalize(w) for w in words) else int(q in normalize(d["text"]))
        if score:
            result.append({"path": name, "title": m["title"], "status": m["status"], "score": score})
    return sorted(result, key=lambda r: (-r["score"], r["path"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    for cmd in ("lint", "prepare", "build", "status"):
        sub.add_parser(cmd)
    p = sub.add_parser("search"); p.add_argument("query")
    p = sub.add_parser("accept"); p.add_argument("extraction", type=Path); p.add_argument("--request", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "lint":
            result = {"valid_documents": len(lint(root)[0])}
        elif args.command == "accept":
            result = accept(root, args.extraction, args.request or root / "graphify-out/extraction-request.json")
        elif args.command == "search":
            result = search(root, args.query)
        else:
            result = globals()[args.command](root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        if args.command != "search":
            mark_stale(root, str(e))
        print(f"실패: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
