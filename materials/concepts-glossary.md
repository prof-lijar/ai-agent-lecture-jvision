# AI 에이전트 핵심 개념 용어집 (2026)

> 본 워크숍에서 다루는 개념과 **취업 시장에서 마주칠 키워드**를 정리한 참고용 사전입니다.
> 각 항목은 **정의 / 용도 / 대표 도구 / 왜 알아야 하는가** 순서로 구성되어 있습니다.
> 영문 용어는 **그대로 표기**합니다 — 채용 공고와 GitHub README에서 그대로 마주칠 형태이기 때문입니다.

---

## 1. LLM 추론 / 서빙 (Inference & Serving)

### 1.1 로컬 추론 엔진

**Ollama**
- 모델 레지스트리 + OpenAI 호환 API를 갖춘 단일 바이너리 로컬 LLM 실행기. 내부적으로 `llama.cpp` 사용.
- 용도: 노트북·로컬 프로토타이핑, 오프라인 데모.
- 대표: `ollama` CLI, `ollama.com/library`.
- 왜: 어떤 오픈 모델이든 로컬에서 가장 빠르게 띄우는 표준. 면접 데모는 거의 여기서 시작.

**llama.cpp**
- C/C++ 추론 엔진. GGUF 포맷으로 CPU/GPU/Apple Silicon에서 양자화 모델 실행.
- 용도: CPU 추론, 엣지 디바이스, Mac M 시리즈.
- 대표: `ggerganov/llama.cpp`.
- 왜: Ollama, LM Studio, Jan 등 모든 "로컬 LLM" 도구의 기반. 알면 모든 로컬 스택이 이해됨.

**LM Studio**
- GGUF 모델을 다운로드·실행하고 OpenAI 호환 서버를 띄우는 데스크탑 GUI.
- 용도: 코드 없이 로컬 실험, 비개발자 데모.
- 왜: 터미널 없이 로컬 모델을 비교·실험하는 가장 쉬운 도구.

### 1.2 프로덕션 / GPU 추론 엔진

**vLLM** ⭐
- UC Berkeley 발 고처리량 GPU 추론 서버. **PagedAttention** + 연속 배칭(continuous batching).
- 용도: 오픈 모델의 프로덕션 서빙. NVIDIA가 기본, AMD/Trainium 일부 지원.
- 대표: `vllm-project/vllm`. HuggingFace Inference Endpoints의 기본값.
- 왜: 오픈 모델 프로덕션의 사실상 표준. 채용 공고 빈출 키워드 TOP 3.

**SGLang**
- **RadixAttention**(트리 기반 prefix caching)을 가진 추론 엔진. MoE 모델과 공유 프리픽스 워크로드에 강함.
- 용도: RAG, 멀티턴 챗, DeepSeek/Qwen 같은 대형 MoE.
- 대표: `sgl-project/sglang`.
- 왜: 2026년 가장 빠르게 성장하는 엔진. 공유 프리픽스 워크로드에서 vLLM 대비 ~29% 빠름.

**TensorRT-LLM**
- NVIDIA의 컴파일 그래프 기반 추론 엔진. H100·Blackwell 하드웨어 통합 극단.
- 용도: NVIDIA 하드웨어에서 토큰 처리량 최대화.
- 왜: H100에서 vLLM 대비 ~15-30% 빠름. Blackwell에선 사용자당 1,000 tok/s. 단점은 긴 컴파일 시간.

**NVIDIA Dynamo**
- 추론 엔진 위에 얹는 오케스트레이션 레이어. KV cache 기반 라우팅, prefill/decode 분리.
- 왜: "엔진 위의 엔진" — 엔진은 모델을, Dynamo는 GPU 플릿을 조율.

### 1.3 호스팅 추론 제공자

**OpenRouter**
- 300+ 모델(OpenAI · Anthropic · Google · 오픈소스)을 단일 API + 통합 청구로 제공.
- 왜: 모델 A/B 테스트와 벤더 락인 회피의 표준. 프로토타이핑 단계 첫 선택.

