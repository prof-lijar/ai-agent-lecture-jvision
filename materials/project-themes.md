# Day 2 본인 프로젝트 주제 12선

Day 2부터 학생이 선택하는 본인 프로젝트 후보. 모든 주제 공통 조건:
- 워커 2~3개 (Supervisor + workers)
- 도구 2~3개 (커스텀 도구 작성 포함)
- 4시간 안에 v1 완성 가능
- 1분 시연으로 "이게 뭘 하는가"가 한눈에 보임

---

## 5.1 Work — 직장 업무 자동화

### 1. pr-review-bot
**한 줄**: 본인 GitHub 저장소에 PR이 열리면 자동으로 리뷰 코멘트 작성.
**워커**: `Diff Reader` · `Style Checker` · `Logic Reviewer`
**도구**: `gh_pr_diff(num)` · `gh_pr_comment(num, text)` · `run_linter(diff)`
**왜 좋은 시연**: 본인 저장소에서 라이브로 PR 열어 30초 만에 코멘트 받는 모습.
**리스크**: 비용 — PR마다 LLM 호출. 변경 라인 수에 토큰 캡.

### 2. meeting-notes-agent
**한 줄**: 회의록(텍스트 또는 음성 전사) 입력 → 액션 아이템 추출 → GitHub Issue 자동 등록.
**워커**: `Extractor` (액션 아이템) · `Assigner` (담당자 추정) · `Issue Creator`
**도구**: `parse_transcript(file)` · `gh_issue_create(title, body, assignee)` · `extract_dates(text)`
**왜 좋은 시연**: 회의록 1개 라이브 입력 → 5초 내 Issue 5개 생성.
**리스크**: 잘못된 담당자 지정 → "review needed" 라벨 자동 부착.

### 3. mini-dev-team
**한 줄**: 작은 코딩 작업을 받아 Planner + Coder + Reviewer가 협업해 자율 완료.
**워커**: `Planner` (step 분해) · `Coder` (구현) · `Reviewer` (코드 리뷰)
**도구**: `run_python(code)` (샌드박스) · `save_to_file(path, content)` · `read_file(path)`
**왜 좋은 시연**: 강사 `orchast_agent/dev-team` 풀버전과 같은 아키텍처 패턴.
**리스크**: 코드 실행 보안 → 서브프로세스 + 타임아웃 + 디스크 격리 필수.

---

## 5.2 Real Problems — 실생활 문제 해결

### 4. interview-prep
**한 줄**: 직무 입력 → 모의 면접 + STAR 프레임워크 피드백.
**워커**: `Question Maker` · `Mock Interviewer` (후속 질문) · `Feedback` (STAR 평가)
**도구**: `search_company(name)` · `save_session(transcript)` · `score_answer(text, rubric)`
**왜 좋은 시연**: 본인이 지원하는 회사로 모의 면접 30초 시연.
**리스크**: 잘못된 회사 정보 → 출처 명시 + AI 답변임을 알림.

### 5. resume-tailor
**한 줄**: 채용 공고 URL + 이력서 → 공고에 맞춰진 이력서 + 자기소개서 초안.
**워커**: `JD Parser` · `Resume Editor` · `Cover Letter Writer`
**도구**: `fetch_url(jd)` · `parse_pdf(resume)` · `save_markdown(content)`
**왜 좋은 시연**: 본인 이력서 + 실제 공고 URL → 즉석 맞춤본.
**리스크**: 사실 왜곡 금지 — 이력서의 사실은 추가/변경하지 않고 강조만 재배치.

### 6. customer-support-triage
**한 줄**: Discord/Slack 문의 메시지를 자동 분류 + 답변 초안 + 필요시 에스컬레이션.
**워커**: `Classifier` (긴급/일반/스팸) · `Drafter` (답변 초안) · `Escalator` (긴급은 멘션)
**도구**: `read_message(payload)` · `post_reply(channel, text)` · `mention_user(uid)`
**왜 좋은 시연**: 본인 Discord 서버에서 라이브 메시지 → 30초 내 답변.
**리스크**: 잘못된 자동 답변 → 항상 "초안" 라벨 또는 사람 승인 단계(HITL).

---

## 5.3 Personal — 개인용

