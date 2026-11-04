---
id: disaster-recovery-rto-rpo
title: RTO·RPO와 Active-Active·Passive·Pilot Light
aliases: []
type: concept
domains:
- 클라우드·인프라
sources:
- id: source-subnote-de61aa8594aa
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# RTO·RPO와 Active-Active·Passive·Pilot Light

## 서브노트

### 한눈에 이해

언제까지 서비스를 다시 열지와 어느 시점의 데이터까지 잃어도 되는지는 서로 다른 목표입니다.

### 정의와 핵심 원리

RTO는 중단후허용하는복구 시간 목표이고 RPO는 복구해야할데이터 시점의 목표로 통상허용손실 시간폭으로표현합니다. BIA로업무 영향·의존성·우선순위를정한 뒤데이터 복제와 실행 환경준비 수준을선택합니다.

- Active-Active는 여러 사이트가평상시요청을 처리합니다. 장애지역트래픽 우회·잔여용량·데이터 충돌·분산일관성·공통의 존성이핵심입니다. 멀티리전이라는이름만 으로RTO/RPO0을 보장하지 않으며데이터 오염은 복제되어 별도 시점 백업이 필요합니다.
- Active-Passive는 주사이트만처리하고 대기는장애 전환후처리합니다. hot/warm/cold등준비 수준에따라 기동·확장·복원 시간이 달라집니다. Pilot Light는 복제 데이터와 핵심 기반은 가동하되응용등추가 자원기동·배포·확장이필요하므로 작은 용량으로 즉시처리하는warm standby와 다릅니다.
- 복구에 는 선언·탐지·결정·DB승격·자원확장·DNS/경로전환·인증·검증 시간이 포함됩니다. 복제 지연관측·백업 복원·장애훈련·failback·정합성 검사를 수행하고 목표와 실제 측정 결과를 분리합니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| Active-Active | 모든 지역평시처리 | 비용·쓰기 충돌·잔여용량 |
| Active-Passive | 대기지역전환후처리 | 대기준비 수준별시간차 |
| Pilot Light | 핵심 데이터·기반만 가동 | 응용기동·확장선행필요 |
| Warm Standby | 작은 규모전체가동 | 즉시제한처리후확장 |

<!-- subnote-page:apply -->

### 적용 예제

**복구 목표 검증**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 장애10:00, 서비스 복구10:25, 최종복구 데이터09:57;목표 RTO30분/RPO5분

1. 실제 복구 시간은 25분입니다.
2. 복구 데이터 손실폭은3분입니다.
3. 25<=30, 3<=5로이번훈련은두목표를 충족합니다.
4. 다만 오염사고·자격증명 침해·전체 리전손실등다른 시나리오도 시험합니다.

**결과·해석:** 시간 목표와 데이터 시점을 독립적으로평가합니다.

**전제·주의:** 명시 시각은가상훈련예이며 제품보장값이 아닙니다.복제는 백업의 대체물이아닙니다.

### 답안 골격과 혼동 방지

BIA·목표정의 → RTO/RPO 시간축 → 세전략구조비교 → 계산·훈련 → failback·오염 복구

- RPO를 서비스 복구에 걸리는시간이라 쓰지않습니다.
- Pilot Light를 작은 서비스가 항상 처리중인상태로 설명하지 않습니다.

### 내용을 가리고 회상

1. RTO가 짧아도RPO가 길수 있습니까?
2. Pilot Light와Warm Standby의차이는무엇입니까?
3. Active-Active에도백업이 필요한 이유는무엇입니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) — AWS; 상시 백서; 확인 2026-11-05. 확인 범위: active/passive, pilot light, warm standby, active/active 설명 열람. 제시 예시시간은 보장값으로 사용하지 않음.

## 연관 기출

- [제133회 1교시 9번](../questions/qnet-133-p1.md#q9) — BCP지표; DRS고려사항. 대응: 핵심원리/비교표/예제; 충족.
- [제137회 3교시 3번](../questions/qnet-137-p3.md#q3) — 멀티리전AA개념·특징; 주요 기술. 대응: 핵심원리/비교표/예제; 충족.
- [제140회 3교시 1번](../questions/qnet-140-p3.md#q1) — RTO·RPO; Active-Active·Active-Passive·Pilot Light. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
