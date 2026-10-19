# 📖 쉬운 용어사전

시험에 나오는 단어를 **수학·전공 지식 0**이어도 알 수 있게 **비유와 함께** 풀었습니다. 본문을 읽다가 모르는 단어가 나오면 여기로 오세요.

{: .참고 }
> **찾는 법**: 상단 검색창에 단어를 치거나(`/` 키), 이 페이지에서 **Ctrl+F**. 한글·영어 아무거나 됩니다.
> 각 용어 아래 💡 줄은 **비유나 예시**입니다.

## 🧮 수학 기초 (몰라도 OK, 여기만 보면 됨)

**벡터** · Vector
: 숫자를 **쭉 늘어놓은 목록**. `[0.1, 0.5, 0.9]` 처럼.
: 💡 단어를 벡터로 바꾼다 = 단어를 숫자 목록으로 바꾼다

**차원** · Dimension
: 벡터 안에 **숫자가 몇 개** 들어 있는지. 숫자 300개면 300차원.

**코사인 유사도** · Cosine similarity
: 두 벡터(화살표)가 **얼마나 같은 방향**을 보는지. **−1~1**, 1에 가까울수록 비슷.
: 💡 같은 방향 1, 직각 0, 반대 −1

**내적** · Dot product
: 두 벡터를 곱해 **비슷한 정도를 점수 하나로** 내는 계산. Attention에서 Q·K 비교에 사용.

**log** · 로그
: "몇 번 곱해야 이 숫자가 되나". **큰 숫자를 작게 눌러주는** 도구. log(10)=1, log(1,000,000)=6.
: 💡 TF-IDF에서 점수 폭발을 막으려고 씀

**확률** · P(A)
: 어떤 일이 일어날 가능성. P(비) = 비 올 확률.

**조건부 확률** · P(A|B)
: **"B일 때 A일 확률"**. 세로줄은 "~일 때".
: 💡 P(going|Where are we) = 그 뒤에 going이 올 확률

**시그마** · Σ
: **"전부 더해라"** 라는 기호.

**행렬** · Matrix
: 숫자를 **엑셀 표처럼** 가로·세로로 늘어놓은 것. 1024×1024 = 약 100만 칸.

**희소** · Sparse
: **대부분이 0**인 것. One-hot 벡터가 대표적.
: 💡 2만 칸 중 1칸만 체크된 서류

**밀집** · Dense
: **모든 칸에 의미 있는 숫자**가 차 있는 것.
: 💡 [0.12, 0.84, 0.11 …]

**차원 축소** · t-SNE, PCA
: 수백 차원 벡터를 **2~3차원으로 줄여 그림**으로 보는 기법.
: 💡 입체를 벽에 비춘 그림자

**반비례** · Inverse
: 하나가 커지면 다른 하나는 작아지는 관계. IDF는 df에 반비례.

## 🧠 학습의 기초 (AI가 '배운다'는 게 뭐야?)

**파라미터** · Parameter
: 모델 안의 **다이얼(숫자)**. 학습 = 이 다이얼을 맞추는 것. GPT-3는 1,750억 개.
: 💡 M = 백만, B = 십억

**가중치** · Weight
: 파라미터 하나하나의 값. 거의 같은 말.

**학습** · Training
: 답 내기 → 정답과 비교 → 틀린 만큼 다이얼 조정, 을 **수십억 번 반복**.
: 💡 문제집 반복 풀기

**손실** · Loss
: 모델 답이 정답과 **얼마나 틀렸는지** 점수. 작을수록 좋음.

**역전파** · Backpropagation
: 틀린 정도를 **거꾸로 따라가며** 어느 다이얼을 고칠지 계산.

**기울기** · Gradient
: 다이얼을 **어느 방향으로 돌려야** 손실이 줄어드는지 알려주는 화살표.

**경사하강법** · Gradient Descent
: 기울기를 따라 **한 걸음씩** 손실이 낮은 쪽으로 내려가기.
: 💡 안갯속 산에서 골짜기 찾아 내려가기

**기울기 소실** · Vanishing Gradient
: 수정 신호가 뒤→앞으로 가며 **점점 약해져** 앞부분을 못 배우는 문제. RNN의 약점.
: 💡 귓속말 전달 게임

**과적합** · Overfitting
: 학습 데이터만 **달달 외워** 처음 보는 데이터는 못 푸는 상태.
: 💡 기출만 외운 학생

