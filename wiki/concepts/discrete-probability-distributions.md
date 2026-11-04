---
id: discrete-probability-distributions
title: 베르누이·기하·이항·포아송 분포
aliases:
- Discrete Probability Distributions
type: concept
domains:
- 통계
sources:
- id: source-subnote-be97d5e93fff
- id: source-subnote-640dbf49e9de
- id: source-subnote-ae8fbc899461
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 베르누이·기하·이항·포아송 분포

## 서브노트

### 한눈에 이해

한 번의 성공 여부, 처음 성공까지 기다린 횟수, 정해진 횟수 중 성공 수, 일정 시간의 사건 수는 모두 세는 값이지만 서로 다른 질문입니다. 무엇을 세는지부터 정하면 분포를 고를 수 있습니다.

### 정의와 핵심 원리

이산분포는 셀 수 있는 값에 확률질량을 부여하며 시행 수·독립성·성공확률·사건률 등 생성 조건에 따라 형태가 달라집니다.

- Bernoulli(p)는 X∈{0,1}, P(X=x)=p^x(1−p)^(1−x), 평균 p·분산 p(1−p)입니다. 독립·동일 p 시행에서 첫 성공의 시행번호 G는 P(G=k)=(1−p)^(k−1)p, k≥1, 평균1/p·분산(1−p)/p²이며 무기억성을 가집니다.
- Binomial(n,p)은 고정 n번 독립 Bernoulli의 성공 수로 P(X=k)=C(n,k)p^k(1−p)^(n−k), 평균np·분산np(1−p)입니다. Geometric은 n을 고정하는 대신 첫 성공에서 멈춥니다. 첫 성공 전 실패 수를 정의하면 지원집합과 평균이 1만큼 달라집니다.
- Poisson(λ)은 일정 구간의 사건 수로 P(X=k)=e^(−λ)λ^k/k!, 평균=분산=λ입니다. 독립 도착·고정 사건률 같은 가정의 적합성을 확인합니다. 큰 n·작은 p·np=λ에서 이항을 포아송으로 근사할 수 있지만 과산포·군집 도착이면 다른 모델을 검토합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Bernoulli·Geometric | 한 번 성공 여부/첫 성공 시행번호 | 0·1/1 이상 정수 |
| Binomial | 고정 n번 중 성공 수 | 0~n, 평균np |
| Poisson | 시간·공간 구간의 사건 수 | 0 이상, 평균=분산λ |

<!-- subnote-page:apply -->

### 적용 예제

**각 분포의 질문 구분**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 성공확률 p=0.2이고 시간당 사건률 λ=2라고 각각 가정합니다.

1. 첫 성공이 3번째일 확률은 0.8²×0.2=0.128입니다.
2. 5번 중 정확히 1번 성공할 확률은 C(5,1)×0.2×0.8⁴=0.4096입니다.
3. 시간당 사건이 0건일 확률은 e^(−2)≈0.1353입니다. 이 λ는 앞의 p와 별도 상황의 모수입니다.

**결과·해석:** 같은 성공/사건이라는 단어도 표본공간과 중단 조건이 다르면 계산식이 달라집니다.

**전제·주의:** 포아송률이 시간당이면 30분의 λ는 1로 단위를 맞춥니다.

### 답안 골격과 혼동 방지

세는 대상 정의 → PMF·지원집합·평균/분산 → 고정 n/중단 시점 비교 → 수치 예시 → 독립·고정률·근사 조건

- 기하분포의 실패 횟수/시행번호 정의를 섞지 않습니다.
- 모든 드문 사건이 포아송을 따른다고 단정하지 않습니다.

### 내용을 가리고 회상

1. 이항과 기하의 종료 조건은 무엇입니까?
2. 기하분포 평균이 1/p 또는 (1−p)/p인 이유는 무엇입니까?
3. 포아송의 λ에서 시간 단위를 어떻게 바꿉니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Introductory Statistics 2e, 4.4 Geometric Distribution](https://openstax.org/books/introductory-statistics-2e/pages/4-4-geometric-distribution) — OpenStax / Rice University; Introductory Statistics 2e; 확인 2026-11-05. 확인 범위: 실제 열람: Bernoulli 반복·독립·고정 p·첫 성공 시행번호와 실패 횟수의 두 정의·무기억성. 지원집합 차이를 명시합니다.
- [NIST/SEMATECH e-Handbook: Binomial Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm) — NIST / SEMATECH; 웹판 날짜 미표시; 확인 2026-11-05. 확인 범위: 실제 열람: PMF, 고정 n/p, np·np(1-p), 최우추정 p=x/n. 가상 숫자는 독립 시행 가정입니다.
- [NIST/SEMATECH e-Handbook: Poisson Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm) — NIST / SEMATECH; 웹판 날짜 미표시; 확인 2026-11-05. 확인 범위: 실제 열람: 구간 사건 횟수·PMF·평균과 분산 λ. 균일률·독립 도착 가정을 무조건 현실에 부여하지 않습니다.

## 연관 기출

- [제130회 1교시 12번](../questions/qnet-130-p1.md#q12) — 베르누이·기하 분포. 대응: 핵심원리; 충족.
- [제135회 4교시 3번](../questions/qnet-135-p4.md#q3) — 이항·포아송 분포 비교. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
