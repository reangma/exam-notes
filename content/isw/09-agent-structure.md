# 9. LLM 기반 Agent의 구조 (Perception–Brain–Action)

## 이 장의 한 줄 요약

> **Agent는 사람처럼 "보고(Perception) → 생각하고(Brain) → 움직인다(Action)". 이걸 계속 반복하는 게 단순 LLM과의 차이.**

이 장은 **"파리 여행 일정 짜줘"** 라는 하나의 예시가 처음부터 끝까지 이어집니다. **예시를 따라가면 구조가 저절로 외워집니다.**

```
"다음 주 파리 여행 일정을 짜줘"
   ↓
[Perception] 글을 받아들임
   ↓
[Brain]  ① 말 해석 → ② 배경지식 → ③ 사용자 기억 → ④ 추론·계획 → ⑤ (다음엔 LA도 응용)
   ↓
[Action] 최종 여행 일정표 출력
```

---

## 1. LLM-based Agent의 구조

- **LLM을 중심으로 자발적으로 환경과 지속적으로 상호작용하는 시스템**

두 가지 대표 그림이 함께 제시됩니다.

**(1) Google의 Cognitive Architecture (Agent Runtime)** — [7장](07-ai-agent.html)에서 본 그림

```
user_query → [ Agent Runtime: Orchestration(Profile·Memory·Reasoning/Planning) + Model + Tools ] → agent_response
```

(+ "A Survey on Large Language Model based Autonomous Agents" (Wang et al., 2024)의 LLM-based autonomous agent 구조도)

**(2) "The Rise and Potential of Large Language Model Based Agents: A Survey" (Xi et al., 2023)**

- **Perception – Brain – Action 모듈로 구성**

```
              ┌──────────── Perception ────────────┐
              │  Inputs: 이미지, 소리, 글, 위치 …    │
              │       → 벡터로 변환 [●●●●]          │
              └──────────────────┬─────────────────┘
                                 ↓
 Environment              ┌─── Brain ───────────────────────────┐
 "하늘 보니 내일 비 올까?   │ Storage:  Memory  │  Knowledge        │
  오면 우산 줘"            │      Summary·Recall  Learn·Retrieve │
      ↑                   │ Decision Making: Planning/Reasoning │
      │                   │ (Generalize / Transfer)             │
      │                   └──────────────────┬──────────────────┘
      │                                      ↓
      │                   ┌──────────── Action ────────────┐
      └───────────────────│ Text │ Tools(Calling API…) │ Embodiment │
  "날씨 예보 보니 내일      └────────────────────────────────┘
   비 올 듯. 우산 여기요"
```

### LLM-based Agent의 Workflow ★★

{: .시험 }
> **Perception → Brain → Action** 정의는 반드시 외우세요.

| 단계 | 정의 | 사람에 비유 |
|---|---|---|
| **1) Perception** (지각) | **외부 환경의 변화를 감지하고, multimodal 정보를 Agent가 이해할 수 있는 표현으로 변환** | **눈·귀** |
| **2) Brain** (두뇌) | **기억 / 추론 / 연산 / 의사결정 등의 정보 처리** | **뇌** |
| **3) Action** (행동) | **Agent의 결정을 수행** | **손·발·입** |

{: .중요 }
> **(단순 LLM과의 차이점)** **위 과정을 반복하면서, 지속적으로 피드백을 받고 환경과 상호작용**한다.
>
> | 단순 LLM | LLM-based Agent |
> |---|---|
> | 입력 → 출력 **한 번**으로 끝 | **보고→생각→행동→결과 보고→다시 생각…** **반복** |
> | 피드백 없음 | 환경에서 **피드백을 계속 받음** |

{: .참고 }
> **multimodal** = 여러 종류의 입력(글·이미지·소리)을 함께 다루는 것
> **"이해할 수 있는 표현으로 변환"** = 사진이나 소리를 **벡터(숫자)로 바꿔서** LLM이 처리할 수 있게 하는 것 (2장 임베딩과 같은 원리)

