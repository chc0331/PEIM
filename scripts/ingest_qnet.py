#!/usr/bin/env python3
"""Capture public Q-Net exam PDFs and create source-linked, session-level wiki drafts.

No LLM/API calls: semantic concept extraction is performed by the Codex session
after wiki.py prepare. Existing raw files and edited wiki pages are never replaced.
"""
import argparse
from datetime import datetime
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://www.q-net.or.kr/cst006.do"


def url(**params):
    return BASE + "?" + urlencode({"gSite": "Q", "gId": "", **params})


def fetch(address):
    with urlopen(Request(address, headers={"User-Agent": "Personal-study-wiki/1.0"}), timeout=45) as response:
        return response.read()


def preserve(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"기존 보관물과 다름; 새 snapshot 경로를 사용하세요: {path}")
    else:
        with path.open("xb") as stream:
            stream.write(data)


def listing(first, last, snapshot):
    found = {}
    for page in range(1, 101):
        address = url(id="cst00601s01", page=page, schText="정보관리", schType="T", brdId="Q006", code=1203)
        cache = snapshot / f"listing-{page}.html"
        data = cache.read_bytes() if cache.exists() else fetch(address)
        preserve(cache, data)
        text = data.decode("utf-8")
        rounds = []
        for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", text, re.S):
            title = re.search(r'title="(제\s*(\d+)회\s*정보관리기술사[^"]*)"', row)
            article = re.search(r"goNext\('([0-9]+)'", row)
            date = re.search(r'class="date">(\d{4}\.\d{2}\.\d{2})', row)
            if not (title and article and date):
                continue
            exam = int(title[2]); rounds.append(exam)
            if first <= exam <= last:
                if exam in found:
                    raise ValueError(f"중복 게시물: {exam}회")
                found[exam] = {"round": exam, "title": html.unescape(title[1]), "article_id": article[1],
                               "posted_date": date[1].replace(".", "-"), "listing_url": address}
        if not rounds or min(rounds) <= first:
            break
    missing = sorted(set(range(first, last + 1)) - set(found))
    if missing:
        raise ValueError(f"목록에서 찾지 못한 회차: {missing}")
    return found


def parse_pages(pages, exam):
    """Keep question wording and PDF page locators; reject incomplete segmentation."""
    sessions = []
    current = None
    for page_no, text in enumerate(pages, 1):
        if not re.search(rf"제\s*{exam}\s*회", text) or "정보관리기술사" not in re.sub(r"\s", "", text):
            raise ValueError(f"{exam}회 PDF p.{page_no}: 종목/회차 확인 실패")
        body = re.split(r"확인하시오\s*[◀<]", text, maxsplit=1)
        if len(body) != 2:
            body = re.split(r"(?m)^\s*야\s+[^\n]*명\s*\n", text, maxsplit=1)
        if len(body) != 2:
            raise ValueError(f"{exam}회 PDF p.{page_no}: 머리말 형식 확인 필요")
        lines = body[1].splitlines()
        count = re.search(r"총\s*(\d+)\s*문제", body[1])
        selection = re.search(r"다음\s*문제\s*중\s*(10|4)\s*문제", body[1])
        if count or selection:
            if current and len(current["questions"]) != current["expected"]:
                raise ValueError(f"{exam}회 {current['session']}교시: 문항 수 불일치")
            expected = int(count[1]) if count else {10: 13, 4: 6}[int(selection[1])]
            current = {"session": len(sessions) + 1, "expected": expected, "questions": []}
            sessions.append(current)
        if current is None:
            raise ValueError(f"{exam}회 p.{page_no}: 교시 시작 확인 필요")
        for line in lines:
            if "채점기준" in line or re.fullmatch(r"\s*\d+\s*[-－–—]\s*\d+\s*", line):
                continue
            match = re.match(r"^[ \t]{0,2}(\d{1,2})\.\s*(.*)", line)
            if match and int(match[1]) != len(current["questions"]) + 1:
                match = None  # Numbered labels within figures/subquestions remain body text.
            if match:
                number = int(match[1])
                if number != len(current["questions"]) + 1:
                    raise ValueError(f"{exam}회 {current['session']}교시 p.{page_no}: 문항 순서 확인 필요 ({number})")
                current["questions"].append({"number": number, "pages": [page_no], "lines": [match[2]]})
            elif current["questions"] and line.strip():
                question = current["questions"][-1]
                if page_no not in question["pages"]:
                    question["pages"].append(page_no)
                question["lines"].append(line.rstrip())
    if [s["expected"] for s in sessions] != [13, 6, 6, 6]:
        raise ValueError(f"{exam}회: 예상한 4개 교시(13/6/6/6)와 다름; 수동 확인 필요")
    for session in sessions:
        if len(session["questions"]) != session["expected"]:
            raise ValueError(f"{exam}회 {session['session']}교시: 문항 누락")
        for question in session["questions"]:
            question["text"] = "\n".join(question.pop("lines")).strip()
    return sessions