**Groq**
- 자체 LPU 칩으로 Llama/Mixtral/Qwen을 500-1000 tok/s로 추론.
- 왜: 오픈 모델 추론 중 압도적으로 빠름. 실시간 보이스 에이전트가 가능해짐.

**Together AI / Fireworks AI**
- 오픈 모델을 호스팅 API로 제공. 서버리스 + 전용 엔드포인트 + 파인튜닝.
- 왜: GPU를 직접 운영하지 않고 오픈 모델을 프로덕션에 올리는 2대 옵션. 한국 스타트업도 다수 사용.

### 1.4 양자화 & 최적화

**GGUF (Q4_K_M, Q5_K_M, Q8_0)**
- `llama.cpp`/Ollama용 양자화 모델 파일 포맷. 2~8비트 가중치 지원.
- 왜: Q4_K_M은 원본 품질의 ~92%를 25% 용량으로 유지. "노트북에서 70B 돌리기"의 정답.

**AWQ (Activation-aware Weight Quantization)**
- 활성화에 중요한 가중치를 보존하는 INT4 양자화.
- 용도: GPU 프로덕션(vLLM, TGI). Marlin 커널과 함께 사용.
- 왜: 2026년 GPU 프로덕션의 최적해 — 품질 ~95%, 속도 최고.

**GPTQ**
- 캘리브레이션 기반 4비트 GPU 양자화. 오래된 방식.
- 왜: AWQ에 밀렸지만 HuggingFace에 양자화된 가중치가 여전히 많음. 둘의 차이는 면접 단골.

**FP8**
- H100/Blackwell이 네이티브 지원하는 8비트 부동소수점 추론.
- 왜: Hopper/Blackwell에서 메모리 ~2배 절약 + 품질 손실 거의 없음.

**PagedAttention**
- vLLM의 KV cache 메모리 관리 알고리즘. 가상메모리처럼 페이지 단위로 cache 관리.
- 왜: vLLM이 왜 동시 요청을 많이 처리하는지에 대한 답. 면접 필수.

**Continuous / In-flight Batching**
- 진행 중인 GPU 배치에 새 요청을 동적으로 합치는 기법.
- 왜: 모든 프로덕션 엔진의 처리량 차별화 요소. HuggingFace `generate()`와의 차이.

**Speculative Decoding**
- 작은 draft 모델이 N개 토큰을 추측 → 큰 모델이 한 번에 검증.
- 왜: 긴 생성에서 지연 2~3.6배 감소. 실시간 에이전트에서 필수.

**Prefix Caching**
- 요청 간 공유되는 prefix의 KV cache를 재사용.
- 왜: SGLang의 RadixAttention이 대표. TTFT(첫 토큰까지 시간)가 5~10배 빨라지는 이유.

---

## 2. 에이전트 저수준 구성 요소 (Low-level Building Blocks)

### 2.1 컨텍스트 (Context)

**Context Window**
- 모델이 한 호출에서 attend 할 수 있는 토큰 예산 (Claude 200K, Gemini 1M 등).
- 왜: 1M이라도 앞쪽과 뒤쪽 토큰만 출력에 안정적으로 영향.

**Context Engineering** ⭐
- 매 스텝마다 시스템 프롬프트·도구·메모리·검색 결과 중 무엇을 컨텍스트에 넣을지 결정하는 학문.
- 대표: Anthropic의 "effective context engineering" 쿡북.
- 왜: "프롬프트 엔지니어링"을 대체한 2026년 핵심 스킬. Gartner는 2026을 "Year of Context"로 지정.

**Context Rot**
- 컨텍스트가 커질수록 정확도가 떨어지는 현상. "lost in the middle"로도 불림.
- 왜: 무작정 1M에 다 욱여넣은 컨텍스트가 정성껏 큐레이션한 10K 컨텍스트보다 못한 이유.

**Compaction (압축)**
- 대화가 길어지면 핵심만 남기고 요약. 대표는 Claude의 `/compact`.
- 왜: 모든 장시간 에이전트에 필수. 압축 프롬프트 튜닝이 실제 엔지니어링.

