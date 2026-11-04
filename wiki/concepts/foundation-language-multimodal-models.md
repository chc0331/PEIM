---
id: foundation-language-multimodal-models
title: 파운데이션·PLM·LLM·멀티모달과 적용 설계
aliases:
- Foundation and Language Models
type: concept
domains:
- 인공지능
sources:
- id: source-subnote-afb76917d8ad
- id: source-subnote-3d7d444bcdb3
- id: source-subnote-1098fc60be7c
- id: source-subnote-02ad74cdb0c9
- id: source-subnote-38c43325a50c
- path: raw/corrections/2026-11-05-subnotes-review.md
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# 파운데이션·PLM·LLM·멀티모달과 적용 설계

## 서브노트

### 한눈에 이해

넓은 자료로 먼저 학습한 공통 모델을 업무에 맞춰 적응시키면 과업마다 처음부터 만들지 않아도 됩니다. 크기가 크거나 여러 입력을 다룬다는 이유만으로 모든 문제를 이해하는 범용지능이 된 것은 아닙니다.

### 정의와 핵심 원리

파운데이션 모델은 광범위 자료에서 학습해 여러 후속 과업에 적응할 기반 모델이며 PLM은 사전학습 언어모델, LLM은 큰 규모의 언어모델, 멀티모달 LLM은 여러 정보 양식을 연계하는 언어모델 시스템입니다.

- 대표 과정은 수집/권리·정제/중복 제거→토큰화→자기지도 사전학습→과업/지시 SFT→필요 시 선호 정렬→평가·배포입니다. decoder LM은 다음 토큰을, masked LM은 가린 토큰을 예측하는 등 목적이 다릅니다. PLM과 LLM의 경계가 단일 공식 파라미터 수로 정해진 것은 아니며 PLM이 반드시 모든 후학습 단계를 거쳐야 LLM이 되는 것은 아닙니다.
- 멀티모달은 이미지/음성 encoder와 언어모델의 연결·공유 표현·대조/지시 학습·출력 decoder를 구성할 수 있습니다. CLIP은 이미지-텍스트 쌍의 표현 정렬 사례이지만 그 자체가 대화형 LLM은 아닙니다. 모달 간 정렬·시간 동기·토큰 비용·평가 집단을 관리합니다. ANI의 특정 과업 역량과 AGI의 넓은 적응/추론 목표를 구분합니다.
- 적용 고려5축은 업무 지표, 데이터/근거 품질, 모델 능력·권리, 인프라/비용·지연, 평가·운영 책임입니다. 실무 구조5예는 직접 호출, prompt workflow, RAG, fine-tuned 모델, RAG+fine-tuning 결합입니다. 이는 조합 가능한 강사 설계 분류로 유일한 공식5종이 아닙니다. 공개 원문의 버전별 도입 절차·법적 요구는 따로 확인합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Foundation·PLM | 넓은 사전학습·과업 적응 | 범위·학습 목적 명시 |
| LLM·Multimodal LLM | 언어 규모·모달 결합 | 크기와 보편 추론 구분 |
| ANI·AGI | 특정 과업 능력/범용 목표 | 연속성·전이 연구, 달성 보장 없음 |

<!-- subnote-page:apply -->

### 적용 예제

**정비 문서·사진 지원**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 정비사가 설비 사진과 고장코드로 매뉴얼 조항을 찾고자 합니다.

1. 사진 encoder로 부품/상태 단서를 얻고 고장코드의 정확 문자열 검색을 함께 사용합니다.
2. 최신 매뉴얼 RAG로 근거를 제공하고 반복 출력 형식이 부족하면 SFT를 별도 검토합니다.
3. 사진 판독·근거 검색·응답 정확도·지연/비용을 분리 평가하고 불확실한 판독은 사용자 확인으로 넘깁니다.

**결과·해석:** 모델 이름보다 학습·검색·모달 연결·운영 책임을 구조로 설명합니다.