---

## 2. Perception Module (지각 모듈)

- **다양한 모달리티의 Inputs을 Brain Module(LLMs)이 이해할 수 있는 내부 표현으로 변환**

| 입력 종류 | 예 |
|---|---|
| **Textual Input** | 글 |
| **Visual Input** | 사진, 영상 |
| **Auditory Input** | 소리, 음성 |
| **(Future…)** | **촉각, 후각, 온도, 습도, 밝기** … (아직 미래 기술) |

**예시 입력**

> **"다음 주 파리 여행 일정을 짜줘. 항공, 숙소, 관광 일정까지 고려해야 해."**

**모달리티(modality)** = 정보의 **종류**(글, 그림, 소리 …)

---

## 3. Brain Module (두뇌 모듈) ★★

- **인간의 뇌와 마찬가지로, AI Agent의 중심 역할 수행 (LLMs으로 구성)**

### Brain의 Typology (5가지 구성) ★

{: .시험 }
> **① Natural Language Interaction ② Knowledge ③ Memory ④ Reasoning & Planning ⑤ Transferability & Generalization**

| # | 이름 | 한 줄 | 파리 예시에서 |
|---|---|---|---|
| ① | **Natural Language Interaction** | **말을 알아듣기** | "다음 주, 파리, 항공+숙소+관광" 해석 |
| ② | **Knowledge** | **배운 지식 쓰기** | "첫날은 피곤하니 가볍게" 같은 여행 상식 |
| ③ | **Memory** | **사용자 기억 쓰기** | "이 사용자는 여유로운 여행 좋아함" |
| ④ | **Reasoning & Planning** | **판단하고 계획 세우기** | "하루 관광지 2개로 제한, Day별 배치" |
| ⑤ | **Transferability & Generalization** | **다른 일에 응용하기** | "이번엔 LA 여행 짜줘"도 바로 해냄 |

---

### ① Natural Language Interaction (자연어 상호작용)

- **언어는 표면적인 정보뿐만 아니라, 화자의 의도/욕구/믿음 등의 숨은 정보를 내포**
- **LLMs은 강력한 자연어 이해(NLU) 및 생성(NLG) 능력을 갖추었음** → **Brain으로서의 역할 수행 가능**
- 기능: **Multi-turn 대화 처리, 고품질 문장 생성, Intent/Implication 해석** 등

{: .참고 }
> - **NLU** (Natural Language Understanding) = 말 **이해** / **NLG** (Natural Language Generation) = 말 **생성**
> - **Intent** = 의도 ("뭘 원하는가") / **Implication** = 함축, 숨은 뜻 ("말 안 했지만 원하는 것")
> - **Multi-turn** = 여러 번 주고받는 대화

**파리 예시 — 입력을 언어적으로 해석**

> "다음 주 파리 여행 일정을 짜줘. 항공, 숙소, 관광 일정까지 고려해야 해."

| 항목 | 해석 |
|---|---|
| 기간 | **다음 주** |
| 장소 | **파리** |
| 범위 | **항공 + 숙소 + 관광 일정** |
| **암묵적인 요구** | **실행 가능한 여행 일정 구성** (말은 안 했지만 "실제로 갈 수 있는" 일정이어야 함) |

→ **내부 표현**: **"다음 주 파리 여행의 여러 하위 task를 포함한 일정 계획 문제"**

---

### ② Knowledge (지식)

- **LLMs은 unstructured/unlabeled 데이터를 대량으로 학습**
- **이론적으로 모델의 파라미터가 늘어날수록, 더 많은 지식과 복잡한 패턴을 내재화할 수 있음**
- **Linguistic(언어) / Commonsense(상식) / Professional domain(전문 분야) 지식을 다양하게 학습**