**Tool-Result Clearing**
- 과거 도구 출력을 컨텍스트에서 제거하고 에이전트의 메모(요약)만 유지.
- 왜: 도구 호출이 많은 에이전트에서 컨텍스트 절약 효과 최대.

**Progressive Disclosure**
- 컨텍스트를 한꺼번에 미리 주지 않고, 에이전트가 도구로 직접 발견하도록 함 (파일 ls, search 등).
- 왜: Claude Code · Cursor의 핵심 패턴. "에이전트가 알아서 파일 읽기"가 "레포 통째 프롬프트"보다 잘 작동하는 이유.

### 2.2 메모리 (Memory)

**Short-Term Memory (단기 메모리)**
- 한 세션/스레드 내의 대화 히스토리.

**Long-Term Memory (장기 메모리)**
- 세션을 넘어 보존되는 사실/선호. 보통 vector store가 백엔드.
- 대표: mem0, Letta, Zep, LangMem.
- 왜: 에이전트에 "사용자 이름"이 생기는 순간 필요.

**Episodic Memory (에피소드 메모리)**
- 과거 사건/상호작용 기억 ("화요일에 사용자가 X를 물어봤다").
- 왜: "지난번엔..." 류의 개인화 UX의 기반.

**Semantic Memory (의미 메모리)**
- 세계나 사용자에 대한 사실 ("사용자는 채식주의자", "본사는 서울").
- 왜: 대부분의 메모리 제품이 이 레이어를 최적화.

**Working Memory (작업 메모리)**
- 모델이 지금 활성으로 추론하고 있는 스크래치패드 = 현재 컨텍스트.

**Letta (구 MemGPT)**
- OS 스타일 계층 메모리(core/recall/archival)를 구현한 오픈소스 에이전트 런타임.
- 왜: "LLM-as-OS" 연구의 정통 구현. 락인 큼, 상한선 높음.

**mem0**
- 어떤 LLM 호출이든 감싸서 사실 추출·저장·검색을 추가하는 드롭인 SDK.
- 왜: 2026년 커뮤니티 디폴트. 3줄로 메모리 추가, 락인 적음.

### 2.3 세션 / 스레드 / 체크포인트

**Thread / Session / `thread_id`**
- 메시지 히스토리와 상태를 묶는 대화 식별자.
- 대표: LangGraph `thread_id`, OpenAI Assistants `thread`.
- 왜: 모든 멀티턴 에이전트에 필요. 보통 `user_id + conversation_id` 조합.

**Checkpointer (LangGraph)** ⭐
- 각 노드 후 그래프 state를 백엔드(Postgres/SQLite/Redis)에 영속화 → 재개 가능.
- 용도: HITL 일시정지, 장애 복구, 타임트래블 디버깅.
- 대표: `langgraph.checkpoint.postgres.PostgresSaver`.
- 왜: 팀이 LangGraph를 프로덕션에 택하는 가장 큰 이유.

### 2.4 도구 / 함수 호출 / 구조화 출력

**Tool / Function Calling** ⭐
- 모델이 함수명 + JSON 인자를 구조화된 요청으로 emit → 런타임이 실행.
- 대표: OpenAI `tools=[...]`, Anthropic `tools=[...]`, Gemini `function_declarations`.
- 왜: 모든 에이전트의 기초 메커니즘. 이거 없으면 에이전트도 없음.

**JSON Schema**
- 도구 파라미터와 구조화 출력 형태를 선언하는 스키마 언어 (Draft 2020-12).
- 왜: 모든 모던 LLM 제공자가 이걸로 도구 인자 검증. 도구 정의 자체가 JSON Schema.

**Structured Outputs (Strict Mode)**
- 제공자가 JSON Schema에 강제 준수하도록 디코딩을 제약.
- 대표: OpenAI `strict: true`, Anthropic `structured-outputs-2025-11-13` 베타.
- 왜: 단순 JSON mode의 85~92% 대비 99.9% 스키마 준수. 재시도 루프 제거.

