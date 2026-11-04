#!/usr/bin/env python3
"""Render canonical wiki subnotes as A4 duplex topic PDFs and a searchable book.

Run with the bundled document Python (ReportLab, pypdf).
"""
import argparse
from io import BytesIO
from functools import partial
import json
from pathlib import Path
import re
import unicodedata
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject, TextStringObject
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, Flowable, Frame, PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
W, H = A4
FONT = ROOT / "assets/fonts/nanum-gothic"
pdfmetrics.registerFont(TTFont("NG", str(FONT / "NanumGothic-Regular.ttf")))
pdfmetrics.registerFont(TTFont("NG-Bold", str(FONT / "NanumGothic-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Math", str(ROOT / "assets/fonts/noto-sans-math/NotoSansMath-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Latin", str(ROOT / "assets/fonts/noto-sans/NotoSans-Regular.ttf")))
pdfmetrics.registerFontFamily("NG", normal="NG", bold="NG-Bold", italic="NG", boldItalic="NG-Bold")
STYLES = {
    "body": ParagraphStyle("body", fontName="NG", fontSize=11, leading=15.4, spaceAfter=6, wordWrap="CJK", splitLongWords=True),
    "small": ParagraphStyle("small", fontName="NG", fontSize=9, leading=12.5, spaceAfter=4, wordWrap="CJK"),
    "h2": ParagraphStyle("h2", fontName="NG-Bold", fontSize=12, leading=17, spaceBefore=10, spaceAfter=6, keepWithNext=True, wordWrap="CJK"),
    "title": ParagraphStyle("title", fontName="NG-Bold", fontSize=20, leading=26, spaceBefore=2, spaceAfter=13, wordWrap="CJK"),
    "label": ParagraphStyle("label", fontName="NG-Bold", fontSize=9, leading=12, spaceAfter=6, wordWrap="CJK"),
    "cell": ParagraphStyle("cell", fontName="NG", fontSize=10, leading=14, wordWrap="CJK"),
    "thead": ParagraphStyle("thead", fontName="NG-Bold", fontSize=10, leading=14, wordWrap="CJK"),
}


def inline(text):
    text = escape(str(text))
    text = text.replace("&amp;#124;", "&#124;")
    text = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", r'<a href="\2" color="#111111"><u>\1</u></a>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    result = []
    regular = pdfmetrics.getFont("NG").face.charToGlyph
    math = pdfmetrics.getFont("Math").face.charToGlyph
    in_tag = False
    for char in text:
        if char == "<":
            in_tag = True
        if in_tag:
            result.append(char)
            if char == ">":
                in_tag = False
            continue
        if char in "‐‑‒–—":
            char = "-"
        decomposition = unicodedata.decomposition(char)
        if decomposition.startswith("<circle> "):
            result.append("(" + unicodedata.normalize("NFKC", char) + ")")
            continue
        if decomposition.startswith(("<super> ", "<sub> ")):
            kind, *points = decomposition.split()
            base = "".join(chr(int(p, 16)) for p in points)
            tag = "super" if kind == "<super>" else "sub"
            result.append(f"<{tag}>{escape(base)}</{tag}>")
            continue
        if ord(char) >= 32 and ord(char) not in regular:
            if 32 <= ord(char) <= 255:
                result.append(f'<font name="Latin">{char}</font>')
                continue
            if ord(char) not in math:
                raise ValueError(f"인쇄 글꼴에 없는 문자: {char!r} U+{ord(char):04X}")
            result.append(f'<font name="Math">{char}</font>')
        else:
            result.append(char)
    return "".join(result)


class TopicDiagram(Flowable):
    """Reviewed teaching diagrams, drawn as vectors at print resolution."""
    def __init__(self, ident):
        super().__init__(); self.ident = ident; self.width = W - 38 * mm
        self.height = 340 if ident == "uml-dice-model" else 270 if ident == "uml-sequence-library" else 82

    def message(self, x1, x2, y, text, dashed=False):
        c = self.canv; c.setDash(3, 2) if dashed else c.setDash()
        c.line(x1, y, x2, y); c.setDash()
        direction = 1 if x2 > x1 else -1
        c.line(x2, y, x2 - direction * 5, y + 3); c.line(x2, y, x2 - direction * 5, y - 3)
        c.setFont("NG", 8.5); c.drawCentredString((x1 + x2) / 2, y + 4, text)

    def lifelines(self, labels, top, bottom):
        c = self.canv; gap = self.width / len(labels); points = []
        for i, label in enumerate(labels):
            x = gap * (i + .5); points.append(x)
            c.rect(x - gap * .46, top, gap * .92, 21); c.setFont("NG", 8.5); c.drawCentredString(x, top + 7, label)
            c.setDash(3, 3); c.line(x, top, x, bottom); c.setDash()
        return points

    def uml_dice(self):
        c, w = self.canv, self.width
        c.setFont("NG-Bold", 10); c.drawString(0, 325, "클래스 · 객체 · 호출 순서를 구분하기")
        # Association, not composition: lifetime ownership is not a given requirement.
        c.setFont("NG", 8.5); c.drawString(325, 325, "값 제약: 1 ≤ faceValue ≤ 6")
        for x, bw, title, attr, methods in [(0, 75, "Player", "", []), (125, 140, "DiceGame", "", ["play(): Result"]), (325, 160, "Die", "faceValue: Integer", ["roll()", "getFaceValue(): Integer"])]:
            c.rect(x, 240, bw, 72); c.setFont("NG-Bold", 9); c.drawCentredString(x + bw / 2, 298, title)
            c.line(x, 290, x + bw, 290); c.setFont("NG", 8.5); c.drawString(x + 5, 277, attr)
            c.line(x, 268, x + bw, 268)
            for i, method in enumerate(methods): c.drawString(x + 5, 255 - 11 * i, method)
        c.line(75, 280, 125, 280); c.line(265, 280, 325, 280)
        c.setFont("NG", 9); c.drawString(312, 284, "2")
        c.setFont("NG", 8.5); c.drawString(0, 232, "객체 예: 인스턴스 이름과 타입에는 밑줄, 구체적인 값은 속성 칸에 표시")
        for x, label, slot in [(0, "game:DiceGame", "dice={die1, die2}"), (200, "die1:Die", "faceValue=3"), (360, "die2:Die", "faceValue=5")]:
            c.rect(x, 190, 120, 36); c.drawCentredString(x + 60, 214, label)
            length = pdfmetrics.stringWidth(label, "NG", 8.5); c.line(x + 60 - length / 2, 212, x + 60 + length / 2, 212)
            c.line(x, 208, x + 120, 208); c.drawCentredString(x + 60, 197, slot)
        c.line(120, 202, 200, 202)
        c.line(145, 202, 145, 183); c.line(145, 183, 345, 183)
        c.line(345, 183, 345, 202); c.line(345, 202, 360, 202)
        c.setFont("NG-Bold", 9); c.drawString(0, 172, "시퀀스 예 · 합이 8이면 승리")
        p, game, d1, d2 = self.lifelines(["player:Player", "game:DiceGame", "die1:Die", "die2:Die"], 139, 9)
        for x1, x2, y, label, dashed in [(p, game, 128, "play()", False), (game, d1, 113, "roll()", False), (game, d1, 98, "getFaceValue()", False), (d1, game, 83, "v1=3", True), (game, d2, 68, "roll()", False), (game, d2, 53, "getFaceValue()", False), (d2, game, 38, "v2=5", True), (game, p, 23, "sum=8 → win", True)]:
            self.message(x1, x2, y, label, dashed)
        c.setFont("NG", 8); c.drawString(0, 0, "일반 규칙: sum=8이면 win, 나머지는 lose. 반환·클래스 설계는 학습용 예시입니다.")

    def uml_library(self):
        c = self.canv; c.setFont("NG-Bold", 10); c.drawString(0, 255, "협력 그림의 연결을 생명선과 메시지 순서로 옮기기")
        borrower, rental, book, item, reservation = self.lifelines(["borrower", "rental", "book", "item", "reservation"], 219, 16)
        self.message(borrower, rental, 203, "1 대여 요청"); self.message(rental, book, 182, "2 재고 확인")
        c.rect(5, 91, self.width - 10, 76); c.setFont("NG-Bold", 8.5); c.drawString(10, 155, "alt")
        c.setFont("NG", 8.5); c.drawString(40, 155, "[재고=0]")
        self.message(book, rental, 140, "3 재고 없음 통보")
        c.setDash(2, 2); c.line(5, 130, self.width - 5, 130); c.setDash(); c.drawString(40, 117, "[재고>0]")
        self.message(book, item, 111, "3 대여 처리"); self.message(item, rental, 96, "3 대여 처리")
        self.message(rental, reservation, 66, "4 예약 요청"); self.message(reservation, book, 43, "5 예약 처리")
        c.setFont("NG", 8); c.drawString(0, 4, "주의: 원문의 4·5에는 가드가 없습니다. 재고 부족 분기로 묶을 경우 업무 가정을 명시하세요.")

    def draw(self):
        c, w = self.canv, self.width
        c.setStrokeColor(colors.black); c.setLineWidth(.6); c.setFont("NG", 9)
        if self.ident == "uml-dice-model":
            self.uml_dice()
        elif self.ident == "uml-sequence-library":
            self.uml_library()
        elif self.ident == "relational-normalization":
            c.rect(0, 24, w * .37, 40)
            c.drawCentredString(w * .185, 49, "학생 정보 × 수강 과목")
            c.drawCentredString(w * .185, 34, "학번·학과·지도교수·수강코드")
            x = w * .48
            for y, text in [(48, "학생(학번 PK, 학과, 지도교수)"), (7, "수강(학번 FK, 수강코드)")]:
                c.rect(x, y, w - x, 30); c.drawCentredString((x + w) / 2, y + 11, text)
                c.line(w * .37, 44, x, y + 15)
            c.drawCentredString(w * .43, 68, "분해")
        elif self.ident == "nist-ai-rmf":
            c.rect(0, 0, w, 77); c.setFont("NG-Bold", 10)
            c.drawCentredString(w / 2, 60, "GOVERN · 조직의 책임·정책·감독이 전 기능에 걸쳐 작동")
            for i, (title, desc) in enumerate([("MAP", "맥락·영향 파악"), ("MEASURE", "평가·불확실성 측정"), ("MANAGE", "위험 처리·감시")]):
                x = 9 + i * (w - 18) / 3; bw = (w - 18) / 3 - 10
                c.rect(x, 19, bw, 31); c.setFont("NG-Bold", 9); c.drawCentredString(x + bw / 2, 37, title)
                c.setFont("NG", 8.5); c.drawCentredString(x + bw / 2, 25, desc)
            c.drawCentredString(w / 2, 6, "맥락에 맞춰 반복하고 피드백 · 일방향 순서가 아님")
        else:
            c.setFont("NG-Bold", 10); c.drawString(0, 67, "192.168.0.0/22 · 전체 1,024주소")
            x = 0
            for ratio, title, size in [(.5, "개발 /23", "512주소"), (.25, "영업 /24", "256주소"), (.125, "인사 /25", "128주소"), (.125, "보안 /25", "128주소")]:
                bw = w * ratio; c.rect(x, 20, bw, 35); c.setFont("NG", 9)
                c.drawCentredString(x + bw / 2, 41, title); c.drawCentredString(x + bw / 2, 27, size); x += bw
            c.setFont("NG", 8.5); c.drawString(0, 5, "큰 블록부터 경계에 맞춰 배치 · 네트워크·브로드캐스트는 호스트에서 제외")


def para(text, style="body"):
    return Paragraph(inline(text), STYLES[style])


class PrintDoc(BaseDocTemplate):
    def __init__(self, path, *, ident="기출 핵심 서브노트", domain="", **kwargs):
        super().__init__(str(path), pagesize=A4, title=ident, author="정보관리기술사 학습 위키 / Codex 생성·검수", **kwargs)
        self.ident, self.domain = ident, domain
        width = W - 38 * mm
        templates = []
        for name, left in [("odd", 22 * mm), ("even", 16 * mm)]:
            templates.append(PageTemplate(name, frames=[Frame(left, 19 * mm, width, H - 39 * mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=self.decorate, autoNextPageTemplate="even" if name == "odd" else "odd"))
        self.addPageTemplates(templates)

    def build(self, flowables, **kwargs):
        super().build(flowables, canvasmaker=partial(canvas.Canvas, initialFontName="NG"), **kwargs)

    def decorate(self, c, doc):
        page = doc.page
        left = (22 if page % 2 else 16) * mm
        c.setStrokeColor(colors.HexColor("#777777")); c.setLineWidth(0.45)
        c.line(left, H - 15 * mm, left + W - 38 * mm, H - 15 * mm)
        c.setFont("NG", 8.5); c.setFillColor(colors.black)
        c.drawString(left, H - 12.4 * mm, self.domain[:45])
        c.drawString(left, 11 * mm, self.ident[:67])
        c.drawRightString(W - (16 if page % 2 else 22) * mm, 11 * mm, str(page))


def md_table(lines):
    rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines]
    rows = [row for row in rows if not all(re.fullmatch(r":?-+:?", c.replace(" ", "")) for c in row)]
    columns = len(rows[0])
    if any(len(row) != columns for row in rows):
        raise ValueError("표의 열 수 불일치")
    width = W - 38 * mm
    if columns == 2:
        weights = [0.27, 0.73]
    elif columns == 3:
        weights = [0.22, 0.40, 0.38]
    else:
        # Wide address tables need space in every column; CJK wraps instead of shrinking fonts.
        weights = [1 / columns] * columns
    cells = [[para(cell, "thead" if r == 0 else "cell") for cell in row] for r, row in enumerate(rows)]
    table = Table(cells, colWidths=[width * n for n in weights], repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 5),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 6),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LINEABOVE", (0, 0), (-1, 0), .65, colors.black),
                               ("LINEBELOW", (0, 0), (-1, 0), .6, colors.black), ("LINEBELOW", (0, 1), (-1, -1), .25, colors.HexColor("#aaaaaa"))]))
    return table


