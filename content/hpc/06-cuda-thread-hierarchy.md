# 6. CUDA 스레드 계층

## 스레드 계층 구조 (thread hierarchy)

{: .시험 }
> **계층 구조와 각 계층을 처리하는 하드웨어의 대응**이 핵심.
>
> | 소프트웨어 계층 | 처리하는 하드웨어 |
> |---|---|
> | **스레드(thread)** | **CUDA core** |
> | **블록(block)** | **Streaming Multiprocessor (SM)** |
> | **그리드(grid)** | **GPU (device)** |
>
> 계층 구성: **스레드(thread) → 워프(warp) → 블록(block) → 그리드(grid)**
>
> 커널이 호출되면 스레드·블록·그리드가 생성되고, **블록 내의 스레드들은 워프(연속된 32개의 스레드) 단위로 실행**된다.

<figure class="diagram">
<svg viewBox="0 0 740 320" role="img" aria-label="그리드는 블록들의 집합이고 블록은 스레드들의 집합이며, 그리드는 GPU가, 블록은 SM이, 스레드는 CUDA 코어가 처리한다">
  <defs>
    <marker id="hier-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <text x="170" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="currentColor">Grid (그리드)</text>
  <rect x="20" y="36" width="300" height="200" rx="8" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.5"/>

  <rect x="34"  y="50"  width="83" height="80" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="128" y="50"  width="83" height="80" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="222" y="50"  width="83" height="80" rx="4" fill="var(--accent)" fill-opacity="0.14" stroke="var(--accent)" stroke-width="2"/>
  <rect x="34"  y="141" width="83" height="80" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="128" y="141" width="83" height="80" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="222" y="141" width="83" height="80" rx="4" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>

  <text x="75"  y="94"  text-anchor="middle" font-size="12" fill="currentColor">Block</text>
  <text x="169" y="94"  text-anchor="middle" font-size="12" fill="currentColor">Block</text>
  <text x="263" y="94"  text-anchor="middle" font-size="12" font-weight="700" fill="var(--accent)">Block</text>
  <text x="75"  y="185" text-anchor="middle" font-size="12" fill="currentColor">Block</text>
  <text x="169" y="185" text-anchor="middle" font-size="12" fill="currentColor">Block</text>
  <text x="263" y="185" text-anchor="middle" font-size="12" fill="currentColor">Block</text>

  <line x1="307" y1="90" x2="412" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#hier-arrow)"/>
  <text x="359" y="80" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.75">블록 1개 확대</text>

  <text x="570" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="currentColor">Block (블록) 내부</text>
  <rect x="420" y="36" width="300" height="200" rx="8" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.5"/>

  <rect x="434" y="50"  width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="504" y="50"  width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="574" y="50"  width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="644" y="50"  width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="434" y="111" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="504" y="111" width="60" height="50" rx="3" fill="var(--accent)" fill-opacity="0.14" stroke="var(--accent)" stroke-width="2"/>
  <rect x="574" y="111" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="644" y="111" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="434" y="172" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="504" y="172" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="574" y="172" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>
  <rect x="644" y="172" width="60" height="50" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45"/>

  <text x="464" y="80"  text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="534" y="80"  text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="604" y="80"  text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="674" y="80"  text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="464" y="141" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="534" y="141" text-anchor="middle" font-size="11" font-weight="700" fill="var(--accent)">스레드</text>
  <text x="604" y="141" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="674" y="141" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="464" y="202" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="534" y="202" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="604" y="202" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>
  <text x="674" y="202" text-anchor="middle" font-size="11" fill="currentColor">스레드</text>

  <text x="170" y="258" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">블록들의 집합</text>
  <text x="570" y="258" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor">스레드들의 집합</text>
  <text x="170" y="280" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.75">GPU (device) 가 처리</text>
  <text x="570" y="280" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.75">SM (Streaming Multiprocessor) 가 처리</text>
  <text x="170" y="302" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.75">커널 호출 1번 = 그리드 1개</text>
  <text x="570" y="302" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.75">스레드 1개 = CUDA core 1개가 처리</text>