**JSON Mode**
- 구조화 출력의 약한 선배. 유효한 JSON은 보장하지만 스키마 일치는 안 함.
- 왜: 구조화 출력 미지원 제공자의 fallback. 2~12% 불일치 예상.

**Tool Calling vs Structured Output vs JSON Mode**
- Tool calling = "함수 호출" / Structured = "이 스키마 따르라" / JSON mode = "JSON이기만 하면 됨".
- 왜: 면접 단골. **추출**이면 structured, **행동**이면 tools.

### 2.5 프롬프트 (Prompts)

**System / User / Assistant 역할**
- 채팅 형식 API의 3대 메시지 역할.
- 왜: `system`만 privileged. user에 규칙을 넣는 건 흔한 버그.

**Prompt Template**
- 플레이스홀더가 있는 파라미터화된 프롬프트 (보통 Jinja, f-string).
- 대표: LangChain `PromptTemplate`, Pydantic AI 시스템 프롬프트.
- 왜: 프롬프트 drift 방지 + A/B 테스트 가능.

**Few-Shot Prompting**
- 입력→출력 라벨된 예시를 프롬프트에 포함시켜 패턴 학습.
- 왜: 파인튜닝까지 가기 전 가장 저렴한 품질 개선.

**ReAct Prompt**
- `Thought → Action → Observation` 루프 인터리브 프롬프트 패턴 (Yao et al. 2022).
- 왜: 단일 에이전트의 표준 루프. 거의 모든 프레임워크가 이 변형 구현.

### 2.6 스킬 (Skills)

**Skills (Claude Code 스타일)** ⭐
- `SKILL.md` + 스크립트/템플릿을 묶은 폴더. 에이전트가 필요 시 로드해 능력 획득.
- 대표: Anthropic Claude Skills, Letta Code skills.
- 왜: "시스템 프롬프트에 다 욱여넣기"를 대체하는 신흥 패턴. 점진적 능력 로딩 = progressive disclosure의 연장.

---

## 3. 멀티 에이전트 패턴

**Supervisor / Orchestrator-Worker** ⭐
- 중앙 조정자가 각 서브태스크를 전문 워커 에이전트로 라우팅.
- 대표: LangGraph `create_supervisor`, OpenAI Agents SDK handoffs.
- 왜: 프로덕션 멀티 에이전트 ~70%. 거버넌스/감사 필요할 때 안전한 디폴트. **본 워크숍의 핵심 패턴**.

**Hierarchical (계층형)**
- Supervisor 패턴을 N 단계로 중첩 (supervisor → team-lead → worker).
- 왜: 워커 ~6개 이상에 필요하지만 매 계층마다 지연 증가. 플랫 구조부터 시작 권장.

**Network / Swarm**
- 중앙 컨트롤러 없이 동급 에이전트들이 handoff·공유 큐로 통신.
- 대표: OpenAI Swarm(2025 deprecated) → Agents SDK, Kimi K2.6.
- 왜: 처리량 최고, 디버깅 최악. 규제 산업엔 부적합.

**Sequential Pipeline (순차 파이프라인)**
- 고정된 선형 체인: A → B → C.
- 왜: 가장 단순한 멀티 에이전트. 워크플로우가 선형이면 과설계 금지.

**Handoff**
- 한 에이전트에서 다른 에이전트로 제어와 대화 히스토리를 넘기는 도구 호출.
- 대표: OpenAI Agents SDK `Agent.handoffs`.
- 왜: swarm/supervisor를 조합 가능하게 만드는 기초 단위.

**Subagent (서브에이전트)**
- 자체 컨텍스트 윈도우를 가진 자식 에이전트. 부모에게 요약만 반환.
- 대표: Claude Agent SDK subagents, Anthropic research multi-agent.
- 왜: 부모 컨텍스트를 깨끗이 유지하면서 깊은 작업을 시키는 표준 방법.

