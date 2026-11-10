---
id: sql-optimizer-tuning
title: SQL 튜닝과 비용 기반 옵티마이저
aliases:
- Query Optimizer
type: concept
domains:
- 데이터베이스
sources:
- id: source-subnote-3e53f56af4cb
- id: source-subnote-df72ec5df449
- id: source-subnote-8e7809b3ad21
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
related_terms:
- SQL Tuning
---

# SQL 튜닝과 비용 기반 옵티마이저

## 서브노트

### 한눈에 이해

SQL에는 필요한 결과를 적습니다. 어떤 순서와 방식으로 데이터를 읽을지는 DB가 정합니다. 튜닝할 때는 결과가 같은지 확인한 뒤 실행 시간과 자원 사용량을 비교합니다.

### 정의와 핵심 원리

옵티마이저는 후보 실행 계획을 평가·선택하는 구성 요소이며 DB 튜닝은 설계·SQL·실행 환경의 병목을 측정하고 개선하는 활동입니다.

- RBO는 정해진 규칙 우선순위에 의존하고 CBO는 테이블/컬럼 통계와 선택도·행수 추정으로 I/O·CPU 등의 비용을 비교합니다. CBO도 모든 가능한 계획의 전역 최적을 보장하지 않으며 통계가 낡거나 데이터 상관이 크면 추정이 빗나갑니다.
- 설계 단계에는 적절한 자료형·키·정규화·인덱스·파티션·접근 패턴을 검토합니다. SQL 단계에서는 불필요한 열/행·조인·정렬을 줄이고 조건이 접근 경로를 활용하는지 봅니다. 파라미터·캐시 증설은 원인 측정 후 판단합니다.
- PostgreSQL에서 EXPLAIN은 추정 행 수와 비용을 보여 줍니다. EXPLAIN ANALYZE는 질의를 실행해 실제 행 수와 시간을 더합니다. 둘을 대조해 추정이 크게 어긋난 단계와 반복 횟수를 찾습니다. Oracle 힌트는 접근 경로(INDEX/FULL), 조인 방법(USE_NL/USE_HASH), 순서(LEADING), 목표와 병렬 실행 등을 유도합니다. 힌트가 무시되거나 데이터 분포가 바뀌어 성능이 떨어질 수 있습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| RBO | 규칙·우선순위 | legacy 접근, 데이터 분포 반영 제한 |
| CBO | 통계·카디널리티·자원 비용 | 통계 오차·제품별 비용 모델 |
| 힌트 | 특정 계획 선택 유도 | 유효성·회귀·유지비 검토 |

<!-- subnote-page:apply -->

### 적용 예제

**대량 조회의 인덱스 역효과**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 직원 100만 명 중 관리자 비율이 처음 1%에서 80%로 바뀌었습니다.

1. 관리자 조건의 실제 행수가 추정 행수와 얼마나 다른지 확인합니다.
2. 조건에 맞는 행이 적을 때는 인덱스로 찾는 편이 유리할 수 있습니다. 80만 건을 여기저기서 읽어야 한다면 테이블을 순서대로 읽는 편이 빠를 수 있습니다.
3. 통계를 갱신하고 두 계획을 같은 부하에서 비교한 뒤 응답시간·논리읽기·쓰기 유지비를 함께 기록합니다.

**결과·해석:** 인덱스 사용 여부보다 전체 자원 비용과 응답 목표를 기준으로 판단합니다.

**전제·주의:** EXPLAIN ANALYZE는 실제 SQL을 실행하므로 변경 SQL은 안전한 검증 환경에서 다룹니다.

### 답안 골격과 혼동 방지

튜닝 목적·설계/SQL/환경 → RBO-CBO 비교 → 실행 계획 추정/실제 → 힌트 유형 → 동일 결과·부하 검증

- 비용 숫자를 초 단위와 같게 읽지 않습니다.
- 모든 SQL에 인덱스나 힌트를 강제하지 않습니다.

### 내용을 가리고 회상

1. 통계가 틀리면 계획의 어떤 결정이 달라집니까?
2. 대부분 행을 읽는 질의가 full scan을 고르는 이유는 무엇입니까?
3. 튜닝 전후에 결과 동등성을 어떻게 확인합니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Query Optimizer Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgsql/query-optimizer-concepts.html) — Oracle; Oracle AI Database 26 문서; 확인 2026-11-05. 확인 범위: 실제 열람: 통계 기반 비용·I/O/CPU/통신 비용·액세스/조인/조인 순서 후보·CBO와 legacy RBO 구분. 비용 값은 실행 초가 아닙니다.
- [PostgreSQL 18: Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html) — PostgreSQL Global Development Group; PostgreSQL 18; 확인 2026-11-05. 확인 범위: 실제 열람: plan tree·scan/join/sort 노드·추정 행수/비용, 통계의 표본성, EXPLAIN ANALYZE와 주의점 구성. 예시 비용을 성능 보장 수치로 전용하지 않습니다.
- [Influencing the Optimizer](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgsql/influencing-the-optimizer.html) — Oracle; Oracle AI Database 26 문서; 확인 2026-11-05. 확인 범위: 실제 열람: hints, 통계, SQL profile, plan management의 역할. 접근 경로·조인 방법·순서 등 힌트 분류는 Oracle 문맥에서 설명합니다.

## 연관 기출

- [제127회 2교시 3번](../questions/qnet-127-p2.md#q3) — 튜닝 개념·목적; 설계 단계 기법; 힌트 유형. 대응: 핵심원리; 충족.
- [제127회 3교시 4번](../questions/qnet-127-p3.md#q4) — 옵티마이저 개념; RBO-CBO 비교; 적용 고려사항. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
