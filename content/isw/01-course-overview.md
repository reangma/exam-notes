# 1. 과목 개요와 AI Agent의 역사

첫 주차 오리엔테이션입니다. 이 장에서 할 일은 두 가지입니다.

1. **이 과목이 결국 무엇을 배우는지** 큰 그림 잡기 → "챗봇"과 "에이전트"는 뭐가 다른가
2. **AI Agent가 어떤 순서로 발전해 왔는지** 외우기 → 시험에 "각 단계의 특징을 쓰시오"로 나오기 좋음

{: .참고 }
> 처음이라면 [0장 수학·용어 기초](00-math-basics.html)를 먼저 훑고 오세요. 벡터, 확률, 파라미터 같은 말이 뒤에서 계속 나옵니다.

---

## 평가 방식

| 항목 | 배점 |
|---|---|
| **중간고사 (필기시험만)** | **40점** |
| 기말 Project | 40점 |
| 실습 및 과제 | 10점 |
| 수업 참여도·태도 | 10점 |

{: .중요 }
> - 중간고사·기말 Project **미응시 시 F**
> - 공결 등은 **사전에 이메일로** 허락받아야 하며, 긴급상황을 제외하면 **당일 통보는 인정되지 않음**
> - 중간고사는 **오직 필기시험(only written test)** → 코드를 치는 게 아니라 **개념을 글로 설명**해야 합니다.
>
> 그러니 공부 전략은 **"용어의 정의 + 왜 필요한지 + 비교"를 내 말로 쓸 수 있게** 하는 것입니다. 이 노트의 노란 박스(시험 포인트)가 그 연습용입니다.

## 강의 일정

| 주차 | 내용 |
|---|---|
| 1 | Introduction |
| 2 | LLM Basic with practice |
| 3 | AI Agent Concepts and Architecture |
| 4 | Agent Planning and ReAct |
| 5 | Structured Output and Tool Use |
| 6 | Loop Engineering and Recovery |
| 7 | From Context to Harness Engineering |
| **8** | **MidTerm Exam** |
| 9 | Workflow 패턴·evaluator loop |
| 10 | Graph engineering with LangGraph 기초 |
| 11 | Stateful Graph, Checkpoint, and HITL |
| 12 | RAG, Memory, and Context Policy |
| 13 | Multi-agent orchestration |
| 14 | Agent Optimization and Deployment |
| 15 | Final Presentation |

- 교재: **『AI 에이전트 엔지니어링』(한빛미디어)** 를 보조 교재로 사용, 그 외 최신 기사·논문 PDF
- 강의 시간: **화요일 13:00~16:00**
- 후반부 일정은 학생들의 학습 성취도에 따라 바뀔 수 있음

---

## 현재 AI Issues? — "지금 왜 이걸 배우나"

### 2026년 가트너 선정 10대 기술 트렌드

가트너(Gartner)는 **IT 시장 조사 회사**입니다. 매년 "앞으로 뜰 기술 10개"를 발표합니다.
2026년 발표는 세 묶음으로 나뉘고, 시기는 **Now(1~3년 안)** 와 **Near(3~5년 안)** 로 구분됩니다.

| 묶음 | 뜻 | 기술 |
|---|---|---|
| **The Architect** (설계자) | AI를 돌릴 **기반** | ① AI-native development platforms ② AI supercomputing platforms ③ Confidential computing |
| **The Synthesist** (종합자) 🔴 | AI를 **엮어서 쓰기** | ④ **Multiagent systems** ⑤ **Domain-specific language models** ⑥ **Physical AI** |
| **The Vanguard** (선봉) | AI를 **지키기** | ⑦ Preemptive cybersecurity ⑧ Digital provenance ⑨ AI security platforms ⑩ Geopatriation |

