# 시스템·보안 서브노트 내용 검수

검수일: 2026-11-05. 대상은 수험 입문자의 토픽별 인쇄 학습노트입니다. `research` 및 `document-content-review`의 검수 기준을 적용했습니다. 원자료·위키·코드는 수정하지 않았습니다.

## 확인 범위

- `raw/research/2026-11-05-systems-security.md`의 72개 토픽 전체 필드와 102개 출처 **메타데이터**를 읽었습니다. 102개 웹 원문을 전수 재열람했다는 뜻은 아닙니다.
- 아래에서 지적한 정의·전제·요구 충족을 대조했고 VLSM, 은행가, SJF/SRT, HPA, RSA, OFB XOR, DP, MPC 합계, FedAvg, 차등 맨체스터를 별도 Python 계산으로 재검산했습니다.
- 공식 기출은 보존된 `raw/exams/qnet/2026-11-01/*/record.json` 중 위험 신호가 있거나 계산·요구 확인이 필요한 14문항의 기계 추출문을 대조했습니다: 127-1-9, 130-2-3, 131-1-4, 131-4-4, 133-1-9, 133-4-1, 136-1-2, 136-2-6, 137-1-8, 138-1-1, 138-3-1, 138-4-1, 138-4-6, 139-4-6. 189문항의 PDF 전체나 그림을 재검수한 것은 아닙니다.
- 후속 교차 확인은 `raw/research/2026-11-05-data-ai.md`의 `foundation-language-multimodal-models` 한 토픽에 한정했습니다. 이 토픽은 개념·특징·기술을 담당하지만 법·환경·사회 세부 고려를 추가 확인 대상으로 남겼고 상태도 부분 충족입니다. 두 담당 토픽을 합쳐도 환경 고려 설명이 현재 완결되어 있지 않습니다.
- 이 파일의 `aliases`는 72개 모두 빈 배열이며 `source_aliases` 필드는 없습니다. 별도 `related_terms`를 다른 개념의 동의어로 저장한 사례는 발견하지 못했습니다. 후속 생성 시 `related_terms`를 자동 별칭으로 복사하지 않아야 합니다.

## 필수 수정

### 1. 켓 표기가 조각나 중첩·간섭 예제가 훼손됨