{: .참고 }
> - **unstructured** = 표처럼 정리되지 않은 (그냥 글) / **unlabeled** = 정답이 안 붙은
> - **내재화** = 머릿속에 자기 것으로 담아 두는 것

**파리 예시 — LLM이 학습한 배경지식 활용**

(앞 단계 NLI 결과: "다음 주 파리 여행의 여러 하위 task를 포함한 일정 계획 문제")

| 지식 종류 | 내용 |
|---|---|
| **해외여행 일정 설계의 규칙** | 첫날/마지막 날은 이동 및 체력 소모가 크므로, **가벼운 일정** 구성 |
| **항공/시차 관련 상식** | 장거리 이동 후에는 **시차 적응** 필수이므로, 비행 후 일정을 유연하게 조정 |
| **숙소 체크인 관련 상식** | 숙소의 위치가 이동 효율에 큰 영향을 미치므로, **역 근처로 예약** |
| **주요 관광지 지식** | 대표 관광 구역을 **묶어** 여행자의 동선을 최적화 |

{: .참고 }
> **NLI** (Natural Language Inference) = 앞 단계에서 한 **자연어 해석의 결과**를 가리킵니다.

---

### ③ Memory (기억) ★

Memory
: **Agent의 과거 observations, thoughts, actions를 순차적으로 기록한 것**

- **(인간의 기억처럼) 과거의 경험을 활용하여 작업을 효율적으로 수행**

**파리 예시 — Agent의 경험 활용**

| 기억 종류 | 내용 |
|---|---|
| **사용자의 과거 여행 패턴** | ✓ 이전 여행에서, **하루에 관광지를 3개 이상** 넣었을 때 **피로도가 높았음**<br>✓ **'첫째 날은 숙소 근처만 돌아보자'** 는 요청이 있었음 |
| **사용자의 선호도** | ✓ 아침 일정은 **9시 이후**에 시작하는 것을 선호함<br>✓ 하루에 한 번씩은 **쇼핑, 자유시간**을 즐김 |

→ **결론: "사용자는 여유로운 여행을 선호하기에, 일정의 밀도를 낮출 필요가 있음"**

{: .참고 }
> **Knowledge vs Memory 차이**
> - **Knowledge**: **세상 일반**에 대한 지식 ("첫날은 피곤하다") — 누구에게나 해당
> - **Memory**: **이 사용자**에 대한 경험 기록 ("이 사람은 3개 넘으면 지침") — 이 사람에게만 해당

#### Memory의 두 가지 Challenge와 해결 방안 ★★

{: .시험 }
> **Challenge 2가지 + 해결 방안 2가지** — 전형적인 출제 포인트.

**Challenge (어려움)**

1. **Memory 데이터의 양이 방대함** (**Transformer 아키텍처의 제약 조건을 초과할 수 있음**)
2. **관련 Memory 추출의 어려움**

{: .참고 }
> **쉽게:**
> 1. 기억이 쌓이면 **너무 많아서** LLM이 한 번에 못 읽음 (LLM은 한 번에 읽을 수 있는 분량 = Context Window가 정해져 있음)
> 2. 기억이 많으면 **지금 필요한 걸 골라내기가 어려움** (일기장 10년 치에서 "파리 여행 때 기억"만 찾기)

**해결 방안**

| 구분 | 방법 | 쉬운 설명 |
|---|---|---|
| **1. Memory Capability 개선** (용량 늘리기) | ✓ **Transformer의 길이 제한 증가** (Text truncation, Segmenting Inputs 등) | 읽을 수 있는 분량을 늘리거나, 자르거나(truncation), 나눠서(segmenting) 넣기 |
| | ✓ **Memory 요약** (프롬프트 활용) | 긴 기억을 **짧게 요약**해서 저장 |
| | ✓ **벡터/데이터 구조를 사용한 메모리 압축** (임베딩 벡터 활용, DB 연동 등) | 기억을 **벡터로 바꿔 DB에** 저장 (2장 임베딩) |
| **2. Memory Retrieval 방안** (잘 찾기) | ✓ **Recency / Relevance / Importance 기반 자동 검색** (**높은 점수가 우선순위**) | **최근인가 / 관련 있나 / 중요한가** 점수로 골라 오기 |
| | ✓ **사용자 혹은 시스템이 메모리를 interactive하게 편집** | 사람이나 시스템이 **기억을 직접 고치고 지우기** |