**Reflection (Self-Refine)**
- 에이전트가 자기 출력을 비판하고 다시 씀. 같은 모델이 generator + critic.
- 왜: 보통 2~3회 후 plateau. 반복 횟수 캡 없으면 토큰 소진.

**Actor-Critic / Verifier**
- generator와 verifier 분리. verifier가 통과시킬 때까지 반복.
- 왜: 고stake 출력 품질 향상, 비용 ~2배.

**Plan-and-Execute**
- 한 에이전트가 step 리스트(plan)를 만들고 다른 에이전트가 step별 실행.
- 대표: LangChain plan-and-execute, BabyAGI 계열.
- 왜: 장기 horizon 작업에서 ReAct보다 강함.

**Reflexion**
- ReAct + 메모리에 저장되는 자기 비판. 실패가 반복될 때 효과적.

**Tree-of-Thoughts (ToT)**
- 추론 분기를 트리로 확장·가지치기·역추적.
- 왜: 퍼즐, 수학, 복잡한 계획 같은 탐색 필요 작업에 적합.

---

## 4. 에이전트 간 / 시스템 간 프로토콜

**MCP (Model Context Protocol)** ⭐⭐
- 에이전트가 외부 도구·리소스를 발견하고 호출하는 오픈 클라이언트-서버 프로토콜.
- 대표: `modelcontextprotocol.io`. Anthropic 발, 현재 Linux Foundation AAIF.
- 왜: 월 9700만+ SDK 다운로드. Anthropic, OpenAI, Google, Microsoft 지원. **에이전트-도구 레이어의 승자**.

**A2A (Agent-to-Agent Protocol)** ⭐
- 서로 다른 프레임워크의 에이전트들이 서로 발견·위임할 수 있는 Google 발 오픈 스펙.
- 대표: `a2aproject` (Linux Foundation, 2025 v1.0).
- 왜: 150+ 파트너 (Salesforce, ServiceNow, SAP). MCP가 수직이면 A2A는 수평.

**Function-Calling Specs**
- 벤더별 JSON 포맷. 거의 수렴했지만 파라미터명·제한 차이.
- 왜: LiteLLM 같은 추상화가 이를 정규화. 한 코드로 여러 LLM 쓸 때 필수.

---

## 5. RAG 연관 개념

**Embeddings**
- 의미적 유사도가 코사인 유사도와 일치하는 텍스트의 dense vector 표현.
- 대표: `text-embedding-3-large` (OpenAI), `voyage-3-large` (Voyage), `bge-large` (오픈).
- 왜: 모든 vector store, semantic cache, 유사도 검색의 기반.

**Vector Store**
- Embedding에 대한 ANN(approximate nearest neighbor) 검색에 최적화된 DB.

**Chroma**
- 임베디드 vector DB. 인프로세스 또는 작은 Docker로 실행.
- 왜: 프로토타이핑 가장 쉬움. **본 워크숍 Day 1에서 사용**.

**Pinecone**
- 완전 관리형 서버리스 vector DB.
- 왜: 인프라 안 만지고 싶을 때.

**Weaviate**
- 오픈소스 vector DB. 네이티브 hybrid 검색(BM25 + dense) + GraphQL.
- 왜: hybrid 검색 챔피언. 멀티모달 RAG 프로덕션에 강함.

**Qdrant**
- Rust 기반 오픈소스 vector DB. 가성비 1위.
- 왜: Weaviate/Milvus 대비 ~10-25% 빠름. 단일 VPS에 셀프호스트 저렴.

**pgvector**
- Postgres의 `vector` 컬럼 + ANN 인덱스 익스텐션.
- 왜: 이미 Postgres 쓰면 ~70% 워크로드의 정답. 트랜잭션 일관성 보너스.

**Reranking**
- 1차 검색 top-K를 cross-encoder 모델로 재점수.
- 대표: Cohere Rerank 3, Voyage Rerank, 오픈 `bge-reranker`.
- 왜: 검색 정밀도 +15~25%. RAG 단일 최대 ROI 업그레이드.