</svg>
<figcaption>
그리드 안에 블록이, 블록 안에 스레드가 들어 있는 <strong>3단 포함 관계</strong>다. 각 계층을 처리하는 하드웨어가 하나씩 대응된다 — 그리드는 GPU 전체, 블록 하나는 SM 하나, 스레드 하나는 CUDA 코어 하나. 커널을 한 번 호출하면 이 구조 전체가 한 세트 생성된다.
</figcaption>
</figure>

---

## 스레드 (thread)

- 각 스레드는 **하나의 CUDA 코어**를 사용하여 **독립적으로 커널 수행**
- 코어는 스레드 간의 **문맥 교환(context switching)** 을 통해 여러 스레드를 처리
  → 여러 스레드가 동시에 실행되는 것처럼 보임

{: .중요 }
> **CUDA 스레드 vs CPU 스레드 — 문맥 교환 overhead 차이**
>
> | | **CUDA(GPU) 스레드** | **CPU 스레드** |
> |---|---|---|
> | 레지스터 | **자신만의 레지스터를 사용** | **자신만의 레지스터를 갖지 않음** |
> | 문맥 교환 overhead | **없음** | **큼** |
> | 결론 | **코어 수보다 많은 스레드를 써도 성능 저하가 거의 없음** | **코어 수보다 많은 스레드를 쓰면 성능 저하가 큼** |

---

## 워프 (warp)

- **연속된 32개의 스레드**로 구성됨
- **SIMT (Single Instruction Multiple Thread)**: 하나의 명령어를 통해 **연속된 32개의 스레드(워프)** 가 여러 데이터를 동시에 처리

{: .시험 }
> **스레드의 연속성은 `blockDim.x` → `blockDim.y` → `blockDim.z` 차원 순으로 결정된다.**
>
> | 조건 | 하나의 워프를 구성하는 스레드 |
> |---|---|
> | `blockDim.x ≥ 32` 이고 `blockDim.y ≥ 32` | **(0,0,0) ~ (31,0,0)** |
> | `blockDim.x = 1` 이고 `blockDim.y ≥ 32` | **(0,0,0) ~ (0,31,0)** |
>
> 즉 **x축을 먼저 다 채우고 y축으로 넘어간다.**

