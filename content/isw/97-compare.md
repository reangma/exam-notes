# 헷갈리는 개념 총정리

시험에서 **틀리는 이유의 대부분은 "비슷한 두 개를 바꿔 쓰는 것"** 입니다. 이 페이지는 짝으로 헷갈리는 개념을 한곳에 모으고, **한 단어로 구분하는 요령**과 **오답 보기로 나올 함정**을 같이 적었습니다.

{: .참고 }
> 읽는 법: 표의 **"한 단어로 구분"** 열만 외워도 대부분의 비교 문제가 풀립니다. 자세한 설명은 오른쪽 장 번호로 돌아가세요.

---

## 1. 연도·이름 한 줄로 보기

<figure class="fig" id="fig-timeline"><svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="연도별 흐름" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-timeline-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-timeline-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-timeline-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-timeline-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <path d="M15 135H745" stroke="#1E3A6E" stroke-width="3"/> <g fill="#C77E16"><circle cx="40" cy="135" r="6"/><circle cx="105" cy="135" r="6"/><circle cx="170" cy="135" r="6"/><circle cx="235" cy="135" r="6"/><circle cx="300" cy="135" r="6"/><circle cx="365" cy="135" r="6"/><circle cx="430" cy="135" r="6"/><circle cx="495" cy="135" r="6"/><circle cx="560" cy="135" r="6"/><circle cx="625" cy="135" r="6"/><circle cx="700" cy="135" r="6"/></g> <g stroke="#CBD9EE" stroke-width="1.5"><path d="M40 129V106"/><path d="M170 129V106"/><path d="M300 129V106"/><path d="M430 129V106"/><path d="M560 129V106"/><path d="M700 129V106"/><path d="M105 141V164"/><path d="M235 141V164"/><path d="M365 141V164"/><path d="M495 141V164"/><path d="M625 141V164"/></g> <g font-size="13" fill="#C77E16"><text x="14" y="52" text-anchor="start">1986</text><text x="170" y="52">2014</text><text x="300" y="52">2018</text><text x="430" y="52">2020</text><text x="560" y="52">2022</text><text x="700" y="52">2024</text><text x="105" y="186">2003</text><text x="235" y="186">2017</text><text x="365" y="186">2019</text><text x="495" y="186">2021</text><text x="625" y="186">2023</text></g> <g font-size="11.5"> <text x="14" y="72" text-anchor="start">Society of Mind</text><text x="14" y="90" text-anchor="start">AutoEncoder</text> <text x="170" y="72">Seq2Seq</text><text x="170" y="90">(Google)</text> <text x="300" y="72">GPT-1 · BERT</text><text x="300" y="90">PLM 시대</text> <text x="430" y="72">GPT-3</text><text x="430" y="90">In-context</text> <text x="560" y="72">ChatGPT (11월)</text><text x="560" y="90">ReAct</text> <text x="700" y="72">CoALA · DyLAN</text><text x="700" y="90">ChatDev(ACL)</text> <text x="105" y="206">임베딩 등장</text><text x="105" y="224">(신경망 LM 논문)</text> <text x="235" y="206">Transformer</text><text x="235" y="224">"Attention Is All…"</text> <text x="365" y="206">GPT-2</text><text x="365" y="224">멀티태스크</text> <text x="495" y="206">FLAN</text><text x="495" y="224">Instruction Tuning</text> <text x="625" y="206">HuggingGPT</text><text x="625" y="224">MetaGPT · ChatEval</text> </g> </svg><figcaption>시험에 나오는 이름과 연도를 한 줄로 (위·아래 번갈아 배치)</figcaption></figure>

{: .시험 }
> **연도로 묻기 쉬운 것**: 임베딩 **2003** / Seq2Seq **2014 (Google)** / Transformer **2017** / GPT-1 **2018** / GPT-2 **2019** / GPT-3 **2020** / FLAN **2021** / ChatGPT **2022년 11월** / AutoEncoder·Society of Mind **1986**

---

## 2. 임베딩·모델 구조 (2~3장)

