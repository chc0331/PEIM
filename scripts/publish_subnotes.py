#!/usr/bin/env python3
"""Publish session-researched findings as canonical wiki notes and a print catalog.

This does not research or verify technical claims. Source/requirement review states
are retained; merely finding a topic for a question is not proof of completeness.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from zoneinfo import ZoneInfo
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ["데이터베이스·데이터 관리", "통계·분석·AI", "소프트웨어·아키텍처", "운영체제·컴퓨터구조", "네트워크·통신", "클라우드·운영·복구", "보안·개인정보·AI 거버넌스", "전략·IT 거버넌스", "프로젝트·감리·사업대가", "산업 적용·신기술"]


def print_domain(value):
    text = value.casefold()
    if any(w in text for w in ["산업적용", "스마트제조", "분산신뢰", "디지털자산", "디지털융합", "디지털서비스", "디지털윤리", "서비스플랫폼", "교육융합"]):
        return DOMAINS[9]
    rules = [(6, ["보안", "개인정보", "정보보호", "ai 거버넌스", "ai거버넌스", "법·윤리", "암호", "포렌식"]),
             (4, ["네트워크", "통신"]), (3, ["운영체제", "컴퓨터구조", "컴퓨터 구조", "하드웨어", "양자컴퓨팅"]),
             (5, ["클라우드", "인프라", "재해", "가상화", "운영·복구"]),
             (8, ["프로젝트", "감리", "대가", "비용", "사업관리"]),
             (0, ["데이터베이스", "데이터 관리", "데이터관리", "데이터거버넌스", "데이터 거버넌스", "데이터 플랫폼", "빅데이터"]),
             (7, ["전략", "경영", "it 거버넌스", "itsm", "it서비스관리", "디지털정부", "it 정책", "it정책"]),
             (1, ["통계", "ai", "분석", "머신러닝", "딥러닝", "인공지능", "llm"]),
             (2, ["소프트웨어", "uml", "아키텍처", "개발", "테스트", "자료구조", "알고리즘"])]
    return next((DOMAINS[i] for i, words in rules if any(w in text for w in words)), DOMAINS[9])


def norm(text):
    return re.sub(r"[\s_-]+", "", unicodedata.normalize("NFKC", str(text))).casefold()


def load_findings(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(text)
    block = re.search(r"```json\s*\n(.*?)\n```", text, re.S)
    if not block:
        raise ValueError(f"연구 JSON 블록 없음: {path}")
    return json.loads(block[1])


def wiki_read(path):
    _, meta, body = path.read_text(encoding="utf-8").split("---", 2)
    return yaml.safe_load(meta), body


def wiki_write(path, meta, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + "---\n\n" + body.strip() + "\n", encoding="utf-8")


def topic_body(topic, sources, original=""):
    lines = [f"# {topic['title']}", "", "## 서브노트", "", "### 한눈에 이해", "", topic["easy"], "", "### 정의와 핵심 원리", "", topic["definition"], ""]
    lines += [f"- {p}" for p in topic["principles"]]
    table = topic.get("comparison") or {}
    if table.get("rows"):
        cell = lambda value: str(value).replace("|", "&#124;").replace("\n", " ")
        lines += ["", "### 구조·비교·판단", "", "| " + " | ".join(cell(v) for v in table["headers"]) + " |", "| " + " | ".join("---" for _ in table["headers"]) + " |"]
        for row in table["rows"]:
            lines.append("| " + " | ".join(cell(v) for v in row) + " |")
    lines += ["", "<!-- subnote-page:apply -->", "", "### 적용 예제", ""]
    ex = topic["example"]
    lines += [f"**{ex['title']}**", "", "강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.", "", f"**조건:** {ex['input']}", ""]
    lines += [f"{i}. {step}" for i, step in enumerate(ex["steps"], 1)]
    lines += ["", f"**결과·해석:** {ex['result']}"]
    if ex.get("caution"):
        lines += ["", f"**전제·주의:** {ex['caution']}"]
    lines += ["", "### 답안 골격과 혼동 방지", "", " → ".join(topic["answer_outline"]), ""]
    lines += [f"- {p}" for p in topic.get("pitfalls", [])]
    lines += ["", "### 내용을 가리고 회상", ""] + [f"{i}. {q}" for i, q in enumerate(topic["recall"], 1)]
    lines += ["", "### 적용 기준과 근거", "", topic.get("version_note") or "자료별 적용 범위와 확인일을 확인하세요.", "", f"**내용 검토 상태: {topic['validation']}**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.", ""]
    for sid in topic["source_ids"]:
        source = sources[sid]
        lines += [f"- [{source['title']}]({source['url']}) — {source['author']}; {source.get('published', '미상')}; 확인 {source['checked_at']}. 확인 범위: {source.get('notes', '')}"]
    lines += ["", "## 연관 기출", ""]
    for req in topic["requirements"]:
        exam, session, number = req["question"].split("-")
        lines += [f"- [제{exam}회 {session}교시 {number}번](../questions/qnet-{exam}-p{session}.md#q{number}) — {'; '.join(req['items'])}. 대응: {req['section']}; {req['status']}."]
    lines += ["", "## 브레인스토밍", "", "예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다."]
    if original:
        lines += ["", "## 이전 문서 기록", "", "아래는 인쇄용 보완 전 문서입니다. 적용 기준과 근거는 위의 최신 서브노트에서 확인하세요.", "", original.strip()]
    # Keep nested matrix brackets distinct from the wiki-link syntax the repo rejects.
    return "\n".join(lines).replace("[[", "[ [").replace("]]", "] ]")


def publish(paths, root=ROOT):
    stamp = datetime.now(ZoneInfo("Asia/Seoul")).date().isoformat()
    questions = {}
    for record_path in sorted((root / "raw/exams/qnet/2026-11-01").glob("*/record.json")):
        record = json.loads(record_path.read_text())
        for session in record["sessions"]:
            for question in session["questions"]:
                ident = f"{record['round']}-{session['session']}-{question['number']}"
                questions[ident] = {"id": ident, "title": question["text"].splitlines()[0], "topics": [], "requirements": []}
    inputs = [(p, load_findings(p)) for p in paths]
    source_titles = {}
    source_details = {}
    for research, findings in inputs:
        for source in findings["sources"]:
            url = re.sub(r"(?i)(?:;|%3b)jsessionid(?:=|%3d)[^?]*", "", source["url"])
            source_titles[url] = "자료: " + source["title"]
            detail = source_details.setdefault(url, {"records": [], "notes": []})
            detail["source"] = {**source, "url": url}
            record = research.resolve().relative_to(root.resolve()).as_posix()
            if record not in detail["records"]:
                detail["records"].append(record)
            if source.get("notes") and source["notes"] not in detail["notes"]:
                detail["notes"].append(source["notes"])
    for detail in source_details.values():
        detail["source"]["notes"] = " / ".join(detail["notes"])
    title_urls = {}
    for url, title in source_titles.items():
        title_urls.setdefault(norm(title), []).append(url)
    for urls in title_urls.values():
        if len(urls) > 1:
            for url in urls:
                host = urlsplit(url).hostname
                suffix = host if sum(urlsplit(u).hostname == host for u in urls) == 1 else host + " " + hashlib.sha256(url.encode()).hexdigest()[:6]
                source_titles[url] += " (" + suffix + ")"
    declared_ids = set()
    for path, findings in inputs:
        source_ids = {s["id"] for s in findings["sources"]}
        for topic in findings["topics"]:
            if topic["id"] in declared_ids:
                raise ValueError(f"연구 토픽 ID 중복: {topic['id']}")
            declared_ids.add(topic["id"])
            if len(topic.get("recall", [])) != 3 or not topic.get("source_ids") or not set(topic["source_ids"]).issubset(source_ids):
                raise ValueError(f"회상 질문/출처 참조 오류: {topic['id']}")
            table = topic.get("comparison") or {}
            if any(len(row) != len(table.get("headers", [])) for row in table.get("rows", [])):
                raise ValueError(f"표 행·열 수 오류: {topic['id']}")
            for req in topic["requirements"]:
                if req["question"] not in questions or not req.get("items"):
                    raise ValueError(f"기출 요구사항 참조 오류: {topic['id']}/{req}")
    catalog_path = root / "docs/subnotes/catalog.json"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    baseline = root / "tmp/subnotes/original-wiki"
    baseline.mkdir(parents=True, exist_ok=True)
    existing = {}
    for path in (root / "wiki/concepts").glob("*.md"):
        meta, body = wiki_read(path)
        for key in [meta["id"], meta["title"], *meta.get("aliases", [])]:
            existing[norm(key)] = (path, meta)
    for _, findings in inputs:
        for topic in findings["topics"]:
            for key in [topic["id"], topic["title"], *topic.get("aliases", [])]:
                match = existing.get(norm(key))
                if match and any(s.get("path", "").startswith("raw/corrections/") for s in match[1]["sources"]):
                    raise ValueError(f"독립 교정본 재반영 거부: {match[0]}. 이 도구는 초기 반영용입니다. 이후 교정은 기준 위키에서 수행하고 PDF를 재생성하세요.")
    all_sources, topics, seen = {}, [], set()
    for research, findings in inputs:
        research_rel = research.resolve().relative_to(root.resolve()).as_posix()
        source_map = {}
        for source in findings["sources"]:
            local_id = source["id"]
            url = re.sub(r"(?i)(?:;|%3b)jsessionid(?:=|%3d)[^?]*", "", source["url"])
            detail = source_details[url]
            source = detail["source"]
            key = "source-subnote-" + hashlib.sha256(source["url"].encode()).hexdigest()[:12]
            source_map[local_id] = key
            all_sources[key] = {**source, "id": key, "record": detail["records"][0], "records": detail["records"]}
            source_path = root / f"wiki/sources/{key.removeprefix('source-')}.md"
            meta = {"id": key, "title": source_titles[source["url"]], "aliases": [], "type": "source", "domains": ["서브노트 근거"],
                    "sources": [{"path": record, "url": source["url"]} for record in detail["records"]], "status": "출처 확인", "updated": stamp,
                    "source_url": source["url"], "author": source["author"], "published": str(source.get("published", "미상")), "captured_at": source["checked_at"]}
            source_body = f"# {source['title']}\n\n## 확인 범위와 수집 형태\n\n{source.get('notes', '')}\n\n강사 생성 조사 요약과 URL 참조를 보관했습니다. 외부 원문 전체 보관이 아닙니다. 기술 주장은 연결된 서브노트의 적용 범위·검토 상태를 함께 확인합니다.\n\n- [기관 원문]({source['url']})\n"
            source_body += "".join(f"- [세션 조사 기록](../../{record})\n" for record in detail["records"])
            if source_path.exists():
                old_meta, old_body = wiki_read(source_path)
                for old_ref in old_meta["sources"]:
                    if old_ref not in meta["sources"]:
                        meta["sources"].append(old_ref)
                if old_body.split("\n## 이전 확인 기록", 1)[0].strip() != source_body.strip():
                    source_body += "\n## 이전 확인 기록\n\n" + old_body.strip() + "\n"
                else:
                    source_body = old_body
            wiki_write(source_path, meta, source_body)
        for original_topic in findings["topics"]:
            topic = dict(original_topic)
            for key in ("easy", "definition", "principles", "example", "answer_outline", "recall", "requirements"):
                if not topic.get(key):
                    raise ValueError(f"빈 토픽 내용: {topic['id']}/{key}")
            topic["source_ids"] = [source_map[s] for s in topic["source_ids"]]
            matches = {v[0]: v for key in [topic["id"], topic["title"], *topic.get("aliases", [])] if (v := existing.get(norm(key)))}
            if len(matches) > 1:
                raise ValueError(f"토픽이 여러 기존 개념에 걸침: {topic['id']}")
            match = next(iter(matches.values()), None)
            if match:
                path, meta = match; meta = dict(meta)
                ident = meta["id"]
                old_title = meta["title"]
                meta["title"] = topic["title"]
                meta["aliases"] = list(dict.fromkeys(meta.get("aliases", []) + topic.get("aliases", []) + ([old_title] if norm(old_title) != norm(topic["title"]) else [])))
            else:
                ident = topic["id"]
                if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", ident):
                    raise ValueError(f"잘못된 토픽 ID: {ident}")
                path = root / f"wiki/concepts/{ident}.md"
                meta = {"id": ident, "title": topic["title"], "aliases": topic.get("aliases", []), "type": "concept", "domains": [topic["domain"]], "sources": []}
            if ident in seen:
                raise ValueError(f"중복 토픽 ID: {ident}; 주제의 범위를 검토해 합치거나 구분하세요")
            seen.add(ident)
            backup = baseline / path.name
            prior = ""
            if not backup.exists():
                if path.exists():
                    backup.write_bytes(path.read_bytes())
                else:
                    backup.write_text("---\n{}\n---\n", encoding="utf-8")
            if backup.exists():
                _, prior = wiki_read(backup)
                prior = re.sub(r"(?m)^#{1,5} ", lambda m: "#" + m[0], prior).strip()
            for sid in topic["source_ids"]:
                if {"id": sid} not in meta["sources"]:
                    meta["sources"].append({"id": sid})
            meta.update(updated=stamp, format="a4-duplex-subnote", review_status=topic["validation"],
                        status="출처 확인" if topic["validation"] == "출처 확인" else "미검증")
            if topic.get("related_terms"):
                meta["related_terms"] = list(dict.fromkeys(meta.get("related_terms", []) + topic["related_terms"]))
            wiki_write(path, meta, topic_body(topic, all_sources, prior))
            topics.append({"id": ident, "title": meta["title"], "domain": print_domain(topic["domain"]), "path": path.relative_to(root).as_posix(),
                           "validation": topic["validation"], "sources": topic["source_ids"], "requirements": topic["requirements"]})
    topics.sort(key=lambda t: DOMAINS.index(t["domain"]))
    for topic in topics:
        for req in topic["requirements"]:
            if req["question"] not in questions:
                raise ValueError(f"없는 기출 문항: {req['question']}")
            item = questions[req["question"]]
            if topic["id"] not in item["topics"]:
                item["topics"].append(topic["id"])
            item["requirements"].append({"topic": topic["id"], **req})
    for item in questions.values():
        statuses = {r["status"] for r in item["requirements"]}
        item["review_status"] = "미연결" if not item["topics"] else "확인 필요" if "확인 필요" in statuses else "부분 확인" if "부분 충족" in statuses else "수록 연결"
    catalog = {"built_at": stamp, "basis": "Q-Net 제126~140회 465문항",
               "topics": topics, "sources": all_sources, "questions": list(questions.values())}
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"topics": len(topics), "sources": len(all_sources), "questions_mapped": sum(bool(q['topics']) for q in questions.values()),
                      "unmapped_count": sum(not q['topics'] for q in questions.values()),
                      "unmapped_sample": [q['id'] for q in questions.values() if not q['topics']][:12]}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("research", nargs="+", type=Path)
    args = parser.parse_args()
    publish(args.research)
