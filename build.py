#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
content/ 의 마크다운을 정적 HTML 사이트로 변환한다.

사용법:
    pip install markdown pygments        # 최초 1회
    python build.py

새 강의를 추가하려면:
    1) content/<과목>/06-xxx.md 작성
    2) content/site.json 의 해당 section > pages 에 한 줄 추가
    3) python build.py
자세한 내용은 README.md 참고.
"""

import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("markdown 패키지가 필요합니다:  pip install markdown pygments")

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ASSETS = ROOT / "assets"

# 콜아웃 한글 이름 -> (CSS 클래스, 표시 제목)
CALLOUTS = {
    "시험": ("exam", "시험 포인트"),
    "중요": ("important", "중요"),
    "참고": ("note", "참고"),
    "주의": ("warning", "주의"),
}

CALLOUT_RE = re.compile(
    r"^\{:\s*\.(?P<name>[^\s}]+)\s*\}[ \t]*\n(?P<body>(?:^>.*\n?)+)",
    re.MULTILINE,
)


def expand_callouts(text: str) -> str:
    """`{: .시험 }` + 인용문 블록을 md_in_html 이 처리할 div 로 바꾼다."""

    def repl(m: re.Match) -> str:
        name = m.group("name")
        cls, label = CALLOUTS.get(name, ("note", name))
        body = "\n".join(
            re.sub(r"^>[ ]?", "", line) for line in m.group("body").splitlines()
        )
        return (
            f'\n<div class="callout callout-{cls}" markdown="1">\n'
            f'<p class="callout-title">{label}</p>\n\n'
            f"{body}\n\n</div>\n"
        )

    return CALLOUT_RE.sub(repl, text)


def slugify_unicode(value: str, separator: str = "-") -> str:
    """한글을 살리는 앵커 생성.

    기본 slugify 는 한글을 전부 버려서 `#_1`, `#_2` 같은 순번 앵커가 된다.
    그러면 나중에 제목을 하나 추가했을 때 뒤쪽 앵커가 전부 밀려
    검색 링크와 북마크가 깨지므로, 제목 글자를 그대로 쓴다.
    """
    value = unicodedata.normalize("NFKC", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_]+", separator, value, flags=re.UNICODE)
    return value.strip(separator) or "section"


def make_md():
    return markdown.Markdown(
        extensions=[
            "extra",          # tables, def_list, fenced_code, attr_list, md_in_html ...
            "toc",
            "sane_lists",
            "codehilite",
        ],
        extension_configs={
            "toc": {
                "permalink": "#",
                "toc_depth": "2-3",
                "slugify": slugify_unicode,
            },
            "codehilite": {"guess_lang": False, "linenums": False},
        },
    )


def rel(from_out: Path, to_out: Path) -> str:
    """출력 파일 간 상대 경로 (POSIX 구분자)."""
    import os

    return os.path.relpath(to_out, from_out.parent).replace("\\", "/")


def build_nav(site, pages, current_out: Path) -> str:
    """좌측 사이드바 HTML."""
    out = ['<nav class="nav">']
    home_out = ROOT / "index.html"
    cls = " class=\"active\"" if current_out == home_out else ""
    out.append(
        f'<a class="nav-home" href="{rel(current_out, home_out)}"{cls}>홈</a>'
    )
    for sec in site["sections"]:
        sec_out = pages[sec["index"]]["out"]
        active = " active" if current_out == sec_out else ""
        out.append('<div class="nav-section">')
        out.append(
            f'<a class="nav-section-title{active}" '
            f'href="{rel(current_out, sec_out)}">{sec["title"]}</a>'
        )
        if sec["pages"]:
            out.append("<ul>")
            for p in sec["pages"]:
                p_out = pages[p["file"]]["out"]
                a = ' class="active"' if current_out == p_out else ""
                out.append(
                    f'<li><a href="{rel(current_out, p_out)}"{a}>{p["title"]}</a></li>'
                )
            out.append("</ul>")
        else:
            out.append('<ul><li class="empty">준비 중</li></ul>')
        out.append("</div>")
    out.append("</nav>")
    return "\n".join(out)


TEMPLATE = """<!doctype html>
<html lang="ko" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>&#128218;</text></svg>">
<link rel="stylesheet" href="{css}">
</head>
<body>
<a class="skip" href="#main">본문으로 건너뛰기</a>
<header class="topbar">
  <button class="menu-btn" aria-label="메뉴" aria-expanded="false">&#9776;</button>
  <a class="brand" href="{home}">{site_title}</a>
  <div class="spacer"></div>
  <input type="search" id="search" placeholder="검색 ( / )" aria-label="검색" autocomplete="off">
  <button class="theme-btn" aria-label="테마 전환" title="테마 전환">&#9681;</button>