{: .참고 }
> 강의에서 **The Synthesist**에 빨간 박스를 쳤습니다. 이유는 이 과목 주제와 직결되기 때문입니다.
> - **Multiagent systems** = 여러 AI가 팀을 이뤄 일하는 것 → [12장](12-agent-architectures.html)
> - **Domain-specific language models** = 특정 분야(법률, 의료 등)에 특화된 언어 모델
> - **Physical AI** = 로봇처럼 실제 세상에서 몸을 움직이는 AI

### 기존 AI (챗봇) vs AI 에이전트 ★

{: .시험 }
> **이 비교가 과목 전체의 출발점**입니다. "AI 에이전트란 무엇인가"를 가장 쉽게 설명하는 방법이기도 합니다.

| | **기존 AI (Chatbot)** | **AI 에이전트** |
|---|---|---|
| **사용자가 하는 말** | "내일 날씨 어때?" | "내일 시애틀행 비행기 **예약해 줘**." |
| **AI가 하는 일** | "서울 날씨는 맑습니다." → **끝** | ① **목표 수립** → ② 비행기 **검색** → ③ 가격 **비교** → ④ 최적 옵션 **선택** → ⑤ **예약 완료** |
| **비유** | 질문하면 답해주는 **'백과사전'** 혹은 **'1인 전문가'** | 목표를 주면 **스스로 계획 세우고 실행까지** 하는 **'비서'** 혹은 **'팀 프로젝트 매니저'** |

**쉽게 말하면:**

- 챗봇은 **말만** 합니다. "비행기는 이런 게 있어요"까지만 알려주고, 예약은 내가 해야 합니다.
- 에이전트는 **일을 끝냅니다.** 직접 사이트에 들어가서 검색하고, 비교하고, 결제까지 합니다.

**Before agent → After agent**

| | 구성 | 의미 |
|---|---|---|
| **Before agent** | Claude, ChatGPT, perplexity | **AI 모델 하나**만 덩그러니 있음 |
| **After agent** | **Public API + DB + LLM model + Agent** | 모델에 **도구(API)·저장소(DB)** 가 붙어서 하나의 시스템이 됨 |

{: .참고 }
> **API**가 뭔가요? **프로그램끼리 대화하는 창구**입니다.
> 예를 들어 "항공사 API"가 있으면, AI가 항공사 홈페이지에 사람처럼 클릭하지 않아도 **"서울→시애틀 내일 항공편 줘"** 라고 요청하면 데이터를 받을 수 있습니다.
> **DB(Database)** 는 **데이터를 저장해 두는 창고**입니다. 사용자의 예전 기록 등을 보관합니다.

{: .중요 }
> 핵심 차이는 **"답을 주느냐"** vs **"일을 끝내주느냐"**.
> 이 차이를 만드는 것이 **Tool(손발) + Memory(기억) + Planning(계획)** 입니다. (아래 "기본 구조"에서 다시 나옵니다)

---

## 오늘의 Hot Issue — Agentic AI 분야

LLM 강의 첫 슬라이드에 나온 최신 동향입니다. **시험 문제로 나올 내용은 아니고**, "업계가 지금 '행동하는 AI'로 경쟁 중"이라는 분위기만 알면 됩니다.

**GPT-6 Astra (OpenAI) vs Claude Fable 5.1 (Anthropic)** — 2026 벤치마크 비교

{: .참고 }
> **벤치마크(benchmark)** = AI 성능을 비교하기 위한 **표준 시험지**입니다. 같은 시험을 보게 해서 점수를 비교합니다.

| 평가 항목 | 무엇을 재나 | GPT-6 Astra | Claude Fable 5.1 | 우세 |
|---|---|---|---|---|
| 종합 지능 지수 | 전반적인 똑똑함 | 61.2 | **65.7** 🏆 | Fable · 범용 추론·지식 |
| 코딩 에이전트 인덱스 | 코딩을 혼자 해내는 능력 | 67 | **70** 🏆 | Fable · 장기 코딩 |
| Terminal-Bench Science 0.1 | 과학 연구 작업 | **64.6%** 🏆 | 52.6% | Astra · 도구 활용·분석·연구 |
| Terminal-Bench 4.0 | 터미널(명령창) 작업 | **57.9%** 🏆 | 55.8% | Astra 근소 · 다단계 작업 |
| ARC-AGI-3 | 처음 보는 규칙 찾기 | **62.7%** / 99.9% 🏆 | 공개값 없음 | Astra · 새 환경 적응 |
| OSWorld 2.0 | 마우스로 컴퓨터 쓰기 | **72.6%** 🏆 | 비교 제한 | Astra · 실제 GUI 작업 |