<figure class="diagram">
<svg viewBox="0 0 740 300" role="img" aria-label="블록 안의 스레드는 threadIdx.x 방향으로 먼저 번호가 매겨지고, x축을 다 채운 뒤 threadIdx.y 방향으로 넘어간다. 연속된 32개가 워프 하나를 이룬다">
  <defs>
    <marker id="warp-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <text x="340" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="currentColor">blockDim = (8, 4, 1) — 블록 안의 스레드 32개</text>

  <line x1="80" y1="38" x2="600" y2="38" stroke="currentColor" stroke-width="1.5" marker-end="url(#warp-arrow)"/>
  <text x="341" y="32" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.75">threadIdx.x 증가</text>
  <line x1="46" y1="66" x2="46" y2="242" stroke="currentColor" stroke-width="1.5" marker-end="url(#warp-arrow)"/>
  <text transform="rotate(-90 28 155)" x="28" y="155" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.75">threadIdx.y 증가</text>

  <rect x="60" y="46" width="562" height="218" rx="8" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.5"/>

  <g fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45">
    <rect x="80"  y="66" width="60" height="40" rx="3"/><rect x="146" y="66" width="60" height="40" rx="3"/>
    <rect x="212" y="66" width="60" height="40" rx="3"/><rect x="278" y="66" width="60" height="40" rx="3"/>
    <rect x="344" y="66" width="60" height="40" rx="3"/><rect x="410" y="66" width="60" height="40" rx="3"/>
    <rect x="476" y="66" width="60" height="40" rx="3"/><rect x="542" y="66" width="60" height="40" rx="3"/>
    <rect x="80"  y="112" width="60" height="40" rx="3"/><rect x="146" y="112" width="60" height="40" rx="3"/>
    <rect x="212" y="112" width="60" height="40" rx="3"/><rect x="278" y="112" width="60" height="40" rx="3"/>
    <rect x="344" y="112" width="60" height="40" rx="3"/><rect x="410" y="112" width="60" height="40" rx="3"/>
    <rect x="476" y="112" width="60" height="40" rx="3"/><rect x="542" y="112" width="60" height="40" rx="3"/>
    <rect x="80"  y="158" width="60" height="40" rx="3"/><rect x="146" y="158" width="60" height="40" rx="3"/>
    <rect x="212" y="158" width="60" height="40" rx="3"/><rect x="278" y="158" width="60" height="40" rx="3"/>
    <rect x="344" y="158" width="60" height="40" rx="3"/><rect x="410" y="158" width="60" height="40" rx="3"/>
    <rect x="476" y="158" width="60" height="40" rx="3"/><rect x="542" y="158" width="60" height="40" rx="3"/>
    <rect x="80"  y="204" width="60" height="40" rx="3"/><rect x="146" y="204" width="60" height="40" rx="3"/>
    <rect x="212" y="204" width="60" height="40" rx="3"/><rect x="278" y="204" width="60" height="40" rx="3"/>
    <rect x="344" y="204" width="60" height="40" rx="3"/><rect x="410" y="204" width="60" height="40" rx="3"/>
    <rect x="476" y="204" width="60" height="40" rx="3"/><rect x="542" y="204" width="60" height="40" rx="3"/>
  </g>

  <g text-anchor="middle" font-size="12" fill="currentColor">
    <text x="110" y="91">0</text><text x="176" y="91">1</text><text x="242" y="91">2</text><text x="308" y="91">3</text>
    <text x="374" y="91">4</text><text x="440" y="91">5</text><text x="506" y="91">6</text><text x="572" y="91">7</text>
    <text x="110" y="137">8</text><text x="176" y="137">9</text><text x="242" y="137">10</text><text x="308" y="137">11</text>
    <text x="374" y="137">12</text><text x="440" y="137">13</text><text x="506" y="137">14</text><text x="572" y="137">15</text>
    <text x="110" y="183">16</text><text x="176" y="183">17</text><text x="242" y="183">18</text><text x="308" y="183">19</text>
    <text x="374" y="183">20</text><text x="440" y="183">21</text><text x="506" y="183">22</text><text x="572" y="183">23</text>
    <text x="110" y="229">24</text><text x="176" y="229">25</text><text x="242" y="229">26</text><text x="308" y="229">27</text>
    <text x="374" y="229">28</text><text x="440" y="229">29</text><text x="506" y="229">30</text><text x="572" y="229">31</text>
  </g>

  <path d="M626,66 H636 V244 H626" fill="none" stroke="var(--accent)" stroke-width="2"/>
  <text x="648" y="148" font-size="12" font-weight="700" fill="var(--accent)">연속된 32개</text>
  <text x="648" y="166" font-size="12" font-weight="700" fill="var(--accent)">= 워프 1개</text>

  <text x="340" y="288" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.75">blockDim.x = 1 이면 x축에 1개뿐이므로 y축으로 32개 → (0,0,0) ~ (0,31,0) 이 한 워프</text>
</svg>
<figcaption>
스레드 번호는 <strong>x축을 끝까지 채운 뒤 y축으로, 그 다음 z축으로</strong> 이어진다. 이 순서로 셌을 때 <strong>연속된 32개</strong>가 워프 하나다. 그래서 같은 32개 스레드라도 블록 모양에 따라 어느 스레드들이 한 워프가 되는지가 달라진다.
</figcaption>
</figure>

{: .참고 }
> 비교: **CPU의 SIMD**는 하나의 명령어로 **전용 레지스터에 있는 여러 데이터(벡터)** 를 동시에 처리한다.
> → [3. GPGPU 및 병렬처리](03-gpgpu-parallel.html)의 SIMT vs SIMD 표 참고

---

## 블록 (block)

- **스레드들의 집합**
- **최대 3차원**까지 표현 가능
- **Streaming Multiprocessor(SM)** 에 의해 처리됨
- SM 내부의 **워프 스케줄러**에 의해 블록 내의 스레드들이 **워프 단위로 실행**됨

## 그리드 (grid)

- **블록들의 집합**
- **최대 3차원**까지 표현 가능
- **GPU(device)** 에 의해 처리됨

