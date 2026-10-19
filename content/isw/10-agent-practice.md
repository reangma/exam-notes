# 10. Agent의 실제 활용 (Agents in Practice)

## 이 장의 한 줄 요약

> **Agent를 실제로 쓰는 3가지 방식: ① 혼자 일하기(Single) ② 여럿이 일하기(Multi) ③ 사람과 같이 일하기(Human-Agent)**

```
              Agents in Practice (Harnessing AI for Good)
       ┌──────────────────┼───────────────────┐
  Single Agent      Multiple Agents      Human-Agent
  (혼자)             (여럿이)              (사람과)
   ├ Task           ├ 협력형 (ChatDev)     ├ Instructor-Executor
   ├ Innovation     └ 적대형 (ChatEval)    └ Equal Partnership
   └ Lifecycle
```

---

## 1. AI Agent의 발전 방향성 ★

{: .시험 }
> **3가지 방향성** — 번호 그대로 서술형에 쓸 수 있어야 합니다.
>
> 1. **사용자가 반복적인 일상 업무에서 벗어나도록 도움 → 작업 효율성 향상**
> 2. **사용자의 명시적인 지침 없이, 에이전트가 독립적으로 문제를 분석/계획/해결**
> 3. **에이전트의 혁신적인 능력을 바탕으로, 최첨단 과학 분야에서 잠재력 발휘**

**쉽게**
1. **귀찮은 반복 일을 대신** 해준다 (이메일 정리, 일정 잡기)
2. **일일이 안 시켜도 알아서** 한다
3. **과학 연구 같은 어려운 일**까지 해낸다 (신약 개발, 논문 쓰기)

### 활용 시나리오 3가지

> **① Single Agent Deployment ② Multiple Agents Interaction ③ Human-Agent Interaction**

{: .참고 }
> **Deployment(배포·배치)** = 실제로 **현장에 투입해서 쓰는 것**

---

## 2. Single Agent 시나리오 ★★

<figure class="fig" id="fig-stairs"><svg viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Single Agent 3단계" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-stairs-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-stairs-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-stairs-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-stairs-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="20" y="140" width="200" height="66" rx="10" fill="#EAF0FA" stroke="#CBD9EE"/> <text x="120" y="166" font-size="14" fill="#1E3A6E">Task-oriented</text><text x="120" y="186" font-size="12" fill="#4A5568">시킨 일을 쪼개서 수행</text><text x="120" y="201" font-size="11.5" fill="#8A93A3">예: 연구계획서 초안</text> <rect x="240" y="95" width="200" height="111" rx="10" fill="#FBF0D8" stroke="#EBCF95"/> <text x="340" y="122" font-size="14" fill="#C77E16">Innovation-oriented</text><text x="340" y="142" font-size="12" fill="#4A5568">새 지식 · 과학적 발견</text><text x="340" y="158" font-size="11.5" fill="#8A93A3">예: 졸업 논문 (연구 공백 찾기)</text> <rect x="460" y="40" width="200" height="166" rx="10" fill="#E4F2EA" stroke="#BFE0CC"/> <text x="560" y="67" font-size="14" fill="#2E7D55">(Future) Lifecycle</text><text x="560" y="87" font-size="12" fill="#4A5568">장기 생존 · 스스로 능력 확장</text><text x="560" y="105" font-size="12" fill="#2E7D55">→ AGI의 최종 목표</text> <text x="120" y="60" font-size="13" fill="#C77E16">자율성 · 난이도 ↑</text> <path d="M60 76L420 40" stroke="#C77E16" stroke-width="2" fill="none" marker-end="url(#fig-stairs-b)"/> </svg><figcaption>Single Agent 배포 3단계: Task → Innovation → Lifecycle로 갈수록 스스로 하는 일이 커진다</figcaption></figure>

에이전트 **하나**를 쓰는 방식이 3단계로 나뉩니다.

