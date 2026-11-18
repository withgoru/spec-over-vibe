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

# [Module 3] 일반 외부 AI vs Dataiku Cobuild — 왜 안전벨트가 필수인가?
## 프로젝트 파일을 직접 수정하는 Cobuild의 특성과 통제 장치 (Slide 3-1)

<div class="mt-3 text-xs">

| 비교 항목 | 외부 AI 도구 활용 (ChatGPT 등) | **Dataiku Cobuild 활용** |
| :--- | :--- | :--- |
| **작업 방식** | 대화창에서 코드 생성 후 **수동 복사·붙여넣기** | 프로젝트 내에서 **실제 Flow·레시피·Webapp을 직접 생성/수정** |
| **데이터·구조 이해** | 사용자가 스키마와 코드를 매번 설명해야 함 | **프로젝트 내 데이터셋 스키마·Flow 맥락을 자동 인식** |
| **실수 시 위험도** | 붙여넣기 전까지는 기존 서비스에 영향 없음 | **지시가 모호하면 작동 중인 기존 코드가 즉시 덮어씌워짐** |
| **복구 및 추적 수단** | 사용자가 수동으로 백업 파일을 따로 저장해야 함 | **Dataiku 내장 Git(Version Control)으로 이력 추적 및 복구** |

</div>

<div class="mt-3 p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs leading-relaxed">
  <strong class="text-amber-800">핵심 포인트:</strong> Cobuild는 프로젝트 파일을 직접 고쳐주는 유능한 조수입니다. 작업 지시서(<code>SPEC.md</code>)와 복구 장치(Git) 없이 구두로만 지시하면 멀쩡한 기능까지 한순간에 덮어쓸 수 있습니다.
</div>

<!--
[Slide 3-1 · 일반 외부 AI vs Dataiku Cobuild — 왜 안전벨트가 필수인가?]
> 강의 포인트: "Cobuild는 프로젝트 파일을 직접 고쳐주는 유능한 조수입니다. 작업 지시서(`SPEC.md`)와 복구 장치(Git) 없이 구두로만 지시하면 멀쩡한 기능까지 한순간에 덮어쓸 수 있습니다."
-->

---

# [Module 3] 비전공자를 위한 Git 핵심 용어 ① — 기록과 복구
## 터미널 명령어 없이 Dataiku 상단 `Version Control` 메뉴의 4가지 동작 의미만 파악 (Slide 3-2)

<div class="mt-2 text-xs">

| Git 핵심 용어 | 비전공자 눈높이 비유 | Dataiku 환경에서의 실제 용도와 의미 |
| :--- | :--- | :--- |
| **Repository (저장소)** | 프로젝트 전체가 담긴 **전용 금고** | Flow, 데이터셋 설정, Webapp(HTML/Python) 코드의 모든 변경 역사가 저장되는 공간. Dataiku는 프로젝트 생성 시 **내부 로컬 저장소**를 기본 제공 |
| **Commit (커밋)** | 게임의 **'세이브 포인트'** | 특정 시점의 프로젝트 상태를 스냅샷으로 기록하는 행위. AI 수정 직전(정상 상태)과 직후(검증 완료)에 반드시 기준점을 남겨야 함 |
| **Diff (변경점 비교)** | 수정 전후 **'틀린 그림 찾기'** | `History` 탭에서 두 커밋을 비교할 때 사용. 추가(`+`, 초록)·삭제(`-`, 빨강) 줄을 보여주어 **AI가 기존 기능을 몰래 지웠는지 10초 만에 검수** |
| **Revert (되돌리기)** | 장애 시 누르는 **'타임머신'** | 특정 커밋의 변경을 취소하는 새 커밋을 생성해 이전 정상 상태로 안전 복원 (과거 기록을 지우지 않아 복구 이력까지 투명하게 보존) |

</div>

<!--
[Slide 3-2 · 비전공자를 위한 Git 핵심 용어 ① — 기록과 복구 (내 프로젝트의 안전벨트)]
- 터미널 명령어를 외울 필요 없이 Dataiku 상단 Version Control 메뉴의 4가지 동작(Repository, Commit, Diff, Revert) 의미만 파악
-->

---

# [Module 3] 비전공자를 위한 Git 핵심 용어 ② — 실험·병합과 원격 동기화
## 운영 서비스를 보호하는 평행우주(`Branch`)와 중앙 금고(`Remote`) 동기화 (Slide 3-3)

<div class="mt-1 text-xs">

