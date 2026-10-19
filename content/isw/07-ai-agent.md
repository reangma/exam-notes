# 7. AI Agent의 개념과 분류

## 이 장의 한 줄 요약

> **LLM은 "머리"만 있다. 여기에 손발(도구)·기억(메모리)·계획(planning)을 붙여서 "스스로 일하게" 만든 것이 AI Agent.**

여기서부터 과목 후반부입니다. 이 장에서 외울 비교표가 많으니, **"무엇과 무엇의 차이인가"** 를 중심으로 읽으세요.

| 비교 | 이 장의 절 |
|---|---|
| Agent vs AI Agent vs Agentic AI | 2절 |
| Model(LLM) vs Agent | 4절 |
| Text Agent ⊃ LLM Agent ⊃ Reasoning Agent | 5절 |
| LLM Agent vs Reasoning Agent | 6절 |
| LLM이 Agent에 적합한 4가지 성질 | 7절 |

---

## 1. Agent의 정의 ★

Agent (에이전트)
: **특정 환경과 상호작용할 수 있는 지능적인 시스템**

**Agent** 는 원래 "대리인"이라는 뜻입니다. 부동산 에이전트, 스포츠 에이전트처럼 **나 대신 일을 해주는 존재**죠.

### 환경의 종류

**환경(Environment)** = 에이전트가 **보고(관찰) 움직이는(행동) 대상 세계**

| 환경 | 예시 | 설명 |
|---|---|---|
| **물리적 환경** | 로봇 등 | 실제 세상에서 몸으로 움직임 |
| **디지털 환경** | 비디오 게임, 아이폰 | 컴퓨터 안의 세상 |
| **인간 환경** | 챗봇 | **인간을 환경으로 간주할 경우 챗봇도 일종의 에이전트** |

{: .참고 }
> **챗봇의 "환경"이 사람이라고?**
> 챗봇은 **사람의 말을 관찰**하고, **답변이라는 행동**을 합니다. 그러면 사람이 또 반응하죠. 이렇게 보면 **사람이 챗봇의 환경**입니다.

### Agent가 환경과 상호작용하는 방식

```
         Action (행동)
  Agent ──────────────→ Environment
        ←──────────────
       Observation (관찰)
```

- **Observation (관찰)**: 환경을 보고 정보를 얻음
- **Action (행동)**: 환경에 영향을 줌

{: .시험 }
> **정의의 필요 요소**: 에이전트를 정의하려면 **지능(Intelligence)** 과 **환경(Environment)** 을 정의해야 함.
> 상호작용 방식: **Action**과 **Observation**.
> (출처: Large Language Model Agent, UC Berkeley)

---

## 2. Agent vs AI Agent vs Agentic AI ★★★

{: .중요 }
> **이 장에서 가장 중요한 비교표.** 비교 서술형으로 나올 확률이 매우 높습니다.

### 먼저 한 줄씩

<figure class="fig" id="fig-agents3"><svg viewBox="0 0 740 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Agent AI Agent Agentic AI" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-agents3-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-agents3-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-agents3-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-agents3-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="8" y="8" width="232" height="214" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="124" y="36" font-size="16" fill="#4A5568">Agent</text><text x="124" y="92" font-size="38">🌡️</text> <text x="124" y="128" font-size="13">관찰 → 행동</text><text x="124" y="150" font-size="13">규칙·정책으로 반응</text><text x="124" y="172" font-size="12.5" fill="#8A93A3">LLM 없어도 됨</text> <text x="124" y="206" font-size="12" fill="#8A93A3">온도조절기 · 로봇청소기 · ELIZA</text> <rect x="254" y="8" width="232" height="214" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="370" y="36" font-size="16" fill="#1E3A6E">AI Agent</text><text x="370" y="92" font-size="38">🤖</text> <text x="370" y="128" font-size="13">LLM 두뇌 + 도구·메모리</text><text x="370" y="150" font-size="13">ReAct 루프로 task 수행</text><text x="370" y="172" font-size="12.5" fill="#8A93A3">똑똑한 직원 한 명</text> <text x="370" y="206" font-size="12" fill="#8A93A3">항공권 예약 · 코드 Copilot</text> <rect x="500" y="8" width="232" height="214" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="616" y="36" font-size="16" fill="#C77E16">Agentic AI</text> <g stroke="#CBD9EE" stroke-width="2"><path d="M616 72L571 104"/><path d="M616 72V104"/><path d="M616 72L661 104"/></g> <circle cx="616" cy="62" r="17" fill="#FBF0D8" stroke="#EBCF95"/><text x="616" y="67" font-size="11" fill="#C77E16">총괄</text> <g font-size="14"><circle cx="571" cy="110" r="14" fill="#EAF0FA"/><text x="571" y="115">🤖</text><circle cx="616" cy="110" r="14" fill="#EAF0FA"/><text x="616" y="115">🤖</text><circle cx="661" cy="110" r="14" fill="#EAF0FA"/><text x="661" y="115">🤖</text></g> <text x="616" y="150" font-size="13">여러 에이전트를 조율</text><text x="616" y="172" font-size="12.5" fill="#8A93A3">분해·분배·통합·재계획</text> <text x="616" y="206" font-size="12" fill="#8A93A3">연구 에이전트 · ChatDev · MetaGPT</text> </svg><figcaption>Agent(일하는 존재 전부) → AI Agent(LLM 두뇌의 한 명) → Agentic AI(팀장이 있는 팀)</figcaption></figure>

