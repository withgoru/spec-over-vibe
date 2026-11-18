---
theme: apple-basic
colorSchema: light
title: 바이브코딩 웹 서비스 구조 이해와 운영·유지보수 실전
info: |
  ## 바이브코딩 웹 서비스 구조 이해와 운영·유지보수 실전
  동우화인켐 기업강의 — 이론 2시간 + 강사 라이브 시연 1시간
mdc: true
transition: slide-left
---

<div class="h-full flex flex-col justify-between py-2">
  <div>
    <div class="inline-block px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-bold tracking-wide mb-3">
      SPEC OVER VIBE
    </div>
    <h1 class="!text-3xl !leading-tight font-bold text-slate-900 mt-1">
      바이브코딩 웹 서비스, '만들기'에서 '운영·유지보수'까지
    </h1>
    <p class="!text-base text-slate-600 font-medium !mt-2">
      감(Vibe)이 아닌 명세(Spec)와 Git으로 AI를 통제하는 현업 실전 가이드
    </p>
  </div>
  <div class="grid grid-cols-3 gap-3 my-4 text-xs">
    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
      <div class="text-blue-700 font-bold text-xs mb-1">PART 1 · 이론 1부 (50분)</div>
      <div class="font-bold text-slate-800 text-sm mb-1">웹 서비스 구조와 코드 독해</div>
      <div class="text-slate-600 leading-relaxed">클라이언트-서버 요청·응답 사이클, HTML/CSS/JS/Python 고유 좌표 읽기, <code>CONFIG</code> 분리</div>
    </div>
    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
      <div class="text-amber-700 font-bold text-xs mb-1">PART 2 · 이론 2부 (70분)</div>
      <div class="font-bold text-slate-800 text-sm mb-1">SDD 명세 기반 개발 & Git 통제</div>
      <div class="text-slate-600 leading-relaxed">7대 실수 교정, 레거시 <code>SPEC.md</code> 역추출, Dataiku Cobuild · Git 12대 용어 & 프롬프팅 3대 기법</div>
    </div>
    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
      <div class="text-emerald-700 font-bold text-xs mb-1">PART 3 · 라이브 시연 (60분)</div>
      <div class="font-bold text-slate-800 text-sm mb-1">실전 트러블슈팅 & 유지보수 4막</div>
      <div class="text-slate-600 leading-relaxed">고장 내고 → 원인 찾고(<code>F12</code> · 서버 로그 · <code>Diff</code>) → 프롬프트로 안전하게 고치기</div>
    </div>
  </div>
  <div class="flex items-center justify-between pt-3 border-t border-slate-200 text-xs text-slate-500">
    <div>Choi Wooyoung, 2026</div>
  </div>
</div>

<!--
[Slide 0-1 · 강의 표지 (Cover)]
- 제목: 바이브코딩 웹 서비스, '만들기'에서 '운영·유지보수'까지
- 부제: 감(Vibe)이 아닌 명세(Spec)와 Git으로 AI를 통제하는 현업 실전 가이드
-->

---

# About me
## Owner of KickcodePlus | Web Developer | Lecturer

