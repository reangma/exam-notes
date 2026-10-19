#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
지능형 소프트웨어 노트(content/isw/*.md)를 "한 파일로 끝내는" 단일 페이지로 만든다.
결과물: isw/onepage.html

사용법:
    python tools/build_isw_onepage.py

장별 노트(build.py 결과)와 내용은 같고, 디자인만 단일 페이지용이다.
마크다운을 고친 뒤 build.py 와 이 스크립트를 둘 다 다시 돌리면 된다.
"""

import html as htmllib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import markdown  # noqa: E402
from build import expand_callouts  # noqa: E402

SRC = ROOT / "content" / "isw"
OUT = ROOT / "isw" / "onepage.html"

# (파일, 섹션 id, 번호표, 목차 칩 이름)
CHAPTERS = [
    ("00-math-basics.md",           "math", "기초", "기초 수학"),
    ("01-course-overview.md",       "ch1",  "01",   "1 개요·역사"),
    ("02-embedding.md",             "ch2",  "02",   "2 임베딩"),
    ("03-transformer.md",           "ch3",  "03",   "3 트랜스포머"),
    ("04-llm-gpt.md",               "ch4",  "04",   "4 LLM·GPT"),
    ("05-adaptation-tuning.md",     "ch5",  "05",   "5 튜닝"),
    ("06-prompt-engineering.md",    "ch6",  "06",   "6 프롬프트"),
    ("07-ai-agent.md",              "ch7",  "07",   "7 에이전트"),
    ("08-react-tool.md",            "ch8",  "08",   "8 ReAct·도구"),
    ("09-agent-structure.md",       "ch9",  "09",   "9 에이전트 구조"),
    ("10-agent-practice.md",        "ch10", "10",   "10 활용"),
    ("11-cognitive-architecture.md","ch11", "11",   "11 CoALA"),
    ("12-agent-architectures.md",   "ch12", "12",   "12 아키텍처"),
    ("97-compare.md",               "compare","비교", "헷갈리는 것"),
    ("99-cheatsheet.md",            "cheat","요약", "치트시트"),
    ("98-exam-questions.md",        "quiz", "문제", "예상문제"),
]

# 장별 노트 사이의 링크(02-embedding.html 등)를 한 페이지 안의 앵커로 바꾸기 위한 표
LINK_MAP = {f: sid for f, sid, _, _ in CHAPTERS}
LINK_MAP["00-glossary.md"] = "glossary"

CALLOUT_TAGS = {
    "callout-exam": "시험 포인트",
    "callout-note": "🐣 쉽게 말하면",
    "callout-important": "❗ 헷갈리지 말기",
    "callout-warning": "⚠ 슬라이드 함정",
}


def inline_md(s: str) -> str:
    s = htmllib.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def build_glossary():
    """content/isw/00-glossary.md (정의 목록) → 검색되는 용어 카드."""
    text = (SRC / "00-glossary.md").read_text(encoding="utf-8")
    out, count = [], 0
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        title, _, rest = block.partition("\n")
        cards = []
        for m in re.finditer(r"^\*\*(.+?)\*\*(?: · (.+))?\n((?:: .*\n?)+)", rest, re.M):
            term, en = m.group(1), m.group(2)
            defs = [d[2:] for d in m.group(3).strip().splitlines()]
            ex = next((d[2:].strip() for d in defs[1:] if d.startswith("💡")), "")
            badge = f' <span class="tb">{inline_md(en)}</span>' if en else ""
            ex_html = f'<span class="ex">{inline_md(ex)}</span>' if ex else ""
            cards.append(
                f'<div class="term"><div class="t">{inline_md(term)}{badge}</div>'
                f"<p>{inline_md(defs[0])}{ex_html}</p></div>"
            )
            count += 1
        out.append(f'<div class="gsec"><h3>{title.strip()}</h3><div class="terms">{"".join(cards)}</div></div>')
    return "\n".join(out), count

# ---------------------------------------------------------------------------
# 마크다운 장 → 섹션 HTML
# ---------------------------------------------------------------------------

def md_to_html(text: str) -> str:
    md = markdown.Markdown(extensions=["extra", "sane_lists"])
    return md.convert(expand_callouts(text))


def rewrite_links(h: str) -> str:
    def repl(m):
        target = m.group(1)
        sid = LINK_MAP.get(target.replace(".html", ".md"))
        return f'href="#{sid}"' if sid else m.group(0)

    return re.sub(r'href="([0-9]{2}-[a-z0-9-]+\.html)(?:#[^"]*)?"', repl, h)


def restyle(h: str) -> str:
    # 제목 한 단계씩 내리기 (## → h3, ### → h4 …) : 섹션 제목이 h2 이므로
    for n in (5, 4, 3, 2):
        h = re.sub(rf"<(/?)h{n}([ >])", rf"<\1h{n + 1}\2", h)
    h = h.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    for cls, tag in CALLOUT_TAGS.items():
        h = re.sub(
            rf'(<div class="callout {cls}">)\s*<p class="callout-title">[^<]*</p>',
            rf'\1<span class="tag">{tag}</span>',
            h,
        )
    return rewrite_links(h)



def quizify(h: str) -> str:
    """98-exam-questions 의 'Q + 정답 보기' 묶음을 문제 카드로 감싼다."""
    pattern = re.compile(
        r"<p><strong>([MBQ]\d+\.)</strong>(.*?)</p>\s*(<ol>.*?</ol>)?\s*<details>\s*<summary>정답 보기</summary>(.*?)</details>",
        re.S,
    )
    return pattern.sub(
        r'<div class="q"><p class="qn"><span class="qno">\1</span>\2</p>\3'
        r'<details class="ans"><summary>정답 보기</summary><div class="body">\4</div></details></div>',
        h,
    )


def split_title(md_text: str):
    m = re.match(r"#\s+(.+)\n", md_text)
    title = m.group(1).strip() if m else ""
    body = md_text[m.end():] if m else md_text
    title = re.sub(r"^\d+\.\s*", "", title)  # "2. 자연어 임베딩" → "자연어 임베딩"
    en = ""
    pm = re.match(r"(.+?)\s*\(([^)]*)\)\s*$", title)
    if pm and re.search(r"[A-Za-z]", pm.group(2)):
        title, en = pm.group(1), pm.group(2)
    return title, en, body


def build_section(fname, sid, num, chip):
    raw = (SRC / fname).read_text(encoding="utf-8")
    title, en, body = split_title(raw)
    h = restyle(md_to_html(body))
    if sid == "quiz":
        h = quizify(h)
    en_html = f' <span class="en">{htmllib.escape(en)}</span>' if en else ""
    extra = ""
    if sid == "quiz":
        extra = '<div class="quizbar"><button type="button" id="openall">정답 전부 펼치기</button><button type="button" id="closeall">전부 접기</button></div>'
    return (
        f'<section id="{sid}">'
        f'<div class="sec-label"><span class="sec-num">{num}</span></div>'
        f"<h2>{htmllib.escape(title)}{en_html}</h2>{extra}\n{h}\n</section>"
    )


# ---------------------------------------------------------------------------
# 페이지 조립
# ---------------------------------------------------------------------------

CSS = """
:root{
  --paper:#FBFAF7; --surface:#FFFFFF;
  --ink:#16243F; --ink-soft:#4A5568; --muted:#8A93A3;
  --navy:#1E3A6E; --navy-deep:#142A52; --navy-tint:#EAF0FA; --navy-line:#CBD9EE;
  --amber:#C77E16; --amber-soft:#FBF0D8; --amber-line:#EBCF95;
  --coral:#C0463F; --coral-soft:#FBE9E7;
  --green:#2E7D55; --green-soft:#E4F2EA;
  --violet:#6B3FA0; --violet-soft:#F3EEFB;
  --line:#E7E2D7; --line-soft:#F0ECE3;
  --radius:14px;
  --font:'Pretendard','Pretendard Variable',-apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Malgun Gothic',sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0; background:var(--paper); color:var(--ink); font-family:var(--font); line-height:1.72; font-size:17px; -webkit-font-smoothing:antialiased; letter-spacing:-0.01em}
.wrap{max-width:920px; margin:0 auto; padding:0 22px}
a{color:var(--navy)}

header.hero{background:linear-gradient(160deg,var(--navy-deep),var(--navy) 70%); color:#fff; padding:64px 0 56px; position:relative; overflow:hidden}
header.hero::after{content:""; position:absolute; right:-80px; top:-80px; width:340px; height:340px; background:radial-gradient(circle,rgba(199,126,22,.32),transparent 65%); pointer-events:none}
.eyebrow{font-size:13px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--amber)}
header.hero .eyebrow{color:#F2C77A}
header.hero h1{font-size:clamp(30px,5vw,46px); line-height:1.18; margin:.5rem 0 .7rem; font-weight:800; letter-spacing:-.02em}
header.hero p{font-size:18px; color:#D8E2F2; margin:0; max-width:640px}
.scope{margin-top:26px; display:inline-flex; flex-wrap:wrap; gap:8px; padding:14px 18px; background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.18); border-radius:12px; font-size:14.5px; color:#EAF0FA}
.scope b{color:#fff}
.chiprow{display:flex; gap:8px; flex-wrap:wrap; margin-top:20px}
.chiprow a{background:#fff; color:var(--navy); text-decoration:none; font-weight:700; font-size:14px; padding:8px 14px; border-radius:999px; transition:transform .12s ease}
.chiprow a:hover{transform:translateY(-2px)}
.backlink{display:inline-block; margin-bottom:14px; color:#D8E2F2; font-size:14px; text-decoration:none}
.backlink:hover{color:#fff}

nav.toc{position:sticky; top:0; z-index:30; background:rgba(251,250,247,.92); backdrop-filter:saturate(1.4) blur(8px); border-bottom:1px solid var(--line)}
nav.toc ul{max-width:920px; margin:0 auto; padding:11px 22px; display:flex; gap:6px; list-style:none; overflow-x:auto; scrollbar-width:thin}
nav.toc a{white-space:nowrap; text-decoration:none; color:var(--ink-soft); font-weight:600; font-size:14px; padding:6px 12px; border-radius:8px}
nav.toc a:hover, nav.toc a.on{background:var(--navy-tint); color:var(--navy)}

section{padding:54px 0 14px; border-bottom:1px solid var(--line-soft); scroll-margin-top:52px}
.sec-label{display:flex; align-items:baseline; gap:14px; margin-bottom:6px}
.sec-num{font-size:15px; font-weight:800; color:var(--amber); letter-spacing:.04em}
h2{font-size:clamp(24px,3.6vw,32px); font-weight:800; margin:.1rem 0 .4rem; letter-spacing:-.02em}
h2 .en{color:var(--muted); font-weight:600; font-size:.62em}
h3{font-size:22px; font-weight:800; margin:40px 0 10px; color:var(--navy-deep); padding-top:6px}
h4{font-size:18.5px; font-weight:800; margin:28px 0 6px; color:var(--navy-deep)}
h5,h6{font-size:17px; font-weight:800; margin:22px 0 4px}
p{margin:.55rem 0}
strong,b{font-weight:800}
.lead{font-size:18.5px; color:var(--ink-soft)}
hr{border:none; border-top:1px solid var(--line); margin:30px 0}
ul,ol{padding-left:1.25rem}
li{margin:.3rem 0}

blockquote,.thesis{border-left:5px solid var(--navy); background:var(--navy-tint); padding:12px 18px; border-radius:0 12px 12px 0; margin:18px 0; font-size:16.5px}
blockquote p{margin:.3rem 0}
blockquote b,blockquote strong,.thesis b{color:var(--navy-deep)}

.callout{border-radius:12px; padding:14px 18px; margin:18px 0; font-size:16px}
.callout .tag{font-weight:800; font-size:13px; letter-spacing:.06em; display:block; margin-bottom:4px}
.callout > :last-child{margin-bottom:0}
.callout ul,.callout ol{margin:.3rem 0}
.callout-exam{background:var(--amber-soft); border:1px solid var(--amber-line)}
.callout-exam .tag{color:var(--amber)}
.callout-note{background:#EEF4FF; border:1px dashed #9FB8E6; font-size:15.5px}
.callout-note .tag{color:#2E5BB8}
.callout-note b,.callout-note strong{color:#1E3A6E}
.callout-important{background:var(--coral-soft); border:1px solid #EFC4C1}
.callout-important .tag{color:var(--coral)}
.callout-warning{background:var(--violet-soft); border:1px solid #D5C6EE; font-size:15.5px}
.callout-warning .tag{color:var(--violet)}
.callout blockquote{background:rgba(255,255,255,.6)}
.callout .tablewrap{margin:10px 0}

code{background:#F2EFE8; padding:2px 7px; border-radius:6px; font-size:.9em; font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace; color:var(--navy-deep)}
pre{background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:14px 16px; overflow-x:auto; font-size:13.5px; line-height:1.5; margin:16px 0}
pre code{background:none; padding:0; color:var(--ink); font-size:inherit}

figure{margin:24px 0; text-align:center}
figure svg{max-width:100%; height:auto; background:var(--surface); border:1px solid var(--line); border-radius:var(--radius); padding:12px; font-family:var(--font)}
figcaption{font-size:13.5px; color:var(--muted); margin-top:8px}

.tablewrap{overflow-x:auto; margin:18px 0}
table{border-collapse:collapse; width:100%; font-size:15px; background:var(--surface); border-radius:12px; overflow:hidden; border:1px solid var(--line)}
th,td{padding:10px 13px; text-align:left; border-bottom:1px solid var(--line-soft); vertical-align:top}
th{background:var(--navy); color:#fff; font-weight:700}
tr:last-child td{border-bottom:none}
tbody tr:nth-child(even){background:#FCFBF8}
td b,td strong{color:var(--navy-deep)}
.callout th{background:var(--navy-deep)}

dl{margin:14px 0}
dt{font-weight:800; color:var(--navy-deep); margin-top:12px}
dd{margin:2px 0 8px 0; padding:8px 14px; background:var(--surface); border:1px solid var(--line); border-radius:10px}

.cards{display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:12px; margin:18px 0}
.card{background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:14px 16px; text-decoration:none; color:inherit; display:block; transition:transform .12s ease, border-color .12s}
.card:hover{transform:translateY(-2px); border-color:var(--navy-line)}
.card .yr{font-size:12.5px; font-weight:800; color:var(--amber); letter-spacing:.05em}
.card h4{margin:.1rem 0 .3rem; font-size:17px}
.card p{margin:0; font-size:14px; color:var(--ink-soft); line-height:1.55}

.q{background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:14px 18px; margin:12px 0}
.q .qn{margin:0; font-weight:700}
.q .qno{color:var(--navy); font-weight:800; margin-right:4px}
.q code{font-size:.8em; color:var(--muted); background:var(--line-soft)}
details.ans{margin-top:10px; border-top:1px dashed var(--line); padding-top:8px}
details.ans summary{cursor:pointer; font-weight:700; color:var(--amber); font-size:14.5px; list-style:none; user-select:none}
details.ans summary::-webkit-details-marker{display:none}
details.ans summary::before{content:"▸ "}
details.ans[open] summary::before{content:"▾ "}
details.ans .body{margin-top:8px; font-size:15px; color:var(--ink-soft)}
details.ans .body b,details.ans .body strong{color:var(--green)}
.quizbar{display:flex; gap:8px; margin:12px 0 4px; flex-wrap:wrap}
.quizbar button{font-family:var(--font); font-weight:700; font-size:14px; padding:7px 14px; border-radius:999px; border:1px solid var(--navy-line); background:#fff; color:var(--navy); cursor:pointer}
.quizbar button:hover{background:var(--navy-tint)}

.gbox{position:sticky; top:46px; z-index:20; background:var(--paper); padding:10px 0 6px}
#gsearch{width:100%; padding:13px 16px; font-size:16px; font-family:var(--font); border:2px solid var(--navy-line); border-radius:12px; background:#fff; color:var(--ink)}
#gsearch:focus{outline:none; border-color:var(--navy)}
.ghint{font-size:13px; color:var(--muted); margin:6px 2px 0}
.gsec{margin:24px 0}
.gsec h3{margin:10px 0 10px}
.terms{display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:12px}
.term{background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:13px 15px}
.term .t{font-weight:800; color:var(--navy-deep); font-size:16.5px; margin-bottom:3px}
.term .tb{display:inline-block; font-size:11.5px; font-weight:700; color:var(--amber); background:var(--amber-soft); border:1px solid var(--amber-line); border-radius:999px; padding:1px 8px; margin-left:6px; vertical-align:middle}
.term p{margin:.2rem 0 0; font-size:14.5px; color:var(--ink-soft); line-height:1.6}
.term .ex{display:block; margin-top:5px; font-size:13.5px; color:#2E5BB8}
.term b{color:var(--navy-deep)}
.gnone{display:none; color:var(--muted); padding:20px 2px}

#totop{position:fixed; right:18px; bottom:18px; z-index:40; width:44px; height:44px; border-radius:50%; border:none; background:var(--navy); color:#fff; font-size:18px; cursor:pointer; box-shadow:0 4px 14px rgba(20,42,82,.25); opacity:0; pointer-events:none; transition:opacity .2s}
#totop.show{opacity:1; pointer-events:auto}

footer{padding:40px 0 70px; color:var(--muted); font-size:14px}

@media(max-width:560px){
  body{font-size:16px}
  section{padding:40px 0 10px}
  pre{font-size:12.5px}
  th,td{padding:9px 10px; font-size:14px}
}
@media print{
  nav.toc,#totop,.gbox,.quizbar{display:none}
  details.ans{display:block}
  details.ans .body{display:block}
  section{break-inside:auto}
}
"""

JS = """
const links=[...document.querySelectorAll('nav.toc a')];
const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
const obs=new IntersectionObserver(es=>{
  es.forEach(e=>{
    if(!e.isIntersecting) return;
    const a=map.get(e.target.id); if(!a) return;
    links.forEach(l=>l.classList.remove('on')); a.classList.add('on');
    a.scrollIntoView({block:'nearest',inline:'center',behavior:'smooth'});
  });
},{rootMargin:'-35% 0px -60% 0px'});
document.querySelectorAll('section[id]').forEach(s=>obs.observe(s));

const box=document.getElementById('gsearch');
if(box){
  const terms=[...document.querySelectorAll('.term')];
  const groups=[...document.querySelectorAll('.gsec')];
  const none=document.getElementById('gnone');
  box.addEventListener('input',()=>{
    const v=box.value.trim().toLowerCase();
    let shown=0;
    terms.forEach(t=>{const hit=t.textContent.toLowerCase().includes(v); t.style.display=hit?'':'none'; if(hit)shown++;});
    groups.forEach(g=>{g.style.display=[...g.querySelectorAll('.term')].some(t=>t.style.display!=='none')?'':'none';});
    none.style.display=shown===0?'block':'none';
  });
}

const ans=()=>[...document.querySelectorAll('details.ans')];
document.getElementById('openall')?.addEventListener('click',()=>ans().forEach(d=>d.open=true));
document.getElementById('closeall')?.addEventListener('click',()=>ans().forEach(d=>d.open=false));

const top=document.getElementById('totop');
addEventListener('scroll',()=>top.classList.toggle('show',scrollY>900),{passive:true});
top.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));
"""

BIG_FIG = re.search(r'<figure class="fig" id="fig-big".*?</figure>', (SRC / "index.md").read_text(encoding="utf-8"), re.S).group(0)

BIG_PICTURE = f"""
<section id="big">
  <div class="sec-label"><span class="sec-num">00</span><span class="eyebrow">시작하기 전에</span></div>
  <h2>가장 큰 그림 한 장</h2>
  <p class="lead">이 과목은 결국 <strong>"글자를 숫자로 바꾸고(임베딩) → 그 숫자로 다음 단어를 맞히는 거대한 모델(LLM)을 만들고 → 그 모델에게 손발과 기억을 달아 스스로 일하게(AI Agent) 하는"</strong> 이야기예요.</p>
  {BIG_FIG}
  <div class="thesis">
    각 장은 <b>앞 장의 한계를 해결</b>하며 이어집니다. "이전 방식의 무엇이 문제였나?"를 같이 기억하면 전체가 하나의 이야기가 돼요.
  </div>
  <div class="tablewrap"><table>
    <thead><tr><th>단계</th><th>한 줄</th><th>해결한 문제</th><th>장</th></tr></thead>
    <tbody>
    <tr><td><b>임베딩</b></td><td>단어 → 벡터(숫자 목록)</td><td>컴퓨터는 글자를 모른다</td><td><a href="#ch2">2</a></td></tr>
    <tr><td><b>Dense 표현</b></td><td>짧고 의미 있는 벡터</td><td>One-hot은 너무 크고 의미가 없다</td><td><a href="#ch2">2</a></td></tr>
    <tr><td><b>Transformer</b></td><td>Attention으로 한꺼번에</td><td>RNN은 느리고 정보를 잃는다</td><td><a href="#ch3">3</a></td></tr>
    <tr><td><b>LLM (GPT)</b></td><td>거대 모델 + In-context Learning</td><td>매번 Fine-tuning이 번거롭다</td><td><a href="#ch4">4</a></td></tr>
    <tr><td><b>Adaptation Tuning</b></td><td>Instruction · Alignment · PEFT</td><td>똑똑한데 말을 안 듣고, 튜닝이 비싸다</td><td><a href="#ch5">5</a></td></tr>
    <tr><td><b>Prompt Engineering</b></td><td>질문을 잘하는 법</td><td>모델은 그대로 두고 성능을 올리고 싶다</td><td><a href="#ch6">6</a></td></tr>
    <tr><td><b>AI Agent</b></td><td>도구 + 기억 + 계획</td><td>LLM은 머리만 있고 손발·기억이 없다</td><td><a href="#ch7">7</a>~<a href="#ch10">10</a></td></tr>
    <tr><td><b>Cognitive Architecture</b></td><td>기억·행동·의사결정 구조화</td><td>어떤 구조로 설계할지 기준이 없다</td><td><a href="#ch11">11</a></td></tr>
    <tr><td><b>Multi-Agent</b></td><td>여러 에이전트로 조직</td><td>혼자서는 복잡한 일을 감당 못 한다</td><td><a href="#ch12">12</a></td></tr>
    </tbody>
  </table></div>
  <div class="callout callout-exam"><span class="tag">시험 포인트</span>
    중간고사는 <b>필기시험(written test)만</b> 40점이에요. 코드를 치는 게 아니라 <b>용어의 정의 + 왜 필요한지 + 비교</b>를 내 말로 쓸 수 있어야 합니다. 노란 박스가 바로 그 연습용이에요.
  </div>
  <div class="callout callout-note"><span class="tag">🐣 처음이라 단어가 어렵다면</span>
    걱정 마세요. 모르는 단어가 나오면 바로 아래 <b>📖 쉬운 용어사전</b>에서 검색하면 됩니다. 수학이 처음이라면 <a href="#math"><b>기초 수학</b></a>을 먼저 읽고 오세요.
  </div>
  <h3>추천 공부 순서</h3>
  <div class="cards">
    <a class="card" href="#glossary"><span class="yr">STEP 1</span><h4>📖 용어사전 훑기</h4><p>단어만 대충 알아도 본문이 두 배 쉬워져요.</p></a>
    <a class="card" href="#ch1"><span class="yr">STEP 2</span><h4>1장 → 12장</h4><p>각 장 맨 위 "한 줄 요약"부터 읽고 들어가기.</p></a>
    <a class="card" href="#compare"><span class="yr">STEP 3</span><h4>헷갈리는 것 총정리</h4><p>짝 비교 · 함정 · 키워드 매칭.</p></a>
    <a class="card" href="#quiz"><span class="yr">STEP 4</span><h4>예상문제</h4><p>객관식 · 빈칸 · 서술, 답 가리고 풀기.</p></a>
    <a class="card" href="#cheat"><span class="yr">STEP 5</span><h4>치트시트</h4><p>시험 직전 30분, 숫자·비교표만.</p></a>
  </div>
</section>
"""


def main() -> None:
    glossary_html, nterms = build_glossary()
    sections = [build_section(*c) for c in CHAPTERS]
    nq = len(re.findall(r'class="q"', sections[-1]))

    toc_items = [("big", "0. 큰 그림"), ("glossary", "📖 용어사전")] + [(sid, chip) for _, sid, _, chip in CHAPTERS]
    toc = "".join(f'<li><a href="#{sid}">{label}</a></li>' for sid, label in toc_items)

    glossary = f"""
<section id="glossary">
  <div class="sec-label"><span class="eyebrow">백지여도 OK</span></div>
  <h2>📖 쉬운 용어 사전 <span class="en">모르는 단어는 여기서</span></h2>
  <p class="lead">시험에 나오는 단어 {nterms}개를 <strong>수학·전공 지식 0</strong>이어도 알 수 있게, <strong>비유와 함께</strong> 풀었어요. 검색창에 쳐 보세요.</p>
  <div class="gbox">
    <input id="gsearch" type="text" placeholder="🔍 단어 검색 (예: 임베딩, lora, 어텐션, rag, 메모리 …)" autocomplete="off">
    <p class="ghint">한글·영어 아무거나. 지우면 전체가 다시 보여요.</p>
  </div>
  <p class="gnone" id="gnone">앗, 그 단어는 없네요. 다른 표현으로 검색하거나 상단 목차에서 해당 장을 찾아보세요.</p>
  {glossary_html}
</section>
"""

    page = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>지능형 소프트웨어 중간 한 방 정리 · LLM · AI Agent</title>
<meta name="description" content="지능형 소프트웨어 중간고사 범위(강의자료 3개, 212p)를 한 페이지로: 임베딩, Transformer, LLM, Adaptation Tuning, Prompt, AI Agent, CoALA, Multi-Agent + 예상문제 {nq}개">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>&#129302;</text></svg>">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
<style>{CSS}</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <a class="backlink" href="index.html">← 장별 노트로 보기</a><br>
    <span class="eyebrow">지능형 소프트웨어 · 중간고사 완벽 정리</span>
    <h1>한 파일로 끝내는<br>LLM · AI Agent</h1>
    <p>수학도, AI도 처음인 사람을 위해. 비유와 그림으로 개념을 잡고, 예상문제 {nq}개로 마무리합니다.</p>
    <div class="scope">📌 시험 범위: <b>강의자료 3개 전부</b> (Orientation · LLM · AI Agent, 212p) · <b>필기시험 40점</b></div>
    <div class="chiprow">
      <a href="#big">큰 그림</a>
      <a href="#glossary">📖 쉬운 용어사전</a>
      <a href="#ch2">임베딩</a>
      <a href="#ch3">Transformer</a>
      <a href="#ch4">GPT</a>
      <a href="#ch5">RLHF·LoRA</a>
      <a href="#ch7">AI Agent</a>
      <a href="#ch11">CoALA</a>
      <a href="#quiz">예상문제</a>
    </div>
  </div>
</header>

<nav class="toc"><ul>{toc}</ul></nav>

<main class="wrap">
{BIG_PICTURE}
{glossary}
{''.join(sections)}
</main>

<footer class="wrap">
  지능형 소프트웨어 중간고사 정리 · 원본: <code>content/isw/*.md</code> → <code>tools/build_isw_onepage.py</code> 로 생성 ·
  <a href="index.html">장별 노트</a> · <a href="../index.html">전체 과목</a>
</footer>

<button id="totop" type="button" aria-label="맨 위로">↑</button>
<script>{JS}</script>
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"완료: {OUT.relative_to(ROOT)}  (섹션 {len(sections) + 2}개, 용어 {nterms}개, 문제 {nq}개, {len(page) // 1024}KB)")


if __name__ == "__main__":
    main()
