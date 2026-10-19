# 핵심 암기 치트시트

시험 직전 30분용. **숫자, 이름, 분류, 비교표**만 모았습니다.

## 전체 흐름 한 줄

> **글자를 숫자로(임베딩) → 그 숫자로 다음 단어 예측(LLM) → 말 잘 듣게 조정(Adaptation Tuning) → 질문 잘하기(Prompt) → 손발·기억·계획 붙이기(Agent) → 구조화(Cognitive Architecture) → 여럿으로(Multi-Agent)**

---

## 숫자로 외우는 것

| 항목 | 값 |
|---|---|
| 코사인 유사도 범위 | **−1 ~ 1** (1에 가까울수록 유사) |
| 임베딩 논문 | **2003년, "A Neural Probabilistic Language Model"** |
| AutoEncoder 논문 | **1986년, "Learning Internal Representation by Error Backpropagation"** |
| Seq2Seq | **Google, 2014** |
| Transformer | **"Attention Is All You Need", 2017** |
| GPT-1 | **2018, 117M** |
| GPT-2 | **2019, 1.5B** (GPT-1의 **10배**) |
| GPT-3 | **2020, 175B (1,750억)** |
| ChatGPT | **2022년 11월, OpenAI** |
| FLAN | **2021** |
| GPT-3 학습 비용 | 약 **50억**, Tesla V100 1대로 **355년** |
| CoT 효과 (PaLM 540B) | 수학 문제 정확도 **17.7% → 58.1%** |
| 프롬프트 서식 변경 영향 | 성능 최대 **76%p** 변화 |
| 프롬프트 템플릿 영향 (GPT-3.5-turbo) | 코드 번역 과제에서 최대 **40%** 차이 |
| Adapter 예시 | d=1024, m=16 → 1,048,576개 → **32,768개** |
| LoRA 예시 | d=1024, m=8 → **16,384개** |
| 양자화 | **FP16 → INT8 → INT4** |
| ELIZA | **MIT 인공지능 연구소**, 룰 기반 챗봇 |
| The Society of Mind | **Marvin Minsky, 1986** |
| Cognitive Architecture 인물 | **Allen Newell, Herbert A. Simon** |

---

## 2장 — 임베딩

**임베딩의 역할 2가지**: ① 자연어의 의미적인 정보 함축 ② 자연어 간 유사도 계산

**One-hot의 한계 2가지**: ① **희소 문제(Sparsity problem)** ② **단어의 유사도를 표현할 수 없음**

**TF-IDF 공식**

```
tf(d,t) = (d에서 t의 등장 횟수) / (d의 전체 단어 빈도)
idf(d,t) = log( n / (1 + df(t)) )
TF-IDF = tf × idf
```

**log를 쓰는 이유 2가지**: ① 가중치를 적절히 조절 ② 분모가 0이 되는 경우 방지

**Sparse vs Dense**

| | Sparse | Dense |
|---|---|---|
| 차원 | 단어 사전 크기 | 사용자가 정한 고정값 |
| 값 | 0/1, 0/가중치 | 연속 실수 |
| 의미 정보 | 없음 | 있음 |
| 공간 복잡도 | 단어 늘면 증가 | 일정 |

**AutoEncoder**: 입력 X / **Latent vector Z** / 출력 X̃ 의 **3계층**, **비지도 학습**

**차원 축소 기법**: **t-SNE, PCA**

---

## 언어 모델 발전 4단계 (SLM → NLM → PLM → LLM)

| | **SLM** | **NLM** | **PLM** | **LLM** |
|---|---|---|---|---|
| 시기 | 1990s | 2010s | 2018+ | 2020+ |
| 핵심 | **N-gram, MLE** 확률 기반 | **신경망 + 단어 임베딩** | **대규모 비지도 사전학습 + 파인튜닝** | **수십억~수천억 파라미터 + 인간 가치 정렬** |
| 대표 | N-gram LM, Kneser-Ney | **word2vec, LSTM, Seq2Seq** | **BERT, GPT-2, T5** | **GPT-4, PaLM 2, LLaMA 3** |
| 한계/특징 | 데이터 의존, 맥락 이해 한계, 긴 문장 어려움 | 분산 표현, 문맥 개선, **기울기 소실** | 범용 언어 이해, 전이 가능 | 복잡한 추론, **안전성·정렬 중요성 확대** |

