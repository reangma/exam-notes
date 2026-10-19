# 5. Adaptation Tuning

## 이 장의 한 줄 요약

> **GPT-3는 똑똑했지만 ① 말을 안 듣고 ② 위험한 말도 하고 ③ 고치려면 돈이 너무 많이 들었다. 그걸 고치는 3가지 방법.**

| 문제 | 해결 방법 | 한 줄 |
|---|---|---|
| ① 질문에 답을 안 하고 엉뚱한 말을 이어 씀 | **Instruction Tuning** | **말 알아듣게** 만들기 |
| ② 거짓말, 욕설, 편견 섞인 말을 함 | **Alignment Tuning (RLHF)** | **착하고 정직하게** 만들기 |
| ③ 모델이 너무 커서 고치는 비용이 큼 | **PEFT (Adapter, LoRA) + Quantization** | **싸게** 고치기 |

---

## 1. 전체 지도 — Training Process of LLMs ★★

<figure class="fig" id="fig-stages"><svg viewBox="0 0 740 175" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="LLM 학습 3단계" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-stages-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-stages-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-stages-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-stages-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <polygon points="10,30 230,30 250,85 230,140 10,140" fill="#F2EFE8"/> <polygon points="250,30 470,30 490,85 470,140 250,140 270,85" fill="#FBF0D8"/> <polygon points="490,30 730,30 730,140 490,140 510,85" fill="#EAF0FA"/> <text x="120" y="62" font-size="15" fill="#142A52">① Pre-training</text><text x="120" y="86" font-size="13" fill="#4A5568">기본 능력 습득</text><text x="120" y="110" font-size="11.5" fill="#8A93A3">Data · Architecture · Task · 최적화</text> <text x="375" y="62" font-size="15" fill="#C77E16">② Adaptation Tuning</text><text x="375" y="86" font-size="13" fill="#4A5568">목표에 맞게 추가 적응</text><text x="375" y="110" font-size="11.5" fill="#8A93A3">Instruction · Alignment · PEFT</text> <text x="615" y="62" font-size="15" fill="#1E3A6E">③ Utilization</text><text x="615" y="86" font-size="13" fill="#4A5568">효과적으로 사용</text><text x="615" y="110" font-size="11.5" fill="#8A93A3">Prompt Engineering (6장)</text> <text x="370" y="166" font-size="12.5" fill="#4A5568">GPT-1~3은 ①로 성능 확보 → InstructGPT·ChatGPT는 ②로 성능 확보</text> </svg><figcaption>Training Process of LLMs: 이 장(5장)은 ②, 다음 장(6장)은 ③</figcaption></figure>

> **"우수한 LLM 구축에는 거대한 모델과 다량의 데이터뿐만 아니라 다양한 학습 기법을 효과적으로 활용하는 것이 매우 중요"**

LLM이 만들어지는 과정은 **3단계**입니다.

| 단계 | 정의 | 포함 내용 | 비유 |
|---|---|---|---|
| **① Pre-training** | **LLM의 기본적인 능력을 습득하는 과정** | Data / Architecture / Pre-training task / Optimization and Scalable Training Techniques | **초·중·고 교육** (기본기) |
| **② Adaptation Tuning** | **LLM을 특정한 목표에 따라 추가로 adaptation 시키는 과정** | **Instruction tuning / Alignment Tuning / Parameter efficient model adaptation** | **직무 교육·예절 교육** |
| **③ Utilization** | **LLM을 효과적으로 사용하는 방법** | **Prompt Engineering** | **일 잘 시키는 법** (6장) |

{: .시험 }
> **3단계 이름과 각각의 정의**, 그리고 **Adaptation Tuning에 속하는 3가지**를 외우세요. (슬라이드에서 ②③에 빨간 박스 = 이 장과 다음 장의 범위)

### Adaptation Tuning이란?

**Adaptation** = 적응. **이미 다 배운 모델을 특정 목적에 맞게 "적응"시키는 것.**

- 다양한 task에서 **사전 학습된 LLM을 효과적으로 더 잘 사용하기 위해 adaptation 시키는 작업**
- **GPT-1, GPT-2, GPT-3까지는 pre-train을 통해** 그 성능을 확보했다면,
- **GPT-3에서부터 InstructGPT, ChatGPT까지는 adaptation tuning을 통해** 성능을 확보하기 시작함
- **GPT-3에서 ChatGPT로의 중요한 변화는 adaptation tuning의 수행**으로 볼 수 있음

Adaptation Tuning의 3가지 (순환 그림):

> **1. Instruction Tuning → 2. Alignment Tuning → 3. Parameter Efficient Model Adaptation**

---

## 2. Instruction Tuning ★★

### 등장 배경 ① — 사용자의 의도에 맞는 답변 출력

**문제 상황**

- LLM은 기본적으로 **다음 단어를 예측하는 language modeling task로 pre-train** 됨
- 그래서 **사용자의 의도에 맞게 자연스럽게 답변하기 어려움**
- LLM은 **사용자의 입력 다음에 이어질 단어 혹은 문장들을 생성**하기 때문에, **질문에 대한 답이 아닌 "이어질 만한 후속 문장"을 출력할 가능성이 큼**

