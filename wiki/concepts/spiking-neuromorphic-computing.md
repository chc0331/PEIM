---
id: spiking-neuromorphic-computing
title: SNN과 뉴로모픽 칩
aliases:
- SNN
- Spiking Neural Network
type: concept
domains:
- 딥러닝
sources:
- id: source-subnote-723fed8ac983
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
related_terms:
- Neuromorphic Chip
---

# SNN과 뉴로모픽 칩

## 서브노트

### 한눈에 이해

일반 신경망이 매 단계 많은 실수를 계산한다면 SNN은 뉴런의 상태가 임계값을 넘을 때 사건을 보냅니다. 움직임이 드문 센서 환경에서는 실제 변화가 있을 때만 계산·통신하는 방식이 유리할 수 있습니다.

### 정의와 핵심 원리

SNN은 시간에 따른 뉴런 상태와 spike 사건으로 정보를 표현·처리하는 신경망이며 뉴로모픽 칩은 이런 계산과 메모리·통신을 뇌의 일부 원리에서 착안해 구현한 하드웨어입니다.

- 대표 LIF 뉴런은 입력을 막전위에 누적하고 시간에 따라 누출시키며 임계값을 넘으면 spike를 내고 reset합니다. spike의 횟수·시각·순서 등 부호화 방식에 따라 정보 표현이 달라집니다. 단순히 ANN 실수를0/1로 바꾸는 것만으로 시간 동역학을 설명할 수 없습니다.
- 뉴로모픽 구현은 neuron/synapse의 지역 상태·메모리, 희소 이벤트 통신, 비동기 처리와 병렬 코어를 활용합니다. Loihi2는 programmable neuron과 graded spike를 지원하는 예입니다. 모든 뉴로모픽 칩이 동일 학습 규칙·정밀도·아날로그 회로인 것은 아닙니다.
- 학습은 국소 STDP 계열·surrogate gradient·ANN-to-SNN 변환 등 접근이 있고 전력·지연은 활동도·시간단계·센서·변환 비용에 따라 달라집니다. 비미분 spike·학습 도구·매핑 제약·고밀도 활성에서의 이득 축소가 한계입니다. event camera·저전력 로봇·신호 탐지가 적용 예이지 모든 DL 대체의 증거는 아닙니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| ANN | 연속 활성·대량 tensor 계산 | GPU 생태계·표현 학습 |
| SNN | 시간 상태·spike 사건 | 희소 시간 신호·학습 난점 |
| 뉴로모픽 칩 | 지역 메모리·event 통신 | 알고리즘/하드웨어 공동 설계 |

<!-- subnote-page:apply -->

### 적용 예제

**누출 뉴런의 발화**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 교육용 이산식 V_t=0.5V_(t−1)+I_t, 임계1, 발화 후0으로 reset합니다.

1. V0=0, 입력0.6이면 V1=0.6으로 발화하지 않습니다.
2. 다음 입력0.8이면 V2=0.5×0.6+0.8=1.1로 임계값을 넘어 spike를 냅니다.
3. reset 후 입력이 없으면 발화가 멈춥니다. 실제 칩의 방정식·정밀도·지연은 구현마다 확인합니다.

**결과·해석:** 시간 누적·누출·임계·사건 출력의 연결을 보여 줍니다.

**전제·주의:** 발화율이 높거나 변환 비용이 크면 희소성의 전력 이득이 줄 수 있습니다.

### 답안 골격과 혼동 방지

SNN·칩 구분 → LIF 시간 동작 → 코어·시냅스·이벤트 구조 → ANN 비교·학습 → 전력 측정 조건·한계

- SNN은 모든 상황에서 무조건 저전력이라는 주장을 피합니다.
- 뉴로모픽을 모든 신경망 가속기와 같은 뜻으로 쓰지 않습니다.

### 내용을 가리고 회상

1. 누출·누적·임계·reset을 순서로 설명할 수 있습니까?
2. SNN 모델과 뉴로모픽 칩은 어떻게 다릅니까?
3. 어떤 workload에서 이벤트 희소성이 이득을 줍니까?

### 적용 기준과 근거

Loihi2 구조·event/LIF 예시는 Intel 원 자료 확인. STDP/surrogate/변환 세부 학습 알고리즘의 개별 원문 검증은 보완 범위입니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Taking Neuromorphic Computing to the Next Level with Loihi 2](https://download.intel.com/newsroom/2021/new-technologies/neuromorphic-computing-loihi-2-brief.pdf) — Intel Labs; 2021 기술 브리프; 확인 2026-11-05. 확인 범위: 실제 열람: PDF p.5~7 비동기 neuron core·synapse memory·spike communication·programmable neuron/LIF. 보고된 배속을 일반 SNN 우위로 옮기지 않습니다.

## 연관 기출

- [제126회 1교시 4번](../questions/qnet-126-p1.md#q4) — SNN. 대응: 핵심원리; 충족.
- [제128회 1교시 9번](../questions/qnet-128-p1.md#q9) — 뉴로모픽 칩. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