| 헷갈리는 짝 | 한 단어로 구분 | 자세히 | 장 |
|---|---|---|---|
| **One-hot** vs **TF-IDF** | **0/1** vs **중요도 점수** | 둘 다 차원 = 어휘 크기, 둘 다 희소. TF-IDF는 중요도를 반영하지만 문맥·동의어·다의어는 여전히 모름 | 2 |
| **Sparse** vs **Dense** | **대부분 0** vs **전부 의미 있는 실수** | Sparse는 차원이 사전 크기만큼 커지고 유사도 표현 불가. Dense는 사용자가 정한 작은 차원, 공간 일정, **일반화** 가능 | 2 |
| **TF** vs **IDF** | **이 문서에서 자주?** vs **다른 문서엔 드묾?** | IDF는 `df(t)`에 **반비례** | 2 |
| **log를 쓰는 이유** 2가지 | **가중치 조절** + **분모 0 방지** | 분모 0 방지는 엄밀히는 `1 + df(t)` 덕분 | 2 |
| **임베딩의 역할** 2가지 | **의미 함축** + **유사도 계산** | | 2 |
| **AutoEncoder** | **비지도**, **3계층** | 입력 X → Latent vector Z → 출력 X̃ | 2 |
| **RNN의 한계** vs **Seq2Seq/RNN의 한계 3가지** | **입출력 길이 고정** vs **정보손실·기울기소실·병렬화불가** | 앞의 것은 Seq2Seq가, 뒤의 3가지는 Transformer가 해결 | 3 |
| **Encoder** vs **Decoder** | **압축** vs **한 단어씩 출력** | 그 사이가 Context vector (고정 크기 1개) | 3 |
| **Encoder Self-Attn** vs **Masked Self-Attn** vs **Enc-Dec Attn** | **입력끼리** / **출력끼리(미래 가림)** / **디코더가 인코더를** | 앞 2개는 같은 문장 안, 마지막은 두 문장 사이 | 3 |
| **BERT** vs **GPT** | **인코더·양방향·이해** vs **디코더·단방향·생성** | GPT-3가 자연어 추론에 약한 이유 = 단방향 | 3·4 |
| **SLM → NLM → PLM → LLM** | **통계 → 신경망 → 사전학습 → 거대** | 1990s / 2010s / 2018+ / 2020+ | 3 |
| **Pre-training** vs **Fine-tuning** | **정답 없는 대량 글, 일반 능력** vs **정답 있는 특정 데이터, 특정 과제** | 비지도 vs 지도 | 3·4 |

{: .중요 }
> **함정 주의**
>
> - "TF-IDF는 **문맥을 고려**한다" → ❌ (문맥 무시가 한계)
> - "One-hot은 **차원이 작아** 효율적이다" → ❌ (희소 문제)
> - "Transformer는 **RNN을 개선해서** 쓴다" → ❌ (**RNN을 쓰지 않고** Attention만 사용, 단 Encoder-Decoder 구조는 유지)
> - "Transformer는 embedding을 **그대로** 입력한다" → ❌ (**Positional Encoding**을 더함)
> - "AutoEncoder는 **지도학습**" → ❌ (**비지도**, label 없음)

---

## 3. LLM·GPT (4장)

| 헷갈리는 짝 | 한 단어로 구분 | 자세히 |
|---|---|---|
| **PLM** vs **LLM** | 차이 = **Emergent Abilities** | "크기가 크다"만 쓰면 부족. **기존 PLM과 구별되는 LLM의 가장 큰 특징** |
| **Fine-tuning** vs **In-context Learning** | **파라미터 바뀜** vs **안 바뀜** | ICL은 프롬프트 속 예시만 보고 수행, 별도 학습 없음 |
| **Zero / One / Few-shot** | 예시 **0 / 1 / 몇 개** | Few-shot = Task 설명 + Context Window k에 맞는 예제 |
| **GPT-1** vs **GPT-2** 목적함수 | P(Out \| In) vs P(Out \| In, Task) | GPT-2는 같은 입력이라도 과제에 따라 다른 출력 |
| **GPT-1 / 2 / 3 훈련 방식** | **사전학습+SFT / 사전학습만 / 프롬프트만** | 가르침이 점점 줄어듦 |
| **GPT-1 / 2 / 3 파라미터** | **117M / 1.5B / 175B** | 2018 / 2019 / 2020 |
| **GPT-1 / 2 / 3 혁신** | **BERT보다 먼저 / 멀티태스킹 / 지능적 프롬프트 이해** | |
| **Fine-tuning 한계** vs **GPT-3 한계** | **데이터 필요·과적합·사람처럼 적은 샘플** vs **긴 글 반복·단방향·토큰 동일 가중치** | 두 목록을 섞은 보기가 나오기 쉬움 |
| **추론 모델** vs **비추론 모델** | **속으로 CoT 후 답** vs **바로 확률 높은 단어** | 수학자 vs 퀴즈 달인 |