- 위치: `qubit-quantum-hardware.example.steps` — 원자료 2180행부터의 토픽.
- 원문: `["첫H후(", "0>+", "1>)/√2로…", …, "0>이됩니다."]`
- 근거: ASCII `|`를 단계 구분자로 처리한 흔적입니다. 첫 H의 중첩 상태와 두 번째 H의 결과를 온전한 식으로 읽을 수 없습니다. [IBM 공식 중첩·간섭 교육자료](https://quantum.cloud.ibm.com/learning/en/modules/quantum-mechanics/superposition-with-qiskit)의 H 연산 설명과 대조했습니다. H²=I 및 중간 측정 유무의 차이도 수학적으로 일치합니다.
- 최소 대체값: `example.steps` 전체를 다음으로 교체합니다. 아래 `∣`는 구분자로 쓰인 ASCII 파이프와 다른 문자입니다.

```json
[
  "첫 H 이후 상태는 (∣0⟩+∣1⟩)/√2이며, 계산 기저에서 0과 1의 측정 확률은 각각 1/2입니다.",
  "중간에 측정하지 않고 H를 다시 적용하면 H²=I이므로 상태는 ∣0⟩이 됩니다.",
  "두 H 사이에서 측정해 고전적 혼합 상태로 만든 실험은 중간에 측정하지 않은 실험과 결과가 다릅니다.",
  "샷 수에 따른 표본 오차와 실제 장치의 잡음을 구분합니다."
]
```

72개 토픽의 `principles`와 `example.steps`를 읽고 짧게 분리된 수식 조각도 추가 탐색했습니다. 같은 종류의 파이프 분할 오류는 이 배열 외에는 발견하지 못했습니다. 정의의 `|ψ>` 및 `|α|²`는 현재 문자열 안에 보존되어 있습니다.

### 2. MPC 예제에 share의 무작위 생성·분배 전제가 빠짐

- 위치: `secure-multiparty-computation.example.input`, `.example.steps` — 6623행부터의 토픽.
- 원문: “A는7을20과88로분산합니다”, “두서버는 공모하지 않는가정”.
- 근거: `(20+88) mod 101=7` 등 산술은 맞습니다. 그러나 합이 맞는 두 수를 정하기만 해서는 개별 share의 기밀성이 나오지 않습니다. 첫 share의 균등 무작위 선택, 독립적인 새 난수, 서버별 분리 전달이 있어야 제시한 비공모 모델에서 설명을 재현할 수 있습니다. [저자 공개 교재 Programming MPC의 가산 비밀분산 구성](https://jnear.github.io/programming-mpc/chapters/chapter02.html#building-additive-secret-shares)의 해당 구성 절을 확인했습니다. 페이지의 다른 예제나 전체 교재를 검증한 것은 아닙니다.
- 최소 추가 문구: 기존 수치 예제 앞에 다음 한 단계를 넣고 기존 계산은 유지합니다.

```json
"각 입력 x마다 r을 0~100에서 독립적으로 균등 무작위 선택하고 (r, (x-r) mod 101)을 만듭니다. 첫 share는 서버1에, 둘째 share는 서버2에 비공개로 전달합니다. 아래 20과 30은 이번 예시에서 선택된 난수이며 고정·재사용하는 값이 아닙니다."
```

### 3. 변조·위조를 설명하지 않고 해당 단답을 충족 처리함

- 위치: `hash-mac-password.requirements[2]`, `.principles` — 4832행부터의 토픽.
- 원문: `"items":["변조와위조구분"], "status":"충족"`.
- 근거: 해시·HMAC·저장 보호는 설명하지만 Modification과 Fabrication 자체의 정의·대조 예제가 없습니다. [Q-Net 127회 1교시 9번](https://www.q-net.or.kr/cst006.do?gSite=Q&gId=&id=cst00602&artlSeq=5210065&brdId=Q006&code=1203&cst=Y)은 이 두 개념을 직접 묻습니다. [RFC 4949의 falsification 항목](https://www.rfc-editor.org/rfc/rfc4949.html)은 유효 자료의 변경·대체와 허위 자료의 삽입을 구분합니다. 이는 해당 용어집 저자의 설명이며 별도 의무 표준이라는 뜻은 아닙니다.
- 상태 최소 정정: `requirements[2].status = "부분 충족"`.
- 본문 최소 보완안: 새 원리 항목으로 다음을 추가하고 요구 충족 여부를 다시 판단합니다.

```json
"변조(Modification)는 기존 자료를 권한 없이 변경하는 것으로 송금액을 10에서 100으로 바꾸는 경우입니다. 위조(Fabrication)는 허위 자료·메시지를 진짜처럼 생성·삽입하는 것으로 존재하지 않는 송금 지시를 만드는 경우입니다. 변경 탐지와 생성 주체의 진위 확인을 구분하며, 키 없는 해시만으로는 공격자가 본문과 해시를 함께 새로 만드는 것을 막지 못합니다."
```

### 4. 파운데이션 모델의 법·환경 고려가 빠졌으나 충족으로 표시됨

- 위치: `adversarial-ai-security.requirements[3]`, `.principles` — 7414행부터의 토픽.
- 원문: `"items":["파운데이션모델 법·환경·사회고려"], "status":"충족"`.
- 근거: 이 토픽은 공격·프라이버시·사회적 위험을 설명하지만 법적 검토와 환경적 고려를 설명하지 않습니다. [Q-Net 131회 4교시 4번](https://www.q-net.or.kr/cst006.do?gSite=Q&gId=&id=cst00602&artlSeq=5212292&brdId=Q006&code=1203&cst=Y)의 원문은 모델의 개념·특징·기반기술과 법·환경·사회적 고려를 요구합니다. 다른 토픽이 나머지를 담당할 수 있으나 이 토픽의 부분 요구도 현재 완결되지 않았습니다.
- 상태 최소 정정: `requirements[3].status = "부분 충족"`. 다른 토픽과 합쳐 원문 요구를 충족한다면 해당 토픽·절을 명시합니다.
- 안전한 추가 문구: [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)의 §2.5, GV-6.1-001, MP-4.1-010, MS-2.12-003을 확인했습니다. 이는 운영상 검토 방향이며 국내 법적 결론은 아닙니다.

```json
"파운데이션 모델 구현에서는 학습 자료·출력의 개인정보와 지식재산권 및 적용되는 이용조건을 검토합니다. 학습·미세조정·추론의 전력·물 사용과 환경영향을 측정하거나 추정하고, 편향·허위정보·접근격차 등 사회적 영향을 평가합니다. 모델의 개념·특징·기반기술은 foundation-language-multimodal-models 단원에서 별도로 설명합니다."
```

마지막 문장의 토픽 ID는 인쇄본의 실제 단원명·페이지 또는 위키 링크로 연결해야 합니다.

### 5. TLS 1.2 구조·과정 요구에 TLS 1.3 흐름만 제시함

- 위치: `tls13.requirements[0]`, `.principles[0]`, `.answer_outline` — 5031행부터의 토픽.
- 원문: “TLS1.3기본 흐름은 ClientHello(key_share등) → ServerHello …”, `"status":"충족"`.
- 근거: [Q-Net 136회 2교시 6번](https://www.q-net.or.kr/cst006.do?gSite=Q&gId=&id=cst00602&artlSeq=5234951&brdId=Q006&code=1203&cst=Y)의 TLS 구조·핸드셰이크 요구에 대해 1.2의 구성과 흐름을 확인할 수 없습니다. [RFC 5246 §6·§7.3 및 Figure 1](https://www.rfc-editor.org/rfc/rfc5246.html#section-7.3)의 1.2 full handshake와 현재 노트의 1.3 과정은 구분해 제시해야 합니다.
- 상태 최소 정정: `requirements[0].status = "부분 충족"`.
- 최소 보완 문구: 다음을 추가하고 기존 1.3 흐름은 유지합니다.

```json
"TLS 1.2는 Record 계층 위에 Handshake·ChangeCipherSpec·Alert와 응용 데이터를 다룹니다. 인증서 기반 ECDHE·클라이언트 인증 없음·최초 full handshake의 예는 ClientHello → ServerHello·Certificate·ServerKeyExchange·ServerHelloDone → ClientKeyExchange·ChangeCipherSpec·Finished → 서버 ChangeCipherSpec·Finished입니다. ChangeCipherSpec은 Handshake 메시지와 별도 콘텐츠 유형이며 키교환·상호인증·세션 재개 조건에 따라 흐름이 달라집니다."
```

취약점과 개선의 인과관계도 한 문장 추가하면 좋습니다: “정적 RSA 키교환은 전방향 안전성을 제공하지 않으며 TLS 1.3은 정적 RSA/DH를 제거했습니다. CBC 등 구형 레코드 암호를 제거하고 AEAD만 허용하며, ServerHello 뒤의 핸드셰이크 메시지를 암호화합니다.” [RFC 8446 §1.2](https://www.rfc-editor.org/rfc/rfc8446.html#section-1.2)를 대조했습니다. TLS 1.2 전체가 해독 가능하다는 주장은 추가하지 않습니다.

## 유지할 내용과 검증 한계

| 범위 | 이번 검수 결과 |
|---|---|
| VLSM·은행가·스케줄링 | /22 배분은 중첩 없이 1024주소, 수용량 510/254/126/126, 호스트 여유16입니다. 안전순서 B→A→C, Work 3→5→8→10입니다. SJF 평균대기5, SRT 평균대기8/3으로 일치합니다. |
| HPA·RSA·모드 | 기본 HPA 3×90/60 올림=5, RSA 4³ mod33=31 및 31⁷ mod33=4, OFB XOR0x26이 일치합니다. [HPA 공식 기본식](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#algorithm-details)을 재열람했습니다. CBC/CFB/OFB의 현재 설명에서 고확신 오류를 찾지 못했습니다. 모드 표준 전체를 이번에 다시 읽지는 않았습니다. |
| DP·MPC·FedAvg | DP count 민감도1·ε0.5이면 Laplace 척도2, 기본 순차합성1.5입니다. [Dwork·Roth §3.3·Corollary3.15](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf)를 대조했습니다. MPC 합계16은 맞지만 위의 난수 조건 보완이 필요합니다. FedAvg3.5는 [원논문 Algorithm1](https://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf)의 표본 수 가중 집계와 일치합니다. |
| NIST AI RMF | [1.0 원문 §3·§5](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)의 7특성·4기능과 일치합니다. GOVERN의 횡단 기능 및 비직렬성을 유지합니다. |
| AI기본법·개인정보법 | 직접 재열람한 현행 AI기본법 [제6조](https://law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1034284625), [제7조](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031809535), [제34조](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031809501)는 원고의 3년 기본계획·대통령 소속 위원회·6책무와 일치합니다. [제정판 연혁 헤더](https://www.law.go.kr/lsInfoP.do?ancYnChk=0&efYd=20260122&lsiSeq=268543)는 2026-01-22 시행, 현행은 2026-07-21 시행으로 분리한 것이 맞습니다. [개인정보 보호법 제37조의2 제3항](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1029335635)의 판본·대응 요약도 일치합니다. 각 법 전체·시행령·고시는 검증하지 않았습니다. |
| CAT·DSA·MCP | [현행 CAT 일러두기](https://tta-trustworthy-ai.gitbook.io/cat)의 제품·서비스/조직 4인증 범위 및 심사·시험 구분은 원고와 일치합니다. [FIPS186-5 §4, 인쇄16쪽](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf)의 DSA 신규 생성 불승인도 맞습니다. [MCP의 명시된 2026-07-28 경로](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)는 실제 열렸고 confused deputy·token passthrough·SSRF 등의 보안 항목이 있습니다. |
| ISMS·N2SF·유료 표준 | ISMS 공식 홈페이지는 이번 재접속에서502였습니다. 최신 ISMS/P·간편인증 상세 기준을 새로 확인하지 못했습니다. N2SF는 [국립목포대가 재게시한 원문 부록1](https://mnuk2.mokpo.ac.kr/bbs/mnusecu/1544/250570/download.do)의 PDF3쪽 문서이력에서 2025.1 Draft→2025.9 1.0을, 표에서 C/S/O의 기밀/민감/공개 표기를 확인했습니다. 원발행기관 직접 호스트에서 받은 파일은 아니며 본문·통제 전체 검증은 아닙니다. ISO42001 유료 전문은 읽지 않았습니다. 기존 미열람·부분 확인 표시를 오류로 간주하거나 충족으로 승격하지 않습니다. |

출처 메타데이터 정합성 보완 1건: `sources[id=sys-signature].notes`에는 “DSA 신규 서명 제한은 본문 후속 확인 필요”가 남아 있으나 `rsa-dsa-ecc-envelope.version_note`는 본문 16쪽 확인으로 되어 있습니다. 이번에 §4를 실제 재확인했으므로 새 정정 기록에는 “공식 게재 페이지 및 FIPS186-5 §4(인쇄16쪽)를 확인했으며 DSA는 신규 서명 생성에 승인되지 않고 기존 서명 검증에 사용할 수 있음”으로 맞출 수 있습니다. 기술 설명 자체의 오류는 아닙니다.

이 결과는 위 72개 토픽의 읽기 검수와 명시한 계산·출처 범위에 한정됩니다. 독자의 이해도 시험이나 전권의 모든 기출 요구 충족 판정은 아닙니다.
