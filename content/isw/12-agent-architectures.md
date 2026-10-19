# 12. AI Agent 아키텍처 분류

## 이 장의 한 줄 요약

> **에이전트를 "혼자" 쓸까(Single), "여럿" 쓸까(Multi)? 여럿이면 "팀장이 있는 조직"(Vertical)일까 "다 같이 평등한 회의"(Horizontal)일까?**

```
AI Agent Architecture
 ├─ Single Agent Architecture        🧑            (혼자 다 함)
 └─ Multi-Agent Architecture
      ├─ Vertical Architecture       🧑            (팀장 1 + 팀원들)
      │                            ↗   ↖
      │                          🧑     🧑
      └─ Horizontal Architecture   🧑 ⇄ 🧑        (전원 평등)
                                     ↘ ↙
                                      🧑
```

---

## 1. 들어가며 — 연구적 관점 ★

{: .중요 }
> "Agentic AI 연구의 현황"을 묻는 문제에 그대로 쓸 수 있습니다.
>
> - **Agentic AI System의 방법론은 아직 표준화된 설계 정답이 없고, 성능/안정성 개선을 위한 지식이 상당히 empirical하게 축적됨**
> - **Cognitive Architecture의 개념이나 agentic system 필수 구성요소의 피상적인 논리와 필요성 자체는 매우 직관적**
> - **대표적인 설계 패턴 및 분류 소개와 Agent에 대한 연구적 관점에 초점을 두고자 함**

{: .참고 }
> **쉽게:**
> - **"정답 설계도가 아직 없다"** — 이렇게 만들면 무조건 좋다는 공식이 없음
> - **empirical(경험적)** = 이론보다 **"해 보니 이게 잘 되더라"** 식으로 지식이 쌓임
> - **피상적인 논리는 직관적** = "기억이 필요하다, 도구가 필요하다" 같은 건 **누구나 당연하게** 이해함
> - 그래서 강의는 **"대표적인 설계 패턴과 분류"** 를 소개하는 데 집중

(출처: ByteByteGo, "What Are AI Agents Really About?")

---

## 2. AI Agent is sort of a control system ★★

**"AI Agent는 일종의 제어 시스템이다"**

{: .시험 }
> - **단일 LLM의 추론 능력에 의존하는 것이 아닌, 신뢰 가능한 구조를 설계하고, 인간처럼 과업을 수행하는 것이 AI Agent의 목표**
> - **문제 해결의 자율적 수행을 위해 feedback loop를 포함한 재귀적인 구조의 Cognitive Architecture 설계가 필요**
>   - **Observation → Planning & Reasoning → Action → Observation** (+ **Reflection**)
> - 이를 기반으로 **performance / robustness / reliability / security의 개선**을 위해 시스템의 **structure / process / interface**를 구성

{: .참고 }
> **제어 시스템(control system)이 뭔가?**
> **에어컨**을 생각하세요. 온도를 **재고(관찰)** → 목표 온도와 비교해서 **판단하고** → 냉방을 **켜거나 끄고(행동)** → 다시 온도를 **재고** … 이렇게 **결과를 보고 계속 조절하는 시스템**입니다.
>
> AI Agent도 똑같이:
> ```
> Observation (관찰) → Planning & Reasoning (계획·추론) → Action (행동) → Observation (결과 관찰) → …
>                                     ↑______ Reflection (돌아보기) ______|
> ```
>
> **용어**
> - **feedback loop** = 결과를 다시 입력으로 돌려보내는 **순환 구조**
> - **재귀적** = 자기 자신을 **반복해서 다시 부르는** 구조
> - **Reflection** = 결과를 **돌아보고 반성**하는 단계
> - **performance**(성능) / **robustness**(견고성: 이상한 상황에도 잘 버팀) / **reliability**(신뢰성: 늘 일정하게 잘 작동) / **security**(보안)
> - **structure**(구조) / **process**(과정) / **interface**(연결 방식)
>
> 핵심 메시지: **"LLM 하나가 똑똑한 것"에 기대지 말고, "믿을 수 있는 구조"를 설계하라.**

(출처: Cobus Greyling, "WebVoyager AI Agent")

---

## 3. Architectural Designs — 분류와 필수 구성요소 ★★

### AI Agent Architecture의 분류

| 대분류 | 소분류 |
|---|---|
| **Single Agent Architecture** | — |
| **Multi-Agent Architecture** | **Vertical Architecture** / **Horizontal Architecture** |

### (거의) 필수 구성요소 ★

{: .시험 }
> 단답으로 나오기 아주 좋습니다.
> - **Components: LLM, tool, database**
> - **Process: reasoning, planning, tool calling**