| 용어 | 한 줄 요약 | 비유 |
|---|---|---|
| **Agent** | **환경을 관찰·행동하는 개념** | **일하는 존재 전부** (로봇청소기 포함) |
| **AI Agent** | **LLM을 두뇌로 쓰는 개체** | **똑똑한 직원 한 명** |
| **Agentic AI** | **여러 에이전트를 조율하는 시스템** | **팀장이 있는 회사 전체** |

{: .참고 }
> **포함 관계로 생각하면 쉽습니다**
>
> - **Agent**: 가장 넓은 개념. 온도조절기도 "온도를 관찰하고 → 히터를 켜는 행동"을 하니 Agent입니다. **LLM이 없어도 됨.**
> - **AI Agent**: 그중에서 **LLM으로 생각하는** 것. 한 명이 **주어진 일을 처리**.
> - **Agentic AI**: AI Agent **여러 명을 팀으로 조직**해서, **큰 목표를 스스로 쪼개고 나눠 맡기는** 시스템.

### 상세 비교 (슬라이드 원본)

| 구분 | **Agent** | **AI Agent** | **Agentic AI** |
|---|---|---|---|
| **핵심 정의** | **환경을 관찰(Observation)하고 행동(Action)하는 지능적 시스템 전반** | **LLM으로 추론하고 도구·메모리를 활용해 주어진 목표를 수행하는 소프트웨어 개체** | **여러 에이전트·도구·메모리를 조율해 복잡한 목표를 자율 수행하는 시스템·설계 패러다임** |
| **의사결정** | **규칙·탐색·강화학습 정책** 등 (**LLM 없이도 구현 가능**) | **LLM 추론 + ReAct 루프** (Thought → Action → Observation) | **Orchestrator가 계획·분배**하고 **하위 에이전트의 결과를 통합·검증** |
| **목표·자율성** | **설계자가 정한 규칙·정책 범위 안에서 반응** | **사용자가 정한 목표를 task 단위로 수행** | **상위 목표를 스스로 하위 목표로 분해**하고, **실패 시 재계획** |
| **예시** | 온도조절기, 로봇청소기, ELIZA, 게임 NPC | 항공권 검색·예약 에이전트, 코드 작성 Copilot | 조사→실험→작성까지 수행하는 연구 에이전트, ChatDev·MetaGPT |
| **강의 연결** | Agent의 정의, Text Agent | ReAct, Reasoning Agent, Agent 구조 | Multi-Agent, Cognitive Architecture |

(출처: Russell & Norvig, *Artificial Intelligence: A Modern Approach* 4th ed., 2021 / Sapkota et al., 2025, *AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges*)

**용어 풀이**