| 구분 | Git 핵심 용어 | 비전공자 눈높이 비유 | 실제 용도와 타이밍 |
| :--- | :--- | :--- | :--- |
| **실험과 병합**<br>(운영 보호) | **Branch (브랜치)** | 운영 서비스를 보호하는 **'평행우주 작업선'** | 실제 사용자가 쓰는 `main` 줄기를 건드리지 않고 새 기능·리팩토링을 실험하는 독립 공간 |
| **실험과 병합** | **Switch / Checkout** | 작업할 **평행우주 선택하기** | 현재 작업 중인 브랜치를 다른 브랜치로 전환 (예: `main` → `feat-defect-rate`) |
| **실험과 병합** | **Merge (병합)** | 검증 끝난 실험 결과를 **본진에 합치기** | 테스트가 완료된 실험 브랜치의 수정 사항을 운영(`main`) 브랜치로 통합 |
| **실험과 병합** | **Conflict (충돌)** | **"둘 중 뭘 살릴지 사람이 골라주세요"** | 두 브랜치(또는 두 사람)가 같은 코드 줄을 다르게 고쳤을 때 임의 덮어쓰기를 막는 안전장치 |
| **원격 동기화**<br>(사내 Git 서버) | **Remote (원격 저장소)** | 사내 중앙 클라우드 금고 | Dataiku 외부의 중앙 Git 서버(GitHub/GitLab 등). 팀 공유 및 이중 백업용 |
| **원격 동기화** | **Push / Fetch / Pull** | **업로드 / 미리보기 / 다운로드 반영** | `Push`(내 커밋 업로드), `Fetch`(변경 유무 확인만), `Pull`(동료 최신판 내려받아 합치기) |

</div>

<!--
[Slide 3-3 · 비전공자를 위한 Git 핵심 용어 ② — 실험·병합과 원격 동기화]
- 그룹 2 (실험과 병합): Branch, Switch / Checkout, Merge, Conflict
- 그룹 3 (원격 동기화): Remote, Push / Fetch / Pull
-->

---

# [Module 3] 상황별 Git 버튼 선택 가이드 & 5단계 표준 루틴
## 현업 상황별 즉시 대응법과 Cobuild + SDD + Git 표준 유지보수 루틴 (Slide 3-4)

<div class="space-y-1.5 mt-2 text-xs">
  <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 flex items-center justify-between">
    <span><strong>"Cobuild로 웹앱 기능을 대폭 고치려고 해요"</strong></span>
    <span class="text-blue-700 font-semibold">→ 먼저 새 <code>Branch</code>를 생성해 <code>main</code>을 보호한 뒤 작업 시작</span>
  </div>
  <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 flex items-center justify-between">
    <span><strong>"AI가 코드를 고쳤는데 뭔가 찝찝해요"</strong></span>
    <span class="text-amber-700 font-semibold">→ <code>Version Control</code> → <code>Diff</code>를 열어 빨간색(<code>-</code>) 핵심 함수 삭제 여부 확인</span>
  </div>
  <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 flex items-center justify-between">
    <span><strong>"AI 수정 후 웹앱이 하얗게 뻗고 에러가 나요"</strong></span>
    <span class="text-red-700 font-semibold">→ 씨름하지 말고 직전 정상 커밋을 찾아 <code>Revert</code>로 3초 만에 원상복구</span>
  </div>
  <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 flex items-center justify-between">
    <span><strong>"수정이 완벽히 끝났고 팀원에게 공유해야 해요"</strong></span>
    <span class="text-emerald-700 font-semibold">→ 작업 브랜치를 <code>main</code>에 <code>Merge</code>한 뒤 <code>Push</code>로 중앙 서버 업로드</span>
  </div>
  <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 flex items-center justify-between">
    <span><strong>"어제 동료가 고친 프로젝트에 이어서 작업할 거예요"</strong></span>
    <span class="text-indigo-700 font-semibold">→ 무작정 수정부터 하지 말고 먼저 <code>Pull</code>을 눌러 최신 코드부터 반영</span>
  </div>
</div>

<div class="mt-3 p-3 rounded-xl bg-blue-50/60 border border-blue-200">
  <div class="text-xs font-bold text-blue-900 mb-2">Cobuild + SDD + Git 표준 5단계 유지보수 루틴</div>
  <div class="grid grid-cols-5 gap-2 text-center text-xs">
    <div class="p-2 rounded-lg bg-white border border-blue-200">
      <div class="font-bold text-blue-800">1단계 · 작업 전 세이브</div>
      <div class="text-[11px] text-slate-600 mt-0.5">정상 상태 <code>Commit</code> 확인</div>
    </div>
    <div class="p-2 rounded-lg bg-white border border-blue-200">
      <div class="font-bold text-blue-800">2단계 · 명세 기반 지시</div>
      <div class="text-[11px] text-slate-600 mt-0.5"><code>SPEC.md</code> 제약조건 주입</div>
    </div>
    <div class="p-2 rounded-lg bg-white border border-amber-200">
      <div class="font-bold text-amber-800">3단계 · Diff 검수</div>
      <div class="text-[11px] text-slate-600 mt-0.5">빨간색(<code>-</code>) 무단 삭제 체크</div>
    </div>
    <div class="p-2 rounded-lg bg-white border border-emerald-200">
      <div class="font-bold text-emerald-800">4단계 · 테스트 & 분기</div>
      <div class="text-[11px] text-slate-600 mt-0.5">성공 시 <code>Commit</code> / 실패 시 <code>Revert</code></div>
    </div>
    <div class="p-2 rounded-lg bg-white border border-slate-300">
      <div class="font-bold text-slate-800">5단계 · SPEC 동기화</div>
      <div class="text-[11px] text-slate-600 mt-0.5">변경 이력(<code>Changelog</code>) 기록</div>
    </div>
  </div>
</div>