**Hybrid Search**
- BM25(lexical) + dense(semantic)를 RRF(Reciprocal Rank Fusion)로 결합.
- 왜: dense 단독은 정확 매치(ID, 코드) 놓침. 프로덕션 필수.

**BM25**
- 클래식 sparse 키워드 랭킹 (TF-IDF 후예).
- 왜: 모든 hybrid 검색의 lexical 절반.

**HyDE (Hypothetical Document Embeddings)**
- LLM에게 가상의 답을 생성시켜 그 임베딩으로 검색.
- 왜: 짧고 모호한 질의 recall 향상.

**Agentic RAG**
- 에이전트 루프 안의 RAG: plan → retrieve → rerank → reflect → re-retrieve → 인용 포함 답변.
- 왜: 어려운 질문에 hallucination ~62% 감소, 비용 ~10배. Adaptive RAG로 라우팅 권장.

**Adaptive RAG**
- 분류기가 각 질의를 naive/advanced/agentic/GraphRAG로 라우팅.
- 왜: 2026 베스트 프랙티스. 비용/품질 최적.

**GraphRAG**
- 문서에서 추출한 knowledge graph 위의 RAG.
- 대표: Microsoft GraphRAG.
- 왜: 여러 문서 간 관계 합성이 필요한 답변에 필수.

---

## 6. 프로덕션 관심사

### 6.1 스트리밍

**Token Streaming**
- 모델이 생성하는 토큰을 SSE/WebSocket으로 즉시 전송.
- 왜: 대화 UX에 필수. 200K 토큰을 안 스트리밍하면 망함.

**Event Streaming**
- 상위 이벤트: tool_call_start, tool_call_end, message_delta 등.
- 대표: LangGraph `astream_events`, OpenAI Responses API events.
- 왜: UI에 에이전트의 추론 단계를 표시할 수 있음.

### 6.2 관측성 (Observability)

**LangSmith**
- LangChain의 상용 트레이싱 + 평가 플랫폼. LangGraph 통합 최고.
- 왜: LangGraph 에이전트의 trajectory view 최강.

**Arize Phoenix**
- 오픈소스 OpenInference/OTel 네이티브 트레이싱 + 평가. 셀프호스트 가능.
- 왜: 디폴트 OSS 관측 플랫폼. 임베딩 시각화가 차별점.

**AgentOps**
- 에이전트 특화 관측. 세션 replay + 비용 추적.
- 왜: 프레임워크 락인 없이 멀티 에이전트 디버깅에 좋음.

**MLflow**
- 클래식 ML 플랫폼 + LLM 트레이싱 + 프롬프트 버저닝 + 에이전트 평가 추가.
- 왜: 회사가 이미 MLflow를 쓴다면 정답.

**OpenLLMetry / OpenInference**
- LLM 스팬을 위한 OpenTelemetry semantic convention.
- 왜: 벤더 중립 트레이싱. 한 번 계측하면 어떤 백엔드에서도 볼 수 있음.

### 6.3 평가 (Evaluation)

**RAGAS**
- 참조 없이 RAG 평가하는 메트릭 라이브러리: faithfulness, answer relevance, context precision/recall.
- 왜: RAG 평가의 진입장벽 최저. 10줄 코드.

**AgentBench**
- 웹·OS·DB·게임 등 작업으로 에이전트 능력 평가하는 벤치마크.
- 왜: 모델의 에이전트 능력 비교에 표준 레퍼런스.

**LLM-as-Judge**
- 강한 LLM을 rubric과 함께 채점자로 사용. 100+ 인간 라벨로 캘리브레이션.
- 왜: 스케일 자동 평가에 저렴. 인간 동의도 65% 이하면 노이즈.

**Trajectory Evaluation**
- 최종 답뿐 아니라 도구 선택·순서 등 중간 단계 채점.
- 대표: LangSmith trajectory evaluators, OpenAI Evals, Phoenix.
- 왜: 에이전트가 실패하면 **어디서** 실패했는지 알아야 함.

