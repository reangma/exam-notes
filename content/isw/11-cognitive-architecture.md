# 11. Cognitive Architecture와 CoALA

## 이 장의 한 줄 요약

> **"사람이 생각하는 구조"를 본떠서 Agent를 설계하자. 그 설계도가 CoALA이고, 구성은 기억(Memory) · 행동(Action) · 의사결정(Decision-making) 3가지.**

```
CoALA = ① Memory (기억)          : Working + Semantic / Episodic / Procedural
        ② Action Space (행동)     : 외부 행동 + 내부 행동(Retrieval / Reasoning / Learning)
        ③ Decision-making (의사결정): Proposal → Evaluation → Selection → Execution
```

---

## 1. 예시로 시작 — 출장을 스스로 준비하는 AI Agent

> **"다음 주 화요일에 부산에서 고객님과 미팅을 해야 하는데, 지난달에 부산에 다녀온 스케줄대로 이동·숙박·일정 예약 모두 준비해줘."**

Agent Runtime 구조([7장](07-ai-agent.html))의 각 부분이 이렇게 생각합니다.

**① Profile, goals, Instructions (목표 이해)**

> 유저는 **정기적으로 출장을 다니는 직장인**이네.
> 다음 주 화요일 **부산에서 고객 미팅이 목적**이구나.
> **"지난달에 다녀온 스케줄대로"** 라고 했으니, **지난 출장 기록을 확인**해 봐야겠다.

**② Memory (기억 참조)**

> 지난달에는 **KTX 이동 + 숙박 포함** 일정이었고,
> 이번엔 **고객 미팅**이니까,
> 이동은 **여유 있게**, **미팅 일정 중심**으로 조금 더 **보수적으로** 조정해야겠다.

**③ Model-based Reasoning / Planning (계획 수립)**

> 지난달 출장 스케줄을 기준으로 이번 부산 고객 미팅 일정에 맞게 전체 흐름을 다시 짜야겠다.
> 먼저 **고객 미팅 시간을 확인**하고, 그 시간에 맞춰 **이동 시간을 역산**하자.
> 지난번처럼 **KTX 이동**이 가장 안정적일 것 같고, **미팅 전날 도착**하는 일정이 더 안전하겠다.
> 숙박은 **지난달 이용했던 호텔을 우선 확인**하되, 미팅 장소와 동선이 맞는지 다시 한번 점검하자.

**④ Tools (실행)**

```
calendar.get_event()        ← 캘린더에서 미팅 시간 확인
hotel.lookup(last_trip)     ← 지난 출장 때 호텔 조회
ktx.search()                ← KTX 표 검색
```

{: .참고 }
> **역산** = 거꾸로 계산하기. "미팅이 화요일 10시니까 → 월요일 저녁엔 도착해야 하고 → 그럼 월요일 오후 KTX…"
> **보수적으로** = 위험을 줄이는 쪽으로, 여유 있게
>
> 이 예시는 **목표 이해 → 기억 참조 → 계획 → 도구 실행** 순서를 보여줍니다. 이 구조를 **체계적으로 정리한 게 Cognitive Architecture** 입니다.

---

## 2. AI Agent의 발전 — 왜 "구조"가 필요해졌나 ★

(논문: **Cognitive Architectures for Language Agents**, *Transactions on Machine Learning Research*, 2024)

슬라이드는 같은 그림을 여러 장에 걸쳐 단계별로 강조하며 보여줍니다.

| 단계 | 구조 | 설명 |
|---|---|---|
| **1단계** | `Prompt construction → LLM → String parsing → Execution` | **LLM을 한 번 부르고 끝.** 프롬프트 만들기 → LLM 호출 → 결과 글 해석 → 실행 |
| **2단계** | **Self-Critique**: `Question → Answer → Critique → Refinement → Answer`<br>**Selection-Inference**: `Context + Question → Selection → Inference → Answer` | **LLM을 여러 번 엮음.** 답하고 → 스스로 비판하고 → 고치기 / 필요한 정보 고르고 → 추론하기 |
| **3단계** | **Inner Monologue**: `Environment / Human → VLM → Act`<br>**ReAct**: `Environment → Reason → Act` (루프) | **환경과 주고받는 Agent.** 환경을 보고 → 생각하고 → 행동 → 다시 환경 … |

