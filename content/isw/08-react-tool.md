# 8. ReAct와 Tool Use

## 이 장의 한 줄 요약

> **Agent가 일을 하려면 ① 생각(Reasoning) ② 최신 지식(Knowledge) ③ 정확한 계산(Computation)이 필요하다. 각각을 프롬프트 기법 / RAG / Tool Use로 해결하고, 생각과 행동을 번갈아 하는 게 ReAct.**

| 필요한 것 | 왜 LLM 혼자 안 되나 | 해결책 |
|---|---|---|
| **Reasoning** (생각) | 복잡한 문제는 한 번에 못 풂 | 프롬프트 기법 (CoT, 과제 분해 등) |
| **Knowledge** (지식) | 학습 이후 정보를 모름 | **RAG** (검색해서 넣어주기) |
| **Computation** (계산) | 정확한 계산을 못 함 | **Tool Use** (계산기·코드 도구) |

---

## 1. ReAct ★★

**ReAct = Reasoning + Acting** (추론 + 행동)

- **Reasoning과 Acting이라는 두 가지 방식을 둘 다 생성**
- **기존에는 모델이 추론만 하거나 행동만 생성했지만, ReAct는 둘 다 생성함**
- **시너지 효과: 추론은 행동을 돕고, 행동은 추론을 도움**
- **ReAct 방식은 다양한 QA 작업을 해결하는 데 사용될 수 있으며, 다른 예시와 도구만 제공하면 됨**

### 세 가지 방식 비교 (슬라이드 그림)

<figure class="fig" id="fig-react"><svg viewBox="0 0 680 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ReAct 루프" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-react-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-react-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-react-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-react-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="245" y="20" width="190" height="58" rx="14" fill="#EAF0FA" stroke="#CBD9EE"/><text x="340" y="45" font-size="15" fill="#1E3A6E">💭 Thought (생각)</text><text x="340" y="66" font-size="12.5" fill="#4A5568">무엇을 할까?</text> <rect x="450" y="160" width="210" height="58" rx="14" fill="#FBF0D8" stroke="#EBCF95"/><text x="555" y="185" font-size="15" fill="#C77E16">🛠 Action (행동)</text><text x="555" y="206" font-size="12.5" fill="#4A5568">검색 · 도구 호출</text> <rect x="20" y="160" width="210" height="58" rx="14" fill="#E4F2EA" stroke="#BFE0CC"/><text x="125" y="185" font-size="15" fill="#2E7D55">👀 Observation (관찰)</text><text x="125" y="206" font-size="12.5" fill="#4A5568">결과 확인</text> <g stroke="#1E3A6E" stroke-width="2.2" fill="none" marker-end="url(#fig-react-a)"><path d="M437 56C510 70 548 110 553 154"/><path d="M446 192H236"/><path d="M127 156C132 110 170 70 241 56"/></g> <text x="590" y="96" font-size="12.5" fill="#1E3A6E">추론이 행동을 돕고</text> <text x="90" y="96" font-size="12.5" fill="#1E3A6E">행동 결과가 추론을 돕는다</text> <text x="340" y="184" font-size="12" fill="#8A93A3">환경 🌍</text> <text x="340" y="130" font-size="13" fill="#C77E16">반복하다가 → Final Answer</text> </svg><figcaption>ReAct = Reasoning + Acting: 생각 → 행동 → 관찰을 번갈아 반복 (시너지)</figcaption></figure>

```
① Reasoning (update internal belief)        ② Acting (obtain external feedback)
   Question                                      Action
      ↓                                            ↓
   [LLM] ⟲ Reasoning                           🤖 ⟲ 🌍
      ↓                                            ↓
   Answer                                      Observation

   "머릿속으로만 생각"                          "생각 없이 행동만"

                      ↘          ↙
           ③ ReAct: a new paradigm of agents that reason and act
              Reasoning ⟲ 🤖 ⟲ 🌍  (Action / Observation)
              "생각하고 → 행동하고 → 결과 보고 → 다시 생각"
```

| 방식 | 하는 일 | 문제 |
|---|---|---|
| **Reasoning만** | 머릿속으로 **생각만** (내부 믿음을 업데이트) | **최신 정보가 없음** → 틀린 걸 그럴듯하게 말함 |
| **Acting만** | 생각 없이 **행동만** (외부 피드백 얻기) | **왜 그 행동을 하는지 판단 못 함** → 엉뚱한 검색 반복 |
| **ReAct** | **생각 ↔ 행동 번갈아** | 둘의 장점을 합침 ✅ |

