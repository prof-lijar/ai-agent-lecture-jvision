# Day 1 — 강사 가이드

> AI/LLM 기초 → LangChain 미니 RAG → LangGraph 첫 챗봇 + 도구 + 메모리

## 운영 흐름 한눈에

```
09:00  OT (20m)
09:20  이론: 산업/채용 (40m)
10:00  이론: LLM + 5패턴 (30m)
10:30  ☕ 휴식
10:40  실습: 환경 세팅 (40m)
11:20  실습: 미니 RAG (1) — 컴포넌트 (40m)
12:00  🍱 점심
13:00  실습: 미니 RAG (2) — 완성 + 실험 (40m)
13:40  이론: LangChain → LangGraph 전환 (30m)
14:10  ☕ 휴식
14:20  실습: LangGraph 챗봇 + Streamlit (50m)
15:10  실습: Tool calling + ToolNode (30m)
15:40  마무리: Checkpointer + 일지 (20m)
16:00  종료
```

## 강사 사전 준비

- [ ] OpenAI 또는 Gemini 데모 키 준비 (수강생용 임시 키 포함)
- [ ] 라이브 코딩용 빈 저장소 1개 (`day1-demo`)
- [ ] 본인이 채울 RAG 샘플 데이터 (PDF 1개 + 텍스트 1개)
- [ ] 화이트보드 또는 디지털 보드 (LangGraph 그래프 그리기용)
- [ ] 1:1 코칭용 보조 강사/조교 1명 (수강생 10명당 1명 권장)

## 시간 블록별 노트

### 09:00 – 09:20 — OT
- 강사 본인의 `orchast_agent/dev-team`을 화면으로 30초 보여주며 "2일 뒤 너희도 이걸 만든다" 충격 요법
- 수강생 자기소개는 30초 × N — Python 경험·만들고 싶은 것만

### 09:20 – 10:00 — 산업/채용 분석
- `materials/job-market-analysis.md` 참고
- 사람인/원티드 AI 채용 공고 3~5개 라이브로 띄워 키워드 동그라미

### 10:40 – 11:20 — 환경 세팅
가장 시간이 새는 구간. 사전 준비가 안 된 학생을 위한 fallback:
- Colab/Replit 백업 준비
- API 키 안 받아온 학생용 임시 키 1~2개

### 14:20 – 15:10 — LangGraph 첫 챗봇
화이트보드 → 코드 순서 반드시 지킬 것. State 정의 → Node 함수 → `add_node`/`add_edge` → `compile()` → Streamlit `session_state`에 그래프 인스턴스 보관.

### 15:10 – 15:40 — Tool calling
Day 1 RAG 함수를 **그대로** 도구로 등록하는 것이 핵심. Day 2에서 멀티 에이전트의 첫 도구로 재사용된다.

## Day 1 종료 시 학생 손에 있어야 하는 것

- `day1-chatbot/` 저장소 (로컬 + GitHub push)
- 동작하는 Streamlit 앱 (`streamlit run app.py`)
- 본인 데이터로 RAG 답변 1회 이상
- Day 1 일지 1페이지

## 자주 발생하는 문제

| 증상 | 해결 |
|------|------|
| API 키 401 | `.env` 위치, `load_dotenv()` 호출 여부, 키 앞뒤 공백 확인 |
| Chroma 설치 실패 (Windows) | `pip install chromadb` 대신 `uv add chromadb` 권장 |
| Streamlit 한글 깨짐 | 폰트 설정 불필요. 브라우저 폰트 문제 — Chrome 권장 |
| `RecursionError` in LangGraph | `recursion_limit` 명시 또는 종료 조건(`END`) 누락 확인 |