그림 범례: **○ Input** (입력) / **□ LLM calls** (LLM 호출) / **둥근 사각형 = Chain / Agent**

{: .참고 }
> **용어**
> - **String parsing** = LLM이 쓴 **글(문자열)을 해석**해서 프로그램이 쓸 수 있게 만드는 것
> - **Critique** = 비평, **Refinement** = 다듬기
> - **Inner Monologue** = 속마음 독백. 로봇이 **"지금 이걸 보니 이렇게 해야겠다"고 속으로 말하며** 행동하는 방식
> - **VLM** (Vision-Language Model) = **그림도 볼 수 있는** 언어 모델
>
> **흐름 한 줄**: **LLM 한 번 호출 → 여러 번 엮어서 스스로 고치기 → 환경과 계속 주고받는 루프**
> 점점 **LLM 호출 하나하나는 "부품"이 되고, 그 부품을 어떻게 엮을지(구조)가 중요**해졌다는 이야기입니다.

{: .시험 }
> **Cognitive Architecture가 필요해진 이유 (서술형 소재 1순위)**
>
> - **LLM 기반의 Agent는 점점 복잡한 일을 수행하도록 발전해 왔음**
> - **과거 AI는 "Task를 잘 수행하기 위해 어떤 기능을 추가할 것인가"에 집중했다면,**
> - **현재는 "AI가 다양한 Task를 잘 수행하기 위해 어떤 구조로 시스템을 설계해야 하는가"를 고민**하게 되었음
> - → **Agent가 더욱 사람처럼 행동하도록 하기 위한 체계적인 Architecture 설계가 필요!**
> - → **Cognitive Architecture**

{: .참고 }
> **비유: 요리사**
> - **과거**: "칼질 기술 추가, 불 조절 기술 추가…" **기능을 하나씩 붙이기**
> - **현재**: "재료 손질 → 조리 → 플레이팅을 **어떤 순서와 체계로 운영**할까" **주방 시스템 설계**

---

## 3. Cognitive Architecture란? ★

Cognitive Architecture (인지 아키텍처)
: **인간이 정보를 인식하고, 기억하고, 추론하고, 행동을 결정하는 기본적인 구조**

- **심리학, 인지과학 분야에서 인간의 인지 과정을 체계적으로 모델링하기 위해** 도입
- 대표 인물: **Allen Newell (1927~1992)**, **Herbert Alexander Simon (1916~2001)**

{: .참고 }
> - **Cognitive(인지)** = 알고, 생각하고, 기억하는 정신 작용
> - **Architecture(아키텍처)** = 구조, 설계도
> - **모델링** = 복잡한 걸 **단순화한 모형**으로 만드는 것
>
> 즉 **"사람의 머리가 돌아가는 구조의 설계도"** 입니다. 원래 심리학 개념인데, AI Agent 설계에 가져온 것입니다.

### 인간의 인지 과정 (슬라이드 예시: 형사)

| 단계 | 형사의 머릿속 |
|---|---|
| **Observation** (관찰) | "…지금 범인이 웃은 거 맞나?" |
| **Perception** (지각) | (본 것을 "웃었다"는 정보로 인식) |
| **Memory** (기억) | "예전에 비슷한 사건에서, 범인이 안 들킨다고 확신하면 저런 표정을 지었었어." |
| **Reasoning** (추론) | "저 시간에 웃고 있었다는 건, 최소한 그때는 안전하다고 느꼈다는 뜻일 수도 있겠네." |
| **Action** (행동) | "비슷한 시간대에, 식당에서는 누가 있었는지 다시 한번 찾아봐야겠어." |

→ **Observation → Perception → Memory → Reasoning → Action**

### Cognitive Architecture for AI Agent

- **AI Agent가 더욱 인간처럼 동작하기 위해, Cognitive Architecture를 기반으로 시스템을 설계할 필요**
- **환경을 인지하고, 기억하고, 추론하며, 계획하고, 행동한 후 결과를 학습할 수 있어야 함**
- 논문에서 **기억, 행동, 의사결정이라는 세 가지 요소**를 통해 LLM 기반 Agent를 설계하는 프레임워크를 제안
- → **CoALA (Cognitive Architectures for Language Agents) 프레임워크**

