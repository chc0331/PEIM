---
id: tcp-control
title: TCP 연결·종료·흐름제어·혼잡제어
aliases: []
type: concept
domains:
- 네트워크·통신
sources:
- id: source-subnote-cf23f6ee70bf
- id: source-subnote-1e0d82b20332
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# TCP 연결·종료·흐름제어·혼잡제어

## 서브노트

### 한눈에 이해

상대 수신기가 감당할 양과 중간 네트워크가 감당할 양을 따로 관리하면 서 손실된 바이트를 복구합니다.

### 정의와 핵심 원리

TCP는 바이트 스트림에 순서·재전송·중복 제거를 제공하는 연결지향 전송 프로토콜입니다. 수신 측 버퍼 보호인 흐름제어와 경로 과부하 완화인 혼잡제어는 목적과 윈도우가 다릅니다.

- 연결은 SYN → SYN+ACK → ACK로 양측 초기 순서 번호를 확인합니다. SYN·FIN은 순서 번호 공간을 하나 사용하지만 데이터 없는 ACK는 소비하지 않습니다. 각 방향 종료가 독립적이어서 FIN/ACK가 보통 네 교환으로 설명되지만 병합도 가능합니다.
- 송신 가능량은 cwnd와 수신 통지 rwnd 중 작은 값에 제한됩니다. 슬라이딩 윈도우는 확인된 바이트만큼 시작점을 옮겨 여러 미확인 데이터를 파이프라인으로 보냅니다. ACK는 전송량과 손실 복구를 진행시키는 신호입니다.
- RFC5681의 slow start는 ACK에 따라 창을 빠르게 늘리고 ssthresh를 넘으면 대체로 RTT당 약1MSS씩 증가시킵니다. 중복ACK와 재전송 타이머로 손실을 감지하며 fast retransmit/recovery 및 timeout 대응은 다릅니다. CUBIC·ECN 등 현행 변형을 구분합니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| 흐름제어 | rwnd;수신 버퍼 보호 | 수신기 상태가 기준 |
| 혼잡제어 | cwnd;경로 과부하 완화 | 손실·지연·ECN 등 신호 |
| 오류제어 | ACK·재전송·순서 번호 | 신뢰성과 중복 제거 |

<!-- subnote-page:apply -->

### 적용 예제

**창과 재전송 타이머**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** cwnd12MSS, rwnd8MSS, 미확인5MSS;전통적RFC5681 가정

1. 새 송신 여유는 min(12, 8)-5=3MSS입니다.
2. timeout 전 FlightSize8MSS이면 ssthresh는 최대 max(8/2, 2)=4MSS입니다.
3. timeout 후 cwnd는1MSS로 줄여 slow start로 복구합니다.
4. 3중복ACK 경로와 timeout 경로를 같은 창 변화로 그리지 않습니다.

**결과·해석:** 수신 버퍼·혼잡·손실의 제약을 분리하여 계산합니다.

**전제·주의:** 이 예는 명시한 고전 정책이며 모든 TCP 구현의 초기창·혼잡반응을 보장하지 않습니다.

### 답안 골격과 혼동 방지

연결·종료 시간축 → 순서 번호·ACK → rwnd/cwnd 비교 → 4혼잡 알고리즘 → 창 계산

- TCP가 메시지 경계를 보존한다고 쓰지 않습니다.
- FIN은 즉시 양방향 전체 종료를 뜻하지 않습니다.

### 내용을 가리고 회상

1. 흐름제어와 혼잡제어의 보호 대상은 무엇입니까?
2. SYN의 ACK값이 1증가하는 이유는 무엇입니까?
3. timeout과 중복ACK복구를 구분해야 하는 이유는 무엇입니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [RFC9293: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — W. Eddy (ed.) / IETF; 2022-08; 확인 2026-11-05. 확인 범위: TCP 연결·종료·순서 번호와 3-way handshake Figure6 직접 열람.
- [RFC5681: TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681.html) — M. Allman; V. Paxson; E. Blanton / IETF; 2009-09; 확인 2026-11-05. 확인 범위: slow start, avoidance, fast retransmit/recovery, cwnd/ssthresh 식 열람. CUBIC 등 모든 현행 구현의 동일 동작을 뜻하지 않음.

## 연관 기출

- [제130회 3교시 3번](../questions/qnet-130-p3.md#q3) — 혼잡제어 구성·감지·제어·윈도우. 대응: 핵심원리/비교표/예제; 충족.
- [제133회 1교시 13번](../questions/qnet-133-p1.md#q13) — 3-way·4-way handshake. 대응: 핵심원리/비교표/예제; 충족.
- [제137회 3교시 5번](../questions/qnet-137-p3.md#q5) — 오류·혼잡제어; 슬라이딩윈도우; 설계고려사항. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