- **Fable 5.1 강점**: 종합 지능, 장기 코딩 → *"더 깊은 지식이 더 큰 가능성을 만듭니다."*
- **GPT-6 Astra 강점**: 적응형 추론, 에이전트 실행, 컴퓨터 사용 → *"추론을 넘어, 행동하는 AI로."*
- **정리: Fable 5.1은 '깊은 지식·추론', GPT-6 Astra는 '추론을 행동으로 연결하는 Agentic AI'에 강점**
- (주의: 일부 항목은 완전한 1:1 비교가 아니므로 해석에 주의)

---

## AI Agent의 역사 (에이전트 유형의 발전) ★

{: .참고 }
> 이 표는 **"AI가 얼마나 스스로 할 수 있게 되었는가"** 를 옛날 → 지금 순서로 늘어놓은 것입니다.
>
> **한 줄 흐름**: 규칙만 따름 → 계획을 세움 → 말로 생각하고 도구를 씀 → 혼자 반복해서 일함 → 여럿이 팀으로 일함
>
> 아래에서 하나씩 쉽게 풀고, 맨 끝에 원본 표를 그대로 둡니다.

### ① Rule-based Agent (규칙 기반 에이전트) — "매뉴얼대로만 하는 직원"

- **AI가 아닙니다.** 사람이 **"만약 A면 B를 해라(If-Then)"** 규칙을 미리 잔뜩 적어 놓은 프로그램
- 예: "온도가 25도 넘으면 → 에어컨 켜기"
- **대표 기술**
  - **Expert Systems (전문가 시스템)**: 전문가의 지식을 규칙으로 옮겨 적은 프로그램 (예: "기침+열 → 감기 의심")
  - **RPA (Robotic Process Automation, 예: UiPath)**: 사람이 하던 **반복 클릭 작업을 녹화해서 자동 재생**하는 프로그램
- **특징**
  - 입력에 **정해진 규칙으로만** 반응
  - **지능적 추론이나 적응 불가** → 매뉴얼에 없는 상황이 오면 멈춤
  - 대신 **미리 정해둔 환경에서는 안정적**으로 작동 (예측 가능함)
  - **지금도 일부 통제용 rule logic으로 사용** (예: "결제 금액 100만원 넘으면 무조건 사람 확인")

### ② Planning Agent (계획 기반 고전 AI) — "길찾기 내비게이션"

- **목표를 주면 거기까지 가는 행동 순서를 스스로 계획**
- 예: 게임 캐릭터가 "적을 잡아라"는 목표를 받으면 → 무기 줍기 → 이동 → 공격 순서를 스스로 짬
- **대표 기술**: **STRIPS, GOAP, HTN Planning** (전부 "목표 → 행동 순서"를 계산하는 고전 알고리즘 이름. 이름만 알면 됩니다)
- **특징**
  - 행동 시퀀스(순서)를 **스스로 계획**
  - 게임·로봇·로직 기반 AI에 활용
  - **자연어는 아님** (사람 말을 알아듣지 못함. 정해진 기호로만 동작)
  - **현대 Agent Planner 구조의 뿌리** (오늘날 AI 에이전트가 "계획 세우기"를 하는 방식의 조상)

### ③ LLM-based Reactive Agent (반응형 LLM 에이전트) — "생각하고 도구를 쓰는 직원"