def capture(entry, snapshot, captured_at, pdftotext):
    exam = entry["round"]
    folder = snapshot / str(exam)
    record_path = folder / "record.json"
    if record_path.exists():
        record = json.loads(record_path.read_text(encoding="utf-8"))
        pdf = ROOT / record["pdf_path"]
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError(f"보관 PDF 해시 불일치: {pdf}")
        return record
    detail_url = url(id="cst00602", artlSeq=entry["article_id"], brdId="Q006", code=1203, cst="Y")
    detail_path = folder / "article.html"
    data = detail_path.read_bytes() if detail_path.exists() else fetch(detail_url)
    preserve(detail_path, data)
    attachments = re.findall(r"fileDown\('([^']*)',\s*'([^']*)',\s*'(\d+)',\s*'(\d+)'\)", html.unescape(data.decode("utf-8")))
    matches = [a for a in attachments if a[1].lower().endswith(".pdf") and "정보관리" in a[1]]
    if len(matches) != 1:
        raise ValueError(f"{exam}회: 정보관리 PDF 첨부가 정확히 하나가 아님: {attachments}")
    filepath, filename, file_seq, article_id = matches[0]
    download_url = url(id="cst00602s01", fileCode="R001", filePath=filepath, fileName=filename,
                       fileSeq=file_seq, artlSeq=article_id, href=0)
    pdf_path = folder / f"qnet-{exam}.pdf"
    pdf = pdf_path.read_bytes() if pdf_path.exists() else fetch(download_url)
    if not pdf.startswith(b"%PDF-"):
        raise ValueError(f"{exam}회: PDF 응답 아님")
    preserve(pdf_path, pdf)
    extracted = subprocess.run([pdftotext, "-layout", str(pdf_path), "-"], capture_output=True, check=True).stdout
    text = extracted.decode("utf-8")
    pages = text.split("\f")
    if not pages[-1].strip():
        pages.pop()
    sessions = parse_pages(pages, exam)
    preserve(folder / "extracted.txt", extracted)
    record = {**entry, "captured_at": captured_at, "detail_url": detail_url, "download_url": download_url,
              "original_filename": filename, "pdf_path": pdf_path.relative_to(ROOT).as_posix(),
              "sha256": hashlib.sha256(pdf).hexdigest(), "bytes": len(pdf), "pdf_pages": len(pages),
              "collection_kind": "공식 PDF 원본과 pdftotext -layout 기계 추출; 해설 아님",
              "sessions": sessions}
    preserve(record_path, (json.dumps(record, ensure_ascii=False, indent=2) + "\n").encode())
    return record