---

## 4. CoALA 프레임워크 ★★★

**CoALA** = **Co**gnitive **A**rchitectures for **L**anguage **A**gents ("코알라"라고 읽음)

{: .시험 }
> **3가지 구성요소와 각각의 정의** — 이 장에서 가장 확실한 출제 포인트. 정의를 그대로 외우세요.

| 구성요소 | 정의 | 한 단어 |
|---|---|---|
| **① Memory Modules [기억]** | **에이전트가 과거의 경험, 지식, 현재의 정보 등을 저장하고 유지하기 위한 정보 저장 시스템** | **저장** |
| **② Action Space [행동]** | **에이전트가 외부 환경과 상호작용하거나, 내부 상태를 조절하기 위해 수행할 수 있는 모든 가능한 동작들의 집합** | **할 수 있는 것** |
| **③ Decision making [의사결정]** | **에이전트가 주어진 목표를 달성하기 위해, 어떤 행동을 선택하고 실행할지 결정하는 과정** | **고르기** |

### CoALA 구조도

```
  ┌───────────────────────────────────────────────────────────────┐
  │ Procedural Memory          Semantic Memory    Episodic Memory │
  │ [LLM] [Agent Code]           [DB 🛢]            [기록 📄]      │
  │  ↑Prompt ↓Parse ↓Retrieval ↑Learning  ↓Retrieval ↑Learning  ↓Retrieval ↑Learning
  │                                                               │
  │ ┌──────────────┐  ⇄  ┌──────────────────────────────────┐     │
  │ │  Decision    │     │        Working Memory            │     │
  │ │  Procedure   │     │        (⟲ Reasoning)             │     │
  │ └──────────────┘     └──────────────────────────────────┘     │
  └──────────────────────────↓ Actions ───── ↑ Observations ──────┘
                    [ Dialogue 🗣 ]  [ Physical 🌍 ]  [ Digital 💻 ]
                      (대화)           (물리 세계)      (디지털 세계)
```

{: .참고 }
> **그림 읽는 법**
> - 위쪽 3개 = **장기 기억** (Procedural / Semantic / Episodic)
> - 가운데 = **Working Memory** (지금 작업 중인 머릿속 메모장) — 여기서 **Reasoning(추론)** 이 일어남
> - 왼쪽 = **Decision Procedure** (무엇을 할지 결정)
> - 아래 = **바깥 환경** 3종류 (대화 상대 / 물리 세계 / 디지털 세계)
> - 화살표 **Retrieval** = 장기 기억에서 꺼내오기, **Learning** = 장기 기억에 저장하기
> - **Procedural Memory에 LLM이 들어 있다**는 점이 특이: LLM 자체가 "어떻게 하는지"를 담은 **절차적 기억**으로 취급됨

---

## 5. ① Memory Modules (기억) ★★★

**에이전트가 과거의 경험, 지식, 현재의 정보 등을 저장하고 유지하기 위한 정보 저장 시스템**

{: .시험 }
> **Short-term 1개 + Long-term 3개 = 총 4가지 메모리.** 이름과 정의 거의 확실히 출제됩니다.

| 구분 | 종류 | 정의 | 사람으로 치면 |
|---|---|---|---|
| **Short-term Memory** | **Working Memory** | **Working Memory로 불리며, 현재 처리하고 있는 정보를 저장하는 공간** | 지금 머릿속에 **잠깐 붙잡고 있는 것** (전화번호 외우며 누르기) |
| **Long-term Memory** | **Semantic** (의미 기억) | **세상에 대한 일반적인 사실, 개념, 학습된 지식을 저장하는 공간** | **"서울은 한국의 수도"** 같은 **지식** |
| | **Episodic** (일화 기억) | **과거에 경험했던 사건이나 상호작용을 저장하는 공간** | **"작년 생일에 친구랑 바다 갔지"** 같은 **경험** |
| | **Procedural** (절차 기억) | **특정 작업을 수행하는 방법이나 규칙(스킬)을 저장하는 공간** | **자전거 타는 법** 같은 **몸에 밴 방법** |