{: .참고 }
> **용어**: **internal belief(내부 믿음)** = 모델이 머릿속에 가진 생각 / **external feedback(외부 피드백)** = 바깥 세상에서 받은 결과

### ReAct의 장점 3가지 (슬라이드)

- **Synergy of reasoning and acting** — 추론과 행동의 **시너지**
- **Simple and intuitive to use** — **단순하고 직관적**으로 사용 가능
- **General across domains** — 여러 **분야에 범용적**

### 예시로 이해하기

{: .참고 }
> **질문: "올해 노벨 문학상 수상자의 대표작은?"**
>
> ```
> Thought 1    : 올해 수상자를 모르니 검색해야겠다.                  ← 생각
> Action 1     : Search["올해 노벨 문학상 수상자"]                    ← 행동
> Observation 1: "OOO 작가가 수상했다."                              ← 결과
> Thought 2    : OOO 작가의 대표작을 찾아야겠다.                     ← 결과를 보고 다시 생각
> Action 2     : Search["OOO 대표작"]                                ← 행동
> Observation 2: "『XXX』가 대표작으로 꼽힌다."                       ← 결과
> Thought 3    : 답을 찾았다.
> Final Answer : 『XXX』입니다.
> ```
>
> - **생각이 행동을 도움**: "모르니까 검색해야겠다", "다음엔 대표작을 찾자" → **무엇을 할지 결정**
> - **행동이 생각을 도움**: 검색 결과를 보고 → **다음 생각을 정확하게 고침**

{: .시험 }
> **예상 문제: "ReAct의 시너지 효과를 설명하시오"**
>
> **모범 답안**: ReAct는 추론(Reasoning)과 행동(Acting)을 **번갈아 생성**한다. **추론은 어떤 행동을 할지 결정하도록 행동을 돕고**, **행동으로 얻은 관찰 결과(Observation)는 추론을 보정하여 추론을 돕는다.** 추론만 하면 외부 정보가 없어 틀리기 쉽고, 행동만 하면 행동의 근거를 판단할 수 없는데, ReAct는 둘을 결합해 이 한계를 해결한다. 또한 **다른 예시와 도구만 제공하면** 다양한 QA 작업에 적용할 수 있다.

---

## 2. Agent의 task 수행의 필요 요건 3가지 ★★★

<figure class="fig" id="fig-3req"><svg viewBox="0 0 740 205" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Agent 필요 요건 3가지" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-3req-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-3req-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-3req-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-3req-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <g font-size="13"> <rect x="10" y="12" width="230" height="74" rx="12" fill="#EAF0FA" stroke="#CBD9EE"/><text x="125" y="42" font-size="15" fill="#1E3A6E">🧩 Reasoning</text><text x="125" y="66" fill="#4A5568">복잡한 문제는 생각이 필요</text> <rect x="10" y="118" width="230" height="74" rx="12" fill="#FBF0D8" stroke="#EBCF95"/><text x="125" y="148" font-size="15" fill="#C77E16">프롬프트 기법</text><text x="125" y="172" font-size="11.5" fill="#4A5568">Instruction·Few-shot·CoT·과제 분해</text> <rect x="255" y="12" width="230" height="74" rx="12" fill="#EAF0FA" stroke="#CBD9EE"/><text x="370" y="42" font-size="15" fill="#1E3A6E">📰 Knowledge</text><text x="370" y="66" fill="#4A5568">학습 이후 정보는 모름</text> <rect x="255" y="118" width="230" height="74" rx="12" fill="#FBF0D8" stroke="#EBCF95"/><text x="370" y="148" font-size="15" fill="#C77E16">RAG</text><text x="370" y="172" font-size="12" fill="#4A5568">먼저 검색해서 넣어주기</text> <rect x="500" y="12" width="230" height="74" rx="12" fill="#EAF0FA" stroke="#CBD9EE"/><text x="615" y="42" font-size="15" fill="#1E3A6E">🧮 Computation</text><text x="615" y="66" fill="#4A5568">정확한 계산은 못 함</text> <rect x="500" y="118" width="230" height="74" rx="12" fill="#FBF0D8" stroke="#EBCF95"/><text x="615" y="148" font-size="15" fill="#C77E16">Tool Use</text><text x="615" y="172" font-size="12" fill="#4A5568">계산기·검색·코드 실행</text> </g> <g stroke="#C77E16" stroke-width="2.2" fill="none" marker-end="url(#fig-3req-b)"><path d="M125 88V114"/><path d="M370 88V114"/><path d="M615 88V114"/></g> </svg><figcaption>필요한 것(위) → 해결책(아래). 짝지어 외우기: Reasoning–프롬프트 / Knowledge–RAG / Computation–Tool</figcaption></figure>