<div class="grid grid-cols-12 gap-4 mt-3 text-xs items-stretch">
  <div class="col-span-5 flex flex-col justify-between p-4 rounded-xl bg-slate-50 border border-slate-200">
    <div>
      <div class="flex items-center justify-between mb-2">
        <div>
          <div class="text-base font-bold text-slate-900">최우영</div>
          <div class="text-xs text-blue-700 font-semibold">KickcodePlus 대표 · Software Engineer</div>
        </div>
        <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-800 font-bold text-[11px]">withgoru.com</span>
      </div>
      <p class="!text-xs text-slate-600 leading-relaxed !my-2">
        소프트웨어 개발, 데이터 분석, 현업 실무 교육의 경계를 연결하는 웹 개발자이자 기술 강사입니다. 현업 구성원이 AI와 웹 기술을 블랙박스 없이 이해하고 안전하게 운영할 수 있도록 돕습니다.
      </p>
      <div class="grid grid-cols-2 gap-2.5 my-3">
        <div class="p-2.5 rounded-lg bg-white border border-slate-200 text-center">
          <div class="text-xl font-bold text-blue-700">290+</div>
          <div class="text-[11px] text-slate-500 mt-0.5">기업·대학 강의 및 워크숍</div>
        </div>
        <div class="p-2.5 rounded-lg bg-white border border-slate-200 text-center">
          <div class="text-xl font-bold text-emerald-700">4,400h+</div>
          <div class="text-[11px] text-slate-500 mt-0.5">누적 실무 교육·코칭 시간</div>
        </div>
      </div>
    </div>
    <div class="pt-2.5 border-t border-slate-200">
      <div class="font-bold text-slate-700 mb-1.5">Core Tech Stack</div>
      <div class="flex flex-wrap gap-1.5 text-[11px]">
        <span class="px-2 py-0.5 rounded bg-white border border-slate-300 text-slate-700 font-medium">Python (Flask · FastAPI · Django)</span>
        <span class="px-2 py-0.5 rounded bg-white border border-slate-300 text-slate-700 font-medium">JS / Svelte / React</span>
        <span class="px-2 py-0.5 rounded bg-white border border-slate-300 text-slate-700 font-medium">Golang</span>
        <span class="px-2 py-0.5 rounded bg-white border border-slate-300 text-slate-700 font-medium">Git / GitHub Actions</span>
        <span class="px-2 py-0.5 rounded bg-white border border-slate-300 text-slate-700 font-medium">Data & Web Architecture</span>
      </div>
    </div>
  </div>
  <div class="col-span-7 flex flex-col justify-between space-y-2.5">
    <div class="p-3.5 rounded-xl bg-white border border-slate-200 space-y-2">
      <div class="font-bold text-slate-800 text-sm mb-1">주요 경력 (Professional Journey)</div>
      <div class="flex items-start justify-between border-b border-slate-100 pb-1.5">
        <div>
          <span class="font-bold text-slate-900">KickcodePlus (킥코드플러스) 대표</span>
          <div class="text-slate-600 mt-0.5">기업 맞춤형 IT·AI 기술 강의, 웹 서비스 개발 및 기술 컨설팅</div>
        </div>
        <span class="text-slate-400 font-medium shrink-0 ml-2">2024 – 현재</span>
      </div>
      <div class="flex items-start justify-between border-b border-slate-100 pb-1.5">
        <div>
          <span class="font-bold text-slate-900">국민대학교 출강 강사 (Lecturer)</span>
          <div class="text-slate-600 mt-0.5">디지털 마케팅 프로그래밍 및 데이터·웹 구현 실무 강의</div>
        </div>
        <span class="text-slate-400 font-medium shrink-0 ml-2">2022 – 현재</span>
      </div>
      <div class="flex items-start justify-between border-b border-slate-100 pb-1.5">
        <div>
          <span class="font-bold text-slate-900">프리랜스 소프트웨어 엔지니어 & 테크 인스트럭터</span>
          <div class="text-slate-600 mt-0.5">웹 아키텍처, 소프트웨어 엔지니어링, 데이터 사이언스 개발 및 기업 교육</div>
        </div>
        <span class="text-slate-400 font-medium shrink-0 ml-2">2016 – 2024</span>
      </div>
      <div class="flex items-start justify-between">
        <div>
          <span class="font-bold text-slate-900">패스트캠퍼스 (Fastcampus)</span>
          <div class="text-slate-600 mt-0.5">백엔드 프로그래밍 스쿨 과정 기획 및 운영</div>
        </div>
        <span class="text-slate-400 font-medium shrink-0 ml-2">2016</span>
      </div>
    </div>
    <div class="p-3 rounded-xl bg-blue-50/70 border border-blue-200">
      <div class="font-bold text-blue-900 text-xs mb-1.5">주요 출강 기업 및 교육 파트너 (Trusted Clients & Partners)</div>
      <div class="grid grid-cols-2 gap-2 text-[11px] text-slate-700">
        <div>
          <span class="font-bold text-slate-800">주요 기업:</span> 삼성전자, LG전자, 카카오, KB국민카드, 신한투자증권, 11번가 등
        </div>
        <div>
          <span class="font-bold text-slate-800">교육기관·대학:</span> 패스트캠퍼스, 데이원컴퍼니, 업스테이지, SeSAC, 성균관대, 국민대, 가톨릭대 등
        </div>
      </div>
    </div>
  </div>
</div>