{: .중요 }
> **세 Long-term memory 구분 요령**
> | 종류 | 질문 | 예 |
> |---|---|---|
> | **Semantic** | **"그게 뭔데?"** (사실·개념) | 파스타 = 면 + 소스 |
> | **Episodic** | **"그때 어땠지?"** (경험·사건) | 전에 물이 적어서 실패했지 |
> | **Procedural** | **"어떻게 하더라?"** (방법·스킬) | 물 끓이고 → 면 넣고 → … |

### 사용 예시 — "친구 집에서 파스타를 만들자!" (사람: 한결이)

슬라이드는 이 예시를 한 장씩 쌓아 가며 보여줍니다.

**Working Memory** (지금 상황 — 단기 기억)

```
장소: 친구 집 주방
목표: 파스타 완성
정보: 가스레인지, 냄비 있음
상태: 배부름                    ← (나중 슬라이드에서 추가)
```

**Semantic Memory** — "파스타를 만들려면 뭐가 필요하지?"

```
파스타 = 면 + 소스
끓는 물이 필요
면은 물에 삶는다
소스는 토마토/크림/오일
파스타는 500원 크기 정도가 1인분    ← (추가)
```

**Episodic Memory** — "전에 파스타 만들 때 어땠지?"

```
물이 너무 적어서 면이 안 익었어
면을 먼저 삶으니 타이밍이 안 맞았어
친구 집에는 소금이 없었어
친구 집 가스불이 약해서 오래 걸려    ← (추가)
```

**Procedural Memory** — "뭐부터 해야 하지?"

```
냄비에 물 붓고, 가스불 켜고,
물 끓으면 소금 넣고 면 투입하고,
남은 시간 동안 소스를 만들자
불이 약하면 기다리는 동안 소스랑 다른 반찬도 같이 준비하자    ← (추가)
```

{: .참고 }
> **기억들이 서로 영향을 줍니다**
> - Working Memory에 "**배부름**"이 들어오자 → Semantic에서 "**1인분 양**" 지식을 떠올림 (조금만 만들자)
> - Episodic에 "**가스불이 약했다**"는 경험 → Procedural에서 "**기다리는 동안 다른 거 하자**"로 방법을 바꿈
>
> 이렇게 **4가지 기억이 함께 작동**해서 더 나은 행동을 만듭니다.

### 같은 예시 — Agent의 경우 (코드처럼 표현)

**Working Memory**

```
stove = detected        (가스레인지 = 감지됨)
pot = detected          (냄비 = 감지됨)
ingredients = unknown   (재료 = 모름)
```

**Semantic Memory**

```
pasta   = requires(noodle, sauce)      (파스타는 면과 소스가 필요)
noodle  = boiled_in(water)             (면은 물에 삶는다)
water   = heated_by(stove)             (물은 가스레인지로 데운다)
boiling = temperature > threshold      (끓는다 = 온도가 기준보다 높다)
```

**Episodic Memory**

```
Episode #42:  - env: tiny pot           - result: fail      (작은 냄비 → 실패)
Episode #82:  - env: hotel restaurant   - result: success   (호텔 주방 → 성공)
```

**Procedural Memory**

```
Skill: find_ingredients()     (재료 찾기)
Skill: boil_water()           (물 끓이기)
Skill: cook_noodle(time)      (면 삶기)
Skill: mix_sauce()            (소스 섞기)
```

{: .참고 }
> 사람의 기억을 **컴퓨터가 다룰 수 있는 형태**로 바꾼 것입니다.
> - Semantic → **사실 관계** (A는 B가 필요하다)
> - Episodic → **사건 기록** (번호, 환경, 결과)
> - Procedural → **함수(스킬)** 이름 — 실제로 실행할 수 있는 코드

---

## 6. ② Action Space (행동) ★★★

**에이전트가 외부 환경과 상호작용하거나, 내부 상태를 조절하기 위해 수행할 수 있는 모든 가능한 동작들의 집합**

{: .시험 }
> **외부 행동 1가지 + 내부 행동 3가지** — 분류와 정의가 핵심.

