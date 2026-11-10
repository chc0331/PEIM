---
id: concept-system-programming
title: 시스템 프로그래밍 기초
aliases:
- System programming fundamentals
type: concept
domains:
- 운영체제·컴퓨터구조
sources:
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://man7.org/linux/man-pages/man2/read.2.html
  locator: DESCRIPTION · RETURN VALUE
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://man7.org/linux/man-pages/man2/fork.2.html
  locator: DESCRIPTION · RETURN VALUE
status: 출처 확인
updated: '2026-11-10'
---

# 시스템 프로그래밍 기초

## 한눈에 이해

파일을 읽는 프로그램은 경로와 읽을 크기를 정합니다. 파일 열기와 읽기처럼 운영체제의 권한과 자원이 필요한 작업은 시스템 호출 인터페이스를 통해 요청합니다.

### 원리와 답안 흐름

프로세스는 실행 중인 프로그램입니다. 파일을 열면 프로세스에서 열린 파일을 가리키는 번호인 **파일 디스크립터**를 받습니다. Linux의 `read`에 이 번호, 버퍼, 최대 읽기 크기를 넘기면 실제로 읽은 바이트 수를 받습니다. `fork`는 프로세스를 새로 만드는 호출의 예입니다. 파일을 읽을 때마다 새 프로세스를 만들 필요는 없습니다.

답안에는 **응용 프로그램의 요청 → 운영체제가 관리하는 자원 → 반환값에 따른 분기**를 순서대로 씁니다.

### 적용 예제

교육용 예입니다. Linux에서 이미 열린 일반 파일에 3바이트만 남아 있고, 버퍼에 최대 8바이트를 요청한다고 가정합니다. 첫 호출이 3을 반환하면 버퍼의 앞 3바이트만 처리합니다. 다음 호출이 0을 반환하면 파일 끝으로 보고 반복을 마칩니다. -1이면 오류 정보를 확인한 뒤 다시 시도할지 결정합니다.

### 회상과 답안 확인

- 읽기 요청이 8바이트인데 반환값이 3이면 몇 바이트를 처리해야 하나요? 0과 -1은 어떻게 구별하나요?
- 답안에서 요청한 길이와 실제 길이를 구분하고, 파일 끝과 오류에 각각 맞는 처리를 제시하면 됩니다.

## 출처와 관련 학습

- [Linux man-pages, read(2)](https://man7.org/linux/man-pages/man2/read.2.html) · Linux man-pages project · DESCRIPTION · RETURN VALUE. 파일 디스크립터와 읽은 바이트 수, EOF, 오류 반환을 확인했습니다.
- [Linux man-pages, fork(2)](https://man7.org/linux/man-pages/man2/fork.2.html) · Linux man-pages project · DESCRIPTION · RETURN VALUE. 자식 프로세스 생성과 부모·자식의 반환값을 확인했습니다.
- [과정 대조표의 해당 항목](../comparisons/qnet-2027-curriculum-map.md#qnet-system-programming)
- [관련 위키 노트](process-memory.md)
- [출처 확인 기록](../../raw/sources/2026-11-10-foundation-references.md)
