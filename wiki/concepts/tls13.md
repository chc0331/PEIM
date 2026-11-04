---
id: tls13
title: TLS1.2 구조와 TLS1.3 개선
aliases: []
type: concept
domains:
- 보안·암호
sources:
- id: source-subnote-e28608fb71a7
- id: source-subnote-429a3ebabc89
- path: raw/corrections/2026-11-05-subnotes-review.md
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# TLS1.2 구조와 TLS1.3 개선

## 서브노트

### 한눈에 이해

서로의 신원과 공유키를 합의한 뒤 데이터를 인증 암호로 보호하며, 예전 기능을 제거해 공격 여지를 줄입니다.

### 정의와 핵심 원리

TLS는 전송위에서기밀성·무결성·상대인증을 제공하는 프로토콜입니다. 핸드셰이크로버전·알고리즘·키 자료·서버신원을확인하고 기록 계층에서 협상된키로 응용 데이터를 보호합니다.

- TLS1.3기본 흐름은 ClientHello(key_share등) → ServerHello → 암호화된확장·인증서·CertificateVerify·Finished → 클라이언트Finished입니다. 일반적으로왕복을줄이고PSK재개·선택적클라이언트 인증을 지원합니다. 인증서체인·호스트명·유효상태 검증이 필요합니다.
- TLS1.3은 구식키교환·CBC등많은구형선택지를 제거하고 AEAD및HKDF기반 키스케줄을사용합니다. 인증서서명알고리즘과 키교환·레코드 암호를 별개로협상합니다. 정상적인현행 설정의 TLS1.2전체를이미암호해독가능하다고단정하지 않습니다.
- 0-RTT조기데이터는 지연을 줄이지만 재전송 위험이 있어송금·중복불가행위에 는 별도 방어없이지정하지 않습니다. 핸드셰이크성공뒤에도응용 인가·쿠키·로그·키보관·종단취약점은 남습니다. 전방향안전성은 사용키교환 방식과 운영 조건을 확인합니다.
- TLS 1.2는 Record 계층 위에 Handshake·ChangeCipherSpec·Alert와 응용 데이터를 다룹니다. 인증서 기반 ECDHE·클라이언트 인증 없음·최초 full handshake의 예는 ClientHello → ServerHello·Certificate·ServerKeyExchange·ServerHelloDone → ClientKeyExchange·ChangeCipherSpec·Finished → 서버 ChangeCipherSpec·Finished입니다. ChangeCipherSpec은 Handshake 메시지와 별도 콘텐츠 유형이며 키교환·상호인증·세션 재개 조건에 따라 흐름이 달라집니다.
- 정적 RSA 키교환은 전방향 안전성을 제공하지 않으며 TLS 1.3은 정적 RSA/DH를 제거했습니다. CBC 등 구형 레코드 암호를 제거하고 AEAD만 허용하며, ServerHello 뒤의 핸드셰이크 메시지를 암호화합니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| TLS1.2 | 다양한레거시선택 지원 | 안전한 설정·패치필요 |
| TLS1.3 | 단순 화·AEAD·왕복축소 | 호환성·검사체계변화 |
| 0-RTT | 조기응용 데이터 | 재전송 위험·업무 멱등성 |

<!-- subnote-page:apply -->

### 적용 예제

**조기 데이터와 중복 송금**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 재개세션에 서 송금POST를0-RTT로허용하는가정

1. 네트워크 공격자가조기데이터를 재전송할가능성을위협 모델에 넣습니다.
2. 송금은조기데이터로 받지않거나멱등키·중복 검사를 강제합니다.
3. 인증완료와업무 권한을 검증후원장에 한번만반영합니다.
4. 읽기 요청이라 도부수효과·민감도·재전송 안전을 검토합니다.

**결과·해석:** 프로토콜개선의지연이 익과업무 정합성 위험을 분리합니다.

**전제·주의:** 제품별TLS 설정과 지원 알고리즘은 버전별공식 문서를 확인해야합니다.

### 답안 골격과 혼동 방지

구조 → 핸드셰이크시간축 → 1.2위험·1.3개선 → 0-RTT → 인증 검증·운영

- TLS1.2의모든 구성이취약하다고쓰지않습니다.
- 암호화면인가가 불필요하다고보지않습니다.

### 내용을 가리고 회상

1. TLS1.3이 제거한레거시기능의 의미는 무엇입니까?
2. CertificateVerify와Finished의역할은어떻게다릅니까?
3. 0-RTT에송금을허용하기어려운이유는무엇입니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [RFC8446: TLS1.3](https://www.rfc-editor.org/rfc/rfc8446.html) — Eric Rescorla / IETF; 2018-08; 확인 2026-11-05. 확인 범위: 핸드셰이크·구형 알고리즘 제거·0-RTT 재전송 위험 설명 열람.
- [The Transport Layer Security Protocol Version 1.2](https://www.rfc-editor.org/rfc/rfc5246.html) — T. Dierks, E. Rescorla / IETF; 2008-08; 확인 2026-11-05. 확인 범위: 독립 검수에서 §6·§7.3 Figure1의 full handshake와 계층 구조를 확인했습니다. 키교환·인증·재개 조건에 따라 생략되는 메시지를 구분합니다.

## 연관 기출

- [제136회 2교시 6번](../questions/qnet-136-p2.md#q6) — TLS 구조·핸드셰이크; TLS1.2취약·1.3개선. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
