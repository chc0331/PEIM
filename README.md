# 정보관리기술사 독학 학원

질문과 답안 훈련을 이어가면 강사가 학습 내용을 위키에 정리하고 관련 개념을 그래프로 연결하는 개인 학습 프로젝트입니다.

## 첫 수업

이 폴더에서 **“1일차 시작해줘”**라고 말하면 정규화 수업을 시작합니다. 주문 예제로 원리를 익힌 뒤 기출 답안을 작성합니다. [1일차 계획](study/timetable.md#day-1) · [정규화 파일럿](study/lessons/normalization-pilot.md)

그날 할 일은 [48주 시간표](study/timetable.md)에서 찾고, 주제별 자료와 완료 체크는 [과목별 커리큘럼](study/curriculum.md#curriculum-week-1)에서 확인하세요.

수업 중에는 다음처럼 요청할 수 있습니다.

- **“이 개념을 기술사 답안 관점으로 설명하고 확인 문제를 내줘.”**
- **“이 답안을 채점하고 가장 큰 오류 세 가지를 고쳐줘.”**
- **“이 자료를 위키에 반영하고 기존 내용과 충돌하는 부분을 찾아줘.”**
- **“이번 주에 반복해서 틀린 개념과 다음 복습을 정리해줘.”**
- **“회상 연습과 답안 훈련의 관계를 그래프로 설명해줘.”**
- **“이 PDF를 ingest하고 기존 개념에 추가되는 내용과 상충을 정리해줘.”**
- **“데이터 모델링의 관련 기출을 찾아 브레인스토밍하고, 결과를 개념 노트에 저장해줘.”**

수업 종료 시 위키 정리는 강사가 수행합니다. 이 기능은 프로젝트 지침과 관리 명령으로 작동하며 앱이 닫힌 동안 실행되는 자동화는 아닙니다.

## 바로 보기

- [강사 운영 지침](AGENTS.md)
- [학습 위키 목차](wiki/index.md)
- [기출·개념 탐색 지도: 2022~2026년 15회·465문항](wiki/comparisons/qnet-exam-map.md)
- [2027~2030 출제기준 사진과 학습 과정 대조표](wiki/comparisons/qnet-2027-curriculum-map.md)
- [토픽별 인쇄 서브노트 224개](docs/subnotes/topics.md) · [통합 PDF](output/pdf/subnotes/정보관리기술사_기출서브노트_통합.pdf) · [개별 PDF 모음](output/pdf/subnotes/정보관리기술사_토픽별서브노트.zip)
- [465문항 요구사항과 수록 위치](docs/subnotes/coverage.md) · [인쇄·재생성 안내](docs/subnotes/README.md)
- [학습자 프로필](study/profile.md) · [진도·복습](study/progress.md)
- [현재 독학 전략](wiki/comparisons/study-strategy.md)
- [공개 개념 그래프](https://chc0331.github.io/PEIM/) · [전체 로컬 그래프](graphify-out/graph.html) · [그래프 보고서와 출처 목록](graphify-out/GRAPH_REPORT.md)
- [문서 형식·갱신·복구 절차](docs/wiki-workflow.md)

Q-Net 제126~140회 공식 PDF 15개와 465문항을 보관하고, 문항마다 원본 PDF 쪽을 연결했습니다. 인쇄용 서브노트 224개에서 개념 설명, 적용 예제, 답안 구성, 회상 질문을 확인할 수 있습니다. 각 노트는 2쪽 또는 4쪽입니다. 기초 목표 11개의 보충 자료는 과목별 커리큘럼에서 찾아볼 수 있습니다.

기술 설명의 검토 상태는 출처 확인 120개·부분 확인 103개·확인 필요 1개입니다. 지정 판본·유료 표준 본문·미확보 가이드의 한계를 해당 노트에 표시했습니다. 문항 연결은 모든 소문항의 검증 완료나 공식 기준답안을 뜻하지 않습니다. 상세 검수·정정 기록은 [서브노트 안내](docs/subnotes/README.md)에서 확인합니다.

진단 수업을 아직 시작하지 않았습니다. 2027~2030 출제기준은 Q-Net에서 적용기간을 확인했고, 제공받은 1~4쪽 사진 중 읽을 수 있는 항목을 학습 과정과 대조했습니다. 4쪽의 작은 글씨 일부와 5~8쪽은 확인이 남아 있습니다. 목표 회차를 정할 때 첨부 원문과 회차 공고를 다시 확인합니다.

## 환경

Python 3.11 환경과 Graphify 0.9.55, PyYAML 6.0.3을 사용합니다. `.venv/`는 이 프로젝트 전용이며 추가 유료 API를 기본 의존성으로 사용하지 않습니다. 그래프 생성·갱신의 의미 추출에는 현재 Codex 세션 사용량이 발생합니다. 별도 API 비용 0과 모델 사용량 0은 다릅니다.

재설치:

```sh
uv venv --python 3.11 .venv
uv pip sync --python .venv/bin/python requirements.lock
```

Codex 스킬은 `.codex/skills/graphify/`에 이미 등록되어 있습니다. 설치 시 생성되는 범용 AGENTS 안내는 학습용 지침으로 교체했고, 기능이 없는 PreToolUse 훅은 제거했습니다. 스킬을 재설치해야 한다면 `.venv/bin/graphify install --project --platform codex` 실행 후 기존 학습 지침이 보존되는지 비교하고 불필요한 훅을 제거하세요. 자동 업그레이드하지 않습니다.

점검과 조회:

```sh
.venv/bin/python scripts/wiki.py lint
.venv/bin/python scripts/wiki.py status
.venv/bin/python scripts/wiki.py search 'Active recall'
.venv/bin/graphify query '회상 연습'
.venv/bin/graphify path '회상 연습' '시간제한 답안 훈련'
.venv/bin/graphify explain '회상 연습'
.venv/bin/python -m unittest discover -s tests -v
```

`prepare`는 목차와 변경 이력을 정리하고 갱신할 문서 목록을 만듭니다. **명령만 실행하면 LLM 추출까지 자동으로 끝나는 것은 아닙니다.** 강사가 세션에서 의미를 추출한 뒤 `accept`, `build`로 반영합니다. 자세한 절차는 운영 문서를 따릅니다.

## 보관 구조

| 위치 | 역할 |
|---|---|
| `raw/` | 추가 전용 출처 기록·제출 원본·수업 기록 |
| `wiki/` | 검증 상태와 근거를 가진 기준 학습 지식 |
| `study/` | 개인 프로필·진도·평가·원자료 보존 기록 |
| `templates/` | 개념·출처·문제·첨삭·수업 기록 양식 |
| `graphify-out/` | 그래프·추출 캐시·최근 정상본; 재생성 가능 |

문서가 존재하는 것과 실제로 회상·답안 작성을 할 수 있는 것은 별개입니다. 사용자의 수행 기록은 그래프에 넣지 않습니다. 검증 상태가 상충·미검증인 내용도 탐색할 수 있으나 정답 근거로 무비판적으로 사용하지 않습니다.

전체 그래프 HTML은 Graphify의 기본 시각화이며 최초 표시 시 vis-network 라이브러리를 CDN에서 불러옵니다. 로컬에 자료를 보관하지만 완전한 오프라인 화면을 보장하지 않습니다. PEIM의 공개 개념 그래프에는 개념 문서에서 추출한 노드와 관계만 담고, 원자료·기출 문서 노드·개인 학습 기록은 싣지 않습니다. PEIM 저장소의 위키 원문도 공개되어 있습니다.

새 자료를 위키에 반영하고 `scripts/wiki.py prepare`·의미 추출·`build`를 마친 다음, `.venv/bin/python scripts/export_concept_graph.py --output site/concept-graph`로 공개 데이터를 갱신합니다. 개념 문서와 생성된 데이터를 `main`에 반영하면 GitHub Actions가 공개 페이지를 배포합니다. 내보내기는 그래프가 최신 상태인지 검사하며 개인 자료 경로가 섞인 결과는 거부합니다.
