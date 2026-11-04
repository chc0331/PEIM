---
id: partitioning-sharding
title: 수평·수직 분할과 샤딩
aliases:
- Database Partitioning and Sharding
type: concept
domains:
- 데이터베이스
sources:
- id: source-subnote-d2f478274ff3
- id: source-subnote-2e1d92f50117
- id: source-subnote-9538aacafedb
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 수평·수직 분할과 샤딩

## 서브노트

### 한눈에 이해

도서 전체를 발행연도별 여러 서가로 나누면 필요한 연도만 읽을 수 있습니다. 이를 여러 독립 서버에 나누면 저장·처리 용량을 키울 수 있지만 어디로 보낼지와 서버 간 작업이 어려워집니다.

### 정의와 핵심 원리

분할은 데이터를 행·열 등의 단위로 나누는 것이며 샤딩은 보통 수평 분할된 자료를 여러 노드에 분산 배치하는 확장 방식입니다.

- 수평 분할은 같은 스키마의 행을 range/list/hash 기준으로 나누고 합집합으로 원래 자료를 복원합니다. 수직 분할은 PK를 함께 둔 채 자주 쓰는 열과 큰/민감 열 등을 분리하고 키 조인으로 복원합니다. 분할 완전성·복원 가능성·중복 관리가 중요합니다.
- 파티셔닝은 논리 표의 조각이라는 넓은 개념이고 반드시 한 서버에만 한정되지는 않습니다. 샤딩은 라우터·분산 메타데이터·재배치가 필요한 여러 머신 배치라는 운영 측면을 강조합니다. 파티션은 단일 DB, 샤드는 다중 DB라는 비교는 대표 구현 예로 한정합니다.
- 키는 질의 조건·분포 균등성·증가 방향·고유성·조인 범위를 기준으로 정합니다. 날짜 range는 범위 질의에 유리하지만 최근 shard에 쓰기가 몰릴 수 있고 hash는 분산에 유리하나 범위 질의가 여러 shard로 퍼질 수 있습니다. 재균형·분산 트랜잭션·백업·FK 지원을 검토합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| 수평 분할 | 행을 나누고 UNION 복원 | 기간·지역·hash |
| 수직 분할 | 열을 나누고 PK JOIN 복원 | 자주 쓰는 열·큰 본문 분리 |
| 샤딩 | 여러 노드에 분할 배치 | 라우팅·재균형·교차 작업 |

<!-- subnote-page:apply -->

### 적용 예제

**고객 주문 분산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 고객별 주문 조회가 대부분이며 고객 ID가 넓게 분포합니다.

1. hash(customer_id)로 주문을 여러 shard에 분산합니다.
2. 같은 고객의 주문이 함께 놓이면 고객 질의가 한 shard로 향할 수 있습니다.
3. 전체 월매출은 여러 shard 집계가 필요하고 한 거대 고객이 부하를 독점할 가능성을 따로 측정합니다.

**결과·해석:** 분산 키는 균등성뿐 아니라 실제 질의의 지역성을 함께 결정합니다.

**전제·주의:** 날짜 경계는 [시작,다음 시작)처럼 중복·누락 없이 선언합니다.

### 답안 골격과 혼동 방지

분할 단위·복원 조건 → 수평/수직 비교 → 샤딩과 파티셔닝 → range/hash 예시 → 운영·질의·제약 고려

- 샤딩하면 모든 질의가 자동 빨라진다고 쓰지 않습니다.
- 수직 분할에서 조인 키를 잃지 않습니다.

### 내용을 가리고 회상

1. 수평과 수직 분할을 각각 어떻게 복원합니까?
2. 증가하는 시간 키의 hotspot을 설명할 수 있습니까?
3. 샤드 키가 없는 질의는 어디로 갈 수 있습니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [PostgreSQL 18: Table Partitioning](https://www.postgresql.org/docs/18/ddl-partitioning.html) — PostgreSQL Global Development Group; PostgreSQL 18; 확인 2026-11-05. 확인 범위: 실제 열람: 논리 테이블의 물리 조각 분할, range/list/hash, pruning·대량 삭제, 하한 포함·상한 배제. 수직분할은 이 기능과 별도 관계 설계 개념입니다.
- [Sharding Introduction and Architecture](https://www.mongodb.com/docs/manual/sharding/) — MongoDB; Database Manual; MongoDB 8.0 언급 포함; 확인 2026-11-05. 확인 범위: 실제 열람: 수평 확장, shard/router/config servers, shard key, range/hashed 구분. 파티셔닝의 상위 개념과 제품별 sharding 구현을 구분합니다.
- [Database System Concepts 5th ed., Chapter 22: Distributed Databases](https://www.db-book.com/Previous-editions/db5/slide-dir/ch22.pdf) — A. Silberschatz, H. F. Korth, S. Sudarshan; 2005-08-22; 확인 2026-11-05. 확인 범위: 실제 열람: 분산 사이트, 복제·분할, 위치·분할·복제 투명성과 분산 트랜잭션 구성. 시험에서 말하는 5종 전체 목록은 출처별 분류 차이를 명시합니다.

## 연관 기출

- [제127회 4교시 3번](../questions/qnet-127-p4.md#q3) — 샤딩 개념·분할방법; 파티셔닝 차이; 고려사항. 대응: 핵심원리; 충족.
- [제138회 3교시 3번](../questions/qnet-138-p3.md#q3) — 분할 단위; 수평·수직분할. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