| 용어 | 쉬운 뜻 |
|---|---|
| **탐색** | 가능한 경우를 다 따져보며 답 찾기 (체스 AI처럼) |
| **강화학습 정책** | 해보고 점수 받으며 배운 "이럴 땐 이렇게" 규칙 |
| **ReAct 루프** | **생각(Thought) → 행동(Action) → 결과 보기(Observation)** 반복 ([8장](08-react-tool.html)) |
| **Orchestrator** | **지휘자.** 일을 나눠 주고 결과를 모으는 총괄 에이전트 |
| **하위 목표로 분해** | "논문 써" → "자료조사 / 실험 / 글쓰기"로 쪼개기 |
| **재계획** | 하다가 실패하면 **계획을 다시 짜기** |
| **게임 NPC** | 게임 속 사람이 조종하지 않는 캐릭터 (상점 주인 등) |
| **ELIZA** | 1960년대 MIT의 규칙 기반 초기 챗봇 (5절) |
| **Copilot** | 코드를 대신 써주는 AI (GitHub Copilot 등) |
| **ChatDev·MetaGPT** | 여러 AI가 회사처럼 역할 나눠 소프트웨어를 만드는 시스템 ([10장](10-agent-practice.html), [12장](12-agent-architectures.html)) |

{: .시험 }
> **예상 문제: "AI Agent와 Agentic AI의 차이를 쓰시오"**
>
> **모범 답안**: AI Agent는 **LLM으로 추론하고 도구·메모리를 활용**하여 **사용자가 정한 목표를 task 단위로 수행하는 단일 소프트웨어 개체**이며, ReAct 루프(Thought→Action→Observation)로 의사결정한다. Agentic AI는 **여러 에이전트·도구·메모리를 조율**하는 **시스템·설계 패러다임**으로, **Orchestrator가 계획·분배하고 하위 에이전트의 결과를 통합·검증**하며, **상위 목표를 스스로 하위 목표로 분해하고 실패 시 재계획**한다.

---

## 3. AI Agent의 정의 ★★

{: .시험 }
> **번호 3개를 그대로 쓰는 문제**가 나오기 좋습니다.
>
> **인간이 설정한 목표를 달성하기 위해**
>
> 1. **LLM으로 추론을 실행하고**
> 2. **외부 도구(API, database)를 연동해 작업을 자동화하며**
> 3. **실시간 환경 변화에 따라 실행 계획을 동적으로 조정하는**
>
> **자율적 지능 시스템**

**쉽게 풀면**
1. **생각한다** (LLM)
2. **도구를 쓴다** (API로 검색·예약, DB로 기록 조회)
3. **상황이 바뀌면 계획도 바꾼다** (항공편이 매진되면 다른 날짜로)

{: .참고 }
> **"동적으로 조정"** = 미리 정한 대로만 하는 게 아니라, **진행하면서 상황에 맞게 바꾼다**는 뜻. 내비게이션이 길이 막히면 경로를 다시 짜주는 것처럼.

### 구성 요소 그림 (Stanford Webinar)

```
     ┌─────────┐        ┌──────────────────────┐
     │ Memory  │        │ Planning & Reasoning │
     └────┬────┘        └──────────┬───────────┘
          └──────────┬─────────────┘
                 ┌───┴───┐
                 │  LM   │   ← 두뇌
                 └───┬───┘
        Action ↓     │      ↑ Observation
              ┌──────┴───────┐
              │ Environment  │
              └──────────────┘
```

### AI Agent가 연결되는 4가지 (AI Agents – Build and Host LLM Apps At Scale)

AI Agent는 가운데서 **"NLP to understand prompt, generate task list + execute"** (사람 말을 이해하고 → 할 일 목록을 만들고 → 실행) 합니다.

```
                ① Any data or document         ② Code executor
                   (데이터·문서)                   (코드 실행기)
                 NLP/SQL query ↕ Response        Any code ↕ Execution response
                              \                  /
   User ──Prompt──→           [   AI agent   ]           ──→ Task output
                              /                  \
                 NLP query ↕ Relevant documents   Query ↕ Model response
                ④ Any LLM                       ③ Any ML model
                 (아무 LLM)                        (Forecasting, Optimization, Prediction,
                                                    Chat LLM, Other agent)
```

| # | 연결 대상 | Agent가 보내는 것 | 받는 것 |
|---|---|---|---|
| **①** | **Any data or document** (모든 데이터·문서) | **NLP/SQL query** (말 또는 DB 질의) | **Response** |
| **②** | **Code executor** (코드 실행기) | **Any code** | **Execution response** (실행 결과) |
| **③** | **Any ML model** (예측·최적화 모델, 챗봇, **다른 에이전트**) | **Query** | **Model response** |
| **④** | **Any LLM** (Claude, Llama, Gemini, ChatGPT 등) | **NLP query** | **Relevant documents** |

