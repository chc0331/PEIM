---
id: database-index-structures
title: B+트리 인덱스와 다차원 색인
aliases:
- Database Index
type: concept
domains:
- 데이터베이스
sources:
- id: source-subnote-52364617abf0
- id: source-subnote-5fd50abecd98
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# B+트리 인덱스와 다차원 색인

## 서브노트

### 한눈에 이해

책의 찾아보기처럼 값을 바로 찾게 하는 별도 구조가 인덱스입니다. 하지만 건물 좌표처럼 여러 방향의 범위를 찾는 질문은 단일 숫자 순서만으로 효율적으로 풀기 어렵습니다.

### 정의와 핵심 원리

검색 조건에 맞는 행 후보와 위치를 빠르게 좁히는 보조 접근 구조이며, 키 정렬·해시·공간 분할·영역 묶음 등을 사용합니다.

- SQL Server rowstore의 clustered 인덱스는 leaf에 데이터 행을 저장하고 키 순서로 조직하므로 하나만 가능합니다. nonclustered leaf는 키와 행 위치자를 저장하고 여러 개 만들 수 있습니다. PK와 clustered는 별개 개념이며 제품마다 물리 저장이 다릅니다.
- B+트리는 균형 탐색·범위 검색에 적합합니다. 복합키는 선두 컬럼과 정렬 순서, 선택도, covering 여부가 중요합니다. 인덱스가 늘면 INSERT/UPDATE/DELETE의 유지 비용과 공간이 증가하므로 조회 계획·실제 읽기를 확인합니다.
- 다차원 색인은 점·영역을 대상으로 합니다. KD-tree는 축을 번갈아 나누고, Quad-tree는 공간을 사분할하며, R-tree는 객체의 최소경계영역을 묶어 탐색합니다. PostGIS는 GiST 기반 R-tree로 후보 영역을 먼저 줄이고 정확 공간 조건을 재검사합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Clustered/nonclustered | 행 자체/별도 키-위치자 | SQL Server 구현 기준 |
| KD·Quad-tree | 축/공간을 분할 | 점·공간 밀도와 차원 영향 |
| R-tree | 겹칠 수 있는 경계영역 계층 | 공간 객체의 교차·포함 검색 |

<!-- subnote-page:apply -->

### 적용 예제

**반경 내 병원 찾기**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 병원 100만 곳에서 현재 위치 1km 내 병원을 조회합니다.

1. 위도 컬럼과 경도 컬럼의 독립 B-tree만으로 원형 범위를 정확히 표현할 수 없음을 확인합니다.
2. 공간 인덱스로 경계영역 후보를 찾은 후 실제 거리 조건으로 필터합니다.
3. 검색 반경·좌표계·자료 분포를 고정하고 후보 수/정확 결과/지연을 측정합니다.

**결과·해석:** 공간 후보 축소와 실제 거리 판정을 분리하면 효율과 정확성을 함께 설명할 수 있습니다.

**전제·주의:** 다차원 색인과 여러 컬럼을 이어 붙인 복합 인덱스를 같은 뜻으로 쓰지 않습니다.

### 답안 골격과 혼동 방지

검색 구조 정의 → clustered/nonclustered 표 → 다차원 3유형 도식 → 공간 검색 예시 → 유지비용·선택도·측정

- 인덱스가 있으면 항상 사용된다고 단정하지 않습니다.
- 고차원에서는 공간 색인의 효율이 낮아질 수 있습니다.

### 내용을 가리고 회상

1. clustered leaf와 nonclustered leaf에는 무엇이 있습니까?
2. R-tree의 경계영역이 겹치면 어떤 비용이 생깁니까?
3. 공간 인덱스 후보가 곧 최종 정답입니까?

### 적용 기준과 근거

SQL Server·PostGIS 구현을 확인했습니다. KD/Quad-tree 세부 알고리즘은 추가 공개 교재 확인이 필요합니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Clustered and nonclustered indexes](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17) — Microsoft; SQL Server 17.x 문서; 확인 2026-11-05. 확인 범위: 실제 열람: rowstore B+ tree, clustered leaf가 데이터 행, nonclustered의 분리 구조와 행 위치자, 한 테이블 하나의 clustered index. 모든 DBMS 공통 물리 구조라고 일반화하지 않습니다.
- [How do I use spatial indexes?](https://postgis.net/documentation/faq/spatial-indexes/) — PostGIS PSC / OSGeo; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: geometry의 GiST 기반 R-tree, USING GIST, 공간 인덱스 인식 함수·사전 필터. KD/Quad-tree의 일반 구조까지 이 문서가 모두 검증하는 것은 아닙니다.

## 연관 기출

- [제136회 2교시 5번](../questions/qnet-136-p2.md#q5) — 인덱스 개념; 클러스터드·논클러스터드 비교. 대응: 핵심원리; 충족.
- [제134회 3교시 5번](../questions/qnet-134-p3.md#q5) — 다차원 색인 개념; 유형; 활용사례. 대응: 핵심원리; 부분 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