{: .시험 }
> **"Users intent ≠ Language modeling"** — 이 예시 그대로 나오기 좋습니다.
>
> 질문: **"한국의 수도는 어디야?"**
>
> | Users intent (사용자가 원하는 것) | Language modeling (실제로 나오는 것) |
> |---|---|
> | A: **"서울입니다."** | A: "한국에 처음 방문하는 외국인 관광객이 궁금해할 수 있습니다." |
> | | A: "한국인이라면 모두 답을 알 것입니다." |

**왜 이런 일이?**

{: .참고 }
> 사전학습만 한 LLM은 **"인터넷 글 이어 쓰기 기계"** 입니다.
> 인터넷에서 "한국의 수도는 어디야?" 다음에 어떤 글이 이어질까요? 블로그라면 "한국에 처음 오는 외국인이 궁금해할 수 있는 질문입니다~" 같은 말이 이어지겠죠.
> 그래서 모델은 **질문에 답하는 게 아니라 "그럴듯하게 이어지는 문장"을 씁니다.** 답을 해야 한다는 걸 배운 적이 없으니까요.

### Instruction Tuning의 정의 ★

Instruction Tuning
: **Instruction(지시문) & input text 와 output text의 pair 데이터 셋**을 통해 **supervised(지도) 형식으로 학습**시키는 것

- **사용자의 의도 및 task에 맞게 LLM을 잘 활용하기 위해서는 instruction-following 데이터로 tuning하는 것이 꼭 필요함**

**예시 (슬라이드)**

```
┌─────────── Input ───────────┐            ┌──── Output ────┐
│ Instruction: Translate into Korean.  │  →  │ 고양이가 상자 위에 있다. │
│ Input data : Text: The cat is on the box. │   └────────────────┘
└─────────────────────────────┘

→ 즉 "Translate 'The cat is on the box.' into Korean." 이라는 지시문 형태
```

{: .참고 }
> **쉽게:** "**이런 지시를 받으면 → 이렇게 답한다**" 는 **문제-정답 쌍**을 엄청 많이 보여주며 가르치는 것입니다.
>
> - "번역해줘: The cat…" → "고양이가…"
> - "요약해줘: (긴 글)" → "(짧은 요약)"
> - "한국의 수도는?" → "서울입니다."
>
> 이렇게 배우면 모델이 **"아, 지시를 받으면 이어 쓰는 게 아니라 시킨 걸 하는 거구나"** 를 깨닫습니다.
> **pair** = 쌍(짝). **supervised(지도)** = 정답을 보여주며 가르침.

### 등장 배경 ② — Zero-shot 성능 향상

**문제 상황**

- 기존의 tuning 기법: **task 별 fine-tuning**, 또는 **별도의 fine-tuning 없이 prompting**
- 기존 LLM은 **few-shot setting에서의 성능은 전반적으로 향상**되었으나, **zero-shot setting에서의 성능은 few-shot 성능만큼 향상되지 못함**
  - (예시를 보여주면 잘하는데, 예시 없이 바로 시키면 잘 못함)

```
[기존 방식 1] Fine-tune on translation task
  Input: The cat is on the box.  →  Output: 고양이가 상자 위에 있다.
  (번역만 따로 학습시킨 번역 전용 모델)

[기존 방식 2] Prompting (GPT-3)
  Task description: Translate English to Korean:
  Examples:         Dog ==> 개 / Bear ==> 곰 / Tiger ==> 호랑이
  Prompt:           Cat ==> ____
  → Output: 고양이
  (예시를 줘야 잘함)
```

**해결**

- **NLP task를 instruction(지시문) 형태로 변환하여 adaptation tuning 진행**
- **다양한 task로 instruction 데이터를 구성하여 학습하면 새로운 task에서의 성능이 향상되며 zero-shot 성능 또한 향상됨**

```
[Translation]                                  [Sentiment Analysis]
Input : Translate into Korean.                 Input : Classify the text into neutral, negative or positive
        Text: The cat is on the box.                   Text: I think the movie was perfect.
Output: 고양이가 상자 위에 있다.                    Output: Positive
                                                                        … (여러 과제를 같은 형식으로)
```

{: .참고 }
> **비유:** 번역 문제만 푼 학생 vs **번역·요약·분류·질의응답 등 온갖 유형의 "지시문 문제"를 풀어본 학생**
> 후자는 **처음 보는 유형의 지시**가 와도 "아 이렇게 하면 되겠다" 하고 **예시 없이도(zero-shot)** 해냅니다.

### FLAN (2021) ★

논문: **"FLAN: Finetuned Language Models Are Zero-Shot Learners"**
(제목 뜻: "미세조정된 언어 모델은 예시 없이도 잘하는 학습자다")

{: .시험 }
> **FLAN의 결론 3가지** — 그대로 출제 포인트
>
> 1. 기존 LLM의 **zero-shot 성능을 향상시킬 수 있는 instruction tuning 기법을 처음으로 제안**함
> 2. Instruction tuning에 사용되는 **task cluster의 개수가 많아질수록 unseen task에서의 성능이 향상**됨
> 3. **크기가 작은 모델에서는 instruction tuning 수행 시 오히려 성능이 하락**하며, **tuning의 효과를 얻기 위해서는 모델의 크기가 일정 수준 이상이 되어야 함**

**용어 풀이**
- **task cluster** = 비슷한 과제끼리 묶은 **과제 그룹** (요약 그룹, 번역 그룹, 감정분석 그룹 …)
- **unseen task** = 학습 때 **한 번도 안 본** 과제