<!--
[Slide 0-2 · 강사 소개 (최우영 — https://withgoru.github.io/about/ 기반)]
- 강사: 최우영 (Owner of KickcodePlus | Web Developer | Lecturer)
- 주요 이력: 290+ 기업·대학 강의 및 워크숍, 4,400+ 시간 교육, 삼성전자·LG전자·카카오·KB국민카드·신한투자증권 등 다수 기업 특강 진행
-->


---

# [Module 1] 웹 서비스가 동작하는 원리
## 클라이언트-서버와 요청·응답 사이클 (Slide 1-1)

- **바이브코딩 서비스가 블랙박스처럼 느껴지는 이유:** 화면(Browser)과 연산(Server)의 경계를 모른 채 코드 전체를 하나의 덩어리로 보기 때문

<div class="font-bold text-xs text-slate-600 mt-2 mb-1.5">웹 서비스의 4단계 대화 사이클 (Request–Response Cycle)</div>

<div class="grid grid-cols-4 gap-2.5 text-xs">
  <div class="p-2.5 rounded-lg bg-slate-100 border border-slate-200">
    <div class="font-bold text-slate-800 mb-0.5">1. 사용자 액션 (Event)</div>
    <div class="text-slate-600 leading-snug">브라우저에서 '조회' 버튼 클릭 또는 조건 선택</div>
  </div>
  <div class="p-2.5 rounded-lg bg-blue-50 border border-blue-200">
    <div class="font-bold text-blue-800 mb-0.5">2. 요청 전송 (Request)</div>
    <div class="text-slate-700 leading-snug">브라우저(클라이언트)가 서버에 필요한 조건을 담아 데이터 요청</div>
  </div>
  <div class="p-2.5 rounded-lg bg-amber-50 border border-amber-200">
    <div class="font-bold text-amber-800 mb-0.5">3. 데이터 연산 (Backend Logic)</div>
    <div class="text-slate-700 leading-snug">서버(Dataiku Python)가 데이터셋 조회·필터링·계산 수행</div>
  </div>
  <div class="p-2.5 rounded-lg bg-emerald-50 border border-emerald-200">
    <div class="font-bold text-emerald-800 mb-0.5">4. 응답 및 화면 갱신 (Response & Render)</div>
    <div class="text-slate-700 leading-snug">서버가 결과(JSON)를 돌려주면 브라우저가 화면 일부만 다시 그림</div>
  </div>
</div>

<div class="mt-3 p-3.5 rounded-xl bg-slate-50 border border-slate-200">
  <div class="text-xs font-bold text-slate-500 mb-2.5">요청·응답 흐름 다이어그램 (Request–Response Flow)</div>
  <div class="grid grid-cols-11 gap-2 items-center text-xs">
    <div class="col-span-3 p-3 rounded-lg bg-white border-2 border-blue-500 shadow-sm text-center">
      <div class="font-bold text-blue-700 text-sm">브라우저: 사용자 화면</div>
      <div class="text-slate-500 mt-0.5">(HTML / CSS / JS)</div>
      <div class="mt-2 pt-1.5 border-t border-emerald-200 bg-emerald-50 rounded px-2 py-1 text-emerald-800 font-semibold">
        ④ JS가 결과값으로 표/차트만 갱신
      </div>
    </div>
    <div class="col-span-3 flex flex-col justify-center space-y-2 px-1">
      <div class="p-1.5 rounded bg-blue-100/80 border border-blue-300 text-blue-900 text-center font-medium">
        ① 버튼 클릭 후 JS가 <code>Request</code> 전송 →
      </div>
      <div class="p-1.5 rounded bg-emerald-100/80 border border-emerald-300 text-emerald-900 text-center font-medium">
        ← ③ 계산 결과(JSON) <code>Response</code> 반환
      </div>
    </div>
    <div class="col-span-3 p-3 rounded-lg bg-white border-2 border-amber-500 shadow-sm text-center">
      <div class="font-bold text-amber-700 text-sm">서버: Dataiku 백엔드</div>
      <div class="text-slate-500 mt-0.5">(Python Pandas / Flask)</div>
      <div class="mt-2 pt-1.5 border-t border-amber-200 bg-amber-50 rounded px-2 py-1 text-amber-900 font-semibold">
        ② 데이터셋 조회·계산 수행
      </div>
    </div>
    <div class="col-span-2 p-2.5 rounded-lg bg-slate-100 border-2 border-slate-400 text-center">
      <div class="font-bold text-slate-700">Dataiku<br/>데이터셋</div>
      <div class="text-[11px] text-slate-500 mt-1">원본 테이블<br/>조회 ⇄ 반환</div>
    </div>
  </div>
</div>

<!--
[Slide 1-1 · 웹 서비스가 동작하는 원리: 클라이언트-서버와 요청·응답 사이클]
> 강의 포인트: "오류가 났을 때 '요청을 보내기 전(화면)' 문제인지, '요청을 받은 후(서버)' 문제인지만 갈라도 디버깅의 절반은 끝납니다."
-->

---

# [Module 1] 웹 구성 4요소의 역할 분담과 코드 좌표(Coordinate) 읽기
## 문법 암기가 아닌 AI에게 수정 위치를 정확히 지목해 주는 '좌표 독해력(Code Reading)' (Slide 1-2)

<div class="mt-3 text-sm">

| 구성 요소 | 핵심 역할 | 수정 시 위험도 | AI에게 지시할 때 읽어야 할 '고유 좌표' |
| :--- | :--- | :--- | :--- |
| **HTML** | 화면 **뼈대**와 요소 배치 | 낮음 | 태그의 **`id="..."`**, **`class="..."`** (예: `id="btn-search"`, `id="result-table"`) |
| **CSS** | 색상, 여백, 글꼴, 레이아웃 | **매우 낮음** | 선택자 이름 (`.card-header`, `#summary-box`) — 데이터 로직과 무관한 안전 영역 |
| **JavaScript** | 클릭 감지, 서버 통신(`fetch`), 화면 갱신 | 중간~높음 | **이벤트 함수명** (`onClickSearch()`), **호출 API 경로** (`/api/yield`) |
| **Python** | 데이터 필터링·집계, 판정 로직, API 창구 | **높음** | **라우트 주소** (`@app.route('/api/yield')`), **핵심 계산 함수명** (`def calc_yield():`) |

</div>

<div class="mt-3 p-2.5 rounded-lg bg-blue-50 border border-blue-200 text-sm">
  <strong>핵심 포인트:</strong> 비전공자에게 필요한 역량은 문법 암기가 아니라 <strong>AI에게 수정 위치를 정확히 지목해 주는 '좌표 독해력(Code Reading)'</strong>입니다.
</div>

<!--
[Slide 1-2 · 웹 구성 4요소의 역할 분담과 코드 좌표(Coordinate) 읽기]
> 강의 포인트: "AI에게 '저기 위에 있는 표 고쳐줘'라고 하면 엉뚱한 곳을 건드리지만, '`id="result-table"` 영역만 고쳐줘'라고 좌표를 찍어주면 사고가 나지 않습니다."
-->

---

# [Module 1] Dataiku Webapp의 두 가지 구현 구조 이해
## Dataiku에서 Cobuild나 코드로 생성하는 Webapp의 두 가지 아키텍처 구분 (Slide 1-3)

<div class="mt-3 text-sm">

| 구분 | ① 표준 웹 분리형 (HTML/CSS/JS + Python Flask) | ② Python 통합형 (Dash / Streamlit) |
| :--- | :--- | :--- |
| **구조 특징** | 화면 파일(`HTML/JS`)과 연산 파일(`Python`)이 **물리적으로 분리**됨 | Python 코드 하나 안에서 **UI 배치와 데이터 연산을 함께** 작성 |
| **통신 방식** | JS가 `fetch('/api/...')`로 Python에 JSON 데이터를 요청 | 위젯 값 변경 시 Python 스크립트가 상태(State)를 감지해 재로딩 |
| **주요 오류 지점** | 프론트-백엔드 간 **JSON 키 이름 불일치** (예: `yieldRate` vs `yield_rate`) | 상태 초기화 누락, 대용량 데이터 전체 재로딩으로 인한 속도 저하 |
| **유지보수 핵심** | API 입출력 규격(계약)을 잠근 상태에서 화면/로직을 각각 수정 | UI 렌더링 코드와 데이터 계산 함수를 명확히 분리해 작성 |

</div>

<!--
[Slide 1-3 · Dataiku Webapp의 두 가지 구현 구조 이해]
- Dataiku에서 Cobuild나 코드로 생성하는 Webapp의 두 가지 아키텍처(표준 웹 분리형 vs Python 통합형)의 구조 특징, 통신 방식, 주요 오류 지점, 유지보수 핵심 비교
-->

---

# [Module 1] 유지보수의 최대 적: 하드코딩(Hardcoding) vs 설정 분리(CONFIG)
## 기준값·컬럼명·경로를 로직에서 분리하여 운영 리스크 차단 (Slide 1-4)

<div class="grid grid-cols-2 gap-4 mt-3 items-start">
  <div class="space-y-2.5 text-sm">
    <div class="p-2.5 rounded-lg bg-red-50 border border-red-200">
      <div class="font-bold text-red-700">하드코딩 (Hardcoding)</div>
      <div class="mt-1">데이터셋 이름, 컬럼명(<code>LOT_ID</code>, <code>MEAS_VAL</code>), 공정 판정 기준치(<code>수율 85.0%</code>), 파일 경로가 코드 중간중간에 직접 박혀 있는 상태</div>
    </div>
    <div class="p-2.5 rounded-lg bg-amber-50 border border-amber-200">
      <div class="font-bold text-amber-700">현업 운영 리스크</div>
      <div class="mt-1">공정 기준치가 <code>85% → 88%</code>로 바뀌거나 원본 테이블 컬럼명이 바뀔 때마다 코드 전체를 뒤져 수정해야 하며, 한 곳이라도 놓치면 서비스 오작동</div>
    </div>
    <div class="p-2.5 rounded-lg bg-emerald-50 border border-emerald-200">
      <div class="font-bold text-emerald-700">해결 원칙 — 최상단 설정 격리 (Top-level Configuration)</div>
      <div class="mt-1">모든 기준값·컬럼명·경로는 파일 맨 위 <code>CONFIG</code> 딕셔너리 한곳에 모으고 로직은 참조만 하도록 강제</div>
    </div>
  </div>
  <div>

```python
# [Bad] 코드 중간에 기준값과 컬럼명이 박혀 있음
if row['GOOD_CNT'] / row['TOTAL_CNT'] * 100 < 85.0:
    status = "불합격"

# [Good] 최상단 CONFIG에 모든 기준을 격리 → 코드 수정 없이 설정값만 변경
CONFIG = {
    "COL_GOOD": "GOOD_CNT",
    "COL_TOTAL": "TOTAL_CNT",
    "PASS_THRESHOLD": 85.0,
    "FAIL_LABEL": "불합격"
}
```

  </div>
</div>

<!--
[Slide 1-4 · 유지보수의 최대 적: 하드코딩(Hardcoding) vs 설정 분리(CONFIG)]
- 하드코딩 정의, 현업 운영 리스크, 최상단 설정 격리(Top-level Configuration) 원칙 및 Bad vs Good 코드 예시
-->

---

# [Module 2] 전통적 개발방법론이 남긴 교훈과 초기 바이브코딩의 함정
## 소프트웨어 공학의 대원칙: "코드를 치기 전에 설계 기준이 있어야 고칠 수 있다" (Slide 2-1)

<div class="mt-3 text-sm">

| 구분 | 폭포수 (Waterfall) | 애자일 (Agile) | 초기 바이브코딩 (Ad-hoc) | **SDD 기반 바이브코딩** |
| :--- | :--- | :--- | :--- | :--- |
| **작업 순서** | 완벽한 설계 → 구현 | 최소 설계 → 반복 구현 | **설계 생략 → 즉시 구현** | **핵심 명세(Spec) → AI 구현** |
| **초기 구현 속도** | 매우 느림 | 빠름 | 매우 빠름 | 빠름 |
| **유지보수 안정성** | 높음 (설계서 존재) | 높음 (규율·테스트 존재) | **매우 낮음 (수정 시 붕괴)** | **높음 (명세 기준 통제)** |
| **현업 비개발자 적합도** | 부적합 (전문 설계 필요) | 보통 (개발 프로세스 숙지) | 시작은 쉬우나 운영 불가 | **최적 (자연어 명세로 통제)** |

</div>

<div class="mt-3 p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs leading-relaxed">
  <strong class="text-amber-800">현업 바이브코딩의 함정:</strong> 애자일의 '속도'만 가져오고 설계와 검증 기준을 통째로 생략한 상태 → 기준점(설계도)이 없으니 AI가 수정할 때마다 기존 코드를 제멋대로 덮어씀
</div>

<!--
[Slide 2-1 · 전통적 개발방법론이 남긴 교훈과 초기 바이브코딩의 함정]
- 핵심 내용: 소프트웨어 공학의 대원칙 = "코드를 치기 전에 설계 기준이 있어야 고칠 수 있다"
- 현업 바이브코딩의 함정: 애자일의 '속도'만 가져오고 설계와 검증 기준을 통째로 생략한 상태 → 기준점(설계도)이 없으니 AI가 수정할 때마다 기존 코드를 제멋대로 덮어씀
-->

---

# [Module 2] AI 시대의 해법: SDD (Spec-Driven Development, 명세 기반 개발)
## 코더(Coder)에서 명세 작성자(Spec Writer)로의 역할 전환 (Slide 2-2)

<div class="p-2.5 rounded-lg bg-slate-50 border border-slate-200 text-xs mt-2">
  <strong>역할의 전환:</strong> 코드를 직접 타이핑하는 <strong>코더(Coder)</strong> → AI가 움직일 울타리를 설계하는 <strong>명세 작성자(Spec Writer)</strong>
</div>

<div class="font-bold text-xs text-slate-600 mt-3 mb-1.5">SDD(명세 기반 개발)의 3대 핵심 요소 (<code>SPEC.md</code>)</div>

<div class="grid grid-cols-3 gap-3 text-xs">
  <div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
    <div class="font-bold text-blue-800 text-sm mb-1">1. 무엇을 구현/변경할 것인가</div>
    <div class="text-blue-700 font-semibold mb-1">(요구사항)</div>
    <div class="text-slate-700 leading-relaxed">화면 구성, 사용자 입력, 계산 공식</div>
  </div>
  <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
    <div class="font-bold text-amber-800 text-sm mb-1">2. 어떤 규칙을 절대 깨뜨리면 안 되는가</div>
    <div class="text-amber-700 font-semibold mb-1">(불변 제약조건)</div>
    <div class="text-slate-700 leading-relaxed">기존 API 경로, 데이터 컬럼명, 유지해야 할 기존 기능 목록</div>
  </div>
  <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200">
    <div class="font-bold text-emerald-800 text-sm mb-1">3. 무엇이 되면 정상인가</div>
    <div class="text-emerald-700 font-semibold mb-1">(완료 기준)</div>
    <div class="text-slate-700 leading-relaxed">정상 데이터 출력 결과 및 결측치·0건 조회 시 기대 동작</div>
  </div>
</div>

<div class="mt-3 p-3 rounded-lg bg-blue-50 border border-blue-200 text-xs text-center font-semibold text-blue-900">
  "감(Vibe)으로 시키는 바이브코딩에서, 명세(Spec)로 통제하는 SDD로 넘어가야 운영이 가능합니다."
</div>

<!--
[Slide 2-2 · AI 시대의 해법: SDD (Spec-Driven Development, 명세 기반 개발)]
- 핵심 전환 메시지: "감(Vibe)으로 시키는 바이브코딩에서, 명세(Spec)로 통제하는 SDD로 넘어가야 운영이 가능합니다."
-->

---

# [Module 2] 비전공자 바이브코딩 7대 실수 패턴과 교정 원칙 (1/2)
## 현업에서 가장 자주 발생하는 프롬프팅·대화 관리 실수 (Slide 2-3)

<div class="mt-2 text-xs">

| # | 흔히 하는 실수 (Anti-Pattern) | 발생하는 문제 | 바로잡는 원칙 (Best Practice) |
| :--- | :--- | :--- | :--- |
| **1** | **"한 번에 다 해줘" 프롬프팅**<br>(기능 5개를 한 번에 지시) | 로직이 한 함수에 뒤엉키고 일부 요구사항이 누락됨 | **기능 단위 수직 분할 (Vertical Slicing):**<br>화면 뼈대 → 데이터 연동 → 필터 → 차트 순 1개씩 검증 |
| **2** | **무지성 전체 덮어쓰기**<br>(`# ...기존 코드 생략...` 그대로 복붙) | 멀쩡하던 기존 함수·로직이 통째로 날아감 | **스냅샷 백업 & 생략 금지 강제:**<br>수정 전 저장 + *"코드 생략(`...`) 없이 전체 출력"* 지시 |
| **3** | **무맥락 오류 투척**<br>(*"버튼이 안 돼요, 고쳐주세요"*) | AI가 원인을 추측(환각)해 정상 코드까지 갈아엎음 | **3종 세트 버그 리포트:**<br>`[증상 + 브라우저/서버 에러 로그 전체 + 해당 코드]` |
| **4** | **망가진 대화창 무한 연장**<br>(오류 루프에 빠진 채 20~30턴 지속) | 과거의 오염된 맥락 때문에 고치면 다른 곳이 깨짐 | **3-Strike 리셋 규칙:**<br>3번 안에 못 고치면 새 채팅창에 `SPEC` + 깨끗한 코드로 재시작 |

</div>

<!--
[Slide 2-3 · 비전공자 바이브코딩 7대 실수 패턴과 교정 원칙 (1/2)]
- 패턴 1: "한 번에 다 해줘" 프롬프팅 → 기능 단위 수직 분할 (Vertical Slicing)
- 패턴 2: 무지성 전체 덮어쓰기 → 스냅샷 백업 & 생략 금지 강제
- 패턴 3: 무맥락 오류 투척 → 3종 세트 버그 리포트
- 패턴 4: 망가진 대화창 무한 연장 → 3-Strike 리셋 규칙
-->

---

# [Module 2] 비전공자 바이브코딩 7대 실수 패턴과 교정 원칙 (2/2)
## 구조 분리·예외 데이터 방어·보안 원칙 (Slide 2-4)

<div class="mt-2 text-xs">

| # | 흔히 하는 실수 (Anti-Pattern) | 발생하는 문제 | 바로잡는 원칙 (Best Practice) |
| :--- | :--- | :--- | :--- |
| **5** | **화면·로직·기준값 뒤섞기**<br>(코드 중간에 임계값·컬럼명 하드코딩) | 공정 기준 하나 바꿀 때도 코드 전체를 뜯어고쳐야 함 | **최상단 설정 격리 (`Top-level CONFIG`):**<br>컬럼명·임계값·경로는 파일 맨 위 `CONFIG`에 모두 분리 |
| **6** | **정상 데이터(Happy Path)만 테스트**<br>(깔끔한 샘플 10줄만 넣고 배포) | 현업 데이터의 결측치(`NaN`)·0 나누기에서 서버 즉시 중단 | **악성 데이터 방어 처리 지시:**<br>배포 전 결측치·조회 0건·타입 오류 예외 처리 일괄 점검 |
| **7** | **사내 실제 데이터·인증키 평문 입력**<br>(실제 데이터 행 및 DB 비밀번호 복붙) | 사내 데이터 외부 유출 및 브라우저 소스 내 키 노출 | **스키마만 전달 & 키 분리:**<br>실제 값 대신 컬럼명+가짜 샘플 3줄 전달, 키는 환경변수 처리 |

</div>

<!--
[Slide 2-4 · 비전공자 바이브코딩 7대 실수 패턴과 교정 원칙 (2/2)]
- 패턴 5: 화면·로직·기준값 뒤섞기 → 최상단 설정 격리 (Top-level CONFIG)
- 패턴 6: 정상 데이터(Happy Path)만 테스트 → 악성 데이터 방어 처리 지시
- 패턴 7: 사내 실제 데이터·인증키 평문 입력 → 스키마만 전달 & 키 분리
-->

---

# [Module 2] [실전 처방] 문서 없는 기존 프로젝트에 스펙 심기
## Reverse-Spec Extraction — 프로젝트 전체를 스캔해 SDD 체제로 전환하는 마스터 프롬프트 (Slide 2-5)

<div class="grid grid-cols-12 gap-4 mt-2 items-start">
<div class="col-span-7">

```text
너는 시니어 소프트웨어 아키텍트야. 현재 이 프로젝트(워크스페이스 전체)는
운영 중인 사내 웹 서비스인데 설계 문서가 없어. 프로젝트 디렉토리 구조와
핵심 소스 파일들을 탐색·분석해서 루트에 기준 문서인 `SPEC.md`를 생성해 줘.

[중요 제약조건]
- 기존 코드는 한 줄도 수정하지 말고 현재 구현된 동작 사실만 정확히 분석할 것.
- node_modules, .venv, dist, 원본 데이터·로그 파일 등은 탐색에서 제외할 것.
- 개발 용어는 괄호 안에 비전공자도 이해할 수 있는 쉬운 풀이를 덧붙일 것.

[SPEC.md 필수 포함 항목]
1. 프로젝트 아키텍처 맵: 디렉토리·파일별 역할 요약 및 핵심 사용자 조작 흐름
2. 코드 구조 맵: 화면 고유 좌표(id/class) 및 백엔드 핵심 함수·API 라우트 입출력
3. 데이터 입출력 규칙: 참조 데이터셋명, 필수 컬럼명, 핵심 비즈니스 계산 공식
4. 하드코딩된 설정값 목록: 경로·컬럼명·임계값이 박혀 있는 실제 파일명과 위치 나열
5. 핵심 불변 규칙: 프론트-백엔드 간 API 경로, 요청/응답 JSON 키 규격 등
```

</div>
<div class="col-span-5 space-y-2.5 text-xs">
  <div class="p-3 rounded-xl bg-blue-50 border border-blue-200">
    <div class="font-bold text-blue-800 text-sm mb-1">프로젝트 단위 역추출 원리</div>
    <div class="text-slate-700 leading-relaxed">특정 코드 조각을 일일이 복붙하는 대신, 에이전트가 <strong>코드 수정을 잠근 채 프로젝트 전체 구조를 스캔</strong>해 단숨에 SDD 기준점(<code>SPEC.md</code>)을 생성합니다.</div>
  </div>
  <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
    <div class="font-bold text-amber-800 text-sm mb-1">⚠️ 주의: 대규모 토큰 소모 위험</div>
    <div class="text-slate-700 leading-relaxed">프로젝트 전체를 무작정 읽게 하면 패키지 폴더(<code>node_modules</code>, <code>.venv</code>), 빌드 산출물, 대용량 데이터셋까지 스캔하여 <strong>토큰이 폭발적으로 소모되고 분석 정확도도 급감</strong>합니다.</div>
  </div>
  <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200">
    <div class="font-bold text-emerald-800 text-sm mb-1">💡 추천 효율화 전략: 2단계 탑다운 스캔</div>
    <div class="text-slate-700 leading-relaxed">
      <strong>① 트리 먼저 스캔:</strong> 폴더·파일 목록만 먼저 읽게 해 핵심 소스 파일(<code>app.py</code>, <code>index.html</code> 등)만 타겟팅<br/>
      <strong>② 탐색 제외 강제:</strong> 데이터·의존성 폴더를 제외 지정한 뒤 선별된 핵심 파일만 분석해 토큰 80%+ 절감
    </div>
  </div>
</div>
</div>

<!--
[Slide 2-5 · [실전 처방] 문서 없는 기존 프로젝트에 스펙 심기 (Reverse-Spec Extraction)]
- 특정 코드 블록이 아닌 프로젝트 전체에 대해 수행하는 마스터 역추출 프롬프트
- 주의사항: 프로젝트 전체 스캔 시 토큰 소모가 극심할 수 있으므로, 1단계 파일 트리 스캔 후 핵심 소스만 선별 분석하는 '2단계 탑다운(Top-Down) 스캔 & 탐색 제외' 효율화 전략 권장
-->

---

# [Module 2] 추출한 `SPEC.md` 실무 운영 3단계 루프
## 역추출 → 현업 도메인 교정 → 수정 완료 후 스펙 동기화 (Slide 2-6)

<div class="grid grid-cols-3 gap-3 mt-2 mb-3 text-xs">
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
    <div class="font-bold text-slate-800 text-sm mb-1">1단계 · 역추출 (AI)</div>
    <div class="text-slate-600 leading-relaxed">마스터 프롬프트로 현재 코드에서 <code>SPEC.md</code> 초안 추출</div>
  </div>
  <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
    <div class="font-bold text-amber-800 text-sm mb-1">2단계 · 현업 도메인 교정 (사람)</div>
    <div class="text-slate-700 leading-relaxed">비전공자 담당자가 한국어 <code>SPEC.md</code>를 읽으며 <em>"이 판정 공식은 원래 이렇게 계산해야 해"</em>처럼 업무 로직 오류를 텍스트로 직접 교정</div>
  </div>
  <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200">
    <div class="font-bold text-emerald-800 text-sm mb-1">3단계 · 수정 후 스펙 동기화 (AI)</div>
    <div class="text-slate-700 leading-relaxed">기능 추가나 버그 수정이 끝날 때마다 코드와 문서가 다시 어긋나지 않도록 <code>SPEC.md</code>와 변경 이력(Changelog)을 함께 업데이트</div>
  </div>
</div>

<div class="font-bold text-xs text-slate-600 mb-1">스펙 동기화 마무리 프롬프트 전문 (Verbatim)</div>

```text
방금 우리가 수정한 코드 내용을 반영해서, 기존 `SPEC.md`의 변경된 부분만 업데이트해 줘.
맨 아래에 '변경 이력(Changelog)' 섹션을 만들고 오늘 날짜와 수정 사유 한 줄을 기록해 줘.
```

<!--
[Slide 2-6 · 추출한 SPEC.md 실무 운영 3단계 루프]
- 1단계: 역추출 (AI) → 2단계: 현업 도메인 교정 (사람) → 3단계: 수정 완료 후 스펙 동기화 (AI)
- 스펙 동기화 마무리 프롬프트 전문 수록
-->

---
layout: center
class: text-left
---

# 오늘 강의 세 줄 요약
## 바이브코딩 웹 서비스 운영·유지보수, 이것만 기억하세요

<div class="grid grid-cols-1 gap-3 mt-4">
  <div class="p-3 rounded-lg bg-blue-50 border border-blue-200">
    <div class="font-bold text-base text-blue-700">1. 코드보다 '명세(<code>SPEC.md</code>)'가 먼저입니다.</div>
    <div class="text-sm mt-1">문서를 먼저 세우고 수정 범위를 잠가야 AI가 기존 기능을 망가뜨리지 않습니다.</div>
  </div>
  <div class="p-3 rounded-lg bg-amber-50 border border-amber-200">
    <div class="font-bold text-base text-amber-700">2. '감'으로 고치지 말고 '로그와 <code>Diff</code>'로 진단하세요.</div>
    <div class="text-sm mt-1">장애가 나면 <code>F12</code>와 서버 로그 맨 아랫줄로 원인을 격리하고, 수정 후에는 반드시 <code>Diff</code>로 AI의 무단 삭제 여부를 검수합니다.</div>
  </div>
  <div class="p-3 rounded-lg bg-emerald-50 border border-emerald-200">
    <div class="font-bold text-base text-emerald-700">3. AI에게 시키기 전 반드시 '세이브(<code>Commit</code>)'하세요.</div>
    <div class="text-sm mt-1">Dataiku의 Git 버전 관리(<code>Branch</code> · <code>Commit</code> · <code>Revert</code>)는 비전공자도 실패 걱정 없이 AI를 통제할 수 있는 가장 강력한 안전벨트입니다.</div>
  </div>
</div>

<!--
[Slide End · Conclusion — 오늘 강의 세 줄 요약 (마지막 장 고정)]
- 제약 4 준수: 프레젠테이션의 맨 마지막 슬라이드는 반드시 지정된 「오늘 강의 세 줄 요약」 슬라이드로 마무리합니다.
- 강의 포인트:
  1. 코드보다 '명세(SPEC.md)'가 먼저입니다.
  2. '감'으로 고치지 말고 '로그와 Diff'로 진단하세요.
  3. AI에게 시키기 전 반드시 '세이브(Commit)'하세요.
-->
