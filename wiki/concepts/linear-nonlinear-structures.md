---
id: linear-nonlinear-structures
title: 선형·비선형 자료구조와 스택·큐·리스트 입출력
aliases: []
type: concept
domains:
- 자료구조·알고리즘
sources:
- id: source-subnote-5049a48a20fa
- id: source-subnote-4108fa3c8647
- id: source-subnote-1c77fbe050a9
- id: source-subnote-a6b26449161b
- id: source-subnote-366123cbd8b7
- id: source-subnote-2d4d3c31545f
- id: source-subnote-78a93fdfa4e6
- id: source-subnote-c00c13ee1593
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
related_terms:
- 선형 자료구조
- 비선형 자료구조
- 스택
- 큐
- 리스트
- 트리
- 그래프
---

# 선형·비선형 자료구조와 스택·큐·리스트 입출력

## 서브노트

### 한눈에 이해

줄을 선 사람처럼 한 순서로 나열하면 선형이고, 조직도나 도로망처럼 가지와 연결을 표현하면 비선형입니다. 실제 메모리에 붙어 있는지와 논리적으로 한 줄인지는 별개입니다.

### 정의와 핵심 원리

자료구조는 데이터 사이의 논리적 관계와 저장·접근·변경 연산을 조직하는 방식입니다. 선형 구조는 원소가 순차 관계로 이어지고, 비선형 구조는 계층 또는 망 관계를 표현합니다.

- 선형 유형은 배열·리스트·스택·큐입니다. 배열은 인덱스로 접근하고 리스트는 순서와 위치에 따라 삽입·조회·삭제합니다. 스택·큐는 허용 연산과 출입 순서를 정한 추상 자료형이며 배열이나 연결 리스트로 구현할 수 있습니다.
- 스택은 top 한쪽에서 push·pop하는 LIFO입니다. 큐는 rear로 enqueue하고 front에서 dequeue하는 FIFO입니다. 원형 배열은 인덱스를 (i+1) mod 용량으로 순환시키며 공백·포화 구분 규칙이 필요합니다.
- 리스트에는 스택·큐처럼 고정된 제거 순서가 없습니다. 배열 리스트의 중간 삽입·삭제는 뒤 원소를 이동합니다. 단일 연결 리스트는 앞 노드를 찾은 뒤 링크를 바꿉니다. 노드 위치를 찾는 O(n)과 이미 찾은 위치의 O(1) 연결 변경을 구분합니다.
- 비선형 유형은 트리와 그래프입니다. 트리는 부모·자식 계층이며 연결된 무방향 비순환 트리는 |E|=|V|-1입니다. 그래프는 G=(V,E)의 임의 연결로 방향·가중치·순환을 표현합니다. 배열로 트리를 구현하거나 리스트로 그래프를 구현해도 논리 분류는 바뀌지 않습니다.

### 구조·비교·판단

| 구분 | 관계·입출력 | 적용·주의 |
| --- | --- | --- |
| 선형 | 일렬 순서; 배열·리스트·스택·큐 | 순차 처리; 물리적 연속 저장과 별개 |
| 비선형 | 계층·망; 트리·그래프 | 탐색·경로·종속관계 표현 |
| 스택 | push/pop 모두 top; LIFO | 호출·되돌리기; 보통 O(1) |
| 큐 | rear 삽입/front 제거; FIFO | 대기열·BFS; 연결 큐는 양 끝 관리 |
| 리스트 | 위치 지정 삽입·조회·삭제 | 배열 임의 접근 O(1), 연결 탐색 O(n) |

<!-- subnote-page:apply -->

### 적용 예제

**동일 입력의 다른 출력과 연결 변경**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 서로 독립된 빈 스택·큐·리스트에 A,B,C를 차례로 넣습니다.

1. 스택은 bottom [A,B,C] top이므로 pop 결과 C,B,A입니다. 큐는 front [A,B,C] rear이므로 dequeue 결과 A,B,C입니다.
2. 0부터 세는 리스트 [A,B,C]의 위치 1에 X를 넣으면 [A,X,B,C]입니다. 위치 2의 B를 삭제하면 [A,X,C]입니다.
3. 배열에서는 삽입 때 B·C 두 원소를 오른쪽 이동합니다. 연결 리스트에서는 A를 찾은 후 X.next=B, A.next=X로 잇습니다. B 삭제는 X.next=C로 변경합니다.

**결과·해석:** 출력 규칙은 추상 자료형, 이동·링크 변경은 구현의 차이입니다.

**전제·주의:** 크기 조절 배열은 확장 한 번에 O(n), 반복 push의 분할상환 비용은 O(1)이 될 수 있습니다.

### 답안 골격과 혼동 방지

자료구조와 논리/물리 구분 → 선형 개념·4유형 → 비선형 개념·트리/그래프 → 관계·접근·변경·적용 비교 → 입출력 순서와 리스트 이동/링크 예시

