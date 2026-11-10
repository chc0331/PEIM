---
id: retrieval-augmented-generation
title: RAG·Advanced/Modular와 하이브리드 검색
aliases:
- RAG
- Retrieval-Augmented Generation
type: concept
domains:
- 인공지능
sources:
- id: source-subnote-02ad74cdb0c9
- id: source-subnote-3f775f631e05
- id: source-subnote-79a654f0a776
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# RAG·Advanced/Modular와 하이브리드 검색

## 서브노트

### 한눈에 이해

모델이 외운 기억만 묻는 대신 최신 업무 문서를 찾아 책을 펴 놓고 답하게 합니다. 다만 책을 잘못 찾거나 근거를 무시하면 여전히 틀릴 수 있어 검색과 답변을 따로 평가합니다.

### 정의와 핵심 원리

RAG는 외부 검색 근거를 언어모델 문맥에 결합하여 응답을 생성하는 방법이며 모델 가중치를 바꾸는 fine-tuning과 다른 갱신 경로입니다.

- 검색을 준비할 때는 문서 권리와 버전을 확인하고 내용을 검색 단위(chunk)로 나눕니다. 임베딩·색인·메타데이터를 저장하고 문서 갱신과 삭제를 반영합니다. 질문이 들어오면 권한에 맞는 후보를 찾고 관련성이 높은 순서로 다시 매겨 모델의 입력에 넣습니다. 답변에는 근거를 표시합니다.
- Gao 등의 분류에서 Naive는 index-retrieve-generate의 기본 구조, Advanced는 사전 query/index 최적화와 사후 reranking/문맥 정리로 보완하며 Modular는 검색·라우팅·반복·재작성 등 모듈을 과업에 맞게 조합합니다. Advanced와 Modular는 배타적 제품 등급이 아니라 저자의 설계 분류입니다.
- 하이브리드는 lexical(BM25 등)의 정확 용어/코드 일치와 vector의 의미 유사성을 결합합니다. RRF는 Σ1/(k+rank_i)로 서로 다른 순위를 합칠 수 있습니다. retrieval recall/precision·근거 적합성과 응답 정확/faithfulness·완결성·지연·비용을 분리 측정하며 답이 없는 질문은 근거 없음으로 처리합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Lexical | 어휘·정확 코드·역색인 | 동의어/표현 차이에 약할 수 있음 |
| Vector | embedding 의미 유사성 | 수치·고유코드 exact match 보완 필요 |
| Advanced·Modular | 전후 개선/모듈 조합 | 반복 검색·라우팅은 비용 증가 |

<!-- subnote-page:apply -->

### 적용 예제

**매뉴얼의 E-42 오류 검색**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 사용자는 E-42 냉각 경보 해제 방법을 질문합니다.

1. 어휘 검색으로 E-42가 적힌 문서를 찾습니다. 벡터 검색으로 냉각·과열처럼 뜻이 가까운 표현이 들어간 절도 찾습니다.
2. 발행일과 장비 모델을 확인해 적용 가능한 문서를 남깁니다. 두 검색 결과의 순위를 합친 뒤 관련 조항을 다시 추립니다.
3. 선정 근거와 적용 모델을 포함해 답하고 검색 누락과 생성 오류를 별도 기록합니다.

**결과·해석:** 최신성은 색인 갱신에서, 답변의 근거 사용은 생성 평가에서 확인합니다.

**전제·주의:** RRF의 k는 군집 수가 아닌 순위 평활 상수이며 source별 점수를 확률처럼 더하지 않습니다.

### 답안 골격과 혼동 방지

RAG 정의·FT 비교 → offline/online 구조 → Advanced/Modular 표 → hybrid·RRF → 품질·날짜·권한·비용 평가

- RAG가 환각을 완전히 없앤다고 쓰지 않습니다.
- 검색된 문서에 있다는 사실만으로 기술 내용이 진실이라고 확정하지 않습니다.

### 내용을 가리고 회상

1. RAG에서 문서를 갱신하면 모델 가중치가 바뀝니까?
2. Advanced와 Modular는 어떤 설계 차이입니까?
3. lexical과 vector를 함께 쓰면 어떤 질문을 보완합니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — Patrick Lewis 외; 2021-04-12 v4; NeurIPS 2020; 확인 2026-11-05. 확인 범위: 실제 열람: parametric generator와 nonparametric dense index 결합, sequence/token별 근거 사용. 모든 RAG가 학습 필요 또는 환각을 제거한다는 주장은 하지 않습니다.
- [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/html/2312.10997v5) — Yunfan Gao 외; 2024-03-27 v5; 확인 2026-11-05. 확인 범위: 실제 열람: II-A/B/C Naive/Advanced/Modular의 저자 분류와 retrieval/generation/augmentation 구성. 이 분류를 제안한 원 자료로만 쓰며 개별 알고리즘 성능 근거는 아닙니다.
- [Hybrid search using vectors and full-text search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) — Microsoft Azure AI Search; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: lexical/vector 병렬 검색·RRF 순위 결합·제품 코드 exact-match 장점. RRF의 k는 설정이고 확률 보정이 아닙니다.

## 연관 기출

- [제134회 1교시 13번](../questions/qnet-134-p1.md#q13) — RAG. 대응: 핵심원리; 충족.
- [제139회 1교시 3번](../questions/qnet-139-p1.md#q3) — Advanced RAG·Modular RAG 비교. 대응: 핵심원리; 충족.
- [제139회 2교시 2번](../questions/qnet-139-p2.md#q2) — fine-tuning·RAG 개념·역할. 대응: 핵심원리; 충족.
- [제140회 1교시 6번](../questions/qnet-140-p1.md#q6) — 어휘·의미 결합 hybrid 검색. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