- ChatGPT 같은 **LLM이 사람 말을 이해하고, 생각한 뒤, 도구를 사용**
- 핵심 방식: **ReAct** (= Reasoning 생각 + Acting 행동, [8장](08-react-tool.html)에서 자세히)
- **대표 기술**: **ReAct, LangChain** (LangChain = LLM에 도구를 붙이기 쉽게 해주는 개발 도구)
- **특징**
  - **입력 → 추론 → 도구 사용** 흐름
  - **LLM 하나**가 도구 호출까지 전부 처리
  - **간단한 task loop 구조** (생각 → 행동 → 결과 보기 → 다시 생각)
  - **초기 LLM Agent의 핵심 틀**

### ④ Autonomous Agent (자율형 반복 에이전트) — "혼자 알아서 계속 일하는 직원"

- **목표 하나만 주면, 스스로 할 일 목록을 만들고, 하나씩 하고, 다시 목록을 고치고… 반복**
- **대표 기술**: **AutoGPT, BabyAGI, AgentGPT** (2023년 화제가 됐던 프로그램들)
- **특징**
  - 목표 설정 후 **작업 분해를 반복**
  - **외부 API, 파일 시스템 조작 가능** (진짜로 파일을 만들고 지우고 인터넷을 씀)
  - **실행 불안정성, 무한 루프 문제** ← 중요!
  - **"행동하는 AI" 인식의 분기점** (사람들이 "AI가 진짜로 일을 하네?" 하고 느낀 전환점)

{: .중요 }
> **"무한 루프 문제"가 뭔가요?**
> 스스로 일을 쪼개서 반복하다 보니, **"이제 다 끝났다"를 스스로 판단하지 못하고** 같은 검색을 계속 하거나 같은 파일을 계속 고치는 문제입니다.
> 비유: 시험공부를 하는데 **"완벽하게 정리하자"며 노트 정리만 무한 반복**하는 상황.
> 이 문제 때문에 뒤에서 **Loop Engineering(반복 제어), evaluator(평가자)** 같은 기술이 필요해집니다.

### ⑤ Multi-Agent / Graph-based Agent (역할 기반 협업) — "팀으로 일하는 회사"

- **여러 개의 AI가 각자 역할을 맡아 협업** (기획자 AI, 개발자 AI, 검토자 AI …)
- **대표 기술**: **AutoGen, LangGraph, CrewAI, Agentic RAG**
- **특징**
  - 여러 LLM이 **역할 분업 및 협업**
  - **그래프 기반 워크플로우 (LangGraph)**: 일의 흐름을 **순서도(그래프)** 로 그려서 관리
  - **직무 중심 구성 (CrewAI)**: "너는 작가, 너는 편집자" 처럼 **직업 단위**로 AI를 배치
  - **로깅 및 디버깅 도구와 통합**: 누가 무슨 일을 했는지 **기록(로그)** 이 남아 문제를 찾기 쉬움

{: .참고 }
> **Orchestration(오케스트레이션)** = 오케스트라 **지휘자**처럼 여러 에이전트를 **조율**하는 것.
> **상태 추적** = "지금 어디까지 진행됐는지"를 계속 기록하는 것.

### 원본 표 (그대로 외우기용)

