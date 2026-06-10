# Day 1 산출물 체크리스트

> 17:00 직전에 학생 본인이 셀프 체크. 강사는 채점 시 참고.

## 환경
- [ ] Python 3.11+ + uv 가상환경 동작
- [ ] `.env`에 API 키 보관, `.gitignore`에 `.env` 등록 (`git status`로 확인)
- [ ] OpenAI / Gemini / OpenRouter / Ollama 중 1개 이상에서 ChatModel 호출 성공

## RAG
- [ ] 본인 데이터 (PDF 또는 텍스트) 1개 이상 인덱싱
- [ ] TextSplitter → Embedding → Chroma → Retriever 흐름 동작
- [ ] 동일 질의에 청크 크기·k값을 바꿔 비교 실험 1회 이상

## LangGraph 챗봇
- [ ] State (TypedDict) 정의 + 노드 2개 이상 + `compile()` 완료
- [ ] Streamlit 앱(`streamlit run app.py`)에서 챗 UI 동작
- [ ] 도구 1개(Day 1 RAG 함수) `ToolNode`로 등록 + `tools_condition` 분기
- [ ] `MemorySaver` Checkpointer + `thread_id` 적용, 멀티턴 기억 확인

## Git / GitHub
- [ ] 로컬 `git init` + GitHub 저장소 생성
- [ ] 의미 있는 커밋 3개 이상 (기능 단위로 분리)
- [ ] README.md에 (1) 프로젝트명, (2) 실행 방법, (3) 데모 스크린샷 1장

## 일지
- [ ] Day 1 개발 일지 1페이지 (`docs/day1-log.md` 또는 노션)
  - 오늘 배운 개념 3개
  - 막혔던 부분 1개 + 해결 방법
  - 내일 가져가고 싶은 질문 1개

---

**미니멈 합격선**: 위 항목 중 **18/22 이상** + LangGraph 챗봇이 멀티턴으로 도구를 호출하면 Day 1 통과.