{: .중요 }
> **Memory Retrieval의 3대 기준 — Recency / Relevance / Importance**
> | 기준 | 뜻 | 예 |
> |---|---|---|
> | **Recency** (최신성) | **최근 기억일수록** 높은 점수 | 어제 한 말 > 1년 전 한 말 |
> | **Relevance** (관련성) | **지금 질문과 관련 있을수록** | 파리 여행 질문엔 여행 기억이 우선 |
> | **Importance** (중요도) | **중요한 기억일수록** | "땅콩 알레르기 있음" > "점심에 김밥 먹음" |

---

### ④ Reasoning and Planning (추론과 계획) ★★

#### Reasoning (추론) 기법

| 기법 | 슬라이드 정의 | 쉬운 설명 |
|---|---|---|
| **Chain-of-Thought (CoT)** | **중간 추론 과정을 통해 최종 답변 생성** | 단계별로 풀기 ([6장](06-prompt-engineering.html)) |
| **+ Self-consistency** | **여러 추론 경로를 생성 → 일관된 답변 선택** | 같은 문제를 **여러 번 풀어보고 가장 많이 나온 답** 고르기 (다수결) |
| **+ Self-polish / Self-refine** | **출력 결과를 반복적으로 검토/수정** | 자기가 쓴 답을 **스스로 다시 보고 고치기** (퇴고) |
| **+ Selection-inference** | **여러 후보 추론 결과 중 가장 적절한 것을 선택** | 후보 여러 개 중 **가장 좋은 걸 골라서** 결론 내기 |

{: .참고 }
> **Self-consistency 예:** 수학 문제를 5번 풀었더니 답이 9, 9, 27, 9, 11 → **가장 많이 나온 9**를 정답으로.
> **Self-refine 예:** 글을 쓰고 → "어색한 데 없나?" 스스로 점검 → 고치기 → 다시 점검 …

**파리 예시 — Reasoning 과정 (3단계)**

**1. 입력 정보 종합**
- Knowledge: 첫날/마지막 날은 가벼운 일정, 이동 시간 고려할 것
- Memory: 사용자가 여유로운 여행 선호

**2. 충돌 요소 식별** (Agent가 논리적으로 판단)
- **파리는 많은 관광지 보유 중 vs. 사용자가 여유로운 일정 선호**
- → **모든 관광지를 넣는 것은 부적절함**

**3. 제약 조건 생성**
- 하루에: **핵심 관광지 2개 제한**, **이동이 많은 날이면 1개 제한**
- 첫날: **체력 소모를 고려하여 관광지 배제**

→ **Reasoning 결과: 사용자의 피로도를 최소화하면서, 여행 만족도를 높이는 문제 (일정 밀도 최소화 및 동선 최적화)**

#### Planning (계획) ★

- **앞선 작업을 기반으로 계획 수립**

{: .시험 }
> **Plan formulation vs Plan reflection**

| 구분 | 내용 | 쉬운 말 |
|---|---|---|
| **Plan formulation** (계획 수립) | **전체 작업을 하위 작업으로 분해**<br>방식: **One-shot (한 번에 계획), Step-by-Step, Hierarchical planning** … | **계획 짜기** |
| **Plan reflection** (계획 반성) | **수립된 계획을 feedback**<br>피드백 종류: **내부적, 인간, 환경 피드백** | **계획 점검·수정** |

