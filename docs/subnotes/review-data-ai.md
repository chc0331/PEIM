# 데이터·AI 서브노트 독립 내용 검수

검수일: 2026-11-05. 대상 독자는 정보관리기술사 수험 입문자이며 IT 실무 경험은 있지만 각 세부 개념을 이미 안다고 가정하지 않았습니다. `research`와 `document-content-review` 스킬 및 검수 기준을 적용한 독립 검수입니다. 원고·위키·스크립트는 수정하지 않았습니다.

## 판정과 범위

필수 수정은 5건입니다. VAE 목적/손실 부호 1건, SVM 예제의 분리 가능성 설명 1건, 실제 설명보다 넓게 표시한 기출 요구 충족 상태 3건입니다. 회상 질문에 필요한 사전 설명은 3건을 별도 개선안으로 남깁니다. 지정된 11종 계산은 직접 재계산한 결과 원고의 수치와 일치했습니다.

- 원고: `raw/research/2026-11-05-data-ai.md`의 JSON topic 68개 전부. `easy → definition → principles → comparison → example → answer_outline → pitfalls → recall → requirements`를 대조했습니다. 출처 ID·문항 ID도 전부 존재합니다.
- 기출: 126~140회 `raw/exams/qnet/2026-11-01/<회차>/record.json`에서 원고가 연결한 154개 요구 레코드의 실제 문항·소문항을 읽었습니다. 같은 문항이 여러 토픽에 대응되는 경우를 포함한 수입니다.
- PDF 시각 확인: 129회 p.6, 132회 p.4, 136회 p.5, 135회 p.1, 140회 p.7을 로컬 공식 PDF에서 렌더링하여 전체 해당 쪽을 읽었습니다. 다섯 PDF의 SHA-256은 각 `record.json`과 일치했습니다. 129회 표, 132회 TF·log 표, 136회 지표 입력·% 절사 조건을 직접 확인했습니다.
- 외부 원문: 아래 표에 적은 17개 URL의 지정 절만 이번 검수에서 재열람했습니다. 원고의 105개 출처 원문 전체를 다시 읽은 검수가 아닙니다. 표에 없는 기술·판본은 본문 내부 연결만 점검했으며 사실 확인 완료로 승격하지 않았습니다.
- 인쇄 산출 PDF, 현행 위키 본문, 전체 출처 첨부의 전수 시각 검수는 이 보고서 범위에 포함하지 않았습니다. 읽기 검토와 계산 검산을 실제 학습자의 이해도 시험으로 표현하지 않습니다.

검수 원고 SHA-256: `b6c721fea72a8408e035c3696e31fd5703bbdb0c908490c18f88b0f525cc4026`.

## 필수 수정

### F01. VAE 표가 최대화 목적과 최소화 손실을 혼합합니다