---

## 스레드 계층 표현을 위한 내장 변수

{: .시험 }
> **4개 내장 변수의 의미를 정확히 구분할 것.** 이름이 비슷해서 가장 많이 틀린다.
>
> | 변수 | 의미 |
> |---|---|
> | **`gridDim`** | **그리드 내의 각 차원에 대한 블록 수** |
> | **`blockIdx`** | **그리드 내의 블록 번호(인덱스)** |
> | **`blockDim`** | **블록 내의 각 차원에 대한 스레드 수** |
> | **`threadIdx`** | **블록 내의 스레드 번호(인덱스)** |
>
> 외우는 법: **`Dim`은 개수(크기), `Idx`는 번호.** **`grid-`는 블록에 대한 것, `block-`은 스레드에 대한 것.**

<figure class="diagram">
<svg viewBox="0 0 740 310" role="img" aria-label="gridDim은 그리드 안의 블록 개수이고 blockIdx는 그 블록의 번호이며, blockDim은 블록 안의 스레드 개수이고 threadIdx는 그 스레드의 번호다">
  <text x="170" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="currentColor">gridDim = (3, 2, 1)</text>
  <text x="170" y="38" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.75">각 칸 = 블록 1개, 칸 안의 숫자 = blockIdx (x, y)</text>
  <rect x="20" y="50" width="300" height="170" rx="8" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.5"/>

  <g fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45">
    <rect x="34"  y="64"  width="83" height="65" rx="4"/>
    <rect x="128" y="64"  width="83" height="65" rx="4"/>
    <rect x="222" y="64"  width="83" height="65" rx="4"/>
    <rect x="34"  y="140" width="83" height="65" rx="4"/>
    <rect x="128" y="140" width="83" height="65" rx="4"/>
  </g>
  <rect x="222" y="140" width="83" height="65" rx="4" fill="var(--accent)" fill-opacity="0.14" stroke="var(--accent)" stroke-width="2"/>

  <g text-anchor="middle" font-size="13" fill="currentColor">
    <text x="75"  y="101">(0, 0)</text><text x="169" y="101">(1, 0)</text><text x="263" y="101">(2, 0)</text>
    <text x="75"  y="177">(0, 1)</text><text x="169" y="177">(1, 1)</text>
  </g>
  <text x="263" y="177" text-anchor="middle" font-size="13" font-weight="700" fill="var(--accent)">(2, 1)</text>

  <line x1="370" y1="50" x2="370" y2="220" stroke="currentColor" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="5 5"/>

  <text x="570" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="currentColor">blockDim = (4, 3, 1)</text>
  <text x="570" y="38" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.75">각 칸 = 스레드 1개, 칸 안의 숫자 = threadIdx (x, y)</text>
  <rect x="420" y="50" width="300" height="170" rx="8" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.5"/>

  <g fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.45">
    <rect x="434" y="64"  width="60" height="40" rx="3"/><rect x="504" y="64"  width="60" height="40" rx="3"/>
    <rect x="574" y="64"  width="60" height="40" rx="3"/><rect x="644" y="64"  width="60" height="40" rx="3"/>
    <rect x="434" y="114" width="60" height="40" rx="3"/><rect x="504" y="114" width="60" height="40" rx="3"/>
    <rect x="574" y="114" width="60" height="40" rx="3"/><rect x="644" y="114" width="60" height="40" rx="3"/>
    <rect x="434" y="164" width="60" height="40" rx="3"/><rect x="504" y="164" width="60" height="40" rx="3"/>
    <rect x="644" y="164" width="60" height="40" rx="3"/>
  </g>
  <rect x="574" y="164" width="60" height="40" rx="3" fill="var(--accent)" fill-opacity="0.14" stroke="var(--accent)" stroke-width="2"/>

  <g text-anchor="middle" font-size="12" fill="currentColor">
    <text x="464" y="88">(0, 0)</text><text x="534" y="88">(1, 0)</text><text x="604" y="88">(2, 0)</text><text x="674" y="88">(3, 0)</text>
    <text x="464" y="138">(0, 1)</text><text x="534" y="138">(1, 1)</text><text x="604" y="138">(2, 1)</text><text x="674" y="138">(3, 1)</text>
    <text x="464" y="188">(0, 2)</text><text x="534" y="188">(1, 2)</text><text x="674" y="188">(3, 2)</text>
  </g>
  <text x="604" y="188" text-anchor="middle" font-size="12" font-weight="700" fill="var(--accent)">(2, 2)</text>

  <text x="170" y="248" text-anchor="middle" font-size="12.5" fill="currentColor"><tspan font-weight="700">gridDim</tspan> = 블록이 몇 개인가 (3 × 2 = 6개)</text>
  <text x="570" y="248" text-anchor="middle" font-size="12.5" fill="currentColor"><tspan font-weight="700">blockDim</tspan> = 스레드가 몇 개인가 (4 × 3 = 12개)</text>
  <text x="170" y="270" text-anchor="middle" font-size="12.5" fill="var(--accent)"><tspan font-weight="700">blockIdx</tspan> = 그 블록이 몇 번인가</text>
  <text x="570" y="270" text-anchor="middle" font-size="12.5" fill="var(--accent)"><tspan font-weight="700">threadIdx</tspan> = 그 스레드가 몇 번인가</text>

  <text x="370" y="298" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.8">상자의 크기 = Dim · 칸의 이름 = Idx  /  grid- 는 블록을, block- 은 스레드를 가리킨다</text>
