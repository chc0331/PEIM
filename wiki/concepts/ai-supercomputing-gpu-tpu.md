---
id: ai-supercomputing-gpu-tpu
title: GPU·TPU·멀티GPU와 AI 슈퍼컴퓨팅
aliases:
- AI Supercomputing Platform
type: concept
domains:
- 인공지능 인프라
sources:
- id: source-subnote-2c46a1269c94
- id: source-subnote-3321723a2248
- id: source-subnote-f6132e96b5c6
- path: raw/corrections/2026-11-05-subnotes-review.md
updated: '2026-11-05'
format: a4-duplex-subnote
review_status: 부분 확인
status: 미검증
---

# GPU·TPU·멀티GPU와 AI 슈퍼컴퓨팅

## 서브노트

### 한눈에 이해

큰 모델은 한 가속기에 안 들어가거나 학습이 너무 오래 걸립니다. 여러 장을 붙여도 gradient 통신·학습자료 읽기·전력/냉각이 따라오지 못하면 비싼 연산기가 기다리게 됩니다.

### 정의와 핵심 원리

대규모 학습·추론을 위해 가속기·고대역 메모리·고속 연결·스토리지·스케줄링·운영 시설을 통합한 병렬 계산 플랫폼입니다.

- GPU는 다양한 병렬 연산과 생태계 유연성, TPU는 Google의 대규모 행렬 연산용 ASIC·HBM·slices·XLA를 특징으로 합니다. TPU는 큰 dense 행렬·큰 batch에 적합할 수 있지만 분기·custom op·높은 정밀도·I/O 병목에는 부적합할 수 있어 GPU보다 항상 좋다는 문항 전제를 조건부로 해석합니다.
- Data parallel은 모델 복제·batch 분할·gradient all-reduce, tensor/model parallel은 한 연산/층의 파라미터 분산, pipeline parallel은 층을 stage로 분할, sharding은 파라미터/optimizer 상태 분산을 활용합니다. 통신 중첩·batch와 학습률·mixed precision·checkpoint·straggler·수치 재현을 검토합니다.
- 플랫폼은 compute fabric·storage fabric·management network, 고성능 공유 저장·checkpoint, job scheduler·registry/관측, 전력·고밀도 냉각으로 구성합니다. 전통 HPC의 다양한 수치해석, cloud의 자원 서비스 모델과 AI platform의 tensor workload 최적화는 다른 분류 축이라 서로 배타적이지 않습니다. 데이터센터 전체 TCO·활용률·장애 복구·환경 제약을 평가합니다.

### 구조·비교·판단

| 구분 | 원리·특징 | 적용·주의 |
| --- | --- | --- |
| GPU | 범용 병렬·custom 연산·넓은 도구 | 메모리·연결·전력 |
| TPU | ASIC 행렬·HBM·XLA·slice | 워크로드·연산 지원 제약 |
| AI 슈퍼컴퓨팅 | 가속기+fabric+storage+운영 | cloud/HPC와 결합 가능 |

<!-- subnote-page:apply -->

### 적용 예제

**4GPU data parallel**

강사 생성 학습 예제입니다. 공식 기준답안이 아닙니다.

**조건:** 단일GPU에 모델이 들어가며 한 step batch128을4GPU로 나눕니다.

1. 각 GPU가32개 표본의 gradient를 계산합니다.
2. 동기 집계 후 같은 파라미터를 갱신하며 글로벌 batch128을 유지합니다.
3. 계산100ms가25ms로 줄어도 통신20ms·I/O10ms가 추가되면55ms로 약1.82배입니다. 실제 겹침·기준 비용을 측정합니다.

**결과·해석:** GPU 수4와 실제 가속비4는 다르며 병목별 시간이 필요합니다.

**전제·주의:** 숫자는 계산 예시이며 특정 장비의 벤치마크가 아닙니다. DCI는 별도 거리·복제·대역폭 설계가 필요합니다.

### 답안 골격과 혼동 방지

배경·GPU/TPU 조건부 비교 → 병렬화4방식 → fabric·storage·software·시설 → 4GPU 시간 계산 → HPC/cloud 비교·TCO·복구

- GPU보다 TPU를 쓰는 이유를 모든 과업의 우위로 일반화하지 않습니다.
- FLOPS나 GPU 수 하나로 플랫폼 성능을 판정하지 않습니다.

### 내용을 가리고 회상

1. data parallel에서 왜 gradient 통신이 필요합니까?
2. 모델이 한 GPU에 안 들어가면 어떤 분할을 검토합니까?
3. 클라우드와 AI platform을 배타적 분류로 두면 왜 부정확합니까?

### 적용 기준과 근거

TPU·DDP·SuperPOD 공식 구조를 확인했습니다. tensor/pipeline/sharding 상세·전력/액체냉각·DCI 기술의 개별 설계 표준은 추가 확인 범위입니다.

**내용 검토 상태: 부분 확인**. 출처 확인은 공식 정답이나 학습 성취를 뜻하지 않습니다.

- [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) — Google Cloud; 상시 문서; 확인 2026-11-05. 확인 범위: 실제 열람: TPU ASIC·행렬 연산·HBM·slices·XLA와 CPU/GPU/TPU 적합/부적합 워크로드. TPU가 GPU를 일반적으로 대체한다는 전제를 거부합니다. / ASIC·행렬 연산·HBM·XLA 및 CPU/GPU/TPU 선택 조건 열람.
- [Getting Started with Distributed Data Parallel](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) — PyTorch developers; 튜토리얼 2.15.0+cu132 표시; 확인 2026-11-05. 확인 범위: 실제 열람: process별 replica·autograd hook·backward gradient synchronization·straggler와 통신 중첩. GPU 수만큼 선형 가속된다는 주장은 하지 않습니다.
- [DGX SuperPOD B200 Reference Architecture](https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html) — NVIDIA; RA-11334-001 V08, 2025-04-24; 페이지 2026-09-02 갱신 표시; 확인 2026-11-05. 확인 범위: 실제 열람: compute/storage/management fabrics·고성능/사용자 스토리지·runtime/system management 역할. 특정 장비 가격·최신 세대 우위를 비교하지 않습니다.

## 연관 기출

- [제134회 2교시 4번](../questions/qnet-134-p2.md#q4) — AI DC 저지연·스케일링; DCI. 대응: 핵심원리; 부분 충족.
- [제134회 4교시 2번](../questions/qnet-134-p4.md#q2) — 멀티GPU 개념·장점; 구축 고려사항. 대응: 핵심원리; 충족.
- [제138회 2교시 3번](../questions/qnet-138-p2.md#q3) — GPU/TPU 개념·비교; TPU 선택 이유·효율·전망. 대응: 핵심원리; 충족.
- [제140회 2교시 4번](../questions/qnet-140-p2.md#q4) — AI 슈퍼컴퓨팅 배경; 구성 역할; HPC·cloud 비교. 대응: 핵심원리; 충족.
- [제140회 4교시 6번](../questions/qnet-140-p4.md#q6) — AI DC 정의·배경; 기존 DC 비교; 핵심 기술. 대응: 핵심원리; 부분 충족.

## 브레인스토밍

예제의 입력·제약을 바꾸면 어떤 판단과 결과가 달라지는지 설명하고, 관련 기출의 요구를 비교합니다. 새 해석은 출처의 사실과 구분해 기록합니다.
