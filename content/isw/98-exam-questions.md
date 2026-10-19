# 예상 문제 모음

노트 전체에서 **시험에 나오기 좋은 것**을 세 가지 유형으로 만들었습니다. **"정답 보기"를 누르기 전에 먼저 직접 풀어 보세요.**

| 유형 | 문항 | 연습 목적 |
|---|---|---|
| [Part 1 · 객관식](#part-1-객관식-30문항) | M1~M30 | 헷갈리는 짝 구분, 함정 보기 거르기 |
| [Part 2 · 빈칸 채우기](#part-2-빈칸-채우기-25문항) | B1~B25 | 정의·숫자·이름을 정확히 쓰기 |
| [Part 3 · 단답·서술](#part-3-단답서술-111문항) | Q1~Q111 | 정의 + 이유 + 비교를 문장으로 쓰기 |

{: .참고 }
> - 서술 모범 답안의 **굵은 글씨**가 채점 키워드입니다.
> - 문제 옆 `[n장]` 은 해당 내용이 있는 장입니다. 틀리면 그 장으로 돌아가세요.
> - 객관식 해설에 나오는 오답 이유는 [헷갈리는 개념 총정리](97-compare.html)의 "함정 주의"와 같습니다.

---

## Part 1 · 객관식 (30문항)

**M1.** One-hot encoding의 한계로 옳은 것을 **모두** 고르면? `[2장]`

1. 벡터 대부분이 0인 희소 문제가 있다
2. 단어 사이의 유사도를 표현할 수 없다
3. 단어 사전이 커져도 벡터 차원은 일정하다
4. 문맥을 고려하지만 계산량이 많다

<details markdown="1"><summary>정답 보기</summary>

**정답 ①, ②** — One-hot의 한계 2가지는 **희소 문제**와 **유사도 표현 불가**입니다. ③은 Dense 표현의 특징(반대로 One-hot은 사전이 커지면 차원도 커짐), ④는 해당 없음.

</details>

**M2.** TF-IDF에 대한 설명으로 **틀린** 것은? `[2장]`

1. TF와 IDF를 곱한 값이다
2. 여러 문서에 공통으로 많이 나오는 단어는 중요도가 낮다
3. 문맥을 고려하므로 동의어·다의어를 구분할 수 있다
4. 검색 시스템에서 결과의 중요도를 정하는 데 효율적이다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — TF-IDF의 한계가 바로 **문맥 무시, 희소성, 동의어/다의어 처리 불가**입니다.

</details>

**M3.** IDF 식 `log(n / (1 + df(t)))` 에 대한 설명으로 옳은 것은? `[2장]`

1. df(t)가 클수록 IDF도 커진다
2. log는 값의 크기를 키우기 위해 쓴다
3. 분모의 1은 단어가 어느 문서에도 없을 때 0으로 나누는 것을 막는다
4. n은 특정 단어가 등장한 문서의 수이다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — ① IDF는 df(t)에 **반비례** ② log는 가중치를 **적절히 조절**(눌러 주기) ④ n은 **전체 문서 수**, 단어가 등장한 문서 수는 df(t).

</details>

**M4.** Dense representation의 특징이 **아닌** 것은? `[2장]`

1. 사용자가 정한 차원으로 모든 단어 벡터의 크기를 맞춘다
2. 연속적인 실수값으로 표현된다
3. 단어 사전이 커질수록 벡터 차원도 함께 커진다
4. '강아지'와 '멍멍이'를 비슷한 벡터로 표현해 일반화가 가능하다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — Dense는 사전 크기와 무관하게 **차원이 일정** → 공간 복잡도 개선. ③은 Sparse(One-hot)의 특징.

</details>

**M5.** AutoEncoder에 대한 설명으로 옳은 것은? `[2장]`

1. 정답 label이 있는 데이터로 학습하는 지도학습이다
2. 입력 X, Latent vector Z, 출력 X̃ 의 3계층으로 구성된다
3. 입력보다 더 높은 차원으로 특징을 확장한다
4. 2017년 Transformer 논문에서 처음 제안되었다

<details markdown="1"><summary>정답 보기</summary>

**정답 ②** — **비지도** 학습(①✗), **낮은 차원**의 특성 표현 학습(③✗), **1986년** "Learning Internal Representation by Error Backpropagation"에서 소개(④✗).

</details>

**M6.** Transformer가 해결한 기존 Seq2Seq/RNN의 한계가 **아닌** 것은? `[3장]`

1. 고정된 크기의 벡터에 모든 정보를 압축해 생기는 정보 손실
2. Vanishing Gradient Problem
3. 입력의 순차적 처리로 인한 병렬화 불가
4. 모델 파라미터 수가 너무 적어 표현력이 부족함

<details markdown="1"><summary>정답 보기</summary>

**정답 ④** — 슬라이드의 고질적 한계 3가지는 ①②③.

</details>

**M7.** Transformer에 대한 설명으로 옳은 것은? `[3장]`

1. RNN을 개선한 LSTM을 인코더로 사용한다
2. Encoder-Decoder 구조를 버리고 디코더만 사용한다
3. 단어 embedding에 Positional Encoding을 더해 입력한다
4. 단어를 한 개씩 순서대로 처리하므로 순서를 자동으로 안다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — RNN을 **사용하지 않고**(①✗) **Encoder-Decoder 구조는 유지**(②✗). 한꺼번에(병렬) 넣기 때문에 순서를 몰라서(④✗) **위치 정보를 더해 줌**.

</details>

**M8.** 디코더에서 아직 생성하지 않은 뒤쪽 단어를 보지 못하게 가리는 Attention은? `[3장]`

1. Encoder Self-Attention
2. Masked Decoder Self-Attention
3. Encoder-Decoder Attention
4. Multi-head Cross Attention

<details markdown="1"><summary>정답 보기</summary>

**정답 ②**

</details>

**M9.** 언어 모델 발전 단계와 대표 모델의 연결이 **틀린** 것은? `[3장]`

1. SLM — N-gram LM
2. NLM — word2vec, LSTM, Seq2Seq
3. PLM — BERT, GPT-2, T5
4. LLM — Kneser-Ney Smoothing

<details markdown="1"><summary>정답 보기</summary>

**정답 ④** — Kneser-Ney Smoothing은 **SLM**. LLM의 대표는 **GPT-4, PaLM 2, LLaMA 3**.

</details>

**M10.** 다음 중 BERT와 GPT의 비교로 옳은 것은? `[3·4장]`

1. BERT는 디코더, GPT는 인코더 기반이다
2. GPT는 양방향으로 문장 앞뒤를 모두 본다
3. GPT는 Autoregressive 방식으로 다음 단어를 예측한다
4. BERT는 GPT보다 늦게 나와 Transformer LM의 시초가 되었다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — BERT = **인코더·양방향**, GPT = **디코더·단방향**. GPT-1의 혁신 포인트가 "**BERT보다 먼저 나온 Transformer LM**".

</details>

**M11.** 기존 PLM과 구별되는 LLM의 가장 큰 특징은? `[4장]`

1. Transformer 구조를 사용한다
2. Emergent Abilities
3. 사전학습을 한다
4. Fine-tuning이 가능하다

<details markdown="1"><summary>정답 보기</summary>

**정답 ②** — ①③④는 PLM도 다 해당.

</details>

**M12.** In-context Learning에 대한 설명으로 옳은 것은? `[4장]`

1. 소량의 정답 데이터로 모델을 미세조정한다
2. 모델 파라미터를 업데이트하지 않고 프롬프트 속 예시로 과제를 수행한다
3. GPT-1에서 처음 공식 도입되었다
4. 예시가 많을수록 오히려 성능이 떨어지는 것이 일반적이다

<details markdown="1"><summary>정답 보기</summary>

**정답 ②** — **GPT-3**가 공식 도입(③✗). Context Window k가 커질수록 성능 **향상**(④✗).

</details>

**M13.** GPT-2의 목적함수로 옳은 것은? `[4장]`

1. P(Output \| Input)
2. P(Input \| Output)
3. P(Output \| Input, Task)
4. P(Task \| Input)

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — ①은 GPT-1. GPT-2는 Task까지 조건으로 → 같은 입력도 과제에 따라 다른 출력.

</details>

**M14.** GPT 시리즈의 연도·파라미터 연결로 옳은 것은? `[4장]`

1. GPT-1 — 2018 — 1.5B
2. GPT-2 — 2019 — 1.5B
3. GPT-3 — 2019 — 175B
4. GPT-3 — 2020 — 117M

<details markdown="1"><summary>정답 보기</summary>

**정답 ②** — GPT-1 **2018·117M** / GPT-2 **2019·1.5B** / GPT-3 **2020·175B**.

</details>

**M15.** GPT-3 논문이 지적한 Fine-tuning의 한계가 **아닌** 것은? `[4장]`

1. Task별 Labeled Dataset이 필요하다
2. 작은 Task 분포에 과적합되어 분포 밖 일반화 성능을 잃을 수 있다
3. 모델의 단방향성으로 자연어 추론을 잘 못한다
4. 사람처럼 적은 샘플로 Task를 수행하는 능력이 필요하다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — 단방향성은 **GPT-3 자체의 한계**. 두 목록을 섞은 함정.

</details>

**M16.** LLM 학습 과정에서 Adaptation Tuning에 속하지 **않는** 것은? `[5장]`

1. Instruction tuning
2. Alignment tuning
3. Parameter efficient model adaptation
4. Prompt Engineering

<details markdown="1"><summary>정답 보기</summary>

**정답 ④** — Prompt Engineering은 **Utilization** 단계.

</details>

**M17.** FLAN(2021)의 결론으로 **틀린** 것은? `[5장]`

1. Instruction tuning 기법을 처음으로 제안했다
2. Task cluster가 많을수록 unseen task 성능이 향상된다
3. 모델 크기와 관계없이 instruction tuning은 항상 성능을 높인다
4. Zero-shot 성능을 향상시킨다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — **작은 모델에서는 오히려 성능이 하락**하며, 일정 크기 이상이어야 효과가 있다.

</details>

**M18.** Alignment의 기준 3H가 **아닌** 것은? `[5장]`

1. Helpfulness
2. Honesty
3. Harmlessness
4. High-performance

<details markdown="1"><summary>정답 보기</summary>

**정답 ④**

</details>

**M19.** RLHF에 대한 설명으로 옳은 것은? `[5장]`

1. 1단계에서 Reward model을 학습한다
2. 2단계에서 사람은 각 답변에 절대 점수를 매긴다
3. 3단계에서 Reward model을 보상 함수로 사용해 PPO로 학습한다
4. 사람 평가자가 필요 없어 비용이 적게 든다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — 1단계 = **SFT**(①✗), 2단계 = 사람이 **선호도 순위**(Ranking)(②✗), annotator **비용이 큰 것**이 한계(④✗).

</details>

**M20.** LoRA가 Adapter Tuning보다 나은 이유로 **틀린** 것은? `[5장]`

1. 더 적은 파라미터로 빠르게 적응한다
2. 병렬로 진행되어 추가적인 추론 지연이 없다
3. 입력 시퀀스 길이를 줄이지 않고 훈련할 수 있다
4. 원래 모델의 파라미터 크기 자체를 줄여 메모리를 절약한다

<details markdown="1"><summary>정답 보기</summary>

**정답 ④** — PEFT(LoRA 포함)는 **원래 모델 크기를 줄이지 않음** → 그래서 **Quantization**이 필요.

</details>

**M21.** "PEFT는 ( ㉠ )을 줄이고, Quantization은 ( ㉡ )을 줄인다. 둘을 결합한 것이 ( ㉢ )이다." 에 들어갈 말로 옳은 것은? `[5장]`

1. ㉠ 메모리 ㉡ 학습 파라미터 수 ㉢ LoRA
2. ㉠ 학습 파라미터 수 ㉡ 메모리(비트 수) ㉢ QLoRA
3. ㉠ 학습 데이터 ㉡ 추론 시간 ㉢ RLHF
4. ㉠ 학습 파라미터 수 ㉡ 메모리(비트 수) ㉢ Adapter

<details markdown="1"><summary>정답 보기</summary>

**정답 ②**

</details>

**M22.** Prompt의 구성 요소 4가지가 **아닌** 것은? `[6장]`

1. Instruction
2. Context
3. Output Indicator
4. Reward Signal

<details markdown="1"><summary>정답 보기</summary>

**정답 ④** — 나머지 하나는 **Input Data**.

</details>

**M23.** Chain-of-Thought에 대한 설명으로 옳은 것은? `[6장]`

1. 예시 없이 질문만 주는 방법이다
2. 예시에 결론만 보여주는 Few-shot의 다른 이름이다
3. 추론 과정을 포함한 예제를 제공해 복잡한 산술·상식·기호 추론 성능을 높인다
4. PaLM 540B에서 정확도가 58.1% → 17.7%로 떨어졌다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — ④는 방향이 반대(**17.7% → 58.1%** 상승).

</details>

**M24.** Prompt Engineering이 여전히 어려운 이유로 슬라이드에 제시되지 **않은** 것은? `[6장]`

1. 표현과 서식에 대한 민감도
2. 예시와 샘플 순서의 민감도
3. 모델 파라미터 수가 공개되지 않음
4. 모델 평가의 어려움

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — 나머지 하나는 **재서술 문장 변화에 의한 성능 분산**.

</details>

**M25.** Agent / AI Agent / Agentic AI에 대한 설명으로 옳은 것은? `[7장]`

1. Agent는 반드시 LLM을 사용해야 한다
2. AI Agent는 Orchestrator가 하위 에이전트 결과를 통합·검증한다
3. Agentic AI는 상위 목표를 스스로 하위 목표로 분해하고 실패 시 재계획한다
4. 온도조절기는 Agentic AI의 예시이다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — Agent는 **LLM 없이도** 가능(①✗), Orchestrator는 **Agentic AI**(②✗), 온도조절기는 **Agent**(④✗).

</details>

**M26.** LLM이 Agent에 적합한 이유 중 "Multi-modal fusion으로 지각 공간을, Embodiment·Tool로 행동 공간을 확장한다"에 해당하는 성질은? `[7장]`

1. 자율성
2. 반응성
3. 능동성
4. 사회성

<details markdown="1"><summary>정답 보기</summary>

**정답 ②** — 능동성은 **next token prediction → 추론·계획 능력**.

</details>

**M27.** Agent의 task 수행 필요 요건과 해결 방법의 연결로 옳은 것은? `[8장]`

1. Reasoning — RAG
2. Knowledge — Tool Use
3. Computation — Tool Use
4. Knowledge — Chain-of-Thought

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — Reasoning–**프롬프트 기법(CoT 등)** / Knowledge–**RAG** / Computation–**Tool Use**.

</details>

**M28.** CoALA의 내부 행동 중 "장기 기억에서 정보를 검색해 Working Memory로 가져오는 행동"은? `[11장]`

1. Retrieval
2. Reasoning
3. Learning
4. Grounding

<details markdown="1"><summary>정답 보기</summary>

**정답 ①** — Learning은 반대 방향(→장기 기억 저장), Grounding은 **외부** 행동.

</details>

**M29.** "과거에 경험했던 사건이나 상호작용을 저장하는 공간"은? `[11장]`

1. Working Memory
2. Semantic Memory
3. Episodic Memory
4. Procedural Memory

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — Semantic = 사실·개념, Procedural = 방법·스킬, Working = 현재 처리 중.

</details>

**M30.** Multi-Agent Architecture에 대한 설명으로 옳은 것은? `[12장]`

1. Vertical에서는 모든 agent가 공용 스레드에서 소통한다
2. Horizontal에서는 리더가 과업을 배정한다
3. MetaGPT는 structured output과 publish-subscribe를 사용하며 vertical에 가깝다
4. DyLAN은 리더가 기여도를 평가해 팀을 고정한다

<details markdown="1"><summary>정답 보기</summary>

**정답 ③** — 공용 스레드는 **Horizontal**(①✗), Horizontal은 agent가 **자원**(②✗), DyLAN은 **리더 없이** round마다 LLM Ranker/peer rating으로 **재편**(④✗).

</details>

---

## Part 2 · 빈칸 채우기 (25문항)

**B1.** 임베딩의 두 가지 역할은 자연어의 ( ㉠ ) 함축과 자연어 간 ( ㉡ ) 계산이다. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **의미적인 정보** ㉡ **유사도**

</details>

**B2.** 코사인 유사도는 ( ㉠ ) ~ ( ㉡ ) 사이의 값이며, ( ㉢ )에 가까울수록 유사하다. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **−1** ㉡ **1** ㉢ **1**

</details>

**B3.** One-hot encoding의 한계는 ( ㉠ ) 문제와 단어의 ( ㉡ )를 표현할 수 없다는 것이다. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **희소(Sparsity)** ㉡ **유사도**

</details>

**B4.** `idf(d,t) = log( ( ㉠ ) / (1 + ( ㉡ )) )` `[2장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **n (전체 문서 수)** ㉡ **df(t) (단어 t가 등장한 문서 수)**

</details>

**B5.** AutoEncoder는 입력 계층 X, 입력 정보를 압축한 ( ㉠ ), 출력 계층 X̃ 로 구성되며 ( ㉡ ) 학습이다. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Latent vector Z** ㉡ **비지도**

</details>

**B6.** Seq2Seq는 ( ㉠ )이 입력을 하나의 ( ㉡ )로 압축하고, ( ㉢ )가 이를 받아 한 단어씩 출력한다. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Encoder** ㉡ **Context vector** ㉢ **Decoder**

</details>

**B7.** Transformer 논문의 제목은 "( )"(2017)이다. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

**Attention Is All You Need**

</details>

**B8.** Language Modeling의 목표는 단어 시퀀스의 생성 가능성을 모델링하여 ( )의 확률을 예측하는 것이다. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

**미래 토큰**

</details>

**B9.** LLM은 방대한 텍스트 데이터로 학습된 ( ㉠ ) 개의 파라미터를 가진 ( ㉡ ) 기반의 Language Model이다. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **수천 억** ㉡ **Transformer**

</details>

**B10.** LLM의 Emergent Abilities 3가지: ( ㉠ ), Instruction Following, ( ㉡ ) `[4장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **In-context Learning** ㉡ **Step-by-Step Reasoning**

</details>

**B11.** GPT는 ( ㉠ ) Pre-trained Transformer의 약자이며, Transformer의 생성형 ( ㉡ ) 구조 기반의 ( ㉢ ) 모델이다. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Generative** ㉡ **Decoder** ㉢ **Autoregressive**

</details>

**B12.** GPT Framework: Step1 ( ㉠ ) → Step2 ( ㉡ ) `[4장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Unsupervised Pre-Training** ㉡ **Supervised Fine-tuning**

</details>

**B13.** GPT-3의 논문 제목은 "Language Models are ( )"이다. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

**Few-shot Learners** (GPT-2는 "Language Models are Unsupervised Multitask Learners")

</details>

**B14.** LLM 학습 3단계: ( ㉠ ) → Adaptation Tuning → ( ㉡ ) `[5장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Pre-training** ㉡ **Utilization**

</details>

**B15.** Instruction Tuning은 Instruction & input text와 output text의 ( ㉠ ) 데이터셋으로 ( ㉡ ) 형식으로 학습시키는 것이다. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **pair** ㉡ **supervised (지도)**

</details>

**B16.** RLHF 3단계: Supervised Fine-tuning → ( ㉠ ) → RL Fine-tuning. 3단계에서는 ( ㉡ ) 알고리즘을 사용한다. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Reward Model Training** ㉡ **PPO (Proximal Policy Optimization)**

</details>

**B17.** LoRA: `W0 + ΔW = W0 + ( )` `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**AB** (A ∈ ℝ^(d×m), B ∈ ℝ^(m×d))

</details>

**B18.** Adapter Tuning에서 d=1024, m=16이면 학습 파라미터는 1,048,576개에서 ( )개로 줄어든다. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**32,768** (= 2 × 1024 × 16)

</details>

**B19.** Prompt의 구성 요소: Instruction, ( ㉠ ), Input Data, ( ㉡ ) `[6장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Context** ㉡ **Output Indicator**

</details>

**B20.** PaLM 540B의 수학 정답률은 CoT 적용 전 ( ㉠ )%에서 적용 후 ( ㉡ )%로 상승했다. `[6장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **17.7** ㉡ **58.1**

</details>

**B21.** ReAct = ( ㉠ ) + ( ㉡ ). ( ㉠ )은 행동을 돕고, 행동은 ( ㉠ )을 돕는다. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Reasoning** ㉡ **Acting**

</details>

**B22.** RAG에서 질문과 관련된 정보를 코퍼스에서 끌어오는 부품을 ( ㉠ )라 하며, 대표적으로 ( ㉡ ), DPR이 있다. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Retriever** ㉡ **BM25**

</details>

**B23.** Memory Retrieval은 ( ㉠ ) / ( ㉡ ) / ( ㉢ ) 기반으로 자동 검색한다. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Recency** ㉡ **Relevance** ㉢ **Importance**

</details>

**B24.** CoALA는 Memory Modules, ( ㉠ ), ( ㉡ )로 구성된다. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **Action Space** ㉡ **Decision-making Process**

</details>

**B25.** AI Agent 아키텍처의 (거의) 필수 구성요소: Components = LLM, ( ㉠ ), database / Process = reasoning, ( ㉡ ), tool calling `[12장]`

<details markdown="1"><summary>정답 보기</summary>

㉠ **tool** ㉡ **planning**

</details>

---

## Part 3 · 단답·서술 (111문항)


### 1장 — 과목 개요와 AI Agent 역사

**Q1.** 기존 AI(챗봇)와 AI 에이전트의 차이를 예시와 함께 설명하시오. `[1장]`

<details markdown="1"><summary>정답 보기</summary>

기존 AI(챗봇)는 사용자가 질문하면 **답을 해주는 '백과사전' 혹은 '1인 전문가'** 다. 예를 들어 "내일 날씨 어때?"에 "서울 날씨는 맑습니다"라고 **답변하고 끝난다.**
AI 에이전트는 사용자가 **목표를 주면 스스로 계획을 세우고 실행까지 하는 '비서' 혹은 '팀 프로젝트 매니저'** 다. 예를 들어 "시애틀행 비행기 예약해 줘"라고 하면 **목표 수립 → 비행기 검색 → 가격 비교 → 최적 옵션 선택 → 예약 완료**까지 수행한다.

</details>

**Q2.** AI Agent의 4대 구성요소와 각각의 역할(비유)을 쓰시오. `[1장]`

<details markdown="1"><summary>정답 보기</summary>

- **LLM Model** — 머리(두뇌): 이해하고 추론
- **Tool / Public API** — 손, 발(행동 도구): 실제 검색·계산·예약
- **DB / Memory** — 기억(상태 저장): **Short term / Long term**
- **Planning** — 작업 계획: **복잡한 목표를 작은 단위의 작업들로 분해** (예: "웹사이트 만들어줘" → 시장조사, 구조설계, 코드 작성)

</details>

**Q3.** AI Agent 유형을 옛날부터 현재 순으로 5가지 쓰시오. `[1장]`

<details markdown="1"><summary>정답 보기</summary>

**Rule-based Agent → Planning Agent → LLM-based Reactive Agent → Autonomous Agent → Multi-Agent / Graph-based Agent**

</details>

**Q4.** Rule-based Agent의 특징을 2가지 이상 쓰시오. `[1장]`

<details markdown="1"><summary>정답 보기</summary>

- 조건-행동 규칙(**If-Then Rules**) 기반, **AI 적용 X**
- 입력에 **정해진 규칙으로 반응**
- **지능적 추론이나 적응 불가**
- **사전 정의된 환경에서 안정 작동**
- 여전히 일부 **통제용 rule logic**에 사용
- 대표: **Expert Systems, RPA (UiPath 등)**

</details>

**Q5.** Autonomous Agent(AutoGPT, BabyAGI 등)의 특징과 한계를 쓰시오. `[1장]`

<details markdown="1"><summary>정답 보기</summary>

특징: **목표 → 계획 → 반복 실행(Loop 구조)**. 목표 설정 후 **작업 분해를 반복**하며, **외부 API·파일 시스템 조작 가능**. **"행동하는 AI" 인식의 분기점**.
한계: **실행 불안정성, 무한 루프 문제** (종료 조건을 스스로 판단하지 못해 같은 작업을 반복).

</details>

**Q6.** Planning Agent의 대표 기술과 특징을 쓰시오. `[1장]`

<details markdown="1"><summary>정답 보기</summary>

대표 기술: **STRIPS, GOAP, HTN Planning**
특징: 목표 기반 행동 계획(Task Planning), **행동 시퀀스를 스스로 계획**, 게임·로봇·로직 기반 AI에 활용, **자연어는 아님**, **현대 Agent Planner 구조의 뿌리**

</details>

---

### 2장 — 자연어 임베딩

**Q7.** 임베딩(Embedding)의 정의와 두 가지 역할을 쓰시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

정의: 자연어 처리에서 **특징 추출을 통해 자연어를 수치화(벡터화)하는 과정**. 단어·문장을 벡터로 변환해 **벡터 공간에 끼워넣는다(embed)** 는 의미.
역할: ① **자연어의 의미적인 정보 함축** ② **자연어 간 유사도 계산**

</details>

**Q8.** 임베딩이 처음 소개된 논문과 연도는? `[2장]`

<details markdown="1"><summary>정답 보기</summary>

**2003년, "A Neural Probabilistic Language Model"**

</details>

**Q9.** 단어 유추 평가(word analogy test)란 무엇이며, 무엇을 확인하는가? `[2장]`

<details markdown="1"><summary>정답 보기</summary>

(첫 번째 단어 벡터) − (두 번째 단어 벡터) + (세 번째 단어 벡터)를 계산하여 짝이 되는 단어를 찾는 평가. 예: **아들 − 딸 + 소년 = 소녀**.
아들-딸의 관계와 소년-소녀의 의미 차이가 임베딩에 함축되어 있으면 **성능 좋은 임베딩임을 간접적으로 확인**할 수 있다. (임베딩은 **사칙연산이 가능**하여 의미적·문법적 관계를 도출할 수 있음)

</details>

**Q10.** 코사인 유사도의 값의 범위와 해석은? `[2장]`

<details markdown="1"><summary>정답 보기</summary>

두 벡터 간 **코사인 각도**로 유사도를 계산. 범위 **−1 ~ 1**, **1에 가까울수록 유사도가 높음**.

</details>

**Q11.** 고차원 벡터를 시각화할 때 쓰는 차원 축소 기법 2가지는? `[2장]`

<details markdown="1"><summary>정답 보기</summary>

**t-SNE, PCA**

</details>

**Q12.** One-hot encoding의 한계 2가지를 설명하시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

① **희소 문제(Sparsity problem)**: 벡터 차원이 단어 사전 크기만큼이고 1개 차원만 1, 나머지는 0인 **희소 행렬**이 된다. (예: 사전 20,000개 → 19,999개가 0) 단어가 늘어날수록 **표현 효율성이 저하**되고 **공간 복잡도가 증가**한다.
② **단어의 유사도를 표현할 수 없음**: **모든 단어 간 거리가 동일**하여 유사도 판단이 불가능하다. (예: 중학교 [1,0,0], 고등학교 [0,1,0], 대학교 [0,0,1])

</details>

**Q13.** TF와 IDF가 각각 무엇을 의미하는지 쓰고, TF-IDF의 활용처를 쓰시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

- **TF (Term Frequency)**: 특정 단어가 **그 문서에서 얼마나 자주** 나오는가
- **IDF (Inverse Document Frequency)**: 전체 문서에서 특정 단어가 **얼마나 희귀한가** (`df(t)`에 반비례 → 여러 문서에 공통적으로 나오는 단어는 중요도가 낮음)
- TF-IDF = **TF × IDF**, 문서-단어 행렬 내 각 단어의 중요도에 가중치를 주는 방법
- 활용: **문서의 유사도 계산, 검색 시스템에서 검색 결과의 중요도 결정, 문서 내 특정 단어의 중요도 계산**

</details>

**Q14.** IDF 공식 `idf = log(n / (1 + df(t)))` 에서 log를 쓰는 이유 2가지는? `[2장]`

<details markdown="1"><summary>정답 보기</summary>

① **가중치를 적절히 조절하기 위해서** (문서 수가 많을 때 값이 지나치게 커지는 것을 방지)
② **분모가 0이 되는 경우(특정 단어가 문서 전체에서 등장하지 않는 경우)를 방지** (분모의 `1 +`)

</details>

**Q15.** 문서 3개 d1="AI is the future", d2="AI and data science", d3="Data is important"에서 단어 "AI"의 각 문서별 TF, IDF, TF-IDF를 구하고(IDF=log(N/df) 사용), "future"와 비교해 해석하시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

- TF: d1 = 1/4 = **0.25**, d2 = 1/4 = **0.25**, d3 = **0**
- IDF("AI") = log(3/2) ≈ **0.176**
- TF-IDF: d1 ≈ **0.044**, d2 ≈ **0.044**, d3 = **0**
- "future"는 d1에만 등장 → IDF = log(3/1) ≈ 1.099(슬라이드 값) → d1의 TF-IDF ≈ **0.275**
- 해석: **한 문서에만 등장하는 단어가 여러 문서에 등장하는 단어보다 TF-IDF가 높다** → TF-IDF는 **그 문서를 특징짓는 단어**에 높은 점수를 준다.

</details>

**Q16.** One-hot encoding과 TF-IDF를 표현 방식, 벡터 차원, 값 분포, 장점, 한계로 비교하시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

| 구분 | One-hot | TF-IDF |
|---|---|---|
| 표현 방식 | 단어 → 0과 1 벡터 | 단어 → 중요도 가중치 벡터 |
| 벡터 차원 | 어휘 크기만큼 | 어휘 크기만큼 |
| 값 분포 | 0과 1 | 0과 가중치(실수) |
| 장점 | 단순, 구현 쉬움 | 단어 중요도 반영, 검색/분류에 효과적 |
| 한계 | 의미 정보 없음, 차원 크다 | 문맥 무시, 희소성, 동의어/다의어 처리 불가 |

</details>

**Q17.** Sparse representation과 Dense representation을 비교하시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

- **Sparse**: 단어 인덱스 값만 1(또는 가중치), 나머지는 0 → **벡터·행렬 대부분이 0**. 차원 = **단어 집합 크기**. 의미 정보 없음.
- **Dense**: 벡터 차원을 단어 집합 크기가 아닌 **사용자가 설정한 값**으로 맞추고, **연속적인 실수값**으로 인코딩. **적은 차원**으로 표현, 각 차원이 모두 정보를 포함해 **학습이 수월**, 단어 사전이 커져도 **차원이 일정 → 공간 복잡도 개선**, **더 큰 일반화 능력**, 의미 이해·정보 검색 향상.

</details>

**Q18.** Dense representation이 일반화 능력이 큰 이유를 '강아지'와 '멍멍이' 예시로 설명하시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

'강아지'는 자주, '멍멍이'는 적게 출현한다고 할 때, **희소 표현**에서는 두 단어의 관계가 **전혀 표현되지 않아** '멍멍이'를 **따로 학습**해야 한다. **밀집 표현**에서는 두 단어가 **서로 비슷한 벡터로 표현**되므로, '강아지'로 학습한 것이 '멍멍이'에도 적용되어 **일반화가 가능**하다.

</details>

**Q19.** AutoEncoder의 구조와 학습 방식을 쓰시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

1986년 "Learning Internal Representation by Error Backpropagation" 논문에서 소개. **3개의 계층**: **입력 계층 X / 입력 데이터의 정보를 압축하고 있는 Latent vector Z / 출력 계층 X̃**. **Label이 없는 데이터로부터 낮은 차원의 특성 표현을 학습하는 비지도 학습**.

</details>

**Q20.** 임베딩 기법의 발전 3단계를 쓰시오. `[2장]`

<details markdown="1"><summary>정답 보기</summary>

**통계 기반의 자연어처리 → 딥러닝 기반의 자연어처리 → 전이학습 기반의 자연어처리 (BERT, GPT 등)**

</details>

---

### 3장 — Seq2Seq와 Transformer

**Q21.** RNN 계열 모델(RNN, LSTM, GRU)의 명확한 한계는? `[3장]`

<details markdown="1"><summary>정답 보기</summary>

**모델의 입력/출력 크기가 고정**된다는 한계. 자연어·소리 등은 **가변적인 길이의 입출력**을 가지므로 대응하기 어렵다. (예: "I am a student" → "je suis étudiant")

</details>

**Q22.** Seq2Seq의 Encoder, Context vector, Decoder의 역할을 쓰시오. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

- **Encoder**: 입력 문장의 모든 단어를 **순차적으로 입력받은 후** 마지막에 **모든 단어 정보를 압축해서 하나의 벡터로** 만듦
- **Context vector**: 입력 문장 전체 정보가 압축된 그 벡터
- **Decoder**: Context vector를 받아 번역된 단어를 **한 개씩 순차적으로 출력** → **서로 다른 길이의 입/출력 시퀀스에 대응**
- (Google, 2014, 두 개의 LSTM 네트워크 사용)

</details>

**Q23.** Transformer가 개선한 기존 Seq2Seq / RNN의 고질적 한계 3가지는? `[3장]`

<details markdown="1"><summary>정답 보기</summary>

① **고정된 크기의 벡터에 모든 정보 압축 → 정보 손실 발생**
② **Vanishing Gradient Problem (기울기 소실)**
③ **입력의 순차적 처리 → 병렬화 불가능**

</details>

**Q24.** Transformer를 처음 제안한 논문 제목과 연도, 핵심 특징을 쓰시오. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

**"Attention Is All You Need" (2017)**. **Seq2Seq(Encoder-Decoder) 구조를 따르면서도 Attention만으로 구현된 모델**. **RNN을 사용하지 않고** Encoder-Decoder 구조로만 설계하여 **RNN보다 우수한 성능**. 지금도 다양한 분야에서 쓰이는 **범용적 모델**.

</details>

**Q25.** Transformer의 입력이 단순한 embedding vector가 아닌 이유는? `[3장]`

<details markdown="1"><summary>정답 보기</summary>

Transformer는 RNN처럼 순서대로 넣지 않고 **모든 단어를 한꺼번에(병렬로)** 입력하므로, 그대로 넣으면 **단어의 순서를 알 수 없다**. 그래서 **Embedding vector에 Positional Encoding(위치 정보)을 더해 조정된 값**을 입력으로 사용한다.

</details>

**Q26.** Transformer의 Attention 3종류를 쓰고 각각 어디서 무엇을 하는지 쓰시오. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

- **Encoder Self-Attention** (인코더): 입력 문장 내 단어들끼리 서로 참조
- **Masked Decoder Self-Attention** (디코더): 출력 문장 단어들끼리 참조하되 **아직 생성하지 않은 미래 단어는 가림**
- **Encoder-Decoder Attention** (디코더): 디코더가 **인코더의 출력**을 참조

</details>

**Q27.** Language Modeling의 목표는? `[3장]`

<details markdown="1"><summary>정답 보기</summary>

**단어 시퀀스의 생성 가능성을 모델링하여 미래 토큰의 확률을 예측**하는 것.

</details>

**Q28.** 언어 모델 발전 4단계(SLM, NLM, PLM, LLM)의 시기와 대표 모델을 쓰시오. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

| | 시기 | 핵심 | 대표 모델 |
|---|---|---|---|
| **SLM** (Statistical) | 1990s | 확률 기반 (N-gram, MLE) | N-gram LM, Kneser-Ney Smoothing |
| **NLM** (Neural) | 2010s | 신경망 + 단어 임베딩 | word2vec, LSTM, Seq2Seq |
| **PLM** (Pre-trained) | 2018+ | 대규모 비지도 사전학습 + 작업별 파인튜닝 | BERT, GPT-2, T5 |
| **LLM** (Large) | 2020+ | 수십억~수천억 파라미터, 사전학습 + 인간 가치 정렬 | GPT-4, PaLM 2, LLaMA 3 |

핵심 전환: **대규모 사전학습 + 다운스트림 작업 파인튜닝이 표준 패러다임이 되었다**

</details>

**Q29.** SLM과 NLM의 한계(특징)를 각각 쓰시오. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

- **SLM**: **데이터 의존적, 맥락 이해 한계, 긴 문장 처리 어려움**
- **NLM**: 분산 표현 학습, 문맥 반영 개선, 그러나 **기울기 소실 문제**

</details>

**Q30.** BERT와 GPT는 각각 Transformer의 어느 부분에서 나왔는가? `[3장]`

<details markdown="1"><summary>정답 보기</summary>

**BERT ← 인코더**, **GPT ← 디코더**

</details>

**Q31.** Pre-trained Language Model(PLM)의 정의와 Pre-training/Fine-tuning 방식의 장점을 쓰시오. `[3장]`

<details markdown="1"><summary>정답 보기</summary>

PLM: **많은 양의 텍스트 데이터를 활용해 일반적인 수준의 '언어 이해'가 가능하도록 사전 학습을 시킨 언어 모델**.
장점: 사전 학습된 모델을 텍스트 분류, 생성, 번역 등 **다양한 downstream task에서 fine-tuning하여 사용** 가능하며, **task마다 end-to-end로 따로 학습하는 방식에 비해 성능을 비약적으로 끌어올림**.

</details>

---

### 4장 — LLM과 GPT

**Q32.** LLM의 정의를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

**방대한 텍스트 데이터로 학습된 수천 억 개의 파라미터를 가진 Transformer 기반의 Language Model**. 언어를 이해하고 복잡한 과업을 수행하는 데 강력한 능력을 가짐.

</details>

**Q33.** 기존 PLM과 구별되는 LLM의 가장 큰 특징은? 그 예 3가지를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

**Emergent Abilities (창발적 능력)**. 예: **In-context Learning, Instruction Following, Step-by-Step Reasoning**

</details>

**Q34.** LLM을 사용하는 이점 3가지는? `[4장]`

<details markdown="1"><summary>정답 보기</summary>

① **사전 학습된 단일 모델이 여러 task에 사용될 수 있음** (번역, 문장 생성, 분류, QA 등)
② **Fine-tuning을 위한 특정 task의 데이터가 많이 필요하지 않음** (Few-shot, zero-shot에서도 우수)
③ **학습 데이터와 파라미터를 증가시킴으로써 성능을 지속적으로 향상**시킬 수 있음

</details>

**Q35.** GPT의 풀네임과 Autoregressive의 의미를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

**Generative Pre-trained Transformer**. Transformer의 **생성형 Decoder 구조** 기반의 Autoregressive 모델.
Autoregressive: **주어진 입력의 일부를 사용하여 이후에 오는 부분을 예측**, 즉 **주어진 연속된 단어의 다음 단어를 맞추는 방식**.

</details>

**Q36.** GPT Framework의 2단계를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

**Step 1: Unsupervised Pre-Training** — 대량의 말뭉치로 언어모델 학습 (지금까지의 토큰 순서로 다음 토큰 확률 추정)
**Step 2: Supervised Fine-tuning** — Labeled Data로 목표 Task에 맞게 미세조정

</details>

**Q37.** GPT-1과 GPT-2의 목적함수(Objective)를 비교하고 그 의미를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

- GPT-1: **P(Output | Input)**
- GPT-2: **P(Output | Input, Task)**
- 의미: GPT-2는 **Task까지 조건으로** 받아 **다른 Task에 대해서는 동일한 Input임에도 다른 Output을 생성** → **동일한 Unsupervised Model로 Multiple Tasks 학습** (Task Conditioning)

</details>

**Q38.** GPT-3가 Fine-tuning을 생략한 이유, 즉 Fine-tuning의 한계 3가지를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

① 새로운 Task에 대한 **Task별 Labeled Dataset이 필요**
② 미세조정을 거쳐 작은 Task의 분포를 따르면 **과적합이 발생하여 분포 밖 Dataset에 대해 일반화 성능을 잃을 수 있음**
③ **사람과 같이 적은 샘플로도 Task를 수행하는 능력**이 필요

</details>

**Q39.** In-context Learning의 정의와 Fine-tuning과의 핵심 차이는? `[4장]`

<details markdown="1"><summary>정답 보기</summary>

정의: **프롬프트의 맥락적 의미(In-context)를 모델이 이해하고, 이에 대한 답변을 생성**하는 것. Demo Context 구성을 위한 **소수의 예시 필요**.
차이: **사전학습이나 미세조정처럼 모델을 업데이트하지 않고, 별도의 모델 학습 과정이 없다** (파라미터가 바뀌지 않음).

</details>

**Q40.** Zero-shot, One-shot, Few-shot을 구분하시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

- **Few-shot**: Task 설명 + Context Window k에 맞는 **몇 개의 예제** 제공
- **One-shot**: **하나의 예제만** 제공
- **Zero-shot**: **예시 제공 없음**, 사전 지식만으로 예측

</details>

**Q41.** GPT-3의 한계 3가지를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

① **긴 문장 구성에 일관성을 잃고 Text Sequence를 반복**하는 경향
② **모델의 단방향성**으로 인해 **자연어 추론과 같은 Task를 잘 해내지 못함** (→ 양방향 모델 고려 가능)
③ **각 Token에 동일한 가중치가 부여**되므로 **목표 지향적 예측 개념 결여**

</details>

**Q42.** GPT-1, GPT-2, GPT-3의 출현 연도와 파라미터 수를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

GPT-1: **2018, 117M** / GPT-2: **2019, 1.5B** / GPT-3: **2020, 175B**

</details>

**Q43.** GPT-1, 2, 3의 핵심 개념과 혁신 포인트를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

- GPT-1: **PLM + SFT** / **BERT보다 먼저 나온 Transformer LM**
- GPT-2: **거대 언어모델 (Generative LM)**, SFT 과정을 없애자 / **멀티태스킹 가능해짐**
- GPT-3: **Few-shot / Zero-shot LLM**, 프롬프트만으로 대부분 작업 수행(In-context learning) / **지능적 프롬프트 이해**

</details>

**Q44.** GPT-3의 사회적 영향(Broader Impacts) 3가지를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

① **언어모델의 오용**: 가짜뉴스, 스팸, 피싱
② **공정성, 편향성 및 대표성**: 인터넷 데이터의 편견과 편향(성별, 민족, 인종, 종교)을 그대로 학습
③ **에너지 소비**: 학습에 상당한 자원 소비(약 50억, Tesla V100 1대로 355년), 훈련 후에는 효율적

</details>

**Q45.** 추론 모델(Reasoning Model)과 비추론 모델(Standard Model)의 차이를 쓰시오. `[4장]`

<details markdown="1"><summary>정답 보기</summary>

- **추론 모델**: 질문을 받으면 **내부적으로 '생각의 사슬(CoT)'을 거치며 스스로 논리적인 단계를 나누어 검토한 뒤** 최종 답변 (예: 깊게 고민하는 수학자 / o1, o3 등)
- **비추론 모델**: **학습한 패턴을 바탕으로 가장 확률이 높은 단어를 실시간으로 빠르게** 출력 (예: 퀴즈 달인 / GPT-4o 등)

</details>

---

### 5장 — Adaptation Tuning

**Q46.** LLM 학습 과정(Training Process of LLMs) 3단계와 각 정의를 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

- **Pre-training**: **LLM의 기본적인 능력을 습득하는 과정** (Data, Architecture, Pre-training task, Optimization and Scalable Training Techniques)
- **Adaptation Tuning**: **LLM을 특정한 목표에 따라 추가로 adaptation 시키는 과정** (Instruction tuning, Alignment Tuning, Parameter efficient model adaptation)
- **Utilization**: **LLM을 효과적으로 사용하는 방법** (Prompt Engineering)

</details>

**Q47.** GPT-3에서 ChatGPT로의 중요한 변화는 무엇으로 볼 수 있는가? `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**Adaptation tuning의 수행**. GPT-1~3까지는 pre-train으로 성능을 확보했다면, GPT-3부터 InstructGPT, ChatGPT까지는 **adaptation tuning을 통해** 성능을 확보하기 시작함.

</details>

**Q48.** Instruction Tuning의 등장 배경 2가지와 정의를 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

배경 ① **사용자의 의도에 맞는 답변 출력**: LLM은 다음 단어 예측으로 pre-train 되어 질문에 대한 답이 아닌 **이어질 만한 후속 문장을 출력**할 가능성이 큼 (Users intent ≠ Language modeling)
배경 ② **Zero-shot 성능 향상**: 기존 LLM은 few-shot 성능은 향상되었으나 **zero-shot 성능은 그만큼 향상되지 못함**
정의: **Instruction(지시문) & input text와 output text의 pair 데이터셋을 통해 supervised 형식으로 학습**시키는 것

</details>

**Q49.** FLAN(2021)의 결론 3가지를 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

① 기존 LLM의 **zero-shot 성능을 향상시킬 수 있는 instruction tuning 기법을 처음으로 제안**
② Instruction tuning에 사용되는 **task cluster의 개수가 많아질수록 unseen task에서의 성능이 향상**
③ **크기가 작은 모델에서는 instruction tuning 시 오히려 성능이 하락**하며, 효과를 얻으려면 **모델 크기가 일정 수준 이상**이어야 함

</details>

**Q50.** Alignment의 3가지 기준(3H)과 각 정의를 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

- **Helpfulness**: 사용자가 **과제를 해결하는 데 도움**이 되어야 함
- **Honesty**: **조작하지 않고 정확한 내용**을 제공해야 함
- **Harmlessness**: **모욕적·차별적 표현을 생성해서는 안 되며, 악의적인 목적의 요청을 감지**할 수 있어야 함

</details>

**Q51.** RLHF의 정의와 필요한 3가지 요소를 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

정의: **강화학습을 이용해 인간의 피드백으로부터 LLM을 최적화하는 방법**
요소: **Human annotator** (인간이 직접 피드백해 선호도 모델링) / **Reward model** (인간의 선호도를 예측하는 모델) / **Aligned model** (인간의 선호도를 반영하여 학습시키고자 하는 모델)

</details>

**Q52.** RLHF의 3단계를 순서대로 쓰고 각 단계를 설명하시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**Step 1: Supervised Fine-tuning** — **인간이 작성한 prompt 데이터셋**으로 LM을 fine-tuning → 어느 정도 인간의 의도에 맞는 답변 생성 가능
**Step 2: Reward Model Training** — 1단계 LM이 **여러 답변을 생성**하고 **인간 평가자가 선호도 순위**를 매김 → 이를 통해 **인간의 선호도를 모방하는 reward model** 학습 (이후 aligned model 평가에 사용)
**Step 3: RL Fine-tuning** — **Reward model을 보상 함수**로 사용하여 **보상을 최대화하도록 aligned model의 정책을 fine-tuning**, 이때 **PPO(Proximal Policy Optimization)** 사용

</details>

**Q53.** RLHF의 한계 2가지는? `[5장]`

<details markdown="1"><summary>정답 보기</summary>

① **Human annotator를 고용해 데이터셋을 확보하기 위한 비용이 많이 필요**
② **주관적인 요인에 따라 학습 데이터셋의 품질 편차가 존재**

</details>

**Q54.** PEFT가 가능한 근거(low intrinsic dimension)를 설명하시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

PLM은 **low intrinsic dimension**을 가짐 → **모델이 크고 복잡하지만 실제로 중요한 정보를 나타내는 특성의 수가 상대적으로 적음**. 예: **RoBERTa는 오직 200개의 학습 가능한 파라미터로 90% 성능 달성**.

</details>

**Q55.** Adapter Tuning을 설명하고, d=1024, m=16일 때 파라미터 수 변화를 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**기존 Layer 위에 adapter layer를 추가**하고, adapter layer만 target task에 맞게 최적화하며 **기존 LLM 파라미터는 고정**. **Down Projection**(핵심 변화만 추출) → **Up Projection**(원래 LLM 표현 공간으로 복원).
파라미터: 1024×1024 = **1,048,576개** → 2×1024×16 = **32,768개**로 감소.

</details>

**Q56.** LoRA의 수식과 ΔW의 의미를 쓰고, d=1024, m=8일 때 학습 파라미터 수를 구하시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**W0 + ΔW = W0 + AB**, A ∈ ℝ^(d×m), B ∈ ℝ^(m×d), m = rank의 차원. PLM 파라미터(W0)는 고정하고 분해된 행렬(A, B)만 학습.
ΔW의 의미: **새로운 task에 적응하기 위해 필요한 변화량만 학습하면 된다**.
파라미터 수: 1024 × 8 × 2 = **16,384개**

</details>

**Q57.** LoRA가 Adapter Tuning보다 나은 이유 3가지는? `[5장]`

<details markdown="1"><summary>정답 보기</summary>

① **adapter tuning보다도 낮은 parameter tuning**으로 새로운 task에 **fast adaptation** 가능
② **순차적으로 진행되는 adapter와 달리 병렬적으로 진행**되어 **추가적인 추론 지연(inference latency)이 발생하지 않음**
③ **입력 시퀀스 길이를 줄이지 않고 훈련 가능**

</details>

**Q58.** 양자화(Quantization)가 필요한 이유는? `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**PEFT 방식들은 원래 모델의 파라미터 크기를 줄이지 않음** → 원래 모델의 파라미터를 저장하고 있어야 하므로 **메모리 및 계산 비용이 크게 증가**. 그래서 파라미터를 **더 작은 비트로 표현**(FP32→FP16→INT8→INT4)하여 메모리를 줄인다.

</details>

**Q59.** PEFT, Quantization, QLoRA의 관계를 한 문장으로 쓰시오. `[5장]`

<details markdown="1"><summary>정답 보기</summary>

**PEFT는 학습할 파라미터 수를 줄이고, Quantization은 파라미터의 표현 크기(메모리 사용량)를 줄인다. 이 두 가지를 결합한 QLoRA(4-bit로 양자화해 freeze한 base LLM + LoRA Adapter)는 거대한 LLM을 작은 자원으로도 효과적으로 활용할 수 있게 해준다.**

</details>

---

### 6장 — Prompt Engineering

**Q60.** Prompt와 Prompt engineering의 정의를 쓰시오. `[6장]`

<details markdown="1"><summary>정답 보기</summary>

- **Prompt**: LLM으로부터 응답을 생성하기 위한 입력값
- **Prompt engineering**: LLM이 생성하는 **결과물의 품질을 높일 수 있는 입력값들의 조합을 찾는 작업**
- LLM의 성능은 prompt의 퀄리티에 크게 좌우되며, 입력값이 조금만 달라져도 완전히 다른 결과물을 생성할 수 있음

</details>

**Q61.** Prompt의 구성 요소 4가지와 각 설명을 쓰시오. `[6장]`

<details markdown="1"><summary>정답 보기</summary>

- **Instruction**: 모델이 수행하기를 원하는 특정 task 혹은 지시 사항
- **Context**: 모델이 더 나은 답변을 하도록 유도하는 외부 정보 또는 추가 내용
- **Input Data**: 답을 구하고자 하는 것에 대한 질문
- **Output Indicator**: 결과물의 유형 또는 형식을 나타내는 요소

</details>

**Q62.** Few-shot Prompting의 한계와, 이를 보완하는 기법을 설명하시오. `[6장]`

<details markdown="1"><summary>정답 보기</summary>

한계: **몇 단계의 추가적인 추론 과정을 거쳐야 하는 복잡한 문제는 풀 수 없음**.
보완: **Chain-of-Thought Prompting** — 답변에 도달하는 과정을 학습시키기 위해, 본 질문 전에 **태스크와 추론 과정을 포함한 답변 예제를 제공**. LLM의 추론 능력을 향상시켜 **복잡한 산술, 상식, 기호 추론**에서 좋은 성능.

</details>

**Q63.** CoT의 효과를 PaLM 540B 수치로 쓰시오. `[6장]`

<details markdown="1"><summary>정답 보기</summary>

PaLM 540B의 수학 문제 정확도가 **단일 샷(CoT 없이) 17.7% → CoT 적용 후 58.1%** 로 대폭 상승. 산술·논리 추론(**MultiArith, GSM8K** 등)에서 두드러진 향상.

</details>

**Q64.** Prompt Engineering이 여전히 어려운 이유 4가지는? `[6장]`

<details markdown="1"><summary>정답 보기</summary>

① **표현과 서식에 대한 민감도** (서식만 바꿔도 최대 76%p 변화, 템플릿 따라 최대 40% 차이)
② **예시와 샘플 순서의 민감도** (모델 크기와 무관, 한 모델의 좋은 순열이 다른 모델엔 안 통함)
③ **재서술 문장 변화에 의한 성능 분산**
④ **모델 평가의 어려움**

</details>

**Q65.** 프롬프트 기반 모델 평가가 어려운 이유를 3가지 이상 쓰시오. `[6장]`

<details markdown="1"><summary>정답 보기</summary>

- **민감성 & 비일관성**: 작은 문장·단어 변화가 결과를 뒤바꿈
- **평가 기준 모호성**: 동일한 답변의 다양한 표현 해석 여부
- **과도한 프롬프트 의존성**: 단일 템플릿 비교 시 편향된 결과
- **비용·리소스 제한**: 수백 개 프롬프트 평가 부담
- **설계자 주관성**: 평가 기준이 사람마다 다름
- **프롬프트 결함 영향**: 입력 구조/형식 오류가 왜곡 유발
- **재현성 & 비교 가능성 낮음**: 동일 조건 재실험 어려움

</details>

---

### 7장 — AI Agent의 개념과 분류

**Q66.** Agent의 정의와, 정의하기 위해 필요한 두 요소는? `[7장]`

<details markdown="1"><summary>정답 보기</summary>

**특정 환경과 상호작용할 수 있는 지능적인 시스템**. 정의하려면 **지능(Intelligence)과 환경(Environment)** 을 정의해야 함. (환경: 물리적·디지털·인간 환경)

</details>

**Q67.** Agent, AI Agent, Agentic AI를 핵심 정의와 의사결정 방식으로 비교하시오. `[7장]`

<details markdown="1"><summary>정답 보기</summary>

| | 핵심 정의 | 의사결정 |
|---|---|---|
| **Agent** | 환경을 관찰하고 행동하는 지능적 시스템 전반 | 규칙·탐색·강화학습 정책 (**LLM 없이도 가능**) |
| **AI Agent** | **LLM으로 추론**하고 도구·메모리를 활용해 주어진 목표를 수행하는 소프트웨어 개체 | **LLM 추론 + ReAct 루프** (Thought→Action→Observation) |
| **Agentic AI** | 여러 에이전트·도구·메모리를 **조율**해 복잡한 목표를 자율 수행하는 시스템·설계 패러다임 | **Orchestrator가 계획·분배**하고 하위 에이전트 결과를 **통합·검증** |

목표·자율성: Agent는 설계자가 정한 범위 안에서 반응 / AI Agent는 사용자 목표를 task 단위로 수행 / Agentic AI는 상위 목표를 스스로 하위 목표로 분해하고 실패 시 재계획

</details>

**Q68.** AI Agent의 정의를 3가지 요소로 쓰시오. `[7장]`

<details markdown="1"><summary>정답 보기</summary>

인간이 설정한 목표를 달성하기 위해 ① **LLM으로 추론을 실행**하고 ② **외부 도구(API, database)를 연동해 작업을 자동화**하며 ③ **실시간 환경 변화에 따라 실행 계획을 동적으로 조정**하는 **자율적 지능 시스템**.

</details>

**Q69.** Models와 AI Agents를 지식 범위, 추론 방식, 도구 구현, 논리 계층 측면에서 비교하시오. `[7장]`

<details markdown="1"><summary>정답 보기</summary>

- **지식 범위**: 모델은 **학습 데이터에 포함된 지식으로 제한** / 에이전트는 **도구로 외부 시스템과 연결되어 지식 확장**
- **추론 방식**: 모델은 **단일 추론/예측**, 별도 구현 없이 연속적 맥락 관리 불가 / 에이전트는 **오케스트레이션 레이어에서 세션 기록을 관리하여 Multi-turn 추론**
- **도구 구현**: 모델 **X** / 에이전트는 **아키텍처 내에 도구가 기본 탑재**
- **논리 계층**: 모델은 **기본 로직 레이어 없음**, 사용자가 직접 복잡한 프롬프트 구성 / 에이전트는 **CoT, ReAct, LangChain 같은 프레임워크를 사용하는 네이티브 Cognitive architecture 보유**

</details>

**Q70.** Text Agent, LLM Agent, Reasoning Agent의 관계와 각각의 정의를 쓰시오. `[7장]`

<details markdown="1"><summary>정답 보기</summary>

관계: **Text Agent ⊃ LLM Agent ⊃ Reasoning Agent**
- **Text Agent**: 환경과 상호작용할 때 **관찰된 텍스트와 행동이 모두 언어로** 이루어지는 경우 (LLM 없는 것도 초창기부터 존재, 예: ELIZA)
- **LLM Agent**: 텍스트 에이전트이면서 **LLM을 사용하여 행동**하는 에이전트
- **Reasoning Agent**: **LLM을 기반으로 다양한 추론을 수행하여 행동**하는 에이전트

</details>

**Q71.** 룰 기반 에이전트(예: ELIZA)의 한계 2가지는? `[7장]`

<details markdown="1"><summary>정답 보기</summary>

① **규칙 설계가 매우 task-specific이며, 새로운 도메인마다 새로운 규칙 개발이 필요**
② **규칙 기반은 단순한 도메인을 넘어서면 작동하지 않음**

</details>

**Q72.** LLM Agent와 Reasoning Agent의 차이를 쓰시오. `[7장]`

<details markdown="1"><summary>정답 보기</summary>

- **LLM Agent**: **프롬프트 엔지니어링의 중요성 증대** (사람이 지시를 잘 구성해야 함)
- **Reasoning Agent**: **목표만 주어지면 알아서 단계별로 생각하고 검증하는 능력 탑재 (인지적 제어 수행)**. "생각(추론)하고, 계획을 세우며, 스스로 오류를 검증"한 후 행동
- Reasoning task와 acting task를 반복 수행하는 **ReAct**를 통해 Reasoning Agent로 확장

</details>

**Q73.** Reasoning Agent 이후 연구가 발전한 두 방향은? `[7장]`

<details markdown="1"><summary>정답 보기</summary>

① **응용 분야 확장**: 웹 상호작용, 엔지니어링, 과학적 발견 등
② **새로운 방법론 탐색**: memory, learning, planning, multi-agent 등

</details>

**Q74.** LLM이 AI Agent에 적합한 이유 4가지(성질)를 쓰고 각각 설명하시오. `[7장]`

<details markdown="1"><summary>정답 보기</summary>

- **자율성(Autonomy)**: 에이전트가 자신의 행동/내부 상태에 대한 통제권 보유 → LLM은 **상세한 단계별 지침 없이도** 인간과 유사한 텍스트를 생성하고 다양한 작업 수행
- **반응성(Reactivity)**: 환경 변화에 신속하게 대응 → **Multi-modal fusion으로 지각 공간 확장**, **Embodiment·Tool 사용으로 행동 공간 확장**
- **능동성(Pro-activeness)**: 주도적으로 목표 지향적 행동 수행 → **next token prediction** 패러다임으로 **일반화된 추론·계획 능력**
- **사회성(Social ability)**: agent-communication language로 다른 에이전트와 상호작용 → **NLU, NLG**로 모델·인간이 해석 가능한 방식으로 상호작용

</details>

---

### 8장 — ReAct와 Tool Use

**Q75.** ReAct를 설명하고 시너지 효과를 쓰시오. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

**ReAct = Reasoning + Acting**. 기존에는 모델이 추론만 하거나 행동만 생성했지만, ReAct는 **두 가지를 모두 생성**한다.
시너지: **추론은 행동을 돕고, 행동은 추론을 돕는다.** 다양한 QA 작업에 사용 가능하며 **다른 예시와 도구만 제공하면** 된다. (장점: Synergy, Simple and intuitive, General across domains)

</details>

**Q76.** Agent의 task 수행을 위한 필요 요건 3가지와 각 해결 방법을 쓰시오. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

- **Reasoning**: 복잡한 질문 해결을 위해 추론 필요 → **Instructions, Few-shot, Context, CoT, 과제 분해(ToT, GoT)**
- **Knowledge**: 훈련 시점 이후 정보에 대해 새로운 지식 필요 → **RAG**
- **Computation**: 매우 수학적이고 어려운 질문은 **트랜스포머의 auto-regression을 넘어서는 계산 방식** 필요 → **Tool Use**

</details>

**Q77.** Reasoning을 돕는 방법 5가지를 쓰시오. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

① 명확하고 충분한 설명을 포함하는 **Instructions** ② **Few-shot examples** ③ **Provide relevant context** ④ **Chain of thought (CoT)** ⑤ **Break down Complex tasks** (Tree-of-Thought, Graph-of-Thoughts)

</details>

**Q78.** 복잡한 과제를 subtask로 나누는 것이 왜 효과적인가? `[8장]`

<details markdown="1"><summary>정답 보기</summary>

Task를 더 간단한 subtask로 나누어 **각각을 다른 prompt에 넣고 이전 결과를 다음 prompt에 전달**하면, **각 subtask는 전체 task보다 간단하기에 error가 줄어든다.**

</details>

**Q79.** RAG의 동작 방식과 대표 Retriever를 쓰시오. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

**위키피디아와 같은 추가 코퍼스**가 존재하고, **Retriever(BM25, DPR 등)** 가 질문에 가장 관련 있는 정보를 코퍼스에서 끌어오며, **검색된 정보를 언어 모델의 컨텍스트에 추가**하여 답변을 쉽게 생성하도록 한다.
(플로우: 사용자 Prompt·Query → 지식 저장소에 Query → 증강된 컨텍스트 반환 → Prompt + Query + 증강 컨텍스트를 LLM에 → 생성된 응답 반환)

</details>

**Q80.** Tool Use의 정의와 예시 3가지를 쓰시오. `[8장]`

<details markdown="1"><summary>정답 보기</summary>

정의: **언어 생성의 자연스러운 형식에 특수 토큰을 도입하여 tool calls를 포함**시키는 것. Tool을 통해 언어모델을 다양한 지식, 정보, 계산 능력으로 **augment**할 수 있음.
예: **웹 검색(web-search), 날씨 API(get-weather), 코드 인터프리터(python-interpreter)** (또는 계산기, 위키피디아 검색)

</details>

**Q81.** Tool 생성 형식의 문제점은? `[8장]`

<details markdown="1"><summary>정답 보기</summary>

**Tool을 사용하기 위한 생성 형식은 인터넷에서 볼 수 있는 일반적인 텍스트와는 매우 다르다.** (LLM이 학습한 자연스러운 글과 형식이 달라 정확히 생성하기 어려움)

</details>

**Q82.** Agent와 API를 연동하는 Extension과 Function의 차이는? `[8장]`

<details markdown="1"><summary>정답 보기</summary>

- **Extension**: **Agent-Side Control** — 에이전트 쪽에서 직접 API를 호출
- **Function**: **Client-Side Control** — 에이전트는 호출할 함수와 인자만 알려주고 실제 API 호출은 클라이언트가 수행

</details>

---

### 9장 — LLM 기반 Agent의 구조

**Q83.** LLM-based Agent의 Workflow 3단계를 쓰고, 단순 LLM과의 차이점을 쓰시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

- **Perception**: 외부 환경의 변화를 감지하고, **multimodal 정보를 Agent가 이해할 수 있는 표현으로 변환**
- **Brain**: **기억/추론/연산/의사결정** 등의 정보 처리
- **Action**: Agent의 **결정을 수행**
- 차이점: 위 과정을 **반복하면서 지속적으로 피드백을 받고 환경과 상호작용**한다.

</details>

**Q84.** Brain Module의 Typology 5가지를 쓰시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

**Natural Language Interaction / Knowledge / Memory / Reasoning & Planning / Transferability & Generalization**

</details>

**Q85.** Agent의 Memory 정의와, Memory의 두 가지 challenge 및 해결 방안을 쓰시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

정의: **Agent의 과거 observations, thoughts, actions를 순차적으로 기록한 것**.
Challenge: ① **Memory 데이터의 양이 방대함** (Transformer 제약 초과 가능) ② **관련 Memory 추출의 어려움**
해결: ① **Memory Capability 개선** — Transformer 길이 제한 증가(Text truncation, Segmenting Inputs), **Memory 요약**, **벡터/데이터 구조를 사용한 메모리 압축**(임베딩, DB 연동) ② **Memory Retrieval** — **Recency / Relevance / Importance 기반 자동 검색**(높은 점수 우선), **사용자/시스템이 메모리를 interactive하게 편집**

</details>

**Q86.** Brain의 Reasoning 기법 4가지를 쓰시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

- **CoT**: 중간 추론 과정을 통해 최종 답변 생성
- **Self-consistency**: 여러 추론 경로 생성 → 일관된 답변 선택
- **Self-polish / Self-refine**: 출력 결과를 반복적으로 검토/수정
- **Selection-inference**: 여러 후보 추론 결과 중 가장 적절한 것을 선택

</details>

**Q87.** Plan formulation과 Plan reflection을 설명하시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

- **Plan formulation**: **전체 작업을 하위 작업으로 분해** (One-shot, Step-by-Step, Hierarchical planning)
- **Plan reflection**: **수립된 계획을 feedback** (내부적, 인간, 환경 피드백)

</details>

**Q88.** Transferability & Generalization의 세 가지 능력을 쓰시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

- **Unseen task Generalization**: Fine-tuning 없이 높은 zero-shot 성능
- **In-context learning**: Context 내 소수의 예시만으로 높은 학습 성능
- **Continual learning**: Forgetting 완화

</details>

**Q89.** Action Module의 행동 종류 3가지와 HuggingGPT의 동작 3단계를 쓰시오. `[9장]`

<details markdown="1"><summary>정답 보기</summary>

행동: **Textual Output / Tool Using** (Agent가 갖추기 어려운 능력 보완: API 호출, 이미지 생성) / **Embodied Action** (미래, 물리적 환경과 상호작용)
HuggingGPT: ① 사용자 요청을 바탕으로 **Task Planning** ② 각 task에 대해 **Hugging Face의 model card**를 바탕으로 **Model Selection** ③ 작업 수행 후 **응답 생성**

</details>

---

### 10장 — Agent의 실제 활용

**Q90.** AI Agent의 발전 방향성 3가지는? `[10장]`

<details markdown="1"><summary>정답 보기</summary>

① 사용자가 **반복적인 일상 업무에서 벗어나도록** 도움 → 작업 효율성 향상
② 사용자의 **명시적인 지침 없이**, 에이전트가 **독립적으로 문제를 분석/계획/해결**
③ 에이전트의 혁신적인 능력을 바탕으로 **최첨단 과학 분야에서 잠재력 발휘**

</details>

**Q91.** Single Agent 시나리오 3가지를 설명하시오. `[10장]`

<details markdown="1"><summary>정답 보기</summary>

- **Task-oriented deployment**: 사용자의 high-quality 자연어 지시를 받아 **계획 → 하위 Task 분해 → 실행 → 환경과의 상호작용(피드백)**
- **Innovation-oriented deployment**: 단순 반복 업무가 아닌 **지식 창출, 과학적 발견, 창의적 문제 해결**
- **(Future) Lifecycle-oriented deployment**: **장기적으로 살아남으며 스스로 능력을 확장하는 에이전트 → AGI의 최종 목표**

</details>

**Q92.** Multi-Agent의 사상적 동기가 된 저작과 그 핵심 주장은? `[10장]`

<details markdown="1"><summary>정답 보기</summary>

**Marvin Minsky, "The Society of Mind" (1986)**: "지능은 통일된 중앙처리장치에서 비롯되는 것이 아닌, **특정 기능을 가진 수많은 작은 에이전트들의 상호작용에 의해 발생**"

</details>

**Q93.** Multi-Agent 상호작용 방식별 장단점을 쓰시오. `[10장]`

<details markdown="1"><summary>정답 보기</summary>

- 자유로운 아이디어 생성 ↔ **통제의 어려움**
- 효율적이며 책임 소재가 명확 ↔ **역할에 대한 고정성**
- 서로의 주장을 반박하며 개선(게임이론) ↔ **잘못된 합의로의 수렴 가능성**

</details>

**Q94.** ChatDev와 ChatEval을 비교하시오. `[10장]`

<details markdown="1"><summary>정답 보기</summary>

- **ChatDev** (ACL 2024): **Ordered Cooperative Engagement**(협력형). 각 Agent의 역할을 분해하여 소프트웨어 개발, **Design → Coding → Testing 단계를 체인화**
- **ChatEval** (2023): **Adversarial Interactions**(적대형). 여러 Agent가 **서로 토론하며 생성된 응답의 품질을 평가**하는 **논쟁 기반 프레임워크**

</details>

**Q95.** Human-Agent Interaction의 두 패러다임을 설명하시오. `[10장]`

<details markdown="1"><summary>정답 보기</summary>

- **Instructor-Executor Paradigm**: **인간이 지시하고 에이전트가 수행** (**현재 에이전트의 기본 모드**). 인간이 지속적인 정량/정성 피드백 제공
- **Equal Partnership Paradigm**: 에이전트가 **사회적 주체로서 인간과 대칭 관계** 유지. **Empathetic Communicator**, **Human-level Participant**(공동 목표를 세우고 협력)

</details>

---

### 11장 — Cognitive Architecture와 CoALA

**Q96.** Cognitive Architecture가 필요해진 배경을 과거와 현재를 비교하여 쓰시오. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

LLM 기반 Agent는 점점 복잡한 일을 수행하도록 발전해 왔다. **과거 AI는 "Task를 잘 수행하기 위해 어떤 기능을 추가할 것인가"에 집중**했다면, **현재는 "AI가 다양한 Task를 잘 수행하기 위해 어떤 구조로 시스템을 설계해야 하는가"를 고민**하게 되었다. 따라서 Agent가 더욱 사람처럼 행동하도록 하기 위한 **체계적인 Architecture 설계, 즉 Cognitive Architecture가 필요**하다.

</details>

**Q97.** Cognitive Architecture의 정의는? `[11장]`

<details markdown="1"><summary>정답 보기</summary>

**인간이 정보를 인식하고, 기억하고, 추론하고, 행동을 결정하는 기본적인 구조**. 심리학, 인지과학 분야에서 인간의 인지 과정을 체계적으로 모델링하기 위해 도입 (Allen Newell, Herbert A. Simon).

</details>

**Q98.** CoALA의 풀네임과 3가지 구성요소 및 정의를 쓰시오. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

**Cognitive Architectures for Language Agents**
- **Memory Modules [기억]**: 에이전트가 **과거의 경험, 지식, 현재의 정보 등을 저장하고 유지하기 위한 정보 저장 시스템**
- **Action Space [행동]**: 에이전트가 **외부 환경과 상호작용하거나, 내부 상태를 조절하기 위해 수행할 수 있는 모든 가능한 동작들의 집합**
- **Decision making [의사결정]**: 에이전트가 주어진 목표를 달성하기 위해 **어떤 행동을 선택하고 실행할지 결정하는 과정**

</details>

**Q99.** CoALA의 메모리 4종류를 단기/장기로 구분하여 정의하시오. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

- **Short-term — Working Memory**: 현재 처리하고 있는 정보를 저장하는 공간
- **Long-term — Semantic**: 세상에 대한 일반적인 사실, 개념, 학습된 지식
- **Long-term — Episodic**: 과거에 경험했던 사건이나 상호작용
- **Long-term — Procedural**: 특정 작업을 수행하는 방법이나 규칙(스킬)

</details>

**Q100.** "친구 집에서 파스타를 만들자" 상황에서 다음 기억은 각각 어떤 메모리에 해당하는가?
(a) 파스타 = 면 + 소스 (b) 전에 물이 너무 적어서 면이 안 익었어 (c) 냄비에 물 붓고 가스불 켜고… (d) 장소: 친구 집 주방, 목표: 파스타 완성 `[11장]`

<details markdown="1"><summary>정답 보기</summary>

(a) **Semantic** (b) **Episodic** (c) **Procedural** (d) **Working**

</details>

**Q101.** CoALA의 Action Space를 외부 행동과 내부 행동으로 나누어 설명하시오. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

- **외부 행동 (External Actions; Grounding)**: API 호출, 인간 혹은 다른 에이전트와의 대화, 인터넷 검색 등
- **내부 행동 (Internal Actions; Memory Access)**
  - **검색 (Retrieval)**: 장기 기억에서 정보를 검색해 **Working Memory로 가져오는** 행동
  - **추론 (Reasoning)**: Working Memory의 내용을 처리하여 **새로운 정보를 생성**하는 행동
  - **학습 (Learning)**: 새로운 정보를 **Long-term memory에 저장**하는 행동 (예: Episodic memory에 일화 추가, LLM parameter update)

</details>

**Q102.** CoALA의 Decision-making Process를 단계별로 설명하시오. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

**Planning Stage**
- **Proposal**: LLM의 추론을 통해 **하나 이상의 Action 후보를 생성**
- **Evaluation**: 여러 Action 후보들의 **가치를 평가** (Heuristic, Simulation 등)
- **Selection**: 평가된 행동 중 **가장 좋은 Action을 선택**, 만족스러운 Action이 없으면 **다시 Proposal로** 돌아갈 수 있음

**Execution Stage**: 선택된 행동(내부 or 외부)을 **실행**하고, **환경으로부터 피드백**을 받아 다음 cycle로 이동

</details>

**Q103.** CoALA 프레임워크로 ReAct를 분석했을 때 드러나는 한계와, 이것이 보여주는 Cognitive Architecture의 필요성을 쓰시오. `[11장]`

<details markdown="1"><summary>정답 보기</summary>

ReAct는 **Long-term memory가 없고(✗)**, 내부 행동 중 reason만 하며 **learning·retrieval을 하지 않고(✗)**, 의사결정에서 propose만 하며 **evaluate·select를 하지 않는다(✗)**.
필요성: Cognitive Architecture를 통해 Agent가 더 인간처럼 복잡한 Task를 수행할 수 있고, **CoALA로 서로 다른 에이전트들이 기억·행동·의사결정을 어떻게 사용하는지 분석**할 수 있어 **에이전트 간 비교가 용이하며, 어떤 부분을 보완·발전시킬지 방향을 제시**할 수 있다.

</details>

---

### 12장 — AI Agent 아키텍처 분류

**Q104.** "AI Agent is sort of a control system"의 의미를 설명하시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

AI Agent의 목표는 **단일 LLM의 추론 능력에 의존하는 것이 아니라, 신뢰 가능한 구조를 설계하고 인간처럼 과업을 수행**하는 것이다. 문제 해결의 자율적 수행을 위해 **feedback loop를 포함한 재귀적인 구조의 Cognitive Architecture**(Observation → Planning & Reasoning → Action → Observation, Reflection)가 필요하며, 이를 기반으로 **performance/robustness/reliability/security** 개선을 위해 시스템의 **structure/process/interface**를 구성한다.

</details>

**Q105.** AI Agent 아키텍처의 (거의) 필수 구성요소를 Components와 Process로 나누어 쓰시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

- **Components: LLM, tool, database**
- **Process: reasoning, planning, tool calling**

</details>

**Q106.** Single Agent와 Multi-Agent Architecture를 비교하고 각각의 예를 쓰시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

- **Single**: **단일 언어모델이 모든 권한을 갖고 reasoning, planning, tool calling을 실행**. **타 모델 피드백은 받을 수 없으나 인간 개입 가능**. **문제가 잘 정의되어 있다면 더 나을 수 있음**. 예: **ReAct, RAISE, Reflexion, AutoGPT+P, LATS**
- **Multi**: **복수의 언어모델이 서로 다른 페르소나, 권한, 역할을 부여받고 소통·지시하며 협력**. **불필요한 행동, 정보 누락** 등 발생 가능. **복잡하고 모호한 과업에 더 적합**. vertical/horizontal로 분류. 예: **DyLAN, AgentVerse, MetaGPT**

</details>

**Q107.** Single Agent Architecture의 한계 2가지와, 이를 보여주는 RAISE의 사례를 쓰시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

한계: ① **너무 많은 tool ⇒ 적절한 tool 선택의 난이도 상승** ② **많은 subtask ⇒ 정보 혼재로 인한 성능 하락, workflow 생성/관리가 어려움**
RAISE: **ReAct에 short/long memory mechanism을 추가**해 특정 task에서 높은 성능을 보였으나, **복잡한 logic 이해를 어려워하고 할루시네이션이 발생** (세일즈를 시켰더니 Python 코드 작성 — 복잡한 과업 하에서 **부여된 역할을 헷갈리기 때문**으로 추측)

</details>

**Q108.** Vertical Architecture와 Horizontal Architecture를 비교하시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

- **Vertical**: **하나의 리더 agent에게 다른 모든 agent들이 보고**. **각 부하는 리더와만 소통**. **분업이 매우 명확**. 리더와의 소통이 모두에게 공유되도록 설계 가능. (CrewAI, ChatDev, MetaGPT)
- **Horizontal**: **모든 agent가 평등**, **집단적 논의**로 문제 해결. **공용 스레드에서 모든 소통**, 모든 메시지 확인 가능. 리더로부터 과업을 받는 게 아니라 **특정 task나 tool calling에 agent가 자원**. (DyLAN, AgentVerse, CAMEL)

</details>

**Q109.** MetaGPT의 특징을 쓰고, 왜 Vertical에 가까운지 쓰시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

- Agent끼리의 **무의미한 잡담(conversational noise)을 방지하기 위해 structured output을 강제**
- 정보 공유에 **"publish-subscribe" mechanism** 도입: 한 공간에 모든 정보를 공유하되 **각 agent의 목표·과업에 관련된 정보만 읽도록** 유도 (structured message의 메타 정보와 agent 정보를 매칭 = subscription)
- **수직적 업무 구조와 분업, 정보 흐름을 강제**하므로 vertical에 가까움

</details>

**Q110.** DyLAN의 동작 방식을 쓰고, 왜 Horizontal에 가까운지 쓰시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

- **공용 스레드에서 함께 과업 수행 후, round마다 각 agent의 기여도를 평가**하여 **기여도가 높은 agent만 다음 round 진출**
- **모든 모델이 각 1개의 메시지를 생성하는 것이 하나의 round**
- 기여도 평가는 **별도의 LLM Ranker 또는 agent끼리의 peer rating**
- 이를 반복하며 **팀 구성을 최적화**
- **리더 없이 수평적으로 협력한 후 성과 기반으로 멤버 재편**이 이루어지므로 horizontal에 매우 가까움

</details>

**Q111.** Agentic AI 시스템 방법론의 현재 연구 상황을 쓰시오. `[12장]`

<details markdown="1"><summary>정답 보기</summary>

Agentic AI System의 방법론은 **아직 표준화된 설계 정답이 없고**, 성능/안정성 개선을 위한 지식이 **상당히 empirical(경험적)하게 축적**되고 있다. 반면 Cognitive Architecture 개념이나 필수 구성요소의 피상적인 논리와 필요성 자체는 **매우 직관적**이다.

</details>
