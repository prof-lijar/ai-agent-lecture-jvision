# 프로젝트 주제 10선 — 24/7 작동하는 에이전트

모든 주제의 공통 조건:
- 워커 2~3개 (Supervisor + workers)
- 자동 실행 트리거 명확 (cron / webhook / scheduler)
- **사람의 실제 업무**를 부분 자동화
- 1분 시연 시 "매일 무엇을 하는가"가 한눈에 보임

---

## 5.1 업무 자동화 에이전트 (Work-Related)

### 1. job-hunt-watcher
**한 줄**: 매일 새 채용 공고를 본인 조건에 맞춰 매칭·요약·알림.
**워커**: `Scraper` (JobKorea/Wanted 스캔) · `Matcher` (조건 매칭) · `Notifier` (Slack/Email)
**도구**: `fetch_listings(query)` · `match_resume(jd, profile)` · `send_slack(text)`
**트리거**: 매일 09:00 GitHub Actions cron
**왜 좋은 면접 데모**: 채용 담당자에게 "오늘 아침에도 자동으로 받았어요"가 가장 강력한 어필.
**리스크**: 사이트 robots.txt 준수 / 합리적 요청 간격.

---

### 2. pr-review-bot
**한 줄**: 본인 GitHub 저장소에 PR이 열리면 자동으로 리뷰 코멘트 작성.
**워커**: `Diff Reader` · `Style Checker` · `Logic Reviewer`
**도구**: `gh_pr_diff(num)` · `gh_pr_comment(num, text)` · `run_linter(diff)`
**트리거**: GitHub Actions `on: pull_request`
**왜 좋은 면접 데모**: 본인 저장소에서 라이브로 PR 열어 30초 만에 코멘트 받는 시연.
**리스크**: 비용 — PR마다 LLM 호출. 변경 라인 수에 토큰 캡.

---

### 3. daily-digest-agent
**한 줄**: 본인 관심 RSS/뉴스/X를 매일 아침 모아 요약 다이제스트 1통.
**워커**: `Collector` (소스 폴링) · `Summarizer` (요약) · `Curator` (관심도 점수 정렬)
**도구**: `fetch_rss(url)` · `fetch_url(url)` · `send_email(body)` 또는 `commit_to_repo()`
**트리거**: 매일 07:00 cron
**왜 좋은 면접 데모**: "본인 다이제스트 보여주세요" → 폰에서 오늘 메일 보여주기.
**리스크**: 중복 제거 · 출처 명시.

---

### 4. standup-compiler
**한 줄**: 팀 Slack/Notion 채널의 어제 활동을 모아 매일 아침 standup 요약 생성.
**워커**: `Activity Collector` · `Per-Person Summarizer` · `Standup Formatter`
**도구**: `fetch_slack_messages(channel, since)` · `fetch_notion_pages(since)` · `post_to_channel(text)`
**트리거**: 매일 09:30 cron
**왜 좋은 면접 데모**: 본인 사이드 프로젝트 팀에서 실제 사용 중인 모습.
**리스크**: 개인 정보 → 본인 데이터 또는 더미 채널로 데모.

---

### 5. customer-support-triage
**한 줄**: Discord/Slack 문의 메시지를 자동 분류 + 답변 초안 작성 + 필요시 에스컬레이션.
**워커**: `Classifier` (긴급/일반/스팸) · `Drafter` (답변 초안) · `Escalator` (긴급은 멘션)
**도구**: `read_message(payload)` · `post_reply(channel, text)` · `mention_user(uid)`
**트리거**: Discord/Slack webhook
**왜 좋은 면접 데모**: 본인 Discord 서버에서 라이브로 메시지 → 30초 내 답변.
**리스크**: 잘못된 자동 답변 → 항상 "초안" 라벨 또는 사람 승인 단계(HITL).

---

### 6. meeting-notes-agent
**한 줄**: 회의록(텍스트 또는 음성 전사) 업로드 → 액션 아이템 추출 → GitHub Issue 자동 등록.
**워커**: `Extractor` (액션 아이템) · `Assigner` (담당자 추정) · `Issue Creator` (GitHub Issue 생성)
**도구**: `parse_transcript(file)` · `gh_issue_create(title, body, assignee)` · `extract_dates(text)`
**트리거**: 파일 업로드 또는 cron (이메일 첨부 폴링)
**왜 좋은 면접 데모**: 강의 중 회의록 1개 라이브 입력 → 5초 내 Issue 5개 생성.
**리스크**: 잘못된 담당자 지정 → 항상 "review needed" 라벨 부착.

---

## 5.2 취업 준비 에이전트

### 7. interview-prep
**한 줄**: 직무 입력 → 질문 5개 생성 → 답변 받고 STAR 기준 피드백.
**워커**: `Question Maker` · `Mock Interviewer` (후속 질문) · `Feedback` (STAR 평가)
**도구**: `search_company(name)` · `save_session(transcript)`
**트리거**: 사용자 호출 (cron 옵션: 매일 신규 질문 1개 푸시)
**리스크**: 잘못된 회사 정보 → 출처 명시.

---

### 8. resume-tailor
**한 줄**: 채용 공고 URL + 이력서 → 공고에 맞춰진 이력서 + 자기소개서 초안.
**워커**: `JD Parser` · `Resume Editor` · `Cover Letter Writer`
**도구**: `fetch_url(jd)` · `parse_pdf(resume)` · `save_markdown(content)`
**트리거**: 사용자 호출 (즐겨찾는 회사 cron으로 매주 자동 업데이트 가능)
**리스크**: 사실 왜곡 금지 — 이력서의 사실은 추가/변경하지 않고 강조만 재배치.

---

## 5.3 개발자 포트폴리오 에이전트

### 9. mini-dev-team
**한 줄**: 작은 코딩 작업을 받아 Planner + Coder + Reviewer가 협업해 자율 완료.
**워커**: `Planner` (step 분해) · `Coder` (구현) · `Reviewer` (코드 리뷰)
**도구**: `run_python(code)` (샌드박스) · `save_to_file(path, content)` · `read_file(path)`
**트리거**: 사용자 호출 또는 GitHub Issue label trigger
**왜 좋은 면접 데모**: 강사 `orchast_agent/dev-team` 풀버전과 같은 패턴 → "엔터프라이즈 멀티 에이전트와 같은 아키텍처" 어필.
**리스크**: 코드 실행 보안 → 서브프로세스 + 타임아웃 + 디스크 격리 필수.

---

### 10. personal-research-agent
**한 줄**: 주제 입력 → 매주 자동으로 리서치 보고서 생성 후 Notion/GitHub 저장.
**워커**: `Researcher` (웹 검색) · `Writer` (1500자 보고서) · `Editor` (출처 인용 검증)
**도구**: `web_search(q)` · `fetch_url(url)` · `commit_to_repo(filename, content)`
**트리거**: 매주 월요일 08:00 cron
**왜 좋은 면접 데모**: 본인 GitHub의 `research/` 폴더에 매주 누적되는 보고서 보여주기 = "꾸준함의 증거".

---

## 강사 1:1 컨펌 체크리스트

학생이 위 10개 외 주제를 제안할 때 통과 기준:
- [ ] 워커 ≤ 3
- [ ] 도구 ≤ 4
- [ ] 외부 의존성 ≤ 2 (API, 사이트, DB 등)
- [ ] **24/7 자동 실행 시나리오가 1줄로 설명 가능** ("매일 09시 cron으로 X 후 Y")
- [ ] 1분 데모로 "매일 무엇을 하는가"가 보임

> 협상 불가: **24/7 트리거 명시** + **워커 3개 이내**. 시간 안에 못 끝남.