{: .참고 }
> **이 그림의 메시지**: Agent는 **특정 LLM이나 특정 DB에 묶이지 않습니다.**
> 어떤 데이터든, 어떤 모델이든, 심지어 **다른 에이전트(Other agent)** 까지 **도구처럼 갈아 끼울 수 있는 "중앙 관리자"** 입니다.
> **SQL** = 데이터베이스에 질문하는 언어. **ML model** = 머신러닝 모델.

---

## 4. Models vs AI Agents ★★

{: .시험 }
> **"LLM(모델)과 에이전트의 차이"** — 반드시 나오는 비교. **4개 항목**으로 외우세요.

| 구분 | **모델 (Models)** | **에이전트 (Agents)** |
|---|---|---|
| **지식 범위** | **학습 데이터에 포함된 지식으로 제한됨** | **도구를 통해 외부 시스템과 연결되어 지식이 확장됨** |
| **추론 방식** | 사용자 질문에 대한 **단일 추론/예측**. **별도 구현 없이는 채팅 기록 등 연속적 맥락 관리 불가** | **오케스트레이션 레이어에서 세션 기록을 관리**하여 **Multi-turn 추론** 수행 |
| **도구 구현** | **X** | **에이전트 아키텍처 내에 도구가 기본적으로 탑재됨** |
| **논리 계층** | **기본 로직 레이어 없음**. 사용자가 **직접 복잡한 프롬프트를 구성**해야 함 | **CoT, ReAct 또는 LangChain 같은 프레임워크를 사용하는 네이티브 Cognitive architecture 보유** |

(출처: Wiesinger, Marlow, Vuskovic, 2024, *Agents: The Next Frontier of AI*, Google Cloud)

**하나씩 쉽게**

| 항목 | 모델 | 에이전트 |
|---|---|---|
| **지식 범위** | **"작년까지 배운 것"만 앎.** 오늘 뉴스 모름 | **검색 도구로 오늘 뉴스도 찾아봄** |
| **추론 방식** | **한 번 묻고 한 번 답함.** 아까 한 말을 기억 못 함 | **대화 기록을 관리**해서 여러 번 주고받기 가능 (**Multi-turn**) |
| **도구** | 없음 | 계산기, 검색, 예약 시스템 등이 **기본 장착** |
| **논리 계층** | "어떻게 생각할지"를 **사용자가 프롬프트로 일일이** 지시 | "생각→행동→확인" 같은 **사고 방식이 내장**됨 |

{: .참고 }
> - **Multi-turn** = 여러 차례(turn) 주고받는 대화
> - **세션(session)** = 한 번의 대화 묶음
> - **오케스트레이션 레이어** = 대화 기록·도구 호출·순서를 **관리하는 층**
> - **네이티브(native)** = **처음부터 기본으로** 들어 있는

### Agent Runtime 구조 (Google Cloud) ★

이 그림은 9장·11장에서도 계속 나옵니다.

```
user_query  →  ┌──────────────── Agent Runtime ────────────────┐  →  agent_response
               │  ┌──────────── Orchestration ─────────────┐   │
               │  │  Profile, goals, & instructions        │   │
               │  │  Memory  (short-term / long-term)      │   │
               │  │  Model based Reasoning / Planning      │   │
               │  └────────────────────────────────────────┘   │
               │        [ Model ]              [ Tools ]       │
               └───────────────────────────────────────────────┘
```

| 부분 | 쉬운 뜻 |
|---|---|
| **Agent Runtime** | 에이전트가 **돌아가는 환경 전체** |
| **Orchestration** | **총괄 관리 층** |
| **Profile, goals, & instructions** | **"너는 누구고, 목표는 뭐고, 이렇게 행동해라"** 설정 |
| **Memory (short-term / long-term)** | **단기 기억** (지금 대화) / **장기 기억** (예전 기록) |
| **Model based Reasoning / Planning** | 모델로 **생각하고 계획** 세우기 |
| **Model** | LLM (두뇌) |
| **Tools** | 도구 (손발) |

