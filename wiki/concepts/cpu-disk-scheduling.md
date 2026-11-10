---
id: cpu-disk-scheduling
title: CPU·디스크 스케줄링과 SJF·SRT·SSTF·SLTF
aliases: []
type: concept
domains:
- 운영체제
sources:
- id: source-subnote-ea8936231fd1
- id: source-subnote-c6ed33ea3c6e
- id: source-subnote-6e46b190713a
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# CPU·디스크 스케줄링과 SJF·SRT·SSTF·SLTF

## 서브노트

### 한눈에 이해

CPU는 대기 중인 작업의 순서를, 하드 디스크는 대기 중인 입출력 요청의 순서를 정합니다. 두 경우에 줄이려는 비용이 다릅니다.

### 정의와 핵심 원리

CPU 스케줄링은 실행 가능한 작업에 CPU를 배분하는 정책이고 디스크 스케줄링은 대기 중인 I/O 요청의 서비스 순서를 정하는 정책입니다. 대기·반환·응답 시간·처리량·공정성의 절충이 다릅니다.

- SJF는 준비된 작업 중 예상 실행 시간이 가장 짧은 작업을 고른 뒤 선점하지 않습니다. SRT 또는 STCF는 남은 시간이 가장 짧은 작업을 고르며, 더 짧은 작업이 도착하면 실행 중인 작업을 멈추고 바꿉니다. 앞으로의 CPU 실행 시간을 정확히 예측하기 어렵고, 긴 작업이 계속 밀리는 기아를 줄여야 합니다.
- HDD에서 SSTF는 현재 헤드 위치에서 탐색 거리가 가장 짧은 요청을, SLTF는 회전 대기 시간이 가장 짧은 요청을 고릅니다. 전체 접근 시간에는 탐색·회전·전송이 모두 포함됩니다.
- 아래 CPU 예제처럼 각 작업의 시간이 실행과 준비 대기로만 구성되면 대기 시간 = 반환 시간 − 실행 시간입니다. 반환 시간은 완료 시각에서 도착 시각을 뺀 값입니다. SSD나 NVMe 장치에는 기계식 헤드와 회전 지연이 없으므로 HDD 정책을 그대로 쓰기 어렵습니다. Linux의 CFS·EEVDF는 공정성을 고려하는 별도의 정책입니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| SJF | 짧은 실행 시간 우선, 비선점 | 실행 시간 예측과 긴 작업의 기아 |
| SRT | 짧은 잔여 시간 우선, 선점 | 빠른 응답과 전환 비용 |
| SSTF·SLTF | 탐색 거리 또는 회전 대기 최소화 | HDD 특성과 기아 고려 |

<!-- subnote-page:apply -->

### 적용 예제

**선점에 따른 대기 시간 차이**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 도착/실행 시간은 A가 0/8, B가 1/4, C가 2/2입니다. 전환 비용은 0입니다.

1. SJF의 실행 순서는 A(0~8) → C(8~10) → B(10~14)입니다.
2. 대기 시간은 A = 0, B = 9, C = 6이며 평균은 5입니다.
3. SRT의 실행 순서는 A(0~1) → B(1~2) → C(2~4) → B(4~7) → A(7~14)입니다.
4. 대기 시간은 A = 6, B = 2, C = 0이며 평균은 8/3입니다.

**결과·해석:** 같은 작업도 선점 허용과 도착 시간에 따라 결과가 달라집니다.

**전제·주의:** 최적성은 작업의 도착 조건, 실행 시간을 미리 아는지, 전환 비용을 고려하는지에 따라 달라집니다.

### 답안 골격과 혼동 방지

대상과 목표 → SJF·SRT 시간축 → SSTF·SLTF 비교 → 대기·반환 시간 계산 → 기아와 장치별 한계

- SJF의 성능은 작업 도착과 실행 시간 예측 조건에 따라 달라집니다.
- SSTF와 SLTF를 같은 용어로 쓰지 않습니다.

### 내용을 가리고 회상

1. SRT는 언제 실행 중인 작업을 선점합니까?
2. 응답 시간과 반환 시간은 어떻게 다릅니까?
3. HDD의 회전 스케줄링을 SSD에 그대로 적용하기 어려운 이유는 무엇입니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [OSTEP: Scheduling Introduction](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf) — Remzi H. Arpaci-Dusseau; Andrea C. Arpaci-Dusseau / UW-Madison; 공개판 1.10; 확인 2026-11-05. 확인 범위: 저자 공개 교재 PDF 열람. SJF/STCF, 반환·응답 시간과 가정. 제품 규격이나 공식 채점 기준 아님.
- [OSTEP: Hard Disk Drives](https://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf) — Remzi H. Arpaci-Dusseau; Andrea C. Arpaci-Dusseau / UW-Madison; 공개판 1.10; 확인 2026-11-05. 확인 범위: HDD 기하와 탐색·회전 지연 및 스케줄링 PDF 열람. SSD의 현행 지연과 구분.
- [CFS Scheduler](https://docs.kernel.org/scheduler/sched-design-CFS.html) — Linux Kernel documentation; 상시 문서; 확인 2026-11-05. 확인 범위: CFS 가상 실행 시간 원리와 EEVDF로 이행 중임을 알리는 문구 확인. SJF를 Linux 현행 기본 정책이라 주장하지 않음.

## 연관 기출

- [제137회 3교시 1번](../questions/qnet-137-p3.md#q1) — CPU·디스크스케줄링; SJF와SRT; SSTF와SLTF. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
