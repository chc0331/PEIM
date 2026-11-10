---
id: concept-programming-fundamentals
title: 프로그래밍 언어와 응용 소프트웨어 기초
aliases:
- Programming language and application fundamentals
type: concept
domains:
- 소프트웨어·아키텍처
sources:
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://docs.python.org/3.11/tutorial/interpreter.html
  locator: Invoking the Interpreter
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://docs.python.org/3.11/tutorial/controlflow.html
  locator: if · for · Defining Functions
status: 출처 확인
updated: '2026-11-10'
---

# 프로그래밍 언어와 응용 소프트웨어 기초

## 한눈에 이해

응용 프로그램은 입력을 받아 자료형에 맞게 값을 다루고, 조건과 반복에 따라 처리한 결과를 내보냅니다. 답안에서 언어 기능을 설명할 때는 이 흐름에 연결하면 기능이 쓰이는 이유를 보여 줄 수 있습니다.

### 원리와 답안 흐름

입력값을 어떤 자료형으로 다룰지 먼저 정합니다. 조건문은 경우를 나누고 반복문은 여러 입력에 같은 처리를 적용합니다. 함수에는 입력과 반환값을 정해 처리 책임을 나눌 수 있습니다. Python에서는 인터프리터에 스크립트를 전달해 실행할 수 있습니다. 다른 실행 환경을 설명할 때는 언어와 구현을 함께 명시합니다.

답안에는 **실행 환경 → 입력 자료형과 검증 → 처리 흐름 → 출력과 오류 처리**를 씁니다.

### 적용 예제

교육용 예입니다. 수량 입력 `["2", "-1", "3"]`을 정수로 변환해 양수만 합산합니다. 반복문에서 각 항목을 읽고 양수이면 더하므로 결과는 5입니다. 숫자로 바꿀 수 없는 문자열이 들어오면 건너뛰고 오류를 기록한다는 규칙을 별도로 둡니다. 입력·검증·합산·결과 표시를 나누면 각 단계의 시험 사례를 만들 수 있습니다.

### 회상과 답안 확인

- Python에서 `"2" + "3"`과 `2 + 3`의 결과는 어떻게 다르나요?
- 자료형 변환, 양수 조건, 잘못된 입력의 처리 기준과 최종 결과를 설명하면 됩니다.

## 출처와 관련 학습

- [The Python Tutorial 3.11, Using the Python Interpreter](https://docs.python.org/3.11/tutorial/interpreter.html) · Python Software Foundation · Invoking the Interpreter. Python 인터프리터로 명령과 스크립트를 실행하는 예를 확인했습니다.
- [The Python Tutorial 3.11, More Control Flow Tools](https://docs.python.org/3.11/tutorial/controlflow.html) · Python Software Foundation · if · for · Defining Functions. 조건·반복·함수의 동작을 확인했습니다.
- [과정 대조표의 해당 항목](../comparisons/qnet-2027-curriculum-map.md#qnet-programming)
- [관련 위키 노트](process-memory.md)
- [출처 확인 기록](../../raw/sources/2026-11-10-foundation-references.md)
