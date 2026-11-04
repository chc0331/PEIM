---
id: uml-dice-model
title: UML 주사위 게임의 객체·시퀀스·클래스 모델
aliases: []
type: concept
domains:
- 소프트웨어공학
sources:
- id: source-subnote-5540c055483d
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
related_terms:
- 개념적 객체 모델
- Sequence Diagram
- Class Diagram
---

# UML 주사위 게임의 객체·시퀀스·클래스 모델

## 서브노트

### 한눈에 이해

같은 게임도 개념 모델은 무엇이 있는지, 시퀀스는 누가 언제 요청하는지, 클래스 모델은 어떤 책임으로 구현하는지 보여줍니다.

### 정의와 핵심 원리

UML은 시스템의 구조와 행위를 공통 표기로 기술하는 모델링 언어입니다. 이 문항은 두 주사위의 합이 정확히 8일 때 승리한다는 규칙을 세 모델에서 일관되게 표현하는 것이 핵심입니다.

- 개념 객체 모델: 참여자(Player), 주사위게임(DiceGame), 주사위(Die)가 도메인 개념입니다. DiceGame 1개는 Die 2개와 관련되고 Player는 DiceGame에 참여합니다. 단순 도메인 관계 단계에서는 메서드·DB 키 같은 구현 세부를 먼저 넣지 않습니다.
- 설계 클래스 모델: DiceGame은 die1:Die, die2:Die와 play():Result 책임을 가집니다. Die는 faceValue:Integer {1≤faceValue≤6}, roll():void, getFaceValue():Integer를 가집니다. DiceGame→Die의 다중성은 2이고 게임이 수명주기를 소유한다고 가정할 때만 합성(채운 마름모)을 사용합니다.
- 시퀀스의 생명선 순서는 player:Player, game:DiceGame, die1:Die, die2:Die입니다. player→game:play(); game→die1:roll(); game→die1:getFaceValue()→v1; game→die2:roll(); game→die2:getFaceValue()→v2; game은 sum=v1+v2를 계산합니다.
- alt [sum=8] 분기에서 win, [else] 분기에서 lose를 참여자에게 반환/표시합니다. 두 주사위는 같은 객체를 두 번 굴린 것이 아니라 구별되는 인스턴스 두 개입니다. 순서는 별도 제약이 없으므로 두 roll의 순차·동시 표현 모두 책임과 값 사용이 일관되면 가능합니다.
- 객체의 한 시점 예는 밑줄 친 game1:DiceGame, d1:Die, d2:Die와 game1—d1, game1—d2 링크이며 d1의 slot faceValue=3, d2는 faceValue=5입니다. 클래스 속성의 값 제약 1~6은 다중성 [1..6]과 다르므로 {1≤faceValue≤6}처럼 제약으로 표기합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·판단 |
| --- | --- | --- |
| 개념 모델 | 도메인 개념·연관·다중성 | 구현 이전 의미 파악 |
| 시퀀스 | 객체 생명선과 시간순 메시지 | 호출 주체·응답·분기 확인 |
| 클래스 | 속성·연산·관계 | 시퀀스 메시지를 받을 책임 제공 |

<!-- subnote-page:apply -->

### 적용 예제

**강사 창작 적용 예시: 합계 8인 게임 실행**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** die1=3, die2=5라는 창작 실행값입니다.

1. Player가 game.play()를 요청합니다.
2. 각 Die가 roll 결과 3과 5를 보관하고 조회에 응답합니다.
3. 게임이 3+5=8을 평가해 win 결과를 표시합니다.

**결과·해석:** 클래스 책임·생명선·승패 가드가 서로 일치합니다.

**전제·주의:** 난수 구현 방식은 문항에 없으므로 특정 라이브러리나 확률분포 보장을 추가하지 않습니다.

### 답안 골격과 혼동 방지

주어진 규칙과 모델링 가정 → 개념 객체·연관·다중성 → 호출 순서·alt 가드 및 설계 클래스 일치

- 일반적인 주사위 게임 규칙으로 합계 7을 쓰면 오답입니다.
- 클래스 이름과 객체 인스턴스 이름을 구분합니다.

### 내용을 가리고 회상

1. 게임과 주사위 사이 다중성은 얼마입니까?
2. 합성을 선택하려면 어떤 가정이 필요합니까?
3. 합계 9의 실행은 어느 가드를 통과합니까?

### 적용 기준과 근거

고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [OMG Unified Modeling Language 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF) — OMG; 2017-12; 확인 2026-11-05. 확인 범위: 공개 PDF를 /tmp에서 텍스트 추출해 Class, Interaction/Sequence, Activities, StateMachines, UseCases 절을 열람했습니다. 127회 문항은 UML2.0을 명시하므로 공통 핵심 표기를 사용합니다.

## 연관 기출

- [제126회 2교시 4번](../questions/qnet-126-p2.md#q4) — 개념적 객체 모델(Conceptual Object Model); 시퀀스 다이어그램(Sequence Diagram); 클래스 다이어그램(Class Diagram). 대응: 핵심원리/예제/비교표; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
