---
id: source-subnote-52364617abf0
title: '자료: Clustered and nonclustered indexes'
aliases: []
type: source
domains:
- 서브노트 근거
sources:
- path: raw/research/2026-11-05-data-ai.md
  url: https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17
status: 출처 확인
updated: '2026-11-05'
source_url: https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17
author: Microsoft
published: SQL Server 17.x 문서
captured_at: '2026-11-05'
---

# Clustered and nonclustered indexes

## 확인 범위와 수집 형태

실제 열람: rowstore B+ tree, clustered leaf가 데이터 행, nonclustered의 분리 구조와 행 위치자, 한 테이블 하나의 clustered index. 모든 DBMS 공통 물리 구조라고 일반화하지 않습니다.

강사 생성 조사 요약과 URL 참조를 보관했습니다. 외부 원문 전체 보관이 아닙니다. 기술 주장은 연결된 서브노트의 적용 범위·검토 상태를 함께 확인합니다.

- [기관 원문](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver17)
- [세션 조사 기록](../../raw/research/2026-11-05-data-ai.md)
