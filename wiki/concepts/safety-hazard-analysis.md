---
id: safety-hazard-analysis
title: SW 안전성·FTA·FMEA·HAZOP·STPA
aliases: []
type: concept
domains:
- 소프트웨어공학
sources:
- id: source-subnote-e46f9fc7583e
- id: source-subnote-d3ce8459ec4b
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# SW 안전성·FTA·FMEA·HAZOP·STPA

## 서브노트

### 한눈에 이해

부품이 모두 정상이어도 잘못된 제어와 상호작용으로 사고가 날 수 있어 시스템 관점의 분석이 필요합니다.

### 정의와 핵심 원리

안전 분석은 허용할 수 없는 손실과 위험 상태를 식별하고 이를 막을 제약·설계·검증을 도출하는 활동입니다. 소프트웨어에서는 내부 결함뿐 아니라 명세·제어·인간·환경의 상호작용을 함께 검토합니다.

- FTA는 최상위 사건(Top Event)에서 원인을 AND/OR 게이트로 내려가는 연역적 분석으로 사고 조합·최소 컷셋을 찾습니다. FMEA는 각 구성요소의 고장모드→영향→원인·검출·대책을 올라가는 귀납적 분석이며, 중요도/위험순위는 평가척도와 한계를 밝혀 사용합니다.
- HAZOP은 유량·압력·온도·시간 같은 매개변수에 없음·과다·부족·역전 등의 가이드워드를 적용해 설계 의도에서 벗어나는 편차와 원인·결과·보호조치를 찾는 협업 분석입니다. 정상 설계 의도와 분석 노드를 명확히 해야 합니다.
- 전통 기법은 개별 고장·사건 연쇄에는 유용하지만 복잡한 SW·조직·인간의 비고장 상호작용이나 제어의 불충분함을 놓칠 수 있습니다. 이는 기법을 버릴 이유가 아니라 분석 모델을 보완할 이유입니다.
- STPA는 분석 목적(손실·위험·시스템 제약) 정의→컨트롤러·제어행동·제어대상·피드백의 제어구조 모델→안전하지 않은 제어행동(UCA)→이를 일으키는 손실 시나리오를 식별합니다. UCA는 필요한 행동 미제공, 위험한 제공, 너무 이르거나 늦음/순서 오류, 너무 오래 또는 일찍 중단으로 분석합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·판단 |
| --- | --- | --- |
| FTA | 사고에서 원인 조합으로 | 연역·AND/OR |
| FMEA/HAZOP | 고장모드 / 의도 편차 | 귀납·체계적 검토 |
| STPA | 안전 제어의 제약과 상호작용 | 고장이 없는 위험도 분석 |

<!-- subnote-page:apply -->

### 적용 예제

**강사 창작 적용 예시: 자동문 제어 안전성**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 사람이 통로에 있는데 문이 닫히면 충돌 손실이 발생합니다.

1. FTA는 센서 고장과 제동 실패의 조합을 검토합니다.
2. HAZOP은 닫힘 명령이 너무 이르거나 오래 지속되는 편차를 찾습니다.
3. STPA에서는 제어기가 오래된 피드백을 받아 통로에 사람이 있는데도 문을 닫으라고 명령하는 경우를 UCA로 봅니다. 센서 정보가 오래되면 문을 닫지 않도록 제약을 정합니다.

**결과·해석:** 부품 고장과 정상 부품의 잘못된 상호작용을 함께 다룹니다.

**전제·주의:** 안전 검증 완료나 인증 적합성을 이 예시만으로 선언하지 않습니다.

### 답안 골격과 혼동 방지

안전 분석 필요성 → 3전통기법 원리·한계 비교 → STPA 절차·UCA·제어구조 사례

- FTA에서는 먼저 피하려는 사고나 고장을 최상위 사건(Top Event)으로 정하고, 어떤 사건이 그 원인이 되는지 거슬러 올라갑니다.
- RPN만으로 모든 치명 위험의 우선순위를 정하지 않습니다.

### 내용을 가리고 회상

1. FTA와 FMEA의 추론 방향은 어떻게 다릅니까?
2. STPA UCA 네 범주를 말하십시오.
3. 고장 없이 사고가 날 수 있는 예를 드십시오.

### 적용 기준과 근거

MIT 자료에서 STPA의 단계와 대상을, NASA 자료에서 FTA 최상위 사건의 의미를 확인했습니다. FTA·FMEA·HAZOP의 세부 절차와 위험평가 척도는 적용 산업의 표준을 추가로 확인해야 합니다. [NASA Fault Tree Handbook with Aerospace Applications 1장](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf)

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Books and Handbooks: STPA Handbook](https://psas.scripts.mit.edu/home/books-and-handbooks/) — Nancy Leveson, John Thomas / MIT; 2018-03; 확인 2026-11-05. 확인 범위: 공식 안내 페이지의 단계·이론·대상 범위 열람. get_file PHP 주소는 HTML을 반환해 전체 핸드북은 그 경로로 확보하지 못했습니다.
- [Guide to the SWEBOK v4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf) — IEEE Computer Society / Hironori Washizaki 편; 2026-08; 확인 2026-11-05. 확인 범위: 공개 PDF 열람. 요구사항·설계·테스트·유지보수·형상관리·품질 장의 해당 절을 참조. 기출 당시 판본과 현재 v4.0a를 구분합니다.

## 연관 기출

- [제128회 3교시 3번](../questions/qnet-128-p3.md#q3) — 전통적 위험분석 기법인 FMEA(Failure Mode and Effects Analysis), HAZOP(Hazard and Operability Analysis)의 특징 및 한계점; STPA(System Theoretic Process Analysis) 개념 및 위험분석 방법 2–1. 대응: 핵심원리/예제/비교표; 충족.
- [제131회 3교시 4번](../questions/qnet-131-p3.md#q4) — FTA(Fault Tree Analysis); FMEA(Failure Mode and Effects Analysis); HAZOP(Hazard and Operability Analysis). 대응: 핵심원리/예제/비교표; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