| 구분 | 종류 | 정의 | 예 |
|---|---|---|---|
| **외부 행동** (External Actions; **Grounding**) | — | **API 호출, 인간 혹은 다른 에이전트와의 대화, 인터넷 검색** 등 | 검색하기, 예약하기, 말하기 |
| **내부 행동** (Internal Actions; **Memory Access**) | **검색 (Retrieval)** | **장기 기억에서 정보를 검색해 Working Memory로 가져오는 행동** | "전에 파스타 어땠지?" 떠올리기 |
| | **추론 (Reasoning)** | **Working Memory의 내용을 처리하여 새로운 정보를 생성하는 행동** | "불이 약하니 오래 걸리겠다" 판단 |
| | **학습 (Learning)** | **새로운 정보를 Long-term memory에 저장하는 행동**<br>(예) **Episodic memory에 일화 추가**<br>(예) **LLM parameter update** | "이번엔 소금 챙겨서 성공!" 기억해 두기 |

{: .참고 }
> **방향으로 외우면 쉽습니다**
> ```
>                  Long-term Memory (장기 기억)
>                    │            ↑
>        Retrieval   │            │  Learning
>        (꺼내오기)   ↓            │  (저장하기)
>                  Working Memory (작업 기억)
>                    ⟲ Reasoning (안에서 가공하기)
> ```
> - **Retrieval**: 장기 **→** 작업
> - **Reasoning**: 작업 **→** 작업
> - **Learning**: 작업 **→** 장기
>
> **Grounding** = 생각을 **바깥 실제 세계에 연결**하는 것 → 그래서 외부 행동 = Grounding
> **LLM parameter update** = 모델 자체를 다시 학습시키는 것도 "학습" 행동의 일종

---

## 7. ③ Decision-making Process (의사결정) ★★★

**에이전트가 주어진 목표를 달성하기 위해, 어떤 행동을 선택하고 실행할지 결정하는 과정**

{: .시험 }
> **Planning Stage 3단계 (Proposal → Evaluation → Selection) + Execution Stage** — 순서까지 출제될 수 있습니다.

### Planning Stage (계획 단계)

| 단계 | 정의 | 쉬운 말 |
|---|---|---|
| **Proposal** (제안) | **LLM의 추론을 통해 하나 이상의 Action 후보를 생성** | **"할 수 있는 거 뭐 있지?"** 후보 내기 |
| **Evaluation** (평가) | **여러 Action 후보들의 가치를 평가** (**Heuristic, Simulation** 등을 이용) | **"각각 해보면 어떨까?"** 점수 매기기 |
| **Selection** (선택) | **평가된 행동 중 가장 좋은 Action을 선택**<br>**만족스러운 Action이 없는 경우 다시 Proposal 단계로 돌아갈 수 있음** | **"이게 제일 낫다!"** 고르기 (없으면 다시 후보 내기) |

### Execution Stage (실행 단계)

- **Planning Stage에서 선택된 행동(내부 or 외부)을 실행**하고, **환경으로부터 피드백을 받아 다음 cycle로 이동**

### 전체 흐름 (Decision Procedure 그림)

```
        Observation (관찰)
             ↓
   ┌──── Planning ────────┐
   │   ┌→ Proposal        │
   │   │      ↓           │
   │   │  Evaluation      │
   │   │      ↓           │
   │   └─ Selection       │  ← 마음에 드는 게 없으면 Proposal로 되돌아감
   └──────────┬───────────┘
              ↓
          Execution (실행)
              │
              └──→ 다시 Planning으로 (다음 cycle)
```

{: .참고 }
> **예: 점심 메뉴 고르기**
> 1. **Proposal**: "김치찌개, 파스타, 햄버거" 후보 생각
> 2. **Evaluation**: 김치찌개(어제 먹음, 3점) / 파스타(멀어, 5점) / 햄버거(가깝고 빨라, 8점)
> 3. **Selection**: 햄버거! (전부 별로였으면 → 다시 후보 생각)
> 4. **Execution**: 햄버거 가게로 가서 주문 → "품절이네?" (피드백) → 다시 Planning
>
> **Heuristic(휴리스틱)** = **경험상 대충 맞는 판단 규칙** ("가까운 게 보통 낫다")
> **Simulation(시뮬레이션)** = **머릿속으로 미리 해보기** ("파스타 가면 왕복 40분 걸리겠네")

---

