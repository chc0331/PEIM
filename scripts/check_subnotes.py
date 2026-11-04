#!/usr/bin/env python3
"""Check print artifacts and coverage structure; does not certify subject knowledge."""
import argparse
import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def check(catalog_path, output, allow_unmapped=False):
    catalog = json.loads(catalog_path.read_text())
    manifest = json.loads((output / "manifest.json").read_text())
    topics = {t["id"]: t for t in catalog["topics"]}
    errors, boxes = [], []
    question_ids = [q["id"] for q in catalog["questions"]]
    if len(question_ids) != 465 or len(set(question_ids)) != 465:
        errors.append("465개 기출 문항 ID의 유일성/개수 오류")
    unmapped = [q["id"] for q in catalog["questions"] if not q["topics"]]
    if unmapped and not allow_unmapped:
        errors.append(f"연결되지 않은 기출 {len(unmapped)}개")
    review_counts = {}
    embedded_fonts = set()
    for topic in topics.values():
        review_counts[topic["validation"]] = review_counts.get(topic["validation"], 0) + 1
        if not topic["sources"] or any(s not in catalog["sources"] for s in topic["sources"]):
            errors.append(f"토픽 출처 참조 오류: {topic['id']}")
    for ident, expected in manifest["topics"].items():
        path = output / "topics" / (ident + ".pdf")
        reader = PdfReader(path)
        if len(reader.pages) not in (2, 4) or len(reader.pages) != expected:
            errors.append(f"2/4쪽 또는 manifest 불일치: {ident}")
        for page_no, page in enumerate(reader.pages, 1):
            if abs(float(page.mediabox.width) - 595.2756) > 1 or abs(float(page.mediabox.height) - 841.8898) > 1:
                errors.append(f"A4 크기 오류: {ident}/{page_no}")
            resources = page.get("/Resources", {}).get_object()
            fonts = resources.get("/Font", {}).get_object()
            for font in fonts.values():
                font = font.get_object(); name = str(font.get("/BaseFont", ""))
                if "Nanum" in name or "NotoSans" in name:
                    descriptor = font.get("/FontDescriptor")
                    if not descriptor or not descriptor.get_object().get("/FontFile2"):
                        errors.append(f"한글/수학 글꼴 미포함: {ident}/{name}")
                    embedded_fonts.add(name.split("+")[-1])
        with pdfplumber.open(path) as pdf:
            for page_no, page in enumerate(pdf.pages, 1):
                bad = [c for c in page.chars if c["x0"] < -0.5 or c["x1"] > page.width + 0.5 or c["top"] < -0.5 or c["bottom"] > page.height + 0.5]
                if bad:
                    errors.append(f"페이지 밖 텍스트: {ident}/{page_no}")
                content = [c for c in page.chars if 55 < c["top"] < page.height - 48]
                boxes.append({"topic": ident, "page": page_no, "characters": len(content),
                              "bottom": round(max((c["bottom"] for c in content), default=0), 1)})
    book_pages = None
    if manifest.get("book"):
        book = PdfReader(ROOT / manifest["book"])
        book_pages = len(book.pages)
        if book_pages % 2:
            errors.append("통합본 양면 페이지 짝수 조건 오류")
        for ident, position in manifest["topic_pages"].items():
            if position % 2 != 1:
                errors.append(f"토픽 시작이 홀수 쪽이 아님: {ident}")
            dest = book.named_destinations.get(ident)
            if dest is None or book.get_destination_page_number(dest) + 1 != position:
                errors.append(f"목차 목적지 오류: {ident}")
        linked = set()
        for page in book.pages:
            for ref in page.get("/Annots", []):
                action = ref.get_object().get("/A", {})
                if str(action.get("/URI", "")).startswith("topic:"):
                    errors.append("목차 임시 링크가 남음")
                if action.get("/S") == "/GoTo":
                    target = str(action.get("/D"))
                    linked.add(target)
                    if target not in book.named_destinations:
                        errors.append(f"없는 목차 링크: {target}")
        if not set(manifest["topics"]).issubset(linked):
            errors.append("일부 토픽의 클릭 목차 링크 누락")
    report = {"topics": len(topics), "pdfs_checked": len(manifest["topics"]), "book_pages": book_pages,
              "questions": len(question_ids), "mapped": len(question_ids) - len(unmapped), "unmapped": unmapped,
              "review_states": review_counts, "errors": errors, "layout_pages": boxes,
              "embedded_fonts": sorted(embedded_fonts),
              "limits": "자동 검사는 문항 ID·연결·PDF 크기·페이지 수·텍스트 경계·링크 구조만 확인합니다. 기술 정확성·소문항의 의미 충족·실제 독자의 이해는 별도 검수입니다."}
    (output / "checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in ("layout_pages", "unmapped", "limits")}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "docs/subnotes/catalog.json")
    parser.add_argument("--output", type=Path, default=ROOT / "output/pdf/subnotes")
    parser.add_argument("--allow-unmapped", action="store_true")
    args = parser.parse_args()
    raise SystemExit(check(args.catalog, args.output, args.allow_unmapped))