| 에이전트 유형 | 주요 개념 | 대표 기술/프레임워크 | 특징 및 설명 |
|---|---|---|---|
| **Rule-based Agent** (규칙 기반 에이전트) | 조건-행동 규칙 기반 (**AI 적용 X**) (If-Then Rules) | Expert Systems, RPA (UiPath 등) | 입력에 정해진 규칙으로 반응 / 지능적 추론이나 적응 불가 / 사전 정의된 환경에서 안정 작동 / 여전히 일부 통제용 rule logic에 사용 |
| **Planning Agent** (계획 기반 고전 AI) | 목표 기반 행동 계획 (Task Planning) | STRIPS, GOAP, HTN Planning | 행동 시퀀스를 스스로 계획 / 게임·로봇·로직 기반 AI에 활용 / **자연어는 아님** / 현대 Agent Planner 구조의 뿌리 |
| **LLM-based Reactive Agent** (반응형 LLM 에이전트) | 자연어 추론 + 도구 사용 (**ReAct**) | ReAct, LangChain | 입력 → 추론 → 도구 사용 / 단일 LLM이 툴 호출 포함 처리 / 간단한 task loop 구조 / 초기 LLM Agent의 핵심 틀 |
| **Autonomous Agent** (자율형 반복 Agent) | 목표 → 계획 → 반복 실행 (**Loop 구조**) | AutoGPT, BabyAGI, AgentGPT | 목표 설정 후 작업 분해 반복 / 외부 API, 파일 시스템 조작 가능 / **실행 불안정성, 무한 루프 문제** / **"행동하는 AI" 인식의 분기점** |
| **Multi-Agent / Graph-based Agent** (역할 기반 협업 구조) | 역할 분리, 협업, 상태 추적 (Agent orchestration) | AutoGen, LangGraph, CrewAI, Agentic RAG | 여러 LLM 역할 분업 및 협업 / 그래프 기반 워크플로우 (LangGraph) / 직무 중심 구성 (CrewAI) / 로깅 및 디버깅 도구와 통합됨 |

{: .시험 }
> **예상 문제: "Rule-based Agent와 LLM-based Agent의 차이를 설명하시오"**
>
> **모범 답안**: Rule-based Agent는 사람이 미리 작성한 **If-Then 규칙**대로만 반응하므로, 규칙에 없는 상황에서는 **추론·적응이 불가능**하고 **새 도메인마다 규칙을 새로 만들어야** 한다. 반면 LLM-based Agent는 **자연어로 추론**하여 사전에 정의되지 않은 상황에도 대응할 수 있고, **도구를 호출**해 능력을 확장할 수 있다.

{: .시험 }
> **예상 문제: "Autonomous Agent의 한계를 쓰시오"**
>
> **모범 답안**: 목표를 스스로 하위 작업으로 분해해 반복 실행하는 구조이므로 **실행이 불안정**하고, 종료 조건을 스스로 판단하지 못해 **무한 루프**에 빠질 수 있다.

---

## AI Agent의 기본 구조 (이 과목의 뼈대) ★

**이 표가 학기 전체의 지도**입니다. 앞으로 나오는 모든 내용은 이 4개 중 하나를 깊게 파는 것입니다.

| 구성요소 | 사람에 비유하면 | 하는 일 | 자세히는 |
|---|---|---|---|
| **LLM Model** | **머리 (두뇌)** | 말을 이해하고 생각(추론)한다 | 2~6장 |
| **Tool / Public API** | **손, 발 (행동 도구)** | 실제로 검색하고, 계산하고, 예약한다 | 8장 |
| **DB / Memory** | **기억 (상태 저장)** | ▷ **Short term** (지금 하는 대화) ▷ **Long term** (예전 경험) | 9장, 11장 |
| **Planning** | **작업 계획** | 복잡한 목표를 **작은 단위 작업들로 분해** | 9장, 11장 |

**Planning 예시 (슬라이드 그대로)**

> **"웹사이트 만들어줘"** → `시장조사` → `구조설계` → `코드 작성` 등으로 분해

{: .참고 }
> **Short-term vs Long-term 메모리** 쉬운 예:
> - **Short-term**: 지금 친구와 대화하면서 "아까 네가 말한 그 식당" 하고 기억하는 것 (대화 끝나면 잊어도 됨)
> - **Long-term**: "이 친구는 매운 걸 못 먹는다"처럼 **오래 기억하는 것**

{: .시험 }
> **AI Agent의 4대 구성요소** — 가장 기본적인 단답·서술 문제입니다.
> **LLM(두뇌) / Tool·API(손발) / DB·Memory(기억, Short·Long term) / Planning(복잡한 목표를 작은 작업으로 분해)**
>
> 슬라이드 끝에 **"우리가 고민해봐야 할 사항들은 뭘까?"** 라는 질문이 있습니다. 답은 이 4개를 **어떻게 잘 설계하고 연결할까**이며, 그게 이 과목 전체의 내용입니다.