<!--
[Slide 3-4 · 상황별 Git 버튼 선택 가이드 & Cobuild+SDD+Git 5단계 표준 루틴]
- 5가지 현업 상황별 Git 버튼(Branch, Diff, Revert, Merge+Push, Pull) 선택 가이드
- Cobuild + SDD + Git 표준 5단계 유지보수 루틴 다이어그램
-->

---

# [Module 3] 유지보수형 프롬프팅 3대 기법 ① — 계획 먼저 승인
## Plan-Before-Code: 코드 생성 전에 수정 계획(Change Spec)부터 브리핑받기 (Slide 3-5)

<div class="p-3 rounded-lg bg-blue-50 border border-blue-200 text-xs mt-2 mb-3 leading-relaxed">
  <strong class="text-blue-800">핵심 원리:</strong> AI가 코드를 짜기 전에 <em>"어느 파일의 어떤 좌표/함수를 왜 고칠 것인지"</em> 수정 계획(Change Spec)부터 브리핑하게 만들어 잘못된 방향의 수정을 코드 생성 전에 차단합니다.
</div>

<div class="font-bold text-xs text-slate-600 mb-1.5">프롬프트 템플릿 전문 (Verbatim)</div>

```text
아래 `SPEC.md`와 현재 코드를 참고해서 [요청 기능: 조회 결과 표에 '불량률(%)' 컬럼 추가]를 구현하려고 해.

⚠️ 주의: 지금은 절대 코드를 작성하지 마.
먼저 아래 3가지만 5줄 이내로 설명해 줘.
1. 수정이 필요한 파일과 정확한 위치(HTML id 좌표 또는 Python 함수명)
2. 기존 기능(수율 계산 및 합격 판정 배지)에 영향을 줄 가능성 여부
3. 변경될 데이터 입출력(JSON 키) 구조
```

<!--
[Slide 3-5 · 유지보수형 프롬프팅 3대 기법 ① — 계획 먼저 승인 (Plan-Before-Code)]
- AI가 코드를 짜기 전에 어느 파일의 어떤 좌표/함수를 왜 고칠 것인지 수정 계획(Change Spec)부터 브리핑하게 만들어 잘못된 방향의 수정을 코드 생성 전에 차단
-->

---

# [Module 3] 유지보수형 프롬프팅 3대 기법 ② — 수정 범위 잠금
## Guardrails & Diff: Whitelist/Blacklist 지정 및 코드 생략(`...`) 금지 (Slide 3-6)

<div class="p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs mt-2 mb-3 leading-relaxed">
  <strong class="text-amber-800">핵심 원리:</strong> 수정 허용 범위(Whitelist)와 수정 금지 영역(Blacklist)을 명시하고, <code># ... 기존 코드 생략 ...</code> 출력을 금지하여 코드 유실 사고를 원천 차단합니다.
</div>

<div class="font-bold text-xs text-slate-600 mb-1.5">프롬프트 템플릿 전문 (Verbatim)</div>

```text
방금 설명한 계획대로 코드를 수정해 줘. 단, 아래 제약조건을 반드시 지켜야 해.

[수정 범위 잠금 규칙]
1. 수정 허용 영역: Python의 `calc_yield()` 함수와 HTML의 `id="result-table"` 영역만 수정할 것.
2. 수정 금지 영역: 기존의 API 경로(`/api/yield`), `CONFIG` 설정 구조, 상단 요약 카드 로직은 한 글자도 바꾸지 말 것.
3. 출력 규칙: 코드를 중간에 줄이거나 생략(`...`)하지 말고, 수정된 함수/영역의 전체 코드를 빠짐없이 출력할 것.
```

<!--
[Slide 3-6 · 유지보수형 프롬프팅 3대 기법 ② — 수정 범위 잠금 (Guardrails & Diff)]
- 수정 허용 범위(Whitelist)와 수정 금지 영역(Blacklist)을 명시하고, `# ... 기존 코드 생략 ...` 출력을 금지하여 코드 유실 사고 원천 차단
-->

---

# [Module 3] 유지보수형 프롬프팅 3대 기법 ③ — 오류 로그 기반 역질문
## Error-Driven Debugging: 3종 세트 버그 리포트와 원인 후보 선(先) 진단 (Slide 3-7)

<div class="p-3 rounded-lg bg-emerald-50 border border-emerald-200 text-xs mt-2 mb-3 leading-relaxed">
  <strong class="text-emerald-800">핵심 원리:</strong> 오류가 발생했을 때 <em>"안 돼요, 고쳐주세요"</em> 대신 <strong>3종 세트 버그 리포트</strong>를 전달하고, <strong>즉시 수정을 금지한 채 원인 후보부터 진단</strong>하게 합니다.
</div>

<div class="font-bold text-xs text-slate-600 mb-1.5">프롬프트 템플릿 전문 (Verbatim)</div>

```text
현재 웹 서비스에서 아래와 같은 오류가 발생했어.
⚠️ 바로 수정 코드를 주지 말고, 먼저 원인을 분석해서 가장 유력한 원인 후보 3가지와 확인 방법부터 알려줘.

1. 발생 현상: 조회 버튼 클릭 시 표가 그려지지 않고 로딩 상태에서 멈춤
2. 에러 로그 원문:
   - 브라우저 F12 Network: `500 Internal Server Error`
   - 서버 Python Log 맨 아랫줄: `ZeroDivisionError: division by zero`
3. 오류가 발생한 관련 코드 블록:
   (여기에 Python `calc_yield()` 함수 코드만 붙여넣기)
```

