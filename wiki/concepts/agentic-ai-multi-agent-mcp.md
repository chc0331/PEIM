---
id: agentic-ai-multi-agent-mcp
title: Agentic AI·다중 에이전트와 MCP
aliases:
- Agentic AI and Multi-Agent Systems
type: concept
domains:
- 인공지능
sources:
- id: source-subnote-38c43325a50c
- id: source-subnote-6a01ecb9df48
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 출처 확인
status: 출처 확인
related_terms:
- MCP
---

# Agentic AI·다중 에이전트와 MCP

## 서브노트

### 한눈에 이해

워크플로는 정해 둔 순서로 문서를 처리합니다. 에이전트는 중간 결과를 보고 다음 도구와 행동을 고를 수 있습니다. 여러 에이전트가 작업을 나눌 때는 결과를 전달하고 대조하는 시간도 듭니다.

### 정의와 핵심 원리

Agentic AI는 목표에 따라 계획·도구 사용·상태 갱신·피드백을 수행하는 시스템이며 MAS는 여러 agent가 역할·정보·행동을 조정하고 MCP는 모델 애플리케이션의 외부 context/도구 연결 규약입니다.

- agent 루프는 목표/상태→계획·행동 선택→도구 실행→관측·검증→상태 갱신→종료/재계획입니다. workflow는 사전 코드 경로 중심이고 agent는 모델이 경로·도구를 더 동적으로 고릅니다. 자율성은 연속적인 설계 선택이며 인간 확인·실행 예산·종료 조건을 과업에 맞게 정합니다.
- MAS는 역할 분담·병렬 조사·전문성·상호 검토가 가능하지만 오류 전파·중복·충돌·동기화·통신 비용이 증가합니다. 중앙 orchestrator-workers·peer 협력·evaluator-optimizer 등의 구조를 목적에 맞게 쓰고 공유 상태·메시지 schema·소유권·결과 통합/중재를 설계합니다.
- MCP 2025-06-18은 JSON-RPC를 사용하는 연결 규약입니다. 호스트는 클라이언트를 여러 개 만들 수 있고, 각 클라이언트는 특정 서버 하나와 1:1 세션을 유지합니다. 서버는 자료(resources)·도구(tools)·프롬프트(prompts)를 제공합니다. 기능을 연결한 뒤에도 권한과 입력값, 결과의 근거를 확인해야 합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| 단일 agent | 하나의 상태·판단 흐름 | 단순·조정 비용 작음 |
| MAS | 여러 역할·병렬·검토 | 통신·충돌·통합 책임 |
| MCP | host-client-server 연결 규약 | 도구/자료 제공·버전 협상 |

<!-- subnote-page:apply -->

### 적용 예제

**설비 보고서 작성 협업**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 검색 에이전트는 매뉴얼을 찾고, 분석 에이전트는 센서 통계를 확인합니다. 통합 에이전트는 두 결과로 보고서를 작성합니다.

1. 공통 설비ID·기간·출처 schema와 각 결과 소유자를 정합니다.
2. 서버는 매뉴얼 자료와 읽기 전용 통계 도구를 제공하고 host가 연결 client를 관리합니다.
3. 서로 다른 결론은 원자료·계산을 대조하고 통합 기준을 적용하며, timeout/실패를 빈 성공 결과로 바꾸지 않습니다.

**결과·해석:** 협업은 역할 수보다 검증·인계·공유 상태 설계에 달려 있습니다.

**전제·주의:** 독립 agent 여러 개의 동의가 같은 잘못된 근거의 반복일 수 있어 원출처를 검증합니다.

### 답안 골격과 혼동 방지

agent 정의·workflow 비교 → 루프·상태·종료 → 단일/MAS 효과·비용 → MCP 구조·primitive → 검증·통합 예시

- MCP를 모델 간 자동 합의 protocol로 설명하지 않습니다.
- agent 수가 많으면 성능이 무조건 좋아진다고 하지 않습니다.

### 내용을 가리고 회상

1. workflow와 agent의 경로 결정 주체는 어떻게 다릅니까?
2. MCP host-client-server의 연결 수 관계는 무엇입니까?
3. MAS의 중복·충돌을 어떤 상태·소유권 규칙으로 줄이겠습니까?

### 적용 기준과 근거

2026-11-05 열람한 출처 범위의 강사 생성 설명·가상 예제입니다. 공식 기출 해설이 아닙니다.

**내용 검토 상태: 출처 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic Engineering; 2024-12-19; 2026 갱신 안내 포함; 확인 2026-11-05. 확인 범위: 실제 열람: predefined workflows vs LLM 동적 agent, orchestrator-workers·evaluator-optimizer, 비용/지연 절충. 단일 공급자 실무 패턴을 MAS 전체 이론과 동일시하지 않습니다.
- [Model Context Protocol Architecture](https://modelcontextprotocol.io/specification/2025-06-18/architecture) — Model Context Protocol maintainers; 2025-06-18 고정 명세; 확인 2026-11-05. 확인 범위: 실제 열람: host-client-server, client:server 1:1, JSON-RPC·상태 세션·resources/tools/prompts. 최신 명세임을 주장하지 않고 고정 버전으로 설명합니다.

## 연관 기출

- [제136회 1교시 3번](../questions/qnet-136-p1.md#q3) — Agentic AI. 대응: 핵심원리; 충족.
- [제136회 1교시 13번](../questions/qnet-136-p1.md#q13) — MCP. 대응: 핵심원리; 충족.
- [제139회 3교시 1번](../questions/qnet-139-p3.md#q1) — MAS 정의·필요성; 단일/MAS 비교; 효과·고려사항. 대응: 핵심원리; 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