- 스택·큐를 각각 배열·연결 리스트와 동의어로 쓰지 않습니다.
- 리스트를 항상 FIFO로 설명하거나 연결 리스트의 위치 탐색 비용을 생략하지 않습니다.

### 내용을 가리고 회상

1. A,B,C 입력 후 스택·큐의 첫 출력은 각각 무엇입니까?
2. 연결 리스트 삽입이 O(1)이라고 말하려면 어떤 조건이 필요합니까?
3. 배열에 저장한 이진트리의 논리 구조는 선형입니까?

### 적용 기준과 근거

2026-11-05 원출처 열람에 따른 강사 생성 설명·자체 예제입니다. 공식 기출 해설이 아닙니다. 배열/연결 구현과 추상 자료형의 분류 축을 구분했습니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Dictionary of Algorithms and Data Structures: array](https://xlinux.nist.gov/dads/HTML/array.html) — NIST / Paul E. Black; 2016-11-16 수정; 확인 2026-11-05. 확인 범위: 실제 열람: 정수 인덱스의 임의 접근, 고정 크기·동적 배열, 중간 삽입 이동 비용. 논리 순서와 물리 저장방식을 구별하는 근거입니다.
- [Dictionary of Algorithms and Data Structures: list](https://xlinux.nist.gov/dads/HTML/list.html) — NIST / Paul E. Black; 웹 항목; 수정일은 이번 열람에서 확인하지 않음; 확인 2026-11-05. 확인 범위: 실제 열람: head부터 tail까지 순차 접근하는 항목 집합, 연결·이중연결·원형 리스트 유형. 리스트를 FIFO/LIFO로 고정하지 않습니다.
- [Dictionary of Algorithms and Data Structures: linked list](https://xlinux.nist.gov/dads/HTML/linkedList.html) — NIST / Paul E. Black; 2022-01-24 수정; 확인 2026-11-05. 확인 범위: 실제 열람: 다음 항목 링크·head 포인터·순차 탐색 및 스택·큐 구현에 사용 가능함. 위치를 이미 아는 경우의 링크 변경과 위치 탐색 비용을 분리해 설명합니다.
- [Dictionary of Algorithms and Data Structures: stack](https://xlinux.nist.gov/dads/HTML/stack.html) — NIST / Paul E. Black; 웹 항목; 수정일은 이번 열람에서 확인하지 않음; 확인 2026-11-05. 확인 범위: 실제 열람: 최근 추가 원소를 먼저 제거하는 LIFO, top·push·pop·isEmpty와 연산 정의.
- [Dictionary of Algorithms and Data Structures: queue](https://xlinux.nist.gov/dads/HTML/queue.html) — NIST / Paul E. Black; 웹 항목; 수정일은 이번 열람에서 확인하지 않음; 확인 2026-11-05. 확인 범위: 실제 열람: tail에 enqueue, head에서 dequeue하는 FIFO 정의. 우선순위 큐와 일반 FIFO 큐를 구분합니다.
- [Dictionary of Algorithms and Data Structures: tree](https://xlinux.nist.gov/dads/HTML/tree.html) — NIST / Paul E. Black 등; 2017-12-15 수정; 확인 2026-11-05. 확인 범위: 실제 열람: root·parent·child·subtree 및 연결된 무방향 비순환 그래프로서의 트리 정의. 자료구조의 순서 있는 이진트리와 그래프 이론의 트리 정의 차이도 확인했습니다.
- [Dictionary of Algorithms and Data Structures: graph](https://xlinux.nist.gov/dads/HTML/graph.html) — NIST / Paul E. Black / Paul J. Tanenbaum; 2022-07-18 수정; 확인 2026-11-05. 확인 범위: 실제 열람: G=(V,E), 방향·무방향·가중 그래프와 인접 리스트/인접 행렬 연결. |V|·|E|는 문자열 그대로 보존하며 메모리 차이는 교과적 계산 예시로 설명합니다.
- [Algorithms, 4th edition, 1.3 Bags, Queues, and Stacks](https://algs4.cs.princeton.edu/13stacks/) — Robert Sedgewick / Kevin Wayne; Algorithms 4판 공개 교재; 페이지 날짜 미확인; 확인 2026-11-05. 확인 범위: 웹 도구 403 후 공식 HTML 직접 다운로드로 실제 열람: FIFO/LIFO, 배열·크기 조절 배열·연결 리스트 구현, 연결 리스트의 앞쪽 삽입/삭제·큐 enqueue/dequeue. 리사이징 한 번의 비용과 분할상환 비용을 구분합니다.

## 연관 기출

- [제131회 3교시 2번](../questions/qnet-131-p3.md#q2) — 선형 구조 개념·유형; 비선형 구조 개념·유형; 선형·비선형 비교. 대응: 정의·핵심원리·비교; 충족.
- [제132회 2교시 6번](../questions/qnet-132-p2.md#q6) — 스택 자료 입출력 원리; 큐 자료 입출력 원리; 리스트 자료 입출력 원리. 대응: 핵심원리·입출력 및 연결 변경 예시; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