{: .중요 }
> **함정 주의**
>
> - "In-context Learning은 소량의 데이터로 **모델을 미세조정**한다" → ❌ (**업데이트 없음**)
> - "GPT-3는 **Fine-tuning을 통해** 성능을 높였다" → ❌ (**Fine-tuning 생략**)
> - "GPT는 Transformer **인코더** 기반" → ❌ (**디코더**)
> - "GPT-2는 GPT-1보다 **100배** 많은 파라미터" → ❌ (**10배**, 1.5B)

---

## 4. Adaptation Tuning (5장)

| 헷갈리는 짝 | 한 단어로 구분 | 자세히 |
|---|---|---|
| **Pre-training / Adaptation Tuning / Utilization** | **기본기 / 목적 맞추기 / 잘 쓰기** | Adaptation = Instruction·Alignment·PEFT, Utilization = Prompt Engineering |
| **Instruction Tuning** vs **Alignment Tuning** | **말 알아듣게** vs **인간 가치에 맞게** | Instruction = 지시문-정답 pair 지도학습 / Alignment = 3H 기준, RLHF |
| **Instruction Tuning 등장 배경 2가지** | **의도에 맞는 답변** + **zero-shot 향상** | Users intent ≠ Language modeling |
| **FLAN 결론** | **cluster 많을수록 ↑**, **작은 모델은 오히려 ↓** | instruction tuning 최초 제안 |
| **3H** | **Helpful · Honest · Harmless** | 도움 / 정직 / 무해 |
| **RLHF 1 / 2 / 3단계** | **모범답안 SFT / 순위로 채점기 / PPO 강화학습** | Reward model은 2단계에서 **학습**, 3단계에서는 **고정되어 채점만** |
| **Human annotator / Reward model / Aligned model** | **사람 심사위원 / 사람 취향 흉내 채점기 / 학습시키려는 모델** | |
| **Adapter** vs **LoRA** | **층을 덧붙임(순차)** vs **변화량을 두 행렬로(병렬)** | LoRA는 추론 지연 없음, 파라미터 더 적음, 시퀀스 길이 안 줄임 |
| **PEFT** vs **Quantization** | **학습할 파라미터 수 ↓** vs **비트 수(메모리) ↓** | 합치면 **QLoRA** |

{: .중요 }
> **함정 주의**
>
> - "RLHF 2단계에서 **사람이 점수를 매긴다**" → 순위(**Ranking**)를 매긴다가 정확
> - "PEFT는 **원래 모델 크기를 줄인다**" → ❌ (그래서 Quantization이 필요)
> - "Instruction Tuning은 **모든 크기의 모델**에서 효과가 있다" → ❌ (작은 모델은 오히려 하락, FLAN)
> - "RLHF는 **비용이 적게** 든다" → ❌ (annotator 비용 큼, 주관적 품질 편차)

---

## 5. Prompt Engineering (6장)

| 헷갈리는 짝 | 한 단어로 구분 | 자세히 |
|---|---|---|
| **Instruction** vs **Context** vs **Input Data** vs **Output Indicator** | **할 일 / 추가 정보 / 질문 대상 / 출력 형식** | 프롬프트 구성요소 4가지 |
| **Few-shot** vs **CoT** | 예시에 **결론만** vs **풀이 과정까지** | Few-shot의 한계(다단계 추론 불가)를 CoT가 보완 |
| **CoT** vs **Self-consistency** vs **Self-refine** vs **Selection-inference** | **단계별로 / 여러 번 풀어 다수결 / 스스로 고치기 / 후보 중 고르기** | 9장 Reasoning 기법 |
| **어려운 이유 4가지** | **서식 / 예시 순서 / 재서술 / 평가** | 76%p(서식), 40%(템플릿) |

---

## 6. AI Agent (7~8장)