{: .참고 }
> **계획 짜는 방식 3가지**
> - **One-shot**: 처음에 **전체 계획을 한 번에** 다 짬
> - **Step-by-Step**: **한 단계씩** 정하면서 진행
> - **Hierarchical (계층적)**: **큰 계획 → 중간 계획 → 세부 계획**으로 나무처럼 쪼갬
>
> **피드백 3종류**
> - **내부적**: 스스로 점검 ("이거 동선이 꼬였네")
> - **인간**: 사용자가 의견 ("Day 2는 너무 빡빡해요")
> - **환경**: 실제 결과 ("그날 루브르 휴관이래")

**파리 예시 — Planning 과정 (4단계)**

| 단계 | 내용 |
|---|---|
| **1. 일정을 시간축으로 분해** | Day 1: 도착일 / Day 2~3: 관광일 / Day 4: 귀국일 |
| **2. 관광지 후보 pool 구성** | 루브르 박물관, 오르세 미술관, 에펠탑, … |
| **3. 동선 기반 Clustering** | [루브르–오르세], [에펠탑–센강], [몽마르뜨–개선문], … |
| **4. Reasoning 결과 기반 배치** | Day 1: 도착 / Day 2: 루브르 → 오르세 / Day 3: 에펠탑 → 센강 / Day 4: 몽마르뜨 → 귀국 |

{: .참고 }
> **pool** = 후보 모음 / **Clustering** = 가까운 것끼리 **묶기** (가까운 관광지끼리 같은 날에)

**전체는 루프로 돕니다**

```
Decision → Action (Textual Output…) → Feedback → Memory Update → 다시 Decision …
```

(참고 논문: Madaan et al., 2023, **"SELF-REFINE: Iterative Refinement with Self-Feedback"**)

---

### ⑤ Transferability and Generalization (전이성과 일반화) ★

- **LLM-based Agents는 새로운 task에 신속하고 유연하게 적응할 수 있는 Dynamic Learning 능력 보유**

{: .시험 }
> 세 가지 능력 이름과 정의

| 능력 | 정의 | 쉬운 설명 |
|---|---|---|
| **Unseen task Generalization** | **Fine-tuning 없이 높은 zero-shot 성능** | **처음 보는 일**도 따로 안 배우고 해냄 |
| **In-context learning** | **Context 내 소수의 예시만으로 높은 학습 성능** | **예시 몇 개** 보고 바로 따라 함 ([4장](04-llm-gpt.html)) |
| **Continual learning** | **Forgetting 완화** | 새로 배워도 **예전 걸 잊지 않음** |

{: .참고 }
> **Forgetting(망각)** = 새 걸 배우면 예전 걸 까먹는 문제 (catastrophic forgetting이라고도 함)
> **Transferability(전이성)** = 한 곳에서 배운 걸 **다른 곳에 옮겨 쓰는** 능력

**파리 예시 확장**: **"이번에는 LA 여행 일정을 짜줘."**
→ **Knowledge + Memory(+파리 여행 경험) + Reasoning & Planning** 을 그대로 재사용해서 바로 해냄

---

## 4. Action Module (행동 모듈) ★

| 행동 종류 | 설명 |
|---|---|
| **Textual Output** | **글로 답변** |
| **Tool Using** | **Agent가 갖추기 어려운 능력을 보완** (API 호출, 이미지 생성 …) |
| **Embodied Action** | **(Futures) 물리적 환경과 상호작용** … (로봇 몸으로 움직이기, 미래 기술) |

**파리 예시 — AI Agent가 추천하는 최종 여행 계획**

```
Day 1: Arrival & Rest      • 파리 도착 → 체크인
                           • 휴식 및 주변 산책
                           • 카페에서 간단한 저녁

Day 2: Louvre & Orsay      • 오전: 루브르 방문
                           • 점심: 근처 식사
                           • 오후: 오르세 방문
                           • 저녁: 자유시간

Day 3: Flex Day            • 오전: 에펠탑 방문
                           • 점심: 근처 식사
                           • 오후: 쇼핑
                           • 저녁: 센강 산책

Day 4: Departure           • 오전: 체크아웃
                           • 점심: 기념품 구매
                           • 오후: 공항 이동 (충분한 buffer time)
```