**슬라이드 그래프 해석**

| 그래프 | 결과 |
|---|---|
| **Task cluster 수에 따른 성능 변화** | 학습에 쓴 과제 그룹이 1개 → 7개로 늘수록 평균 성능 **49.9 → 55.0 → 59.3 → 59.2 → 60.8 → 61.9 → 63.5** 로 상승 |
| **모델 크기에 따른 성능 변화** | 0.4B·2B·8B(작은 모델)에선 instruction tuning한 쪽이 **오히려 낮음**, 68B·137B(큰 모델)에선 **훨씬 높음** |

{: .참고 }
> **결론 3이 왜 그럴까?** 작은 모델은 **"머리 용량"이 작아서**, 여러 과제를 한꺼번에 배우면 오히려 헷갈려서 원래 하던 것도 못 하게 됩니다. 큰 모델은 용량이 넉넉해서 여러 과제를 배운 게 **시너지**가 됩니다.
> → **4장의 Emergent Abilities**(일정 크기 이상에서 능력이 생김)와 같은 맥락입니다.

---

## 3. Alignment Tuning ★★

**Alignment** = 정렬, 맞추기. **AI의 행동을 인간의 가치에 맞추는 것.**

### 등장 배경

- LLM은 학습 데이터에 포함된 **거짓 정보, 해로운 표현, 사회적 편향(인종, 성별 등)** 이 반영되어 **인간의 가치와 선호를 고려하지 않는 답변을 생성**하기도 함
- 이러한 **부적절한 행동을 방지하기 위해 human alignment 기법들이 제안**됨
- **Pre-train 및 instruction tuning과 달리 alignment는 매우 다른 기준을 고려해야 함**

{: .참고 }
> **왜 "다른 기준"?**
>
> - Pre-training / Instruction Tuning은 **"정답을 맞혔나"** 가 기준입니다.
> - Alignment는 **"착한가, 정직한가, 해롭지 않은가"** 가 기준입니다. 이건 **정답이 딱 정해진 게 아니라 사람의 가치 판단**이 필요하죠.

### Alignment의 기준 — 3H ★★

{: .시험 }
> **Helpfulness / Honesty / Harmlessness** — 이름과 정의를 모두 쓸 수 있어야 합니다. (전부 H로 시작 → "3H")

| 기준 | 정의 | 쉬운 말 |
|---|---|---|
| **Helpfulness** (유용성) | **사용자가 과제를 해결하는 데 도움이 되어야 함** | **도움이 돼라** |
| **Honesty** (정직성) | **조작하지 않고 정확한 내용을 사용자에게 제공해야 함** | **거짓말하지 마라** |
| **Harmlessness** (무해성) | **모욕적이거나 차별적인 표현을 생성해서는 안 되며, 악의적인 목적으로 요청하는 시도를 감지할 수 있어야 함** | **해롭게 하지 마라** |

### RLHF (Reinforcement Learning with Human Feedback) ★★★

RLHF
: **강화학습을 이용해 인간의 피드백으로부터 LLM을 최적화하는 방법**

{: .참고 }
> **강화학습(Reinforcement Learning)이 뭔가요?** ([0장](00-math-basics.html) 11절)
> **"해보고 → 점수 받고 → 점수 높은 쪽으로 행동을 바꾸기"** 를 반복하는 학습입니다.
> 강아지 훈련과 같아요. "앉아" 했을 때 앉으면 **간식(보상)**, 아니면 없음. 반복하면 강아지는 **간식 받는 행동**을 하게 됩니다.
>
> **RLHF** = 그 **"간식(점수)"을 사람의 평가로** 주는 강화학습.

**총 3단계로 학습**이 이루어지며, 다음 **3가지 요소**가 필요합니다.

| 요소 | 역할 | 비유 |
|---|---|---|
| **Human annotator** (인간 평가자) | LM이 생성한 답변에 대해 **인간이 직접 피드백을 주어 선호도를 모델링** | **심사위원** |
| **Reward model** (보상 모델) | LM이 생성한 답변에 대해 **인간의 선호도를 예측하는 모델** | **심사위원을 흉내 내는 AI 채점기** |
| **Aligned model** (정렬 모델) | **인간의 선호도를 반영하여 학습시키고자 하는 모델** | **훈련받는 학생** (최종 결과물) |

#### RLHF 3단계 ★★★