**핵심 전환**: **대규모 사전학습 + 다운스트림 파인튜닝이 표준 패러다임이 되었다**

**NLP 패러다임 쌓임**: 언어모델(LM) → **트랜스포머**(인코더/디코더/어텐션) → **대규모 언어모델**(BERT=인코더, GPT=디코더) → **초거대 AI**

**PLM vs LLM의 결정적 차이** = **Emergent Abilities**

---

## 3장 — Transformer

**RNN/Seq2Seq의 한계 3가지** (= Transformer가 해결한 것)

1. **고정 크기 벡터에 모든 정보 압축 → 정보 손실**
2. **Vanishing Gradient Problem**
3. **순차적 처리 → 병렬화 불가능**

**Seq2Seq 구성**: Encoder → **Context Vector** → Decoder (`<sos>` ~ `<eos>`)

**Transformer 입력** = **Embedding + Positional Encoding**

**Attention 3종류**

| 이름 | 위치 |
|---|---|
| Encoder Self-Attention | 인코더 |
| **Masked** Decoder Self-Attention | 디코더 (미래 단어 가림) |
| Encoder-Decoder Attention | 디코더가 인코더 출력 참조 |

---

## 4장 — LLM / GPT

**LLM 정의**: 방대한 텍스트 데이터로 학습된 **수천 억 개 파라미터**를 가진 **Transformer 기반** Language Model

**Emergent Abilities 3가지**: **In-context Learning / Instruction Following / Step-by-Step Reasoning**

**GPT 정리표**

| | GPT-1 | GPT-2 | GPT-3 |
|---|---|---|---|
| 연도 | 2018 | 2019 | 2020 |
| 파라미터 | 117M | 1.5B | 175B |
| Objective | `P(Out\|In)` | `P(Out\|In, Task)` | 프롬프트만으로 |
| 훈련 | Pre-train + SFT | Pre-train만 (SFT 제거) | In-context learning |
| 혁신 | Transformer LM | **멀티태스킹** | **지능적 프롬프트 이해** |

**Fine-tuning의 한계 3가지**: ① Task별 Labeled Dataset 필요 ② 과적합 → 분포 밖 일반화 성능 상실 ③ 적은 샘플로 수행하는 능력 필요

**Zero / One / Few-shot**: 예시 **0개 / 1개 / 몇 개**

**GPT-3 한계 3가지**: ① 긴 문장 일관성 상실·반복 ② **단방향성** → 자연어 추론 약함 ③ 토큰에 동일 가중치 → 목표 지향적 예측 결여

---

## 5장 — Adaptation Tuning

**LLM 학습 3단계**: **Pre-training → Adaptation Tuning → Utilization**

**Adaptation Tuning 3가지**: **Instruction Tuning → Alignment Tuning → Parameter Efficient Model Adaptation**

**Instruction Tuning 등장 배경 2가지**: ① **사용자의 의도에 맞는 답변 출력** (Users intent ≠ Language modeling) ② **Zero-shot 성능 향상**

**FLAN 결론 3가지**: ① zero-shot 향상 기법 최초 제안 ② **task cluster 수가 많을수록** unseen task 성능 향상 ③ **모델이 작으면 오히려 성능 하락**

**Alignment 기준 3H**: **Helpfulness / Honesty / Harmlessness**

**RLHF 3단계**

| Step | 이름 | 내용 |
|---|---|---|
| 1 | **Supervised Fine-tuning** | 인간이 작성한 prompt 데이터로 LM fine-tuning |
| 2 | **Reward Model Training** | 여러 답변에 인간이 **선호도 순위(Ranking)** → reward model 학습 |
| 3 | **RL Fine-tuning** | reward model을 보상 함수로 **PPO**로 정책 fine-tuning |

**RLHF 요소 3가지**: Human annotator / Reward model / Aligned model

**RLHF 한계**: 비용 많이 듦, 주관적 요인에 따른 **품질 편차**

