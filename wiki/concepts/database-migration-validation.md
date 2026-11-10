---
id: database-migration-validation
title: DB 전환·프로파일링·마이그레이션 검증
aliases:
- Database Migration
type: concept
domains:
- 데이터베이스
sources:
- id: source-subnote-ba5d524c8f67
- id: source-subnote-84761216a5c4
- id: source-subnote-03a1f618cdb4
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# DB 전환·프로파일링·마이그레이션 검증

## 서브노트

### 한눈에 이해

서버를 옮겼는데 행 수가 같다고 모든 값과 업무 동작이 같다고 할 수 없습니다. 문자·숫자·날짜의 의미와 변경 중인 데이터의 기준 시점까지 맞아야 전환이 끝납니다.

### 정의와 핵심 원리

DB 제품·환경 변경 시 구조·코드·데이터·운영 기능을 변환하고 원본 대비 값과 업무 결과의 동등성을 검증하는 과정입니다.

- 무결성은 키·도메인·참조 등 규칙 위반 여부, 정합성은 여러 표현·시스템 간 자료의 일치라는 문맥을 먼저 정합니다. 프로파일링은 NULL·중복·빈도·최솟값/최댓값·형식·패턴·참조 고아·업무 규칙 위반을 실제 값에서 찾는 진단입니다.
- 전환 목표·비용·라이선스·운영 역량을 검토하고, DB 객체·SQL·프로시저·자료형의 호환성을 확인합니다. 시범 이관 뒤 전체 데이터를 옮기고 변경분(CDC)을 반영합니다. 응용 쿼리·배치·백업·모니터링과 부하·장애 대응을 시험한 뒤 전환(cutover)과 원복(rollback) 기준을 정합니다.
- 검증은 행수/집계·키별 대조·정규화된 hash·샘플 및 경계값·업무 결과·CDC 지연을 결합합니다. HA는 주-대기 복제와 장애 탐지/승격·접속 전환·분할뇌 방지·복구 시험이 필요하며 복제는 삭제·오류도 전파하므로 독립 백업을 대체하지 않습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| 건수·합계 | 누락/중복·총량 대사 | 서로 상쇄되는 오류는 놓침 |
| 행·값 비교 | 키별 대응과 mismatch | 기준 snapshot·정규화 필요 |
| 업무·운영 시험 | 결과·성능·복구 확인 | 경계값·장애 시나리오 |

<!-- subnote-page:apply -->

### 적용 예제

**오픈소스 DB로 주문 이관**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 원본 금액은 소수 둘째 자리, 시각은 시간대 포함입니다.

1. 대상 numeric의 정밀도와 timestamp 의미를 매핑하고 NULL·고아 FK를 먼저 진단합니다.
2. 원본과 대상의 비교 기준 시점을 맞춥니다. 건수·일매출·키별 금액·시각을 대조하고, 그 시점까지 원본에서 바뀐 내용이 대상에 반영됐는지 확인합니다.
3. 읽기/쓰기 전환 전 부하·failover를 시험하고 실패 시 원복 가능한 종료 기준을 둡니다.

**결과·해석:** 데이터 값과 응용 의미·운영 복구를 함께 검증합니다.

**전제·주의:** hash 비교는 문자 인코딩·NULL·시간대·소수 표현이 같게 정규화된 경우에만 유효합니다.

### 답안 골격과 혼동 방지

전환 배경·제약 → 프로파일링 관점 → 단계별 이관·CDC → 값/업무 검증 → HA·backup·rollback

- 건수가 같다는 이유로 검증을 끝내지 않습니다.
- 오픈소스라는 이유만으로 TCO가 자동 감소하지 않습니다.

### 내용을 가리고 회상

1. 정합성과 무결성을 어떤 문맥으로 구분하겠습니까?
2. 데이터가 계속 바뀔 때 비교 시점을 어떻게 맞춥니까?
3. 복제와 독립 백업의 역할은 어떻게 다릅니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html) — Amazon Web Services; AWS DMS User Guide; 날짜 미표시; 확인 2026-11-05. 확인 범위: 실제 열람: full-load 후 행 단위 비교, CDC 변경 검증, mismatch 보고와 검증 부하. DB 전환 전체 프로젝트 절차는 이 원리를 바탕으로 한 강사 설계입니다.
- [PostgreSQL 18: High Availability, Load Balancing, and Replication](https://www.postgresql.org/docs/18/high-availability.html) — PostgreSQL Global Development Group; PostgreSQL 18; 확인 2026-11-05. 확인 범위: 실제 열람: 주 서버 장애 시 대기 서버 인계, replication·log shipping·synchronous replication·failover 구성. 제품이 자동으로 모든 장애전환을 제공한다고 주장하지 않습니다.
- [Data quality use cases](https://legacy.docs.greatexpectations.io/docs/reference/learn/data_quality_use_cases/dq_use_cases_lp/) — Great Expectations; GX 1.23.2 표시; 확인 2026-11-05. 확인 범위: 실제 열람: distribution/freshness/integrity/missingness/schema/uniqueness/volume와 비정형 metadata 검사. 국내 공공 성숙도 모델 등급을 이 문서로 검증하지 않습니다.

## 연관 기출

- [제128회 3교시 5번](../questions/qnet-128-p3.md#q5) — 무결성·정합성 차이; 값 진단 프로파일링; 마이그레이션 검증 테스트. 대응: 핵심원리; 충족.
- [제138회 2교시 1번](../questions/qnet-138-p2.md#q1) — 오픈소스 DBMS 전환 배경; 제약사항; 단계별 절차; HA 구성. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