<!--
[Slide 3-7 · 유지보수형 프롬프팅 3대 기법 ③ — 오류 로그 기반 역질문 (Error-Driven Debugging)]
- 오류가 발생했을 때 "안 돼요, 고쳐주세요" 대신 3종 세트 버그 리포트를 전달하고, 즉시 수정을 금지한 채 원인 후보부터 진단
-->

---

# [Module 4] 장애 격리(Fault Isolation) — 오류 발생 지점 이분법 진단
## 서비스가 멈췄을 때 30초 만에 범인이 화면(Browser)인지 서버(Python)인지 가르는 진단 트리 (Slide 4-1)

<div class="mt-2 p-2.5 rounded-xl bg-slate-100 border border-slate-300 text-center text-xs font-bold text-slate-800">
  🚨 출발: [장애 발생 — 화면이 안 나오거나 버튼이 먹통일 때] &nbsp;→&nbsp; 브라우저에서 <code>F12</code> (개발자 도구) 열기
</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs">
  <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 space-y-2">
    <div class="font-bold text-amber-900 text-sm">분기 A · Console 빨간 에러 / Network 요청 미전송</div>
    <div class="p-2 rounded bg-white border border-amber-200 font-bold text-amber-800 text-center">
      ▶ 프론트엔드 (HTML / JS) 오류 확정
    </div>
    <div class="text-slate-700 leading-relaxed">
      <strong>주요 원인:</strong><br/>
      • HTML 버튼·테이블 <code>id</code> 좌표 불일치<br/>
      • JavaScript 문법 오류 또는 이벤트 함수 연결 누락<br/>
      • 서버에서 받은 JSON 키 이름 오타 (예: <code>yieldRate</code> vs <code>yield_rate</code>)
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-red-50 border border-red-200 space-y-2">
    <div class="font-bold text-red-900 text-sm">분기 B · Network 탭 빨간 줄 (<code>Status 500</code> 등)</div>
    <div class="p-2 rounded bg-white border border-red-200 font-bold text-red-800 text-center">
      ▶ 백엔드 (Python / 데이터) 오류 확정 (요청은 갔으나 서버 에러)
    </div>
    <div class="text-slate-700 leading-relaxed">
      <strong>즉시 조치:</strong><br/>
      • Dataiku Webapp의 <strong><code>[Log]</code> 탭</strong> 열기<br/>
      • Python Traceback의 <strong>'맨 아랫줄'</strong> 에러명 복사 후 AI에 전달
    </div>
  </div>
</div>

<div class="mt-3 p-2.5 rounded-lg bg-blue-50 border border-blue-200 text-xs leading-relaxed">
  <strong class="text-blue-800">강의 포인트:</strong> Python 에러 로그(Traceback)는 수십 줄이 쏟아지지만, 비전공자는 <strong>가장 맨 아랫줄 2줄(<code>KeyError</code>, <code>ZeroDivisionError</code>, <code>TypeError</code>)</strong>만 복사해서 AI에게 주면 됩니다.
</div>

<!--
[Slide 4-1 · 장애 격리(Fault Isolation) — 오류 발생 지점 이분법 진단]
> 강의 포인트: "Python 에러 로그(Traceback)는 수십 줄이 쏟아지지만, 비전공자는 가장 맨 아랫줄 2줄(KeyError, ZeroDivisionError, TypeError)만 복사해서 AI에게 주면 됩니다."
-->

---

# [Module 4] 코드는 그대로인데 서비스가 죽는 주원인: 데이터 스키마 드리프트
## 코드 수정 없이 갑자기 500 에러가 터지는 원인의 80% = 원본 데이터의 변화 (Slide 4-2)

<div class="mt-3 text-xs">

| 데이터 변화 유형 | 현업 발생 사례 | 서버에서 터지는 Python 에러 | 사전 방어 코딩 패턴 |
| :--- | :--- | :--- | :--- |
| **컬럼명 변경** | 원본 엑셀/DB의 `GOOD_CNT`가 `GOOD_QTY`로 변경 | `KeyError: 'GOOD_CNT'` | 시작 시 필수 컬럼 존재 여부 검증 및 안내 메시지 반환 |
| **결측치(`Null`/`NaN`) 유입** | 미측정 배치의 수량 칸이 비어 있음 | `TypeError: unsupported operand type(s) for /: 'NoneType'` | 연산 전 `fillna(0)` 또는 `None` 체크 방어 로직 필수 |
| **0 나누기 (`0` 유입)** | 가동 중단 배치의 총 생산수량(`TOTAL`)이 `0` | `ZeroDivisionError: division by zero` | 분모가 `0`일 때 `0.0`을 반환하는 조건문 추가 |
| **조건 일치 0건** | 해당 날짜에 생산 데이터가 0건 조회됨 | 빈 배열 통계 계산 시 `IndexError` / `NaN` JSON 오류 | `if len(df) == 0:` 시 빈 결과 안내 응답 분기 처리 |

</div>