### 동작 예시 — 항공권 예약 ★

사용자: **"I want to book a flight from Austin to Zurich."** (오스틴→취리히 항공권 예약하고 싶어)

```
Question:     "I want to book a flight..."            (질문 받음)
Thought:      I should search for flights...          (생각: 항공편을 검색해야겠다)
Action:       Flights Tool                            (행동: 항공편 도구 사용)
Action Input: Flights from Austin to Zurich           (도구에 넣을 값)
Observation:  The flight tool returns many options    (관찰: 여러 옵션이 나옴)
Thought:      I should present these to user...       (생각: 사용자에게 보여줘야겠다)
Final Answer: Here are some flights...                (최종 답변)
```

Tools: **Flights, Search, Code, Calc** 등

{: .참고 }
> 이 **Thought → Action → Action Input → Observation → … → Final Answer** 형식이 바로 **ReAct 루프**입니다 ([8장](08-react-tool.html)).

### 상황 예시 — 대학생의 자취방 전세 vs 월세 비교분석

> "내가 지금 학교 근처에서 **월세 70만원(보증금 1,000만원)** 에 살고 있는데, 2026년 현재 시행 중인 **청년 버팀목 전세자금대출**을 받아서 **1.5억원짜리 전세**로 옮기는 게 좋을까? 대출 금리랑 내 통장 잔고를 고려해서 **2년 동안 나가는 총 비용 차이**를 계산하면 좋을 것 같은데…"

에이전트의 처리:

| 순서 | 종류 | 내용 |
|---|---|---|
| 1 | **검색** | 청년 버팀목 전세자금대출 신청 자격 및 대출 금리 확인 |
| 2 | **추론** | 전세 이동 시 비용과 현 상태 비용의 비교 분석 |
| 3 | **계산** | Python을 활용한 계산 |

결과: *"2026년 현재 변경된 버팀목 금리 **2.1%** 를 적용하여 추론해본 결과, 전세로 옮길 시 월 이자는 약 **21만원**입니다. 기존 월세 70만원과 비교하여 파이썬으로 계산해보니, 2년간 이사 비용을 제외하고도 총 **1,120만원**을 절약할 수 있습니다. 적극 추천합니다."*

{: .중요 }
> 포인트: **검색(Knowledge) + 추론(Reasoning) + 계산(Computation)** 세 가지가 모두 필요.
> 이게 [8장](08-react-tool.html)의 **"Agent의 task 수행의 필요 요건 3가지"** 와 정확히 대응합니다.
>
> - 최신 금리는 LLM이 모름 → **검색**
> - 어느 쪽이 나은지 판단 → **추론**
> - 정확한 숫자 계산 → **Python 도구**

---

## 5. Agent의 분류 (3단계) ★★

<figure class="fig" id="fig-nested"><svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Text LLM Reasoning Agent 포함관계" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-nested-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-nested-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-nested-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-nested-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <ellipse cx="320" cy="135" rx="300" ry="120" fill="#F2EFE8" stroke="#E7E2D7"/> <ellipse cx="320" cy="152" rx="212" ry="84" fill="#EAF0FA" stroke="#CBD9EE"/> <ellipse cx="320" cy="172" rx="124" ry="46" fill="#FBF0D8" stroke="#EBCF95"/> <text x="320" y="42" font-size="15" fill="#4A5568">Text Agent</text><text x="320" y="60" font-size="12" fill="#8A93A3">관찰·행동이 모두 언어 (LLM 없어도 됨, 예: ELIZA)</text> <text x="320" y="94" font-size="15" fill="#1E3A6E">LLM Agent</text><text x="320" y="112" font-size="12" fill="#4A5568">LLM으로 행동 · 프롬프트 엔지니어링이 중요</text> <text x="320" y="166" font-size="15" fill="#C77E16">Reasoning Agent</text><text x="320" y="186" font-size="12" fill="#4A5568">스스로 생각·계획·검증 (ReAct)</text> </svg><figcaption>Text Agent ⊃ LLM Agent ⊃ Reasoning Agent (안으로 갈수록 더 똑똑함)</figcaption></figure>

{: .시험 }
> **Text Agent ⊃ LLM Agent ⊃ Reasoning Agent** — **포함 관계**(큰 원 안에 작은 원)로 그려져 있습니다.

