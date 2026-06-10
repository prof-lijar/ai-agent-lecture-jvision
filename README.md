# ai-agent-lecture-jvision

**2일 12시간 AI 에이전트 집중 워크숍** — 대학 1~2학년 컴퓨터공학 전공 학생의 첫 취업을 위한 포트폴리오 프로젝트 실전 교육.

## 한 줄 요약

LangChain + LangGraph로 **멀티 에이전트 시스템**을 직접 설계·구현·배포하고, 채용 시장에서 차별화되는 GitHub 포트폴리오 한 개를 12시간 안에 완성한다.

## 누구를 위한 강의인가

- 컴퓨터공학 전공 1~2학년 (Python 기본 문법은 안다는 가정)
- 첫 인턴/신입 취업을 준비 중인 학생
- "AI 사용은 해봤지만 직접 만든 적은 없는" 단계

## 12시간 후 손에 남는 것

1. **공개 GitHub 저장소** — 의미 있는 커밋 히스토리가 있는 멀티 에이전트 프로젝트
2. **배포된 데모 URL** — Streamlit Cloud에 라이브된 본인 에이전트
3. **1분 데모 영상** — 면접에서 보여줄 수 있는 작동 영상
4. **README + 그래프 시각화** — 기술 블로그에 그대로 옮길 수 있는 문서

## 핵심 산출물 흐름

```
Day 1 끝: 미니 RAG + 첫 LangGraph 챗봇 (싱글 에이전트)
   ↓
Day 2 끝: Supervisor 패턴 멀티 에이전트 + Streamlit UI + 배포된 URL
```

## 디렉토리 구조

```
ai-agent-lecture-jvision/
├── 강의계획서.md              # 정식 강의계획서 (소스 오브 트루스)
├── 강의계획서.docx            # pandoc으로 자동 생성 (학교 제출용)
├── README.md                  # 이 파일
├── pyproject.toml             # 학생 실습 의존성
├── scripts/
│   └── md_to_docx.py          # 강의계획서 → docx 변환
├── day1/
│   ├── README.md              # Day 1 강사 가이드
│   └── code/                  # 데모 코드 스켈레톤
├── day2/
│   ├── README.md              # Day 2 강사 가이드
│   └── code/                  # 멀티 에이전트 템플릿
└── materials/
    ├── project-themes.md      # 학생이 고를 수 있는 프로젝트 주제 5개
    ├── checklist-day1.md      # Day 1 산출물 체크리스트
    ├── checklist-day2.md      # Day 2 산출물 체크리스트
    └── job-market-analysis.md # 채용 시장 분석 자료 (Day 1 도입부용)
```

## 강의계획서 docx 생성

```bash
# 사전 요구: pandoc 설치 (brew install pandoc)
python scripts/md_to_docx.py
# → 강의계획서.docx 생성됨
```

## 참고

- 본 강의는 문성현 강사의 4일 강의안을 압축·재구성하여 만들었음 (참고 원본: 상위 디렉토리의 `AI_강의계획서_문성현.docx`)
- 강사 본인의 멀티 에이전트 모노레포 [orchast_agent](../orchast_agent/) (특히 `dev-team`)가 Day 2 라이브 코딩의 레퍼런스로 사용됨
