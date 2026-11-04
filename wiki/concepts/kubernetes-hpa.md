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

컨테이너가 원하는 개수와 상태로 계속 실행되도록 제어하고, 관측한 부하에 따라 복제본 수를 조절합니다.

### 정의와 핵심 원리

Kubernetes는 컨테이너화워크로드의 배치·수명·서비스발견·상태회복을선언적API와 제어루프로관리합니다. HPA는 메트릭에따라 Deployment등대상의 복제본수를조절하는수평확장기능입니다.

- 제어평면의APIserver는 요청창구, etcd는 상태 저장, scheduler는Pod배치, controller-manager는 원하는상태와 실제 상태를 조정합니다. 노드의 kubelet은Pod 실행을 관리하고 런타임은컨테이너를실행하며 네트워크 구현은 서비스 연결을 지원합니다.
- Pod는 배치기본 단위이고 Deployment는 복제·배포를 관리하며 Service는 변동하는Pod에 안정적인접점을제공합니다. readiness는 트래픽수용, liveness는 재시작판단과관련되므로임의로같은 검사로 구성하지 않습니다.
- HPA 기본식은ceil(현재 복제본×현재 메트릭/목표메트릭)입니다. CPU이 용률은request대비값이 므로request설정이 중요합니다. min/max·측정누락·미준비Pod·안정화시간·확장속도·노드수 용량을 반영해야합니다. Pod확장과노드확장은다른 제어루프입니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| HPA | Pod수증감 | 메트릭·request·안정화 |
| VPA | Pod 자원 요구조절 | 재시작·경합검토 |
| 노드확장 | 노드 용량증감 | 기동지연·한도·비용 |

<!-- subnote-page:apply -->

### 적용 예제

**HPA 기본식 검산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 현재3Pod, 평균CPU이 용률90%, 목표60%, 최대10

1. 기본식은ceil(3×90/60)=ceil4.5=5입니다.
2. 새Pod의 준비완료와메트릭수집을 기다리며과도한반복증감을막습니다.
3. 현재 노드 여유가 부족하면 5개를원해도Pending이 될수 있습니다.
4. DB·외부 API 병목은 Pod수확장만으로해결되지않는지확인합니다.

**결과·해석:** 요청 복제본5와 실제 서비스 용량의 차이를구분합니다.

**전제·주의:** 수식은기본 원리이며 제품 버전별기본허용오차·안정화값을 고정된보장으로쓰지않습니다.

### 답안 골격과 혼동 방지

구조도 → 컴포넌트역할 → Pod·Service·Deployment → HPA수식 → 안정성·용량

- Kubernetes가 모든 응용 상태·데이터를 자동복구한다고쓰지않습니다.
- HPA를 CPU크기변경이라 하지 않습니다.

### 내용을 가리고 회상

1. desiredReplicas5가 즉시5배성능을 뜻합니까?
2. CPUrequest를 왜설정합니까?
3. readiness와liveness를 분리하는이유는무엇입니까?

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