def markdown_flow(text):
    lines = text.splitlines(); result = []; i = 0; source_note = False
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1; continue
        if line == "<!-- subnote-page:apply -->":
            result.append(PageBreak()); i += 1; continue
        if line.startswith("<!--"):
            i += 1; continue
        if line.startswith("|"):
            table = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table.append(lines[i]); i += 1
            result += [Spacer(1, 3), md_table(table), Spacer(1, 7)]; continue
        if line.startswith("### "):
            result.append(para(line[4:], "h2")); i += 1; continue
        if line.startswith("- "):
            is_source = "확인 " in line and "](http" in line and ". 확인 범위:" in line
            if is_source:
                if not source_note:
                    result.append(para("출처별 상세 열람 범위는 위키의 출처 기록에서 확인합니다.", "small")); source_note = True
                line = line.split(". 확인 범위:", 1)[0] + "."
            result.append(para("• " + line[2:], "small" if is_source else "body")); i += 1; continue
        if re.match(r"\d+\. ", line):
            result.append(para(line)); i += 1; continue
        paragraph = [line]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(### |[-|]|\d+\. |<!--)", lines[i].strip()):
            paragraph.append(lines[i].strip()); i += 1
        result.append(para(" ".join(paragraph)))
    return result


def render_topic(topic, out):
    path = ROOT / topic["path"]
    _, fm, body = path.read_text(encoding="utf-8").split("---", 2)
    match = re.search(r"(?ms)^## 서브노트\s*\n(.*?)(?=^## |\Z)", body)
    if not match:
        raise ValueError(f"서브노트 절 없음: {path}")
    questions = list(dict.fromkeys(r["question"] for r in topic["requirements"]))
    heading = [para(topic["id"].upper(), "label"), para(topic["title"], "title"), para("연관 기출 · " + ", ".join(questions), "small")]
    flow = markdown_flow(match[1])
    if topic["id"] in ("relational-normalization", "nist-ai-rmf", "ipv4-subnetting-vlsm", "uml-dice-model", "uml-sequence-library"):
        if topic["id"].startswith("uml-"):
            heading_pos = next(i for i, item in enumerate(flow) if isinstance(item, Paragraph) and item.getPlainText() == "구조·비교·판단")
            flow.insert(heading_pos, PageBreak())
        position = next((i for i, item in enumerate(flow) if isinstance(item, Table)), 1)
        flow.insert(position, TopicDiagram(topic["id"]))
    doc = PrintDoc(out, ident=topic["id"], domain=topic["domain"])
    doc.build(heading + flow)
    reader = PdfReader(out)
    count = len(reader.pages)
    if count > 4:
        raise ValueError(f"토픽이 4쪽 초과: {topic['id']} ({count}쪽). 내용을 독립 하위 토픽으로 분할하세요")
    if count % 2:
        writer = PdfWriter(); writer.append(reader)
        buffer = BytesIO(); c = canvas.Canvas(buffer, pagesize=A4, initialFontName="NG")
        left, right = 16 * mm, W - 22 * mm
        c.setFont("NG-Bold", 15); c.drawString(left, H - 26 * mm, "회상·답안 메모")
        c.setFont("NG", 10); c.drawString(left, H - 35 * mm, "내용을 가리고 핵심 정의·비교·예제를 적은 뒤 본문과 대조하세요.")
        c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(.3)
        for row in range(12):
            y = H - (51 + 17 * row) * mm; c.line(left, y, right, y)
        c.setFillColor(colors.black); c.setFont("NG", 8.5)
        c.drawString(left, 11 * mm, topic["id"][:67]); c.drawRightString(right, 11 * mm, str(count + 1))
        c.showPage(); c.save(); writer.append(PdfReader(buffer))
        with out.open("wb") as stream:
            writer.write(stream)
        count += 1
    return count


def render_front(catalog, page_map, out):
    story = [para("정보관리기술사", "label"), para("기출 핵심 서브노트", "title"), para("개념을 이해하고, 비교하고, 답안으로 연결하기"), Spacer(1, 10 * mm),
             para("2022~2026년 제126~140회 · 465문항", "h2"), para(f"{len(catalog['topics'])}개 토픽 · 기준 {catalog['built_at']}"),
             para("A4 · 흑백 · 양면 · 실제 크기(100%) · 긴 쪽으로 넘김", "body"), Spacer(1, 5 * mm), para("읽는 순서", "h2"),
             para("한눈에 이해 → 정의와 원리 → 비교·판단 → 적용 예제 → 답안 골격 → 내용을 가리고 회상"),
             para("확인 필요·부분 확인 표시는 근거가 충분하지 않은 항목입니다. 최신 법령·표준과 지정 버전의 차이를 함께 확인하세요. 강사 생성 설명·예제이며 공식 기준답안이 아닙니다."),
             para("분야 구분은 학습을 위한 편집 분류입니다. 전체 출제기준과의 매핑이나 향후 출제 가능성을 뜻하지 않습니다.", "small"),
             para("기출 번호는 회차-교시-문항입니다. 뒤의 기출 찾아보기에서 연결 토픽과 쪽수를 확인할 수 있습니다."), PageBreak(), para("분야별 토픽 목차", "title")]
    domain = None
    for topic in catalog["topics"]:
        if topic["domain"] != domain:
            domain = topic["domain"]; story.append(para(domain, "h2"))
        number = page_map.get(topic["id"], "—")
        story.append(Paragraph(f'<a href="topic:{topic["id"]}" color="#111111">{inline(topic["title"])} · {number}</a>', STYLES["small"]))
    PrintDoc(out, ident="목차", domain="학습과 인쇄 안내").build(story)
    return len(PdfReader(out).pages)


def render_index(catalog, pages, out):
    names = {t["id"]: t["title"] for t in catalog["topics"]}
    story = [para("기출 문항별 찾아보기", "title"), para("문항 연결은 해당 지식의 수록 위치를 뜻합니다. 모든 소요구사항의 검증 완료를 보장하는 표시는 아닙니다. 확인 필요 항목은 토픽의 적용 기준과 근거에서 확인하세요.")]
    for q in catalog["questions"]:
        refs = " / ".join(f"{names[t]} (p.{pages[t]})" for t in q["topics"])
        if not refs:
            refs = "연결 미완료 — 추가 조사 필요"
        state = q.get("review_status", "")
        tag = f" [{state}]" if state in ("부분 확인", "확인 필요", "미연결") else ""
        story.append(para(f"{q['id']}{tag} · {refs}", "small"))
    PrintDoc(out, ident="기출 찾아보기", domain="465문항 → 토픽·본문 위치").build(story)


def book_footer(page, number):
    buffer = BytesIO(); c = canvas.Canvas(buffer, pagesize=A4, initialFontName="NG")
    x = W - (16 if number % 2 else 22) * mm
    c.setFillColor(colors.white); c.rect(x - 22 * mm, 8 * mm, 24 * mm, 9 * mm, fill=1, stroke=0)
    c.setFillColor(colors.black); c.setFont("NG", 8.5); c.drawRightString(x, 11 * mm, str(number)); c.save()
    page.merge_page(PdfReader(buffer).pages[0])


def write_indexes(catalog, manifest, out):
    """Keep the topic collection and requirement map tied to the rendered book."""
    names = {t["id"]: t["title"] for t in catalog["topics"]}
    lines = ["# 토픽별 인쇄 서브노트", "", "A4 · 실제 크기 100% · 흑백 · 양면 · 긴 쪽으로 넘김", "",
             "각 토픽은 2쪽 또는 4쪽입니다. 일부 4쪽 노트의 마지막 면은 회상·답안 메모입니다.", "",
             "부분 확인·확인 필요 표시는 본문 근거와 적용 판본을 함께 확인하세요. 공식 기준답안이 아닙니다.", ""]
    domain = None
    repo_lines = ["# 토픽별 서브노트 목록", "", "[통합 PDF](../../output/pdf/subnotes/정보관리기술사_기출서브노트_통합.pdf) · [개별 PDF 모음](../../output/pdf/subnotes/정보관리기술사_토픽별서브노트.zip) · [기출 요구사항 대응](coverage.md)", ""]
    for topic in catalog["topics"]:
        if domain != topic["domain"]:
            domain = topic["domain"]
            lines += [f"## {domain}", ""]
            repo_lines += [f"## {domain}", ""]
        ident = topic["id"]; count = manifest["topics"][ident]; page = manifest["topic_pages"][ident]
        lines.append(f"- [{topic['title']}](topics/{ident}.pdf) — {count}쪽; 통합 p.{page}; {topic['validation']}")
        repo_lines.append(f"- [{topic['title']}](../../{topic['path']}) · [PDF](../../output/pdf/subnotes/topics/{ident}.pdf) — {count}쪽; 통합 p.{page}; {topic['validation']}")
    index = out / "토픽별_목록.md"; index.write_text("\n".join(lines) + "\n")
    docs = ROOT / "docs/subnotes"; (docs / "topics.md").write_text("\n".join(repo_lines) + "\n")
    coverage = ["# 기출 요구사항과 수록 위치", "", "제126~140회 465문항입니다. ‘수록 연결’은 모든 소문항·판본의 검증 완료를 뜻하지 않습니다. 각 줄은 강사 작성 대응 기록이며 공식 채점 기준이 아닙니다.", ""]
    for question in catalog["questions"]:
        exam, session, number = question["id"].split("-")
        coverage += [f"## {question['id']} · {question['review_status']}", "", question["title"], "",
                     f"[공식 기출 보관 문서](../../wiki/questions/qnet-{exam}-p{session}.md#q{number})", ""]
        for req in question["requirements"]:
            ident = req["topic"]
            path = next(t["path"] for t in catalog["topics"] if t["id"] == ident)
            coverage.append(f"- {'; '.join(req['items'])} → [{names[ident]}](../../{path}), {req['section']}; **{req['status']}**; 통합 p.{manifest['topic_pages'][ident]}.")
        coverage.append("")
    (docs / "coverage.md").write_text("\n".join(coverage).rstrip() + "\n")
    bundle = out / "정보관리기술사_토픽별서브노트.zip"
    with ZipFile(bundle, "w", compression=ZIP_DEFLATED, compresslevel=6) as archive:
        archive.write(index, index.name)
        for ident in manifest["topics"]:
            archive.write(out / "topics" / (ident + ".pdf"), "topics/" + ident + ".pdf")
    return str(bundle.relative_to(ROOT))


def render(catalog_path, out, selected):
    catalog = json.loads(catalog_path.read_text())
    topics = [t for t in catalog["topics"] if not selected or t["id"] in selected]
    if not topics:
        raise ValueError("선택한 토픽 없음")
    for topic in topics:
        body = (ROOT / topic["path"]).read_text(encoding="utf-8").split("---", 2)[2]
        title = re.search(r"(?m)^# (.+)$", body)
        if title:
            topic["title"] = title[1].strip()
    out.mkdir(parents=True, exist_ok=True); individual = out / "topics"; individual.mkdir(exist_ok=True)
    counts = {}
    for topic in topics:
        count = render_topic(topic, individual / (topic["id"] + ".pdf")); counts[topic["id"]] = count
        print(f"{topic['id']}: {count}쪽", flush=True)
    result = {"topics": counts}
    if not selected:
        scratch = ROOT / "tmp/subnotes/layout"; scratch.mkdir(parents=True, exist_ok=True)
        front = scratch / "front.pdf"; start = render_front(catalog, {}, front)
        start += start % 2
        for _ in range(3):
            positions = {}; p = start + 1
            for topic in topics:
                positions[topic["id"]] = p; p += counts[topic["id"]]
            actual = render_front(catalog, positions, front); actual += actual % 2
            if actual == start:
                break
            start = actual
        else:
            raise ValueError("목차 페이지 계산이 수렴하지 않음")
        index = scratch / "index.pdf"; render_index(catalog, positions, index)
        writer = PdfWriter(); writer.append(str(front))
        if len(writer.pages) % 2:
            writer.add_blank_page(W, H)
        for topic in topics:
            before = len(writer.pages)
            writer.append(str(individual / (topic["id"] + ".pdf")))
            writer.add_outline_item(topic["title"], before)
            writer.add_named_destination(topic["id"], before)
        writer.append(str(index))
        if len(writer.pages) % 2:
            writer.add_blank_page(W, H)
        for number, page in enumerate(writer.pages, 1):
            for ref in page.get("/Annots", []):
                annot = ref.get_object(); action = annot.get("/A")
                uri = str(action.get("/URI", "")) if action else ""
                if uri.startswith("topic:"):
                    ident = uri.removeprefix("topic:")
                    if ident not in positions:
                        raise ValueError(f"목차 대상 없음: {ident}")
                    annot[NameObject("/A")] = DictionaryObject({NameObject("/S"): NameObject("/GoTo"), NameObject("/D"): TextStringObject(ident)})
            book_footer(page, number)
        writer.add_metadata({"/Title": "정보관리기술사 기출 핵심 서브노트", "/Author": "정보관리기술사 학습 위키"})
        book = out / "정보관리기술사_기출서브노트_통합.pdf"
        with book.open("wb") as stream:
            writer.write(stream)
        result.update(book=str(book.relative_to(ROOT)), pages=len(writer.pages), topic_pages=positions)
    if not selected:
        result["collection"] = write_indexes(catalog, result, out)
    manifest_name = "manifest-selected.json" if selected else "manifest.json"
    (out / manifest_name).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "topics" and k != "topic_pages"}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "docs/subnotes/catalog.json")
    parser.add_argument("--output", type=Path, default=ROOT / "output/pdf/subnotes")
    parser.add_argument("--topic", action="append", default=[])
    args = parser.parse_args()
    render(args.catalog, args.output.resolve(), args.topic)
