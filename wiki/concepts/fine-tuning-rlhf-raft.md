---
id: fine-tuning-rlhf-raft
title: Fine-tuning·RLHF·RAFT 파이프라인
aliases:
- Fine-tuning, RLHF and RAFT
type: concept
domains:
- 인공지능
sources:
- id: source-subnote-1098fc60be7c
- id: source-subnote-30c747a1ce4c
- id: source-subnote-02ad74cdb0c9
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# Fine-tuning·RLHF·RAFT 파이프라인

## 서브노트

### 한눈에 이해

검색 증강 생성(RAG)은 답변할 때 필요한 문서를 찾아 보여 줍니다. 미세 조정(fine-tuning)은 반복할 과업의 형식과 행동을 가중치에 학습시킵니다. RLHF는 사람이 선호하는 답변에, RAFT는 주어진 문서에서 답의 근거를 고르는 데 초점을 둡니다.

### 정의와 핵심 원리

Fine-tuning은 사전학습 모델의 파라미터를 추가 자료로 조정하며 RLHF는 인간 선호 보상으로 정책을 최적화하고 RAFT는 도메인 RAG 문맥을 읽는 지도학습 데이터 구성법입니다.

- SFT는 입력-바람직한 출력 쌍으로 조건부 언어모델 손실을 줄여 형식·업무 스타일·과업 행동을 학습합니다. RAG는 외부 색인·문맥 갱신으로 지식을 공급하므로 둘을 결합할 수 있습니다. 가중치에 지식을 넣으면 삭제·최신성·근거 추적이 더 어려울 수 있습니다.
- InstructGPT의 RLHF는 시범 응답 수집→SFT→모델 출력 쌍의 인간 순위→reward model 학습→PPO 등으로 보상과 기준모델 이탈을 고려해 정책 최적화→독립 평가입니다. 보상 모형의 편향·reward hacking·선호/사실의 차이를 점검합니다.
- RAFT에서는 질문과 정답 근거 문서, 방해 문서, 근거를 인용한 답변을 만들어 지도 미세 조정(SFT)에 씁니다. 실제로 답할 때는 RAG로 문맥을 제공합니다. 원 논문은 일부 학습 표본에서 정답 근거 문서를 빼기도 했습니다. 선호 순위, 보상 모델, 강화학습은 필수 단계가 아닙니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| RAG | 질의 시 외부 문서 공급 | 지식 갱신·근거 제공 |
| RLHF | 선호→보상모형→정책 최적화 | 행동 정렬·보상 오류 |
| RAFT | 관련/방해 문서+근거 응답의 SFT | 도메인 근거 읽기 적응 |

<!-- subnote-page:apply -->

### 적용 예제

**사내 규정 QA 개선**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 같은 질문에 현행 규정과 구 규정/무관 문서가 섞여 검색됩니다.

1. RAG로 문서 날짜·관련 절을 공급하고 최신 문서가 검색되는지 먼저 확인합니다.
2. RAFT 자료에는 질문·정답 근거·방해 문서·근거 응답을 넣어 방해를 무시하는 행동을 학습시킵니다.
3. 정중함·유용성 선호를 개선하려면 별도의 선호 라벨·RLHF 절차를 검토하고 사실 정확도는 독립 정답으로 평가합니다.

**결과·해석:** 현행 규정이 검색되지 않았는지, 근거가 있어도 답에 쓰지 못했는지, 답변 표현이 선호와 어긋났는지 나눠 확인합니다.

**전제·주의:** 공개 규정이 바뀌었다고 fine-tuning만 반복하면 검색 최신성 문제가 남을 수 있습니다.

### 답안 골격과 혼동 방지

FT/RAG 역할 → RLHF 단계 도식 → RAFT 자료·SFT 단계 → 학습 신호·목표 비교 → 평가·최신성·비용

- RAFT를 강화학습 알고리즘이라고 쓰지 않습니다.
- 인간 선호 보상이 사실 정확성과 항상 같다고 하지 않습니다.

### 내용을 가리고 회상

1. RLHF에서 reward model 학습 자료는 무엇입니까?
2. RAFT의 distractor를 넣는 목적은 무엇입니까?
3. RAG와 FT를 결합할 업무 조건은 무엇입니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — Long Ouyang 외; 2022-03-04 v1; 확인 2026-11-05. 확인 범위: 실제 열람: demonstration SFT, response ranking, reward model과 RLHF 단계. 인간 선호가 모든 사실 정확성을 보장하는 것은 아닙니다.
- [RAFT: Adapting Language Model to Domain Specific RAG](https://arxiv.org/html/2403.10131v2) — Tianjun Zhang 외 / UC Berkeley 연구진; 2024-06-05 v2; 확인 2026-11-05. 확인 범위: 실제 열람: HTML 3절의 질문·golden/distractor 문서·근거 포함 응답, 일부 학습 표본의 golden 문서 제외, 도메인 RAG 적응. RAFT는 supervised fine-tuning이며 RLHF와 같은 강화학습 정렬 기법이 아닙니다.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — Patrick Lewis 외; 2021-04-12 v4; NeurIPS 2020; 확인 2026-11-05. 확인 범위: 실제 열람: parametric generator와 nonparametric dense index 결합, sequence/token별 근거 사용. 모든 RAG가 학습 필요 또는 환각을 제거한다는 주장은 하지 않습니다.

## 연관 기출

- [제139회 2교시 2번](../questions/qnet-139-p2.md#q2) — fine-tuning·RAG 개념·역할; RLHF 학습 pipeline; RAFT 학습 pipeline 비교. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
