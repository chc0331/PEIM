---
id: socket-sctp-websocket
title: 소켓·WebSocket·SCTP
aliases: []
type: concept
domains:
- 네트워크·통신
sources:
- id: source-subnote-8c504832ca42
- id: source-subnote-bdde15b3166d
- id: source-subnote-cf23f6ee70bf
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# 소켓·WebSocket·SCTP

## 서브노트

### 한눈에 이해

소켓은 통신을 여는 프로그래밍 창구이고, 그 창구에서TCP·UDP·SCTP같은 전송 방식을 선택합니다.

### 정의와 핵심 원리

소켓은 주소·포트 등 종단점을 통해 송수신하는 운영체제 인터페이스입니다. WebSocket은 HTTP 기반 오프닝 이후 TCP 위에서 메시지 프레임을 교환하는 응용 프로토콜이며 SCTP는 메시지 기반의 신뢰성 있는 전송 프로토콜입니다.

- TCP 서버는 socket → bind → listen → accept 후 연결된 소켓으로 송수신하고 클라이언트는 socket → connect를 수행합니다. 스트림의 read/write 한 번이 애플리케이션 메시지 하나와 일치하지 않으므로 길이·구분자 등 프레이밍이 필요합니다.
- UDP는 연결 설정 없이 데이터그램을 교환하며 응용이 손실·순서·혼잡·MTU를 고려해야 합니다. HTTP는 요청·응답 의미를 제공하는 응용 프로토콜이 므로 소켓과 배타적 대안이 아닙니다. WebSocket도 인증·권한·Origin검증과 TLS가 필요합니다.
- SCTP는 association을 만들고 공통헤더와 chunk를 사용합니다. INIT → INIT ACK → COOKIE ECHO → COOKIE ACK의 쿠키 방식, 스트림별 순서화, TSN·SACK, 멀티호밍을 제공합니다. 멀티스트리밍이 모든 종류의 HOL지연을 없애거나 멀티호밍이 자동 대역 합산을 뜻하지는 않습니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| TCP socket | 신뢰성 바이트 스트림 | 응용 프레이밍 필요 |
| WebSocket | 양방향 메시지 프레임 | 브라우저·웹 연계 |
| SCTP | 멀티스트림 메시지·멀티호밍 | 지원망·방화벽·구현 검토 |

<!-- subnote-page:apply -->

### 적용 예제

**실시간 대시보드**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 서버가 초당 상태 변경을 브라우저로 전달

1. 처음 HTTP 오프닝에서 사용자와 Origin을 확인합니다.
2. WebSocket 세션에 서 구독 권한을 검증하고 메시지 크기를 제한합니다.
3. 연결이 끊기면 마지막 이벤트 번호를 기준으로 재동기화합니다.
4. 일반 조회HTTP와 푸시WebSocket의 역할을 나누어 상태를 관리합니다.

**결과·해석:** 소켓API·전송 계층·응용 프로토콜을 계층별로 설명합니다.

**전제·주의:** WebSocket 연결이 살아 있어도 업무 이벤트의 exactly-once 처리는 별도 설계입니다.

### 답안 골격과 혼동 방지

계층과 정의 → 소켓 호출 흐름 → TCP·UDP·WebSocket 비교 → SCTP 구조·쿠키 → 보안·복구

- HTTP를 소켓을 사용하지 않는 통신이라 고 설명하지 않습니다.
- SCTP의 association과TCP 연결을 완전히 같은 기능으로 쓰지 않습니다.

### 내용을 가리고 회상

1. TCP수신에서 프레이밍이 필요한 이유는 무엇입니까?
2. SCTP의 stream과TSN은 어떤 역할입니까?
3. WebSocket의 인증은 연결 이후 에도 왜 필요합니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [RFC9260: Stream Control Transmission Protocol](https://www.rfc-editor.org/rfc/rfc9260.html) — R. Stewart et al. / IETF; 2022-06; 확인 2026-11-05. 확인 범위: SCTP 메시지·멀티스트리밍·멀티호밍·association 설명 열람.
- [RFC6455: The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455.html) — I. Fette; A. Melnikov / IETF; 2011-12; 확인 2026-11-05. 확인 범위: 오프닝 핸드셰이크·TCP 위 메시지 프레이밍·양방향 통신 원문 열람.
- [RFC9293: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — W. Eddy (ed.) / IETF; 2022-08; 확인 2026-11-05. 확인 범위: TCP 연결·종료·순서 번호와 3-way handshake Figure6 직접 열람.

## 연관 기출

- [제131회 2교시 5번](../questions/qnet-131-p2.md#q5) — 소켓 정의·유형; TCP소켓·WebSocket 흐름; HTTP 비교. 대응: 핵심원리/비교표/예제; 충족.
- [제132회 3교시 4번](../questions/qnet-132-p3.md#q4) — SCTP 개요·특징; 구조·동작. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