**DeepEval / Promptfoo**
- pytest 스타일 평가 라이브러리. CI 게이팅용.
- 왜: 평가 스택의 가벼운 절반 (CI + 대시보드).

### 6.4 가드레일 (Guardrails)

**Prompt Injection**
- 공격자 입력이 시스템 명령을 override (직접, RAG 경유 간접, 멀티턴).
- 왜: OWASP LLM Top-10 #1. 단일 방어 없음 → 다층 방어.

**Guardrails AI**
- Reusable Validator 기반 출력 검증 프레임워크 (Guardrails Hub).
- 왜: 다운스트림 코드가 의존할 수 있는 구조 강제에 최적.

**NVIDIA NeMo Guardrails**
- Colang DSL로 프로그래밍 가능한 대화 rail.
- 왜: 대화 주제·안전 제어에 최적. 규제 산업 표준.

**LLM Guard**
- 오픈소스 입출력 스캐너 모음 (PII, 독성, 인젝션, 시크릿).
- 왜: 빠른 스캐닝 레이어. 첫 가드레일로 좋음.

**Output Validation**
- 모든 모델 출력에 스키마 체크 + 콘텐츠 필터.
- 왜: 저렴하고 ROI 높음. hallucination 포맷과 정책 위반 모두 잡음.

### 6.5 비용 / 캐싱

**Prompt Caching (제공자 측)** ⭐
- prompt prefix의 KV cache 공유. 후속 호출은 prefix를 10~90% 할인.
- 대표: OpenAI(자동, 50% 할인, >1024 토큰), Anthropic(`cache_control`, 90%, 5분/1시간 TTL), Gemini 명시적 캐싱.
- 왜: 에이전트 루프 비용 70~85% 절감. 2026년 필수.

**Semantic Caching**
- prompt를 임베딩 → 유사한 prompt가 캐시에 있으면 캐시된 응답 반환.
- 대표: GPTCache, Redis Semantic Cache, Vercel KV.
- 왜: prompt의 ~31%가 의미적 중복. 비용 추가 30~70% 절감 가능.

**Token Budget**
- 요청당/작업당 토큰 상한 + 조기 종료.
- 대표: Anthropic `task_budget` (2026), 프레임워크 토큰 추적.
- 왜: 에이전트 루프 폭주로 청구서가 터지는 걸 방지.

### 6.6 Human-in-the-Loop (HITL)

**HITL Checkpoint**
- 승인 노드에서 그래프 일시정지 → 사람 결정을 state에 주입하고 재개.
- 대표: LangGraph `interrupt()` + Checkpointer.
- 왜: 되돌릴 수 없는 행동(이메일 전송, 결제, 배포)을 수행하는 모든 에이전트에 필수.

### 6.7 Async / 병렬

**Async Tool Calls**
- 한 에이전트 턴에서 여러 도구 호출을 동시 실행.
- 대표: LangGraph `Promise.all` 스타일, OpenAI `parallel_tool_calls`.
- 왜: 읽기 전용 멀티 도구 단계의 지연 대폭 감소.

**Fan-Out / Map-Reduce**
- 작업을 N개 병렬 subagent로 분할 → 출력 병합.
- 왜: 다문서 요약, 병렬 리서치의 실제 구현 방식.

---

## 7. 프레임워크 지형