| 종류 | 구성 | 쉬운 말 |
|---|---|---|
| **Components** (부품) | **LLM, tool, database** | 두뇌, 도구, 저장소 |
| **Process** (과정) | **reasoning, planning, tool calling** | 생각하기, 계획하기, 도구 부르기 |

{: .참고 }
> 1장의 **"AI Agent 기본 구조 4가지 (LLM / Tool / Memory / Planning)"** 와 같은 이야기입니다.

(출처: Masterman et al., 2024, *The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey*)

---

## 4. Single Agent vs Multi-Agent ★★★

{: .중요 }
> 이 장의 핵심 비교표입니다.

| 구분 | **Single Agent Architecture** | **Multi-Agent Architecture** |
|---|---|---|
| **정의** | **단일 언어모델이 모든 권한을 갖고 reasoning, planning, tool calling을 실행하는 agent** | **복수의 언어모델이 서로 다른 페르소나, 권한, 역할을 부여받고 서로 소통, 지시하며 협력적으로 과업을 수행하는 agent** |
| **피드백** | **타 모델로부터 피드백을 받을 수 없으나, 인간의 개입은 가능** | 여러 모델을 사용하면서 **불필요한 행동, 정보 누락 등 발생 가능** |
| **적합한 문제** | **문제가 잘 정의되어 있다면 하나의 모델이 모든 역할을 수행하는 것이 더 나을 수 있음** | **복잡하고 모호한 과업 수행에 상대적으로 더 적합** |
| **구성** | — | **다양한 구성이 가능하나, 크게 vertical/horizontal 구조로 분류** |
| **예시** | **ReAct, RAISE, Reflexion, AutoGPT+P, LATS** | **DyLAN, AgentVerse, MetaGPT** |

{: .참고 }
> **비유**
> - **Single** = **1인 사업자**. 기획·개발·영업을 혼자 다 함. 일이 단순하면 **오히려 빠르고 효율적**. 대신 **옆에서 "이거 틀렸어" 말해줄 동료가 없음** (사람이 봐줄 순 있음)
> - **Multi** = **회사**. 각자 역할이 있음. 복잡한 일엔 유리하지만, **소통 실수**(같은 일 두 번 하기, 정보 전달 누락)가 생길 수 있음
>
> **페르소나(persona)** = AI에게 부여한 **캐릭터·역할** ("너는 꼼꼼한 테스터야")
> **well-defined problem** = **문제가 명확하게 정해진** 문제 ("이 숫자들 정렬해" 같은)

---

## 5. Single Agent Architecture ★★

- **타 모델/유저의 피드백이 불필요한 well-defined problem에 대해서는 강점 有**
- **작업이 복잡해질수록 단일 모델이 모든 도구와 작업을 감당하기 어려움**

{: .시험 }
> **Single Agent의 한계 2가지**
> - **너무 많은 tool ⇒ 적절한 tool 선택의 난이도 상승**
> - **많은 subtask ⇒ 정보 혼재로 인한 성능 하락, workflow 생성/관리가 어려움**

{: .참고 }
> **쉽게**
> - **도구가 너무 많으면**: 공구함에 공구가 100개면 **"이 나사엔 뭘 써야 하지?"** 고르기가 어려워짐
> - **할 일이 너무 많으면**: 한 사람이 10가지 일을 동시에 하면 **정보가 뒤섞여서** 실수가 늘고, **일의 순서(workflow)** 를 관리하기 힘듦
>
> **subtask** = 큰 일을 쪼갠 **작은 일** / **workflow** = 일의 **흐름·순서**

### 사례: RAISE ★

(Liu et al., 2024, *From LLM to Conversational Agent: A Memory Enhanced Architecture with Fine-Tuning of Large Language Models*)

- **ReAct에 short/long memory mechanism을 추가**
- **특정 task들에서 기존 연구들에 비해 높은 성능**을 보임

**그러나…**

{: .중요 }
> - **복잡한 logic 이해를 어려워함**
> - **할루시네이션 발생**
>   - **세일즈를 시켰더니 Python 코드를 작성..**
>   - **복잡한 과업 하에서 부여된 역할을 헷갈리기 때문으로 추측**
>
> → **"Single Agent의 한계"를 보여주는 구체적 증거**로 쓰입니다.

{: .참고 }
> **세일즈(판매 상담)** 를 하라고 했더니 **갑자기 파이썬 코드**를 짠 것. 혼자서 너무 많은 역할을 맡다 보니 **"내가 지금 뭐 하는 역할이지?"** 를 헷갈린 것으로 보입니다.
> 이런 문제 때문에 **역할을 여러 에이전트에게 나누는 Multi-Agent**가 나옵니다.