def create_wiki(record, date):
    exam = record["round"]
    source_id = f"source-qnet-{exam}"
    source_file = ROOT / f"wiki/sources/qnet-{exam}.md"
    common = {"aliases": [], "domains": ["정보관리기술사 기출"], "status": "출처 확인", "updated": date}
    meta = {"id": source_id, "title": f"Q-Net 제{exam}회 정보관리기술사 공식 문제지", "type": "source", **common,
            "sources": [{"path": record["pdf_path"], "url": record["detail_url"]}],
            "source_url": record["detail_url"], "author": "한국산업인력공단 Q-Net",
            "published": record["posted_date"], "captured_at": record["captured_at"]}
    body = f"# {meta['title']}\n\n## 확인 범위\n\n공식 PDF {record['pdf_pages']}페이지, 1~4교시 총 31문항을 수집했습니다. 게시물 날짜는 시험일을 뜻하지 않습니다.\n\n"
    body += "원본은 보존하고 줄바꿈만 정리한 기계 추출을 문항으로 나눴습니다. 표·그림·기호의 정확한 배치는 원본 PDF로 대조합니다. 출처 확인은 문제의 존재·문구에 대한 확인이며 정답·해설 검증이나 학습 성취가 아닙니다.\n\n"
    body += f"- [공식 게시물]({record['detail_url']})\n- [원본 PDF](../../{record['pdf_path']})\n- [수집 기록](../../{record['pdf_path'].rsplit('/', 1)[0]}/record.json)\n- SHA-256: `{record['sha256']}`\n\n## 교시별 문항\n\n"
    for session in record["sessions"]:
        n = session["session"]
        body += f"- [{n}교시 {session['expected']}문항](../questions/qnet-{exam}-p{n}.md)\n"
    write_draft(source_file, meta, body)
    for session in record["sessions"]:
        n = session["session"]
        title = f"제{exam}회 정보관리기술사 {n}교시 공식 기출"
        questions = [{"number": q["number"], "pdf_pages": q["pages"]} for q in session["questions"]]
        meta = {"id": f"question-qnet-{exam}-p{n}", "title": title, "type": "question", **common,
                "question_kind": "공식 기출", "exam_round": exam, "exam_session": n, "questions": questions,
                "source_url": record["detail_url"], "author": "한국산업인력공단 Q-Net", "captured_at": record["captured_at"],
                "sources": [{"id": source_id, "locator": f"{n}교시; 각 문항의 PDF 페이지 참조"}]}
        body = f"# {title}\n\n[공식 출처](../sources/qnet-{exam}.md) · [기출 탐색](../comparisons/qnet-exam-map.md)\n\n"
        body += "문항 본문은 공식 PDF의 기계 추출입니다. 교시는 PDF 수록 순서와 문항 선택 안내로 구분했습니다. PDF에 인쇄된 일부 교시의 쪽표기는 반복될 수 있으므로 아래 페이지는 파일 기준입니다. 그림·표·기호는 원본과 대조하세요. 공식 해설은 수집하지 않았습니다.\n\n"
        for q in session["questions"]:
            locator = ", ".join(str(p) for p in q["pages"])
            body += f"<a id=\"q{q['number']}\"></a>\n\n## {q['number']}번\n\n"
            body += f"[공식 PDF p. {locator}](../../{record['pdf_path']}#page={q['pages'][0]})\n\n"
            body += q["text"] + "\n\n"
        write_draft(ROOT / f"wiki/questions/qnet-{exam}-p{n}.md", meta, body)


def write_draft(path, meta, body):
    if path.exists():
        return  # Later Codex annotations and corrections belong to the wiki owner.
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        stream.write("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + "---\n\n" + body)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first", type=int, default=126)
    parser.add_argument("--last", type=int, default=140)
    parser.add_argument("--snapshot", type=Path, required=True, help="New append-only folder under raw/exams/qnet")
    parser.add_argument("--pdftotext", default=shutil.which("pdftotext"))
    args = parser.parse_args()
    if not args.pdftotext:
        parser.error("pdftotext (Poppler) 설치 또는 --pdftotext 경로가 필요합니다")
    snapshot = args.snapshot.resolve()
    snapshot.relative_to(ROOT / "raw/exams/qnet")
    if not 1 <= args.first <= args.last:
        parser.error("잘못된 회차 범위")
    captured_at = datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")
    entries = listing(args.first, args.last, snapshot)
    for exam in sorted(entries, reverse=True):
        record = capture(entries[exam], snapshot, captured_at, args.pdftotext)
        create_wiki(record, record["captured_at"][:10])
        print(json.dumps({"round": exam, "pdf_pages": record["pdf_pages"], "questions": sum(len(s['questions']) for s in record['sessions'])}, ensure_ascii=False), flush=True)
    print("수집 완료. 개념/탐색 자료를 보완한 뒤 wiki.py prepare → 세션 의미 추출 → accept → build를 실행하세요.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"수집 중단: {error}", file=sys.stderr)
        raise SystemExit(1)