```
┌────────────────── Text agent ──────────────────┐
│                                                │
│     ┌─────────── LLM agent ───────────┐        │
│     │                                 │        │
│     │    ┌──── Reasoning agent ───┐   │        │
│     │    │                        │   │        │
│     │    └────────────────────────┘   │        │
│     └─────────────────────────────────┘        │
└────────────────────────────────────────────────┘
```

### ① Text Agent

- 에이전트가 환경과 상호작용할 때, **관찰된 텍스트와 행동이 모두 언어로 이루어지는 경우**
- **LLM을 사용하지 않는 텍스트 에이전트는 AI 초창기부터 존재했음**

**예시: ELIZA**

- **MIT 인공지능 연구소에서 개발된 초기의 챗봇** (자연언어처리 컴퓨터 프로그램)
- **작동 방식: 룰 기반 (a bunch of rules)** 을 사용하여 작동

{: .참고 }
> **ELIZA는 어떻게 대화했나?** 상담사 흉내를 낸 프로그램인데, 규칙이 이런 식이었습니다.
> ```
> 규칙: 사용자가 "나는 ___가 슬퍼" 라고 하면 → "왜 ___가 슬프다고 생각하나요?" 라고 답하라
>
> 사용자: 나는 시험 때문에 슬퍼
> ELIZA : 왜 시험 때문에 슬프다고 생각하나요?
> ```
> 진짜 이해하는 게 아니라 **패턴 맞춰서 말을 돌려주는 것**뿐입니다.

**룰 기반 에이전트의 한계**

{: .시험 }
> 1. **규칙 설계가 매우 task-specific이며, 새로운 도메인마다 새로운 규칙 개발이 필요**
> 2. **규칙 기반은 단순한 도메인을 넘어서면 작동하지 않음**

### ② LLM Agent

- **텍스트 에이전트이면서 LLM을 사용하여 행동하는 에이전트**
- **LLM: Input을 기반으로 다음 token을 예측하는 모델**

{: .중요 }
> **LLM ≠ LLM Agent**
>
> - **LLM**: 그냥 **다음 단어를 예측하는 모델** (엔진)
> - **LLM Agent**: 그 모델을 이용해 **환경에서 행동하는 주체** (엔진을 단 자동차)

**LLM이 하는 일 (슬라이드 수식)**

```
S = "Where are we going"

        Previous words (Context)   Word being predicted
               ↓                        ↓
P(S) = P(Where) × P(are | Where) × P(we | Where are) × P(going | Where are we)
```

**읽는 법** ([0장](00-math-basics.html) 4절)

- `P(are | Where)` = "Where 다음에 are가 올 확률"
- 문장 전체 확률 = 각 단어가 **앞 단어들 다음에 올 확률을 전부 곱한 것**
- **앞 단어들 = Context(문맥)**, **맞히려는 단어 = Word being predicted**

### ③ Reasoning Agent

- **LLM을 기반으로 다양한 추론(Reason)들을 수행하여 행동하는 에이전트**

슬라이드 질문: **"LLM Agent vs Reasoning Agent 둘의 차이가 무엇인지..?"** → 다음 절

---

## 6. LLM Agent vs Reasoning Agent ★★

### 배경

- **2020년경 LLM의 등장**: GPT-3를 시작으로 LLM이 등장하며 새로운 움직임 시작
- **LLM의 두 가지 Task**

| Task | 예 | 관련 기법 |
|---|---|---|
| **Reasoning Tasks** (추론) | Question Answering 등 | **CoT, Zero-shot CoT, Self-consistency** … |
| **Acting Tasks** (행동) | 게임, 로보틱스 등 | **Game, Robotics, RAG** … (**Grounding, tool use** 등) |

{: .참고 }
> - **Grounding(그라운딩)** = AI의 말을 **실제 세상(외부 정보·행동)에 연결**하는 것. 머릿속 생각을 현실에 "땅에 붙인다"는 뜻
> - **Self-consistency** = 여러 번 풀어보고 **가장 많이 나온 답**을 고르는 방법 ([9장](09-agent-structure.html))
> - **Zero-shot CoT** = 예시 없이 "**단계별로 생각해보자**"라는 말만 붙여서 CoT 효과를 내는 방법

