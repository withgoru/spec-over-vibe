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

# [TODO: Intro 슬라이드 직접 작성 영역]

강의 표지, 강사 소개, 교육 배경 및 전체 아젠다(이론 2시간 + 시연 1시간)를 이 위치에 작성합니다.

<!--
[Slide 0 · Cover / Intro Placeholder]
- 제약 2 준수: 표지(Cover) 및 도입부(Intro)는 강사가 직접 작성할 예정이므로 플레이스홀더만 배치합니다.
- 이후 Module 1 ~ Module 4 및 Live Demo 슬라이드가 이 아래에 이어집니다.
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