<!--
[Slide 4-2 · 코드는 그대로인데 서비스가 죽는 주원인: 데이터 스키마 드리프트]
- 어제까지 멀쩡히 돌아가던 웹 서비스가 코드 수정 없이 갑자기 500 에러를 뿜는 원인의 80% = 원본 데이터의 변화(Data Schema Drift)
-->

---

# [Module 4] 회귀 버그(Regression Bug) 예방과 현업 수정 요청(CR) 3분류 기준
## 수정 크기에 따라 안전 절차의 강도를 다르게 적용하는 운영 원칙 (Slide 4-3)

<div class="p-3 rounded-lg bg-red-50 border border-red-200 text-xs mt-2 mb-3 leading-relaxed">
  <strong class="text-red-800">회귀 버그 (Regression Bug):</strong> 기능 A를 고쳤는데 전혀 상관없어 보이던 기능 B가 망가지는 현상 (함수 간 강한 결합도 또는 AI의 코드 생략·덮어쓰기로 발생)
</div>

<div class="font-bold text-xs text-slate-600 mb-2">현업 사용자 수정 요청(CR) 3단계 분류 및 대응 기준</div>

<div class="grid grid-cols-3 gap-3 text-xs">
  <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 space-y-1.5">
    <div class="font-bold text-amber-900 text-sm">등급 1 · 긴급 버그 수정 (Hotfix)</div>
    <div class="text-slate-600"><strong>대상:</strong> 기존 기능 오작동 · 500 에러</div>
    <div class="pt-1.5 border-t border-amber-200 text-slate-800 font-medium leading-relaxed">
      즉시 로그 격리 진단 → 최소 범위 수정 후 <code>Commit</code>
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-blue-50 border border-blue-200 space-y-1.5">
    <div class="font-bold text-blue-900 text-sm">등급 2 · 단순 UI·기준값 개선 (Minor)</div>
    <div class="text-slate-600"><strong>대상:</strong> 문구 수정, 색상 변경, <code>CONFIG</code> 임계값 조정</div>
    <div class="pt-1.5 border-t border-blue-200 text-slate-800 font-medium leading-relaxed">
      <code>CONFIG</code> 또는 CSS만 수정 (핵심 데이터 로직 접촉 금지)
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 space-y-1.5">
    <div class="font-bold text-emerald-900 text-sm">등급 3 · 신규 기능 추가 (Feature)</div>
    <div class="text-slate-600"><strong>대상:</strong> 새 차트, 새 계산 컬럼, 필터 추가</div>
    <div class="pt-1.5 border-t border-emerald-200 text-slate-800 font-medium leading-relaxed">
      <strong>반드시 새 <code>Branch</code> 생성 → <code>SPEC.md</code> 기반 <code>Plan-Before-Code</code> → 테스트 후 <code>Merge</code></strong>
    </div>
  </div>
</div>

<!--
[Slide 4-3 · 회귀 버그(Regression Bug) 예방과 현업 수정 요청(CR) 3분류 기준]
- 등급 1(Hotfix), 등급 2(Minor), 등급 3(Feature)별 차별화된 유지보수 통제 기준
-->

---

# [Module 4] 배포 전·후 웹 서비스 운영·유지보수 최종 체크리스트
## 실무 투입 및 수정 배포 시 반드시 점검해야 할 5대 안전 항목 (Slide 4-4)

<div class="space-y-2.5 mt-3 text-xs">
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-3">
    <span class="px-2.5 py-1 rounded-md bg-blue-100 text-blue-800 font-bold shrink-0">1. 설계·문서</span>
    <span class="text-slate-800 font-medium">현재 서비스의 기준 문서(<code>SPEC.md</code>)가 존재하며, 이번 수정 사항이 반영되었는가?</span>
  </div>
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-3">
    <span class="px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-800 font-bold shrink-0">2. 설정 분리</span>
    <span class="text-slate-800 font-medium">데이터셋 이름, 컬럼명, 판정 임계값, 경로가 코드 중간이 아닌 최상단 <code>CONFIG</code>에 모여 있는가?</span>
  </div>
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-3">
    <span class="px-2.5 py-1 rounded-md bg-amber-100 text-amber-800 font-bold shrink-0">3. 예외 방어</span>
    <span class="text-slate-800 font-medium">결측치(<code>Null</code>), 분모 <code>0</code>, 조회 결과 <code>0건</code> 데이터를 넣었을 때 서버가 500 에러로 뻗지 않는가?</span>
  </div>
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-3">
    <span class="px-2.5 py-1 rounded-md bg-emerald-100 text-emerald-800 font-bold shrink-0">4. 버전 관리</span>
    <span class="text-slate-800 font-medium">수정 전 정상 시점의 <code>Commit</code>이 기록되어 있고, 수정 후 <code>Diff</code>로 무단 삭제된 코드가 없는지 확인했는가?</span>
  </div>
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-3">
    <span class="px-2.5 py-1 rounded-md bg-rose-100 text-rose-800 font-bold shrink-0">5. 장애 대비</span>
    <span class="text-slate-800 font-medium">장애 발생 시 브라우저 <code>F12</code>와 서버 <code>Log</code> 탭에서 에러 메시지를 확인할 수 있는 상태인가?</span>
  </div>
