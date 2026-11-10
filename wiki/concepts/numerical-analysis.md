---
id: concept-numerical-analysis
title: 수치해석 기초
aliases:
- Numerical analysis fundamentals
type: concept
domains:
- 운영체제·컴퓨터구조
sources:
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://dlmf.nist.gov/3.8
  locator: §3.8(i), §3.8(iii) Bisection Method
status: 출처 확인
updated: '2026-11-10'
---

# 수치해석 기초

## 한눈에 이해

정확한 해를 한 번에 구하기 어려울 때는 근삿값을 계산하고, 오차가 어느 정도인지 함께 확인합니다. **수렴**은 반복 횟수를 늘릴 때 근삿값이 어떤 값에 한없이 가까워지는 성질입니다. 허용 오차는 계산을 언제 멈출지 정하는 기준입니다.

### 원리와 답안 흐름

함수가 구간에서 연속이고 양 끝 함수값의 부호가 반대라면 그 사이에 근이 있습니다. **이분법**은 중점을 구한 뒤 양 끝의 부호가 다른 절반을 남깁니다. 중점에서 함수값이 0이면 그 값이 근입니다. 근이 들어 있는 구간의 중점을 답으로 쓰면, 구간 길이의 절반이 절대오차의 상한입니다.

답안에는 **시작 구간과 조건 → 반복 규칙 → 중단 조건과 오차 상한**을 씁니다.

### 적용 예제

교육용 예입니다. `f(x) = x² - 2`의 양의 근을 `[1, 2]`에서 찾습니다. 첫 중점 1.5에서는 함수값이 0.25이므로 `[1, 1.5]`를 남깁니다. 다음 중점 1.25에서는 음수이므로 `[1.25, 1.5]`를 남깁니다. 이 구간의 중점 1.375를 답으로 쓰면 오차는 최대 0.125입니다.

### 회상과 답안 확인

- 허용 절대오차가 0.05라면 위 단계에서 멈출 수 있나요?
- 현재 상한 0.125가 0.05보다 크므로 반복을 계속하고, 남은 구간 길이의 절반이 0.05 이하일 때 멈춘다고 설명하면 됩니다.

## 출처와 관련 학습

- [Digital Library of Mathematical Functions](https://dlmf.nist.gov/3.8) · NIST · §3.8(i), §3.8(iii) Bisection Method. 반복 계산의 수렴과 이분법으로 근을 좁히는 원리를 확인했습니다.
- [과정 대조표의 해당 항목](../comparisons/qnet-2027-curriculum-map.md#qnet-numerical)
- [관련 위키 노트](algorithm-complexity-big-o.md)
- [출처 확인 기록](../../raw/sources/2026-11-10-foundation-references.md)