{: .참고 }
> 결과를 보면 앞 단계가 다 반영돼 있습니다.
> - **Knowledge**: 첫날·마지막 날 가볍게, 공항 이동 시간 넉넉히 (buffer time = 여유 시간)
> - **Memory**: 하루 관광지 2개 이하, 쇼핑·자유시간 포함
> - **Planning**: 루브르–오르세처럼 가까운 곳끼리 묶음

### Tool Using 예시 — HuggingGPT (2023) ★

논문: **"HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face"** (Shen et al., 2023)

{: .시험 }
> **3단계 동작**
> 1. **사용자의 요청을 바탕으로 Task Planning**
> 2. **각 task에 대해 Hugging Face의 model card를 바탕으로 Model Selection**
> 3. **작업 수행 후 응답 생성**

**슬라이드 그림 (4단계로 그려져 있음)**

```
사용자: "Can you describe this picture and count how many objects in the picture?"
        (이 사진을 설명하고 물체가 몇 개인지 세줄래?)
                 ↓
┌─ LLM as Controller (ChatGPT) ─┐        ┌─ HuggingFace ─────────────────┐
│ Ⅰ Task Planning               │        │                               │
│ Ⅱ Model Selection  ───────────┼──→ Ⅲ Task Execution                    │
│                               │        │  • facebook/detr-resnet-101    │ (물체 찾기)
│ Ⅳ Response Generation ←───────┼── Prediction                          │
│                               │        │  • nlpconnet/vit-gpt2-image-captioning │ (사진 설명)
└───────────────────────────────┘        └───────────────────────────────┘
                 ↓
"A herd of giraffes and zebras grazing in a field. In addition, there are five detected objects:
 giraffe 99.9%, zebra 99.7%, zebra 99.9%, giraffe 97.1%, zebra 99.8% …"
(들판에서 풀을 뜯는 기린과 얼룩말 무리. 물체 5개 감지 …)
```

{: .참고 }
> **쉽게:** ChatGPT가 **지휘자(Controller)** 역할만 하고, 실제 일(사진 설명, 물체 찾기)은 **Hugging Face에 있는 전문 AI 모델들에게 맡깁니다.**
> - **Hugging Face** = AI 모델들을 모아 둔 **거대한 공개 저장소**
> - **model card** = 각 모델의 **설명서** ("나는 물체 찾기 모델이고 이런 걸 잘해")
> - ChatGPT가 설명서를 읽고 **"이 일엔 이 모델이 적합하겠다"** 고 고름
>
> → **LLM이 도구로 "다른 AI 모델"을 쓰는** 대표 사례

---

## 이 장 정리

| 모듈 | 하는 일 | 핵심 키워드 |
|---|---|---|
| **Perception** | 외부 변화 감지, multimodal → 내부 표현 | Text / Visual / Auditory / (촉각·후각…) |
| **Brain** | 기억·추론·연산·의사결정 | **① 자연어 상호작용 ② Knowledge ③ Memory ④ Reasoning & Planning ⑤ Transferability** |
| └ Memory | 과거 observation·thought·action 기록 | Challenge 2개 / **Recency·Relevance·Importance** |
| └ Reasoning | 추론 기법 | **CoT, Self-consistency, Self-refine, Selection-inference** |
| └ Planning | 계획 | **Plan formulation** (One-shot, Step-by-Step, Hierarchical) / **Plan reflection** (내부·인간·환경) |
| └ Transferability | 새 일에 적응 | **Unseen task Generalization / In-context learning / Continual learning** |
| **Action** | 결정 수행 | **Textual Output / Tool Using / Embodied Action** / 예: **HuggingGPT** |
| **차이점** | 단순 LLM과 다른 점 | **반복하며 지속적으로 피드백 받고 환경과 상호작용** |