{: .중요 }
> **Task → Innovation → Lifecycle** 순으로 **난이도와 자율성이 올라갑니다.**
> | 단계 | 비유 |
> |---|---|
> | Task-oriented | **시킨 일 잘하는 직원** |
> | Innovation-oriented | **새로운 걸 발견하는 연구원** |
> | Lifecycle-oriented | **스스로 성장하며 평생 일하는 존재** (미래) |

### 1) Task-oriented deployment (과업 지향)

- **사용자의 high-quality 자연어 지시를 받아 계획 → 하위 Task 분해 → 실행 → 환경과의 상호작용(피드백)**

**예시: "… 분야의 연구 계획서 초안 작성해줘"**

- … 분야의 **최근 연구 동향 파악**
- **연구 배경 제안 및 요약**
- **방법론 초안 작성**
- (교수님 취향에 맞추어) **산업 현장의 문제를 풀 수 있게 조정**

{: .참고 }
> 핵심은 **"사람이 시킨 구체적인 일"** 을 해낸다는 것. 목표가 명확하고, 에이전트는 그걸 **쪼개서 실행**합니다.

### 2) Innovation-oriented deployment (혁신 지향)

- **(단순 반복 업무가 아닌) 지식 창출, 과학적 발견, 창의적 문제 해결 등을 수행**

**예시: "… 분야로 졸업 논문 작성해줘"**

- **기존 연구 100편 비교** …
- **연구 공백 탐색 및 문제점 제시**
- **방법론 제안 및 실험 수행**
- **결과 제안 및 논문 작성**

{: .참고 }
> **연구 공백(research gap)** = 아직 **아무도 연구하지 않은 빈틈**. 이걸 찾아내는 건 **새로운 지식을 만드는 일**이라 Task-oriented보다 어렵습니다.
>
> **Task vs Innovation 차이**
>
> - 연구 **계획서 초안** (기존 정보 정리) → **Task**
> - 졸업 **논문** (새로운 발견, 실험) → **Innovation**

### 3) (Future) Lifecycle-oriented deployment (생애주기 지향)

- **장기적으로 살아남으며, 스스로 능력을 확장하는 에이전트**
- → **AGI의 최종 목표**

{: .참고 }
> **AGI (Artificial General Intelligence, 범용 인공지능)** = 특정 일만 하는 게 아니라 **사람처럼 무엇이든 할 수 있는** 인공지능.
> **Lifecycle** = 생애 주기. 한 번 쓰고 끝이 아니라 **계속 살아가면서 배우고 성장**하는 것. 아직은 **미래(Future)** 의 이야기입니다.

{: .시험 }
> **"Lifecycle-oriented deployment란?"** → **장기적으로 생존하면서 스스로 능력을 확장해 나가는 에이전트이며, AGI의 최종 목표.**

---

## 3. Multiple Agents 시나리오 ★★

### Motivation (동기) — "The Society of Mind"

**Marvin Minsky, "The Society of Mind" (1986)**

> **"지능은 통일된 중앙처리장치에서 비롯되는 것이 아닌, 특정 기능을 가진 수많은 작은 에이전트들의 상호작용에 의해 발생"**

{: .참고 }
> **쉽게:** 사람의 지능도 **하나의 똑똑한 덩어리가 아니라**, 보는 부분·듣는 부분·기억하는 부분·판단하는 부분… **작은 전문가들이 협력해서** 생긴다는 생각입니다.
> 그러니 AI도 **작은 에이전트 여럿이 협력**하면 더 똑똑해질 수 있다 → Multi-Agent의 사상적 근거.
>
> **마빈 민스키** = 인공지능의 아버지 중 한 명 (MIT)

{: .시험 }
> Multi-Agent의 근거: **Marvin Minsky, "The Society of Mind" (1986)** + 위 인용문. 이름·연도까지 나올 수 있습니다.

### 에이전트 간 상호작용의 특징

- **Natural Language 기반 통신**을 통해 에이전트 간 (**사람이 이해하기 쉬운 방향으로**) 상호작용

