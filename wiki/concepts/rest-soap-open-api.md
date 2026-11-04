---
id: rest-soap-open-api
title: REST·SOAP·Open API 설계
aliases: []
type: concept
domains:
- 소프트웨어공학
sources:
- id: source-subnote-e49be8a320d5
- id: source-subnote-0925e855af61
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# REST·SOAP·Open API 설계

## 서브노트

### 한눈에 이해

Open API는 공개 범위의 선택이고, REST와 SOAP는 통신을 설계하는 서로 다른 접근입니다.

### 정의와 핵심 원리

Open API는 정해진 계약을 외부 개발자나 시스템에 개방하는 인터페이스입니다. REST는 네트워크 시스템의 아키텍처 제약 집합이고 SOAP는 XML 기반 메시징 프레임워크입니다.

- REST의 제약은 클라이언트-서버, 무상태, 캐시, 일관된 인터페이스, 계층화와 선택적 코드 온 디맨드입니다. 일관된 인터페이스는 자원 식별, 표현을 통한 조작, 자기설명 메시지, 애플리케이션 상태의 하이퍼미디어를 포함합니다. HTTP+JSON이라는 사실만으로 모든 REST 제약을 만족하지 않습니다.
- SOAP 메시지는 Envelope 안에 선택적 Header와 Body를 두며 오류는 Fault로 표현합니다. WSDL은 서비스 계약 기술, WS-Security 등은 별도 관련 규격입니다. SOAP 자체를 HTTP에만 한정하지 않습니다.
- HTTP API는 자원 URI·메서드 의미·상태코드·스키마·버전·페이징·멱등성·오류 응답을 계약으로 명세해야 합니다. GET은 조회, PUT은 대상 표현의 대체, POST는 대상 자원의 의미에 따른 처리를 나타내며 관례와 규범을 구분합니다.
- 공개 시 인증·인가, 객체별 권한, 입력/출력 검증, 속도·용량 제한, 비밀 관리, 변경 공지·폐기 정책, 모니터링이 필요합니다. 특히 로그인 여부 확인만으로 다른 사용자 주문을 열람하게 하면 객체 수준 권한 문제가 남습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·판단 |
| --- | --- | --- |
| Open API | 외부에 제공하는 계약·운영 정책 | REST·SOAP 등 여러 방식 사용 가능 |
| REST | 자원·표현·제약 기반 스타일 | 분산 웹의 확장과 진화 지향 |
| SOAP | Envelope/Header/Body/Fault | 명시적 메시지와 관련 계약 규격 활용 |

<!-- subnote-page:apply -->

### 적용 예제

**강사 창작 적용 예시: 주문 조회 API**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 파트너가 자신의 주문을 조회해야 합니다.

1. GET /orders/{id}와 응답 스키마·오류 코드를 공개합니다.
2. 토큰의 파트너 ID와 주문 소유권을 서버에서 함께 검증합니다.
3. 변경 시 하위 호환·요청 한도·감사로그를 점검합니다.

**결과·해석:** 통신 규약과 공개 서비스의 운영 책임을 함께 제시할 수 있습니다.

**전제·주의:** 보안 취약점의 상세 분류와 대응은 보안 담당 원고와 함께 확인해야 합니다.

### 답안 골격과 혼동 방지

정의·특징·REST 제약 → SOAP 구성요소와 REST 비교 → API 수명주기·취약점 대응 사례

- Open API와 OpenAPI Specification을 같은 용어로 취급하지 않습니다.
- REST의 무상태는 서버에 DB나 자원 상태가 없다는 뜻이 아닙니다.

### 내용을 가리고 회상

1. REST 무상태에서 유지하지 않는 상태는 무엇입니까?
2. SOAP Header와 Body의 역할은 무엇입니까?
3. 인증이 되어도 객체별 인가가 필요한 이유는 무엇입니까?

### 적용 기준과 근거

고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Architectural Styles and the Design of Network-based Software Architectures, Chapter 5](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) — Roy T. Fielding / UC Irvine; 2000; 확인 2026-11-05. 확인 범위: 본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다.
- [SOAP Version 1.2 Part 1: Messaging Framework (Second Edition)](https://www.w3.org/TR/soap12/) — W3C; 2007-04-27; 확인 2026-11-05. 확인 범위: 본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다.

## 연관 기출

- [제133회 1교시 1번](../questions/qnet-133-p1.md#q1) — REST API(REpresentational State Transfer Application Programming Interface)에 대하여 설명하시오.. 대응: 핵심원리/예제/비교표; 충족.
- [제134회 4교시 4번](../questions/qnet-134-p4.md#q4) — 정의 및 특징; SOAP 및 REST 구성요소; 취약점 및 대응 방안. 대응: 핵심원리/예제/비교표; 부분 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