</svg>
<figcaption>
왼쪽은 <strong>그리드를 블록 단위로</strong> 쪼갠 것, 오른쪽은 <strong>블록 하나를 스레드 단위로</strong> 쪼갠 것이다. 두 그림의 생김새가 똑같다는 점이 핵심 — 같은 "상자와 칸" 구조가 한 계층 아래에서 반복될 뿐이다. 그래서 변수도 네 개가 아니라 <strong>(개수, 번호) 두 쌍</strong>이다.
</figcaption>
</figure>

### gridDim

그리드의 **차원 크기 정보**를 포함하는 구조체. `gridDim.x`, `gridDim.y`, `gridDim.z`

| 항목 | 최대값 |
|---|---|
| **`gridDim.x`** | **2³¹ − 1** (거의 무제한) |
| **`gridDim.y`, `gridDim.z`** | **65535** |

예: `gridDim = (3,2,1)` → 한 그리드 내에 **6개의 블록**

### blockDim

블록의 **차원 크기 정보**를 포함하는 구조체. `blockDim.x`, `blockDim.y`, `blockDim.z`

{: .중요 }
> | 항목 | 최대값 |
> |---|---|
> | **`blockDim.x`, `blockDim.y`** | **1024** |
> | **`blockDim.z`** | **64** |
> | **한 블록 내의 최대 스레드 수** | **1024** (`blockDim.x × blockDim.y × blockDim.z ≤ 1024`) |
>
> **블록당 스레드 수를 너무 작거나 크게 설정하면 CUDA 프로그램 성능 저하를 초래**한다.

예: `blockDim = (4,3,1)` → 한 블록 내에 **12개의 스레드**

### blockIdx / threadIdx

- **`blockIdx`**: 그리드 내의 블록 번호. `blockIdx.x`, `blockIdx.y`, `blockIdx.z`
- **`threadIdx`**: 블록 내의 스레드 번호. `threadIdx.x`, `threadIdx.y`, `threadIdx.z`

{: .주의 }
> **서로 다른 블록에서 동일한 `threadIdx`가 존재한다.**
> `threadIdx`는 **블록 내에서만** 유일한 번호이므로, 전체 데이터를 다루려면 **전역 번호(global ID)** 를 따로 계산해야 한다.
> → [7. 스레드 레이아웃과 인덱싱](07-cuda-thread-indexing.html)

---

## Compute capability 상의 제약 정리

| 항목 | 값 |
|---|---|
| Maximum dimensionality of grid of thread blocks | **3** |
| Maximum **x**-dimension of a grid of thread blocks | **2³¹ − 1** |
| Maximum **y-** or **z**-dimension of a grid of thread blocks | **65535** |
| Maximum dimensionality of thread block | **3** |
| Maximum **x-** or **y**-dimension of a block | **1024** |
| Maximum **z**-dimension of a block | **64** |
| **Maximum number of threads per block** | **1024** |
| **Warp size** | **32** |