**전제·주의:** 기관별 법적·환경적·사회적 고려와 공식 도입 절차는 관련 원문을 추가 확인해야 합니다.

### 답안 골격과 혼동 방지

정의와 용어 경계 → 사전→지시→선호 학습 → 멀티모달 구성 → 5고려·5실무구조 → ANI 역할·적용 한계

- PLM을 작은 모델, LLM을 특정 후학습 완료 모델로만 정의하지 않습니다.
- 멀티모달 모델의 출력 문장이 원 이미지 판독의 진실성을 보장하지 않습니다.

### 내용을 가리고 회상

1. 파운데이션 모델과 언어모델의 포함 관계는 무엇입니까?
2. CLIP과 대화형 멀티모달 LLM은 어떻게 다릅니까?
3. 새 지식 반영과 출력 행동 학습을 어떤 구조로 나누겠습니까?

### 적용 기준과 근거

기반 정의·CLIP·SFT/RLHF·RAG 원문 확인. 5종 구조는 공개한 강사 설계이며 공식 가이드2.0의 지정 절차·사회/법 세부는 이 토픽에서 확정하지 않습니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) — Rishi Bommasani 외 / Stanford CRFM; 2022-07-12 v3; 확인 2026-11-05. 확인 범위: 실제 열람: 광범위 데이터 사전학습 후 다양한 과업 적응이라는 foundation model 정의·범위. 법적 세부 규정의 근거는 아니며 AGI 달성 증거로 쓰지 않습니다.
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) — Alec Radford 외; 2021-02-26 v1; 확인 2026-11-05. 확인 범위: 실제 열람: 이미지-텍스트 쌍의 대조적 학습과 zero-shot transfer. CLIP 자체를 대화형 Multimodal LLM과 동일시하지 않습니다.
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — Long Ouyang 외; 2022-03-04 v1; 확인 2026-11-05. 확인 범위: 실제 열람: demonstration SFT, response ranking, reward model과 RLHF 단계. 인간 선호가 모든 사실 정확성을 보장하는 것은 아닙니다.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — Patrick Lewis 외; 2021-04-12 v4; NeurIPS 2020; 확인 2026-11-05. 확인 범위: 실제 열람: parametric generator와 nonparametric dense index 결합, sequence/token별 근거 사용. 모든 RAG가 학습 필요 또는 환각을 제거한다는 주장은 하지 않습니다.
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic Engineering; 2024-12-19; 2026 갱신 안내 포함; 확인 2026-11-05. 확인 범위: 실제 열람: predefined workflows vs LLM 동적 agent, orchestrator-workers·evaluator-optimizer, 비용/지연 절충. 단일 공급자 실무 패턴을 MAS 전체 이론과 동일시하지 않습니다.

## 연관 기출

- [제131회 4교시 4번](../questions/qnet-131-p4.md#q4) — 파운데이션 개념·특징·기술; 법적·환경적·사회적 고려. 대응: 핵심원리; 부분 충족.
- [제133회 2교시 4번](../questions/qnet-133-p2.md#q4) — PLM 특성; LLM 학습 과정. 대응: 핵심원리; 충족.
- [제133회 3교시 2번](../questions/qnet-133-p3.md#q2) — 생성형AI 개념·활용서비스. 대응: 핵심원리; 부분 충족.
- [제135회 1교시 2번](../questions/qnet-135-p1.md#q2) — Multimodal LLM. 대응: 핵심원리; 충족.
- [제135회 1교시 13번](../questions/qnet-135-p1.md#q13) — AGI 측면 ANI 필요성. 대응: 핵심원리; 부분 충족.
- [제135회 2교시 5번](../questions/qnet-135-p2.md#q5) — LLM 적용 5가지 고려; 구현 가능한 5가지 아키텍처. 대응: 핵심원리; 부분 충족.
- [제137회 2교시 4번](../questions/qnet-137-p2.md#q4) — 초거대AI 개념·구성·기술; 2.0 도입절차. 대응: 핵심원리; 부분 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
