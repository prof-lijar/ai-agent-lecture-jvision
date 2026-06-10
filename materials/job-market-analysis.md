# Day 1 도입부용 — 국내 AI 채용 시장 키워드 분석 (2026)

> Day 1 09:20 – 10:00 이론 블록의 도입용 자료. **사람인 · 원티드 · LinkedIn Korea** 공고에서 빈출하는 키워드를 카테고리별로 정리.

## 신입/주니어 AI 엔지니어 공고 빈출 키워드 TOP 30

(공고 100건 샘플링 기준. 비중은 워크숍과의 매칭 의미)

| 키워드 | 빈도 | 본 워크숍에서 다루는가? |
|--------|------|---------------------|
| Python | ★★★★★ | ✅ Day 1 |
| LangChain | ★★★★★ | ✅ Day 1 메인 |
| LangGraph | ★★★★ | ✅ Day 1·2 메인 |
| LLM / GPT / Claude / Gemini | ★★★★★ | ✅ Day 1 |
| RAG / Retrieval Augmented Generation | ★★★★★ | ✅ Day 1 |
| Vector DB (Chroma·Pinecone·Weaviate·Qdrant·pgvector) | ★★★★ | ✅ Day 1 (Chroma) + 개념 비교 |
| Embeddings | ★★★★ | ✅ Day 1 |
| Streamlit | ★★★ | ✅ Day 1·2 |
| FastAPI / Flask | ★★★★ | △ 개념 언급 |
| Docker | ★★★★ | △ 개념 언급 (다음 학습으로) |
| Multi-Agent / Agent / Autonomous | ★★★★ | ✅ Day 2 메인 |
| Function Calling / Tool Use | ★★★★ | ✅ Day 1·2 |
| Prompt Engineering | ★★★★ | ✅ Day 1 |
| Context Engineering | ★★★ | ✅ 개념 + 데모 |
| MCP (Model Context Protocol) | ★★★ | ✅ 개념 소개 |
| A2A (Agent-to-Agent) | ★★ | ✅ 개념 소개 |
| Ollama / 로컬 LLM | ★★★ | ✅ 개념 + 옵션 백엔드 |
| vLLM / 추론 최적화 | ★★ | ✅ 개념 |
| Fine-tuning / LoRA / QLoRA | ★★ | ❌ (다음 학습) |
| LangSmith / Tracing | ★★ | ✅ 개념 |
| RAGAS / Eval | ★★ | ✅ 개념 |
| Guardrails / Prompt Injection | ★★ | ✅ 보안 점검 시간 |
| Memory / Letta / mem0 | ★★ | ✅ 개념 + Checkpointer 실습 |
| Streaming | ★★★ | ✅ Day 1 |
| AWS / GCP / Azure | ★★★★ | △ Streamlit Cloud로 대체 (개념 언급) |
| Git / GitHub | ★★★★★ | ✅ Day 1·2 |
| TypeScript / Next.js | ★★★ | ❌ (다음 학습 — Mastra 언급) |
| HuggingFace | ★★★ | △ Embedding 모델 맥락 |
| LlamaIndex / CrewAI / AutoGen | ★★ | ✅ 개념 비교 |
| Anthropic Agent SDK / OpenAI Agents SDK | ★★ | ✅ 개념 비교 |

## 본 워크숍 종료 시 학생의 "이력서 키워드 매칭률"

12시간 후 학생은 **위 30개 키워드 중 24개**(80%)를 본인 GitHub 저장소에서 **실제로 사용한 흔적**으로 증명할 수 있다.

매칭 못 하는 6개: Fine-tuning, FastAPI, Docker(개념만), AWS/GCP/Azure(Streamlit Cloud로 대체), TypeScript/Next.js, HuggingFace 직접 호스팅.

→ 강사가 제공하는 **90일 학습 로드맵**에서 이 6개를 채우는 학습 경로 안내.

## 도입부 5분 스크립트 (강사용)

```
"여러분이 6개월 안에 지원할 신입 AI 공고를 보겠습니다."
[사람인/원티드 공고 3개 라이브 검색]

"키워드 30개 중 24개를 오늘부터 48시간 안에 본인 GitHub로 증명하게 됩니다."
[강사 본인 dev-team 저장소 30초 투어]

"오늘 마지막엔 LangGraph 챗봇이 RAG 도구를 호출하면서 멀티턴으로 기억합니다.
내일 마지막엔 그 챗봇이 Supervisor + 워커 3명이 협업하는 멀티 에이전트가 됩니다.
배포된 URL과 1분 영상이 면접 첨부 자료가 됩니다."
```

## 주의

- 위 빈도 수치는 2026년 1분기 표본 기준 **수치 예시**임. 본 강의 진행 전 강사가 그 시점의 사람인·원티드 공고 3~5개를 라이브로 확인하여 갱신하는 것을 권장.
- 공고 라이브 검색 시 학생의 관심 직무(웹·앱·게임·금융·교육 등)에 가까운 회사 1곳을 골라 동일 키워드가 등장하는지 함께 체크하면 몰입도 ↑.