- **위치:** `variational-autoencoder`, `comparison.rows[2][1]`, 원고 L5037. 같은 토픽 `principles[0]`의 ELBO 식과 대조했습니다. 배열 인덱스는 0부터 셉니다.
- **현재 문구:** “재구성−KL 또는 음의 ELBO 최소화”. 행 제목은 “VAE 손실”입니다.
- **문제:** 재구성 로그가능도−KL은 ELBO로서 최대화합니다. 최소화할 음의 ELBO는 −재구성 로그가능도+KL입니다. 표만 보고 손실을 구현하면 KL을 증가시키는 쪽으로 최적화할 수 있습니다. 본문의 올바른 식과 표가 충돌합니다.
- **정확한 대체 문구:** “ELBO=재구성 로그가능도−KL 최대화; 손실=−재구성 로그가능도+KL 최소화”. ‘재구성 오차’라는 양의 손실 용어를 쓸 경우에는 “재구성 오차+KL 최소화”로 씁니다.
- **근거 URL·열람 범위:** [Kingma·Welling, Auto-Encoding Variational Bayes v11](https://arxiv.org/html/1312.6114v11), §2.2 식 (3), §2.3 및 Appendix B의 maximization 설명. 2022-12-10 판, 2026-11-05 재열람. 원 논문의 로그가능도 정의와 최대화 방향만 이 판정에 사용했습니다.

### F02. SVM의 추가 음성 표본은 여전히 선형 분리됩니다

- **위치:** `support-vector-machine`, `example.steps[2]`, 원고 L4192. 예제 입력 및 `principles[0]`의 hard-margin 조건과 대조했습니다.
- **현재 문구:** “x=0.5인 음성 잡음이 추가되면 같은 hard 제약은 충돌할 수 있어 soft margin의 위반 비용을 검토합니다.”
- **문제:** 기존 w=1,b=0은 새 표본의 제약을 위반하지만, 새 집합 전체는 여전히 hard-margin으로 분리할 수 있습니다. w=4,b=−3이면 음성 −2,−1,0.5의 y(wx+b)는 11,7,1이고 양성 1,2는 1,5입니다. 따라서 ‘기존 경계 위반’과 ‘어떤 선형 경계로도 분리 불가능’을 구분해야 합니다. 현재 연결은 soft margin이 필요한 비분리 사례로 오독하게 합니다.
- **정확한 대체 문구:** “x=1.5인 음성 잡음이 추가되면 양성 x=1과 x=2 사이에 음성이 놓여 1차원 선형 hard-margin 분리가 불가능하므로 soft margin의 위반 비용을 검토합니다.”
- **대안:** x=0.5를 유지하려면 “기존 경계는 제약을 위반하지만 새 경계 x=0.75로 여전히 hard-margin 분리할 수 있습니다. 다만 마진이 좁아집니다.”로 바꾸십시오. 두 설명을 동시에 섞지 않습니다.
- **근거 URL·열람 범위:** [scikit-learn SVM, Mathematical formulation §1.4.7.1](https://scikit-learn.org/stable/modules/svm.html#svc), primal 제약과 slack·C 설명. 표시 버전 1.9.1, 2026-11-05 재열람. 구체적 w,b 대입과 비분리 판단은 독립 검산입니다.

### F03. ANI의 필요성을 설명하지 않고 해당 요구를 충족 처리합니다

- **위치:** `foundation-language-multimodal-models`, `principles[1]` L5676 및 `requirements[4]` L5774 부근, 문항 `135-1-13`.
- **현재 문구:** “ANI의 특정 과업 역량과 AGI의 넓은 적응/추론 목표를 구분합니다.” / items “AGI 측면 ANI 필요성”, status “충족”.
- **문제:** 본문과 표는 ANI/AGI의 범위 차이만 설명합니다. ANI가 AGI 연구·구현에서 어떤 역할을 하며 왜 필요한지의 논거는 없습니다. 답안 골격의 ‘ANI 역할’도 설명을 대신하지 못합니다. 기출의 ‘필요성’ 요구와 현재 내용이 다릅니다.
- **정확한 최소 대체:** `requirements[4].status`: “부분 충족”. 항목 설명이 가능하면 “ANI/AGI 구분은 설명했으나 AGI 측면의 ANI 필요성 논거는 미보완”이라고 남깁니다. 검증된 논거를 본문에 보강한 뒤 충족 여부를 다시 판단합니다. ‘ANI를 합치면 AGI가 된다’는 새 단정을 넣지 않습니다.
- **근거 URL·열람 범위:** [Q-Net 제135회 정보관리기술사](https://www.q-net.or.kr/cst006.do?gSite=Q&gId=&id=cst00602&artlSeq=5226360&brdId=Q006&code=1203&cst=Y). 로컬 공식 PDF `raw/exams/qnet/2026-11-01/135/qnet-135.pdf` p.1, 1교시 13번을 시각 확인했습니다. 온라인 게시 상태를 다시 확인한 것은 아닙니다. 이 판정은 정답 이론이 아니라 문항 요구와 본문 연결의 불일치에 한정합니다.

### F04. 기존 데이터센터와 AI 데이터센터의 비교가 빠졌습니다

- **위치:** `ai-supercomputing-gpu-tpu`, `comparison` 및 `requirements[4]`, 원고 L6740 부근·L6817 부근, 문항 `140-4-6`.
- **현재 문구:** 비교표 행 “GPU / TPU / AI 슈퍼컴퓨팅”. 요구 items “AI DC 정의·배경 / 기존 DC 비교 / 핵심 기술”, status “충족”.
- **문제:** GPU/TPU 비교와 HPC/cloud/AI 플랫폼의 분류 축 설명은 있습니다. 그러나 기존 DC와 AI DC를 직접 대조하는 설명은 없습니다. 다른 세 대상을 비교한 표만으로 이 소문항을 충족했다고 표시할 수 없습니다.
- **정확한 최소 대체:** `requirements[4].status`: “부분 충족”. 설명은 “기존 DC와 AI DC의 직접 비교 미보완”으로 남깁니다. 작업부하·연산자원·연결·스토리지·전력/냉각 등의 공통 축에서 실제 대조를 보강한 뒤 다시 판단합니다.
- **근거 URL·열람 범위:** [Q-Net 제140회 정보관리기술사](https://www.q-net.or.kr/cst006.do?gSite=Q&gId=&id=cst00602&artlSeq=5274150&brdId=Q006&code=1203&cst=Y). 로컬 공식 PDF `raw/exams/qnet/2026-11-01/140/qnet-140.pdf` p.7, 4교시 6번 가~다를 시각 확인했습니다. 온라인 게시 상태는 재확인하지 않았습니다.

### F05. AI 데이터 획득 방법·선정 기준 요구를 충족 처리합니다

- **위치:** `ai-training-data-quality`, `principles` 및 `requirements[0]`, 원고 L5282 부근·L5346 부근, 문항 `126-3-6`.
- **현재 문구:** 생애주기는 “계획→수집/획득→정제→가공/라벨…”로 나열되어 있고, 품질 활동은 “목적 적합·정확 라벨·중복/손상 제거…”입니다. 요구 items “획득·정제 방법·기준”, status “충족”.
- **문제:** 정제·품질 점검의 일부 기준은 있지만, 데이터를 어떤 방법으로 획득하며 어떤 기준으로 원천·대상을 선정하는지 설명하지 않습니다. 단계 이름 ‘획득’을 적은 것과 ‘획득 방법과 기준’을 설명한 것은 다릅니다.
- **정확한 최소 대체:** `requirements[0].status`: “부분 충족”. 설명은 “특성·어노테이션 및 일부 정제 활동은 설명했으나 데이터 획득 방법·선정 기준은 미보완”으로 남깁니다. 지정판 자료를 확인하지 않은 채 임의의 공식 기준 목록을 추가하지 않습니다.
- **근거 URL·열람 범위:** [Q-Net 제126회 정보관리기술사](https://www.q-net.or.kr/cst006.do?gSite=Q&gId=&id=cst00602&artlSeq=5209513&brdId=Q006&code=1203&cst=Y). `raw/exams/qnet/2026-11-01/126/record.json`의 3교시 6번(공식 PDF p.5 대응) 문항 텍스트를 읽었습니다. 이 쪽 PDF의 추가 시각 열람은 하지 않았습니다. 요구 범위 판정이며 NIA 지정판의 정확 목록을 새로 확정한 것이 아닙니다.

## 설명 개선: 회상 질문과 선행 설명의 연결

### E01. 층화와 군집 추출의 차이가 회상 전에 설명되지 않습니다

- **위치:** `sampling-estimation-unbiasedness`, `principles[0]` 및 `recall[0]` L3140.
- **현재 문구:** “단순무작위·층화·군집·계통 추출이 있습니다.” / “층화와 군집 추출은 무엇이 다릅니까?”
- **독자의 어려움:** 예제는 층별 표집과 가중치만 보여 줍니다. 군집을 어떤 단위로 선택하는지 몰라 비교 질문에 답하기 어렵습니다.
- **정확한 보완 문구:** “층화는 각 층에서 관측 단위를 일부씩 뽑습니다. 1단계 군집 추출은 일부 군집을 무작위로 고른 뒤 선택한 군집의 모든 구성원을 관측합니다.”
- **근거 URL·열람 범위:** [OpenStax Introductory Statistics 2e §1.2](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling), stratified/cluster 설명과 Example 1.12, 2026-11-05 재열람. 원고의 동수 비례 보정 예제는 유지합니다.

### E02. p값의 올바른 정의가 없이 해석을 회상하게 합니다

- **위치:** `t-test-z-test`, `principles[2]` 및 `recall[2]` L3445.
- **현재 문구:** “p값을 귀무가설이 참일 확률로 읽지 않습니다.” / “p값이 0.03이면 무엇의 확률을 뜻합니까?”
- **독자의 어려움:** 틀린 해석만 금지했고 무엇의 확률인지는 설명하지 않았습니다.
- **정확한 보완 문구:** “p값은 귀무가설과 검정 가정 아래에서 관측한 통계량만큼 또는 더 극단적인 통계량이 나올 확률입니다. 0.03은 귀무가설이 참일 확률 3%를 뜻하지 않습니다.”
- **근거 URL·열람 범위:** [NIST/SEMATECH §7.1.3.1 Critical values and p values](https://www.itl.nist.gov/div898/handbook/prc/section1/prc131.htm), p-values·Good practice 문단, 2026-11-05 재열람. 현재 t 수치 예제는 오류가 없습니다.

### E03. attention의 √d_k 보정 이유를 회상 전에 설명하지 않습니다

- **위치:** `transformer-mixture-of-experts`, `principles[0]` 및 `recall[0]` L5864.
- **현재 문구:** 식은 “softmax(QKᵀ/√d_k)V”이나 회상은 “QKᵀ 뒤 √d_k로 나누는 목적은 무엇입니까?”입니다.
- **독자의 어려움:** 식의 계수만 제시하여 차원이 커질 때 생기는 문제를 원고만으로 설명할 수 없습니다.
- **정확한 보완 문구:** “Q와 K 성분을 독립·평균0·분산1로 보는 설명용 가정에서는 내적의 분산이 d_k입니다. √d_k로 나누어 점수 크기를 안정화하고 큰 내적으로 인한 softmax 포화와 작은 기울기를 완화합니다.”
- **근거 URL·열람 범위:** [Vaswani 외, Attention Is All You Need v7](https://arxiv.org/html/1706.03762v7), §3.2.1 및 각주 1. 2023-08-02 판, 2026-11-05 재열람. 이 문구를 MoE routing의 정규화 원리로 옮기지 않습니다.

## 필수 11종 독립 검산

분수·십진수 계산을 사용해 중간값부터 재계산했습니다. 기출에서 정한 log 근삿값·최종 절사를 유지했고, 임의의 라이브러리 기본 평활값을 넣지 않았습니다.

| 대상 | 독립 검산 결과 | 판정·한계 |
| --- | --- | --- |
| Bayes | 불량 양성90, 정상 오양성495, 사후90/585=2/13=15.384615…% | 15.38%와 일치 |
| 대응 t | d 평균4, 표본분산4, SE=2/√3, t=3.4641016…, df=2 | 원고와 일치; α·단측/양측을 확정하지 않은 결론 유보도 타당 |
| Jackknife | 제외 평균2.5/2/1.5, 평균2, bias0, 보정값2, V=1/3, SE=.577350… | 원고와 일치; 출처 강의노트의 add 문구와 편향 부호 충돌도 실제 확인 |
| TF-IDF | DF=(3,1,3,2,3); D1=(0,1.41,0,0,0), D2=(0,0,0,.85,0), D3=(0,0,0,.17,0) | 132회 PDF p.4의 TF·지정 log·DF 가공 금지와 일치 |
| 혼동행렬 | N121; Accuracy90.0826…%, Precision95.2380…%, Recall93.4579…%, F1 94.3396…% → 90/95/93/94% | 136회 PDF p.5의 최종 소수점 버림과 일치 |
| DCF | 110/1.1 + 121/1.1² =100+100=200 | 연말 현금흐름·잔존가치0의 선언 가정에서 일치; 국내 법정 모델 검증 아님 |
| 연관규칙 | support.3, confidence.75, lift1.5, leverage.1, conviction2, 역방향 confidence.6 | 결측 없는 거래와 선언한 분모에서 일치 |
| Q-learning | target7.4, TD오차2.4, Q_new5.24 | 비종료 전이에서 일치; 원고의 종료 가치0 안내 확인 |
| 역전파 | 예측6, 손실8, dL/dw=−8, w_new3.8, 예측7.6, 손실2.88 | b=0 고정이라는 입력 조건에서 일치 |
| 확장성 해싱 | hash(key)=key, 하위2비트 기준 0·4→00, 2→10, 01/11은 l=1 홀수 버킷 공유 | g=2, 포인터4개, 홀수 버킷 공유 포인터2개로 일치 |
| 2NF | 129회 실제 5행을 학생4행·수강5행으로 투영하고 학번으로 조인하면 원 5행 복원 | 명시한 학생당 학과/지도교수 하나의 업무 가정에서 일치; 컴퓨터과의 K1/M1 때문에 학과→지도교수는 성립한다고 단정할 수 없음 |

## 68개 토픽별 확인 목록

아래 ‘내부 확인’은 모든 필드의 연결·수치·요구 문항을 읽었다는 뜻입니다. 모든 외부 기술 사실을 재검증했다는 뜻이 아닙니다. ‘필수 지적 없음’도 이번 범위에서 발견하지 못했다는 의미입니다. 원고가 이미 명시한 부분 확인·과거 판본·강사 설계 한계는 그대로 유지합니다.

| # | Topic ID · 원고 시작 줄 | 내부 검수 결과 |
| --- | --- | --- |
| 1 | `relational-data-modeling` · L956 | 내부 확인; 이번 필수 지적 없음 |
| 2 | `relational-normalization` · L1066 | 내부 확인; 2NF·원표 복원 검산 일치 |
| 3 | `database-denormalization` · L1166 | 내부 확인; 이번 필수 지적 없음 |
| 4 | `transaction-concurrency-control` · L1251 | 내부 확인; 이번 필수 지적 없음 |
| 5 | `transaction-isolation-levels` · L1356 | 내부 확인; 이번 필수 지적 없음 |
| 6 | `database-index-structures` · L1456 | 내부 확인; 이번 필수 지적 없음 |
| 7 | `extendible-hashing` · L1550 | 내부 확인; 하위 비트 분할 검산 일치 |
| 8 | `sql-optimizer-tuning` · L1633 | 내부 확인; 이번 필수 지적 없음 |
| 9 | `static-dynamic-sql` · L1731 | 내부 확인; 이번 필수 지적 없음 |
| 10 | `nosql-document-modeling` · L1813 | 내부 확인; 이번 필수 지적 없음 |
| 11 | `partitioning-sharding` · L1913 | 내부 확인; 이번 필수 지적 없음 |
| 12 | `distributed-database-transparency` · L2008 | 내부 확인; 이번 필수 지적 없음 |
| 13 | `cap-pacelc` · L2099 | 내부 확인; 이번 필수 지적 없음 |
| 14 | `database-migration-validation` · L2184 | 내부 확인; 이번 필수 지적 없음 |
| 15 | `public-database-standardization` · L2281 | 내부 확인; 이번 필수 지적 없음 |
| 16 | `data-governance-master-data` · L2383 | 내부 확인; 이번 필수 지적 없음 |
| 17 | `data-quality-management` · L2476 | 내부 확인; 이번 필수 지적 없음 |
| 18 | `dataops-observability-elk` · L2573 | 내부 확인; 이번 필수 지적 없음 |
| 19 | `big-data-platform-data-lake` · L2674 | 내부 확인; 이번 필수 지적 없음 |
| 20 | `data-commerce-marketplace` · L2785 | 내부 확인; 이번 필수 지적 없음 |
| 21 | `data-valuation-assetization` · L2878 | 내부 확인; DCF200 일치 |
| 22 | `data-visualization` · L2985 | 내부 확인; 이번 필수 지적 없음 |
| 23 | `sampling-estimation-unbiasedness` · L3079 | 설명 E01; 층별 가중평균76 계산 일치 |
| 24 | `normal-distribution-lln-clt` · L3189 | 내부 확인; 이번 필수 지적 없음 |
| 25 | `discrete-probability-distributions` · L3290 | 내부 확인; 이번 필수 지적 없음 |
| 26 | `t-test-z-test` · L3382 | 설명 E02; t 계산 일치 |
| 27 | `jackknife-bias-variance` · L3474 | 내부 확인; 편향·분산·SE 일치 |
| 28 | `bayes-theorem` · L3558 | 내부 확인; 기저율 계산 일치 |
| 29 | `correlation-causation-ab-testing` · L3640 | 내부 확인; 이번 필수 지적 없음 |
| 30 | `regression-assumptions` · L3731 | 내부 확인; 이번 필수 지적 없음 |
| 31 | `machine-learning-lifecycle-modelops` · L3823 | 내부 확인; 이번 필수 지적 없음 |
| 32 | `machine-learning-evaluation-metrics` · L3948 | 내부 확인; 136회 수치·절사 일치 |
| 33 | `decision-tree-ensembles` · L4048 | 내부 확인; 이번 필수 지적 없음 |
| 34 | `support-vector-machine` · L4147 | 필수 F02; 원래 마진 폭2는 일치 |
| 35 | `clustering-silhouette` · L4246 | 내부 확인; 이번 필수 지적 없음 |
| 36 | `self-organizing-map` · L4353 | 내부 확인; 이번 필수 지적 없음 |
| 37 | `outliers-noise-bias-filtering` · L4438 | 내부 확인; 이번 필수 지적 없음 |
| 38 | `time-series-models-anomaly-detection` · L4541 | 내부 확인; 이번 필수 지적 없음 |
| 39 | `learning-optimization-bayesian-search` · L4645 | 내부 확인; 이번 필수 지적 없음 |
| 40 | `metaheuristics-genetic-algorithm` · L4737 | 내부 확인; 이번 필수 지적 없음 |
| 41 | `dimensionality-reduction` · L4828 | 내부 확인; 이번 필수 지적 없음 |
| 42 | `neural-network-backpropagation` · L4910 | 내부 확인; gradient·갱신·손실 일치 |
| 43 | `variational-autoencoder` · L5003 | 필수 F01; 재매개화 z=1.5는 일치 |
| 44 | `synthetic-data-generation-evaluation` · L5086 | 내부 확인; 이번 필수 지적 없음 |
| 45 | `spiking-neuromorphic-computing` · L5181 | 내부 확인; 이번 필수 지적 없음 |
| 46 | `ai-training-data-quality` · L5274 | 필수 F05; 기존 v2.0 부분 확인 유지 |
| 47 | `federated-learning` · L5407 | 내부 확인; 이번 필수 지적 없음 |
| 48 | `reinforcement-learning` · L5491 | 내부 확인; 이번 필수 지적 없음 |
| 49 | `graph-neural-network` · L5574 | 내부 확인; 이번 필수 지적 없음 |
| 50 | `foundation-language-multimodal-models` · L5665 | 필수 F03; 지정 가이드·법/사회 범위의 기존 부분 표시 유지 |
| 51 | `transformer-mixture-of-experts` · L5803 | 설명 E03; 전문가 결합 [1.4,1.2] 일치 |
| 52 | `retrieval-augmented-generation` · L5887 | 내부 확인; 이번 필수 지적 없음 |
| 53 | `vector-ann-hnsw-ivf` · L5996 | 내부 확인; 이번 필수 지적 없음 |
| 54 | `fine-tuning-rlhf-raft` · L6082 | 내부 확인; 이번 필수 지적 없음 |
| 55 | `prompt-harness-engineering` · L6168 | 내부 확인; 이번 필수 지적 없음 |
| 56 | `agentic-ai-multi-agent-mcp` · L6260 | 내부 확인; 이번 필수 지적 없음 |
| 57 | `on-device-ai` · L6363 | 내부 확인; 이번 필수 지적 없음 |
| 58 | `physical-ai` · L6447 | 내부 확인; 이번 필수 지적 없음 |
| 59 | `quantum-machine-learning` · L6529 | 내부 확인; 이번 필수 지적 없음 |
| 60 | `turboquant-vector-quantization` · L6622 | 내부 확인; Google 발표의 조건부 6배/8배 보고와 일치 |
| 61 | `ai-supercomputing-gpu-tpu` · L6708 | 필수 F04; 4GPU 예제 100/55≈1.82 일치 |
| 62 | `text-mining-opinion-tfidf` · L6831 | 내부 확인; 공식 TF·log 표와 3×5 계산 일치 |
| 63 | `speech-data-mining` · L6926 | 내부 확인; 이번 필수 지적 없음 |
| 64 | `deepview-visual-intelligence` · L7011 | 내부 확인; 이번 필수 지적 없음 |
| 65 | `text-to-sql-langchain-predictive-maintenance` · L7094 | 내부 확인; 이번 필수 지적 없음 |
| 66 | `deepfake-generation-detection` · L7188 | 내부 확인; 이번 필수 지적 없음 |
| 67 | `association-rule-metrics` · L7282 | 내부 확인; 5개 지표·방향 검산 일치 |
| 68 | `file-database-blockchain-storage` · L7364 | 내부 확인; 이번 필수 지적 없음 |

## 이번에 재열람한 외부 1차 자료

모두 2026-11-05에 아래 범위를 실제 읽었습니다. 발행일·버전이 없는 웹 문서는 표시를 임의 생성하지 않았습니다. ‘원 논문’은 해당 저자의 원문, 제품 문서는 그 기능을 제공하는 개발 주체의 문서입니다. 검색 결과에 나온 2차 글은 판정 근거로 사용하지 않았습니다.

| 자료·기관·판 | URL | 실제 재열람 범위 |
| --- | --- | --- |
| Kingma·Welling, VAE v11, 2022-12-10 | [원 논문](https://arxiv.org/html/1312.6114v11) | §2.2 식(1)~(3), §2.3, Appendix B의 목적 방향 |
| scikit-learn, 1.9.1 표시 | [SVM](https://scikit-learn.org/stable/modules/svm.html) | §1.4.7.1 primal·slack·C |
| Google Research, 2026-03-24 | [TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) | How it works·QJL/PolarQuant·Experiments의 3bit·6배·H100 4bit logits 최대8배; 그림 성능곡선의 독립 재현은 아님 |
| NIST/SEMATECH, 웹판 날짜 미표시 | [Two-sample t-test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm) | paired/unpaired 정의·Welch/pooled 식·자유도·기각역 |
| C. R. Shalizi / CMU, 2023-11-29 | [Jackknife notes](https://stat.cmu.edu/~cshalizi/490/23/2023-11-29-jackknife.pdf) | PDF pp.1~3, 편향·분산·SE 식과 독립/연속성 조건; pp.4~7 전수 재검증 아님 |
| Jignesh Patel / CMU, Spring 2024 | [Hash Tables](https://15445.courses.cs.cmu.edu/spring2024/slides/07-hashtables.pdf) | PDF pp.74~90의 extendible hashing 텍스트·분할 예제 추출; 전체117쪽 재검증 아님 |
| Christian Söderberg / Lund, 2025-02-10 | [EDAF75 Lecture 7](https://fileadmin.cs.lth.se/cs/Education/edaf75/classes/wJOsnG1ZwNvuntuU0kLDB/s07-slides.pdf) | PDF pp.5~7의 투영·prime/non-prime·부분종속·2NF·BCNF 정의 |
| OpenStax / Rice, 온라인 교재 날짜 미표시 | [Probability Theory §3.4](https://openstax.org/books/principles-data-science/pages/3-4-probability-theory) | 조건부확률·Bayes 식과 이진 검사 예시 |
| scikit-learn, 1.9.1 표시 | [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) | §3.4.4.9.1 TP/FP/FN·precision/recall/Fβ, AP와 PR 적분 차이 |
| scikit-learn, 1.9.1 표시 | [Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html) | §8.2.3.5 TF×IDF·DF·기본 +1/평활/L2 옵션; 기출식은 Q-Net 지시를 별도 적용 |
| WIPO, 웹 문서 날짜 미표시 | [Valuing IP Assets](https://www.wipo.int/en/web/business/ip-valuation) | Income/Market/Cost 방법; 국내 데이터 고시나 회계 인식의 세부 원문은 아님 |
| mlxtend 개발자, 날짜/버전 미표시 | [Association rules](https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/association_rules/) | support/confidence/lift/leverage/conviction 식·결측 없는 기본 분모 |
| PyTorch, 2.15.0+cu132 표시 | [DQN tutorial](https://docs.pytorch.org/tutorials/intermediate/reinforcement_q_learning.html) | Bellman/TD 설명, optimize_model의 reward+GAMMA×maxQ 및 종료 마스크; VPP 실증 아님 |
| Goodfellow·Bengio·Courville, 2016 | [Deep Learning Ch.6](https://www.deeplearningbook.org/contents/mlp.html) | feedforward 정의·§6.5.2 chain rule·§6.5.3 미분 재사용; 전체 장 전수 재열람 아님 |
| OpenStax / Rice, Introductory Statistics 2e | [Sampling §1.2](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling) | 층화/1단계 군집/계통 설명·Example 1.12 |
| Vaswani 외, 2023-08-02 v7 | [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) | §3.2.1 및 각주1의 scaling·내적 분산·softmax 기울기 |
| NIST/SEMATECH, 웹판 날짜 미표시 | [Critical values and p values](https://www.itl.nist.gov/div898/handbook/prc/section1/prc131.htm) | p-values·Good practice 문단 |

## 확인 필요로 유지할 범위

원고에 이미 표시된 14개 ‘부분 충족’은 이 검수에서 근거 없이 ‘충족’으로 올리지 않습니다. 특히 NIA v2.0 첨부, 공공부문 초거대 AI 가이드라인 2.0의 지정 도입절차, 2025 개정 DB 서식과 과거 서식의 동일성, 특정 성숙도 모델 등급, 팬텀충돌 용어의 지정 문맥, NoSQL의 특정 3분류와 분산 DB의 특정 5분류, PET/법적 대응 세부는 이번에 새로 확정하지 않았습니다.

자료를 열지 못했다는 기존 기록만으로 기술 설명이 틀렸다고 판정하지 않았습니다. 본문 보완과 판본 재조사가 필요한 범위는 충족 상태 정정과 구분했습니다. 보고서가 제안한 문구는 교정 제안이며 원고에 적용된 변경은 아닙니다.