<figure class="fig" id="fig-rlhf"><svg viewBox="0 0 780 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="RLHF 3단계" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-rlhf-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-rlhf-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-rlhf-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-rlhf-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <g><rect x="10" y="20" width="230" height="200" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="125" y="48" fill="#C77E16" font-size="13">STEP 1</text><text x="125" y="70" fill="#142A52">Supervised Fine-tuning</text> <rect x="35" y="90" width="180" height="40" rx="8" fill="#F2EFE8"/><text x="125" y="115" font-size="13" fill="#4A5568">사람이 쓴 질문 + 모범답안</text> <rect x="35" y="160" width="180" height="40" rx="8" fill="#EAF0FA"/><text x="125" y="185" font-size="13" fill="#1E3A6E">LM이 따라 쓰며 학습 🔥</text></g> <path d="M125 132V156" stroke="#1E3A6E" stroke-width="2" marker-end="url(#fig-rlhf-a)"/> <g><rect x="275" y="20" width="230" height="200" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="390" y="48" fill="#C77E16" font-size="13">STEP 2</text><text x="390" y="70" fill="#142A52">Reward Model Training</text> <rect x="300" y="90" width="180" height="40" rx="8" fill="#F2EFE8"/><text x="390" y="115" font-size="13" fill="#4A5568">답변 A·B·C·D → 사람이 순위</text> <rect x="300" y="160" width="180" height="40" rx="8" fill="#FBF0D8"/><text x="390" y="185" font-size="13" fill="#C77E16">취향 흉내 채점기 🔥</text></g> <path d="M390 132V156" stroke="#1E3A6E" stroke-width="2" marker-end="url(#fig-rlhf-a)"/> <g><rect x="540" y="20" width="230" height="200" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="655" y="48" fill="#C77E16" font-size="13">STEP 3</text><text x="655" y="70" fill="#142A52">RL Fine-tuning (PPO)</text> <rect x="565" y="90" width="180" height="40" rx="8" fill="#FBF0D8"/><text x="655" y="115" font-size="13" fill="#C77E16">채점기가 점수 👍👎 ❄</text> <rect x="565" y="160" width="180" height="40" rx="8" fill="#E4F2EA"/><text x="655" y="185" font-size="13" fill="#2E7D55">점수 높게 받도록 수정 🔥</text></g> <path d="M655 132V156" stroke="#1E3A6E" stroke-width="2" marker-end="url(#fig-rlhf-a)"/> <g stroke="#C77E16" stroke-width="2.2" fill="none"><path d="M242 120H271" marker-end="url(#fig-rlhf-b)"/><path d="M507 120H536" marker-end="url(#fig-rlhf-b)"/></g> <text x="390" y="244" font-size="12.5" fill="#8A93A3">🔥 = 학습되는 중 · ❄ = 고정(채점만 함)</text> </svg><figcaption>RLHF: 모범답안 따라 쓰기 → 사람 취향을 흉내 내는 채점기(Reward model) 만들기 → 채점기 점수를 높이도록 PPO로 강화학습</figcaption></figure>

{: .시험 }
> **3단계의 이름과 각 단계에서 하는 일** — 서술형 출제 1순위입니다.
> **Step 1: Supervised Fine-tuning → Step 2: Reward Model Training → Step 3: RL Fine-tuning**

---

**Step 1: Supervised Fine-tuning (지도 미세조정)**

- **인간이 작성한 prompt 데이터 셋을 이용해 LM을 fine-tuning** 함
- 학습이 완료된 LM은 **어느 정도 인간의 의도에 맞는 답변을 생성할 수 있게 됨**

```
Human Annotator ──→ Prompts (질문)
               └──→ Demonstrations (사람이 쓴 모범 답안)
                         ↓  Training with demonstration data
                    Pre-trained LM 🔥 (학습됨)
```

{: .참고 }
> **쉽게:** 사람이 질문과 **모범 답안**을 직접 써서, 모델에게 **"이렇게 답하는 거야"** 하고 따라 쓰게 가르침.
> (= 앞에서 배운 Instruction Tuning과 비슷한 단계)
> **Demonstration** = 시범, 모범 답안

---

**Step 2: Reward Model Training (보상 모델 학습)**

- **1단계에서 학습된 LM이 여러 개의 답변을 생성**하도록 하고, 각 답변에 대해 **인간 평가자는 선호도 순위를 매김 (Ranking)**
- **답변과 해당 답변에 대응되는 인간 선호도**를 통해, **인간의 선호도를 모방할 수 있는 reward model을 학습**시킴
- **Reward model은 이후 aligned model의 평가를 위해 사용**됨

```
Prompts → LM Outputs (답변 A, B, C, D)
              ↓
     사람이 순위 매김 (Ranking): B > A > D > C
              ↓
     Human Feedback 데이터 저장
              ↓  Training with feedback data
     Reward Model 🔥 (학습됨)   ← "사람이라면 이 답을 몇 점 줄까?"를 예측
```

{: .참고 }
> **쉽게:** 모델에게 같은 질문에 답을 **4개** 쓰게 하고, 사람이 **"B가 제일 낫고, 그다음 A, D, C 순"** 이라고 줄을 세웁니다.
> 이걸 수만 번 반복해서 모은 데이터로 **"사람 취향을 흉내 내는 채점 AI(Reward model)"** 를 만듭니다.
>
> **왜 채점 AI를 따로 만드나?** 사람이 매번 직접 채점하면 너무 느리고 비싸니까요. 한 번 채점 AI를 만들어 두면 **수백만 개 답변을 자동으로 채점**할 수 있습니다.
>
> **왜 점수가 아니라 순위?** "이 답은 7점" 같은 절대 점수는 사람마다 기준이 들쭉날쭉하지만, **"A가 B보다 낫다"** 는 비교는 훨씬 일관되게 할 수 있기 때문입니다.

---

**Step 3: RL Fine-tuning (강화학습 미세조정)**

- **강화 학습을 통해 aligned model을 최적화**시킴
- **Reward model을 보상 함수로 사용**하고, **보상을 최대화하기 위해 aligned model의 정책(policy)을 fine-tuning** 함
- 이 과정에서 **PPO (Proximal Policy Optimization)** 가 사용됨

