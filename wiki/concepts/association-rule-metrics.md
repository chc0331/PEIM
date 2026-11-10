---
id: association-rule-metrics
title: 연관규칙의 지지도·신뢰도·향상도
aliases:
- Association Rule Metrics
type: concept
domains:
- 데이터분석
sources:
- id: source-subnote-dad35df52ffb
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 연관규칙의 지지도·신뢰도·향상도

## 서브노트

### 한눈에 이해

빵을 산 사람이 우유를 자주 산다고 해도 우유가 원래 매우 흔하면 추천 규칙의 특별한 의미가 약할 수 있습니다. 전체 빈도·조건부 비율·독립 대비 증가를 따로 계산합니다.

### 정의와 핵심 원리

거래 안에서 항목 집합 A의 발생과 다른 집합 B의 동시 발생 관계를 A→B로 표현하고 빈도·조건부 연관 강도를 평가하는 방법입니다.

- 결측 없는 N개 거래에서 support(A→B)=n(A∪B)/N입니다. 여기서 itemset 합집합은 A와B의 모든 항목을 함께 포함하는 거래를 뜻합니다. confidence(A→B)=support(A∪B)/support(A)=P(B|A)이며 방향이 달라지면 분모도 바뀝니다.
- lift=confidence/P(B)=P(A,B)/(P(A)P(B))입니다.1은 독립 수준,1 초과는 양의 연관 단서,1 미만은 음의 연관 단서입니다. leverage=P(A,B)−P(A)P(B), conviction=(1−P(B))/(1−confidence)도 사용할 수 있으나 분모0·극소 표본·기저율을 확인합니다.
- 최소 support로 드문 우연을 줄이고 confidence/lift·통계 불확실성·업무 가치·검증 기간으로 규칙을 평가합니다. Apriori의 downward closure는 빈발 항목 집합의 모든 부분집합도 빈발이라는 가지치기 근거입니다. 동시 구매는 인과나 향후 추천의 매출 증가를 증명하지 않으므로 독립 기간·실험으로 확인합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Support | 함께 발생한 거래/전체 거래 | 규칙의 빈도 |
| Confidence | 함께 발생/선행 A 거래 | 방향·B 기저율 영향 |
| Lift | confidence/B 전체 비율 | 독립 대비·표본 오차 |

<!-- subnote-page:apply -->

### 적용 예제

**분모를 분리한 계산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 거래 10건 중 A가 있는 거래는 4건, B가 있는 거래는 5건, A와 B가 모두 있는 거래는 3건입니다. 결측은 없습니다.

1. 전체 거래를 분모로 둔 지지도는 3/10=.3입니다. A가 있는 거래를 분모로 둔 신뢰도는 3/4=.75입니다.
2. lift=.75/(5/10)=1.5, leverage=.3−.4×.5=.1입니다.
3. conviction=(1−.5)/(1−.75)=2입니다. 반대방향 confidence(B→A)=3/5=.6으로 달라집니다.

**결과·해석:** 전체 거래의 30%에 A와 B가 함께 있습니다. A가 있는 거래에서는 75%에 B가 있습니다. 이는 B가 전체에서 나온 비율의 1.5배입니다.

**전제·주의:** lift1.5가 곧 추천 적용 시 매출1.5배라는 의미는 아닙니다. 결측이 있으면 정의·분모 정책을 다시 정합니다.

### 답안 골격과 혼동 방지

규칙·거래 단위 → 3핵심 지표 식 → 추가 지표·임계값 → 10거래 수치 예시 → 검증·인과·업무 가치

- itemset A∪B를 A 또는 B 중 하나만 있는 거래로 세지 않습니다.
- 높은 confidence만으로 흔한 결과 항목의 규칙을 좋은 추천이라 결론 내리지 않습니다.

### 내용을 가리고 회상

1. 지지도·신뢰도의 분모는 각각 무엇입니까?
2. A→B와 B→A의 lift와 confidence는 어떻게 다릅니까?
3. 우유가 아주 흔할 때 lift가 왜 필요합니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Association rules](https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/association_rules/) — Sebastian Raschka / mlxtend developers; 문서 버전·날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: 결측 없는 기본 support/confidence/lift/leverage/conviction 식. NaN을 허용하는 확장 분모도 있어 예제는 결측 없는 거래로 한정합니다. 본문 not symmetric or directed 문구는 방향성 설명과 모순되어 confidence 식에 따라 방향성을 해석합니다.

## 연관 기출

- [제137회 1교시 13번](../questions/qnet-137-p1.md#q13) — 연관 규칙 분석 지표. 대응: 예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
