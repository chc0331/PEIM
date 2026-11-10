---
id: rsa-dsa-ecc-envelope
title: RSA·DSA·ECC와 전자봉투
aliases: []
type: concept
domains:
- 보안·암호
sources:
- id: source-subnote-04eae6c819ad
- id: source-subnote-2bf84be7c801
- id: source-subnote-d04c2dcbf10b
- id: source-subnote-4c8d441eeaf9
- path: raw/corrections/2026-11-05-subnotes-review-followup.md
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
---

# RSA·DSA·ECC와 전자봉투

## 서브노트

### 한눈에 이해

암호화·서명·키 설정은 같은 공개 키 수학을 쓰더라도 목적과 안전한 포맷이 다릅니다.

### 정의와 핵심 원리

RSA는 모듈러 거듭제곱을 사용하며 큰 정수의 인수분해가 어렵다는 점과 관련됩니다. DSA는 이산로그 문제를 이용하는 서명 알고리즘입니다. ECC는 타원곡선 위 이산로그 문제를 이용하는 암호 기법의 계열로 ECDH·ECDSA 등을 포함합니다. 전자봉투는 대칭 암호문과 수신자용으로 보호한 데이터 키를 함께 담습니다.

- RSA는 `n = pq`, 공개 지수 `e`, 비밀 지수 `d`로 키를 구성합니다. 실무의 RSA 암호화에는 OAEP, 서명에는 PSS처럼 검증된 인코딩을 사용합니다. 아래 정수 계산은 원리 설명용입니다.
- DSA나 ECDSA에서 서명 nonce를 재사용하거나 치우친 값으로 생성하면 개인 키가 노출될 수 있습니다. FIPS 186-5는 DSA를 기존 서명 검증에만 허용합니다. 2022년 기출의 원리 비교와 현행 선택 기준을 구분합니다. ECC의 키 길이는 곡선과 매개변수를 고려해 같은 보안 수준에서 비교합니다.
- 전자봉투를 만들 때 난수 데이터 키로 본문을 대칭 암호화합니다. 데이터 키는 수신자 공개 키로 보호하고 알고리즘·수신자 정보와 함께 묶습니다. 수신자는 개인 키로 데이터 키를 복구한 뒤 암호문을 인증·복호합니다. 송신자를 입증할 때는 별도로 서명을 검증합니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| RSA | 암호화·서명 방식 | OAEP·PSS, 키 길이·인증 |
| DSA | 서명 전용 | nonce, 표준의 개정 전후 구분 |
| ECC | ECDH·ECDSA 등 | 곡선·검증·nonce |

<!-- subnote-page:apply -->

### 적용 예제

**작은 정수로 RSA 암·복호 계산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** `p = 3`, `q = 11`, `n = 33`, `φ = 20`, `e = 3`, `d = 7`, 평문 `m = 4`입니다.

1. `e × d = 21 ≡ 1 (mod 20)`입니다.
2. 암호문은 `c = 4³ mod 33 = 64 mod 33 = 31`입니다.
3. `31⁷ mod 33 = 4`이므로 원래 평문을 얻습니다.
4. 실제 RSA 암호화는 충분히 큰 키와 검증된 인코딩을 사용합니다.

**결과·해석:** 계산으로 암호화와 복호의 수학적 관계를 확인합니다. 실제 암호화의 안전성은 인코딩과 구현까지 고려해 설명합니다.

**전제·주의:** 작은 소수와 인코딩을 생략한 RSA는 원리 설명용입니다.

### 답안 골격과 혼동 방지

세 계열 비교 → 키·서명 원리 → 전자봉투 양방향 도식 → 정수 계산 → 현행 DSA 상태

- DSA는 서명 알고리즘입니다.
- RSA 서명에서는 서명 방식에 맞게 메시지를 인코딩한 뒤 개인 키 연산을 수행합니다.

### 내용을 가리고 회상

1. 전자봉투의 본문과 키는 각각 어떻게 보호합니까?
2. DSA와 RSA의 기능 차이는 무엇입니까?
3. nonce 재사용은 왜 치명적입니까?

### 적용 기준과 근거

FIPS186-5본문 16쪽DSA 상태 확인;RSA31⁷mod33=4는Pythonpow로직접 검산.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [RFC8017: PKCS#1 v2.2](https://www.rfc-editor.org/rfc/rfc8017.html) — K. Moriarty et al. / IETF; 2016-11; 확인 2026-11-05. 확인 범위: RSA 원시연산·암호화·서명 스킴 구분 열람. 작은 정수 예시는 교육용.
- [FIPS186-5: Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final) — NIST; 2023-02-03; 확인 2026-11-05. 확인 범위: 공식 게재 페이지 및 FIPS186-5 §4(인쇄16쪽)를 독립 검수에서 확인했습니다. DSA는 신규 서명 생성에 승인되지 않고 기존 서명 검증에 사용할 수 있습니다. 표준 전체 재검증은 아닙니다.
- [RFC6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.html) — D. McGrew; K. Igoe; M. Salter / IETF; 2011-02; 확인 2026-11-05. 확인 범위: 타원곡선군·이산로그·공개 키 알고리즘 배경 실제 열람.
- [RFC5652: Cryptographic Message Syntax](https://www.rfc-editor.org/rfc/rfc5652.html) — R. Housley / IETF; 2009-09; 확인 2026-11-05. 확인 범위: 서명·인증·암호화 및 EnvelopedData 구조 개요 열람.

## 연관 기출

- [제126회 4교시 5번](../questions/qnet-126-p4.md#q5) — RSA·DSA비교. 대응: 핵심원리/비교표/예제; 충족.
- [제133회 1교시 4번](../questions/qnet-133-p1.md#q4) — 전자봉투생성·개봉. 대응: 핵심원리/비교표/예제; 충족.
- [제136회 1교시 12번](../questions/qnet-136-p1.md#q12) — ECC. 대응: 핵심원리/비교표/예제; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
