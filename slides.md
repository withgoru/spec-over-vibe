---
theme: default
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
layout: center
class: text-left
---

# 오늘 강의 세 줄 요약
## 바이브코딩 웹 서비스 운영·유지보수, 이것만 기억하세요

<div class="grid grid-cols-1 gap-4 mt-6">
  <div class="p-4 rounded-lg bg-blue-50 dark:bg-blue-900/20 border-l-4 border-blue-500">
    <div class="font-bold text-lg text-blue-700 dark:text-blue-300">1. 코드보다 '명세(<code>SPEC.md</code>)'가 먼저입니다.</div>
    <div class="text-sm mt-1 opacity-90">문서를 먼저 세우고 수정 범위를 잠가야 AI가 기존 기능을 망가뜨리지 않습니다.</div>
  </div>
  <div class="p-4 rounded-lg bg-amber-50 dark:bg-amber-900/20 border-l-4 border-amber-500">
    <div class="font-bold text-lg text-amber-700 dark:text-amber-300">2. '감'으로 고치지 말고 '로그와 <code>Diff</code>'로 진단하세요.</div>
    <div class="text-sm mt-1 opacity-90">장애가 나면 <code>F12</code>와 서버 로그 맨 아랫줄로 원인을 격리하고, 수정 후에는 반드시 <code>Diff</code>로 AI의 무단 삭제 여부를 검수합니다.</div>
  </div>
  <div class="p-4 rounded-lg bg-emerald-50 dark:bg-emerald-900/20 border-l-4 border-emerald-500">
    <div class="font-bold text-lg text-emerald-700 dark:text-emerald-300">3. AI에게 시키기 전 반드시 '세이브(<code>Commit</code>)'하세요.</div>
    <div class="text-sm mt-1 opacity-90">Dataiku의 Git 버전 관리(<code>Branch</code> · <code>Commit</code> · <code>Revert</code>)는 비전공자도 실패 걱정 없이 AI를 통제할 수 있는 가장 강력한 안전벨트입니다.</div>
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