### 발전 흐름

```
                    LLM
           ┌─────────┴─────────┐
       Reasoning             Acting
  (CoT, Zero-shot CoT,   (Game, Robotics, RAG …
   Self-consistency …)    / Grounding, tool use)
           │                   │
           │      LLM agent (but not reasoning agent)
           └─────────┬─────────┘
                   ReAct          ← 둘을 합침!
                     │
              Reasoning agent
           ┌─────────┴─────────┐
  New applications/          New methods
  tasks/benchmarks           (Memory, learning,
  (Web browsing,              planning, multi-agent …)
   Software engineering,
   Scientific discovery …)
```

### 핵심 차이 ★★

{: .시험 }
> - **LLM Agent** → **프롬프트 엔지니어링의 중요성 증대**
> - **Reasoning Agent** → **목표만 주어지면 알아서 단계별로 생각하고 검증하는 능력 탑재 (인지적 제어 수행)**

**쉽게 풀면**

| | LLM Agent | Reasoning Agent |
|---|---|---|
| 비유 | **시키는 대로만 잘하는 신입** | **알아서 생각하고 확인하는 경력직** |
| 잘하게 하려면 | 사람이 **지시를 잘 써줘야 함** (프롬프트 엔지니어링) | **목표만 주면 됨** |
| 하는 일 | 행동은 하지만 깊이 생각하진 않음 | **생각(추론) → 계획 → 스스로 오류 검증 → 행동** |

{: .참고 }
> **인지적 제어(cognitive control)** = 자기 생각을 **스스로 점검하고 조절**하는 능력. "잠깐, 이거 맞나? 다시 확인해보자" 하는 것.

### ReAct와 Reasoning Agent

- **ReAct: Reasoning task와 acting task를 반복적으로 수행하여 문제를 해결하는 방법** → **Reasoning Agent로 확장**
- **Reasoning Agent → "생각(추론)하고, 계획을 세우며, 스스로 오류를 검증"한 후 행동하는 에이전트**

**Reasoning Agent 이후 연구는 두 방향으로 발전**

1. **응용 분야 확장**: 웹 상호작용, 엔지니어링, 과학적 발견 등
2. **새로운 방법론 탐색**: **memory, learning, planning, multi-agent** 등

**예시 (대학원생의 자취방 전세 vs 월세 비교분석)**: 앞 절과 같은 질문을 Reasoning Agent가 처리하면, **검색(Act) → 추론(Reasoning) → 계산(Act)** 을 번갈아 하며 답을 만듭니다. 생각과 행동이 **번갈아 반복**되는 것이 핵심입니다.

---

## 7. LLM이 AI Agent에 적합한 이유 — 4가지 성질 ★★★

<figure class="fig" id="fig-4props"><svg viewBox="0 0 740 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="LLM이 Agent에 적합한 4가지 성질" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-4props-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-4props-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-4props-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-4props-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <g text-anchor="start"> <rect x="10" y="10" width="355" height="110" rx="14" fill="#EAF0FA" stroke="#CBD9EE"/> <text x="28" y="42" font-size="16" fill="#1E3A6E">🧭 자율성 Autonomy</text><text x="28" y="70" font-size="13">스스로: 행동·내부 상태의 통제권</text><text x="28" y="96" font-size="12.5" fill="#4A5568">LLM: 단계별 지침 없이도 작업 수행</text> <rect x="375" y="10" width="355" height="110" rx="14" fill="#E4F2EA" stroke="#BFE0CC"/> <text x="393" y="42" font-size="16" fill="#2E7D55">⚡ 반응성 Reactivity</text><text x="393" y="70" font-size="13">대응: 환경 변화에 신속히</text><text x="393" y="96" font-size="12.5" fill="#4A5568">LLM: Multi-modal(지각↑) + Embodiment·Tool(행동↑)</text> <rect x="10" y="130" width="355" height="110" rx="14" fill="#FBF0D8" stroke="#EBCF95"/> <text x="28" y="162" font-size="16" fill="#C77E16">🎯 능동성 Pro-activeness</text><text x="28" y="190" font-size="13">주도: 목표 지향 행동을 먼저</text><text x="28" y="216" font-size="12.5" fill="#4A5568">LLM: next token prediction → 추론·계획</text> <rect x="375" y="130" width="355" height="110" rx="14" fill="#FBE9E7" stroke="#EFC4C1"/> <text x="393" y="162" font-size="16" fill="#C0463F">💬 사회성 Social ability</text><text x="393" y="190" font-size="13">소통: 다른 에이전트와 상호작용</text><text x="393" y="216" font-size="12.5" fill="#4A5568">LLM: NLU · NLG (사람이 읽을 수 있는 말)</text> </g> </svg><figcaption>자·반·능·사: 스스로 / 대응 / 주도 / 소통</figcaption></figure>

