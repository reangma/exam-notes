# 지능형 소프트웨어

중간고사 범위를 **수학·AI를 하나도 모르는 사람도 이해할 수 있게** 다시 쓴 노트입니다.
이 과목 중간고사는 **필기시험(written test)** 이라서, **용어의 정의 + 왜 필요한지 + 비교**를 내 말로 쓸 수 있는지가 핵심입니다.

{: .중요 }
> **범위: 배포된 강의 자료 3개가 전부이고, 212페이지를 한 장도 빠짐없이 이 노트에 옮겼습니다.**
>
> | 강의 자료 | 페이지 | 이 노트 |
> |---|---|---|
> | #0 Orientation | 11p | 1장 |
> | #1 Large Language Model | 109p | 2~6장 |
> | #2 AI Agent 개념 · Cognitive Architecture | 92p | 7~12장 |
>
> 그림으로만 되어 있던 슬라이드(RLHF 3단계, 언어모델 발전사, QLoRA 정리, 프롬프트 민감도 논문 등)도 전부 글로 풀었습니다. **이것만 보면 됩니다.**

---

## 공부 순서 (추천)

1. **[0장 수학·용어 기초](00-math-basics.html)** — 벡터, log, 확률, 파라미터 같은 말이 처음이면 **반드시 먼저**
2. **[📖 쉬운 용어사전](00-glossary.html)** — 173개 단어를 비유와 함께. 한 번 쭉 훑고 시작하면 본문이 훨씬 쉬워요
3. **1장 → 12장** 순서대로 — 각 장 맨 위 **"이 장의 한 줄 요약"** 과 **그림**부터 보고 들어가세요 (그림 31개)
4. **[헷갈리는 개념 총정리](97-compare.html)** — 비슷한 두 개를 한 단어로 구분하기 + 함정 보기 + 키워드 매칭
5. **[예상 문제](98-exam-questions.html)** — 객관식 30 · 빈칸 25 · 단답·서술 111, 답을 가리고 풀기
6. **[핵심 암기 치트시트](99-cheatsheet.html)** — 시험 직전 30분

---

## 이 과목이 결국 하려는 이야기

<figure class="fig" id="fig-big"><svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="과목 전체 흐름" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-big-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-big-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-big-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-big-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="10" y="40" width="150" height="80" rx="14" fill="#F2EFE8" stroke="#E7E2D7"/> <text x="85" y="76" font-size="15">"사과"</text><text x="85" y="100" font-size="12.5" fill="#8A93A3">글자 (컴퓨터는 모름)</text> <rect x="205" y="40" width="160" height="80" rx="14" fill="#EAF0FA" stroke="#CBD9EE"/> <text x="285" y="76" font-size="15" fill="#1E3A6E">임베딩</text><text x="285" y="100" font-size="12.5" fill="#4A5568">[0.8, 0.1, 0.3 …]</text> <rect x="410" y="40" width="160" height="80" rx="14" fill="#EAF0FA" stroke="#CBD9EE"/> <text x="490" y="76" font-size="15" fill="#1E3A6E">LLM</text><text x="490" y="100" font-size="12.5" fill="#4A5568">다음 단어 맞히기</text> <rect x="615" y="40" width="135" height="80" rx="14" fill="#FBF0D8" stroke="#EBCF95"/> <text x="682" y="76" font-size="15" fill="#C77E16">AI Agent</text><text x="682" y="100" font-size="12.5" fill="#4A5568">+도구·기억·계획</text> <g stroke="#1E3A6E" stroke-width="2.2" fill="none" marker-end="url(#fig-big-a)"><path d="M162 80H200"/><path d="M367 80H405"/><path d="M572 80H610"/></g> <g font-size="12.5" fill="#8A93A3"><text x="285" y="150">2장</text><text x="490" y="150">3·4·5·6장</text><text x="682" y="150">7~12장</text></g> <text x="380" y="185" font-size="13" fill="#4A5568">숫자로 바꾸고 → 그 숫자로 말을 하고 → 손발을 달아 일을 시킨다</text> </svg><figcaption>이 과목 전체를 한 장으로: 글자 → 숫자(임베딩) → 말하는 모델(LLM) → 일하는 모델(Agent)</figcaption></figure>

> **"글자를 숫자로 바꾸는 법(임베딩)" → "그 숫자로 다음 단어를 맞히는 거대한 모델(LLM)" → "그 모델에게 손발과 기억을 달아준 것(AI Agent)"**