---

## AI Agent 파트 커리큘럼 (AI Agent 강의 자료 목차)

| No. | Contents | 이 노트 |
|---|---|---|
| 1 | AI 에이전트의 기초 개념과 정의 | [7장](07-ai-agent.html) |
| 2 | Cognitive Architectures 개론 및 Reasoning | [11장](11-cognitive-architecture.html) |
| 3 | ReAct & Agent Loop Engineering | [8장](08-react-tool.html) |
| 4 | Tool Use & Function Calling | [8장](08-react-tool.html) |
| 5 | Context Engineering | (학기 계획) |
| 6 | Memory & State Management | [9장](09-agent-structure.html), [11장](11-cognitive-architecture.html) |
| 7 | Single Agent Practice | [10장](10-agent-practice.html) |
| 8 | Harness & Graph Engineering | (학기 계획) |
| 9 | Multi-Agent Architecture | [12장](12-agent-architectures.html) |
| 10 | Multi-Agent / Subagents 실습 | [12장](12-agent-architectures.html) |
| 11 | 에이전트 평가와 벤치마킹 | (학기 계획) |

### 각 파트에서 배우는 것 (강의 안내 그대로)

**✓ AI Agent의 이해**

- **LLM과 에이전트의 근본적 차이점인 자율성(Autonomy) / 능동성(Proactivity)에 대한 이해**
  - 자율성 = 시키지 않아도 스스로 함 / 능동성 = 먼저 나서서 목표를 향해 움직임
- **LLM이 agent로 진화하기 위한 다층적 처리 구조**

**✓ Cognitive Architectures (인지 구조)**

- **AI Agent의 목표 달성을 위한 인지 구조 설계 필요**
- **기억(memory), 목표 및 계획 수립(Goal & Planning), 지각 및 행동 인터페이스(Perception & Action)로 구성**

**✓ LLM Reasoning (추론)**

- **큰 문제를 작은 단위로 분해하여 순차적으로 해결하는 과정**
- **Agent Reasoning의 추적 가능성 향상** (AI가 왜 그렇게 판단했는지 따라가 볼 수 있게)
- **Reasoning trace의 깊이와 폭을 모두 넓히는 방법론** (생각을 더 깊게, 더 다양하게)
- **구체적인 예시를 통해 새로운 도메인에 즉시 적용 가능한 능력**

**✓ Action (행동)**

- **Tool use를 위한 외부 API 도입** — **어떻게 도구를 정확히 호출할 것인가?**
- **RAG: 검색 기반 생성으로 할루시네이션 방지 및 Agent별 지식 베이스를 생성하고 업데이트**
  - 할루시네이션(hallucination) = AI가 **모르는 걸 그럴듯하게 지어내는 현상** ("환각")

**✓ ReAct**

- **ReAct = Reasoning + Action**
- **추론과 동시에 환경과 상호작용하는 Reasoning Agent**

**✓ Single- and Multi-Agent system**

- **광범위한 협업과 집단지능이 필요한 문제에서의 한계점 해결**
- **단일 시스템의 오버로드 방지 및 분산된 에이전트의 전문성 유지** (한 AI에게 일을 몰아주지 않고 나눠서 전문화)
- **Agentic AI**

**✓ 평가 & 벤치마크**

- **연속적인 상호작용 하에서 평가** (한 번 묻고 끝이 아니라, 여러 번 주고받는 상황에서 평가)
- **최종 목표 완수 여부 평가 및 동적 환경에서 적응적 의사결정 능력 검증**

{: .중요 }
> 위 표의 "(학기 계획)" 항목은 걱정하지 않아도 됩니다. 이 목록은 **학기 전체 계획**이고, 실제 배포된 강의 자료는 **Orientation / LLM / AI Agent 3개가 전부**입니다.
> **이 노트가 다루는 범위 = 중간고사 범위 전부**입니다.
