# Do It Django A to Z - Frontend 학습 기록

> 이 파일은 stash restore 전 현재 상태를 기록한 스냅샷입니다.
> 복원 후 변경된 내용과 비교하는 데 사용하세요.
> 기록 시점: 2026-04-09 (commit `ae458c0`)

---

## 수업 진행 내역 (git 커밋 기준)

| 커밋 | 내용 | 주요 작업 |
|------|------|-----------|
| `bf45706` | Initial commit | 프로젝트 시작 |
| `30675b8` | Do It! HTML 연습 | `index.html`, `about_me.html` 기초 작성 |
| `7d0cc7d` | Do it! style 적용하기 | 인라인 스타일 적용 |
| `add610a` | Do it! CSS 파일 사용하기 | `practice.css` 분리 |
| `cd2e97c` | JS 덧셈 기능 추가하기 | `doSomething()` 함수, 두 수 실시간 합산 |
| `56d1c19` | JS 현재 시각 alert로 보여주기 | `whatTimeIsIt()` 함수 |
| `1cfd211` | JS파일 분리하기 | `add_two_numbers.js`, `what_time_is_it.js` 파일 분리 |
| `b59fe71` | 부트스트랩 추가하고 navbar 적용하기 | Bootstrap 4 로컬 추가, navbar 구성 |
| `7418805` | 부트스트랩 Grid 사용하기 | Bootstrap grid 레이아웃 |
| `cd8f623` | 부트스트랩 Spacing 사용하기 | `my-`, `py-`, `mb-` 등 spacing 유틸리티 |
| `36b2679` | 사이트 모양 구상하기 0 | blog_list 레이아웃 초안 |
| `84ce285` | 사이트 모양 구상하기 (card) | Bootstrap card 컴포넌트 |
| `6785862` | 사이트 모양 구상하기 (pagination) | Bootstrap pagination |
| `e8b6132` | 사이트 모양 구상하기 (footer) | footer 섹션 |
| `e5f6af4` | 사이트 모양 구상하기 (Modal) | Login modal |
| `6ce0d15` | 사이트 모양 구상하기 (Buttons) | 버튼 스타일 |
| `a9f91fb` | 사이트 모양 구상하기 (font awesome) | Font Awesome 아이콘 적용 |
| `8d55ac3` | lec05 | Flask 앱 도입, 파일 `static/`, `templates/`로 재구성, `blog_list.html` 신규, `layout.html` 분리 |
| `ae458c0` | . | hw08 폴더 추가, 메인 템플릿 `layout.html` 상속 구조로 리팩토링 |

---

## lec05에서 한 주요 변경 (8d55ac3)

- `app.py` 신규 생성 — Flask 라우팅 3개 (`/`, `/blog_list`, `/about`)
- 파일 정리: `bootstrap4/` → `static/css/`, `images/` → `static/images/`, JS/CSS 파일 → `static/`
- `blog_list.html` 신규 작성 (카드 2개, 페이지네이션, 사이드바)
- `layout.html` 분리 — navbar, footer, Bootstrap CDN 공통화
- `about_me.html`, `index.html` → `templates/` 이동, `url_for('static', ...)` 경로 수정

## 마지막 커밋에서 한 주요 변경 (ae458c0)

- `hw08/` 폴더 신규 — 별도 Flask 앱 (갤러리/프로필 페이지, `layout.html` 상속 구조)
- 메인 `templates/` 리팩토링:
  - `layout.html`: navbar, login modal, footer만 남기고 page별 콘텐츠 제거, `{% block content %}` 추가
  - `index.html`: `{% extends "layout.html" %}` 적용, 중복 `<head>`/`<nav>` 제거
  - `blog_list.html`: `{% extends "layout.html" %}` 적용, 중복 JS 스크립트 제거
  - `about_me.html`: `{% extends "layout.html" %}` 적용, `url_for('static', ...)` 경로 수정

---

## 현재 파일 구조 (stash restore 전)

```
do_it_django_atoz_frontend/
├── app.py                          # Flask 앱 (라우트 3개)
├── CLAUDE.md                       # 이 파일
├── README.md
├── templates/
│   ├── layout.html                 # 공통 base: navbar + login modal + footer
│   ├── index.html                  # 홈 (extends layout)
│   ├── blog_list.html              # 블로그 목록 (extends layout)
│   └── about_me.html              # 소개 페이지 (extends layout)
├── static/
│   ├── css/bootstrap.min.css       # Bootstrap 4.4.1 로컬
│   ├── practice.css                # nav 스타일 (현재 미사용)
│   ├── add_two_numbers.js          # 두 수 합산 인터랙션
│   ├── what_time_is_it.js          # 현재 시각 alert
│   └── images/
│       ├── stay_funky.jpg
│       ├── boy_01.jpg
│       ├── image_a.jpg
│       ├── image_b.jpg
│       └── image_c.jpg
└── hw08/                           # 별도 실습 앱
    ├── app.py
    ├── templates/
    │   ├── layout.html
    │   ├── index.html
    │   ├── gallery.html
    │   └── profile.html
    └── static/
        ├── styles.css
        └── *.jpg (hoodie, old, young_*)
```

---

## 현재 각 파일 핵심 내용

### app.py
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")       → index.html
@app.route("/blog_list") → blog_list.html
@app.route("/about")  → about_me.html

app.run(debug=True)
```

### templates/layout.html
- Bootstrap 4.4.1 (로컬 CSS) + Font Awesome CDN
- Bootstrap 4 JS (jQuery slim, Popper, Bootstrap) CDN
- Navbar: "Do It Django" 브랜드, Home/Blog/About Me/Dropdown 메뉴, Log In 버튼
- Login Modal: Google/Email 로그인, Email 회원가입 버튼 (Font Awesome 아이콘)
- `{% block content %}{% endblock %}` 위치: navbar 아래, footer 위
- Footer: "Copyright © Do It Django A to Z 2021"

### templates/index.html
- `{% extends "layout.html" %}`
- h1~h5 헤딩 예제
- "현재시간" 버튼 (`whatTimeIsIt()`)
- a/b 입력 → 실시간 덧셈 (`doSomething()`)
- `stay_funky.jpg` 이미지
- `add_two_numbers.js`, `what_time_is_it.js` 스크립트 로드

### templates/blog_list.html
- `{% extends "layout.html" %}`
- 8:4 컬럼 분할 (col-md-8 / col-md-4)
- 왼쪽: 포스트 카드 2개 (dummyimage.com 썸네일) + pagination
- 오른쪽 사이드바: Search, Categories 위젯

### templates/about_me.html
- `{% extends "layout.html" %}`
- 9:3 컬럼 — 텍스트 + `boy_01.jpg`
- Portfolio: `image_a.jpg` (col-lg-6), `image_b.jpg` (col-lg-3), `image_c.jpg` (col-lg-3)
- `what_time_is_it.js` 스크립트 로드

---

## stash restore 후 비교 포인트

stash를 복원하면 아래 항목들이 달라질 수 있습니다:

- `templates/` 내 파일 변경 여부
- `static/` 내 새 파일 추가 여부
- `app.py` 라우트 추가/변경 여부
- 새 강의 내용 반영 여부 (lec06 이후?)

`git diff` 또는 `git stash show -p` 로 확인하세요.
