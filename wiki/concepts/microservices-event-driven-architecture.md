---
id: microservices-event-driven-architecture
title: MSA·서비스 메시·이벤트 아키텍처
aliases: []
type: concept
domains:
- 소프트웨어공학
sources:
- id: source-subnote-d3ce8459ec4b
- id: source-subnote-85904d98dcbb
- id: source-subnote-5f044abea53f
- id: source-subnote-69fdbdc50a28
- id: source-subnote-7849de084f0e
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# MSA·서비스 메시·이벤트 아키텍처

## 서브노트

### 한눈에 이해

서비스를 독립적으로 배포하면 변경 범위를 줄일 수 있습니다. 이벤트로 연결하면 보내는 쪽이 받는 쪽의 처리를 기다릴 필요가 줄어듭니다.

### 정의와 핵심 원리

MSA는 업무 능력 중심의 독립 배포 가능한 서비스와 명확한 계약으로 시스템을 구성합니다. 서비스 메시는 서비스 간 통신 정책을 데이터·제어 평면으로 다루며, EDA는 상태 변화를 이벤트로 발행하여 소비자가 반응하는 구조입니다.

- MSA에서는 경계가 분명한 업무 책임, 독립 배포·자동화, 서비스 소유 데이터, 장애 격리, 관측가능성을 설계합니다. 모놀리스는 단일 배포와 로컬 호출·트랜잭션이 단순하지만 서비스 분리는 네트워크 지연, 분산 일관성, 운영 복잡도를 늘립니다.
- 서비스 메시는 프록시 기반 또는 다른 데이터평면 구현으로 라우팅·재시도·타임아웃·상호인증·계측을 제공하고 제어평면이 정책을 배포합니다. 업무 코드를 대체하거나 분산 트랜잭션 문제를 자동 해결하지 않습니다.
- 중재자 토폴로지는 초기 이벤트를 중앙 중재자가 해석해 단계·순서를 조정합니다. 복잡한 업무 흐름과 추적은 명확하지만 중재자에 지식과 장애 영향이 집중될 수 있습니다.
- 브로커 토폴로지는 발행 이벤트를 중개하고 소비자가 독립 반응합니다. 확장·변경 격리에 유리하나 전체 흐름 추적·재처리·보상·순서·중복을 명시해야 합니다. 적어도 한 번 전달에서는 소비자의 멱등 처리가 특히 중요합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·판단 |
| --- | --- | --- |
| 모놀리스 | 한 배포·로컬 일관성 | 규모가 작을 때 운영 단순 |
| MSA | 독립 배포·서비스 소유권 | 조직과 자동화 역량 필요 |
| 중재자/브로커 | 중앙 업무 조정 / 분산 반응 | 업무 가시성 / 느슨한 결합의 절충 |

<!-- subnote-page:apply -->

### 적용 예제

**강사 창작 적용 예시: 주문 후 배송 준비**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 주문서비스가 OrderPlaced를 발행합니다.

1. 중재자 방식은 결제→재고→배송을 오케스트레이터가 지시합니다.
2. 브로커 방식은 결제·재고 소비자가 이벤트에 반응하고 실패 이벤트에 보상합니다.
3. 주문 ID로 중복 처리를 막고 메시의 타임아웃·계측 정책을 설정합니다.

**결과·해석:** 각 토폴로지의 제어 위치와 실패 처리 차이가 드러납니다.

**전제·주의:** 서비스 수를 늘리는 것이 목표가 아니며 단일 DB 공유는 독립성을 약화할 수 있습니다.

### 답안 골격과 혼동 방지

MSA 특징·원칙·모놀리스 비교 → 메시의 두 평면과 기능 → EDA 두 토폴로지 구성·실패 사례

- 메시와 메시지 브로커는 다른 개념입니다.
- 이벤트 전달 성공과 업무 트랜잭션 성공을 구분합니다.

### 내용을 가리고 회상

1. MSA의 독립 배포를 깨뜨리는 설계를 하나 드십시오.
2. 중재자와 브로커의 업무 지식은 어디에 있습니까?
3. 재시도에는 왜 멱등성이 필요합니까?

### 적용 기준과 근거

Azure의 MSA·EDA 문서, Istio 공식 문서, SWEBOK에서 구조 원리를 확인했습니다. 확인한 Istio 문서에는 sidecar와 ambient 두 모드가 나옵니다. 기출에서 요구한 broker·mediator 분류의 원출전 전체는 확인이 필요합니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Guide to the SWEBOK v4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf) — IEEE Computer Society / Hironori Washizaki 편; 2026-08; 확인 2026-11-05. 확인 범위: 공개 PDF 열람. 요구사항·설계·테스트·유지보수·형상관리·품질 장의 해당 절을 참조. 기출 당시 판본과 현재 v4.0a를 구분합니다.
- [Capabilities: Continuous delivery](https://dora.dev/capabilities/continuous-delivery/) — DORA; 지속 갱신 문서; 확인 2026-11-05. 확인 범위: 본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다.
- [Microservices Architecture Style](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices) — Microsoft Azure Architecture Center; 지속 갱신 문서; 확인 2026-11-05. 확인 범위: 본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다.
- [Event-Driven Architecture Style](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven) — Microsoft Azure Architecture Center; 지속 갱신 문서; 확인 2026-11-05. 확인 범위: 본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다.
- [The Istio service mesh](https://istio.io/latest/about/service-mesh/) — Istio 프로젝트; 열람 화면 1.31.3; 확인 2026-11-05. 확인 범위: 공식 문서에서 서비스 메시 기능과 ambient/sidecar 두 배포 모드 확인. 모든 메시가 sidecar만 사용한다고 설명하지 않습니다.

## 연관 기출

- [제127회 4교시 1번](../questions/qnet-127-p4.md#q1) — MSA 개념 및 특징과 구현시 지켜야 할 원칙; 모놀리스 아키텍처(Monolith Architecture)와 MSA 비교; MSA 구현을 위한 서비스 매쉬(Service Mesh). 대응: 핵심원리/예제/비교표; 충족.
- [제129회 3교시 5번](../questions/qnet-129-p3.md#q5) — EDA(Event Driven Architecture)의 토폴로지 구성요소인 중재자 토폴로지(Mediator Topology), 브로커 토폴로지(Broker Topology)를 비교 설명하시오.. 대응: 핵심원리/예제/비교표; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