```
Prompts → Aligned LM 🔥 이 답변 생성 → LM Outputs
                                        ↓
                               Reward Model ❄ (고정, 채점만 함)
                                        ↓
                               Reward 👍 / 👎 (점수)
                                        ↓  Training with RL algorithm (PPO)
                               Aligned LM 🔥 업데이트
                               (점수 높게 받는 방향으로)
```

{: .참고 }
> **쉽게:** 이제 모델이 답을 쓰면 **채점 AI가 점수**를 줍니다. 모델은 **점수를 더 많이 받는 방향으로** 자기 말투·내용을 계속 고쳐 나갑니다. (강아지가 간식 받는 행동을 배우듯)
>
> **용어 풀이**
>
> - **정책(policy)** = 모델의 **"이런 상황에선 이렇게 답한다"는 행동 방식**
> - **보상 함수** = 점수를 매겨 주는 기준 (여기선 Reward model)
> - **PPO** = 강화학습 방법 이름. 핵심은 **"한 번에 너무 많이 바꾸지 말고 조금씩(proximal = 가까운)"** 바꾸게 하는 안전장치. 갑자기 확 바뀌면 이상해질 수 있으니까요.
>
> 그림의 🔥 = 학습되는 중 / ❄ = 고정(학습 안 함)

---

**3단계 한눈에 보기**

| 단계 | 이름 | 하는 일 | 비유 |
|---|---|---|---|
| **1** | **Supervised Fine-tuning** | 사람이 쓴 **모범 답안**으로 따라 쓰게 학습 | 모범 답안 베껴 쓰기 |
| **2** | **Reward Model Training** | 모델 답변들에 사람이 **순위** → **채점 AI** 학습 | 심사위원 흉내 내는 채점기 만들기 |
| **3** | **RL Fine-tuning** | 채점 AI 점수를 **최대화**하도록 **PPO**로 학습 | 채점기 점수 높게 받는 연습 |

#### RLHF의 효과와 한계

- RLHF를 통해 사용자의 입력에 대해 **안전하고 유용하게 답변하는 모델**을 얻을 수 있음 (**Safety + Helpfulness**)
- **InstructGPT 및 ChatGPT는 GPT-3에 RLHF가 적용되어 더 나은 품질의 답변을 생성**할 수 있게 됨

{: .중요 }
> **RLHF의 한계** (추가 개선이 필요한 이유) — 2가지
>
> 1. **Human annotator를 고용해 데이터 셋을 확보하기 위한 비용이 많이 필요**
> 2. **주관적인 요인에 따라 학습 데이터 셋의 품질 편차가 존재** (평가자마다 취향이 달라서)

---

## 4. Parameter-Efficient Model Adaptation (PEFT) ★★

**PEFT = Parameter-Efficient Fine-Tuning** = **파라미터를 아껴 쓰는 미세조정**

### 왜 필요한가?

{: .참고 }
> GPT-3는 파라미터(다이얼)가 **1,750억 개**입니다. 새 과제를 위해 이걸 **전부 다시 조절(full fine-tuning)** 하려면:
>
> - 엄청난 GPU와 메모리가 필요
> - 과제마다 1,750억 개짜리 모델을 **통째로 하나씩 저장**해야 함 (번역용 1개, 요약용 1개 …)
>
> **"전부 다 고칠 필요 있나? 조금만 고치면 안 되나?"** 에서 나온 게 PEFT입니다.

### 근거 — Low intrinsic dimension

- Pre-trained 언어 모델(**PLM**)의 경우 **low intrinsic dimension**을 가짐
- → **모델이 크고 복잡하지만, 실제로 중요한 정보를 나타내는 특성의 수가 상대적으로 적음**
- → **RoBERTa의 경우 오직 200개의 학습 가능한 파라미터로 90% 성능을 달성**

{: .참고 }
> **Intrinsic dimension (내재 차원)** = **"진짜로 필요한 자유도"**.
> **비유:** 자동차 계기판에 버튼이 1,000개 있어도, 실제로 운전할 때 쓰는 건 **핸들·엑셀·브레이크** 정도죠.
> 모델도 수억 개 파라미터 중 **새 과제를 위해 진짜 바꿔야 하는 방향은 몇 개 안 된다**는 발견입니다. 그러니 **그 몇 개만 학습하면 됩니다.**
> **RoBERTa** = BERT의 개선 버전 모델.

### Adapter Tuning ★

- **기존 Layer 위에 adapter layer를 추가**함
- 이때 adapter layer는 **target task에 따라 최적화**되며, **기존 LLM 파라미터는 고정(freeze)**
- 구조:
  - **Down Projection** → **핵심 변화만 추출** (큰 차원 `d` → 작은 차원 `m` 으로 줄임)
  - **Up Projection** → **원래 LLM 표현 공간으로 복원** (작은 차원 `m` → 다시 `d`)
  - (`d` = 모델의 차원, `m` = 차원 축소를 위한 차원)

```
   원래 층 출력 (d=1024 크기)
        ↓
   [Down Projection]  1024 → 16   (핵심만 뽑기)
        ↓
   [Up Projection]    16 → 1024   (원래 크기로 되돌리기)
        ↓
   다음 층으로
```

**계산 예시 (슬라이드)** — `d = 1024`, `m = 16`