**일반화** · Generalization
: **처음 보는 문제도** 잘 푸는 능력. 과적합의 반대.

**분포 밖** · Out-of-distribution
: 학습 때 본 것과 **다른 종류**의 데이터.

**지도학습** · Supervised
: **문제 + 정답지**로 배우기. Fine-tuning, Instruction Tuning.

**비지도학습** · Unsupervised
: **정답 없이** 자료만 보고 패턴 찾기. Pre-training, AutoEncoder.

**준지도학습** · Semi-supervised
: 비지도 + 지도를 **섞은** 것. GPT-1이 제시.

**강화학습** · Reinforcement
: 해보고 **점수(보상)** 받으며 점수 높은 쪽으로 배우기. RLHF.
: 💡 강아지 간식 훈련

**레이블** · Label
: 데이터에 붙은 **정답**. "이 리뷰 = 긍정".

**드롭아웃** · Dropout
: 학습 때 연결 일부를 **일부러 끊어** 외우기(과적합)를 막는 기법.

**소프트맥스** · Softmax
: 여러 점수를 **합이 100%인 확률**로 바꾸는 함수. Transformer 맨 마지막.
: 💡 고양이 66%, 강아지 24% …

**시그모이드** · Sigmoid
: 어떤 숫자든 **0~1 사이**로 눌러주는 S자 함수. 둘 중 하나 고를 때.

**정규화** · Normalization
: 숫자들의 크기를 **고르게** 맞추는 것. Add & Norm의 Norm.

**추론(사용)** · Inference
: 학습이 끝난 모델로 **실제 답을 내는 것**. 걸리는 시간 = latency.

## 📝 자연어 처리 · 임베딩 (2장)

**자연어** · Natural Language
: 사람이 쓰는 말. 한국어, 영어 등.

**토큰 / 토큰화** · Token / Tokenization
: 글을 자르는 단위(대략 단어 조각) / 글을 토큰으로 자르기.

**단어 사전** · Vocabulary
: 토큰들을 모은 전체 목록.

**코퍼스** · Corpus
: 학습에 쓰는 **대량의 글 모음**. 말뭉치.

**표제어** · Lemma
: 단어의 **겉모양**. 하나의 표제어에 여러 뜻이 들어 있음.
: 💡 "배" = 몸·과일·탈것

**중의성** · Ambiguity
: 한 단어에 **뜻이 여럿**이라 헷갈리는 문제.

**특징 추출** · Feature extraction
: 데이터의 특징을 찾아 **벡터로 바꾸는** 작업.

**임베딩** · Embedding
: 특징 추출로 **자연어를 벡터로** 수치화하는 것. 2003년 처음 소개. 역할: 의미 함축 + 유사도 계산.

**단어 유추 평가** · Word analogy test
: 벡터 덧셈·뺄셈으로 짝을 찾아 임베딩 성능을 보는 평가.
: 💡 아들 − 딸 + 소년 = 소녀

**One-hot 인코딩** · One-hot encoding
: 단어 자리만 **1**, 나머지 0. 한계: **희소 문제 + 유사도 표현 불가**.
: 💡 출석부 한 칸에만 체크

**TF** · Term Frequency
: 이 단어가 **이 문서에** 얼마나 자주 나오나.

**IDF** · Inverse Document Frequency
: 이 단어가 **전체 문서 중** 얼마나 희귀한가. log(n / (1+df)).

**TF-IDF**
: TF × IDF. **이 문서를 특징짓는 단어**에 높은 점수. 한계: 문맥 무시, 희소, 동의어·다의어 불가.
: 💡 자소서의 "드론 대회 우승"

**희소 표현** · Sparse representation
: 벡터·행렬 **대부분이 0**인 표현. One-hot, TF-IDF.

**밀집 표현** · Dense representation
: 사용자가 정한 **작은 차원의 실수 벡터**. 의미 담김, 공간 일정, 일반화 가능.
: 💡 강아지 ≈ 멍멍이

**오토인코더** · AutoEncoder
: 입력 X → **Latent vector Z(압축)** → 출력 X̃ 복원, 3계층. **비지도**. 1986년.
: 💡 책 3줄 요약 후 다시 쓰기

**잠재 벡터** · Latent vector
: AutoEncoder 가운데의 **압축된 핵심** 벡터.

**N-gram**
: **앞의 N−1개 단어만** 보고 다음 단어를 맞히는 통계 모델(SLM).