**상호작용 방식별 장단점 (슬라이드)**

| 방식 | 장점 | 단점 |
|---|---|---|
| **자유 토론형** | **자유로운 아이디어 생성** | **통제의 어려움** |
| **역할 분담형 (협력)** | **효율적이며, 책임 소재가 명확** | **역할에 대한 고정성** |
| **반박·토론형 (적대)** | **서로의 주장을 반박하며 개선 (게임이론)** | **잘못된 합의로의 수렴 가능성** |

{: .참고 }
> **하나씩 쉽게**
>
> - **자유 토론**: 브레인스토밍처럼 마음껏 의견 → 아이디어는 많지만 **배가 산으로** 갈 수 있음
> - **역할 분담**: "넌 기획, 넌 개발, 넌 테스트" → 효율적이고 **누구 잘못인지 명확**하지만, **정해진 역할 밖의 일**은 못 함
> - **반박·토론**: 서로 "그건 틀렸어" 하며 개선 → 질이 좋아지지만, **다 같이 틀린 답에 동의**해 버릴 수도 있음
>
> **게임이론** = 여러 참가자가 서로의 선택을 고려하며 최선을 찾는 이론. 여기선 "서로 견제하며 더 나은 답을 찾는다"는 뜻
> **잘못된 합의로의 수렴** = 토론하다 보니 **다 같이 틀린 결론에 의견이 모이는 것** (집단 착각)

{: .중요 }
> **"잘못된 합의로의 수렴 가능성"** 은 토론형 Multi-Agent의 핵심 위험으로 자주 묻습니다.

### 협력 유형 ① — Ordered Cooperative Engagement (순서 있는 협력): ChatDev ★

**"ChatDev: Communicative Agents for Software Development" (ACL 2024)**

- **각 Agent의 역할을 분해하여 소프트웨어 개발 수행**
- **Design → Coding → Testing 단계를 체인화**

```
[CEO 에이전트] → [CTO 에이전트] → [프로그래머 에이전트] → [테스터 에이전트]
    Design      →      Coding      →         Testing
```

{: .참고 }
> **가상 소프트웨어 회사**입니다. 각 AI가 **직급과 역할**을 맡아 **순서대로(체인)** 일을 넘깁니다.
> **체인화** = 사슬처럼 **앞 단계 결과가 다음 단계로** 이어지게 만드는 것

### 협력 유형 ② — Adversarial Interactions (적대적 상호작용): ChatEval ★

**"ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate" (2023)**

- **여러 Agents가 서로 토론을 하며 생성된 응답의 품질을 평가**
- **논쟁 기반 프레임워크**

{: .참고 }
> **심사위원 여러 명이 토론해서 점수 매기기**. 한 명이 채점하면 편향될 수 있지만, **여러 AI가 "이 답은 이래서 좋다/나쁘다" 논쟁**하면 더 공정한 평가가 나옵니다.
> **Adversarial(적대적)** = 서로 **반대 입장**에서 공격·반박하는

{: .시험 }
> | | ChatDev | ChatEval |
> |---|---|---|
> | 유형 | **Ordered Cooperative Engagement** (협력형) | **Adversarial Interactions** (적대형) |
> | 하는 일 | **소프트웨어 개발** | **응답 품질 평가** |
> | 방식 | **Design → Coding → Testing 체인** | **Multi-Agent Debate (토론)** |

---

## 4. Human-Agent Interaction (인간-에이전트 상호작용) ★★