| | 계산 | 파라미터 수 |
|---|---|---|
| 원래 층 전체를 학습 | 1024 × 1024 | **1,048,576개** (약 100만) |
| Adapter만 학습 | 2 × 1024 × 16 | **32,768개** (약 3만) |

→ **약 1/32로 감소**

> **Adapter Tuning은 전체 모델을 다시 학습하지 않고, 작은 추가 모듈만 학습하여 효율적인 모델 적응을 시킴**

{: .참고 }
> **비유: 기존 건물은 그대로 두고 작은 별채만 증축**
> 건물 전체를 리모델링하는 대신, **옆에 작은 방(adapter)을 하나 붙여서** 새 용도에 맞춥니다.
> 과제가 바뀌면 **작은 방만 갈아 끼우면** 됩니다.
>
> **왜 `2 × 1024 × 16`?** Down(1024×16) + Up(16×1024) = 표 두 개니까 ×2. ([0장](00-math-basics.html) 6절 행렬)

### LoRA (Low-Rank Adaptation) ★★

<figure class="fig" id="fig-lora"><svg viewBox="0 0 740 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="LoRA 행렬 분해" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-lora-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-lora-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-lora-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-lora-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="30" y="40" width="170" height="170" rx="8" fill="#EAF0FA" stroke="#CBD9EE" stroke-width="2"/> <text x="115" y="112" font-size="24" fill="#1E3A6E">W0</text><text x="115" y="138" font-size="13" fill="#4A5568">원래 가중치</text><text x="115" y="162" font-size="13" fill="#1E3A6E">❄ 고정</text> <text x="115" y="234" font-size="12.5" fill="#8A93A3">1024 × 1024 ≈ 100만 개</text> <text x="236" y="136" font-size="30" fill="#4A5568">+</text> <rect x="270" y="40" width="26" height="170" rx="4" fill="#FBF0D8" stroke="#C77E16" stroke-width="1.5"/> <text x="283" y="32" font-size="15" fill="#C77E16">A</text><text x="283" y="234" font-size="12" fill="#8A93A3">1024×8</text> <text x="322" y="134" font-size="22" fill="#4A5568">×</text> <rect x="345" y="112" width="170" height="26" rx="4" fill="#FBF0D8" stroke="#C77E16" stroke-width="1.5"/> <text x="430" y="104" font-size="15" fill="#C77E16">B</text><text x="430" y="160" font-size="12" fill="#8A93A3">8×1024</text> <text x="546" y="136" font-size="28" fill="#4A5568">=</text> <rect x="575" y="40" width="150" height="170" rx="8" fill="#FBF0D8" stroke="#C77E16" stroke-width="2" stroke-dasharray="7 5"/> <text x="650" y="108" font-size="24" fill="#C77E16">ΔW</text><text x="650" y="134" font-size="13" fill="#4A5568">변화량만</text><text x="650" y="158" font-size="13" fill="#C77E16">학습 🔥</text> <text x="650" y="234" font-size="12.5" fill="#C77E16">16,384개만 학습</text> </svg><figcaption>LoRA: W0 + ΔW = W0 + A·B. 원본(교과서)은 그대로 두고, 얇은 두 행렬(포스트잇)로 변화량만 학습</figcaption></figure>

- **가정: Adapter Tuning과 동일** → 즉 **weight update 행렬은 low-rank(낮은 랭크) intrinsic rank를 가짐**
- PLM 모델의 weight matrix `W0 ∈ ℝ^(d×d)` 를 `ΔW` 라는 **작은 두 개의 행렬로 분해**
- **Adapter tuning과 유사하게, PLM 파라미터는 고정하고 분해된 행렬만 학습**

```
W0 + ΔW  =  W0 + A·B

A ∈ ℝ^(d×m),   B ∈ ℝ^(m×d),   m = rank의 차원
```

**기호 하나씩 풀기** ([0장](00-math-basics.html) 14절에 자세히)

| 기호 | 뜻 |
|---|---|
| `W0` | **원래 모델의 가중치** (1024×1024 표). **얼려 둠(freeze)** |
| `ΔW` (델타 W) | **"변화량"**. 새 과제를 위해 **얼마나 바꿔야 하는지** |
| `A`, `B` | 그 변화량을 표현하는 **얇은 표 두 개** (1024×8, 8×1024) |
| `A·B` | 두 표를 곱하면 → 1024×1024 크기의 변화량이 만들어짐 |
| `ℝ^(d×m)` | "d행 m열짜리 실수 표" 라는 뜻 |
| `m` (rank) | **얼마나 얇게 쪼갤지**. 작을수록 파라미터가 적음 |

**ΔW의 의미 (슬라이드)** → **새로운 task에 적응하기 위해 필요한 변화량만 학습하면 된다**

**계산 예시** — `d = 1024`, `m = 8`이면 → `1024 × 8 × 2 = 16,384`개

{: .참고 }
> **비유: 교과서에 포스트잇 붙이기**
> 교과서(원래 모델 `W0`)에 **직접 낙서하지 않고**, 고칠 내용을 **포스트잇(`A·B`)** 에 써서 붙입니다.
>
> - 원본은 깨끗하게 보존
> - 포스트잇은 작고 가벼움
> - 과제가 바뀌면 **포스트잇만 바꿔 붙이면** 됨
>
> 그리고 포스트잇 내용을 **얇은 종이 두 장(A, B)** 으로 압축해서 적는 게 LoRA의 비결입니다.