{: .시험 }
> **Reasoning / Knowledge / Computation** 과 각 해결책을 **짝지어** 외우세요.

| 요건 | 슬라이드 정의 | 해결 방법 |
|---|---|---|
| **Reasoning** | **복잡한 질문 해결을 위해서는 추론이 필요** | **프롬프트 기법** (Instructions, Few-shot, Context, CoT, 과제 분해) |
| **Knowledge** | **모델이 훈련된 시점 이후에 발생한 정보**(예: 2026년 1월 5일 뉴스)에 대해서는 **새로운 지식이 필요** | **RAG** (Retrieval-Augmented Generation) |
| **Computation** | **매우 수학적이고 어려운 질문의 경우, 트랜스포머의 auto-regression을 넘어서는 계산 방식이 필요** | **Tool Use** |

{: .참고 }
> **Computation이 왜 필요?** LLM은 **다음 단어를 확률로 맞히는 기계**(auto-regression)입니다. "3847 × 2961 = ?" 를 물으면 **계산하는 게 아니라 그럴듯한 숫자를 "짐작"** 합니다. 그래서 자주 틀려요.
> 사람도 큰 곱셈은 **계산기**를 쓰죠. AI에게도 **계산기(도구)** 를 쥐여 주는 겁니다.
>
> **Knowledge가 왜 필요?** LLM은 **학습이 끝난 날까지의 정보만** 압니다 (knowledge cutoff). 그 이후 뉴스는 모릅니다.

---

## 3. ① Reasoning — 추론을 돕는 5가지 방법 ★

슬라이드 목록:

1. **명확하고 충분한 설명을 포함하는 Instructions**
2. **Few-shot examples**
3. **Provide relevant context**
4. **Chain of thought (CoT)**
5. **Break down Complex tasks** (**Tree-of-Thought, Graph-of-Thoughts**)

### 1) Instructions — 명확한 지시

```
❌ Bad : "맛있는 저녁 레시피 하나 알려줘."

✅ Good (Instructions):
   "너는 전문 요리사야. 냉장고에 남은 두부와 김치를 활용해서 만들 수 있는
    15분 내외의 간단한 저녁 메뉴를 추천해줘. 단, 내가 매운 걸 잘 못 먹으니까
    최대한 덜 맵게 만드는 법을 알려줘야 해."
```

**Good이 좋은 이유**: **역할**(전문 요리사) + **재료 조건**(두부, 김치) + **시간 조건**(15분) + **개인 조건**(덜 맵게) 이 모두 명확함

### 2) Few-shot examples — 예시 제공

```
"내가 좋아하는 영화 스타일로 오늘 볼 영화를 추천해줘.
 '인셉션'      -> 복잡한 설정과 반전이 있는 영화
 '어바웃 타임'  -> 따뜻하고 감동적인 로맨스 영화
 '극한직업'    -> 생각 없이 웃을 수 있는 코미디 영화
 '라라랜드'    -> [이 영화의 스타일을 모델이 설명함]"
```

**좋은 이유**: 예시 3개로 **"영화 → 스타일 설명"이라는 패턴**을 보여줌 → 모델이 따라 함

### 3) Provide relevant context — 관련 맥락 제공

```
❌ Bad : "부모님 선물로 뭐가 좋을까?"

✅ Good (Context):
   "우리 부모님은 올해 환갑이셔. 평소에 등산을 아주 좋아하시고 주말마다 산에 가셔.
    하지만 최근에 무릎이 조금 안 좋으시다고 하셨어. 이런 상황에서 부모님이
    감동하실 만한 20만원대 선물을 3가지 추천해줘."
```

**좋은 이유**: **상황 정보**(환갑, 등산 좋아함, 무릎 안 좋음, 예산) → 맞춤형 답 가능

### 4) Chain of thought (CoT) — 단계별 사고 유도

