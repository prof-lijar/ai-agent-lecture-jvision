# Day 2 — 강사 가이드

> 멀티 에이전트 패턴 → Supervisor 라이브 코딩 → 학생 프로젝트 → Streamlit Cloud 배포 → 라이브 시연

## 운영 흐름 한눈에

```
09:00  회고 + 미리보기 (20m)
09:20  이론: 멀티 에이전트 패턴 (40m)
10:00  라이브 코딩: Supervisor 미니 dev-team (60m)
11:00  ☕ 휴식
11:10  실습: 프로젝트 주제 선정 + 기획 (20m)
11:30  실습: 프로젝트 1단계 — Supervisor + 첫 워커 (30m)
12:00  🍱 점심
13:00  실습: 프로젝트 2단계 — 워커 추가 + 도구 (60m)
14:00  실습: UI + 그래프 시각화 + 보안 (30m)
14:30  ☕ 휴식
14:40  실습: Git 정리 + Streamlit Cloud 배포 (30m)
15:10  실습: 1분 데모 영상 (15m)
15:25  발표: 라이브 시연 (30m)
15:55  마무리: 90일 로드맵 + 수료 (5m)
16:00  종료
```

## 강사 사전 준비

- [ ] 라이브 코딩용 미니 dev-team 데모 코드 (Planner + Coder + Reviewer, ~200줄)
- [ ] `materials/project-themes.md` 5개 주제 각 1페이지 기획서 샘플
- [ ] Streamlit Cloud 사이드바 Secrets 설정 데모 (본인 계정으로 시연)
- [ ] 학생별 1:1 코칭 체크 시트 (주제·진척도·블로커)
- [ ] 1분 영상 녹화 가이드 (macOS: QuickTime, Windows: Xbox Game Bar)

## 시간 블록별 노트

### 09:00 – 09:20 — 회고
- 어제 막힌 학생부터 발언 (심리적 안전감)
- 오늘 끝에 만들어질 것을 다시 보여줌 (강사의 미리 만든 5개 프로젝트 데모 URL 클릭)

### 10:00 – 11:00 — Supervisor 라이브 코딩 (★ 핵심)
60분에 200줄을 라이브로 치는 건 무모하다. 사전에 80% 작성된 스켈레톤을 두고 **결정적 부분만** 채우는 형태로 진행:
- State 설계 (TypedDict)
- Supervisor 라우팅 노드 (LLM 호출 → 다음 워커 선택)
- 워커 노드 3개 (가장 단순한 형태)
- `Command(goto=...)` 또는 `add_conditional_edges`로 라우팅

데모 코드는 `day2/code/supervisor_demo.py`에 위치 (다음 세션에서 구현).

### 11:10 – 11:30 — 주제 선정
**1:1 컨펌 필수**. 너무 큰 스코프(예: "에이전트가 알아서 코딩하고 배포까지")는 시간 안에 끝나지 않음. 워커 2~3개 + 도구 2~3개 이내로 강제.

### 13:00 – 14:00 — 프로젝트 2단계 (가장 위험한 1시간)
1:1 코칭이 가장 필요한 구간. 막힌 학생에게 너무 오래 머물지 않는 룰:
- 5분 안에 해결 안 되면 우회로 제시 (예: Conditional Edge 대신 단순 if/else로 일단 동작시키기)
- 동료 도움도 적극 권장 (해결한 학생 → 막힌 학생 옆자리 코칭)

### 14:40 – 15:10 — 배포 (Streamlit Cloud)
- GitHub 저장소가 Public인지 먼저 확인
- `requirements.txt` 또는 `pyproject.toml` 둘 중 하나만 존재해야 충돌 없음
- Secrets에 `OPENAI_API_KEY` (또는 `GOOGLE_API_KEY`) 등록
- 첫 배포 5~10분 걸리는 점 사전 안내

### 15:25 – 15:55 — 발표 (★ 학생에겐 가장 떨리는 시간)
- 1인 1분 시연 + 30초 "왜 이 기술을 골랐는지" 설명만 받기
- 강사 피드백은 **칭찬 1개 + 다음 90일에 할 것 1개**로 통일

## Day 2 종료 시 학생 손에 있어야 하는 것

| 산출물 | 검증 방법 |
|--------|----------|
| GitHub Public 저장소 | 강사가 URL 클릭으로 확인 |
| 라이브 Streamlit URL | 강사가 외부망(LTE)에서 접속 테스트 |
| 그래프 시각화 PNG | README에 임베드되어 보임 |
| 1분 데모 영상 | README의 GIF 또는 YouTube/Loom 링크 |
| 협업하는 워커 2개+ | 라이브 시연 중 강사 확인 |

## 자주 발생하는 문제

| 증상 | 해결 |
|------|------|
| Streamlit Cloud 배포 실패 (의존성) | `pyproject.toml`과 `requirements.txt` 동시 존재 시 제거 |
| Secrets가 앱에서 안 읽힘 | `st.secrets["OPENAI_API_KEY"]` 형식 사용, `os.environ`도 함께 설정 |
| Supervisor 무한 루프 | 워커가 "끝났다"는 신호(`FINISH`)를 State에 명시적으로 쓰는 패턴 |
| `draw_mermaid_png()` 실패 | `pyppeteer` 의존 — 로컬에서만 실행 후 PNG를 저장소에 커밋 |
| 한글 폰트로 mermaid 깨짐 | 영문 노드명만 사용 (`planner`, `coder`, `reviewer`) |
