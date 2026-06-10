# Day 2 산출물 체크리스트

> 15:25 발표 직전에 학생 본인이 셀프 체크. 강사는 채점 + 라이브 시연 확인.

## 멀티 에이전트 시스템
- [ ] Supervisor 노드가 존재하고 워커별로 라우팅
- [ ] 워커 에이전트 2개 이상 동작 (선택 주제에 따라 3개까지)
- [ ] 도구 2개 이상 통합 (Day 1 RAG 함수 재활용 권장)
- [ ] Conditional Edge로 워커 선택 또는 종료(FINISH) 처리
- [ ] 그래프가 무한 루프 없이 정상 종료 (recursion_limit 또는 명시적 END)

## UI / 시각화
- [ ] Streamlit 앱이 사이드바·로딩·에러 처리 포함
- [ ] `graph.get_graph().draw_mermaid_png()` 결과 PNG가 README에 첨부

## 보안 점검
- [ ] API 키가 코드/저장소에 노출되지 않음 (강사 직접 확인)
- [ ] 사용자 입력에 대한 1차 검증 (빈 입력·과도한 길이·명백한 prompt injection 시도 차단)
- [ ] 출력에 대한 1차 검증 (JSON 강제 또는 길이 캡)
- [ ] (선택) HITL 노드 1개 이상 (`interrupt()` 적용 또는 시연)

## 비용 관리
- [ ] `gpt-4o-mini` / `gemini-2.0-flash` / `claude-haiku` 등 저비용 모델 디폴트 사용
- [ ] 그래프 한 회 실행 시 토큰·비용 대략 측정 (강사 보조 확인)

## Git / 저장소
- [ ] GitHub 저장소 **Public**
- [ ] README.md에 (1) 데모 GIF/영상 링크, (2) 라이브 URL, (3) 그래프 PNG, (4) 실행 방법
- [ ] 의미 있는 커밋 5개 이상 (Day 1 포함)
- [ ] `pyproject.toml` 또는 `requirements.txt` 중 하나만 존재 (충돌 방지)

## 배포
- [ ] Streamlit Cloud 배포 완료
- [ ] Secrets에 API 키 등록 (저장소에는 노출 X)
- [ ] 강사가 외부 환경(LTE)에서 라이브 URL 접속 → 정상 동작 확인

## 데모 영상
- [ ] 1~2분 길이의 화면 녹화 (mp4 또는 GIF)
- [ ] 핵심 시연 흐름 30~60초 (입력 → Supervisor 라우팅 → 워커 → 답변)
- [ ] README에 임베드 또는 링크

## 일지 + 학습 로드맵
- [ ] Day 2 개발 일지 1페이지
- [ ] 다음 90일 학습 로드맵 (예시 템플릿 강사 제공)
  - 30일: LangGraph 고급 패턴 (Subgraph, Send/Receive)
  - 60일: 평가 (RAGAS, LangSmith Trajectory) + 메모리 (mem0)
  - 90일: 본인 프로젝트 v2 (멀티 에이전트 + MCP 서버 자작)

---

**미니멈 합격선**: 위 항목 중 **22/27 이상** + 라이브 URL 외부망 정상 동작 + 라이브 시연 성공 시 Day 2 통과 (수료).
