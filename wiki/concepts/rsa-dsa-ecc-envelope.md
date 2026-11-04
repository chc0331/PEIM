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

RSA는 모듈러거듭제곱과정수인수분해난점에기반한 공개 키계열이며 DSA는 이산로그 기반서명알고리즘입니다. ECC는 타원곡선군에서의이산로그난점을이용하는계열로ECDH·ECDSA등을 포함합니다. 전자봉투는대칭암호문과 수신자용으로보호한데이터 키를 묶습니다.

- RSA는 n=pq, 공개지수e, 비밀지수d를 구성하지만실제 암호화·서명에는OAEP·PSS등검증된인코딩이필요합니다. 원시RSA의 작은 정수예를그대로안전한 실무암호라하면 안됩니다.
- DSA/ECDSA의 서명nonce재사용·편향은개인키를 노출할 수 있습니다.FIPS186-5는DSA신규서명생성을승인하지 않고기존 서명검증을 허용합니다. 2022기출의원리비교와현행 선택권고를구분합니다. ECC의 짧은키는 동일보안수준의적절한 곡선·파라미터비교조건에 서 판단합니다.
- 전자봉투생성은난수데이터 키 → 대칭암호화 → 수신자 공개 키로 키 보호 → 알고리즘·수신자 정보와 패키징입니다. 개봉은개인키로 키 복구 → 암호문 인증·복호입니다. 기밀 봉투만으로송신자의 서명이자동생성되지는않습니다.

### 구조·비교·판단

| 구분 | 핵심 원리 | 적용·한계 |
| --- | --- | --- |
| RSA | 암호화·서명스킴 | OAEP/PSS·키 길이·인증 |
| DSA | 서명전용 | nonce·구판현행구분 |
| ECC | ECDH·ECDSA등계열 | 곡선·검증·nonce |

<!-- subnote-page:apply -->

### 적용 예제

**RSA 장난감 계산 검산**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** p3, q11, n33, φ20, e3, d7;평문m4

1. e×d=21≡1(mod20)입니다.
2. 암호문c=4³ mod33=64 mod33=31입니다.
3. 복호31⁷ mod33=4입니다.
4. 실제 암호는 큰키와 안전한 패딩·난수·검증을 사용합니다.

**결과·해석:** 암·복호의 수학관계를 확인하고 스킴수준보안을별도로설명합니다.

**전제·주의:** 작은 p/q와textbookRSA는 보안용으로사용하지 않습니다.

### 답안 골격과 혼동 방지

세계열비교 → 키·서명원리 → 전자봉투양방향도식 → 정수계산 → 현행 DSA 상태

- DSA를 기밀암호화 알고리즘이라 쓰지않습니다.
- 서명을개인키 암호화의 단순 역연산으로 만설명하지 않습니다.

### 내용을 가리고 회상

1. 전자봉투의본문과키는 각각 어떻게보호합니까?
2. DSA와 RSA의 기능차이는무엇입니까?
3. nonce재사용은왜치명적입니까?

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
