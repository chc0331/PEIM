---
id: routing-and-prefix-lookup
title: IGP·EGP·RIP·OSPF와 라우팅 탐색
aliases: []
type: concept
domains:
- 네트워크·통신
sources:
- id: source-subnote-e12ae2ef9364
- id: source-subnote-fc789171d698
- id: source-subnote-56d74ada367f
- id: source-subnote-c6210b0cf68d
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# IGP·EGP·RIP·OSPF와 라우팅 탐색

## 서브노트

### 한눈에 이해

경로를 계산해 표를 만드는 일과, 패킷 목적지에 가장 구체적으로 맞는 표 항목을 찾는 일을 구분합니다.

### 정의와 핵심 원리

IGP는 한 자율시스템 내부의 경로 정보를 교환하고 EGP는 자율시스템 사이의 도달성·정책을 교환하는 범주입니다. 대표적IGP에는RIP·OSPF가, 현재 대표적AS간프로토콜에 는 BGP가 있습니다.

- RIP은 거리벡터로 이웃의 거리 정보를 받고 홉수를 사용하며 16을 도달불가로 둡니다. split horizon·poisoned reverse·triggered update등으로 루프·느린수렴을 완화합니다. OSPF는 링크상태를 전파하여 LSDB를 구성하고 최단경로트리를계산하며 area로규모를 관리합니다.
- BGP는AS_PATH등경로속성과정책으로도 달성을교환합니다.EGP라는범주와 역사적EGP프로토콜을 구별합니다.루팅정책은 무조건 최소홉을고르는문제가 아니며경로 검증·필터·인증과 장애수렴을고려합니다.
- 포워딩표검색은Longest Prefix Match가 핵심입니다.일반 BST는 키의 대소비교이지만 IP프리픽스는 포함관계와 길이를다루므로binarytrie·Patricia·다중비트trie·TCAM등을 사용합니다.균형BST의O(logn)을모든 라우팅검색의확정복잡도로 일반 화하지 않습니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| RIP | 거리벡터·홉수 | 단순;15홉상한·수렴 |
| OSPF | 링크상태·SPF·area | 규모·자원·설정 복잡도 |
| BGP | AS경로·정책 | AS간확장·정책 오류 위험 |

<!-- subnote-page:apply -->

### 적용 예제

**가장 긴 프리픽스 선택**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 경로0.0.0.0/0 → A, 10.0.0.0/8 → B, 10.1.0.0/16 → C;목적지10.1.2.3

1. 세 항목이 모두 주소를 포함하는 지 확인합니다.
2. 프리픽스 길이0, 8, 16중16이 가장 길므로C로 보냅니다.
3. 10.2.2.3은/16에 안맞아B를 고릅니다.
4. 표 생성의OSPF최단경로 계산과 표 검색의LPM을 분리해 도식화합니다.

**결과·해석:** 탐색자료 구조의 공통점은 분기 탐색이지만 정렬 키와 매칭조건이 다릅니다.

**전제·주의:** IPv6·하드웨어포워딩·캐시 구조별 구현은 장비별 확인이 필요합니다.

### 답안 골격과 혼동 방지

IGP/EGP범주 → RIP/OSPF 비교 → BGP정책 → 제어·포워딩분리 → BST와LPM예

- OSPF를 단순 홉수프로토콜이라 하지 않습니다.
- 정확한주소일치만찾는검색으로설명하지 않습니다.

### 내용을 가리고 회상

1. 라우팅계산과 LPM의차이는무엇입니까?
2. RIP의16은 무슨뜻입니까?
3. BST대소비교만으로prefix포함관계를 해결할 수 있습니까?

### 적용 기준과 근거

명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [RFC2453: RIP Version 2](https://www.rfc-editor.org/rfc/rfc2453.html) — G. Malkin / IETF; 1998-11; 확인 2026-11-05. 확인 범위: 거리벡터·16 infinity·split horizon 절 열람.
- [RFC2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — J. Moy / IETF; 1998-04; 확인 2026-11-05. 확인 범위: 링크상태·LSDB·최단경로트리·area 개요 열람.
- [RFC4271: Border Gateway Protocol 4](https://www.rfc-editor.org/rfc/rfc4271.html) — Y. Rekhter et al. / IETF; 2006-01; 확인 2026-11-05. 확인 범위: AS 경로·도달성·정책·CIDR 원문 열람.
- [RFC4632: Classless Inter-domain Routing](https://www.rfc-editor.org/rfc/rfc4632.html) — V. Fuller; T. Li / IETF; 2006-08; 확인 2026-11-05. 확인 범위: IPv4 프리픽스·집성 원문 열람. 서브넷 계산은 자체 검산.

## 연관 기출

- [제134회 1교시 8번](../questions/qnet-134-p1.md#q8) — RIP·OSPF비교. 대응: 핵심원리/비교표/예제; 충족.
- [제137회 1교시 1번](../questions/qnet-137-p1.md#q1) — IGP·EGP. 대응: 핵심원리/비교표/예제; 충족.
- [제139회 3교시 5번](../questions/qnet-139-p3.md#q5) — BST와 라우팅테이블탐색상관관계. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