**최대우도추정** · MLE
: 데이터에서 **가장 자주 나온 것**을 정답으로 추정하는 통계 방법.

## 🔁 모델 구조 · 트랜스포머 (3장)

**RNN** · Recurrent Neural Network
: **한 단어씩 순서대로** 읽으며 메모(hidden state)를 넘기는 모델. 입출력 길이 고정이 한계.

**LSTM / GRU**
: RNN의 기억력 개선판 / LSTM을 더 단순화한 것.

**은닉 상태** · Hidden state
: RNN이 앞에서 읽은 내용을 적어 두는 **메모장**.

**Seq2Seq** · Sequence to Sequence
: **Encoder → Context vector → Decoder** 구조. Google 2014. 가변 길이 입출력 해결.
: 💡 순차통역사

**인코더** · Encoder
: 입력을 받아 **벡터로 압축**하는 부분.

**디코더** · Decoder
: 벡터를 받아 **한 단어씩 출력**하는 부분.

**문맥 벡터** · Context vector
: 입력 문장 전체가 **압축된 벡터 1개**. 고정 크기라 정보 손실.

**sos / eos** · start / end of sentence
: 디코더의 **시작 신호 / 종료 신호** 토큰.

**트랜스포머** · Transformer
: **Attention만으로** 만든 Encoder-Decoder. 2017 "Attention Is All You Need". RNN 한계 3가지 해결.

**어텐션** · Attention
: 문장의 다른 단어들 중 **중요한 데에 집중**하는 계산.
: 💡 "그것"이 "동물"을 가리킴을 찾기

**셀프 어텐션** · Self-Attention
: **같은 문장 안에서** 단어끼리 서로 참고.

**Query / Key / Value** · Q / K / V
: 찾는 것 / 각 단어의 이름표 / 실제 내용. Q·K로 점수 → softmax → V를 섞음.
: 💡 도서관: 질문·책 제목·책 내용

**멀티헤드** · Multi-head
: Attention을 **여러 관점으로 동시에**.
: 💡 평론가 여러 명이 동시에 리뷰

**마스킹** · Masked
: 디코더에서 **아직 안 쓴 뒤쪽 단어를 가림**.
: 💡 받아쓰기에서 다음 문장 가리기

**위치 인코딩** · Positional Encoding
: 한꺼번에 넣으니 순서를 모름 → **위치 번호표**를 더해 줌.
: 💡 단체 사진 번호표

**Add & Norm** · 잔차 연결 + 정규화
: 결과에 **원본을 다시 더하고**(안전장치) 숫자 크기를 고르게.

**FFNN** · Feed-Forward Neural Network
: 각 위치마다 적용하는 **일반 신경망**. Attention으로 모은 정보를 한 번 더 가공.

**병렬화** · Parallelization
: 여러 계산을 **동시에**. RNN은 불가, Transformer는 가능.
: 💡 채점자 100명이 동시에 채점

**BERT**
: Transformer **인코더** 계열. **양방향**, 이해에 강함.

**GPT** · Generative Pre-trained Transformer
: Transformer **디코더** 계열. **단방향, Autoregressive**, 생성에 강함.

**자기회귀** · Autoregressive
: **자기가 방금 쓴 단어를 다시 보며** 다음 단어 예측.

**언어 모델링** · Language Modeling
: 단어 시퀀스의 생성 가능성을 모델링해 **미래 토큰의 확률 예측**.

**SLM → NLM → PLM → LLM**
: 통계(1990s) → 신경망(2010s) → 사전학습(2018+) → 거대(2020+) 언어모델.

## 🚀 LLM · GPT (4장)

**LLM** · Large Language Model
: 방대한 텍스트로 학습된 **수천 억 파라미터**의 **Transformer 기반** 언어 모델.

**PLM** · Pre-trained Language Model
: 대량의 글로 **일반적 언어 이해**를 사전학습한 모델.

**사전학습** · Pre-training
: 정답 없는 대량의 글로 **기본기**를 익히는 단계.
: 💡 교양 수업

**미세조정** · Fine-tuning
: 정답 있는 특정 데이터로 **그 과제에 맞추는** 단계.
: 💡 전공 수업

**SFT** · Supervised Fine-Tuning
: **지도** 미세조정.

**다운스트림 태스크** · Downstream task
: 사전학습 **다음에** 하는 실제 목표 과제(분류, 번역 등).

