---
id: dataops-observability-elk
title: DataOps와 데이터 관측가능성·ELK
aliases:
- DataOps and Data Observability
type: concept
domains:
- 데이터관리
sources:
- id: source-subnote-8b3c1ac5d94d
- id: source-subnote-25650580e31c
- id: source-subnote-b917357338c0
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# DataOps와 데이터 관측가능성·ELK

## 서브노트

### 한눈에 이해

배치가 성공으로 기록됐는데 오늘 주문 10만 건 중 1만 건만 들어올 수 있습니다. 실행 로그와 별도로 데이터가 제때 도착했는지, 양과 형식이 맞는지 확인해야 문제가 생긴 단계를 찾을 수 있습니다.

### 정의와 핵심 원리

DataOps는 데이터 파이프라인의 변경·검증·배포·운영 피드백을 자동화하는 협업 방식이며 관측 가능성은 수집한 신호로 데이터 상태·원인·영향을 파악하는 능력입니다.

- DevOps는 응용 코드/서비스의 배포와 운영이 중심이고 DataOps는 원천·변환 코드·스키마·데이터 품질·계보까지 함께 관리합니다. 버전관리→CI 검사→시험 데이터 검증→배포/오케스트레이션→운영 관측→복구·개선으로 연결하며 원천 자료의 재처리 가능성이 중요합니다.
- Monte Carlo의 5요소 분류는 freshness(도착 시각), volume(양), schema(구조), distribution(값 분포), lineage(연결/영향)입니다. 이는 공급자 분류이지 유일한 국제 표준은 아닙니다. 규칙 검사와 통계 이상 탐지는 알려진 문제와 예상 못한 변화를 각각 보완합니다.
- ELK에서 Logstash/Beats는 수집·변환, Elasticsearch는 저장·색인·검색/집계, Kibana는 탐색·대시보드를 담당합니다. 데이터 품질 신호를 로그로 모을 수 있지만 ELK 설치 자체가 품질 보장은 아닙니다. 경보는 owner·영향 데이터·실행 이력·복구 방법과 연결되어야 합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| DevOps | 서비스 코드·실행 상태 | 배포·장애 복구 |
| DataOps | 데이터+변환+품질·계보 | 데이터 제품의 반복 전달 |
| 관측 가능성 | 신호→상태·원인·영향 | 경보 이후 책임·조치 필요 |

<!-- subnote-page:apply -->

### 적용 예제

**배치 성공인데 매출 급감**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 매일 02시에 10만 건이 오던 주문 적재가 오늘 1만 건입니다.

1. 도착 시각은 정상이라 최신성(freshness)만 보면 통과합니다. 평소보다 건수가 적으므로 데이터 양(volume)에서 경보가 납니다. 지역별 건수도 비교해 어느 지역에서 줄었는지 살핍니다.
2. 데이터 계보(lineage)를 따라 지점의 수집 API, 주문 원본, 매출 집계를 차례로 확인합니다. 이상이 시작된 작업의 로그는 ELK에서 살핍니다.
3. 원천 보존분을 재처리하고 중복 방지 키로 적재한 뒤 매출 집계를 검증합니다.

**결과·해석:** 성공/실패 로그와 데이터 내용 관측을 함께 써야 업무 영향을 줄일 수 있습니다.

**전제·주의:** 계절성·휴일을 고려하지 않은 고정 임계값은 잦은 오경보를 만들 수 있습니다.

### 답안 골격과 혼동 방지

DataOps·DevOps 비교 → 파이프라인 구조·자동화 → 관측 5요소 → ELK 역할 → 경보→원인→복구 예시

- 관측 가능성을 단순 대시보드 개수로 평가하지 않습니다.
- 데이터 재처리 때 중복이 생기지 않는지 확인합니다.

### 내용을 가리고 회상

1. 파이프라인 성공과 데이터 품질 성공은 어떻게 다릅니까?
2. freshness는 정상인데 volume이 틀리는 예를 들 수 있습니까?
3. lineage가 장애 조치에 주는 정보는 무엇입니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Data Observability Evaluation Guide](https://info.montecarlodata.com/hubfs/Assets%20-%20Guides,%20Ebooks,%20Reports/Data%20Observability%20Evaluation%20Guide.pdf) — Monte Carlo; 날짜 미표시; 25쪽 공급자 가이드; 확인 2026-11-05. 확인 범위: 실제 열람: PDF p.5 freshness/volume/schema/distribution/lineage, end-to-end·incident/root-cause. 5요소는 해당 공급자가 제시한 분류이며 보편 표준이 아닙니다.
- [Elastic Stack: Elasticsearch, Kibana, Beats and Logstash](https://www.elastic.co/elastic-stack) — Elastic; 2026-11-05 확인한 제품 설명; 날짜 미표시; 확인 2026-11-05. 확인 범위: 실제 열람: Logstash/Beats 수집, Elasticsearch 검색·분석, Kibana 시각화 역할. 현재 제품 홍보 수치를 성능 근거로 쓰지 않습니다.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — Google Cloud; 문서 날짜 미표시; 2026-11-05 확인; 확인 2026-11-05. 확인 범위: 실제 열람: 자동 ML 파이프라인·검증·CT/CI/CD·feature store의 training-serving skew 방지. ModelOps의 조직 전체 범위는 강사 비교로 표시합니다.

## 연관 기출

- [제130회 4교시 6번](../questions/qnet-130-p4.md#q6) — DataOps와 DevOps 비교; DataOps 아키텍처·기술. 대응: 핵심원리; 충족.
- [제132회 1교시 7번](../questions/qnet-132-p1.md#q7) — ELK 스택. 대응: 핵심원리; 충족.
- [제138회 1교시 8번](../questions/qnet-138-p1.md#q8) — 데이터 관측가능성. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
