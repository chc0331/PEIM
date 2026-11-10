---
id: transformer-mixture-of-experts
title: Transformer와 MoE의 결합
aliases:
- Transformer and MoE
type: concept
domains:
- 딥러닝
sources:
- id: source-subnote-8a455ddf634c
- id: source-subnote-bf9cd21d7a7a
- path: raw/corrections/2026-11-05-subnotes-review.md
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# Transformer와 MoE의 결합

## 서브노트

### 한눈에 이해

문장 안에서 어떤 단어를 참고할지 정하는 attention과 어떤 계산 전문가를 쓸지 정하는 routing은 다른 기능입니다. Transformer의 일부 계산층을 전문가 여러 개로 바꾸어 선택 실행할 수 있습니다.

### 정의와 핵심 원리

Transformer는 self-attention과 위치별 신경망을 중심으로 순서를 처리하는 구조이며 MoE는 입력별로 일부 전문가를 선택하는 조건부 계산 구조입니다.

- 입력 embedding·위치 정보에서 Q/K/V를 만들고 Attention(Q,K,V)=softmax(QKᵀ/√d_k)V를 계산합니다. multi-head는 여러 투영 공간의 결과를 결합합니다. residual·normalization·FFN을 쌓으며 decoder의 causal mask는 미래 토큰을 가려 자기회귀 학습의 정보 누출을 막습니다.
- 밀집 FFN에서는 모든 토큰에 같은 가중치를 적용합니다. 희소 MoE에서는 라우터가 토큰마다 점수가 높은 전문가 k개를 골라 실행하고 결과를 합칩니다. 한 모델 안에서 어텐션 층과 MoE FFN을 함께 쓸 수 있으며, 전문가를 늘려도 토큰마다 실행하는 연산이 같은 비율로 늘지는 않습니다.
- MoE는 용량 확대와 계산 효율 가능성이 있으나 전문가 편중·capacity overflow·라우터 불안정·노드 간 all-to-all 통신·추론 배치효율·큰 메모리를 다뤄야 합니다. load balancing·전문가 배치·통신 최적화를 검토하며 Switch의 특정 실험 배속을 모든 모델의 비용 절감률로 일반화하지 않습니다.
- Q와 K 성분을 독립·평균0·분산1로 보는 설명용 가정에서는 내적의 분산이 d_k입니다. √d_k로 나누어 점수 크기를 안정화하고 큰 내적으로 인한 softmax 포화와 작은 기울기를 완화합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Attention | 입력 위치별 참조 가중 | Q/K/V·mask·위치 |
| Dense FFN | 토큰마다 같은 계산층 | 단순 배치·모든 파라미터 활성 |
| MoE FFN | router가 전문가 일부 선택 | 활성 연산·통신·편중 관리 |

<!-- subnote-page:apply -->

### 적용 예제

**전문가 두 명의 가중 결합**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 한 토큰에 대해 라우터가 전문가 E1에 0.7, E2에 0.3을 줍니다. 두 전문가의 출력은 각각 [2,0]과 [0,4]입니다.

1. 두 전문가를 모두 고르면 0.7[2,0]+0.3[0,4]=[1.4,1.2]입니다.
2. top-1이면 하나만 실행하므로 정규화·capacity 정책에 따라 결과가 달라집니다.
3. expert 총개수·top-k·토큰 분배와 네트워크 비용을 함께 기록해야 모델 규모와 실제 계산량을 비교할 수 있습니다.

**결과·해석:** 전문가 선택은 여러 모델의 답을 사람이 투표하는 것과 다른 내부 계산입니다.

**전제·주의:** 예제 가중치는 교육용이며 특정 제품의 router 정규화 규칙을 가정하지 않습니다.

### 답안 골격과 혼동 방지

두 개념 정의·관계 → attention 식·mask → MoE routing 흐름 → 가중 결합 예시 → 연산/메모리/통신 절충

- Transformer와 MoE를 반드시 대체 관계로 쓰지 않습니다.
- 전체 파라미터 수를 매 토큰 계산량과 동일시하지 않습니다.

### 내용을 가리고 회상

1. QKᵀ 뒤 √d_k로 나누는 목적은 무엇입니까?
2. causal mask는 무엇을 막습니까?
3. 전문가가 늘어도 활성 계산과 메모리는 어떻게 다를 수 있습니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) — Ashish Vaswani 외; 2017 원 논문; 2023-08-02 v7; 확인 2026-11-05. 확인 범위: 실제 열람: HTML 본문 3.2의 scaled dot-product attention, QK^T/√d_k·softmax·V와 mask, encoder-decoder·multi-head 구성. 원 성능을 최신 LLM 성능 예측으로 옮기지 않습니다.
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) — William Fedus, Barret Zoph, Noam Shazeer; 2022-06-16 v3; 확인 2026-11-05. 확인 범위: 실제 열람: 입력별 expert 선택·sparse activation·routing·통신/불안정성 문제. 전체 파라미터와 토큰당 활성 파라미터 차이를 설명합니다.

## 연관 기출

- [제137회 1교시 7번](../questions/qnet-137-p1.md#q7) — 트랜스포머; MoE. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