**창발적 능력** · Emergent Abilities
: 모델이 **일정 크기를 넘으면 갑자기 생기는** 능력. **PLM과 구별되는 LLM의 가장 큰 특징**.
: 💡 물이 100도에서 끓기

**In-context Learning** · 문맥 내 학습
: 프롬프트 속 **예시만 보고** 과제 수행. **모델 파라미터는 안 바뀜**. GPT-3가 공식 도입.
: 💡 알바생에게 예시 보여주기

**Zero / One / Few-shot**
: 예시 **0개 / 1개 / 몇 개**를 주고 시키기.

**컨텍스트 윈도우** · Context Window
: 모델이 **한 번에 읽을 수 있는 분량**.

**태스크 컨디셔닝** · Task conditioning
: GPT-2: P(Output|Input, **Task**). 과제까지 조건으로 받음.

**할루시네이션** · Hallucination
: AI가 **모르는 걸 그럴듯하게 지어내는** 현상. RAG로 줄임.

**멀티모달** · Multimodal
: 글뿐 아니라 **이미지·소리**까지 다룸.

**MoE** · Mixture of Experts
: 모델 안 **전문가 여럿** 중 필요한 것만 불러 쓰는 구조.

**추론 모델** · Reasoning Model
: 답하기 전 **속으로 CoT를 거쳐** 검토 후 답함(o1, o3 등). ↔ 비추론 모델은 바로 답함.
: 💡 수학자 vs 퀴즈 달인

## 🛠 튜닝 · 효율화 (5장)

**Adaptation Tuning**
: 사전학습된 LLM을 **특정 목적에 맞게 추가로 적응**시키기. GPT-3 → ChatGPT의 핵심 변화.

**Instruction Tuning**
: **지시문 + 입력 → 출력 쌍**으로 지도학습. 사용자 의도대로 답하게 + zero-shot 향상.

**FLAN**
: 2021, instruction tuning 최초 제안. task cluster 많을수록 좋고, **작은 모델엔 역효과**.

**태스크 클러스터** · Task cluster
: 비슷한 과제끼리 묶은 **과제 그룹**.

**얼라인먼트** · Alignment
: AI 행동을 **인간 가치에 맞추기**. 기준: 3H.

**3H** · Helpful · Honest · Harmless
: **도움 되기 · 정직하기 · 해롭지 않기**.

**RLHF** · Reinforcement Learning with Human Feedback
: 사람 피드백으로 강화학습. **SFT → Reward Model → RL(PPO)** 3단계.

**보상 모델** · Reward model
: **사람 취향을 흉내 내는 채점 AI**. 사람이 매긴 순위로 학습.

**PPO** · Proximal Policy Optimization
: "**조금씩만 바꿔라**" 안전장치가 있는 강화학습 방법. RLHF 3단계에서 사용.

**정책** · Policy
: 모델의 "이런 상황엔 이렇게 답한다" **행동 방식**.

**PEFT** · Parameter-Efficient Fine-Tuning
: **학습할 파라미터 수를 줄인** 미세조정. Adapter, LoRA.

**내재 차원** · Intrinsic dimension
: 진짜로 필요한 자유도. PLM은 **낮음** → 조금만 학습해도 됨(RoBERTa 200개로 90%).
: 💡 계기판 버튼 1000개 중 핸들·엑셀·브레이크만 씀

**Adapter**
: 기존 층 위에 작은 층 추가, **Down → Up Projection**. 원본 freeze. 1,048,576 → 32,768개.
: 💡 건물 옆 작은 별채

**LoRA** · Low-Rank Adaptation
: **W0 + ΔW = W0 + A·B**. 변화량만 얇은 두 행렬로 학습. 병렬이라 **추론 지연 없음**. 16,384개.
: 💡 교과서에 포스트잇

**랭크** · Rank (m)
: LoRA에서 행렬을 **얼마나 얇게** 쪼갤지. 작을수록 싸다.

**프리즈** · Freeze
: 원래 파라미터를 **고정**(학습 안 함).

**양자화** · Quantization
: 숫자를 **더 적은 비트로** 저장(FP32→FP16→INT8→INT4). **메모리 절감**.
: 💡 사진 화질 낮추기

**비트** · bit
: 숫자 하나를 저장하는 **칸 수**. 많을수록 정밀, 적을수록 가벼움.

**QLoRA** · Quantization + LoRA
: **4-bit로 양자화해 freeze한 LLM + LoRA**. 작은 GPU로도 학습.

## 💬 프롬프트 (6장)

