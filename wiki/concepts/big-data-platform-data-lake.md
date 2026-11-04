---
id: big-data-platform-data-lake
title: 빅데이터 플랫폼·데이터 레이크·늪 방지
aliases:
- Big Data Platform and Data Lake
type: concept
domains:
- 데이터관리
sources:
- id: source-subnote-ef9aac0339a9
- id: source-subnote-8c8ebef2ac84
- id: source-subnote-2c976683a113
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 빅데이터 플랫폼·데이터 레이크·늪 방지

## 서브노트

### 한눈에 이해

여러 종류의 자료를 모으는 창고가 있어도 이름표·담당자·정리 규칙이 없으면 필요한 자료를 못 찾습니다. 데이터 레이크는 원형을 보관하는 저장소이고 활용 가능한 플랫폼은 수집부터 제공까지 갖춰야 합니다.

### 정의와 핵심 원리

다양한 규모·속도·형태의 자료를 수집·저장·처리·분석·제공하는 기반이며 레이크는 원형 자료를 대규모로 보관하고 필요 시 해석하는 저장 계층입니다.

- 인프라는 분산 compute·object/분산 storage·네트워크·스케줄러·모니터링을 workload에 맞춰 설계합니다. 데이터 구조는 정형/반정형/비정형, 크기·변화율·키·시간·schema 진화·보존을 분석합니다. 저장과 계산을 분리하면 처리량을 따로 확장할 수 있지만 이동 비용을 측정해야 합니다.
- 입출력은 batch/file·CDC·stream/API 수집→raw→정제/검증→curated→mart/feature/API로 설계하고 카탈로그·계보·표준·품질·권한을 가로 계층으로 둡니다. 중복·늦은 도착·스키마 변경·재처리·오류 격리·제공 지연 SLA를 명시합니다.
- 레이크는 schema-on-read로 원형을 폭넓게 저장하고 warehouse는 분석용 구조를 미리 정리합니다. 무분별한 적재·메타데이터 누락·품질/owner 부재·중복 방치가 data swamp를 만듭니다. 도구는 목적·지연·데이터형·규모·팀 역량·호환성·재현성·TCO로 비교하며 인기 순서로 고르지 않습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| Lake | 원형·다양한 형태·읽을 때 해석 | 카탈로그/품질 없으면 늪 |
| Warehouse | 정제·구조화·반복 BI | 모델·적재 지연 관리 |
| 플랫폼 | 수집~제공과 공통 관리 | 저장소만 구축하면 불충분 |

<!-- subnote-page:apply -->

### 적용 예제

**설비 로그 분석**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 초당 센서값과 월별 정비 PDF, ERP 주문표를 함께 분석합니다.

1. 센서 stream과 ERP CDC, 정비 문서 file 입력 경로를 구분합니다.
2. raw 보존 후 시각/설비ID를 표준화하고 정제 표와 문서 검색 색인을 만듭니다.
3. 모델은 시간순 feature를 읽고 운영자는 mart/대시보드를 조회하며 schema·품질·계보를 확인합니다.

**결과·해석:** 하나의 도구로 모든 입출력을 해결하기보다 역할과 경계를 분명히 합니다.

**전제·주의:** 실시간이 필요 없는 월간 보고를 stream으로 만드는 비용도 따져야 합니다.

### 답안 골격과 혼동 방지

목표·도구 선택 기준 → 인프라/데이터/입출력 3설계 → raw→curated→소비 구조 → lake/warehouse 비교 → 늪 원인·예방

- schema-on-read를 스키마·품질 불필요로 해석하지 않습니다.
- 자료가 많다는 이유만으로 빅데이터 도구를 강제하지 않습니다.

### 내용을 가리고 회상

1. 인프라 설계와 데이터 구조 분석은 무엇이 다릅니까?
2. raw를 남기는 이유와 보존 비용은 무엇입니까?
3. data swamp를 막는 owner·metadata·품질의 역할은 무엇입니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Data architecture, AWS CAF Platform Perspective](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/data-arch.html) — Amazon Web Services; AWS Prescriptive Guidance; 날짜 미표시; 확인 2026-11-05. 확인 범위: 실제 열람: raw/curated/product marts, batch·stream, compute-storage 분리, 거버넌스·비용·반정규화 관리. 분석도구 선택 기준은 이를 바탕으로 한 강사 판단입니다.
- [What is a data lake?](https://learn.microsoft.com/en-us/azure/architecture/data-guide/scenarios/data-lake) — Microsoft Azure Architecture Center; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: raw native formats, schema-on-read, lake vs warehouse, 수집/분산 처리/BI/학습. data swamp 방지는 이 구조와 catalog/품질 근거를 결합한 강사 설계입니다.
- [Data governance with Microsoft Purview](https://learn.microsoft.com/en-us/purview/data-governance-overview) — Microsoft; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: 중앙 data office·domain stewards 연합 운영, catalog/data map·metadata와 원데이터 권한의 차이. 거버넌스의 실무 예이며 법정 표준이라고 표현하지 않습니다.

## 연관 기출

- [제126회 1교시 5번](../questions/qnet-126-p1.md#q5) — 빅데이터 분석도구 선택 원칙. 대응: 핵심원리; 충족.
- [제126회 2교시 6번](../questions/qnet-126-p2.md#q6) — 인프라 구조; 데이터 구조 분석; 입출력 설계. 대응: 핵심원리; 충족.
- [제137회 1교시 10번](../questions/qnet-137-p1.md#q10) — 데이터 늪. 대응: 핵심원리; 충족.
- [제139회 2교시 3번](../questions/qnet-139-p2.md#q3) — 데이터 레이크 아키텍처; 스웜프 원인·방지. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