<figure class="fig" id="fig-human"><svg viewBox="0 0 680 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="인간과 에이전트 관계" font-weight="700" text-anchor="middle" font-size="14" fill="#16243F"><defs><marker id="fig-human-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1E3A6E"/></marker><marker id="fig-human-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C77E16"/></marker><marker id="fig-human-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#2E7D55"/></marker><marker id="fig-human-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#C0463F"/></marker></defs> <rect x="8" y="8" width="324" height="184" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="170" y="34" font-size="14" fill="#1E3A6E">Instructor-Executor (현재 기본)</text> <text x="170" y="82" font-size="34">🧑</text> <path d="M170 92V128" stroke="#1E3A6E" stroke-width="2.2" marker-end="url(#fig-human-a)"/> <text x="180" y="116" font-size="12" fill="#4A5568" text-anchor="start">지시 · 정량/정성 피드백</text> <text x="170" y="164" font-size="30">🤖</text> <text x="170" y="184" font-size="12" fill="#8A93A3">상사 - 부하</text> <rect x="348" y="8" width="324" height="184" rx="14" fill="#fff" stroke="#E7E2D7"/> <text x="510" y="34" font-size="14" fill="#2E7D55">Equal Partnership</text> <text x="430" y="120" font-size="34">🧑</text><text x="590" y="120" font-size="34">🤖</text> <path d="M466 108H554" stroke="#2E7D55" stroke-width="2.2" marker-end="url(#fig-human-c)" marker-start="url(#fig-human-c)"/> <text x="510" y="96" font-size="12" fill="#4A5568">공동 목표 · 공감</text> <text x="510" y="184" font-size="12" fill="#8A93A3">동료 - 동료 (대칭 관계)</text> </svg><figcaption>지금은 사람이 시키고 AI가 하는 관계, 앞으로는 같이 목표를 세우는 동료 관계로</figcaption></figure>

**인간과 Agent는 어떻게 협력해야 하는가?**

{: .시험 }
> 두 패러다임의 이름과 차이를 구분하세요.

### 1) Instructor-Executor Paradigm (지시자-실행자)

- **인간이 지시하고 에이전트가 수행** (**현재 에이전트의 기본 모드**)
- (인간 → 로봇) **지속적인 정량/정성 피드백 제공**

{: .참고 }
> - **Instructor** = 지시하는 사람, **Executor** = 실행하는 쪽
> - **정량 피드백** = 숫자로 주는 평가 ("7점")
> - **정성 피드백** = 말로 주는 평가 ("좀 더 짧게 써줘")

### 2) Equal Partnership Paradigm (동등한 파트너십)

- **에이전트가 사회적 주체로서, 인간과 대칭 관계 유지**
- **Empathetic Communicator** — **공감하는 대화 상대**
- **Human-level Participant** — **공동 목표를 세우고 협력** (사람 수준의 참여자)

{: .참고 }
> **비유**
> | | Instructor-Executor | Equal Partnership |
> |---|---|---|
> | 관계 | **상사 - 부하** | **동료 - 동료** |
> | 누가 목표를 정하나 | 사람 | **같이** |
> | 현재 | ✅ 지금 대부분 | 앞으로의 방향 |
>
> **대칭 관계** = 어느 한쪽이 위가 아니라 **동등한** 관계

---

## 이 장 정리

| 시나리오 | 세부 | 핵심 |
|---|---|---|
| **방향성 3가지** | 반복 업무 해방 / 지침 없이 독립 해결 / 최첨단 과학 | |
| **Single Agent** | **Task-oriented** | 지시 → 계획 → 분해 → 실행 → 피드백 (연구계획서) |
| | **Innovation-oriented** | 지식 창출, 과학적 발견 (졸업논문) |
| | **Lifecycle-oriented** (Future) | 장기 생존, 스스로 능력 확장 → **AGI** |
| **Multiple Agents** | 근거 | **Minsky, The Society of Mind (1986)** |
| | 장단점 | 자유↔통제 어려움 / 효율·책임 명확↔역할 고정 / 반박 개선↔**잘못된 합의** |
| | **ChatDev** | 협력형, Design→Coding→Testing |
| | **ChatEval** | 적대형, Multi-Agent Debate |
| **Human-Agent** | **Instructor-Executor** | 인간 지시, 에이전트 수행 (**현재 기본**) |
| | **Equal Partnership** | 대칭 관계, Empathetic Communicator, Human-level Participant |