---

## 6. Multi-Agent Architecture ★★★

- **복수의 LLM에게 페르소나, 역할, 권한을 부여하여 복잡한 과업을 협력적으로 수행하도록 함**
- **조직 구성의 두 극단을 Vertical Architecture, Horizontal Architecture로 분류 가능**

### Vertical vs Horizontal ★★★

{: .시험 }
> **이 장에서 가장 출제 확률이 높습니다.** 각각 특징을 외우세요.

| **Vertical Architecture** (수직) | **Horizontal Architecture** (수평) |
|---|---|
| **하나의 리더 agent에게 다른 모든 agent들이 보고하는 구조** | **모든 agent들이 평등하며, 집단적 논의를 통해 문제 해결** |
| **각 부하들은 리더와만 소통** | **공용 스레드에서 모든 소통을 수행하여, 모든 메시지 확인 가능** |
| **Agent들 간 분업이 매우 명확** | **리더로부터 과업을 부여받는 것이 아니라, 특정 task나 tool calling에 agent가 자원할 수 있음** |
| **리더와의 소통이 모두에게 공유되도록 설계도 가능** | |

```
   Vertical (수직)                     Horizontal (수평)

        🧑 리더                          🧑 ⇄ 🧑
       ↗    ↖                             ↘   ↙
     🧑      🧑                             🧑
   (팀원은 리더에게만 보고)            (전원이 한 방에서 다 같이 대화)
```

{: .참고 }
> **비유**
> | | Vertical | Horizontal |
> |---|---|---|
> | 조직 | **회사 조직도** (팀장-팀원) | **원탁 회의** / 단체 카톡방 |
> | 일 배정 | **팀장이 나눠줌** | **하고 싶은 사람이 손 듦** (자원) |
> | 소통 | 팀원 ↔ 팀장만 | **모두가 모든 메시지를 봄** |
> | 장점 | 분업이 명확, 통제 쉬움 | 다양한 의견, 집단지성 |
>
> **공용 스레드** = 모두가 같이 쓰는 **하나의 대화방** / **자원(自願)** = 스스로 하겠다고 나서는 것

### 프레임워크 스펙트럼 ★

실제 시스템들은 두 극단 사이 어딘가에 있습니다.

```
Vertical ●──────────────────────────────────────────────────● Horizontal
          ↑        ↑     ↑           ↑         ↑    ↑              ↑
        CrewAI  ChatDev MetaGPT    AutoGen  AgentVerse CAMEL      DyLAN
```

| 더 Vertical (수직 쪽) | 중간 | 더 Horizontal (수평 쪽) |
|---|---|---|
| **CrewAI, ChatDev, MetaGPT** | **AutoGen, AgentVerse, CAMEL** | **DyLAN** |

{: .시험 }
> **양 끝 대표 사례**: 수직 쪽 **MetaGPT** / 수평 쪽 **DyLAN** — 아래에서 자세히.

---

## 7. Vertical 사례: MetaGPT ★★

**"MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"** (Hong et al., 2023)

{: .시험 }
> **MetaGPT의 특징 3가지**
>
> 1. **Agent끼리의 무의미한 잡담(conversational noise)을 방지하기 위해 structured output을 강제**
> 2. **정보 공유에 "publish-subscribe" mechanism을 도입**
>    - **한 공간에 모든 정보를 공유하되, 각 agent의 목표 및 과업에 관련된 정보만 읽도록 유도**
>    - **Structured message에 포함된 메타 정보와 agent 정보를 매칭해서 관련된 정보를 연결** (i.e. subscription)
> 3. **수직적 업무 구조와 분업, 정보 흐름을 강제하므로 vertical architecture에 가까움**

### 하나씩 쉽게

**① Structured output 강제 — "보고서 양식 통일"**

{: .참고 }
> AI들끼리 자유롭게 대화하게 두면 **"좋은 생각이네요!" "저도 동의해요~"** 같은 **쓸데없는 말(잡담, noise)** 이 많아집니다.
> 그래서 **정해진 양식(structured output)** 으로만 말하게 합니다. 회사에서 **"보고는 이 양식으로만"** 하는 것처럼요.
> → 예: 기획자 AI는 반드시 "요구사항 문서" 양식으로, 개발자 AI는 "설계 문서" 양식으로

**② Publish-subscribe — "신문 구독"**