**Adapter vs LoRA 파라미터 비교**

| 방법 | 설정 | 학습 파라미터 수 |
|---|---|---|
| 전체 학습 | d=1024 | 1,048,576 |
| Adapter | d=1024, m=16 | 32,768 |
| **LoRA** | d=1024, m=8 | **16,384** |

#### 왜 LoRA가 Adapter보다 나은가? ★★

{: .시험 }
> **3가지로 답하세요.**
>
> 1. **adapter tuning보다도 낮은 parameter tuning**을 통한 새로운 task에 **fast adaptation 가능**
> 2. **순차적인 방식으로 진행되는 adapter와 달리 병렬적으로 진행**되어 **추가적인 추론 지연(inference latency)이 발생하지 않음**
> 3. **입력 시퀀스 길이를 줄이지 않고 훈련이 가능**

{: .참고 }
> **2번이 무슨 뜻?**
>
> - **Adapter**: 원래 층 **다음에** adapter를 거쳐야 함 → 길에 **정거장이 하나 더 생긴 것** → 답 나오는 데 **조금 더 오래 걸림** (추론 지연)
> - **LoRA**: 원래 경로 **옆에 나란히(병렬)** 붙어서 동시에 계산하고 더하기만 함. 게다가 학습이 끝나면 `W0 + A·B` 를 **미리 더해서 하나로 합쳐버릴 수 있어서**, 실제 사용할 땐 **원래 모델과 속도가 똑같음**
>
> **추론(inference)** = 학습이 끝난 모델을 **실제로 사용해서 답을 내는 것**. **latency(지연)** = 걸리는 시간.

---

## 5. Quantization (양자화) ★

### 왜 필요한가?

- 앞서 설명한 **PEFT 방식들은 원래 모델의 파라미터 크기를 줄이지 않음**
- → **원래 모델의 파라미터를 저장해 놓고 있어야 하기 때문에 메모리 및 계산 비용이 크게 증가**

{: .참고 }
> LoRA로 **학습할 양**은 줄였지만, 원래 1,750억 개짜리 모델은 **여전히 메모리에 통째로** 올려 둬야 합니다. 이 **덩치 자체**를 줄이는 게 양자화입니다.

### 양자화란? — 숫자를 대충(짧게) 저장하기

**파라미터 하나를 저장하는 데 쓰는 칸(비트) 수를 줄이는 것** ([0장](00-math-basics.html) 15절)

```
FP32 (32 bit)  →  FP16 (16 bit)  →  INT8 (8 bit)  →  INT4 (4 bit)
 3.14159265         3.1416            3.14            3
 아주 정밀            ←─────────────────────────────→    거침
 용량 큼                                                  용량 작음
```

- 효과: **메모리 사용량 감소 | 계산량 감소**
- 32비트 → 4비트면 **용량이 1/8**

{: .참고 }
> **비유: 사진 화질 낮추기**
> 원본 사진(FP32)은 화질이 좋지만 용량이 큽니다. 화질을 조금 낮추면(INT4) 용량이 확 줄어도 **알아보는 데는 거의 문제가 없죠.**
> **FP** = Floating Point (소수점 숫자), **INT** = Integer (정수)

---

## 6. 거대한 LLM을 효율적으로 활용하는 두 가지 접근 방법 ★★

{: .시험 }
> 이 장 전체를 한 장으로 요약한 슬라이드입니다. **PEFT와 Quantization이 각각 "무엇을" 줄이는지** 정확히 구분하세요.

**출발점 — Pre-trained LLM** (이미 방대한 지식을 학습한 거대한 모델, 예: LLaMA, GPT / 수십억~수천억 개 파라미터)

| 잘하는 것 | 하지만… |
|---|---|
| ✓ **일반적인 언어 이해** | ⚠ **모델이 너무 커서 학습 비용이 큼** |
| ✓ **다양한 주제에 대한 지식** | ⚠ **많은 GPU 메모리가 필요** |
| ✓ **풍부한 세계 지식** | ⚠ **새로운 작업에 맞게 전체 모델을 다시 학습하기는 비효율적** |

> **"LLM은 이미 방대한 지식을 학습했지만, 새로운 작업에 맞게 활용하기 위해서는 학습 비용과 메모리 사용량을 줄이는 효율적인 방법이 필요합니다."**

### 두 가지 핵심 아이디어

| | **① PEFT** (Parameter-Efficient Fine-Tuning) | **② Quantization** |
|---|---|---|
| **줄이는 것** | **학습할 파라미터 수를 줄이기** | **파라미터의 표현 크기(비트 수)를 줄이기** |
| **구조** | **기존 LLM (대부분 Freeze) + 작은 모듈만 학습** (예: Adapter, LoRA) | **FP32 → FP16 → INT8 → INT4** |
| **핵심 개념** | • 기존 LLM의 파라미터는 **대부분 고정(Freeze)**<br>• **작은 모듈(또는 작은 가중치 변화량)만 학습**<br>• 학습 파라미터 수를 크게 줄여 **작은 자원으로 효과적인 성능 향상** 가능 | • 모델의 파라미터를 **더 작은 비트로 표현**<br>• **모델 크기와 메모리 사용량을 크게 감소**<br>• 적절한 양자화 기법을 사용하면 **성능 저하를 최소화**하면서도 효율적으로 모델을 활용 가능 |
| **효과** | ✓ **학습 비용 절감 \| 적은 데이터로 학습 가능**<br>✓ **다양한 작업에 빠르게 적용** | ✓ **메모리 절감 \| 추론 속도 향상**<br>✓ **더 작은 하드웨어에서도 실행 가능** |