## 8. Cognitive Architecture의 필요성 (정리) ★★

{: .시험 }
> 마무리 3문장 — 서술형 마지막 문단으로 쓰기 좋습니다.
>
> - **Cognitive Architecture를 통해 Agent가 더욱 인간처럼 행동해 복잡한 Task를 수행할 수 있음**
> - **CoALA 프레임워크를 통해 서로 다른 에이전트들이 세 가지 요소(기억, 행동, 의사결정)를 어떻게 사용하는지 분석 가능**
> - **이를 통해 각 에이전트 간 비교가 용이하며, 어떤 부분을 보완하거나 발전시킬 수 있을지에 대한 방향 제시 가능**

### CoALA로 기존 에이전트들을 분석한 표 (Table 2)

| 에이전트 | Long-term Memory | External Grounding | Internal Actions | Decision Making |
|---|---|---|---|---|
| **SayCan** (Ahn et al., 2022) | – | physical | – | evaluate |
| **ReAct** (Yao et al., 2022b) | **–** | **digital** | **reason** | **propose** |
| **Voyager** (Wang et al., 2023a) | procedural | digital | reason / retrieve / learn | propose |
| **Generative Agents** (Park et al., 2023) | episodic / semantic | digital / agent | reason / retrieve / learn | propose |
| **Tree of Thoughts** (Yao et al., 2023) | – | digital | reason | propose, evaluate, select |

**표 읽는 법**
- **Long-term Memory**: 어떤 장기 기억을 가졌나 (– = 없음)
- **External Grounding**: 어떤 외부 환경과 상호작용하나 (physical = 물리 로봇, digital = 컴퓨터, agent = 다른 에이전트)
- **Internal Actions**: 내부 행동 중 뭘 하나
- **Decision Making**: Proposal / Evaluation / Selection 중 뭘 하나

{: .중요 }
> 강의에서 **ReAct 행**에 빨간 박스를 치고 이렇게 적었습니다:
> **"Long-term memory ✗ / learning, retrieval ✗ / evaluate, select ✗"**
>
> 즉 **ReAct는**
> - **장기 기억이 없고**
> - 내부 행동 중 **reason(추론)만** 하고 **learning·retrieval은 안 하며**
> - 의사결정 중 **propose(제안)만** 하고 **evaluate·select는 안 한다**
>
> → **"CoALA로 분석하면 어떤 부분이 비어 있는지 보인다"** = 이 프레임워크의 가치. 이 예시가 그 증거입니다.

{: .참고 }
> **다른 에이전트 간단 소개**
> - **SayCan**: 구글의 **로봇** 에이전트 (physical). 할 수 있는 행동을 **평가**해서 고름
> - **Voyager**: **마인크래프트** 게임 에이전트. 배운 기술을 **procedural memory(스킬 라이브러리)** 에 쌓음
> - **Generative Agents**: 가상 마을에 사는 **25명의 AI 주민**. 일화·의미 기억을 가지고 서로 대화함 (agent)
> - **Tree of Thoughts**: 생각을 나무처럼 펼쳐 **제안·평가·선택을 모두** 함 ([8장](08-react-tool.html))

---

## 이 장 정리

| 구성요소 | 세부 | 핵심 |
|---|---|---|
| **필요성** | 과거: 기능 추가 → 현재: **구조 설계** | 사람처럼 행동하도록 |
| **정의** | 인간이 인식·기억·추론·행동 결정하는 기본 구조 | Newell, Simon |
| **① Memory** | **Working** (현재 처리 중) | Short-term |
| | **Semantic** (사실·개념·지식) / **Episodic** (경험·사건) / **Procedural** (방법·스킬) | Long-term |
| **② Action Space** | **External (Grounding)**: API, 대화, 검색 | |
| | **Internal (Memory Access)**: **Retrieval**(장기→작업) / **Reasoning**(작업 가공) / **Learning**(→장기) | |
| **③ Decision-making** | **Planning**: **Proposal → Evaluation → Selection** (불만족 시 Proposal로) | |
| | **Execution**: 실행 + 피드백 → 다음 cycle | |
| **분석 예** | **ReAct**: 장기 기억 ✗ / learning·retrieval ✗ / evaluate·select ✗ | |
