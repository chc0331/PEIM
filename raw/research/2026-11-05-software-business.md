# 소프트웨어공학·사업관리·IT전략·경영융합 조사 요약

강사 생성 조사 요약입니다. 공식 답안이나 공식 채점기준이 아닙니다. 원자료는 Q-Net 126~140회 465문항의 저장된 record.json 전체를 읽고 담당 분야의 148개 문항에 연결했습니다. 하나의 문항을 여러 토픽이 나누어 설명하는 경우가 있으며, 소문항별 충족과 출처 검증 상태는 별도입니다.

확인일은 2026-11-05입니다. 외부 원문 전체를 전재하지 않고 URL·서지정보·자체 요약을 보관합니다. 표준의 공개 소개/미리보기만 읽은 경우, 지정 판본 원문을 찾지 못한 경우, 현행 법령의 최종 조문을 대조하지 못한 경우는 해당 토픽의 검증 상태와 판본 주석에 남겼습니다. 적용 예시는 기출 조건을 이용한 강사 구성 예 또는 자체 창작 예이며 실제 조직의 성과를 주장하지 않습니다. 학습자의 수행·점수·숙련도 기록은 포함하지 않았습니다.

```json
{
  "sources": [
    {
      "id": "sb-swebok",
      "title": "Guide to the SWEBOK v4.0a",
      "url": "https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf",
      "author": "IEEE Computer Society / Hironori Washizaki 편",
      "published": "2026-08",
      "checked_at": "2026-11-05",
      "notes": "공개 PDF 열람. 요구사항·설계·테스트·유지보수·형상관리·품질 장의 해당 절을 참조. 기출 당시 판본과 현재 v4.0a를 구분합니다."
    },
    {
      "id": "sb-ctfl",
      "title": "Certified Tester Foundation Level Syllabus v4.0.1",
      "url": "https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf",
      "author": "ISTQB",
      "published": "2024-09-15",
      "checked_at": "2026-11-05",
      "notes": "공개 PDF 열람. §1.3, §2.2, §3, §4, §5의 원리·기법·계획 범위를 확인했습니다. 자격시험 공식답안이라는 뜻은 아닙니다."
    },
    {
      "id": "sb-nasa-req",
      "title": "6.2 Requirements Management",
      "url": "https://www.nasa.gov/reference/6-2-requirements-management/",
      "author": "NASA",
      "published": "발행일 페이지 미표기",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-inspection",
      "title": "NASA-STD-8739.9 Software Formal Inspections Standard",
      "url": "https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/1/nasa-std-87399_with_change_1.pdf",
      "author": "NASA",
      "published": "2013 / Change 1",
      "checked_at": "2026-11-05",
      "notes": "공개 PDF의 요구사항 인스펙션 체크리스트와 절차를 열람했습니다. NASA 적용 기준을 국내 사업의 의무로 일반화하지 않습니다."
    },
    {
      "id": "sb-uml",
      "title": "OMG Unified Modeling Language 2.5.1",
      "url": "https://www.omg.org/spec/UML/2.5.1/PDF",
      "author": "OMG",
      "published": "2017-12",
      "checked_at": "2026-11-05",
      "notes": "공개 PDF를 /tmp에서 텍스트 추출해 Class, Interaction/Sequence, Activities, StateMachines, UseCases 절을 열람했습니다. 127회 문항은 UML2.0을 명시하므로 공통 핵심 표기를 사용합니다."
    },
    {
      "id": "sb-atam",
      "title": "ATAM: Method for Architecture Evaluation",
      "url": "https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/",
      "author": "Rick Kazman, Mark Klein, Paul Clements / CMU SEI",
      "published": "2000-08-01",
      "checked_at": "2026-11-05",
      "notes": "보고서 CMU/SEI-2000-TR-004와 연결된 공개 PDF 열람. 9단계·품질속성 시나리오·민감점/절충점의 의미를 확인했습니다."
    },
    {
      "id": "sb-cbam",
      "title": "Using Economic Considerations to Choose Among Architecture Design Alternatives",
      "url": "https://www.sei.cmu.edu/documents/670/2001_005_001_13916.pdf",
      "author": "Jayatirtha Asundi, Rick Kazman, Mark Klein / CMU SEI",
      "published": "2001-12",
      "checked_at": "2026-11-05",
      "notes": "CBAM 원 보고서 공개 PDF 열람. 효용·시나리오 우선순위·전략 비용과 편익의 결합을 참조합니다."
    },
    {
      "id": "sb-parnas",
      "title": "On the Criteria To Be Used in Decomposing Systems into Modules",
      "url": "https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html",
      "author": "David L. Parnas",
      "published": "1972",
      "checked_at": "2026-11-05",
      "notes": "원 논문을 대학 공개 강의자료에서 열람. 변경 가능한 설계 결정을 모듈 내부에 숨기는 분해 기준을 참조합니다."
    },
    {
      "id": "sb-spl",
      "title": "Software Product Lines Curriculum",
      "url": "https://www.sei.cmu.edu/library/software-product-lines-curriculum/",
      "author": "CMU SEI",
      "published": "2020-11-20",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-scrum",
      "title": "The Scrum Guide",
      "url": "https://scrumguides.org/scrum-guide.html",
      "author": "Ken Schwaber, Jeff Sutherland",
      "published": "2020-11",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-kanban",
      "title": "The Kanban Guide",
      "url": "https://kanbanguides.org/the-kanban-guide/2025.5/",
      "author": "Kanban Guides 공동 저자",
      "published": "2025-05-01",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-springboot",
      "title": "Auto-configuration",
      "url": "https://docs.spring.io/spring-boot/reference/using/auto-configuration.html",
      "author": "Spring",
      "published": "열람 화면 Spring Boot 4.1.2",
      "checked_at": "2026-11-05",
      "notes": "현재 문서 열람. 기출 당시 Spring Boot 세대와 차이가 있으므로 특정 Java 최소버전·패키지명을 일반화하지 않습니다."
    },
    {
      "id": "sb-aop",
      "title": "Aspect Oriented Programming with Spring",
      "url": "https://docs.spring.io/spring-framework/reference/core/aop.html",
      "author": "Spring",
      "published": "열람 화면 Spring Framework 7.0.10",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-refactoring",
      "title": "Refactoring",
      "url": "https://refactoring.com/",
      "author": "Martin Fowler",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-debt",
      "title": "Technical Debt",
      "url": "https://martinfowler.com/bliki/TechnicalDebt.html",
      "author": "Martin Fowler",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "최초 open 본문과 기술부채 의미를 확인했습니다. 뒤의 find 재요청은 오류였으므로 사분면 세부는 별도 원문 확인이 필요합니다."
    },
    {
      "id": "sb-rest",
      "title": "Architectural Styles and the Design of Network-based Software Architectures, Chapter 5",
      "url": "https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm",
      "author": "Roy T. Fielding / UC Irvine",
      "published": "2000",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-soap",
      "title": "SOAP Version 1.2 Part 1: Messaging Framework (Second Edition)",
      "url": "https://www.w3.org/TR/soap12/",
      "author": "W3C",
      "published": "2007-04-27",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-webperf",
      "title": "Learn Performance",
      "url": "https://web.dev/learn/performance",
      "author": "Google web.dev",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-krds",
      "title": "리소스 다운로드 및 디지털 정부서비스 UI/UX 가이드라인",
      "url": "https://www.krds.go.kr/html/site/outline/outline_05.html",
      "author": "행정안전부 / KRDS",
      "published": "2024-02 / 2024-07 / 2025-08 판 제공",
      "checked_at": "2026-11-05",
      "notes": "공식 페이지와 2024판 가이드 설명을 실제 열람. 2019판의 7개 설계기준 원문과 같은 목록이라고 간주하지 않습니다."
    },
    {
      "id": "sb-govui",
      "title": "공공 웹·앱 UI/UX 혁신",
      "url": "https://www.mois.go.kr/frt/sub/a06/b04/uixInnovation/screen.do",
      "author": "행정안전부",
      "published": "지속 갱신 페이지",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-iso25010",
      "title": "ISO/IEC 25010:2023 Product quality model",
      "url": "https://www.iso.org/standard/78176.html",
      "author": "ISO/IEC",
      "published": "2023-11",
      "checked_at": "2026-11-05",
      "notes": "공식 초록 및 판본 메타데이터 열람. 유료 표준 전체 본문 미열람. 9개 주특성과 부특성 상세는 공개 제공 범위에서만 확인하며 전 목록의 규범적 번역은 추가 확인 필요합니다."
    },
    {
      "id": "sb-gs",
      "title": "GS시험인증(1등급)",
      "url": "https://cs.tta.or.kr/tta/introduce/introCont.do?tabMode=cont&tnc_cls_no=T000127&tnc_lab=T000003&up_tnc_cls_no=T000020",
      "author": "한국정보통신기술협회(TTA)",
      "published": "지속 갱신 페이지",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-monkey",
      "title": "UI/Application Exerciser Monkey",
      "url": "https://developer.android.com/studio/test/other-testing-tools/monkey",
      "author": "Google Android Developers",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-mutation",
      "title": "Mutation operators",
      "url": "https://pitest.org/quickstart/mutators/",
      "author": "PIT 프로젝트",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-metamorphic",
      "title": "Metamorphic Testing: A New Approach for Generating Next Test Cases",
      "url": "https://www.cse.ust.hk/faculty/scc/publ/CS98-01-metamorphictesting.pdf",
      "author": "T. Y. Chen, S. C. Cheung, S. M. Yiu",
      "published": "1998",
      "checked_at": "2026-11-05",
      "notes": "HKUST-CS98-01 원 논문 공개 PDF 열람. 변환 전후 관계에 의한 오류 탐지 근거입니다."
    },
    {
      "id": "sb-deepxplore",
      "title": "DeepXplore: Automated Whitebox Testing of Deep Learning Systems",
      "url": "https://arxiv.org/abs/1705.06640",
      "author": "Kexin Pei, Yinzhi Cao, Junfeng Yang, Suman Jana",
      "published": "2017",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-deepsafe",
      "title": "DeepSafe: A Data-driven Approach for Checking Adversarial Robustness in Neural Networks",
      "url": "https://arxiv.org/abs/1710.00486",
      "author": "Divya Gopinath, Guy Katz, Corina Pasareanu, Clark Barrett",
      "published": "2017",
      "checked_at": "2026-11-05",
      "notes": "원 논문 초록 열람. 기출의 안전 반경 최대화라는 번역이 이 특정 논문만을 지칭한다고 확정하지 않습니다."
    },
    {
      "id": "sb-dora",
      "title": "Capabilities: Continuous delivery",
      "url": "https://dora.dev/capabilities/continuous-delivery/",
      "author": "DORA",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-git",
      "title": "Pro Git: About Version Control",
      "url": "https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control",
      "author": "Scott Chacon, Ben Straub / Git",
      "published": "2판 온라인판",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-terraform",
      "title": "What is Terraform",
      "url": "https://developer.hashicorp.com/terraform/intro",
      "author": "HashiCorp",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-stpa",
      "title": "Books and Handbooks: STPA Handbook",
      "url": "https://psas.scripts.mit.edu/home/books-and-handbooks/",
      "author": "Nancy Leveson, John Thomas / MIT",
      "published": "2018-03",
      "checked_at": "2026-11-05",
      "notes": "공식 안내 페이지의 단계·이론·대상 범위 열람. get_file PHP 주소는 HTML을 반환해 전체 핸드북은 그 경로로 확보하지 못했습니다."
    },
    {
      "id": "sb-iso21500",
      "title": "ISO 21500:2021 Context and concepts",
      "url": "https://www.iso.org/standard/75704.html",
      "author": "ISO",
      "published": "2021-03",
      "checked_at": "2026-11-05",
      "notes": "공식 초록·판본 확인. 유료 전체본문 미열람. 구 2012판의 프로세스 모델과 현행 2021 개념표준을 구분합니다."
    },
    {
      "id": "sb-iso21502",
      "title": "ISO 21502:2020 Guidance on project management",
      "url": "https://www.iso.org/standard/74947.html",
      "author": "ISO",
      "published": "2020-12",
      "checked_at": "2026-11-05",
      "notes": "공식 초록 확인. 전체 규범적 조문·표는 미열람입니다."
    },
    {
      "id": "sb-wbs",
      "title": "NASA Work Breakdown Structure Handbook",
      "url": "https://www.nasa.gov/wp-content/uploads/2023/08/nasa-work-breakdown-structure-handbook.pdf",
      "author": "NASA",
      "published": "2021-11",
      "checked_at": "2026-11-05",
      "notes": "NASA/SP-20210023927 공개 PDF 열람. 산출물 분해·사전·통제 용도를 확인했습니다."
    },
    {
      "id": "sb-risk",
      "title": "ISO 31000:2018 Risk management — Guidelines",
      "url": "https://www.iso.org/standard/31000",
      "author": "ISO",
      "published": "2018-02 / 2023 확인",
      "checked_at": "2026-11-05",
      "notes": "공식 공개 설명과 판본 확인. 인증 요구사항 표준이 아닌 지침입니다. 유료 전체 본문은 미열람입니다."
    },
    {
      "id": "sb-pmi-risk",
      "title": "Collaborative tools and techniques to build the project risk plan",
      "url": "https://www.pmi.org/learning/library/tools-techniques-build-project-risk-plan-7223",
      "author": "PMI Learning Library / 발표 저자",
      "published": "웹 페이지 발행일 미확인",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-tuckman",
      "title": "This IS your grandfather’s project management: Building a trust-based team",
      "url": "https://www.pmi.org/learning/library/building-trust-based-team-9278",
      "author": "PMI Learning Library",
      "published": "2014",
      "checked_at": "2026-11-05",
      "notes": "5단계 팀 발달 설명을 실제 열람. Tuckman 원논문 전부를 읽었다는 뜻은 아닙니다."
    },
    {
      "id": "sb-audit2023",
      "title": "지능정보기술 감리 실무 가이드",
      "url": "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=25211&cbIdx=99860",
      "author": "한국지능정보사회진흥원",
      "published": "2023-02-06",
      "checked_at": "2026-11-05",
      "notes": "공식 첨부 PDF 실제 다운로드·텍스트 열람. 빅데이터 분석/설계 p.11~35, 클라우드 장, 운영/유지관리 p.150 이후 표의 영역을 참조했습니다."
    },
    {
      "id": "sb-auditbase",
      "title": "정보시스템 감리기준 개정 알림",
      "url": "https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000016&nttId=110444",
      "author": "행정안전부",
      "published": "2024-06-27",
      "checked_at": "2026-11-05",
      "notes": "공식 고시 공지와 국가법령정보센터의 제2024-53호 메타데이터 확인. 129회는 제2021-4호를 명시하므로 현행 고시로 문구를 덮어쓰지 않습니다."
    },
    {
      "id": "sb-egovlaw",
      "title": "전자정부법 시행령 제71조",
      "url": "https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0071&lsiSeq=288965&urlMode=lsScJoRltInfoR",
      "author": "국가법령정보센터 / 행정안전부",
      "published": "2026-08-28 시행",
      "checked_at": "2026-11-05",
      "notes": "해당 조문 현행 원문 열람. 다른 조항 및 PMO 대상의 모든 예외 요건까지 이 조문에서 확인된 것은 아닙니다."
    },
    {
      "id": "sb-fee2025",
      "title": "SW사업 대가산정 가이드(2025년 개정판)",
      "url": "https://www.sw.or.kr/site/sw/ex/board/View.do?bcIdx=63607&cbIdx=276",
      "author": "한국인공지능·소프트웨어산업협회(KOSA)",
      "published": "2025-08-11",
      "checked_at": "2026-11-05",
      "notes": "공식 첨부 PDF 다운로드·열람. SW규모·개발비·운영비·AI사업 p.157~169 및 부록을 확인했습니다. 적용 단가·요율은 판본과 사업 조건을 함께 확인해야 합니다."
    },
    {
      "id": "sb-fee2023",
      "title": "SW사업 대가산정 가이드(2023년 개정판)",
      "url": "https://www.sw.or.kr/site/sw/ex/board/View.do?bcIdx=57880&cbIdx=276",
      "author": "한국소프트웨어산업협회",
      "published": "2023-12-08",
      "checked_at": "2026-11-05",
      "notes": "공식 배포 설명과 공개 PDF 열람을 대상으로 삼았습니다. 132회 명시 판본이므로 2025 수치를 소급 적용하지 않습니다."
    },
    {
      "id": "sb-swlaw2023",
      "title": "소프트웨어 진흥법 [시행 2023.10.19]",
      "url": "https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20231019&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=249973&mokChaChk=N",
      "author": "국가법령정보센터 / 과학기술정보통신부",
      "published": "법률 제19349호",
      "checked_at": "2026-11-05",
      "notes": "기출 지정 판본 PDF 본문 제5조·제30조 등 열람. 법령 조문은 출처를 밝히고 간추렸습니다."
    },
    {
      "id": "sb-swlawcurrent",
      "title": "소프트웨어 진흥법 현행 및 예정법령 검색",
      "url": "https://www.law.go.kr/LSW/lsSc.do?eventGubun=060101&menuId=1&query=%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4+%EC%A7%84%ED%9D%A5%EB%B2%95&subMenuId=15&tabMenuId=81",
      "author": "국가법령정보센터",
      "published": "현행 2025-04-23 / 예정 2027-02-12",
      "checked_at": "2026-11-05",
      "notes": "2026-11-05 현재 검색 화면은 제20476호 현행, 제21865호 2027-02-12 시행 예정법령을 구분해 표시합니다. 현행 전 조문과 2023판의 세부 대조는 추가 확인 필요합니다."
    },
    {
      "id": "sb-taskreview",
      "title": "소프트웨어사업 과업심의위원회",
      "url": "https://fund.hknu.ac.kr/icc/5447/subview.do",
      "author": "한경국립대학교",
      "published": "지속 갱신 페이지",
      "checked_at": "2026-11-05",
      "notes": "공공기관의 실제 운영안내 열람. 해당 기관의 운영 범위나 내부 기준을 전국 공통 법령으로 일반화하지 않습니다."
    },
    {
      "id": "sb-procurement",
      "title": "조달청 협상계약 평가… 기업 부담 낮추고 공정성 높인다",
      "url": "https://www.pps.go.kr/kor/bbs/view.do?bbsSn=2409110017&key=00634",
      "author": "조달청",
      "published": "2024-09-11",
      "checked_at": "2026-11-05",
      "notes": "2024-09-13 시행 개정에 관한 공식 보도자료 본문 열람. 후속 개정 여부는 별도 현행 규정 확인 필요합니다."
    },
    {
      "id": "sb-itsqf",
      "title": "ITSQF 기반 표준 직무 설명회 안내",
      "url": "https://www.ksfc.or.kr/ksfch620_1.do?bbsSeq=20898",
      "author": "소프트웨어공제조합 / 정보기술ISC 발표 안내",
      "published": "2018",
      "checked_at": "2026-11-05",
      "notes": "공식 산업단체의 9개 직종·28개 직무 도입 설명을 열람. 2026년 직무 수 및 임금 단가는 이 수치로 확정하지 않습니다."
    },
    {
      "id": "sb-isp",
      "title": "ISP·ISMP 수립 공통가이드 제9판",
      "url": "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=28088&cbIdx=99835",
      "author": "기획재정부 / NIA",
      "published": "2025-05-19 / 첨부 2025-12 일부개정",
      "checked_at": "2026-11-05",
      "notes": "공식 첨부 PDF 실제 열람. 본문 p.40~44 ISP/ISMP 기본 구성 및 산출물, 세부 요건 분석을 참조했습니다. 129회 지정 6판과 세부 개정 차이는 추가 대조 필요합니다."
    },
    {
      "id": "sb-cobit",
      "title": "Employing COBIT 2019 for Enterprise Governance Strategy",
      "url": "https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy",
      "author": "ISACA",
      "published": "2019",
      "checked_at": "2026-11-05",
      "notes": "공식 발행기관의 공개 설명 열람. 프레임워크 전체 유료 본문을 읽었다는 뜻은 아닙니다."
    },
    {
      "id": "sb-itsm",
      "title": "ISO/IEC 20000-1:2018 Service management system requirements",
      "url": "https://www.iso.org/standard/70636.html",
      "author": "ISO/IEC",
      "published": "2018-09 / Amd1:2024",
      "checked_at": "2026-11-05",
      "notes": "공식 초록·판본·서비스 수명주기 범위 확인. §8.5 세부 요구사항 전체는 유료 본문 미열람으로 부분 확인입니다."
    },
    {
      "id": "sb-sla",
      "title": "KS X ISO/IEC 19086-1 클라우드 SLA 프레임워크",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010125305",
      "author": "한국표준협회 / ISO·IEC",
      "published": "2019 국내 채택 정보",
      "checked_at": "2026-11-05",
      "notes": "공식 표준 판매/안내 페이지의 적용범위 열람. 전체 표준 본문 미열람입니다."
    },
    {
      "id": "sb-cloudsla",
      "title": "클라우드 서비스 SLA 가이드의 역할",
      "url": "https://www.korea.kr/briefing/policyBriefingView.do?newsId=148720333",
      "author": "방송통신위원회 / 정책브리핑",
      "published": "2011",
      "checked_at": "2026-11-05",
      "notes": "공식 설명 열람. 오래된 소개의 시장 전망 수치는 사용하지 않습니다. 현행 금융 클라우드 세부 절차 원문은 별도 확인 필요합니다."
    },
    {
      "id": "sb-coe",
      "title": "Power Platform Center of Excellence Starter Kit overview",
      "url": "https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview",
      "author": "Microsoft",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "공식 제품 문서의 CoE 개념·거버넌스·활성화 범위 열람. 특정 제품 구현 예이지 일반 조직의 의무모델이 아닙니다."
    },
    {
      "id": "sb-bsc",
      "title": "Partnering and the Balanced Scorecard",
      "url": "https://www.library.hbs.edu/working-knowledge/partnering-and-the-balanced-scorecard",
      "author": "Robert Kaplan / Harvard Business School",
      "published": "2002",
      "checked_at": "2026-11-05",
      "notes": "저자의 공개 해설 열람. 재무·고객·내부프로세스·학습성장의 네 관점 및 전략 전달 용도를 참조했습니다."
    },
    {
      "id": "sb-ahp",
      "title": "Decision making with the analytic hierarchy process",
      "url": "https://doi.org/10.1504/IJSSCI.2008.017590",
      "author": "Thomas L. Saaty",
      "published": "2008-03-18",
      "checked_at": "2026-11-05",
      "notes": "원 논문 초록 열람. 가중치의 상위 노드별 곱셈 및 합산, 쌍대비교·판단 일관성의 의미를 확인했습니다."
    },
    {
      "id": "sb-tam",
      "title": "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology",
      "url": "https://www.jstor.org/stable/249008",
      "author": "Fred D. Davis / MIS Quarterly",
      "published": "1989-09",
      "checked_at": "2026-11-05",
      "notes": "원 논문 공개 초록 열람. 설문지 전문이나 모든 구조방정식 계수는 미열람입니다."
    },
    {
      "id": "sb-strategy",
      "title": "A Firm’s External Macro Environment: PESTEL",
      "url": "https://openstax.org/books/principles-management/pages/8-3-a-firms-external-macro-environment-pestel",
      "author": "OpenStax / Rice University",
      "published": "2019",
      "checked_at": "2026-11-05",
      "notes": "공개 대학 교재 열람. PEST는 PESTEL의 환경·법률 축을 별도 분리하지 않는 형태로 설명합니다. 3C 원저 전체는 미열람입니다."
    },
    {
      "id": "sb-scm",
      "title": "What Is Supply Chain Management?",
      "url": "https://www.oracle.com/scm/what-is-supply-chain-management/",
      "author": "Oracle",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-stock",
      "title": "What Is Safety Stock?",
      "url": "https://www.ibm.com/think/topics/safety-stock",
      "author": "IBM",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-esg",
      "title": "업종별 K-ESG 가이드라인(2024년 통합본)",
      "url": "https://www.k-esg.org/guide/guide_handbook_view?idx=3077",
      "author": "산업통상자원부 / 지속가능경영지원센터",
      "published": "2024-12-10",
      "checked_at": "2026-11-05",
      "notes": "공식 배포 페이지 및 업종별 지표체계 설명 열람. 특정 기업 ESG 점수나 성과를 창작하지 않습니다."
    },
    {
      "id": "sb-ems",
      "title": "ISO 14001:2026 Environmental management systems",
      "url": "https://www.iso.org/standard/14001",
      "author": "ISO",
      "published": "2026-04",
      "checked_at": "2026-11-05",
      "notes": "공식 소개·판본·인증 절차 설명 열람. 132회 시점 2015판과 현재 2026판을 구분합니다. 전체 표준 유료 본문은 미열람입니다."
    },
    {
      "id": "sb-tax2021",
      "title": "Statement on a Two-Pillar Solution – 8 October 2021",
      "url": "https://www.oecd.org/en/about/news/announcements/2021/10/statement-on-a-two-pillar-solution-to-address-the-tax-challenges-arising-from-the-digitalisation-of-the-economy-october-2021.html",
      "author": "OECD/G20 Inclusive Framework",
      "published": "2021-10-08",
      "checked_at": "2026-11-05",
      "notes": "기출 당시 합의의 공식 설명 열람. 당시 2023 시행 목표와 실제 효력 발생을 구분합니다."
    },
    {
      "id": "sb-taxcurrent",
      "title": "Cross-border and international tax",
      "url": "https://www.oecd.org/en/topics/policy-issues/cross-border-and-international-tax.html",
      "author": "OECD",
      "published": "지속 갱신 페이지",
      "checked_at": "2026-11-05",
      "notes": "Pillar One Amount A/B와 Pillar Two 대상 범위의 공식 설명 열람. 2026-11-05의 국가별 시행·다자협약 비준 전부는 확인하지 못했습니다."
    },
    {
      "id": "sb-egdi",
      "title": "United Nations E-Government Survey 2024",
      "url": "https://desapublications.un.org/sites/default/files/publications/2024-09/%28Web%20version%29%20E-Government%20Survey%202024%201392024.pdf",
      "author": "UN DESA",
      "published": "2024-09",
      "checked_at": "2026-11-05",
      "notes": "공식 PDF의 지수 구성 및 방법론 변경 설명 열람. 국가 순위 암기나 2026 순위 주장은 하지 않습니다."
    },
    {
      "id": "sb-blockchain",
      "title": "Blockchain Technology Overview (NISTIR 8202)",
      "url": "https://www.nist.gov/publications/blockchain-technology-overview",
      "author": "Dylan Yaga 외 / NIST",
      "published": "2018-10",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-nft",
      "title": "ERC-721 Non-Fungible Token Standard",
      "url": "https://ethereum.org/en/developers/docs/standards/tokens/erc-721/",
      "author": "Ethereum 공식 문서 / EIP 공동체",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-twin",
      "title": "Digital twins",
      "url": "https://www.nist.gov/digital-twins",
      "author": "NIST",
      "published": "지속 갱신 페이지",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-metaverse",
      "title": "정부 메타버스 윤리원칙 발표",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148908796",
      "author": "과학기술정보통신부",
      "published": "2022-11-28",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-metaverse2023",
      "title": "메타버스 실천윤리 제정",
      "url": "https://m.korea.kr/news/policyNewsView.do?newsId=148924147",
      "author": "과학기술정보통신부",
      "published": "2023-12-26",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-azure-msa",
      "title": "Microservices Architecture Style",
      "url": "https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices",
      "author": "Microsoft Azure Architecture Center",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-azure-eda",
      "title": "Event-Driven Architecture Style",
      "url": "https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven",
      "author": "Microsoft Azure Architecture Center",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-istio",
      "title": "The Istio service mesh",
      "url": "https://istio.io/latest/about/service-mesh/",
      "author": "Istio 프로젝트",
      "published": "열람 화면 1.31.3",
      "checked_at": "2026-11-05",
      "notes": "공식 문서에서 서비스 메시 기능과 ambient/sidecar 두 배포 모드 확인. 모든 메시가 sidecar만 사용한다고 설명하지 않습니다."
    },
    {
      "id": "sb-sem",
      "title": "Beyond ERP: Strategic Enterprise Management",
      "url": "https://help.sap.com/docs/SAP_ERP/b216b6bc6d8843e9acd99baa92b65ea9/799fcf535b804808e10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=6.17.latest",
      "author": "SAP Help Portal",
      "published": "ERP6.0 EHP7 문서",
      "checked_at": "2026-11-05",
      "notes": "제품 공식 문서의5구성요소·ERP/BW 연결을 실제 열람했습니다. 특정 제품 분류를 모든 SEM의 유일한 국제표준 구성으로 일반화하지 않습니다."
    },
    {
      "id": "sb-market",
      "title": "TAM SAM SOM Calculation (Bottom-up)",
      "url": "https://www.itu.int/en/ITU-D/Regional-Presence/CIS/Documents/Events/2021/SCE/Presentations/ITU%20Workshop%20on%20startup%20ecosystems%20-%20Artem%20Yaremchuk.pdf",
      "author": "Artem Yaremchuk / ITU Workshop 공개자료",
      "published": "2021",
      "checked_at": "2026-11-05",
      "notes": "공식 공개 워크숍 자료의 시장 범위·고객수×연간 계약가 계산 부분을 확인했습니다. 실제 시장 숫자로 사용하지 않습니다."
    },
    {
      "id": "sb-whitelabel",
      "title": "White Label Marketing Agency",
      "url": "https://www.whitelabelagency.co/",
      "author": "White Label Agency",
      "published": "지속 갱신 페이지",
      "checked_at": "2026-11-05",
      "notes": "해당 서비스 제공자의 자사 제공 방식과 화이트라벨 정의를 확인했습니다. 일반 산업 규모·효과 통계의 근거는 아닙니다."
    },
    {
      "id": "sb-publicsla",
      "title": "정보시스템 가용률, 장애시간 표준안 등으로 디지털정부서비스 품질 높인다",
      "url": "https://mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=120101",
      "author": "행정안전부 디지털기반안전과",
      "published": "2025-08-28",
      "checked_at": "2026-11-05",
      "notes": "첨부 보도자료3쪽의 가용률·장애시간·위약금 표를 실제 열람했습니다. 2027 의무화는 이 발표의 추진계획이며 개정 법률의 최종 적용 조문·시행령 등급 산정점수 전체를 확인한 것은 아닙니다."
    },
    {
      "id": "sb-kesg2",
      "title": "K-ESG 가이드라인 v2.0",
      "url": "https://k-esg.org/uploads/post/2024/12/e6d63e812307ab3e093a783e074db91d.pdf",
      "author": "관계부처 합동 / 산업통상자원부",
      "published": "2024-12",
      "checked_at": "2026-11-05",
      "notes": "공식 PDF의 진단체계·정보보호 항목을 열람. 자가진단 지침과 법정 의무·모든 평가기관의 동일 점수는 구분합니다."
    },
    {
      "id": "sb-dpg",
      "title": "디지털플랫폼정부 실현계획 합동 브리핑",
      "url": "https://www.korea.kr/briefing/policyBriefingView.do?newsId=156563254",
      "author": "디지털플랫폼정부위원회·과학기술정보통신부 등",
      "published": "2023-04-17(게시일; 실현계획 발표2023-04)",
      "checked_at": "2026-11-05",
      "notes": "공식 브리핑의 비전·4대 과제·사례·보호장치 설명 열람. 계획의 목표값을 현재 달성 실적으로 쓰지 않습니다."
    },
    {
      "id": "sb-osi-sspl",
      "title": "The SSPL is Not an Open Source License",
      "url": "https://opensource.org/blog/the-sspl-is-not-an-open-source-license",
      "author": "Open Source Initiative Board",
      "published": "2021-01-19",
      "checked_at": "2026-11-05",
      "notes": "본문 또는 해당 절을 실제 열람했습니다. 자체 요약만 저장하며 외부 원문 전체는 보관하지 않습니다."
    },
    {
      "id": "sb-bsl",
      "title": "Business Source License 1.1",
      "url": "https://mariadb.com/bsl11/",
      "author": "MariaDB",
      "published": "1.1 공개 라이선스 본문",
      "checked_at": "2026-11-05",
      "notes": "사용권·Additional Use Grant·Change Date/Change License·판본별 적용을 실제 열람했습니다. 개별 제품의 추가 사용허락을 일반 BSL의 일률 조건으로 해석하지 않습니다."
    },
    {
      "id": "sb-hashicorp-bsl",
      "title": "HashiCorp adopts Business Source License",
      "url": "https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license",
      "author": "HashiCorp",
      "published": "2023-08-10",
      "checked_at": "2026-11-05",
      "notes": "라이선스 변경 주체의 상업적 동기와 추가 사용허락 설명을 열람. 기업 입장과 OSI의 오픈소스 정의 판단을 구분합니다."
    },
    {
      "id": "sb-forecast",
      "title": "What is predictive forecasting?",
      "url": "https://www.ibm.com/think/topics/predictive-forecasting",
      "author": "Teaganne Finn·Ian Smalley / IBM",
      "published": "2026-03-26",
      "checked_at": "2026-11-05",
      "notes": "공식 설명의 목표·자료·모델·검증·전개·감시 원리를 확인했습니다. 128회에서 요구한 고전 수요예측7단계의 원출전과는 다른 자료이므로 동일 출전이라고 쓰지 않습니다."
    },
    {
      "id": "sb-pop",
      "title": "A Point of Production System for Semiconductor Wafer Dicing Process",
      "url": "https://journal.kci.go.kr/jksci/archive/articleView?artiId=ART001388561",
      "author": "김인호 / 한국컴퓨터정보학회논문지14(10),55–61",
      "published": "2009",
      "checked_at": "2026-11-05",
      "notes": "원 논문 공개 초록의 POP단말·라인컨트롤러·네트워크와 양방향 계획/실적 흐름을 실제 열람했습니다. 사례의 수치 성과·전체 실험은 확인하지 않았습니다."
    },
    {
      "id": "sb-darkfactory",
      "title": "Lights-out factory",
      "url": "https://www.siemens.com/en-us/technology/lights-out-factory/",
      "author": "Siemens",
      "published": "갱신일 미표기",
      "checked_at": "2026-11-05",
      "notes": "제공자의 공식 공개 본문에서 자동화 셀·MOM·원격 감독·고정 일정 표준제품의 적합성을 확인했습니다. 검색에서 본문을 읽었으며 직접 open은 타임아웃이었습니다. 특정 공장의 인력·생산량 성과는 사용하지 않습니다."
    },
    {
      "id": "sb-web3",
      "title": "Introduction to Web3",
      "url": "https://ethereum.org/en/web3/",
      "author": "Ethereum.org contributors",
      "published": "지속 갱신 문서",
      "checked_at": "2026-11-05",
      "notes": "개발 생태계의 자체 설명에서 탈중앙·소유·권한·기술 및 한계를 열람. 이상적 지향과 실제 서비스의 분산 수준을 구분합니다."
    },
    {
      "id": "sb-virtualworld",
      "title": "Frequently Asked Questions on virtual worlds",
      "url": "https://digital-strategy.ec.europa.eu/en/faqs/frequently-asked-questions-faq-virtual-worlds",
      "author": "European Commission",
      "published": "갱신일 미표기",
      "checked_at": "2026-11-05",
      "notes": "가상세계·메타버스·디지털트윈·NFT·시맨틱 Web3.0을 구분하는 공식 FAQ 열람. 문서의 낙관적 기대를 검증된 보안 보장으로 옮기지 않습니다."
    },
    {
      "id": "sb-twintrust",
      "title": "Security and Trust Considerations for Digital Twin Technology, NIST IR8356",
      "url": "https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8356.pdf",
      "author": "Jeffrey Voas·Peter Mell·Phillip Laplante·Vartan Piroumian / NIST",
      "published": "2025-02",
      "checked_at": "2026-11-05",
      "notes": "공개 PDF의 정의·동기·운영·신뢰/보안 고려를 열람했습니다. NIST는 단일 합의 정의의 부재도 명시합니다."
    },
    {
      "id": "sb-dysfunction",
      "title": "Digital Inclusion Report4: 디지털 역기능3대 이슈 쟁점과 과제",
      "url": "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=24588&cbIdx=39485",
      "author": "이형주 / 한국지능정보사회진흥원 AI윤리팀",
      "published": "2022-06-02",
      "checked_at": "2026-11-05",
      "notes": "첨부 PDF의3대 이슈 정의·대응과제p.16~17을 실제 열람했습니다. 보고서에 인용된 언론통계를 현행 공식 통계처럼 재사용하지 않았습니다."
    },
    {
      "id": "sb-darkpatterns-ftc",
      "title": "Bringing Dark Patterns to Light",
      "url": "https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf",
      "author": "US FTC Bureau of Consumer Protection",
      "published": "2022-09",
      "checked_at": "2026-11-05",
      "notes": "공개 원 보고서의 정의·소비자 선택 침해·대표 유형과 대응 설명 열람. 미국 법집행을 국내 규정과 동일시하지 않습니다."
    },
    {
      "id": "sb-darkpatterns-korea",
      "title": "정기결제 대금 인상 또는 유료 전환 전30일 이내 소비자 동의받아야",
      "url": "https://m.korea.kr/news/policyNewsView.do?newsId=148939436",
      "author": "공정거래위원회",
      "published": "2025-02-10",
      "checked_at": "2026-11-05",
      "notes": "2025-02-14 개정 시행에 대한 기관 공식 설명 열람. 선택 예외·정당한 사유 등 실제 적용은 법문·후속 지침을 확인해야 합니다."
    },
    {
      "id": "sb-darkpatterns-2026",
      "title": "온라인 다크패턴 규제 관련 가이드라인 배포",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156784349",
      "author": "공정거래위원회",
      "published": "2026-10-06",
      "checked_at": "2026-11-05",
      "notes": "새 가이드라인 배포 사실과 공식 본문 열람. 별첨 지침 전체의 세부 해석은 미열람으로 종전 설명을2026최종 해석이라고 단정하지 않습니다."
    },
    {
      "id": "sb-superapp",
      "title": "Superapp Homepage",
      "url": "https://intl.cloud.tencent.com/ko/document/product/1219/73453",
      "author": "Tencent Cloud",
      "published": "2026-07-10",
      "checked_at": "2026-11-05",
      "notes": "공식 SDK·패키지/번들 식별·슈퍼앱 호스트와 미니프로그램 통합 설명 열람. 키를 발급하거나 API를 호출한 것은 아닙니다."
    },
    {
      "id": "sb-miniprogram",
      "title": "Weixin Mini Programs",
      "url": "https://www.tencent.com/products/weixin-mini-programs/",
      "author": "Tencent",
      "published": "갱신일 미표기",
      "checked_at": "2026-11-05",
      "notes": "제공자가 공개한 QR/검색 진입·쇼핑/생활/공공 서비스의 실제 지원 범위 열람. 이용자 수·시장 전망 수치는 사용하지 않습니다."
    },
    {
      "id": "sb-mini-spi",
      "title": "Integrate Native SPIs",
      "url": "https://miniprogram.alipay.com/docs/miniprogram/mpdev/sdk_android_integrate_native_spi",
      "author": "Alipay+ Mini Program Documentation",
      "published": "2024-11-08",
      "checked_at": "2026-11-05",
      "notes": "호스트 nativeSPI·JSAPI·OAuth권한과 결제/사용자 기능 연결 설명 열람. 제품별 동의 요건과 일반 법률 의무를 구분합니다."
    },
    {
      "id": "sb-aidt2023",
      "title": "교육 혁신 도구로서의 AI 디지털 교과서: 개발 방향과 현황",
      "url": "https://www.nypi.re.kr/repository/handle/2022.oak/6210",
      "author": "장시준 / KERIS 교육플랫폼본부장, NYPI 콜로키움23-06",
      "published": "2023-09-18",
      "checked_at": "2026-11-05",
      "notes": "공식 공개 PDF 이미지p.6~13을 직접 렌더링·열람해 정의·개발원칙·공공/민간 구조·핵심서비스·데이터허브를 확인했습니다. 2023의 법적 교과서 지위·도입 일정은 당시 계획으로 구분합니다."
    },
    {
      "id": "sb-aidtcurrent",
      "title": "학교의 안전하고 효과적인 학습지원 소프트웨어 선정을 위한 기준 안내",
      "url": "https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=105007&lev=0&m=020",
      "author": "교육부·개인정보보호위원회",
      "published": "2025-12-29",
      "checked_at": "2026-11-05",
      "notes": "2025-08-14 법 개정에 따른 교육자료 선정의 필수/선택기준·학교운영위원회 절차와NEIS연계 AI·디지털교육자료 포털 운영을 실제 열람했습니다."
    },
    {
      "id": "sb-govui2019",
      "title": "전자정부 웹사이트 UI·UX 가이드라인",
      "url": "https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000045&nttId=69451",
      "author": "행정안전부",
      "published": "2019-03-21",
      "checked_at": "2026-11-05",
      "notes": "공식 첨부 PDF의7개 설계기준 표를 실제 열람했습니다. 2024 디지털정부서비스 가이드의 구조와 혼동하지 않습니다."
    },
    {
      "id": "sb-govui2025",
      "title": "전자정부 웹사이트 품질관리 가이드 수정본 안내",
      "url": "https://www.mois.go.kr/frt/bbs/type013/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000006&nttId=118639",
      "author": "행정안전부 공공서비스혁신과",
      "published": "2025-07-01",
      "checked_at": "2026-11-05",
      "notes": "공식 개정 안내에서 KWCAG2.1→2.2,진단24→33개, UIUX37→43개 서비스패턴 재편, 검색로봇 일부차단 허용의 설명을 실제 열람했습니다. 첨부 전체를 읽었다는 뜻은 아닙니다."
    },
    {
      "id": "sb-sspl",
      "title": "Server Side Public License v1",
      "url": "https://www.mongodb.com/legal/licensing/server-side-public-license",
      "author": "MongoDB",
      "published": "2018-10-16",
      "checked_at": "2026-11-05",
      "notes": "공개 라이선스§13의 서비스 제공·Service Source Code 범위와 기본 허락을 직접 열람했습니다. 특정 제품/서비스의 계약상 법적 판단은 별도입니다."
    },
    {
      "id": "sb-riskpreview",
      "title": "ISO31000:2018 공개 미리보기: 원칙",
      "url": "https://preview.sist.si/sist-preview/65694/60673072317a4b96bd36efb910b68926/ISO-31000-2018.pdf",
      "author": "ISO / Slovenian Institute for Standardization(SIST) 공개 미리보기",
      "published": "2018",
      "checked_at": "2026-11-05",
      "notes": "국가표준기관이 제공한 공개 미리보기의Figure2와8원칙 범위를 읽었습니다. 전체 표준 본문 열람·복제는 하지 않았습니다."
    }
  ],
  "topics": [
    {
      "id": "requirements-engineering",
      "title": "요구공학과 요구사항 개발",
      "domain": "소프트웨어공학",
      "aliases": [
        "Requirements Engineering",
        "요구사항 공학"
      ],
      "related_terms": [],
      "easy": "요구공학은 만들 기능을 받아 적는 일이 아니라, 누구의 어떤 문제를 어떤 조건에서 해결할지 합의하는 과정입니다.",
      "definition": "이해관계자의 필요와 제약을 도출·분석·명세·검증하고 변경과 추적성을 관리하여 개발 및 인수의 기준선을 만드는 공학 활동입니다.",
      "principles": [
        "도출에서는 사용자·발주자·운영자·규제기관을 식별하고 인터뷰, 관찰, 워크숍, 문서분석, 설문, 프로토타입을 선택합니다. 말로 표현되지 않은 현장 예외와 외부 시스템 제약까지 확인합니다.",
        "분석에서는 기능/비기능/인터페이스/데이터/제약 요구를 구분하고 모델링·우선순위·협상을 통해 모순과 중복을 제거합니다. 요구의 출처, 근거, 소유자, 우선순위, 검증방법을 기록해야 변경을 판단할 수 있습니다.",
        "명세에서는 단일 요구에 하나의 검증 가능한 의무를 적고 입력·조건·동작·출력을 구체화합니다. 개별 요구는 필요성·명확성·실현가능성·검증가능성 등을, 요구 집합은 완전성·일관성·수정가능성·추적가능성을 점검합니다.",
        "검증에서는 요구가 사용자 의도에 맞는지 검토·시뮬레이션·프로토타입·인수기준으로 확인합니다. 기준선 이후 변경은 비용·일정·설계·시험 영향평가와 승인, 관련 산출물 동시 갱신을 거칩니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "도출",
            "필요와 제약을 발견",
            "관찰은 실제 업무, 인터뷰는 의도 확인에 유리"
          ],
          [
            "명세",
            "합의된 의무를 표현",
            "모호한 형용사를 측정조건과 기준으로 바꿈"
          ],
          [
            "관리",
            "기준선·변경·추적 통제",
            "관리 활동은 개발 전 과정에 걸쳐 반복"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 주문 취소 요구 정제",
        "input": "담당자가 “빠르고 편리하게 취소”를 요구했습니다.",
        "steps": [
          "고객·정산·물류 담당자를 인터뷰해 출고 이후 취소 불가 규칙을 찾습니다.",
          "“출고 전, 결제완료 주문의 취소를 접수하면 재고 복원과 환불요청을 생성한다”로 분리합니다.",
          "환불실패의 재시도와 인수 테스트, 응답시간 조건을 합의합니다."
        ],
        "result": "개발과 인수에서 동일한 조건을 확인할 수 있는 요구 묶음이 됩니다.",
        "caution": "예시의 시간·처리 규칙은 가정이며 실제 법적 환불 의무를 대체하지 않습니다."
      },
      "answer_outline": [
        "정의와 품질저하 원인",
        "도출→분석→명세→검증의 입력·활동·산출물",
        "변경·추적 관리와 인수기준 적용"
      ],
      "pitfalls": [
        "애자일은 요구 명세가 없다는 뜻이 아닙니다.",
        "요구 검증과 구현 제품 검증을 혼동하지 않습니다."
      ],
      "recall": [
        "관찰과 인터뷰는 각각 무엇을 발견합니까?",
        "개별 요구의 품질과 집합의 품질은 어떻게 다릅니까?",
        "변경 승인 뒤 함께 바꿀 문서를 세 가지 말해 보십시오."
      ],
      "source_ids": [
        "sb-swebok",
        "sb-nasa-req"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "130-4-4",
          "items": [
            "소프트웨어(SW) 요구사항 품질속성",
            "요구사항 도출기법",
            "요구사항 개발 프로세스"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "133-3-5",
          "items": [
            "요구공학 정의 및 필요성",
            "요구공학 절차",
            "요구사항 명세서"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "requirements-specification-traceability",
      "title": "요구사항 명세서·추적표·성능 요구",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [
        "SRS",
        "RTM",
        "성능 요구사항"
      ],
      "easy": "명세서는 약속의 내용이고 추적표는 그 약속이 설계와 시험 어디에 반영됐는지를 보여주는 지도입니다.",
      "definition": "SRS는 소프트웨어의 기능·품질·제약·외부 인터페이스와 검증기준을 기술하는 문서이며, RTM은 요구의 출처부터 설계·구현·시험·인수까지 관계를 양방향으로 유지하는 표입니다.",
      "principles": [
        "SRS는 목적·범위·용어·관련 문서, 사용자와 운영환경, 가정·제약, 기능, 외부 인터페이스, 데이터, 비기능 요구와 검증기준을 포함합니다. 문서 장 구성보다 요구 ID·근거·조건·동작·예외·확인방법을 누락 없이 기록하는 것이 중요합니다.",
        "RTM의 행은 안정된 요구 ID로 삼고 원천 요구, 기능·화면·API·테이블 등 설계, 구현 버전, 시험케이스, 결과·결함, 승인 상태를 연결합니다. 역추적은 근거 없는 기능을, 정추적은 누락 구현과 미시험 요구를 찾습니다.",
        "성능 요구는 응답시간의 평균뿐 아니라 p95/p99, 처리량(TPS), 동시 사용자, 오류율, 자원 사용률, 데이터량과 증가율을 함께 정의합니다. 부하 패턴·측정 구간·환경·워밍업·제외조건까지 있어야 재현 가능한 인수 기준입니다.",
        "추적률은 연결의 존재를 셀 뿐 연결이 정확하다는 것을 보장하지 않습니다. 요구 변경 시 영향받는 설계와 시험을 추출하고, 링크 타당성·버전 일치·미검증 상태를 검토해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "SRS",
            "무엇을 만족해야 하는가",
            "설계의 임의 구현 선택과 구분"
          ],
          [
            "RTM",
            "어디에 반영·검증됐는가",
            "변경영향·인수 증거 조회"
          ],
          [
            "성능 명세",
            "어떤 부하에서 어느 수준인가",
            "평균만 좋아도 꼬리 지연은 나쁠 수 있음"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 검색 기능의 인수 기준",
        "input": "동시 사용자 300명, 데이터 100만 건이라는 가정입니다.",
        "steps": [
          "PER-01을 “10분간 읽기 90%/쓰기 10%에서 검색 p95≤2초, 오류율<0.1%”로 적습니다.",
          "PER-01→검색 API/색인 설계→성능시험 TC-P01→실행 보고서를 연결합니다.",
          "데이터량을 500만 건으로 바꾸면 용량·색인·부하시험을 재평가합니다."
        ],
        "result": "요구의 의미와 검증 결과가 연결됩니다.",
        "caution": "예시 수치는 학습용 가정입니다. 부하의 폐쇄/개방 모델과 서버·네트워크 조건도 실제 사업에서 명세해야 합니다."
      },
      "answer_outline": [
        "SRS 항목 및 품질요건",
        "RTM 구조와 양방향 추적",
        "성능 지표를 조건·기준·측정방법으로 구체화"
      ],
      "pitfalls": [
        "TPS와 동시 사용자 수는 같은 값이 아닙니다.",
        "링크가 있다고 요구가 충족된 것으로 표시하지 않습니다."
      ],
      "recall": [
        "추적표에서 고아 기능과 미시험 요구를 어떻게 찾습니까?",
        "p95가 평균보다 유용한 경우는 언제입니까?",
        "성능 요구에 환경조건이 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-nasa-req",
        "sb-inspection",
        "sb-isp"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "130-1-3",
          "items": [
            "요구사항명세서에 기술되어야 하는 항목 설명"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "135-1-3",
          "items": [
            "요구사항 추적표(Requirement Traceability Matrix)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "132-3-6",
          "items": [
            "정보시스템의 성능 요구사항 작성 시 고려해야 하는 주요 성능지표 및 내용에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "agile-lifecycle-tailoring",
      "title": "구조적·폭포수·애자일과 방법론 테일러링",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "방법론은 순서를 지키는 의식이 아니라, 불확실성과 위험에 맞춰 피드백 시점을 설계하는 방법입니다.",
      "definition": "예측형 개발은 요구와 계획을 앞에서 구체화하고 단계적으로 통제하며, 애자일은 짧은 주기의 작동하는 결과와 피드백으로 요구·계획을 적응시킵니다. 테일러링은 사업의 위험·규모·규제에 따라 활동과 산출물을 조정하는 일입니다.",
      "principles": [
        "구조적 방법론은 기능분해·자료흐름 중심 분석/설계이며, 폭포수는 단계 순서를 중심으로 한 수명주기 모형입니다. 두 용어가 항상 동의어는 아닙니다. 요구가 안정적이고 계약·인증 증거가 중요한 상황은 예측형의 명확한 기준선이 유용합니다.",
        "Scrum은 제품책임자·스크럼마스터·개발자가 제품백로그를 정렬하고 한 달 이하 스프린트에서 가치 있는 증분을 만듭니다. 계획·데일리·리뷰·회고로 결과와 작업 방식을 점검하고 완료의 정의로 품질을 유지합니다.",
        "Kanban은 작업흐름을 정의·시각화하고 진행 중 작업(WIP)을 통제하여 흐름을 관리합니다. 처리량, 작업항목 나이, 주기시간, WIP로 병목을 찾아 개선하며 필수적인 스프린트나 고정 역할을 요구하지 않습니다.",
        "선도개발은 핵심 기술·연계의 검증할 가설과 종료기준을 먼저 정하고 위험이 큰 부분을 작게 구현합니다. 테일러링은 필수 통제를 식별한 뒤 생략·통합·반복 활동의 이유와 책임·산출물·검증 방법을 기록해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "예측형",
            "범위·단계 기준선과 변경통제",
            "안정 요구에 유리, 늦은 피드백 위험"
          ],
          [
            "Scrum",
            "시간상자와 증분·검토",
            "제품 목표와 우선순위에 집중"
          ],
          [
            "Kanban",
            "흐름·WIP·명시 정책",
            "운영 요청·불규칙 유입에 적용"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 레거시 포털 개선",
        "input": "외부 정산 인터페이스는 고정이고 사용자 화면은 불확실합니다.",
        "steps": [
          "정산 규격과 법정 산출물은 사전 확정합니다.",
          "조회 화면은 2주 증분으로 사용자 검토를 받고 운영 버그는 별도 WIP 제한 흐름으로 관리합니다.",
          "새 인증기술은 선도개발로 지연·호환성 가설을 검증합니다."
        ],
        "result": "규제 증거와 빠른 학습을 함께 확보하는 혼합 운영안이 됩니다.",
        "caution": "애자일 전환만으로 생산성이 자동 향상된다고 주장하지 않습니다."
      },
      "answer_outline": [
        "수명주기와 구조적 방법론의 구분",
        "Scrum·Kanban 구성 비교",
        "적용 상황·효율화·테일러링 사례"
      ],
      "pitfalls": [
        "문서·테스트·변경통제를 전부 없애는 것은 테일러링이 아닙니다.",
        "스프린트마다 무조건 운영 배포해야 하는 것은 아닙니다."
      ],
      "recall": [
        "구조적 방법론과 폭포수의 분류 축은 왜 다릅니까?",
        "WIP 제한이 병목을 드러내는 이유는 무엇입니까?",
        "선도개발의 종료기준을 하나 제시하십시오."
      ],
      "source_ids": [
        "sb-scrum",
        "sb-kanban",
        "sb-swebok"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "129-2-5",
          "items": [
            "구조적 방법론과 Agile 방법론 비교",
            "Agile 방법론의 스크럼(Scrum)과 칸반(Kanban) 설명",
            "Agile 방법론의 효율적인 수행 방안 제시"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-1-3",
          "items": [
            "폭포수 개발 방법론과 애자일 개발 방법론의 특징 및 장·단점 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "138-1-6",
          "items": [
            "소프트웨어 개발 프로젝트에서 선도개발을 위한 개발방법론 테일러링(Tailoring)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-product-line",
      "title": "소프트웨어 제품계열 방법론",
      "domain": "소프트웨어공학",
      "aliases": [
        "Software Product Line",
        "SPL",
        "제품계열"
      ],
      "related_terms": [],
      "easy": "제품마다 복사해서 고치는 대신 공통 기능과 달라지는 지점을 먼저 관리해 여러 제품을 만듭니다.",
      "definition": "특정 시장·임무의 공통 특징을 공유하는 제품군을 공통 핵심자산과 정해진 생산 방식으로 개발하는 계획적 재사용 접근입니다.",
      "principles": [
        "핵심 활동은 공통 핵심자산 개발, 개별 제품 개발, 조직·기술 관리입니다. 핵심자산은 코드뿐 아니라 제품계열 아키텍처, 요구 모델, 시험, 생성 규칙과 운영 지식까지 포함합니다.",
        "도메인 공학에서 시장과 제품 범위를 정하고 공통성과 가변성을 분석합니다. 기능모델의 필수·선택·대안·의존/배제 제약으로 허용되는 구성을 정하고 변이점을 아키텍처·컴포넌트에 배치합니다.",
        "응용 공학에서는 제품 요구에 맞춰 특징을 선택하고 핵심자산을 구성·확장한 뒤 제품별 시험과 계열 공통 회귀시험을 수행합니다. 플러그인, 설정, 컴포넌트 조립, 템플릿·생성기, 공통 인터페이스를 활용할 수 있습니다.",
        "도입 전에는 제품 간 공통성, 향후 제품 수, 자산의 소유자, 버전 호환성과 회수 가능한 초기투자를 판단합니다. 변이점이 과도하면 조합 폭발과 시험비가 커지고 공통자산 결함이 모든 제품에 확산될 수 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "단일 제품 개발",
            "현재 제품 요구를 최적화",
            "초기 부담이 작지만 제품군 복제 비용 발생"
          ],
          [
            "제품계열",
            "범위 내 공통성·가변성을 계획",
            "선행 자산투자와 구성 관리 필요"
          ],
          [
            "단순 라이브러리 재사용",
            "일부 코드 기능을 공유",
            "제품 구성·생산 계획까지 포괄하지 않음"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 지자체 민원 제품군",
        "input": "A시는 카드결제, B시는 계좌이체와 다국어가 필요합니다.",
        "steps": [
          "신청·심사·통지는 공통 특징, 결제수단과 언어는 가변 특징으로 모델링합니다.",
          "결제 인터페이스를 공통자산으로 정하고 특징 선택에 따라 어댑터를 조립합니다.",
          "각 결제 조합과 공통 심사 규칙을 시험하고 자산 버전을 고정합니다."
        ],
        "result": "공통 업무 변경을 여러 제품에 통제하여 반영할 수 있습니다.",
        "caution": "공통률·개발기간 절감률은 실제 측정 없이 숫자로 만들지 않습니다."
      },
      "answer_outline": [
        "개념과 공통성·가변성",
        "도메인/응용 공학 및 핵심자산",
        "활용기술·경제성·시험과 조직 고려"
      ],
      "pitfalls": [
        "소스 저장소를 복사하는 것은 관리되는 제품계열과 다릅니다.",
        "허용되지 않은 특징 조합도 제약으로 관리합니다."
      ],
      "recall": [
        "제품계열의 세 가지 핵심 활동은 무엇입니까?",
        "가변성과 변경가능성은 어떻게 연결됩니까?",
        "변이점을 무제한 늘리면 어떤 비용이 생깁니까?"
      ],
      "source_ids": [
        "sb-spl"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "136-2-4",
          "items": [
            "개념과 특징",
            "활용 기술과 고려사항"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "modularity-encapsulation",
      "title": "모듈 응집도·결합도·캡슐화·정보은닉",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "함께 바뀌는 책임은 모으고, 다른 모듈이 몰라도 되는 내부 결정은 감춥니다.",
      "definition": "응집도는 모듈 내부 요소가 한 책임에 연관된 정도, 결합도는 모듈 사이 의존 정도입니다. 캡슐화는 상태와 연산을 경계 안에 묶는 구조이며 정보은닉은 변경 가능한 내부 설계 결정을 외부 계약 뒤에 감추는 원칙입니다.",
      "principles": [
        "고전적 응집도는 우연적→논리적→시간적→절차적→통신적→순차적→기능적 순으로 높은 응집을 지향합니다. 분류 명칭과 순서의 세부 변형이 있으므로 핵심은 하나의 변경 이유와 책임으로 묶는 것입니다.",
        "결합은 내용 결합(타 모듈 내부 침범), 공통 결합(전역 상태 공유), 외부 결합(외부 규약 의존), 제어 결합(플래그로 상대 동작 지정), 스탬프 결합(큰 자료구조 전달), 자료 결합(필요 값 전달) 등으로 구분합니다. 객체 간 메시지 계약으로 내부 의존을 줄일 수 있지만 호출 수만 줄이는 것은 목표가 아닙니다.",
        "fan-in은 해당 모듈을 호출하는 모듈 수, fan-out은 해당 모듈이 호출하는 모듈 수입니다. 높은 fan-in은 재사용이나 공통 병목, 높은 fan-out은 조정 책임의 복잡성 가능성을 뜻하며 그 자체가 결함 판정은 아닙니다.",
        "정보은닉은 접근제한자만 붙이는 것으로 끝나지 않습니다. 내부 자료형·정책·외부 도구를 그대로 반환하지 않고 불변식과 작업 계약을 제공해야 내부 변경이 외부로 번지지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "캡슐화",
            "데이터와 연산을 경계로 묶음",
            "구조를 만드는 수단"
          ],
          [
            "정보은닉",
            "불필요한 내부 지식을 외부에서 차단",
            "변경 파급을 줄이는 설계 목적"
          ],
          [
            "응집·결합 지표",
            "내부 책임과 외부 의존을 관찰",
            "맥락과 변경 시나리오를 함께 평가"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 계좌 모듈 경계",
        "input": "여러 화면이 balance 변수를 직접 수정합니다.",
        "steps": [
          "잔액을 비공개로 두고 입금·출금 연산에 금액 검증과 잔액 불변식을 모읍니다.",
          "UI가 자료구조를 수정하지 않고 withdraw(amount) 결과만 받도록 합니다.",
          "내부 저장을 메모리에서 DB로 바꿀 때 외부 계약이 유지되는지 시험합니다."
        ],
        "result": "정책과 저장 변경의 파급 범위를 계좌 모듈 안으로 줄입니다.",
        "caution": "예시는 단일 계좌 동작입니다. 실제 금융 시스템은 동시성·원장·감사 통제가 추가됩니다."
      },
      "answer_outline": [
        "정의와 설계 목표",
        "응집/결합 종류·fan-in/out",
        "캡슐화와 은닉의 차이 및 사례"
      ],
      "pitfalls": [
        "높은 fan-in만으로 좋은 모듈이라고 결론내리지 않습니다.",
        "getter로 내부 가변 객체를 노출하면 private 필드라도 은닉이 깨집니다."
      ],
      "recall": [
        "제어 결합과 자료 결합의 예를 만드십시오.",
        "캡슐화했지만 은닉하지 못한 코드는 어떤 모습입니까?",
        "fan-out이 큰 조정 모듈은 언제 정당합니까?"
      ],
      "source_ids": [
        "sb-parnas",
        "sb-swebok"
      ],
      "validation": "부분 확인",
      "version_note": "모듈성 원리는 원 논문과 SWEBOK에서 확인했습니다. 고전 응집·결합 유형의 전 목록은 공개 대학 교재 추가 대조가 필요합니다.",
      "requirements": [
        {
          "question": "128-3-1",
          "items": [
            "소프트웨어 모듈의 응집도와 결합도",
            "소프트웨어 모듈의 fan-in과 fan-out"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-1-7",
          "items": [
            "소프트웨어 결합도(Coupling)의 종류"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-1-9",
          "items": [
            "객체지향 프로그래밍의 캡슐화(Encapsulation)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-1-12",
          "items": [
            "객체지향 방법론에서 캡슐화(Encapsulation)와 정보은닉(Information Hiding)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "134-1-5",
          "items": [
            "객체 간의 데이터 보호를 위한 정보은닉(Information Hiding)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "architecture-styles-design-patterns",
      "title": "아키텍처 스타일·GoF 패턴·프록시",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "스타일은 시스템의 큰 연결 규칙, 패턴은 반복되는 설계 문제를 푸는 협력 구조입니다.",
      "definition": "아키텍처 스타일은 구성요소·연결자·제약으로 시스템 전체의 조직을 규정하고, 디자인 패턴은 특정 맥락에서 반복되는 설계 문제의 역할·협력·결과를 재사용 가능한 형태로 설명합니다.",
      "principles": [
        "계층형은 표현·업무·데이터 책임을 나누어 변경과 의존을 관리하지만 계층 관통 호출과 불필요한 지연을 통제해야 합니다. 파이프-필터는 단계별 변환을 연결해 재사용·병렬화를 돕지만 공유 상태와 대화형 처리가 어렵습니다. 클라이언트-서버는 요청자와 서비스 제공자를 분리하되 서버 병목과 네트워크 장애를 고려합니다.",
        "GoF 생성 패턴은 객체 생성 변경을 감추는 Factory Method·Abstract Factory·Builder 등을, 구조 패턴은 구성·접근을 바꾸는 Adapter·Decorator·Proxy 등을, 행위 패턴은 알고리즘과 협력을 바꾸는 Strategy·Observer·Command 등을 다룹니다.",
        "Proxy는 Subject 인터페이스를 구현하고 RealSubject를 대신 참조해 접근을 통제합니다. 원격 프록시, 지연 생성의 가상 프록시, 권한 검사의 보호 프록시가 대표적이며 호출자는 같은 계약을 사용합니다.",
        "리팩토링은 외부 동작을 유지하는 변화의 과정이고 패턴은 도착 가능한 설계 구조입니다. 모두 유지보수성을 도울 수 있으나 패턴 도입은 클래스·간접호출을 늘릴 수 있으므로 실제 변화 압력이 있을 때 선택합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "스타일",
            "시스템 수준 구성과 제약",
            "계층형·파이프필터·클라이언트서버"
          ],
          [
            "디자인 패턴",
            "클래스·객체의 역할과 협력",
            "생성·구조·행위 문제 해결"
          ],
          [
            "리팩토링",
            "행동을 보존하는 작은 변환",
            "필요할 때 패턴 구조로 이동"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 대용량 문서 프록시",
        "input": "목록 화면에서 실제 PDF 전체를 즉시 읽어 지연됩니다.",
        "steps": [
          "Document.display()를 Subject 계약으로 정합니다.",
          "DocumentProxy는 파일 위치와 제목만 보관하고 최초 display 시 RealDocument를 생성합니다.",
          "로그인 권한을 먼저 확인하고 생성 실패를 같은 계약의 오류로 반환합니다."
        ],
        "result": "사용하지 않은 문서의 로딩을 늦추고 접근 정책을 모을 수 있습니다.",
        "caution": "지연 로딩은 총비용을 제거하지 않으며 첫 열람 지연과 동시 생성 제어가 필요합니다."
      },
      "answer_outline": [
        "스타일과 패턴 비교",
        "스타일 3종과 GoF 분류·대표 예",
        "Proxy 객체 연결 및 리팩토링과의 관계"
      ],
      "pitfalls": [
        "모든 프록시가 네트워크 리버스 프록시를 의미하지 않습니다.",
        "패턴 명칭 나열 대신 해결하는 변경 문제를 적습니다."
      ],
      "recall": [
        "Proxy와 Decorator의 주된 의도는 어떻게 다릅니까?",
        "파이프-필터에 공유 상태가 많으면 무엇이 어려워집니까?",
        "리팩토링과 디자인 패턴의 공통점과 차이점을 말하십시오."
      ],
      "source_ids": [
        "sb-swebok",
        "sb-refactoring"
      ],
      "validation": "부분 확인",
      "version_note": "SWEBOK의 스타일·패턴 구분은 확인했습니다. GoF 원저 전체를 열람하지 않아 세부 분류·표기의 규범적 대조는 추가 확인 필요합니다.",
      "requirements": [
        {
          "question": "131-2-6",
          "items": [
            "아키텍처 스타일과 디자인 패턴의 차이점",
            "대표적인 아키텍처 스타일 3가지",
            "GoF(Gang of Four) 디자인 패턴의 유형을 구분하고, 유형별 대표적인 디자인 패턴 설명"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-2-6",
          "items": [
            "객체지향의 기법 중에는 리팩토링(Refactoring)과 디자인패턴(Design Pattern)이 있다. 두 기법을 각각 정의하고 공통점과 차이점에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "136-1-5",
          "items": [
            "프록시(Proxy) 디자인 패턴"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "architecture-evaluation-atam-cbam",
      "title": "아키텍처 분석·ATAM·CBAM",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "아키텍처 평가는 그림의 예쁨이 아니라, 중요한 상황에서 설계가 품질 목표를 만족하는지 따져보는 일입니다.",
      "definition": "ATAM은 이해관계자의 품질속성 시나리오로 아키텍처의 위험·민감점·절충점을 찾는 평가 방법이고, CBAM은 아키텍처 대안에 비용·편익·불확실성을 결합해 투자 우선순위를 결정하는 방법입니다.",
      "principles": [
        "정방향 분석은 요구와 설계 의도에서 예상 품질·의존을 평가합니다. 역방향 분석은 코드·실행·배포 정보에서 실제 구조를 복원하여 설계와의 차이를 찾습니다. 정방향의 주장과 역방향의 관찰을 대조하면 아키텍처 침식을 발견할 수 있습니다.",
        "ATAM의 9단계는 방법 소개, 사업동인 제시, 아키텍처 제시, 아키텍처 접근법 식별, 품질속성 효용트리 작성, 접근법 분석, 시나리오 브레인스토밍·우선순위화, 재분석, 결과 발표입니다. 시나리오는 자극원·자극·환경·대상·반응·반응척도로 구체화합니다.",
        "민감점은 설계 매개변수가 특정 품질에 큰 영향을 주는 지점, 절충점은 여러 품질에 서로 다른 영향을 주는 지점입니다. 예컨대 캐시는 지연을 줄이지만 최신성·복구 복잡도와 절충할 수 있습니다. 위험은 근거가 부족하거나 목표를 위협하는 결정입니다.",
        "CBAM은 시나리오별 효용과 중요도를 정하고 전략이 반응 수준을 얼마나 개선하는지 편익을 산정합니다. 비용·일정·불확실성과 비교해 예산 안의 전략 조합을 선택하며 단순히 ATAM 점수로 ROI를 계산하는 것은 아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "ATAM",
            "품질속성 위험·절충 분석",
            "정성·정량 시나리오와 설계 근거"
          ],
          [
            "CBAM",
            "경제적 효용과 비용 결합",
            "자원이 제한된 개선 전략 선택"
          ],
          [
            "역방향 분석",
            "구현에서 구조 복원",
            "문서-구현 차이와 실제 의존 탐지"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 조회 서비스 캐시 도입",
        "input": "응답 p95 3초를 1초로 줄이되 가격 최신성은 10초 이내여야 합니다.",
        "steps": [
          "성능·최신성 시나리오를 효용트리에 넣고 중요도를 합의합니다.",
          "TTL 변경이 지연과 최신성에 미치는 영향을 분석해 절충점으로 기록합니다.",
          "캐시와 DB색인 대안의 개선효용·구현비·운영비를 비교합니다."
        ],
        "result": "설계 위험과 비용에 근거한 선택안을 만듭니다.",
        "caution": "효용 점수와 예시 성능은 가정이며 확률이나 실제 성과가 아닙니다."
      },
      "answer_outline": [
        "분석 필요성과 정/역방향",
        "ATAM 절차·산출물·민감/절충점",
        "CBAM 경제성 및 사례"
      ],
      "pitfalls": [
        "중심성이나 복잡도 하나로 아키텍처 우열을 단정하지 않습니다.",
        "ATAM은 위험을 찾아내며 품질을 인증해 주지 않습니다."
      ],
      "recall": [
        "민감점과 절충점을 캐시 사례로 설명하십시오.",
        "효용트리는 기능 목록과 무엇이 다릅니까?",
        "CBAM에서 비용이 싼 대안이 항상 선택됩니까?"
      ],
      "source_ids": [
        "sb-atam",
        "sb-cbam"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "126-3-5",
          "items": [
            "소프트웨어 아키텍처 분석의 필요성",
            "소프트웨어 아키텍처 정방향 분석과 역방향 분석 개념",
            "소프트웨어 아키텍처 평가 기법 중 ATAM(Architecture Trade-off Analysis Method)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "128-1-7",
          "items": [
            "소프트웨어 아키텍처 평가모델 중 CBAM(Cost Benefit Analysis Method)에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "140-1-3",
          "items": [
            "ATAM(Architecture Trade-off Analysis Method)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "microservices-event-driven-architecture",
      "title": "MSA·서비스 메시·이벤트 아키텍처",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "작은 서비스로 나눈다는 것은 배포 경계를 나누는 것이고, 이벤트로 연결한다는 것은 시간과 제어의 결합을 줄이는 선택입니다.",
      "definition": "MSA는 업무 능력 중심의 독립 배포 가능한 서비스와 명확한 계약으로 시스템을 구성합니다. 서비스 메시는 서비스 간 통신 정책을 데이터·제어 평면으로 다루며, EDA는 상태 변화를 이벤트로 발행하여 소비자가 반응하는 구조입니다.",
      "principles": [
        "MSA에서는 경계가 분명한 업무 책임, 독립 배포·자동화, 서비스 소유 데이터, 장애 격리, 관측가능성을 설계합니다. 모놀리스는 단일 배포와 로컬 호출·트랜잭션이 단순하지만 서비스 분리는 네트워크 지연, 분산 일관성, 운영 복잡도를 늘립니다.",
        "서비스 메시는 프록시 기반 또는 다른 데이터평면 구현으로 라우팅·재시도·타임아웃·상호인증·계측을 제공하고 제어평면이 정책을 배포합니다. 업무 코드를 대체하거나 분산 트랜잭션 문제를 자동 해결하지 않습니다.",
        "중재자 토폴로지는 초기 이벤트를 중앙 중재자가 해석해 단계·순서를 조정합니다. 복잡한 업무 흐름과 추적은 명확하지만 중재자에 지식과 장애 영향이 집중될 수 있습니다.",
        "브로커 토폴로지는 발행 이벤트를 중개하고 소비자가 독립 반응합니다. 확장·변경 격리에 유리하나 전체 흐름 추적·재처리·보상·순서·중복을 명시해야 합니다. 적어도 한 번 전달에서는 소비자의 멱등 처리가 특히 중요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "모놀리스",
            "한 배포·로컬 일관성",
            "규모가 작을 때 운영 단순"
          ],
          [
            "MSA",
            "독립 배포·서비스 소유권",
            "조직과 자동화 역량 필요"
          ],
          [
            "중재자/브로커",
            "중앙 업무 조정 / 분산 반응",
            "업무 가시성 / 느슨한 결합의 절충"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 주문 후 배송 준비",
        "input": "주문서비스가 OrderPlaced를 발행합니다.",
        "steps": [
          "중재자 방식은 결제→재고→배송을 오케스트레이터가 지시합니다.",
          "브로커 방식은 결제·재고 소비자가 이벤트에 반응하고 실패 이벤트에 보상합니다.",
          "주문 ID로 중복 처리를 막고 메시의 타임아웃·계측 정책을 설정합니다."
        ],
        "result": "각 토폴로지의 제어 위치와 실패 처리 차이가 드러납니다.",
        "caution": "서비스 수를 늘리는 것이 목표가 아니며 단일 DB 공유는 독립성을 약화할 수 있습니다."
      },
      "answer_outline": [
        "MSA 특징·원칙·모놀리스 비교",
        "메시의 두 평면과 기능",
        "EDA 두 토폴로지 구성·실패 사례"
      ],
      "pitfalls": [
        "메시와 메시지 브로커는 다른 개념입니다.",
        "이벤트 전달 성공과 업무 트랜잭션 성공을 구분합니다."
      ],
      "recall": [
        "MSA의 독립 배포를 깨뜨리는 설계를 하나 드십시오.",
        "중재자와 브로커의 업무 지식은 어디에 있습니까?",
        "재시도에는 왜 멱등성이 필요합니까?"
      ],
      "source_ids": [
        "sb-swebok",
        "sb-dora",
        "sb-azure-msa",
        "sb-azure-eda",
        "sb-istio"
      ],
      "validation": "부분 확인",
      "version_note": "Azure공식MSA/EDA·Istio공식문서와SWEBOK의구조원리확인. Istio최신은sidecar와ambient모드를지원하므로서비스메시가항상사이드카만을뜻하지않습니다. 기출이요구한broker/mediator고정분류의원출전전체는별도확인필요합니다.",
      "requirements": [
        {
          "question": "127-4-1",
          "items": [
            "MSA 개념 및 특징과 구현시 지켜야 할 원칙",
            "모놀리스 아키텍처(Monolith Architecture)와 MSA 비교",
            "MSA 구현을 위한 서비스 매쉬(Service Mesh)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-3-5",
          "items": [
            "EDA(Event Driven Architecture)의 토폴로지 구성요소인 중재자 토폴로지(Mediator Topology), 브로커 토폴로지(Broker Topology)를 비교 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "technical-application-architect",
      "title": "TA와 AA의 역할·산출물·협업",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "TA는 시스템이 놓일 기술 기반을, AA는 업무 기능이 협력하는 애플리케이션 구조를 설계합니다.",
      "definition": "TA(Technical Architect)는 인프라·플랫폼·연결·배포·비기능 기반의 기술 아키텍처를, AA(Application Architect)는 업무 서비스·모듈·인터페이스·애플리케이션 품질의 구조와 원칙을 책임지는 역할입니다.",
      "principles": [
        "TA는 컴퓨트·네트워크·스토리지·플랫폼·통합·가용성·보안·성능·관측 구조를 다룹니다. 기술 표준, 배포 토폴로지, 자원·용량 산정, 장애복구·운영 설계서, 기술 검증 결과가 주요 산출물입니다.",
        "AA는 업무 경계·응용 기능·서비스/모듈 책임·API·트랜잭션·데이터 접근·오류 처리·개발 표준을 다룹니다. 응용 구성도, 서비스/인터페이스 명세, 공통 모듈과 개발지침, 품질속성 설계·검증 결과가 주요 산출물입니다.",
        "클라우드 전환에서는 TA가 플랫폼을 골라도 AA가 세션·파일 저장·배치·트랜잭션을 기존 방식으로 유지하면 확장·복구가 막힐 수 있습니다. 공동 비기능 요구·의존성·ADR·성능시험·장애실험으로 기술 기반과 응용 구조를 함께 검증해야 합니다.",
        "책임 분장은 조직마다 달라 유일한 국제 표준 직무표처럼 제시하지 않습니다. DA·보안·운영·업무책임자와 RACI를 합의하고 설계심의·공통 백로그·계약시험으로 변경을 조정합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "TA",
            "플랫폼·자원·배포·운영 기반",
            "인프라 구성도·용량·복구 설계"
          ],
          [
            "AA",
            "업무 서비스·모듈·응용 계약",
            "응용 구성도·API·개발 표준"
          ],
          [
            "공동",
            "비기능 요구와 품질 증거",
            "ADR·부하/장애 시험·운영 인수"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 공공 포털과 ERP 클라우드 전환",
        "input": "대국민 조회는 확장되고 ERP 마감 배치는 정해진 시간에 끝나야 합니다.",
        "steps": [
          "AA가 조회/마감의 서비스 경계와 트랜잭션을 정합니다.",
          "TA가 배포·자원 격리·확장·복구 구조를 설계합니다.",
          "양쪽이 DB 연결 한도, 상태 저장, 배치 재시작, API 계약을 공동 시험합니다."
        ],
        "result": "플랫폼 자동확장과 실제 업무 처리 가능성을 함께 확인합니다.",
        "caution": "역할명만으로 계약상 최종 책임을 추정하지 말고 조직의 승인권을 확인해야 합니다."
      },
      "answer_outline": [
        "역할 범위·목표·산출물 비교",
        "클라우드 전환의 상호 의존",
        "협업 절차와 검증 사례"
      ],
      "pitfalls": [
        "TA는 장비 구매 담당자만을 뜻하지 않습니다.",
        "AA가 화면 설계만 한다고 축소하지 않습니다."
      ],
      "recall": [
        "자동확장이 있어도 응용이 확장되지 않는 원인은 무엇입니까?",
        "두 역할의 공동 산출물을 두 개 제시하십시오.",
        "RACI를 언제 합의해야 합니까?"
      ],
      "source_ids": [
        "sb-isp",
        "sb-swebok"
      ],
      "validation": "부분 확인",
      "version_note": "공통가이드의 목표 응용·기술 구조와 아키텍처 원리에 근거한 역할 정리입니다. 특정 기관 표준 직무 정의와의 일치는 확인이 필요합니다.",
      "requirements": [
        {
          "question": "138-2-4",
          "items": [
            "TA와 AA의 역할 비교 (범위, 책임/목표, 주요 산출물 측면)",
            "TA와 AA 협업의 중요성 및 협업 방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "uml-dice-model",
      "title": "UML 주사위 게임의 객체·시퀀스·클래스 모델",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [
        "개념적 객체 모델",
        "Sequence Diagram",
        "Class Diagram"
      ],
      "easy": "같은 게임도 개념 모델은 무엇이 있는지, 시퀀스는 누가 언제 요청하는지, 클래스 모델은 어떤 책임으로 구현하는지 보여줍니다.",
      "definition": "UML은 시스템의 구조와 행위를 공통 표기로 기술하는 모델링 언어입니다. 이 문항은 두 주사위의 합이 정확히 8일 때 승리한다는 규칙을 세 모델에서 일관되게 표현하는 것이 핵심입니다.",
      "principles": [
        "개념 객체 모델: 참여자(Player), 주사위게임(DiceGame), 주사위(Die)가 도메인 개념입니다. DiceGame 1개는 Die 2개와 관련되고 Player는 DiceGame에 참여합니다. 단순 도메인 관계 단계에서는 메서드·DB 키 같은 구현 세부를 먼저 넣지 않습니다.",
        "설계 클래스 모델: DiceGame은 die1:Die, die2:Die와 play():Result 책임을 가집니다. Die는 faceValue:Integer {1≤faceValue≤6}, roll():void, getFaceValue():Integer를 가집니다. DiceGame→Die의 다중성은 2이고 게임이 수명주기를 소유한다고 가정할 때만 합성(채운 마름모)을 사용합니다.",
        "시퀀스의 생명선 순서는 player:Player, game:DiceGame, die1:Die, die2:Die입니다. player→game:play(); game→die1:roll(); game→die1:getFaceValue()→v1; game→die2:roll(); game→die2:getFaceValue()→v2; game은 sum=v1+v2를 계산합니다.",
        "alt [sum=8] 분기에서 win, [else] 분기에서 lose를 참여자에게 반환/표시합니다. 두 주사위는 같은 객체를 두 번 굴린 것이 아니라 구별되는 인스턴스 두 개입니다. 순서는 별도 제약이 없으므로 두 roll의 순차·동시 표현 모두 책임과 값 사용이 일관되면 가능합니다.",
        "객체의 한 시점 예는 밑줄 친 game1:DiceGame, d1:Die, d2:Die와 game1—d1, game1—d2 링크이며 d1의 slot faceValue=3, d2는 faceValue=5입니다. 클래스 속성의 값 제약 1~6은 다중성 [1..6]과 다르므로 {1≤faceValue≤6}처럼 제약으로 표기합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "개념 모델",
            "도메인 개념·연관·다중성",
            "구현 이전 의미 파악"
          ],
          [
            "시퀀스",
            "객체 생명선과 시간순 메시지",
            "호출 주체·응답·분기 확인"
          ],
          [
            "클래스",
            "속성·연산·관계",
            "시퀀스 메시지를 받을 책임 제공"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 합계 8인 게임 실행",
        "input": "die1=3, die2=5라는 창작 실행값입니다.",
        "steps": [
          "Player가 game.play()를 요청합니다.",
          "각 Die가 roll 결과 3과 5를 보관하고 조회에 응답합니다.",
          "게임이 3+5=8을 평가해 win 결과를 표시합니다."
        ],
        "result": "클래스 책임·생명선·승패 가드가 서로 일치합니다.",
        "caution": "난수 구현 방식은 문항에 없으므로 특정 라이브러리나 확률분포 보장을 추가하지 않습니다."
      },
      "answer_outline": [
        "주어진 규칙과 모델링 가정",
        "개념 객체·연관·다중성",
        "호출 순서·alt 가드 및 설계 클래스 일치"
      ],
      "pitfalls": [
        "일반적인 주사위 게임 규칙으로 합계 7을 쓰면 오답입니다.",
        "클래스 이름과 객체 인스턴스 이름을 구분합니다."
      ],
      "recall": [
        "게임과 주사위 사이 다중성은 얼마입니까?",
        "합성을 선택하려면 어떤 가정이 필요합니까?",
        "합계 9의 실행은 어느 가드를 통과합니까?"
      ],
      "source_ids": [
        "sb-uml"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "126-2-4",
          "items": [
            "개념적 객체 모델(Conceptual Object Model)",
            "시퀀스 다이어그램(Sequence Diagram)",
            "클래스 다이어그램(Class Diagram)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "uml-sequence-library",
      "title": "UML 순차 다이어그램과 도서예약 변환",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "협력 다이어그램의 번호와 조건을 시간축으로 펼치면 순차 다이어그램이 됩니다.",
      "definition": "순차 다이어그램은 상호작용 참여자의 생명선 사이 메시지 발생 순서와 조건을 보여주는 UML 상호작용 다이어그램입니다. 호출 번호와 가드를 보존하며 협력 구조를 시간 순서로 바꿉니다.",
      "principles": [
        "Frame은 좌상단 sd와 상호작용 이름을 가진 범위입니다. Object는 objectName:Class 형식의 참여자 머리, Lifeline은 아래로 뻗는 점선, Activation(ExecutionSpecification)은 실행 중 구간의 얇은 직사각형입니다.",
        "동기 호출은 닫힌 화살촉의 실선, 비동기 메시지는 열린 화살촉, 반환은 점선 화살표로 구별합니다. Guard는 [조건]으로 쓰며 alt 프레임은 상호배타적 대안, opt는 선택 동작, loop는 반복을 표현합니다. 위에서 아래는 발생 순서이며 수평 길이가 수행시간은 아닙니다.",
        "목적은 참여자 간 메시지의 시간순서·조건·실행 책임을 표현하는 것입니다. 작성은 시나리오/참여자 선정→lifeline 배치→원도식 번호/화살표에 맞춘 메시지→guard/대안·실행구간→정합성 검토입니다. 참여자는 대여자, 대여, 예약, 도서, 도서항목이며 127회 공식 PDF p.7 원도식을 직접 렌더링해 연결을 확인했습니다.",
        "원도식 연결은 1 대여자→대여:대여요청, 2 대여→도서:재고확인, 3 [재고=0] 도서→대여:재고없음통보, 3 [재고>0] 도서→도서항목:대여처리, 3 도서항목→대여:대여처리, 4 대여→예약:예약요청, 5 예약→도서:예약처리입니다. 원문의 4·5에는 가드가 없어 재고=0일 때만 예약한다고 단정하지 않고 후속 메시지로 보존합니다. 통보 메시지의 반환 타입·동기성도 원도식에서 확정하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "협력/통신 다이어그램",
            "연결과 메시지 번호 중심",
            "번호·중첩번호로 순서 식별"
          ],
          [
            "순차 다이어그램",
            "생명선과 시간순 메시지",
            "조건·반복·활성구간 가시화"
          ],
          [
            "Guard / 반환",
            "실행 조건 / 응답",
            "조건은 대괄호, 반환은 점선으로 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 구성 적용 예시: 기출 도서예약 상호작용의 변환",
        "input": "127회 원도식의 참여자 5개·메시지 번호 1~5와 재고 조건을 사용합니다.",
        "steps": [
          "참여자 lifeline을 배치하고 1 대여요청과 2 재고확인을 위에서 아래로 연결합니다.",
          "원도식의 번호 3은 재고=0 통보와 재고>0 대여처리의 조건을 표시하고 도서항목→대여의 대여처리도 연결합니다.",
          "4 대여→예약, 5 예약→도서를 번호 뒤에 보존하고 원문에 없는 가드·반환값은 추가하지 않습니다."
        ],
        "result": "원도식의 객체·연결·호출순서를 보존한 순차 표현을 구성합니다.",
        "caution": "공식 답안이 아닌 강사 변환 예입니다. 번호3의세부 중첩순서와4·5의비즈니스 조건은 설계 가정이 추가될 경우 명시해야 하며 재고없음통보를 무조건 점선 반환으로 만들지 않습니다."
      },
      "answer_outline": [
        "목적·작성순서",
        "Frame/Object/Lifeline/Activation/Message/Guard 표기",
        "도서예약 메시지와 alt 변환"
      ],
      "pitfalls": [
        "가드를 메시지 이름의 설명으로만 쓰고 분기를 없애지 않습니다.",
        "원문 도식에서 불명확한 연결을 사실처럼 보충하지 않습니다."
      ],
      "recall": [
        "동기·비동기·반환 화살표를 구분해 보십시오.",
        "재고 0과 재고 양수는 어떤 프레임에 배치합니까?",
        "활성상자와 생명선은 어떻게 다릅니까?"
      ],
      "source_ids": [
        "sb-uml"
      ],
      "validation": "출처 확인",
      "version_note": "기출127회 공식PDF p.7의 원도식과 OMG2.5.1의 시퀀스 표기를 확인했습니다. 문항의UML2.0과 공통 핵심 표기를 사용하며 명시되지 않은 가드·호출/반환 타입을 확정하지 않았습니다.",
      "requirements": [
        {
          "question": "127-4-5",
          "items": [
            "순차 다이어그램의 목적과 작성순서, 구성요소별 표기법 구성요소 Frame, Object, Lifelines, Activation Box, Messages, Guard",
            "아래의 도서예약시스템의 협력 다이어그램(Collaboration Diagram)을 순차 다이어 그램으로 변환 1. 대여 요청 대여자 대여 4. 예약 요청 3. 대여 처리 2. 재고 확인 3. [재고=0] 재고 없음 통보 3. [재고>0] 5. 예약 처리 대여 처리 예약 도서 도서항목 (대여표시처리)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ],
      "diagram_data": {
        "kind": "sequence",
        "participants": [
          "대여자",
          "대여",
          "예약",
          "도서",
          "도서항목"
        ],
        "messages": [
          {
            "order": "1",
            "from": "대여자",
            "to": "대여",
            "label": "대여요청"
          },
          {
            "order": "2",
            "from": "대여",
            "to": "도서",
            "label": "재고확인"
          },
          {
            "order": "3",
            "from": "도서",
            "to": "대여",
            "label": "재고없음통보",
            "guard": "재고=0"
          },
          {
            "order": "3",
            "from": "도서",
            "to": "도서항목",
            "label": "대여처리",
            "guard": "재고>0"
          },
          {
            "order": "3",
            "from": "도서항목",
            "to": "대여",
            "label": "대여처리"
          },
          {
            "order": "4",
            "from": "대여",
            "to": "예약",
            "label": "예약요청"
          },
          {
            "order": "5",
            "from": "예약",
            "to": "도서",
            "label": "예약처리"
          }
        ],
        "note": "4·5가드는원문미표기,통보반환타입미확정;그림재구성은강사해석"
      }
    },
    {
      "id": "uml-behavior-diagrams",
      "title": "UML 활동·상태·유스케이스 다이어그램",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "활동은 일의 흐름, 상태는 한 대상의 생애, 유스케이스는 외부 사용자가 얻는 목표를 보여줍니다.",
      "definition": "행위 다이어그램은 실행과 상호작용을 모델링합니다. 활동 다이어그램은 제어·객체 흐름을, 상태기계는 이벤트에 따른 상태 전이를, 유스케이스는 액터와 시스템 목표 기능의 관계를 표현합니다.",
      "principles": [
        "활동의 시작은 채운 원, 행동은 둥근 사각형, 의사결정/병합은 마름모, fork/join은 굵은 막대, 활동 종료는 이중 원으로 표현합니다. 분기의 [가드]와 병렬의 fork를 혼동하지 말고 객체 흐름으로 데이터 전달을 표현합니다.",
        "상태는 둥근 사각형으로 나타내고 전이는 event [guard] / effect 형식입니다. entry·do·exit 동작은 상태의 진입·유지·이탈에 대응합니다. 하나의 객체가 같은 이벤트에도 현재 상태에 따라 다르게 반응하는 규칙을 명확히 할 때 유용합니다.",
        "유스케이스는 시스템 경계 상자 안 타원으로, 외부 역할인 액터는 바깥에 둡니다. include는 공통 필수 행위를 포함하는 유스케이스에서 포함 대상 방향으로, extend는 조건부 확장 유스케이스에서 기본 유스케이스 방향으로 점선 화살표를 그립니다.",
        "세 도식을 하나의 상세도처럼 섞지 않습니다. 유스케이스로 목표·범위를 합의하고 활동으로 시나리오 흐름을 풀며 상태기계로 객체 생애 제약을 검증할 수 있습니다. 관계 경로 자체가 반드시 개발 순서를 뜻하지는 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "활동",
            "행동·결정·병렬 흐름",
            "신청→검증→심사→통지"
          ],
          [
            "상태",
            "현재 상태와 사건에 따른 전이",
            "작성중→접수→승인/반려"
          ],
          [
            "유스케이스",
            "외부 액터의 목표",
            "민원인이 신청, 심사자가 심사"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 민원 신청 모델",
        "input": "민원인·심사자 두 역할과 신청서 객체가 있습니다.",
        "steps": [
          "유스케이스: 민원인—신청, 심사자—심사; 신청 include 본인확인으로 연결합니다.",
          "활동: 시작→작성→검증→[오류]수정 또는 [정상]제출→종료를 그립니다.",
          "상태: 작성중 --submit[검증성공]/접수번호발급→접수, 접수 --approve→승인으로 그립니다."
        ],
        "result": "동일한 업무를 목표·흐름·생애라는 다른 관점으로 설명할 수 있습니다.",
        "caution": "실제 본인확인 의무는 업무별로 다릅니다. 여기서는 도식 학습을 위한 가정입니다."
      },
      "answer_outline": [
        "세 다이어그램 정의와 목적",
        "노드·연결·가드 표기",
        "동일 업무 적용 및 include/extend 방향"
      ],
      "pitfalls": [
        "액터는 특정 개인이 아니라 외부 역할입니다.",
        "상태명에 모든 업무 절차를 나열하지 않습니다."
      ],
      "recall": [
        "fork와 decision은 어떻게 다릅니까?",
        "extend 화살표는 어느 방향입니까?",
        "상태 전이에 가드와 효과를 적는 예를 만드십시오."
      ],
      "source_ids": [
        "sb-uml"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "137-4-4",
          "items": [
            "UML(Unified Modeling Language)에서 사용하는 행위 다이어그램(Behavior Diagram)인 활동 다이어그램(Activity Diagram), 상태 다이어그램(State Diagram), 그리고 유스케이스 다이어그램(Use-Case Diagram)에 대하여 각각 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "refactoring-code-smell-technical-debt",
      "title": "리팩토링·코드스멜·기술부채",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [
        "코드스멜",
        "기술부채",
        "리팩토링"
      ],
      "easy": "코드스멜은 점검 신호이고, 기술부채는 앞으로 추가로 치를 변경 비용이며, 리팩토링은 동작을 보존해 구조를 개선하는 작업입니다.",
      "definition": "리팩토링은 관찰 가능한 외부 행동을 바꾸지 않고 내부 구조를 작은 단계로 재구성하는 기법입니다. 기술부채는 빠른 선택이나 학습으로 남은 구조상의 부족이 이후 변경에 추가 비용을 만드는 현상을 설명하는 비유입니다.",
      "principles": [
        "명확하지 않은 요구는 임시 분기·중복·예외 누락을 만들 수 있습니다. 다만 모든 결함과 스멜이 곧 기술부채인 것은 아니고, 기술부채는 후속 작업의 이자 비용과 갚을 원금을 함께 따져 관리해야 합니다.",
        "리팩토링 순서는 변경 목적·행동 계약 확인→회귀시험 확보→작은 변환→시험→반복→구조와 문서 정합성 확인입니다. 기능 추가와 구조 변경을 구별하면 실패의 원인을 좁히기 쉽습니다.",
        "긴 메서드는 Extract Function으로 책임을 나누고, 중복 코드는 공통 의미가 같을 때 추출합니다. 큰 클래스는 책임에 따라 Extract Class, 기능 편애는 책임 있는 데이터 쪽으로 Move Function, 원시값 집착은 의미 있는 타입 도입을 검토합니다.",
        "부채는 요구·설계/아키텍처·코드·테스트·문서/운영 등 발생 위치와 의도·인지 여부로 구분할 수 있습니다. 등록부에 근거·영향·지연비용·상환안·담당자·기한을 적고 변경 빈도와 위험이 큰 부채부터 일정에 반영합니다. 무조건 전면 재작성하는 것은 상환 전략이 아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "코드스멜",
            "구조 문제 가능성의 징후",
            "정적 지표와 코드 맥락으로 판단"
          ],
          [
            "기술부채",
            "미래의 추가 비용·위험",
            "사업상 선택과 우선순위 관리"
          ],
          [
            "리팩토링",
            "행동 보존 구조 변환",
            "작은 단계와 회귀 검증 필요"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 할인 규칙의 중복 제거",
        "input": "여러 화면이 서로 다른 할인 조건을 구현합니다.",
        "steps": [
          "현행 입출력과 예외를 특성화 시험으로 고정합니다.",
          "한 가지 의미의 할인 계산을 별도 함수/정책 객체로 옮기고 호출자를 하나씩 전환합니다.",
          "불명확했던 규칙은 별도 요구 변경으로 승인하고 시험을 추가합니다."
        ],
        "result": "구조 정리와 요구 수정의 효과를 구분하여 검증할 수 있습니다.",
        "caution": "의미가 다른 코드를 모양이 비슷하다는 이유만으로 합치면 잘못된 추상화를 만들 수 있습니다."
      },
      "answer_outline": [
        "세 개념의 정의·연결",
        "코드스멜 3종 이상과 개선기법",
        "부채 유형·관리·요구 불명확성 사례"
      ],
      "pitfalls": [
        "행동이 달라졌다면 그 변경 전체를 리팩토링이라고 부르지 않습니다.",
        "부채 규모를 LOC나 스멜 개수만으로 확정하지 않습니다."
      ],
      "recall": [
        "Extract Function이 적절하지 않은 중복은 무엇입니까?",
        "부채 원금과 이자는 각각 무엇입니까?",
        "요구 변경과 리팩토링을 어떻게 나누어 검증합니까?"
      ],
      "source_ids": [
        "sb-refactoring",
        "sb-debt",
        "sb-swebok"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "127-3-2",
          "items": [
            "정의, 목적, 리팩토링 순서, 리팩토링 주요기법",
            "코드스멜(Code Smell)의 정의와 특징",
            "코드스멜의 종류를 3개 이상 기술하고 각각의 리팩토링 방법"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "135-1-9",
          "items": [
            "소프트웨어 기술 부채의 유형과 관리 방법"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-3-3",
          "items": [
            "기술부채(Technical Debt)",
            "코드스멜(Code Smell)",
            "리팩토링(Refactoring)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-reengineering-three-r",
      "title": "역공학·재공학·재구조화와 3R",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [
        "3R",
        "Reverse Engineering",
        "Reengineering",
        "Restructuring"
      ],
      "easy": "역공학은 현재 구현의 의미를 알아내고, 재공학은 그 이해를 바탕으로 다시 쓸 수 있는 형태로 바꾸는 작업입니다.",
      "definition": "역공학은 구현에서 설계·구조·요구 등 높은 추상수준의 정보를 복원하는 분석이며, 재공학은 기존 시스템을 조사·변환하여 새 형태로 재구성하는 유지보수 개선 활동입니다.",
      "principles": [
        "3R은 수험 자료에서 Reverse Engineering(역공학), Restructuring(재구조화), Reengineering(재공학)으로 묶는 관행이 있습니다. 이는 서로 완전히 배타적인 수명주기 단계가 아니라, 재공학 안에 역공학과 재구조화가 포함될 수 있는 관계입니다.",
        "재공학은 대상 자산·업무 가치·위험 평가→문서/코드/데이터 이해→구조·자료·인터페이스 개선 설계→변환·재구성→동등성·성능·회귀 검증→전환·운영 안정화 순으로 계획할 수 있습니다. 목표에 따라 자동 변환과 점진 대체를 조합합니다.",
        "역공학은 호출/의존 분석, 데이터·규칙 추출, 실행 추적과 아키텍처 복원으로 문서 없는 레거시의 영향분석·이관·보안 검토를 돕습니다. 분석만 수행하는 경우 시스템의 외부 행동을 바꾸는 활동은 아닙니다.",
        "재구조화는 같은 추상수준에서 코드·데이터 구조를 정리하는 변환이고, 재공학은 플랫폼 전환·데이터 이관·업무 개선까지 넓어질 수 있습니다. 라이선스·영업비밀·개인정보·호환 계약, 원본 보존과 회귀 증거를 고려합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "역공학",
            "구현→추상 모델 복원",
            "이해·영향분석·이관 준비"
          ],
          [
            "재구조화",
            "동일 수준에서 구조 변환",
            "코드/자료 구조 개선"
          ],
          [
            "재공학",
            "분석과 변환을 통한 재구성",
            "유지보수성·플랫폼 수명 연장"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 문서 없는 배치 시스템 이전",
        "input": "정산 배치의 코드는 있으나 업무 규칙 문서가 부족합니다.",
        "steps": [
          "실행 로그와 호출 그래프, SQL을 분석해 입력·정산규칙·출력을 복원합니다.",
          "중복 모듈과 데이터 구조를 정리하고 새 플랫폼으로 단계적으로 변환합니다.",
          "같은 입력에 대한 금액·건수·예외 처리 결과를 구/신 시스템에서 비교합니다."
        ],
        "result": "현행 의미를 잃지 않으면서 전환 위험을 통제합니다.",
        "caution": "기존 동작의 오류를 바로잡는 경우에는 동등성 검증과 별도로 요구 변경을 명시해야 합니다."
      },
      "answer_outline": [
        "3R 정의·관계",
        "재공학 목적과 절차",
        "역공학 활용·검증·법적 고려"
      ],
      "pitfalls": [
        "역공학만으로 새 구현이 완성되는 것은 아닙니다.",
        "재공학이 항상 전면 재작성보다 싸다고 단정하지 않습니다."
      ],
      "recall": [
        "역공학 산출물을 세 가지 말하십시오.",
        "재구조화와 재공학의 범위는 어떻게 다릅니까?",
        "잘못된 기존 규칙은 동등성 검증에서 어떻게 처리합니까?"
      ],
      "source_ids": [
        "sb-swebok"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "133-1-11",
          "items": [
            "소프트웨어 유지보수 향상 및 비용절감을 위한 3R을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "137-1-11",
          "items": [
            "소프트웨어 역공학과 재공학을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "138-2-5",
          "items": [
            "재공학 개념 및 목적",
            "재공학 절차",
            "역공학 개념 및 활용 방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "spring-boot-aop",
      "title": "Spring Boot와 AOP",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "Boot는 반복 설정을 줄여 실행을 시작하게 돕고, AOP는 여러 기능에 흩어진 공통 관심을 따로 모읍니다.",
      "definition": "Spring Boot는 자동설정·의존성 관리와 실행 지원으로 Spring 애플리케이션 구성을 단순화합니다. AOP는 로깅·권한·트랜잭션처럼 여러 객체에 걸친 횡단 관심을 Aspect라는 모듈로 분리하는 접근입니다.",
      "principles": [
        "Boot 자동설정은 클래스패스 의존성, 정의된 빈, 설정값 같은 조건을 보고 필요한 구성을 등록합니다. 사용자가 명시한 DataSource 등이 있으면 관련 기본 설정이 물러날 수 있고, 조건 평가 보고서로 적용 근거를 점검할 수 있습니다.",
        "starter는 관련 의존성 묶음을 일관되게 가져오도록 돕고 외부설정은 환경별 값을 코드와 구분합니다. 실행 가능한 애플리케이션과 내장 서버, 운영 엔드포인트 등은 구성 부담을 줄이지만 자동 선택된 설정을 이해하고 노출 범위를 통제해야 합니다.",
        "AOP의 Aspect는 관심 모듈, Join Point는 적용 가능한 실행 지점, Pointcut은 지점 선택식, Advice는 그 지점에서 수행할 동작, Weaving은 적용 결합입니다. Spring AOP는 주로 프록시를 통해 메서드 실행을 가로챕니다.",
        "공통 로깅이나 트랜잭션 처리를 업무 코드에서 분리하면 중복을 줄일 수 있으나 프록시를 거치지 않는 내부 자기호출, 적용 순서, 예외/트랜잭션 전파를 고려해야 합니다. AOP가 객체지향을 대체하지는 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "Spring",
            "객체 생성·의존성·애플리케이션 기반",
            "명시 구성과 확장"
          ],
          [
            "Spring Boot",
            "조건 기반 자동설정·실행 편의",
            "기본값과 실제 적용을 검토"
          ],
          [
            "AOP",
            "횡단 관심의 분리·적용",
            "선택한 메서드 경계에서 정책 실행"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 결제 처리 로그 분리",
        "input": "결제·취소·환불 메서드에 수행시간 코드가 반복됩니다.",
        "steps": [
          "Boot로 웹·DB 의존성을 구성하고 자동설정 결과를 확인합니다.",
          "결제 서비스 메서드를 선택하는 Pointcut과 시간 측정 Around Advice를 정의합니다.",
          "정상·예외 경로와 프록시를 경유하지 않는 자기호출을 시험합니다."
        ],
        "result": "업무 계산식과 공통 계측의 책임을 나눌 수 있습니다.",
        "caution": "실제 결제정보나 인증정보를 로그에 남기는 설계는 피해야 합니다."
      },
      "answer_outline": [
        "Boot 특징과 자동설정",
        "AOP 구성·적용 흐름",
        "기대효과·프록시 한계와 사례"
      ],
      "pitfalls": [
        "자동설정은 모든 설정을 마법처럼 최적화하지 않습니다.",
        "Spring AOP와 AspectJ의 전체 weaving 범위를 같다고 보지 않습니다."
      ],
      "recall": [
        "자동설정이 물러나는 조건의 예는 무엇입니까?",
        "Pointcut과 Advice는 어떻게 다릅니까?",
        "자기호출에서 Advice가 누락될 수 있는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-springboot",
        "sb-aop"
      ],
      "validation": "출처 확인",
      "version_note": "열람 화면은 Boot4.1.2/Framework7.0.10입니다. 기출은 이전 세대이므로 세부 버전 요구와 API는 당시 문서와 구분해야 합니다.",
      "requirements": [
        {
          "question": "127-1-6",
          "items": [
            "스프링 부트(Spring Boot)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-1-3",
          "items": [
            "AOP(Aspect Oriented Programming)의 정의, 구성, 기대효과"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "low-code-no-code",
      "title": "로우코드·노코드 플랫폼",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "화면을 끌어다 만드는 속도뿐 아니라, 만들어진 앱의 권한·데이터·변경을 누가 관리하는지도 설계해야 합니다.",
      "definition": "로우코드는 시각 모델·템플릿·연결자와 필요한 코드를 결합하여 앱 개발을 단순화하고, 노코드는 정해진 기능과 설정 중심으로 프로그래밍 부담을 더 줄이는 플랫폼 접근입니다.",
      "principles": [
        "주요 특징은 모델 기반 화면·업무흐름, 데이터 연결자, 재사용 컴포넌트, 자동 생성/실행, 통합 배포·모니터링입니다. 로우코드는 전문 개발자의 확장 코드를 허용하는 경우가 많고 노코드는 업무 사용자의 구성 범위 안 해결을 지향하지만 제품별 경계는 연속적입니다.",
        "적용 전 업무 복잡성, 사용자 규모, 지연·가용성, 연계 API, 데이터 위치·분류, 모바일·접근성, 배포와 버전·시험 가능성을 평가합니다. 간단한 승인·조회 앱은 적합할 수 있으나 복잡한 최적화·실시간 제어는 별도 기술이 필요할 수 있습니다.",
        "한계는 공급자 종속·이식성, 라이선스와 호출비용, 성능/확장 제약, 디버깅·자동시험의 제약, 시민개발자의 보안 실수와 그림자 IT입니다. 생성된 코드가 보이지 않아도 책임이 사라지지 않습니다.",
        "CoE가 환경·계정·연결자·데이터 손실방지 정책·소유자·폐기 규칙·승인 게이트·교육을 운영하고 전문 개발자는 공통 API·배포 자동화·복잡한 확장을 지원합니다. PoC로 요구 적합성과 총비용을 검증한 뒤 범위를 확장합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "노코드",
            "기성 기능과 설정 중심",
            "빠른 소규모 업무 앱, 확장 제한"
          ],
          [
            "로우코드",
            "시각모델+선택적 코드",
            "개발자 확장과 복잡 연계 가능"
          ],
          [
            "일반 개발",
            "코드로 세밀한 제어",
            "자유도와 구축·운영 책임 증가"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 휴가 승인 앱",
        "input": "사내 직원 200명의 휴가 신청·승인을 자동화합니다.",
        "steps": [
          "신청폼·승인흐름을 시각 모델로 만들고 인사 API 연결 권한을 제한합니다.",
          "관리 환경에만 배포하고 소유자·감사로그·퇴사자 권한 회수를 정합니다.",
          "API 지연과 호출비용, 데이터 내보내기·플랫폼 종료 절차를 시험합니다."
        ],
        "result": "개발 속도와 조직 통제를 함께 검증한 적용안을 얻습니다.",
        "caution": "직원 수와 도구 구성은 창작 예시이며 특정 제품의 성능 보장이 아닙니다."
      },
      "answer_outline": [
        "특징 및 no-code 비교",
        "적용조건·한계",
        "CoE·ALM·PoC 대응 사례"
      ],
      "pitfalls": [
        "노코드는 데이터·권한 설계까지 필요 없다는 뜻이 아닙니다.",
        "플랫폼 제품마다 확장과 코드 추출 범위가 다릅니다."
      ],
      "recall": [
        "노코드로 만들기 어려운 요구를 하나 제시하십시오.",
        "CoE가 최소한 관리할 세 가지는 무엇입니까?",
        "구독료 외의 총비용 항목은 무엇입니까?"
      ],
      "source_ids": [
        "sb-coe"
      ],
      "validation": "부분 확인",
      "version_note": "Microsoft 공식 CoE 문서를 실제 열람했습니다. 로우코드/노코드는 제품별 용어 경계가 다르므로 일반화된 비교로 제시했습니다.",
      "requirements": [
        {
          "question": "130-1-1",
          "items": [
            "노코드(no-code)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "138-3-2",
          "items": [
            "로우코드(Low Code)의 주요 특징",
            "노코드 (No Code)와 로우코드(Low Code) 비교",
            "로우코드(Low Code) 적용 시 한계점"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "rest-soap-open-api",
      "title": "REST·SOAP·Open API 설계",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "Open API는 공개 범위의 선택이고, REST와 SOAP는 통신을 설계하는 서로 다른 접근입니다.",
      "definition": "Open API는 정해진 계약을 외부 개발자나 시스템에 개방하는 인터페이스입니다. REST는 네트워크 시스템의 아키텍처 제약 집합이고 SOAP는 XML 기반 메시징 프레임워크입니다.",
      "principles": [
        "REST의 제약은 클라이언트-서버, 무상태, 캐시, 일관된 인터페이스, 계층화와 선택적 코드 온 디맨드입니다. 일관된 인터페이스는 자원 식별, 표현을 통한 조작, 자기설명 메시지, 애플리케이션 상태의 하이퍼미디어를 포함합니다. HTTP+JSON이라는 사실만으로 모든 REST 제약을 만족하지 않습니다.",
        "SOAP 메시지는 Envelope 안에 선택적 Header와 Body를 두며 오류는 Fault로 표현합니다. WSDL은 서비스 계약 기술, WS-Security 등은 별도 관련 규격입니다. SOAP 자체를 HTTP에만 한정하지 않습니다.",
        "HTTP API는 자원 URI·메서드 의미·상태코드·스키마·버전·페이징·멱등성·오류 응답을 계약으로 명세해야 합니다. GET은 조회, PUT은 대상 표현의 대체, POST는 대상 자원의 의미에 따른 처리를 나타내며 관례와 규범을 구분합니다.",
        "공개 시 인증·인가, 객체별 권한, 입력/출력 검증, 속도·용량 제한, 비밀 관리, 변경 공지·폐기 정책, 모니터링이 필요합니다. 특히 로그인 여부 확인만으로 다른 사용자 주문을 열람하게 하면 객체 수준 권한 문제가 남습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "Open API",
            "외부에 제공하는 계약·운영 정책",
            "REST·SOAP 등 여러 방식 사용 가능"
          ],
          [
            "REST",
            "자원·표현·제약 기반 스타일",
            "분산 웹의 확장과 진화 지향"
          ],
          [
            "SOAP",
            "Envelope/Header/Body/Fault",
            "명시적 메시지와 관련 계약 규격 활용"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 주문 조회 API",
        "input": "파트너가 자신의 주문을 조회해야 합니다.",
        "steps": [
          "GET /orders/{id}와 응답 스키마·오류 코드를 공개합니다.",
          "토큰의 파트너 ID와 주문 소유권을 서버에서 함께 검증합니다.",
          "변경 시 하위 호환·요청 한도·감사로그를 점검합니다."
        ],
        "result": "통신 규약과 공개 서비스의 운영 책임을 함께 제시할 수 있습니다.",
        "caution": "보안 취약점의 상세 분류와 대응은 보안 담당 원고와 함께 확인해야 합니다."
      },
      "answer_outline": [
        "정의·특징·REST 제약",
        "SOAP 구성요소와 REST 비교",
        "API 수명주기·취약점 대응 사례"
      ],
      "pitfalls": [
        "Open API와 OpenAPI Specification을 같은 용어로 취급하지 않습니다.",
        "REST의 무상태는 서버에 DB나 자원 상태가 없다는 뜻이 아닙니다."
      ],
      "recall": [
        "REST 무상태에서 유지하지 않는 상태는 무엇입니까?",
        "SOAP Header와 Body의 역할은 무엇입니까?",
        "인증이 되어도 객체별 인가가 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-rest",
        "sb-soap"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "133-1-1",
          "items": [
            "REST API(REpresentational State Transfer Application Programming Interface)에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "134-4-4",
          "items": [
            "정의 및 특징",
            "SOAP 및 REST 구성요소",
            "취약점 및 대응 방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "web-performance-optimization",
      "title": "웹 성능 저하 원인과 프런트엔드 최적화",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "페이지가 느린 원인을 서버·네트워크·브라우저로 나누어 측정한 뒤, 사용자가 기다리는 경로부터 줄입니다.",
      "definition": "웹 성능 최적화는 자원 전송과 브라우저 파싱·실행·렌더링의 병목을 줄여 로딩·상호작용·시각적 안정성을 개선하는 활동입니다.",
      "principles": [
        "성능 저하는 서버 처리·DB, 왕복지연·대역폭·연결, 큰 이미지·스크립트·폰트, 렌더링 차단 CSS/JS, 과도한 DOM·레이아웃·메인스레드 작업, 캐시 부재와 외부 스크립트에서 발생합니다. 한 계층의 개선만으로 다른 병목까지 제거되지는 않습니다.",
        "①이미지를 적절한 크기·형식·압축과 반응형 소스로 제공합니다. ②번들 축소·트리셰이킹·코드 분할로 초기 JS를 줄입니다. ③defer/module 등으로 불필요한 파서 차단을 피하고 중요한 CSS를 우선합니다.",
        "④HTTP 캐시·압축·CDN으로 전송과 반복 로딩 비용을 줄입니다. ⑤화면 아래 이미지·iframe은 지연 로딩하되 핵심 이미지까지 늦추지 않습니다. ⑥DOM 작업을 모으고 긴 JS 작업을 분리하거나 Worker를 사용하여 입력 반응을 확보합니다.",
        "최적화 전후 동일한 기기·회선·부하에서 실제 사용자와 실험실 측정을 함께 비교합니다. LCP, INP, CLS 및 요청 워터폴·롱태스크를 관찰하되 하나의 점수를 서비스 품질 전체로 일반화하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "전송 병목",
            "큰 자원·왕복·캐시 부재",
            "크기 축소·캐시·CDN"
          ],
          [
            "실행/렌더링 병목",
            "긴 JS·레이아웃 반복",
            "코드 분할·DOM 최적화·Worker"
          ],
          [
            "잘못된 선행로딩",
            "모든 자원을 미리 받음",
            "핵심 경로 우선, 사용하지 않는 자원은 지연"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 모바일 상품 목록",
        "input": "원본 사진 30장과 큰 검색 스크립트를 초기 로딩합니다.",
        "steps": [
          "워터폴로 이미지 전송량과 JS 긴 작업을 확인합니다.",
          "보이는 사진은 알맞은 크기로 우선 제공하고 아래 사진은 지연합니다.",
          "상세검색 코드를 분할하고 저성능 기기에서 상호작용을 재측정합니다."
        ],
        "result": "어떤 비용을 줄였는지 원인과 지표로 설명할 수 있습니다.",
        "caution": "성능 개선 수치는 측정 전에는 제시하지 않습니다. 무분별한 캐시는 개인정보와 최신성 문제를 만들 수 있습니다."
      },
      "answer_outline": [
        "저하 원인 계층별 분류",
        "프런트엔드 6개 방안과 작동원리",
        "측정→개선→재측정 사례"
      ],
      "pitfalls": [
        "모든 이미지를 lazy-load하면 주요 콘텐츠가 더 늦어질 수 있습니다.",
        "압축만으로 JS 실행시간이 줄어드는 것은 아닙니다."
      ],
      "recall": [
        "전송시간과 실행시간을 어떻게 구분합니까?",
        "코드 분할은 어떤 초기 비용을 줄입니까?",
        "실험실 점수와 실제 사용자 지표가 다른 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-webperf"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "128-3-2",
          "items": [
            "웹 성능저하 요인",
            "프론트-엔드 관점에서의 웹 최적화 방안 6가지"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "digital-government-ui-quality",
      "title": "전자정부 UI/UX·웹 품질·KRDS",
      "domain": "디지털정부",
      "aliases": [],
      "related_terms": [],
      "easy": "공공 웹의 품질은 디자인 통일뿐 아니라 누구나 이해하고 필요한 일을 끝낼 수 있는지를 확인하는 문제입니다.",
      "definition": "디지털 정부서비스 UI/UX 가이드라인은 공공 웹·모바일 웹·앱의 공통 요소와 핵심 과업에 대한 설계·구현 기준을 제공하며 KRDS는 이를 적용할 디자인·개발 리소스를 함께 제공합니다.",
      "principles": [
        "2024 가이드의 구조는 소개와 원칙, 스타일, 컴포넌트, 기본 패턴, 서비스 패턴입니다. 작은 버튼부터 신청·검색·로그인 같은 과업 흐름까지 공통 기준을 적용하고 기관 특성에 맞춰 조합합니다. 발주 요구·설계·구현·시험·운영 개선의 각 단계에서 체크리스트로 연결합니다.",
        "적용대상은 행정·공공기관의 웹사이트·모바일 웹·앱이며 내부 업무시스템은 사용성·접근성 원칙을 목적에 맞게 조정할 수 있습니다. 특정 화면을 그대로 복제하는 것이 아니라 이용자 조사와 주요 과업의 문제를 찾아 개선합니다.",
        "접근성은 장애·고령 등 이용자의 차이에도 정보와 기능을 사용할 수 있게 하는 것이며 대체텍스트·키보드 조작·명도대비 등이 예입니다. 호환성은 다양한 브라우저·운영체제에서 동작하도록 표준과 검증을 적용하는 것입니다.",
        "개방성은 검색·수집·이용을 위한 불필요한 차단을 줄이는 것이고 최적화는 전송·렌더링·접속 환경 개선입니다. 2019판 7기준은 ①필요한 정보/기능 ②작업시간/단계 최소화 ③직관성/일관성 ④원하는 이용 방식 ⑤실수 방지 ⑥모든 유형의 이용자 ⑦서비스/정보 찾기입니다. 각각 요구조사·중복입력 제거·공통 패턴·입력/채널 선택·확인/오류 예방·접근성·명확한 탐색/검색으로 구현합니다.",
        "2025 품질관리 개정은 KWCAG2.1→2.2, 접근성 진단 24→33, UIUX 기능 중심 37→서비스 패턴 43으로 재편했습니다. 개방성의 검색로봇 완전 허용 기준은 부하·악용 방지를 위한 일부 차단을 허용하도록 완화했으므로 모든 차단을 동일하게 실패로 판정하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "접근성",
            "사람의 이용 제약을 줄임",
            "키보드·대체텍스트·자막"
          ],
          [
            "호환성",
            "기술 환경 차이를 수용",
            "표준·교차 브라우저 시험"
          ],
          [
            "개방성/최적화",
            "정보 접근 가능 / 효율적 전달",
            "검색 허용과 성능 개선을 별도 점검"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 지원금 신청 화면 개선",
        "input": "고령 이용자가 필수 정보를 놓치고 같은 내용을 반복 입력합니다.",
        "steps": [
          "이용자 관찰로 실패 단계와 어려운 용어를 찾습니다.",
          "공통 입력폼·오류·진행 표시 패턴을 적용하고 이전 입력을 재사용합니다.",
          "스크린리더·키보드·모바일과 실제 신청 완료 시나리오로 검증합니다."
        ],
        "result": "구성요소 준수와 과업 성공을 함께 평가합니다.",
        "caution": "강사 창작 개선안입니다. 2019의7기준·2024 가이드구조·2025품질진단항목은 판본과 적용목적을 구분해 사용합니다."
      },
      "answer_outline": [
        "목적·특징·구조",
        "적용대상과 단계별 활용",
        "네 가지 웹 품질 비교 및 예시"
      ],
      "pitfalls": [
        "UI 일관성과 사용자의 과업 성공을 별개로 측정합니다.",
        "웹 개방성을 개인정보까지 무제한 공개하는 의미로 쓰지 않습니다."
      ],
      "recall": [
        "컴포넌트와 서비스 패턴은 어떻게 다릅니까?",
        "접근성과 호환성의 평가 대상 차이는 무엇입니까?",
        "가이드라인은 발주와 운영에서 각각 어떻게 씁니까?"
      ],
      "source_ids": [
        "sb-krds",
        "sb-govui",
        "sb-govui2019",
        "sb-govui2025"
      ],
      "validation": "출처 확인",
      "version_note": "2019공식첨부의7기준,2024디지털정부서비스가이드의구조,2025-07-01개정안내를직접확인했습니다. 새37→43진단은 구버전7기준과 다른 분류입니다.",
      "requirements": [
        {
          "question": "133-2-2",
          "items": [
            "목적 및 주요특징",
            "가이드라인의 구조(구성요소)",
            "적용대상 및 기준",
            "가이드라인의 활용방법 2–1"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "126-3-2",
          "items": [
            "전자정부 웹사이트 UI/UX 설계기준 7가지와 웹접근성, 웹호환성, 웹개방성, 웹최적화에 대해 각각 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-quality-model",
      "title": "소프트웨어 품질과 ISO/IEC 25010 판본",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "품질모델은 좋은 소프트웨어라는 말을 측정 가능한 여러 목표로 나누어 주는 분류체계입니다.",
      "definition": "소프트웨어 품질은 명시·묵시적 필요와 사용 맥락을 만족하는 특성의 정도입니다. ISO/IEC 25010은 제품 품질의 특성과 부특성으로 요구·설계·측정·시험·인수 기준의 공통 틀을 제공합니다.",
      "principles": [
        "2011판의 제품 품질 주특성 8개는 기능적합성·성능효율성·호환성·사용성·신뢰성·보안성·유지보수성·이식성입니다. 예를 들어 기능적합성은 완전성/정확성/적절성, 성능효율성은 시간반응/자원사용/용량, 호환성은 공존성/상호운용성을 나눕니다.",
        "2011판 신뢰성은 성숙성·가용성·결함허용성·회복성, 보안성은 기밀성·무결성·부인방지·책임성·인증성, 유지보수성은 모듈성·재사용성·분석성·변경성·시험성, 이식성은 적응성·설치성·대체성을 구분하는 고전 학습 틀입니다.",
        "2023판 공식 초록은 9개 주특성 모델로의 개정을 확인시켜 줍니다. 기능적합성·성능효율성·호환성·상호작용역량·신뢰성·보안성·유지보수성·유연성·안전성으로 설명되는 최신 모델을 2011판 8특성과 혼합해서 쓰면 안 됩니다. 사용중 품질은 별도 ISO/IEC 25019와 구분해야 합니다.",
        "품질 목표는 요구별로 측정조건과 기준에 연결합니다. “신뢰성이 좋다” 대신 고장 빈도·가용시간·복구시간, 유지보수성은 변경 영향과 시험가능성을 측정합니다. 좋은 SW의 4가지 특징이라는 교재 분류는 유지보수성·신뢰성/보안·효율성·수용가능성으로 쓰이지만 유일한 국제표준 4특성은 아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "2011판",
            "제품 품질 8특성",
            "기출 당시의 구분·용어 유지"
          ],
          [
            "2023판",
            "제품 품질 9특성",
            "안전·상호작용·유연성 변경 확인"
          ],
          [
            "제품/사용중 품질",
            "제품 속성 / 사용 맥락의 결과",
            "표준 범위를 명확히 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 장애 알림 서비스의 품질 목표",
        "input": "기능 요구는 알림 전달이며 사용자는 누락과 지연을 우려합니다.",
        "steps": [
          "정확성은 대상·내용의 일치, 성능은 전달 지연, 신뢰성은 실패 시 재시도로 나눕니다.",
          "각 특성의 부특성에 시험과 측정조건을 연결합니다.",
          "보안·가용성을 동시에 높이는 설계의 비용과 절충을 검토합니다."
        ],
        "result": "품질모델을 외우는 데서 요구·시험 설계로 연결합니다.",
        "caution": "2023판 부특성 전체 목록·정식 번역은 유료 원문 미열람으로 추가 대조가 필요합니다."
      },
      "answer_outline": [
        "품질 정의와 모델의 용도",
        "2011/2023 주특성·부특성 구분",
        "측정·인수 적용과 판본 주의"
      ],
      "pitfalls": [
        "140회에 구판 8특성을 최신이라고 단정하지 않습니다.",
        "인증 획득과 모든 사용 환경에서의 품질 보장을 동일시하지 않습니다."
      ],
      "recall": [
        "2023판에서 늘어난 품질 주특성 수는 얼마입니까?",
        "제품 품질과 사용중 품질은 어떻게 다릅니까?",
        "가용성과 회복성의 차이를 예로 설명하십시오."
      ],
      "source_ids": [
        "sb-iso25010",
        "sb-swebok"
      ],
      "validation": "부분 확인",
      "version_note": "공식 초록으로 2023판·9특성은 확인했습니다. 2011/2023 세부 부특성 전체와 네 특징 교재 출전은 원문 추가 대조 필요합니다.",
      "requirements": [
        {
          "question": "140-1-5",
          "items": [
            "ISO/IEC 25010의 주특성 및 부특성"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "132-1-9",
          "items": [
            "좋은 소프트웨어가 갖추어야 할 4가지 특징"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "quality-assurance-inspection-certification",
      "title": "품질보증·인스펙션·GS 인증·품질비용",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "품질보증은 결함을 찾는 시험을 포함해 결함이 생기고 빠져나가는 과정을 관리하는 일입니다.",
      "definition": "SQA는 제품과 프로세스가 정해진 요구·표준·절차를 따르고 품질 목표를 만족하도록 계획적·체계적으로 증거를 확보하는 활동입니다. 인스펙션은 산출물을 실행하지 않고 역할과 절차에 따라 결함을 찾는 정적 검토입니다.",
      "principles": [
        "SQA는 품질계획, 표준·절차 수립, 산출물 검토, 프로세스 준수 확인, 측정·보고, 시정·예방 조치의 추적으로 구현합니다. QC가 제품의 결과를 검사하는 데 무게를 둔다면 QA는 결과를 만드는 과정의 적절성에도 책임을 둡니다.",
        "인스펙션은 대상·진입기준과 역할 선정→개요 공유→개별 준비→결함 기록/검토회의→재작업→후속 확인으로 운영할 수 있습니다. 작성자·조정자·검토자·기록자 역할을 정하고 결함의 발견과 기술적 해결 토론을 분리해 효율을 높입니다.",
        "품질비용은 예방비용(표준·교육·설계 개선), 평가비용(검토·시험·감사), 내부실패비용(출하 전 수정·재시험), 외부실패비용(운영 장애·보상·현장 수정)으로 나눕니다. 예방비용을 0으로 줄이면 전체 비용이 늘 수 있으므로 총비용과 위험으로 판단합니다.",
        "GS는 실제 운영환경과 유사한 환경의 제품 시험·평가에 기반한 국내 소프트웨어 품질인증입니다. TTA 공식 페이지는 ISO/IEC 25023·25041·25051 기반 시험을 안내합니다. 제품 인증과 조직 개발 프로세스 품질인증(SP)은 평가 대상을 구분해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "QA",
            "과정과 증거의 체계적 확보",
            "품질계획·표준·감사·개선"
          ],
          [
            "인스펙션",
            "정적 산출물 결함 발견",
            "요구·설계·코드의 조기 점검"
          ],
          [
            "GS/SP",
            "제품 품질 / 프로세스 역량",
            "인증 대상과 효력을 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 요구 누락 예방의 경제성",
        "input": "출시 후 할인 오류가 발견될 위험이 있습니다.",
        "steps": [
          "교육과 요구 체크리스트는 예방비, 리뷰·시험은 평가비로 분류합니다.",
          "출시 전 수정은 내부실패비, 출시 후 환불·장애대응은 외부실패비로 기록합니다.",
          "요구 인스펙션으로 발견한 모순을 재작업하고 해결 증거를 확인합니다."
        ],
        "result": "어떤 활동에 돈을 쓰고 어떤 실패 비용을 줄이려는지 설명할 수 있습니다.",
        "caution": "비용 절감 액수는 실제 자료 없이 창작하지 않습니다. 인증을 운영 무결점 보장으로 해석하지 않습니다."
      },
      "answer_outline": [
        "품질·SQA 목적과 기능",
        "인스펙션 역할·절차",
        "4종 품질비용·제품/프로세스 인증"
      ],
      "pitfalls": [
        "테스트만 완료했다고 모든 QA 활동이 끝난 것은 아닙니다.",
        "SP 인증의 현행 등급·세부 요건은 별도 공식 자료 확인 대상입니다."
      ],
      "recall": [
        "예방비와 평가비의 차이는 무엇입니까?",
        "인스펙션의 개별 준비가 필요한 이유는 무엇입니까?",
        "GS와 SP의 평가 대상 차이를 말하십시오."
      ],
      "source_ids": [
        "sb-inspection",
        "sb-gs",
        "sb-swebok"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "126-1-6",
          "items": [
            "소프트웨어 품질인증"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "128-1-5",
          "items": [
            "소프트웨어 개발 프로젝트의 품질비용 항목 4가지를 제시하고, 각 항목별로 사례를 들어 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "136-3-3",
          "items": [
            "소프트웨어 품질의 의미",
            "소프트웨어 품질보증의 목적과 기능",
            "인스펙션(Inspection)과 인스펙션 프로세스(Inspection Process)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-testing-principles-techniques",
      "title": "테스트 7대 원리와 기법 분류",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "시험을 많이 한다는 말보다 무엇을 어떤 근거로 골라 시험했는지가 중요합니다.",
      "definition": "소프트웨어 테스트는 결함 발견·위험 감소·요구 충족 증거 확보를 위해 산출물을 평가하는 활동입니다. 동적 테스트는 실행을, 정적 테스트는 실행 없는 검토·분석을 사용합니다.",
      "principles": [
        "7대 원리는 ①결함의 존재를 보일 수 있으나 부재를 증명하지 못함 ②전수시험은 단순 사례 외 불가능 ③조기시험은 후속 비용을 줄임 ④결함은 특정 부분에 군집 ⑤같은 시험은 새로운 결함 발견 효과가 떨어질 수 있음 ⑥시험은 맥락 의존 ⑦결함 제거만으로 사용자 목적을 만족하는 것은 아니라는 오류부재의 궤변입니다.",
        "블랙박스/명세기반 기법은 내부 구현보다 입력·출력·규칙을 근거로 동등분할·경계값·결정표·상태전이를 설계합니다. 화이트박스/구조기반은 제어·데이터 흐름을 분석해 문장·분기·조건 등 구조의 실행을 점검합니다.",
        "경험기반은 오류추정·탐색적 시험·체크리스트로 숙련자의 지식을 활용합니다. 명세에 빠진 위험을 찾을 수 있지만 사람 의존성과 재현성 관리가 필요하므로 기록과 다른 기법을 결합합니다.",
        "어떤 기법도 혼자 충분하지 않습니다. 위험이 큰 요구의 명세 테스트, 복잡 분기의 구조 커버리지, 운영 이슈를 반영한 탐색을 조합하고 결과를 요구·위험에 추적합니다. 반복 회귀시험은 새 결함 발견 효과가 줄어도 기존 기능 보호라는 가치가 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "명세기반",
            "사용자 관찰 가능한 규칙",
            "누락·잘못된 기능과 경계 오류"
          ],
          [
            "구조기반",
            "코드/설계 내부 흐름",
            "실행되지 않은 문장·분기"
          ],
          [
            "경험기반",
            "도메인 경험·휴리스틱",
            "예상 밖 상호작용과 사용 위험"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 로그인 잠금 기능 시험",
        "input": "5회 연속 실패 시 잠긴다는 요구가 있습니다.",
        "steps": [
          "실패 4·5·6회와 성공 시 초기화를 명세기반으로 시험합니다.",
          "잠금·해제·예외 분기가 실행됐는지 구조기반으로 점검합니다.",
          "시간변경·여러 탭·동시 요청을 탐색하고 재현 절차를 기록합니다."
        ],
        "result": "요구·내부 구조·현장 위험을 서로 보완합니다.",
        "caution": "계정 잠금 정책의 적정성 자체는 보안 요구와 사용 맥락에서 별도로 판단합니다."
      },
      "answer_outline": [
        "테스트 개념·7원리",
        "화이트/블랙박스 비교",
        "명세·구조·경험 기법의 조합 사례"
      ],
      "pitfalls": [
        "100% 문장 커버리지로 무결점을 주장하지 않습니다.",
        "테스트 마모는 회귀시험을 버리라는 뜻이 아닙니다."
      ],
      "recall": [
        "오류부재의 궤변을 사례로 설명하십시오.",
        "블랙박스와 화이트박스의 테스트 근거는 무엇입니까?",
        "경험기반 시험의 결과를 어떻게 재현 가능하게 합니까?"
      ],
      "source_ids": [
        "sb-ctfl"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "129-1-8",
          "items": [
            "화이트박스 테스트(White Box Test)와 블랙박스 테스트(Black Box Test)의 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "134-3-2",
          "items": [
            "소프트웨어 테스트 원리",
            "블랙박스 테스트와 화이트박스 테스트",
            "명세기반, 구조기반, 경험기반 테스트 기법"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-3-4",
          "items": [
            "가. 소프트웨어 테스트의 7대 원리",
            "나. 화이트박스 테스트와 블랙박스 테스트의 개념 및 기법 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "equivalence-boundary-classification-tests",
      "title": "동등분할·경계값·분류트리 테스트케이스",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [
        "Equivalence Partitioning",
        "Boundary Value Analysis",
        "Classification Tree"
      ],
      "easy": "같이 처리될 입력은 묶고, 처리 방식이 바뀌는 경계는 앞뒤를 함께 시험합니다.",
      "definition": "동등분할은 동일한 처리 결과가 기대되는 입력 집합을 나누어 대표값을 선정하고, 경계값 분석은 순서가 있는 분할의 경계와 인접값을 시험합니다. 분류트리는 입력 특성을 계층적으로 분류하고 유효 조합을 선택하는 기법입니다.",
      "principles": [
        "139회 학점 명세의 정수 분할은 x<0→ERROR, 0~59→F, 60~69→D, 70~79→C, 80~89→B, 90~100→A, x>100→ERROR입니다. 대표값 -1,30,65,75,85,95,101은 각 분할을 한 번씩 검증합니다.",
        "전이 경계의 바로 전/후를 포함하는 집합은 {-1,0,59,60,69,70,79,80,89,90,100,101}입니다. 더 엄격한 3값 BVA를 쓰면 각 분할 끝점 양 이웃까지 포함하므로 {-1,0,1,58,59,60,61,68,69,70,71,78,79,80,81,88,89,90,91,99,100,101}처럼 선택하고 어떤 규칙을 썼는지 밝힙니다.",
        "137회 명세는 정수 여부→정수이면 범위를 분류합니다. {비정수}, {정수<10}, {10≤정수≤100}, {정수>100} 네 분할의 대표값은 1.5→Invalid Input,9→Fail,50→Pass,101→Fail입니다. 유효 경계는 9/10과100/101이며 10·100은 Pass입니다.",
        "분류트리는 루트 입력 아래 타입(정수/비정수), 정수의 범위(10미만/10~100/100초과)를 놓고 불가능한 조합을 제외합니다. 비정수의 범위 판단은 하지 않습니다. 입력창의 문자열 파싱·공백 처리는 명세에 없으면 가정 또는 확인사항으로 구분합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "동등분할",
            "각 분할 대표값",
            "분할 누락과 유효/무효 입력 점검"
          ],
          [
            "경계값",
            "전이 주변의 인접값",
            "<와≤ 등의 경계 결함 탐지"
          ],
          [
            "분류트리",
            "입력 특성·클래스·조합",
            "불가능 조합과 조합 범위를 명시"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 137회 입력값 실행표",
        "input": "입력은 9,10,50,100,101,1.5입니다.",
        "steps": [
          "기대값을 각각 Fail,Pass,Pass,Pass,Fail,Invalid Input으로 적습니다.",
          "각 케이스가 타입·범위의 어느 클래스를 덮는지 표시합니다.",
          "실행 결과가 다르면 입력·기대·실제·버전을 결함으로 기록합니다."
        ],
        "result": "대표값과 경계 검증을 구분한 재현 가능한 테스트가 됩니다.",
        "caution": "139회는 정수형만 명시하므로 비정수의 ERROR 처리까지 공식 요구로 추가하지 않습니다."
      },
      "answer_outline": [
        "입력 조건과 분할·기대값 표",
        "139회 7분할·경계 집합",
        "137회 타입 우선 분류트리와 테스트"
      ],
      "pitfalls": [
        "60은 F가 아닌 D,90은 A입니다.",
        "3값 BVA를 적어 놓고 끝점 인접값을 빠뜨리지 않습니다."
      ],
      "recall": [
        "139회 x=59,60,100,101의 출력은 무엇입니까?",
        "137회 비정수 입력을 먼저 구분해야 하는 이유는 무엇입니까?",
        "동등분할 100%가 모든 값 시험을 뜻합니까?"
      ],
      "source_ids": [
        "sb-ctfl"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "137-2-5",
          "items": [
            "동적 테스트의 명세 기반 테스트와 구조 기반 테스트 비교",
            "아래의 [프로그램 명세]로 명세 기반 테스트 기법의 동등 분할과 분류 트리 기법의 테스트 케이스 작성 [프로그램 명세] 이 기능의 입력창은 정수로 입력되며, 입력값이 10 미만이거나 100을 초과하면 “Fail”, 10 이상이고 100 이하면 “Pass”, 정수가 아니면 “Invalid Input” 메시지를 출력한다."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-3-4",
          "items": [
            "다. 학점 처리 모듈 명세의 동등 분할과 경계값 테스트케이스 작성"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "integration-regression-monkey-testing",
      "title": "통합·회귀·몽키 테스트와 계획서",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "통합은 연결부의 계약을, 회귀는 변경이 기존 동작을 깨뜨리지 않았는지를, 몽키는 무작위 조작에서의 견고함을 살핍니다.",
      "definition": "통합 테스트는 결합된 컴포넌트·시스템의 인터페이스와 상호작용을 확인하는 시험입니다. 통합 전략은 결함 위치 파악·실행 가능한 부분 시스템·임시 대역 비용을 함께 고려해 선택합니다.",
      "principles": [
        "비점진적 Big Bang은 모든 구성요소를 한꺼번에 연결하므로 준비는 단순할 수 있으나 결함 원인 분리가 어렵고 시험 시작이 늦어집니다. 점진적 통합은 작은 묶음씩 연결해 결함 위치를 좁히고 조기 피드백을 얻습니다.",
        "하향식은 상위 제어에서 하위로 내려가며 아직 없는 하위 모듈을 Stub으로 대체합니다. 상향식은 하위 기능부터 상위로 결합하고 상위 호출자를 Driver로 대체합니다. 혼합 통합은 계층 특성과 위험에 따라 두 방향을 조합합니다.",
        "회귀 테스트는 수정·환경변경 뒤 영향받는 기존 기능이 유지되는지 확인합니다. 확인 테스트는 특정 결함이 실제 수정됐는지 재시험하는 것으로 회귀와 목적이 다릅니다. 몽키는 무작위 또는 의사무작위 이벤트로 충돌·예외·자원 문제를 찾고 seed·이벤트 수를 보관하면 재현성을 높일 수 있습니다.",
        "통합 시험계획서는 목적·범위·제외, 대상/버전·연계 목록, 전략·일정·역할, 환경·도구·대역·데이터, 테스트 기법·케이스/추적, 진입·종료 기준, 결함 처리·재시험/회귀, 위험·대응, 산출물·승인을 담아야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "하향식",
            "상위 흐름 우선, Stub 필요",
            "조기 업무 흐름 확인"
          ],
          [
            "상향식",
            "하위 기능 우선, Driver 필요",
            "기초 모듈 안정화"
          ],
          [
            "회귀/몽키",
            "기존 행동 보호 / 무작위 견고성 탐색",
            "체계적 요구 커버리지를 서로 대체하지 않음"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 주문-결제 통합",
        "input": "주문 모듈은 있고 외부 결제 샌드박스는 다음 주 준비됩니다.",
        "steps": [
          "결제 Stub으로 승인·거절·지연 응답을 정해 주문 흐름부터 시험합니다.",
          "샌드박스가 준비되면 실제 계약·타임아웃·중복 요청을 통합합니다.",
          "결제 수정 후 주문·취소 회귀시험, 무작위 UI 이벤트는 seed와 함께 별도로 수행합니다."
        ],
        "result": "부품 대역에서 실제 연계로 가며 위험을 단계적으로 확인합니다.",
        "caution": "Stub만 통과했다고 외부 결제 연계가 검증됐다고 표시하지 않습니다."
      },
      "answer_outline": [
        "통합 목적·점진/비점진 비교",
        "Top-down/Bottom-up·Stub/Driver",
        "몽키/회귀·계획서 항목"
      ],
      "pitfalls": [
        "Stub과 Driver의 호출 방향을 바꾸지 않습니다.",
        "몽키가 통과해도 업무 규칙이 맞다는 증거는 부족합니다."
      ],
      "recall": [
        "하향식 통합에서 없는 하위 모듈은 무엇으로 대체합니까?",
        "확인 테스트와 회귀 테스트는 어떻게 다릅니까?",
        "무작위 시험을 재현하려면 무엇을 남겨야 합니까?"
      ],
      "source_ids": [
        "sb-ctfl",
        "sb-monkey"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "129-4-4",
          "items": [
            "몽키 테스트(Monkey Test)와 회귀 테스트(Regression Test) 비교 설명",
            "통합 테스트 계획서에 포함되어야 할 주요 사항"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-3-3",
          "items": [
            "비점진적 통합 방식과 점진적 통합 방식",
            "하향식(Top Down) 통합 테스트와 상향식(Bottom Up) 통합 테스트",
            "테스트 드라이버(Test Driver)와 테스트 스텁(Test Stub)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "embedded-reliability-portability-testing",
      "title": "임베디드·신뢰성·이식성 테스트",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "기능이 맞아도 실제 장치의 시간·자원 제약에서 실패하거나 새 환경에서 설치되지 않으면 제품 품질은 부족합니다.",
      "definition": "임베디드 테스트는 하드웨어와 상호작용하며 제약된 환경에서 실행되는 소프트웨어를 검증합니다. 신뢰성 테스트는 정해진 조건·시간에 기능을 지속할 능력을, 이식성 테스트는 다른 환경으로 이전·설치·대체할 능력을 평가합니다.",
      "principles": [
        "임베디드는 센서·구동기·인터럽트·실시간 응답·제한 메모리/전력·통신·안전 상태를 고려합니다. 호스트 단위시험과 시뮬레이션을 거쳐 타깃 장치에서 실제 타이밍과 자원 사용, HW-SW 통합·오류 입력·복구를 확인합니다.",
        "MIL은 모델 자체, SIL은 소프트웨어 실행, PIL은 목표 프로세서, HIL은 실제 제어기와 모사된 물리환경의 연결로 추상 수준을 달리합니다. 위험과 재현성·장비 비용에 맞춰 조합하며 HIL이 실제 현장시험을 항상 대체하지는 않습니다.",
        "신뢰성의 세부 활동은 장시간 안정성/부하, 고장 주입과 결함허용, 장애·전원·통신 단절 뒤 회복, 가용성·복구시간 측정입니다. 실패의 정의·관찰시간·운영 프로파일이 없으면 고장률을 의미 있게 비교할 수 없습니다.",
        "2011 품질모델의 이식성은 적응성·설치성·대체성으로 나누어 OS/CPU/브라우저/런타임 조합, 설치·업그레이드·제거·롤백, 데이터·설정 이전과 대체품 호환을 시험합니다. 기능·성능·보안·신뢰성 등 시험 유형은 단위·통합·시스템·인수 수준에서 함께 적용될 수 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "신뢰성",
            "시간 경과와 고장·회복",
            "장시간·고장주입·복구 시험"
          ],
          [
            "이식성",
            "환경 이전·설치·대체",
            "호환 매트릭스·업그레이드/롤백"
          ],
          [
            "임베디드",
            "실제 장치 제약·물리 인터페이스",
            "SIL/PIL/HIL과 타깃 검증"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 온도 제어기 검증",
        "input": "센서 입력 10ms 주기, 통신 단절 시 안전 출력을 요구한다고 가정합니다.",
        "steps": [
          "SIL에서 경계 온도·비정상 센서값의 논리를 시험합니다.",
          "HIL/타깃에서 주기 지연·인터럽트·통신 단절을 주입하고 안전 전이를 관찰합니다.",
          "새 MCU/RTOS 전환 후 설치·자원·동일 기능과 복구를 회귀 검증합니다."
        ],
        "result": "논리 정확성과 실제 실행 환경의 제약을 함께 평가합니다.",
        "caution": "시간·안전 상태는 창작 가정입니다. 산업별 안전 인증 기준은 별도 확인해야 합니다."
      },
      "answer_outline": [
        "시험 수준·유형 분류",
        "임베디드 환경과 시험 단계",
        "신뢰성·이식성 세부 활동·증거"
      ],
      "pitfalls": [
        "PC 시뮬레이션의 성공을 타깃 타이밍 성공으로 간주하지 않습니다.",
        "이식성 용어는 2023모델 유연성과 판본을 구분합니다."
      ],
      "recall": [
        "HIL에서 실제인 부분과 모사되는 부분은 무엇입니까?",
        "가용성과 고장률의 측정에 필요한 조건은 무엇입니까?",
        "설치·롤백 시험에 어떤 데이터를 포함합니까?"
      ],
      "source_ids": [
        "sb-swebok",
        "sb-ctfl"
      ],
      "validation": "부분 확인",
      "version_note": "테스트 수준·비기능 원리는 확인했습니다. MIL/SIL/PIL/HIL의 산업별 세부 표준·구성 요건은 해당 제품 공식 문서 추가 확인 대상입니다.",
      "requirements": [
        {
          "question": "126-1-9",
          "items": [
            "임베디드 소프트웨어 테스트(Embedded Software Test)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "133-4-2",
          "items": [
            "정보시스템 개발과 운영 단계에서 수행되는 소프트웨어 테스트의 종류를 쓰고, 이 중 신뢰성 테스트와 이식성 테스트의 세부 활동에 대하여 각각 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "coverage-mutation-cyclomatic-complexity",
      "title": "커버리지·뮤테이션·순환복잡도",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "많이 실행했다는 것과 잘못된 결과를 잡았다는 것은 다릅니다. 커버리지와 변이시험을 같이 보면 그 차이가 보입니다.",
      "definition": "테스트 커버리지는 정한 시험 기준 항목 중 실행한 비율이며 코드 커버리지는 그 기준이 문장·분기·조건 같은 코드 구조인 경우입니다. 변이시험은 코드를 작은 오류로 바꾼 변이가 기존 시험에서 검출되는지 확인합니다.",
      "principles": [
        "커버리지=실행된 기준 항목 수/전체 기준 항목 수×100입니다. 요구·위험·플랫폼·데이터 분할 커버리지도 가능하므로 테스트 커버리지가 코드 커버리지보다 넓습니다. 문장100%가 분기100%를 뜻하지 않고, 분기100%도 모든 조건 조합·경로를 보장하지 않습니다.",
        "McCabe V(G)=E−N+2P이며 P는 독립 연결 성분 수입니다. 단일 연결 제어흐름에서는 단순한 이진 결정 노드 수+1과 일치하는 경우가 많으나 switch·복합논리·예외를 어떻게 CFG로 구성했는지 밝힙니다. 값은 독립 경로 기저의 크기이지 입력값 전체 수가 아닙니다.",
        "변이 연산자는 >를≥로, +를−로, 반환값·조건을 바꾸는 작은 변경입니다. 원본을 통과하던 시험이 변이에서 실패하면 kill, 살아남으면 survive입니다. 변이점수는 검출 가능한 변이 중 killed의 비율로 정의하되 동등변이·타임아웃·오류생성 변이 처리 규칙을 적습니다.",
        "복잡한 모듈은 분기 경계·예외·상태 조합을 집중 시험하고 의미 있는 assertion을 확인합니다. 커버리지는 시험 누락을 찾는 지표, 변이는 판정의 민감도를 점검하는 보조 수단이며 어느 것도 무결점 인증은 아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "코드 커버리지",
            "무엇을 실행했는가",
            "실행 누락 구조 탐지"
          ],
          [
            "변이점수",
            "작은 잘못을 시험이 잡는가",
            "assertion·입력의 약점 탐지"
          ],
          [
            "순환복잡도",
            "독립 제어경로 수",
            "시험 계획·구조 개선 우선순위 참고"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 경계 판정 변이",
        "input": "f(x)는 x>=10이면 Pass, 아니면 Fail을 반환합니다.",
        "steps": [
          "x=20만 시험하면 두 분기는 덮지 못합니다.",
          "x=9와20을 시험해 분기를 덮어도 >=를>로 바꾼 변이는 살아남을 수 있습니다.",
          "x=10의 기대값 Pass를 추가하면 해당 경계 변이를 검출합니다."
        ],
        "result": "실행 커버리지와 검출력의 차이를 구체적으로 설명합니다.",
        "caution": "동등 변이를 결함으로 계산하면 점수가 왜곡됩니다. 복잡도만으로 코드 품질을 단정하지 않습니다."
      },
      "answer_outline": [
        "테스트/코드 커버리지 비교",
        "V(G) 공식과 해석",
        "변이 생성→시험→kill/survive 및 사례"
      ],
      "pitfalls": [
        "분기100%를 경로100%라고 쓰지 않습니다.",
        "변이점수 분모의 제외 규칙을 숨기지 않습니다."
      ],
      "recall": [
        "V(G)=E−N+2P에서 P는 무엇입니까?",
        "분기 커버리지가 높아도 경계 결함이 남는 이유는 무엇입니까?",
        "동등 변이는 무엇이며 점수에 어떤 영향을 줍니까?"
      ],
      "source_ids": [
        "sb-ctfl",
        "sb-mutation",
        "sb-swebok"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "127-1-7",
          "items": [
            "테스트 커버리지(Test Coverage)와 코드 커버리지(Code Coverage)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "133-1-2",
          "items": [
            "소프트웨어 테스트 유형 중 뮤테이션 테스트(Mutation Test)에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-1-9",
          "items": [
            "맥케이브 순환복잡도(McCabe’s Cyclomatic Complexity)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "ai-metamorphic-neuron-robustness-testing",
      "title": "AI 메타모픽·뉴런 커버리지·안전 반경 테스트",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "정답 하나를 알기 어려우면 입력을 바꿨을 때 출력 사이에 성립해야 할 관계를 시험할 수 있습니다.",
      "definition": "메타모픽 테스트는 원본·후속 입력과 출력 사이의 필수 관계로 오류를 찾는 기법입니다. 뉴런 커버리지는 시험 입력이 활성화한 신경망 내부 뉴런 범위를, 안전 반경은 정한 거리 안 변화에서 예측·안전속성이 유지되는 범위를 다룹니다.",
      "principles": [
        "오라클 문제는 특정 입력의 올바른 출력을 얻거나 판정하기 어렵다는 뜻입니다. 메타모픽 관계(MR)는 예컨대 정렬 입력의 순서를 바꿔도 정렬 결과가 같아야 한다는 관계입니다. 학습 시스템은 의미를 보존하는 변환이 라벨을 보존하는지 도메인 근거를 먼저 검토해야 합니다.",
        "절차는 대상 속성·관계 정의→원본 입력 선정과 실행→변환으로 후속 입력 생성→후속 실행→출력 관계 검증→위반 원인 분석입니다. MR 위반은 결함 후보이며 관계 자체의 오류·부동소수 오차·확률적 출력도 점검합니다.",
        "뉴런 커버리지는 정해진 활성화 임계값을 넘은 뉴런 수/대상 뉴런 수로 정의할 수 있습니다. DeepXplore는 다중 모델의 차등 출력과 커버리지 목표를 결합해 입력을 찾았습니다. 뉴런 활성화가 높다는 사실은 의미 있는 동작이나 강건성의 충분조건은 아닙니다.",
        "안전 반경 관점은 입력 x 주변 ||δ||≤ε에서 허용 속성이 유지되는지 탐색·최적화·검증하는 것입니다. 반례를 찾으면 범위를 줄이거나 학습을 보완합니다. 경험적 적대적 탐색의 실패와 형식적 검증의 보장을 구분하고 거리·모델·입력 제약을 명시합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "전통 오라클 시험",
            "입력별 기대 출력과 비교",
            "정답이 있는 기능에 직접적"
          ],
          [
            "메타모픽",
            "변환 전후 필수 관계 확인",
            "정답 개별 생성 부담 완화"
          ],
          [
            "뉴런/안전반경",
            "내부 실행 범위 / 지역 강건성",
            "커버리지 지표와 보장 범위를 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 교통표지 인식의 밝기 변환",
        "input": "표지 내용과 가시성이 유지되는 약한 밝기 조절을 가정합니다.",
        "steps": [
          "원본과 변환 이미지의 클래스가 같아야 한다는 MR을 정합니다.",
          "밝기 범위를 제한하고 결과·신뢰도·활성 뉴런을 기록합니다.",
          "라벨이 달라지는 반례를 찾으면 실제 의미 변화인지 모델 결함인지 검토합니다."
        ],
        "result": "오라클 문제·관계·커버리지·강건성의 역할을 구분할 수 있습니다.",
        "caution": "과도한 어두움·가림은 의미 보존 가정이 깨지므로 무조건 같은 라벨을 요구하지 않습니다."
      },
      "answer_outline": [
        "오라클 문제와 등장 배경",
        "MR·절차·전통시험 비교",
        "뉴런 커버리지·안전반경 원리와 한계"
      ],
      "pitfalls": [
        "메타모픽 관계를 근거 없이 정하면 정상 동작을 결함으로 오인합니다.",
        "안전 반경 최대화라는 기출 용어의 특정 국내 가이드 출전은 추가 확인 필요합니다."
      ],
      "recall": [
        "정렬 함수의 MR을 하나 더 만드십시오.",
        "뉴런100%가 안전100%가 아닌 이유는 무엇입니까?",
        "반례 탐색과 형식적 지역 강건성 보장의 차이는 무엇입니까?"
      ],
      "source_ids": [
        "sb-metamorphic",
        "sb-deepxplore",
        "sb-deepsafe"
      ],
      "validation": "부분 확인",
      "version_note": "각 원 논문은 확인했습니다. 135회 안전 반경 최대화의 정확한 출전·번역과 국내 가이드 절차는 추가 대조가 필요합니다.",
      "requirements": [
        {
          "question": "140-3-2",
          "items": [
            "테스트 오라클(Test Oracle) 문제와 메타모픽 테스트의 등장 배경",
            "핵심 구성요소인 메타모픽 관계와 메타모픽 테스트 수행 절차",
            "전통적 테스트와 메타모픽 테스트 기법과의 차이점"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "135-4-5",
          "items": [
            "메타모픽 테스트(Metamorphic Test)",
            "뉴런 커버리지 테스트(Neuron Coverage Test)",
            "안전 반경 최대화 테스트"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "devops-cicd-dataops",
      "title": "DevOps·CI/CD·DataOps와 보안 자동화",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "개발과 운영 사이 전달을 자동화하고, 변경의 품질을 빨리 확인하는 협업 방식이 DevOps의 핵심입니다.",
      "definition": "DevOps는 개발·운영이 서비스 결과를 공동 책임지며 자동화·관측·피드백으로 전달을 개선하는 접근입니다. CI는 빈번한 변경 통합·검증, 지속적 전달은 배포 가능 상태 유지, 지속적 배포는 검증된 변경의 운영 자동 반영입니다.",
      "principles": [
        "파이프라인은 변경/검토→빌드·의존성 고정→단위·정적 검사→패키징·아티팩트 식별→통합·성능·보안 검증→배포 승인/자동전환→관측·롤백으로 구성할 수 있습니다. 동일 빌드 산출물을 승격하고 환경설정과 비밀을 분리해야 재현 가능합니다.",
        "장점은 빠른 피드백·작은 변경·반복 작업 감소·추적성입니다. 단점/비용은 초기 자동화 투자, 도구 복잡도, 조직 갈등, 권한·비밀 노출, 자동화된 잘못의 확산이며 플랫폼 표준과 단계적 적용으로 통제합니다.",
        "DevSecOps는 요구·위협모델·SAST·SCA·비밀 탐지·컨테이너/IaC 검사·DAST·서명/출처 검증·런타임 관측을 파이프라인에 통합합니다. 위험 임계값·예외 승인·담당자·증거를 정해 무조건 검사만 늘려 전달을 막지 않도록 합니다.",
        "DataOps는 데이터 파이프라인의 품질·흐름·협업을 관리합니다. 수집→저장/변환→시험·품질계약→제공→관측 구조에서 데이터·스키마·변환코드·계보를 버전 관리하고 지연·완전성·정확성·변경을 감시합니다. 앱 배포뿐 아니라 바뀌는 데이터의 검증과 재처리가 중요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "CI",
            "빈번한 통합과 자동 피드백",
            "깨진 기본 브랜치 즉시 복구"
          ],
          [
            "Delivery/Deployment",
            "배포 가능 / 운영 자동 반영",
            "수동 승인 여부와 제품 특성 구분"
          ],
          [
            "DataOps",
            "데이터 품질·계보·재처리",
            "DevOps 원리를 데이터 수명주기에 적용"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 정산 API와 데이터 집계 배포",
        "input": "코드 수정과 원천 스키마 변경이 함께 들어옵니다.",
        "steps": [
          "코드는 단위·통합·보안 검사를 거쳐 불변 아티팩트로 만듭니다.",
          "집계는 스키마 계약·행수·합계 대사와 데이터 계보를 검증합니다.",
          "운영 반영 후 오류율·지연·집계 품질을 관찰하고 코드·데이터 복구 절차를 수행합니다."
        ],
        "result": "코드와 데이터 변화의 서로 다른 실패 원인을 함께 통제합니다.",
        "caution": "보안 자동화 상세 분류·공급망 검증은 보안 담당 원고를 결합해야 완전한 답안이 됩니다."
      },
      "answer_outline": [
        "DevOps 개념·장단점",
        "CI/Delivery/Deployment 파이프라인",
        "DataOps 비교·아키텍처와 DevSecOps 활동"
      ],
      "pitfalls": [
        "지속적 전달과 지속적 배포를 같은 뜻으로 쓰지 않습니다.",
        "검사 통과가 위험이 없다는 인증은 아닙니다."
      ],
      "recall": [
        "배포 가능한 상태와 실제 자동배포는 어떻게 다릅니까?",
        "불변 아티팩트를 승격하는 이유는 무엇입니까?",
        "DataOps에서 코드 외에 버전 관리할 대상은 무엇입니까?"
      ],
      "source_ids": [
        "sb-dora",
        "sb-swebok"
      ],
      "validation": "부분 확인",
      "version_note": "DORA의 CI/CD 구분을 확인했습니다. DataOps 아키텍처·보안 자동화 도구의 상세 검증은 관련 담당 자료와 결합해야 합니다.",
      "requirements": [
        {
          "question": "136-1-6",
          "items": [
            "DevOps 장점과 단점"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "130-4-6",
          "items": [
            "데이터옵스와 데브옵스의 비교",
            "데이터옵스 아키텍처 및 주요 기술"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "135-2-2",
          "items": [
            "CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "136-4-6",
          "items": [
            "소프트웨어 보안 품질의 정의와 중요성",
            "보안 품질 확보를 위한 자동화 기술과 도구",
            "소프트웨어 라이프사이클 관점에서 보안 자동화 구현방안",
            "기대 효과와 시사점"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "deployment-ab-testing",
      "title": "무중단 배포·테스트 전략·A/B 실험",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "서버를 바꾸는 배포와 이용자를 나누는 실험은 목적이 다릅니다. 두 경우 모두 실패를 빨리 알아차릴 지표가 필요합니다.",
      "definition": "무중단 배포는 서비스 제공을 유지하면서 새 버전으로 전환하는 전략입니다. A/B 테스팅은 사용자를 무작위 집단에 배정해 대안의 인과적 효과를 비교하는 통제 실험입니다.",
      "principles": [
        "중단 배포는 프로세스를 멈추고 교체하므로 요청 실패·작업 손실·가용성 저하가 발생할 수 있습니다. 리버스 프록시는 백엔드 앞에서 요청을 대리하고 로드밸런서는 준비된 인스턴스에 분산하며 상태 확인·연결 드레이닝으로 전환을 돕습니다.",
        "Rolling은 일부 인스턴스씩 교체하여 자원 부담을 줄이지만 구/신 버전 공존 호환성이 필요합니다. Blue-Green은 두 환경을 준비해 트래픽을 일괄 전환하므로 복귀가 빠르나 자원 비용과 데이터 호환을 고려합니다. Canary는 일부 트래픽부터 점진 확대해 영향 범위를 제한합니다.",
        "배포 전 단위·계약·통합·성능·보안 시험, 배포 중 헬스체크·스모크·합성 트랜잭션, 배포 후 오류율·지연·업무 지표를 확인합니다. 스키마는 추가→양 버전 호환→전환→구필드 제거의 확장/축소 방식으로 계획하고 기능 플래그와 롤백을 준비합니다.",
        "A/B는 가설·분석 단위·대상·주요 지표·보호 지표·표본 크기/기간·종료 규칙을 사전에 정합니다. 사용자 단위의 안정된 무작위 배정, 집단 간 간섭·선택편향·반복 엿보기·다중비교를 통제하고 효과크기와 불확실성을 해석합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "Blue-Green",
            "두 환경 일괄 전환",
            "빠른 복귀·추가 자원"
          ],
          [
            "Rolling/Canary",
            "인스턴스 교체 / 트래픽 단계 확대",
            "호환성과 관측·중단 기준 필요"
          ],
          [
            "A/B",
            "대안의 업무 효과 실험",
            "무작위 배정·통계적 검증"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 결제 화면 변경",
        "input": "신규 UI가 전환율을 높이는지 확인하려고 합니다.",
        "steps": [
          "Canary로 작은 운영 트래픽에서 오류·지연을 먼저 확인합니다.",
          "안정성 확인 뒤 사용자별 A/B 배정과 사전 정의한 전환·환불 지표를 측정합니다.",
          "지표 악화 시 기능을 끄고 호환 버전으로 복귀합니다."
        ],
        "result": "운영 안전 검증과 효과 실험의 의사결정을 구분합니다.",
        "caution": "전환율 수치·유의성은 실제 데이터 없이는 만들지 않습니다. A/B 표본설계 세부는 통계 원고와 연결해야 합니다."
      },
      "answer_outline": [
        "중단 배포 문제·프록시/LB",
        "3종 배포 방식·검증·DB호환",
        "A/B 목적·절차·유의점"
      ],
      "pitfalls": [
        "무중단은 새 버전의 논리 오류까지 없다는 뜻이 아닙니다.",
        "Canary의 표본이 임의라면 이를 곧 A/B 인과실험으로 부르지 않습니다."
      ],
      "recall": [
        "Rolling에서 구/신 버전 공존이 왜 중요합니까?",
        "애플리케이션 롤백만으로 DB 변경을 복구할 수 있습니까?",
        "A/B의 무작위 배정과 보호 지표는 왜 필요합니까?"
      ],
      "source_ids": [
        "sb-dora",
        "sb-istio",
        "sb-ctfl"
      ],
      "validation": "부분 확인",
      "version_note": "배포·트래픽 분할 공식 자료를 확인했습니다. A/B의 통계 세부와 효과 추정은 별도 통계 근거 추가 대조가 필요합니다.",
      "requirements": [
        {
          "question": "127-2-2",
          "items": [
            "중단 배포의 문제점",
            "무중단 배포를 위한 리버스 프록시와 로드밸런싱",
            "무중단 배포 방식의 종류"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "134-3-1",
          "items": [
            "실행 중인 애플리케이션에 대한 배포 전략 및 테스트 전략에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-1-5",
          "items": [
            "소프트웨어 무중단 배포 방식"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "137-1-9",
          "items": [
            "A/B 테스팅을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "configuration-management-iac",
      "title": "형상관리·기준선·IaC",
      "domain": "소프트웨어공학",
      "aliases": [
        "Software Configuration Management",
        "소프트웨어 형상관리"
      ],
      "related_terms": [
        "IaC",
        "기준선"
      ],
      "easy": "버전관리는 파일의 이력을 저장하고 형상관리는 어떤 조합을 승인해 배포했는지까지 통제합니다.",
      "definition": "SCM은 소프트웨어 수명주기 산출물의 식별·변경 통제·상태 기록·감사와 릴리즈를 관리해 무결성과 추적성을 유지하는 활동입니다. 기준선은 공식 검토·승인되어 이후 통제된 변경의 출발점이 되는 형상입니다.",
      "principles": [
        "형상 식별에서 요구·설계·코드·시험·데이터/스키마·환경설정·빌드 스크립트 등 형상항목과 식별자를 정합니다. 형상통제에서는 변경요청→영향분석→승인→구현·시험→기준선 갱신을 수행합니다. 상태회계는 요청과 버전·승인·배포 상태를 기록하고 형상감사는 내용과 산출물 일치를 검토합니다.",
        "기능 기준선은 합의된 기능·성능 요구, 할당 기준선은 구성요소에 할당된 설계·인터페이스, 제품 기준선은 시험·인수된 구현과 릴리즈 구성을 대표하는 전형적 분류입니다. 이름과 수립 시점은 개발 수명주기·계약에 맞춰 명시합니다.",
        "Git·SVN은 소스 버전, 변경/이슈 도구는 승인과 추적, 아티팩트 저장소는 빌드 결과·의존성, CI는 재현 빌드·시험, CMDB는 운영 구성 관계를 지원합니다. Git 태그 하나가 문서·배포·환경까지 자동 통제하지는 않습니다.",
        "IaC는 인프라의 원하는 상태나 구성 절차를 코드로 기술해 검토·버전·자동 적용합니다. Terraform의 plan은 변경을 검토하고 apply가 반영하며 상태와 실제 자원 차이, 비밀 노출, 동시 실행, 드리프트를 통제해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "버전관리",
            "파일 변화·브랜치·병합",
            "형상관리의 지원 도구"
          ],
          [
            "형상관리",
            "승인된 구성·변경·증거",
            "요구부터 운영 환경까지 포함"
          ],
          [
            "IaC",
            "인프라 변경의 코드화",
            "재현·검토·자동화와 상태 보호"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 긴급 패치의 기준선",
        "input": "v1.2 운영 버전에서 결제 결함이 발견됩니다.",
        "steps": [
          "변경요청과 영향받는 요구·코드·시험을 연결해 승인합니다.",
          "패치 커밋·의존성·컨테이너 digest·IaC 버전을 함께 식별합니다.",
          "시험·감사 뒤 v1.2.1 기준선을 확정하고 실제 배포 구성을 기록합니다."
        ],
        "result": "원인을 재현하고 승인된 버전으로 복귀할 수 있는 구성을 남깁니다.",
        "caution": "긴급 변경도 사후 승인·추적·시험 증거를 생략하는 면책 절차가 아닙니다."
      },
      "answer_outline": [
        "SCM 정의·4활동·절차",
        "기준선 종류·변경 통제",
        "도구 역할·IaC 적용 예"
      ],
      "pitfalls": [
        "baseline은 변경 불가능이 아니라 통제된 변경의 기준입니다.",
        "Terraform 상태 파일에 민감정보가 있을 수 있습니다."
      ],
      "recall": [
        "형상 식별과 상태회계는 어떻게 다릅니까?",
        "Git 커밋 외에 릴리즈를 재현할 정보는 무엇입니까?",
        "IaC와 실제 자원의 드리프트는 무엇입니까?"
      ],
      "source_ids": [
        "sb-swebok",
        "sb-git",
        "sb-terraform"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "134-1-4",
          "items": [
            "형상관리의 개념과 형상관리 기준선(Baseline)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "140-4-3",
          "items": [
            "소프트웨어 형상관리 정의 및 절차",
            "소프트웨어 형상관리 기준선",
            "소프트웨어 형상관리 도구"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-1-10",
          "items": [
            "코드형 인프라스트럭처"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "safety-hazard-analysis",
      "title": "SW 안전성·FTA·FMEA·HAZOP·STPA",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "부품이 모두 정상이어도 잘못된 제어와 상호작용으로 사고가 날 수 있어 시스템 관점의 분석이 필요합니다.",
      "definition": "안전 분석은 허용할 수 없는 손실과 위험 상태를 식별하고 이를 막을 제약·설계·검증을 도출하는 활동입니다. 소프트웨어에서는 내부 결함뿐 아니라 명세·제어·인간·환경의 상호작용을 함께 검토합니다.",
      "principles": [
        "FTA는 최상위 사건(Top Event)에서 원인을 AND/OR 게이트로 내려가는 연역적 분석으로 사고 조합·최소 컷셋을 찾습니다. FMEA는 각 구성요소의 고장모드→영향→원인·검출·대책을 올라가는 귀납적 분석이며, 중요도/위험순위는 평가척도와 한계를 밝혀 사용합니다.",
        "HAZOP은 유량·압력·온도·시간 같은 매개변수에 없음·과다·부족·역전 등의 가이드워드를 적용해 설계 의도에서 벗어나는 편차와 원인·결과·보호조치를 찾는 협업 분석입니다. 정상 설계 의도와 분석 노드를 명확히 해야 합니다.",
        "전통 기법은 개별 고장·사건 연쇄에는 유용하지만 복잡한 SW·조직·인간의 비고장 상호작용이나 제어의 불충분함을 놓칠 수 있습니다. 이는 기법을 버릴 이유가 아니라 분석 모델을 보완할 이유입니다.",
        "STPA는 분석 목적(손실·위험·시스템 제약) 정의→컨트롤러·제어행동·제어대상·피드백의 제어구조 모델→안전하지 않은 제어행동(UCA)→이를 일으키는 손실 시나리오를 식별합니다. UCA는 필요한 행동 미제공, 위험한 제공, 너무 이르거나 늦음/순서 오류, 너무 오래 또는 일찍 중단으로 분석합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "FTA",
            "사고에서 원인 조합으로",
            "연역·AND/OR"
          ],
          [
            "FMEA/HAZOP",
            "고장모드 / 의도 편차",
            "귀납·체계적 검토"
          ],
          [
            "STPA",
            "안전 제어의 제약과 상호작용",
            "고장이 없는 위험도 분석"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 자동문 제어 안전성",
        "input": "사람이 통로에 있는데 문이 닫히면 충돌 손실이 발생합니다.",
        "steps": [
          "FTA는 센서 고장과 제동 실패의 조합을 검토합니다.",
          "HAZOP은 닫힘 명령이 너무 이르거나 오래 지속되는 편차를 찾습니다.",
          "STPA는 오래된 피드백으로 통로가 비었다고 믿는 제어기의 UCA와 제약을 도출합니다."
        ],
        "result": "부품 고장과 정상 부품의 잘못된 상호작용을 함께 다룹니다.",
        "caution": "안전 검증 완료나 인증 적합성을 이 예시만으로 선언하지 않습니다."
      },
      "answer_outline": [
        "안전 분석 필요성",
        "3전통기법 원리·한계 비교",
        "STPA 절차·UCA·제어구조 사례"
      ],
      "pitfalls": [
        "FTA 정상 사건을 분석 절차의 시작 정상 상태로 오해하지 않습니다.",
        "RPN만으로 모든 치명 위험의 우선순위를 정하지 않습니다."
      ],
      "recall": [
        "FTA와 FMEA의 추론 방향은 어떻게 다릅니까?",
        "STPA UCA 네 범주를 말하십시오.",
        "고장 없이 사고가 날 수 있는 예를 드십시오."
      ],
      "source_ids": [
        "sb-stpa",
        "sb-swebok"
      ],
      "validation": "부분 확인",
      "version_note": "MIT의 STPA 단계·대상은 확인했습니다. FTA/FMEA/HAZOP 규범적 절차와 위험평가 척도는 해당 산업 표준 전체 원문 추가 확인이 필요합니다.",
      "requirements": [
        {
          "question": "128-3-3",
          "items": [
            "전통적 위험분석 기법인 FMEA(Failure Mode and Effects Analysis), HAZOP(Hazard and Operability Analysis)의 특징 및 한계점",
            "STPA(System Theoretic Process Analysis) 개념 및 위험분석 방법 2–1"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-3-4",
          "items": [
            "FTA(Fault Tree Analysis)",
            "FMEA(Failure Mode and Effects Analysis)",
            "HAZOP(Hazard and Operability Analysis)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-safety-diagnosis",
      "title": "SW 안전진단의 기능동작 정확성",
      "domain": "소프트웨어공학",
      "aliases": [],
      "related_terms": [],
      "easy": "안전 기능이 있다는 문서만 보지 않고 위험 조건에서 실제로 올바른 반응을 하는지 증거로 확인해야 합니다.",
      "definition": "기능동작 정확성 진단은 안전 관련 요구가 명확하고 설계·코드·시험·실행 동작에 일관되게 반영되는지를 확인하는 안전성 검증 활동으로 설명할 수 있습니다.",
      "principles": [
        "중요한 확인 한계: 126회가 명시한 「소프트웨어 안전진단 가이드(공통분야)」 원문을 확보하지 못했습니다. 아래는 NASA·SWEBOK에 근거한 일반 안전 진단 틀이며 해당 가이드의 공식 단계명·순서로 제시하지 않습니다.",
        "준비에서는 대상 기능·운영환경·진단 경계·안전 중요도·자료·도구·판정기준을 정합니다. 요구 검토는 위험분석에서 도출된 안전 요구, 금지 동작, 안전 상태, 타이밍·오류 대응과 양방향 추적을 확인합니다.",
        "설계·코드 검토는 상태전이·제어/데이터 흐름·경계·예외·동시성·초기화·오류전파·방어 동작을 정적 분석과 인스펙션으로 점검합니다. 사용하지 않는 코드·도달 불가 상태·미정의 입력이 안전 동작을 방해하는지 살핍니다.",
        "동적 검증은 정상·경계·비정상·고장주입·실제 타이밍을 포함하고 기대 안전반응과 실제 결과를 대조합니다. 결과 분석에서 결함의 위험·원인·수정·재검증과 잔여 위험·미검증 범위를 기록하며 기준선과 진단 버전을 고정합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "요구/추적 검토",
            "무엇이 안전한 동작인가",
            "위험→안전요구→시험의 연결"
          ],
          [
            "정적 검토",
            "실행 전에 논리·구조 결함 탐지",
            "상태·예외·동시성 분석"
          ],
          [
            "동적 검증",
            "조건별 실제 반응·시간 확인",
            "고장주입·타깃·회귀 시험"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 과열 방지 제어의 진단",
        "input": "온도 임계 초과 시 히터 차단과 경보를 요구한다고 가정합니다.",
        "steps": [
          "요구에서 임계값·허용 지연·센서 단선 시 안전 상태를 확인합니다.",
          "코드의 경계 비교와 경보·차단 경로를 추적합니다.",
          "정상·임계 전후·센서 고착·재시작을 시험하고 결함을 수정·재검증합니다."
        ],
        "result": "안전 요구의 명확성에서 실행 증거까지 연결하는 연습입니다.",
        "caution": "이는 강사 창작 일반 예시입니다. 지정 가이드 단계별 절차의 답안 충족 증거로 사용하지 않습니다."
      },
      "answer_outline": [
        "지정 원문 확보 여부를 먼저 명시",
        "일반 안전 기능 진단의 입력·활동·증거",
        "미확인 공식 단계명 재대조 과제"
      ],
      "pitfalls": [
        "일반 V&V 순서를 지정 가이드의 공식 단계로 사칭하지 않습니다.",
        "미확인 항목을 충족으로 표시하지 않습니다."
      ],
      "recall": [
        "안전 상태를 요구에 명시해야 하는 이유는 무엇입니까?",
        "정적 검토와 고장주입은 어떻게 보완합니까?",
        "이 노트에서 아직 확인하지 못한 원문 범위는 무엇입니까?"
      ],
      "source_ids": [
        "sb-inspection",
        "sb-swebok"
      ],
      "validation": "확인 필요",
      "version_note": "지정된 SW 안전진단 가이드(공통분야)의 기능동작 정확성 단계명·순서·주요 활동 원문 미확보. 일반 공학 설명만 부분 제공했습니다.",
      "requirements": [
        {
          "question": "126-3-3",
          "items": [
            "최근 SW가 대부분 산업에 적용되면서 소프트웨어 안전이 중요하게 여겨지고 있다. 「소프트웨어 안전진단 가이드(공통분야)」에 따른 소프트웨어 안전성 진단 항목 중 기능동작 정확성 진단의 단계별 절차 및 주요 활동 내용을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "확인 필요"
        }
      ]
    },
    {
      "id": "project-program-portfolio-iso",
      "title": "프로젝트·프로그램·포트폴리오와 ISO 21500",
      "domain": "프로젝트관리",
      "aliases": [],
      "related_terms": [],
      "easy": "프로젝트는 결과물을 완성하고, 프로그램은 관련 프로젝트의 공동 편익을, 포트폴리오는 투자 전체의 전략 적합성을 관리합니다.",
      "definition": "프로젝트 관리는 정해진 목표를 달성하기 위해 범위·일정·비용·품질·자원·위험 등 상호 제약을 조정하는 활동입니다. ISO21500:2021은 프로젝트·프로그램·포트폴리오의 조직 맥락과 개념을, ISO21502:2020은 프로젝트 관리 실무 지침을 다룹니다.",
      "principles": [
        "프로젝트는 시작·종료가 있고 독특한 결과물/서비스를 만듭니다. 목표·성공기준·사업타당성·이해관계자를 정의하고 계획→수행→감시·통제→종료를 반복/중첩하며 범위·일정·비용 기준선의 변경을 통합 관리합니다.",
        "프로그램은 관련 프로젝트 사이 의존성·자원·변화를 조정하여 개별 관리보다 큰 편익을 얻습니다. 포트폴리오는 프로젝트/프로그램/운영 투자를 전략·위험·자원·가치에 따라 선정·균형·우선순위화하며 구성항목이 서로 기술적으로 연관될 필요는 없습니다.",
        "구 ISO21500:2012는 착수·계획·이행·통제·종료의 5프로세스그룹과 통합·이해관계자·범위·자원·일정·원가·위험·품질·조달·의사소통의 10주제그룹으로 설명되는 프로세스 모델입니다. 현재 표준의 제목·범위가 바뀌었으므로 구판 표를 그대로 현행 모델로 쓰지 않습니다.",
        "IT 사업은 기술 결과 외에 업무 정착·사용자 전환·데이터 이전·운영 인계까지 성공 기준에 넣어야 합니다. 요구가 불확실하면 증분 전달과 점검으로 계획을 갱신하되 책임·승인·품질 증거를 유지합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "프로젝트",
            "정해진 결과·범위·납기",
            "완료 및 요구 충족 관리"
          ],
          [
            "프로그램",
            "관련 프로젝트의 공동 편익",
            "의존성·조직변화·편익 실현"
          ],
          [
            "포트폴리오",
            "전략적 투자 묶음",
            "선택·중단·우선순위·균형"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 공공 서비스 현대화",
        "input": "인증 개편·포털 재구축·데이터 표준화 사업이 있습니다.",
        "steps": [
          "포털 재구축은 프로젝트로 범위와 인수기준을 통제합니다.",
          "세 사업을 통합 서비스 편익을 위한 프로그램으로 묶어 의존성을 조정합니다.",
          "기관 전체 포트폴리오에서 보안·신규서비스 투자와 우선순위를 비교합니다."
        ],
        "result": "관리에 필요한 의사결정 수준을 구분할 수 있습니다.",
        "caution": "편익과 개별 프로젝트 산출물을 동일시하지 않고 실제 성과를 확인해야 합니다."
      },
      "answer_outline": [
        "관리 개념·프로세스",
        "3관리 수준의 목표·범위·판단 비교",
        "ISO 구판/현행 범위와 IT 적용"
      ],
      "pitfalls": [
        "ISO21500이 현재도 세부 프로젝트 실무 프로세스 표준이라고 단정하지 않습니다.",
        "프로그램을 단지 큰 프로젝트라고 정의하지 않습니다."
      ],
      "recall": [
        "포트폴리오 구성은 반드시 서로 연관돼야 합니까?",
        "산출물 완성과 편익 실현은 어떻게 다릅니까?",
        "ISO21500:2021과 21502:2020의 역할은 무엇입니까?"
      ],
      "source_ids": [
        "sb-iso21500",
        "sb-iso21502"
      ],
      "validation": "부분 확인",
      "version_note": "현행 두 ISO의 공개 초록·판본을 확인했습니다. 2012판의 세부 프로세스 표 원문 전체는 미열람이므로 정확한 구성도 재대조가 필요합니다.",
      "requirements": [
        {
          "question": "135-3-1",
          "items": [
            "IT 프로젝트 관리의 개념",
            "IT 프로젝트 관리 프로세스",
            "IT 프로젝트 관리, 프로그램 관리, 포트폴리오 관리의 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "130-1-13",
          "items": [
            "ISO 21500 구성 모델"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "work-breakdown-structure",
      "title": "WBS 작성·범위·일정 만회",
      "domain": "프로젝트관리",
      "aliases": [
        "Work Breakdown Structure",
        "작업분류체계"
      ],
      "related_terms": [],
      "easy": "WBS는 해야 할 일을 산출물 중심으로 빠짐없이 나눠 책임과 예산을 연결하는 틀입니다.",
      "definition": "작업분류체계는 프로젝트 전체 범위를 관리 가능한 하위 산출물과 작업 패키지로 계층 분해한 구조입니다. 일정표 자체가 아니며 일정·비용·조직 책임을 계획할 공통 기준입니다.",
      "principles": [
        "프로젝트 목표·승인 범위·주요 산출물을 확인하고 상위 산출물→하위 구성→작업패키지로 분해합니다. 상위 범위를 하위가100% 포괄하고 형제 항목은 불필요하게 중복하지 않아야 누락·이중계상을 막습니다. 관리할 수 있을 정도까지만 분해하며 모든 가지의 깊이를 같게 만들 필요는 없습니다.",
        "각 패키지의 WBS 사전에 내용·제외·완료/인수기준·책임자·입출력·가정·추정 근거·의존성을 기록합니다. 완료를 “80% 진행” 같은 주관적 숫자가 아니라 산출물과 증거로 확인할 수 있게 합니다.",
        "WBS에서 활동을 도출하고 의존순서·자원·기간을 추정하여 일정 네트워크와 주요 경로를 계산합니다. 담당 조직과 연결한 통제계정은 범위·일정·비용 실적을 통합 관리할 수 있게 합니다. WBS 코드가 부서조직도와 같아야 하는 것은 아닙니다.",
        "지연 시 우선 원인·주요 경로·잔여 여유를 분석합니다. Fast Tracking은 순차 작업 중첩으로 재작업 위험을, Crashing은 자원 추가로 비용을 늘릴 수 있습니다. 범위 조정·대체기술·우선순위 재조정도 승인된 기준선 변경으로 평가합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "WBS",
            "범위·산출물 계층",
            "무엇을 완성할지 정의"
          ],
          [
            "일정 네트워크",
            "활동 선후행·기간",
            "언제 끝날지 계산"
          ],
          [
            "일정 만회",
            "중첩·자원추가·범위조정",
            "주요 경로와 재작업 위험 평가"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 데이터 이전 지연 만회",
        "input": "이관 패키지가2주 늦고 병행 검증에 의존성이 있습니다.",
        "steps": [
          "WBS 사전에서 누락된 정합성 검증 책임을 확인합니다.",
          "정제와 모의 이관의 안전한 일부 중첩을 검토하고 추가 인력의 분할 가능성을 평가합니다.",
          "재작업 위험·비용·인수기준을 검토해 만회안을 승인합니다."
        ],
        "result": "막연한 야근 대신 범위·의존·자원에 근거한 계획을 만듭니다.",
        "caution": "인력 추가가 항상 기간을 선형으로 줄이지 않으며 검증 생략은 만회대책이 아닙니다."
      },
      "answer_outline": [
        "정의·작성원칙·절차",
        "WBS 사전과 범위/일정/비용 연결",
        "지연 원인·주요경로·만회 사례"
      ],
      "pitfalls": [
        "WBS를 단순 날짜 목록으로 만들지 않습니다.",
        "누락 범위를 숨겨100%규칙을 형식적으로 맞추지 않습니다."
      ],
      "recall": [
        "100%규칙은 무엇을 의미합니까?",
        "WBS와 일정표의 차이를 설명하십시오.",
        "Crashing을 적용해도 종료일이 안 줄 수 있는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-wbs"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "128-1-1",
          "items": [
            "WBS(Work Breakdown Structure)에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-3-2",
          "items": [
            "WBS 작성 원칙",
            "WBS 작성 장점",
            "WBS 작성 고려사항",
            "일정지연 시 만회대책 및 사례"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-1-1",
          "items": [
            "WBS(Work Breakdown Structure) 작성방법"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "project-risk-management",
      "title": "프로젝트 위험관리·대응·ISO 31000",
      "domain": "프로젝트관리",
      "aliases": [],
      "related_terms": [],
      "easy": "위험은 이미 발생한 문제와 다릅니다. 아직 불확실한 사건이 목표에 주는 영향을 미리 관리합니다.",
      "definition": "위험관리는 목표에 대한 불확실성의 영향을 식별·분석·평가·처리·감시·소통하는 활동입니다. ISO31000은 이를 조직 의사결정·거버넌스와 통합하는 원칙·프레임워크·프로세스 지침입니다.",
      "principles": [
        "관리계획에서 위험 범주·확률/영향 척도·허용기준·소유자·보고주기를 정합니다. 워크숍·과거사례·가정/의존성 분석으로 원인→사건→결과 형태의 위험을 식별하고 등록부에 기록합니다. 발생한 이슈는 별도 조치와 변경을 관리합니다.",
        "정성 분석은 확률·영향·긴급성 등으로 우선순위를 정하고, 필요하면 기대금액·민감도·시뮬레이션으로 일정·비용 범위를 분석합니다. 숫자는 자료·분포·가정을 밝혀야 하며 위험 점수는 객관적 확률 그 자체가 아닙니다.",
        "위협은 회피(원인/노출 제거), 전가(보험·계약으로 부담 이전), 완화(가능성/영향 감소), 수용(능동적 예비·대기), 상위 이관으로 대응할 수 있습니다. 기회는 활용·증대·공유·수용·상위 이관을 상황에 맞게 씁니다.",
        "대응안마다 소유자·기한·트리거·조치비·비상/대체계획·잔여/2차 위험을 기록합니다. 실행 후 효과를 점검하고 신규 위험을 갱신합니다. ISO31000의 가치창출·보호 목적 아래 통합·체계적/포괄적·맞춤형·포용적·역동적·최선 정보·인간/문화·지속 개선의 8원칙을 반영합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "위협 회피/완화",
            "원인 제거 / 노출 감소",
            "회피와 위험이 일부 남는 완화를 구분"
          ],
          [
            "전가/공유",
            "위협 부담 이전 / 기회 공동 확보",
            "계약으로 모든 책임이 사라지지 않음"
          ],
          [
            "수용",
            "불확실성을 인지해 잔여 위험 유지",
            "트리거·예비·승인 필요"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 외부 API 제공 지연 위험",
        "input": "연계기관 API가 준비되지 않으면 통합시험이 늦습니다.",
        "steps": [
          "담당자·준비일·트리거를 위험등록부에 적습니다.",
          "Stub 선행검증과 대체 일정으로 영향을 완화하고 계약상 협조를 합의합니다.",
          "트리거가 발생하면 비상계획을 수행하고 잔여 연계 위험을 보고합니다."
        ],
        "result": "위험·대응·실행 증거가 연결됩니다.",
        "caution": "미확인 확률이나 손실 금액을 만들어 정량분석을 장식하지 않습니다."
      },
      "answer_outline": [
        "위험/이슈·ISO 지침 정의",
        "식별→분석→평가→대응→감시",
        "위협/기회 전략·등록부·예시"
      ],
      "pitfalls": [
        "리스크 대응을 전부 완화라고 부르지 않습니다.",
        "ISO31000을 인증 요구사항 표준으로 설명하지 않습니다."
      ],
      "recall": [
        "잔여 위험과2차 위험은 어떻게 다릅니까?",
        "전가와 회피를 구분해 보십시오.",
        "기회의 활용과 증대는 어떤 차이가 있습니까?"
      ],
      "source_ids": [
        "sb-risk",
        "sb-pmi-risk",
        "sb-riskpreview"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "132-1-1",
          "items": [
            "ISO 31000"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "134-4-1",
          "items": [
            "리스크 대응 계획 수립 절차",
            "위협에 대한 대응 전략",
            "기회에 대한 대응 전략"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "138-1-2",
          "items": [
            "프로젝트 위험관리"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "139-1-4",
          "items": [
            "IT 프로젝트에서 발생할 수 있는 부정적 위험(Negative Risk)과 대응 전략"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "project-conflict-team-development",
      "title": "PM의 갈등관리와 Tuckman 팀 발달",
      "domain": "프로젝트관리",
      "aliases": [],
      "related_terms": [],
      "easy": "갈등의 종류와 시급성을 보고 해결 방식을 고르며 팀의 단계에 맞게 규칙과 신뢰를 쌓아야 합니다.",
      "definition": "갈등은 이해관계자의 목표·가치·정보·역할·자원·의존성이 충돌하는 상태입니다. 관리 목적은 갈등을 무조건 없애는 것이 아니라 과업상의 이견을 좋은 결정으로 연결하고 관계 손상을 줄이는 것입니다.",
      "principles": [
        "과업 갈등은 대안·위험을 드러내 의사결정에 도움이 될 수 있지만 관계 갈등·차별·공격은 협력과 안전을 해칩니다. 적정 갈등과 성과의 관계를 역U자 개념도로 설명할 수 있어도 모든 조직에 적용되는 실증 법칙·임계값으로 단정하지 않습니다.",
        "주요 원인은 일정 우선순위·부족 자원·역할 모호성·기술 대안·보상·의사소통·문화 차이입니다. 사실과 해석을 분리하고 이해관계·권한·제약을 확인한 뒤 당사자와 해결 기준·실행·재확인을 합의합니다.",
        "협업/문제해결은 공동 원인을 해결하고, 타협은 각자 일부 양보합니다. 완화/수용은 관계와 공통점을 우선하고, 강제/지시는 긴급 의사결정에 유용할 수 있으나 수용성이 약해질 수 있습니다. 회피/철수는 냉각과 준비에 쓰되 문제를 방치하지 않습니다.",
        "Tuckman의 형성(Forming)은 목적·역할 탐색, 혼란(Storming)은 권한·방법 충돌, 규범(Norming)은 신뢰·규칙 합의, 수행(Performing)은 자율 협력, 종료(Adjourning)는 인수·회고·해산입니다. 구성원 변화로 이전 단계로 돌아갈 수 있으며 반드시 선형으로 한 번만 통과하지는 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "협업",
            "원인과 상호 이익 탐색",
            "시간·정보와 신뢰 필요"
          ],
          [
            "타협/강제",
            "부분 양보 / 권한 결정",
            "납기·긴급성·위험을 고려"
          ],
          [
            "팀 발달",
            "역할 탐색→갈등→규범→수행→종료",
            "상황별 지원·위임·회고"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 개발·운영의 배포 갈등",
        "input": "개발은 빠른 출시, 운영은 장애 감소를 우선합니다.",
        "steps": [
          "서로의 목표와 실제 실패 데이터를 확인합니다.",
          "완료의 정의·자동시험·중단 기준·당직 책임을 공동 규칙으로 정합니다.",
          "작은 배포에서 결과를 검토하고 팀의 자율 범위를 넓힙니다."
        ],
        "result": "가치 충돌을 공동 서비스 지표와 실행 규칙으로 전환합니다.",
        "caution": "공격적 행동을 건설적 갈등이라는 이름으로 정당화하지 않습니다."
      },
      "answer_outline": [
        "갈등과 성과의 관계",
        "요인·해결전략·PM 절차",
        "팀 발달5단계와 적용"
      ],
      "pitfalls": [
        "강제와 회피도 맥락 없이 언제나 나쁘다고 단정하지 않습니다.",
        "Tuckman 모형은 모든 팀의 경로를 보장하지 않습니다."
      ],
      "recall": [
        "과업 갈등과 관계 갈등은 어떻게 다릅니까?",
        "타협과 협업의 결과 차이는 무엇입니까?",
        "Storming에서 PM이 해야 할 일은 무엇입니까?"
      ],
      "source_ids": [
        "sb-tuckman",
        "sb-iso21502"
      ],
      "validation": "부분 확인",
      "version_note": "PMI 공개 자료에서5단계는 확인했습니다. 갈등 해결전략의 명칭은 프레임워크별로 다를 수 있어 적용 의도와 함께 설명했습니다.",
      "requirements": [
        {
          "question": "134-1-1",
          "items": [
            "터크만 사다리 모델(Tuckman Ladder Model)의 팀 발달 단계별 특징"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "136-3-1",
          "items": [
            "갈등과 프로젝트 성과의 관계",
            "갈등의 요인과 해결 전략",
            "터크만(Tuckman)의 팀 발달 5단계 모델"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "pmo-pmc-information-system-audit",
      "title": "감리·상주감리·PMO·PMC 비교",
      "domain": "프로젝트관리",
      "aliases": [],
      "related_terms": [],
      "easy": "사업을 잘 진행하도록 돕는 역할과 독립적으로 점검하는 역할의 책임과 이해관계를 구분해야 합니다.",
      "definition": "정보시스템 감리는 발주자·사업자의 이해관계에서 독립된 제3자가 구축·운영을 종합 점검하여 문제 개선을 유도하는 활동입니다. PMO는 사업관리 체계와 실행을 지원하며 PMC는 계약에 정한 범위의 프로젝트 관리 자문·관리 서비스를 뜻합니다.",
      "principles": [
        "국내 공공 감리는 전자정부법 제57조, 공공 PMO인 전자정부사업관리 위탁은 제64조의2와 시행령·관련 고시에 근거를 둡니다. PMO는 계획·범위·일정·위험·품질·조달·성과·이해관계자 조정과 의사결정을 지원하나 발주자의 법적 승인·책임을 자동 대체하지 않습니다.",
        "현장감리는 사전자료·계획과 착수회의 후 산출물 검토·관계자 면담·실증/시험·점검 결과 검토를 수행하고 종료회의·보고·조치결과 확인으로 이어집니다. 129회 지정2021-4호의 정확한 작업명은 해당 판본과 대조해야 합니다.",
        "상주감리는 사업 현장에 지속 투입되어 위험과 문제를 조기에 확인하는 감리 형태입니다. 지속 참여한다는 공통점이 있어도 관리 실행을 지원하는 PMO와 독립 평가·개선 권고라는 목적이 다릅니다. 서로의 과업·승인·보고·이해상충을 분리합니다.",
        "PMO는 조직 내부의 상설 기능·여러 사업의 표준화까지 포함할 수 있고, PMC는 특정 사업에 제공되는 외부 전문서비스의 계약 용례가 많습니다. 그러나 용어 정의는 산업·발주 조건마다 달라 일반적 비교를 법정 고정 정의처럼 쓰지 않습니다. PMO 대상 사업 금액·예외 범위는 현행 시행령을 별도 확인해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "감리",
            "독립 점검·평가·개선 권고",
            "특정 단계 또는 상주 형태"
          ],
          [
            "PMO",
            "발주자 관리역량 보완·관리 지원",
            "사업 전 과정·표준·위험·의사결정"
          ],
          [
            "PMC",
            "계약 기반 전문 관리/자문",
            "범위·책임·기간을 계약에서 확정"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 차세대 시스템 오픈 관리",
        "input": "발주기관에 기술·일정 관리 인력이 부족합니다.",
        "steps": [
          "PMO가 요구·일정·위험·개통 기준을 통합 관리하도록 지원 범위를 정합니다.",
          "감리는 요구·설계·종료 단계의 독립 점검과 조치 확인을 수행합니다.",
          "상주감리와 PMO의 회의·산출물·승인권·보고 관계 중복을 정리합니다."
        ],
        "result": "발주기관 의사결정, 관리 지원, 독립 검증의 책임을 구분합니다.",
        "caution": "위탁했다고 발주자의 감독·인수 책임이 없어지지 않습니다."
      },
      "answer_outline": [
        "법적 근거와 정의",
        "현장감리 활동·PMO/상주감리 비교",
        "PMC 용례·과업·책임 분리"
      ],
      "pitfalls": [
        "PMO가 사업자 역할을 수행하고 자기 결과를 감리하는 구조는 독립성 문제가 있습니다.",
        "모든 금액의 사업에 공공 PMO가 의무라고 단정하지 않습니다."
      ],
      "recall": [
        "감리와 PMO의 목적 차이는 무엇입니까?",
        "상주감리도 독립성을 지켜야 하는 이유는 무엇입니까?",
        "PMC의 책임을 판단할 우선 문서는 무엇입니까?"
      ],
      "source_ids": [
        "sb-auditbase",
        "sb-egovlaw",
        "sb-audit2023"
      ],
      "validation": "부분 확인",
      "version_note": "2024 감리기준 공지·2026 시행령 감리 조문 확인. 2021-4호 현장감리 작업명, PMO 대상 범위/예외, PMC 특정 정의는 추가 원문 대조가 필요합니다.",
      "requirements": [
        {
          "question": "129-1-4",
          "items": [
            "정보시스템 감리기준 고시(2021-4호, 2021.1.19)에 의거한 현장감리의 활동, 작업 내용을 기술하고 PMO(Project Management Office)와의 차이점을 설명"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "131-1-6",
          "items": [
            "정보시스템 감리와 PMO(Project Management Office) 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "136-2-2",
          "items": [
            "정보시스템 감리의 법적 근거",
            "PMO의 정의와 역할",
            "PMO 대상 사업의 범위",
            "PMO와 상주감리의 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "140-1-4",
          "items": [
            "PMC(Project Management Consultancy)와 PMO(Project Management Office) 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "big-data-system-audit",
      "title": "빅데이터 사업 분석·설계 감리",
      "domain": "감리",
      "aliases": [],
      "related_terms": [],
      "easy": "분석 단계의 합의가 설계의 수집·저장·분석·시각화와 실제 확보 가능한 데이터로 이어졌는지 확인합니다.",
      "definition": "NIA2023 지능정보기술 감리 실무가이드는 빅데이터 정보화사업의 단계·영역별 요구·설계·구현·운영 위험과 점검 항목을 제시합니다. 분석단계와 데이터 분석 알고리즘 수행 단계는 다른 분류입니다.",
      "principles": [
        "분석단계 응용시스템 영역은 사업목표·구현방안 이해, 목표 달성을 위한 분석항목과 상관관계·결과품질, 분석가/사용자 인터페이스, 시각화 유형·도구, 운영·관리 기능, 기능·성능·품질 요구 도출을 점검합니다.",
        "분석단계 데이터 영역은 목적에 맞는 종류·양·보관·수집/분석 주기와 백업 요구, 원시데이터 확보 가능성을 확인합니다. 내·외부 데이터를 활용한 서비스와 운영 환경·연계 요건도 검토하여 나중에 데이터가 없거나 권한이 없어 구축이 막히는 위험을 줄입니다.",
        "설계단계 응용은 수집대상·정제기준·개인정보 처리, ETL·주기적 연계와 품질관리, 요구에 맞는 분석대상·범위·모델·알고리즘과 타당성, 화면·시각화·서비스 기능을 점검합니다.",
        "설계단계 데이터는 속성·형식·길이·필수여부·명명/용어/도메인·코드 표준, 유형·변환·유효성 규칙·융합을 확인합니다. 시스템 구조는 수집·저장·분석·시각화 아키텍처와 외부연계·접근제어·보안의 상세설계가 요구와 연결되는지 검토합니다. 자료의 버전과 실제 산출물·실증 증거를 함께 기록합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "분석",
            "목표·사용·데이터 요구와 확보",
            "요구의 적정성·실현성"
          ],
          [
            "설계-응용/데이터",
            "처리·모델·시각화·표준화",
            "요구와 상세 설계의 일치"
          ],
          [
            "설계-시스템",
            "아키텍처·연계·보안",
            "수집부터 활용까지 실행 가능성"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 민원 수요 분석 사업 감리",
        "input": "목표는 지역별 수요 예측이나 외부 데이터 이용권이 미정입니다.",
        "steps": [
          "분석에서 데이터 보유기관·비용·제공주기·이용 근거를 확인합니다.",
          "설계에서 지역코드 변환·결측처리·모델·시각화 요구를 추적합니다.",
          "샘플 수집과 변환·모델 입력을 실증해 누락과 불일치를 기록합니다."
        ],
        "result": "알고리즘 이름만 있는 사업의 실현 위험을 조기에 드러냅니다.",
        "caution": "가이드의 “자료에 명시”와 해당 데이터·모델의 실제 타당성 검증을 구분합니다."
      },
      "answer_outline": [
        "가이드 목적·영역·감리 단계",
        "분석단계 응용/데이터 점검",
        "설계단계 시스템/응용/데이터와 증거"
      ],
      "pitfalls": [
        "분석단계를 모델 학습 단계만으로 축소하지 않습니다.",
        "품질 기준이 있다는 서류만 보고 실제 품질 충족으로 표시하지 않습니다."
      ],
      "recall": [
        "데이터 확보 가능성은 왜 분석에서 확인합니까?",
        "설계의 ETL 감리에서 어떤 기준을 찾습니까?",
        "응용과 데이터 영역의 점검 차이는 무엇입니까?"
      ],
      "source_ids": [
        "sb-audit2023"
      ],
      "validation": "출처 확인",
      "version_note": "NIA 「지능정보기술 감리 실무가이드(2023.2)」 빅데이터 장 p.11~35 기준으로 자체 요약했습니다.",
      "requirements": [
        {
          "question": "130-3-5",
          "items": [
            "인공지능 등 지능정보 기술에 비현실적인 감리기준을 해결하기 위해 지능정보기술 감리 실무 가이드(한국지능정보사회진흥원, 2023년)를 발간했다. 그 중 빅데이터 정보화 사업의 분석·설계 단계별, 영역별 점검 항목에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "cloud-migration-audit",
      "title": "클라우드 전환 사업의 단계별 감리",
      "domain": "감리",
      "aliases": [],
      "related_terms": [],
      "easy": "클라우드 자원을 만들었는지보다 업무와 데이터를 안전하게 옮기고 운영할 수 있는지 단계별로 검증합니다.",
      "definition": "클라우드 전환 감리는 전환 목표·대상 선정에서 설계·이행·시험·운영 인수까지 요구와 위험·통제를 독립적으로 점검하는 활동입니다. 전환 방식과 서비스 모델에 따라 점검 범위를 조정합니다.",
      "principles": [
        "계획/분석에서는 업무 중요도·데이터 분류·현행 자산/의존성·라이선스·비용·제약을 파악하고 공공/민간·IaaS/PaaS/SaaS·전환 방식·우선순위·중단 허용·출구전략의 타당성을 검토합니다. 가상서버 이전만으로 클라우드 네이티브 목표가 충족되지는 않습니다.",
        "설계에서는 자원·망·계정/권한·암호키·모니터링·백업·가용성·재해복구·SLA·책임분담, 앱의 상태·확장·연계·데이터 이전 구조를 확인합니다. 규정상 보안성 검토·인증·데이터 위치 요건은 적용대상과 현행 기준을 별도 대조합니다.",
        "구축/전환에서는 IaC·설정·접근권한·이미지·보안구성, 단계별 데이터 이관·정합성·재처리, 구/신 시스템 연계와 전환순서·롤백 계획이 설계대로 구현되었는지 실증합니다. 원본과 이관 증거를 보존합니다.",
        "시험/종료에서는 기능·성능·부하·확장·장애·복구·보안 시험과 사용자 인수, 운영 매뉴얼·교육·자산/권한 인계, 지표·비용·SLA 보고·공급자 지원·종료 시 데이터 반환/삭제를 확인합니다. 감리 지적의 조치 결과를 다시 확인하고 미해결 위험의 승인 주체를 기록합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "분석",
            "전환 대상·제약·목표·계획",
            "업무·데이터·의존성 누락 점검"
          ],
          [
            "설계/이행",
            "목표 구조·변경·이관 통제",
            "책임분담·일관성·롤백"
          ],
          [
            "검증/운영인수",
            "실제 서비스와 복구 능력",
            "시험·운영 증거와 잔여 위험"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 신청 포털 클라우드 이전",
        "input": "첨부파일 서버와 인증 서버가 외부 연계에 의존합니다.",
        "steps": [
          "현행 의존성과 중단 허용시간을 분석합니다.",
          "첨부 저장·세션·인증 경로와 백업 복구를 설계·검토합니다.",
          "모의 이관·부하·장애·복구 시험을 거쳐 운영 인계의 누락을 확인합니다."
        ],
        "result": "인프라 구성 완료와 업무 서비스 전환 완료를 구분합니다.",
        "caution": "가용률·인증 필요 여부는 문항 시점과 실제 법령·계약 조건으로 확인해야 합니다."
      },
      "answer_outline": [
        "전환 유형·감리 범위",
        "분석→설계→구축/이행→시험/종료",
        "단계별 산출물·실증·시정조치"
      ],
      "pitfalls": [
        "CSP가 맡는 보안과 고객이 맡는 앱/데이터 보안을 구분합니다.",
        "운영비 감소를 측정 없이 성과로 주장하지 않습니다."
      ],
      "recall": [
        "전환 전 의존성 조사에서 빠지기 쉬운 것은 무엇입니까?",
        "전환 후 복구시험이 필요한 이유는 무엇입니까?",
        "데이터 종료전략에서 확인할 두 가지는 무엇입니까?"
      ],
      "source_ids": [
        "sb-audit2023"
      ],
      "validation": "출처 확인",
      "version_note": "NIA2023 클라우드 정보화사업 감리 장에 근거한 단계별 재구성입니다. 현행 공공 클라우드 보안 규정의 세부 수치·인증 절차는 별도 최신 확인 대상입니다.",
      "requirements": [
        {
          "question": "134-4-5",
          "items": [
            "클라우드 전환 사업의 단계별 감리 방법과 검토 항목에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "operations-maintenance-audit",
      "title": "시스템 운영·유지보수 감리",
      "domain": "감리",
      "aliases": [],
      "related_terms": [],
      "easy": "운영 감리는 서비스의 지속 수행을, 유지보수 감리는 변경과 복구를 포함한 유지관리의 적절성을 점검합니다.",
      "definition": "NIA2023 가이드는 운영과 유지관리 대상을 개발SW·상용SW·인프라로 구분하고 사업 유형에 맞는 절차·계획·수행·기록의 적정성을 평가합니다.",
      "principles": [
        "운영 감리에서 개발SW는 릴리스/배포(운영반영)·테스트 지원·장애관리입니다. 인프라는 신규/변경 서비스 지원·서비스수준·보고·연속성/가용성·용량·정보보안·비즈니스 관계·공급자·인시던트/요청·문제·구성·변경/릴리스·운영상태를 점검합니다. 각 절차·계획과 실제 이행 기록을 대조합니다.",
        "유지보수의 개발SW 분야는 응용 모니터링·응용 장애처리·사용자 지원·성능·정기/비정기 점검·시스템 테스트 지원·장애관리·유지보수 계획·표준/절차·요구사항·CSR 이행·구성·릴리스/배포(운영이관)입니다. 접수부터 변경 분석·시험·승인·반영까지 추적하여 변경 누락/무승인 반영을 확인합니다.",
        "상용SW 유지보수는 계획·표준/절차·업그레이드/패치·이전/재설치·일상 지원·긴급/장애처리·예방점검·운영자/사용자 교육·보안 정책/계획·보안점검/예방·보안조치/기술지원입니다. 인프라는 OS 업그레이드/패치·HW 업그레이드·예방점검·긴급/장애·자원 할당/회수·교육·기술이전·부품지원·운영상태·이전/재설치입니다.",
        "증거는 계약/SLA·자산/구성 목록·지원범위·계획/절차·작업/장애/변경 로그·복구 결과·보안/권한·성능/용량 보고·사용자 요청과 완료 승인입니다. 2023 가이드 개요와 상세의 분야/항목 수·코드가 일부 달라 단순 총계는 확정하지 않고 상세 분야명과 실제 사업의 대상/과업에 따라 테일러링합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "운영-개발SW",
            "릴리스·시험지원·장애관리",
            "일상 서비스와 운영 반영"
          ],
          [
            "유지관리-개발/상용SW",
            "CSR·수정·패치·지원·품질",
            "계약 범위와 변경 통제"
          ],
          [
            "운영/유지관리-인프라",
            "상태·점검·장애·자원·기술이전",
            "실행 기록·복구 증거 검토"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 장애 처리와 유지보수 분리",
        "input": "야간 장애를 임시 우회하고 다음 날 코드를 수정합니다.",
        "steps": [
          "운영 기록에서 접수·영향·우회·복구시간·보고를 확인합니다.",
          "유지보수 기록에서 원인·수정·시험·승인·배포와 요구/형상 추적을 확인합니다.",
          "재발방지 조치와 실제 복구시험 결과를 대조합니다."
        ],
        "result": "빠른 임시복구와 안전한 영구수정의 관리 증거를 구분합니다.",
        "caution": "가이드 전체 점검표를 여기의 예시 분야만으로 완전 복제했다고 주장하지 않습니다."
      },
      "answer_outline": [
        "운영/유지보수 정의·대상",
        "사업유형별 점검분야",
        "절차·실제 이행·증거·시정 확인"
      ],
      "pitfalls": [
        "상용SW 유지관리를 자체 소스 수정과 동일시하지 않습니다.",
        "백업 성공 로그만으로 복구 가능하다고 확정하지 않습니다."
      ],
      "recall": [
        "운영과 유지보수의 장애 활동은 어떻게 다릅니까?",
        "상용SW 유지관리에서 라이선스를 점검하는 이유는 무엇입니까?",
        "절차가 실제 이행됐는지 확인할 증거를 세 가지 말하십시오."
      ],
      "source_ids": [
        "sb-audit2023"
      ],
      "validation": "부분 확인",
      "version_note": "NIA2023공개PDF p.152~153·186~187의운영/유지보수상세분야를대조했습니다. 개요표와본문의항목집계·코드불일치로총개수는확정하지않았습니다.",
      "requirements": [
        {
          "question": "137-3-2",
          "items": [
            "시스템 운영, 유지보수 감리의 개념",
            "시스템 운영 감리의 점검분야",
            "유지보수 감리의 점검분야"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "go-live-readiness",
      "title": "대규모 공공시스템 개통 준비도",
      "domain": "프로젝트관리",
      "aliases": [],
      "related_terms": [],
      "easy": "납기일이 왔다는 사실과 개통 준비가 끝났다는 판단을 분리해야 합니다.",
      "definition": "개통 준비도는 서비스 전환에 필요한 기능·데이터·성능·연계·보안·운영·사용자 준비와 잔여 위험이 합의된 기준을 만족하는지를 증거로 판단하는 상태입니다.",
      "principles": [
        "대규모 사업 실패 원인은 불명확/잦은 요구변경, 업무/연계 복잡도 과소추정, 비현실적 예산·기간, 부족한 사용자 참여, 시험 환경·데이터의 비대표성, 데이터 이관 오류, 책임 분산, 단계적 검증 부족 등으로 분석할 수 있습니다. 특정 실제 사업의 원인은 공식 조사 없이 단정하지 않습니다.",
        "예방은 사업계획·요구·과업변경과 적정기간 심의, 이해관계자·의존성 통합관리, 단계별 인수기준, 독립 감리와 PMO 역할, 사용자 실무자 참여, 모의 이관·업무 리허설·부하/장애 시험, 전환·롤백·비상운영 체계로 구체화합니다.",
        "지표는 중요 요구 구현/시험 완료, 치명·중대 결함 잔여, 핵심 업무 성공률, 데이터 건수/금액 대사, 목표부하 p95·오류율, 연계기관 시험 완료, RTO/RPO 검증, 운영인력 교육·매뉴얼·당직·헬프데스크 준비를 포함합니다. 지표의 분모와 중요도를 명시해 단순 평균이 치명 결함을 가리지 않게 합니다.",
        "Go/No-Go 회의에서 기준별 증거·미충족·우회방안·잔여 위험·승인 책임을 보고합니다. 미충족 핵심 기능은 범위 조정·단계 개통·일정 재승인으로 해결하고 성과를 가리기 위한 임의 기준 완화는 피합니다. 법제도 개선은 현실적인 대가·기간·변경·책임·전문평가와 운영 감리의 실효성 관점에서 제안합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "진척률",
            "얼마나 만들었는가",
            "개통 가능성의 일부 정보"
          ],
          [
            "준비도",
            "운영할 증거가 충분한가",
            "중요 위험·이관·복구·사용자 포함"
          ],
          [
            "Go/No-Go",
            "기준·증거·잔여 위험의 승인",
            "판단 주체와 책임 명확화"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 복지급여 시스템 전환",
        "input": "기능95% 완료이나 지급액 대사와 외부기관 연계가 미완료입니다.",
        "steps": [
          "전체 평균보다 지급 정확성과 핵심 연계의 실패를 우선 보고합니다.",
          "모의 지급·데이터 대사·비상처리와 롤백을 검증합니다.",
          "미충족 시 단계 개통이나 일정 변경을 승인받습니다."
        ],
        "result": "숫자상 진척과 공공 서비스 위험을 구별한 의사결정이 됩니다.",
        "caution": "예시의95%는 창작 조건이며 실제 공공사업의 실패율·원인 통계가 아닙니다."
      },
      "answer_outline": [
        "복합 실패원인과 제도적 보완",
        "준비 지표·측정·증거",
        "Go/No-Go·단계개통·비상전략"
      ],
      "pitfalls": [
        "시험100%가 어떤 중요 요구를 덮는지 분모를 확인합니다.",
        "개통 뒤 수정할 계획만으로 치명 결함을 승인하지 않습니다."
      ],
      "recall": [
        "전체 진척95%가 개통 가능을 뜻하지 않는 이유는 무엇입니까?",
        "데이터 이관의 핵심 대사 지표는 무엇입니까?",
        "개통 판단에 잔여 위험의 소유자가 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-audit2023",
        "sb-ctfl",
        "sb-taskreview"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "129-2-4",
          "items": [
            "발생된 문제점의 원인",
            "재발 방지를 위한 대책 및 법제도 보완 방안",
            "시스템 오픈 가능여부 판단을 위한 지표관리"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-size-cost-estimation",
      "title": "소프트웨어 규모·비용 산정",
      "domain": "사업관리·대가",
      "aliases": [],
      "related_terms": [],
      "easy": "크기·노력·기간·비용은 서로 연결되지만 같은 단위가 아닙니다. 기능 규모를 구하고 생산성과 단가·조건을 적용해야 비용이 됩니다.",
      "definition": "규모 산정은 개발할 소프트웨어의 양을 일정 기준으로 측정·추정하는 활동이며 비용 산정은 규모·생산성·인력·환경·위험·경비 등으로 필요한 대가를 추정하는 활동입니다.",
      "principles": [
        "규모는 LOC, 기능점수(FP), 유스케이스점수, 객체/화면·보고서점수, 스토리포인트 등으로 추정할 수 있습니다. LOC는 구현 언어·생성코드에 민감하고 초기 추정이 어렵습니다. FP는 사용자가 인식하는 기능·논리데이터를 측정해 언어 독립성이 있으나 경계·유형·복잡도 판단 역량이 필요합니다.",
        "FP는 측정 목적·범위·경계를 정하고 내부논리파일(ILF)·외부연계파일(EIF), 외부입력(EI)·외부출력(EO)·외부조회(EQ)를 식별해 규칙에 따라 규모를 계산합니다. 화면 개수와 FP를 일대일로 같게 세지 않고 사용자의 단위 프로세스와 데이터 유지 여부를 따집니다.",
        "비용 추정은 전문가 판단/Delphi, 유사사례, 상향식 WBS, 모수모형(COCOMO 등), 기능점수 단가 방식 등을 비교합니다. 전문가·유사는 빠르나 편향/비교 가능성, 상향식은 상세하나 초기 누락, 모수모형은 일관되나 보정 데이터 의존성이 있습니다.",
        "공공사업은 해당 판본 가이드와 예산/발주 기준으로 개발비·보정·이윤·직접경비 등을 산정합니다. 기능 요구의 불명확성, 비기능·전환·데이터·통합·시험 과업의 누락을 줄이고 산정 근거·가정·변경 이력을 공유하며 독립 검토와 실적 피드백으로 개선합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "LOC",
            "코드 양",
            "언어/개발환경 영향·사후 측정 용이"
          ],
          [
            "FP",
            "사용자 기능 규모",
            "경계·논리파일·단위프로세스 판단"
          ],
          [
            "공수/스토리포인트",
            "노력/팀 내 상대 크기",
            "기능규모와 단가를 혼동하지 않음"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 고객조회와 매출보고 규모 판단",
        "input": "조회는 저장 데이터를 그대로, 보고는 합계·세금 계산을 출력합니다.",
        "steps": [
          "애플리케이션 경계와 논리 데이터 소유를 정합니다.",
          "추가 계산 없는 조회와 파생 계산 보고를 EQ/EO 규칙으로 구분합니다.",
          "측정 근거와 보정·단가의 판본을 기록하고 누락 과업을 점검합니다."
        ],
        "result": "화면 수가 아닌 기능 처리의 차이로 규모를 설명합니다.",
        "caution": "공식 산정 규칙의 복잡도·단가·보정계수는 해당 판본 원문과 실제 요구로 계산해야 합니다."
      },
      "answer_outline": [
        "규모/노력/비용 구분·필요성",
        "규모 방식·비용 추정 방식 장단점",
        "FP 절차·공공 현실적 개선"
      ],
      "pitfalls": [
        "스토리포인트를 조직 간 고정 원화 단가로 환산하지 않습니다.",
        "근거 없는 임의 난이도 가산으로 누락 과업을 감추지 않습니다."
      ],
      "recall": [
        "EI·EO·EQ를 구분하는 핵심은 무엇입니까?",
        "LOC로 초기 비용을 추정할 때의 한계는 무엇입니까?",
        "상향식 추정에서 누락을 줄일 기준은 무엇입니까?"
      ],
      "source_ids": [
        "sb-fee2025",
        "sb-isp"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "126-2-1",
          "items": [
            "소프트웨어 비용 산정 방법에 대하여 설명하고, 각각의 장·단점을 비교하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-4-5",
          "items": [
            "필요성과 산정방법",
            "규모산정 방식의 종류별 특징"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "132-4-5",
          "items": [
            "소프트웨어 개발에 필요한 규모 산정 방식 종류와 특징을 비교 설명하고, 공공 소프트웨어 사업 규모 산정 방식의 현실적 개선 방안에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-operations-pricing",
      "title": "2023 운영단계 SW 대가산정",
      "domain": "사업관리·대가",
      "aliases": [],
      "related_terms": [],
      "easy": "유지관리 대상 규모에 요율을 적용하는 방식과 실제 운영업무의 필요한 노력을 계산하는 방식을 구분해야 합니다.",
      "definition": "SW 운영단계 대가산정은 응용SW 유지관리·상용SW 지원·운영·재개발 등 과업 범위와 서비스 조건에 맞춰 비용을 산정하는 활동입니다. 132회는2023년 가이드 판본을 명시합니다.",
      "principles": [
        "2023 응용SW 요율제는 계약시점 현재가치로 재산정한 개발비×요율+직접경비입니다. 유지관리 횟수·사용자 수·중요도·타시스템 연계·오류복구 신속성의 난이도 총점 TMP(0~100)를 구하고 요율(%)=10+5×TMP/100, 즉 10~15%를 적용합니다. 과거 개발 당시 총액을 그대로 현재가치로 쓰지 않습니다.",
        "운영 투입공수는 대상SW/서비스 정의→일상운영/지원업무를 대·중·소분류→업무별 직무와 경험·난이도·운영생산성/실적으로 소요공수 산정→직무별 평균임금을 곱해 직접인건비를 구합니다. 직접인건비+제경비(직접인건비 144~154%)+기술료(인건비+제경비의 20~40%)+직접경비가 운영비이며 기간·단위·세금 처리를 확인합니다.",
        "혼합방식의 고정비는 적응/수리 유지관리·일상운영·지원업무를 투입공수로 운영비 산정합니다. 변동비는 완전 유지관리의 기능개선/추가개발로 계획량+예측량을 구해 기능점수/재개발 방식을 적용합니다. 무상 하자보수 기간의 수리 유지관리는 유상 대가에서 제외하며 업무 특성에 맞춰 분류합니다.",
        "혼합 대가는 사전준비→고정/변동 업무 구분→각각 산정→직접경비→고정비+변동비+직접경비의 5단계입니다. 변동비 실적량과 사전추정 차이는 계약상 가능한 정산방식으로 처리하고 범위·승인·실적·단가·한도를 기록합니다. 이미 포함된 과업을 중복 계상하거나 신규 개발을 무상 운영에 숨기지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "응용SW 요율제",
            "유지관리 대상가치×적용요율",
            "대상·난이도·범위·기간 확정"
          ],
          [
            "운영 투입공수",
            "업무량→직무별 노력→비용",
            "일상운영/서비스 조건을 반영"
          ],
          [
            "고정/변동",
            "상시업무 / 실적에 따라 변하는 과업",
            "측정·승인·정산 단위 명확화"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 운영·기능개선 분리",
        "input": "월간 모니터링과 분기별 신규 기능 요청이 함께 있습니다.",
        "steps": [
          "현재가치 개발비 1억원, TMP40이라면 요율12%로 연간 기본 유지관리비 1,200만원+직접경비를 계산합니다.",
          "운영 인력의 업무/직무별 공수와 기능개선 FP를 분리하고 혼합방식의 고정/변동분을 정합니다.",
          "요율제와 혼합방식을 같은 과업에 중복 적용하지 않고 계약방식을 선택·검증합니다."
        ],
        "result": "대상과 업무량의 중복 없는 산정 구조가 됩니다.",
        "caution": "모든 금액·TMP는 강사 창작값입니다. 2023 가이드 요율·산식을 원리 설명에 적용했고 현행 계약단가·임금과 세금은 별도 확인합니다."
      },
      "answer_outline": [
        "132회 지정 판본·범위",
        "요율제/공수 방식 절차",
        "고정/변동 과업·정산·판본 차이"
      ],
      "pitfalls": [
        "상용SW 유지관리 요율을 응용SW 요율과 혼합하지 않습니다.",
        "공표 제경비율을 모든 사업 항목에 무조건 적용하지 않습니다."
      ],
      "recall": [
        "요율제의 대상가치와 구매가격은 항상 같습니까?",
        "일상운영과 기능개선은 왜 분리합니까?",
        "변동비 정산의 증거는 무엇입니까?"
      ],
      "source_ids": [
        "sb-fee2023",
        "sb-fee2025"
      ],
      "validation": "출처 확인",
      "version_note": "KOSA2023공식PDF p.165~171·199~201·221~223의산식과5단계를직접대조했습니다.2025판AI항목등을2023문항에소급하지않습니다.",
      "requirements": [
        {
          "question": "132-3-1",
          "items": [
            "응용SW 요율제 유지관리비 산정방식과 SW운영 투입공수 산정방식",
            "고정비/변동비 산정방식"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "ai-service-pricing-2025",
      "title": "2025 AI 서비스 도입 사업 대가산정",
      "domain": "사업관리·대가",
      "aliases": [],
      "related_terms": [],
      "easy": "AI 모델을 쓰는 비용과 기관에 맞게 바꾸는 비용, 다른 시스템과 개발·통합하는 비용을 나누어 산정합니다.",
      "definition": "KOSA2025 가이드는 SW 수명주기 사업의 예산·발주·계약에 적정대가 기준을 제공하며, AI 도입 사업비를 서비스 총이용료+커스터마이징 작업비용+구축·개발비용으로 구분합니다.",
      "principles": [
        "단순 AI서비스 도입형은 개발·변형 없이 구독료를 지불하고 이용합니다. 커스터마이징형은 기관 목적에 맞게 조정하며 기본형, AI데이터 구축형, AI모델형으로 작업 수준을 구분합니다. 시스템통합형은 커스터마이징과 추가 SW 개발·통합을 병행합니다.",
        "기본 커스터마이징은 기초 요구·설계·샘플데이터·사전학습 모델 적용·검증을, 데이터형은 신규/재구축 데이터의 수집·정제·가공·검수를, 모델형은 최적화·파인튜닝·모델/알고리즘 개발·검증을 포함할 수 있습니다. 실제 요구와 포함 범위를 보고 중복을 제거합니다.",
        "산정 절차는①사전준비로 대상서비스·유형·추가작업 결정②기능·기간·사용규모에 따른 서비스 이용료 계산③가격표/견적·유사사례·공수로 커스터마이징 작업비 계산④필요 개발/통합을 기능점수 또는 공수 방식으로 산정⑤세 비용을 합산합니다.",
        "커스터마이징 요소는 요구 분석·설계, 데이터 구축, 모델 구현·학습, 서비스 검증·안정화입니다. 성능 미달 시 반복되는 작업의 비용·일정을 고려하고 이용료에 이미 포함된 기본 지원을 중복 지급하지 않습니다. 단위 이용료의 토큰·호출·좌석·기간과 초과 요금·인프라 포함 여부도 확인합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "단순 도입",
            "서비스 이용료",
            "기관별 변형 없이 사용"
          ],
          [
            "커스터마이징",
            "이용료+기관별 조정작업",
            "기본·데이터·모델 유형"
          ],
          [
            "시스템통합",
            "이용료+조정+구축/개발",
            "추가 연계·기능 개발 포함"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 민원 상담 AI 도입",
        "input": "상용 서비스를 쓰되 기관 문서 정제와 내부 업무 연계가 필요합니다.",
        "steps": [
          "구독/사용량 이용료와 포함 지원 범위를 확인합니다.",
          "문서 수집·정제·검수와 모델/검색 조정 작업을 분리합니다.",
          "인증·업무 연계 개발을 별도 규모로 계산하고 합산·중복 검토합니다."
        ],
        "result": "유형과 작업에 근거한 사업비 내역을 만들 수 있습니다.",
        "caution": "예시에는 금액을 두지 않았습니다. 가격표와 견적은 동일한 서비스 수준·기간·범위로 비교해야 합니다."
      },
      "answer_outline": [
        "가이드 목적과2025 개정",
        "3사업유형·비용구조",
        "5단계 산정·작업요소·중복 방지"
      ],
      "pitfalls": [
        "모든 AI사업을 FP 하나로 산정하지 않습니다.",
        "파인튜닝이 반드시 필요한 과업이라고 미리 가정하지 않습니다."
      ],
      "recall": [
        "시스템통합형에는 어떤 비용이 추가됩니까?",
        "커스터마이징 네 작업요소를 말하십시오.",
        "이용료와 작업비의 중복을 어떻게 찾습니까?"
      ],
      "source_ids": [
        "sb-fee2025"
      ],
      "validation": "출처 확인",
      "version_note": "KOSA2025년 개정판 p.157~169 실제 원문 열람. 2025판의 명칭은 전문작업비가 아니라 커스터마이징 작업비용입니다.",
      "requirements": [
        {
          "question": "137-4-6",
          "items": [
            "소프트웨어 대가산정 가이드 목적",
            "인공지능(AI) 서비스 도입 사업유형과 사업비 산정 절차"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "public-software-task-review",
      "title": "공공SW 과업 확정·기간·변경 심의",
      "domain": "사업관리·제도",
      "aliases": [],
      "related_terms": [],
      "easy": "과업을 시작 전에 구체화하고, 바뀌는 요구가 비용과 일정에 미치는 영향을 공식적으로 판단해야 합니다.",
      "definition": "과업심의는 공공 SW사업의 내용·범위·대가·기간과 변경의 적정성을 검토하는 절차입니다. 발주자가 요구를 명확히 하고 정당한 변경의 계약 조정을 다룰 수 있도록 합니다.",
      "principles": [
        "계획/확정 단계는 목적·필요성·범위·기능과 비기능 요구·산출물·검증기준의 명확성, 예산 산정 근거·기능규모·누락 과업, 타 사업/시스템 중복·연계와 상용SW 직접구매 적용 등을 검토합니다.",
        "적정기간은 요구·규모·생산성·조직·자원·기술 난이도·연계·데이터 이관·시험·발주/협의 절차를 반영합니다. 총 개발기간에서 법정/행정 절차와 사용자 인수·안정화 시간을 누락하지 말고 근거를 문서화합니다. 특정 금액·사업 유형의 의무·간소화 요건은 현행 지침을 대조합니다.",
        "변경 심의는 변경 사유·발주/사업자 책임·당초 범위와의 차이·필요성·기술 가능성, 기능/작업의 증가·감소, 일정·비용·품질·보안·기존 연계 영향, 대안과 미변경 위험을 평가합니다. 계약금액·기간 조정과 변경된 인수기준을 함께 결정해야 합니다.",
        "사업자 요청을 포함해 변경요청서·원래/변경 과업 비교·규모/공수·일정 영향·견적과 시험 근거를 제출하고 심의·결정·계약변경·형상/추적 갱신으로 연결합니다. 단순 오류수정·하자와 추가 과업을 근거 없이 혼동하면 분쟁을 유발합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "확정",
            "발주할 범위·대가·기간",
            "명확성·완전성·산정 근거"
          ],
          [
            "변경",
            "새 요구·환경 변화의 영향",
            "책임·필요·추가/감소·계약 조정"
          ],
          [
            "인수",
            "합의한 결과의 검증",
            "원/변경 기준선과 증거 일치"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 신규 법정 보고서 추가",
        "input": "개발 중 당초 없던 월간 집계보고서가 필요해졌습니다.",
        "steps": [
          "원 요구와 비교해 신규 기능·데이터·시험 범위를 적습니다.",
          "기간·비용·연계 영향과 대안을 평가해 과업심의를 요청합니다.",
          "승인된 금액·기간·인수 기준과 RTM을 갱신합니다."
        ],
        "result": "무상 추가 요청이나 임의 구현이 아닌 추적 가능한 변경이 됩니다.",
        "caution": "구체적 위원 구성·간소화 조건과 기한은 해당 시점 법령·고시를 확인해야 합니다."
      },
      "answer_outline": [
        "계획 확정 검토항목",
        "적정기간 산정의 요소",
        "변경 적정성·계약·기준선 조정"
      ],
      "pitfalls": [
        "모든 요구 변경을 하자로 분류하지 않습니다.",
        "예산이 그대로라는 이유만으로 추가 과업의 비용이0이 되지 않습니다."
      ],
      "recall": [
        "과업 확정과 인수는 어떤 차이가 있습니까?",
        "적정기간에서 시험·이관을 별도로 확인하는 이유는 무엇입니까?",
        "변경 요청에 필요한 증거를 세 가지 말하십시오."
      ],
      "source_ids": [
        "sb-taskreview",
        "sb-swlaw2023",
        "sb-isp"
      ],
      "validation": "부분 확인",
      "version_note": "공공기관 공식 운영안내·지정 법 원문을 확인했습니다. 128회 당시 과업심의 가이드의 정식 평가 항목명 및 현행 고시 조문별 대조는 추가 확인이 필요합니다.",
      "requirements": [
        {
          "question": "128-3-4",
          "items": [
            "공공소프트웨어 사업의 계획단계에서 사업의 확정 및 사업 기간의 적정성 평가를 위한 검토항목과 사업수행 중 과업 변경에 대한 적정성 판단 평가 기준에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "software-promotion-act-plan-safety",
      "title": "SW 진흥법 기본계획·SW안전 지침",
      "domain": "사업관리·법령",
      "aliases": [],
      "related_terms": [],
      "easy": "진흥계획은 산업을 어떻게 키울지, 안전지침은 SW의 위험을 수명주기에서 어떻게 줄일지 규정합니다.",
      "definition": "132회는 시행2023.10.19 소프트웨어 진흥법 제5조제2항의 기본계획과 제30조제2항의 안전 지침 포함사항을 묻습니다. 해당 지정 판본을 기준으로 조항의 범위를 설명해야 합니다.",
      "principles": [
        "제5조제2항의13사항은①산업 진흥 시책 기본방향②부문별 육성시책③산업 기반 조성④SW교육·인력양성⑤기술 연구개발·보급⑥이용 촉진·유통 활성화⑦SW/융합 창업 지원⑧국제협력·해외진출⑨자산관리 활성화⑩SW융합 활성화⑪지역별 특성 기반 산업 진흥·지역 산업 융합⑫SW안전 관리⑬그 밖의 진흥 필요사항입니다.",
        "제30조제2항의5사항은①SW안전 관련 위험 분석②안전 확보 설계·구현 방법③안전 검증 방법④운영단계 안전 확보 방안⑤그 밖에 안전 확보에 필요한 사항입니다. 위험분석→설계/구현→검증→운영이라는 수명주기 통제를 연결해 이해합니다.",
        "2023판의 SW안전 정의는 외부 침해가 없는 상태에서 내부 오작동·안전기능 미비 등으로 사람의 생명·신체 위험에 충분히 대비된 상태를 뜻합니다. 보안 침해 방어와 안전의 분석 관점은 구분되지만 실제 시스템에서는 서로 영향을 주므로 함께 관리합니다.",
        "2026-11-05 법령 검색 화면은2025.4.23 시행 제20476호와2027.2.12 시행 예정 제21865호를 별도 표시했습니다. 예정 법령을 현재 시행이라고 쓰지 않으며, 현행 조항 전체와2023판의 상세 대조를 마치기 전 위13/5사항이 그대로라고 단정하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "제5조",
            "국가 SW산업 진흥의 계획 범위",
            "산업·교육·R&D·유통·국제·지역·안전"
          ],
          [
            "제30조",
            "안전 지침의 필수 내용",
            "위험·설계구현·검증·운영"
          ],
          [
            "기출/현행/예정",
            "2023 지정 /2025 현행 /2027 예정",
            "시행일과 적용 시점을 분리"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 산업용 제어SW 사업 기획",
        "input": "산업진흥 지원과 안전 활동 예산을 검토합니다.",
        "steps": [
          "인력양성·R&D·융합은 기본계획의 진흥 축에 연결합니다.",
          "제어위험 분석·안전설계·검증·운영 모니터링을 안전 지침 축으로 연결합니다.",
          "적용 법령의 시행일과 사업 시점을 표기합니다."
        ],
        "result": "조항을 나열하는 데서 사업 수명주기 활동으로 연결할 수 있습니다.",
        "caution": "예시는 법률 자문이나 특정 사업의 적법성 확정이 아닙니다."
      },
      "answer_outline": [
        "지정 판본·조문·목적",
        "제5조13사항·제30조5사항",
        "안전/보안·현행/예정 구분"
      ],
      "pitfalls": [
        "SW안전을 정보보안만으로 설명하지 않습니다.",
        "2027 시행 예정법을2026 현행으로 인용하지 않습니다."
      ],
      "recall": [
        "제30조5사항을 수명주기 순서로 설명하십시오.",
        "지역 산업 융합은 제5조에서 어떤 의미를 가집니까?",
        "공포일과 시행일을 구분해야 하는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-swlaw2023",
        "sb-swlawcurrent"
      ],
      "validation": "부분 확인",
      "version_note": "기출 지정2023.10.19판 제5조·제30조는 원문 확인. 2026-11-05 현행 법령 메타데이터는 확인했으나 해당 조항 상세 신구대조는 미완료입니다.",
      "requirements": [
        {
          "question": "132-4-4",
          "items": [
            "제5조(기본계획의 수립 등)의 2항에 따른 기본계획 내 포함되어야 할 사항",
            "제30조(소프트웨어안전 확보)의 2항에 따른 소프트웨어안전 확보를 위한 지침 내 포함되어야 할 사항"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "it-job-competency-system",
      "title": "SW 기술자 등급제와 IT직무제",
      "domain": "사업관리·인력",
      "aliases": [],
      "related_terms": [],
      "easy": "경력 연수만으로 사람을 한 줄 세우는 것과 실제 맡는 직무·역량에 맞춰 인력을 구분하는 것은 다른 방식입니다.",
      "definition": "과거 SW 기술자 등급제는 자격·학력·경력으로 기술자를 등급화한 체계이고, IT직무제는 실제 직무와 필요한 역량을 기준으로 역할·인력·임금을 파악하는 접근입니다.",
      "principles": [
        "IT분야 역량체계(ITSQF)는 직무와 요구 역량·수준을 공통 언어로 설명하여 인재 양성·배치·경력개발·역량 인정의 연결을 돕습니다. 업무분석·아키텍처·개발·시험·운영·PM 등 다른 책임을 단순 경력연수 하나로 환산하지 않는 것이 취지입니다.",
        "등급제는 발주·인력 비교가 단순하지만 실제 능력·전문성을 충분히 반영하지 못할 수 있습니다. 직무제는 과업과 역량을 연결하기 유리하지만 직무 경계·수준의 해석 차이, 한 사람이 여러 직무를 맡는 현실, 실적·역량 검증의 어려움이 있습니다.",
        "현장 문제는 폐지된 등급을 관성적으로 요구, 평균임금을 고정 지급임금으로 오해, 역할 정의 없이 직무 명칭만 바꿈, 경력 서류와 실제 과업의 불일치 등입니다. 평균임금은 통계적 산정 자료로 근로자 개별 급여를 법적으로 동일화하는 표가 아닙니다.",
        "개선은 RFP/WBS에 역할·책임·과업·요구역량·검증방식을 명시하고 직무별 공수·인건비 산정 근거를 연결하는 것입니다. 면담·포트폴리오·수행실적·현장평가로 역량을 확인하고 교육·경력경로·자격의 상호 인정과 계약 운영 지침을 정비합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "등급 중심",
            "학력·자격·연수로 범주화",
            "비교가 쉽지만 직무 적합성 한계"
          ],
          [
            "직무 중심",
            "실제 역할·역량·수준",
            "과업 정의와 검증 체계 필요"
          ],
          [
            "임금 활용",
            "직무별 통계와 공수 근거",
            "개인 급여의 자동 결정과 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: DB 전환 사업 인력 요구",
        "input": "발주서가 고급2명만 요구합니다.",
        "steps": [
          "실제 과업을 데이터 이관 설계·튜닝·검증·운영전환으로 나눕니다.",
          "역할별 경험·기술·책임과 수행 증거를 요구합니다.",
          "직무별 투입공수와 계약 대가를 산정하고 겸임 충돌을 점검합니다."
        ],
        "result": "과거 등급명 대신 사업 수행에 필요한 역량을 설명합니다.",
        "caution": "직무 수·명칭·평균임금 단가는 최신 공식 고시·통계로 확인해야 합니다."
      },
      "answer_outline": [
        "두 제도의 정의·특징",
        "현행 실무 문제",
        "과업·역량·검증·임금 연결 개선"
      ],
      "pitfalls": [
        "2018 도입 당시 직무 수를2026 현행 수로 단정하지 않습니다.",
        "직무제와 자격증을 완전히 대체 관계로 보지 않습니다."
      ],
      "recall": [
        "동일 경력연수라도 다른 역량이 필요한 예를 드십시오.",
        "평균임금을 개인 급여표로 쓰면 왜 문제가 됩니까?",
        "직무 요구에 어떤 검증 자료를 붙일 수 있습니까?"
      ],
      "source_ids": [
        "sb-itsqf",
        "sb-fee2025"
      ],
      "validation": "부분 확인",
      "version_note": "산업단체의 ITSQF 도입 설명 확인. 등급제 폐지일·현행 직무 목록·2026 임금 수치는 별도 최신 원문 확인이 필요합니다.",
      "requirements": [
        {
          "question": "132-2-3",
          "items": [
            "소프트웨어 기술자 등급제와 IT직무제의 개념과 특징",
            "현행 IT직무제의 문제점과 개선방향"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "software-proposal-evaluation-2024",
      "title": "2024 조달청 대형SW 전문평가제",
      "domain": "사업관리·조달",
      "aliases": [],
      "related_terms": [],
      "easy": "규모가 큰 SW사업은 공통 역량과 기술 전문성을 나눠 평가해 수요기관의 판단을 보완합니다.",
      "definition": "2024.9.13 시행된 제안서평가 세부기준 개정은 대형SW 전문평가, 수의계약 적합성 평가 대행, 허위·비방 판단 정비, 발표기준 조정과 기술용역 평가기준 신설을 도입했습니다.",
      "principles": [
        "대형 SW전문평가는 사업금액40억원 이상 SW사업에 적용하되 유지관리 사업은100억원 이상 기준으로 설명되었습니다. 정보기술개발·정보보호·데이터구축·디지털기술4전문영역에 대해 심층 평가가 필요한 경우 관련 전문가가 전담합니다.",
        "최종 점수는 공통평가60%와 전문평가40%를 합산하는 구조로 공개됐습니다. 공통평가는 수행체계·관리 등 일반 역량, 전문평가는 해당 기술 제안의 실현성과 품질·전문성을 깊게 판단하는 취지이며 실제 세부항목은 발주 평가표를 확인합니다.",
        "개정은 수요기관 요청 시 수의계약 제안서 정성평가 대행 근거를 마련하고, 허위 내용과 입찰 결과 영향은 내부 심의로 판단하도록 명확히 했습니다. 타사 비방 기재·발표에 대한 감점과 온라인 제안서 발표 기준을5억원 이상으로 높이는 조치도 포함됐습니다.",
        "제도의 효과는 전문성·공정경쟁·입찰 부담 개선이라는 정책 목표와 실제 성과를 구분합니다. 평가위원의 전문성·이해상충·자료 신뢰성·기술 검증·기준 공개·질의응답 기록을 운영해야 형식적인 가중치 변경에 그치지 않습니다. 이후 개정의 현행 기준을2024 보도자료로 확정하면 안 됩니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "공통평가",
            "사업 수행 전반의 평가",
            "2024 안내 가중치60%"
          ],
          [
            "전문평가",
            "4영역의 심층 기술 평가",
            "2024 안내 가중치40%"
          ],
          [
            "기타 개정",
            "대행·허위/비방·발표기준·기술용역",
            "입찰 분쟁·부담과 전문성 보완"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 대규모 데이터 플랫폼 제안 평가",
        "input": "50억원 SW 구축 사업에 고급 데이터 기술이 포함됩니다.",
        "steps": [
          "적용 대상과 전문 평가 필요 영역을 확인합니다.",
          "공통 수행체계와 데이터 구축·품질 기술을 분리해 평가합니다.",
          "근거자료·위원 이해상충·질의응답과 점수 산식을 기록합니다."
        ],
        "result": "가격·발표 능력만으로 기술 실현성을 판단하는 위험을 줄입니다.",
        "caution": "50억원은 창작 사업규모이며2024 기준을 적용하는 예입니다. 실제 입찰은 현행 공고·규정을 따릅니다."
      },
      "answer_outline": [
        "개정 배경·시행일",
        "대상·4영역·60/40 구조",
        "기타 주요 개정·공정성 운영"
      ],
      "pitfalls": [
        "2024의40억/100억 기준을 검증 없이 미래 모든 입찰에 적용하지 않습니다.",
        "공식 기대 비용절감 추계를 실제 실현 성과로 쓰지 않습니다."
      ],
      "recall": [
        "유지관리 사업의2024 적용금액은 얼마입니까?",
        "공통과 전문평가의 가중치는 무엇입니까?",
        "허위 제안서 내용의 판단 절차가 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-procurement"
      ],
      "validation": "출처 확인",
      "version_note": "조달청2024-09-11 공식 보도자료의2024-09-13 시행 개정 기준입니다. 후속 개정 여부는 별도 현행 규정 확인 필요합니다.",
      "requirements": [
        {
          "question": "136-4-3",
          "items": [
            "계약 제안서평가 세부기준 개정 주요 내용",
            "대형소프트웨어 사업 전문평가제도"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "isp-ismp-bpr",
      "title": "ISP·ISMP·BPR 수행과 산출물",
      "domain": "IT전략",
      "aliases": [],
      "related_terms": [
        "ISP",
        "ISMP",
        "BPR"
      ],
      "easy": "BPR은 일하는 방식을 바꾸고, ISP는 조직의 정보화 방향을, ISMP는 특정 시스템을 발주할 상세 요건을 구체화합니다.",
      "definition": "ISP는 경영/업무 전략에 정렬된 정보화 비전·목표모델·이행계획을 수립하는 계획이고, ISMP는 특정 정보시스템의 방향·업무/기술 요건·구조·구축계획을 상세화합니다. BPR은 고객 가치와 성과를 중심으로 업무 프로세스를 재설계하는 활동입니다.",
      "principles": [
        "NIA9판의 ISP는 환경분석(경영·법제도·IT동향), 현황분석(업무·응용·데이터·인프라·거버넌스·벤치마킹·차이/이슈), 정보화 비전·전략, 목표모델(과제·업무프로세스·응용·데이터·기술/보안), 통합 이행계획(우선순위·일정·구축비·효과)으로 구성합니다. 단계 산출물은 각 분석서·정보화전략정의서·To-Be 설계서·통합이행계획서입니다.",
        "ISMP는 착수/참여자 결정→정보시스템 방향성→업무·IT요건 분석→시스템 구조·요건 정의→구축사업 이행방안→제안요청서입니다. 조직/계획·범위/목표·업무/IT 요구분석서·To-Be 모델·요구연관표·요건기술서·이행계획/RFP를 만듭니다.",
        "BPR은 범위·성과목표와 프로세스 소유자 정의→As-Is 흐름/대기/중복·근본원인 분석→고객 가치 중심 To-Be 재설계→조직·권한·IT 변화 설계→실행·성과 검증으로 접근합니다. 기존 비효율을 그대로 전산화하는 것을 피합니다.",
        "상호 보완은 BPR이 바꿀 업무·책임과 성과를 제시하고 ISP가 이를 정보화 과제·데이터·아키텍처·투자로 연결하며 ISMP가 발주 가능한 요건으로 상세화하는 것입니다. AI기반 BPR은 분류·예측·문서처리·추천으로 대기·재작업·판단을 개선할 수 있으나 예외처리·인간 승인·편향·책임·측정이 필요합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "ISP",
            "기관/조직 정보화 전략과 로드맵",
            "왜·무엇을·어떤 순서로 투자할지"
          ],
          [
            "ISMP",
            "특정 시스템 구축 요건·발주계획",
            "어떤 요구·구조·범위로 구축할지"
          ],
          [
            "BPR",
            "업무 흐름·역할·가치 재설계",
            "불필요 업무 제거 후 IT 연결"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 허가 신청 처리 재설계",
        "input": "같은 서류를 세 부서가 다시 입력하고 심사 대기가 깁니다.",
        "steps": [
          "BPR로 중복 입력을 없애고 병렬 심사·예외 승인 규칙을 정합니다.",
          "ISP로 공통 데이터·연계·통합포털 과제와 이행순서를 수립합니다.",
          "ISMP로 API·권한·성능·시험 요구와 RFP를 상세화합니다."
        ],
        "result": "업무 변화와 투자·발주의 연결 근거가 생깁니다.",
        "caution": "AI도입 효과의 기간·비용 절감률은 실제 측정 없이 수치로 만들지 않습니다."
      },
      "answer_outline": [
        "3개념·목적·비교",
        "ISP/ISMP 단계별 활동·산출물",
        "BPR 상호보완·AI 활용과 통제"
      ],
      "pitfalls": [
        "ISP를 장비 구매계획으로 축소하지 않습니다.",
        "129회 지정6판과9판의 행정절차/기준을 혼합하지 않습니다."
      ],
      "recall": [
        "ISP와 ISMP의 범위 차이는 무엇입니까?",
        "BPR 없는 전산화가 실패하는 예를 드십시오.",
        "요구 연관표는 ISMP에서 왜 필요합니까?"
      ],
      "source_ids": [
        "sb-isp"
      ],
      "validation": "부분 확인",
      "version_note": "ISP·ISMP9판(2025.12 일부개정) p.40~44 실제 열람. 129회6판의 고유 변경내용·산출물 표와의 세부 대조는 미완료입니다.",
      "requirements": [
        {
          "question": "127-3-1",
          "items": [
            "단계별 활동 및 산출물",
            "ISMP(Information System Master Plan)와 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-3-1",
          "items": [
            "공통 가이드 수립 배경 및 필요성",
            "ISP와 ISMP의 차이점",
            "ISP 및 ISMP의 각 단계별 활동 내용 및 산출물의 종류"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "130-1-10",
          "items": [
            "정보시스템마스터플랜(ISMP)의 기본 구성 내용(단계별 활동, 세부내용, 산출물)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-2-1",
          "items": [
            "ISP(Information Strategic Planning)와 BPR(Business Process Reengineering)의 개념과 수행절차를 비교 설명하고, 기업에서 이 두 가지가 상호 보완적으로 활용하기 위한 방안을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "138-2-2",
          "items": [
            "ISP(Information Strategy Planning)의 정의 및 목적",
            "ISP 수행방법론 체계와 절차",
            "ISP, ISMP(Information System Master Plan) 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "140-1-1",
          "items": [
            "AI 기반의 업무 프로세스 재설계(BPR, Business Process Reengineering) 도입 효과"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "it-governance-enterprise-architecture",
      "title": "IT 거버넌스·EA·효과 평가",
      "domain": "IT전략",
      "aliases": [],
      "related_terms": [],
      "easy": "거버넌스는 누가 무엇을 기준으로 결정하고 책임지는지, 관리는 그 방향에 따라 어떻게 수행하는지를 다룹니다.",
      "definition": "IT거버넌스는 이해관계자의 요구를 평가하고 정보기술의 가치·위험·자원을 균형 있게 통제하며 방향 설정과 성과 감시를 수행하는 체계입니다. EA는 업무·데이터·응용·기술의 현행/목표 구조와 이행관계를 일관되게 기술합니다.",
      "principles": [
        "구성은 의사결정권·위원회·책임, 전략·투자·위험·성과 프로세스, 원칙·정책·정보, 사람·역량·문화, 서비스·인프라·응용 등으로 설명할 수 있습니다. COBIT은 거버넌스를 EDM(평가·방향·감시), 관리를 APO·BAI·DSS·MEA 영역으로 구분합니다.",
        "주요 평가 관점은 전략 정렬, 가치/편익 실현, 위험 최적화, 자원 최적화, 성과·이해관계자 투명성입니다. 지표는 전략과 연결된 투자 비중, 약속한 편익 실현, 위험 수용범위 초과, 중복자산·용량 활용, 서비스 수준·만족도·규정 준수 등으로 구체화합니다.",
        "효과 측정은 목표-지표-기준선-목표값-측정책임을 연결하고 IT-BSC·성숙도/역량 평가·벤치마킹·투자 사후평가를 함께 적용합니다. 프로세스 준수율이 높아도 고객 성과가 좋아졌는지 별도로 확인해야 합니다.",
        "EA는 업무 목표에 맞는 목표 아키텍처와 재사용·상호운용·표준을 제시하고 사업 검토·중복 방지·이행 로드맵에 연결합니다. 거버넌스는 EA 준수 예외의 승인과 영향·기한을 관리하고, EA 산출물을 만드는 활동 자체를 가치 실현으로 간주하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "거버넌스",
            "목적·방향·책임·감시",
            "무엇을 왜 우선할지 결정"
          ],
          [
            "관리",
            "계획·구축·운영·평가 실행",
            "목표를 달성할 활동 수행"
          ],
          [
            "EA",
            "업무/데이터/응용/기술 구조",
            "투자·표준·전환 의사결정 지원"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 중복 고객시스템 투자 심의",
        "input": "세 부서가 별도 고객DB와 포털을 요청합니다.",
        "steps": [
          "EA에서 공통 업무·데이터·기술의 중복과 목표구조를 확인합니다.",
          "거버넌스 위원회가 통합 편익·위험·비용과 예외 필요성을 판단합니다.",
          "사후에는 중복 감소만 아니라 사용자 처리성과와 서비스 수준도 측정합니다."
        ],
        "result": "구조 검토와 투자 책임·성과를 하나의 의사결정으로 연결합니다.",
        "caution": "프레임워크의 점수나 성숙도를 실제 정확도·출제 중요도와 연결하지 않습니다."
      },
      "answer_outline": [
        "거버넌스 구성·EDM/관리 구분",
        "효과 지표와 측정방법론",
        "EA 구조·투자·예외관리 연계"
      ],
      "pitfalls": [
        "COBIT과 ITIL·ISO20000을 같은 범위의 프레임워크라고 쓰지 않습니다.",
        "성숙도 상승만으로 투자편익 실현을 보장하지 않습니다."
      ],
      "recall": [
        "EDM과 관리4영역의 차이는 무엇입니까?",
        "EA 예외를 허용할 때 남길 정보는 무엇입니까?",
        "통제 지표와 성과 지표를 하나씩 제시하십시오."
      ],
      "source_ids": [
        "sb-cobit",
        "sb-isp"
      ],
      "validation": "부분 확인",
      "version_note": "ISACA 공식 공개 설명·NIA 목표모델 근거 확인. COBIT2019 유료 본문 전체의 구성요소 정의·역량 산정표는 미열람입니다.",
      "requirements": [
        {
          "question": "134-2-3",
          "items": [
            "IT 거버넌스의 구성요소",
            "IT 거버넌스 효과 측정 지표",
            "IT 거버넌스 효과 측정 방법론"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "it-investment-balanced-scorecard",
      "title": "IT 투자평가·ROI·BSC",
      "domain": "IT전략·경영",
      "aliases": [],
      "related_terms": [
        "ROI",
        "BSC",
        "NPV"
      ],
      "easy": "투자 전에는 가정이 타당한지, 투자 후에는 약속한 편익이 실제로 생겼는지를 확인해야 합니다.",
      "definition": "IT투자평가는 전략 적합성·경제성·위험·자원·편익을 검토하여 투자 선정과 사후 개선을 지원하는 과정입니다. BSC는 재무뿐 아니라 고객·내부프로세스·학습성장의 관점으로 전략을 목표·지표·과제로 연결합니다.",
      "principles": [
        "프로세스는 사업목표·대안·분석범위/기간 정의→비용·편익·위험 식별→현금흐름·비재무 평가→민감도·시나리오와 우선순위→승인→실행성과 추적→편익/가정 사후검증입니다. 사업책임자가 편익 실현을 맡아야 IT산출물만 만들고 끝나는 것을 줄입니다.",
        "경제성은 ROI=(편익−비용)/비용, NPV=기간별 순현금흐름의 할인합, B/C=할인편익/할인비용, IRR=NPV를0으로 하는 할인율, 회수기간=누적 순편익이 초기투자를 회수하는 시점으로 비교합니다. 할인·기간·단위·세금·잔존가치 등 가정을 일관되게 해야 합니다.",
        "TCO는 도입비 외 개발·운영·전환·교육·장애·종료 비용을 포함합니다. 무형 편익·법적 필수·위험 감소는 가능한 지표와 의사결정 근거를 제시하되 근거 없이 모두 원화로 바꾸지 않습니다. 중복 편익과 다른 사업의 기여를 분리합니다.",
        "BSC의 재무(비용/가치), 고객(만족·서비스), 내부프로세스(처리시간·품질), 학습성장(역량·조직·정보) 관점을 전략지도·선행/후행 지표로 연결합니다. IT-ROI라는 이름 아래 재무·프로세스·조직·전략 등을 평가하는 다양한 모델이 있으므로 단일 법정 구성이라고 암기하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "ROI",
            "비용 대비 순편익 비율",
            "기간·할인 누락에 주의"
          ],
          [
            "NPV/B-C",
            "시간가치가 반영된 가치/비율",
            "대안 규모와 가정 비교"
          ],
          [
            "BSC",
            "4관점의 전략·성과 연결",
            "재무 외 편익과 선행지표 보완"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 업무 자동화 투자 산술",
        "input": "초기비용100, 운영비20, 편익60이2년간 발생하며 할인은 생략합니다.",
        "steps": [
          "순편익은(60−20)×2−100=−20으로 계산합니다.",
          "비용140, 편익120 기준 단순 ROI는−20/140≈−14.3%입니다.",
          "처리오류·직원부담·규제 준수는 별도 측정하고 투자 대안을 재검토합니다."
        ],
        "result": "좋아 보이는 기술과 경제적으로 타당한 투자를 구분합니다.",
        "caution": "가상의 단위 없는 예시이며 현금흐름·잔존가치·할인율이 달라지면 결과도 바뀝니다."
      },
      "answer_outline": [
        "투자평가 프로세스·프레임워크",
        "ROI/NPV/B-C/IRR/TCO 비교",
        "BSC4관점·비재무·사후평가"
      ],
      "pitfalls": [
        "시간 절감 전부가 현금 인건비 절감이라고 가정하지 않습니다.",
        "서로 다른 기간의 ROI를 그대로 비교하지 않습니다."
      ],
      "recall": [
        "ROI와 NPV의 핵심 차이는 무엇입니까?",
        "BSC4관점에 IT지표를 하나씩 배치해 보십시오.",
        "편익 사후검증의 책임은 왜 필요합니까?"
      ],
      "source_ids": [
        "sb-bsc",
        "sb-isp",
        "sb-fee2025"
      ],
      "validation": "부분 확인",
      "version_note": "BSC 저자 해설과 ISP 경제성 활동을 확인했습니다. 특정 IT-ROI 명칭의 단일 모델 출전·전체 지표는 추가 확인 필요합니다.",
      "requirements": [
        {
          "question": "127-1-4",
          "items": [
            "균형성과기록표(Balanced Score Card)의 구성요소"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "128-1-2",
          "items": [
            "IT-ROI 투자 성과평가 모델에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "129-4-5",
          "items": [
            "프로세스",
            "프레임워크",
            "분석 방법론"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "analytic-hierarchy-process",
      "title": "AHP 계층분석 의사결정",
      "domain": "IT전략·의사결정",
      "aliases": [
        "Analytic Hierarchy Process",
        "계층분석법"
      ],
      "related_terms": [],
      "easy": "평가 기준을 나누고 두 개씩 비교해 상대 중요도를 구한 뒤, 대안의 종합 우선순위를 계산합니다.",
      "definition": "AHP는 목표-기준/하위기준-대안의 계층을 만들고 쌍대비교 판단으로 우선순위 가중치를 도출·종합하는 다기준 의사결정 방법입니다.",
      "principles": [
        "먼저 목표와 비교 가능한 대안, 중복되지 않는 평가기준을 정합니다. 각 계층의 요소를 바로 위 기준에 대해 쌍대비교하여 aij>0, aji=1/aij, aii=1인 행렬을 구성합니다. 전형적으로1~9 중요도 척도를 사용하지만 숫자의 의미를 평가자에게 설명해야 합니다.",
        "가중치는 주고유벡터를 정규화하거나 기하평균 근사로 구할 수 있습니다. 일관성은 A가중치와 고유값에 기반한 CI=(λmax−n)/(n−1), CR=CI/RI로 평가합니다. 통상0.1 기준을 쓰지만 이는 맥락과 지침을 밝혀 사용하며 모든 판단의 진실성을 보장하지 않습니다.",
        "각 기준에서 대안의 국지 가중치를 구하고 상위 기준 가중치와 곱해 합산하여 전체 우선순위를 만듭니다. 평가자가 여러 명이면 판단을 어떻게 통합했는지 밝히고 결과의 민감도를 점검합니다.",
        "장점은 정성·정량의 구조화, 판단의 투명성·일관성 점검이고 한계는 주관성·쌍대비교 부담 n(n−1)/2, 기준 중복·의존, 대안 추가에 따른 순위 변화 가능성입니다. 결과는 의사결정 지원이며 책임 있는 선택을 대체하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "가중치 산정",
            "쌍대비교→우선순위",
            "기준 중요도와 대안 성능 구분"
          ],
          [
            "일관성",
            "판단 간 모순 정도",
            "낮은 CR도 잘못된 기준을 고치지 못함"
          ],
          [
            "민감도",
            "가중치 변화의 순위 영향",
            "불안정한 선택·핵심 가정 확인"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 클라우드 A/B 선택",
        "input": "기준 비용/안정성 가중치가0.4/0.6, 대안 A의 국지가중치0.7/0.3, B는0.3/0.7입니다.",
        "steps": [
          "A=0.4×0.7+0.6×0.3=0.46을 계산합니다.",
          "B=0.4×0.3+0.6×0.7=0.54로 이 조건에서는B가 높습니다.",
          "비용 중요도가 커질 때 순위가 바뀌는지 민감도를 검토합니다."
        ],
        "result": "어떤 기준·판단 때문에 결론이 나왔는지 설명할 수 있습니다.",
        "caution": "가중치는 창작 값이며 실제 공급자의 우열이나 품질을 뜻하지 않습니다."
      },
      "answer_outline": [
        "계층·쌍대비교·역수행렬",
        "가중치·CI/CR와 종합",
        "장단점·민감도·계산 예"
      ],
      "pitfalls": [
        "CR을 실제 정답 확률로 해석하지 않습니다.",
        "중복 기준으로 같은 장점을 두 번 가중하지 않습니다."
      ],
      "recall": [
        "n개 기준 쌍대비교 횟수는 얼마입니까?",
        "국지 가중치와 종합 가중치의 차이는 무엇입니까?",
        "판단이 일관돼도 결론이 잘못될 수 있는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-ahp"
      ],
      "validation": "부분 확인",
      "version_note": "Saaty 원 논문 초록의 쌍대비교·합성 원리는 확인했습니다. CI/CR 전체 유도·RI표·척도 규칙은 원 논문 본문 추가 대조가 필요합니다.",
      "requirements": [
        {
          "question": "130-1-11",
          "items": [
            "AHP(Analytic Hierarchy Process) 기법"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "it-service-management",
      "title": "ITSM과 서비스 설계·구축·전환",
      "domain": "IT서비스관리",
      "aliases": [],
      "related_terms": [],
      "easy": "서비스 관리의 대상은 서버 한 대가 아니라 고객이 받는 서비스의 전체 수명주기입니다.",
      "definition": "ITSM은 고객에게 가치를 제공하도록 서비스의 계획·설계·구축·전환·제공·개선을 관리하는 활동이며 ISO/IEC20000-1은 서비스관리시스템(SMS)의 수립·운영·개선 요구사항을 규정합니다.",
      "principles": [
        "SMS는 조직 맥락·리더십·계획·지원·운영·성과평가·개선을 통해 역할·정책·프로세스·정보·자원을 연결합니다. 서비스 포트폴리오·계약·공급자·수요/용량·가용성/연속성·구성/변경·사고/문제·보안·측정의 상호작용을 관리합니다.",
        "설계는 고객/서비스 요구·품질·제약·위험·역할·지원시간·비용·SLA·보안·연속성·용량·공급자와 인수기준을 구체화합니다. 새 서비스와 변경 서비스가 기존 서비스에 미칠 영향도 평가합니다.",
        "구축은 요구에 맞는 인프라·응용·절차·조직·문서·지원체계를 준비하고 시험·검증·결함 조치를 수행합니다. 구성·변경관리와 연결해 승인된 상태·버전을 유지하며 운영인력의 교육과 지원도 포함합니다.",
        "전환은 준비도·인수기준을 확인하고 배포·릴리스·이관·롤백·초기 안정화·운영 인계와 결과 평가를 수행합니다. 이후 합의 수준을 모니터링해 사고는 서비스 복구, 문제관리는 근본원인·재발방지, 지속 개선은 지표와 고객 경험의 개선으로 연결합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "설계",
            "서비스가 만족할 요구와 운영방식",
            "SLA·지원·보안·용량·인수기준"
          ],
          [
            "구축",
            "기술·절차·조직과 검증",
            "시험·형상·교육·문서"
          ],
          [
            "전환",
            "운영으로 안전하게 이동",
            "배포·이관·롤백·안정화·인수"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 전자상거래 서비스 운영 인수",
        "input": "개발팀이 완성한 주문 서비스를 운영팀에 넘깁니다.",
        "steps": [
          "결제·주문·재고의 지원범위와 장애 우선순위·SLA를 설계합니다.",
          "모니터링·운영 절차·복구·헬프데스크를 구축하고 교육합니다.",
          "전환 리허설·롤백·인수기준을 확인한 후 초기 안정화 결과를 평가합니다."
        ],
        "result": "운영 인수에서 기술 구축과 서비스 준비를 함께 확인합니다.",
        "caution": "ISO20000-1 유료 세부 조문 전체는 미열람으로 규범적 필수사항 목록과 정확히 같다고 주장하지 않습니다."
      },
      "answer_outline": [
        "ITSM·SMS 개념과 목적",
        "서비스 설계·구축·전환 활동",
        "서비스 운영·평가·개선 연결"
      ],
      "pitfalls": [
        "ITIL은 실무 프레임워크, ISO20000-1은 SMS 요구사항이라는 범위를 구분합니다.",
        "장애 복구와 근본원인 제거를 같은 활동으로 축소하지 않습니다."
      ],
      "recall": [
        "서비스 설계에서 기술 외에 정할 것은 무엇입니까?",
        "운영 인수에서 롤백을 확인해야 하는 이유는 무엇입니까?",
        "사고관리와 문제관리의 목적 차이는 무엇입니까?"
      ],
      "source_ids": [
        "sb-itsm",
        "sb-audit2023"
      ],
      "validation": "부분 확인",
      "version_note": "ISO/IEC20000-1:2018 공식 초록·수명주기 범위와 NIA 운영 가이드 확인. §8.5 등의 세부 요구사항 전체 대조는 필요합니다.",
      "requirements": [
        {
          "question": "133-2-3",
          "items": [
            "ISO/IEC 20000에서 제시하는 기준을 중심으로, 정보기술 서비스 관리체계(ITSM)의 개념을 설명하고, 이 시스템의 서비스 설계 및 구축, 전환을 위한 활동에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "service-level-agreement-financial-cloud",
      "title": "SLA 지표·측정·금융 클라우드",
      "domain": "IT서비스관리",
      "aliases": [],
      "related_terms": [],
      "easy": "좋은 SLA는 높은 숫자만 적는 계약이 아니라, 무엇을 어느 구간에서 누가 어떻게 측정하고 미달 때 무엇을 할지 정합니다.",
      "definition": "SLA는 서비스 제공자와 이용자가 서비스 범위·역할·수준·측정·보고·미달 조치와 변경을 합의하는 약정입니다. 클라우드는 서비스 모델별 책임과 외부 의존·데이터 종료를 함께 다룹니다.",
      "principles": [
        "구성은 서비스·적용대상/기간·지원시간·역할·정의, 지표·목표/최소수준·측정원·주기·제외조건·가중치, 보고·검토·개선, 위약/보상·분쟁·변경·종료입니다. 요구분석→지표/수준 협의→계약→측정/보고→평가/개선→갱신 절차로 운영합니다.",
        "전자상거래의 HW는 가용성·CPU/메모리·복구시간, SW는 결제성공·주문처리 지연·오류율·배포실패, 네트워크는 지연·손실·대역폭·가용성을 측정할 수 있습니다. 자원 지표와 고객이 보는 업무 성공을 함께 측정해야 합니다.",
        "가용률=(약정서비스시간−산정장애시간)/약정서비스시간×100이며 장애 시작/종료·부분 장애·계획정지·고객귀책·중복 장애·측정 실패를 정의해야 합니다. 평균만으로 장시간·반복 장애나 꼬리 지연이 가려지지 않게 보호 지표를 둡니다.",
        "금융 클라우드에서는 업무 중요도·CSP 위험·보안/연속성 평가, 위탁/재위탁·감사권·접근/통제·사고 통지·데이터 위치/반환/파기·출구전략을 계약에 반영합니다. 2025 금융보안원 가이드는2025.2.5 시행 감독규정을 반영하므로130회 당시 절차와 보고기한을 혼합하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "서비스 지표",
            "응답·성공·가용성",
            "고객 체감 결과"
          ],
          [
            "운영 지표",
            "자원·작업·복구·요청",
            "문제 원인과 개선 관리"
          ],
          [
            "금융 클라우드",
            "감사·연속성·데이터/위탁 통제",
            "책임분담·종료·규제 반영"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 월 가용률 산술",
        "input": "30일24시간 서비스, 산정 대상 장애60분입니다.",
        "steps": [
          "약정시간43200분을 계산합니다.",
          "가용률=(43200−60)/43200×100≈99.8611%입니다.",
          "제외조건·장애 중복과 실제 결제 영향에 따라 산정 근거를 검토합니다."
        ],
        "result": "분모와 산정범위를 명확히 하는 연습입니다.",
        "caution": "예시는 특정 공공/금융 SLA의 목표나 위약금 기준이 아닙니다."
      },
      "answer_outline": [
        "SLA 구성·수립 절차",
        "HW/SW/망 지표·측정 사례",
        "클라우드·금융 통제·가용률 계산"
      ],
      "pitfalls": [
        "RTO와 SLA 장애조치시간을 자동으로 같은 값이라 보지 않습니다.",
        "제공자 가용률 합의가 고객 전체 업무 가용성을 보장하지 않습니다."
      ],
      "recall": [
        "가용률 산정의 분모를 어떻게 정의합니까?",
        "전자상거래 SW 지표로 결제성공을 보는 이유는 무엇입니까?",
        "출구전략에서 데이터 반환 외에 무엇을 확인합니까?"
      ],
      "source_ids": [
        "sb-sla",
        "sb-cloudsla",
        "sb-audit2023"
      ],
      "validation": "부분 확인",
      "version_note": "일반 SLA 공식 표준 적용범위·운영 가이드는 확인. 금융2025 공식 배포는 확인했고 세부 원문 대조 중이며130회 당시 금융 가이드와의 차이는 추가 확인 필요합니다.",
      "requirements": [
        {
          "question": "137-2-2",
          "items": [
            "SLA(Service Level Agreement) 구성요소와 절차",
            "(A)기업의 특성을 고려하여 하드웨어, 소프트웨어, 네트워크 영역별 SLA 평가지표와 측정방법에 대한 사례"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "130-3-6",
          "items": [
            "SLA의 개념",
            "클라우드 SLA 가이드",
            "금융 클라우드 SLA 가이드"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "digital-transformation-ax-coe",
      "title": "DX·AX·CoE와 전략적 추진",
      "domain": "IT전략·경영",
      "aliases": [],
      "related_terms": [],
      "easy": "기술을 추가하는 것보다 어떤 업무 성과와 책임 구조를 바꿀지부터 정해야 전환이 됩니다.",
      "definition": "디지털 전환은 디지털 기술·데이터로 고객 가치·업무·운영·사업모델을 재구성하는 변화이며 AX는 AI를 그 변화의 핵심 수단으로 사용하는 접근입니다. CoE는 전문 역량·표준·지원·지식을 조직에 확산하는 기능입니다.",
      "principles": [
        "고려사항은 경영목표·고객 문제·업무 프로세스·데이터·기술/레거시·조직/역량·규제/신뢰·경제성입니다. 단순 시스템 교체와 성과/사업모델 변화는 구분하며 경영 후원·현업 소유자·측정 기준을 확보합니다.",
        "추진은 비전/성과기준→현황·성숙도·문제 분석→가치·위험·실현성 기반 유스케이스/포트폴리오→데이터/아키텍처/조직 준비→PoC·시범→확대·변화관리→성과·위험 지속 점검으로 설계합니다. PoC의 모델 정확도만으로 운영 도입을 승인하지 않습니다.",
        "CoE는 재사용 플랫폼·데이터/기술 표준·참조 아키텍처·도구, 전문가 자문·교육·커뮤니티, 실험·평가·확대 지원, 거버넌스·위험/비용 가시성·성과 확산을 맡습니다. 모든 의사결정을 중앙에 몰아 현업의 책임과 속도를 약화하지 않도록 역할을 정합니다.",
        "AX 장애 요인은 데이터 품질/접근 부족→책임·품질·권한 정비, 레거시/통합 난이도→API·점진 전환, 역량·변화 저항→현업 참여·재교육·역할설계, 신뢰/법적 위험→평가·인간 감독·모니터링, 수익성 불명확→기준선·대조·총비용 검증으로 대응합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "디지털화",
            "기존 정보·절차의 전산화",
            "개별 작업 효율"
          ],
          [
            "DX/AX",
            "가치·업무·모델의 재구성",
            "기술+조직+책임+성과"
          ],
          [
            "CoE",
            "전문성·공통 자산·정책 지원",
            "현업 소유권과 균형"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 콜센터 AI 전환",
        "input": "상담원이 문서 탐색에 시간을 쓰고 예외 민원 판단이 어렵습니다.",
        "steps": [
          "탐색·분류·최종 판단을 나눠 AI지원과 인간책임 범위를 정합니다.",
          "CoE가 문서 품질·평가셋·공통 검색/계측을 지원합니다.",
          "시범에서 처리시간·정확한 해결·재문의·오류·비용을 검증한 뒤 확장합니다."
        ],
        "result": "기술 성능을 실제 업무 변화와 연결하는 실행안이 됩니다.",
        "caution": "기대효과는 가설이며 실제 시간 절감·인력 감축 성과를 창작하지 않습니다."
      },
      "answer_outline": [
        "DX/AX 개념·필요성",
        "전략적 단계·CoE 역할",
        "장애요인3개 이상·대응·검증"
      ],
      "pitfalls": [
        "자동화율만 높이고 고객 문제를 악화시키는 전환을 피합니다.",
        "PoC 성공을 전체 조직 확장 성공으로 간주하지 않습니다."
      ],
      "recall": [
        "CoE와 현업의 책임을 어떻게 나눕니까?",
        "AX에서 모델 정확도 외에 측정할 지표는 무엇입니까?",
        "변화 저항을 교육만으로 해결하기 어려운 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-coe",
        "sb-isp",
        "sb-cobit"
      ],
      "validation": "부분 확인",
      "version_note": "공식 CoE 제품 문서와 공통 계획/거버넌스 원리에 근거한 강사 종합입니다. AX는 단일 표준화 방법론의 공식 단계가 아닙니다.",
      "requirements": [
        {
          "question": "128-2-5",
          "items": [
            "디지털 혁신을 위한 고려사항과 CoE(Center of Excellence)의 역할에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "131-1-1",
          "items": [
            "디지털 트랜스포메이션(Digital Transformation)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "136-3-2",
          "items": [
            "기업에서 AX가 중요한 이유",
            "기업에서 AX를 성공적으로 추진하기 위한 전략적 추진 절차와 고려사항",
            "기업이 AX를 추진할 때 발생 가능한 장애 요인 3가지 이상과 각 대응방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "strategic-enterprise-management",
      "title": "SEM 전략적 기업경영",
      "domain": "경영·IT전략",
      "aliases": [],
      "related_terms": [],
      "easy": "전략을 발표하는 데서 끝내지 않고 계획·예산·성과·피드백의 반복 과정에 연결합니다.",
      "definition": "SEM은 기업 전략을 경영계획·자원배분·실행·성과 측정·이해관계자 소통과 통합하여 편익과 가치를 관리하는 접근입니다. ERP의 일상 실행 데이터를 전략 의사결정과 양방향으로 연결합니다.",
      "principles": [
        "고전 SAP SEM 구성은 BPS(사업계획·시뮬레이션), BIC(사업정보 수집), BCS(연결/통합), CPM(전사성과 모니터), SRM(이해관계자 관계관리)입니다. 데이터웨어하우스 기반으로 공통 지표·다차원 분석·계획/실적 비교를 지원합니다.",
        "BPS는 목표·사업 시나리오와 예산/자원을 연결하고 BIC는 내외부 정보를 수집합니다. BCS는 조직 단위별 정보를 연결·조정하며 CPM은 BSC·KPI·경영 조종석으로 전략 이행을 관찰합니다. SRM은 임직원·투자자·파트너 등 이해관계자에게 전략과 결과를 전달하고 피드백을 받습니다.",
        "구축은 비전·전략·가치동인·목표 정의→전략지도·BSC·KPI와 책임·데이터 정의→ERP/외부 데이터 통합과 품질·지표 거버넌스→계획·예산·시뮬레이션→성과 모니터/보고→변경·피드백·보상/업무 정착으로 추진할 수 있습니다.",
        "기술만 구축하면 KPI가 부서별로 달라지고 목표 조작·측정 편향이 생길 수 있습니다. 선행/후행 지표와 목표 간 가설을 검증하고 정량·정성 정보를 함께 봅니다. 전략의 인과관계는 전략지도 화살표만으로 증명되지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "ERP",
            "업무 거래의 수평 통합·실행",
            "일상 운영의 정확성·통제"
          ],
          [
            "SEM",
            "전략·계획·성과의 수직 연결",
            "편익·자원배분·학습"
          ],
          [
            "BSC",
            "4관점 목표·지표·과제",
            "SEM을 지원하는 성과관리 틀"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 서비스 기업의 고객 이탈 관리",
        "input": "매출 목표만 있고 이탈의 원인·담당자가 불명확합니다.",
        "steps": [
          "재무·고객·처리품질·직원역량의 전략 가설과 KPI를 정합니다.",
          "운영 거래·상담 데이터와 계획·예산을 연결합니다.",
          "이탈 변화와 실제 서비스 개선 활동을 비교하고 전략·자원을 조정합니다."
        ],
        "result": "성과 보고를 사후 숫자 집계에서 실행·학습 체계로 연결합니다.",
        "caution": "고전 SAP 구성은 개념 설명의 예이며 최신 제품 기능·지원 현황을 뜻하지 않습니다."
      },
      "answer_outline": [
        "SEM 정의·ERP/BSC 관계",
        "고전5구성요소와 역할",
        "구축 절차·데이터/지표·변화관리"
      ],
      "pitfalls": [
        "SEM-SRM을 공급자관계관리 제품의 SRM과 문맥 없이 혼동하지 않습니다.",
        "KPI 달성이 기업가치 전체를 대변한다고 보지 않습니다."
      ],
      "recall": [
        "BPS와 CPM의 역할 차이는 무엇입니까?",
        "전략지도와 실제 인과 검증의 차이는 무엇입니까?",
        "공통 지표 정의가 없는 SEM의 위험은 무엇입니까?"
      ],
      "source_ids": [
        "sb-sem",
        "sb-bsc"
      ],
      "validation": "출처 확인",
      "version_note": "고전 개념의 설명이며 2026-11-05 열람 원문을 기준으로 했습니다.",
      "requirements": [
        {
          "question": "131-4-1",
          "items": [
            "전략적 기업경영의 정의",
            "전략적 기업경영의 구성요소",
            "전략적 기업경영의 구축 방안 및 구축 절차"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "business-environment-analysis",
      "title": "SWOT·3C·PEST 경영환경 분석",
      "domain": "경영·전략",
      "aliases": [],
      "related_terms": [],
      "easy": "거시 환경과 시장 경쟁·고객, 내부 역량을 구분해 수집한 뒤 실제 전략 선택으로 연결합니다.",
      "definition": "SWOT은 내부 강점/약점과 외부 기회/위협을 통합하고, 3C는 고객·경쟁자·자사의 상대적 위치를, PEST는 정치/제도·경제·사회·기술의 거시 변화를 분석하는 틀입니다.",
      "principles": [
        "PEST는 정책·규제/정치, 금리·소득·경기, 인구·가치관·이용행태, 기술성숙·대체기술을 조사하여 산업/사업에 미치는 기회·위협을 도출합니다. 환경·법률을 분리한 PESTEL과 분류가 다르지만 대상과 기간·지리 범위를 먼저 정해야 합니다.",
        "3C는 고객의 과업·세분시장·지불의사·전환비용, 경쟁사의 대체가치·가격·채널·역량, 자사의 자원·브랜드·원가·실행능력을 비교해 차별화 가능한 고객 가치를 찾습니다. 경쟁사를 현재 같은 제품만 만드는 기업으로 한정하면 대체재를 놓칠 수 있습니다.",
        "SWOT의 강/약은 경쟁기준과 내부 증거로, 기회/위협은 외부 변화로 구분합니다. SO는 강점으로 기회 활용, ST는 강점으로 위협 대응, WO는 기회와 결합해 약점 보완, WT는 노출·손실을 줄이는 선택으로 구체화합니다.",
        "적용 조건은 의사결정 질문·시장 경계·기간·자료 신뢰성이 명확한 경우입니다. 다수 요인을 적는 것으로 끝내지 말고 중요도·불확실성·변화 방향·행동·책임·측정지표를 연결합니다. 예측 가능한 사실과 가설을 구분하고 새 정보가 오면 갱신합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "PEST",
            "거시 환경 변화",
            "산업·시장 경계 이전의 외부 요인"
          ],
          [
            "3C",
            "고객·경쟁·자사 관계",
            "경쟁우위·목표 고객 선택"
          ],
          [
            "SWOT",
            "내외부 요인 통합·전략화",
            "SO/ST/WO/WT의 행동 도출"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 공공 문서 검색 서비스 진입",
        "input": "자사는 한국어 검색 기술이 있으나 영업망은 작습니다.",
        "steps": [
          "PEST로 공공 조달·AI 정책·보안 제약·기술 변화를 조사합니다.",
          "3C로 사용자 과업·기존 솔루션·자사 강점을 비교합니다.",
          "SWOT에서 파트너와의 영업 협력을 WO 대안으로 도출하고 실험합니다."
        ],
        "result": "분석 틀마다 다른 질문을 맡겨 전략의 근거를 연결합니다.",
        "caution": "시장 크기·고객 의사·정책 효과는 실제 조사 없이 확정하지 않습니다."
      },
      "answer_outline": [
        "세 기법 정의·특성",
        "적용 조건·분석 절차",
        "결과 통합과 전략 대안 사례"
      ],
      "pitfalls": [
        "자사 약점을 외부 위협으로 중복 분류하지 않습니다.",
        "SWOT 네 칸이 자동으로 실행 우선순위를 정하지 않습니다."
      ],
      "recall": [
        "3C와 PEST의 분석 범위 차이는 무엇입니까?",
        "WO전략의 예를 만드십시오.",
        "분석 자료의 기간을 고정해야 하는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-strategy",
        "sb-isp"
      ],
      "validation": "부분 확인",
      "version_note": "공개 대학 교재의 거시환경·SWOT 연결 확인. 3C 원저 전체는 미열람이며 그 구성을 일반 경영분석 관행으로 설명했습니다.",
      "requirements": [
        {
          "question": "133-3-4",
          "items": [
            "경영환경을 분석하는 방법인 SWOT(Strengths, Weaknesses, Opportunities, Threats), 3C(Customer, Competitor, Company), PEST(Political, Economical, Social, Technological) 분석에 대하여 각 방법의 특성과 적용을 위한 조건, 그리고 분석 방법에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "technology-acceptance-model",
      "title": "TAM 기술수용모델",
      "domain": "경영·정보시스템",
      "aliases": [
        "Technology Acceptance Model",
        "기술수용모형"
      ],
      "related_terms": [],
      "easy": "사용자가 기술을 유용하고 사용하기 쉽다고 느끼는지가 이용 의도와 행동에 어떻게 연결되는지 설명하는 모형입니다.",
      "definition": "TAM은 지각된 유용성(PU)과 지각된 사용용이성(PEOU) 등 사용자의 믿음으로 기술 이용 수용을 설명하는 정보시스템 연구 모형입니다.",
      "principles": [
        "지각된 유용성은 기술이 자신의 업무 성과를 개선할 것이라는 믿음이며 사용용이성은 사용하는 데 큰 노력이 들지 않을 것이라는 믿음입니다. 제품의 객관적 성능과 사용자의 지각은 다를 수 있으므로 둘을 혼동하지 않습니다.",
        "고전 모형은 외부 요인→PU/PEOU→사용 태도→이용 의도→실제 사용의 관계를 설명하며 PEOU가 PU에도 영향을 줄 수 있습니다. 연구 판본에 따라 태도·직접 경로·외부 요인이 다르므로 단일 화살표를 모든 TAM 연구의 확정 구조로 일반화하지 않습니다.",
        "적용은 대상 사용자·업무·기술과 기간 정의→검증된 문항의 맥락 조정→설문·행동 자료 수집→신뢰도·타당도·관계 분석→기능·교육·UX 개선→후속 행동 검증으로 진행할 수 있습니다. 상관이나 자기보고 의도만으로 실제 사용의 인과를 확정하지 않습니다.",
        "유용성 개선은 업무 관련 기능·출력 품질·결과 가시성을, 용이성 개선은 학습·탐색·조작·오류 복구와 지원을 다룹니다. 규제·강제사용·사회적 영향·신뢰·접근성·지원환경 등 모형 밖의 요인도 필요에 따라 고려합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "PU",
            "성과·문제해결에 도움이 된다는 믿음",
            "업무 적합·출력 품질"
          ],
          [
            "PEOU",
            "배우고 쓰기 쉽다는 믿음",
            "조작·학습·오류복구"
          ],
          [
            "의도/행동",
            "쓸 생각 / 실제 사용",
            "설문과 로그의 차이·시간차"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 직원 지식검색 도구 수용",
        "input": "도구 접속은 많으나 반복 이용이 적습니다.",
        "steps": [
          "사용자가 원하는 문서를 찾는지(PU)와 검색·필터가 쉬운지(PEOU)를 구분해 조사합니다.",
          "검색 정확도·용어·동선과 교육을 개선합니다.",
          "설문 변화와 실제 재방문·업무완료 로그를 함께 비교합니다."
        ],
        "result": "낮은 수용을 단순 교육 부족이라고 가정하지 않고 원인을 나눌 수 있습니다.",
        "caution": "창작 예시이며 설문 점수나 실제 인과효과는 측정 전 확정하지 않습니다."
      },
      "answer_outline": [
        "TAM 정의·PU/PEOU",
        "태도·의도·행동의 관계",
        "활용 절차·한계·개선 사례"
      ],
      "pitfalls": [
        "TAM을 시장규모의 TAM(Total Addressable Market)과 혼동하지 않습니다.",
        "지각된 유용성을 객관적 정확도와 같은 값으로 보지 않습니다."
      ],
      "recall": [
        "PU와 PEOU를 다른 문항으로 측정하는 이유는 무엇입니까?",
        "이용 의도와 실제 사용이 다른 예를 드십시오.",
        "강제사용 환경에서 해석할 주의점은 무엇입니까?"
      ],
      "source_ids": [
        "sb-tam"
      ],
      "validation": "부분 확인",
      "version_note": "Davis1989 원 논문 초록에서 두 지각변수와 검증 취지를 확인. 전체 모형의 판본별 경로·문항 전문은 추가 확인 대상입니다.",
      "requirements": [
        {
          "question": "133-1-6",
          "items": [
            "기술수용모델(Technology Acceptance Model; TAM)의 개념과 주요 구성요소에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "market-size-white-label",
      "title": "TAM·SAM·SOM과 화이트레이블 마케팅",
      "domain": "경영·사업모델",
      "aliases": [],
      "related_terms": [
        "TAM-SAM-SOM",
        "화이트 레이블 마케팅"
      ],
      "easy": "시장 전체의 크기와 우리 회사가 실제 서비스할 수 있고 확보할 수 있는 범위를 순서대로 좁힙니다.",
      "definition": "시장규모의 TAM은 전체 해결 가능한 수요, SAM은 제품·지역·채널·규제 조건상 서비스 가능한 부분, SOM은 자원·경쟁·기간을 고려해 확보 가능한 부분입니다. 화이트레이블은 다른 제공자가 만든 제품/서비스를 자기 브랜드로 제공하는 사업 방식입니다.",
      "principles": [
        "TAM은 고객 수×연간 고객당 수익 등으로 단위를 맞추고 시장의 문제·고객·기간·지역을 정의합니다. SAM은 언어·제품 기능·지역·규제·서비스 능력으로 범위를 줄이며 SOM은 판매채널·영업주기·전환율·공급능력·경쟁 점유를 근거로 추정합니다.",
        "하향식은 공신력 있는 시장 통계에서 조건을 좁히고, 상향식은 실제 고객 세그먼트·계약가·도달/전환 능력을 합산합니다. 두 접근을 대조하고 가격·고객수·확보 시나리오에 민감도를 적용합니다. SOM을 TAM의 임의1%로 놓는 것은 근거가 약합니다.",
        "화이트레이블 마케팅 서비스는 공급자가 광고·콘텐츠·분석 등 실행을 제공하고 판매사가 자신의 브랜드와 고객관계를 유지하는 방식입니다. 직접 개발 부담과 출시시간을 줄일 수 있으나 차별화·품질 통제·마진·공급자 종속·고객 데이터·지식재산권·재판매 범위 위험이 있습니다.",
        "적용 시 브랜드 표시·재판매 권한·책임·SLA·데이터 처리·지원/에스컬레이션·계약 종료와 이전을 정합니다. OEM/ODM·단순 제휴/리셀러와의 경계는 계약에 따라 달라 이름만 보고 동일한 법적 관계로 판단하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "TAM",
            "문제 전체의 이론적 수요",
            "총 잠재 고객·단위 수익"
          ],
          [
            "SAM/SOM",
            "서비스 가능 / 실제 확보 가능",
            "제품·지역 제약 / 자원·경쟁·기간"
          ],
          [
            "화이트레이블",
            "타사 실행·제품을 자기 브랜드로",
            "출시 편의와 통제/차별화의 절충"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 중소기업 분석서비스 시장 산술",
        "input": "전체 고객10만, 서비스 가능2만,3년 내 확보200개, 연간 계약100만원 가정입니다.",
        "steps": [
          "TAM1000억원, SAM200억원, SOM2억원을 연간 매출 기회로 계산합니다.",
          "실제 확보200개가 영업능력·전환율에 맞는지 검증합니다.",
          "분석 엔진을 화이트레이블로 제공받는다면 원가·품질·데이터·재판매 계약을 추가 검토합니다."
        ],
        "result": "범위·단위·확보근거와 사업모델 통제를 함께 설명합니다.",
        "caution": "시장과 계약가는 모두 창작 가정이며 기업가치나 실제 시장 통계가 아닙니다."
      },
      "answer_outline": [
        "세 시장 범위·산정 절차",
        "상/하향식·민감도",
        "화이트레이블 개념·장단점·계약"
      ],
      "pitfalls": [
        "기술수용모델TAM과 시장TAM은 다른 약어입니다.",
        "SOM을 매출 목표와 근거 없이 같게 만들지 않습니다."
      ],
      "recall": [
        "SAM이TAM보다 작아지는 이유는 무엇입니까?",
        "SOM의 영업능력 근거는 어떻게 만듭니까?",
        "화이트레이블에서 고객지원 책임을 왜 명확히 합의합니까?"
      ],
      "source_ids": [
        "sb-market",
        "sb-whitelabel"
      ],
      "validation": "부분 확인",
      "version_note": "ITU 공개자료와 실제 제공자의 사업방식 설명 확인. 화이트레이블의 일반 용어 경계는 계약별 차이를 명시했습니다.",
      "requirements": [
        {
          "question": "134-1-2",
          "items": [
            "시장 규모 추정 방법인 TAM-SAM-SOM(Total Addressable Market-Serviceable Addressable Market-Serviceable Obtainable Market) 프레임워크"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "136-1-1",
          "items": [
            "화이트 레이블 마케팅(White Label Marketing)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "public-sector-service-level-agreement",
      "title": "공공 SLA 표준안·시스템 등급별 적용",
      "domain": "IT서비스관리·전자정부",
      "aliases": [],
      "related_terms": [],
      "easy": "중요 공공서비스의 운영 품질을 같은 지표로 약속하고, 목표 미달·장애 지연에 대한 책임을 계약으로 연결합니다.",
      "definition": "공공 SLA는 행정·공공기관과 운영·유지관리 사업자가 서비스 수준, 책임과 의무를 합의하는 협약입니다. 유사한 영향도의 시스템마다 다른 운영 수준·협약 부재를 개선하려는 표준입니다.",
      "principles": [
        "등급 분류는 국민 생명·안전, 사회·경제 파급과 업무 중요도에 따른 영향도를 고려하는 체계로 이해하되, 정량 분류표·산정점수·예외는 현행 별도 기준을 확인해야 합니다. 표준안의 종합지표는1·2등급 필수,3·4등급 권고이며 장애조치 최대허용시간은 전체 등급 필수, 제재금은1·2 필수·3·4 권고로 구분됩니다.",
        "2025 첨부표의 가용률 목표는1·2등급100%,3·4등급99.98%, 최소허용은 순서대로99.92/99.90/99.88/99.85%입니다. 가용률은 종합평가 비중30% 이상, 장애건수·평균장애시간·변경절차 준수율 등22개 선택지표는70% 이하로 구성합니다. 목표와 최소허용 수준을 혼동하지 않습니다.",
        "종합점수95~100미만 탁월,90~95미만 우수,85~90미만 보통,80~85미만 미흡,80미만 불량이며 월 위약금은 미흡10%, 불량20%입니다. 연평가 탁월/우수/보통의 누적 위약금 면제는100/75/50%, 미흡·불량은 전액 부과라는 보상 구조입니다.",
        "개별 장애등급1/2/3/4의 최대허용시간은120/180/300/480분, 초과 제재금은 분당 계약금액×초과분×가중치2.5/1.7/1/0.6입니다. 시스템 등급과 개별 장애등급을 구분하고 측정시간·제외시간·장애시작/복구·책임귀속·자료확정·중복제재·복구 검증을 계약에 명시해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "종합서비스",
            "가용률 필수+선택지표",
            "월평가 위약금·연평가 감면"
          ],
          [
            "개별서비스",
            "등급별 장애조치 허용시간",
            "초과 지체분의 제재금"
          ],
          [
            "시스템/장애등급",
            "서비스 중요도 / 해당 장애 영향",
            "서로 다른 분류와 측정근거 확인"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 지연 장애의 제재금 산술",
        "input": "분당 계약금액100원,1등급 장애 조치150분을 가정합니다.",
        "steps": [
          "허용120분을 빼 지체30분을 구합니다.",
          "100×30×2.5=7,500원으로 예시 제재금을 계산합니다.",
          "월 종합평가 위약금과의 관계·책임귀속·감면 조항은 실제 계약으로 확인합니다."
        ],
        "result": "허용시간과 전체 장애시간을 혼동하지 않고 제재금을 계산합니다.",
        "caution": "창작 계약값입니다. 표준안 발표만으로 특정 기관 계약에 자동 부과하거나2027 시행 완료라고 단정하지 않습니다."
      },
      "answer_outline": [
        "도입 필요·개념",
        "시스템 등급·종합/개별 적용",
        "수치·산식·측정/계약 고려"
      ],
      "pitfalls": [
        "1등급 최소99.92%를 목표100% 대신 쓰지 않습니다.",
        "표준안의 계획과 법률의 현행 효력을 분리합니다."
      ],
      "recall": [
        "시스템 등급과 장애등급의 차이는 무엇입니까?",
        "종합 위약금과 개별 제재금의 계산기준은 무엇입니까?",
        "가용률 계산에서 합의할 시간 범위는 무엇입니까?"
      ],
      "source_ids": [
        "sb-publicsla"
      ],
      "validation": "부분 확인",
      "version_note": "2025-08-28 표준안 본문·표 확인. 2026 시범·2027 의무화는 발표 당시 일정입니다. 정보시스템 등급의 정량 산정표와 법령 최종 시행 조문은 확인 필요합니다.",
      "requirements": [
        {
          "question": "139-2-5",
          "items": [
            "공공 SLA의 개념과 도입 필요성",
            "정보시스템 등급 분류 기준과 등급별 SLA 적용방식",
            "공공 SLA 표준안의 주요 내용(가용률, 장애조치 시간, 위약금 체계)과 적용 시 고려사항"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "esg-information-technology",
      "title": "ESG 경영·지표와 IT 역할",
      "domain": "경영·ESG",
      "aliases": [],
      "related_terms": [],
      "easy": "환경·사회·지배구조의 위험과 영향을 경영 의사결정에 반영하고, IT로 실행·증빙·감시합니다.",
      "definition": "ESG 경영은 환경(E), 사회(S), 지배구조(G)를 전략·운영·투자·공시에 통합해 지속가능한 가치와 책임 있는 경영을 추구하는 접근입니다. 좋은 홍보보다 실제 영향·위험·성과와 검증 가능한 데이터가 중요합니다.",
      "principles": [
        "E의 지표는 온실가스·에너지·용수·폐기물·오염/자원 사용이며 IT는 계측IoT·EMS·배출량 집계·물류/설비 최적화·제품 생애주기 추적을 지원합니다. IT자체의 전력·장비 폐기·학습/추론 자원까지 포함해 순효과와 범위를 평가합니다.",
        "S는 노동·안전·다양성·인권·공급망·고객 권리·정보보호를 다룹니다. 안전 센서·접근성·디지털 포용·공급망 추적·개인정보 권리지원으로 실현하고 사고건수·재해·교육·차별·권리구제의 실제 결과를 봅니다. K-ESG의 정보보호 시스템 구축과 개인정보 침해/구제는 사회영역의 구체 항목입니다.",
        "정보보호 구축은 책임자·정책·예산·인력·자산/위험관리→접근통제·암호·로그·탐지/대응→교육·취약점·점검을 갖추고 운영 증거를 남기는 것입니다. 개인정보 침해/구제는 최소처리·안전조치·요청/고충 창구·조사·피해 회복·재발방지를 포함하며 인증 취득만으로 침해가 없다고 보지 않습니다.",
        "G는 이사회·독립성·윤리/준법·감사·주주/이해관계자와 책임·공시를 다룹니다. IT는 권한분리·승인/감사추적·내부통제·공시 데이터의 계보/품질·협력사 실사를 지원합니다. 데이터 정의·기간·사업장 경계·책임자·증빙과 변경이력을 통제해야 그린워싱을 줄일 수 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "E",
            "자원·배출·생태 영향",
            "IoT/EMS·배출 데이터·최적화"
          ],
          [
            "S",
            "사람·안전·인권·정보권리",
            "접근성·안전·보안·피해구제"
          ],
          [
            "G",
            "책임·감독·윤리·투명성",
            "권한분리·감사추적·검증 공시"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 공급망 ESG 데이터 서비스",
        "input": "협력사마다 전력 사용량과 보안사고 보고 형식이 다릅니다.",
        "steps": [
          "지표의 단위·기간·조직경계·증빙과 책임자를 표준화합니다.",
          "전력/안전/보안 자료를 수집하고 누락·이상·변경을 검증합니다.",
          "경영 검토에서 원인·개선과제·실제 성과를 추적하고 공시 근거를 남깁니다."
        ],
        "result": "정보 수집과 실제 환경·사회 개선을 연결하는 운영 구조가 됩니다.",
        "caution": "특정 ESG 등급·점수·규제 의무·절감량은 실제 기준과 측정 없이 만들지 않습니다."
      },
      "answer_outline": [
        "ESG 정의·목표·주요지표",
        "E/S/G별 IT기여·IT자체영향",
        "정보보호 구축·침해구제·데이터 통제"
      ],
      "pitfalls": [
        "보안 시스템 구매를 사회책임 이행 완료로 쓰지 않습니다.",
        "각 평가기관 지표와 공시기준을 하나로 혼합하지 않습니다."
      ],
      "recall": [
        "IT for Green과 IT자체 환경영향을 어떻게 함께 봅니까?",
        "정보보호 구축과 개인정보 피해구제의 차이는 무엇입니까?",
        "ESG 데이터의 경계를 통일해야 하는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-kesg2",
        "sb-esg"
      ],
      "validation": "출처 확인",
      "version_note": "기출 당시 K-ESG1.0과 현재2.0(2024)을 구분합니다. 본문은 공통 원리이며 특정 상장사 공시 의무 시점·세부 법률은 별도 확인해야 합니다.",
      "requirements": [
        {
          "question": "126-2-2",
          "items": [
            "포스트 코로나 시대의 지속가능 경영전략으로 ESG(Environmental, Social and Governance) 경영이 각광받고 있다. ESG경영에서 정보기술(IT)의 역할에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "129-3-6",
          "items": [
            "정보보호 시스템 구축 측면에서의 ESG",
            "개인정보 침해 및 구제 측면에서의 ESG"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "134-2-5",
          "items": [
            "ESG 경영의 정의 및 목표",
            "ESG 경영의 주요 지표",
            "ESG 경영 목표 달성을 지원하기 위한 정보기술(IT)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "environmental-management-iso14000",
      "title": "ISO14000 계열·환경경영시스템 인증",
      "domain": "경영·ESG",
      "aliases": [],
      "related_terms": [],
      "easy": "조직의 환경 영향을 찾아 목표·운영 통제·평가·개선의 반복 체계로 관리하는 것이 환경경영시스템입니다.",
      "definition": "ISO14000은 환경경영 관련 표준 계열이며, 일반적으로 환경경영시스템 인증은 요구사항 표준 ISO14001을 기준으로 합니다. 계열 전체가 하나의 인증규격이거나 제품이 친환경임을 보증하는 제도는 아닙니다.",
      "principles": [
        "필요성은 환경 법규·이해관계자 요구의 대응, 자원·폐기물과 사고 위험의 관리, 공급망 거래·조달 요구와 지속 개선입니다. 먼저 조직의 활동·제품·서비스와 적용범위, 이해관계자·준수의무·중대한 환경측면을 파악하고 경영진의 책임과 방침을 정합니다.",
        "PDCA로 계획(영향·위험/기회·준수의무·목표와 실행계획), 실행(역량·의사소통·문서/운영 통제·비상대응), 점검(측정·준수평가·내부심사·경영검토), 개선(부적합·시정·효과 확인)을 연결합니다. 모든 문서를 두껍게 만드는 것보다 현장 활동과 증거가 일치해야 합니다.",
        "계열의 역할은14001의 인증 가능한 EMS 요구사항,14004의 실행 지침,14040/14044의 전과정평가 원칙/요구,14064 계열의 온실가스 정량화/검증 등으로 구분합니다. 각 표준의 현행 판본·적용대상과 온실가스 검증·제품라벨 인증은 별도로 확인합니다.",
        "구축·인증은 현황/갭 분석→범위·방침·역할→환경측면/준수의무·목표→운영·교육·기록→내부심사·시정·경영검토→인증기관의1단계 준비성/문서와2단계 현장심사→부적합 시정→인증·사후심사/갱신으로 접근합니다. ISO는 표준을 만들며 직접 조직 인증서를 발급하는 기관은 아닙니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "ISO14000 계열",
            "환경경영의 여러 도구·지침",
            "모두 같은 인증 대상이 아님"
          ],
          [
            "ISO14001",
            "EMS 요구사항",
            "조직의 범위 내 관리체계 인증"
          ],
          [
            "인증효과",
            "준수·위험·효율·신뢰 개선 지원",
            "무사고·무배출·성과 수치 보장 아님"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 데이터센터 환경경영 구축",
        "input": "전력·냉각수·폐배터리 영향과 책임이 분리돼 있습니다.",
        "steps": [
          "범위와 전력/물/폐기물의 기준선·준수의무·중대 측면을 정합니다.",
          "냉각·폐기물 위탁·비상 누출 대응을 통제하고 담당자를 교육합니다.",
          "측정·내부심사·경영검토로 효과와 부적합을 확인한 뒤 인증심사를 준비합니다."
        ],
        "result": "장비 구매를 넘어 지속적인 환경 성과 관리의 증거가 생깁니다.",
        "caution": "절감률·인증 통과·법규 준수 전부를 가정하지 않습니다. 인증기관별 심사계약을 확인합니다."
      },
      "answer_outline": [
        "계열·14001 개념/필요",
        "PDCA 구축·관련규격",
        "인증 절차·효과·한계"
      ],
      "pitfalls": [
        "환경경영 인증을 제품 친환경 성능 인증으로 설명하지 않습니다.",
        "2026에2015판을 최신판이라고 쓰지 않습니다."
      ],
      "recall": [
        "ISO14000과14001의 차이는 무엇입니까?",
        "환경측면과 환경영향의 연결 예를 만드십시오.",
        "인증 후에도 측정과 시정조치가 필요한 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-ems"
      ],
      "validation": "부분 확인",
      "version_note": "132회 시점 ISO14001:2015와 현행 ISO14001:2026(2026-04,4판)을 구분했습니다. ISO 공개 소개만 확인했고2026 유료 본문·조항별 변경·인증 전환 유예기간은 미확인입니다.",
      "requirements": [
        {
          "question": "132-2-5",
          "items": [
            "ISO 14000 인증의 개념과 필요성, 인증규격, 구축 및 인증절차, 인증효과를 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "oecd-digital-tax-two-pillars",
      "title": "OECD 디지털세·두 축 국제조세 개편",
      "domain": "경영·디지털정책",
      "aliases": [],
      "related_terms": [],
      "easy": "사업장이 없는 나라에서도 큰 시장 매출이 나는 문제와 국가 간 낮은 법인세 경쟁을 서로 다른 두 장치로 다룹니다.",
      "definition": "디지털세라는 통칭 아래 OECD/G20 포괄적 이행체계의 Pillar One은 시장 소재국의 과세권 배분, Pillar Two는 다국적기업의 글로벌 최저한세를 다룹니다. 온라인 기업만 대상으로 하는 단일 거래세가 아닙니다.",
      "principles": [
        "2021.10 합의의 Pillar One Amount A는 원칙적으로 매출200억유로 초과·수익성10% 초과의 대형 다국적기업 중 예외업종을 제외하고, 매출의10%를 초과하는 잔여이익의25%를 시장 소재국에 배분하는 구조였습니다. 기존 물리적 사업장 중심 과세권을 시장 참여와 연결한다는 의미가 있습니다.",
        "Pillar Two의 GloBE는 통상 연결매출7.5억유로 이상 다국적그룹의 관할국별 유효세율을15%와 비교해 부족분을 추가 과세하는 틀입니다. 소득산입규칙(IIR), 저율과세소득 규칙(UTPR), 적격 국내최저추가세(QDMTT) 등 연결 규칙의 순서·예외·세이프하버를 검토해야 하며 명목세율과 유효세율은 다릅니다.",
        "의미는 시장국 세수·공정경쟁과 조세회피/이익이전 감소에 있으나 세원 재배분, 이중과세 방지, 국가별 이해관계와 조약/국내법 전환 문제가 있습니다. 기업은 국가별 재무·세무 데이터·결합범위·조정 항목·통제와 보고시스템을 준비해야 합니다.",
        "126회 문항의2023 부과는 당시 합의의 시행 목표입니다. 이를2023부터 모든 국가에서 두 축이 전면 시행됐다고 쓰면 틀립니다. Amount A 협약과 Amount B, 글로벌 최저한세의 국가별 시행·2026 조정 상황은 서로 달라 현재 효력과 전망을 분리해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "Pillar One",
            "초대형·고수익 기업의 시장국 과세권",
            "물리적 사업장과 매출 시장의 불일치"
          ],
          [
            "Pillar Two",
            "글로벌 최저한세15% 틀",
            "관할국별 유효세율·추가세"
          ],
          [
            "도입 전망",
            "국제합의→협약/국내법·집행",
            "합의 일정과 법적 시행을 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 최저한세의 단순 원리",
        "input": "가상 관할국의 조정소득100, 대상세액10으로 단순화합니다.",
        "steps": [
          "유효세율10%를 구하고15%와 차이5%를 계산합니다.",
          "단순 부족분5를 파악하되 실질기반 소득공제·적격추가세 등 실제 조정을 확인합니다.",
          "국가별 데이터를 대사하고 어떤 규칙·법률이 적용되는지 검토합니다."
        ],
        "result": "명목 세율이나 매출에15%를 곱하는 오류를 피합니다.",
        "caution": "실제 납부세액 계산이나 세무 자문이 아닌 창작 원리 예시입니다. 예외·공제·국내법을 생략했습니다."
      },
      "answer_outline": [
        "디지털화의 과세 문제·두 축",
        "대상·Amount A/최저한세 원리",
        "의미·기업대응·당시 목표/현재 효력"
      ],
      "pitfalls": [
        "7.5억유로를 Pillar One 대상매출과 혼동하지 않습니다.",
        "15%를 디지털 매출 거래세율로 쓰지 않습니다."
      ],
      "recall": [
        "두 축은 각각 어떤 문제를 해결합니까?",
        "2023 시행 목표와 실제 시행을 왜 나눠 써야 합니까?",
        "기업의 세무 IT데이터 준비 항목은 무엇입니까?"
      ],
      "source_ids": [
        "sb-tax2021",
        "sb-taxcurrent"
      ],
      "validation": "부분 확인",
      "version_note": "2021-10-08 합의와 OECD 현행 개요를 확인했습니다. 2026-11-05 기준 각국 법령·다자협약 비준·세이프하버의 전체 현행 상태는 별도 확인 필요합니다.",
      "requirements": [
        {
          "question": "126-2-3",
          "items": [
            "최근 경제협력개발기구(OECD)에서 2023년부터 부과하기로 합의한 디지털세의 내용과 의미 및 전망에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        }
      ]
    },
    {
      "id": "un-egovernment-development-index",
      "title": "UN 전자정부 평가·EGDI",
      "domain": "IT전략·전자정부",
      "aliases": [],
      "related_terms": [],
      "easy": "온라인 서비스가 좋아도 통신 기반과 사람이 이를 이용할 역량이 부족하면 전자정부 발전이 제한됩니다.",
      "definition": "UN 전자정부 조사는 회원국의 디지털 정부 발전을 비교·지원하는 조사이며 EGDI는 온라인서비스(OSI), 통신인프라(TII), 인적자본(HCI)을 결합한 복합지수입니다. 지수는 국가의 모든 행정 품질이나 인권 수준을 그대로 대변하지 않습니다.",
      "principles": [
        "평가지수는 국가 전자정부발전 EGDI, 온라인 참여의 EPI, 지방도시 온라인서비스 LOSI 등을 구분합니다. EPI는 전자정보제공·전자협의·전자의사결정 참여를 평가하며 온라인 제공 기능과 실제 참여·영향력의 차이에 주의합니다.",
        "EGDI=(정규화 OSI+정규화 TII+정규화 HCI)/3으로 세 차원을 같은 가중치로 통합합니다. 온라인서비스는 정부 포털의 제도·기술·콘텐츠·서비스와 참여 기능을 조사하고, 통신은 연결·접속 기반, 인적자본은 교육·활용 기반의 국제 데이터를 사용합니다.",
        "평가 절차는 조사 설계/설문·다국어 포털 관찰·국제기구 통신/교육 자료 수집→하위지표 산정과 정규화→세 차원 결합→수준·국가군 분석입니다. 조사 연도와 자료 기준연도, 조사자의 관찰 범위·언어·기준 변경에 따른 한계를 밝혀야 합니다.",
        "2024는 TII에서 고정광대역 가입 지표를 제외하고 인터넷 보급의 경제성/접근성을 보완하는 변화, HCI의 전자정부 문해력 추가 등 방법론을 개편했습니다. 127회 당시2022와 현재 설명을 혼합하지 않고 비교할 때 같은 정의·시계열의 값인지 확인합니다. 순위 상승을 특정 정책의 인과 성과로 단정하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "OSI",
            "온라인서비스·기능의 조사",
            "포털 제공과 실제 이용성과 구분"
          ],
          [
            "TII",
            "통신 연결·접근 기반",
            "국제 통신통계·연도 확인"
          ],
          [
            "HCI/EPI",
            "교육·역량 / 전자참여",
            "EGDI 구성과 별도 지수를 구분"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 균형 개선의 산술",
        "input": "정규화 OSI0.9,TII0.6,HCI0.6을 가정합니다.",
        "steps": [
          "EGDI=(0.9+0.6+0.6)/3=0.7을 계산합니다.",
          "서비스 기능 추가와 접속·역량 개선의 병목을 함께 봅니다.",
          "지수와 별도로 취약계층 이용·업무완료·만족도 결과를 조사합니다."
        ],
        "result": "단일 포털의 기능 확대만으로 전체 발전을 평가하지 않습니다.",
        "caution": "창작 지수이며 실제 국가 값·순위가 아닙니다. 하위지표 정규화·방법론 변경을 생략한 예입니다."
      },
      "answer_outline": [
        "조사 개념·EGDI/EPI/LOSI",
        "세 하위지수와 계산·평가방법",
        "판본 변경·해석한계·정책 활용"
      ],
      "pitfalls": [
        "HCI를 세계은행의 동명 지수와 혼동하지 않습니다.",
        "2024순위를2026현황으로 발표하지 않습니다."
      ],
      "recall": [
        "EGDI의 세 축과 가중치는 무엇입니까?",
        "EPI와OSI의 범위 차이는 무엇입니까?",
        "시계열 비교에서 방법론 개편을 확인할 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-egdi"
      ],
      "validation": "출처 확인",
      "version_note": "기출2022와2024 방법론을 구분합니다. 실제 열람 기준은 UN2024 보고서이며2026 조사 발간·국가순위는 미확인으로 순위를 싣지 않았습니다.",
      "requirements": [
        {
          "question": "127-2-1",
          "items": [
            "전자정부 평가 개념과 평가지수의 종류",
            "전자정부 발전지수(E-Government Development Index)개념과 평가 방법"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "digital-platform-government",
      "title": "디지털플랫폼정부의 구조·효과",
      "domain": "IT전략·전자정부",
      "aliases": [],
      "related_terms": [],
      "easy": "기관별 사이트를 모으는 수준을 넘어 데이터를 연결하고 민간과 함께 필요한 서비스를 선제적으로 제공하는 구상입니다.",
      "definition": "디지털플랫폼정부는 디지털플랫폼에서 데이터가 연결되고 국민·기업·정부가 함께 사회문제를 해결하며 새로운 가치를 만드는 정부의 정책 구상입니다. 2023 실현계획은 국민 중심 서비스·과학적 정부·민관 성장·신뢰를 강조했습니다.",
      "principles": [
        "특징은 기관·사업 경계를 넘는 데이터 연계, 이용자/생애사건 중심 맞춤·선제 서비스, AI/데이터 기반 의사결정, 민간 플랫폼·혁신 역량과 협업, 공통 기능·클라우드 재사용입니다. 디지털 기술만으로 부처의 권한·책임·법적 제약이 사라지는 것은 아닙니다.",
        "구성은 국민/기업 접점과 통합서비스, 공통 인증·알림·결제/신청 등 서비스 기반, 데이터 표준·품질·연계/API·개방, 클라우드/공통 인프라·AI/분석 도구, 법제·거버넌스·역량·성과관리, 보안·개인정보·신뢰로 설명할 수 있습니다. 이는 계획을 답안에 설명하기 위한 기능적 재구성입니다.",
        "2023의4대 과제는 오직 국민을 위한 정부, 똑똑한 원팀 정부, 민관이 함께하는 성장 플랫폼, 믿고 안심할 수 있는 플랫폼정부로 정리됩니다. 첨부서류 제로화·맞춤 혜택·공장 인허가 통합 등은 대표 추진 사례로, 완료 여부·목표 수치는 별도 실적 확인이 필요합니다.",
        "기대효과는 신청·서류·중복입력 부담과 기관 간 단절 감소, 근거 기반 의사결정, 민간 서비스·산업의 새 기회입니다. 접근성·오프라인 대안·이의신청·데이터 오류 정정·최소수집/권한·장애 대응이 있어야 편의와 권리가 함께 보장됩니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "기관 중심",
            "업무·포털별 분절",
            "국민이 경로를 찾아 반복입력"
          ],
          [
            "이용자 중심",
            "생애사건·과업으로 연계",
            "필요 서비스의 통합·선제 안내"
          ],
          [
            "플랫폼 기반",
            "공통기능·데이터/API·민관참여",
            "재사용·혁신과 책임/접근 통제"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 창업자의 공장 허가 신청",
        "input": "사업자는 입지·환경·건축기관의 서류를 각각 제출합니다.",
        "steps": [
          "사용자 과업을 중심으로 신청과 기관별 심사를 연결합니다.",
          "동의·법적 근거·권한을 확인한 데이터는 재사용하고 결과를 통합 안내합니다.",
          "오류·거절 사유·이의신청·대체 채널과 처리시간을 측정합니다."
        ],
        "result": "기관 통합이 이용자의 실제 과업 완수에 어떤 영향을 주는지 설명합니다.",
        "caution": "실제 구축·효과를 주장하지 않는 창작 설계 예시입니다. 2023의 사업·목표와 현재 조직/정책을 구분합니다."
      },
      "answer_outline": [
        "정의·특징",
        "접점·데이터·공통기반·통제",
        "4대 과제·기대효과·사례"
      ],
      "pitfalls": [
        "모든 개인 데이터를 중앙에 무조건 모으는 정부로 설명하지 않습니다.",
        "정책 계획의 목표 서비스를 완료 실적으로 쓰지 않습니다."
      ],
      "recall": [
        "공통 플랫폼과 단순 포털 통합의 차이는 무엇입니까?",
        "선제 서비스에서 필요한 권리보장 장치는 무엇입니까?",
        "행정 효율과 국민 편의를 별도로 측정하는 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-dpg",
        "sb-isp"
      ],
      "validation": "출처 확인",
      "version_note": "129회 시점과 가까운2023-04 실현계획을 기준으로 설명합니다. 2026 정부조직·위원회·명칭과 모든 과제 이행 실적은 별도 확인 필요합니다.",
      "requirements": [
        {
          "question": "129-1-1",
          "items": [
            "디지털 플랫폼 정부의 특징, 구성요소, 기대효과"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "source-available-license-transition",
      "title": "오픈소스에서 소스공개 라이선스로의 전환",
      "domain": "소프트웨어공학·사업모델",
      "aliases": [],
      "related_terms": [],
      "easy": "코드를 볼 수 있는 것과 제한 없이 사용·수정·재배포할 권리는 다릅니다. 라이선스 변경은 이용 방식·버전에 따라 영향을 판단합니다.",
      "definition": "MIT/BSD 같은 허용적 라이선스는 조건을 지키면 폭넓은 이용·변경·재배포를 허용합니다. SSPL·BSL 전환은 소스를 계속 공개하더라도 사용 분야나 서비스 제공 등에 제약을 두는 소스공개 방식으로, OSI 승인 오픈소스와 구분해야 합니다.",
      "principles": [
        "배경은 개발·유지보수 비용을 부담하는 기업의 수익 확보, 클라우드 사업자의 관리형 서비스 경쟁, 기여/가치 환원의 불균형 인식과 상용 서비스 차별화입니다. 이는 변경 기업의 사업상 판단이며 오픈소스 모델 전체의 실패로 단정할 근거는 아닙니다.",
        "SSPL은 프로그램을 서비스로 제공할 때 서비스 운영에 필요한 관련 소프트웨어까지 공개하도록 요구하는 성격이 핵심입니다. OSI는 사용 분야의 자유 등 오픈소스 정의와 불일치를 지적했습니다. 단순 GPL/AGPL과 같거나 모든 내부 사용에 자동 공개의무가 생긴다고 일반화하지 않습니다.",
        "BSL1.1은 비운영 이용과 복사·수정·배포를 허용하되 운영 사용은 추가 사용허락에 따르며 Change Date 또는 최초 배포4년 중 먼저 도래한 시점에 Change License로 전환하는 구조입니다. 제품·버전마다 추가허락과 날짜가 다를 수 있습니다. HashiCorp는 경쟁 제품/서비스의 제공을 제한하는 허락을 설명했습니다.",
        "영향은 공급자의 사업 지속과 투자 여력, 이용자의 비용/법무 검토·벤더 종속·보안패치 선택, 커뮤니티 신뢰·기여·포크, 클라우드 생태계의 경쟁/상호운용입니다. 대응은 SBOM·버전/라이선스 기록→사용·수정·배포·SaaS 방식 분석→허락/계약 확인→상용 전환·기존 버전·포크/대체의 비용·보안·이행성 비교입니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "허용적 오픈소스",
            "MIT/BSD 조건 아래 폭넓은 권리",
            "저작권·라이선스 고지 등 준수"
          ],
          [
            "SSPL",
            "서비스 제공 시 넓은 공개요구",
            "OSI 승인 오픈소스로 부르지 않음"
          ],
          [
            "BSL",
            "추가허락·시간 후 다른 라이선스",
            "버전·운영 이용·변경일 확인"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 관리형 서비스 제공사의 전환 검토",
        "input": "인프라 도구의 새 버전을 고객 SaaS에 포함하려 합니다.",
        "steps": [
          "구성요소·버전·원래 조건·새 추가 사용허락을 수집합니다.",
          "내부 이용인지 경쟁 서비스 제공인지 계약상 범위를 검토합니다.",
          "상용계약·대체/포크의 패치·호환·전환 비용을 비교하고 결정을 기록합니다."
        ],
        "result": "최신 소스가 공개됐다는 이유만으로 배포·운영 가능성을 판단하지 않습니다.",
        "caution": "창작 검토 절차입니다. 개별 라이선스 적용의 법률 판단은 실제 문구·계약·사용방식을 확인해야 합니다."
      },
      "answer_outline": [
        "배경·정의 교정",
        "MIT/BSD·SSPL·BSL 비교",
        "공급자/사용자/커뮤니티 영향·대응"
      ],
      "pitfalls": [
        "소스공개를 폐쇄된 비공개 소스와 동일시하지 않습니다.",
        "미래 릴리스 조건이 이미 받은 구버전 조건을 자동 소급 변경한다고 쓰지 않습니다."
      ],
      "recall": [
        "source-available과OSI 오픈소스의 차이는 무엇입니까?",
        "BSL의 Change Date와 추가 사용허락은 각각 무엇입니까?",
        "포크 선택에서 보안 유지보수를 확인할 이유는 무엇입니까?"
      ],
      "source_ids": [
        "sb-osi-sspl",
        "sb-bsl",
        "sb-hashicorp-bsl",
        "sb-sspl"
      ],
      "validation": "출처 확인",
      "version_note": "2023 전환 발표와 BSL1.1·OSI 공식 입장을 확인했습니다. 제품별2026 현행 라이선스·기존 계약·법적 해석은 개별 확인이 필요합니다.",
      "requirements": [
        {
          "question": "134-3-6",
          "items": [
            "일부 오픈소스 라이선스가 개방형(예: MIT, BSD 등)에서 폐쇄형(예: SSPL(Server Side Public License), BSL(Business Source License) 등)으로 변화하고 있다. 이러한 오픈소스 라이선스 정책 변경의 배경 및 소프트웨어 산업에 미치는 영향에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "supply-chain-demand-inventory",
      "title": "SCM·수요예측·안전재고/적정재고",
      "domain": "경영·산업적용",
      "aliases": [],
      "related_terms": [],
      "easy": "공급망의 각 회사가 자기 재고만 줄이는 대신, 고객 수요를 만족시키는 전체 흐름의 비용·납기·위험을 함께 조정합니다.",
      "definition": "SCM은 공급자-제조-물류-판매-고객에 걸친 물자·정보·자금의 흐름과 수급 계획·실행을 통합 관리하는 활동입니다. 글로벌 분업·수요 변동·단기 제품수명·재난/지정학적 단절로 가시성과 회복력이 중요합니다.",
      "principles": [
        "효율성은 같은 서비스를 적은 비용·재고·시간·자원으로 제공하는 것이고, 효과성은 고객의 품질·수량·납기와 전략적 회복력 등 목표 달성입니다. 재고 회전만 높여 납기 실패가 늘면 국지 효율은 좋아져도 공급망 효과성은 악화할 수 있습니다.",
        "수요예측의 전형7단계는 목적/사용처 결정→품목 선택→기간 결정→기법 선택→자료 수집→예측 수행→검증·실행입니다. 정성은 전문가/델파이·시장조사, 시계열은 이동/가중평균·지수평활·추세/계절, 인과는 회귀 등이 있습니다. 실제 수요·결품으로 관측되지 않은 수요·행사 효과와 오차/편향을 구분해 검증합니다.",
        "안전재고는 수요·조달기간 불확실성에 대비한 완충입니다. 기간L이 고정되고 기간별 수요가 독립, 평균d·표준편차σ라면 SS=zσ√L, 재주문점 ROP=dL+SS입니다. 일정 수요·조달기간·일시보충 등 단순 EOQ모형은 Q*=√(2DS/H), D는 연수요,S는 주문당 비용,H는 단위당 연보유비입니다.",
        "적정재고는 평균 순환재고Q/2+안전재고에 필요 시 운송·작업중재고를 더하되 서비스수준·품절손실·리드타임·공급능력·유통기한으로 조정합니다. 수요/기간 변동·상관이 있으면 단순식을 그대로 쓰지 않고 경험분포·시뮬레이션·복수공급원/대체품·주기적 재산정을 검토합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "효율성",
            "원가·재고·리드타임 대비 산출",
            "회전율·물류비·자원생산성"
          ],
          [
            "효과성",
            "고객/전략 목표 달성",
            "납기준수·품절·복구·만족"
          ],
          [
            "SS/ROP/EOQ",
            "완충량 / 주문시점 / 주문량",
            "확률·기간·비용의 다른 결정"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 부품 재주문점 계산",
        "input": "일수요100개,일표준편차10개,고정 리드타임4일,z=1.65를 가정합니다.",
        "steps": [
          "SS=1.65×10×√4=33개를 구합니다.",
          "ROP=100×4+33=433개로 재고위치 기준 주문점을 정합니다.",
          "이행 중 주문·예약수요를 포함한 재고위치를 관리하고 실제 품절/과잉을 검증합니다."
        ],
        "result": "수요 변동에 대한 완충과 리드타임 수요를 분리해 설명합니다.",
        "caution": "창작 정규근사 예시이며 z는 주기 서비스수준의 가정입니다. 충족률·공급 중단 위험과 같은 값으로 보지 않습니다."
      },
      "answer_outline": [
        "SCM 정의·배경·통합흐름",
        "효율/효과·예측7단계/기법",
        "SS·ROP·EOQ 가정과 산술"
      ],
      "pitfalls": [
        "공급망의 재고 최소화가 항상 전체 최적이라고 쓰지 않습니다.",
        "7단계의 이름을 출전 확인 없이 공식 표준이라고 말하지 않습니다."
      ],
      "recall": [
        "안전재고와 재주문점은 무엇이 다릅니까?",
        "독립 수요 가정이 깨지면 어떤 문제가 생깁니까?",
        "재고 회전율과 납기준수율이 상충하는 예를 드십시오."
      ],
      "source_ids": [
        "sb-scm",
        "sb-stock",
        "sb-forecast"
      ],
      "validation": "부분 확인",
      "version_note": "SCM·재고의 공식 제품기관 설명을 확인했습니다. 기출의 고전 수요예측7단계 원저 전체와 EOQ/확률식의 공개 교재 원문 대조는 추가 확인 필요합니다. 산식은 가정을 명시한 강사 풀이입니다.",
      "requirements": [
        {
          "question": "128-2-3",
          "items": [
            "공급망관리(SCM)의 개념과 중요성 대두 배경",
            "수요 예측의 7단계 및 수요 예측 기법",
            "안전재고 및 적정재고 산정방법 2–1"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "136-2-1",
          "items": [
            "공급망관리의 정의와 배경",
            "공급망관리에서 효과성과 효율성"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "point-of-production",
      "title": "POP 생산시점 정보관리",
      "domain": "경영·스마트제조",
      "aliases": [
        "Point of Production",
        "생산시점 정보관리"
      ],
      "related_terms": [],
      "easy": "현장에서 언제 누가 어떤 설비로 무엇을 만들었고 불량·정지가 왜 발생했는지 즉시 수집해 생산계획과 연결합니다.",
      "definition": "POP(Point of Production)는 생산시점의 설비·작업자·제품·작업 실적과 상태를 수집·전달·관리하는 현장정보 체계입니다. 수기로 나중에 합산하는 지연을 줄이고 생산 진도·품질·비가동 원인의 가시성을 높입니다.",
      "principles": [
        "구조는 센서/PLC·계측기·바코드/RFID·작업자 입력→POP단말/수집장치→라인컨트롤러/게이트웨이→네트워크→수집서버·DB→현황판·분석/상위시스템입니다. 원 논문 사례는 LAN·RS485와 라인컨트롤러를 사용했지만 특정 통신방식이 POP의 필수 정의는 아닙니다.",
        "하향으로 작업지시·품목/공정·수량·기준·일정, 상향으로 착수/완료·생산/불량량·설비상태·정지/원인·검사·작업 이력을 전달합니다. 이벤트 시각·설비/작업/로트 식별·단위·중복/누락 검증이 없으면 실시간 데이터도 잘못된 진도를 보여줄 수 있습니다.",
        "MES는 생산실행 전반의 작업지시·WIP·품질·설비·추적·자원 관리를 맡으며 POP는 이를 위한 현장 데이터 수집/실적 가시화의 핵심 접점으로 볼 수 있습니다. ERP의 자원·회계/수급 계획과 설비제어의 즉시 동작 사이를 연결하되 제품별 POP/MES 경계는 다릅니다.",
        "적용은 공정/설비·수집항목/주기 정의→원천·코드·시간 동기화→연계·단말/통신 설계→결측/오류·오프라인 버퍼/재전송→계획/실적 대사→현장 대시보드와 개선 활동입니다. 수집망·단말 보안, 작업자 감시/개인정보, 현장 입력 부담과 장애 시 수동 절차도 고려합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "POP",
            "생산시점 데이터·실적 수집",
            "현장의 현재 상태·이력"
          ],
          [
            "MES",
            "생산실행 통합·추적/품질",
            "POP정보로 작업·자원 조정"
          ],
          [
            "ERP",
            "수요·조달·계획·회계 통합",
            "현장 실적과 계획/원가 대사"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 가공 설비 정지 원인 수집",
        "input": "완료량은 알지만 야간 생산 부족의 원인을 모릅니다.",
        "steps": [
          "PLC상태 변화와 작업지시/로트·불량량을 시각과 함께 수집합니다.",
          "계획정지·고장·재료부족의 코드와 입력 책임을 정합니다.",
          "진도·비가동/불량을 대사하고 반복 원인에 개선 과제를 부여합니다."
        ],
        "result": "생산량 숫자에서 원인을 설명할 현장정보로 확장합니다.",
        "caution": "창작 공정입니다. 센서가 알려주지 않는 원인을 자동 추론한 사실로 기록하지 않습니다."
      },
      "answer_outline": [
        "정의·필요",
        "현장→게이트웨이→서버→상위의 구조",
        "양방향 흐름·MES/ERP 비교·고려"
      ],
      "pitfalls": [
        "POP를 소매점POS와 혼동하지 않습니다.",
        "수집 주기만 빠르면 데이터 품질도 높다고 판단하지 않습니다."
      ],
      "recall": [
        "POP에 작업지시 식별자가 필요한 이유는 무엇입니까?",
        "ERP와MES,POP의 역할을 연결해 보십시오.",
        "통신 단절 후 중복 실적을 막으려면 무엇이 필요합니까?"
      ],
      "source_ids": [
        "sb-pop",
        "sb-scm"
      ],
      "validation": "부분 확인",
      "version_note": "2009 원 논문 공개 초록의 구조·정보흐름을 확인했습니다. 현대 특정 MES/POP 제품의 전체 기능과 표준 적합성을 확인한 것은 아닙니다.",
      "requirements": [
        {
          "question": "128-1-3",
          "items": [
            "POP(Point Of Production)에 대하여 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "dark-factory",
      "title": "다크 팩토리·무인 생산 운영",
      "domain": "경영·스마트제조",
      "aliases": [
        "Lights-out factory",
        "다크팩토리"
      ],
      "related_terms": [],
      "easy": "생산 셀이나 공정을 사람이 현장에 계속 머무르지 않아도 운영하도록 자동화하고 원격 감독·예외처리를 갖춥니다.",
      "definition": "다크 팩토리 또는 lights-out factory는 현장 인간 개입을 최소화한 자동 생산 체계입니다. 문자 그대로 조명을 끄는 것이 목적이 아니라 생산·물류·검사·일정·복구를 연결해 일정 시간 무인 운영을 가능하게 하는 것입니다.",
      "principles": [
        "기술구조는 센서/IIoT·PLC/CNC·산업로봇/이송장치, 머신비전/자동검사, MES/MOM·스케줄링·공정/품질 데이터, 예지보전·디지털트윈·원격관제, ERP/공급망 연계입니다. AI는 예측/검사를 지원할 수 있지만 모든 공정이 학습모델만으로 제어되는 것은 아닙니다.",
        "무인 운영에는 원재료 자동공급·공구/소모품 관리·완제품 배출·불량 격리·장애감지와 안전정지·원격 알림/승인·복구가 함께 필요합니다. 기계 한 대가 반복 동작해도 자재 부족이나 품질 이상 때 사람이 즉시 개입해야 한다면 공장 전체의 완전 자율화는 아닙니다.",
        "적합성은 표준 제품·안정 공정·고정 일정·반복량이 높고 상태를 관측/제어할 수 있는지로 평가합니다. 변종/소량·불안정 자재·복잡한 예외는 난도가 높으므로 특정 셀·야간 교대부터 시범 확장하는 방식이 현실적일 수 있습니다. 공정 안정성을 검증하지 않고 인력을 먼저 없애면 위험을 키웁니다.",
        "효과는 연속 운영·일관 품질·위험 작업 노출 감소의 가능성이며, 초기 투자·통합/보전비·공급자 종속·OT보안·기능안전·단일장애점·예외 책임·직무전환을 평가해야 합니다. OEE·불량/재작업·무인 지속시간·안전사건·복구·총비용으로 성과를 검증합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "자동화 설비",
            "정해진 작업의 자동 수행",
            "공급·검사·예외는 별도일 수 있음"
          ],
          [
            "무인 셀",
            "경계 내 공정의 일정시간 무인",
            "조건·안전·원격개입 검증"
          ],
          [
            "다크 팩토리",
            "생산/물류/품질/운영의 연동",
            "전체 흐름·장애·책임의 통합"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 야간 가공 셀의 무인화",
        "input": "반복 부품을 가공하지만 공구 마모와 자재 대기가 발생합니다.",
        "steps": [
          "자재공급·가공·검사·배출·공구교체의 예외를 분석합니다.",
          "안전정지·불량 격리·원격 통보와 대응 담당을 설계합니다.",
          "주간 감시 시범→제한 야간 무인→지표 검증 후 확장합니다."
        ],
        "result": "로봇 도입과 무인 운영 가능성의 차이를 설명합니다.",
        "caution": "창작 단계이며 실제 공장 생산성·인력·원가 개선률을 주장하지 않습니다."
      },
      "answer_outline": [
        "정의·배경",
        "설비·데이터·MOM·자율/예외 구조",
        "적합성·효과/위험·단계적 적용"
      ],
      "pitfalls": [
        "무인공장을 유지보수·감독 인력이 전혀 필요 없는 공장이라고 쓰지 않습니다.",
        "단일 자동화 셀을 공장 전체 완전 자율화 실적으로 확대하지 않습니다."
      ],
      "recall": [
        "다크 팩토리에 자재공급과 품질 격리가 중요한 이유는 무엇입니까?",
        "예외가 많은 공정은 어떤 순서로 접근합니까?",
        "무인 지속시간 외에 검증할 지표는 무엇입니까?"
      ],
      "source_ids": [
        "sb-darkfactory",
        "sb-pop"
      ],
      "validation": "부분 확인",
      "version_note": "Siemens 공식 공개 설명의 정의·MOM·원격 감독·적합 조건 확인. 특정 공장 사례의 현행 성과·인증·수치와 완전 자율화 수준은 미확인입니다.",
      "requirements": [
        {
          "question": "140-1-2",
          "items": [
            "다크 팩토리(Dark Factory)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "blockchain-deployment-data-storage",
      "title": "블록체인 유형·파일/DB와 저장 방식 비교",
      "domain": "경영·분산신뢰",
      "aliases": [],
      "related_terms": [],
      "easy": "모든 참여자를 한 관리자가 신뢰로 묶기 어려울 때, 공동 기록의 순서와 상태를 어떤 규칙으로 합의할지 결정합니다.",
      "definition": "블록체인은 암호학적 연결과 분산 합의 등으로 거래 기록의 일관된 원장을 유지하는 기술입니다. 저장 데이터의 진실성이나 외부 사실을 자동 보증하지 않으며 권한·합의·운영 거버넌스에 따라 성질이 달라집니다.",
      "principles": [
        "퍼블릭은 대체로 누구나 열람·참여 가능한 네트워크에서 검증 권한을 프로토콜로 조정합니다. 검열 저항·공개 검증을 추구하지만 지연·수수료·프라이버시·키 분실·합의 공격의 비용을 평가해야 합니다. 공개 여부와 검증 참여 허가 여부는 별도 축입니다.",
        "프라이빗/허가형은 조직이 참여자·검증자·읽기/쓰기 권한을 관리해 처리량·통제·기밀성을 높일 수 있으나 운영주체·구성원의 신뢰와 담합·키/권한·복구 책임이 필요합니다. 컨소시엄은 여러 기관의 공동 거버넌스라는 특성을 별도로 설명합니다.",
        "하이브리드는 공개망의 증명/검증과 허가망의 기밀 데이터·업무를 조합하는 설계로 설명할 수 있습니다. 비공개 거래의 해시를 공개망에 앵커링하는 예가 있으나 업계에서 단일하게 합의된 제3유형 표준은 아닙니다. 연결 경계·동기화·권한·외부 데이터의 진위를 검증합니다.",
        "파일은 응용이 구조·검색·중복/동시성·복구를 주로 책임지고, DB는 스키마·질의·트랜잭션·제약/권한·백업을 관리합니다. 블록체인은 여러 주체의 기록 순서·상태에 대한 합의를 추가하며 대용량 원본·개인정보는 별도 저장하고 해시/참조만 기록할 수 있습니다. 삭제·정정·비용 요구가 강하면 일반 DB가 더 적절할 수 있습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "파일",
            "응용 중심의 단순 저장·교환",
            "구조/동시성·정합성 별도 구현"
          ],
          [
            "DB",
            "관리된 질의·트랜잭션·무결성",
            "단일/통제된 운영주체의 신뢰"
          ],
          [
            "블록체인",
            "공동 원장·암호 연결·합의",
            "신뢰경계·권한·처리비용 검토"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 기관 공동 자격 증명 기록",
        "input": "발급기관들은 원본 명부를 외부에 공개할 수 없습니다.",
        "steps": [
          "각 기관 DB에 원본·개인정보를 보관하고 공동 검증할 항목을 정의합니다.",
          "허가형망에 발급/취소 상태, 필요 시 공개망에 묶음 해시를 기록하는 대안을 비교합니다.",
          "키 회전·취소·오류 정정·발급 권한과 검증절차를 시험합니다."
        ],
        "result": "공개성·기밀성·합의 비용을 목적에 맞게 조합하는 근거가 됩니다.",
        "caution": "창작 구조이며 해시가 원본 내용의 사실성·적법성까지 보증하지 않습니다."
      },
      "answer_outline": [
        "원장·합의·권한 정의",
        "퍼블릭/프라이빗/하이브리드 비교",
        "파일/DB/블록체인과 적용판단"
      ],
      "pitfalls": [
        "블록체인을 절대 수정 불가능·해킹 불가능하다고 설명하지 않습니다.",
        "permissioned와private를 모든 문맥에서 완전한 동의어로 통합하지 않습니다."
      ],
      "recall": [
        "파일/DB에는 없던 블록체인의 추가 비용은 무엇입니까?",
        "읽기 공개와 검증 참여 허가는 왜 다른 축입니까?",
        "하이브리드 앵커링이 증명하지 못하는 것은 무엇입니까?"
      ],
      "source_ids": [
        "sb-blockchain"
      ],
      "validation": "부분 확인",
      "version_note": "NISTIR8202의 공개/허가형·원장 설명 근거 확인. 하이브리드는 강사 설계 예와 용어 한계를 명시했고 단일 국제표준의 고정 분류로 제시하지 않았습니다.",
      "requirements": [
        {
          "question": "126-2-5",
          "items": [
            "퍼블릭 블록체인(Public Blockchain), 프라이빗 블록체인(Private Blockchain), 하이브리드 블록체인(Hybrid Blockchain)을 비교 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족"
        },
        {
          "question": "130-3-2",
          "items": [
            "데이터저장 측면에서 파일, 데이터베이스, 블록체인을 비교하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "non-fungible-token",
      "title": "NFT 대체불가능 토큰",
      "domain": "경영·디지털자산",
      "aliases": [
        "Non-Fungible Token",
        "대체불가능 토큰"
      ],
      "related_terms": [],
      "easy": "토큰마다 식별자를 달리해 소유·이전 상태를 기록합니다. 연결된 그림 파일 자체를 복제 불가능하게 만드는 기술은 아닙니다.",
      "definition": "NFT는 서로 구별되는 자산을 나타내는 토큰이며 대표 ERC-721은 소유·잔액·승인·이전 등 인터페이스를 정의합니다. 같은 수량의 동종 토큰이 교환 가능한 경우와 달리 개별 토큰의 식별성과 속성이 중요합니다.",
      "principles": [
        "ERC-721에서 동일 체인의 자산 식별은 컨트랙트 주소와 tokenId의 조합으로 이뤄집니다. ownerOf로 현재 소유자, balanceOf로 보유 개수, approve/setApprovalForAll로 이전 권한, transferFrom/safeTransferFrom으로 이전을 다루며 safe형은 수신 컨트랙트의 수용 여부를 확인합니다.",
        "발행은 민팅·식별자/소유 설정→메타데이터/원본 연결→지갑·마켓 등록→주문/서명/승인→체인 거래와 소유 변경으로 설명할 수 있습니다. 원본은 체인 밖 서버·분산저장에 있을 수 있어 URI 지속성·무결성·삭제/변조·운영 종료 문제를 평가합니다.",
        "소유권 기록, 원본 저작권·이용허락, 실제 물건의 권리와 진품성은 별개입니다. NFT를 받았다고 저작권이 자동 이전되거나 복제된 원본이 사라지지 않습니다. 로열티도 별도 구현과 거래처 준수에 달려 모든 재판매에서 자동 보장되는 것은 아닙니다.",
        "활용은 디지털 창작물·입장권·회원권·게임자산·자격/수집품의 추적 등에 있습니다. 위험은 피싱·키 분실·과도한 operator승인·서명 이해 부족·컨트랙트 오류·마켓/외부 저장·프론트엔드 침해이며 권리문서·발급자 신뢰·지갑/승인 관리·거래 검증·사고대응을 함께 설계해야 합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "대체가능 토큰",
            "종류가 같으면 수량 단위로 교환",
            "잔액이 핵심 상태"
          ],
          [
            "NFT",
            "고유 식별자별 소유·이전",
            "권리·메타데이터는 별도 확인"
          ],
          [
            "원본 파일/권리",
            "복제·보관·저작권/사용허락",
            "토큰 소유와 자동 일치하지 않음"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 행사 입장권 NFT",
        "input": "같은 등급 좌석도 좌석번호·입장상태가 달라야 합니다.",
        "steps": [
          "컨트랙트/tokenId와 좌석·유효기간·양도 조건의 관계를 정합니다.",
          "구매/이전 승인과 검표 후 사용 처리·중복 검표 방지를 구현합니다.",
          "지갑 분실·환불·발급 취소·접속 장애 때의 대체 절차를 검증합니다."
        ],
        "result": "고유성의 목적을 가격 투기가 아닌 서비스 권리·상태 관리로 설명합니다.",
        "caution": "창작 서비스입니다. 체인 기록만으로 입장권의 법적 효력·저작권을 보장하지 않습니다."
      },
      "answer_outline": [
        "정의·대체불가능성",
        "ERC721식별/소유/승인/이전",
        "생애주기·활용·권리/보안 한계"
      ],
      "pitfalls": [
        "NFT tokenId가 모든 체인·컨트랙트에서 혼자 고유하다고 쓰지 않습니다.",
        "안전이전 함수가 피싱·권리 사기를 모두 막는다고 판단하지 않습니다."
      ],
      "recall": [
        "토큰과 연결된 파일의 소유/복제는 어떻게 다릅니까?",
        "operator승인이 유출되면 어떤 위험이 있습니까?",
        "메타데이터를 체인 밖에 둘 때 무엇을 검증합니까?"
      ],
      "source_ids": [
        "sb-nft",
        "sb-virtualworld"
      ],
      "validation": "부분 확인",
      "version_note": "ERC721원문 인터페이스와 EC의 권리/원본 구분을 확인했습니다. 128회 OpenSea의 특정 침해일·원인·피해수치는 이 토픽에서 검증하지 않았습니다.",
      "requirements": [
        {
          "question": "127-1-1",
          "items": [
            "대체불가능 토큰(Non-Fungible Token)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "128-4-1",
          "items": [
            "최근 NFT(Non-Fungible Token) 시장의 활성화 및 생태계 형성의 견인차인 NFT 마켓 플레이스가 해커들의 주요 타겟이 되고 있다. 대형 거래소인 OpenSea의 보안 침해사례를 기반으로 NFT 특성과 NFT 마켓 플레이스에서의 보안 취약점을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "부분 충족",
          "coverage_note": "본토픽은NFT특성과승인/저장취약지점을설명합니다.OpenSea특정침해사실은보안토픽보완이필요합니다."
        }
      ]
    },
    {
      "id": "decentralized-web3",
      "title": "Web3·분산 소유 웹 서비스",
      "domain": "경영·디지털서비스",
      "aliases": [],
      "related_terms": [],
      "easy": "서비스 운영자의 계정·서버에만 의존하는 구조에서 사용자 소유·분산 검증·프로그램 가능한 자산을 강화하려는 접근입니다.",
      "definition": "블록체인 맥락의 Web3는 분산 네트워크·스마트컨트랙트·지갑/토큰을 이용해 사용자가 데이터·자산·거버넌스에 더 많은 통제권을 갖도록 지향하는 웹입니다. 시맨틱웹을 뜻하는 Web3.0 용례도 있어 문맥을 밝혀야 합니다.",
      "principles": [
        "도입배경은 대형 플랫폼의 데이터·접근/수익 배분 집중, 계정 차단·서비스 종료 종속, 중개자의 신뢰·검증 비용입니다. Web1의 읽기, Web2의 읽기/쓰기/플랫폼 참여, Web3의 소유·분산 검증 구분은 설명 틀이며 실제 웹 세대가 특정 연도에 일괄 교체된 것은 아닙니다.",
        "주요 기술은 블록체인/합의·스마트컨트랙트·암호학적 지갑/서명·토큰/NFT·분산저장·DApp·오라클·분산 신원·DAO 등입니다. 지갑 서명은 키 통제를 입증하지만 실세계 신원·계약 이해·원본 진위까지 자동 입증하지 않습니다.",
        "서비스는 창작물의 발급/이전·회원/입장 권리, 공급망/자격 검증, 공동 기금·거버넌스와 거래의 프로그램화로 검토할 수 있습니다. 참여자 간 공동 검증이 필요한지, 중앙 DB보다 얻는 편익이 합의 지연·수수료·키관리·개발/운영비를 넘는지 먼저 판단합니다.",
        "한계는 처리량·가스비·복구/UX·프라이버시·컨트랙트/브리지/오라클 위험, 투표권 집중·규제·자산 변동입니다. 프론트엔드·RPC·저장·거래소·관리자키는 여전히 중앙에 집중될 수 있으므로 이름만으로 탈중앙·무신뢰·익명·보안을 달성했다고 선언하지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "Web2 중심 구조",
            "중앙 플랫폼 계정·데이터·규칙",
            "편의·복구와 운영자 의존"
          ],
          [
            "블록체인 Web3",
            "서명·컨트랙트·분산 원장",
            "소유/검증과 키·성능·비용 책임"
          ],
          [
            "시맨틱 Web3.0",
            "메타데이터·연결 데이터·기계해석",
            "RDF/OWL/SPARQL 등 다른 용례"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 기관 간 수료증 검증 서비스",
        "input": "여러 교육기관의 수료 여부를 사용자 동의 아래 검증하려 합니다.",
        "steps": [
          "발급/취소의 공동 검증 필요성과 개인정보 비공개 요구를 분석합니다.",
          "원본은 기관에 두고 필요한 증명·식별/권한·갱신 구조를 비교합니다.",
          "키 분실 복구·철회·잘못된 발급·서비스 종료와 비용을 시험합니다."
        ],
        "result": "기술 요소를 실제 권리·신뢰·운영 문제와 연결합니다.",
        "caution": "창작 설계이며 블록체인 없이 서명 증명서를 검증하는 대안도 같은 기준으로 비교해야 합니다."
      },
      "answer_outline": [
        "문맥·배경·정의",
        "특징·기술구조",
        "활용·경제성·분산 수준·한계"
      ],
      "pitfalls": [
        "시맨틱웹과블록체인Web3를 무조건 동일개념으로 합치지 않습니다.",
        "분산 소유의 지향을 실제 서비스의 검증된 현황으로 쓰지 않습니다."
      ],
      "recall": [
        "Web3에도 중앙 의존이 남는 위치는 어디입니까?",
        "지갑 서명이 증명하는 것과 못 하는 것은 무엇입니까?",
        "서비스 적용 전 검토할 신뢰 문제는 무엇입니까?"
      ],
      "source_ids": [
        "sb-web3",
        "sb-virtualworld",
        "sb-blockchain"
      ],
      "validation": "출처 확인",
      "version_note": "Ethereum의 블록체인 Web3와 EC의 시맨틱Web3.0을 용례 차이로 병기했습니다. 특정 서비스 자산의 법적 성격·2026 시장 규모는 주장하지 않습니다.",
      "requirements": [
        {
          "question": "130-4-5",
          "items": [
            "웹3.0의 도입배경 및 개념",
            "웹3.0의 주요특징 및 기술요소",
            "웹3.0 기반의 서비스 활용 방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "digital-twin-metaverse",
      "title": "디지털트윈·메타버스 비교와 안전한 적용",
      "domain": "경영·디지털융합",
      "aliases": [],
      "related_terms": [
        "디지털 트윈",
        "메타버스"
      ],
      "easy": "트윈은 현실 대상의 상태·행동을 모델과 연결하는 데, 메타버스는 가상 공간의 경험·상호작용을 연결하는 데 초점이 있습니다.",
      "definition": "디지털트윈은 실제 개체나 프로세스의 전자적 표현과 관측·분석·예측 등을 제공하는 기술이며 동기화 주기·정밀도는 목적에 따릅니다. 메타버스는 지속적인 가상세계들에서 사용자가 사회·업무·경제적 상호작용을 하는 비전/환경입니다.",
      "principles": [
        "트윈 구조는 현실 대상/센서→수집·통신/식별→상태·물리/통계 모델→시뮬레이션·분석/시각화→의사결정/필요 시 제어입니다. 단순3D외관과 달리 어떤 대상·상태·주기·정확도를 표현하고 검증하는지 중요하며 모든 트윈이 제어·실시간3D를 필수로 갖는다는 단일 정의는 합의되지 않았습니다.",
        "메타버스의 특징은 지속/실시간 상호작용·몰입/현존감·아바타·참여/창작·사회/경제 활동·플랫폼 간 상호운용의 지향입니다. XR·실시간3D·네트워크/클라우드·신원·콘텐츠 도구가 지원하며 블록체인은 일부 구현의 선택 요소입니다. 트윈을 가상 공간에 연결해 공동 설계·훈련을 수행할 수 있습니다.",
        "보안 위협은 단말/센서·계정 탈취·아바타 사칭, 생체/시선/행동 추적, 통신/API·콘텐츠/자산 변조, 가상공간 악용·서비스 방해입니다. 트윈에서는 잘못된 관측·모델/제어가 물리 설비의 위험으로 연결될 수 있어 무결성·권한·안전정지·검증이 중요합니다.",
        "사회 문제는 괴롭힘·사적 영역 침범·아동 유해노출·과몰입·디지털 격차·창작권/거래 분쟁입니다. 최소수집·동의/권한·안전거리/차단·연령 적합 보호·신고/구제·접근성·휴식·이력/책임·사고대응을 기능과 운영정책에 함께 설계합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "디지털트윈",
            "현실 대상/과정의 상태·모델",
            "관측·예측·시나리오/제어 검증"
          ],
          [
            "메타버스",
            "가상세계 경험·교류·활동",
            "지속/몰입·참여·상호운용"
          ],
          [
            "결합",
            "트윈의 모델을 공동 가상공간에 제공",
            "정밀도·동기·권한·안전 검증"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 공장 설비의 공동 가상 점검",
        "input": "원격 전문가가 현장 작업자와 펌프 상태를 함께 봅니다.",
        "steps": [
          "센서값과 특정 펌프 모델의 대응·주기·오차를 검증합니다.",
          "공동 가상공간에서 상태를 확인하고 가상 시나리오를 시험합니다.",
          "실제 제어는 별도 권한·안전인터록·현장 승인과 로그로 통제합니다."
        ],
        "result": "공유 경험과 물리 시스템 제어의 책임 경계를 분명히 설명합니다.",
        "caution": "창작 예시입니다. 현실의 안전성을 가상 시뮬레이션 성공만으로 보장하지 않습니다."
      },
      "answer_outline": [
        "정의·구조·비교",
        "메타버스 특징·결합 활용",
        "기술위협·사회문제·대응"
      ],
      "pitfalls": [
        "트윈을 단순히 현실과 똑같은3D그림이라고 설명하지 않습니다.",
        "메타버스의 모든 서비스에NFT가 필수라고 쓰지 않습니다."
      ],
      "recall": [
        "트윈에서 동기화 주기와정밀도를 정하는 기준은 무엇입니까?",
        "가상공간 사칭과현실 제어변조는 어떤 피해 차이가 있습니까?",
        "안전한 메타버스의 기능/운영 조치를 하나씩 제시하십시오."
      ],
      "source_ids": [
        "sb-twin",
        "sb-twintrust",
        "sb-virtualworld",
        "sb-metaverse"
      ],
      "validation": "출처 확인",
      "version_note": "NIST2025는 정의 다양성을 명시합니다. 2022 기출의 공통 기술원리를 보완하며 특정 기업의2026 상호운용·완전자율화 성과를 주장하지 않습니다.",
      "requirements": [
        {
          "question": "127-1-12",
          "items": [
            "디지털 트윈(Digital Twin)과 메타버스(Metaverse)"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        },
        {
          "question": "126-4-1",
          "items": [
            "메타버스의 특징",
            "정보시스템 측면의 메타버스의 보안 위협",
            "메타버스에서 발생할 수 있는 사회적 문제점",
            "안전한 메타버스를 위한 방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "metaverse-ethical-principles",
      "title": "메타버스 윤리원칙·3가치8원칙",
      "domain": "경영·디지털윤리",
      "aliases": [],
      "related_terms": [],
      "easy": "가상자아도 존중받아야 하며, 몰입과 데이터 수집이 커질수록 이용자 선택·안전·권리와 공정한 생태계를 설계해야 합니다.",
      "definition": "2022 메타버스 윤리원칙은 개발·운영·이용자와 관련 이해관계자가 윤리 문제를 미리 숙고하고 자발적으로 활용하는 연성규범입니다. 법률을 대신하는 강제 처벌기준이 아니라 실천의 방향을 제시합니다.",
      "principles": [
        "3대 지향가치는 온전한 자아(자신의 가치에 충실하고 자율적으로 행동), 안전한 경험(구성원이 충분히 경험할 안전한 생태계), 지속가능한 번영(누구도 의도적으로 배제하지 않고 미래에도 편익 공유)입니다. 사람의 선택과 안전·공동체의 지속성을 함께 봅니다.",
        "8대 원칙은 진정성·자율성·호혜성·사생활 존중·공정성·개인정보 보호·포용성·책임성입니다. 진정성은 가상자아의 성실한 표현과 관계, 자율성은 참여/행동의 자기결정, 호혜성은 상호 존중·협력, 사생활 존중은 사적 공간·영역을 침범하지 않는 실천으로 풀이할 수 있습니다.",
        "공정성은 창작물 권리·보상/기회와 규칙의 투명성, 개인정보 보호는 광범위한 생체/행동정보의 최소처리·통제, 포용성은 성별·연령·장애·경제조건 등의 차이에 따른 배제 방지, 책임성은 영향·피해에 대한 주체별 책임·구제를 요구하는 방향입니다. 해석을 실제 기능·정책·교육·처리절차에 연결합니다.",
        "인터넷 윤리는 정보 유통·표현·소통의 책임을, AI윤리는 데이터·알고리즘의 편향·설명·자율 판단/인간책임을, 메타버스 윤리는 가상자아·몰입·공간·현실/가상 연동·자산/활동의 경험을 강조한다고 비교할 수 있습니다. 상호 배타적인 규범이 아니며 하나의 서비스에 동시에 적용됩니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "인터넷 윤리",
            "콘텐츠·소통·정보권리",
            "표현·명예·저작권·사이버폭력"
          ],
          [
            "AI 윤리",
            "데이터·모델·판단과 영향",
            "편향·투명·감독·책임"
          ],
          [
            "메타버스 윤리",
            "가상자아·몰입공간·경험",
            "거리/접촉·추적·창작/보상·포용"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 가상 전시회 안전 설계",
        "input": "관람자의 아바타가 원치 않는 접근을 받고 시선정보가 수집됩니다.",
        "steps": [
          "개인 공간·차단/신고와 개인정보 수집 선택을 제공합니다.",
          "창작물 권리·유료 보상·이용/제재 규칙과 이의신청을 공개합니다.",
          "접근성·아동 보호·신고 처리·데이터 삭제가 실제 작동하는지 검증합니다."
        ],
        "result": "가치·원칙을 서비스 운영의 확인 가능한 요구로 바꿉니다.",
        "caution": "창작 예시입니다. 원칙 준수만으로 모든 법률 준수·무피해가 보장되는 것은 아닙니다."
      },
      "answer_outline": [
        "연성규범·적용주체",
        "3가치·8원칙과 의미",
        "3윤리 비교·기능/운영 적용"
      ],
      "pitfalls": [
        "사생활 존중과 개인정보 보호를 동일 항목으로 합쳐7개만 쓰지 않습니다.",
        "2023 실천윤리의 세부 조항 수를2022의8원칙 수와 혼동하지 않습니다."
      ],
      "recall": [
        "3대 지향가치를 각각 설명하십시오.",
        "사생활 존중과 개인정보 보호의 다른 적용 예는 무엇입니까?",
        "한 서비스에 인터넷·AI·메타버스 윤리가 함께 적용되는 예를 드십시오."
      ],
      "source_ids": [
        "sb-metaverse",
        "sb-metaverse2023"
      ],
      "validation": "출처 확인",
      "version_note": "2022-11-28의3가치8원칙을 기준으로 했습니다. 2023-12 실천윤리는 기본40·주체별120조항으로 구체화한 후속 자료이며 원칙의 강제 법규화를 뜻하지 않습니다.",
      "requirements": [
        {
          "question": "130-2-5",
          "items": [
            "3대 지향가치와 8대 실천원칙",
            "인터넷 윤리, 인공지능 윤리 및 메타버스 윤리 비교"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "digital-dysfunctions",
      "title": "디지털 역기능·3대 사회 이슈와 대응",
      "domain": "경영·디지털윤리",
      "aliases": [],
      "related_terms": [],
      "easy": "연결·복제·추천·익명성이 주는 편익이 거짓 정보·차별·범죄의 빠른 확산에도 쓰이는 문제를 다룹니다.",
      "definition": "디지털 역기능은 디지털 기술·서비스의 사용/악용으로 개인·집단·사회에 발생하는 피해와 부정적 영향입니다. 중독·격차·침해 등 넓은 현상이 있으나130회3대 이슈는 NIA2022보고서의 허위조작정보·혐오표현·성범죄에 대응합니다.",
      "principles": [
        "디지털 허위조작정보는 오도·피해 의도로 만들거나 유통하는 거짓/조작 정보를 중심으로 봅니다. 단순 오류·풍자·의견 불일치와 구분하고 출처·문맥·원자료 검증, 정정·사실확인, 추천/광고·조직 유포의 투명성을 적용합니다. 자동 탐지가 의미와 의도를 완벽히 판단하지 못합니다.",
        "디지털 혐오표현은 인종·성별·장애 등 집단의 정체성에 근거해 모욕·차별·적대 등을 유발하는 표현의 문제입니다. 비판·표현의 자유와 보호 필요성을 함께 평가하고 명확한 정책·신고/심사·이의신청·맥락 판단·피해자 지원·교육을 운영합니다.",
        "디지털 성범죄는 불법촬영·동의 없는 유포/재유포·협박·성착취·성적 합성물 등의 피해를 포함합니다. 피해자에게 책임을 돌리지 않고 신고·증거 보전·신속한 삭제/차단과 재유포 감시, 상담·법률/회복 지원·수사기관 연계·예방교육을 결합합니다.",
        "공통 대응은 정부의 권리보호·법집행/기술 지원, 사업자의 설계/운영 책임·자율규제·대응 창구, 시민·학교의 디지털 리터러시·참여, 탐지/검증·신고·피해구제의 기술/조직 협력입니다. 과도한 감시·오탐·검열·재피해를 점검하고 처리시간·재유포·구제 결과로 실효성을 측정합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "허위조작정보",
            "거짓/조작·맥락 왜곡으로 판단 방해",
            "출처검증·정정·유포 투명성"
          ],
          [
            "혐오표현",
            "집단 정체성 기반 차별·적대",
            "맥락 심사·정책·이의신청·교육"
          ],
          [
            "성범죄",
            "동의 없는 촬영/유포·착취 등",
            "신속 삭제·증거·지원·재유포 방지"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 커뮤니티의 조작 영상 확산 대응",
        "input": "공적 사건의 영상이 문맥을 바꾸어 퍼집니다.",
        "steps": [
          "원본·시간·편집 여부·출처를 확인하고 단순 의견과 사실 주장을 구분합니다.",
          "사용자에게 검증 맥락·정정을 제공하고 조작 유포·피해 신고를 심사합니다.",
          "오탐 이의신청과 피해지원·반복 유포 대응의 결과를 점검합니다."
        ],
        "result": "삭제 버튼 하나로 끝내지 않고 검증·권리·회복을 연결합니다.",
        "caution": "창작 비성적 사례입니다. 불필요하게 피해 자료를 복제·공개하여 재피해를 만들지 않습니다."
      },
      "answer_outline": [
        "개념·확산 특성·사례",
        "2022보고서3대 이슈",
        "민관협력·기술·교육·피해구제"
      ],
      "pitfalls": [
        "3대 이슈를 임의의 보안기술3개로 대체하지 않습니다.",
        "정책 제안과 현재 법적 의무·처벌을 혼합하지 않습니다."
      ],
      "recall": [
        "허위조작정보와 단순 오류를 구분할 이유는 무엇입니까?",
        "삭제와 피해구제는 왜 다른 과업입니까?",
        "역기능 대응의 오탐·검열 위험을 줄일 장치는 무엇입니까?"
      ],
      "source_ids": [
        "sb-dysfunction"
      ],
      "validation": "출처 확인",
      "version_note": "기출과 가까운 NIA2022 보고서의3대 이슈와 제안 중심입니다. 범죄의 법적 구성요건·최신 처벌·신고기관 연락처를 이 자료만으로 확정하지 않습니다.",
      "requirements": [
        {
          "question": "130-2-6",
          "items": [
            "디지털 역기능 개념과 사례",
            "디지털 역기능 3대 이슈",
            "대응방안"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "dark-patterns",
      "title": "다크패턴 유형·예방/규제 대응",
      "domain": "경영·디지털윤리",
      "aliases": [],
      "related_terms": [],
      "easy": "사용자의 편향·주의 한계를 이용해 원치 않는 결제·동의·가입을 유도하거나 취소를 어렵게 만드는 설계입니다.",
      "definition": "다크패턴은 인터페이스의 정보·선택·순서·시각적 강조를 조작해 사용자의 자율적 판단을 흐리거나 방해하고 사업자에게 유리한 행동을 유도하는 방식입니다. 단순히 미적으로 나쁜 화면과는 구분합니다.",
      "principles": [
        "대표 유형은 광고를 독립 정보로 위장, 허위 희소성/타이머·사회적 압박, 주요조건·추가비용 은폐, 사전선택·장바구니 끼워넣기, 복잡한 취소/탈퇴, 동의 유도/거절 방해와 개인정보 과다 제공 유도입니다. 여러 패턴이 한 흐름에서 결합하면 한 화면만 검사해서는 문제를 놓칩니다.",
        "국내2025 신설6유형은 숨은 갱신(증액/무료→유료의 인지·동의 문제), 순차공개 가격책정(필수 총비용을 뒤늦게 공개), 특정옵션 사전선택(다른 구매를 미리 선택), 잘못된 계층구조(차별적 강조로 유인), 취소·탈퇴 방해, 반복간섭입니다. 유형 이름과 구체 행위·피해를 연결해 설명합니다.",
        "개선은 총가격·기간/갱신·필수/선택의 명확한 표시, 구매/개인정보의 적극적 선택, 유사한 명확성의 수락/거절, 가입만큼 찾기 쉬운 취소, 실재하는 희소성·진실한 광고/후기, 동의 철회·완료 확인입니다. 불필요한 반복팝업·수치심 유발 문구와 방향을 바꾼 버튼을 피합니다.",
        "조직 대응은 기획·UX·개발·법무의 흐름 검토, 취약 사용자·접근성 시험, 버전/동의·가격/갱신 기록, 민원/환불/탈퇴 성공률 감시, 제휴/광고와 실험의 감독입니다. 전환율만으로 성과를 보상하면 피해가 커질 수 있어 이해·실수/후회·구제 지표를 함께 봅니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "정보 왜곡",
            "광고위장·가격/중요조건 은폐",
            "진실한 정보·총비용·적시 고지"
          ],
          [
            "선택 유도",
            "사전선택·시각차별·반복간섭",
            "명확하고 자유로운 수락/거절"
          ],
          [
            "행동 방해",
            "취소/탈퇴를 숨기거나 지연",
            "쉽게 찾는 절차·완료/철회 확인"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 무료 체험 구독 화면 교정",
        "input": "가입 버튼만 크게 보이고 유료 전환·해지는 작은 글씨입니다.",
        "steps": [
          "기간·전환일·금액·해지 조건을 결정 전에 명확히 제공합니다.",
          "적용 법률에 맞는 동의와 취소/철회·고지 기록을 설계합니다.",
          "취소까지 전체 흐름을 시험하고 성공률·민원·원치 않는 결제를 점검합니다."
        ],
        "result": "가입 수치와 함께 소비자 이해·통제권을 검증합니다.",
        "caution": "창작 UX 사례입니다. 모든 갱신이 불법인 것은 아니며 법의 대상·예외·현행 가이드 해석을 확인합니다."
      },
      "answer_outline": [
        "정의·인지편향·피해",
        "세부 유형·구체 예",
        "UX·운영·법제·성과 통제"
      ],
      "pitfalls": [
        "정당한 안내나 필요한 확인을 모두 다크패턴으로 단정하지 않습니다.",
        "2025 개정6유형과 전체 분류 또는2026금융 가이드 유형 수를 섞지 않습니다."
      ],
      "recall": [
        "사전선택과 잘못된 계층구조는 무엇이 다릅니까?",
        "화면 한 장이 아닌 전체 흐름을 봐야 하는 이유는 무엇입니까?",
        "전환율 외에 어떤 소비자 지표가 필요합니까?"
      ],
      "source_ids": [
        "sb-darkpatterns-ftc",
        "sb-darkpatterns-korea",
        "sb-darkpatterns-2026"
      ],
      "validation": "부분 확인",
      "version_note": "기출 당시 일반 유형·2025-02-14 신설 규율을 구분했습니다. 2026-10-06 새 운영 가이드 배포를 확인했으나 별첨 전체·현행 법령의 후속 변경 대조는 추가 확인 필요합니다.",
      "requirements": [
        {
          "question": "134-2-2",
          "items": [
            "소비자를 기만하여 이익을 편취하고자 하는 다크패턴(Dark Pattern)이 발생하고 있다. 이와 관련하여 다크패턴의 세부 유형 및 대응 방안을 설명하시오."
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "superapp-miniapp",
      "title": "슈퍼앱·미니앱과 멀티앱 비교",
      "domain": "경영·서비스플랫폼",
      "aliases": [],
      "related_terms": [],
      "easy": "자주 쓰는 핵심 앱이 인증·결제·탐색 같은 공통 기능을 제공하고 여러 사업자의 작은 서비스를 그 안에서 실행합니다.",
      "definition": "슈퍼앱은 하나의 사용자 접점과 공통 기반 위에서 여러 생활·업무 서비스를 통합 제공하는 앱/생태계입니다. 미니앱은 호스트 앱의 런타임·API·배포체계 안에서 작동하는 비교적 작은 서비스로 별도 설치 부담을 줄입니다.",
      "principles": [
        "주요 요소는 빈번한 핵심 서비스·큰 접점, 통합 계정/신원·결제·알림/검색·개인화·데이터, 미니앱 컨테이너/SDK·JS/네이티브 브리지·권한 API, 개발도구·심사/배포·버전/운영, 파트너와 수익배분·거버넌스입니다. 모든 기능을 한 코드·DB에 합쳐야 한다는 뜻은 아닙니다.",
        "멀티앱은 서비스별 설치·로그인·업데이트로 집중된 UX와 독립 운영을 얻지만 전환·계정·탐색의 마찰이 생깁니다. 슈퍼앱은 공통 경험·교차 유입·낮은 진입장벽을 얻는 대신 복잡성·장애 영향·플랫폼 종속·개인정보 결합·독점/수수료 문제가 커질 수 있습니다.",
        "미니앱은 검색·QR·딥링크 등으로 진입하고 호스트가 패키지/버전 로딩·런타임·화면/생명주기를 관리합니다. 네이티브 기능은 브리지/API와 허용 권한으로 제공하며 호스트 인증을 연결해도 백엔드는 사용자·대상·범위를 다시 검증해야 합니다. 서비스 간 정보가 무조건 공유되는 구조로 만들지 않습니다.",
        "실제 Weixin 미니프로그램은 쇼핑·음식·교통·공공서비스 등을 호스트에서 제공합니다. Alipay계열도 공통 인증/결제 능력을 미니프로그램에 연결합니다. 전망은 경량 파트너 서비스·자주 쓰는 접점의 확장 가능성으로 해석하되 국가별 개인정보·경쟁·금융 규제와 사용자 피로·신뢰/보안·개방성을 평가합니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "슈퍼앱",
            "여러 서비스를 공통 접점에 통합",
            "편의·교차유입 / 복잡성·집중위험"
          ],
          [
            "멀티앱",
            "독립 서비스별 설치·운영",
            "특화UX·격리 / 전환·인증 마찰"
          ],
          [
            "미니앱",
            "호스트 런타임·API에서 실행",
            "빠른 접근 / 권한·심사·종속"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 지역 생활 앱에 주차 미니앱 연결",
        "input": "주민이 교통 앱에서 주차 예약과 결제를 하려 합니다.",
        "steps": [
          "호스트는 로그인·지도·결제, 파트너는 주차 재고·예약 책임을 맡습니다.",
          "허용 API·OAuth범위·승인·배포와 예약/환불의 거래 경계를 정합니다.",
          "중복결제·권한남용·파트너 장애·버전 변경을 시험합니다."
        ],
        "result": "통합 UX와 분리된 사업 책임을 함께 설계합니다.",
        "caution": "창작 예시입니다. 공통 로그인은 모든 파트너에 무제한 개인정보 제공을 허용한다는 뜻이 아닙니다."
      },
      "answer_outline": [
        "정의·핵심요소",
        "슈퍼앱/멀티앱 비교",
        "미니앱 구조·실제 사례·전망/이슈"
      ],
      "pitfalls": [
        "기능이 많은 앱을 개발 생태계 검토 없이 모두 같은 슈퍼앱으로 단정하지 않습니다.",
        "미니앱을 호스트 통제에서 독립된 일반 네이티브앱으로 설명하지 않습니다."
      ],
      "recall": [
        "미니앱의 네이티브 기능 호출은 어떤 경계로 통제합니까?",
        "슈퍼앱의 편의와 장애 집중은 어떻게 연결됩니까?",
        "파트너 종료 때 사용자 거래 책임을 왜 미리 정합니까?"
      ],
      "source_ids": [
        "sb-superapp",
        "sb-miniprogram",
        "sb-mini-spi"
      ],
      "validation": "출처 확인",
      "version_note": "공식 제공자 문서의 호스트/미니앱 구조와 기능을 확인했습니다. 2026의 시장규모·이용자 수·특정 국내 서비스의 완성도는 주장하지 않습니다.",
      "requirements": [
        {
          "question": "133-3-3",
          "items": [
            "슈퍼앱의 정의와 주요요소",
            "슈퍼앱과 멀티앱의 비교",
            "슈퍼앱상 구동 서비스 미니앱",
            "슈퍼앱의 사례와 전망 및 이슈사항 2–1"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    },
    {
      "id": "ai-digital-textbook-platform",
      "title": "AI 디지털교과서의 구조·핵심 서비스",
      "domain": "경영·교육융합",
      "aliases": [],
      "related_terms": [],
      "easy": "학생의 진단·학습 이력으로 경로와 콘텐츠를 조정하고, 교사가 그 결과를 검토해 수업과 지원을 결정하도록 돕는 교육 서비스입니다.",
      "definition": "기출 당시 AI 디지털교과서는 AI 등 지능정보기술로 다양한 학습자료와 지원 기능을 제공해 학생 개인의 능력·수준에 맞는 학습 기회를 지원하는 SW입니다. 단순 전자책·동영상 목록과 학습 진단/적응·교사 지원의 차이를 설명합니다.",
      "principles": [
        "2023 개발원칙은 인간 존엄을 위한 교육, 평등한 학습기회, 교사 전문성 존중입니다. 학습분석(Learning Analytics), 수준/속도에 맞춘 적응학습, 학생 중심 설계와 보충/심화, UDL·접근성을 구현하고 교사의 맥락 판단·관찰·정서 지원을 보완합니다.",
        "당시 구조는 공공 포털의 교육디지털원패스 통합인증·교과서 책장·통합대시보드, 민간의 교과별 SaaS서비스(진단/평가·AI보조교사/튜터·콘텐츠·교과대시보드), 공통 학습데이터허브와 표준API/데이터 수집도구입니다. NEIS·시도교육청 서비스 등 외부 연계와 국가/시도 분석을 분리해 설명합니다.",
        "핵심 서비스는 학생의 진단·학습분석→경로/콘텐츠·문항 추천→AI튜터의 맞춤 지원, 교사의 수업설계·맞춤처방·콘텐츠 재구성/추가·이력 기반 관리, 학부모의 자녀 분석 대시보드입니다. 공통으로 주체 간 소통·통합 로그인·쉬운UI/UX·접근성을 지원합니다.",
        "데이터 흐름은 인증/소속·역할→교과서비스→활동/성과 수집→규격화·전송/허브→분석/대시보드→교사 검토·맞춤 지원입니다. 데이터 최소화·동의/권한·아동 보호·오류 정정·보안·정확한 콘텐츠·학교 기기/네트워크·장애/오프라인 대안·추천 편향을 시험해야 합니다. 점수 예측을 학생의 고정 능력으로 낙인찍지 않습니다."
      ],
      "comparison": {
        "headers": [
          "구분",
          "원리·특징",
          "적용·판단"
        ],
        "rows": [
          [
            "공공 포털",
            "공통인증·책장·통합 대시보드",
            "교과/사업자 간 사용자 접점"
          ],
          [
            "민간 교과서비스",
            "콘텐츠·진단·튜터/보조교사",
            "교과별 맞춤 학습·수업 지원"
          ],
          [
            "학습데이터허브",
            "공통규격의 학습정보 수집/연계",
            "목적·접근·품질·보유 통제"
          ]
        ]
      },
      "example": {
        "title": "강사 창작 적용 예시: 분수 학습 지원",
        "input": "학습자는 통분 문제에서 반복 오류를 보입니다.",
        "steps": [
          "활동·정오답을 분석해 필요한 선행 개념과 불확실성을 표시합니다.",
          "보충 콘텐츠·문항을 추천하고 교사가 원인·진도·학생 상태를 검토합니다.",
          "후속 수행과 설명 능력을 확인해 경로를 조정하고 불필요한 수집을 줄입니다."
        ],
        "result": "AI의 분석→교사 판단→학습 지원의 피드백을 설명합니다.",
        "caution": "창작 예시입니다. 실제 학습효과·분석 정확도는 검증해야 하며 자동으로 성적 평가를 확정하지 않습니다."
      },
      "answer_outline": [
        "기출 당시 정의·특징·3원칙",
        "공공/민간/허브 구조·흐름",
        "학생/교사/학부모 핵심서비스·현재 지위"
      ],
      "pitfalls": [
        "2023의2025도입계획을 현재 확정된 전면 시행으로 쓰지 않습니다.",
        "AI추천이 교사의 최종 교육 판단을 완전히 대체한다고 설명하지 않습니다."
      ],
      "recall": [
        "공공 포털과 민간 교과서비스의 역할 차이는 무엇입니까?",
        "학습데이터허브로 보낼 데이터의 기준은 무엇입니까?",
        "교과서에서 교육자료로의 제도 변화를 어떻게 구분해 설명합니까?"
      ],
      "source_ids": [
        "sb-aidt2023",
        "sb-aidtcurrent"
      ],
      "validation": "출처 확인",
      "version_note": "2023 KERIS발표 구조로135회 당시 기술을 설명했습니다. 교육부2025-12 설명은2025-08 초중등교육법 개정 후 학습지원SW를 교육자료로 선정하고 기준 충족·학운위 심의를 거치는 체계, NEIS연계 구AI교과서의 AI·디지털교육자료 포털 운영을 안내합니다. 2026 전체 후속법령·선정 실적은 미확인입니다.",
      "requirements": [
        {
          "question": "135-2-6",
          "items": [
            "개념 및 특징",
            "플랫폼 구조",
            "기능 및 핵심 서비스"
          ],
          "section": "핵심원리/예제/비교표",
          "status": "충족"
        }
      ]
    }
  ]
}
```