```
"편의점에서 1+1 행사를 하는 3,000원짜리 우유를 사는 게 좋을까,
 아니면 대형마트에서 900ml 한 팩에 2,500원 하는 우유를 사는 게 좋을까?
 우유 100ml당 가격을 비교해서 어느 쪽이 얼마나 더 저렴한지 단계별로 계산해줘."
```

**좋은 이유**: **"100ml당 가격으로 비교해서 단계별로"** → 풀이 과정을 거치게 해서 정확도 ↑ ([6장](06-prompt-engineering.html))

### 5) Break down Complex tasks — 복잡한 과제 쪼개기

- **Task를 더 간단한 subtask로 나누어서 각각을 다른 prompt에 넣기**
- **각 subtask는 전체 task보다 간단하기에 error가 줄어듦**

```
Prompt 1                        → SubTask 1
Prompt 2  + Previous result 1   → SubTask 2
Prompt 3  + Previous result 2   → SubTask 3
Prompt 4  + Previous result 3   → SubTask 4
```

{: .참고 }
> **비유: 보고서 쓰기를 한 번에 시키지 말고 나눠서**
>
> 1. "주제에 대한 자료 정리해줘" → 결과 1
> 2. "결과 1을 보고 목차 짜줘" → 결과 2
> 3. "결과 2 목차대로 본문 써줘" → 결과 3
> 4. "결과 3을 다듬어줘" → 완성
>
> 한 번에 "보고서 써줘"보다 **각 단계가 쉬워서 실수가 줄어듭니다.** 앞 결과를 다음 프롬프트에 넣는 게 포인트.

**확장 기법**

| 기법 | 생각의 모양 | 쉬운 설명 |
|---|---|---|
| **CoT** (Chain-of-Thought) | **일직선** ─── | 한 갈래로 차례차례 |
| **ToT** (Tree-of-Thought) | **나무** ─┬─ | 여러 갈래로 뻗어 보고, **좋은 가지를 골라** 계속 |
| **GoT** (Graph-of-Thoughts) | **그물** ─╳─ | 갈래들이 다시 **합쳐지기도** 하는 자유로운 형태 |

---

## 4. ② Knowledge — RAG ★★

RAG (Retrieval-Augmented Generation, 검색 증강 생성)
: **외부 자료에서 질문에 관련된 정보를 찾아와서, 그걸 언어 모델의 입력에 덧붙여 답을 만들게 하는 방식**

**이름 풀이**: **Retrieval**(검색해서) + **Augmented**(보강된) + **Generation**(생성)

### 동작 (슬라이드)

- **위키피디아와 같은 추가 코퍼스가 존재**
- **Retriever(BM25, DPR 등)가 질문에 가장 관련 있는 정보를 코퍼스에서 끌어옴**
- **검색된 정보를 언어 모델의 컨텍스트에 추가하여 답변을 쉽게 생성하도록 함**

{: .참고 }
> **비유: 오픈북 시험**
>
> - RAG 없는 LLM = **클로즈드북 시험**. 외운 것만으로 답해야 함 → 모르면 지어냄 (할루시네이션)
> - RAG 있는 LLM = **오픈북 시험**. 관련 페이지를 **먼저 찾아서 펼쳐 놓고** 답함 → 정확
>
> **Retriever(검색기)** = 관련 자료를 찾아오는 부품
>
> - **BM25** = 단어가 **겹치는 정도**로 찾는 전통적 방식 (2장 TF-IDF의 친척, sparse)
> - **DPR (Dense Passage Retrieval)** = **의미가 비슷한 걸** 벡터로 찾는 방식 (2장 Dense 표현)

### RAG 프레임워크 플로우 (5단계) ★

