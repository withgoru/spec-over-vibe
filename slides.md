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

# 최우영
## Owner of KickcodePlus | Web Developer | Lecturer

<div class="grid grid-cols-12 gap-4 mt-3 text-xs items-stretch">
  <div class="col-span-5 flex flex-col justify-between p-4 rounded-xl bg-slate-50 border border-slate-200">
    <div>
      <div class="flex items-center justify-between mb-2">
        <div>
          <div class="text-base font-bold text-slate-900">최우영 (goru)</div>
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

<div class="mt-3 p-2.5 rounded-lg bg-blue-50 border-l-4 border-blue-500 text-sm">
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
    <div class="p-2.5 rounded-lg bg-red-50 border-l-4 border-red-500">
      <div class="font-bold text-red-700">하드코딩 (Hardcoding)</div>
      <div class="mt-1">데이터셋 이름, 컬럼명(<code>LOT_ID</code>, <code>MEAS_VAL</code>), 공정 판정 기준치(<code>수율 85.0%</code>), 파일 경로가 코드 중간중간에 직접 박혀 있는 상태</div>
    </div>
    <div class="p-2.5 rounded-lg bg-amber-50 border-l-4 border-amber-500">
      <div class="font-bold text-amber-700">현업 운영 리스크</div>
      <div class="mt-1">공정 기준치가 <code>85% → 88%</code>로 바뀌거나 원본 테이블 컬럼명이 바뀔 때마다 코드 전체를 뒤져 수정해야 하며, 한 곳이라도 놓치면 서비스 오작동</div>
    </div>
    <div class="p-2.5 rounded-lg bg-emerald-50 border-l-4 border-emerald-500">
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
layout: center
class: text-left
---

# 오늘 강의 세 줄 요약
## 바이브코딩 웹 서비스 운영·유지보수, 이것만 기억하세요

<div class="grid grid-cols-1 gap-3 mt-4">
  <div class="p-3 rounded-lg bg-blue-50 border-l-4 border-blue-500">
    <div class="font-bold text-base text-blue-700">1. 코드보다 '명세(<code>SPEC.md</code>)'가 먼저입니다.</div>
    <div class="text-sm mt-1">문서를 먼저 세우고 수정 범위를 잠가야 AI가 기존 기능을 망가뜨리지 않습니다.</div>
  </div>
  <div class="p-3 rounded-lg bg-amber-50 border-l-4 border-amber-500">
    <div class="font-bold text-base text-amber-700">2. '감'으로 고치지 말고 '로그와 <code>Diff</code>'로 진단하세요.</div>
    <div class="text-sm mt-1">장애가 나면 <code>F12</code>와 서버 로그 맨 아랫줄로 원인을 격리하고, 수정 후에는 반드시 <code>Diff</code>로 AI의 무단 삭제 여부를 검수합니다.</div>
  </div>
  <div class="p-3 rounded-lg bg-emerald-50 border-l-4 border-emerald-500">
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
