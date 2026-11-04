---
id: nosql-document-modeling
title: NoSQL 유형과 MongoDB 모델링
aliases:
- NoSQL Data Modeling
type: concept
domains:
- 데이터베이스
sources:
- id: source-subnote-9a050cca5cd7
- id: source-subnote-2e1d92f50117
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# NoSQL 유형과 MongoDB 모델링

## 서브노트

### 한눈에 이해

주문과 소량의 주문상세를 문서 하나로 읽으면 조인을 줄일 수 있습니다. 대신 상세가 끝없이 늘거나 여러 곳에서 독립적으로 바뀌면 별도 문서의 참조가 더 알맞을 수 있습니다.

### 정의와 핵심 원리

관계형 표만을 기본 모델로 삼지 않는 저장소 계열이며 대표적으로 key-value·document·wide-column·graph 모델이 있습니다.

- Key-value는 키로 값을 조회하고, document는 중첩 필드·배열을 갖는 문서, wide-column은 행 키와 유연한 컬럼 집합, graph는 노드·엣지 관계 탐색을 중심으로 합니다. 기출의 3가지 구조 요구에는 채택한 분류 기준을 먼저 적고 그래프가 별도 분류일 수 있음을 덧붙입니다.
- MongoDB는 BSON 문서·collection을 사용합니다. 스키마가 유연하다는 말은 스키마가 없다는 뜻이 아닙니다. 데이터 타입·필수 필드·검증 규칙·인덱스를 정해야 하고 단일 문서 원자성과 다중 문서 트랜잭션의 적용 범위를 구분해야 합니다.
- 모델링은 조회·갱신 패턴 수집→관계/수명/증가량 분석→내장 또는 참조 선택→문서 크기·인덱스·shard key 검토→대표 부하 검증입니다. 함께 읽고 크기가 제한된 하위 자료는 내장, 독립 수명·큰 다대다·무한 증가 배열은 참조를 검토합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Key-value | 키 중심 단순 접근 | 캐시·세션 |
| Document | 중첩 객체·필드 질의 | 상품 카탈로그·주문 |
| Wide-column·Graph | 행 키/컬럼 집합 또는 관계 그래프 | 대규모 로그 또는 연결 탐색 |

<!-- subnote-page:apply -->

### 적용 예제

**주문·후기 모델 비교**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 주문당 상세는 최대 20개, 상품 후기는 수백만 개까지 증가할 수 있습니다.

1. 주문과 상세는 자주 함께 읽고 한 번에 갱신하므로 상세 배열 내장을 검토합니다.
2. 상품 후기는 별도 collection에 product_id 참조로 두어 무한 배열을 피합니다.
3. 필요 필드와 조회 인덱스를 정하고 문서 크기·갱신 충돌·페이지네이션을 부하 시험합니다.

**결과·해석:** 같은 1:N 관계라도 접근 패턴과 증가량에 따라 설계가 달라집니다.

**전제·주의:** MongoDB 문서의 최대 크기는 16 MiB이므로 배열의 장기 증가량과 실제 크기 여유를 검토합니다.

### 답안 골격과 혼동 방지

NoSQL 분류 기준 → MongoDB 문서 구조 → 요구→패턴→모델→검증 → 내장/참조 예시 → 일관성·운영 절충

- NoSQL은 SQL·트랜잭션이 절대 없다는 뜻이 아닙니다.
- 관계형 테이블을 collection으로 1:1 옮기지 않습니다.

### 내용을 가리고 회상

1. 3분류와 4분류가 갈리는 기준은 무엇입니까?
2. 같은 1:N에서도 내장 대신 참조하는 조건은 무엇입니까?
3. 스키마 유연성과 검증 규칙은 양립합니까?

### 적용 기준과 근거

MongoDB 문서 모델은 공식 확인. NoSQL 전체 유형의 제품별 특징과 128회가 의도한 정확한 3분류 명칭은 단일 공식 분류로 확정하지 않았습니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Embedded Data in Your MongoDB Schema](https://www.mongodb.com/docs/manual/data-modeling/embedding/) — MongoDB; Database Manual; 문서 날짜 미표시; 확인 2026-11-05. 확인 범위: 실제 열람: 문서·배열·내장, 한 번 조회/단일 문서 원자성, 16 MiB 제한, 내장/참조 선택 조건. NoSQL 전체가 동일한 일관성·트랜잭션 기능을 가진다는 주장은 하지 않습니다.
- [Sharding Introduction and Architecture](https://www.mongodb.com/docs/manual/sharding/) — MongoDB; Database Manual; MongoDB 8.0 언급 포함; 확인 2026-11-05. 확인 범위: 실제 열람: 수평 확장, shard/router/config servers, shard key, range/hashed 구분. 파티셔닝의 상위 개념과 제품별 sharding 구현을 구분합니다.

## 연관 기출

- [제127회 1교시 8번](../questions/qnet-127-p1.md#q8) — MongoDB 개념·특징. 대응: 핵심원리; 충족.
- [제128회 1교시 6번](../questions/qnet-128-p1.md#q6) — NoSQL 3가지 구조. 대응: 핵심원리; 부분 충족.
- [제133회 1교시 3번](../questions/qnet-133-p1.md#q3) — NoSQL 유형; 모델링 절차. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