</div>

<!--
[Slide 4-4 · 배포 전·후 웹 서비스 운영·유지보수 최종 체크리스트]
- 5대 최종 점검표: [설계·문서], [설정 분리], [예외 방어], [버전 관리], [장애 대비]
-->

---

# [Live Demo] 라이브 시연 소개: 초간단 샘플 앱 (`공정 배치 수율 판정기`)
## "고장 내고 → 원인 찾고(F12 · 로그 · Diff) → 프롬프트로 안전하게 고치기" (Slide D-0)

<div class="grid grid-cols-12 gap-4 text-xs items-start">
<div class="col-span-5 space-y-2.5">
  <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
    <div class="font-bold text-slate-800 text-sm mb-1">시연 환경 (Dataiku 1:1 동일 구조)</div>
    <div class="text-slate-600 leading-relaxed">Python(Flask) 백엔드 + HTML/JS 프론트엔드 + Git 버전 관리 (Dataiku Webapp 및 Version Control과 1:1 동일 구조)</div>
  </div>
  <div class="p-3 rounded-xl bg-blue-50 border border-blue-200 space-y-1.5">
    <div class="font-bold text-blue-900 text-sm">초간단 샘플 코드 구조 (총 35줄 내외)</div>
    <div class="text-slate-700 leading-relaxed">
      <strong>• <code>app.py</code>:</strong> 배치 데이터 리스트를 받아 수율(<code>good / total * 100</code>)을 계산하고 <code>85.0</code> 이상이면 <code>"합격"</code>, 미만이면 <code>"불합격"</code>을 반환하는 초간단 서버
    </div>
    <div class="text-slate-700 leading-relaxed">
      <strong>• <code>index.html</code>:</strong> <code>[전체 조회]</code> 버튼과 <code>[합격만 보기]</code> 필터 버튼, 그리고 결과를 보여주는 표(<code>id="yield-table"</code>) 1개로 구성된 화면
    </div>
  </div>
</div>
<div class="col-span-7">

```python
from flask import Flask, jsonify
app = Flask(__name__)

BATCH_DATA = [
    {"batch": "B-01", "total": 100, "good": 92},
    {"batch": "B-02", "total": 200, "good": 160},
    {"batch": "B-03", "total": 150, "good": 141},
]

@app.route("/api/yield")
def get_yield():
    results = []
    for row in BATCH_DATA:
        # 판정 기준(85.0)과 컬럼명이 코드 중간에 하드코딩되어 있음
        rate = round(row["good"] / row["total"] * 100, 1)
        status = "합격" if rate >= 85.0 else "불합격"
        results.append({"batch": row["batch"], "rate": rate, "status": status})
    return jsonify(results)
```

</div>
</div>

<!--
[Slide D-0 · 라이브 시연 소개: 초간단 샘플 앱 (공정 배치 수율 판정기)]
- 시연 연출 핵심: 코드는 비전공자도 한눈에 읽을 수 있도록 20~35줄 내외의 극도로 단순한 샘플 앱을 사용합니다. 화려한 코딩이 아니라 "① 왜 고장 났는지 도구(F12 · 로그 · Diff)로 정확히 짚어내고 → ② 배운 프롬프트 공식으로 안전하게 해결하는 과정"을 라이브로 증명합니다.
-->

---

# [Live Demo · Act 1] 문서 없는 레거시 앱 해부 & `SPEC.md` 역추출 + `CONFIG` 분리
## 전임자가 남긴 하드코딩 레거시 코드를 3분 만에 SDD 체제로 전환하기 (Slide D-1 · 15분)

<div class="p-2.5 rounded-xl bg-slate-100 border border-slate-300 text-xs mb-3">
  <strong>🎬 상황 설정:</strong> 전임자가 바이브코딩으로 짜두고 간 문서 없는 초간단 앱. 판정 기준을 <code>85.0 → 90.0</code>으로 바꾸고 싶지만 어디를 고쳐야 할지 모르는 상태.
</div>

<div class="grid grid-cols-2 gap-4 text-xs">
  <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 space-y-2">
    <div class="font-bold text-amber-900 text-sm">1단계 · 원인 파악 (코드 독해)</div>
    <div class="p-2.5 rounded-lg bg-white border border-amber-200 text-slate-700 leading-relaxed">
      <strong>① 프론트엔드 좌표 확인:</strong><br/>
      브라우저 <code>F12</code>로 <code>index.html</code>의 표 좌표(<code>id="yield-table"</code>)와 API 주소(<code>/api/yield</code>) 확인
    </div>
    <div class="p-2.5 rounded-lg bg-white border border-amber-200 text-slate-700 leading-relaxed">
      <strong>② 백엔드 하드코딩 포착:</strong><br/>
      <code>app.py</code>를 열어 <code>85.0</code>이라는 숫자와 <code>"good"</code>, <code>"total"</code> 컬럼명이 로직 한가운데 하드코딩되어 있음을 포착
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 space-y-2">
    <div class="font-bold text-emerald-900 text-sm">2단계 · 프롬프트 해결 (역추출 & 리팩토링)</div>
    <div class="p-2.5 rounded-lg bg-white border border-emerald-200 text-slate-700 leading-relaxed">
      <strong>[프롬프트 1 실행 · 역추출]</strong><br/>
      Module 2의 <strong>마스터 역추출 프롬프트</strong>를 입력 → 20초 만에 <code>SPEC.md</code>(불변 규칙 + 하드코딩 위치 목록) 자동 생성
    </div>
    <div class="p-2.5 rounded-lg bg-white border border-emerald-200 text-slate-700 leading-relaxed">
      <strong>[프롬프트 2 실행 · <code>CONFIG</code> 분리]</strong><br/>
      <em>"추출된 <code>SPEC.md</code>의 4번 항목(하드코딩 목록)을 근거로, 기존 API 구조는 유지한 채 판정 기준치와 컬럼명을 파일 최상단 <code>CONFIG</code> 딕셔너리로 분리해 줘"</em> → 전환 후 <code>Commit</code>
    </div>
  </div>