<figure class="fig" id="fig-rag"><svg viewBox="0 0 740 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="RAG 흐름" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-rag-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-rag-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-rag-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-rag-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="20" y="95" width="120" height="60" rx="12" fill="#F2EFE8" stroke="#E7E2D7"/><text x="80" y="130" font-size="15">🙋 사용자</text> <rect x="280" y="95" width="150" height="60" rx="12" fill="#EAF0FA" stroke="#CBD9EE"/><text x="355" y="130" font-size="15" fill="#1E3A6E">⚙ 시스템</text> <rect x="560" y="12" width="160" height="72" rx="12" fill="#FBF0D8" stroke="#EBCF95"/><text x="640" y="42" font-size="15" fill="#C77E16">📚 지식 저장소</text><text x="640" y="64" font-size="12" fill="#4A5568">문서 · DB · 웹</text> <rect x="560" y="165" width="160" height="60" rx="12" fill="#E4F2EA" stroke="#BFE0CC"/><text x="640" y="200" font-size="15" fill="#2E7D55">🧠 LLM</text> <g stroke="#1E3A6E" stroke-width="2" fill="none" marker-end="url(#fig-rag-a)"><path d="M142 125H276"/><path d="M432 104L556 42"/><path d="M556 70L436 118"/><path d="M432 140L556 190"/></g> <path d="M600 227V240H80V158" stroke="#2E7D55" stroke-width="2" fill="none" marker-end="url(#fig-rag-c)"/> <g font-size="12.5"><text x="209" y="116" fill="#1E3A6E">① 질문</text><text x="470" y="58" fill="#1E3A6E">② 검색</text><text x="520" y="114" fill="#C77E16">③ 관련 정보</text><text x="470" y="186" fill="#1E3A6E" text-anchor="end">④ 질문+찾은 정보</text><text x="340" y="234" fill="#2E7D55">⑤ 생성된 답변</text></g> </svg><figcaption>RAG: 먼저 검색(②③)해서 찾은 자료를 질문과 함께 LLM에 넣고(④) 답을 만든다(⑤) = 오픈북 시험</figcaption></figure>

```
 ① 사용자 ──── Prompt와 Query ────→ [시스템]
                                       │
 ② [시스템] ──────── Query ─────────→ [지식 컨텐츠 저장소] (문서, DB)
                                       │
 ③ [시스템] ←── 증강된 컨텍스트(관련 정보) ── [지식 컨텐츠 저장소]
                                       │
 ④ [시스템] ── Prompt + Query + 증강된 컨텍스트 ──→ [LLM]
                                       │
 ⑤ 사용자 ←──── 생성된 텍스트 응답 ──── [시스템]
```

| 단계 | 하는 일 |
|---|---|
| ① | 사용자가 **질문**을 보냄 |
| ② | 시스템이 질문으로 **자료 저장소를 검색** |
| ③ | 저장소가 **관련 정보**를 돌려줌 |
| ④ | **질문 + 찾은 정보**를 합쳐서 LLM에 보냄 |
| ⑤ | LLM이 그걸 바탕으로 **답을 생성**해 사용자에게 |

**Agent 관점 (Google Cloud)**

```
Agent ──→ Data Store ──┬──→ Private Docs     (사내 문서 등 비공개 자료)
                       ├──→ Websites         (웹 페이지)
                       └──→ Structured Data  (표 형태의 정형 데이터)
```

{: .중요 }
> **순서 포인트: 검색이 먼저, 생성이 나중**
> 질문을 받자마자 답하는 게 아니라 **① 관련 자료 찾기 → ② 질문에 끼워 넣기 → ③ 생성**.
>
> **RAG가 필요한 이유 (서술형용)**
>
> - LLM은 **학습 시점 이후의 정보를 모름**
> - 모르는 걸 **그럴듯하게 지어냄 (할루시네이션)**
> - RAG는 **모델을 다시 학습시키지 않고도** 최신·전문 지식을 넣어줄 수 있음
> - (1장 커리큘럼: **"RAG: 검색 기반 생성으로 할루시네이션 방지 및 Agent별 지식 베이스를 생성하고 업데이트"**)

---

## 5. ③ Computation — Tool Use ★★

Tool Use (도구 사용)
: **언어 생성의 자연스러운 형식에 특수 토큰을 도입하여 tool calls(도구 호출)를 포함시키는 것**

- 예: **계산기, 위키피디아 검색, 날씨 API 호출** 등
- **Tool을 통해 언어모델을 다양한 지식, 정보, 심지어 계산 능력으로 augment(증강)할 수 있음**

{: .참고 }
> **"특수 토큰을 도입"이 무슨 뜻?**
> 모델이 글을 쓰다가 **"여기서 도구 써!"라는 특별한 표시**를 출력하게 가르치는 겁니다.
> 그 표시가 나오면 프로그램이 **진짜 도구를 실행**하고, 결과를 다시 모델에게 넘겨줍니다.

### 일반 LM vs Tool Augmented LM (TALM, 2022)

```
[Language Model]
   input ──→ [LM] ──→ output

[Tool Augmented Language Model]
   input ──→ [LM] ──→ tool input ──→ (call external tool 🔧) ──→ tool result
                                                                     ↓
                                     [LM] ←── (append tool result) ──┘
                                       ↓
                                    output
```