### 7. daily-digest-agent
**한 줄**: 본인 관심 RSS/뉴스/X를 모아 요약 다이제스트 1통 생성.
**워커**: `Collector` (소스 폴링) · `Summarizer` (요약) · `Curator` (관심도 점수 정렬)
**도구**: `fetch_rss(url)` · `fetch_url(url)` · `send_email(body)` 또는 `commit_to_repo()`
**왜 좋은 시연**: "본인 오늘의 다이제스트 보여주세요" → 폰에서 보여주기.
**리스크**: 중복 제거 · 출처 명시.

### 8. study-buddy-crew
**한 줄**: 학습 자료(PDF·노트) 입력 → 퀴즈 생성 + 모르는 개념 튜터링 + 채점.
**워커**: `Quiz Maker` (객관식 5문제) · `Tutor` (개념 질문 답변) · `Grader` (답안 채점·해설)
**도구**: `load_document(pdf|url)` · `save_progress(user_id, score)` · `lookup_concept(term)`
**왜 좋은 시연**: 본인 전공 책으로 데모. 시험 직전 공부 도우미.
**리스크**: 환각으로 잘못된 정답 → 채점 시 RAG 인용 표시 강제.

### 9. personal-finance-categorizer
**한 줄**: 가계부 CSV(은행 거래내역) → 자동 분류 + 주간 리포트 + 차트.
**워커**: `Transaction Reader` (CSV 파싱) · `Categorizer` (카테고리 분류) · `Reporter` (요약 + 차트)
**도구**: `parse_csv(file)` · `classify_transaction(text)` · `generate_chart(data)`
**왜 좋은 시연**: 본인 한 달치 거래 → 1초에 카테고리별 차트.
**리스크**: 개인 금융 데이터 → 더미 데이터로 데모. 분류 오류는 사용자 수정 UI 제공.

---

## 5.4 Fun & Easy & Interesting — 재미

### 10. ai-storyteller
**한 줄**: 짧은 프롬프트 → 단편소설/웹툰 시나리오 한 챕터 자동 생성.
**워커**: `Plot Designer` (구조 설계) · `Character Designer` (인물 카드) · `Dialogue Writer` (대화 작성)
**도구**: `save_chapter(text)` · `check_continuity(prev_chapter, new_chapter)` · `name_generator(gender, era)`
**왜 좋은 시연**: 강의실에서 학생 1명이 한 줄 프롬프트 입력 → 1분 뒤 모두가 한 챕터 읽으며 폭소.
**리스크**: 표절 회피 — 출처/스타일 명시. 폭력·성적 콘텐츠는 시스템 프롬프트로 차단.

### 11. dnd-dungeon-master
**한 줄**: 텍스트 RPG의 Dungeon Master 역할. 학생이 말하면 에이전트가 응대.
**워커**: `Narrator` (장면 묘사) · `NPC` (캐릭터 연기) · `Rule Master` (규칙·주사위 판정)
**도구**: `roll_dice(sides)` · `check_inventory(player)` · `update_story_state(event)`
**왜 좋은 시연**: 강의실에서 라이브 플레이 — 학생들이 입력 던지면 즉석 진행. 도구 호출(주사위)이 가장 자연스럽게 보이는 시연.
**리스크**: 폭력적 콘텐츠 → PG-13 시스템 프롬프트.

### 12. playlist-curator
**한 줄**: "오늘 비 오는 카페에서 들을 음악" 류 자연어 입력 → 큐레이션 플레이리스트.
**워커**: `Mood Reader` (분위기·상황 파악) · `Song Selector` (곡 선정) · `Order Optimizer` (순서 최적화)
**도구**: `search_song(query)` · `fetch_lyrics(song_id)` · `build_youtube_playlist(songs)`
**왜 좋은 시연**: 결과를 즉시 YouTube/Spotify 링크로 들을 수 있음.
**리스크**: 저작권 — 음원 직접 출력 X, 링크/플레이리스트만.

---

## 강사 1:1 컨펌 체크리스트

학생이 위 12개 외 본인 주제를 제안할 때:
- [ ] 워커 ≤ 3
- [ ] 도구 ≤ 4
- [ ] 외부 의존성 ≤ 2 (API · 사이트 · DB)
- [ ] 1분 시연으로 "무엇을 하는가"가 한눈에 보임
- [ ] 4시간 안에 v1 완성 가능 — 너무 야심차면 강사가 스코프 다운 협상

> 협상 불가: **워커 3개 이내**. 시간 안에 끝나지 않음.