각 장이 **앞 장의 한계**를 해결하면서 이어집니다. "이전 방식의 무엇이 문제였나?"를 같이 기억하면 전체가 하나의 이야기가 됩니다.

| 단계 | 내용 | 해결한 문제 | 장 |
|---|---|---|---|
| 임베딩 | 단어를 벡터(숫자 목록)로 | 컴퓨터는 글자를 모른다 | 2 |
| Dense 표현 | 짧고 의미 있는 벡터로 | One-hot은 너무 크고 의미가 없다 | 2 |
| Transformer | Attention으로 한꺼번에 처리 | RNN은 느리고 정보를 잃는다 | 3 |
| LLM (GPT) | 거대 모델 + In-context Learning | 매번 Fine-tuning 하기 번거롭다 | 4 |
| Adaptation Tuning | Instruction · Alignment · PEFT | 똑똑한데 말을 안 듣고, 튜닝이 비싸다 | 5 |
| Prompt Engineering | 질문을 잘하는 법 | 모델은 그대로 두고 성능을 올리고 싶다 | 6 |
| AI Agent | 도구 + 기억 + 계획 | LLM은 머리만 있고 손발·기억이 없다 | 7~10 |
| Cognitive Architecture | 기억·행동·의사결정 구조화 | Agent를 어떤 구조로 설계할지 기준이 없다 | 11 |
| Multi-Agent | 여러 에이전트로 조직 | 혼자서는 복잡한 일을 감당 못 한다 | 12 |

## 전체 목차

| 장 | 내용 |
|---|---|
| [0. 수학·용어 기초](00-math-basics.html) | 벡터, 코사인 유사도, log, 확률, 행렬, 파라미터, softmax, sigmoid, 학습 방식, 약어 |
| [📖 쉬운 용어사전](00-glossary.html) | 시험에 나오는 단어 173개, 비유·예시 포함 |
| [1. 과목 개요와 AI Agent 역사](01-course-overview.html) | 챗봇 vs 에이전트, 에이전트 유형 5단계, 기본 구조 4가지 |
| [2. 자연어 임베딩](02-embedding.html) | One-hot, TF-IDF(계산), Sparse vs Dense, AutoEncoder |
| [3. Seq2Seq와 Transformer](03-transformer.html) | RNN 한계, Attention, SLM→NLM→PLM→LLM |
| [4. LLM과 GPT 시리즈](04-llm-gpt.html) | GPT-1/2/3 비교표, In-context Learning, 추론 모델 |
| [5. Adaptation Tuning](05-adaptation-tuning.html) | Instruction Tuning, RLHF 3단계, LoRA, 양자화, QLoRA |
| [6. Prompt Engineering](06-prompt-engineering.html) | 구성요소 4가지, CoT, 어려운 이유 4가지 |
| [7. AI Agent의 개념과 분류](07-ai-agent.html) | Agent vs AI Agent vs Agentic AI, 4가지 성질 |
| [8. ReAct와 Tool Use](08-react-tool.html) | ReAct, Reasoning/Knowledge/Computation, RAG |
| [9. LLM 기반 Agent의 구조](09-agent-structure.html) | Perception–Brain–Action, Memory 챌린지 |
| [10. Agent의 실제 활용](10-agent-practice.html) | Single/Multi/Human-Agent 시나리오 |
| [11. Cognitive Architecture와 CoALA](11-cognitive-architecture.html) | 메모리 4종, Action Space, Decision-making |
| [12. AI Agent 아키텍처 분류](12-agent-architectures.html) | Single vs Multi, Vertical vs Horizontal |
| [헷갈리는 개념 총정리](97-compare.html) | 연도 연표, 짝 비교표, 함정 보기, 키워드 → 정답 매칭 |
| [예상 문제](98-exam-questions.html) | 객관식 30 + 빈칸 25 + 단답·서술 111 (모범 답안 포함) |
| [핵심 암기 치트시트](99-cheatsheet.html) | 숫자·정의·비교표만 |

## 박스 읽는 법

{: .시험 }
> **노란 박스** = **문제로 나오기 좋은 지점**. 서술형으로 쓸 수 있을 만큼 외우세요.

{: .중요 }
> **빨간 박스** = **헷갈리기 쉬워서 비교 문제로 나오기 좋은 것**.

{: .참고 }
> **파란 박스** = **쉬운 설명·비유·용어 풀이**. 외울 필요는 없지만, 읽으면 이해가 훨씬 쉬워집니다.

{: .주의 }
> **보라 박스** = **슬라이드 자체의 오류나 함정**. 시험에서 어떻게 쓸지 안내합니다.