**흐름**: 입력 → 모델이 **도구에 줄 입력**을 만듦 → **외부 도구 호출** → **결과를 붙여서** 다시 모델에 → 최종 출력

**추상적 형식 (슬라이드)**

```
An abstract task:
  task input text |tool-call tool input text |result tool output text |output task output text

A weather task:
  how hot will it get in NYC today?                         ← 질문
  |weather lookup region=NYC                                ← 도구 호출 (날씨 조회, 지역=뉴욕)
  |result precipitation chance: 10, high temp: 20c, low-temp: 12c   ← 도구 결과
  |output today's high will be 20C                          ← 최종 답
```

{: .참고 }
> `|` 기호로 **질문 / 도구 호출 / 도구 결과 / 최종 답**을 구분합니다. 모델은 이 형식을 배워서 **필요할 때 도구 호출 부분을 스스로 써냅니다.**

### Tool 사용 예시 3가지 ★

{: .시험 }
> 그대로 나오기 좋습니다.

| 도구 | 질문 | 동작 |
|---|---|---|
| **웹 검색 (Web-search)** | "사용자 리뷰를 바탕으로 가장 좋은 카페는 어디야?" | 모델이 `{tool: web-search, query: "cafe reviews"}` 생성 → 외부 도구가 결과 전달 |
| **날씨 API (Get-weather)** | "샌프란시스코 날씨 어때?" | 모델이 `{tool: get-weather, query: "SF"}` 생성 → 실시간 날씨 정보 반환 |
| **코드 인터프리터 (Python-interpreter)** | "100달러를 연 7% 복리로 12년 투자하면 최종 금액이 얼마야?" | 모델이 **파이썬 코드 생성 및 실행** → 결과값 도출 |

{: .참고 }
> - **API** = 프로그램끼리 대화하는 창구 (날씨 API에 "SF" 주면 날씨 데이터를 돌려줌)
> - **코드 인터프리터** = 파이썬 코드를 **실제로 실행해주는** 도구. 복리 계산은 `100 * (1.07 ** 12)` 를 실행하면 정확히 약 225달러가 나옴
>   (슬라이드엔 `100 * (1+0.07)*12` 로 적혀 있는데, 복리는 **12제곱**(`**12`)이 맞습니다. 의도는 "파이썬으로 계산한다"는 것)
> - **복리** = 이자에 또 이자가 붙는 방식

### Tool 생성 형식의 문제점 ★

{: .중요 }
> **Tool을 사용하기 위한 생성 형식은 인터넷에서 볼 수 있는 일반적인 텍스트와는 매우 다름**
>
> LLM은 **자연스러운 글**(블로그, 뉴스, 책)로 학습했는데, `{tool: get-weather, query: "SF"}` 같은 **기계적인 형식**은 인터넷에 거의 없습니다. 그래서 **형식을 틀리기 쉽습니다** (괄호 빠뜨리기, 이름 틀리기 등).
> → 이게 **Structured Output / Function Calling** (5주차 주제)이 필요한 이유입니다.

### Extension / Function을 이용해서 Agent와 API를 연동 ★

