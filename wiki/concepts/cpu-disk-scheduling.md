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

CPU에 서 는 짧은 일을 먼저 할지, 디스크에서 는 헤드 이동과 회전을 얼마나 줄일지 목적에 맞게 순서를 정합니다.

### 정의와 핵심 원리

CPU 스케줄링은 실행 가능한 작업에 CPU를 배분하는 정책이고 디스크 스케줄링은 대기 중인 I/O 요청의 서비스 순서를 정하는 정책입니다. 대기·반환·응답 시간·처리량·공정성의 절충이 다릅니다.

- SJF는 준비된작업중예측실행 시간이 가장짧은것을비선점실행합니다.SRT또는STCF는 남은시간이 가장짧은작업을 고르며더짧은작업 도착시선점합니다.미래CPU버스트의정확한예측이어렵고긴작업의 기아를완화해야합니다.
- HDD의SSTF는 현재 헤드위치에서탐색거리가짧은요청을 선택하고 SLTF는 회전대기 시간이 짧은요청을 선택합니다.최단탐색이최단접근 시간전체를항상 뜻하지 않으며탐색·회전·전송 비용을 구분합니다.
- CPU대기 시간=반환 시간-실행 시간, 반환 시간=완료-도착입니다.SSD/NVMe에는기계적헤드·회전이없으므로HDD정책을 동일하게적용하지 않습니다.Linux의실제 정책도 SJF와 구분하며 CFS·EEVDF같은 공정성 정책은 별개입니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| SJF | 짧은버스트;비선점 | 예측필요·긴작업기아 |
| SRT | 짧은잔여시간;선점 | 응답개선·전환비용 |
| SSTF/SLTF | 탐색/회전최소화 | HDD특성과 기아고려 |

<!-- subnote-page:apply -->

### 적용 예제

**선점에 따른 대기 시간 차이**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** A도 착0/실행8, B도 착1/실행4, C도 착2/실행2;전환비용0

1. SJF는A0~8, C8~10, B10~14입니다.
2. 대기는A0, B9, C6으로평균5입니다.
3. SRT는A0~1, B1~2, C2~4, B4~7, A7~14입니다.
4. 대기는A6, B2, C0으로평균8/3입니다.

**결과·해석:** 같은 작업도 선점허용과도착 시간에 따라 결과가 달라집니다.

**전제·주의:** 최적성주장은도착 조건·실행 시간기지·전환비용 가정에 의존합니다.

### 답안 골격과 혼동 방지

대상과 목표 → SJF/SRT시간축 → SSTF/SLTF비교 → 대기·반환계산 → 기아·장치별한계

- SJF가 모든 현실조건에 서 최선이라쓰지않습니다.
- SSTF와SLTF를 같은 용어로 쓰지않습니다.

### 내용을 가리고 회상

1. SRT는 어떤때선점합니까?
2. 응답 시간과 반환 시간은 어떻게다릅니까?
3. SSD에HDD회전스케줄링을그대로적용할 수 있습니까?

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