**PEFT 근거**: PLM은 **low intrinsic dimension** → RoBERTa는 **200개 파라미터로 90% 성능**

**LoRA**: `W0 + ΔW = W0 + A·B`, `A ∈ ℝ^(d×m)`, `B ∈ ℝ^(m×d)`

**LoRA가 Adapter보다 나은 이유 3가지**: ① 더 적은 파라미터로 fast adaptation ② **병렬 처리 → 추론 지연 없음** ③ 입력 시퀀스 길이를 줄이지 않음

**한 문장 정리**: **PEFT는 학습할 파라미터를 줄이고, Quantization은 메모리를 줄인다. 둘을 결합한 것이 QLoRA.**

---

## 6장 — Prompt Engineering

**Prompt 구성요소 4가지**: **Instruction / Context / Input Data / Output Indicator**

**Prompting 기법**: Zero-shot → One/Few-shot → **CoT**

**Few-shot의 한계**: **여러 단계의 추론이 필요한 복잡한 문제는 풀 수 없음** → CoT 등장

**Prompt Engineering이 어려운 이유 4가지**

1. **표현과 서식에 대한 민감도**
2. **예시와 샘플 순서의 민감도**
3. **재서술 문장 변화에 의한 성능 분산**
4. **모델 평가의 어려움**

---

## 7장 — AI Agent 개념

**Agent 정의**: **특정 환경과 상호작용할 수 있는 지능적인 시스템** (정의에 **지능 + 환경** 필요)

**Agent / AI Agent / Agentic AI**

| | 한 줄 | 의사결정 |
|---|---|---|
| Agent | 환경을 관찰·행동하는 개념 | 규칙·탐색·강화학습 (LLM 없이도 가능) |
| AI Agent | LLM을 두뇌로 쓰는 개체 | **LLM 추론 + ReAct 루프** |
| Agentic AI | 여러 에이전트를 조율하는 시스템 | **Orchestrator가 계획·분배·통합·검증** |

**AI Agent 정의 3요소**: ① LLM으로 추론 ② 외부 도구(API, DB) 연동해 자동화 ③ **실시간 환경 변화에 따라 실행 계획을 동적으로 조정**

**Models vs Agents**: 지식 범위 / 추론 방식 / 도구 구현 / 논리 계층

**Agent 분류 (포함관계)**: **Text Agent ⊃ LLM Agent ⊃ Reasoning Agent**

**LLM Agent vs Reasoning Agent**: 전자는 **프롬프트 엔지니어링 중요**, 후자는 **목표만 주면 알아서 단계별로 생각·검증(인지적 제어)**

**LLM이 Agent에 적합한 이유 4가지**

| 성질 | 근거 |
|---|---|
| **자율성 (Autonomy)** | 상세 지침 없이도 작업 수행 |
| **반응성 (Reactivity)** | Multi-modal fusion → **지각 공간** 확장 / Embodiment·Tool → **행동 공간** 확장 |
| **능동성 (Pro-activeness)** | next token prediction → 추론·계획 능력 |
| **사회성 (Social ability)** | NLU·NLG로 상호작용 |

---

## 8장 — ReAct / Tool

**ReAct = Reasoning + Acting**, **시너지: 추론은 행동을 돕고, 행동은 추론을 도움**

**Agent task 수행 필요요건 3가지**

| 요건 | 해결책 |
|---|---|
| **Reasoning** | 프롬프트 기법 (Instructions, Few-shot, Context, CoT, 과제 분해) |
| **Knowledge** | **RAG** (Retriever: **BM25, DPR**) |
| **Computation** | **Tool Use** |

**과제 분해 확장**: **Tree-of-Thought, Graph-of-Thoughts**

**Tool 예시 3가지**: Web-search / Get-weather / Python-interpreter

**Tool 생성 형식의 문제점**: **인터넷의 일반적인 텍스트와 형식이 매우 다름**

**Extension vs Function**: **Extension = Agent-Side Control**, **Function = Client-Side Control**

---

## 9장 — Agent 구조

**Perception → Brain → Action** (단순 LLM과의 차이: **반복하며 피드백·상호작용**)