<figure class="fig" id="fig-extfn"><svg viewBox="0 0 740 215" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Extension과 Function 비교" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-extfn-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-extfn-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-extfn-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-extfn-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="8" y="8" width="354" height="198" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="185" y="34" font-size="14" fill="#1E3A6E">Extension · Agent-Side Control</text> <rect x="22" y="84" width="76" height="44" rx="10" fill="#F2EFE8"/><text x="60" y="111" font-size="13">📱 앱</text> <rect x="128" y="84" width="104" height="44" rx="10" fill="#FBF0D8" stroke="#EBCF95"/><text x="180" y="111" font-size="13">🤖 에이전트</text> <rect x="268" y="84" width="80" height="44" rx="10" fill="#EAF0FA"/><text x="308" y="111" font-size="13">✈ API</text> <g stroke-width="2" fill="none"><path d="M100 106H124" stroke="#1E3A6E" marker-end="url(#fig-extfn-a)"/><path d="M234 106H264" stroke="#C77E16" marker-end="url(#fig-extfn-b)"/></g> <text x="249" y="76" font-size="12" fill="#C77E16">직접 호출</text> <text x="185" y="180" font-size="12.5" fill="#8A93A3">에이전트가 직접 부름 (비서에게 카드 맡기기)</text> <rect x="378" y="8" width="354" height="198" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="555" y="34" font-size="14" fill="#2E7D55">Function · Client-Side Control</text> <rect x="510" y="48" width="110" height="40" rx="10" fill="#FBF0D8" stroke="#EBCF95"/><text x="565" y="73" font-size="13">🤖 에이전트</text> <rect x="398" y="128" width="90" height="44" rx="10" fill="#F2EFE8"/><text x="443" y="155" font-size="13">📱 앱</text> <rect x="622" y="128" width="96" height="44" rx="10" fill="#EAF0FA"/><text x="670" y="155" font-size="13">✈ API</text> <g stroke-width="2" fill="none"><path d="M440 126L520 90" stroke="#1E3A6E" marker-end="url(#fig-extfn-a)"/><path d="M548 90L478 128" stroke="#1E3A6E" marker-end="url(#fig-extfn-a)"/><path d="M490 150H618" stroke="#2E7D55" marker-end="url(#fig-extfn-c)"/></g> <text x="452" y="100" font-size="11.5" fill="#1E3A6E" text-anchor="end">① 요청</text> <text x="566" y="114" font-size="11.5" fill="#1E3A6E" text-anchor="start">② "이 함수를 이 값으로"</text> <text x="554" y="190" font-size="12" fill="#2E7D55">③ 앱이 직접 호출 (메모만 받고 내가 결제)</text> </svg><figcaption>차이 = 실제로 API를 누가 부르나: Extension은 에이전트, Function은 클라이언트(앱)</figcaption></figure>

```
┌──────────── Agent ────────────┐
│  Reasoning Loop               │
│    [Model]   [Tools]          │
│                ├── Flights Extension ──→ Flights API
│                ├── Maps Extension    ──→ Maps API
│                └── Weather Extension ──→ Weather API
└───────────────────────────────┘
```

**두 가지 방식**

```
A. Extension (Agent-Side Control)
   UI / Middleware → Agent → Extension → Google Flights API
                              └── 에이전트 쪽이 API를 직접 호출

B. Function (Client-Side Control)
   UI / Middleware → Agent → Function ┐
                     ↓                │ "이 함수를 이 값으로 불러" 라고만 알려줌
   UI / Middleware ─────────────────→ Google Flights API
                     └── 실제 호출은 클라이언트(앱) 쪽이 함
```

| 방식 | 제어 주체 | 누가 API를 실제 호출? | 언제 유리? |
|---|---|---|---|
| **Extension** | **Agent-Side Control** | **에이전트**가 직접 | 에이전트에게 맡겨도 될 때, 간단할 때 |
| **Function** | **Client-Side Control** | **클라이언트(앱)** 가 | 보안·인증·권한을 **앱이 쥐고 있어야** 할 때 |

{: .참고 }
> **비유: 비서에게 항공권 예약 시키기**
>
> - **Extension** = 비서에게 **내 카드를 주고** "알아서 예약해" → 비서가 직접 결제
> - **Function** = 비서는 **"이 항공편을 이 날짜로 예약하세요"라고 메모만** 써주고, **결제는 내가** 직접
>
> **클라이언트(client)** = 사용자가 쓰는 앱·프로그램 쪽. **Middleware** = 중간에서 연결해주는 소프트웨어.

{: .시험 }
> **Extension과 Function의 차이 = 누가 실제로 API를 호출하는가**
>
> - **Extension**: **Agent-Side Control** — 에이전트가 직접 호출
> - **Function**: **Client-Side Control** — 클라이언트가 호출

---

## 이 장 정리

| 주제 | 핵심 |
|---|---|
| **ReAct** | Reasoning + Acting 둘 다 생성 / **추론은 행동을, 행동은 추론을 도움** / 장점: Synergy, Simple, General |
| **필요 요건 3가지** | **Reasoning** → 프롬프트 기법 / **Knowledge** → RAG / **Computation** → Tool Use |
| **Reasoning 5방법** | Instructions, Few-shot, Context, CoT, 과제 분해(ToT, GoT) |
| **RAG** | Retriever(**BM25, DPR**)가 코퍼스에서 찾아 컨텍스트에 추가 / 5단계 플로우 |
| **Tool Use** | 특수 토큰으로 tool call / 예: web-search, get-weather, python-interpreter / 문제: 형식이 일반 텍스트와 다름 |
| **Extension vs Function** | **Agent-Side** vs **Client-Side** Control |