**프롬프트** · Prompt
: LLM에게 **넣는 입력값**.

**프롬프트 엔지니어링** · Prompt Engineering
: 결과 품질을 높이는 **입력값 조합 찾기**. 구성: Instruction · Context · Input Data · Output Indicator.

**Chain-of-Thought** · CoT
: 예시에 **풀이 과정**을 넣어 단계별로 생각하게 함. PaLM 540B **17.7% → 58.1%**.
: 💡 연습장에 풀기

**Zero-shot CoT**
: 예시 없이 "**단계별로 생각해보자**" 한마디로 CoT 효과.

**Self-consistency**
: 여러 번 풀고 **가장 많이 나온 답** 선택(다수결).

**Self-refine** · Self-polish
: 자기 답을 **스스로 검토·수정** 반복(퇴고).

**Selection-inference**
: 후보 추론 중 **가장 적절한 것을 골라** 결론.

**ToT / GoT** · Tree / Graph of Thoughts
: 생각을 **나무처럼 갈래** / **그물처럼 합치며** 펼치기.

**프롬프트 인젝션** · Prompt Injection
: 악의적 지시를 **몰래 끼워 넣어** AI를 속이는 공격.

**오버 프롬프팅** · Over-prompting
: 예시를 **너무 많이** 넣어 오히려 성능이 떨어지는 현상.

**민감도** · Sensitivity
: 작은 변화에 결과가 **얼마나 흔들리나**. 서식만 바꿔도 최대 76%p.

**재현성** · Reproducibility
: 똑같이 다시 하면 **똑같은 결과**가 나오는 성질.

## 🤖 에이전트 기초 (7·8장)

**에이전트** · Agent
: **특정 환경과 상호작용**하는 지능적 시스템. 정의엔 지능 + 환경 필요.

**환경** · Environment
: 에이전트가 보고 움직이는 세계(물리·디지털·인간).

**관찰 / 행동** · Observation / Action
: 환경을 **보고** 얻는 정보 / 환경에 **영향**을 주는 것.

**AI 에이전트** · AI Agent
: **LLM으로 추론**하고 도구·메모리로 목표를 수행하는 개체. ReAct 루프.
: 💡 똑똑한 직원 한 명

**에이전틱 AI** · Agentic AI
: 여러 에이전트를 **조율**해 복잡한 목표를 자율 수행하는 시스템. Orchestrator, 재계획.
: 💡 팀장 있는 회사

**오케스트레이터** · Orchestrator
: 일을 **나눠 주고 결과를 모으는** 지휘자 에이전트.

**에이전트 런타임** · Agent Runtime
: Orchestration(Profile·Memory·Reasoning/Planning) + Model + Tools 구조(Google).

**멀티턴** · Multi-turn
: 여러 번 **주고받는** 대화. 에이전트는 세션 기록으로 가능.

**Text / LLM / Reasoning Agent**
: 언어로 상호작용 ⊃ LLM으로 행동 ⊃ LLM으로 **추론까지**.

**ELIZA**
: MIT의 초기 **룰 기반** 챗봇. 한계: task-specific 규칙, 단순 도메인만.

**인지적 제어** · Cognitive control
: 자기 생각을 **스스로 점검·조절**. Reasoning Agent의 특징.

**자율성** · Autonomy
: 행동·내부 상태 **통제권** 보유. 단계별 지침 없이도 수행.

**반응성** · Reactivity
: 환경 변화에 **신속 대응**. Multi-modal(지각) + Embodiment·Tool(행동) 확장.

**능동성** · Pro-activeness
: **주도적으로 목표 지향** 행동. next token prediction → 추론·계획.

**사회성** · Social ability
: 다른 에이전트와 **상호작용**. NLU·NLG.

**NLU / NLG** · Natural Language Understanding / Generation
: 자연어 **이해** / 자연어 **생성**.

**ReAct** · Reasoning + Acting
: **생각 ↔ 행동**을 번갈아 생성. 추론은 행동을, 행동은 추론을 도움.

**그라운딩** · Grounding
: 생각을 **실제 세계(외부 정보·행동)에 연결**. 외부 행동 = Grounding.

**RAG** · Retrieval-Augmented Generation
: **먼저 검색**해서 찾은 자료를 넣고 생성. 할루시네이션 방지.
: 💡 오픈북 시험

**리트리버** · Retriever
: 관련 자료를 찾아오는 부품. **BM25**(단어 겹침), **DPR**(의미 벡터).

