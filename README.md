# spec-over-vibe

> **바이브코딩 웹 서비스 구조 이해와 운영·유지보수 실전**  
> 감(Vibe)으로 시키는 바이브코딩에서, 명세(Spec)로 통제하는 SDD(Spec-Driven Development)로의 전환을 다루는 기업 특강 Slidev 교안 및 라이브 시연 저장소입니다.

---

## 1. 강의 개요 (Overview)

- **교육 대상:** Dataiku 및 바이브코딩을 활용해 웹 서비스를 개발·배포하는 현업 구성원(비개발자 주력) 및 데이터 사이언티스트(DS)
- **강의 구성:** 총 3시간 특강 (**이론 2시간 + 강사 라이브 시연 1시간**, 수강생 실습 없음)
- **핵심 목표:**
  1. **웹 서비스 구조 및 코드 좌표 해독력:** 클라이언트-서버 요청·응답 사이클과 웹 4요소(HTML/CSS/JS/Python)의 역할 및 고유 좌표(Coordinate) 독해
  2. **SDD(명세 기반 개발) 및 역방향 스펙 추출:** 문서 없는 레거시 코드에서 `SPEC.md`를 역추출하고 설정(`CONFIG`)을 분리해 유지보수 기준 수립
  3. **Dataiku Cobuild & Git 안전 통제:** 내장 Git 버전 관리(`Branch`, `Commit`, `Diff`, `Revert`, `Merge`)와 유지보수형 프롬프팅 3대 기법 체득

---

## 2. 커리큘럼 및 슬라이드 구성 (Curriculum)

| 파트 | 시간 | 주요 내용 | 슬라이드 범위 |
| :--- | :---: | :--- | :--- |
| **Intro** | - | 강의 표지, 강사 소개, 교육 배경 및 아젠다 (강사 직접 작성 영역) | `Slide 0` |
| **Module 1** | 50분 | 웹 서비스 동작 원리(요청·응답 사이클), 웹 4요소 코드 좌표 읽기, Dataiku Webapp 2가지 구현 구조, 하드코딩 vs `CONFIG` 분리 | `Slide 1-1 ~ 1-4` |
| **Module 2** | 25분 | 개발방법론 비교와 SDD(`SPEC.md`), 비전공자 바이브코딩 7대 실수 패턴 교정, 역방향 스펙 추출(`Reverse-Spec Extraction`) 및 3단계 루프 | `Slide 2-1 ~ 2-6` |
| **Module 3** | 25분 | 외부 AI vs Dataiku Cobuild, 비전공자용 Git 핵심 용어 12개, 5단계 표준 루틴, 유지보수형 프롬프팅 3대 기법 (`Plan-Before-Code`, 범위 잠금, 오류 역질문) | `Slide 3-1 ~ 3-7` |
| **Module 4** | 20분 | 장애 격리 이분법(F12 vs 서버 Log), 데이터 스키마 드리프트 4대 유형 방어, 회귀 버그 예방 및 CR 3등급 분류, 배포 전·후 5대 최종 체크리스트 | `Slide 4-1 ~ 4-4` |
| **Live Demo** | 60분 | 초간단 샘플 앱(`공정 배치 수율 판정기`) 기반 4막 시연: ① 레거시 해부 & `SPEC.md` 역추출/리팩토링 → ② 기능 증발 사고 & Git `Diff`/`Revert` → ③ 결측치·0 데이터 500 장애 격리 해결 → ④ SDD 기반 신규 기능(`불량률 %`) 추가 & 스펙 동기화 | `Slide D-0 ~ D-4` |
| **Conclusion** | - | 오늘 강의 세 줄 요약 (`SPEC.md` 우선 · 로그와 `Diff` 진단 · 작업 전 `Commit`) | `Slide End` |

---

## 3. 프로젝트 구조 (Repository Structure)

```text
spec-over-vibe/
├── .gitignore             # Slidev(Node.js) 및 Flask(Python) Git 제외 규칙
├── README.md              # 프로젝트 개요 및 작업 규칙 안내
├── package.json           # Slidev 실행 스크립트 및 의존성 설정
├── slides.md              # Slidev 프레젠테이션 메인 마크다운 파일
└── demo/                  # 라이브 시연용 초간단 샘플 웹 서비스 (공정 배치 수율 판정기)
    ├── app.py             # Flask 백엔드 API 서버 (20~35줄 내외)
    └── index.html         # 프론트엔드 테이블 및 필터 화면
```

---

## 4. 기술 스택 (Tech Stack)

- **Presentation:** [Slidev](https://sli.dev/) (Markdown 기반 프레젠테이션 프레임워크, Mermaid 다이어그램, UnoCSS/Tailwind)
- **Live Demo App:** Python (Flask), Vanilla HTML/CSS/JavaScript

---

## 5. 협업 및 작업 규칙 (Workflow & Conventions)

- **GitHub Flow 기반 진행:**
  - 모든 작업은 **Sane GitHub Labels**가 적용된 GitHub Issue 단위로 관리합니다.
  - 이슈별 작업 브랜치를 생성하여 작업한 뒤 Pull Request(PR)를 생성하고, 리뷰 후 **Squash Merge**로 `main` 브랜치에 반영합니다.
- **Commit Message Convention:**
  - 모든 커밋 메시지는 **Conventional Commits** 규격을 따르며 **영어(English)**로 작성합니다.
  - 예시:
    - `chore: initialize repo settings and update gitignore`
    - `docs: add Slidev lecture skeleton and intro/conclusion slides (#1)`
    - `feat(slides): add Module 1 web architecture and coordinate reading slides (#2)`
    - `feat(demo): implement minimal batch yield evaluator Flask app (#6)`