### 두 방법의 결합 — QLoRA (Quantization + LoRA) ★

```
  ┌──────────────────────────────┐
  │ 양자화된 LLM (4-bit, Freeze) 🔒 │  ← Quantization으로 덩치 줄이고 얼림
  └──────────────────────────────┘
                 +
  ┌──────────────────────────────┐
  │    LoRA Adapter (학습 가능)     │  ← LoRA로 작은 부분만 학습
  └──────────────────────────────┘
```

**QLoRA의 주요 장점 4가지**

- ✓ **매우 적은 메모리로 학습 가능**
- ✓ **학습 파라미터 수 최소화**
- ✓ **큰 모델도 개인/소규모 GPU에서 활용**
- ✓ **성능과 효율성의 균형 달성**

{: .중요 }
> **핵심 메시지 (슬라이드 원문 — 그대로 외우기)**
> **"PEFT는 학습할 파라미터 수를 줄이고, Quantization은 파라미터의 표현 크기를 줄인다.**
> **이 두 가지를 결합한 QLoRA는 거대한 LLM을 작은 자원으로도 효과적으로 활용할 수 있게 해준다."**
>
> (요약 슬라이드 버전: **"PEFT는 학습할 파라미터를 줄이고, Quantization은 메모리 사용량을 줄인다. 두 방법을 결합한 것이 QLoRA이다."**)

### 정리 그림

<figure class="fig" id="fig-qlora"><svg viewBox="0 0 740 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="PEFT 양자화 QLoRA 관계" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-qlora-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-qlora-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-qlora-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-qlora-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="20" y="18" width="290" height="74" rx="12" fill="#EAF0FA" stroke="#CBD9EE"/><text x="165" y="48" font-size="15" fill="#1E3A6E">PEFT (Adapter · LoRA)</text><text x="165" y="74" font-size="13" fill="#4A5568">학습할 파라미터 수 ↓</text> <rect x="20" y="108" width="290" height="74" rx="12" fill="#E4F2EA" stroke="#BFE0CC"/><text x="165" y="138" font-size="15" fill="#2E7D55">Quantization</text><text x="165" y="164" font-size="13" fill="#4A5568">표현 크기(FP32→INT4) ↓ → 메모리 ↓</text> <g stroke="#C77E16" stroke-width="2.4" fill="none" marker-end="url(#fig-qlora-b)"><path d="M312 55L432 84"/><path d="M312 145L432 116"/></g> <rect x="436" y="40" width="284" height="120" rx="14" fill="#FBF0D8" stroke="#EBCF95" stroke-width="2"/> <text x="578" y="70" font-size="17" fill="#C77E16">QLoRA</text><text x="578" y="96" font-size="13">4-bit 양자화 LLM ❄ (고정)</text><text x="578" y="118" font-size="13">+ LoRA Adapter 🔥 (학습)</text><text x="578" y="142" font-size="12" fill="#8A93A3">큰 모델도 개인 GPU에서</text> </svg><figcaption>PEFT는 학습할 파라미터 수를, Quantization은 메모리(비트 수)를 줄인다. 둘을 합친 것이 QLoRA</figcaption></figure>

```
                    Large Language Model
                   (너무 크고 학습이 비쌈)
                   /                    \
       Trainable Parameters          Model Memory
            (너무 많음)                  (너무 큼)
                ↓                          ↓
              PEFT                    Quantization
        (Adapter / LoRA)          (FP16 → INT8 → INT4)
                   \                    /
                         QLoRA
              Quantized Base LLM (4-bit, Freeze)
                           +
                      LoRA Adapter
```

| 기법 | 해결하는 문제 | 줄이는 것 | 방법 |
|---|---|---|---|
| **PEFT** (Adapter, LoRA) | Trainable Parameters가 너무 많음 | **학습할 파라미터 수** | 원본 freeze, 작은 모듈만 학습 |
| **Quantization** | Model Memory가 너무 큼 | **메모리 (비트 수)** | 숫자 정밀도 낮추기 |
| **QLoRA** | 둘 다 | **둘 다** | 4-bit 양자화 base + LoRA |

---

## 이 장 정리

| 기법 | 목적 | 핵심 키워드 |
|---|---|---|
| **Instruction Tuning** | 사용자 의도에 맞게 답하기 + zero-shot 향상 | 지시문-정답 **pair**, **지도학습**, **FLAN** |
| **Alignment Tuning** | 인간 가치에 맞추기 | **3H** (Helpful·Honest·Harmless), **RLHF 3단계**, **PPO** |
| **PEFT** | 학습 파라미터 줄이기 | **Adapter** (Down/Up Projection), **LoRA** (W0 + A·B) |
| **Quantization** | 메모리 줄이기 | **FP32→FP16→INT8→INT4** |
| **QLoRA** | 둘 다 | 4-bit freeze + LoRA |
