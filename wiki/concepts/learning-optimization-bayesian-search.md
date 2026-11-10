---
id: learning-optimization-bayesian-search
title: 학습 최적화와 베이지안 탐색
aliases:
- Learning Optimization and Bayesian Optimization
type: concept
domains:
- 머신러닝
sources:
- id: source-subnote-658572757207
- id: source-subnote-203675e9a4bb
- id: source-subnote-e2dd8c44bacd
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 학습 최적화와 베이지안 탐색

## 서브노트

### 한눈에 이해

모델 내부 가중치를 조금씩 바꾸는 일과 학습률·모델 크기 같은 설정을 바깥에서 고르는 일은 다릅니다. 전자는 손실의 기울기를, 후자는 비싼 실험을 몇 번 할지와 어디서 할지를 다룹니다.

### 정의와 핵심 원리

학습 최적화는 손실을 줄일 파라미터를 찾고 베이지안 최적화는 대리모형과 획득함수로 다음 비싼 목적함수 평가 위치를 고르는 방법입니다.

- 기울기 갱신은 θ←θ−η∇L입니다. Batch GD는 전체 자료로 안정적이나 비싸고 SGD는 한 표본으로 빠르나 흔들리며 mini-batch는 처리 병렬성과 잡음의 절충입니다. 학습률이 크면 발산·작으면 느림, 특징 scale·비볼록성·saddle point 등을 고려합니다.
- Momentum은 이전 이동을 누적해 진동을 줄이고 AdaGrad는 누적 제곱 gradient로 좌표별 스텝을 조정하나 지나치게 작아질 수 있습니다. RMSProp은 이동평균, Adam은 1·2차 모멘트와 bias correction을 조합합니다. AdamW는 adaptive update와 weight decay를 분리하며 Adam이 언제나 일반화 우수한 것은 아닙니다.
- 베이지안 최적화는 몇 차례 실험한 결과로 설정과 성능의 관계를 대리모형(surrogate)에 학습시킵니다. 획득함수(acquisition function)는 성능이 좋을 것으로 예상되는 곳과 아직 잘 모르는 곳 중 다음 실험의 가치를 비교합니다. 실제로 검증 점수를 측정해 모형을 갱신합니다. 시험 자료는 반복 탐색에 쓰지 않습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| GD·SGD·mini-batch | gradient 산출 자료량 차이 | 속도·메모리·잡음 절충 |
| Momentum·AdamW | 관성·적응 스텝·분리 감쇠 | 학습률·일반화 검증 |
| Bayesian optimization | surrogate+acquisition | 비싼 hyperparameter 탐색 |

<!-- subnote-page:apply -->

### 적용 예제

**경사 한 단계와 설정 탐색**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** L(w)=(w−3)², w=0, η=0.1입니다.

1. gradient=2(w−3)=−6이므로 w_new=0−0.1×(−6)=0.6입니다.
2. 손실은 9에서 (0.6−3)²=5.76으로 줄어듭니다.
3. 학습률 η를 바꿀 때마다 학습부터 검증까지 다시 하면 비용이 큽니다. 베이지안 최적화는 앞선 실험 결과와 모형의 불확실성을 보고 다음 η 후보를 고릅니다.

**결과·해석:** gradient 계산과 hyperparameter 실험의 목적·정보를 구분할 수 있습니다.

**전제·주의:** BO의 surrogate 평균이 실제 성능의 보장값은 아니며 새 실험으로 확인해야 합니다.

### 답안 골격과 혼동 방지

학습/설정 최적화 구분 → GD 계열 장단점 → 적응·관성 optimizer → BO 순환·탐험/활용 → 검증·비용 한계

- 역전파 자체를 가중치 갱신 알고리즘과 동일시하지 않습니다.
- Adam의 L2와 AdamW의 decay를 항상 같다고 쓰지 않습니다.

### 내용을 가리고 회상

1. mini-batch가 SGD와 batch의 무엇을 절충합니까?
2. BO에서 surrogate와 acquisition은 각각 어떤 역할입니까?
3. 학습률 0.1의 한 단계 결과 0.6을 재계산할 수 있습니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Deep Learning, Chapter 6: Deep Feedforward Networks](https://www.deeplearningbook.org/contents/mlp.html) — Ian Goodfellow, Yoshua Bengio, Aaron Courville; 2016 공개 교재; 확인 2026-11-05. 확인 범위: 실제 열람: 순전파 함수 합성·MLP·chain rule 기반 역전파·활성화·역전파와 최적화 분리. 수치 예제는 1개 선형 뉴런의 강사 계산입니다.
- [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101) — Ilya Loshchilov, Frank Hutter; 2019-01-04 v3, ICLR 2019; 확인 2026-11-05. 확인 범위: 실제 열람: 초록의 SGD와 adaptive Adam에서 L2/weight decay 비동등·AdamW 분리. 모든 작업에서 Adam이 SGD보다 우수하다는 주장은 하지 않습니다.
- [Practical Bayesian Optimization of Machine Learning Algorithms](https://arxiv.org/abs/1206.2944) — Jasper Snoek, Hugo Larochelle, Ryan P. Adams; 2012-08-29 v2; 확인 2026-11-05. 확인 범위: 실제 열람: 저자 원 논문 초록·GP surrogate·과거 실험에 근거한 다음 hyperparameter 선택·비용 고려. 세부 성능 비교는 재현하지 않았습니다.

## 연관 기출

- [제130회 1교시 9번](../questions/qnet-130-p1.md#q9) — 최적화 알고리즘 유형·장단점. 대응: 핵심원리; 충족.
- [제132회 1교시 3번](../questions/qnet-132-p1.md#q3) — 베이지안 최적화. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
