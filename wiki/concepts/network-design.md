---
id: concept-network-design
title: 네트워크 설계 기초
aliases:
- Network design fundamentals
type: concept
domains:
- 네트워크·통신
sources:
- path: raw/sources/2026-11-10-foundation-references.md
  url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html
  locator: Campus Wired LAN · Hierarchical design · High availability
status: 출처 확인
updated: '2026-11-10'
---

# 네트워크 설계 기초

## 한눈에 이해

네트워크를 설계할 때는 먼저 누가 어디에서 어떤 서비스에 접속하고, 어떤 장애까지 견뎌야 하는지 정합니다. 그러면 망을 어떻게 나누고 어느 구간을 이중화할지 판단할 수 있습니다.

### 원리와 답안 흐름

사용자와 서비스 사이의 트래픽을 그린 뒤 주소 대역과 망의 경계를 정합니다. 접속 계층은 단말을 연결하고 분배 계층은 접속 구간을 묶습니다. 큰 망에서는 코어가 여러 분배 구간을 연결합니다. 규모와 장애 영향에 따라 분배·코어 기능을 합칠 수 있습니다. 망을 나눴다면 구간 사이에서 허용할 통신도 정합니다.

답안에는 **요구와 트래픽 → 주소·배치 → 접근 정책·장애 대응 → 검증 방법**을 연결합니다.

### 적용 예제

교육용 예입니다. 직원과 방문객이 같은 사무실에서 무선망을 사용하고, 직원만 내부 업무 서버에 접속할 수 있어야 합니다. 두 사용자군의 망과 주소를 구분하고 방문객 망에서는 인터넷으로 가는 트래픽만 허용합니다. 업무에 필요한 상향 링크에는 대체 경로를 설계합니다. 시험에서는 방문객의 내부 접속 차단, 직원의 정상 접속, 링크 하나를 끊었을 때의 복구 시간을 확인합니다.

### 회상과 답안 확인

- 방문객과 직원을 주소 대역으로만 나누면 요구를 충족하나요?
- 경계에서 접근 정책을 적용하고, 정상 접근·차단·장애 전환을 각각 시험해야 한다고 설명하면 됩니다.

## 출처와 관련 학습

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) · Cisco · Campus Wired LAN · Hierarchical design · High availability. 접속·분배·코어의 역할과 가용성 설계 사례를 확인했습니다.
- [과정 대조표의 해당 항목](../comparisons/qnet-2027-curriculum-map.md#qnet-network-design)
- [관련 위키 노트](ipv4-subnetting-vlsm.md)
- [출처 확인 기록](../../raw/sources/2026-11-10-foundation-references.md)
