---
id: support-vector-machine
title: SVM의 최대 마진과 hard/soft margin
aliases:
- SVM
- Support Vector Machine
type: concept
domains:
- 머신러닝
sources:
- id: source-subnote-a3bde06f6255
- path: raw/corrections/2026-11-05-subnotes-review.md
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# SVM의 최대 마진과 hard/soft margin

## 서브노트

### 한눈에 이해

두 집단 사이를 가르는 선을 여러 개 그을 수 있다면 가장 가까운 표본과의 여유 폭이 큰 선을 고릅니다. 완벽히 분리되지 않으면 일부 위반을 허용하면서 여유와 오류의 균형을 정합니다.

### 정의와 핵심 원리

결정경계와 가까운 support vector를 중심으로 마진을 최대화하는 분류·회귀 방법이며 선형 SVM은 초평면 wᵀx+b=0을 사용합니다.

- y_i∈{−1,+1}일 때 hard margin은 y_i(wᵀx_i+b)≥1을 모두 만족하며 1/2||w||²를 최소화합니다. 경계면 간 마진 폭은 2/||w||입니다. 완전 선형 분리가 필요하여 이상치 한 점에도 불가능하거나 경계가 크게 흔들릴 수 있습니다.
- Soft margin은 slack ξ_i≥0와 y_i(wᵀx_i+b)≥1−ξ_i, 목적함수 1/2||w||²+CΣξ_i를 사용합니다. C가 크면 위반 비용이 커지고 작으면 규제가 강해집니다. 마진 내부이지만 정분류인 점과 오분류인 점을 slack 크기로 구별합니다.
- 비선형에서는 kernel로 특징 공간의 내적을 계산할 수 있습니다. RBF의 γ와 C를 검증으로 정하고 특징 scale·클래스 불균형·자료 수·확률 보정 요구를 고려합니다. SVM 점수는 자동으로 보정된 확률이 아니며 큰 표본의 kernel SVM은 학습 자원 부담이 커질 수 있습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Hard margin | 위반 없는 최대 마진 | 완전 분리·잡음 적은 경우 |
| Soft margin | slack·C로 위반 허용 | 겹침·잡음에 대응 |
| Kernel SVM | 고차원 내적을 kernel로 계산 | scale·C·γ·자원 검증 |

<!-- subnote-page:apply -->

### 적용 예제

**1차원 분리 경계**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 음성 x=−2,−1, 양성 x=1,2로 두고 w=1,b=0입니다.

1. 가까운 x=−1,+1에서 y(wx+b)=1이므로 support vector입니다.
2. 경계는 x=0, 두 마진선은 x=−1,+1이고 폭은2/|w|=2입니다.
3. x=1.5인 음성 잡음이 추가되면 양성 x=1과 x=2 사이에 음성이 놓여 1차원 선형 hard-margin 분리가 불가능하므로 soft margin의 위반 비용을 검토합니다.

**결과·해석:** 결정경계·마진선·support vector와 slack의 의미를 같은 그림으로 설명할 수 있습니다.

**전제·주의:** 위 예시의 최적 경계는 가정한 자료와 선형 모형에 한정합니다.

### 답안 골격과 혼동 방지

정의·초평면 도식 → hard 목적·제약 → soft 식·C/slack → kernel·전처리 → 적용·한계

- C를 정규화 강도와 같은 방향으로 설명하지 않습니다.
- support vector를 데이터 전체의 평균이라고 쓰지 않습니다.

### 내용을 가리고 회상

1. 마진 폭 2/||w||가 나오는 두 경계식은 무엇입니까?
2. C가 커지면 어떤 오류를 더 엄격히 벌합니까?
3. kernel 사용 전 특징 scale을 맞추는 이유는 무엇입니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [scikit-learn: Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html) — scikit-learn developers; 1.9.1 표시; 확인 2026-11-05. 확인 범위: 실제 열람: 초평면·support vectors·soft-margin primal formulation·C·kernel. hard-margin은 slack을 허용하지 않는 제한형으로 설명합니다.

## 연관 기출

- [제127회 1교시 10번](../questions/qnet-127-p1.md#q10) — SVM. 대응: 핵심원리; 충족.
- [제130회 2교시 1번](../questions/qnet-130-p2.md#q1) — SVM. 대응: 핵심원리; 충족.
- [제132회 2교시 2번](../questions/qnet-132-p2.md#q2) — 선형 SVM의 마진 분류 2가지. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
