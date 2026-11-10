---
id: kubernetes-hpa
title: 쿠버네티스와 HPA·오토스케일링
aliases: []
type: concept
domains:
- 클라우드·인프라
sources:
- id: source-subnote-1cdff7a0931a
- id: source-subnote-cdcbb8339d01
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 쿠버네티스와 HPA·오토스케일링

## 서브노트

### 한눈에 이해

Kubernetes는 워크로드를 지정된 상태로 유지합니다. HPA는 CPU 사용률 같은 지표를 보고 Pod 복제본 수를 조절합니다.

### 정의와 핵심 원리

Kubernetes는 선언적 API와 제어 루프로 컨테이너 워크로드의 배치, 수명, 서비스 발견과 상태 복구를 관리합니다. HPA(Horizontal Pod Autoscaler)는 관측 지표에 따라 Deployment 등의 복제본 수를 늘리거나 줄입니다.

- 제어 평면에서 API 서버는 요청을 받고 etcd는 상태를 저장합니다. 스케줄러는 Pod를 배치할 노드를 고르고, 컨트롤러 관리자는 실제 상태를 목표 상태에 맞추는 컨트롤러를 실행합니다. 각 노드의 kubelet은 Pod 실행을 관리하고, 런타임은 컨테이너를 실행합니다. 네트워크 구현은 서비스 연결을 지원합니다.
- Pod는 배치의 기본 단위입니다. Deployment는 복제본과 배포를 관리하고, Service는 바뀌는 Pod에 안정적으로 접속할 수 있게 합니다. 준비 상태 검사(readiness)는 트래픽을 받을 수 있는지, 활성 상태 검사(liveness)는 재시작이 필요한지 판단합니다.
- HPA 기본식은 ceil(현재 복제본 수 × 현재 지표값 / 목표 지표값)입니다. CPU 사용률은 CPU 요청량(requests) 대비 사용량이므로 요청량 설정이 중요합니다. 실제 조절에는 최소·최대 복제본 수, 지표 누락, 준비되지 않은 Pod, 안정화 시간, 조절 속도 등이 영향을 줍니다. 노드 증설은 별도의 제어 과정입니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| HPA | Pod 복제본 수 조절 | 지표·요청량·안정화 |
| VPA | Pod의 자원 요청량 조절 | 재시작·경합 여부 검토 |
| 노드 확장 | 클러스터의 노드 용량 조절 | 노드 기동 시간·한도·비용 |

<!-- subnote-page:apply -->

### 적용 예제

**HPA 기본식 검산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 현재 Pod 3개가 준비된 상태이며 평균 CPU 사용률은 90%, 목표는 60%, 최대 복제본 수는 10입니다. 기본식을 설명하기 위해 지표 누락과 조절 제한이 없다고 가정합니다.

1. 기본식에 대입하면 ceil(3 × 90 / 60) = ceil(4.5) = 5입니다.
2. 실제 운영에서는 새 Pod가 준비되고 지표가 수집되기까지 시간이 걸립니다. 안정화 설정과 조절 속도를 확인해 복제본 수가 너무 자주 바뀌지 않게 합니다.
3. 노드의 여유 자원이 부족하면 목표가 5개여도 새 Pod가 대기 상태(Pending)에 머물 수 있습니다.
4. 병목이 DB나 외부 API에 있다면 Pod만 늘려 해결할 수 있는지 확인합니다.

**결과·해석:** HPA가 원하는 복제본 수와 실제로 트래픽을 처리할 수 있는 Pod 수를 구분합니다.

**전제·주의:** 기본식을 설명하는 예제입니다. 제품 버전에 따라 달라지는 허용 오차와 안정화 기본값은 공식 문서를 확인합니다.

### 답안 골격과 혼동 방지

구조도 → 구성 요소의 역할 → Pod·Service·Deployment → HPA 계산식 → 안정화와 노드 용량

- Kubernetes가 모든 응용 상태와 데이터를 자동으로 복구한다고 쓰지 않습니다.
- HPA는 Pod당 CPU 요청량 대신 복제본 수를 조절합니다.

### 내용을 가리고 회상

1. 목표 복제본 수(`desiredReplicas`)가 5이면 처리 성능도 곧바로 5배가 됩니까?
2. CPU 사용률로 복제본 수를 조절할 때 CPU 요청량을 왜 설정합니까?
3. 준비 상태 검사와 활성 상태 검사를 나누는 이유는 무엇입니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/) — Kubernetes project; 상시 문서; 확인 2026-11-05. 확인 범위: Control plane·worker 컴포넌트 문서 열람. 특정 버전 API 세부가 아닌 공통 구조.
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) — Kubernetes project; 상시 문서; 확인 2026-11-05. 확인 범위: desiredReplicas 식·metrics·안정화와 자원 request 조건 열람.

## 연관 기출

- [제133회 1교시 12번](../questions/qnet-133-p1.md#q12) — Kubernetes. 대응: 핵심원리/비교표/예제; 충족.
- [제137회 4교시 3번](../questions/qnet-137-p4.md#q3) — 개념·특징; 컴포넌트; HPA. 대응: 핵심원리/비교표/예제; 충족.
- [제131회 1교시 8번](../questions/qnet-131-p1.md#q8) — Auto Scaling. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