</div>

<!--
[Slide D-1 · Act 1 (15분): 문서 없는 레거시 앱 해부 & SPEC.md 역추출 + CONFIG 분리]
- 1단계: 브라우저 F12로 id="yield-table" 및 /api/yield 확인, app.py 내 하드코딩 포착
- 2단계: 마스터 역추출 프롬프트로 SPEC.md 생성 후 CONFIG 딕셔너리 분리 및 Commit
-->

---

# [Live Demo · Act 2] 무맥락 지시로 기존 기능 증발 사고 유발 → Git `Diff` & `Revert`
## 비전공자 실수 패턴 재현과 Git 타임머신을 활용한 3초 복구 시연 (Slide D-2 · 15분)

<div class="p-2.5 rounded-xl bg-slate-100 border border-slate-300 text-xs mb-3">
  <strong>🎬 상황 설정:</strong> 현업 요청 <em>"표 디자인이 너무 밋밋하니 좀 깔끔하게 고쳐주세요"</em>를 비전공자 실수 패턴(무맥락 지시 + 전체 덮어쓰기) 그대로 AI에게 입력.
</div>

<div class="grid grid-cols-3 gap-3 text-xs">
  <div class="p-3.5 rounded-xl bg-red-50 border border-red-200 space-y-1.5">
    <div class="font-bold text-red-900 text-sm">1단계 · 의도적 사고 유발</div>
    <div class="text-slate-700 leading-relaxed">
      AI가 테이블 스타일을 예쁘게 바꾸면서, 기존에 있던 <strong><code>[합격만 보기]</code> 필터 버튼과 JS 필터 함수를 통째로 삭제</strong>해 버림 (회귀 버그 발생)
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 space-y-1.5">
    <div class="font-bold text-amber-900 text-sm">2단계 · 원인 파악 (Git <code>Diff</code> 검수)</div>
    <div class="text-slate-700 leading-relaxed">
      화면에서 필터 버튼이 사라진 것을 발견 → 즉시 Git <strong><code>Diff</code></strong> 화면 오픈<br/><br/>
      초록색(<code>+</code>) 스타일 코드 아래에 <strong>빨간색(<code>-</code>) 줄로 기존 <code>filterPassOnly()</code> 함수가 삭제된 결정적 증거</strong>를 수강생과 함께 확인
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 space-y-1.5">
    <div class="font-bold text-emerald-900 text-sm">3단계 · 복구 및 안전 작업선 확보</div>
    <div class="text-slate-700 leading-relaxed">
      AI에게 다시 고쳐달라고 조르는 대신 Git <strong><code>Revert</code></strong> 클릭 한 번으로 3초 만에 정상 상태 복원<br/><br/>
      이후 안전한 작업을 위해 새 <strong><code>Branch</code> (<code>feat/table-style</code>) 생성</strong> 후 범위 잠금 프롬프트로 스타일만 안전하게 적용
    </div>
  </div>
</div>

<!--
[Slide D-2 · Act 2 (15분): 무맥락 지시로 기존 기능 증발 사고 유발 → Git Diff 포착 & Revert 복구]
- 1단계: 무맥락 디자인 수정 지시로 [합격만 보기] 버튼 및 filterPassOnly() 삭제 사고 유발
- 2단계: Git Diff에서 빨간색(-) 삭제 줄 확인
- 3단계: Git Revert로 3초 복원 후 feat/table-style 브랜치에서 범위 잠금 프롬프트 적용
-->

---

# [Live Demo · Act 3] 결측치·0 데이터 유입 500 장애 유발 → 로그 격리 & 버그 리포트 해결
## F12 Network 탭과 서버 Traceback 맨 아랫줄로 30초 만에 원인 특정하기 (Slide D-3 · 15분)

<div class="p-2.5 rounded-xl bg-slate-100 border border-slate-300 text-xs mb-3">
  <strong>🎬 상황 설정:</strong> 원본 데이터셋(<code>BATCH_DATA</code>)에 현업에서 흔히 발생하는 불량 데이터 1행(<code>{"batch": "B-04", "total": 0, "good": None}</code>)이 유입된 상황.
</div>

