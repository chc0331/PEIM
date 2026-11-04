---
id: spring-boot-aop
title: Spring Boot와 AOP
aliases: []
type: concept
domains:
- 소프트웨어공학
sources:
- id: source-subnote-b6fc716e051f
- id: source-subnote-e338225b5a4a
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# Spring Boot와 AOP

## 서브노트

### 한눈에 이해

Boot는 반복 설정을 줄여 실행을 시작하게 돕고, AOP는 여러 기능에 흩어진 공통 관심을 따로 모읍니다.

### 정의와 핵심 원리

Spring Boot는 자동설정·의존성 관리와 실행 지원으로 Spring 애플리케이션 구성을 단순화합니다. AOP는 로깅·권한·트랜잭션처럼 여러 객체에 걸친 횡단 관심을 Aspect라는 모듈로 분리하는 접근입니다.

- Boot 자동설정은 클래스패스 의존성, 정의된 빈, 설정값 같은 조건을 보고 필요한 구성을 등록합니다. 사용자가 명시한 DataSource 등이 있으면 관련 기본 설정이 물러날 수 있고, 조건 평가 보고서로 적용 근거를 점검할 수 있습니다.
- starter는 관련 의존성 묶음을 일관되게 가져오도록 돕고 외부설정은 환경별 값을 코드와 구분합니다. 실행 가능한 애플리케이션과 내장 서버, 운영 엔드포인트 등은 구성 부담을 줄이지만 자동 선택된 설정을 이해하고 노출 범위를 통제해야 합니다.
- AOP의 Aspect는 관심 모듈, Join Point는 적용 가능한 실행 지점, Pointcut은 지점 선택식, Advice는 그 지점에서 수행할 동작, Weaving은 적용 결합입니다. Spring AOP는 주로 프록시를 통해 메서드 실행을 가로챕니다.
- 공통 로깅이나 트랜잭션 처리를 업무 코드에서 분리하면 중복을 줄일 수 있으나 프록시를 거치지 않는 내부 자기호출, 적용 순서, 예외/트랜잭션 전파를 고려해야 합니다. AOP가 객체지향을 대체하지는 않습니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·판단 |
| --- | --- | --- |
| Spring | 객체 생성·의존성·애플리케이션 기반 | 명시 구성과 확장 |
| Spring Boot | 조건 기반 자동설정·실행 편의 | 기본값과 실제 적용을 검토 |
| AOP | 횡단 관심의 분리·적용 | 선택한 메서드 경계에서 정책 실행 |

<!-- subnote-page:apply -->

### 적용 예제

**강사 창작 적용 예시: 결제 처리 로그 분리**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 결제·취소·환불 메서드에 수행시간 코드가 반복됩니다.

1. Boot로 웹·DB 의존성을 구성하고 자동설정 결과를 확인합니다.
2. 결제 서비스 메서드를 선택하는 Pointcut과 시간 측정 Around Advice를 정의합니다.
3. 정상·예외 경로와 프록시를 경유하지 않는 자기호출을 시험합니다.

**결과·해석:** 업무 계산식과 공통 계측의 책임을 나눌 수 있습니다.

**전제·주의:** 실제 결제정보나 인증정보를 로그에 남기는 설계는 피해야 합니다.

### 답안 골격과 혼동 방지

Boot 특징과 자동설정 → AOP 구성·적용 흐름 → 기대효과·프록시 한계와 사례

- 자동설정은 모든 설정을 마법처럼 최적화하지 않습니다.
- Spring AOP와 AspectJ의 전체 weaving 범위를 같다고 보지 않습니다.

### 내용을 가리고 회상

1. 자동설정이 물러나는 조건의 예는 무엇입니까?
2. Pointcut과 Advice는 어떻게 다릅니까?
3. 자기호출에서 Advice가 누락될 수 있는 이유는 무엇입니까?

### 적용 기준과 근거

열람 화면은 Boot4.1.2/Framework7.0.10입니다. 기출은 이전 세대이므로 세부 버전 요구와 API는 당시 문서와 구분해야 합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Auto-configuration](https://docs.spring.io/spring-boot/reference/using/auto-configuration.html) — Spring; 열람 화면 Spring Boot 4.1.2; 확인 2026-11-05. 확인 범위: 현재 문서 열람. 기출 당시 Spring Boot 세대와 차이가 있으므로 특정 Java 최소버전·패키지명을 일반화하지 않습니다.
- [Aspect Oriented Programming with Spring](https://docs.spring.io/spring-framework/reference/core/aop.html) — Spring; 열람 화면 Spring Framework 7.0.10; 확인 2026-11-05. 확인 범위: 본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다.

## 연관 기출

- [제127회 1교시 6번](../questions/qnet-127-p1.md#q6) — 스프링 부트(Spring Boot). 대응: 핵심원리/예제/비교표; 충족.
- [제129회 1교시 3번](../questions/qnet-129-p1.md#q3) — AOP(Aspect Oriented Programming)의 정의, 구성, 기대효과. 대응: 핵심원리/예제/비교표; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