---

## CUDA 스레드 레이아웃 (thread layout)

**스레드 레이아웃**: **스레드 배치 형태**를 정의한 것

- 커널의 **성능 특성과 GPU 자원(레지스터와 공유 메모리)** 등을 고려하여 정해야 함
- 커널 호출 시 **그리드 차원 크기**(그리드 내의 블록 수)와 **블록 차원 크기**(블록 내의 스레드 수)로 설정

```
kernel <<< 그리드 차원 크기, 블록 차원 크기 >>> ();
```

| 호출 | 의미 |
|---|---|
| `kernel <<< 1, n >>> ();` | **1개의 블록**과 **n개의 스레드** 생성 |
| `kernel <<< n, m >>> ();` | **n개의 블록**과 (블록당) **m개의 스레드** 생성 |

### dim3 자료형

**`dim3`**: CUDA에서 제공하는 자료형으로 3차원 크기를 설정

```c
dim3 dimGrid(3, 2, 1);
dim3 dimBlock(6, 4, 2);
kernel <<< dimGrid, dimBlock >>> ();
// 3 x 2 개의 블록, 각 블록에 6 x 4 x 2 개의 스레드 생성
```

{: .중요 }
> **차원 크기가 1이면 생략 가능**하다.
>
> ```c
> dim3 dimGrid(4);     // dim3 dimGrid(4,1,1); 과 동일
> dim3 dimBlock(8);    // dim3 dimBlock(8,1,1); 과 동일
> kernel <<< dimGrid, dimBlock >>> ();
> ```
>
> 그리고 `kernel <<< dimGrid, dimBlock >>>` 는 `kernel <<< 4, 8 >>>` 와 동일하다.

---

## 내장 변수 확인 예제 (lec04_01.cu)

```c
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__global__ void checkIndex(void)
{
    printf("gridDim:(%d, %d, %d) blockDim:(%d, %d, %d) "
           "blockIdx:(%d, %d, %d) threadIdx:(%d, %d, %d)\n",
           gridDim.x,  gridDim.y,  gridDim.z,
           blockDim.x, blockDim.y, blockDim.z,
           blockIdx.x, blockIdx.y, blockIdx.z,
           threadIdx.x, threadIdx.y, threadIdx.z);
}

int main(void)
{
    dim3 dimGrid(2, 1, 1);                      // dim3 dimGrid(2); 와 동일
    dim3 dimBlock(3, 1, 1);                     // dim3 dimBlock(3); 와 동일

    checkIndex <<< dimGrid, dimBlock >>> ();    // checkIndex <<< 2, 3 >>> (); 와 동일
    cudaDeviceSynchronize();
}
```

### 실행 결과

```
gridDim:(2, 1, 1) blockDim:(3, 1, 1) blockIdx:(1, 0, 0) threadIdx:(0, 0, 0)
gridDim:(2, 1, 1) blockDim:(3, 1, 1) blockIdx:(1, 0, 0) threadIdx:(1, 0, 0)
gridDim:(2, 1, 1) blockDim:(3, 1, 1) blockIdx:(1, 0, 0) threadIdx:(2, 0, 0)
gridDim:(2, 1, 1) blockDim:(3, 1, 1) blockIdx:(0, 0, 0) threadIdx:(0, 0, 0)
gridDim:(2, 1, 1) blockDim:(3, 1, 1) blockIdx:(0, 0, 0) threadIdx:(1, 0, 0)
gridDim:(2, 1, 1) blockDim:(3, 1, 1) blockIdx:(0, 0, 0) threadIdx:(2, 0, 0)
```

{: .시험 }
> 이 출력에서 읽어야 할 두 가지
>
> 1. **서로 다른 블록(`blockIdx` 0과 1)에서 동일한 `threadIdx`(0,1,2)가 존재**한다.
> 2. **블록의 실행 순서는 보장되지 않는다.** (블록 1이 블록 0보다 먼저 출력됨)
