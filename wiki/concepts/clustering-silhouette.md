---
id: clustering-silhouette
title: K-means·DBSCAN과 실루엣 평가
aliases:
- Clustering and Silhouette
type: concept
domains:
- 머신러닝
sources:
- id: source-subnote-3e48badc01c0
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# K-means·DBSCAN과 실루엣 평가

## 서브노트

### 한눈에 이해

비슷한 고객을 묶되 정답 이름이 없는 상황이 군집입니다. 둥근 집단을 평균으로 묶는 방법과 밀집된 연결 영역을 찾는 방법은 모양과 잡음에 다르게 반응합니다.

### 정의와 핵심 원리

군집은 특징의 유사성·거리·밀도를 기준으로 라벨 없는 자료를 묶는 비지도 학습이며 실루엣은 군집 내부 응집과 외부 분리를 비교하는 지표입니다.

- K-means는 K개 중심을 초기화→가까운 중심 할당→군집 평균으로 중심 갱신을 반복하여 Σ||x_i−μ_cluster||²를 줄입니다. K·초기화·scale·이상치에 민감하고 구형/볼록 군집에 적합하며 국소해에 머물 수 있습니다. 중심이 실제 표본일 필요는 없습니다.
- DBSCAN은 eps 이웃과 min_samples로 core를 정하고 density-connected core와 border를 확장하며 멀리 떨어진 점을 noise로 둡니다. K를 미리 정하지 않고 임의 모양을 찾을 수 있지만 밀도 차이·고차원 거리·eps 선택에 민감합니다. min_samples에 자기 자신을 포함하는지 구현 정의를 확인합니다.
- 점 i의 a는 같은 군집에 속한 다른 점들과의 평균 거리입니다. 다른 군집마다 그 안의 점들과 평균 거리를 구한 뒤, 가장 작은 값을 b로 씁니다. 실루엣은 s=(b−a)/max(a,b)이고 −1~1 범위입니다. 0에 가까우면 경계에 있을 수 있고, 음수라면 다른 군집의 점들이 평균적으로 더 가깝습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| K-means | K·중심·제곱거리 최소화 | 구형 군집·빠른 반복 |
| DBSCAN | eps·min_samples·core/border/noise | 불규칙 모양·가변 밀도 주의 |
| Silhouette | (b−a)/max(a,b) | 거리·scale·모양 영향 |

<!-- subnote-page:apply -->

### 적용 예제

**실루엣 계산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 한 고객의 같은 군집 평균 거리 a=2, 가장 가까운 다른 군집 평균 거리 b=5입니다.

1. s=(5−2)/max(2,5)=3/5=0.6입니다.
2. a=5,b=2라면 s=−0.6으로 현재 군집보다 다른 군집이 가까운지 점검합니다.
3. K 후보별 평균 실루엣과 군집 규모·업무 의미·안정성을 함께 비교합니다.

**결과·해석:** 실루엣으로 군집 내부의 가까움과 다른 군집과의 거리 차이를 비교합니다. 비정형 군집은 평균 실루엣만으로 적합성을 판단하기 어렵습니다.

**전제·주의:** 서로 다른 거리 척도로 산출한 점수를 곧바로 같은 기준으로 비교하지 않습니다.

### 답안 골격과 혼동 방지

군집 정의 → K-means 흐름·장단점 → DBSCAN 구성·장단점 → 실루엣 식·계산 → 목적·scale·밀도 고려

- 군집 번호를 정답 클래스 이름으로 오인하지 않습니다.
- b를 가장 가까운 단일 점의 거리로 계산하지 않습니다.

### 내용을 가리고 회상

1. K-means 중심과 실제 표본은 반드시 같습니까?
2. DBSCAN core와 border는 어떻게 다릅니까?
3. a=2,b=5의 실루엣은 얼마입니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [scikit-learn: Clustering](https://scikit-learn.org/stable/modules/clustering.html) — scikit-learn developers; 1.9.1 표시; 확인 2026-11-05. 확인 범위: 실제 열람: k-means inertia/centroid, DBSCAN eps/min_samples/core/border/noise, silhouette s=(b−a)/max(a,b). 평균 silhouette의 볼록 군집 선호 한계를 확인했습니다.

## 연관 기출

- [제129회 1교시 5번](../questions/qnet-129-p1.md#q5) — K-means·DBSCAN 개념·구성·장단점. 대응: 핵심원리; 충족.
- [제130회 2교시 1번](../questions/qnet-130-p2.md#q1) — K-means; DBSCAN. 대응: 핵심원리; 충족.
- [제135회 1교시 6번](../questions/qnet-135-p1.md#q6) — 실루엣 계수. 대응: 핵심원리; 충족.
- [제139회 4교시 1번](../questions/qnet-139-p4.md#q1) — 클러스터링. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