{: .시험 }
> **자율성 / 반응성 / 능동성 / 사회성** — 이름, 정의, **LLM의 어떤 능력이 그걸 가능하게 하는지**까지 세트로. 서술형 1순위입니다.

| 성질 | 정의 | LLM이 이를 만족하는 이유 |
|---|---|---|
| **자율성 (Autonomy)** | 에이전트가 **자신의 행동 혹은 내부 상태에 대한 통제권을 보유** | LLM이 **상세한 단계별 지침이 없어도, 인간과 유사한 텍스트를 생성하고 다양한 작업을 수행**함 → 자율성 |
| **반응성 (Reactivity)** | **환경의 변화에 신속하게 대응할 수 있는 능력** | **Multi-modal fusion** 기술로 LLM의 **지각 공간을 확장** (시각, 청각 정보 처리 가능) / **Embodiment 기술, Tool 사용**을 바탕으로 LLM의 **행동 공간을 확장** → 반응성 |
| **능동성 (Pro-activeness)** | 에이전트가 **주도적으로 목표 지향적인 행동을 수행하는 능력** | LLM의 **next token prediction 패러다임**을 바탕으로, **일반화된 추론 능력과 계획 능력**을 보임 → 능동성 |
| **사회성 (Social ability)** | 에이전트가 (**agent-communication language를 통해**) **다른 에이전트와 상호작용하는 능력** | **NLU, NLG**를 바탕으로 **모델 혹은 인간이 해석 가능한 방식으로 상호작용** 가능 → 사회성 |

### 하나씩 쉽게

**① 자율성 — "시키지 않아도 스스로"**
- 하나하나 "1번 해, 2번 해" 지시하지 않아도 **알아서 일을 처리**
- LLM은 "보고서 써줘" 한마디에 **구조 잡고 내용 채우는 걸 스스로** 함

**② 반응성 — "상황이 바뀌면 바로 대응"**
- **지각 공간 확장** (보고 듣는 범위 넓히기): **Multi-modal fusion** = 글뿐 아니라 **이미지·소리**도 함께 처리
- **행동 공간 확장** (할 수 있는 행동 넓히기): **Embodiment**(로봇 몸 달기) + **Tool**(도구 사용)

**③ 능동성 — "목표를 향해 먼저 움직임"**
- 반응만 하는 게 아니라 **목표를 이루려고 먼저 계획하고 행동**
- LLM은 다음 단어 예측을 엄청 많이 학습하면서 **추론·계획 능력**이 생김

**④ 사회성 — "다른 존재와 소통"**
- **다른 에이전트나 사람과 대화하며 협력**
- **NLU** (Natural Language Understanding, 자연어 **이해**) + **NLG** (Natural Language Generation, 자연어 **생성**) 능력 덕분에 **사람이 읽을 수 있는 말로** 소통 가능

{: .참고 }
> **외우는 요령: 자·반·능·사**
>
> | 성질 | 키워드 | 한 단어 |
> |---|---|---|
> | **자**율성 | 통제권, 단계별 지침 없이 | **스스로** |
> | **반**응성 | 지각 공간(Multi-modal) + 행동 공간(Embodiment, Tool) | **대응** |
> | **능**동성 | next token prediction → 추론·계획 | **주도** |
> | **사**회성 | agent-communication language, NLU·NLG | **소통** |

{: .중요 }
> **반응성 vs 능동성 헷갈리지 않기**
>
> - **반응성**: 환경이 **바뀌면 → 대응** (수동적, 바깥에서 시작)
> - **능동성**: **목표가 있으니 → 먼저 행동** (주도적, 안에서 시작)