| 헷갈리는 짝 | 한 단어로 구분 | 자세히 |
|---|---|---|
| **Agent** vs **AI Agent** vs **Agentic AI** | **관찰·행동 전부 / LLM 두뇌 한 명 / 여럿을 조율하는 시스템** | 의사결정: 규칙·탐색·RL / ReAct 루프 / Orchestrator |
| **Model** vs **Agent** | **학습 지식만·단일 추론·도구 X·로직 X** vs **도구로 확장·Multi-turn·도구 탑재·Cognitive architecture** | 4개 항목 |
| **Text ⊃ LLM ⊃ Reasoning Agent** | **언어로 / LLM으로 행동 / LLM으로 추론까지** | 포함 관계 |
| **LLM Agent** vs **Reasoning Agent** | **프롬프트 엔지니어링 중요** vs **알아서 생각·검증(인지적 제어)** | |
| **자율성 / 반응성 / 능동성 / 사회성** | **스스로 / 대응 / 주도 / 소통** | 반응성 = 지각(Multi-modal)·행동(Embodiment·Tool) 공간 확장 |
| **반응성** vs **능동성** | **바뀌면 대응(밖에서)** vs **목표가 있어 먼저(안에서)** | 가장 많이 헷갈리는 짝 |
| **Reasoning / Knowledge / Computation** | **프롬프트 기법 / RAG / Tool Use** | 필요 요건 ↔ 해결책 짝 |
| **BM25** vs **DPR** | **단어 겹침(sparse)** vs **의미 벡터(dense)** | 둘 다 RAG의 Retriever |
| **Extension** vs **Function** | **Agent-Side** vs **Client-Side** Control | 누가 실제로 API를 호출하나 |

{: .중요 }
> **함정 주의**
>
> - "Agent는 반드시 **LLM을 사용**한다" → ❌ (Agent는 규칙·탐색·강화학습으로도 가능, LLM을 쓰는 건 **AI Agent**)
> - "ELIZA는 **LLM 기반** 에이전트" → ❌ (**룰 기반** Text Agent)
> - "ReAct는 추론**만** 강화한 방법" → ❌ (추론 + 행동 **둘 다** 생성)
> - "Function은 **에이전트가 직접** API를 호출" → ❌ (그건 Extension)

---

## 7. 구조·아키텍처 (9~12장)

| 헷갈리는 짝 | 한 단어로 구분 | 자세히 |
|---|---|---|
| **Perception / Brain / Action** | **감지·변환 / 기억·추론·결정 / 수행** | 단순 LLM과의 차이 = **반복하며 피드백** |
| **Knowledge** vs **Memory** (9장 Brain) | **세상 일반 지식** vs **이 사용자에 대한 경험** | |
| **Memory challenge** 2개 vs **해결** 2개 | **양이 방대·추출 어려움** vs **용량 개선·검색 방안** | 검색 기준 = Recency·Relevance·Importance |
| **Plan formulation** vs **Plan reflection** | **분해해서 계획 짜기** vs **피드백으로 점검** | One-shot·Step-by-Step·Hierarchical / 내부·인간·환경 |
| **Unseen task Gen. / In-context / Continual** | **처음 보는 일 / 예시 몇 개 / 잊지 않기** | Transferability 3가지 |
| **Task / Innovation / Lifecycle** | **시킨 일 / 새 지식 / 스스로 성장(AGI)** | Single Agent 3단계 |
| **ChatDev** vs **ChatEval** | **협력(개발 체인)** vs **적대(토론 평가)** | |
| **Instructor-Executor** vs **Equal Partnership** | **상사-부하(현재)** vs **동료** | |
| **Working / Semantic / Episodic / Procedural** | **지금 / 사실 / 경험 / 방법** | 단기 1 + 장기 3 |
| **Retrieval / Reasoning / Learning** | **장기→작업 / 작업 안 가공 / →장기** | 내부 행동 3가지 (외부 행동 = Grounding) |
| **Proposal / Evaluation / Selection / Execution** | **후보 / 평가 / 선택 / 실행** | 불만족이면 Selection → Proposal |
| **Single** vs **Multi-Agent** | **잘 정의된 문제** vs **복잡·모호한 문제** | Single 한계: tool 많으면 선택 어려움, subtask 많으면 정보 혼재 |
| **Vertical** vs **Horizontal** | **리더에게 보고** vs **전원 평등·공용 스레드·자원** | |
| **MetaGPT** vs **DyLAN** | **structured output + publish-subscribe (수직)** vs **round별 기여도 평가로 재편 (수평)** | |

