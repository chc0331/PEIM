# 시스템·통신·클라우드·보안·개인정보·AI 거버넌스 서브노트 연구

- 확인일: 2026-11-05. 제126~140회 공식 수집 원장(record.json) 465문항을 읽고 담당 범위의 189문항을 72개 토픽, 192개 요구 연결로 정리했습니다.
- 수집 형태: 실제 열람한 1차 출처의 URL·판본·확인 범위와 강사가 생성한 자체 설명·가상 예제입니다. 웹 원문 전체를 복제하지 않았습니다. 공식 기출과 자체 계산 예제를 구분했습니다.
- 검증 상태: 출처 확인 33개, 부분 확인 39개입니다. 부분 확인은 설명 전체나 법정 요건이 검증됐다는 뜻이 아닙니다. 출처의 `notes`, 토픽의 `version_note`와 예제의 `caution`을 함께 읽어야 합니다.
- 원문 확인의 주요 한계: ISO/IEC42001 유료 전문, 최신 ISMS-P·간편인증·CSAP 상세 기준, N2SF 전문, CISA 성숙도2.0, 국내 고시의 모든 조항·부칙, AI기본법 시행령·고시·최초판 전 조문, IoT 공통보안7원칙 및 특정 침해사건 원자료는 충분히 열람하지 못했습니다. 홈페이지 안내·공식 색인만 확인한 경우 이를 출처 메타데이터에 밝혔으며 일반 설계 지식을 해당 요건의 확인으로 대체하지 않았습니다.
- 법령 시점: AI기본법 최초 시행 2026-01-22와 이번에 읽은 현행 표시 2026-07-21을 분리했습니다. 현행 제6·7·34조는 직접 읽었으며 고영향 정의·활용 영역은 법제처 공식 해설로 확인했습니다. 개인정보 안전성 기준의 단계 시행과 개정판 차이를 일괄 현재 의무로 단정하지 않았습니다.
- 의미 구분: `aliases`에는 다른 개념을 넣지 않았습니다. 복합 계산·비교 단원의 유관 개념은 필요할 때 `related_terms`에 기록합니다. 문서 생성은 개인 학습 숙련도를 올리는 근거가 아닙니다.
- 검산: /24 고정4분할, /22 VLSM의 경계·중첩·수용량, 은행가 안전순서, SRT 대기시간, HPA 기본식, RSA 정수 예제, OFB 재사용 XOR, 차등 맨체스터 역해독, DP 척도·기본 합성, MPC 모듈러 합, FedAvg 가중평균을 직접 확인했습니다.
- 구조 검사: 토픽 ID 중복 없음, 출처 ID 참조 유효, 모든 표의 행·열 수 일치, 토픽별 회상 질문3개, 모든 연결 기출 번호가 465문항 원장에 존재함을 확인했습니다. 본문 실질 문자열은 토픽별 992~1416자이며 JSON 키와 요구 매핑은 제외한 수치입니다.

아래 JSON은 출판·위키 반영을 위한 구조화된 조사 결과입니다. 요구의 `부분 충족`과 토픽의 `부분 확인`을 완료 판정으로 승격하지 마십시오.