| 프레임워크 | 한 줄 설명 | 언제 |
|----------|----------|------|
| **LangChain** | LLM 앱 일반 프레임워크 (chains, retrievers, 통합) | 통합 가장 많음. 이주해도 lingua franca |
| **LangGraph** ⭐ | LangChain의 그래프 기반 stateful 에이전트 런타임 + checkpointing + HITL | **본 워크숍 메인 스택.** stateful 워크플로 프로덕션 디폴트 |
| **LlamaIndex** | 데이터 프레임워크. RAG 인제스션·검색·에이전트 워크플로 | 문서/지식 에이전트 |
| **Google ADK** | Google의 다언어 에이전트 프레임워크. 네이티브 A2A + Vertex AI | GCP 네이티브, Gemini 작업 |
| **CrewAI** | 역할 기반 멀티 에이전트 ("crew" of roles + tools) | 학습 곡선 최저. 한국 스타트업 프로토타입 빈출 |
| **AutoGen / MS Agent Framework** | MS 대화형 멀티 에이전트 (AutoGen) + 통합 후계자 (Agent Framework, 2026) | MS 스택 |
| **Pydantic AI** | Pydantic 팀의 타입 안전 Python 에이전트 | Python 타입 진심. Logfire 통합 최고 |
| **smolagents** | HuggingFace의 ~1000 LOC 코드 실행 에이전트 | 계산 에이전트, 끝까지 코드 읽기 가능 |
| **Anthropic Agent SDK** | (구 Claude Code SDK) MCP + computer-use 깊은 통합 | Claude 네이티브 에이전트, Claude Code 기반 |
| **OpenAI Agents SDK** | Swarm 후계자. agents, handoffs, tracing, guardrails, sandboxes | OpenAI 생태계 최고 DX. 내장 트레이싱 우수 |
| **Mastra** | TypeScript-first 에이전트 (workflows, memory, evals, RAG) | TS / Next.js / Node 스택의 사실상 디폴트 |

---

## 부록: 2026년 안전한 디폴트

| 레이어 | 디폴트 |
|------|------|
| 로컬 LLM | Ollama (Q4_K_M GGUF) |
| GPU 서빙 | vLLM (또는 공유 prefix 워크로드는 SGLang) |
| 호스팅 멀티 모델 | OpenRouter |
| Vector DB | Postgres 있으면 pgvector, 아니면 Qdrant |
| 임베딩 | `text-embedding-3-large` 또는 `voyage-3-large` |
| Reranker | Cohere Rerank 3 |
| 에이전트 프레임워크 (Python) | LangGraph (복잡) 또는 Pydantic AI (단순) |
| 에이전트 프레임워크 (TypeScript) | Mastra |
| 메모리 | mem0 (드롭인) 또는 Letta (깊이) |
| 도구 프로토콜 | MCP |
| 에이전트 간 | A2A |
| 트레이싱 | LangSmith (LC 스택) 또는 Phoenix (OSS) |
| 평가 | RAGAS (RAG) + DeepEval (CI) |
| 가드레일 | LLM Guard + Guardrails AI |
| 캐싱 | 제공자 prompt caching 먼저, semantic caching 다음 |

---

## 🎯 본 워크숍에서 직접 다루는 개념 (체크리스트)

Day 1:
- [x] LLM, 토큰, 임베딩, 컨텍스트, 환각
- [x] Tool / Function Calling, JSON Schema
- [x] Prompt (system/user/assistant), Prompt Template, Few-Shot
- [x] Embeddings, Chroma Vector Store, BM25 개념 소개
- [x] LangChain RAG 5대 컴포넌트
- [x] LangGraph State (TypedDict), Node, Edge, Conditional Edge, ToolNode
- [x] Checkpointer, thread_id, 단기/장기 메모리 구분
- [x] Streaming (token)
- [x] Ollama, OpenRouter (개념 소개)

Day 2:
- [x] 멀티 에이전트 패턴: Supervisor, Hierarchical 비교
- [x] Handoff, Subagent
- [x] Skills (Claude Code 스타일 개념)
- [x] Context Engineering, Context Rot, Compaction (개념)
- [x] Reflection / Self-Refine
- [x] MCP, A2A (개념 소개)
- [x] Prompt Injection, Output Validation (보안 점검)
- [x] Prompt Caching, Token Budget (비용)
- [x] HITL Checkpoint (LangGraph `interrupt()`)
- [x] Streamlit Cloud 배포, Secrets 관리

> **이수자 권장 다음 학습**: vLLM, AWQ 양자화, mem0 또는 Letta, RAGAS 평가, LangSmith 트레이싱, MCP 서버 직접 구축.