<div class="grid grid-cols-3 gap-3 text-xs">
  <div class="p-3.5 rounded-xl bg-red-50 border border-red-200 space-y-1.5">
    <div class="font-bold text-red-900 text-sm">1단계 · 의도적 장애 유발</div>
    <div class="text-slate-700 leading-relaxed">
      브라우저에서 <code>[전체 조회]</code> 클릭 시 표가 아무것도 그려지지 않고 멈춤
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 space-y-1.5">
    <div class="font-bold text-amber-900 text-sm">2단계 · 원인 파악 (장애 격리 이분법)</div>
    <div class="text-slate-700 leading-relaxed">
      <strong>① 브라우저 <code>F12</code> → <code>Network</code> 탭:</strong><br/>
      <code>/api/yield</code> 요청이 빨간색 <strong><code>500 Internal Server Error</code></strong>로 실패 → <em>"화면 문제가 아니라 서버(Python) 문제다!"</em> 확정<br/><br/>
      <strong>② 서버 실행 <code>Log</code> 탭:</strong><br/>
      Python Traceback <strong>맨 아랫줄</strong>(<code>TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'</code>)로 원인 특정
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 space-y-1.5">
    <div class="font-bold text-emerald-900 text-sm">3단계 · 프롬프트 해결 (Error-Driven)</div>
    <div class="text-slate-700 leading-relaxed">
      <strong>[프롬프트 실행]</strong><br/>
      <code>[발생 현상 + 500 로그 및 Traceback 맨 아랫줄 + get_yield() 함수 코드]</code> 3종 세트를 넣고 <em>"바로 고치지 말고 원인 후보와 방어 대책부터 알려줘"</em> 지시 → <code>None</code> 결측치 처리 및 <code>total == 0</code> 방어 코드 적용 후 정상 출력 확인
    </div>
  </div>
</div>

<!--
[Slide D-3 · Act 3 (15분): 결측치·0 데이터 유입으로 500 장애 유발 → 로그 격리 & 버그 리포트 해결]
- 1단계: {"batch": "B-04", "total": 0, "good": None} 유입으로 장애 유발
- 2단계: F12 Network 500 에러 및 서버 Log Traceback 맨 아랫줄 TypeError 확인
- 3단계: 3종 세트 버그 리포트 및 Error-Driven 프롬프트로 방어 로직 적용
-->

---

# [Live Demo · Act 4] SDD 기반 신규 기능 추가 (`불량률(%)` 컬럼) & 스펙 동기화 완주
## Plan-Before-Code → Guardrails → Git Diff & Merge → SPEC.md 동기화 (Slide D-4 · 15분)

<div class="p-2.5 rounded-xl bg-slate-100 border border-slate-300 text-xs mb-3">
  <strong>🎬 상황 설정:</strong> 운영 중인 앱에 <strong><code>불량률(%)</code> (<code>100 - 수율</code>) 컬럼을 추가</strong>해 달라는 신규 기능 요청(CR 등급 3) 접수.
</div>

<div class="grid grid-cols-3 gap-3 text-xs">
  <div class="p-3.5 rounded-xl bg-blue-50 border border-blue-200 space-y-1.5">
    <div class="font-bold text-blue-900 text-sm">1단계 · 계획 승인 (<code>Plan-Before-Code</code>)</div>
    <div class="text-slate-700 leading-relaxed">
      작업 <code>Branch</code>에서 <code>SPEC.md</code>와 현재 코드를 함께 입력 → <em>"코드를 짜지 말고 수정할 위치와 기존 기능 영향 여부부터 5줄로 보고해 줘"</em> 실행<br/><br/>
      AI가 제안한 수정 계획(<code>get_yield()</code> 반환 키 추가 + <code>index.html</code> 테이블 열 추가)을 눈으로 승인
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-amber-50 border border-amber-200 space-y-1.5">
    <div class="font-bold text-amber-900 text-sm">2단계 · 수정 범위 잠금 (<code>Guardrails</code>)</div>
    <div class="text-slate-700 leading-relaxed">
      <em>"승인한 계획대로 수정하되, 기존 <code>rate</code>(수율)와 <code>status</code>(합격 판정) 로직은 절대 건드리지 말고 수정 함수 전체를 생략 없이 출력해 줘"</em> 실행
    </div>
  </div>
  <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 space-y-1.5">
    <div class="font-bold text-emerald-900 text-sm">3단계 · 최종 검수 및 문서 동기화</div>
    <div class="text-slate-700 leading-relaxed">
      Git <code>Diff</code>로 의도한 줄만 정확히 추가되었는지 확인 → <code>main</code> 브랜치로 <strong><code>Merge</code></strong><br/><br/>
      마무리로 <strong><code>SPEC.md</code> 동기화 프롬프트</strong>를 실행해 <code>불량률(%)</code> 스펙과 오늘 날짜 변경 이력(Changelog)을 기록하며 시연 종료
    </div>
  </div>
</div>

<!--
[Slide D-4 · Act 4 (15분): SDD 기반 신규 기능 추가 (불량률(%) 컬럼) & 스펙 동기화 완주]
- 1단계: Plan-Before-Code로 수정 위치 및 영향도 5줄 보고 승인
- 2단계: Guardrails 프롬프트로 기존 rate/status 로직 보호 및 전체 코드 출력
- 3단계: Git Diff 검수 → main Merge → SPEC.md 및 Changelog 동기화 마무리
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