```json
{
  "sources": [
    {
      "id": "sys-linux-locks",
      "title": "Lock types and their rules",
      "url": "https://docs.kernel.org/locking/locktypes.html",
      "author": "Linux Kernel documentation",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "sleeping/spinning lock, owner semantics, rt_mutex PI 절을 열람. 커널 내부 락의 제약과 일반 사용자 동기화 개념은 구분."
    },
    {
      "id": "sys-linux-pagetables",
      "title": "Page Tables",
      "url": "https://docs.kernel.org/mm/page_tables.html",
      "author": "Linux Kernel documentation",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "가상 → 물리 주소, 계층형 페이지 테이블, 4KiB 주소 예시 열람."
    },
    {
      "id": "sys-linux-wait",
      "title": "wait(2)",
      "url": "https://man7.org/linux/man-pages/man2/wait.2.html",
      "author": "Linux man-pages project",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "종료한 자식 회수와 좀비 상태 설명 열람."
    },
    {
      "id": "sys-banker",
      "title": "EWD108: Een algorithme ter voorkoming van de dodelijke omarming",
      "url": "https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD108.html",
      "author": "Edsger W. Dijkstra / University of Texas archive",
      "published": "전사 수정 2004-01-06",
      "checked_at": "2026-11-05",
      "notes": "은행가 원고 전사 열람. 단일 자원 원고를 다중 자원 벡터 교육 예시로 확장한 부분은 자체 예시."
    },
    {
      "id": "sys-cfs",
      "title": "CFS Scheduler",
      "url": "https://docs.kernel.org/scheduler/sched-design-CFS.html",
      "author": "Linux Kernel documentation",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "CFS 가상 실행 시간 원리와 EEVDF로 이행 중임을 알리는 문구 확인. SJF를 Linux 현행 기본 정책이라 주장하지 않음."
    },
    {
      "id": "sys-linux-dma",
      "title": "Dynamic DMA mapping Guide",
      "url": "https://docs.kernel.org/core-api/dma-api-howto.html",
      "author": "Linux Kernel documentation",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "CPU virtual/physical/bus address, IOMMU, coherent와 streaming mapping 절 열람."
    },
    {
      "id": "sys-rtmutex",
      "title": "RT-mutex implementation design",
      "url": "https://docs.kernel.org/locking/rt-mutex-design.html",
      "author": "Steven Rostedt / Linux Kernel",
      "published": "2006 저작권 표기",
      "checked_at": "2026-11-05",
      "notes": "우선순위 역전·상속 및 PI chain에 관한 구현 설명 열람. 우선순위 천장 자체 원전은 미열람."
    },
    {
      "id": "sys-shm",
      "title": "shm_overview(7)",
      "url": "https://man7.org/linux/man-pages/man7/shm_overview.7.html",
      "author": "Linux man-pages project",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "POSIX 공유 메모리 shm_open/ftruncate/mmap 및 동기화 필요 설명 열람."
    },
    {
      "id": "sys-malloc",
      "title": "malloc(3)",
      "url": "https://man7.org/linux/man-pages/man3/malloc.3.html",
      "author": "Linux man-pages project",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "malloc/free 계약 및 오류 설명 열람. Java/Python GC 세부 구현은 이 출처 범위 밖."
    },
    {
      "id": "sys-ostep-sched",
      "title": "OSTEP: Scheduling Introduction",
      "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf",
      "author": "Remzi H. Arpaci-Dusseau; Andrea C. Arpaci-Dusseau / UW-Madison",
      "published": "공개판 1.10",
      "checked_at": "2026-11-05",
      "notes": "저자 공개 교재 PDF 열람. SJF/STCF, 반환·응답 시간과 가정. 제품 규격이나 공식 채점 기준 아님."
    },
    {
      "id": "sys-ostep-seg",
      "title": "OSTEP: Segmentation",
      "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/vm-segmentation.pdf",
      "author": "Remzi H. Arpaci-Dusseau; Andrea C. Arpaci-Dusseau / UW-Madison",
      "published": "공개판 1.10",
      "checked_at": "2026-11-05",
      "notes": "저자 공개 교재 PDF 열람. base/bounds, 논리 세그먼트와 외부단편화 설명."
    },
    {
      "id": "sys-ostep-vm",
      "title": "OSTEP: Beyond Physical Memory Policies",
      "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/vm-beyondphys-policy.pdf",
      "author": "Remzi H. Arpaci-Dusseau; Andrea C. Arpaci-Dusseau / UW-Madison",
      "published": "공개판 1.10",
      "checked_at": "2026-11-05",
      "notes": "교체정책과 메모리 압력, AMAT 설명 PDF 열람."
    },
    {
      "id": "sys-ostep-disk",
      "title": "OSTEP: Hard Disk Drives",
      "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/file-disks.pdf",
      "author": "Remzi H. Arpaci-Dusseau; Andrea C. Arpaci-Dusseau / UW-Madison",
      "published": "공개판 1.10",
      "checked_at": "2026-11-05",
      "notes": "HDD 기하와 탐색·회전 지연 및 스케줄링 PDF 열람. SSD의 현행 지연과 구분."
    },
    {
      "id": "sys-tpu",
      "title": "Introduction to Cloud TPU",
      "url": "https://docs.cloud.google.com/tpu/docs/intro-to-tpu",
      "author": "Google Cloud",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "ASIC·행렬 연산·HBM·XLA 및 CPU/GPU/TPU 선택 조건 열람."
    },
    {
      "id": "sys-neuromorphic",
      "title": "Neuromorphic Computing and Engineering",
      "url": "https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html",
      "author": "Intel Labs",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "Loihi2 이벤트 기반 SNN, 메모리·연산 결합 소개 열람. 제조사 실험 수치를 보편 성능으로 쓰지 않음."
    },
    {
      "id": "sys-cxl",
      "title": "About CXL",
      "url": "https://computeexpresslink.org/about-cxl/",
      "author": "CXL Consortium",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "캐시 일관성 인터커넥트 소개와 4.0 현행 표기 열람. 버전별 지원은 제품·명세 확인 필요."
    },
    {
      "id": "sys-rfc4632",
      "title": "RFC4632: Classless Inter-domain Routing",
      "url": "https://www.rfc-editor.org/rfc/rfc4632.html",
      "author": "V. Fuller; T. Li / IETF",
      "published": "2006-08",
      "checked_at": "2026-11-05",
      "notes": "IPv4 프리픽스·집성 원문 열람. 서브넷 계산은 자체 검산."
    },
    {
      "id": "sys-rfc5681",
      "title": "RFC5681: TCP Congestion Control",
      "url": "https://www.rfc-editor.org/rfc/rfc5681.html",
      "author": "M. Allman; V. Paxson; E. Blanton / IETF",
      "published": "2009-09",
      "checked_at": "2026-11-05",
      "notes": "slow start, avoidance, fast retransmit/recovery, cwnd/ssthresh 식 열람. CUBIC 등 모든 현행 구현의 동일 동작을 뜻하지 않음."
    },
    {
      "id": "sys-rfc9293",
      "title": "RFC9293: Transmission Control Protocol",
      "url": "https://www.rfc-editor.org/rfc/rfc9293.html",
      "author": "W. Eddy (ed.) / IETF",
      "published": "2022-08",
      "checked_at": "2026-11-05",
      "notes": "TCP 연결·종료·순서 번호와 3-way handshake Figure6 직접 열람."
    },
    {
      "id": "sys-rfc9260",
      "title": "RFC9260: Stream Control Transmission Protocol",
      "url": "https://www.rfc-editor.org/rfc/rfc9260.html",
      "author": "R. Stewart et al. / IETF",
      "published": "2022-06",
      "checked_at": "2026-11-05",
      "notes": "SCTP 메시지·멀티스트리밍·멀티호밍·association 설명 열람."
    },
    {
      "id": "sys-rfc2453",
      "title": "RFC2453: RIP Version 2",
      "url": "https://www.rfc-editor.org/rfc/rfc2453.html",
      "author": "G. Malkin / IETF",
      "published": "1998-11",
      "checked_at": "2026-11-05",
      "notes": "거리벡터·16 infinity·split horizon 절 열람."
    },
    {
      "id": "sys-rfc2328",
      "title": "RFC2328: OSPF Version 2",
      "url": "https://www.rfc-editor.org/rfc/rfc2328.html",
      "author": "J. Moy / IETF",
      "published": "1998-04",
      "checked_at": "2026-11-05",
      "notes": "링크상태·LSDB·최단경로트리·area 개요 열람."
    },
    {
      "id": "sys-rfc4271",
      "title": "RFC4271: Border Gateway Protocol 4",
      "url": "https://www.rfc-editor.org/rfc/rfc4271.html",
      "author": "Y. Rekhter et al. / IETF",
      "published": "2006-01",
      "checked_at": "2026-11-05",
      "notes": "AS 경로·도달성·정책·CIDR 원문 열람."
    },
    {
      "id": "sys-rfc7348",
      "title": "RFC7348: VXLAN",
      "url": "https://www.rfc-editor.org/rfc/rfc7348.html",
      "author": "M. Mahalingam et al. / RFC Editor",
      "published": "2014-08",
      "checked_at": "2026-11-05",
      "notes": "Informational RFC. 24비트 VNI와 L2-over-L3 설명 열람."
    },
    {
      "id": "sys-rfc7149",
      "title": "RFC7149: Software-Defined Networking",
      "url": "https://www.rfc-editor.org/rfc/rfc7149.html",
      "author": "M. Boucadair; C. Jacquenet / IETF",
      "published": "2014-03",
      "checked_at": "2026-11-05",
      "notes": "SDN 개요·제어 기능 관점 원문 열람. OpenFlow 명세 전체는 미열람."
    },
    {
      "id": "sys-rfc1633",
      "title": "RFC1633: Integrated Services Overview",
      "url": "https://www.rfc-editor.org/rfc/rfc1633.html",
      "author": "R. Braden; D. Clark; S. Shenker / IETF",
      "published": "1994-06",
      "checked_at": "2026-11-05",
      "notes": "WFQ에 의한 가중 대역 분배 설명 열람."
    },
    {
      "id": "sys-cloud",
      "title": "NIST SP800-145: Definition of Cloud Computing",
      "url": "https://csrc.nist.gov/pubs/sp/800/145/final",
      "author": "Peter Mell; Timothy Grance / NIST",
      "published": "2011-09",
      "checked_at": "2026-11-05",
      "notes": "공식 게재 페이지 열람. 5특성·3서비스·4배포 모델을 확인하되 제품별 책임은 계약 확인."
    },
    {
      "id": "sys-dr",
      "title": "Disaster recovery options in the cloud",
      "url": "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html",
      "author": "AWS",
      "published": "상시 백서",
      "checked_at": "2026-11-05",
      "notes": "active/passive, pilot light, warm standby, active/active 설명 열람. 제시 예시시간은 보장값으로 사용하지 않음."
    },
    {
      "id": "sys-k8s",
      "title": "Kubernetes Components",
      "url": "https://kubernetes.io/docs/concepts/overview/components/",
      "author": "Kubernetes project",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "Control plane·worker 컴포넌트 문서 열람. 특정 버전 API 세부가 아닌 공통 구조."
    },
    {
      "id": "sys-hpa",
      "title": "Horizontal Pod Autoscaling",
      "url": "https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/",
      "author": "Kubernetes project",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "desiredReplicas 식·metrics·안정화와 자원 request 조건 열람."
    },
    {
      "id": "sys-storage",
      "title": "Block vs File vs Object Storage",
      "url": "https://aws.amazon.com/compare/the-difference-between-block-file-object-storage/",
      "author": "AWS",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "접근 단위·계층·워크로드 차이 공식 비교 열람."
    },
    {
      "id": "sys-lambda",
      "title": "What is AWS Lambda?",
      "url": "https://docs.aws.amazon.com/lambda/latest/dg/welcome.html",
      "author": "AWS",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "서버 관리 없는 실행·이벤트와 함수 서비스 개요 열람."
    },
    {
      "id": "sys-terraform",
      "title": "What is Terraform",
      "url": "https://developer.hashicorp.com/terraform/intro",
      "author": "HashiCorp",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "Write-Plan-Apply와 버전 관리 가능한 인프라 정의 설명 열람."
    },
    {
      "id": "sys-wifi7",
      "title": "How Wi-Fi7 Works",
      "url": "https://www.juniper.net/documentation/us/en/software/mist/wi-fi-7-guide/wi-fi-7/topics/concept/how-wi-fi-7-works.html",
      "author": "Juniper Networks",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "공식 제품 문서의 320MHz·MLO·4K-QAM 설명 열람. Wi-Fi Alliance 페이지는 502 실패."
    },
    {
      "id": "sys-wifi8",
      "title": "IEEE P802.11bn Project Authorization Request",
      "url": "https://www.ieee802.org/11/PARs/P802.11bn_PAR.pdf",
      "author": "IEEE802.11",
      "published": "PAR 2023-09-21 승인",
      "checked_at": "2026-11-05",
      "notes": "3쪽 PAR 원문 열람. UHR 프로젝트 목표이며 완성 규격으로 서술하지 않음."
    },
    {
      "id": "sys-6g",
      "title": "ITU-R M.2160-0: IMT2030 Framework",
      "url": "https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf",
      "author": "ITU-R",
      "published": "2023-11",
      "checked_at": "2026-11-05",
      "notes": "21쪽 원문 열람. 사용 시나리오·능력 목표는 상용 보장 및 최종 무선규격과 구분."
    },
    {
      "id": "sys-nfc",
      "title": "NFC Technology Technical Overview",
      "url": "https://nfc-forum.org/learn/nfc-technology/",
      "author": "NFC Forum",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "13.56MHz·유도결합·배터리 없는 동작·NDEF 소개 열람. 전송률·거리 일반 화 주의."
    },
    {
      "id": "sys-modbus",
      "title": "Modbus Specifications and Implementation Guides",
      "url": "https://www.modbus.org/modbus-specifications",
      "author": "Modbus Organization",
      "published": "Application protocol V1.1b3 소개",
      "checked_at": "2026-11-05",
      "notes": "공식 규격 목록 및 보안 프로토콜 소개 열람. 기능 코드별 예외와 ISA62443 조항은 미열람."
    },
    {
      "id": "sys-airmf",
      "title": "NIST AI100-1: AI RMF1.0",
      "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
      "author": "NIST",
      "published": "2023-01",
      "checked_at": "2026-11-05",
      "notes": "원문 PDF 열람. 신뢰성 7특성, GOVERN/MAP/MEASURE/MANAGE 및 Profiles. 자발적 프레임워크이며 인증 규격 아님."
    },
    {
      "id": "sys-42001",
      "title": "ISO/IEC42001:2023 AI Management System",
      "url": "https://www.iso.org/standard/42001",
      "author": "ISO/IEC",
      "published": "2023-12 판1",
      "checked_at": "2026-11-05",
      "notes": "공식 소개·공개 개요만 열람. 유료 표준 전문 및 인증 심사 조항 전체 미열람. 상세 준수 판정 금지."
    },
    {
      "id": "sys-owasp",
      "title": "2025 Top10 Risk and Mitigations for LLMs and GenAI Apps",
      "url": "https://genai.owasp.org/llm-top-10/",
      "author": "OWASP GenAI Security Project",
      "published": "2025 목록",
      "checked_at": "2026-11-05",
      "notes": "2025 공식 위험 목록과 링크된 설명 열람. 규제·인증 기준이 아닌 보안 실무 참고."
    },
    {
      "id": "sys-zerotrust",
      "title": "NIST SP800-207: Zero Trust Architecture",
      "url": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf",
      "author": "Scott Rose et al. / NIST",
      "published": "2020-08",
      "checked_at": "2026-11-05",
      "notes": "59쪽 PDF 열람. 신뢰 가정 제거와 PE/PA/PEP. CISA 성숙도2.0 페이지는 403으로 세부 단계 미확인."
    },
    {
      "id": "sys-modes",
      "title": "NIST SP800-38A: Block Cipher Modes",
      "url": "https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf",
      "author": "Morris Dworkin / NIST",
      "published": "2001-12",
      "checked_at": "2026-11-05",
      "notes": "ECB/CBC/CFB/OFB/CTR 원문과 식 열람. 기밀성 모드이 므로 단독 무결성 보장 없음."
    },
    {
      "id": "sys-aes",
      "title": "FIPS197-upd1: AES",
      "url": "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf",
      "author": "NIST",
      "published": "2023-05-09 갱신",
      "checked_at": "2026-11-05",
      "notes": "128비트 블록·128/192/256키 원문 PDF 열람. 2023 갱신은 알고리즘 변경이 아님."
    },
    {
      "id": "sys-tls",
      "title": "RFC8446: TLS1.3",
      "url": "https://www.rfc-editor.org/rfc/rfc8446.html",
      "author": "Eric Rescorla / IETF",
      "published": "2018-08",
      "checked_at": "2026-11-05",
      "notes": "핸드셰이크·구형 알고리즘 제거·0-RTT 재전송 위험 설명 열람."
    },
    {
      "id": "sys-hmac",
      "title": "RFC2104: HMAC",
      "url": "https://www.rfc-editor.org/rfc/rfc2104.html",
      "author": "H. Krawczyk et al. / IETF",
      "published": "1997-02",
      "checked_at": "2026-11-05",
      "notes": "비밀키 기반 해시 MAC 구성 원문 열람. 당시 MD5/SHA1 예시를 현행 권장으로 제시하지 않음."
    },
    {
      "id": "sys-rsa",
      "title": "RFC8017: PKCS#1 v2.2",
      "url": "https://www.rfc-editor.org/rfc/rfc8017.html",
      "author": "K. Moriarty et al. / IETF",
      "published": "2016-11",
      "checked_at": "2026-11-05",
      "notes": "RSA 원시연산·암호화·서명 스킴 구분 열람. 작은 정수 예시는 교육용."
    },
    {
      "id": "sys-cms",
      "title": "RFC5652: Cryptographic Message Syntax",
      "url": "https://www.rfc-editor.org/rfc/rfc5652.html",
      "author": "R. Housley / IETF",
      "published": "2009-09",
      "checked_at": "2026-11-05",
      "notes": "서명·인증·암호화 및 EnvelopedData 구조 개요 열람."
    },
    {
      "id": "sys-ldap",
      "title": "RFC4513: LDAP Authentication Methods",
      "url": "https://www.rfc-editor.org/rfc/rfc4513.html",
      "author": "R. Harrison / IETF",
      "published": "2006-06",
      "checked_at": "2026-11-05",
      "notes": "Bind·SASL·StartTLS와 인증/인가 상태 원문 열람."
    },
    {
      "id": "sys-ipsec",
      "title": "RFC4301: Security Architecture for IP",
      "url": "https://www.rfc-editor.org/rfc/rfc4301.html",
      "author": "S. Kent; K. Seo / IETF",
      "published": "2005-12",
      "checked_at": "2026-11-05",
      "notes": "IPsec·SA·SPD/SAD 및 transport/tunnel 개요 열람."
    },
    {
      "id": "sys-tor",
      "title": "About Tor",
      "url": "https://support.torproject.org/about-tor/",
      "author": "Tor Project",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "공식 소개·설계·보안 보호와 한계 목록 열람. 모든 트래픽 익명성 보장이라고 쓰지 않음."
    },
    {
      "id": "sys-signature",
      "title": "FIPS186-5: Digital Signature Standard",
      "url": "https://csrc.nist.gov/pubs/fips/186-5/final",
      "author": "NIST",
      "published": "2023-02-03",
      "checked_at": "2026-11-05",
      "notes": "공식 게재 페이지 열람. 서명 목적과 개정 상태 확인; DSA 신규 서명 제한은 본문 후속 확인 필요."
    },
    {
      "id": "sys-pqc",
      "title": "FIPS203: ML-KEM",
      "url": "https://csrc.nist.gov/pubs/fips/203/final",
      "author": "NIST",
      "published": "2024-08-13",
      "checked_at": "2026-11-05",
      "notes": "ML-KEM과 3개 파라미터 공식 설명 열람. 2025-11 잠재 정정 공지 있음."
    },
    {
      "id": "sys-fips140",
      "title": "FIPS140-2 Security Requirements for Cryptographic Modules",
      "url": "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.140-2.pdf",
      "author": "NIST",
      "published": "2001-05-25;2002정정",
      "checked_at": "2026-11-05",
      "notes": "69쪽 PDF의 4수준·보안영역 열람. 구판 문제 해설이며 현행 도입은140-3 전환상태 확인 필요."
    },
    {
      "id": "sys-tpm",
      "title": "TPM2.0 Library",
      "url": "https://www.trustedcomputinggroup.org/resources/documents/tpm-library-specification",
      "author": "Trusted Computing Group",
      "published": "상시 규격목록",
      "checked_at": "2026-11-05",
      "notes": "공식 규격 게재 페이지 열람. PCR·seal·attest의 상세 명령 명세는 미열람."
    },
    {
      "id": "sys-identity",
      "title": "NIST SP800-63B-4 Authentication",
      "url": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf",
      "author": "NIST",
      "published": "2025-07",
      "checked_at": "2026-11-05",
      "notes": "인증·인증 수단 관리 원문 PDF 열람. 국내 법 인증 요건과 별개."
    },
    {
      "id": "sys-forensic",
      "title": "NIST SP800-86 Integrating Forensics into Incident Response",
      "url": "https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf",
      "author": "Karen Kent et al. / NIST",
      "published": "2006-08",
      "checked_at": "2026-11-05",
      "notes": "수집·검사·분석·보고, 파일·OS·네트워크·응용 데이터 설명 열람. 법적 증거능력 보장 문서 아님."
    },
    {
      "id": "sys-mitre",
      "title": "MITRE ATT&CK TA0008 Lateral Movement",
      "url": "https://attack.mitre.org/tactics/TA0008/",
      "author": "MITRE",
      "published": "최종수정 2025-08-11",
      "checked_at": "2026-11-05",
      "notes": "정상 자격증명·원격서비스로 측면이동하는 전술과 기법 열람."
    },
    {
      "id": "sys-nhi",
      "title": "Workload identities overview",
      "url": "https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview",
      "author": "Microsoft",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "workload/device/human identity 구분과 관리형 신원·수명 관리 위험 열람."
    },
    {
      "id": "sys-mcp",
      "title": "MCP Security Best Practices",
      "url": "https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices",
      "author": "Model Context Protocol project",
      "published": "2026-07-28 경로",
      "checked_at": "2026-11-05",
      "notes": "confused deputy, token passthrough, SSRF, scope 최소화 실제 열람. 최신 링크가 이 판으로 리다이렉트."
    },
    {
      "id": "sys-mirai",
      "title": "Common IoT Devices May Expose Consumers to Cyber Exploitation",
      "url": "https://www.ic3.gov/PSA/2017/PSA171017",
      "author": "FBI IC3",
      "published": "2017-10-17",
      "checked_at": "2026-11-05",
      "notes": "Mirai·기본 자격증명·IoT 보안 권고 공식 공지 실제 열람."
    },
    {
      "id": "sys-bpfdoor",
      "title": "BPFDoor 악성코드 점검 가이드 공지",
      "url": "https://www.krcert.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=71754&pageIndex=1",
      "author": "KISA KrCERT/CC",
      "published": "2025-05-12",
      "checked_at": "2026-11-05",
      "notes": "공식 공지 열람. 첨부 PDF의 변종별 점검 값 전체는 미열람. 해시·프로세스명만의 완전탐지 주장 금지."
    },
    {
      "id": "sys-dp",
      "title": "The Algorithmic Foundations of Differential Privacy",
      "url": "https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf",
      "author": "Cynthia Dwork; Aaron Roth",
      "published": "2014",
      "checked_at": "2026-11-05",
      "notes": "저자 원문 PDF 열람. 인접 데이터셋·프라이버시 파라미터 정의와 순차 합성 개념."
    },
    {
      "id": "sys-he",
      "title": "Homomorphic Encryption Standardization",
      "url": "https://homomorphicencryption.org/standard/",
      "author": "HE Standardization consortium",
      "published": "2018 표준 소개",
      "checked_at": "2026-11-05",
      "notes": "공식 컨소시엄의 표준·보안 가이드 소개 열람. 특정 파라미터 조합 검증은 미수행."
    },
    {
      "id": "sys-pbd",
      "title": "Privacy by Design: Seven Foundational Principles",
      "url": "https://www.ipc.on.ca/sites/default/files/legacy/2018/01/pbd.pdf",
      "author": "Information and Privacy Commissioner of Ontario",
      "published": "2018-01",
      "checked_at": "2026-11-05",
      "notes": "공공기관 2쪽 원문 열람. 7원칙 직접 확인."
    },
    {
      "id": "sys-pds",
      "title": "Privacy Design Strategies, The Little Blue Book",
      "url": "https://www.cs.ru.nl/~jhh/publications/pds-booklet.pdf",
      "author": "Jaap-Henk Hoepman",
      "published": "2022-04-19",
      "checked_at": "2026-11-05",
      "notes": "저자 원문 8전략 열람. abstract를 기존 문헌의 aggregate와 무조건 동일 용어로 바꾸지 않음."
    },
    {
      "id": "sys-isms",
      "title": "ISMS-P 공식 누리집",
      "url": "https://isms.kisa.or.kr/",
      "author": "KISA",
      "published": "2026 표시 페이지",
      "checked_at": "2026-11-05",
      "notes": "인증 제도 공식 소개 열람. 자료실은 502 실패; 2023.11 안내서 및2024.7 간편인증 목록만 검색으로 확인. 상세 최신 항목·의무 대상 미확인."
    },
    {
      "id": "sys-aiact",
      "title": "인공지능기본법 제34조 조문정보",
      "url": "https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031809501",
      "author": "국가법령정보센터",
      "published": "시행2026-07-21;법률21311호",
      "checked_at": "2026-11-05",
      "notes": "현행 표시 제34조 6개 책무 직접 열람. 138기출의2026-01-22 최초판·시행령·다른 조문 전체 미열람."
    },
    {
      "id": "sys-aiact-history",
      "title": "인공지능기본법 제정판 연혁",
      "url": "https://www.law.go.kr/lsInfoP.do?ancYnChk=0&efYd=20260122&lsiSeq=268543",
      "author": "국가법령정보센터",
      "published": "2025-01-21 제정;2026-01-22 시행",
      "checked_at": "2026-11-05",
      "notes": "연혁 헤더 직접 열람. 동적 본문 미노출로 개별조문 전체 확인 불가."
    },
    {
      "id": "sys-privacy-guides",
      "title": "개인정보보호위원회 현재 안내서 목록",
      "url": "https://pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS217&mCode=D010030000.Updated",
      "author": "개인정보보호위원회",
      "published": "목록에2026-03 가명정보 가이드 표시",
      "checked_at": "2026-11-05",
      "notes": "공식 현재 안내서 목록 확인. 첨부 원문 미열람으로 현행 세부요건 확인 필요."
    },
    {
      "id": "sys-safezone",
      "title": "개인정보위 신산업 혁신 및 안심구역 운영",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148936325",
      "author": "개인정보보호위원회 / 정책브리핑",
      "published": "2024 보도자료",
      "checked_at": "2026-11-05",
      "notes": "안전한 가명정보 분석공간 소개 실제 열람. 지정요건 전문은 미열람."
    },
    {
      "id": "sys-mit",
      "title": "The MIT License",
      "url": "https://opensource.org/license/MIT",
      "author": "Open Source Initiative",
      "published": "SPDX MIT;게시일 미표시",
      "checked_at": "2026-11-05",
      "notes": "라이선스 원문 실제 열람. 고지 유지 의무 자체 요약."
    },
    {
      "id": "sys-osaid",
      "title": "Open Source AI Definition1.0",
      "url": "https://opensource.org/ai/open-source-ai-definition",
      "author": "Open Source Initiative",
      "published": "1.0",
      "checked_at": "2026-11-05",
      "notes": "4자유, 데이터 정보·코드·파라미터 요구 실제 열람. 오픈웨이트와 오픈소스 AI 구분."
    },
    {
      "id": "sys-genai-profile",
      "title": "NIST AI600-1 Generative AI Profile",
      "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
      "author": "NIST",
      "published": "2024-07",
      "checked_at": "2026-11-05",
      "notes": "원문 PDF 열람. 생성형AI 고유 위험 및 생애주기 대응. 법적 적법성 판정 아님."
    },
    {
      "id": "sys-websocket",
      "title": "RFC6455: The WebSocket Protocol",
      "url": "https://www.rfc-editor.org/rfc/rfc6455.html",
      "author": "I. Fette; A. Melnikov / IETF",
      "published": "2011-12",
      "checked_at": "2026-11-05",
      "notes": "오프닝 핸드셰이크·TCP 위 메시지 프레이밍·양방향 통신 원문 열람."
    },
    {
      "id": "sys-qubit",
      "title": "Single Systems: Introduction",
      "url": "https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/introduction",
      "author": "John Watrous / IBM Quantum Learning",
      "published": "상시 강의",
      "checked_at": "2026-11-05",
      "notes": "복소벡터·측정·유니터리 행렬의 공식 강의 소개 열람. 물리 구현 상세는 미열람."
    },
    {
      "id": "sys-mementos",
      "title": "Getting Things Done on Computational RFIDs with Energy-Aware Checkpointing",
      "url": "https://static.usenix.org/events/hotpower08/tech/full_papers/ransford/ransford_html/",
      "author": "Benjamin Ransford et al. / USENIX",
      "published": "2008",
      "checked_at": "2026-11-05",
      "notes": "원학회 검색 노출 본문의 체크포인트·전압 측정 설명 확인. 직접 open은 접근실패로 전문 열람 아님."
    },
    {
      "id": "sys-containers",
      "title": "What is a container?",
      "url": "https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/",
      "author": "Docker",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "격리된 프로세스와 VM 비교 공식 제품 문서 실제 열람."
    },
    {
      "id": "sys-daas",
      "title": "What is Azure Virtual Desktop?",
      "url": "https://learn.microsoft.com/en-us/azure/virtual-desktop/overview",
      "author": "Microsoft",
      "published": "상시 문서",
      "checked_at": "2026-11-05",
      "notes": "데스크톱·앱 가상화와 full desktop/RemoteApp 제공 공식 설명 열람."
    },
    {
      "id": "sys-ecc",
      "title": "RFC6090: Fundamental Elliptic Curve Cryptography Algorithms",
      "url": "https://www.rfc-editor.org/rfc/rfc6090.html",
      "author": "D. McGrew; K. Igoe; M. Salter / IETF",
      "published": "2011-02",
      "checked_at": "2026-11-05",
      "notes": "타원곡선군·이산로그·공개 키 알고리즘 배경 실제 열람."
    },
    {
      "id": "sys-abac",
      "title": "NIST SP800-162: ABAC Definition and Considerations",
      "url": "https://csrc.nist.gov/pubs/sp/800/162/upd1/final",
      "author": "NIST",
      "published": "2014;2019갱신",
      "checked_at": "2026-11-05",
      "notes": "주체·객체·환경 속성·정책 기반 접근 결정의 공식 소개 열람. BLP/Biba/CW원논문은미열람."
    },
    {
      "id": "sys-aml",
      "title": "NIST AI100-2e2025: Adversarial Machine Learning",
      "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf",
      "author": "Apostol Vassilev et al. / NIST",
      "published": "2025-03",
      "checked_at": "2026-11-05",
      "notes": "127쪽 공식 PDF 열람. 회피·오염·프라이버시·오용과 생애주기별 위협 분류."
    },
    {
      "id": "sys-pipa-auto",
      "title": "개인정보보호법 제37조의2 조문정보",
      "url": "https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1029335635",
      "author": "국가법령정보센터",
      "published": "2026-09-11시행;법률21445호",
      "checked_at": "2026-11-05",
      "notes": "공식 조문 정보에 서 3항의대응 의무와 현행판표시직접 열람.제37조의2전체 및시행령은 미열람."
    },
    {
      "id": "sys-privacy-safety",
      "title": "개인정보의 안전성 확보조치 기준",
      "url": "https://www.law.go.kr/admRulLsInfoP.do?admRulId=73493&efYd=0",
      "author": "국가법령정보센터",
      "published": "2026-07-01개정표시",
      "checked_at": "2026-11-05",
      "notes": "공식 페이지및검색본문에서암호화·접속기록과 부칙시행차이확인.동적전문미노출로 최신전항목 미확인."
    },
    {
      "id": "sys-aiethics",
      "title": "2020 AI 윤리기준",
      "url": "https://ai.kisdi.re.kr/aieth/main/contents.do?menuNo=400029",
      "author": "과기정통부·KISDI",
      "published": "2020-12-23",
      "checked_at": "2026-11-05",
      "notes": "공식윤리소통채널의3원칙·10요건 설명실제 열람."
    },
    {
      "id": "sys-reverseproxy",
      "title": "What is a Reverse Proxy?",
      "url": "https://www.f5.com/glossary/reverse-proxy",
      "author": "F5",
      "published": "상시문서",
      "checked_at": "2026-11-05",
      "notes": "공식 제품사설명의 중계·부하분산·보안 기능열람."
    },
    {
      "id": "sys-mpc",
      "title": "Multi-Party Threshold Cryptography",
      "url": "https://csrc.nist.gov/projects/threshold-cryptography",
      "author": "NIST",
      "published": "상시프로젝트",
      "checked_at": "2026-11-05",
      "notes": "MPC 기반분산 신뢰·임계서명·키 생성·보조기술 설명직접 열람.특정 MPC 프로토콜 전문은 미열람."
    },
    {
      "id": "sys-seal",
      "title": "Microsoft SEAL official repository",
      "url": "https://github.com/microsoft/SEAL",
      "author": "Microsoft",
      "published": "열람시README",
      "checked_at": "2026-11-05",
      "notes": "BFV/BGV정수모듈러연산·CKKS근사실수/복소연산 설명직접 열람.특정 버전빌드나보안파라미터 시험은 미수행."
    },
    {
      "id": "sys-fedavg",
      "title": "Communication-Efficient Learning of Deep Networks from Decentralized Data",
      "url": "https://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf",
      "author": "H. Brendan McMahan et al. / Google;AISTATS",
      "published": "2017",
      "checked_at": "2026-11-05",
      "notes": "학회원논문PDF실제 열람.로컬업데이트집계와FedAvg.데이터가 중예시는자체검산."
    },
    {
      "id": "sys-aiact-plan",
      "title": "인공지능기본법 제6조 기본계획",
      "url": "https://law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1034284625",
      "author": "국가법령정보센터",
      "published": "시행2026-07-21",
      "checked_at": "2026-11-05",
      "notes": "현행제6조직접 열람.최초제정판과2026공공데이터·교육항목추가를구분."
    },
    {
      "id": "sys-aiact-official-guide",
      "title": "인공지능 및 고영향 인공지능 정의",
      "url": "https://www.easylaw.go.kr/CSP/CnpClsMain.laf?ccfNo=1&cciNo=1&cnpClsNo=1&csmSeq=2987",
      "author": "법제처 찾기쉬운생활법령정보",
      "published": "열람일현재",
      "checked_at": "2026-11-05",
      "notes": "정부해설의 고영향정의·법정활용 영역·사업자구분직접 열람.법 조문 원문과 시행령 전문 미열람은별도 표기."
    },
    {
      "id": "sys-metaverse-ethics",
      "title": "정부 메타버스 윤리원칙 발표",
      "url": "https://www.korea.kr/briefing/policyBriefingView.do?newsId=148908796",
      "author": "과기정통부 / 정책브리핑",
      "published": "2022-11-28",
      "checked_at": "2026-11-05",
      "notes": "3지향가치·8실천원칙·연성규범성격공식발표본문 직접 열람."
    },
    {
      "id": "sys-apache",
      "title": "Apache License Version2.0",
      "url": "https://www.apache.org/licenses/LICENSE-2.0",
      "author": "Apache Software Foundation",
      "published": "2004-01",
      "checked_at": "2026-11-05",
      "notes": "배포 고지·변경 표시·NOTICE·특허허여원문직접 열람."
    },
    {
      "id": "sys-gpl",
      "title": "GNU GPL version3",
      "url": "https://opensource.org/license/gpl-3.0",
      "author": "Free Software Foundation;OSI원문게재",
      "published": "2007-06-29",
      "checked_at": "2026-11-05",
      "notes": "OSI게재라이선스 원문직접 열람.GNU직접 링크는타임아웃.배포 조건·소스 제공개요를 설명하며 결합물법적 판단은하지 않음."
    },
    {
      "id": "sys-scancode",
      "title": "ScanCode Toolkit Documentation",
      "url": "https://scancode-toolkit.readthedocs.io/en/stable/",
      "author": "AboutCode / ScanCode project",
      "published": "상시문서",
      "checked_at": "2026-11-05",
      "notes": "코드·패키지·의존성의저작권·라이선스·취약점 탐지 기능 공식 문서직접 열람.법적완전성보장은아님."
    },
    {
      "id": "sys-cat",
      "title": "인공지능 신뢰성 인증 CAT 가이드 일러두기",
      "url": "https://tta-trustworthy-ai.gitbook.io/cat",
      "author": "TTA AI신뢰성센터",
      "published": "열람시현행가이드",
      "checked_at": "2026-11-05",
      "notes": "공식가 이드직접 열람.제품·서비스/조직의 4범위와 심사·시험차이.표준 전문과 2025기출 당시모든 판본은 미열람."
    },
    {
      "id": "sys-ai-user-guideline",
      "title": "생성형 AI 서비스 이용자 보호 가이드라인",
      "url": "https://user-archive.kisdi.re.kr/download/AIguideline.pdf",
      "author": "방송통신위원회·KISDI",
      "published": "2025-02-28",
      "checked_at": "2026-11-05",
      "notes": "공식 기관색인본문에서6실행 방식·입력 데이터 관리 설명 확인.직접 PDFopen타임아웃이므로 전문열람아님."
    },
    {
      "id": "sys-ai-committee",
      "title": "인공지능기본법 제7조",
      "url": "https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031809535",
      "author": "국가법령정보센터",
      "published": "시행2026-07-21",
      "checked_at": "2026-11-05",
      "notes": "대통령소속국가 인공지능전략위원회제7조직접 열람.심의세부대상관련후속조문전부는미열람."
    },
    {
      "id": "sys-ssdf",
      "title": "NIST SP800-218 SSDF1.1",
      "url": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf",
      "author": "Murugiah Souppaya;Karen Scarfone;Donna Dodson / NIST",
      "published": "2022-02",
      "checked_at": "2026-11-05",
      "notes": "원문PDF실제 열람.조직준비·SW보호·안전SW생산·취약점 대응의 4실무군.특정 개발 방법론을강제하지 않음."
    },
    {
      "id": "sys-manchester",
      "title": "Microchip DS60001813E: Encoding / Decoding",
      "url": "https://onlinedocs.microchip.com/oxy/GUID-51CE727C-126C-4670-A2BA-189781F25924-en-US-3/GUID-98860B4D-1868-47A4-A497-5C9F3373692C.html",
      "author": "Microchip Technology",
      "published": "DS60001813E 온라인판",
      "checked_at": "2026-11-05",
      "notes": "공식 제품 문서본문 직접 열람.1=시작전이없음, 0=시작전이있음, 중간전이필수, 극성반전에무관함을확인."
    },
    {
      "id": "sys-soar",
      "title": "What is SOAR?",
      "url": "https://www.microsoft.com/en-us/security/business/security-101/what-is-soar",
      "author": "Microsoft Security",
      "published": "2026-05-26 갱신",
      "checked_at": "2026-11-05",
      "notes": "공식 제품사문서본문 직접 열람.도구조정·자동화·사고 대응·플레이북·케이스관리·감독·SIEM비교확인."
    },
    {
      "id": "sys-cbpr",
      "title": "APEC Cross-Border Privacy Rules System Implementation: Peru",
      "url": "https://www.apec.org/apecapi/publication/getfile?publicationId=c688bc14-b066-471b-bd9c-5e83efc24882",
      "author": "Lucy L. Thomson / APEC Secretariat",
      "published": "2013-02",
      "checked_at": "2026-11-05",
      "notes": "APEC공식 24쪽PDF직접 열람.9개프라이버시 원칙 기반자율책임 제도 개요;현행한국인증 요건이나 GlobalCBPR전문아님."
    }
  ],
  "topics": [
    {
      "id": "nist-ai-rmf",
      "title": "AI 거버넌스와 NIST AI RMF 1.0",
      "domain": "AI 거버넌스·법·윤리",
      "aliases": [],
      "easy": "AI가 잘못 판단했을 때 누가 멈추고 고칠지, 어떤 증거로 안전을 판단할지를 개발 전부터 정하는 체계입니다.",
      "definition": "AI 거버넌스는 AI 생애주기의 의사결정 권한·책임·정책·감독을 정하는 운영체계입니다. NIST AI RMF1.0은 부정적 영향을 관리하고 신뢰성을 높이는 자발적 위험 관리 프레임워크로 Core와 활용 맥락에 맞춘 Profile을 제공합니다.",
      "principles": [
        "GOVERN은 경영진 책임, 위험 수용기준, 조직 정책과 자원을 정하며 나머지 기능 전체에 걸쳐 작동합니다. MAP은 사용목적·대상자·배포 환경·이해관계자·가능한 피해를 맥락화합니다.",
        "MEASURE는 유효성·보안·프라이버시·편향을 정량·정성 방법으로 평가하고 측정 한계를 기록합니다. MANAGE는 우선순위에 따라 위험을 처리하고 출시·중단·감시·사고 대응을 결정합니다. 네 기능은 일회성 직렬 체크리스트가 아닙니다.",
        "7특성은 유효하고 신뢰할 수 있음, 안전함, 보안성과 회복탄력성, 책임성과 투명성, 설명가 능성과 해석가능성, 프라이버시 강화, 유해한 편향을 관리한 공정성입니다. 특성 간 절충을 사용 맥락과 피해 규모로 판단합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "AI 거버넌스",
            "조직 책임·의사결정",
            "누가 어떤 근거로 결정하는가"
          ],
          [
            "AI RMF",
            "위험 관리 프레임워크",
            "위험의 식별·측정·처리"
          ],
          [
            "ISO42001",
            "AI 경영시스템 요구사항",
            "상세 조항·인증 범위 별도 확인"
          ]
        ]
      },
      "example": {
        "title": "채용 추천 AI의 출시 판단",
        "input": "지원자 순위를 추천하되 최종채용은 사람이 결정한 다는 가정",
        "steps": [
          "GOVERN: 인사·보안·이의제기 담당과 중단 권한을 정합니다.",
          "MAP: 대표성·차별·개인정보 이용 근거와 잘못된 탈락 피해를 기록합니다.",
          "MEASURE: 집단별 오류율·설명 충실도·정보 유출을 시험하고 표본 부족을 표시합니다.",
          "MANAGE: 제한 운영·검토·이의제기·드리프트 감시와 롤백 조건을 남깁니다."
        ],
        "result": "정확도 하나 대신 책임자·위험 목록·평가 결과·잔여위험 승인·운영 감시를 연결합니다.",
        "caution": "가상 사례이며 법정 채용요건 충족이나 NIST 인증을 뜻하지 않습니다."
      },
      "answer_outline": [
        "거버넌스 정의와 책임",
        "보안·프라이버시·사회적 위험",
        "네 기능 순환 도식",
        "7특성·절충",
        "잔여위험과 운영 감시"
      ],
      "pitfalls": [
        "AI RMF를 법령·인증 제도로 표현하지 않습니다.",
        "정확도를 공정성·안전성과 동일시하지 않습니다.",
        "사람의 최종 승인 문구만 으로 실효적 감독이 구현되지 않습니다."
      ],
      "recall": [
        "GOVERN이 모든 기능에 걸쳐 작동하는 이유는 무엇입니까?",
        "MAP과 MEASURE의 산출물을 두 가지씩 말하십시오.",
        "채용 AI의 보안 위험과 사회적 위험은 어떻게 다릅니까?"
      ],
      "source_ids": [
        "sys-airmf",
        "sys-42001"
      ],
      "validation": "출처 확인",
      "version_note": "NIST AI RMF1.0(2023-01). ISO42001은 공식 소개의 성격 비교에 한정하며 상세 요구사항 전문은 미열람.",
      "requirements": [
        {
          "question": "138-1-1",
          "items": [
            "AI RMF 개념",
            "4가 지 핵심 구조",
            "7가 지 신뢰 가능한 특성"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "137-1-6",
          "items": [
            "AI 거버넌스 개념과 운영체계"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "131-2-3",
          "items": [
            "AI 개발·적용 윤리와 거버넌스 모형"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "133-1-8",
          "items": [
            "인공지능 신뢰성의 개념",
            "핵심 속성"
          ],
          "section": "핵심원리/비교표",
          "status": "충족"
        }
      ],
      "related_terms": [
        "AI 거버넌스",
        "AI 리스크",
        "AI 신뢰성",
        "ISO/IEC42001"
      ]
    },
    {
      "id": "ipv4-subnetting-vlsm",
      "title": "IPv4 서브네팅·슈퍼네팅·VLSM 계산",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "주소를 부서 인원에 맞는 크기의 방으로 나누되, 각 방의 시작 위치를 정해진 경계에 맞춥니다.",
      "definition": "서브네팅은 프리픽스를 늘려 주소 블록을 분할하고, 슈퍼네팅은 연속되고 정렬된 블록을 짧은 공통 프리픽스로 집성합니다. VLSM은 호스트 요구에 맞춰 서로 다른 길이의 마스크를 사용합니다. 관련 개념을 계산 단원으로 묶었으며 서로의 동의어는 아닙니다.",
      "principles": [
        "IPv4 /p의 전체 주소 수는 2^(32-p)입니다. 일반 LAN의 사용 가능 수는 네트워크·브로드캐스트를 뺀 2^h-2입니다. /31 점대점·/32 예외를 일반 LAN에 적용하지 않습니다.",
        "고정 4분할은 2비트를 빌립니다. 192.168.100.0/24 → /26, 255.255.255.192, 64주소·62호스트입니다. 경계는 .0, .64, .128, .192이며 각 호스트는 .1~.62, .65~.126, .129~.190, .193~.254입니다.",
        "VLSM은 큰 요구부터 최소 2의 거듭제곱을 산정합니다. 500 → 512(/23), 250 → 256(/24), 125 → 128(/25) 두 개입니다. 512+256+128+128=1024로 /22에 정확히 들어갑니다. 인원 합에8을 더하는 방법은 블록별 반올림을 반영하지 못합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "개발500",
            "192.168.0.0/23;255.255.254.0",
            "호스트192.168.0.1~1.254;BC1.255"
          ],
          [
            "영업250",
            "192.168.2.0/24;255.255.255.0",
            "호스트192.168.2.1~2.254;BC2.255"
          ],
          [
            "인사125",
            "192.168.3.0/25;255.255.255.128",
            "호스트192.168.3.1~3.126;BC3.127"
          ],
          [
            "보안125",
            "192.168.3.128/25;255.255.255.128",
            "호스트192.168.3.129~3.254;BC3.255"
          ]
        ]
      },
      "example": {
        "title": "139-4-6 네 부서 배분",
        "input": "192.168.0.0/22;500·250·125·125호스트",
        "steps": [
          "전체는192.168.0.0~192.168.3.255, 마스크255.255.252.0입니다.",
          "개발을 /23의 세 번째 옥텟0 경계부터 배치합니다.",
          "다음 주소192.168.2.0에 영업 /24를 배치합니다.",
          "남은192.168.3.0/24를 .0/25와 .128/25로 나눕니다.",
          "각 경계·중첩 없음·510/254/126/126 수용량과 총1024주소를 검산합니다."
        ],
        "result": "네 부서 수용 가능, 주소 블록 여유0, 호스트 여유 합 16개입니다.",
        "caution": "게이트웨이·프린터·증설이 별도 라면 추가 요구를 먼저 반영합니다. 제시 순서는 유일해가 아닙니다."
      },
      "answer_outline": [
        "분할·집성 정의",
        "호스트 수 식",
        "큰 부서부터 정렬",
        "마스크·호스트·BC 표",
        "중첩·확장 검산"
      ],
      "pitfalls": [
        "/22를1024호스트라고 쓰지 않습니다.",
        "125명에 /26은 부족합니다.",
        "임의 시작 주소·브로드캐스트 할당은 오류입니다."
      ],
      "recall": [
        "/24를 네 블록으로 나눈 마스크·호스트 수는 얼마입니까?",
        "500명에 /23이 필요한 이유를 식으로 설명하십시오.",
        "연속된 두 블록 집성에도 경계 확인이 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sys-rfc4632"
      ],
      "validation": "출처 확인",
      "version_note": "RFC4632의 CIDR 원리와 일반 LAN 조건. 기출 주소배분은 Python ipaddress로 중첩·경계·수용량 직접 검산.",
      "requirements": [
        {
          "question": "130-2-3",
          "items": [
            "슈퍼네팅·서브네팅",
            "/24 동일4분할 절차",
            "마스크 및 할당 수량"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "139-4-6",
          "items": [
            "슈퍼네팅·서브네팅",
            "/22 네 부서 VLSM",
            "각 Subnet Mask 및 Host IP 대역"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ],
      "related_terms": [
        "CIDR",
        "서브네팅",
        "슈퍼네팅",
        "VLSM"
      ]
    },
    {
      "id": "process-synchronization",
      "title": "경쟁 상태와 뮤텍스·세마포어·모니터",
      "domain": "운영체제",
      "aliases": [],
      "easy": "여러 작업이 같은 값을 고칠 때 순서에 따라 결과가 달라지지 않도록 출입 순서를 정합니다.",
      "definition": "경쟁 상태는 공유 상태를 다루는 실행의 상대적 순서가 결과를 바꾸는 현상입니다. 임계 구역은 공유 불변조건을 바꾸는 코드이며 동기화는 상호배제와 실행 순서를 보장합니다.",
      "principles": [
        "뮤텍스는 소유자가 있는 배타 잠금입니다. 잠근 스레드가 해제하는 것이 원칙이며 재진입 가능 여부는 별도 속성입니다. 세마포어는 자원 개수를 원자적으로 감소·증가시키는 계수기여서 다른 실행 주체의 신호 전달에도 사용할 수 있습니다.",
        "P는 자원이 없으면 대기하고 있으면 계수를 감소시키며 V는 반환·통지를 수행합니다. 값 읽기와 감소 자체가 원자적이어야 합니다. 모니터는 공유 상태·연산·상호배제를 캡슐화하고 조건변수로 조건 충족을 기다리게 합니다.",
        "조건변수 대기는 잠금을 풀고 대기한 뒤 깨어나 잠금을 다시 얻습니다. 깨어났다는 사실은 조건이 여전히 참이라는 보장이 아니므로 while로 조건을 재검사합니다. 잠금 순서 불일치는 교착상태를 만들며 긴 임계 구역은 경합과 응답 시간을 늘립니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "뮤텍스",
            "한 소유자의 배타 접근",
            "소유자 해제;공유 자료 보호"
          ],
          [
            "세마포어",
            "N개 자원 또는 순서 신호",
            "소유자 의미가 약함;중복V 주의"
          ],
          [
            "모니터",
            "상태·연산·조건대기 결합",
            "언어·런타임의 대기 의미 확인"
          ]
        ]
      },
      "example": {
        "title": "잔액 감소의 갱신 분실",
        "input": "잔액100에서 T1은10, T2는20 인출",
        "steps": [
          "둘이100을 읽고90·80을 차례로 쓰면 최종80으로 잘못됩니다.",
          "lock → 잔액읽기 → 차감 → 쓰기 → unlock을 임계 구역으로 둡니다.",
          "T1 후T2이면 100 → 90 → 70이며 역순도70입니다.",
          "원자 감소만으로 복수 계좌 이체의 전체 불변조건까지 보장되지는 않습니다."
        ],
        "result": "필요한 공유 불변조건의 범위를 함께 잠가 최종70을 보장합니다.",
        "caution": "단일 CPU도 선점으로 경쟁이 발생합니다. 스핀락은 잠들 수 없는 문맥 등 실제 조건에 맞게 선택합니다."
      },
      "answer_outline": [
        "경쟁상태 사례",
        "임계 구역 조건",
        "세 기법 원리·표",
        "P/V 예",
        "교착·기아·경합"
      ],
      "pitfalls": [
        "volatile은 상호배제의 대체물이 아닙니다.",
        "세마포어1과 뮤텍스의 소유권 의미는 다릅니다."
      ],
      "recall": [
        "상호배제와 순서 동기화의 차이는 무엇입니까?",
        "조건변수 대기에 while이 필요한 이유는 무엇입니까?",
        "잘못된 V 호출은 어떤 문제를 만듭니까?"
      ],
      "source_ids": [
        "sys-linux-locks"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-1-3",
          "items": [
            "Race Condition"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "139-4-2",
          "items": [
            "Mutex",
            "Semaphore",
            "Monitor"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "136-4-2",
          "items": [
            "공유 자원 충돌과 동기화"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "priority-inversion",
      "title": "우선순위 역전·상속·천장",
      "domain": "운영체제",
      "aliases": [],
      "easy": "급한 작업이 덜 급한 작업의 잠금을 기다리는데, 중간 순위 작업까지 끼어들어 지연이 길어지는 문제입니다.",
      "definition": "우선순위 역전은 높은 우선순위 작업이 낮은 우선순위 작업이 점유한 자원 때문에 막히는 현상입니다. 중간 우선순위 작업이 낮은 작업을 선점하면 높은 작업의 대기 시간이 간접적으로 늘어납니다.",
      "principles": [
        "T1>T2>T3이고 이진세마포어 S=1일 때 T3가P(S)로 임계 구역에 들어갑니다. T1이 도착해P(S)에서 막히면 T3가 실행되어 V(S)해야 합니다. 이때 자원이 필요 없는 T2가 T3를 선점하면 T1까지 늦어집니다.",
        "우선순위 상속은 T1이 대기하는 동안 잠금 소유자T3에 T1의 유효 우선순위를 임시 부여합니다. 중첩된 잠금에서 는 상속이 대기 사슬로 전파될 수 있고 해제 시 남은 대기자와 원래 우선순위를 반영해 되돌립니다.",
        "우선순위 천장 방식은 자원을 이용할 작업 중 최고 우선순위에 기반한 천장과 진입 규칙을 사용합니다. 획득 즉시 올리는 방식 등 변형이 있으므로 천장의 정의·상승 시점·진입 조건을 함께 씁니다. 짧은 임계 구역과 일관된 잠금 순서도 필요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "상속",
            "실제 고우선 대기가 발생하면 상승",
            "동적 대응;PI chain 관리"
          ],
          [
            "천장",
            "자원별 최고 우선순위 기반 제한",
            "사전 이용 관계 분석 필요"
          ],
          [
            "단순 우선순위",
            "실행 가능한 최고 작업 선점",
            "잠금 의존성 자체 해결 못함"
          ]
        ]
      },
      "example": {
        "title": "세 작업의 P/V 순서",
        "input": "T1 높음, T2 중간, T3 낮음;모두 단일 CPU",
        "steps": [
          "T3:P(S) → 임계 구역 시작.",
          "T1:P(S) → 대기.",
          "T2가 실행되어 T3를 지연시키면 역전이 확대됩니다.",
          "상속 시T3를T1 수준으로 올려 임계 구역 완료 → V(S) → T1 재개.",
          "T3의 유효 우선순위는 잠금과 대기 사슬 상태에 맞게 복원합니다."
        ],
        "result": "고우선순위 작업의 간접 차단을 제한합니다. 모든 종류의 지연과 교착이 자동 제거되지는 않습니다.",
        "caution": "Linux rt_mutex의 실제 상속 구현은 확인했습니다. 천장 프로토콜의 모든 변형은 원표준 추가 확인 대상입니다."
      },
      "answer_outline": [
        "실시간 응답 문제",
        "T1/T2/T3 시간축",
        "P/V 흐름",
        "상속·천장 비교",
        "블로킹 상한"
      ],
      "pitfalls": [
        "낮은 작업이 자원을 가진 사실 자체를 모두 비정상이라 하지 않습니다.",
        "상속을 영구 우선순위 변경이라 쓰지 않습니다."
      ],
      "recall": [
        "T2가 공유 자원을 쓰지 않아도T1을 늦추는 이유는 무엇입니까?",
        "상속을 언제 복원합니까?",
        "천장에 사전 자원 이용 정보가 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sys-rtmutex",
        "sys-linux-locks"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-4-2",
          "items": [
            "T1>T2>T3 사례",
            "P, V 연산",
            "해결기법 두 가지"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "bankers-algorithm",
      "title": "은행가 알고리즘과 안전 상태",
      "domain": "운영체제",
      "aliases": [],
      "easy": "지금 자원이 남았다는 이유만으로 빌려주지 않고, 모든 고객이 끝낼 수 있는 순서가 남는지 먼저 계산합니다.",
      "definition": "은행가 알고리즘은 최대 자원 요구를 사전에 알고 요청을 가상 배정한 상태가 안전한 경우에만 허용하는 교착 회피 기법입니다. 안전 상태는 각 작업이 남은 요구를 받아 완료할 수 있는 안전 순서가 존재하는 상태입니다.",
      "principles": [
        "Allocation은 현재 보유량, Max는 최대 선언량, Need=Max-Allocation, Available은 미할당량입니다. 다중 자원 비교는 모든 성분에 대해 수행하며 자원 종류의 합계만 비교하면 안 됩니다.",
        "안전성 검사는 Work=Available로 시작하여 미완료 작업 중Need<=Work를 찾고 완료를 가정한 뒤Work+=Allocation을 반복합니다. 모두 완료되면 안전 순서가 있습니다. 요청<=Need 및 요청<=Available을 먼저 확인하고 가상 배정 후 안전성 검사를 합니다.",
        "안전하지 않은 상태는 지금 교착이라는 뜻이 아닙니다. 이후 최대 요구가 발생하면 완료를 보장할 수 없다는 뜻입니다. 최대 요구 예측이 어렵고 자원 종류·작업이 동적으로 늘어나는 환경에 서 는 보수적이거나 관리 부담이 큽니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "예방",
            "교착 필요조건 하나 제거",
            "정적 제한·자원 활용 저하 가능"
          ],
          [
            "회피",
            "안전 상태를 유지",
            "최대 요구 사전 선언 필요"
          ],
          [
            "탐지·회복",
            "교착을 찾고 종료·회수",
            "회복 비용·데이터 일관성 고려"
          ]
        ]
      },
      "example": {
        "title": "단일 자원 안전 순서 직접 검산",
        "input": "총10;A보유3/최대7, B보유2/최대4, C보유2/최대3;Available3",
        "steps": [
          "Need는A4, B2, C1입니다.",
          "Work3에서B 완료 가능:Work=3+2=5.",
          "A 완료 가능:Work=5+3=8.",
          "C 완료 가능:Work=8+2=10, 따라 서B → A → C는 안전합니다.",
          "A에3을 먼저 추가 배정하면 Available0, NeedA1/B2/C1이 어서 어느 작업도 완료할 수 없습니다. 요청을 보류합니다."
        ],
        "result": "추가 요청이 남은 자원 이하라도 안전성 검사에 서 거부될 수 있습니다.",
        "caution": "완료 가정에 서 Work에 더하는 값은 Max나Need가 아니라 현재 Allocation입니다."
      },
      "answer_outline": [
        "교착회피 정의",
        "네 자료 구조",
        "요청 검사·가상할당·안전성",
        "표 계산",
        "한계"
      ],
      "pitfalls": [
        "불안전과 교착을 동일시하지 않습니다.",
        "행·열을 바꾸거나 자원벡터를 합산 비교하지 않습니다."
      ],
      "recall": [
        "Need는 어떻게 계산합니까?",
        "Available이 충분한데 요청이 거절되는 이유는 무엇입니까?",
        "안전 순서 하나가 실제 실행 순서를 강제합니까?"
      ],
      "source_ids": [
        "sys-banker"
      ],
      "validation": "출처 확인",
      "version_note": "Dijkstra EWD108 단일 자원 원고를 근거로 한 자체 교육 예시. 수치와 순서를 직접 검산했습니다.",
      "requirements": [
        {
          "question": "138-1-11",
          "items": [
            "은행가 알고리즘 개념·동작"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "virtual-memory",
      "title": "가상 메모리·단편화·스레싱",
      "domain": "운영체제",
      "aliases": [],
      "easy": "프로그램이 보는 주소와 실제 RAM 위치를 분리하고 필요한 조각만 올리지만, 조각 교체에 매달리면 오히려 느려집니다.",
      "definition": "가상 메모리는 프로세스별 가상 주소를 물리 프레임에 매핑하여 격리·보호·공유·비연속 배치를 제공하는 메모리 추상화입니다. 페이지 부재 시 운영체제가 저장 장치 등에서 필요한 내용을 준비합니다.",
      "principles": [
        "페이징은 고정 크기 페이지와 프레임을 매핑합니다. 페이지 내부의 사용하지 않는 끝 공간은 내부단편화이며 비연속 프레임 배치로 일반적인 외부단편화를 피합니다. 페이지 테이블·TLB가 주소변환 비용을 줄입니다.",
        "세그멘테이션은 코드·데이터 등 논리 단위의 가변길이 영역과 base/limit를 사용합니다. 논리 보호·공유가 쉽지만 물리 공간의 외부단편화가 생길 수 있습니다. 결합형은 논리 세그먼트를 다시 페이지로 나눕니다.",
        "스레싱은 활동 작업집합이 가용 프레임보다 커져 잦은 페이지 부재와 교체가 유효 CPU 실행을 압도하는 상태입니다. 다중프로그래밍 정도 축소, 작업집합·부재 빈도 기반 프레임 조절, 메모리 증설과 접근 지역성 개선을 검토합니다. 큰페이지는 TLB 효율 대신 내부낭비·연속할당 부담을 늘릴 수 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "페이징",
            "고정단위;페이지 표",
            "내부단편화·표 메모리"
          ],
          [
            "세그멘테이션",
            "논리단위;base/limit",
            "외부단편화·배치문제"
          ],
          [
            "스레싱제어",
            "활성작업집합을 RAM에 맞춤",
            "CPU 낮다고 작업을 더 늘리면 악화"
          ]
        ]
      },
      "example": {
        "title": "주소변환과 내부단편화",
        "input": "페이지4KiB, 가상 주소0x12345, 해당VPN0x12 → PFN0xA0",
        "steps": [
          "하위 12비트오프셋은0x345입니다.",
          "물리 주소는 0xA0000+0x345=0xA0345입니다.",
          "크기10KiB영역에 3페이지를 배정하면 12KiB 중2KiB가 남습니다.",
          "서로 다른 많은페이지를 순환참조하면 TLB미스와부재를분리 측정합니다."
        ],
        "result": "주소변환과공간낭비를각각 계산하여 단편화와교체문제를 구분합니다.",
        "caution": "페이지 부재는항상 디스크I/O를 뜻하지 않으며zero-fill·COW도 있습니다."
      },
      "answer_outline": [
        "주소변환도식",
        "페이지·세그먼트비교",
        "단편화종류",
        "스레싱원인·제어",
        "계산예"
      ],
      "pitfalls": [
        "가상 메모리를 단순 히디스크를 RAM처럼쓰는기술로 한정하지 않습니다.",
        "모든 부재를오류라하지 않습니다."
      ],
      "recall": [
        "페이징에내부단편화가생기는이유는무엇입니까?",
        "스레싱때CPU이 용률이낮아질수 있는 이유는무엇입니까?",
        "큰페이지의 절충은 무엇입니까?"
      ],
      "source_ids": [
        "sys-linux-pagetables",
        "sys-ostep-seg",
        "sys-ostep-vm"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-1-10",
          "items": [
            "스레싱"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "131-3-5",
          "items": [
            "페이징·세그멘테이션 개념과 비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "139-4-4",
          "items": [
            "가상 메모리 관리",
            "단편화유형",
            "최소화방안"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "process-memory",
      "title": "코드·데이터·힙·스택과 메모리 오류",
      "domain": "운영체제",
      "aliases": [],
      "easy": "실행할 명령, 계속 유지할 값, 동적으로 얻은 값, 함수 호출의 임시값은 수명과 관리 방법이 다릅니다.",
      "definition": "일반적인 프로세스 주소 공간은 실행 코드·정적데이터·동적힙·호출 스택 등 논리 영역으로 설명할 수 있습니다. 실제 실행파일·메모리 매핑은 운영체제·언어·실행 환경에 따라 더 세분됩니다.",
      "principles": [
        "코드는 명령과읽기전용자료를 두며데이터는 초기화 전역·정적 변수와BSS등을 포함합니다.힙은 동적 할당객체의 수명을 관리하고 스택은 호출별인자·지역변수·복귀정보를 프레임으로 보관합니다.모든 지역변수가반드시 스택에 있는 것은아니며최적화·클로저·코루틴의예외가 있습니다.",
        "C의malloc은 영역을 할당하고 free는 반환합니다.참조를 잃어반환하지못하면 누수, 반환뒤접근하면 use-after-free, 중복반환은double-free입니다.Java/Python도 불필요한 객체를 컬렉션·캐시·리스너가계속참조하면 GC가 회수하지못합니다.",
        "세그멘테이션오류는 허용되지않은메모리 접근에 대한보호위반으로NULL·경계초과·해제후접근등이 원인일수 있습니다.메모리 누수는사용량추세·힙덤프·보유 참조 분석으로, 보호위반은덤프·스택추적·메모리 검사기로원인을 좁힙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "코드·데이터",
            "프로그램·정적수명",
            "권한과 초기화 구분"
          ],
          [
            "힙",
            "객체별동적수명",
            "누수·해제후사용"
          ],
          [
            "스택",
            "호출 프레임 수명",
            "깊은재귀·범위탈출참조"
          ]
        ]
      },
      "example": {
        "title": "요청마다 쌓이는 캐시",
        "input": "요청 1회마다1MiB객체를 전역리스트에추가;1000회",
        "steps": [
          "요청이 끝나도전역리스트가객체를 참조합니다.",
          "대략1000MiB+객체 관리 비용이 남아압력이증가합니다.",
          "힙덤프의지배객체·참조 경로로 리스트를확인합니다.",
          "필요한 보관기간·항목한도를정하고 수명 종료시에참조를 제거합니다."
        ],
        "result": "GC 호출만 반복하는 대신 도달가능한 불필요 객체의 보유 원인을 수정합니다.",
        "caution": "논리 영역 그림은개념 모델이며 힙·스택의 성장방향을모든 플랫폼의 법칙으로쓰지않습니다."
      },
      "answer_outline": [
        "네영역역할·수명",
        "호출·할당 흐름",
        "누수·보호위반 구분",
        "언어별진단",
        "재발방지"
      ],
      "pitfalls": [
        "GC가 있으면 누수가불가능하다고쓰지않습니다.",
        "SIGSEGV를 항상 물리 메모리부족으로해석하지 않습니다."
      ],
      "recall": [
        "힙 객체가 GC대상에 서 제외되는이유는무엇입니까?",
        "스택지역값의 참조를 반환하면 왜위험합니까?",
        "누수와해제후사용의차이는무엇입니까?"
      ],
      "source_ids": [
        "sys-malloc",
        "sys-ostep-seg"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "138-2-6",
          "items": [
            "Code",
            "Data",
            "Heap",
            "Stack",
            "영역 간 동작"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-3-6",
          "items": [
            "동적 할당필요",
            "누수문제",
            "Java·Python 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-1-7",
          "items": [
            "Segmentation Fault"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "interprocess-communication",
      "title": "IPC와 공유 메모리 동기화",
      "domain": "운영체제",
      "aliases": [],
      "easy": "서로 분리된 프로세스가 메시지를 보내거나 공동 공간을 열어 협력하되, 공동 공간의 갱신 순서를 따로 지킵니다.",
      "definition": "IPC는 프로세스 사이에 데이터·이벤트·상태를 교환하는 운영체제의 통신 메커니즘입니다. 프로세스 격리를 유지하면 서 협력·병렬처리·서비스 분리를 가능하게 합니다.",
      "principles": [
        "파이프는바이트흐름을 전달하며 익명파이프는주로관계있는 프로세스사이에서, 이름있는 FIFO는 경로를 통해 접속합니다.메시지큐는메시지 경계를 유지하고 우선순위·비동기교환에유리하지만복사와큐용량 관리가 필요합니다.",
        "공유 메모리는 여러 프로세스 주소 공간에동일한 영역을 매핑하여 대용량복사를줄입니다.POSIX에서는shm_open → ftruncate → mmap후사용하고 수명에 맞춰해제합니다.데이터가 공유된다는사실이원자성·가시성·순서보장을자동제공하지 않으므로세마포어·프로세스공유뮤텍스등을 결합합니다.",
        "소켓은로컬UNIX도 메인또는네트워크를 통한통신을 제공합니다.시그널은이벤트통지에적합하며 복잡한데이터 전달에 는 제약이있습니다.기법 선택은 전달량·지연·메시지 경계·생산자/소비자관계·권한·오류 복구로 판단합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "파이프·큐",
            "커널이전달·버퍼관리",
            "프레이밍·역압·용량"
          ],
          [
            "공유 메모리",
            "같은 페이지매핑",
            "별도 동기화·수명 관리"
          ],
          [
            "소켓",
            "로컬·원격종단점",
            "직렬화·접속·부분전송"
          ]
        ]
      },
      "example": {
        "title": "유한 버퍼 생산자·소비자",
        "input": "N=4칸;empty4, full0, mutex1",
        "steps": [
          "생산자는P(empty) → P(mutex) → 쓰기 → V(mutex) → V(full)입니다.",
          "소비자는P(full) → P(mutex) → 읽기 → V(mutex) → V(empty)입니다.",
          "버퍼가비면소비자는full에서대기하고 가득차면생산자는empty에서대기합니다.",
          "mutex를 잡은채empty를 기다리면상대의반환작업을 막을수 있어잠금 순서를 검토합니다."
        ],
        "result": "상호배제와빈칸·데이터존재순서를 분리하여 오버런·언더런을방지합니다.",
        "caution": "개념적의사코드이며 취소·프로세스죽음·복구 정책은 운영 요구에 맞춰보완합니다."
      },
      "answer_outline": [
        "IPC필요성",
        "기법별구조",
        "통신과 동기화분리",
        "P/V버퍼예",
        "성능·복구판단"
      ],
      "pitfalls": [
        "공유 메모리는 네트워크공유파일과같은 개념이 아닙니다.",
        "메시지큐가애플리케이션트랜잭션을자동보장하지 않습니다."
      ],
      "recall": [
        "공유 메모리에도 잠금이 필요한 이유는무엇입니까?",
        "파이프와메시지큐의경계차이는무엇입니까?",
        "역압이없으면 어떤문제가 생깁니까?"
      ],
      "source_ids": [
        "sys-shm",
        "sys-linux-locks"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "136-4-2",
          "items": [
            "IPC 개념과 목적",
            "주요 기법3가 지",
            "동기화기법"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "zombie-process",
      "title": "좀비 프로세스와 자식 회수",
      "domain": "운영체제",
      "aliases": [],
      "easy": "실행은 끝났지만 부모가 종료 결과를 가져가지 않아 작은 종료 기록이 남아 있는 상태입니다.",
      "definition": "좀비 프로세스는 종료했으나 부모가 wait 계열 호출로 종료 상태를 회수하지 않아 프로세스 테이블의 상태 정보가 남은 프로세스입니다. 계속 실행하는 프로세스나 부모를 잃은 고아 프로세스와 구분합니다.",
      "principles": [
        "자식 종료시주소 공간등대부분의자원은 해제되지만PID·종료 상태·사용자원 통계등을 부모가 확인할때까지보존합니다.wait/waitpid/waitid는 자식의 상태변화를기다리고종료 결과를 회수할 수 있게합니다.",
        "부모는 다수자식이 동시에종료할 수 있으므로SIGCHLD를 받았다는사실만세지않고WNOHANG을 이용한반복회수등설계에 맞는방법을 사용합니다.명시적인SIGCHLD무시·SA_NOCLDWAIT동작은 운영체제규칙을 확인합니다.",
        "좀비자체는이미종료했으므로kill로실행을 중단시킬대상이 아닙니다.회수하지 않는부모의 버그를고치거나적절한 재시작으로 관리 주체가 회수하게합니다.컨테이너에서도PID1역할을하는프로세스의 자식 회수 기능을 확인해야합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "좀비",
            "자식 종료·결과미회수",
            "프로세스슬롯·PID고갈가능"
          ],
          [
            "고아",
            "부모가 먼저 종료",
            "다른 관리 주체에 재부모화"
          ],
          [
            "실행·대기",
            "아직작업이 끝나지않음",
            "CPU·I/O·잠금 상태 분석"
          ]
        ]
      },
      "example": {
        "title": "배치 서버의 종료 누락",
        "input": "부모가 매초자식 10개생성;모두즉시종료;wait없음",
        "steps": [
          "ps의상태Z와 부모PID를 확인합니다.",
          "60초면최대 600개의미 회수 종료 기록이 쌓일수 있습니다.",
          "부모의 상태 회수루프를추가 하고 이미대기가능한 모든 자식을 회수합니다.",
          "반복부하후Z상태개수가증가하지 않고종료 코드 처리가 유지되는지확인합니다."
        ],
        "result": "CPU사용량보다 미회수 자식수의증가를 증거로 원인을 판단합니다.",
        "caution": "부모 강제 종료는 다른 업무를 중단할 수 있으므로프로그램 수정과 정상관리 절차를 우선합니다."
      },
      "answer_outline": [
        "정의·상태전이",
        "남는정보",
        "wait와SIGCHLD",
        "고아비교",
        "컨테이너회수"
      ],
      "pitfalls": [
        "좀비를죽지않는실행 프로세스라하지 않습니다.",
        "메모리전체가계속점유된다고설명하지 않습니다."
      ],
      "recall": [
        "좀비와고아는 어떻게다릅니까?",
        "wait호출이 회수하는정보는 무엇입니까?",
        "SIGCHLD 1회에종료 자식 1개만회수하면 왜부족합니까?"
      ],
      "source_ids": [
        "sys-linux-wait"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "140-1-8",
          "items": [
            "좀비프로세스"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "cpu-disk-scheduling",
      "title": "CPU·디스크 스케줄링과 SJF·SRT·SSTF·SLTF",
      "domain": "운영체제",
      "aliases": [],
      "easy": "CPU에 서 는 짧은 일을 먼저 할지, 디스크에서 는 헤드 이동과 회전을 얼마나 줄일지 목적에 맞게 순서를 정합니다.",
      "definition": "CPU 스케줄링은 실행 가능한 작업에 CPU를 배분하는 정책이고 디스크 스케줄링은 대기 중인 I/O 요청의 서비스 순서를 정하는 정책입니다. 대기·반환·응답 시간·처리량·공정성의 절충이 다릅니다.",
      "principles": [
        "SJF는 준비된작업중예측실행 시간이 가장짧은것을비선점실행합니다.SRT또는STCF는 남은시간이 가장짧은작업을 고르며더짧은작업 도착시선점합니다.미래CPU버스트의정확한예측이어렵고긴작업의 기아를완화해야합니다.",
        "HDD의SSTF는 현재 헤드위치에서탐색거리가짧은요청을 선택하고 SLTF는 회전대기 시간이 짧은요청을 선택합니다.최단탐색이최단접근 시간전체를항상 뜻하지 않으며탐색·회전·전송 비용을 구분합니다.",
        "CPU대기 시간=반환 시간-실행 시간, 반환 시간=완료-도착입니다.SSD/NVMe에는기계적헤드·회전이없으므로HDD정책을 동일하게적용하지 않습니다.Linux의실제 정책도 SJF와 구분하며 CFS·EEVDF같은 공정성 정책은 별개입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "SJF",
            "짧은버스트;비선점",
            "예측필요·긴작업기아"
          ],
          [
            "SRT",
            "짧은잔여시간;선점",
            "응답개선·전환비용"
          ],
          [
            "SSTF/SLTF",
            "탐색/회전최소화",
            "HDD특성과 기아고려"
          ]
        ]
      },
      "example": {
        "title": "선점에 따른 대기 시간 차이",
        "input": "A도 착0/실행8, B도 착1/실행4, C도 착2/실행2;전환비용0",
        "steps": [
          "SJF는A0~8, C8~10, B10~14입니다.",
          "대기는A0, B9, C6으로평균5입니다.",
          "SRT는A0~1, B1~2, C2~4, B4~7, A7~14입니다.",
          "대기는A6, B2, C0으로평균8/3입니다."
        ],
        "result": "같은 작업도 선점허용과도착 시간에 따라 결과가 달라집니다.",
        "caution": "최적성주장은도착 조건·실행 시간기지·전환비용 가정에 의존합니다."
      },
      "answer_outline": [
        "대상과 목표",
        "SJF/SRT시간축",
        "SSTF/SLTF비교",
        "대기·반환계산",
        "기아·장치별한계"
      ],
      "pitfalls": [
        "SJF가 모든 현실조건에 서 최선이라쓰지않습니다.",
        "SSTF와SLTF를 같은 용어로 쓰지않습니다."
      ],
      "recall": [
        "SRT는 어떤때선점합니까?",
        "응답 시간과 반환 시간은 어떻게다릅니까?",
        "SSD에HDD회전스케줄링을그대로적용할 수 있습니까?"
      ],
      "source_ids": [
        "sys-ostep-sched",
        "sys-ostep-disk",
        "sys-cfs"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "137-3-1",
          "items": [
            "CPU·디스크스케줄링",
            "SJF와SRT",
            "SSTF와SLTF"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "memory-layout-bandwidth",
      "title": "엔디언·메모리 인터리빙·캐시 일관성",
      "domain": "컴퓨터구조",
      "aliases": [],
      "easy": "바이트를 어떤 순서로 놓을지, 연속 접근을 여러 메모리에 어떻게 나눌지, 복제된 캐시 값의 충돌을 어떻게 막을지 구분합니다.",
      "definition": "엔디언은 다중바이트 값의 바이트 배치 순서이고 메모리 인터리빙은 주소를 여러 뱅크·채널에 분산하여 병렬성을 높이는 배치 기법입니다. 캐시는 자주 쓰는 데이터를 가까운 계층에 복제하며 여러 코어의 사본에 는 일관성이 필요합니다.",
      "principles": [
        "빅엔디언은최상위바이트를낮은 주소에, 리틀엔디언은최하위바이트를낮은 주소에 둡니다.값자체나비트의중요도가바뀌는것은아닙니다.통신·파일형식은명시한 바이트순서로 직렬화하고 호스트와변환합니다.",
        "하위주소비트로뱅크를고르는저위인터리빙은연속주소를 다른 뱅크로보내병렬·파이프라인 접근을 돕습니다.같은 뱅크로몰리는stride접근은 충돌할 수 있습니다.캐시선·채널·NUMA의배치와한계는 장치구성에따릅니다.",
        "write-through는 하위계층에 함께 반영하고 write-back은dirty상태로 두었다가축출등의 시점에 반영합니다.멀티코어에 서 동일캐시선의사본이 낡으면일관성문제가 생겨snooping·directory와MESI계열상태 프로토콜로 소유권·무효화를관리합니다.일관성과메모리일관성모델은 동일개념이 아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "엔디언",
            "값의 바이트순서",
            "포맷명세와변환"
          ],
          [
            "인터리빙",
            "주소의 뱅크분산",
            "대역폭 증가·뱅크충돌"
          ],
          [
            "캐시 일관성",
            "여러 사본의 쓰기전파",
            "false sharing·프로토콜 비용"
          ]
        ]
      },
      "example": {
        "title": "바이트와 뱅크 배치",
        "input": "32비트0x12345678;주소100~103;4뱅크",
        "steps": [
          "빅엔디언은12, 34, 56, 78;리틀엔디언은78, 56, 34, 12입니다.",
          "워드주소mod4로뱅크를고르면0, 1, 2, 3은 서로 다른 뱅크입니다.",
          "0, 4, 8, 12는 모두뱅크0이 므로 연속접근과 같은 병렬성을 기대할 수 없습니다.",
          "두코어가 같은 캐시선의서로 다른 변수를수정하면 false sharing이 가능합니다."
        ],
        "result": "순서·배치·사본 관리라는서로 다른 문제를 구체예로구분합니다.",
        "caution": "엔디언·인터리빙·MESI상세의직접 명세는추가 확인이 필요하며 DMA공식 문서로 주소·일관성기본 범위만 검증했습니다."
      },
      "answer_outline": [
        "계층 구조",
        "엔디언예",
        "인터리빙계산",
        "쓰기 정책·일관성",
        "성능 절충"
      ],
      "pitfalls": [
        "write-through가 동시성 잠금을 대체하지 않습니다.",
        "엔디언을주소 증가방향과혼동하지 않습니다."
      ],
      "recall": [
        "0x12345678의리틀엔디언첫바이트는무엇입니까?",
        "뱅크충돌은 어떤stride에서생깁니까?",
        "캐시 일관성과프로그램 동기화는어떻게다릅니까?"
      ],
      "source_ids": [
        "sys-linux-dma"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-1-11",
          "items": [
            "Big Endian·Little Endian"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "128-1-11",
          "items": [
            "메모리인터리빙"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "137-2-1",
          "items": [
            "캐시 쓰기 정책",
            "일관성문제 원인과 해결"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "ai-accelerator-memory",
      "title": "AI 가속기·HBM·CXL·뉴로모픽 칩",
      "domain": "컴퓨터구조",
      "aliases": [],
      "easy": "AI 속도는 계산기 수뿐 아니라 데이터가 계산기까지 오는 길과, 잘 맞는 연산 형태에 달려 있습니다.",
      "definition": "GPU는 대규모 병렬 연산을 수행하는 프로세서이고 TPU는 Google이 행렬 중심 ML 워크로드를 위해 설계한 ASIC입니다. HBM은 패키지 가까이에 높은 대역폭의 적층 메모리를 두고, CXL은 CPU와 연결 장치 사이의 일관성 있는 메모리 접근을 지원합니다.",
      "principles": [
        "GPU의 SIMT·행렬가속기는범용병렬생태계와 다양한연산에 유리합니다.TPU는 행렬연산용구조와 XLA컴파일을활용하며 형상·연산 지원·배치크기·입출력 병목에 따라 효율이달라집니다.TPU가 항상 GPU보다 빠르거나저렴하다는일반 화는부적절합니다.",
        "HBM은 넓은인터페이스와적층연결로 대역폭을 높여가중치·활성값이 동병목을 줄입니다.CXL은 PCIe물리기반 연결에 서 cache·memory프로토콜로 확장·공유를돕지만장치유형·버전·지연·RAS·격리를검토해야합니다.HBM 대체와 원격메모리를 동일시하지 않습니다.",
        "뉴로모픽칩은SNN의 희소한스파이크 이벤트를 활용하고 메모리와 연산을 가깝게결합합니다.시간 정보·저전력엣지작업에 잠재력이있지만학습 방법·정확도·도구·워크로드적합성이과제입니다.반도체가치사슬은설계/IP → 제조 → 패키징·시험 → 시스템으로 구분합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "GPU",
            "병렬·행렬연산과 넓은생태계",
            "다양한모델·메모리 병목"
          ],
          [
            "TPU",
            "ML특화ASIC·XLA",
            "지원 연산·배치·입출력 검토"
          ],
          [
            "HBM/CXL",
            "근접 대역폭/일관성연결",
            "용량·비용·지연 절충"
          ],
          [
            "뉴로모픽",
            "이벤트 기반 SNN",
            "실측전력·품질동시평가"
          ]
        ]
      },
      "example": {
        "title": "가속기 선정 실험",
        "input": "같은 모델과 목표 정확도;학습/추론을 분리",
        "steps": [
          "지원 연산·정밀도·모델 메모리와 배치크기를고정합니다.",
          "GPU와 TPU의 처리량·p95지연·총비용·전력을 동일 조건으로 측정합니다.",
          "계산이 아닌데이터로 딩·AllReduce·메모리 대역폭이 병목인지프로파일링합니다.",
          "필요시HBM 용량·네트워크·CXL확장의효과를 따로평가합니다."
        ],
        "result": "명목TOPS대신 요구 품질을 만족하는시스템전체 효율로선택합니다.",
        "caution": "제품수치와버전은 변동합니다.비메모리 산업성장정책의 현행수치·정부전략은이토픽에서미확인입니다."
      },
      "answer_outline": [
        "연산·메모리 병목",
        "GPU/TPU비교",
        "HBM/CXL 구조",
        "뉴로모픽특성",
        "측정 기반선정"
      ],
      "pitfalls": [
        "HBM을 CPU 캐시라고쓰지않습니다.",
        "CXL 연결이 로컬DRAM과 같은 지연이라 고보장하지 않습니다."
      ],
      "recall": [
        "행렬특화가유리하지 않은작업은 무엇입니까?",
        "HBM과 CXL이 해결하는문제는 어떻게다릅니까?",
        "뉴로모픽의희소이벤트가 전력과 어떻게연결됩니까?"
      ],
      "source_ids": [
        "sys-tpu",
        "sys-neuromorphic",
        "sys-cxl"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "128-1-9",
          "items": [
            "뉴로모픽칩"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "134-1-12",
          "items": [
            "HBM"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-1-8",
          "items": [
            "CXL"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-2-3",
          "items": [
            "GPU·TPU 개념·비교",
            "TPU사용이유·효율·전망"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "129-4-3",
          "items": [
            "메모리·비메모리비교",
            "반도체가치사슬",
            "성장전략"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "127-2-4",
          "items": [
            "온디바이스 AI 하드웨어 기술 배경",
            "가속기·메모리 제약"
          ],
          "section": "핵심원리/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "intermittent-computing",
      "title": "인터미턴트 컴퓨팅",
      "domain": "컴퓨터구조",
      "aliases": [],
      "easy": "전원이 자주 끊기는 초저전력 장치가 다음에 켜질 때 이전 일을 안전하게 이어 가도록 설계합니다.",
      "definition": "인터미턴트 컴퓨팅은 에너지 하베스팅 등으로 전원이 불안정한 장치에 서 실행 상태를 비휘발성 저장소에 보존하거나 작업을 재구성하여 반복 정전에도 계산 진척과 데이터 일관성을 확보하는 기법입니다.",
      "principles": [
        "전압이임계값으로 내리면레지스터·스택등상태를 체크포인트로보존하고 재기동후복구하는방식과, 작업을 원자적인작은 태스크로 나누어완료된진척만커밋하는방식이 있습니다.저장 시점·에너지여유·복구 비용이 설계 핵심입니다.",
        "전원이 쓰기중끊기면체크포인트자체가불완전할 수 있어이중버퍼·버전 번호·커밋마커등의 일관된기록 절차가 필요합니다.재실행되는코드는 멱등성을 검토하며 센서 읽기·패킷송신같은 외부 효과는 메모리롤백만으로취소되지않습니다.",
        "기존 배터리장치와 달리정전을예외가 아닌정상 조건으로 다룹니다.작업크기가한번에확보할 수 있는 에너지보다크면영구재시작에 빠질수 있습니다.비휘발성메모리의 쓰기내구성·원자성·지연·보안상태 보호를 함께 고려합니다.",
        "체크포인트 저장에 쓰는 에너지 자체가 남은 에너지보다 작아야 하므로 임계전압에는 저장 비용과 최소 동작전압의 여유를 반영합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "체크포인트",
            "실행 상태 저장·복원",
            "저장 비용과 일관성"
          ],
          [
            "태스크 기반",
            "완료단위만 커밋",
            "태스크분해와외부 효과"
          ],
          [
            "상시전원",
            "연속실행 가정",
            "정전복구의 전제가 다름"
          ]
        ]
      },
      "example": {
        "title": "중복 송신을 피하는 센서",
        "input": "태양광센서가 측정후서버에 값 전송;응답전정전",
        "steps": [
          "측정 값과 고유번호를 안전하게기록합니다.",
          "서버는 번호로 중복 요청을 식별하여 같은 측정의 중복 반영을 막습니다.",
          "장치는 응답 확인후전송완료상태를 커밋합니다.",
          "정전위치별재시작을 가정해미송신·재송신·부분기록을 점검합니다."
        ],
        "result": "단순 PC복원에 더해외부세계와의진척일관성을다룹니다.",
        "caution": "원학회의 색인 본문으로 에너지 인지 체크포인트 원리를 확인했습니다. 태스크 방식·외부 효과의 정합성은 별도 원논문 추가 확인이 필요합니다."
      },
      "answer_outline": [
        "전원 모델",
        "체크포인트·태스크 원리",
        "일관성문제",
        "센서예",
        "전력·내구성한계"
      ],
      "pitfalls": [
        "정전때마다모든 상태를 저장할에너지가있다고가정하지 않습니다.",
        "재실행을 무조건 안전하다고보지않습니다."
      ],
      "recall": [
        "멱등성이 필요한 이유는무엇입니까?",
        "체크포인트도원자성이필요한 이유는무엇입니까?",
        "태스크크기와에너지의관계는 무엇입니까?"
      ],
      "source_ids": [
        "sys-mementos"
      ],
      "validation": "부분 확인",
      "version_note": "USENIX HotPower2008 원논문의 공식 색인 본문에서 에너지 인지 체크포인트를 확인했으나 원문 전체 직접 열람은 접근 실패했습니다. 일반 메모리 문서를 해당 주제의 근거로 대체하지 않았습니다.",
      "requirements": [
        {
          "question": "134-1-9",
          "items": [
            "인터미턴트컴퓨팅"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "qubit-quantum-hardware",
      "title": "큐비트와 양자컴퓨팅 하드웨어",
      "domain": "컴퓨터구조",
      "aliases": [],
      "easy": "큐비트는 0과1의 확률만 저장하는 동전이 아니라 위상과 간섭을 가진 양자 상태로 연산합니다.",
      "definition": "이상적인 단일 큐비트는 |ψ>=α|0>+β|1>, |α|²+|β|²=1로 표현합니다. 계산 기저 측정의 0·1확률은 각 진폭의 절댓값 제곱이며 측정 전 상태의 상대위상이 이후 간섭과 결과에 영향을 줍니다.",
      "principles": [
        "중첩은 두고전값을 읽어낼수 있다는뜻이아닙니다.얽힘은 다중큐비트의상태를 각부분상태의 곱으로분리할 수 없는 관계이며 초광속통신을 허용하지 않습니다.게이트는 가역적인유니터리변환으로진폭·위상을 바꿉니다.",
        "초전도·이온트랩·중성원자·광자등서로 다른 물리 구현이 있으며게이트속도·결맞음시간·연결성·제어·확장성이절충됩니다.외부잡음과디코히런스때문에물리큐비트수와논리큐비트수를구분하고 오류 정정의큰오버헤드를 고려합니다.",
        "양자우위는특정 문제·비교기준·입출력 비용에 관한주장입니다.임의의2^n개답을한번에읽는일반 병렬컴퓨터로설명하면 안됩니다.QML도 양자상태준비·데이터인코딩·샷비용·고전기준선까지 포함해효용을 검증해야합니다.",
        "정규화는 측정 확률의 합이 1이 되게 하는 조건이며 전역위상과 상대위상의 차이를 구분해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "고전비트",
            "측정가 능한0또는1",
            "복제·논리연산"
          ],
          [
            "물리큐비트",
            "잡음있는 양자상태",
            "제어·측정오차"
          ],
          [
            "논리큐비트",
            "다수물리큐비트로보호",
            "오류 정정오버헤드"
          ]
        ]
      },
      "example": {
        "title": "위상이 측정 뒤에 미치는 영향",
        "input": "초기|0>, H게이트를 두번적용",
        "steps": [
          "첫H후(",
          "0>+",
          "1>)/√2로0·1확률은 각1/2입니다.",
          "다시H를 적용하면 간섭으로",
          "0>이됩니다.",
          "중간에측정하여 고전혼합상태로 만든뒤H를 적용하는것은같은 실험이아닙니다.",
          "샷수에따른표본오차와장치잡음을구분합니다."
        ],
        "result": "중첩·간섭·측정의 역할을분리하여 설명할 수 있습니다.",
        "caution": "IBM 공식 강의의 상태·연산 개요를 확인했습니다. 물리 구현·오류 정정 자원·QML 성능 주장은 추가 원문 확인이 필요합니다."
      },
      "answer_outline": [
        "정규화된상태식",
        "측정·간섭",
        "물리 구현비교",
        "오류 정정",
        "QML한계"
      ],
      "pitfalls": [
        "큐비트수를고전메모리 용량과 직접 등치하지 않습니다.",
        "양자암호와 양자컴퓨터를동일기술로 쓰지않습니다."
      ],
      "recall": [
        "위상이 확률에 어떤경로로 영향을 줍니까?",
        "물리·논리큐비트의차이는무엇입니까?",
        "상태준비비용을 무시하면 어떤과장이생깁니까?"
      ],
      "source_ids": [
        "sys-qubit",
        "sys-pqc"
      ],
      "validation": "부분 확인",
      "version_note": "IBM 공식 강의 소개에서 복소 상태벡터·측정·유니터리 연산을 확인했습니다. 물리 구현·오류 정정·QML 성능의 상세 원문은 미열람입니다. 기초 행렬 예는 직접 검산했습니다.",
      "requirements": [
        {
          "question": "128-1-13",
          "items": [
            "큐비트"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "139-1-12",
          "items": [
            "양자머신러닝의하드웨어배경"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "tcp-control",
      "title": "TCP 연결·종료·흐름제어·혼잡제어",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "상대 수신기가 감당할 양과 중간 네트워크가 감당할 양을 따로 관리하면 서 손실된 바이트를 복구합니다.",
      "definition": "TCP는 바이트 스트림에 순서·재전송·중복 제거를 제공하는 연결지향 전송 프로토콜입니다. 수신 측 버퍼 보호인 흐름제어와 경로 과부하 완화인 혼잡제어는 목적과 윈도우가 다릅니다.",
      "principles": [
        "연결은 SYN → SYN+ACK → ACK로 양측 초기 순서 번호를 확인합니다. SYN·FIN은 순서 번호 공간을 하나 사용하지만 데이터 없는 ACK는 소비하지 않습니다. 각 방향 종료가 독립적이어서 FIN/ACK가 보통 네 교환으로 설명되지만 병합도 가능합니다.",
        "송신 가능량은 cwnd와 수신 통지 rwnd 중 작은 값에 제한됩니다. 슬라이딩 윈도우는 확인된 바이트만큼 시작점을 옮겨 여러 미확인 데이터를 파이프라인으로 보냅니다. ACK는 전송량과 손실 복구를 진행시키는 신호입니다.",
        "RFC5681의 slow start는 ACK에 따라 창을 빠르게 늘리고 ssthresh를 넘으면 대체로 RTT당 약1MSS씩 증가시킵니다. 중복ACK와 재전송 타이머로 손실을 감지하며 fast retransmit/recovery 및 timeout 대응은 다릅니다. CUBIC·ECN 등 현행 변형을 구분합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "흐름제어",
            "rwnd;수신 버퍼 보호",
            "수신기 상태가 기준"
          ],
          [
            "혼잡제어",
            "cwnd;경로 과부하 완화",
            "손실·지연·ECN 등 신호"
          ],
          [
            "오류제어",
            "ACK·재전송·순서 번호",
            "신뢰성과 중복 제거"
          ]
        ]
      },
      "example": {
        "title": "창과 재전송 타이머",
        "input": "cwnd12MSS, rwnd8MSS, 미확인5MSS;전통적RFC5681 가정",
        "steps": [
          "새 송신 여유는 min(12, 8)-5=3MSS입니다.",
          "timeout 전 FlightSize8MSS이면 ssthresh는 최대 max(8/2, 2)=4MSS입니다.",
          "timeout 후 cwnd는1MSS로 줄여 slow start로 복구합니다.",
          "3중복ACK 경로와 timeout 경로를 같은 창 변화로 그리지 않습니다."
        ],
        "result": "수신 버퍼·혼잡·손실의 제약을 분리하여 계산합니다.",
        "caution": "이 예는 명시한 고전 정책이며 모든 TCP 구현의 초기창·혼잡반응을 보장하지 않습니다."
      },
      "answer_outline": [
        "연결·종료 시간축",
        "순서 번호·ACK",
        "rwnd/cwnd 비교",
        "4혼잡 알고리즘",
        "창 계산"
      ],
      "pitfalls": [
        "TCP가 메시지 경계를 보존한다고 쓰지 않습니다.",
        "FIN은 즉시 양방향 전체 종료를 뜻하지 않습니다."
      ],
      "recall": [
        "흐름제어와 혼잡제어의 보호 대상은 무엇입니까?",
        "SYN의 ACK값이 1증가하는 이유는 무엇입니까?",
        "timeout과 중복ACK복구를 구분해야 하는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sys-rfc9293",
        "sys-rfc5681"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "130-3-3",
          "items": [
            "혼잡제어 구성·감지·제어·윈도우"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "133-1-13",
          "items": [
            "3-way·4-way handshake"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "137-3-5",
          "items": [
            "오류·혼잡제어",
            "슬라이딩윈도우",
            "설계고려사항"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "socket-sctp-websocket",
      "title": "소켓·WebSocket·SCTP",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "소켓은 통신을 여는 프로그래밍 창구이고, 그 창구에서TCP·UDP·SCTP같은 전송 방식을 선택합니다.",
      "definition": "소켓은 주소·포트 등 종단점을 통해 송수신하는 운영체제 인터페이스입니다. WebSocket은 HTTP 기반 오프닝 이후 TCP 위에서 메시지 프레임을 교환하는 응용 프로토콜이며 SCTP는 메시지 기반의 신뢰성 있는 전송 프로토콜입니다.",
      "principles": [
        "TCP 서버는 socket → bind → listen → accept 후 연결된 소켓으로 송수신하고 클라이언트는 socket → connect를 수행합니다. 스트림의 read/write 한 번이 애플리케이션 메시지 하나와 일치하지 않으므로 길이·구분자 등 프레이밍이 필요합니다.",
        "UDP는 연결 설정 없이 데이터그램을 교환하며 응용이 손실·순서·혼잡·MTU를 고려해야 합니다. HTTP는 요청·응답 의미를 제공하는 응용 프로토콜이 므로 소켓과 배타적 대안이 아닙니다. WebSocket도 인증·권한·Origin검증과 TLS가 필요합니다.",
        "SCTP는 association을 만들고 공통헤더와 chunk를 사용합니다. INIT → INIT ACK → COOKIE ECHO → COOKIE ACK의 쿠키 방식, 스트림별 순서화, TSN·SACK, 멀티호밍을 제공합니다. 멀티스트리밍이 모든 종류의 HOL지연을 없애거나 멀티호밍이 자동 대역 합산을 뜻하지는 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "TCP socket",
            "신뢰성 바이트 스트림",
            "응용 프레이밍 필요"
          ],
          [
            "WebSocket",
            "양방향 메시지 프레임",
            "브라우저·웹 연계"
          ],
          [
            "SCTP",
            "멀티스트림 메시지·멀티호밍",
            "지원망·방화벽·구현 검토"
          ]
        ]
      },
      "example": {
        "title": "실시간 대시보드",
        "input": "서버가 초당 상태 변경을 브라우저로 전달",
        "steps": [
          "처음 HTTP 오프닝에서 사용자와 Origin을 확인합니다.",
          "WebSocket 세션에 서 구독 권한을 검증하고 메시지 크기를 제한합니다.",
          "연결이 끊기면 마지막 이벤트 번호를 기준으로 재동기화합니다.",
          "일반 조회HTTP와 푸시WebSocket의 역할을 나누어 상태를 관리합니다."
        ],
        "result": "소켓API·전송 계층·응용 프로토콜을 계층별로 설명합니다.",
        "caution": "WebSocket 연결이 살아 있어도 업무 이벤트의 exactly-once 처리는 별도 설계입니다."
      },
      "answer_outline": [
        "계층과 정의",
        "소켓 호출 흐름",
        "TCP·UDP·WebSocket 비교",
        "SCTP 구조·쿠키",
        "보안·복구"
      ],
      "pitfalls": [
        "HTTP를 소켓을 사용하지 않는 통신이라 고 설명하지 않습니다.",
        "SCTP의 association과TCP 연결을 완전히 같은 기능으로 쓰지 않습니다."
      ],
      "recall": [
        "TCP수신에서 프레이밍이 필요한 이유는 무엇입니까?",
        "SCTP의 stream과TSN은 어떤 역할입니까?",
        "WebSocket의 인증은 연결 이후 에도 왜 필요합니까?"
      ],
      "source_ids": [
        "sys-rfc9260",
        "sys-websocket",
        "sys-rfc9293"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "131-2-5",
          "items": [
            "소켓 정의·유형",
            "TCP소켓·WebSocket 흐름",
            "HTTP 비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "132-3-4",
          "items": [
            "SCTP 개요·특징",
            "구조·동작"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "error-control-arq",
      "title": "오류 검출·정정과 Stop-and-Wait·Go-Back-N",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "잘못 온 것을 알아내는 것과 원래 값을 복원하는 것은 다르며, 복원 대신 다시 보내 달라고 할 수도 있습니다.",
      "definition": "오류 검출은 중복 정보를 통해 수신 데이터의 손상을 찾아내는 기능이고 오류 정정은 재전송 없이 일정 범위의 오류를 복원하는 기능입니다. ARQ는 검출·순서 번호·ACK·타이머와 재전송을 결합합니다.",
      "principles": [
        "패리티는 단순 하지만 짝수 개 비트 반전 등을 놓칩니다. CRC는 생성다항식에 대한 이진 다항식 나머지로 검출하며 모든 손상을 확률0으로 잡는 기능은 아닙니다. FEC는 Hamming·Reed-Solomon·LDPC등 부호의 거리와 복잡도에 따라 정정능력이 정해집니다.",
        "Stop-and-Wait는 프레임 하나를 보낸 뒤 ACK를 기다리고 timeout이면 재전송합니다. 교대 순서 번호로 ACK손실 뒤의 중복을 구별합니다. 전파지연이 긴 경로에 서 는 한 번에 하나라는 제약으로 이용률이 낮습니다.",
        "Go-Back-N은 송신윈도우내 여러 프레임을 연속 전송하고 누적ACK를 사용합니다. 수신기가 다음 기대 프레임만 받아들이는 기본형에서 중간 프레임 손실 시 해당프레임부터 뒤의 미확인 프레임을 재전송합니다. 순서 번호 공간·윈도우크기·타이머 규칙을 명시해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "Stop-and-Wait",
            "1개 전송 후대기",
            "단순·긴RTT에서 비효율"
          ],
          [
            "Go-Back-N",
            "윈도우·누적ACK",
            "손실 뒤 정상프레임도 재전송"
          ],
          [
            "Selective Repeat",
            "선택 재전송·버퍼",
            "복잡도·순서 번호 공간 증가"
          ]
        ]
      },
      "example": {
        "title": "이용률과 손실 복구",
        "input": "프레임송신1ms, 편도전파4ms, ACK시간무시;오류없음",
        "steps": [
          "Stop-and-Wait 주기는 1+2×4=9ms이 므로 이용률은1/9≈11.1%입니다.",
          "윈도우W=9이면 이상적 파이프라인에 서 경로를 채울 수 있습니다.",
          "GBN에서0, 1, 2, 3전송중1손실이면 기본 수신기는 2·3을 버리고1을 기대합니다.",
          "타이머 만료 후1부터 미확인 프레임을 재전송합니다."
        ],
        "result": "대역·지연곱이 커질수록 파이프라인의 효과가 커집니다.",
        "caution": "계산은 처리·ACK전송·큐잉을 무시한 가정입니다. 링크규격별 실제 동작은 다를 수 있습니다."
      },
      "answer_outline": [
        "검출·정정·ARQ 관계",
        "두 절차 시간축",
        "윈도우 비교",
        "이용률 계산",
        "번호·타이머 고려"
      ],
      "pitfalls": [
        "CRC를 암호학적 무결성으로 보지 않습니다.",
        "누적ACK를 각프레임 개별ACK와 혼동하지 않습니다."
      ],
      "recall": [
        "오류 검출만으로 복원이 가능합니까?",
        "GBN에서 정상프레임 재전송이 생기는 이유는 무엇입니까?",
        "RTT가10배이면정지대기효율은 어떻게 됩니까?"
      ],
      "source_ids": [
        "sys-rfc9293"
      ],
      "validation": "부분 확인",
      "version_note": "ARQ일반 원리를 TCP 자료로 교차확인했으나GBN링크규격·부호원표준은 직접 미열람. 계산은 자체검산.",
      "requirements": [
        {
          "question": "138-4-4",
          "items": [
            "오류 검출·정정",
            "정지대기·GBN개념·절차",
            "상세비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "137-3-5",
          "items": [
            "오류제어·슬라이딩윈도우"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "differential-manchester",
      "title": "차등 맨체스터 부호화",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "비트 중간에는 항상 뒤집어 시계를 맞추고, 비트 시작에 서 뒤집는지로0·1을 구별합니다.",
      "definition": "차등 맨체스터는 매 비트 중앙의 전이로 동기를 제공하고 비트 경계의 전이 유무에 데이터 값을 부여하는 차등선로부호입니다. 절대 전압 높낮이보다 이전 신호와의 변화 관계를 사용합니다.",
      "principles": [
        "반드시 사용 규약을 먼저 선언합니다. 본 예는 0=비트 시작 전이, 1=시작 전이 없음으로 두고 중간 전이는 모든 비트에 둡니다. 다른 규약·초기 레벨을 쓰는 문제는 그 조건에 맞춰 다시 그립니다.",
        "중간 전이는 수신기의 클록 복구를 돕고 긴 0·1연속에서도 전이가 사라지지 않습니다. 전체 파형의 극성이 반전되어도 전이 유무는 유지되어 데이터 판단에 유리합니다. 이는 잡음·지터·전이 누락까지 모두 복구한다는 뜻은 아닙니다.",
        "NRZ와 비교하면 더 잦은 신호 변화와 필요한 대역폭의 부담이 있습니다. 일반 맨체스터는 중앙 전이의 방향으로 데이터를 구분하는 반면 차등 방식은 시작 전이 유무를 사용하므로 두 부호의 판독 기준을 섞으면 안 됩니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "NRZ",
            "레벨 또는 차분레벨",
            "긴연속값에 서 동기 문제"
          ],
          [
            "Manchester",
            "중앙 전이 방향",
            "자기동기·극성규약 필요"
          ],
          [
            "Differential Manchester",
            "시작 전이 유무+항상 중앙 전이",
            "극성반전강인·대역 부담"
          ]
        ]
      },
      "example": {
        "title": "1010 직접 부호화",
        "input": "초기직전레벨L;1=시작전이없음, 0=시작전이있음",
        "steps": [
          "첫1:시작L 유지 → 중앙H, 반비트LH입니다.",
          "다음0:직전H에서시작L로전이 → 중앙H, 따라 서LH입니다.",
          "다음1:시작H 유지 → 중앙L, 따라 서HL입니다.",
          "마지막0:직전L에서시작H → 중앙L, 따라 서HL입니다.",
          "반비트열LH LH HL HL을 경계 전이기준으로 역해독하면 1010입니다."
        ],
        "result": "파형은 초기 레벨과 규약을 함께 적어야 유일하게 재현됩니다.",
        "caution": "규약과 초기 레벨에 따른 교육용 예시입니다. 수신기 제품별 idle 레벨·프리앰블·오류 처리는 해당 문서를 확인합니다."
      },
      "answer_outline": [
        "규약·초기 레벨",
        "비트별반파형",
        "중앙 전이와경계 전이",
        "Manchester비교",
        "대역·잡음한계"
      ],
      "pitfalls": [
        "H는 항상1이라는 해석은오류입니다.",
        "중앙 전이를데이터전이로세면안됩니다."
      ],
      "recall": [
        "초기 레벨이 바뀌어도복호 데이터가 같을수 있는 이유는무엇입니까?",
        "0·1규약을 왜명시해야합니까?",
        "반비트열을어떻게역검산합니까?"
      ],
      "source_ids": [
        "sys-manchester"
      ],
      "validation": "출처 확인",
      "version_note": "Microchip DS60001813E 공식 제품 문서의 차등 맨체스터 규약을 직접 확인했습니다. 예제는 초기 레벨 L과 해당 규약에 대한 자체 계산·역검산입니다. IEEE802.5 원문 전문을 읽었다고 주장하지 않습니다.",
      "requirements": [
        {
          "question": "140-1-10",
          "items": [
            "차등적맨체스터부호화"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "routing-and-prefix-lookup",
      "title": "IGP·EGP·RIP·OSPF와 라우팅 탐색",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "경로를 계산해 표를 만드는 일과, 패킷 목적지에 가장 구체적으로 맞는 표 항목을 찾는 일을 구분합니다.",
      "definition": "IGP는 한 자율시스템 내부의 경로 정보를 교환하고 EGP는 자율시스템 사이의 도달성·정책을 교환하는 범주입니다. 대표적IGP에는RIP·OSPF가, 현재 대표적AS간프로토콜에 는 BGP가 있습니다.",
      "principles": [
        "RIP은 거리벡터로 이웃의 거리 정보를 받고 홉수를 사용하며 16을 도달불가로 둡니다. split horizon·poisoned reverse·triggered update등으로 루프·느린수렴을 완화합니다. OSPF는 링크상태를 전파하여 LSDB를 구성하고 최단경로트리를계산하며 area로규모를 관리합니다.",
        "BGP는AS_PATH등경로속성과정책으로도 달성을교환합니다.EGP라는범주와 역사적EGP프로토콜을 구별합니다.루팅정책은 무조건 최소홉을고르는문제가 아니며경로 검증·필터·인증과 장애수렴을고려합니다.",
        "포워딩표검색은Longest Prefix Match가 핵심입니다.일반 BST는 키의 대소비교이지만 IP프리픽스는 포함관계와 길이를다루므로binarytrie·Patricia·다중비트trie·TCAM등을 사용합니다.균형BST의O(logn)을모든 라우팅검색의확정복잡도로 일반 화하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "RIP",
            "거리벡터·홉수",
            "단순;15홉상한·수렴"
          ],
          [
            "OSPF",
            "링크상태·SPF·area",
            "규모·자원·설정 복잡도"
          ],
          [
            "BGP",
            "AS경로·정책",
            "AS간확장·정책 오류 위험"
          ]
        ]
      },
      "example": {
        "title": "가장 긴 프리픽스 선택",
        "input": "경로0.0.0.0/0 → A, 10.0.0.0/8 → B, 10.1.0.0/16 → C;목적지10.1.2.3",
        "steps": [
          "세 항목이 모두 주소를 포함하는 지 확인합니다.",
          "프리픽스 길이0, 8, 16중16이 가장 길므로C로 보냅니다.",
          "10.2.2.3은/16에 안맞아B를 고릅니다.",
          "표 생성의OSPF최단경로 계산과 표 검색의LPM을 분리해 도식화합니다."
        ],
        "result": "탐색자료 구조의 공통점은 분기 탐색이지만 정렬 키와 매칭조건이 다릅니다.",
        "caution": "IPv6·하드웨어포워딩·캐시 구조별 구현은 장비별 확인이 필요합니다."
      },
      "answer_outline": [
        "IGP/EGP범주",
        "RIP/OSPF 비교",
        "BGP정책",
        "제어·포워딩분리",
        "BST와LPM예"
      ],
      "pitfalls": [
        "OSPF를 단순 홉수프로토콜이라 하지 않습니다.",
        "정확한주소일치만찾는검색으로설명하지 않습니다."
      ],
      "recall": [
        "라우팅계산과 LPM의차이는무엇입니까?",
        "RIP의16은 무슨뜻입니까?",
        "BST대소비교만으로prefix포함관계를 해결할 수 있습니까?"
      ],
      "source_ids": [
        "sys-rfc2453",
        "sys-rfc2328",
        "sys-rfc4271",
        "sys-rfc4632"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "134-1-8",
          "items": [
            "RIP·OSPF비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "137-1-1",
          "items": [
            "IGP·EGP"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "139-3-5",
          "items": [
            "BST와 라우팅테이블탐색상관관계"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "sdn-openflow-ibn",
      "title": "SDN·OpenFlow·IBN",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "장비마다 명령을 입력하는 데서 나아가 중앙의 정책과 상태를 바탕으로 네트워크 동작을 제어합니다.",
      "definition": "SDN은 네트워크 제어 기능과 패킷 전달 기능의 분리·추상화·프로그래밍 가능성을 강조하는 접근입니다. OpenFlow는 컨트롤러와 스위치가 흐름 규칙을 교환하는 인터페이스 계열이고 IBN은 의도를 정책으로 변환하고 충족 여부를 지속 검증합니다.",
      "principles": [
        "응용 계층은 서비스 요구를 표현하고 제어계층은 토폴로지·경로·정책을 계산하며 데이터평면은규칙에 따라 전달합니다.논리적중앙화와물리적단일장애점은 같은 뜻이아니며컨트롤러복제·분산일관성·상실시정책을 설계합니다.",
        "OpenFlow의 흐름 표는 일치조건·우선순위·동작·카운터등을 갖습니다.기존 규칙이 없는 패킷을 컨트롤러로알려규칙을 설치하거나사전설치할 수 있습니다.버전별pipeline·group등의 세부기능은 명세확인이 필요합니다.",
        "IBN은 의도수집 → 변환·검증 → 활성화 → 텔레메트리기반보장으로설명합니다.예를들어고객정보 서버에 승인 업무만 접속가능하다는의도를분류·접근 정책으로 구현하고 실제 흐름과 대조합니다.AI사용이필수정의 는아니며잘못된의도·충돌·관측누락을고려합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "전통관리",
            "장비별명령·구성",
            "수동오류·변경추적"
          ],
          [
            "SDN",
            "제어/전달 분리·API",
            "제어면가용성·보안"
          ],
          [
            "IBN",
            "의도와결과의 폐루프",
            "의도모호성·검증 모델"
          ]
        ]
      },
      "example": {
        "title": "업무망 격리 의도",
        "input": "인사서비스는 인사단말에 서 만허용;백업은 별도 경로",
        "steps": [
          "의도를출발지·목적지·서비스·예외로 명세합니다.",
          "컨트롤러가토폴로지와정책 충돌을 검증합니다.",
          "허용·차단 규칙을 설치하고 카운터·플로우로그를 수집합니다.",
          "실제 접속시험에 서 위반이있으면 변경 원인과 정책을 재평가합니다."
        ],
        "result": "원하는상태와 관측한상태의 차이를운영루프로관리합니다.",
        "caution": "RFC7149는SDN관점문서이며 OpenFlow명세및IBN 규격 전문은 미열람입니다."
      },
      "answer_outline": [
        "문제와 정의",
        "3계층도 식",
        "OpenFlow 흐름 표",
        "IBN폐루프",
        "보안·가용성"
      ],
      "pitfalls": [
        "SDN이 OpenFlow하나와동의어라고쓰지않습니다.",
        "중앙화가반드시 하나의서버를 뜻하지 않습니다."
      ],
      "recall": [
        "제어면과데이터면은무엇을각각 결정합니까?",
        "의도검증이 구성배포이 후에도필요한 이유는무엇입니까?",
        "컨트롤러장애시정책은 무엇입니까?"
      ],
      "source_ids": [
        "sys-rfc7149"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "127-3-5",
          "items": [
            "SDN제어평면구조",
            "OpenFlow"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "135-1-4",
          "items": [
            "IBN"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "vxlan-overlay",
      "title": "VXLAN 오버레이 네트워크",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "IP 네트워크 위에 가상 이더넷 망을 얹어 같은 물리망에서도 여러 입주자의 통신을 나눕니다.",
      "definition": "VXLAN은 Ethernet 프레임을 UDP/IP로 캡슐화하여 L3언더레이 위에L2오버레이를 제공하는 기법입니다. VTEP는 캡슐화·역캡슐화를 담당하고 24비트VNI로 가상세그먼트를 식별합니다.",
      "principles": [
        "원래프레임에 는 내부 MAC·페이로드가있고VTEP가 외부IP·UDP·VXLAN헤더를붙입니다.중간IP라우터는외부 주소로 전달하고 목적VTEP가 내부 프레임을 복원합니다.내부테넌트식별과외부 경로 선택을 분리합니다.",
        "24비트VNI는 약1600만식별공간을제공하지만실제 장비 지원 규모·예약·정책은 별개입니다.BUM트래픽처리에 는 멀티캐스트나헤드엔드복제등구현이 있고MAC 학습·위치배포에 는 EVPN같은 제어면을결합할 수 있습니다.",
        "캡슐화는추가 헤더를만들어MTU·단편화·성능에 영향을 줍니다.언더레이ECMP·지연·장애수렴과오버레이의MAC/ARP상태를 함께 관측해야합니다.VNI는 격리식별자이지암호화나인증 기능이 아니므로접근 통제·VTEP신뢰·관리면보호가 필요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "VLAN",
            "12비트태그의L2구분",
            "규모·물리L2범위제약"
          ],
          [
            "VXLAN",
            "24비트VNI·L2overL3",
            "캡슐화·MTU·상태 관리"
          ],
          [
            "언더레이",
            "VTEP간IP도 달성",
            "오버레이정책과 별도"
          ]
        ]
      },
      "example": {
        "title": "두 테넌트의 같은 내부 주소",
        "input": "테넌트A와B가 모두10.0.0.1사용;VNI100/200",
        "steps": [
          "VTEP가 각프레임에 VNI100또는200을 부여합니다.",
          "외부IP망은VTEP주소로 전달하며 내부 주소 중복에 영향받지않습니다.",
          "수신VTEP는VNI별분리된브리지도메인으로전달합니다.",
          "다른 VNI로 통신하려면명시적게이트웨이·정책을 사용합니다."
        ],
        "result": "주소 공간중복을 테넌트문맥으로분리할 수 있습니다.",
        "caution": "식별자분리만 으로악성VTEP나관리 권한 침해를 방어할 수 없습니다."
      },
      "answer_outline": [
        "필요성",
        "VTEP·VNI·헤더도식",
        "VLAN비교",
        "전달 사례",
        "MTU·보안"
      ],
      "pitfalls": [
        "24비트VNI를 24비트IP주소라쓰지않습니다.",
        "VXLAN자체가암호화라고하지 않습니다."
      ],
      "recall": [
        "외부라우터는어느주소로 포워딩합니까?",
        "VNI와 보안인증의 차이는무엇입니까?",
        "MTU를 확인해야 하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-rfc7348"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "130-1-8",
          "items": [
            "VXLAN 개념·구조"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "wireless-multiple-access",
      "title": "CSMA/CA·TDMA·CDMA·NOMA",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "여러 단말이 같은 전파 자원을 나눠 쓰는 방식은 기다리기, 시간 나누기, 코드 나누기, 겹쳐 보내고 분리하기로 구분할 수 있습니다.",
      "definition": "다중접속은 제한된 무선매체를 여러 사용자가 공유하는 규칙입니다. CSMA/CA는 경쟁접근과 회피를, TDMA는 시간슬롯을, CDMA는 확산코드를, NOMA는 비직교중첩과 수신분리를 활용하는 접근입니다.",
      "principles": [
        "CSMA/CA는 매체감지후대기·무작위백오프를수행하고 ACK로성공을확인합니다.무선송신중충돌검출이어려우므로충돌 회피를 사용하지만충돌이 0이라는 보장은없습니다.RTS/CTS는 숨은단말 문제를 완화하는선택 기법이며 오버헤드가 있습니다.",
        "TDMA는 시간슬롯과동기·가드시간이 필요합니다.CDMA는 사용자별확산코드와 상관검출로분리하며 코드직교성·전력제어·near-far문제가 중요합니다.시간·주파수·코드 자원은 실제 시스템에 서 결합될수 있습니다.",
        "전력 영역 NOMA예에서는서로 다른 전력으로 신호를중첩하고 SIC로강한간섭을 순차소거합니다.다른 NOMA유형도있으므로SIC하나로전체를정의하지 않습니다.채널추정오차·소거오류전파·단말 복잡도와 공정성에 따라 이득이달라집니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "CSMA/CA",
            "감지·백오프·ACK",
            "유동접속;충돌·변동지연"
          ],
          [
            "TDMA",
            "슬롯분할",
            "동기·가드시간·유휴낭비"
          ],
          [
            "CDMA",
            "확산코드",
            "전력제어·코드상관"
          ],
          [
            "NOMA",
            "비직교중첩·분리",
            "SIC복잡도·채널추정"
          ]
        ]
      },
      "example": {
        "title": "동일 슬롯의 전력 중첩",
        "input": "기지국이근거리·원거리단말에 동시송신;교육용개념",
        "steps": [
          "원거리단말에 상대적으로큰전력을 배정합니다.",
          "근거리단말은 먼저 큰전력성분을복호하고 소거한뒤자기신호를복호합니다.",
          "원거리단말은 다른성분을간섭으로 보고 복호합니다.",
          "채널상태·전력할당·오류율을함께 평가합니다."
        ],
        "result": "직교자원 분할과 비직교간섭 처리의 차이를설명합니다.",
        "caution": "CSMA/CA·CDMA·NOMA의 원표준 전문은 이번조사에서미확인입니다.이론개요이며 특정5G·6G필수규격으로 단정하지 않습니다."
      },
      "answer_outline": [
        "자원공유문제",
        "네방식도 식",
        "비교표",
        "숨은단말·SIC사례",
        "절충"
      ],
      "pitfalls": [
        "CSMA/CA를 충돌검출이라쓰지않습니다.",
        "NOMA를 6G최종필수규격이라 확정하지 않습니다."
      ],
      "recall": [
        "무선에서충돌 회피가 필요한 이유는무엇입니까?",
        "CDMA의 near-far문제는 무엇입니까?",
        "SIC오류는 어떻게전파됩니까?"
      ],
      "source_ids": [
        "sys-6g"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "129-1-12",
          "items": [
            "NOMA"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-3-4",
          "items": [
            "CSMA/CA",
            "CDMA",
            "TDMA"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "wifi7-wifi8",
      "title": "Wi-Fi7과 IEEE802.11bn UHR",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "큰 최대속도와 혼잡한 현장에서 끊기지 않는 품질은 다른 목표이 므로 채널·링크·지연을 함께 봅니다.",
      "definition": "Wi-Fi7은IEEE802.11be의EHT기술을 기반으로 하는세대이며, 802.11bn은UHR(Ultra High Reliability)향상을목표로 개발중인프로젝트입니다. Wi-Fi인증명과IEEE표준판·초안상태를 구분합니다.",
      "principles": [
        "Wi-Fi7의주요 기술은 320MHz채널, 4096-QAM, MLO입니다.더넓은채널은가용 대역과규제·간섭에 좌우되고고차변조는좋은신호품질을 요구합니다.4096-QAM의심볼당 12비트는1024-QAM의 10비트보다20%많지만실사용속도전체가항상20%향상되는것은아닙니다.",
        "MLO는 여러 링크를통한전송·스케줄링으로처리량·신뢰성·지연을 개선할 수 있습니다.단말의 동시송수신능력과링크간간섭·전력·AP지원을 확인해야합니다.기존 OFDMA·MU-MIMO와 의관계 도구분합니다.",
        "802.11bnPAR는 특정 조건에 서 MAC 처리량 증가, 95백분위지연과 MPDU손실감소등UHR목표를 다룹니다.개발 목표를 확정제품의 보장성능·완성표준 기능으로 쓰지않습니다.고밀도·이동·중첩 BSS에 서 평균뿐 아니라꼬리지연과 연속성을측정합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "Wi-Fi6/6E",
            "효율·6GHz확장",
            "주파수와단말호환성"
          ],
          [
            "Wi-Fi7",
            "EHT·MLO·320MHz·4KQAM",
            "환경별효과 검증"
          ],
          [
            "802.11bn",
            "UHR개발프로젝트",
            "초안·목표와 최종 규격구분"
          ]
        ]
      },
      "example": {
        "title": "밀집 사무실 검증",
        "input": "동일AP배치에서업무영상회의와대용량 전송혼재",
        "steps": [
          "클라이언트의 대역·MLO지원여부를확인합니다.",
          "평균처리량과 함께 p95지연·손실·로밍중단을측정합니다.",
          "320MHz가 혼잡·간섭으로 불리하면 채널폭과재사용계획을 조절합니다.",
          "동일업무·동일위치에서링크구성변경전후를비교합니다."
        ],
        "result": "최대PHY속도와업무체감품질을 구분해도입근거를 만듭니다.",
        "caution": "Wi-Fi7제품 문서검색본문은확인했으나직접 open은 리다이렉트실패였습니다.802.11bnPAR 원문은 열람했습니다."
      },
      "answer_outline": [
        "세대·표준 상태",
        "Wi-Fi7핵심 기술",
        "bnUHR목표",
        "측정예",
        "주파수·호환성"
      ],
      "pitfalls": [
        "bn초안을완성규격으로 쓰지않습니다.",
        "PHY최대속도를사용자실효속도로바꾸지않습니다."
      ],
      "recall": [
        "4KQAM이 좋은SNR을 필요로하는이유는무엇입니까?",
        "MLO는 어떤문제를 개선합니까?",
        "p95지연을 평균과함께 봐야하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-wifi7",
        "sys-wifi8"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "139-1-10",
          "items": [
            "Wi-Fi7"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "135-1-10",
          "items": [
            "IEEE802.11bn"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "imt2030-ai-native",
      "title": "6G·SATIN·AI-Native 네트워크·5G 특화망",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "통신망이 데이터를 전달하는 데서 더 나아가AI·센싱·위성연결을 결합하는 방향과, 현재 구축 가능한 지역 전용망을 구분합니다.",
      "definition": "IMT-2030은2030년이후 이동통신 발전의 ITU프레임워크입니다. SATIN은 위성·상공·지상망을결합한연결 구조이며 AI-Native는AI를 망의설계·제어·운영에 통합하는지향입니다. 5G특화망은한정된공간·업무에 맞춰구축하는전용이동통신망입니다.",
      "principles": [
        "ITU-RM.2160은 몰입통신·초고신뢰저지연·대규모 통신의 확장과유비쿼터스연결·AI및통신·통합센싱통신등의 시나리오를 제시합니다.능력목표의 범위는 시나리오에 따른연구목표이며 모든 목표를 동시에보장하는상용규격이 아닙니다.",
        "SATIN은 재난시지상망우회·낙후지역백홀·UAV연결을 돕지만궤도별지연·이동성·가시성·핸드오버·주파수공유를고려합니다.AI-Native는 텔레메트리 → 학습·추론 → 정책 → 행동 → 감시의 폐루프로트래픽·무선자원을 최적화하며 AI-RAN과 망디지털트윈을활용할 수 있습니다.",
        "특화망은업무 SLA와 커버리지·실내외환경·주파수·간섭·코어/엣지배치·보안·이중화를먼저 정합니다.공장지연은 무선구간만아니라단말·전송·코어·응용전체로측정합니다.주파수할당·6G후보대역은시점·국가별확인사항입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "6G프레임워크",
            "미래사용·능력목표",
            "최종 규격·상용보장과구분"
          ],
          [
            "SATIN",
            "비지상·지상통합",
            "지연·핸드오버·가시성"
          ],
          [
            "5G특화망",
            "업무·지역전용구축",
            "간섭·가용성·운영인력"
          ]
        ]
      },
      "example": {
        "title": "재난 현장 연결",
        "input": "지상백홀손상;UAV영상과구조대데이터 연결",
        "steps": [
          "저대역필수음성·위치와대용량영상을우선순위로나눕니다.",
          "위성백홀과임시기지국·UAV중계의가시성과전원을 확인합니다.",
          "단절시로컬처리와 저장후전송을 사용합니다.",
          "AI정책이 망을불안정하게만들면안전한 기본 설정으로 복귀합니다."
        ],
        "result": "이종망통합의가치와 AI자동제어의안전 조건을 연결합니다.",
        "caution": "SATIN·AI-RAN상세명세와국내주파수현황은직접 확인하지못했습니다."
      },
      "answer_outline": [
        "ITU프레임워크",
        "6시나리오·목표",
        "SATIN구조",
        "AI폐루프·트윈",
        "특화망설계"
      ],
      "pitfalls": [
        "6G가 이미단일최종성능 규격으로 확정됐다고쓰지않습니다.",
        "AI가 항상 최적정책을 보장한다고하지 않습니다."
      ],
      "recall": [
        "SATIN은 재난 대응에 서 어떤제약이있습니까?",
        "망디지털트윈으로무엇을시험합니까?",
        "특화망의간섭과 이중화는어떻게함께 설계합니까?"
      ],
      "source_ids": [
        "sys-6g"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "130-1-7",
          "items": [
            "6G"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "128-4-3",
          "items": [
            "SATIN개념·특징",
            "재난·UAV·낙후지역활용"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "135-2-4",
          "items": [
            "6G서비스·성능 요구·주파수동향"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-4-3",
          "items": [
            "자율최적화",
            "AI-RAN",
            "트윈망관리"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "133-4-5",
          "items": [
            "5G특화망안정성·신뢰성",
            "간섭 회피"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "nfc-ot-modbus",
      "title": "NFC와 MODBUS·산업제어 보안",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "근접 태그 통신과 산업 제어 통신은 사용 환경이 다르지만, 연결됐다는 사실만으로 신뢰해서는 안 됩니다.",
      "definition": "NFC는 13.56MHz기반의 근접비접촉통신으로 태그의전력공급·데이터교환을지원합니다. MODBUS는 장치간기능 코드와 데이터 모델로 읽기·쓰기 요청을 주고받는산업용응용 프로토콜입니다. 두개념은 통신기출의독립소단원으로묶었습니다.",
      "principles": [
        "NFC는 리더/라이터·카드에뮬레이션등의 이용형태가있고NDEF는 공통메시지표현입니다.유도결합으로수동태그에도전력을 전달할 수 있습니다.짧은거리라는특성이 도청·릴레이·악성태그·분실기기 위험을 제거하지는않습니다.",
        "MODBUS 데이터 모델은 coil·discreteinput·inputregister·holdingregister등을 구분합니다.RTU등직렬방식과 TCP 방식의 전달형식이달라도응용 기능의 역할은구분하여 설명합니다.주소 표현·엔디언·레지스터조합은장비명세를따릅니다.",
        "전통산업망은평문·신뢰망전제를 보완해야합니다.자산·통신 흐름식별 → 구역과통로 분리 → 필요기능 코드·출발지허용 → 원격접속인증 → 수동모니터링·변경 관리순으로설계합니다.ISA/IEC62443은 산업 자동화제어보안의역할·생애주기·구역과통로등을 다루는 표준군이며 세부조항은 판본별확인합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "NFC",
            "근접·태그·유도전력",
            "릴레이·위조태그·사용자 고지"
          ],
          [
            "MODBUS",
            "기능 코드·레지스터",
            "평문·쓰기 권한·장비 특성"
          ],
          [
            "산업보안",
            "구역·통로·생애주기",
            "가용성·안전성·변경 위험"
          ]
        ]
      },
      "example": {
        "title": "공장 계측값 조회",
        "input": "MES는 온도레지스터조회만필요;제어쓰기는 PLC만허용",
        "steps": [
          "장비별레지스터맵과통신필요성을기록합니다.",
          "조회서버에 서 읽기 기능만 허용하고 제어쓰기를 차단합니다.",
          "원격유지보수는승인·시간제한·기록을 적용합니다.",
          "패치·차단 변경은 공정안전에 미치는영향을 검증후적용합니다."
        ],
        "result": "업무최소 권한과 산업 가용성을 같이확보합니다.",
        "caution": "MODBUS 공식 목록은 열람했으나기능 코드 원문과 ISA62443전문은 미열람입니다."
      },
      "answer_outline": [
        "각통신정의",
        "NFC 동작·위험",
        "MODBUS 데이터·흐름",
        "62443범위",
        "안전한 통제예"
      ],
      "pitfalls": [
        "근거리라서인증이 불필요하다고쓰지않습니다.",
        "IT보안스캔을무조건가 동중PLC에적용하지 않습니다."
      ],
      "recall": [
        "수동태그는전력을 어떻게얻습니까?",
        "MODBUS 읽기와 쓰기 권한을 나누는이유는무엇입니까?",
        "구역과통로가 업무 흐름과 연결돼야하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-nfc",
        "sys-modbus"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "131-1-2",
          "items": [
            "NFC"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "137-1-3",
          "items": [
            "MODBUS"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-1-5",
          "items": [
            "ISA/IEC62443"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "fifo-wfq",
      "title": "FIFO와 Weighted Fair Queueing",
      "domain": "네트워크·통신",
      "aliases": [],
      "easy": "먼저 온 패킷을 순서대로 처리할지, 흐름별 약속한 비율로 공평하게 나눠 보낼지 선택합니다.",
      "definition": "FIFO는 도착순으로하나의큐에서처리하는정책입니다. WFQ는 흐름·클래스별큐와가중치를 사용하여 이상적인가중공유서비스를 패킷수준에서근사하는스케줄링정책입니다.",
      "principles": [
        "FIFO는 분류·상태 관리가 단순 하지만대용량 흐름이 큐를채우면다른 흐름의 지연·손실도 증가합니다.버퍼를크게하는것만으로품질을 해결하면 bufferbloat가 생길수 있습니다.정책의 단순성과서비스차등화의한계를 함께 씁니다.",
        "WFQ는 각흐름의 가중치와 패킷길이를고려한가상완료시각등으로전송 순서를 정합니다.활성흐름들사이의가중몫을제공하며 놀고있는 몫은다른 흐름이 사용할 수 있습니다.흐름식별·가중치 설계·상태 메모리·분류 공격을 검토합니다.",
        "가중비율은동시에백로그가 있는 흐름의 장기적분배를설명합니다.매순간패킷하나까지정확한비율이거나절대지연 상한을 단독보장하는것은아닙니다.경로대역·입구폴리싱·쉐이핑·큐관리·혼잡제어와연결하여 SLA를 설계합니다.",
        "혼잡 시 패킷을 언제 버리거나 표시할지 정하는 큐 관리와, 다음 패킷을 고르는 스케줄링도 다른 기능입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "FIFO",
            "도착순·단일큐",
            "단순;흐름간간섭"
          ],
          [
            "WFQ",
            "흐름별큐·가중공유",
            "분류·상태·가중치 관리"
          ],
          [
            "우선순위큐",
            "높은 클래스우선",
            "저우선 기아방지필요"
          ]
        ]
      },
      "example": {
        "title": "가중치로 대역 분배",
        "input": "링크60Mbps;A/B/C가 항상 백로그;가중치1/2/3",
        "steps": [
          "가중치 합은6입니다.",
          "이상적장기분배는A10, B20, C30Mbps입니다.",
          "C가 비면활성가중치 합3으로A20, B40Mbps까지재분배할 수 있습니다.",
          "패킷길이·프로토콜 오버헤드·도착 시점으로 짧은구간실측은달라집니다."
        ],
        "result": "가중치와 고정예약을구분하고 유휴대역활용을 설명합니다.",
        "caution": "구현에 따라 WFQ명칭의정확한알고리즘과 클래스단위가 다르므로장비 정책을 확인합니다."
      },
      "answer_outline": [
        "큐잉목적",
        "두정책 원리",
        "대역·지연·복잡도비교",
        "1:2:3계산",
        "QoS통합"
      ],
      "pitfalls": [
        "WFQ의 W를 윈도우로해석하지 않습니다.",
        "가중치만 으로종단간지연보장을선언하지 않습니다."
      ],
      "recall": [
        "FIFO에 서 큰흐름이 다른 흐름에 미치는영향은 무엇입니까?",
        "활성흐름이 줄면몫은어떻게바뀝니까?",
        "패킷길이를고려하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-rfc1633"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "140-2-5",
          "items": [
            "FIFO·WFQ비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "cloud-service-deployment-edge",
      "title": "클라우드 서비스·배포 모델과 엣지",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "무엇을 서비스로 빌리는지와 누구와 자원을 공유하는지, 연산을 어디서 하는지는 서로 다른 선택입니다.",
      "definition": "클라우드 컴퓨팅은 공유된 구성가능 자원에 필요시 접근하고 신속히 할당·반환하는 서비스 모델입니다. IaaS/PaaS/SaaS는 제공 계층, 퍼블릭/프라이빗/커뮤니티/하이브리드는 배포 모델이며 엣지는 데이터 발생원 가까이에 연산을 배치하는 접근입니다.",
      "principles": [
        "NIST의 다섯 특성은 주문형 셀프서비스, 광대역 네트워크 접근, 자원 풀링, 신속한 탄력성, 측정 가능한 서비스입니다. 단순한 외부 서버 호스팅이나 가상화만으로 모든 특성을 충족하는 것은 아닙니다.",
        "IaaS는 컴퓨팅·스토리지·네트워크를 제공하고 이용자가 OS·응용을 관리합니다. PaaS는 응용 실행 플랫폼을 제공하고 SaaS는 제공자의 응용을 사용합니다. 어느 모델에서도 이용자의 데이터·권한·설정 책임이 전부 없어지는 것은 아닙니다.",
        "엣지는 전송 지연·대역 비용·연결 단절·데이터 지역성 때문에 유리하지만 작은 자원·분산 운영·물리보안이 과제입니다. 중앙 클라우드는 대규모 자원과 통합 관리에 유리하므로 엣지의 즉시 제어와 클라우드의 학습·장기 분석을 연결할 수 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "서비스 모델",
            "IaaS/PaaS/SaaS",
            "관리 책임 경계"
          ],
          [
            "배포 모델",
            "공유·소유·접근 범위",
            "퍼블릭도전용자원가 능"
          ],
          [
            "엣지배치",
            "발생원 인근 처리",
            "단절·지연·분산관리"
          ]
        ]
      },
      "example": {
        "title": "공장 영상 검사",
        "input": "불량판정50ms이 내;중앙망가끔단절",
        "steps": [
          "엣지에서 즉시추론과 안전한 기본제어를 수행합니다.",
          "클라우드에 선별 데이터와 지표를 전송해 재학습·집계를 합니다.",
          "모델 버전·업데이트 서명·롤백과 단절시 정책을 둡니다.",
          "중앙 집중과 엣지 분산의 총운영비·보안 범위를 비교합니다."
        ],
        "result": "서비스 계층과 배치 위치를 조합하여 요구를 충족합니다.",
        "caution": "클라우드·엣지의 빠르기를 거리만으로 단정하지 않고 종단간 지연을 측정합니다."
      },
      "answer_outline": [
        "5특성",
        "3서비스 책임 표",
        "4배포 모델",
        "엣지 비교",
        "적용 사례"
      ],
      "pitfalls": [
        "퍼블릭과IaaS를 같은 분류축으로비교하지 않습니다.",
        "엣지가클라우드를 완전히대체한다고쓰지않습니다."
      ],
      "recall": [
        "PaaS이 용자의 책임은 무엇입니까?",
        "하이브리드와멀티클라우드의 차이는무엇입니까?",
        "엣지가보안에추가 하는과제는무엇입니까?"
      ],
      "source_ids": [
        "sys-cloud"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "131-1-4",
          "items": [
            "Service Model·Deployment Model비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "139-1-6",
          "items": [
            "Edge·Cloud차이"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "virtualization-daas",
      "title": "가상화·응용 가상화·DaaS",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "실제 장비·실행 환경을 추상화해 나눠 쓰거나, 화면만 전달해 다른 장소의 프로그램을 사용하게 합니다.",
      "definition": "가상화는 물리 자원의 구체 구현을 감추고 논리 자원·실행 환경을 제공하는 기법입니다. 서버 VM·응용 가상화·원격 데스크톱은 격리하는 대상과 실행 위치가 다르며 DaaS는 데스크톱을 서비스로 제공하는 방식입니다.",
      "principles": [
        "일반 응용은 OS의 시스템콜·라이브러리·파일·레지스트리 등 환경에 의존합니다. 응용가 상화는 이 의존성을 패키징·리다이렉트·격리하여 충돌과 설치 부담을 줄이거나 서버에 서 실행한 응용 화면을 전달할 수 있습니다. 구현 방식을 먼저 구별합니다.",
        "VM은 하이퍼바이저가 가상하드웨어를 제공하고 각각 게스트OS를 실행합니다. 컨테이너는 주로 호스트커널을 공유하는 격리된 프로세스이 므로 가벼운 배포에 유리하되 보안경계와 OS호환성의 전제가 다릅니다.",
        "원격데스크톱은 입력을 원격으로 보내고 화면·오디오 등을 전달합니다. RDP·ICA/HDX·PCoIP·VNC등은 압축·전송·장치리다이렉션·보안 기능이 다릅니다. DaaS는 사용자 프로필·접속인증·세션·라이선스·망지연·데이터 반출을 함께 운영해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "서버 VM",
            "게스트OS별실행",
            "격리·무게·라이선스"
          ],
          [
            "컨테이너",
            "커널공유프로세스",
            "이식·배포·커널경계"
          ],
          [
            "DaaS",
            "데스크톱서비스·원격표시",
            "세션·프로필·반출통제"
          ]
        ]
      },
      "example": {
        "title": "외주 개발자의 원격 작업",
        "input": "중요소스는 내부보관;개발자는 원격접속",
        "steps": [
          "개인 단말에 서 강한 인증 후 제한된 데스크톱을 제공합니다.",
          "클립보드·드라이브·프린터 리다이렉션 필요성을 승인합니다.",
          "사용자 프로필과 작업 데이터의 수명·백업을 분리합니다.",
          "지연·동시접속·빌드부하를 측정해 자원을 산정합니다."
        ],
        "result": "데이터 보관 위치와 실제 반출 경로를 함께 관리합니다.",
        "caution": "화면전달만 으로촬영·악성단말·권한오용위험이 사라지지는않습니다."
      },
      "answer_outline": [
        "일반 실행 흐름",
        "응용가 상화유형",
        "VM·컨테이너비교",
        "원격프로토콜",
        "DaaS운영"
      ],
      "pitfalls": [
        "가상화와클라우드를 동의어로쓰지않습니다.",
        "컨테이너마다게스트OS가 필요하다고설명하지 않습니다."
      ],
      "recall": [
        "응용 실행위치와화면표시위치는어떻게다릅니까?",
        "VM과 컨테이너의커널은어떻게다릅니까?",
        "DaaS에반출통제가 필요한 이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-containers",
        "sys-daas"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "129-2-1",
          "items": [
            "일반 OS 프로그램 동작",
            "응용가 상화",
            "원격데스크톱프로토콜"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "127-1-13",
          "items": [
            "DaaS"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "infrastructure-as-code",
      "title": "코드형 인프라 IaC",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "서버·망을 클릭한 기억에 의존하지 않고, 원하는 구성을 코드로 검토·재현합니다.",
      "definition": "IaC는 인프라 자원을 기계가 읽을 수 있는 정의로 관리하여 버전 관리·검토·자동배포·재현을 가능하게 하는 접근입니다. 선언형은 원하는 상태를, 명령형은 수행 절차를 중심으로 기술합니다.",
      "principles": [
        "일반 흐름은 정의작성 → 검증·계획 → 차이검토 → 적용 → 관측입니다. Terraform의 plan은 현재 상태와 구성의차이를계산하고 apply는 변경을 수행합니다. 코드 검토에 생성뿐 아니라삭제·대체·의존순서·장애 영향을 포함합니다.",
        "상태파일은관리 자원과 실제 자원의 연결 정보를 보유하므로 잠금·접근 통제·암호화·버전 보호가 필요합니다. 비밀값이 코드또는상태에 남을수 있어비밀관리체계와분리해야합니다. 수동변경으로 인한drift는 정기계획·정책 검사로 찾습니다.",
        "모듈·템플릿은검증된반복단위를 만들되과도한추상화는검토를 어렵게합니다. 정책 코드·승인·최소 권한 실행 주체·공급망서명·롤백또는복원 절차를 CI/CD에연결합니다. IaC가 모든 작업의 원자성·자동롤백을보장하는것은아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "수동관리",
            "콘솔·문서 절차",
            "변경누락·재현어려움"
          ],
          [
            "선언형IaC",
            "원하는상태와 차이계산",
            "상태·provider관리"
          ],
          [
            "명령형자동화",
            "작업 순서명시",
            "중간실패·반복안전성"
          ]
        ]
      },
      "example": {
        "title": "운영 DB의 의도치 않은 대체 방지",
        "input": "스토리지설정 변경 계획에 DB replacement표시",
        "steps": [
          "plan에서삭제·대체 자원과 의존영향을 확인합니다.",
          "백업·복구 가능성과변경허용시간을 검토합니다.",
          "정책 검사로 승인없는 중요자원 삭제를 차단합니다.",
          "테스트 환경 검증뒤검토된정확한계획을 적용하고 상태를 확인합니다."
        ],
        "result": "코드차이가작아도자원 영향은 클수 있음을검토 절차로 통제합니다.",
        "caution": "provider·API 버전변화와외부수동변경까지 영구고정되는것은아닙니다."
      },
      "answer_outline": [
        "정의·필요성",
        "Write-Plan-Apply",
        "상태·drift",
        "검토·보안",
        "변경예"
      ],
      "pitfalls": [
        "코드가 있으면 복구훈련이불필요하다고하지 않습니다.",
        "state를 민감정보없는 단순 캐시로 취급하지 않습니다."
      ],
      "recall": [
        "계획과 적용을 분리하는이유는무엇입니까?",
        "drift는 어떻게발생합니까?",
        "상태파일잠금은 무엇을보호합니까?"
      ],
      "source_ids": [
        "sys-terraform"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "129-1-10",
          "items": [
            "코드형인프라스트럭처"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "kubernetes-hpa",
      "title": "쿠버네티스와 HPA·오토스케일링",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "컨테이너가 원하는 개수와 상태로 계속 실행되도록 제어하고, 관측한 부하에 따라 복제본 수를 조절합니다.",
      "definition": "Kubernetes는 컨테이너화워크로드의 배치·수명·서비스발견·상태회복을선언적API와 제어루프로관리합니다. HPA는 메트릭에따라 Deployment등대상의 복제본수를조절하는수평확장기능입니다.",
      "principles": [
        "제어평면의APIserver는 요청창구, etcd는 상태 저장, scheduler는Pod배치, controller-manager는 원하는상태와 실제 상태를 조정합니다. 노드의 kubelet은Pod 실행을 관리하고 런타임은컨테이너를실행하며 네트워크 구현은 서비스 연결을 지원합니다.",
        "Pod는 배치기본 단위이고 Deployment는 복제·배포를 관리하며 Service는 변동하는Pod에 안정적인접점을제공합니다. readiness는 트래픽수용, liveness는 재시작판단과관련되므로임의로같은 검사로 구성하지 않습니다.",
        "HPA 기본식은ceil(현재 복제본×현재 메트릭/목표메트릭)입니다. CPU이 용률은request대비값이 므로request설정이 중요합니다. min/max·측정누락·미준비Pod·안정화시간·확장속도·노드수 용량을 반영해야합니다. Pod확장과노드확장은다른 제어루프입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "HPA",
            "Pod수증감",
            "메트릭·request·안정화"
          ],
          [
            "VPA",
            "Pod 자원 요구조절",
            "재시작·경합검토"
          ],
          [
            "노드확장",
            "노드 용량증감",
            "기동지연·한도·비용"
          ]
        ]
      },
      "example": {
        "title": "HPA 기본식 검산",
        "input": "현재3Pod, 평균CPU이 용률90%, 목표60%, 최대10",
        "steps": [
          "기본식은ceil(3×90/60)=ceil4.5=5입니다.",
          "새Pod의 준비완료와메트릭수집을 기다리며과도한반복증감을막습니다.",
          "현재 노드 여유가 부족하면 5개를원해도Pending이 될수 있습니다.",
          "DB·외부 API 병목은 Pod수확장만으로해결되지않는지확인합니다."
        ],
        "result": "요청 복제본5와 실제 서비스 용량의 차이를구분합니다.",
        "caution": "수식은기본 원리이며 제품 버전별기본허용오차·안정화값을 고정된보장으로쓰지않습니다."
      },
      "answer_outline": [
        "구조도",
        "컴포넌트역할",
        "Pod·Service·Deployment",
        "HPA수식",
        "안정성·용량"
      ],
      "pitfalls": [
        "Kubernetes가 모든 응용 상태·데이터를 자동복구한다고쓰지않습니다.",
        "HPA를 CPU크기변경이라 하지 않습니다."
      ],
      "recall": [
        "desiredReplicas5가 즉시5배성능을 뜻합니까?",
        "CPUrequest를 왜설정합니까?",
        "readiness와liveness를 분리하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-k8s",
        "sys-hpa"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "133-1-12",
          "items": [
            "Kubernetes"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "137-4-3",
          "items": [
            "개념·특징",
            "컴포넌트",
            "HPA"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "131-1-8",
          "items": [
            "Auto Scaling"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "serverless-computing",
      "title": "서버리스 컴퓨팅",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "서버가 없어지는 것이 아니라 실행 환경의 준비·확장을 서비스 제공자가 맡고, 사용자는 업무 코드를 중심으로 구성합니다.",
      "definition": "서버리스는서버프로비저닝과운영부담을추상화하고 요청·이벤트에 따라 실행과 확장을제공하는 서비스 운영 모델입니다. FaaS와 관리형백엔드서비스등을 조합하며 이벤트트리거·함수·권한·외부 상태 저장이 주요 구성 요소입니다.",
      "principles": [
        "함수는 이벤트 입력을 받아짧은단위 작업을 수행하고 응답하거나다른 서비스에 결과를 남깁니다. 유휴자원 관리부담과탄력적확장이장점이지만 초기실행 지연·실행제한·외부의 존·제공자종속을검토합니다. 요금은제품의 호출·시간·자원·데이터 전송 방식에 따릅니다.",
        "실행컨텍스트의재사용가능성은내구성보장이아닙니다. 필요한 상태는 외부내구저장소에두고중복 이벤트·재시도·순서역전·부분실패를설계합니다. 멱등키·중복제거·실패큐·타임아웃·추적ID가 중요합니다.",
        "서비스가 자동확장해도DB접속·하위API쿼터·계정 동시성은 제한됩니다. 폭주를완화하는큐·예약동시성·백프레셔와최소 권한·비밀관리·로그 보호를 함께 적용합니다. 장시간지속작업이나 일정한 대규모부하에서는대안의총비용을 비교합니다.",
        "관측에는 호출 수뿐 아니라 실패율·재시도 수·동시성·하위서비스 지연·작업당 비용을 함께 사용합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "FaaS",
            "이벤트별함수 실행",
            "콜드스타트·시간제한"
          ],
          [
            "컨테이너서비스",
            "실행이 미지·서비스 운영",
            "수명·확장설정유연"
          ],
          [
            "전통서버",
            "용량·운영직접 관리",
            "지속부하예측·운영 책임"
          ]
        ]
      },
      "example": {
        "title": "이미지 업로드 후 썸네일",
        "input": "객체생성이벤트가 같은 파일에두번도착할 수 있음",
        "steps": [
          "객체 버전과 작업 종류로 멱등키를 생성합니다.",
          "완료기록을 확인하고 이미완료한작업은 중복 반영하지 않습니다.",
          "변환실패는제한재시도후실패큐로보냅니다.",
          "처리량확대전에스토리지·DB쿼터와비용 경보를 설정합니다."
        ],
        "result": "이벤트 중복에도 결과일관성을유지하며 호출폭주를통제합니다.",
        "caution": "서버리스명칭만으로보안·무한확장·최저비용이 보장되지는않습니다."
      },
      "answer_outline": [
        "정의·이벤트 구조",
        "구성 요소",
        "장단점",
        "멱등처리예",
        "도입판단"
      ],
      "pitfalls": [
        "서버가 존재하지 않는다고설명하지 않습니다.",
        "함수로 컬파일을영구저장으로 사용하지 않습니다."
      ],
      "recall": [
        "멱등성이 왜필요합니까?",
        "확장자동화에도 하위서비스 보호가 필요한 이유는무엇입니까?",
        "콜드스타트의영향을 어떻게측정합니까?"
      ],
      "source_ids": [
        "sys-lambda"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "136-1-9",
          "items": [
            "서버리스컴퓨팅"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "140-2-1",
          "items": [
            "정의·특징",
            "구성·장단점",
            "도입 고려"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "multicloud-cmp",
      "title": "멀티클라우드와 클라우드 관리 플랫폼",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "여러 공급자를 쓰는 사실과 그 환경을 통제할 수 있다는 사실은 다르므로 공통 관리와 예외를 정합니다.",
      "definition": "멀티클라우드는 둘이상클라우드 제공자의 서비스를 활용하는 구성입니다. CMP는 서로 다른 환경의 자원·배포·비용·보안·관측을통합 관리하는 플랫폼이며 모든 제공자 기능을 완전히동일하게만드는도구는 아닙니다.",
      "principles": [
        "도입목적은 서비스적합성·규제·지역·협상력·집중위험완화등으로명시합니다. 업무 분할·활성복제·DR등구조에 따라 인증 연계·전용망·DNS·데이터 복제·일관성·장애상관·출구비용의 요구가 달라집니다. 단순 분산이독립성을보장하지 않습니다.",
        "CMP필수기능은 자원발견·목록, 계정·권한·정책, 프로비저닝·IaC, 비용배부·예산, 성능·로그관측, 보안상태·준수, 백업·수명 관리등입니다. 공통최소기능만 사용할지제공자고유기능을 허용할지운영 정책을 정합니다.",
        "선정은지원 API·가시성·정책 실행력·연동·확장성·플랫폼자체가용성·이관성·총비용을 실제 시나리오로 검증합니다. 통합 관리자의 권한집중과비밀저장소는큰공격 표면이 므로 분리·감사·비상접속을설계해야합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "멀티클라우드",
            "여러 제공자 활용",
            "도구·계약·기술 중복"
          ],
          [
            "하이브리드",
            "서로 다른 배포 환경결합",
            "온프레미스·클라우드 경계"
          ],
          [
            "CMP",
            "관리와 정책통합",
            "고유기능차이·관리면집중"
          ]
        ]
      },
      "example": {
        "title": "두 CSP의 운영 통제",
        "input": "CSPA웹서비스, CSPB분석;공통 비용·권한 정책필요",
        "steps": [
          "공통태그와업무 소유자·데이터등급을정합니다.",
          "계정연합과최소 권한을 구성하되제공자별권한 모델차이를기록합니다.",
          "CMP에서미태깅·과다 권한·예산초과를찾고실제 조치를검증합니다.",
          "공급자장애·CMP장애시독립운영과 복구 절차를 시험합니다."
        ],
        "result": "화면통합보다자원 책임·정책 실행·복구 가능성을성과로평가합니다.",
        "caution": "NIST 클라우드정의는기본배경만지원합니다.CMP특정 제품 원문·멀티클라우드세부규격은 미열람입니다."
      },
      "answer_outline": [
        "필요성·목적",
        "구조·요구사항",
        "CMP기능",
        "선정기준",
        "이관·운영비"
      ],
      "pitfalls": [
        "멀티클라우드가 자동으로vendorlock-in을 없앤다고하지 않습니다.",
        "모든 데이터를 동기 복제하는설계를 기본 값으로 두지않습니다."
      ],
      "recall": [
        "둘의장애가 같이날수 있는 공통의 존성은무엇입니까?",
        "CMP의최소3기능은 무엇입니까?",
        "고유기능과 이관성의절충은 어떻게판단합니까?"
      ],
      "source_ids": [
        "sys-cloud",
        "sys-terraform"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "135-3-3",
          "items": [
            "멀티클라우드 개념·필요",
            "시스템 요구",
            "주요 기술"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-3-2",
          "items": [
            "CMP정의·필요",
            "필수기능",
            "선정·효과"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "cloud-security-assurance",
      "title": "클라우드 도입 보안·아웃소싱·CSAP",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "사업자가 받은 인증과 이용자가 안전하게 설정·운영하는 일은 구분하여, 계약에 서 종료와 복구까지 확인합니다.",
      "definition": "클라우드보안은공유책임 환경에 서 데이터·신원·워크로드·관리면·연결망을보호하고 제공자 위험을 관리하는 활동입니다. 공공부문 이용은 CSAP등해당제도와 보안성 검토·데이터등급·서비스 계약을 함께 검토해야합니다.",
      "principles": [
        "사전단계는 업무·정보등급·법적이용 근거·위험을 분석하고 서비스 모델·배치·데이터위치·운영 책임을 결정합니다. 설계는 망연결·인증·암호 키·로그·백업·관리자접속·취약점·사고통지·공급망을포괄합니다. 구축뒤구성검증·이관·복구·부하시험으로 전환을판단합니다.",
        "아웃소싱계약에 는 보호 목표·접근 권한·하도급·사고 대응·감사권·가용성 측정·복구·데이터 반환·삭제 증빙·계약 종료를 명시합니다. 제공자 장애와 사업중단·가격·종속·국외이전위험도 관리합니다. 암호화시제공자 권한과 키 소유·회전·복구 경로를 따로확인합니다.",
        "CSAP는 적용 서비스·범위·인증 상태를 확인해야 하며 IaaS인증이 그위의모든 SaaS까지자동인증하는것은아닙니다. 공공이용4가 지구조, 유형별평가 항목·점수·절차, 공공SaaS가 이드및금융SLA의 세부의무는 최신 원문을 읽기전확정하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "제공자보안",
            "시설·서비스 기반 보호",
            "인증 범위·책임 확인"
          ],
          [
            "이용자보안",
            "데이터·권한·설정·업무",
            "서비스 모델별경계"
          ],
          [
            "보증·계약",
            "측정·감사·사고·종료",
            "통제 실효성·증빙"
          ]
        ]
      },
      "example": {
        "title": "공공 SaaS 전환 검토",
        "input": "민감업무 정보를 처리하는문서협업서비스 가정",
        "steps": [
          "처리 정보와 외부 연계·국외저장여부를분류합니다.",
          "인증서의 서비스명·범위·유효상태와 별도 보안검토 요구를 확인합니다.",
          "관리 권한·로그반출·백업 복원·계약 종료시표준형식반환을실제 시험합니다.",
          "잔여위험과 예외를 업무 책임자가 승인하고 재평가 주기를 둡니다."
        ],
        "result": "기술 검토와 공급자·계약·철수위험을 한목록으로 추적합니다.",
        "caution": "이번조사는제도세부원문을 충분히확보하지못했습니다.일반 설계예시를법정인증 요건충족으로사용하면 안됩니다."
      },
      "answer_outline": [
        "도입수명 주기",
        "공유책임도",
        "보안요소",
        "CSP실사·계약",
        "CSAP 확인 범위"
      ],
      "pitfalls": [
        "제공자보안인증을 이용자준수전체로간주하지 않습니다.",
        "계약 종료·삭제 증빙을누락하지 않습니다."
      ],
      "recall": [
        "서비스 모델이 바뀌면책임은 어떻게달라집니까?",
        "관리면·데이터면보호를 왜분리합니까?",
        "반환·삭제 시험을 언제합니까?"
      ],
      "source_ids": [
        "sys-cloud",
        "sys-isms"
      ],
      "validation": "부분 확인",
      "version_note": "일반 보안원리는 설명했으나CSAP 평가 기준·공공SaaS·금융SLA가 이드전문 미열람.해당소요구는 확인필요로유지.",
      "requirements": [
        {
          "question": "128-2-2",
          "items": [
            "활용 절차·설계",
            "4활용 구조·CSAP 절차",
            "유형·평가 기준"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "129-4-6",
          "items": [
            "아웃소싱요구",
            "리스크고려·대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-4-3",
          "items": [
            "도입보안요소"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "134-2-1",
          "items": [
            "위험 원칙",
            "보안대책·검토",
            "SLA"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-3-6",
          "items": [
            "금융클라우드 SLA가 이드의보안맥락"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "storage-architecture",
      "title": "블록·파일·오브젝트 스토리지와 가상화",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "작은 주소 단위로 읽고 쓸지, 폴더와 파일로 공유할지, 메타데이터를 가진 객체로 저장할지 업무 접근 방식에 맞춥니다.",
      "definition": "블록스토리지는주소를 가진고정단위공간을, 파일스토리지는계층형경로와 파일공유인터페이스를, 오브젝트스토리지는식별자·본문·메타데이터를 API로 다루는 저장 방식입니다. 스토리지가상화는여러 물리저장 자원을 논리볼륨·풀로추상화합니다.",
      "principles": [
        "블록은 호스트파일시스템이나 DB가 구조를 관리하며 낮은 지연의 임의I/O에맞춥니다. 파일은NFS/SMB등으로여러 사용자가 경로·권한·잠금을 공유합니다. 오브젝트는대규모 비정형 데이터·버전·수명 주기·API에 유리하지만일반 블록 장치의 제자리수정·POSIX의미와 동일하지 않습니다.",
        "선정은IOPS·처리량·p95지연·객체/파일크기·동시성·일관성·접근 권한·내구성·복구·비용으로 판단합니다. 현대서비스의 일관성은제품별로 확인하며 오브젝트는무조건 최종일관성이라고외우지않습니다.",
        "가상화는호스트·스토리지컨트롤러·네트워크 계층등에매핑을두며풀링·씬프로비저닝·마이그레이션을돕습니다. 인밴드는제어·데이터 경로가 가상화장치를 지나고아웃오브밴드는메타데이터제어와실제 I/O경로를 분리하는방식으로 설명할 수 있습니다. 메타데이터·가상화계층 가용성도 보호합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "블록",
            "주소·랜덤I/O",
            "DB·VM 디스크"
          ],
          [
            "파일",
            "경로·공유·파일권한",
            "공동작업·POSIX워크로드"
          ],
          [
            "오브젝트",
            "객체ID·API·메타데이터",
            "학습 원본·백업·대규모 비정형"
          ]
        ]
      },
      "example": {
        "title": "AI 학습 저장 계층",
        "input": "원본영상100TB, 공동라벨링, 학습 캐시, 메타DB",
        "steps": [
          "원본·버전은 오브젝트에보관하고 수명 정책을 둡니다.",
          "협업도구의 파일의미 요구가 있으면 파일서비스를 사용합니다.",
          "학습중빈번한읽기는 로컬/병렬캐시로 완화합니다.",
          "트랜잭션메타DB는 지연·복구 요구에 맞는블록 계층을 검토합니다."
        ],
        "result": "저장형식하나를모든 워크로드에 강제하지 않고접근패턴별로조합합니다.",
        "caution": "분류는 접근추상화이며 실제성능·일관성·최저비용은 제품실측과계약을 확인합니다."
      },
      "answer_outline": [
        "세접근도 식",
        "비교표",
        "I/O요구 분석",
        "가상화위치·유형",
        "AI예"
      ],
      "pitfalls": [
        "오브젝트를폴더없는 파일시스템하나로만설명하지 않습니다.",
        "가상화계층의 장애·풀고갈을누락하지 않습니다."
      ],
      "recall": [
        "DB에 블록이 자주맞는이유는무엇입니까?",
        "오브젝트와POSIX파일의의미차이는무엇입니까?",
        "씬프로비저닝은어떤고갈위험이 있습니까?"
      ],
      "source_ids": [
        "sys-storage"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "132-1-12",
          "items": [
            "세스토리지접근 방식"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-3-5",
          "items": [
            "블록·파일·오브젝트비교",
            "최적활용"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "134-1-10",
          "items": [
            "스토리지가상화유형"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "availability-ft-ha",
      "title": "FTS와 HA·장애 격리",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "고장을 서비스 중단 없이 견디는 설계와 고장 뒤 다른 구성 요소로 빨리 전환하는 설계의 비용·중단 차이를 봅니다.",
      "definition": "FTS는 일부구성 요소고장에도 정의된서비스를 계속제공하도록내결함성을갖춘시스템입니다. HA는 중복·탐지·전환·복구로 비가용시간을 줄이는설계·운영 목표이며 제품명칭만으로둘의경계를 확정할수는없습니다.",
      "principles": [
        "FT구현에 는 하드웨어 중복·잠금 단계 실행·다수결·오류 정정·고장격리등이 있습니다. 무엇을복제하고 어떤고장을 가정하는지명시해야공통 모드실패와범위를 판단할 수 있습니다. 모든 소프트웨어버그·데이터손상을자동으로막는것은아닙니다.",
        "HA클러스터는상태 검사·heartbeat·멤버십·정족수·fencing·자원재시작을 통해 전환합니다. 두노드가 자신을주로판단하는split-brain은 이중쓰기와 손상을만들수 있어실패노드의 접근을 차단하고 쓰기 소유권을 보호합니다.",
        "가용률은정의된관측 시간중서비스가 능시간의 비율입니다. MTBF/(MTBF+MTTR)는단순 정상상태모형이며 측정창·계획중단·사용자관점·부분장애를 구분합니다. 노드 중복만 아니라망·전원·DNS·인증·스토리지같은 공통의 존성을점검합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "FTS",
            "고장중에도서비스연속성지향",
            "중복·검증 비용"
          ],
          [
            "HA",
            "탐지·전환·복구로 중단단축",
            "전환지연·상태 동기"
          ],
          [
            "DR",
            "장소·재난 범위 복구",
            "데이터 시점·업무 복구"
          ]
        ]
      },
      "example": {
        "title": "이중화 DB의 망 분할",
        "input": "두노드A/B간heartbeat단절;각자접속가능",
        "steps": [
          "정족수와외부witness등정해진 정책으로 쓰기 주체를 결정합니다.",
          "비주노드가 스토리지에계속쓰기못하도록fencing을 적용합니다.",
          "클라이언트전환과미완료트랜잭션복구를 검증합니다.",
          "분할 복구후중복 쓰기·데이터일관성과재합류절차를 점검합니다."
        ],
        "result": "서버생존보다한명의정당한 쓰기 주체와 업무정상성을확인합니다.",
        "caution": "HA제품 공식 원문 접근이 실패하여 fencing세부명령·FTS제품 구현은 직접 검증하지못했습니다."
      },
      "answer_outline": [
        "고장 모델·정의",
        "FTS/HA비교",
        "탐지·정족수·fencing",
        "가용지표",
        "시험"
      ],
      "pitfalls": [
        "Active-Active면항상 무중단이라고쓰지않습니다.",
        "heartbeat실패를곧노드완전정지로단정하지 않습니다."
      ],
      "recall": [
        "split-brain은 왜데이터 문제입니까?",
        "정족수와fencing은 각각 무엇을막습니까?",
        "HA와DR의고장 범위는 어떻게다릅니까?"
      ],
      "source_ids": [
        "sys-dr"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "138-3-4",
          "items": [
            "FTS구현",
            "HA구현",
            "FTS·HA비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-2-1",
          "items": [
            "오픈소스 DB전환의HA구성"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "disaster-recovery-rto-rpo",
      "title": "RTO·RPO와 Active-Active·Passive·Pilot Light",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "언제까지 서비스를 다시 열지와 어느 시점의 데이터까지 잃어도 되는지는 서로 다른 목표입니다.",
      "definition": "RTO는 중단후허용하는복구 시간 목표이고 RPO는 복구해야할데이터 시점의 목표로 통상허용손실 시간폭으로표현합니다. BIA로업무 영향·의존성·우선순위를정한 뒤데이터 복제와 실행 환경준비 수준을선택합니다.",
      "principles": [
        "Active-Active는 여러 사이트가평상시요청을 처리합니다. 장애지역트래픽 우회·잔여용량·데이터 충돌·분산일관성·공통의 존성이핵심입니다. 멀티리전이라는이름만 으로RTO/RPO0을 보장하지 않으며데이터 오염은 복제되어 별도 시점 백업이 필요합니다.",
        "Active-Passive는 주사이트만처리하고 대기는장애 전환후처리합니다. hot/warm/cold등준비 수준에따라 기동·확장·복원 시간이 달라집니다. Pilot Light는 복제 데이터와 핵심 기반은 가동하되응용등추가 자원기동·배포·확장이필요하므로 작은 용량으로 즉시처리하는warm standby와 다릅니다.",
        "복구에 는 선언·탐지·결정·DB승격·자원확장·DNS/경로전환·인증·검증 시간이 포함됩니다. 복제 지연관측·백업 복원·장애훈련·failback·정합성 검사를 수행하고 목표와 실제 측정 결과를 분리합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "Active-Active",
            "모든 지역평시처리",
            "비용·쓰기 충돌·잔여용량"
          ],
          [
            "Active-Passive",
            "대기지역전환후처리",
            "대기준비 수준별시간차"
          ],
          [
            "Pilot Light",
            "핵심 데이터·기반만 가동",
            "응용기동·확장선행필요"
          ],
          [
            "Warm Standby",
            "작은 규모전체가동",
            "즉시제한처리후확장"
          ]
        ]
      },
      "example": {
        "title": "복구 목표 검증",
        "input": "장애10:00, 서비스 복구10:25, 최종복구 데이터09:57;목표 RTO30분/RPO5분",
        "steps": [
          "실제 복구 시간은 25분입니다.",
          "복구 데이터 손실폭은3분입니다.",
          "25<=30, 3<=5로이번훈련은두목표를 충족합니다.",
          "다만 오염사고·자격증명 침해·전체 리전손실등다른 시나리오도 시험합니다."
        ],
        "result": "시간 목표와 데이터 시점을 독립적으로평가합니다.",
        "caution": "명시 시각은가상훈련예이며 제품보장값이 아닙니다.복제는 백업의 대체물이아닙니다."
      },
      "answer_outline": [
        "BIA·목표정의",
        "RTO/RPO 시간축",
        "세전략구조비교",
        "계산·훈련",
        "failback·오염 복구"
      ],
      "pitfalls": [
        "RPO를 서비스 복구에 걸리는시간이라 쓰지않습니다.",
        "Pilot Light를 작은 서비스가 항상 처리중인상태로 설명하지 않습니다."
      ],
      "recall": [
        "RTO가 짧아도RPO가 길수 있습니까?",
        "Pilot Light와Warm Standby의차이는무엇입니까?",
        "Active-Active에도백업이 필요한 이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-dr"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "133-1-9",
          "items": [
            "BCP지표",
            "DRS고려사항"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "137-3-3",
          "items": [
            "멀티리전AA개념·특징",
            "주요 기술"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "140-3-1",
          "items": [
            "RTO·RPO",
            "Active-Active·Active-Passive·Pilot Light"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "ai-data-center-platform",
      "title": "AI 데이터센터·슈퍼컴퓨팅·DCI·입지·규모산정",
      "domain": "클라우드·인프라",
      "aliases": [],
      "easy": "GPU를 많이 놓는 것만으로 AI센터가 되지 않으며 계산·메모리·통신·전력·냉각이 함께 지속 처리량을 결정합니다.",
      "definition": "AI데이터센터는대규모AI학습·추론을 위한가속기·고속망·저장·전력·냉각·운영체계를통합한시설입니다. AI슈퍼컴퓨팅플랫폼은 이자원을 워크로드스케줄링·분산학습·개발 도구와 연결하여 제공하는 시스템입니다.",
      "principles": [
        "학습은 가속기간AllReduce·모델/파이프라인병렬통신과 체크포인트I/O가 병목이 되기쉽습니다. HBM·GPU간링크·RDMA네트워크·병렬스토리지·데이터 캐시·스케줄러·관측을함께 설계합니다. 추론은 토큰 처리량·첫토큰 지연·동시성·KV캐시·배치절충을 측정합니다.",
        "전통HPC는 범용과학계산과 정밀도요구, 클라우드는 탄력적서비스제공, AI플랫폼은 텐서연산과 대규모 학습·추론이 주요 강점입니다. 서로 배타적인분류는 아닙니다. 고밀도랙은전력공급·UPS·배전·액체냉각·열관리·소방·유지보수동선을요구합니다.",
        "DCI는 센터간데이터·서비스 연결로 광전송·라우팅·암호화·대역·지연·경로다양성을고려합니다. 입지는지진·홍수·전쟁·전력·통신·물·인력·규제·거리별공통 재난을 분석합니다. 규모는 업무량·동시성·성능 측정·성장·장애시잔여용량으로 산정하며 공식TTA산식은판본 원문 확인이 필요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "전통HPC",
            "과학계산·정밀도·MPI",
            "문제별메모리·통신"
          ],
          [
            "클라우드",
            "서비스·탄력·과금",
            "제공 계층·책임·비용"
          ],
          [
            "AI플랫폼",
            "텐서·분산학습·추론",
            "가속기·HBM·데이터·전력"
          ]
        ]
      },
      "example": {
        "title": "지역 상실을 가정한 AI 서비스",
        "input": "2센터평시각40%부하;한센터전체 중단대비",
        "steps": [
          "한센터에서전체80%를수용할 수 있는 지연산·망·전력을 검증합니다.",
          "학습배치는중단가능성·체크포인트시점으로 재개전략을둡니다.",
          "추론은 모델 복제·캐시워밍·트래픽 우회지연을 측정합니다.",
          "두센터가같은 변전소·통신관로·재난권역에의존하는지확인합니다."
        ],
        "result": "명목 장비 수보다실제 종단성능과 장애후수용력을확인합니다.",
        "caution": "NVIDIA설계가 이드접근실패·TTA0292/R3전문 미열람.구체규모계수·의무입지거리·제품숫자는미확인입니다."
      },
      "answer_outline": [
        "등장배경",
        "구성 요소도식",
        "세플랫폼비교",
        "네트워크·DCI",
        "입지·가용성·산정"
      ],
      "pitfalls": [
        "대역폭과 지연을 동일지표로 쓰지않습니다.",
        "두센터면공통 재난이 없다고가정하지 않습니다."
      ],
      "recall": [
        "AllReduce의통신 병목은 왜중요합니까?",
        "고밀도전력과 냉각은 어떻게연결됩니까?",
        "재해센터입지에거리하나만쓰면왜부족합니까?"
      ],
      "source_ids": [
        "sys-tpu",
        "sys-cxl",
        "sys-dr"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "134-2-4",
          "items": [
            "저지연·스케일링",
            "DCI"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "134-4-2",
          "items": [
            "멀티GPU 개념·장점",
            "구축고려"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "139-4-3",
          "items": [
            "IDC지리적위치선정",
            "재난 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-2-4",
          "items": [
            "AI슈퍼컴퓨팅정의·배경",
            "구성역할",
            "HPC·Cloud비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-4-6",
          "items": [
            "AI센터정의·배경",
            "기존 센터비교",
            "핵심 기술"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "133-2-1",
          "items": [
            "HW규모산정개념·대상",
            "절차",
            "방식"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "access-control-models-ldap",
      "title": "접근 통제 정책·보안모델·LDAP",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "로그인에 성공한 사람도 모든 자료를 볼 수 있는 것은 아니며, 업무·등급·속성에 따라 허용행위를 다시 결정합니다.",
      "definition": "접근 통제는 주체가 객체에 수행할 행위를 정책과 조건에 따라 허용·거부하는 기능입니다. 식별·인증 → 인가 결정 → 정책집행 → 감사의 절차로 설명하고 보안모델의 보호 목표를 구분합니다.",
      "principles": [
        "DAC는 소유자의 재량, MAC는 중앙의 등급·레이블, RBAC는 역할과 권한, ABAC는 주체·객체·행위·환경 속성과 정책을 중심으로 결정합니다. 최소 권한·직무 분리·기본거부·정기회수와 정책 결정/집행 분리가 중요합니다.",
        "BLP는 기밀성을 위한no read up/no write down, Biba의 엄격모델은 무결성을 위한no read down/no write up으로설명합니다. Clark-Wilson은 인증된변환절차·무결성 검증·제약자료·직무 분리로 상업적무결성을 관리합니다. 목적·허용정보 흐름을 반대로쓰지않습니다.",
        "LDAP는 디렉터리접근 프로토콜이며 인증은 Bind로수행합니다. TLS 서버 검증 → 필요시서비스 계정검색 → 사용자DN확인 → 사용자 인증Bind → 권한속성조회·인가로 구성할 수 있습니다. 평문simpleBind·빈암호의 익명/비인증 의미·과다검색권한을 주의합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "BLP",
            "기밀성;상향읽기·하향쓰기금지",
            "비밀의낮은 등급유출방지"
          ],
          [
            "Biba",
            "무결성;하향읽기·상향쓰기금지",
            "오염된정보의 전파방지"
          ],
          [
            "Clark-Wilson",
            "정당한 거래·직무 분리",
            "승인변환절차와 감사"
          ]
        ]
      },
      "example": {
        "title": "급여 수정 권한",
        "input": "인사입력자·승인자·감사자를분리",
        "steps": [
          "입력자는초안수정만 하고 승인자는본인입력을 승인하지못합니다.",
          "정당한 변환API만 급여자료를 갱신하게합니다.",
          "무결성 검사와 감사 로그로 이상변경을 확인합니다.",
          "인증 성공과급여수정 인가를 독립평가합니다."
        ],
        "result": "역할·절차·감사로업무 불변조건을 유지합니다.",
        "caution": "LDAP·ABAC는 공식 자료 확인;BLP/Biba/CW원논문전문은 미열람입니다."
      },
      "answer_outline": [
        "정의·절차",
        "DAC/MAC/RBAC/ABAC",
        "3보안모델",
        "LDAP 흐름",
        "정책집행·감사"
      ],
      "pitfalls": [
        "인증과 인가를 동의어로쓰지않습니다.",
        "BLP와 Biba 읽기방향을혼동하지 않습니다."
      ],
      "recall": [
        "BLP가 낮은 등급쓰기를 막는이유는무엇입니까?",
        "ABAC의환경속성예는무엇입니까?",
        "LDAPBind성공이업무 인가를 보장합니까?"
      ],
      "source_ids": [
        "sys-ldap",
        "sys-abac"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "127-2-6",
          "items": [
            "BLP",
            "Biba",
            "Clark-Wilson"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "129-2-2",
          "items": [
            "통제 정책",
            "LDAP 인증 흐름"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "133-4-3",
          "items": [
            "접근제어개념·정책·절차·메커니즘"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "identity-authentication-nhi",
      "title": "식별·인증·비인간 신원 NHI",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "누구라고 주장하는지와 그 주장을 어떻게 입증하는지, 어떤 권한을 언제 회수할지를 사람과 소프트웨어 모두에 적용합니다.",
      "definition": "식별은계정·식별자등으로주체를 구별하는절차이고 인증은 주체가 제시한인증 수단을 검증하는절차입니다. NHI는 서비스·애플리케이션·장치등비인간개체의신원으로, 워크로드신원과장치신원을포함할 수 있습니다.",
      "principles": [
        "지식기반 비밀번호, 소유기반보안키·토큰, 생체기반 특성은 서로 다른 인증요소입니다. 위치·행동은 맥락·위험신호로이용할 수 있지만독립요소라는분류는 문헌별차이가있습니다. 동일종류비밀두개를쓰는것만으로MFA가 되지않습니다.",
        "인증 요구는 도청·재전송·피싱·온라인추측·복구 경로·세션 탈취와 등록·변경·폐기를 포함합니다. 생체정보는 변경이 곤란하고 확률적오류가 있어단독비밀처럼취급하지 않습니다. 강한인증뒤세션과 인가도 보호해야합니다.",
        "NHI는 API 키·인증서·서비스 계정·관리형신원등으로자원에 접근합니다. 수량·소유자불명·장기비밀·과다 권한·CI로그 노출·폐기누락이취약점입니다. 목록·책임자·짧은수명 토큰·워크로드연합·최소 권한·회전·사용감시·자동폐기로 통제합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "사람신원",
            "직원·고객·사용자",
            "MFA·접속맥락·퇴사회수"
          ],
          [
            "워크로드신원",
            "앱·배치·컨테이너",
            "토큰·역할·실행 환경 검증"
          ],
          [
            "장치신원",
            "서버·IoT·단말",
            "인증서·보안상태·등록 폐기"
          ]
        ]
      },
      "example": {
        "title": "CI 파이프라인 자격증명",
        "input": "배포 작업에 운영 환경 접근필요",
        "steps": [
          "저장소에장기관리자 키를 두지않고신뢰된실행 주체가 짧은토큰을 받게합니다.",
          "대상 환경과 브랜치등신뢰 조건을 검증합니다.",
          "배포에 필요한 권한만 부여하고 세션·변경을 기록합니다.",
          "프로젝트종료시신원·연합관계·권한을 회수합니다."
        ],
        "result": "비인간접근도 생성부터폐기까지 책임을 추적합니다.",
        "caution": "비밀번호 정책·보안등급은적용 표준과 업무 요건별확인이 필요합니다."
      },
      "answer_outline": [
        "식별·인증·인가",
        "인증요소비교",
        "생애주기 요구",
        "NHI 취약점",
        "워크로드예"
      ],
      "pitfalls": [
        "API 키를 사용자 비밀번호보다 덜민감하게보지않습니다.",
        "생체값이 완전히정확하고 회수가 능하다고하지 않습니다."
      ],
      "recall": [
        "식별자와인증비밀의차이는무엇입니까?",
        "NHI의 소유자를 정해야 하는이유는무엇입니까?",
        "같은 종류두인증 값은 왜MFA가 아닐수 있습니까?"
      ],
      "source_ids": [
        "sys-identity",
        "sys-nhi"
      ],
      "validation": "부분 확인",
      "version_note": "NIST800-63B-4(2025-07), Microsoft신원공식 문서.기출의4가 지유형분류원출처미확인;위치·행동을 독립NIST요소로사칭하지 않음.",
      "requirements": [
        {
          "question": "128-4-6",
          "items": [
            "식별·인증정의차이",
            "보안 요구",
            "4유형분류"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-1-11",
          "items": [
            "NHI보안취약점"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "symmetric-asymmetric-aes",
      "title": "대칭·비대칭 암호와 AES",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "많은 데이터를 빠르게 잠그는 열쇠와 낯선 상대에게 안전하게 열쇠·서명을 전달하는 수단을 조합합니다.",
      "definition": "대칭암호는 암·복호에 공유 비밀키를 사용하고 공개 키 암호는 공개 키와 개인키 관계를 이용합니다. 블록 암호는 고정 크기블록변환이며 AES는 128비트블록과 128/192/256비트키를 갖는대칭블록 암호입니다.",
      "principles": [
        "AES는 SubBytes·ShiftRows·MixColumns·AddRoundKey등상태변환과키스케줄을라운드로 결합합니다. 키 길이에따라 10/12/14라운드를 사용하고 최종라운드는 구성차이가있습니다. 블록 크기와키 길이를혼동하지 않습니다.",
        "공개 키 기법은 키 설정·암호화·서명등용도를구분합니다. 큰데이터는 대칭암호로 처리하고 세션 키를 공개 키스킴으로설정하는하이브리드구조가 일반적입니다. 공개 키의 정당성을 인증서·검증 경로등으로확인하지 않으면중간자위험이 남습니다.",
        "안전성은 알고리즘 이름뿐 아니라키 생성·저장·폐기·nonce/IV·패딩·모드·오류반응·부채널·프로토콜결합에좌우됩니다. 암호화만 으로송신자 진위·무결성·부인 방지가동시에보장되지는않습니다. 인증 암호와 키 분리를 검토합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "대칭암호",
            "공유키·고속대량처리",
            "키분배·공유범위"
          ],
          [
            "공개 키 암호",
            "키쌍·서명·키 설정",
            "계산 비용·키 진위"
          ],
          [
            "AES",
            "128비트블록·3키 길이",
            "모드·nonce·키 관리필요"
          ]
        ]
      },
      "example": {
        "title": "하이브리드 파일 전달",
        "input": "큰파일1GB를 수신자한명에게기밀전달",
        "steps": [
          "난수로대칭데이터 키를 만듭니다.",
          "인증 암호로 파일을암호화하고 수신자 공개 키스킴으로데이터 키를 보호합니다.",
          "수신자는 개인키로 키를 복구하고 태그검증뒤평문을 사용합니다.",
          "필요한 송신자증명은별도 서명정책으로 추가 합니다."
        ],
        "result": "대량처리효율과공개 키 기반 키 전달의 장점을연결합니다.",
        "caution": "교육개념이며 직접 설계한암호포맷대신 검증된표준 프로토콜과 라이브러리를 사용합니다."
      },
      "answer_outline": [
        "분류·보안목표",
        "AES 구조·라운드",
        "대칭/비대칭비교",
        "하이브리드예",
        "키·모드 관리"
      ],
      "pitfalls": [
        "AES256의블록이 256비트라고쓰지않습니다.",
        "공개 키 암호를 모두개인키 암호화로 설명하지 않습니다."
      ],
      "recall": [
        "AES의 블록과 키 길이는각각 무엇입니까?",
        "공개 키의 진위를 확인해야 하는이유는무엇입니까?",
        "암호화와 무결성을 분리해야 하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-aes",
        "sys-rsa"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "130-1-6",
          "items": [
            "블록 암호화 알고리즘"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "132-1-4",
          "items": [
            "대칭·비대칭암호화"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "block-cipher-modes",
      "title": "ECB·CBC·CFB·OFB 블록 암호 모드",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "같은 블록 암호도 이전 암호문이나 키스트림을 연결하는 방법에 따라 패턴노출·오류전파·병렬성이 달라집니다.",
      "definition": "운영 모드는 고정 크기블록 암호를 여러 블록메시지에적용하는방법입니다. SP800-38A의ECB/CBC/CFB/OFB는 기밀성 모드이며 변조검출을단독제공하지 않으므로무결성 보호를 별도로결합해야합니다.",
      "principles": [
        "ECB는C_i=E_K(P_i)로같은 평문 블록이 같은 암호문이 되어 패턴이노출됩니다.CBC는C_i=E_K(P_i XOR C_(i-1)), C_0=IV이며 암호화는 연쇄의존하고 복호 블록 연산은 병렬화가능합니다. 패딩과예측불가능한 IV등규격 조건이 중요합니다.",
        "CFB는 이전암호문또는IV를 암호화한출력과 평문을 XOR합니다. OFB는 이전암호기출력을 반복암호화하여 평문과 독립적인 키스트림을 만듭니다. 두 방식은 암호기의정방향연산을 활용하나상태피드백대상·오류전파·동기성이다릅니다.",
        "OFB의동일키·IV재사용은같은 키스트림을 반복하여 C XOR C′=P XOR P′를노출합니다.CBC의IV·CFB세그먼트크기·패딩규칙을 생략하지 않습니다. 현대프로토콜의 AEAD는 암호화와 태그를결합하며 nonce규칙위반에도주의합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "ECB",
            "블록독립",
            "패턴노출;일반 메시지부적합"
          ],
          [
            "CBC",
            "이전암호문XOR",
            "IV·패딩·오류반응"
          ],
          [
            "CFB",
            "암호문피드백",
            "세그먼트·동기·전파"
          ],
          [
            "OFB",
            "출력피드백키스트림",
            "키/IV재사용금지"
          ]
        ]
      },
      "example": {
        "title": "OFB 재사용의 XOR 누출",
        "input": "한바이트장난감예:P=0x12, P′=0x34, 키스트림0xAA재사용",
        "steps": [
          "C=0x12 XOR0xAA=0xB8입니다.",
          "C′=0x34 XOR0xAA=0x9E입니다.",
          "C XOR C′=0x26이며 P XOR P′도0x26입니다.",
          "평문하나를알면다른 평문을 복구할 수 있어같은 키스트림재사용이위험합니다."
        ],
        "result": "모드운용조건의 실패가알고리즘강도와별개로정보를 노출합니다.",
        "caution": "한바이트예는XOR원리 설명이며 실제 AES의 블록 크기는 128비트입니다."
      },
      "answer_outline": [
        "모드필요성",
        "네식·도식",
        "IV·패딩·병렬성비교",
        "재사용계산",
        "AEAD연결"
      ],
      "pitfalls": [
        "모드 이름만 으로인증까지 보장하지 않습니다.",
        "OFB피드백을암호문이라 고그리지않습니다."
      ],
      "recall": [
        "ECB패턴은왜보입니까?",
        "CBC암호화와 복호의 병렬성은 왜다릅니까?",
        "OFB의IV재사용은무엇을노출합니까?"
      ],
      "source_ids": [
        "sys-modes"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "127-4-6",
          "items": [
            "ECB",
            "CBC",
            "CFB",
            "OFB"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "hash-mac-password",
      "title": "해시·MAC·솔트·키 스트레칭",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "해시는 지문, MAC은 비밀키를 가진 이의 지문, 비밀번호 저장은 추측을 느리게 하는 별도의 설계입니다.",
      "definition": "암호학적해시는임의길이입력을 고정길이값으로 매핑하고 역상·제2역상·충돌저항성을목표로 합니다. MAC은 공유키로 메시지무결성과 키 소유자의 인증을 제공하며 HMAC은 해시를안전한 키드구조로 결합합니다.",
      "principles": [
        "일반 해시는비밀이없어공격자가본문과해시를함께 바꾸면진위를 입증하지못합니다.HMAC은 K와ipad/opad를 사용하는 안쪽·바깥쪽해시구조입니다. 공유키를 가진양측모두태그를만들수 있으므로제3자에대한부인 방지는전자서명과다릅니다.",
        "비밀번호는 작은 후보공간탓에단방향해시도추측검사가 가능합니다.RainbowTable은 미리계산한연쇄를활용해시간·메모리를 절충합니다. 계정별서로 다른 무작위솔트는동일비밀번호해시일치를숨기고사전계산재사용을어렵게하지만온라인추측이나약한비밀번호자체를제거하지 않습니다.",
        "키스트레칭은전용비밀번호해싱/KDF의비용 파라미터로 공격자추측 비용을 높입니다. 솔트·해시·알고리즘·비용 버전을 함께 보관하고 로그인시비용상향을지원합니다. 별도 비밀pepper는 솔트와다르며회전·복구 정책이 필요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "일반 해시",
            "비밀없음;지문",
            "원본 진위·기밀성없음"
          ],
          [
            "MAC/HMAC",
            "공유 비밀키",
            "무결성·양자간인증"
          ],
          [
            "비밀번호KDF",
            "솔트·작업 비용",
            "오프라인추측 비용 증가"
          ]
        ]
      },
      "example": {
        "title": "같은 비밀번호의 저장 비교",
        "input": "A/B가 같은 비밀번호사용;솔트sA≠sB",
        "steps": [
          "동일한 단순 해시이면두계정의 결과가 같습니다.",
          "KDF(password, sA, cost)와KDF(password, sB, cost)는서로 다르게계산됩니다.",
          "공격자는각솔트의후보계산을 다시해야합니다.",
          "온라인속도제한·피싱 대응·MFA도 함께 적용합니다."
        ],
        "result": "저장 보호와 온라인인증 보호의 다층관계를 설명합니다.",
        "caution": "빠른SHA함수를 반복횟수 없이비밀번호 저장에 그대로쓰는것은적절하지 않습니다."
      },
      "answer_outline": [
        "해시성질",
        "MAC와 서명비교",
        "RainbowTable",
        "솔트·스트레칭",
        "운영 정책"
      ],
      "pitfalls": [
        "해시는복호하는암호가 아닙니다.",
        "솔트를숨겨야만안전한 비밀키로 설명하지 않습니다."
      ],
      "recall": [
        "충돌과 역상은어떻게다릅니까?",
        "HMAC에 부인 방지가없는 이유는무엇입니까?",
        "솔트가있어도 약한비밀번호가 위험한이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-hmac",
        "sys-identity"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "127-1-5",
          "items": [
            "메시지인증 코드"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "138-4-2",
          "items": [
            "단방향해시문제",
            "RainbowTable",
            "Salt·Stretching",
            "활용"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "127-1-9",
          "items": [
            "변조와위조구분"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "rsa-dsa-ecc-envelope",
      "title": "RSA·DSA·ECC와 전자봉투",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "암호화·서명·키 설정은 같은 공개 키 수학을 쓰더라도 목적과 안전한 포맷이 다릅니다.",
      "definition": "RSA는 모듈러거듭제곱과정수인수분해난점에기반한 공개 키계열이며 DSA는 이산로그 기반서명알고리즘입니다. ECC는 타원곡선군에서의이산로그난점을이용하는계열로ECDH·ECDSA등을 포함합니다. 전자봉투는대칭암호문과 수신자용으로보호한데이터 키를 묶습니다.",
      "principles": [
        "RSA는 n=pq, 공개지수e, 비밀지수d를 구성하지만실제 암호화·서명에는OAEP·PSS등검증된인코딩이필요합니다. 원시RSA의 작은 정수예를그대로안전한 실무암호라하면 안됩니다.",
        "DSA/ECDSA의 서명nonce재사용·편향은개인키를 노출할 수 있습니다.FIPS186-5는DSA신규서명생성을승인하지 않고기존 서명검증을 허용합니다. 2022기출의원리비교와현행 선택권고를구분합니다. ECC의 짧은키는 동일보안수준의적절한 곡선·파라미터비교조건에 서 판단합니다.",
        "전자봉투생성은난수데이터 키 → 대칭암호화 → 수신자 공개 키로 키 보호 → 알고리즘·수신자 정보와 패키징입니다. 개봉은개인키로 키 복구 → 암호문 인증·복호입니다. 기밀 봉투만으로송신자의 서명이자동생성되지는않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "RSA",
            "암호화·서명스킴",
            "OAEP/PSS·키 길이·인증"
          ],
          [
            "DSA",
            "서명전용",
            "nonce·구판현행구분"
          ],
          [
            "ECC",
            "ECDH·ECDSA등계열",
            "곡선·검증·nonce"
          ]
        ]
      },
      "example": {
        "title": "RSA 장난감 계산 검산",
        "input": "p3, q11, n33, φ20, e3, d7;평문m4",
        "steps": [
          "e×d=21≡1(mod20)입니다.",
          "암호문c=4³ mod33=64 mod33=31입니다.",
          "복호31⁷ mod33=4입니다.",
          "실제 암호는 큰키와 안전한 패딩·난수·검증을 사용합니다."
        ],
        "result": "암·복호의 수학관계를 확인하고 스킴수준보안을별도로설명합니다.",
        "caution": "작은 p/q와textbookRSA는 보안용으로사용하지 않습니다."
      },
      "answer_outline": [
        "세계열비교",
        "키·서명원리",
        "전자봉투양방향도식",
        "정수계산",
        "현행 DSA 상태"
      ],
      "pitfalls": [
        "DSA를 기밀암호화 알고리즘이라 쓰지않습니다.",
        "서명을개인키 암호화의 단순 역연산으로 만설명하지 않습니다."
      ],
      "recall": [
        "전자봉투의본문과키는 각각 어떻게보호합니까?",
        "DSA와 RSA의 기능차이는무엇입니까?",
        "nonce재사용은왜치명적입니까?"
      ],
      "source_ids": [
        "sys-rsa",
        "sys-signature",
        "sys-ecc",
        "sys-cms"
      ],
      "validation": "출처 확인",
      "version_note": "FIPS186-5본문 16쪽DSA 상태 확인;RSA31⁷mod33=4는Pythonpow로직접 검산.",
      "requirements": [
        {
          "question": "126-4-5",
          "items": [
            "RSA·DSA비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "133-1-4",
          "items": [
            "전자봉투생성·개봉"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "136-1-12",
          "items": [
            "ECC"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "tls13",
      "title": "TLS1.2 구조와 TLS1.3 개선",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "서로의 신원과 공유키를 합의한 뒤 데이터를 인증 암호로 보호하며, 예전 기능을 제거해 공격 여지를 줄입니다.",
      "definition": "TLS는 전송위에서기밀성·무결성·상대인증을 제공하는 프로토콜입니다. 핸드셰이크로버전·알고리즘·키 자료·서버신원을확인하고 기록 계층에서 협상된키로 응용 데이터를 보호합니다.",
      "principles": [
        "TLS1.3기본 흐름은 ClientHello(key_share등) → ServerHello → 암호화된확장·인증서·CertificateVerify·Finished → 클라이언트Finished입니다. 일반적으로왕복을줄이고PSK재개·선택적클라이언트 인증을 지원합니다. 인증서체인·호스트명·유효상태 검증이 필요합니다.",
        "TLS1.3은 구식키교환·CBC등많은구형선택지를 제거하고 AEAD및HKDF기반 키스케줄을사용합니다. 인증서서명알고리즘과 키교환·레코드 암호를 별개로협상합니다. 정상적인현행 설정의 TLS1.2전체를이미암호해독가능하다고단정하지 않습니다.",
        "0-RTT조기데이터는 지연을 줄이지만 재전송 위험이 있어송금·중복불가행위에 는 별도 방어없이지정하지 않습니다. 핸드셰이크성공뒤에도응용 인가·쿠키·로그·키보관·종단취약점은 남습니다. 전방향안전성은 사용키교환 방식과 운영 조건을 확인합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "TLS1.2",
            "다양한레거시선택 지원",
            "안전한 설정·패치필요"
          ],
          [
            "TLS1.3",
            "단순 화·AEAD·왕복축소",
            "호환성·검사체계변화"
          ],
          [
            "0-RTT",
            "조기응용 데이터",
            "재전송 위험·업무 멱등성"
          ]
        ]
      },
      "example": {
        "title": "조기 데이터와 중복 송금",
        "input": "재개세션에 서 송금POST를0-RTT로허용하는가정",
        "steps": [
          "네트워크 공격자가조기데이터를 재전송할가능성을위협 모델에 넣습니다.",
          "송금은조기데이터로 받지않거나멱등키·중복 검사를 강제합니다.",
          "인증완료와업무 권한을 검증후원장에 한번만반영합니다.",
          "읽기 요청이라 도부수효과·민감도·재전송 안전을 검토합니다."
        ],
        "result": "프로토콜개선의지연이 익과업무 정합성 위험을 분리합니다.",
        "caution": "제품별TLS 설정과 지원 알고리즘은 버전별공식 문서를 확인해야합니다."
      },
      "answer_outline": [
        "구조",
        "핸드셰이크시간축",
        "1.2위험·1.3개선",
        "0-RTT",
        "인증 검증·운영"
      ],
      "pitfalls": [
        "TLS1.2의모든 구성이취약하다고쓰지않습니다.",
        "암호화면인가가 불필요하다고보지않습니다."
      ],
      "recall": [
        "TLS1.3이 제거한레거시기능의 의미는 무엇입니까?",
        "CertificateVerify와Finished의역할은어떻게다릅니까?",
        "0-RTT에송금을허용하기어려운이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-tls"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "136-2-6",
          "items": [
            "TLS 구조·핸드셰이크",
            "TLS1.2취약·1.3개선"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "vpn-tor",
      "title": "IPsec·TLS VPN과 Tor",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "터널이 보호하는 두 끝과, 익명 경로가 숨기는 관계를 구별하고 종단과 제공자에 남는 신뢰를 봅니다.",
      "definition": "VPN은 공용망위에논리적사설연결을 만들고정책에 따라 트래픽을보호합니다. IPsec은IP계층에서 보호하고 TLS VPN은 TLS 기반원격접속·응용터널을제공합니다. Tor는 여러 중계노드를 통한계층 암호화로 출발지와목적지관계의 노출을 줄이는익명통신망입니다.",
      "principles": [
        "IPsec은SA로보안관계·알고리즘·키·시퀀스등을 관리하고 SPD는 보호 정책, SAD는SA상태를 관리합니다. ESP는 기밀성·무결성등을 제공할 수 있으며전송 모드와 터널모드의 보호 범위를 구분합니다. 키협상과피어인증·재전송방지도중요합니다.",
        "TLS VPN은 브라우저포털또는에이전트등을 통해 접속하고 사용자·단말·응용수준정책과 연결할 수 있습니다. 실제 보호 범위는 구현·split tunneling·DNS·로컬경로에 따라 달라집니다. 터널종단·인증서·취약한게이트웨이도 보호해야합니다.",
        "Tor는 각중계가일부경로 정보만 알게하여 단일관측점의연계를 어렵게합니다. VPN은 주로단일제공자·게이트웨이에 신뢰를 모으는반면Tor는 다중중계를활용하지만지연·출구관측·종단식별·트래픽상관위험이 남습니다. HTTPS는 출구이후 기밀성에도 중요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "IPsecVPN",
            "IP계층·SA·터널",
            "사이트간·원격접속"
          ],
          [
            "TLS VPN",
            "TLS 기반 응용/네트워크접속",
            "구현별접근 범위"
          ],
          [
            "Tor",
            "계층 암호화·다중중계",
            "익명성 한계·지연"
          ]
        ]
      },
      "example": {
        "title": "원격 업무 접속",
        "input": "직원단말 → VPN 게이트웨이 → 업무 서버",
        "steps": [
          "강한피어·사용자 인증과 단말 상태를 검증합니다.",
          "전체 내부망대신 필요응용만 허용합니다.",
          "터널밖DNS·트래픽경로와 로그의 민감정보를 확인합니다.",
          "게이트웨이패치와세션 회수·감사를정기운영합니다."
        ],
        "result": "터널암호화·인가·종단보호를 함께 다룹니다.",
        "caution": "Tor 사용자라는사실이나VPN사용만으로추적불가능·불법성·합법성을단정하지 않습니다."
      },
      "answer_outline": [
        "VPN정의",
        "IPsec구조",
        "TLS VPN비교",
        "Tor 경로·신뢰",
        "실무제약"
      ],
      "pitfalls": [
        "VPN이 종단악성코드까지 치료한다고쓰지않습니다.",
        "Tor출구부터목적지까지항상 암호화됐다고가정하지 않습니다."
      ],
      "recall": [
        "터널종단은어디입니까?",
        "SPD와SAD는 어떻게다릅니까?",
        "Tor에서도 HTTPS가 중요한이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-ipsec",
        "sys-tor",
        "sys-tls"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-4-4",
          "items": [
            "VPN·Tor"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "133-4-6",
          "items": [
            "VPN정의·특징",
            "IPsec·SSLVPN",
            "기술요소"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "qkd-pqc",
      "title": "양자키분배 QKD와 양자내성암호 PQC",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "빛의 양자 상태로 키를 나누는 장치와, 양자컴퓨터에도 견디도록 설계한 고전 암호 알고리즘을 구분합니다.",
      "definition": "QKD는 양자채널의측정·교란특성을 활용하여 비밀키를 분배하고 고전인증채널의후처리로 키를 확정하는기술입니다. PQC는 고전컴퓨터에서실행하면 서양자공격에 대한내성을목표로 설계한키 설정·서명등암호 알고리즘입니다.",
      "principles": [
        "QKD는 일반적으로양자상태 전송 → 기저등정보교환·sifting → 오류율추정 → 정보정합 → 프라이버시증폭의흐름으로 설명합니다. 도청은오류 통계에 나타날수 있지만인증없는 고전채널의중간자·장치부채널·구현결함·서비스거부는별도 문제입니다.",
        "QKD는 광장치·거리·손실·키 생성률·신뢰중계·위성경로와 환경 조건을 고려합니다. 분배된키로 데이터를 보호하는 대칭암호도 필요합니다. 도감청이 원천적으로어떤형태로도불가능한 완전체 계라는표현은부적절합니다.",
        "NISTFIPS203은 격자문제 기반ML-KEM을 표준화했으며512/768/1024파라미터를 제공합니다. KEM은 공유비밀을설정하고 본문암호는 별도 입니다. PQC도 파라미터·구현·부채널·업데이트와 인증서·프로토콜전환이필요합니다. 전환은자산·알고리즘 목록과 수명·민감기간에 서 시작합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "QKD",
            "양자물리·키분배",
            "장치·광경로·인증고전채널"
          ],
          [
            "PQC",
            "고전수학암호·키 설정/서명",
            "소프트웨어·프로토콜전환"
          ],
          [
            "공통",
            "키 관리·구현 안전성",
            "인증·운영·검증필요"
          ]
        ]
      },
      "example": {
        "title": "장기 기밀문서 보호 전환",
        "input": "오래기밀유지할문서를 전송하는기관 가정",
        "steps": [
          "현재 키교환·서명·인증서·장비를 목록화합니다.",
          "수집후미래복호 위험과 문서민감기간을 분석합니다.",
          "검증된PQC 지원과 호환성을시험하고 필요한 경우하이브리드전환을검토합니다.",
          "QKD는 물리경로·운영비·인증 전제까지 별도로평가합니다."
        ],
        "result": "제품명보다위협 기간과 전환가능성으로우선순위를정합니다.",
        "caution": "QKD원표준 전문은 미열람이며 FIPS203의ML-KEM정의·파라미터만 직접 확인했습니다."
      },
      "answer_outline": [
        "양자위협",
        "두원리도 식",
        "인프라·용도비교",
        "전환절차",
        "QKD 한계"
      ],
      "pitfalls": [
        "QKD와 PQC를 동의어로쓰지않습니다.",
        "ML-KEM을 데이터 암호화·전자서명알고리즘으로 쓰지않습니다."
      ],
      "recall": [
        "QKD에 인증고전채널이필요한 이유는무엇입니까?",
        "PQC가 양자컴퓨터에서실행되는암호입니까?",
        "장기데이터가 전환우선순위에영향을 주는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-pqc"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "128-4-4",
          "items": [
            "키분배",
            "주요 기술",
            "취약점"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "135-3-4",
          "items": [
            "QKD",
            "PQC",
            "비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "security-assurance-tpm-fips-cc",
      "title": "TPM·FIPS140-2·CC·신속확인 제도",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "알고리즘이 강한지, 키를 다루는 모듈이 안전한 지, 제품의 주장한 보안 기능을 평가했는지는 서로 다른 보증 범위입니다.",
      "definition": "TPM은 키 보호·측정 값보관·상태증명등을 지원하는신뢰 기반모듈입니다. FIPS140은 암호모듈보안 요구를, CC는 정의된평가 대상과 보안 요구·보증을 다루며신속확인은 기존 평가 기준이 없는 신기술보안제품의 공공도입을돕는국내 제도입니다.",
      "principles": [
        "TPM은 보호된키와 PCR측정 값을 연결한seal/unseal·attestation등에활용됩니다. 측정된부팅은구성변경의 증거를 제공하지만실행중모든 악성행위를 항상 탐지하는완전무결장치가 아닙니다. 소유권·등록·복구·펌웨어·물리 공격을 고려합니다.",
        "FIPS140-2는 레벨1~4의점증적보증수준을제공합니다. 모듈명세·인터페이스·역할/인증·물리보안·운영 환경·키 관리·자가시험·설계 보증등을 다룹니다. 대체로 1기본 요구, 2tamper-evidence와 역할인증, 3침입방어·신원인증, 4포괄물리보호·환경 대응으로 설명하되수준별전요구는 원문 표를 확인합니다.",
        "CC는TOE·ST·PP와 기능 요구/보증 요구를 구분하며 높은 평가수준이모든 위협에 서 무조건 더안전함을뜻하지 않습니다. 신속확인은 취약점·소스보안약점 점검과 보안성 심사등의 범위를 확인해야 하고 정식CC와 동일인증이라 하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "TPM",
            "키·측정·증명기반",
            "플랫폼 신뢰의 일부"
          ],
          [
            "FIPS140",
            "암호모듈보안",
            "제품·전체 서비스와 범위구분"
          ],
          [
            "CC/신속확인",
            "제품별보안성 보증",
            "대상·판본·유효성확인"
          ]
        ]
      },
      "example": {
        "title": "보안모듈 구매 검토",
        "input": "AES 지원 제품의 공공업무사용가정",
        "steps": [
          "인증서의 모듈명·버전·운영 모드·보안경계를 확인합니다.",
          "승인 알고리즘 지원과 모듈검증을 구분합니다.",
          "키 생성·백업·복구·관리자역할·감사요구를 검토합니다.",
          "실제 배포 버전이 평가 대상과 같은 지검증합니다."
        ],
        "result": "인증 이름보다 적용 범위와 운용조건으로 보증을 판단합니다.",
        "caution": "FIPS140-2구판원문은 확인했으나140-3전환·CC현행 절차·신속확인 최신 요건은 미확인입니다."
      },
      "answer_outline": [
        "보증 계층비교",
        "TPM활용",
        "FIPS 4수준",
        "CC핵심 용어",
        "도입확인"
      ],
      "pitfalls": [
        "FIPS140-2레벨을 암호 키 길이등급으로쓰지않습니다.",
        "TPM있음과완전한신뢰확보를동일시하지 않습니다."
      ],
      "recall": [
        "암호 알고리즘 검증과 모듈검증은 어떻게다릅니까?",
        "TPM의측정과 실행 차단은 같습니까?",
        "CC평가 범위를 확인해야 하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-tpm",
        "sys-fips140"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "132-1-8",
          "items": [
            "TPM"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-4-1",
          "items": [
            "FIPS140-2레벨",
            "설계·보안요소·위협 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-1-11",
          "items": [
            "CC"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "129-1-11",
          "items": [
            "정보 보호 제품신속확인"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "digital-forensics",
      "title": "디지털 포렌식·아티팩트·슬랙·카빙·안티포렌식",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "흔적을 많이 모으는 것보다 원본을 훼손하지 않고, 어떤 과정으로 해석했는지 재현 가능하게 남기는 일이 핵심입니다.",
      "definition": "디지털포렌식은디지털자료를 식별·수집·보존·검사·분석·보고하여 사건사실을규명하는활동입니다. 아티팩트는OS·응용·통신사용등이 남긴흔적이며 존재만으로행위자·고의·정확시각을단정하지 않습니다.",
      "principles": [
        "계획과 권한 확인 → 휘발성우선순위를고려한수집 → 원본 보존·이미징·해시·인계기록 → 검사와 복원 → 상관분석 → 보고로 설명합니다. NIST800-86의수집·검사·분석·보고 구조와 법집행절차는 분리하며 해시일치가수집의 적법성까지자동보장하지는않습니다.",
        "파일슬랙은할당단위안의논리적파일끝이 후 남는공간입니다. 비할당영역과 다르며과거잔존데이터가 능성은파일시스템·초기화·SSDTRIM에좌우됩니다. 카빙은정상메타데이터없이내용특징으로파일을복원하는기법으로 조각화·압축·암호화·오탐에취약합니다.",
        "교육상카빙을헤더/푸터서명, 고정 크기·최대 크기, 파일내부 구조 검증, 내용·조각분류의 네접근으로 비교할 수 있으나기출이지정한 원분류는 확인하지못했습니다. 안티포렌식은삭제·암호화·타임스탬프조작·로그훼손등이며 독립로그·시각동기·중앙보존·교차증거로 대응합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "메타데이터 복원",
            "파일시스템 기록이 용",
            "기록손상시한계"
          ],
          [
            "카빙",
            "본문서명·구조·내용",
            "조각화·오탐검증"
          ],
          [
            "아티팩트분석",
            "OS·앱·네트워크흔적",
            "시각·버전·대안설명"
          ]
        ]
      },
      "example": {
        "title": "삭제 파일과 접속 시각 조사",
        "input": "디스크이 미지·중앙프록시로그·브라우저DB 가정",
        "steps": [
          "수집 권한·대상·시간대·도구 버전·해시를기록합니다.",
          "사본에서 파일구조와 카빙후보를검사합니다.",
          "브라우저·로그·파일 시각을교차비교하고 불일치를기록합니다.",
          "사용자직접 행위·백그라운드 동기화등대안설명을 평가합니다."
        ],
        "result": "복원파일과행위주장을분리하고 근거·제약이있는 보고서를 만듭니다.",
        "caution": "카빙4분류와 국내 증거능력·컴플라이언스요건의 원문은 미확인입니다."
      },
      "answer_outline": [
        "정의·유형",
        "원본 보존·증거연속성",
        "4단계",
        "카빙·슬랙",
        "안티포렌식대응"
      ],
      "pitfalls": [
        "포렌식도구 출력을 무오류로 보지않습니다.",
        "타임스탬프하나로범인을확정하지 않습니다."
      ],
      "recall": [
        "해시가보장하는것과보장하지 않는것은무엇입니까?",
        "슬랙과비할당영역은 어떻게다릅니까?",
        "카빙오탐은무엇으로검증합니까?"
      ],
      "source_ids": [
        "sys-forensic"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-1-13",
          "items": [
            "FileSlack"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "126-4-6",
          "items": [
            "FileCarving개념",
            "4기법특징"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-4-2",
          "items": [
            "포렌식정의",
            "유형·절차",
            "기술·활용"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "133-3-1",
          "items": [
            "안티포렌식배경·기술",
            "준수시스템구축·활용"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "137-1-2",
          "items": [
            "아티팩트"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-1-12",
          "items": [
            "디지털포렌식"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "ransomware-credential-threats",
      "title": "랜섬웨어·RaaS·인포스틸러·계정 공격",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "파일 암호화 뒤의 복구 문제와 그 전에 빼앗긴 계정·세션·자료 유출을 함께 다룹니다.",
      "definition": "랜섬웨어는암호화·데이터 탈취·공개 위협등으로피해자를갈취하는악성행위입니다. RaaS는 운영자·제휴공격자등이 도구·인프라·수익분배로역할을나누는서비스형범죄 모델이며 별도 암호 알고리즘이 아닙니다.",
      "principles": [
        "초기경로는 피싱·노출원격접속·취약점·공급망·도난자격증명등입니다. 공격은 정찰·권한상승·측면이동·정보 탈취·백업훼손·암호화로 이어질수 있지만순서는 사례마다 다릅니다. 대용량파일은대칭암호로 암호화하고 키를 공개 키로 보호하는 등하이브리드구조가 가능합니다.",
        "인포스틸러는브라우저비밀번호·쿠키·토큰·지갑등을 탈취하며 세션 토큰은 MFA후세션을 악용할 수 있습니다. 크리덴셜스터핑은타서비스 유출 계정·암호쌍을재사용하고 무차별대입과구분합니다. 큐싱은QR코드로 악성사이트·피싱을 유도하는사회공학입니다.",
        "예방은 패치·피싱저항인증·계정 권한·원격노출축소·분리·탐지·오프라인/불변백업·복원 시험입니다. 사고시격리·증거 보존·범위파악·자격증명/세션 회수·신고/통지검토·깨끗한복구·원인 제거·재발평가를 합니다. 복구와 업무연속성·유출 대응을 분리하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "랜섬웨어",
            "암호화·탈취·갈취",
            "복원·유출·업무 영향"
          ],
          [
            "RaaS",
            "도구·인프라·제휴분업",
            "공격 규모·역할분리"
          ],
          [
            "인포스틸러/스터핑",
            "비밀탈취/유출쌍재사용",
            "세션 회수·중복 암호 대응"
          ]
        ]
      },
      "example": {
        "title": "백업이 있어도 필요한 대응",
        "input": "파일암호화와 관리자쿠키 탈취의 동시징후",
        "steps": [
          "네트워크·계정 접근을 격리하고 증거를 보존합니다.",
          "암호화 범위와 탈취·백업훼손을따로조사합니다.",
          "비밀변경뿐 아니라기존 세션·토큰을 회수합니다.",
          "깨끗한시점 복구후취약원인과 새접근흔적을검증합니다."
        ],
        "result": "백업 복원완료를사고전체 종결과동일시하지 않습니다.",
        "caution": "CISA가 이드직접 접근403으로최신 절차 전문은 미열람.일반 대응 원칙을 NIST포렌식·MITRE자료로 교차설명했습니다."
      },
      "answer_outline": [
        "위협·분업",
        "침입과 확산",
        "키·데이터갈취",
        "예방·대응 흐름",
        "복구 검증"
      ],
      "pitfalls": [
        "RaaS를SaaS의합법 서비스와 같이취급하지 않습니다.",
        "MFA사용이면쿠키 탈취에 안전하다고하지 않습니다."
      ],
      "recall": [
        "랜섬웨어와RaaS의비교축은무엇입니까?",
        "비밀번호 변경만 으로세션 탈취가 끝납니까?",
        "불변백업에도 복원 시험이 필요한 이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-mitre",
        "sys-forensic",
        "sys-identity"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "128-1-12",
          "items": [
            "랜섬웨어·RaaS"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-4-5",
          "items": [
            "개념비교",
            "감염·암호화",
            "예방·사고 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "129-4-1",
          "items": [
            "인포스틸러·공격 절차·대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "131-1-10",
          "items": [
            "크리덴셜스터핑"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-1-6",
          "items": [
            "큐싱"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "threat-exposure-ttp",
      "title": "공격 표면·벡터·TTPs·측면이동·CTEM",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "취약점 개수만 세지 않고, 실제로 어디로 들어와 어떤 권한과 경로로 중요한 업무에도 달할 수 있는 지 봅니다.",
      "definition": "공격 표면은 공격자가상호작용할 수 있는 노출 지점의집합이고공격 벡터는침투·피해를일으키는 경로·수단입니다. TTPs는 전술(목표)·기법(방법)·절차(구체수행)를구분하며 CTEM은 노출을 지속적으로발견·우선순위화·검증·개선하는운영 접근입니다.",
      "principles": [
        "네트워크스캐닝은호스트·포트·서비스·응답 특성등을 통해 노출을 파악합니다. 자산발견과취약점 진단은 다르며스캔결과는 방화벽·시간·네트워크 경로·인증 권한에 따라 달라집니다. 승인 범위·장치 영향·탐지 로그를 확인하고 산업 장치에 는 안전한 방법을 선택합니다.",
        "측면이동은최초침입뒤다른 내부 시스템으로 접근·제어를확장하는행위입니다. 내부탐색·자격증명획득·원격서비스악용·권한확대등이 조합되며 정상SSH/RDP·계정을 써도악성목표가 가능합니다. 계정·단말·망의이벤트를 연결해경로를 분석합니다.",
        "CTEM은 범위 설정 → 발견 → 우선순위화 → 검증 → 동원/개선의폐루프로설명할 수 있습니다. 자산중요도·실제도달가능성·공격가 능성·보완통제·업무피해를함께 봅니다. CVSS가 높은 항목만 나열하거나제품 설치로 완료했다고판단하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "표면",
            "노출 지점전체",
            "외부·내부·신원·공급망"
          ],
          [
            "벡터",
            "공격의 진입 경로",
            "피싱·원격서비스등"
          ],
          [
            "TTP/CTEM",
            "공격 행동언어/개선루프",
            "관측·검증·책임자"
          ]
        ]
      },
      "example": {
        "title": "인터넷 웹에서 급여 DB까지",
        "input": "노출웹취약점 → 과다서비스 계정 → 내부 DB 접근가 능가정",
        "steps": [
          "노출과 업무자산을하나의경로로 모델링합니다.",
          "웹패치와계정 권한축소·망정책의 효과를 안전하게검증합니다.",
          "접속·토큰·원격실행 로그로 실제이동가능성을평가합니다.",
          "조치후동일경로를 재검증하고 새노출을 관측합니다."
        ],
        "result": "단일취약점점수보다중요업무까지 의실제 경로를 기준으로 개선합니다.",
        "caution": "CTEM명칭의원저작자 방법론전문 미열람.다섯단계를 공식 의무 표준으로 쓰지않습니다."
      },
      "answer_outline": [
        "용어구분",
        "TTP계층",
        "스캐닝범위",
        "측면이동경로",
        "CTEM루프"
      ],
      "pitfalls": [
        "열린포트모두를취약점이라 하지 않습니다.",
        "TTP를IOC해시목록과 동일시하지 않습니다."
      ],
      "recall": [
        "공격 표면과 벡터의차이는무엇입니까?",
        "정상계정을 쓰는측면이동은어떻게관측합니까?",
        "패치뒤재검증이 필요한 이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-mitre"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-1-12",
          "items": [
            "네트워크스캐닝"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-1-10",
          "items": [
            "TTPs"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-3-5",
          "items": [
            "표면·벡터",
            "측면이동단계·기법"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "139-1-11",
          "items": [
            "CTEM"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "iot-drone-platform-security",
      "title": "Mirai·IoT·드론·NFT·메타버스 보안",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "기기가 인터넷에 연결되고 가상세계가 실물 권리와 결합하면 계정·펌웨어·센서·거래의 신뢰 경로가 넓어집니다.",
      "definition": "Mirai는 기본 자격증명등취약한IoT 장치를 감염시켜DDoS 자원으로 활용한봇넷악성코드 사례입니다. IoT보안은설계부터 폐기까지 기기·연결·플랫폼·데이터를 보호하며 드론·가상플랫폼은 고유한물리·사회 위험을 추가 합니다.",
      "principles": [
        "IoT는 고유 신원·안전한 초기설정·최소서비스·서명업데이트·지원 기간·비밀보호·취약점 대응·안전 폐기를 설계합니다. 기본 암호 변경과 원격관리제한·패치·망분리·이상송신탐지가 Mirai류위험을 줄입니다. 재부팅만으로재감염조건까지 제거되지는않습니다.",
        "드론은명령링크가로채기·GNSS기만·센서교란·펌웨어변조·촬영정보 유출·분실위험이 있어명령인증·무결성·센서교차검증·업데이트서명·비상동작을 결합합니다. 암호화가 전파방해나위치기만을단독해결하지 않습니다.",
        "NFT마켓은피싱서명·과다토큰 승인·스마트계약·웹프론트·보관키를 보호합니다. NFT식별이저작권소유를자동증명하지 않습니다. 메타버스는아바타사칭·괴롭힘·생체/행동추적·미성년자보호·디지털격차를신고·차단·동의·최소수집·권리구제와연결합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "IoT",
            "기기·계정·업데이트",
            "생애주기·지원 종료"
          ],
          [
            "드론",
            "통신·위치·물리안전",
            "안전 상태·다중센서"
          ],
          [
            "NFT/메타버스",
            "키·서명·플랫폼·사용자",
            "거래권한·권리·피해 구제"
          ]
        ]
      },
      "example": {
        "title": "기본 암호 카메라의 봇넷 감염",
        "input": "외부 노출카메라에기본 계정잔존가정",
        "steps": [
          "장비를 격리하고 관리 접근·펌웨어·설정을 점검합니다.",
          "고유한자격증명과 필요한 연결만 허용합니다.",
          "지원 종료 제품은 대체·격리정책을 정합니다.",
          "비정상외부접속·송신량을감시하고 복구후재감염을확인합니다."
        ],
        "result": "기술조치와제품 지원·운영 책임을 수명 주기에 연결합니다.",
        "caution": "IoT 공통보안7대원칙 원문과 OpenSea특정 사건원자료는 미열람.위일반 통제를 해당7원칙·사건확인으로 대체하지 않습니다."
      },
      "answer_outline": [
        "Mirai사례",
        "수명 주기 위협·통제",
        "드론물리위험",
        "NFT서명권한",
        "가상공간사회 대응"
      ],
      "pitfalls": [
        "NFT원본성 표시를완전한법적권리로쓰지않습니다.",
        "IoT재부팅을근본원인 제거로판단하지 않습니다."
      ],
      "recall": [
        "기본 암호와 지원 기간은 어떤관계입니까?",
        "드론암호화로 방해전파를막을수 있습니까?",
        "서명피싱에서 사용자는 무엇을승인합니까?"
      ],
      "source_ids": [
        "sys-mirai",
        "sys-genai-profile"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "126-4-3",
          "items": [
            "Mirai",
            "IoT생애주기 위협·해결",
            "공통7원칙"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-1-5",
          "items": [
            "드론보안위협·대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "128-4-1",
          "items": [
            "NFT특성",
            "OpenSea침해 기반 취약점"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "126-4-1",
          "items": [
            "메타버스특징",
            "기술·사회 위협",
            "안전방안"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "siem-soar",
      "title": "SIEM과 SOAR·사고 대응 자동화",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "여러 로그에 서 사건을 찾아 연결하는 일과, 그 사건에 대해 도구·사람의 대응을 조율하는 일을 이어 붙입니다.",
      "definition": "SIEM은 보안이벤트를 수집·정규화·상관분석·검색하여 탐지와 조사를지원합니다. SOAR는 여러 보안도구·절차·사람을 플레이북으로연결하고 반복대응을 자동화·기록하는기능군입니다.",
      "principles": [
        "SIEM은 시간 동기·자산·사용자문맥·로그 품질·규칙튜닝이핵심입니다. 수집량증가만 으로탐지 효과가 커지지않으며누락·오탐·저장 비용·프라이버시를 관리합니다. 전술·기법에 연결된탐지로 유효성을시험합니다.",
        "SOAR는 경보수신 → 중복제거·강화정보조회 → 분류·우선순위 → 승인/자동조치 → 티켓·증거 기록 → 종결·피드백을구성합니다. IP차단·계정비활성화같은 행위는 업무 영향·확신도·승인 기준·롤백·타임아웃이필요합니다.",
        "구성은오케스트레이션연계·자동화엔진·사건/케이스관리·위협 정보등으로설명할 수 있습니다. 기대효과는 반복시간단축·일관성·증거추적이며 실제 MTTD/MTTR·오탐·재오픈·자동조치실패로검증합니다. 자동화 대상과 사람의 판단경계를 명확히합니다.",
        "도구 연계용 계정과 API 토큰도 최소 권한·회전·실행감사를 적용하여 자동화 플랫폼의 권한집중을 줄입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "SIEM",
            "로그 수집·상관·탐지",
            "이벤트 품질·탐지튜닝"
          ],
          [
            "SOAR",
            "도구·플레이북·대응",
            "승인·권한·롤백"
          ],
          [
            "공통",
            "사건문맥과감사",
            "연계 API·운영 책임"
          ]
        ]
      },
      "example": {
        "title": "피싱 메일 플레이북",
        "input": "직원신고메일의URL평가필요",
        "steps": [
          "원본과 헤더를보존하고 안전한 환경에 서 평판·관측을조회합니다.",
          "동일메일수신범위를 검색합니다.",
          "확신도와업무 영향에 따라 승인후메일격리·도메인차단합니다.",
          "조치 결과·예외·복원을 기록하고 탐지 규칙을 보완합니다."
        ],
        "result": "자동화속도와잘못된광역차단 위험을 함께 관리합니다.",
        "caution": "플레이북은 조직의 권한·절차·업무 영향에 맞춰 시험해야 하며 자동 차단의 효과를 보장하지 않습니다."
      },
      "answer_outline": [
        "등장배경",
        "수집 → 대응 구조",
        "SIEM/SOAR비교",
        "플레이북예",
        "도입·효과 측정"
      ],
      "pitfalls": [
        "SOAR가 SIEM이나 분석가 를완전히대체한다고쓰지않습니다.",
        "모든 경보를 무승인 차단으로 연결하지 않습니다."
      ],
      "recall": [
        "오케스트레이션과자동화는 무엇이다릅니까?",
        "위험한조치의승인 기준은 무엇입니까?",
        "효과 측정에 오탐도포함해야 하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-soar",
        "sys-mitre",
        "sys-forensic"
      ],
      "validation": "출처 확인",
      "version_note": "Microsoft 공식 SOAR 설명(2026-05-26)과 NIST/MITRE 근거로 원리·비교·운영을 확인했습니다. 제조사의 효과 주장을 보편 성과 수치로 옮기지 않았습니다.",
      "requirements": [
        {
          "question": "127-3-6",
          "items": [
            "SOAR정의·배경",
            "구성·기능",
            "효과·도입"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "135-1-5",
          "items": [
            "SIEM·SOAR비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "zero-trust-supply-chain-n2sf",
      "title": "제로 트러스트·공급망 보안·N2SF",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "내부망·기존 계정·납품업체라는 이유만으로 접근을 허용하지 않고 자원별 정책과 관측 증거로 판단합니다.",
      "definition": "제로트러스트는위치나자산소유만으로암묵적신뢰를 주지않고각접근의 인증·인가·상태를 평가하는보안원칙입니다. 공급망보안은개발·빌드·의존성·배포·운영의 신뢰를 관리하며 N2SF는 국가·공공기관의 정보중요도와위협 기반망보안체계를지향합니다.",
      "principles": [
        "NIST800-207의정책엔진은접근 결정, 정책 관리자는 통신 경로 설정·해제, PEP는 연결을 허용·감시·종료합니다. 모든 통신 보호·세션별최소 권한·동적정책·자산상태관측과지속적인증거 수집이 핵심이며 인증반복만으로정의하지 않습니다.",
        "공급망은소스 보호·동료검토·의존성고정·취약점/라이선스 분석·격리 빌드·서명·provenance·SBOM·배포 검증·운영 감시를 연결합니다. 빌드작업의 NHI·토큰도 짧은수명·최소 권한으로 보호하고 외부공급자의접근을 서비스별로 제한합니다.",
        "N2SF는 정보·서비스식별과C/S/O분류등을 통해 업무 환경에 맞는보안대책을정하는맥락으로설명합니다. 2025년초안과2025.9정식1.0·후속지침은 구분해야합니다. CISA성숙도2.0의단계·기둥·횡단기능과 N2SF세부통제는 원문 미열람상태에 서 정확한필수목록을 확정하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "경계보안",
            "망위치중심기본 정책",
            "경계 통제는 여전히활용가 능"
          ],
          [
            "제로트러스트",
            "자원·신원·상태·세션",
            "점진이행·관측필요"
          ],
          [
            "공급망/N2SF",
            "생애주기 신뢰/공공위험 기반",
            "서명·분류만 으로완료아님"
          ]
        ]
      },
      "example": {
        "title": "외부 유지보수업체 접근",
        "input": "협력사계정으로 내부전체 VPN 접근하던환경",
        "steps": [
          "자산·서비스·신원·데이터 흐름을 식별합니다.",
          "유지보수대상·시간·승인·단말 상태에 맞춘접근 정책을 둡니다.",
          "연결중행위와 위험 상태를 관측하고 필요시세션을 끊습니다.",
          "서명된배포물·작업 기록과 계약 종료 권한 회수를 검증합니다."
        ],
        "result": "망경계하나의신뢰를 업무 자원별검증과 수명 관리로 세분합니다.",
        "caution": "CISA2.0은403, N2SF공식 원문은 미열람입니다.일반 ZT설계를 해당제도세부요건충족으로표시하지 않습니다."
      },
      "answer_outline": [
        "원칙",
        "PE/PA/PEP도 식",
        "경계비교",
        "공급망적용",
        "N2SF검증 상태"
      ],
      "pitfalls": [
        "ZT도 입을VPN제거제품하나로축소하지 않습니다.",
        "물리망분리와 ZT를 항상 택일이라고설명하지 않습니다."
      ],
      "recall": [
        "세션별최소 권한은 무엇입니까?",
        "서명된악성코드도 가능한 이유는무엇입니까?",
        "N2SF정보등급과사용자 인가를 어떻게연결합니까?"
      ],
      "source_ids": [
        "sys-zerotrust",
        "sys-nhi"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "131-2-4",
          "items": [
            "ZT원리·원칙·적용",
            "경계 신뢰비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "135-4-6",
          "items": [
            "경계보안·ZT성숙도2.0",
            "도입 고려"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-4-4",
          "items": [
            "공급망보안",
            "ZT기반아키텍처"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "137-3-6",
          "items": [
            "N2SF개념",
            "적용 절차",
            "고려"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "bpfdoor-defense",
      "title": "BPFDoor 백도어와 리눅스 탐지",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "열린 수신포트만 확인하는 점검으로 조용히 대기하는 백도어를 놓칠 수 있어 프로세스·소켓·패킷·파일 증거를 결합합니다.",
      "definition": "BPFDoor는 리눅스의BPF기반 패킷필터등을 악용하여 특정 네트워크트래픽을감시하고 명령·후속연결을 활성화하는백도어계열로알려져있습니다. 정상BPF기능자체와악성사용을구분해야합니다.",
      "principles": [
        "전통적고정포트listen형백도어와달리항상 눈에띄는수신포트가없어도 트리거패킷을 관찰하는구조가 가능합니다. 따라 서포트스캔결과하나로감염없음을보장할 수 없습니다. 변종별프로세스위장·지속성·통신 동작은 다를 수 있습니다.",
        "위협은 서버명령실행·자격증명및정보 탈취·측면이동·서비스 가용성훼손입니다. 관리자 권한·raw socket·BPF관련사용과예상외실행파일·삭제된실행파일·비정상통신·지속성 설정을 조합해조사하고 정상운영 도구와 구별합니다.",
        "대응은 자산과공식 점검 범위 확인 → 의심호스트격리 → 휘발성·디스크·로그 증거 보존 → 감염·침입 경로파악 → 비밀·세션 회수 → 깨끗한재구축·취약점제거 → 재검증입니다. 일괄삭제·재부팅으로증거를 잃거나원격접속을영구상실하지 않도록업무 복구와 연계합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "포트listen형",
            "고정연결대기흔적",
            "포트·소켓관측"
          ],
          [
            "패킷트리거형",
            "특정 패킷 감시후활성화",
            "포트점검만 으로부족"
          ],
          [
            "다층조사",
            "프로세스·파일·네트워크",
            "시간·변종·오탐검증"
          ]
        ]
      },
      "example": {
        "title": "포트가 정상인 의심 서버",
        "input": "외부이 상통신관측;평상시포트목록변화없음",
        "steps": [
          "공식가 이드와서버역할을대조해의심증거를 보존합니다.",
          "실행 경로·권한·소켓·프로세스 관계를 분석합니다.",
          "동일계정과 인접서버의 원격접근이 력을추적합니다.",
          "발견된변종의지속성·초기침입을 제거후복구합니다."
        ],
        "result": "단일IOC나포트검사보다 다층증거와 원인 제거로대응합니다.",
        "caution": "KISA2025-05-12공지직접 열람.첨부가 이드전문·변종별IOC는 미열람이며 특정 명령·해시검출의완전성을주장하지 않습니다."
      },
      "answer_outline": [
        "기능과 악용구분",
        "기존 백도어비교",
        "위협 영향",
        "기술·관리 대응",
        "증거·복구"
      ],
      "pitfalls": [
        "모든 BPF프로세스를 악성으로분류하지 않습니다.",
        "점검스크립트음성을절대무감염증명으로쓰지않습니다."
      ],
      "recall": [
        "수신포트없음이무감염을뜻하지 않는이유는무엇입니까?",
        "정상BPF와 악성활동을어떻게구분합니까?",
        "격리전후증거 보존의 우선순위는무엇입니까?"
      ],
      "source_ids": [
        "sys-bpfdoor",
        "sys-forensic",
        "sys-mitre"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "137-4-1",
          "items": [
            "BPFDoor개념·기존 백도어차이",
            "위협·영향",
            "기술·관리 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "reverse-proxy-ddos",
      "title": "리버스 프록시·로드밸런싱·DDoS 대피",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "사용자 앞에서 요청을 받아 안전한 서버로 전달하되, 회선 자체가 막히는 공격은 더 앞단에서 흡수해야 합니다.",
      "definition": "리버스프록시는클라이언트가 접속하는대표종단점으로서백엔드서버에 요청을 전달하고 응답을 중계합니다. 로드밸런싱은여러 대상으로 부하를분배하는기능이며 DDoS대피는대규모 공격트래픽을외부 보호망으로우회·정제하는대응입니다.",
      "principles": [
        "주요 기능은 TLS종단·캐시·압축·접근 정책·WAF연계·백엔드은닉·라우팅입니다. 단일프록시가새장애점이되지않도록다중화·상태 검사·용량·보안패치를설계합니다. Host·전달IP·프로토콜헤더를신뢰할범위와 직접 백엔드접근 차단을 정합니다.",
        "동작은 클라이언트 요청 → 프록시인증·정책 → 대상 선택 → 백엔드요청 → 응답입니다. 설정에 는 upstream대상·timeout·최대본문·재시도·세션·로그를 포함합니다. 이미처리된비멱등요청을 무조건 재시도하면 중복거래위험이 있습니다.",
        "DDoS는 볼륨·프로토콜·응용 공격을 구분하고 회선 용량을 초과하면 서버안의방어만으로부족합니다. CDN·Anycast·대피소·ISP와 의우회·속도제한·캐시·원본 보호를 사전 준비하고 DNS·라우팅·전환조건·연락망·실전훈련을갖춥니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "리버스프록시",
            "서버앞요청중계",
            "TLS·정책·캐시·집중점"
          ],
          [
            "로드밸런서",
            "대상간분배·헬스체크",
            "세션·용량·전환"
          ],
          [
            "DDoS대피",
            "상위망우회·정제",
            "사전가입·경로·원본 보호"
          ]
        ]
      },
      "example": {
        "title": "웹사이트 공격 시 전환",
        "input": "업링크1Gbps;공격이 수Gbps로유입되는가정",
        "steps": [
          "서비스내속도제한만으로회선고갈을해결할 수 없음을확인합니다.",
          "상위보호 서비스로 트래픽을우회하고 정상요청만 원본으로 전달합니다.",
          "원본직접 주소 노출과 우회경로를 차단합니다.",
          "정상사용자의 지연·오차단·복귀절차를 감시합니다."
        ],
        "result": "대응지점을공격 병목보다 앞으로옮기고업무 품질을 검증합니다.",
        "caution": "국내 DDoS 사이버대피소의현행 대상·용량·가입절차 원문은 이번조사에서미확인입니다."
      },
      "answer_outline": [
        "정의·전달도 식",
        "주요 설정",
        "LB차이",
        "공격층별대응",
        "대피소운영"
      ],
      "pitfalls": [
        "프록시설정만 으로대역폭고갈을항상 막는다고쓰지않습니다.",
        "재시도를 모든 HTTP요청에 동일적용하지 않습니다."
      ],
      "recall": [
        "리버스와포워드프록시는누구를대신 합니까?",
        "정상IP전달헤더를아무클라이언트에 서 나믿으면왜위험합니까?",
        "DDoS우회는어느병목을 해결합니까?"
      ],
      "source_ids": [
        "sys-reverseproxy"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "128-4-2",
          "items": [
            "리버스프록시정의·동작·설정",
            "DDoS 사이버대피소"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "127-2-2",
          "items": [
            "무중단배포프록시·로드밸런싱"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "privacy-law-internal-plan",
      "title": "개인정보 보호 법·내부 관리 계획·마이데이터 권리",
      "domain": "개인정보·컴플라이언스",
      "aliases": [],
      "easy": "수집에 서 파기까지 누가 어떤 근거와 권한으로 처리하는지를 기록하고, 정보 주체가 이동·설명·거부 권리를 행사할 통로를 둡니다.",
      "definition": "개인정보 보호는 처리 목적·법적근거·최소수집·정확성·안전조치·보유 기간·권리행사를생애주기로 관리하는 활동입니다. 내부 관리 계획은 이를조직 내책임·절차·점검으로 실행하는관리 기준이며 전송 요구권과자동화 결정권리는적용 조건을 확인해야합니다.",
      "principles": [
        "내부 관리에 는 책임자·취급자역할, 권한부여/변경/말소, 접근 통제, 암호화, 접속기록, 악성코드 대응, 교육, 물리보호, 위탁·사고·재난·파기등을 연결합니다. 명목문서작성보다실제이행·점검·예외·개선증거가 중요하며 규모·처리 정보별적용 조건이 다릅니다.",
        "암호화는 저장·전송·단말·백업과 키 접근·분리보관·회전·복구를 함께 설계합니다. 비밀번호는 복호형저장보다 적절한 일방향KDF가 필요합니다. 법정암호화 대상·보존 기간·점검 주기는 고시 원문을 판본과 대상에 맞게확인합니다.",
        "2023개정맥락의전송 요구권은개인이자신의정보를 전송하도록요구하는권리이고자동화 결정은 완전자동화·권리의무중대영향·예외·설명등의 조건을 구분합니다. 2026현행제37조의2제3항은정당사유없이필요조치를거절하지못하는대응을 규정합니다. 마이데이터는 단순 복제 서비스보다 전송 인증·권한·철회·수신처보호가 필요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "내부 계획",
            "조직 통제·책임·점검",
            "실제 증빙·범위·예외"
          ],
          [
            "전송 요구",
            "정보 주체주도이동",
            "대상·수신자·보안조건"
          ],
          [
            "자동화 결정권리",
            "거부·설명·인적개입",
            "적용 요건·예외 확인"
          ]
        ]
      },
      "example": {
        "title": "AI 신용심사 문의 처리",
        "input": "고객이자동심사 결과에 설명을 요청하는가정",
        "steps": [
          "완전자동화와 영향·처리 근거등적용 조건을 검토합니다.",
          "설명·인적재처리·이의제기담당과응답 절차를 둡니다.",
          "모델 입력·판정·주요 기준·검토 증거의 보호·보존을 정합니다.",
          "처리 결과와 고객권리행사기록을 남깁니다."
        ],
        "result": "업무 프로세스와 정보 주체 권리·안전조치를연결합니다.",
        "caution": "2023개정전체·데이터3법·산업별제공범위·2023마이데이터보안안내서전문은 미열람.2026고시 부칙의 단계시행을일괄현재의무로 단정하지 않습니다."
      },
      "answer_outline": [
        "처리 흐름·주체",
        "내부 계획체계",
        "암호화·접근·로그",
        "전송·자동화권리",
        "판본·조건"
      ],
      "pitfalls": [
        "가명정보를 개인정보 보호 법밖의자료로 보지않습니다.",
        "법정권리를모든 AI결과 의무 조건거부권으로확대하지 않습니다."
      ],
      "recall": [
        "내부 계획이 행을어떤증거로 확인합니까?",
        "전송 요구권과열람권은무엇이다릅니까?",
        "자동화 결정권리의적용 조건은 무엇입니까?"
      ],
      "source_ids": [
        "sys-privacy-safety",
        "sys-pipa-auto",
        "sys-identity"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "127-2-5",
          "items": [
            "내부 관리 계획정의·필요·내용"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "131-4-2",
          "items": [
            "내부 관리 계획",
            "암호화"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "128-2-4",
          "items": [
            "데이터3법배경·개정",
            "마이데이터 범위",
            "활성화"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-2-4",
          "items": [
            "2023개정",
            "주체·처리 흐름",
            "전송·자동화권리"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-2-4",
          "items": [
            "마이데이터 보호 책임자",
            "접근 관리",
            "재해조치"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "pseudonymization-anonymization",
      "title": "가명처리·익명처리와 재식별 위험",
      "domain": "개인정보·컴플라이언스",
      "aliases": [],
      "easy": "이름을 지워도 다른 자료와 합쳐 누군지 알 수 있으므로 식별정보·준식별자·추가 정보·이용 환경을 같이 평가합니다.",
      "definition": "가명처리는 추가 정보없이는특정 개인을알아볼수 없도록개인정보일부를삭제·대체하는처리이고 익명화는합리적으로고려할 수 있는 수단으로 개인을알아볼수 없는 수준을목표로 합니다. 둘은처리 기술뿐 아니라재식별가능성·법적취급의차이가있습니다.",
      "principles": [
        "직접 식별자는토큰 대체·삭제하고 생년월일·주소·희귀직업같은 준식별자는범주화·일반 화·억제·표본추출·노이즈등을 검토합니다. 일관된가명은분석 연결성을유지하지만연계 공격의 경로도 될수 있습니다. 추가 정보·매핑키는 분리하여 접근을 통제합니다.",
        "위험 평가는 목적·수신자·외부 자료·공격자능력·희귀값·조합식별·반출조건을 포함합니다. k-익명성은 동일준식별조합의최소집단크기이지만 민감값이 동질적이거나배경지식이있으면 노출이 남습니다. 분석 유용성과 보호의 절충을 검증합니다.",
        "준비 → 위험 검토 → 가명처리 → 적정성검토 → 안전 관리의 흐름으로 설명할 수 있습니다. 재식별시도금지·목적준수·로그·보유 기간·추가 정보 분리를 운영합니다. 최신가 이드의법정절차·결합전문 기관 요건등은 해당원문을 확인해야합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "가명",
            "추가 정보없이식별곤란",
            "추가 정보·목적·통제필요"
          ],
          [
            "익명",
            "합리적수단으로 식별곤란",
            "환경변화·외부 정보재검토"
          ],
          [
            "마스킹",
            "화면·필드의 표시가림",
            "데이터전체 익명성보장아님"
          ]
        ]
      },
      "example": {
        "title": "소규모 진료 통계",
        "input": "이름 삭제후정확나이·우편번호·희귀질환잔존",
        "steps": [
          "직접 식별자가없어도 희귀조합으로개인이드러날수 있는 지평가합니다.",
          "나이를연령대·지역을넓은권역으로일반 화하고 작은 셀을억제합니다.",
          "질환분포 보존과 재식별 위험을 함께 검사합니다.",
          "반출대상·통제 환경에 맞춰잔여위험을 기록합니다."
        ],
        "result": "값 삭제수보다식별가능성과목적 적합성을판단합니다.",
        "caution": "2026.3공식가 명정보가 이드목록만 확인;첨부 전문은 미열람입니다.법정익명성판정이나활용 승인 사례로 사용하지 않습니다."
      },
      "answer_outline": [
        "정의·추가 정보",
        "기법 분류",
        "처리 절차",
        "유용성·위험 평가",
        "안전 운영"
      ],
      "pitfalls": [
        "식별자해시만으로익명이라선언하지 않습니다.",
        "k가 크면모든 민감속성이보호된다고하지 않습니다."
      ],
      "recall": [
        "가명과익명은추가 정보에 대해어떻게다릅니까?",
        "준식별자조합은왜위험합니까?",
        "마스킹과가명처리의 범위차이는무엇입니까?"
      ],
      "source_ids": [
        "sys-privacy-guides",
        "sys-dp"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "128-1-10",
          "items": [
            "가명·익명처리 기술"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "139-1-13",
          "items": [
            "가명처리 기법"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "pet-homomorphic-encryption",
      "title": "PET 분류와 동형암호",
      "domain": "개인정보·보안기술",
      "aliases": [],
      "easy": "데이터를 원문으로 모으지 않고 계산하거나, 공개 결과에 서 개인의 영향을 줄이는 등 보호지점을 먼저 선택합니다.",
      "definition": "PET는 개인정보 침해 위험을 줄이면서정해진 데이터 활용을 가능하게하는기술군입니다. 동형암호는 암호문에 연산한결과를 복호하면 대응하는평문 연산 결과가 나오는암호 기법으로, 계산위탁자가원문을 보지않게할 수 있습니다.",
      "principles": [
        "PET는 암호 기반 계산(HE/MPC), 분산학습(FL), 통계적공개 보호(DP), 데이터변환·합성등으로나눌수 있습니다. 보호 대상은 입력·중간계산·출력·모델중어디인지명확히하며 기술 이름만 으로법적익명성이나 정확한보호수준을보장하지 않습니다.",
        "PHE는 제한된연산 종류, SHE/leveled는 제한깊이, FHE는 부트스트래핑등으로일반 연산을 지속하도록설명합니다. 암호문잡음·곱셈깊이·회전·키교환·패킹이성능·정확도에 영향을 줍니다. SEAL의BFV/BGV는 암호화정수모듈러연산, CKKS는 근사실수/복소연산에 적합합니다.",
        "HE는 암호화된정확/근사계산을 하지만결과자체의개인정보 노출은 별도 입니다.DP는 분포 보호를 위해잡음을넣고합성데이터는 학습한분포를 모사해새자료를 만드나학습 원본을 기억할 수 있습니다. 계산 비용·공개수준·유용성·공모 가정으로 선택합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "HE",
            "암호문 계산;입력비공개",
            "연산 비용·출력 누출"
          ],
          [
            "DP",
            "개인영향제한;통계 보호",
            "ε·잡음·누적질의"
          ],
          [
            "합성데이터",
            "분포를 모사한생성자료",
            "품질·기억·재식별검사"
          ]
        ]
      },
      "example": {
        "title": "비공개 급여 합계",
        "input": "회사두곳이개별급여를서버에 노출하지 않고합계계산",
        "steps": [
          "권한있는 집계자가공개 키를 제공합니다.",
          "각급여를암호화하고 서버는 암호문합을구합니다.",
          "집계자는결과만 복호하고 소집단 노출 위험을 검토합니다.",
          "필요시최소집계크기·DP등출력 보호를 추가 합니다."
        ],
        "result": "암호문 계산의 입력 보호와 최종통계 보호를 구분합니다.",
        "caution": "구체보안파라미터·키 관리와 성능 시험은 미수행입니다.합성자료를 자동익명으로간주하지 않습니다."
      },
      "answer_outline": [
        "PET 보호지점",
        "HE식·유형",
        "세기술상세비교",
        "집계사례",
        "성능·출력 한계"
      ],
      "pitfalls": [
        "FHE가 무제한무료계산을 뜻하지 않습니다.",
        "CKKS근사값을 회계정 수정확값과 혼동하지 않습니다."
      ],
      "recall": [
        "HE가 보호하지못할 수 있는 출력 위험은 무엇입니까?",
        "CKKS와BFV선택 기준은 무엇입니까?",
        "DP·HE·합성을함께 쓸수 있습니까?"
      ],
      "source_ids": [
        "sys-he",
        "sys-seal",
        "sys-dp"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "133-1-5",
          "items": [
            "동형암호 원리·유형"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "134-1-11",
          "items": [
            "PET"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "138-4-6",
          "items": [
            "PET정의·배경",
            "분류·핵심",
            "HE·DP·합성상세비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "differential-privacy",
      "title": "차분 프라이버시와 프라이버시 예산",
      "domain": "개인정보·보안기술",
      "aliases": [],
      "easy": "한 사람의 포함 여부가 발표 결과를 크게 바꾸지 않게 만들어 참여자의 추가 노출을 제한합니다.",
      "definition": "차분프라이버시는 한개인의기록이 차이나는인접데이터셋에 서 확률적알고리즘의 출력 분포가 가깝도록제한하는보호정의입니다. ε는구별가능성의한계를 조절하며(ε, δ)-DP는 추가 실패허용항δ를가집니다.",
      "principles": [
        "순수ε-DP는 모든 출력사건S에대해Pr[M(D)∈S]<=exp(ε)Pr[M(D′)∈S]를요구합니다. ε가작을수록강한보호가 될수 있지만유용성과 절충됩니다. ε를실제 재식별확률로 번역하거나출력오차율과같다고하면 안됩니다.",
        "질의민감도는 한기록 변경이 결과에 미치는최대차이입니다. Laplace기법은 일반적으로척도Δf/ε의잡음을추가 합니다. 합계에서는개인값 범위를 clipping하지 않으면민감도가 무한정커질수 있어범위·인접성정의가필수입니다.",
        "반복질의는 정보를 누적하므로 프라이버시 회계와예산관리가 필요합니다. 순차합성의기본 상한은ε들의합이며 사후처리는 추가 정보 접근이 없으면 보호를 악화시키지않습니다. 중앙형은신뢰집계자가원자료를 보고, 로컬형은각단말이 출력전섭동하여 신뢰·정확도 조건이 다릅니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "중앙DP",
            "원자료를 신뢰집계자가처리",
            "신뢰·접근 통제필요"
          ],
          [
            "로컬DP",
            "각단말에 서 섭동",
            "강한원자료분산·오차증가"
          ],
          [
            "출력 관리",
            "예산·민감도·반복질의",
            "회계와유용성 검증"
          ]
        ]
      },
      "example": {
        "title": "인원수 질의의 잡음 척도",
        "input": "포함/미포함인접성;개인당1기록;count민감도1",
        "steps": [
          "ε=0.5이면 Laplace척도b=1/0.5=2입니다.",
          "이는항상 정확히2만큼더한다는뜻이아니라확률 분포척도입니다.",
          "같은 대상에ε0.5질의를세번하면 기본순차상한은 1.5입니다.",
          "필요정확도·표본수·발표 정책에 맞춰예산을배분합니다."
        ],
        "result": "수학적보호정의와실제 확률오차·질의 운영을 분리합니다.",
        "caution": "예제는단순 count와 기본합성조건입니다.임의의 학습 알고리즘을 그대로DP라부를수 없습니다."
      },
      "answer_outline": [
        "인접성·정의식",
        "ε·δ의미",
        "민감도·Laplace",
        "합성·회계",
        "신뢰 모델"
      ],
      "pitfalls": [
        "ε를익명성보장퍼센트로쓰지않습니다.",
        "노이즈를넣었다는이유만으로DP라하지 않습니다."
      ],
      "recall": [
        "민감도는 무엇의최대변화입니까?",
        "반복질의가 예산을쓰는이유는무엇입니까?",
        "합계에서개인값 범위를 정해야 하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-dp"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "138-4-6",
          "items": [
            "차분프라이버시 원리·상세비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "secure-multiparty-computation",
      "title": "다자간 안전 계산 MPC와 임계 인증",
      "domain": "개인정보·보안기술",
      "aliases": [],
      "easy": "서로 입력을 공개하지 않고 합의한 결과만 계산하거나, 한 장치가 전체 서명키를 갖지 않게 나눠 보관합니다.",
      "definition": "MPC는 여러 참여자가 각자의입력을 비공개로 유지하며 정해진 함수를 공동 계산하는프로토콜군입니다. 보안은정확성·입력 기밀성·허용누출과 공모·악의성·통신·가용성 가정에 따라 정의합니다.",
      "principles": [
        "대표구성은비밀분산, 가블드회로, OT, 동형암호 기반등입니다. 비밀분산은 한값을 여러 share로나눠일정수준이모여야복원하게하며 단순가산분산과임계분산의복원 조건은 다릅니다. MPC는 분산저장만 하는것이아니라share상태의 안전한 연산과 검증을 포함합니다.",
        "semi-honest는 규칙은 따르되관측으로추론하는상대, malicious는 임의로행동하는상대를가정합니다. 정직다수·비동기·참여자탈락·결과 공개 범위에 따라 비용과 보장이바뀝니다. 결과가 소집단의 민감값을 드러내는위험은 입력 암호화만 으로없어지지않습니다.",
        "임계인증은 개인키를 분산한여러 주체가 부분연산을 통해 표준서명을만들도록할 수 있습니다. NIST다자임계암호프로젝트는서명·복호·키 생성등의 분산 신뢰를 다룹니다. 정책 승인·share갱신·백업·공모 한계·감사를함께 설계합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "비밀분산",
            "입력을 share로분할",
            "그자체가전체 MPC는 아님"
          ],
          [
            "안전 계산",
            "share·회로등으로공동연산",
            "공모·악의모델명시"
          ],
          [
            "임계서명",
            "키전체 복원없이공동서명",
            "승인·가용성·복구"
          ]
        ]
      },
      "example": {
        "title": "가산분산 합계의 장난감 예",
        "input": "mod101;A입력7, B입력9;두서버는 공모하지 않는가정",
        "steps": [
          "A는7을20과88로분산합니다:20+88=108≡7.",
          "B는9를30과80으로분산합니다:30+80=110≡9.",
          "서버1합50, 서버2합168≡67입니다.",
          "50+67=117≡16으로7+9의합계가복원됩니다."
        ],
        "result": "개별share와 합계결과의 관계를 모듈러계산으로 확인합니다.",
        "caution": "이예는합계만의교육예시이며 악의서버·인증·공모·중단을처리하는완성프로토콜이 아닙니다."
      },
      "answer_outline": [
        "정의·보안모델",
        "기술 종류",
        "분산합예",
        "임계인증",
        "성능·공모 한계"
      ],
      "pitfalls": [
        "MPC를 모든 참여자가 데이터를 합쳐암호화하는방식으로 쓰지않습니다.",
        "결과 누출을 무시하지 않습니다."
      ],
      "recall": [
        "공모 가정이 바뀌면왜보장이달라집니까?",
        "비밀분산과 MPC는 어떻게다릅니까?",
        "임계인증의 키 복구·가용성 위험은 무엇입니까?"
      ],
      "source_ids": [
        "sys-mpc"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "133-4-1",
          "items": [
            "MPC 개념·원리·특징",
            "기술 종류",
            "기반 인증 서비스"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "federated-learning-security",
      "title": "연합학습·FedAvg와 프라이버시 보완",
      "domain": "개인정보·AI보안",
      "aliases": [],
      "easy": "원자료를 현장에 남기고 모델 갱신을 모으지만, 갱신값 자체에 남은 정보를 별도로 보호합니다.",
      "definition": "연합학습은 여러 클라이언트가 로컬 데이터로 모델을 학습하고 업데이트를 집계하여 공유모델을 개선하는방식입니다. FedAvg는 클라이언트의 로컬학습 결과를 데이터 양등으로가중평균하는대표 알고리즘입니다.",
      "principles": [
        "서버가 초기모델·참여자를 선택하고 모델 배포 → 로컬최적화 → 업데이트업로드 → 집계 → 다음라운드를 반복합니다. 데이터를 중앙에직접 수집하지 않아전송·거버넌스부담을줄일수 있지만서버와 클라이언트의 신뢰·업무 근거는 여전히필요합니다.",
        "Non-IID데이터·불균등표본·시스템 성능·연결단절·통신 비용·straggler가 수렴과공정성에 영향을 줍니다. FedSGD는 기울기를빈번히집계하고 FedAvg는 여러로컬업데이트후평균하여 통신을 줄일수 있습니다. FedProx등변형의목적과 원문은 별도 확인합니다.",
        "업데이트로 부터기울기역추정·회원추론이 가능하고 오염 클라이언트가 백도어를주입할 수 있습니다. secure aggregation은 개별업데이트관측을줄이고DP는 출력의 개인영향을 제한하며 HE/MPC는 계산 기밀성을 돕습니다. 클라이언트 인증·강건 집계·감사·검증과 결합합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "중앙학습",
            "원자료중앙집중",
            "데이터 이동·권한"
          ],
          [
            "FedAvg",
            "로컬학습후가중집계",
            "Non-IID·통신·이탈"
          ],
          [
            "보호 기술",
            "SecureAgg·DP·HE/MPC",
            "정확도·공모·성능 절충"
          ]
        ]
      },
      "example": {
        "title": "데이터 수에 따른 가중 평균",
        "input": "A표본100/가중치2, B표본300/가중치4;단일스칼라모델예",
        "steps": [
          "전체 표본은 400입니다.",
          "집계값=(100×2+300×4)/400=3.5입니다.",
          "클라이언트단순 평균3과 다름을확인합니다.",
          "비균등데이터·악성업데이트에 의한집계왜곡을평가합니다."
        ],
        "result": "가중규칙을 명시하고 기밀성·강건성·공정성을 별도로검토합니다.",
        "caution": "예제는원리 검산이며 모든 알고리즘이 같은가중치·참여정책을 사용하는 것은아닙니다."
      },
      "answer_outline": [
        "라운드도 식",
        "알고리즘비교",
        "Non-IID·통신",
        "누출·오염 위협",
        "보완기술"
      ],
      "pitfalls": [
        "원자료 미전송을 완전한프라이버시보장으로쓰지않습니다.",
        "암호화집계가악성입력까지 정상화한다고하지 않습니다."
      ],
      "recall": [
        "FedAvg에서표본가 중을쓰는이유는무엇입니까?",
        "원자료를 안보내도누출될수 있는 정보는 무엇입니까?",
        "secureaggregation과DP는 어떻게다릅니까?"
      ],
      "source_ids": [
        "sys-fedavg",
        "sys-aml"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "128-3-6",
          "items": [
            "동작 원리",
            "주요 알고리즘",
            "보안·프라이버시 기술"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "privacy-by-design",
      "title": "Privacy by Design의 7원칙과 8전략",
      "domain": "개인정보·컴플라이언스",
      "aliases": [],
      "easy": "완성된 제품에 동의창 하나를 붙이는 데서 끝내지 않고, 목적·데이터·기본 설정·이용자 권리를 설계의 재료로 둡니다.",
      "definition": "PbD는IT·업무·인프라의 설계 단계부터 프라이버시를 내재화하는방법론입니다. 7원칙은 설계방향을, 8전략은그방향을구체적인데이터·조직 설계 행동으로 번역하는데도움을줍니다.",
      "principles": [
        "7원칙은 사후대응보다 사전예방, 기본 설정으로 서의프라이버시, 설계에 내재화, 기능과 보호의 상생, 수명 주기전체 보호, 가시성과투명성, 사용자 프라이버시존중입니다. 보호를 사용자가 힘들게설정해야얻는옵션으로만두지않습니다.",
        "Hoepman의8전략은데이터중심minimise/hide/separate/abstract와 절차중심inform/control/enforce/demonstrate로정리합니다. 일부문헌의 aggregate표기와현저자판abstract용어를 구분합니다. 최소수집·암호화·분리·거친추상화·설명·선택·집행·증빙으로설계에 연결합니다.",
        "개인정보 보호 법제3조의목적명확·최소처리·목적 범위·정확성·안전 관리·공개·권리·사생활최소화등과 방향을비교할 수 있으나국내 법 조문전항과완전일대일 대응 표라고단정하지 않습니다. 기술·정책·UI·운영이 같이동작해야 하며 영향 평가와 잔여위험을 문서화합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "7원칙",
            "어떤가치를 기본으로 둘것인가",
            "기본 보호·내재화"
          ],
          [
            "8전략",
            "어떤설계 행동을 할것인가",
            "데이터·절차 행동"
          ],
          [
            "법적의무",
            "무엇을준수해야 하는가",
            "대상·판본·근거 확인"
          ]
        ]
      },
      "example": {
        "title": "위치 기반 알림 앱",
        "input": "근처매장알림에위치가필요한 가정",
        "steps": [
          "필요시점에만 위치를읽고정확좌표대신 영역 정보사용을검토합니다.",
          "기본추적은최소화하고 목적·보관기간을 설명합니다.",
          "사용자가 일시정지·삭제·동의철회를쉽게하도록설계합니다.",
          "실제로그·SDK·백업까지 정책이 집행되는지증빙합니다."
        ],
        "result": "원칙을 데이터 필드·기본 설정·권리흐름·운영 증거로 구현합니다.",
        "caution": "국내 법제3조최신 원문전항은미열람이며 본비교는방향성설명입니다."
      },
      "answer_outline": [
        "배경·정의",
        "7원칙",
        "8전략",
        "법 원칙방향비교",
        "설계예"
      ],
      "pitfalls": [
        "암호화하나로PbD가 완료됐다고하지 않습니다.",
        "동의만받으면최소수집이 불필요하다고쓰지않습니다."
      ],
      "recall": [
        "기본 설정 프라이버시는 어떤UI결정을 뜻합니까?",
        "separate와abstract는 어떻게다릅니까?",
        "demonstrate는 어떤증거를 요구합니까?"
      ],
      "source_ids": [
        "sys-pbd",
        "sys-pds"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "133-2-5",
          "items": [
            "PbD7원칙",
            "8전략",
            "개인정보 보호 법3조비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "safe-data-zones-cbpr",
      "title": "개인정보 안심구역·데이터안심구역·CBPR",
      "domain": "개인정보·컴플라이언스",
      "aliases": [],
      "easy": "안전한 분석 공간과 국경 간 처리의 책임 인증은 데이터 활용을 돕지만, 법적 근거와 반출 통제를 대신 하지 않습니다.",
      "definition": "개인정보안심구역은가명정보등을 안전한 분석 환경에 서 활용하도록지원하는공간·체계이며 데이터안심구역은외부 공개가 어려운데이터의 분석을 통제된환경에 서 지원하는제도맥락을가집니다. CBPR은APEC프라이버시 원칙에 기반한 국경간처리 책임의 자율인증체계입니다.",
      "principles": [
        "안심구역은이용자 승인·목적 검토·접근 통제·반입검사·보호된분석·로그·결과반출 심사를 연결합니다. 물리적으로안전한 방이거나인터넷차단이라는 조건만 으로재식별·통계 결과 누출이 사라지지않습니다. 두국내 제도의 주관·법적근거·대상·지정요건은 원문별로 분리 확인합니다.",
        "APEC9원칙은 피해예방, 고지, 수집제한, 개인정보이 용, 선택, 정확성/무결성, 보호조치, 열람·정정, 책임성입니다. 인증은 조직 정책·실행을 책임 기관이 평가하는맥락이며 국외이전의모든 국가 법 요건을 자동대체하지 않습니다.",
        "CBPR과PRP및후속GlobalCBPR의구분·현행 운영은 시점별 확인사항입니다. 기업은정보 흐름·처리자/수탁자·수신국·하위처리·목적·정보 주체 권리·사고 대응을 추적하고 인증서 범위·유효성·계약을 확인해야합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "개인정보안심구역",
            "가명정보 활용·보호 환경",
            "재식별·반출위험 관리"
          ],
          [
            "데이터안심구역",
            "통제 분석 환경·이용 지원",
            "데이터 종류·지정요건 확인"
          ],
          [
            "CBPR",
            "국경간처리 책임 인증",
            "이전근거·국내 법별도"
          ]
        ]
      },
      "example": {
        "title": "외부 연구자의 분석",
        "input": "기관 데이터를 연구자가분석후통계만 반출",
        "steps": [
          "목적과 필요필드를 검토하고 승인된환경에 반입합니다.",
          "원자료 접근과 분석 도구·로그를 통제합니다.",
          "소수 집단·개별추정가 능성이있는 결과를 반출 심사합니다.",
          "반출결과·이용 종료·데이터파기를기록합니다."
        ],
        "result": "입력 기밀성뿐 아니라결과 공개 위험과 책임을 관리합니다.",
        "caution": "국내지정요건 전문·CBPR인증 기준 전문 미열람.공식 기관검색본문에서9원칙·제도 개요만 확인했습니다."
      },
      "answer_outline": [
        "제도 목적",
        "두구역비교",
        "분석·반출흐름",
        "9원칙·인증",
        "법적한계"
      ],
      "pitfalls": [
        "안심구역이면임의재식별이허용된다고쓰지않습니다.",
        "CBPR인증이면 모든 국외이전이합법이라 고하지 않습니다."
      ],
      "recall": [
        "분석 환경과 반출결과를 왜같이검사합니까?",
        "개인정보안심구역과데이터안심구역의범위를 왜확인합니까?",
        "인증이 국내 법을 자동대체하지 않는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-safezone",
        "sys-privacy-guides",
        "sys-cbpr"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "135-1-7",
          "items": [
            "개인정보안심구역"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-1-10",
          "items": [
            "개인정보·데이터안심구역비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "133-2-6",
          "items": [
            "데이터안심구역정의·기능·지정요건"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-3-5",
          "items": [
            "APEC9원칙",
            "CBPR인증 기준"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "isms-compliance-governance",
      "title": "ISMS·ISMS-P·간편인증과 정보 보호 컴플라이언스",
      "domain": "개인정보·컴플라이언스",
      "aliases": [],
      "easy": "법과 인증 요구를 체크표로 만 남기지 않고 자산·위험·책임자·운영 증거·개선으로 이어 관리합니다.",
      "definition": "정보 보호컴플라이언스는적용 법령·계약·내부 정책·표준의 요구를 식별하고 통제를 구현·검증·개선하는활동입니다. ISMS는 정보 보호 관리체계인증, ISMS-P는 개인정보 처리 단계 보호까지 포괄하는통합 관리체계인증입니다.",
      "principles": [
        "관리 흐름은 경영진지원·범위·조직 정책수립 → 자산·위험식별평가 → 보호대책선정·구현 → 운영 점검·감사 → 결함개선·재평가입니다. 인증 범위 밖시스템·위탁·개발·운영 책임과 예외를 명시합니다. 정책은 의도와책임을 정하고 절차·지침은 실제 수행방법으로 연결합니다.",
        "기술 통제만 아니라교육·인사·공급자·사고 대응·업무연속성·개인권리·물리보호를 다룹니다. 증거는 접근 권한 승인·회수, 취약점조치, 백업 복원, 로그 점검, 사고훈련등실제 운영 기록이 어야합니다. 인증서가 사고0을 보장하지 않습니다.",
        "ISMS 의무 대상과 간편인증 적용 기준·항목수·최신 인증 영역은 법과 고시의 시점별원문으로 확인해야합니다. 2023안내서·2024간편항목 목록을 2026변경후요건이라 사칭하지 않습니다. 강화방안은NHI·클라우드·AI·공급망의실제 범위 반영, 위험 기반증빙과지속감시라는제안으로구분합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "ISMS",
            "정보 보호 관리·보호대책",
            "인증 범위·의무 대상 확인"
          ],
          [
            "ISMS-P",
            "개인정보 처리 단계포함",
            "권리·생애주기증빙"
          ],
          [
            "준수운영",
            "법·계약·정책매핑",
            "통제 실행·책임·개선"
          ]
        ]
      },
      "example": {
        "title": "신규 AI SaaS의 준수 검토",
        "input": "기존 인증 조직이 외부AI서비스를 추가 하는가정",
        "steps": [
          "개인정보·비밀·모델입출력 흐름과 계약을 새범위로 검토합니다.",
          "적용 요구를 통제·소유자·증거·점검 주기에 매핑합니다.",
          "권한·유출·보관·사고통지·종료 삭제를 시험합니다.",
          "인증 범위 변경과 잔여위험을 정식절차로 관리합니다."
        ],
        "result": "기존 인증을 신규서비스전체의포괄보증으로 오해하지 않습니다.",
        "caution": "공식누리집소개와자료 목록만 확인;2026최신세부인증 항목·의무 기준·간편대상 전문은 미열람입니다."
      },
      "answer_outline": [
        "준수필요성",
        "법·정책·통제매핑",
        "관리과 정",
        "ISMS/P/간편구분",
        "개선제안"
      ],
      "pitfalls": [
        "미열람항목수를암기표로 확정하지 않습니다.",
        "인증을 개인정보 유출면책으로설명하지 않습니다."
      ],
      "recall": [
        "정책과 절차의 차이는무엇입니까?",
        "준수증거의 실효성을어떻게검증합니까?",
        "인증 범위가 중요한이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-isms",
        "sys-privacy-safety"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "131-3-6",
          "items": [
            "ISMS·ISMS-P차이",
            "의무 대상"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-3-6",
          "items": [
            "인증 영역·법 근거",
            "관리과 정",
            "간편인증",
            "강화방안"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-4-5",
          "items": [
            "준수개념",
            "필요",
            "대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "132-4-6",
          "items": [
            "정보 보호 정책",
            "SecurityActionCycle",
            "전문가 역할"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "129-3-6",
          "items": [
            "정보 보호·개인정보구제측면ESG"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "iso42001-ai-management",
      "title": "ISO/IEC42001과 CAT의 보증 범위",
      "domain": "AI 거버넌스·법·윤리",
      "aliases": [],
      "easy": "하나의 모델 점수와 조직이 AI를 책임 있게 운영하는 체계는 다른 평가 대상입니다.",
      "definition": "ISO/IEC42001:2023은 조직의 AI경영시스템을 수립·구현·유지·지속개선하기위한요구와 지침을 제공하는 표준입니다. CAT는 TTA의인공지능 신뢰성검·인증체계로평가 대상·범위를 정해심사와 시험을 수행합니다.",
      "principles": [
        "ISO공식 개요는 AI관련정책·목표·프로세스를 조직의 맥락안에두고PDCA로관리한다고설명합니다. AI개발·제공·사용조직에 적용할 수 있고위험과 기회·책임·투명성·추적성을관리합니다. 일반 보안관리와 AI의데이터·편향·설명·생애주기 위험을 연결합니다.",
        "이번에읽은CAT 현행가 이드는제품·서비스의 AI위험 관리(ISO23894), 신뢰성확보조치(TR24028참고), 조직의 AI경영시스템(42001), AI사용거버넌스(38507)의서로 다른 범위를 제시합니다. 문서·절차 심사와 측정·기능 시험을 구분하며 인증이 특정 위험0의증명이아님을명시합니다.",
        "실무준비는대상·적용 범위·AI목록·이해관계자·역할·정책·위험 평가·처리·운영 통제·감시·감사·개선의증거를 연결하는방향으로설명할 수 있습니다. 이것을42001조항 전문이나 필수서류목록으로 사칭하지 않습니다. 다른 인증을 받아도국내 법 의무는 별도 확인합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "AI RMF",
            "자발적위험 관리 프레임워크",
            "인증 규격아님"
          ],
          [
            "ISO42001",
            "조직AI경영시스템 표준",
            "원문 조항·범위 확인"
          ],
          [
            "CAT",
            "정해진 대상·범위의 검인증",
            "판본·심사·시험구분"
          ]
        ]
      },
      "example": {
        "title": "조직 인증과 챗봇 성능",
        "input": "업체가AI경영시스템 보증을 설명하는 가정",
        "steps": [
          "인증서의 조직·제품·서비스 대상과 범위를 확인합니다.",
          "정책·위험·책임·운영 증거를 검토합니다.",
          "특정 챗봇의환각률·편향·보안시험 결과는 별도 검증합니다.",
          "2025기출 당시제도와 현행가 이드의용어·범위차이를기록합니다."
        ],
        "result": "관리체계의보증과 개별모델의 실제 품질을 구분합니다.",
        "caution": "ISO42001유료전문·부속통제·인증 심사 세부항목은 미열람입니다.현행 CAT소개가2025당시요건전부를확인해주지는않습니다."
      },
      "answer_outline": [
        "정의·대상",
        "PDCA운영",
        "RMF/ISO/CAT비교",
        "심사·시험 증거",
        "미열람경계"
      ],
      "pitfalls": [
        "ISO42001인증이면 모든 모델이 정확·안전하다고하지 않습니다.",
        "ISO소개만으로조항별적합판정을하지 않습니다."
      ],
      "recall": [
        "AI경영시스템과 모델 시험의 대상은 어떻게다릅니까?",
        "CAT 범위를 먼저 확인해야 하는이유는무엇입니까?",
        "PDCA에서개선의증거는 무엇입니까?"
      ],
      "source_ids": [
        "sys-42001",
        "sys-cat",
        "sys-airmf"
      ],
      "validation": "부분 확인",
      "version_note": "ISO42001판1(2023-12)공식소개와열람시현행 CAT가 이드만확인.표준 전문·2025CAT전판미열람.",
      "requirements": [
        {
          "question": "138-1-3",
          "items": [
            "ISO/IEC42001:2023"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "137-1-8",
          "items": [
            "AI신뢰성검인증 CAT"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "ai-ethics-user-protection",
      "title": "국내 AI 윤리·메타버스 윤리·이용자 보호",
      "domain": "AI 거버넌스·법·윤리",
      "aliases": [],
      "easy": "윤리 원칙은 선언문에 머물지 않고 누구의 피해를 어떻게 줄이고 누가 이의를 처리할지로 구체화합니다.",
      "definition": "AI윤리는AI생애주기의 영향을 인간의권리·공공선·책임관점에서판단하는기준입니다. 2020국내 기준의 최고가치는 인간성이며 메타버스윤리는가상자아와상호작용·지속가능한 생태계의 특성을 반영합니다.",
      "principles": [
        "국내AI3원칙은 인간존엄성·사회의 공공선·기술의 합목적성입니다. 10요건은 인권보장·프라이버시 보호·다양성존중·침해금지·공공성·연대성·데이터 관리·책임성·안전성·투명성입니다. 생성AI에는허위정보·차별·저작권·사생활·딥페이크·과신·접근격차의문제가 연결됩니다.",
        "메타버스3지향가치는 온전한자아·안전한 경험·지속가능한 번영이며 8원칙은 진정성·자율성·호혜성·사생활존중·공정성·개인정보 보호·포용성·책임성입니다. 인터넷의정보교환, AI의자동판단, 메타버스의몰입·가상자아라는강조점을비교하되공통권리원칙을 배타적으로나누지않습니다.",
        "2025생성AI이 용자 보호가 이드는인격권보호, 결정과 정알림노력, 다양성존중, 입력 데이터 관리, 콘텐츠활용의 문제해결책임·참여, 건전유통·배포의 6실행 방식을 제시합니다. 기출이 4개를요구하면 그중 4개와중요이유를설명하며 전체가 4개라고쓰지않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "AI윤리",
            "학습·자동판단·권리",
            "3원칙·10요건"
          ],
          [
            "메타버스윤리",
            "가상자아·몰입·생태계",
            "3가 치·8원칙"
          ],
          [
            "이용자 보호",
            "서비스 고지·관리·구제",
            "6방식중요구한 4개선택"
          ]
        ]
      },
      "example": {
        "title": "이미지 생성 서비스의 이용자 보호",
        "input": "실존인물딥페이크·입력사진학습 활용 위험 가정",
        "steps": [
          "인격권침해콘텐츠의예방·신고·중단절차를 둡니다.",
          "생성물임을알리고모델의 제약을이해하기쉽게설명합니다.",
          "입력사진학습 활용 고지·선택·삭제 정책을 운영합니다.",
          "집단별편향·신고처리·반복위반을지속평가합니다."
        ],
        "result": "원칙을 고지·데이터·콘텐츠·구제의실제 흐름으로 전환합니다.",
        "caution": "2025가 이드PDF전문직접 열람은타임아웃;공식 기관색인본문에서실행 방식 확인.디지털역기능3대이슈원출처분류는 미확인입니다."
      },
      "answer_outline": [
        "AI3·10",
        "메타버스3·8",
        "세윤리비교",
        "이용자 보호4실행예",
        "피해·구제"
      ],
      "pitfalls": [
        "윤리기준을 곧바로법률벌칙으로쓰지않습니다.",
        "딥페이크탐지 정확도만 으로문제를 종결하지 않습니다."
      ],
      "recall": [
        "AI윤리의합목적성은 어떤판단입니까?",
        "메타버스포용성은접근 설계와 어떻게연결됩니까?",
        "이용자 입력을 학습에 쓸때무엇을정해야합니까?"
      ],
      "source_ids": [
        "sys-aiethics",
        "sys-metaverse-ethics",
        "sys-ai-user-guideline",
        "sys-genai-profile"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "129-1-2",
          "items": [
            "AI윤리3원칙·10요건"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "136-4-1",
          "items": [
            "AI윤리기준",
            "생성AI역기능"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-2-5",
          "items": [
            "메타버스3가 치·8원칙",
            "인터넷·AI·메타버스윤리비교"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "138-3-1",
          "items": [
            "가이드배경·필요",
            "실행 방식 4개·중요이유"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "130-2-6",
          "items": [
            "디지털역기능정의·사례",
            "3대이슈",
            "대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "134-4-3",
          "items": [
            "AI법·윤리·기술 문제와 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "korean-ai-basic-act",
      "title": "AI기본법·고영향 AI와 사업자 책무",
      "domain": "AI 거버넌스·법·윤리",
      "aliases": [],
      "easy": "고영향 분야에 쓰인다는 분류와 실제 중대한 영향·위험, 사업자의 지위·책무·판본을 함께 확인합니다.",
      "definition": "인공지능기본법은 산업 발전과 안전·신뢰 기반을 함께 다루는 국내 기본법입니다. 고영향 AI는 사람의 생명, 신체의 안전 및 기본권에 중대한 영향이나 위험을 초래할 우려가 있는 시스템으로서 법이 정한 영역에서 활용되는 것을 말합니다.",
      "principles": [
        "법제처 공식 해설은 에너지 공급, 먹는물 생산 공정, 보건의료 체계, 의료기기·디지털의료기기, 원자력 안전, 수사·체포용 생체인식, 채용·대출 등 중요한 평가, 교통의 주요 작동, 공공 자격·징수 등 의사결정, 초·중등 학생 평가와 그 밖의 중요한 영역을 열거합니다. 단순히 AI를 사용한다는 사실만으로 고영향 여부를 확정하지 않습니다.",
        "현행제34조는위험 관리방안, 기술적으로가능한 결과·주요 기준·학습 데이터 개요 설명, 이용자 보호, 사람의 관리·감독, 조치문서작성·보관, 그밖에위원회심의사항의6책무를 규정합니다. 대통령령에따른구체이행·다른 법조치의준수간주는 해당원문 확인이 필요합니다.",
        "현행제6조는3년마다기본 계획을 수립하고 정책전략·인력/기반·윤리/법문화·재원투자·공공데이터 학습활성화·신뢰·사회변화·교육·취약계층 접근등을 다룹니다. 제7조의위원회는 대통령소속주요 정책심의·의결기구입니다. 산업 지원은 R&D·학습 데이터·인력·도입확산등과 연결하되법정조문별조건은 미확인입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "법정사실",
            "읽은판본·조문·영역",
            "제6·7·34조및공식 해설"
          ],
          [
            "해석·적용",
            "실제 용도·영향·사업자지위",
            "개별 사실과하위법 검토"
          ],
          [
            "운영조치",
            "위험·설명·보호·감독·문서",
            "이행증빙·재평가"
          ]
        ]
      },
      "example": {
        "title": "채용 AI 도입기관 검토",
        "input": "외부 모델로 지원자순위를추천하는서비스 가정",
        "steps": [
          "사업자·이용자지위와실제 채용영향을 정리합니다.",
          "법정영역·영향을 검토하고 필요시공식 확인 절차를 확인합니다.",
          "위험·설명·이용자 보호·감독·문서화활동을담당자와증거로 연결합니다.",
          "관련개인정보·차별·노동법 요구도 별도 검토합니다."
        ],
        "result": "법정분류와 위험 관리 실행을 연결하며 자동준수판정을하지 않습니다.",
        "caution": "138기출의최초시행2026-01-22판과열람한현행2026-07-21판은다릅니다.시행령·고시 전문·최초판전조문·산업시책4조문은 미열람입니다."
      },
      "answer_outline": [
        "법 목적·판본",
        "기본 계획·위원회",
        "고영향정의·영역",
        "6책무",
        "적용예·하위법 미확인"
      ],
      "pitfalls": [
        "고영향과 생성형AI를 동일분류로 쓰지않습니다.",
        "현행 개정 내용을 기출 당시내용으로 소급하지 않습니다."
      ],
      "recall": [
        "고영향판단에영역만 확인하면 충분합니까?",
        "설명 책무가 다루는 정보는 무엇입니까?",
        "문서화가위험 관리와 어떻게연결됩니까?"
      ],
      "source_ids": [
        "sys-aiact",
        "sys-aiact-plan",
        "sys-ai-committee",
        "sys-aiact-official-guide",
        "sys-aiact-history"
      ],
      "validation": "부분 확인",
      "version_note": "제정판연혁2025-01-21/2026-01-22와 현행 법률 21311호2026-07-21을 분리.현행제6·7·34직접 열람, 정의·영역은 법제처 공식 해설.",
      "requirements": [
        {
          "question": "138-4-1",
          "items": [
            "목적·원칙",
            "기본 계획",
            "전략위원회",
            "산업육성시책4"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "140-3-6",
          "items": [
            "고영향정의",
            "활용 영역",
            "안전·신뢰확보활동"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "adversarial-ai-security",
      "title": "AI 리스크·적대적 학습 공격·모델 전도",
      "domain": "AI 보안",
      "aliases": [],
      "easy": "모델이 틀릴 수 있다는 품질 문제와 공격자가 데이터·입력·출력을 이용해 의도적으로 실패시키는 위협을 구분합니다.",
      "definition": "AI리스크는사용맥락에서AI가 야기할 수 있는 피해의가능성과영향입니다. 적대적ML은 공격자의목표·지식·능력·생애주기위치에따라 오염·회피·기밀추론·모델 탈취·오용등을 분석합니다.",
      "principles": [
        "학습 단계poisoning은 데이터·라벨·모델 업데이트등을 조작해전체성능저하나조건부백도어를유도합니다. 추론 단계evasion은 입력을 조작해오분류·우회를노립니다. model extraction은 질의·응답등으로기능을 복제하고 membership inference는 특정 기록의 학습 참여 여부를추정합니다. 기출의4분류는 분류축을먼저 명시합니다.",
        "모델 전도/model inversion은 출력·파라미터등에서입력 특성이나 민감 자료를 추론·복원하는공격입니다. 전도 결과가 항상 특정 개인의실제 원본과 일치한다는뜻은아닙니다. 접근제한·출력 정밀도/질의량·DP·학습 최소화·공격 평가를 상황에 맞게적용합니다.",
        "보안 위험은 오염·탈취·프롬프트주입·권한남용, 프라이버시 위험은 학습 자료·입출력 누출·재식별, 사회 위험은 차별·허위정보·조작·의존·권력집중등으로구분합니다. provenance·검증집합·강건성평가·데이터정제·접근 분리·운영 감시와 피해 구제를전생애주기에 연결합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "오염",
            "학습 자료·업데이트변조",
            "출처·검증·강건 집계"
          ],
          [
            "회피",
            "추론 입력조작",
            "위협 모델·강건성·입력 통제"
          ],
          [
            "프라이버시 공격",
            "참여·특성·원문 추정",
            "출력·질의·DP·수집제한"
          ]
        ]
      },
      "example": {
        "title": "고객분류 모델의 누출 평가",
        "input": "확률벡터를무제한공개하는API 가정",
        "steps": [
          "공격자가어떤출력·지식·질의량을얻는지정의합니다.",
          "회원추론·전도·추출을별도로시험하고 실제 원본일치여부를검증합니다.",
          "필요이상의출력·반복질의와 접근 권한을 줄입니다.",
          "유용성저하와잔여위험을 측정하며 모니터링합니다."
        ],
        "result": "공격 목표·관측·방어효과를 분리하고 단일방어의한계를 기록합니다.",
        "caution": "공격 분류는 문헌별로 다릅니다.방어가특정 위협 모델밖에서도완전보호한다는보장은없습니다."
      },
      "answer_outline": [
        "리스크범주",
        "공격생애주기도 식",
        "4공격비교",
        "전도·회원추론구분",
        "다층대응"
      ],
      "pitfalls": [
        "모든 AI오류를 적대적공격이라 하지 않습니다.",
        "전도와 모델 파라미터추출을동일시하지 않습니다."
      ],
      "recall": [
        "오염과 회피는 어느단계가 다릅니까?",
        "회원추론과 전도는 무엇을알아내려합니까?",
        "보안·프라이버시·사회적위험을 한사례에서 구분하십시오."
      ],
      "source_ids": [
        "sys-aml",
        "sys-genai-profile",
        "sys-airmf"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "130-3-4",
          "items": [
            "적대적공격4·방어",
            "생성형취약점"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "138-1-13",
          "items": [
            "ModelInversion"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "139-2-1",
          "items": [
            "AI리스크",
            "보안",
            "프라이버시",
            "사회적리스크"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "131-4-4",
          "items": [
            "파운데이션모델 법·환경·사회고려"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "136-1-2",
          "items": [
            "범용 AI 위험 관리 프레임워크의 맥락과 위험 분류"
          ],
          "section": "핵심원리/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "llm-owasp-mcp-autonomy",
      "title": "OWASP LLM2025·프롬프트 주입·MCP·자율성 통제",
      "domain": "AI 보안",
      "aliases": [],
      "easy": "모델이 읽은 외부 문장을 명령으로 오해하더라도 실제 도구가 권한 밖의 일을 못 하도록 시스템에 서 경계를 둡니다.",
      "definition": "LLM보안은모델·데이터·검색·프롬프트·출력·도구·실행 권한을 포함하는 응용전체 보안입니다. 프롬프트인젝션은신뢰하지 않는입력이 모델의 의도된정책·작업을 변경하도록유도하는취약점이며 직접 입력과 검색문서등간접경로를 구분합니다.",
      "principles": [
        "OWASP2025의10항목은 프롬프트주입, 민감정보 노출, 공급망, 데이터/모델 오염, 부적절출력 처리, 과도한에이전시, 시스템프롬프트누출, 벡터/임베딩취약점, 허위정보, 무제한소비입니다. 이전판번호와 섞지말고발생지점·영향·대응을 연결합니다.",
        "MCP는 모델과 도구·자원을 연결하는프로토콜이 지만도구 설명·응답의 신뢰, OAuth동의, 대상audience·토큰 검증, confused deputy, token passthrough, SSRF, 로컬서버 실행이 공격면입니다. 서버허용목록·서명/검토·최소scope·리소스별인가·비밀격리·감사를적용합니다.",
        "고성능AI의사이버 공격 지원은 피싱·정찰·코드생성·자동화 규모를 늘릴수 있어접근·오용탐지·위험능력평가가 필요합니다. 자율성위험은 목표오해·권한과 다·연쇄행동·예산폭주로설명하고 읽기/쓰기 분리·허용도구·고위험 행위 승인·격리·지출/시간한도·중단/복구를 설계합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "모델수준",
            "정렬·강건성평가",
            "정책이 탈가능성잔존"
          ],
          [
            "응용수준",
            "출력 검증·권한·실행격리",
            "비밀·SQL·도구 경계"
          ],
          [
            "운영수준",
            "감시·승인·중단·복구",
            "자율성·규모·사고 대응"
          ]
        ]
      },
      "example": {
        "title": "검색 문서의 악성 지시",
        "input": "문서본문에비밀을외부로 보내라는문장포함",
        "steps": [
          "문서를 데이터로 취급하고 명령권한을 주지않습니다.",
          "모델 출력과 무관하게도구 서버가 사용자·리소스 권한을 검증합니다.",
          "외부 전송·삭제·배포같은 중요작업은 구체대상과 내용을 검토합니다.",
          "실행 로그·예산·중단조건과 사고회수를 갖춥니다."
        ],
        "result": "필터한겹보다신뢰 경계와 최소 권한으로 실제 피해를제한합니다.",
        "caution": "프롬프트필터·정렬만 으로주입완전차단을 보장하지 않습니다.MCP는 열람시2026-07-28보안문서에 근거합니다."
      },
      "answer_outline": [
        "LLM전체 구조",
        "2025Top10",
        "MCP공격·대응",
        "공격 지원·자율성",
        "권한 경계예"
      ],
      "pitfalls": [
        "시스템프롬프트를절대비밀저장소로쓰지않습니다.",
        "모델이 안전하다고응답한것을인가판정으로쓰지않습니다."
      ],
      "recall": [
        "간접주입은어디서들어옵니까?",
        "MCP토큰 전달을 무조건 허용하면 왜위험합니까?",
        "자율성한도와사람 승인은 어떤행위에 필요합니까?"
      ],
      "source_ids": [
        "sys-owasp",
        "sys-mcp",
        "sys-aml"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "138-1-12",
          "items": [
            "PromptInjection"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "136-2-3",
          "items": [
            "LLM개발보안 위험3이 상·대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "136-4-5",
          "items": [
            "OWASP배경·특징",
            "2025주요 위협",
            "설계 운영 대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "137-2-3",
          "items": [
            "MCP취약·대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "140-2-6",
          "items": [
            "사이버 공격 지원 위협·대응",
            "통제상실위협·대응"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "133-3-2",
          "items": [
            "생성AI가 이드2023맥락의보안위협·개발 고려"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    },
    {
      "id": "ai-code-openweight-licensing",
      "title": "AI 생성 코드·오픈웨이트 라이선스와 컴플라이언스",
      "domain": "AI 거버넌스·법·윤리",
      "aliases": [],
      "easy": "생성된 결과나 내려받은 가중치가 자유이용을 뜻하지 않으므로 각 구성 요소의 출처·허용범위·배포 의무를 확인합니다.",
      "definition": "AI 라이선스 관리는 코드·의존성·모델 가중치·데이터·도구·출력에 적용되는 조건을 식별하고 사용·수정·배포·서비스 제공의 의무를 관리하는 활동입니다. 오픈웨이트는 가중치 공개를 뜻할 뿐, OSI의 오픈소스 AI 정의 충족을 자동으로 의미하지 않습니다.",
      "principles": [
        "MIT는 고지 유지가 핵심이며 Apache2.0은 라이선스·변경 고지·관련 NOTICE등과 특허 조건을 검토합니다. GPL은 배포·결합 관계에 따른 소스 제공 등의 조건을 확인해야 하고 AGPL의 네트워크 조항·모델 커스텀 사용 제한은 개별 원문을 확인합니다. 생성 코드의 유사성이 있으면 출처·권리·적용 조건을 검토하되 유사성 점수만으로 위반을 단정하지 않습니다.",
        "점검은 출처·버전·저작권·SPDX식별·허용 용도·배포/수정·상표/특허·고지·소스 제공·재배포·사용 제한·데이터 권리·의존 조건을 포함합니다. 모델 라이선스와 추론 엔진코드 라이선스가 다를 수 있고 버전별 정책 변경을 추적합니다. SSPL/BSL을 무조건 OSI승인 오픈소스라하지 않습니다.",
        "통합 절차는 인벤토리/SBOM·모델 목록 → 자동탐지/SCA·ScanCode등 → 정책 분류·법무/권리검토 → 승인·고지/소스 준비 → 릴리스 게이트 → 운영 모니터링·업데이트입니다. OSI1.0은 이용·연구·수정·공유 자유와 수정에 필요한 데이터 정보·코드·파라미터를 다룹니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "코드 라이선스",
            "저작권·배포·결합조건",
            "생성출력도 검토"
          ],
          [
            "모델 가중치 조건",
            "이용·재배포·사용 제한",
            "오픈웨이트≠자동오픈소스"
          ],
          [
            "스캔·심사",
            "탐지·정책·권리 판단",
            "도구는 법적완전판정아님"
          ]
        ]
      },
      "example": {
        "title": "AI가 제안한 함수의 배포",
        "input": "코드조각과 오픈웨이트모델을 제품에 포함하는 가정",
        "steps": [
          "생성 코드의 유사원본·의존성과모델정확버전을 기록합니다.",
          "해당라이선스의 이용·수정·배포 조건을 각각 검토합니다.",
          "필요고지·소스 제공·사용 제한준수증거를 릴리스에연결합니다.",
          "스캔미검출과권리확보를동일시하지 않고잔여이슈를검토합니다."
        ],
        "result": "생성 시점부터 업데이트까지 추적가능한 정책과 증빙을만듭니다.",
        "caution": "개별저작권침해·파생저작물·계약효력의법적 판단은아닙니다.AGPl·SSPL·BSL·특정 모델 원문 전체는미열람입니다."
      },
      "answer_outline": [
        "리스크·구성 요소",
        "허용·카피레프트·커스텀조건",
        "점검 표",
        "통합거버넌스",
        "검증 도구 한계"
      ],
      "pitfalls": [
        "공개 가중치면상업이용·재배포가 항상 자유롭다고쓰지않습니다.",
        "AI가 만든코드는 저작권이없다고단정하지 않습니다."
      ],
      "recall": [
        "오픈웨이트와오픈소스 AI는 어떻게다릅니까?",
        "라이선스스캐너가확인못하는법적쟁점은무엇입니까?",
        "고지 의무는 릴리스어느단계에 서 검증합니까?"
      ],
      "source_ids": [
        "sys-mit",
        "sys-apache",
        "sys-gpl",
        "sys-osaid",
        "sys-scancode"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "140-2-2",
          "items": [
            "AI코드주요의무·위험",
            "주요 점검",
            "AI거버넌스통합 절차·도구"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        },
        {
          "question": "134-3-6",
          "items": [
            "라이선스 정책 변경배경·영향의 AI맥락"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "cryptanalysis-threat-models",
      "title": "암호 공격 모델과 암호문 공격",
      "domain": "보안·암호",
      "aliases": [],
      "easy": "공격자가 암호문만 갖는지, 원문을 알거나 암·복호 장치에 질의할 수 있는 지에 따라 요구되는 안전성을 다르게 평가합니다.",
      "definition": "암호 분석 공격 모델은 공격자가획득하는정보와 질의능력을정의한조건입니다. 암호문 단독공격은 암호문만 으로평문또는키에 관한정보를 얻으려는모델이고 알려진 평문·선택 평문·선택 암호문은 추가 정보·오라클능력이있습니다.",
      "principles": [
        "ciphertext-only는 암호문 통계·구조를 이용하고 known-plaintext는 원문/암호문쌍을가집니다. chosen-plaintext는 선택한 원문의 암호화 결과를 받고chosen-ciphertext는 제한조건하에서선택 암호문의 복호 결과·반응을얻습니다. 오라클은실제 서버의 에러·시간·API일수 있습니다.",
        "단순한키 길이보다안전한 스킴과무결성·오류 처리가 중요합니다. 패딩오류를 구별해주는응답은 평문 복원에 정보를 제공할 수 있어인증 암호·균일한오류·상수시간·질의통제등검증된방식을 사용합니다. 암호문을 바꿔도검출못하는모드는 공격 표면을 넓힙니다.",
        "Kerckhoffs원칙관점에서알고리즘을 숨기는것만안전성의 근거로 두지않고키를 보호합니다. 부채널·키 탈취·약한난수는수학적분석과 다른 경로이며 프로토콜·구현·운영을 함께 검토합니다. 모델의 가정밖위협까지 안전하다고확장하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "암호문 단독",
            "C만관측",
            "분포·패턴노출"
          ],
          [
            "알려진/선택 평문",
            "P, C쌍/암호화질의",
            "구별·구조 분석"
          ],
          [
            "선택 암호문",
            "복호반응질의",
            "인증·패딩·오류 통제"
          ]
        ]
      },
      "example": {
        "title": "오류 메시지의 정보 노출",
        "input": "변조암호문에 패딩오류와 인증 오류를 다르게응답하는가정",
        "steps": [
          "공격자가무엇을반복질의하고 관측하는지정의합니다.",
          "오류 종류·응답 시간차이가정보를 주는지안전한 환경에 서 평가합니다.",
          "검증된AEAD와 권장복호 절차로 태그검증전평문사용을막습니다.",
          "오류통일만으로충분한지구현·라이브러리 정책을 검토합니다."
        ],
        "result": "공격 모델을 명확히하면 암호 알고리즘과 운용스킴의방어범위를 구분할 수 있습니다.",
        "caution": "교육용위협 분석이며 특정 시스템 침입 절차를 제공하지 않습니다.선택 암호문보장의상세증명은원규격을 추가 확인합니다."
      },
      "answer_outline": [
        "모델정의",
        "네조건비교",
        "오라클·오류 사례",
        "AEAD·구현 대응",
        "가정 한계"
      ],
      "pitfalls": [
        "암호문 단독공격을 암호문을 변조하는공격하나로한정하지 않습니다.",
        "키 길이만으로모든 공격 모델 안전을 선언하지 않습니다."
      ],
      "recall": [
        "알려진 평문과 선택 평문의 차이는무엇입니까?",
        "오류 응답이 어떻게정보가 됩니까?",
        "알고리즘 공개와 키 보호를 구분하는이유는무엇입니까?"
      ],
      "source_ids": [
        "sys-rsa",
        "sys-tls",
        "sys-modes"
      ],
      "validation": "부분 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "137-1-4",
          "items": [
            "암호문 공격"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "devsecops-sbom-security-quality",
      "title": "DevSecOps·SBOM과 보안 품질 자동화",
      "domain": "보안·침해대응",
      "aliases": [],
      "easy": "보안을 마지막 검사 한 번에 맡기지 않고 코드·의존성·빌드·배포·운영에 검증과 책임을 연결합니다.",
      "definition": "DevSecOps는 개발·보안·운영이 보안목표와 책임을 공유하고 CI/CD수명 주기에 보안활동을통합하는접근입니다. SBOM은 소프트웨어구성 요소와관계를 표현하는목록이며 보안 품질은 기밀성·무결성·가용성등보호 요구를 만족하는제품·운영 특성으로 평가합니다.",
      "principles": [
        "NISTSSDF1.1은 조직준비(PO), 소프트웨어 보호(PS), 안전한 소프트웨어생산(PW), 취약점 대응(RV)의실무군을제시합니다. 보안 요구·위협 모델·안전 설계·구현 검토·시험·취약점접수/수정·원인 분석을 기존 개발 방법에 통합합니다.",
        "자동화는 커밋비밀탐지·SAST, 의존성SCA·라이선스, 컨테이너/IaC설정 검사, DAST/API보안시험, 서명·빌드출처검증, 배포 정책, 운영런타임탐지·패치로연결합니다. 탐지 규칙·심각도·실제도달성·예외 승인·기한·재검증을 관리하지 않으면경보가 쌓이거나배포를 불필요하게막습니다.",
        "SBOM의이름·버전·공급자·식별자·의존 관계등은 실제 배포물과연결해야합니다. 취약점 목록과 동일한 문서가 아니며새취약점발표시해당구성의영향을 찾는데도움이됩니다. 목록정확성·갱신·서명·취약점 DB·VEX같은적용성정보와 분석을 결합합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "핵심 원리",
          "적용·한계"
        ],
        "rows": [
          [
            "SAST/DAST",
            "소스/실행 행위 분석",
            "오탐·누락·범위"
          ],
          [
            "SCA/SBOM",
            "의존위험 분석/구성목록",
            "버전·도달성·갱신"
          ],
          [
            "배포·운영 통제",
            "서명·정책·관측",
            "권한·예외·사고복구"
          ]
        ]
      },
      "example": {
        "title": "새 취약점의 영향 추적",
        "input": "공통 라이브러리에 취약점 공개;여러 서비스 배포 가정",
        "steps": [
          "SBOM으로실제 포함버전과 배포 서비스를 찾습니다.",
          "공격가 능성과업무중요도를평가합니다.",
          "수정 버전 시험·서명·배포를 실행하고 예외는 기한과통제를 기록합니다.",
          "수정 확인과 유사결함의근본원인개선을수행합니다."
        ],
        "result": "보안 품질을 도구 실행횟수보다위험감소·조치완료·재발방지로검증합니다.",
        "caution": "도구가 모든 보안결함·라이선스위반을찾는것은아닙니다.SBOM형식필드전항은각규격 판본을 확인합니다."
      },
      "answer_outline": [
        "보안 품질과 책임",
        "SSDF4군",
        "파이프라인 검사도 식",
        "SBOM활용예",
        "지표·예외"
      ],
      "pitfalls": [
        "스캐너통과를절대안전 인증으로 쓰지않습니다.",
        "SBOM과 취약점스캔결과를 동일시하지 않습니다."
      ],
      "recall": [
        "보안자동화에 예외기한이필요한 이유는무엇입니까?",
        "SBOM이0-day발표후어떻게도움이됩니까?",
        "SSDF의취약점 대응은 개발에 무엇을환류합니까?"
      ],
      "source_ids": [
        "sys-ssdf",
        "sys-scancode"
      ],
      "validation": "출처 확인",
      "version_note": "명시한 출처 판본의 원리를 설명하며 제품별 구현 차이는 별도 확인합니다.",
      "requirements": [
        {
          "question": "135-2-2",
          "items": [
            "CI/CD의DevSecOps"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "136-4-6",
          "items": [
            "보안 품질정의·중요",
            "자동화 기술·도구",
            "SDLC구현",
            "효과"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "131-1-13",
          "items": [
            "SBOM"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        },
        {
          "question": "134-3-3",
          "items": [
            "오픈소스취약",
            "SBOM관리"
          ],
          "section": "핵심원리/비교표/예제",
          "status": "충족"
        }
      ]
    }
  ]
}
```