</header>
<div class="search-results" id="search-results" hidden></div>
<div class="layout">
  <aside class="sidebar">{nav}</aside>
  <main id="main" class="content">
{body}
  <footer class="page-footer">{footer}</footer>
  </main>
  <aside class="toc-rail">{toc}</aside>
</div>
<script>window.SEARCH_INDEX_URL = "{index_json}";</script>
<script src="{js}"></script>
</body>
</html>
"""


def strip_tags(html: str) -> str:
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"&[a-z]+;", " ", html)
    return re.sub(r"\s+", " ", html).strip()


def main() -> None:
    site = json.loads((CONTENT / "site.json").read_text(encoding="utf-8"))

    # 1) 변환 대상 수집: src(상대경로) -> {out, title}
    pages = {}

    def add(src: str, title: str):
        out = ROOT / (Path(src).with_suffix(".html"))
        pages[src] = {"out": out, "title": title}

    add(site["home"], "홈")
    for sec in site["sections"]:
        add(sec["index"], sec["title"])
        for p in sec["pages"]:
            add(p["file"], p["title"])

    missing = [s for s in pages if not (CONTENT / s).exists()]
    if missing:
        print("[!] content/ 에 없는 파일 (site.json 확인):")
        for m in missing:
            print("    -", m)
        for m in missing:
            pages.pop(m)

    search_index = []
    built = 0

    for src, info in pages.items():
        md_path = CONTENT / src
        out_path = info["out"]
        out_path.parent.mkdir(parents=True, exist_ok=True)

        raw = md_path.read_text(encoding="utf-8")
        md = make_md()
        body = md.convert(expand_callouts(raw))
        toc = md.toc if md.toc_tokens else ""

        m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        # 제목 안의 퍼머링크 앵커(<a class="headerlink">#</a>)는 빼고 읽는다
        page_title = (
            strip_tags(re.sub(r'<a class="headerlink".*?</a>', "", m.group(1), flags=re.S))
            if m
            else info["title"]
        )

        full_title = (
            page_title
            if page_title == site["title"]
            else f'{page_title} · {site["title"]}'
        )

        html = TEMPLATE.format(
            title=full_title,
            site_title=site["title"],
            description=site.get("description", ""),
            css=rel(out_path, ASSETS / "style.css"),
            js=rel(out_path, ASSETS / "app.js"),
            index_json=rel(out_path, ROOT / "search-index.json"),
            home=rel(out_path, ROOT / "index.html"),
            nav=build_nav(site, pages, out_path),
            body=body,
            toc=(f'<div class="toc-title">목차</div>{toc}' if toc.strip() else ""),
            footer=f"<code>content/{src}</code> 에서 생성됨",
        )
        out_path.write_text(html, encoding="utf-8")
        built += 1

        # 검색 인덱스: 섹션(h2/h3) 단위로 쪼갬
        url = rel(ROOT / "index.html", out_path)
        # re.split 에 캡처 그룹이 있으면 [앞부분, 캡처1, 구간1, 캡처2, 구간2, ...] 순으로
        # 돌아온다. 즉 앵커(캡처)가 그 구간보다 "앞"에 온다.
        chunks = re.split(r'(?=<h[23][^>]*id="([^"]+)")', body)
        search_index.append(
            {"url": url, "page": page_title, "heading": "", "text": strip_tags(chunks[0])[:400]}
        )
        for i in range(1, len(chunks) - 1, 2):
            anchor, seg = chunks[i], chunks[i + 1]
            hm = re.search(r"<h[23][^>]*>(.*?)</h[23]>", seg, re.S)
            heading = strip_tags(hm.group(1)).rstrip("#").strip() if hm else ""
            search_index.append(
                {
                    "url": f"{url}#{anchor}",
                    "page": page_title,
                    "heading": heading,
                    # 제목은 heading 에 이미 있으므로 본문만 남겨 미리보기를 깔끔하게
                    "text": strip_tags(seg[hm.end():] if hm else seg)[:400],
                }
            )

    (ROOT / "search-index.json").write_text(
        json.dumps(search_index, ensure_ascii=False), encoding="utf-8"
    )

    # content/ 안의 이미지 등 정적 파일 복사
    copied = 0
    for f in CONTENT.rglob("*"):
        if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
            dest = ROOT / f.relative_to(CONTENT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
            copied += 1

    print(f"완료: {built}개 페이지 생성, 검색 항목 {len(search_index)}개" + (f", 이미지 {copied}개 복사" if copied else ""))
    print("로컬에서 보려면:  python -m http.server 8000   →  http://localhost:8000")


if __name__ == "__main__":
    main()