**Brain의 5가지**: ① Natural Language Interaction ② Knowledge ③ Memory ④ Reasoning & Planning ⑤ Transferability & Generation

**Memory challenge 2가지**: ① 데이터 양이 방대 (Transformer 제약 초과) ② 관련 Memory 추출의 어려움

**Memory Retrieval 기준 3가지**: **Recency / Relevance / Importance**

**Reasoning 기법**: CoT, Self-consistency, Self-polish/Self-refine, Selection-inference

**Planning 2단계**: **Plan formulation**(하위 작업 분해: One-shot / Step-by-Step / Hierarchical) + **Plan reflection**(내부·인간·환경 피드백)

**Transferability 3가지**: Unseen task Generalization / In-context learning / Continual learning

**HuggingGPT 3단계**: Task Planning → **Model Selection (model card 기반)** → 응답 생성

---

## 10장 — 활용

**Single Agent 3가지**: **Task-oriented → Innovation-oriented → (Future) Lifecycle-oriented (AGI의 최종 목표)**

**Multi-Agent 장단점 쌍**

| 장점 | 단점 |
|---|---|
| 자유로운 아이디어 생성 | 통제의 어려움 |
| 효율적·책임 소재 명확 (분업) | 역할의 고정성 |
| 반박하며 개선 (게임이론) | **잘못된 합의로의 수렴 가능성** |

**사례**: **ChatDev = 협력형**(Design→Coding→Testing) / **ChatEval = 적대형**(Multi-Agent Debate 평가)

**Human-Agent 2가지**: **Instructor-Executor**(현재 기본 모드) / **Equal Partnership**(Empathetic Communicator, Human-level Participant)

---

## 11장 — CoALA

**CoALA 3요소**: **Memory Modules(기억) / Action Space(행동) / Decision-making Process(의사결정)**

**Memory 4종**

| 구분 | 종류 | 저장하는 것 |
|---|---|---|
| Short-term | **Working Memory** | 현재 처리 중인 정보 |
| Long-term | **Semantic** | 일반적 사실·개념·지식 |
| Long-term | **Episodic** | 과거 경험한 사건·상호작용 |
| Long-term | **Procedural** | 작업 수행 방법·규칙(스킬) |

**Action Space**

- **External Actions (Grounding)**: API 호출, 대화, 인터넷 검색
- **Internal Actions (Memory Access)**: **Retrieval**(장기→Working) / **Reasoning**(Working 내 가공) / **Learning**(→장기 저장)

**Decision-making**: **Planning Stage (Proposal → Evaluation → Selection)** + **Execution Stage** (만족스러운 Action 없으면 Proposal로 복귀)

**CoALA로 본 ReAct의 빈칸**: **Long-term memory ✗ / learning·retrieval ✗ / evaluate·select ✗**

---

## 12장 — 아키텍처

**필수 구성요소**: Components = **LLM, tool, database** / Process = **reasoning, planning, tool calling**

**Agent as control system**: **Observation → Planning & Reasoning → Action → Observation** (+ Reflection), 개선 목표는 **performance / robustness / reliability / security**

**Single Agent 한계 2가지**: ① **tool이 너무 많으면 선택 난이도 상승** ② **subtask가 많으면 정보 혼재로 성능 하락, workflow 관리 어려움**

**RAISE**: ReAct + short/long memory → 그러나 **복잡한 logic 이해 어려움, 할루시네이션**(세일즈 시켰더니 Python 코드 작성)

**Vertical vs Horizontal**

| Vertical | Horizontal |
|---|---|
| 리더 1명에게 전원 보고 | 전원 평등, 집단 논의 |
| 부하는 **리더와만** 소통 | **공용 스레드**에서 전원 소통 |
| 분업이 매우 명확 | task·tool calling에 **자원** 가능 |
| CrewAI, ChatDev, **MetaGPT** | **DyLAN**, AgentVerse, CAMEL |

**MetaGPT**: **structured output 강제**(conversational noise 방지) + **publish-subscribe** 메커니즘

**DyLAN**: **round**마다 기여도 평가(**LLM Ranker 또는 peer rating**) → 높은 agent만 다음 round 진출 → **팀 구성 최적화**