{: .중요 }
> **함정 주의**
>
> - "Episodic memory = **사실·개념**" → ❌ (그건 Semantic, Episodic = **경험**)
> - "Retrieval = 새 정보를 장기 기억에 **저장**" → ❌ (그건 Learning)
> - "ReAct는 **장기 기억**과 **evaluate·select**를 갖췄다" → ❌ (CoALA 분석: 셋 다 ✗)
> - "Horizontal에서는 **리더가 과업을 배정**" → ❌ (agent가 **자원**)
> - "MetaGPT는 Horizontal" → ❌ (**Vertical**에 가까움)

---

## 8. 키워드만 보면 답이 보인다 (객관식 대비)

보기나 문제에 **이 단어가 보이면 → 이 개념**입니다.

| 이 키워드가 보이면 | 답 |
|---|---|
| 희소 행렬, 19,999개가 0, 공간 복잡도 증가 | **One-hot의 희소 문제** |
| 모든 단어 간 거리 동일 | **One-hot의 유사도 표현 불가** |
| 문서-단어 행렬, 가중치, 검색 결과 중요도 | **TF-IDF** |
| 사용자가 설정한 차원, 연속적인 실수, 강아지≈멍멍이 | **Dense representation** |
| Latent vector, 라벨 없이, 3계층 | **AutoEncoder** |
| 아들 − 딸 + 소년 | **Word analogy test** (임베딩 성능 평가) |
| Context vector, 두 개의 LSTM, 가변 길이 | **Seq2Seq** |
| Attention Is All You Need, 병렬화 | **Transformer** |
| 다음 단어 예측, Autoregressive, 디코더 | **GPT** |
| P(Output \| Input, Task) | **GPT-2 (Task Conditioning)** |
| 1,750억, Few-shot Learners, 미세조정 생략 | **GPT-3** |
| 모델 업데이트 없음, 프롬프트의 맥락적 의미 | **In-context Learning** |
| 크기가 커지면 갑자기 생기는 능력 | **Emergent Abilities** |
| 지시문 + input + output pair, supervised | **Instruction Tuning** |
| task cluster, zero-shot learners, 2021 | **FLAN** |
| Helpfulness, Honesty, Harmlessness | **Alignment 기준 (3H)** |
| Human annotator, Reward model, PPO | **RLHF** |
| low intrinsic dimension, RoBERTa 200개 | **PEFT의 근거** |
| Down/Up Projection | **Adapter Tuning** |
| W0 + AB, rank, 추론 지연 없음 | **LoRA** |
| FP16 → INT8 → INT4 | **Quantization** |
| 4-bit freeze + LoRA | **QLoRA** |
| 중간 추론 과정, 17.7% → 58.1%, GSM8K | **Chain-of-Thought** |
| 76%p, 템플릿 40%, 예시 순서 | **Prompt Engineering의 어려움** |
| Orchestrator, 재계획, 하위 목표 분해 | **Agentic AI** |
| 통제권, 신속 대응, 목표 지향, agent-communication language | **자율성 / 반응성 / 능동성 / 사회성** |
| Thought → Action → Observation | **ReAct** |
| Retriever, BM25, DPR, 할루시네이션 방지 | **RAG** |
| 특수 토큰, tool calls, augment | **Tool Use** |
| Agent-Side / Client-Side Control | **Extension / Function** |
| Perception–Brain–Action | **LLM 기반 Agent 구조 (Xi et al., 2023)** |
| Recency / Relevance / Importance | **Memory Retrieval** |
| model card, Task Planning → Model Selection | **HuggingGPT** |
| 장기 생존, 스스로 능력 확장, AGI | **Lifecycle-oriented deployment** |
| 수많은 작은 에이전트의 상호작용, Minsky | **The Society of Mind** |
| Design → Coding → Testing | **ChatDev** |
| Multi-Agent Debate, 응답 품질 평가 | **ChatEval** |
| Memory · Action Space · Decision-making | **CoALA** |
| Proposal · Evaluation · Selection | **CoALA의 Planning Stage** |
| ReAct + short/long memory, 세일즈→Python | **RAISE** |
| structured output, publish-subscribe | **MetaGPT** |
| round, 기여도, LLM Ranker, peer rating | **DyLAN** |