{: .참고 }
> - **Publish(발행)**: 모든 에이전트는 자기 결과를 **공용 게시판에 올림**
> - **Subscribe(구독)**: 각 에이전트는 **자기 일에 필요한 정보만 골라서 읽음**
>
> **비유:** 신문사는 모든 기사를 발행하지만, 독자는 **자기가 구독한 섹션(스포츠, 경제…)** 만 받아 봅니다.
>
> **왜 이렇게?** 모든 메시지를 다 읽으면 **정보가 너무 많아서** 헷갈리고 성능이 떨어집니다 (5절 Single Agent 한계와 같은 문제). 필요한 것만 읽게 해서 해결.
>
> **메타 정보** = 메시지에 붙은 **꼬리표** ("이건 설계 문서야, 개발자용"). 이걸 보고 누가 읽을지 매칭합니다.

**③ Vertical에 가까운 이유**

- **업무 구조가 수직적** (정해진 순서와 역할)
- **분업이 명확**
- **정보 흐름이 강제됨** (양식과 구독으로)

---

## 8. Horizontal 사례: DyLAN ★★

**"A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration"** (Liu et al., 2024)

{: .시험 }
> **DyLAN의 동작 — "round"와 "기여도 평가"가 핵심**
>
> - **공용 스레드에서 함께 과업을 수행 후, round마다 각 agent의 기여도를 평가, 기여도가 높은 agent만 다음 round 진출**
>   - **모든 모델이 각 1개의 메시지를 생성하는 것이 하나의 round**
>   - **기여도 평가는 별도의 LLM Ranker 또는 agent끼리의 peer rating**
> - **이를 반복하면서 팀 구성을 최적화**
> - **리더 없이 수평적으로 협력하여 수행한 후 성과 기반으로 멤버 재편이 이루어지므로, horizontal architecture에 매우 가까움**

### 쉽게

{: .참고 }
> **비유: 서바이벌 오디션 프로그램**
> ```
> Round 1: 에이전트 A, B, C, D, E 가 한 방에서 각자 의견 1개씩 냄
>          → 심사(LLM Ranker 또는 서로 점수 매기기)
>          → C, E 탈락 (기여도 낮음)
>
> Round 2: A, B, D 가 다시 각자 의견 1개씩
>          → 심사 → B 탈락
>
> Round 3: A, D 로 최종 팀 구성 ✅
> ```
>
> - **round** = 모든 참가자가 **한 번씩 말하는 한 바퀴**
> - **LLM Ranker** = 순위를 매기는 **별도의 심사위원 AI**
> - **peer rating** = 참가자끼리 **서로 점수 매기기** (동료 평가)
> - **Dynamic(동적)** = 팀 구성이 **고정되지 않고 계속 바뀜**

**Horizontal에 가까운 이유**
- **리더가 없음** (전원 평등)
- **공용 스레드**에서 모두 소통
- **성과에 따라** 멤버가 재편됨 (누가 시켜서가 아니라)

### MetaGPT vs DyLAN

| | **MetaGPT** | **DyLAN** |
|---|---|---|
| 구조 | **Vertical**에 가까움 | **Horizontal**에 매우 가까움 |
| 소통 | **Structured output 강제** + **publish-subscribe** | **공용 스레드**에서 자유롭게 |
| 팀 구성 | **고정된 역할 분업** | **round마다 기여도 평가 → 재편** |
| 핵심 아이디어 | 잡담 방지, 필요한 정보만 읽기 | 잘하는 에이전트만 남기기 |

---

## 이 장 정리

| | **Single Agent** | **Multi-Agent (Vertical)** | **Multi-Agent (Horizontal)** |
|---|---|---|---|
| **구조** | 모델 1개가 모든 권한 | **리더 1 + 부하 N** | **전원 평등** |
| **소통** | (타 모델 피드백 없음, 인간 개입만) | 부하는 **리더와만** | **공용 스레드**에서 전원, 모든 메시지 확인 |
| **과업 배정** | 혼자 다 함 | **리더가 분배**, 분업 매우 명확 | **agent가 자원** |
| **적합** | **well-defined 문제** | 복잡·모호한 과업 | 복잡·모호한 과업 |
| **단점** | tool 많으면 선택 어려움 / subtask 많으면 성능 하락·workflow 관리 어려움 | (역할 고정) | (통제 어려움) |
| **Multi 공통 단점** | | 불필요한 행동, 정보 누락 | 불필요한 행동, 정보 누락 |
| **예시** | **ReAct, RAISE, Reflexion, AutoGPT+P, LATS** | **CrewAI, ChatDev, MetaGPT** | **DyLAN**, AgentVerse, CAMEL |

**필수 구성요소**: Components = **LLM, tool, database** / Process = **reasoning, planning, tool calling**
