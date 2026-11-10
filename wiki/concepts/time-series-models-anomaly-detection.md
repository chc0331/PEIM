---
id: time-series-models-anomaly-detection
title: AR·MA·시계열 딥러닝과 실시간 이상 탐지
aliases:
- Time Series Models and Anomaly Detection
type: concept
domains:
- 머신러닝
sources:
- id: source-subnote-f9a4e44c6dbd
- id: source-subnote-e908f754eade
- id: source-subnote-658572757207
- id: source-subnote-3862adf089ef
- id: source-subnote-1f79f995685a
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# AR·MA·시계열 딥러닝과 실시간 이상 탐지

## 서브노트

### 한눈에 이해

오늘 전력 수요는 어제 같은 시각의 수요, 기온, 휴일 여부와 관련될 수 있습니다. 예측 모델을 검증할 때는 미래 기록이 학습에 섞이지 않도록 시간을 기준으로 나눕니다. 실시간 이상 탐지는 새 관측값이 정상 예측에서 얼마나 벗어나는지 확인합니다.

### 정의와 핵심 원리

시계열 모형은 시간 의존·추세·계절성 등을 모델링하며 이상 탐지는 단일 시점·맥락·구간의 비정상 변화를 적은 지연으로 식별합니다.

- AR(p)는 y_t=c+Σφ_i y_(t−i)+ε_t처럼 과거 관측값을 씁니다. MA(q)는 y_t=μ+ε_t+Σθ_i ε_(t−i)처럼 현재와 과거의 충격(innovation)을 씁니다. MA 모형의 이동 평균은 최근 관측값을 산술 평균하는 평활법과 다릅니다.
- 시계열 딥러닝은 lag window의 다변량 패턴을 RNN/LSTM·TCN·attention 등으로 학습해 다음 값/여러 시점 또는 입력 재구성을 예측합니다. 학습/검증/시험을 시간 순으로 나누고 학습 구간에서만 스케일러를 맞추며 미래 기상 확정값 같은 누출을 막습니다.
- 실시간 탐지는 수집→시간 정렬/누락 처리→sliding window→예측/재구성 오차→적응 임계값·연속성 확인→경보/조치입니다. point/contextual/collective 이상과 drift를 구분하고 처리량·event time 지연·늦은 도착·오탐 비용을 함께 관리합니다. 모델 점수 하나가 장애 원인까지 알려 주지는 않습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| AR | 과거 y의 선형 조합 | 지속성·자기상관 |
| MA | 과거 예측 충격의 조합 | 오차 전파·단순 평활과 다름 |
| 딥러닝 탐지 | 비선형 예측·재구성 잔차 | window·누출·지연·drift |

<!-- subnote-page:apply -->

### 적용 예제

**AR 예측 잔차 경보**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** AR(1) 모형은 y_t=0.8y_(t−1)+ε_t입니다. 직전 수요는 100, 새 관측은 150입니다.

1. 조건부 예측값은 80이고 잔차는 150−80=70입니다.
2. 정상 구간의 잔차 평균이 0이고 표준편차가 10이라면, 표준화한 잔차는 (70−0)/10=7입니다.
3. 가동 상태/기온·센서 오류를 확인하고 3회 연속 등 경보 규칙을 적용합니다. 실제 임계값은 검증 자료와 비용으로 정합니다.

**결과·해석:** 잔차70은 기대 대비 이탈을 나타내며 곧바로 특정 고장을 증명하지는 않습니다.

**전제·주의:** 학습 구간의 미래 값을 window 안에 넣거나 test 전체로 스케일링하지 않습니다.

### 답안 골격과 혼동 방지

AR·MA 정의와 식 → 비교·정상성 → 딥러닝 window → 실시간 탐지 구조 → 유형·지연·drift·평가

- MA(q)를 관측값 q개 산술 평균으로 쓰지 않습니다.
- 시계열을 임의 섞기만 한 검증으로 운영 성능을 과장하지 않습니다.

### 내용을 가리고 회상

1. AR과 MA의 설명변수는 각각 무엇입니까?
2. 예측 오차와 reconstruction 오차를 어떻게 쓰겠습니까?
3. 온라인 임계값 조정 시 어떤 과거 정보를 사용할 수 있습니까?

### 적용 기준과 근거

AR/MA·lag window·시간순 분할·convolutional autoencoder의 재구성 탐지를 실제 확인했습니다. LSTM/TCN 전체 구조와 실시간 운영 설계는 추가 확인 범위입니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Forecasting: Principles and Practice, ARIMA models](https://otexts.com/fpp3/arima.html) — Rob J. Hyndman, George Athanasopoulos / Monash University·OTexts; 3판 온라인 공개 교재; 확인 2026-11-05. 확인 범위: 실제 열람: AR(p) 과거 y, MA(q) 과거 innovation, stationarity/differencing·ACF/PACF. 딥러닝/실시간 탐지의 전 범위를 이 출처 하나로 검증하지 않습니다.
- [scikit-learn: Novelty and Outlier Detection](https://scikit-learn.org/stable/modules/outlier_detection.html) — scikit-learn developers; 1.9.1 표시; 확인 2026-11-05. 확인 범위: 실제 열람: 오염 학습 표본의 outlier vs clean train의 novelty, IsolationForest의 무작위 분리와 LOF. 전역/맥락/집단 이상 구분은 시계열 예제에서 강사 분석으로 제시합니다.
- [Deep Learning, Chapter 6: Deep Feedforward Networks](https://www.deeplearningbook.org/contents/mlp.html) — Ian Goodfellow, Yoshua Bengio, Aaron Courville; 2016 공개 교재; 확인 2026-11-05. 확인 범위: 실제 열람: 순전파 함수 합성·MLP·chain rule 기반 역전파·활성화·역전파와 최적화 분리. 수치 예제는 1개 선형 뉴런의 강사 계산입니다.
- [Dive into Deep Learning, Working with Sequences](https://d2l.ai/chapter_recurrent-neural-networks/sequence.html) — Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola; 1.0.3 온라인 공개 교재; 확인 2026-11-05. 확인 범위: 실제 열람: 고정 lag window·latent state·autoregressive 조건부 확률, 시간순 학습·미래 자료 사용 금지. 전체 DL 시계열 구조의 성능을 검증한 자료는 아닙니다.
- [Timeseries anomaly detection using an Autoencoder](https://keras.io/examples/timeseries/timeseries_anomaly_detection/) — pavithrasv / Keras examples; 2020-05-31 생성·수정 표시; 확인 2026-11-05. 확인 범위: 실제 열람: convolutional autoencoder·window sequence·재구성 MAE로 이상 점수/임계값 구성. 최대 학습 MAE 임계는 튜토리얼 예시이며 보편 최적 임계가 아닙니다.

## 연관 기출

- [제138회 1교시 7번](../questions/qnet-138-p1.md#q7) — AR·MA 모형. 대응: 핵심원리; 충족.
- [제139회 4교시 5번](../questions/qnet-139-p4.md#q5) — 시계열 딥러닝. 대응: 핵심원리; 충족.
- [제140회 4교시 4번](../questions/qnet-140-p4.md#q4) — 시계열 이상 유형; 탐지 방식; 딥러닝 탐지 기법. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
