---
id: synthetic-data-generation-evaluation
title: 합성데이터 생성과 품질 평가
aliases:
- Synthetic Data
type: concept
domains:
- 데이터관리
sources:
- id: source-subnote-b0ceddead282
- id: source-subnote-bd650446d393
- id: source-subnote-c7e0bc3f8888
- id: source-subnote-047809fe9878
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# 합성데이터 생성과 품질 평가

## 서브노트

### 한눈에 이해

원본의 나이·매출 분포와 관계를 닮은 새 행을 만들면 학습·시험 자료를 보완할 수 있습니다. 단순히 비슷하게 보인다고 희귀 집단의 성능이나 원본 보호까지 확인된 것은 아닙니다.

### 정의와 핵심 원리

실제 현상을 모형·규칙·시뮬레이션·생성모형으로 모사하여 만든 인공 자료이며 통계 유사성·과업 효용·노출 위험을 별도로 평가해야 합니다.

- 생성에는 규칙·시뮬레이션, 통계 모형, VAE·GAN, 확산 모델·언어 모델 등을 쓸 수 있습니다. 필요한 데이터와 희귀 사례를 정한 뒤 실제 데이터를 학습용과 평가용(holdout)으로 나눕니다. 드문 고장이나 경계 사례는 조건부 생성이나 물리 시뮬레이션으로 보완할 수 있습니다.
- 품질은 유효 범위·PK/FK·논리 제약, 단변량 분포(KS·빈도 차이), 다변량 관계/상관·관계표 cardinality, coverage/다양성, downstream task 효용으로 나눕니다. Train-on-synthetic/Test-on-real로 실제 holdout 성능을 비교하며 분포가 닮았다는 점수만으로 업무 가치를 확정하지 않습니다.
- 과적합·원본 중복·근접도·속성/멤버십 추론 등 노출 위험을 함께 평가합니다. 원본과 똑같은 행이 없어도 민감한 패턴이 노출될 수 있습니다. 통계 위험 지표와 법적 익명성 판단은 별개이며 일반 합성 데이터가 차분 프라이버시 같은 수학적 보장을 자동 제공하지 않습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| 충실도 | 원본 분포·관계 유사성 | holdout·희귀 집단 확인 |
| 유용성 | 실제 과업의 성능·가치 | TSTR 등 실제 시험 필요 |
| 노출 위험 | 복제·근접·추론 가능성 | 유사성과 상충 가능 |

<!-- subnote-page:apply -->

### 적용 예제

**연령·구매액 합성 자료**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 실제 자료 1만 행 중 2천 행은 평가용으로 남기고, 나머지 8천 행으로 생성기를 학습합니다. 생성기는 합성 자료 1만 행을 만듭니다.

1. 나이와 금액의 분포·상관·불가능 값·중복을 검사합니다.
2. 합성 자료로 학습한 수요 모델과 실제 학습용 자료로 학습한 기준 모델을 준비합니다. 두 모델의 오류를 같은 실제 평가용 자료에서 비교합니다.
3. 원본 train과 holdout에 대한 근접도 차이·민감 속성 노출을 점검하고 집단별 효용 차이를 보고합니다.

**결과·해석:** 그럴듯함·실용성·보호 성질을 다른 증거로 평가합니다.

**전제·주의:** 합성 생성법과 학습 범위·시드·평가 기준을 남겨 재현과 오류 추적이 가능하게 합니다.

### 답안 골격과 혼동 방지

정의·생성 유형 → 생성/분할 흐름 → 충실도·효용·노출 3축 → TSTR 사례 → 목적·제약·한계

- 통계 품질 점수 100%를 개인정보 보호 100%로 해석하지 않습니다.
- 생성기 학습에 실제 시험 holdout을 넣지 않습니다.

### 내용을 가리고 회상

1. 분포가 비슷한데 예측 성능은 낮을 수 있습니까?
2. TSTR의 test에는 어떤 자료를 씁니까?
3. 중복행이 없다는 사실만으로 보호를 보장할 수 있습니까?

### 적용 기준과 근거

평가 축·지표와 VAE 원리는 원 자료 확인. GAN/diffusion 등 생성법 전체의 원 논문 확인과 PET 법/보안 비교는 담당 범위 밖·추가 확인입니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [SDMetrics: Quality](https://docs.sdv.dev/sdmetrics/data-metrics/quality) — DataCebo / SDV developers; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: 통계 유사성·column shapes·pair trends·cardinality와 downstream ROI의 차이. 단일 점수가 실제 모델 효용을 보장하지 않는다는 설명을 확인했습니다.
- [SDMetrics: Privacy](https://docs.sdv.dev/sdmetrics/data-metrics/privacy) — DataCebo / SDV developers; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: disclosure protection, real/synthetic 거리 기반 overfitting·random baseline. 통계 프라이버시 지표가 법적 익명성을 자동 보장한다는 주장은 하지 않습니다.
- [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) — Diederik P. Kingma, Max Welling; 2013 원 논문; 2022-12-10 v11; 확인 2026-11-05. 확인 범위: 실제 열람: 연속 잠재변수·approximate posterior·reparameterization·variational lower bound 요약. ELBO의 재구성/KL 분해는 원 이론을 교육용으로 설명합니다.
- [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) — Ian J. Goodfellow 외; 2014-06-10 v1; 확인 2026-11-05. 확인 범위: 실제 열람: 생성기G·판별기D의 적대적 두 모형 학습·minimax와 gradient 학습. 모든 딥페이크가 GAN이라는 주장의 근거는 아닙니다.

## 연관 기출

- [제140회 3교시 3번](../questions/qnet-140-p3.md#q3) — 합성데이터 개념; 생성 기법; 품질 평가 지표. 대응: 핵심원리; 충족.
- [제138회 4교시 6번](../questions/qnet-138-p4.md#q6) — 합성데이터 기술 비교 중 기술적 성질. 대응: 핵심원리; 부분 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
