# 학습 문서 내용·표현 점검과 정정

- 작성일 및 아래 원문 확인일: 2026-11-10.
- 검수 범위: 수험 입문자용 학습 안내, 기존 서브노트 224개의 현재 설명·예제·답안 구성·회상 질문, 관련 위키 개요와 비교 문서. 아래는 별도로 원문을 대조했거나 교육용 가정과 예제 조건을 수정한 대표 항목이다.
- Q-Net 시험 문제와 기술 근거의 역할을 구분했다. 법령, 표준, 제품의 과거 판본과 현재 적용 범위를 모두 재검증한 것은 아니다. 근거가 충분하지 않은 항목은 노트에 적힌 확인 상태를 따른다.
- 기초 목표 11개에 추가한 자료의 기관·열람 범위는 [출처 확인 기록](../sources/2026-11-10-foundation-references.md)에 있다. 예제와 회상 질문은 학습용이다.

## 데이터베이스와 통계·AI

- [관계형 모델링](../../wiki/concepts/relational-data-modeling.md)의 수량 예에서 양수 검사와 값의 존재를 별개로 다뤘다. PostgreSQL 16은 검사 조건이 참이거나 NULL일 때 만족한 것으로 취급하므로, 수량 입력을 반드시 받아야 하는 예에는 `NOT NULL` 조건을 따로 적었다. [PostgreSQL 16 §5.4](https://www.postgresql.org/docs/16/ddl-constraints.html)
- [트랜잭션 격리](../../wiki/concepts/transaction-isolation-levels.md)는 SQL 표준이 허용하는 현상과 PostgreSQL 구현에서 더 강하게 보장하는 범위를 구분했다. [PostgreSQL 16 §13.2](https://www.postgresql.org/docs/16/transaction-iso.html)
- [옵티마이저](../../wiki/concepts/sql-optimizer-tuning.md)는 실행계획의 추정과 실제 실행을 구분했다. 실제 실행 결과를 확인하는 예에는 PostgreSQL `EXPLAIN ANALYZE`를 적었다. [PostgreSQL 16 §14.1](https://www.postgresql.org/docs/16/using-explain.html)
- [t 검정](../../wiki/concepts/t-test-z-test.md) 예제는 통계량 3.464와 자유도 2의 양측 유의수준 5% 임계값 4.303을 비교하고, 귀무가설을 기각하지 못한다는 판단을 덧붙였다. [NIST t 분포 임계값 표](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3672.htm)
- [변분 오토인코더](../../wiki/concepts/variational-autoencoder.md)의 ELBO를 로그 주변 가능도의 하한으로 명시했다. [Kingma·Welling, Auto-Encoding Variational Bayes §2.2](https://arxiv.org/html/1312.6114)
- [신경망 학습](../../wiki/concepts/neural-network-backpropagation.md)은 수치 예제에서 예측값, 오차, 손실, 가중치 갱신을 순서대로 읽을 수 있게 정리했다. [합성 데이터](../../wiki/concepts/synthetic-data-generation-evaluation.md)는 예제에 사용한 생성기 학습 자료와 성능 평가용 자료를 구분했다.

## 소프트웨어·전략·사업과 산업

- [요구공학](../../wiki/concepts/requirements-engineering.md)은 재고가 부족할 때와 결제 후 취소할 때를 다른 검증 사례로 나눴다.
- [테스트 기법](../../wiki/concepts/software-testing-principles-techniques.md)의 로그인 잠금 예제에서 잠기지 않은 초기 상태, 4회와 5회의 경계, 성공 시 실패 횟수 초기화를 명시했다. 잠긴 계정의 요청 처리처럼 문제에서 정하지 않은 동작은 확인 대상으로 남겼다. [ISTQB CTFL 4.0.1, §4.2.4 상태 전이 테스팅](https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
- [알고리즘 복잡도](../../wiki/concepts/algorithm-complexity-big-o.md)는 표에서 부분집합과 순열 하나를 1회로 세는 전제를 명시했다. 각 원소를 복사해 출력할 때는 별도의 비용이 든다.
- [위험 분석](../../wiki/concepts/safety-hazard-analysis.md)은 FTA 예제에서 분석할 최상위 사건과 원인 사건을 구분했다. [NASA Fault Tree Handbook with Aerospace Applications, §3.1](https://extapps.ksc.nasa.gov/reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf)
- [권한형 블록체인](../../wiki/concepts/blockchain-deployment-data-storage.md) 예에서는 기록 참여 권한과 데이터 열람 권한을 구분했다. [NISTIR 8202 §2.2](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf)
- [전자정부 UI/UX 노트](../../wiki/concepts/digital-government-ui-quality.md)의 133회 2교시 2번은 2024년 2월판을 지정한다. 행정안전부 배포 안내를 확인했으며 2월판 첨부는 열람하지 못했다. 7월판의 세부 적용 수준을 2월판에 적용할 수 있는지는 확인이 남아 있다.

## 시스템·네트워크·클라우드와 보안

- [IPC](../../wiki/concepts/interprocess-communication.md)는 파이프의 바이트 스트림과 메시지 큐의 메시지 경계를 구분했다. 생산자·소비자 예에는 버퍼의 빈자리와 데이터 수를 세는 세마포어 및 버퍼 접근을 직렬화하는 뮤텍스의 역할을 밝혔다. [Linux man-pages pipe(7)](https://man7.org/linux/man-pages/man7/pipe.7.html)
- [TCP](../../wiki/concepts/tcp-control.md)는 새 송신 여유를 계산하는 시점의 미확인 데이터 5 MSS와 재전송 타이머가 만료되기 전의 FlightSize 8 MSS를 서로 다른 조건으로 나눴다. [RFC 5681 §3.1–3.2](https://www.rfc-editor.org/rfc/rfc5681.html)
- [쿠버네티스 HPA](../../wiki/concepts/kubernetes-hpa.md)는 3개에서 5개로 늘어나는 기본 계산이 성립하는 전제와 실제 조정에서 결과가 달라질 수 있는 조건을 설명했다. [Kubernetes HPA 알고리즘](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details)
- [적대적 AI](../../wiki/concepts/adversarial-ai-security.md)와 [연합학습 보안](../../wiki/concepts/federated-learning-security.md)의 멤버십 추론을 특정 기록이 학습에 쓰였는지 알아내려는 공격으로 풀어 썼다. [NIST CSRC 멤버십 추론 용어집](https://csrc.nist.gov/glossary/term/membership_inference_attack)
- [AI 거버넌스 개요](../../wiki/concepts/ai-governance.md)는 Govern이 세 기능 전반에 적용되며 위험관리 활동을 필요에 따라 반복한다는 점을 명시했다. [NIST AI RMF 1.0 §5, 인쇄 20~21쪽](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)
- [클라우드 개요](../../wiki/concepts/cloud-computing.md)에 서비스 모델과 별도로 프라이빗·커뮤니티·퍼블릭·하이브리드 배치 모델을 명시했다. [NIST SP 800-145, 인쇄 3쪽](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)