**툴 사용** · Tool Use
: 특수 토큰으로 **도구 호출**을 생성. 계산기·검색·날씨 API·코드 실행.

**API** · Application Programming Interface
: **프로그램끼리 대화하는 창구**.

**Extension / Function**
: API를 **에이전트가 직접 호출**(Agent-Side) / **클라이언트가 호출**(Client-Side).
: 💡 비서에게 카드 주기 vs 메모만 받기

## 🧩 에이전트 구조 · 아키텍처 (9~12장)

**Perception · Brain · Action**
: **감지·변환 → 기억·추론·결정 → 수행**. 반복하며 피드백 받는 게 LLM과의 차이.

**Embodiment** · 체화
: 로봇 몸처럼 **물리적으로 행동**하는 능력.

**메모리 검색 기준** · Recency · Relevance · Importance
: **최근인가 · 관련 있나 · 중요한가** 점수로 기억 골라오기.

**계획 수립 / 반성** · Plan formulation / reflection
: 하위 작업으로 **분해**(One-shot·Step-by-Step·Hierarchical) / 계획을 **피드백**(내부·인간·환경).

**Continual learning** · 지속 학습
: 새로 배워도 **예전 걸 잊지 않기**(Forgetting 완화).

**HuggingGPT**
: ChatGPT가 지휘: **Task Planning → Model Selection(model card) → 응답 생성**.

**Task / Innovation / Lifecycle**
: Single Agent 3단계: 시킨 일 / 새 지식 창출 / 스스로 성장(**AGI 목표**).

**AGI** · Artificial General Intelligence
: 사람처럼 **무엇이든** 하는 범용 인공지능.

**The Society of Mind** · 마음의 사회
: Minsky 1986: 지능은 **작은 에이전트들의 상호작용**에서 생긴다 → Multi-Agent 근거.

**ChatDev / ChatEval**
: **협력형**(Design→Coding→Testing) / **적대형**(토론으로 평가).

**Instructor-Executor / Equal Partnership**
: 사람이 지시·AI 수행(**현재 기본**) / 대칭 관계의 동료.

**인지 아키텍처** · Cognitive Architecture
: 인간이 **인식·기억·추론·행동 결정**하는 기본 구조. Newell, Simon.

**CoALA** · Cognitive Architectures for Language Agents
: **Memory · Action Space · Decision-making** 3요소 프레임워크.

**작업 기억** · Working Memory
: **지금 처리 중인** 정보(단기).

**의미 기억** · Semantic Memory
: **사실·개념·지식**(장기).
: 💡 파스타 = 면 + 소스

**일화 기억** · Episodic Memory
: **과거 경험·사건**(장기).
: 💡 전에 물이 적어서 실패

**절차 기억** · Procedural Memory
: **방법·규칙·스킬**(장기).
: 💡 boil_water()

**Retrieval / Reasoning / Learning** · 내부 행동
: 장기→작업으로 **꺼내기** / 작업 기억 **가공** / →장기에 **저장**.

**Proposal → Evaluation → Selection** · 의사결정
: 후보 **제안** → **평가**(휴리스틱·시뮬레이션) → **선택**(없으면 다시 제안) → Execution.
: 💡 점심 메뉴 고르기

**휴리스틱** · Heuristic
: 경험상 **대충 맞는** 판단 규칙.

**피드백 루프** · Feedback loop
: 결과를 **다시 입력으로** 돌리는 순환. Agent = 제어 시스템.
: 💡 에어컨 온도 조절

**Single / Multi-Agent**
: 모델 하나가 전부 / 여러 모델이 **페르소나·역할**을 나눠 협력.

**페르소나** · Persona
: AI에게 준 **캐릭터·역할**.

**Vertical / Horizontal** · 수직 / 수평
: **리더에게 보고**, 분업 명확 / **전원 평등**, 공용 스레드, 자원.

**Publish-subscribe** · 발행-구독
: 모두 게시판에 올리고 **자기 일에 필요한 것만 읽기**. MetaGPT.
: 💡 신문 구독

**MetaGPT**
: **structured output 강제** + publish-subscribe → Vertical.

**DyLAN**
: round마다 **기여도 평가 → 높은 agent만 진출** → Horizontal.
: 💡 서바이벌 오디션

**RAISE**
: ReAct + short/long memory. 그러나 역할 혼동·할루시네이션(세일즈 시켰더니 코드 작성).
