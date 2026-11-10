---
id: concept-system-software-architecture
title: 시스템 소프트웨어 아키텍처와 기술문서
aliases:
- System software architecture documentation
type: concept
domains:
- 운영체제·컴퓨터구조
sources:
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://www.sei.cmu.edu/library/documenting-software-architectures-views-and-beyond-second-edition/
  locator: 2010년 2판 공식 소개
status: 출처 확인
updated: '2026-11-10'
---

# 시스템 소프트웨어 아키텍처와 기술문서

## 한눈에 이해

아키텍처 문서는 시스템의 구성요소와 관계를 보여 줍니다. 운영팀이 장애를 추적할 때와 개발팀이 인터페이스를 바꿀 때 필요한 정보는 서로 다릅니다. 목적에 맞게 같은 시스템을 여러 관점에서 그릴 수 있습니다.

### 원리와 답안 흐름

개발팀에는 모듈의 책임과 의존 관계를, 운영팀에는 실행 위치와 통신 경로를 보여 줍니다. 인터페이스에는 입력·출력, 시간 제한, 오류를 받았을 때의 동작을 적습니다. 품질 요구에는 측정 조건과 통과 기준을 붙이면 설계 판단을 검증하기 쉽습니다.

답안에는 **요구 → 구성요소와 관계 → 인터페이스 → 품질 판단과 시험**을 연결합니다.

### 적용 예제

교육용 예입니다. 프린터 관리 서비스가 대기열에 작업을 넣고 드라이버로 넘깁니다. 모듈 그림에는 접수기·대기열·전송기의 책임을 표시합니다. 실행 그림에는 프로세스 배치와 통신 경로를 표시합니다. 프린터 연결이 끊겼을 때는 전송기가 어떤 오류를 남기고, 이미 접수한 작업을 어떻게 보관할지 설계합니다. 테스트에서는 연결을 끊었다가 복구해 접수 기록과 재전송 결과를 확인합니다.

### 회상과 답안 확인

- 운영팀과 개발팀에 각각 어떤 그림을 주겠습니까? 장애 복구 조건은 문서 어디에 적겠습니까?
- 두 관점의 목적, 오류 인터페이스, 실패를 재현할 시험을 하나씩 연결하면 됩니다.

## 출처와 관련 학습

- [Documenting Software Architectures: Views and Beyond, 2nd Edition](https://www.sei.cmu.edu/library/documenting-software-architectures-views-and-beyond-second-edition/) · CMU Software Engineering Institute · 2010년 2판 공식 소개. 이해관계자에 맞는 관점과 인터페이스·동작 문서화의 범위를 확인했습니다.
- [과정 대조표의 해당 항목](../comparisons/qnet-2027-curriculum-map.md#qnet-system-sw-arch)
- [관련 위키 노트](technical-application-architect.md)
- [출처 확인 기록](../../raw/sources/2026-11-10-foundation-references.md)
