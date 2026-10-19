# 3학년 2학기 시험 정리

강의 자료를 시험 대비용으로 정리한 노트. 마크다운으로 쓰고 정적 HTML로 빌드해서 GitHub Pages로 공개한다.

## 구조

```
.
├── content/              ← 여기만 수정한다 (마크다운 원본)
│   ├── site.json         ← 사이트 구조(네비게이션) 정의
│   ├── _TEMPLATE.md      ← 새 강의 작성용 템플릿
│   ├── index.md
│   ├── embedded/         ← 임베디드 IoT 프로그래밍
│   └── hpc/              ← 고성능 컴퓨팅
│
├── build.py              ← content/ → HTML 변환
├── assets/               ← 스타일, 스크립트
├── tools/pdf2md.py       ← 강의 PDF에서 텍스트 뽑는 보조 스크립트
│
├── index.html            ┐
├── embedded/*.html       ├ 빌드 결과물 (자동 생성, 직접 수정 금지)
├── hpc/*.html            │
└── search-index.json     ┘
```

빌드 결과물을 그대로 커밋하기 때문에 GitHub Pages에서 **별도 설정이나 빌드 없이** 바로 서비스된다.

## 최초 1회 설정

```bash
pip install markdown pygments
```

## 내용 추가하는 법

### 1. 새 강의 페이지 추가

```bash
cp content/_TEMPLATE.md content/embedded/06-flask.md
```

마크다운을 작성한 뒤 `content/site.json` 의 해당 과목 `pages` 에 한 줄 추가한다.

```json
{ "file": "embedded/06-flask.md", "title": "6. Flask 센서 제어" }
```

그리고 빌드.

```bash
python build.py
```

### 2. 새 과목 추가

`content/site.json` 의 `sections` 에 항목을 추가하고, `content/<id>/index.md` 를 만든다.

```json
{
  "id": "network",
  "title": "컴퓨터 네트워크",
  "index": "network/index.md",
  "pages": []
}
```

### 3. 결과 확인

```bash
python -m http.server 8000
```

→ http://localhost:8000

> 검색 기능은 `fetch` 를 쓰기 때문에 **파일을 더블클릭해서 열면(`file://`) 동작하지 않는다.**
> 내용 확인은 되지만, 검색까지 보려면 위처럼 로컬 서버를 띄워야 한다.

## 글 쓸 때 쓸 수 있는 것

| 문법 | 결과 |
|---|---|
| 표, 목록, 코드블록 | 일반 마크다운 그대로 |
| `용어` + 다음 줄 `: 정의` | 정의 목록 |
| `{: .시험 }` + 인용문 | 노란 "시험 포인트" 박스 |
| `{: .중요 }` + 인용문 | 빨간 "중요" 박스 |
| `{: .주의 }` + 인용문 | 보라 "주의" 박스 |
| `{: .참고 }` + 인용문 | 파란 "참고" 박스 |

콜아웃 안에도 표·목록·코드를 그대로 넣을 수 있다. 자세한 예시는 `content/_TEMPLATE.md` 참고.

문서의 `##`, `###` 제목은 자동으로 우측 목차와 검색 인덱스에 들어간다.

## 강의 PDF에서 초안 뽑기

```bash
pip install pymupdf

# 폴더 안 모든 PDF 텍스트 추출 → .extract/
python tools/pdf2md.py "고성능컴퓨팅"

# 이미지로 된 코드/회로도 페이지를 PNG로 렌더
python tools/pdf2md.py "고성능컴퓨팅/Lec_2_CUDA_개요.pdf" --images 7,12,20
```

슬라이드의 코드나 회로도는 대부분 이미지라서 텍스트로 안 나온다. `--images` 로 해당 페이지를 그림으로 뽑아 보면서 옮겨 적으면 된다.

## GitHub Pages 배포

1. 이 폴더를 GitHub 저장소로 push
2. 저장소 **Settings → Pages → Source: Deploy from a branch**
3. Branch: `main`, Folder: `/ (root)` → Save

이후에는 `python build.py` 후 커밋·push 하면 반영된다.

## 주의

- **`.html` 파일을 직접 고치지 말 것.** 다음 빌드 때 덮어써진다. 항상 `content/` 의 마크다운을 고친다.
- 강의 원본 PDF는 저작권 문제로 `.gitignore` 에 넣어 공개 저장소에 올리지 않는다.
