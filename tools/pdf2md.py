#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
강의 PDF에서 텍스트를 뽑아 정리 초안을 만들기 위한 보조 스크립트.

이건 "정리된 노트"를 만들어주지 않는다. PDF 안의 글자를 페이지 구분과 함께
텍스트로 뽑아줄 뿐이고, 그걸 보면서 content/ 아래 마크다운을 직접 쓰면 된다.
(슬라이드의 코드·회로도는 보통 이미지라서 텍스트로 안 나온다 → --images 사용)

사용법:
    pip install pymupdf

    # 폴더 안 모든 PDF 텍스트 추출 → .extract/ 에 저장
    python tools/pdf2md.py "고성능컴퓨팅"

    # 특정 PDF의 특정 페이지를 PNG로 렌더 (이미지로 된 코드/도표 확인용)
    python tools/pdf2md.py "고성능컴퓨팅/Lec_2_CUDA_개요.pdf" --images 7,12,20
"""

import argparse
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf  # 구버전 이름
    except ImportError:
        sys.exit("pymupdf 가 필요합니다:  pip install pymupdf")

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".extract"


def extract_text(pdf: Path) -> Path:
    doc = pymupdf.open(pdf)
    OUT.mkdir(exist_ok=True)
    dest = OUT / (pdf.stem + ".txt")
    with dest.open("w", encoding="utf-8") as fh:
        for i, page in enumerate(doc, start=1):
            fh.write(f"\n===== PAGE {i} =====\n")
            fh.write(page.get_text())
    print(f"  {pdf.name}  ({doc.page_count}p)  ->  {dest.relative_to(ROOT)}")
    return dest


def render_pages(pdf: Path, pages: list[int], dpi: int) -> None:
    doc = pymupdf.open(pdf)
    OUT.mkdir(exist_ok=True)
    for pn in pages:
        if not (1 <= pn <= doc.page_count):
            print(f"  [!] {pn} 페이지 없음 (총 {doc.page_count}p)")
            continue
        dest = OUT / f"{pdf.stem}_p{pn}.png"
        doc[pn - 1].get_pixmap(dpi=dpi).save(dest)
        print(f"  p{pn}  ->  {dest.relative_to(ROOT)}")


def main() -> None:
    ap = argparse.ArgumentParser(description="강의 PDF → 텍스트/이미지 추출")
    ap.add_argument("target", help="PDF 파일 또는 PDF가 들어있는 폴더")
    ap.add_argument("--images", help="PNG로 렌더할 페이지 번호 (예: 7,12,20)")
    ap.add_argument("--dpi", type=int, default=150, help="렌더 해상도 (기본 150)")
    args = ap.parse_args()

    target = Path(args.target)
    if not target.is_absolute():
        target = ROOT / target
    if not target.exists():
        sys.exit(f"경로를 찾을 수 없습니다: {target}")

    if args.images:
        if target.is_dir():
            sys.exit("--images 는 PDF 파일 하나를 지정해야 합니다.")
        pages = [int(x) for x in args.images.replace(" ", "").split(",") if x]
        render_pages(target, pages, args.dpi)
        return

    pdfs = sorted(target.glob("*.pdf")) if target.is_dir() else [target]
    if not pdfs:
        sys.exit(f"PDF가 없습니다: {target}")

    print(f"텍스트 추출 ({len(pdfs)}개)")
    for pdf in pdfs:
        extract_text(pdf)
    print(f"\n.extract/ 의 txt를 보면서 content/ 아래 마크다운을 작성하세요.")
    print(".extract/ 는 .gitignore 에 있으므로 커밋되지 않습니다.")


if __name__ == "__main__":
    main()
