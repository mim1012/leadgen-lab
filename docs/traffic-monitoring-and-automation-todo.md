# Traffic Monitoring and Channel Automation TODO

## Purpose

이 문서는 `moving-quote-call-burden` 캠페인의 유입 모니터링, 알림 기준, Threads / Naver Blog / Naver Cafe 자동화 범위를 정한다.

핵심 원칙:

- 먼저 측정 가능한 유입-클릭-DB 품질 루프를 만든다.
- 자동화는 초안 생성, UTM, 알림, 리포트부터 한다.
- 게시 자동화는 공식 API, 계정 권한, 채널 규칙, per-post human approval이 확인된 채널만 허용한다.
- 댓글, 좋아요, DM, 반복 링크 드롭, 카페 활동 자동화는 하지 않는다.

## Current Baseline

Existing tracking assets:

- Landing: `outputs/sites/moving-quote-call-burden/index.html`
- Campaign config: `data/campaigns/moving-quote-call-burden.yaml`
- Draft queue generator: `src/marketing_automation.py`
- Metrics ledger: `outputs/marketing/moving-quote-call-burden/*/metrics_template.csv`
- Current browser-side events: `page_view`, `selector_choice`, `diagnosis_completed`, `checklist_toggled`, `outbound_cta_clicked`

Known gap:

- The landing currently stores event data in browser `localStorage`; this is useful for local QA but not enough for source-level production monitoring.

## Measurement Events To Capture Server-Side

Minimum event schema:

| Field | Example | Why it matters |
| --- | --- | --- |
| `event_name` | `page_view`, `diagnosis_completed`, `outbound_cta_clicked` | funnel step |
| `campaign` | `moving_quote_call_burden` | campaign grouping |
| `utm_source` | `threads`, `naver_blog`, `naver_cafe` | channel attribution |
| `utm_medium` | `social`, `post`, `community` | medium attribution |
| `utm_content` | `thread_call_control` | content variant |
| `cta_position` | `hero`, `diagnosis_ready`, `final` | CTA quality |
| `diagnosis_result` | `ready`, `prepare_first` | lead quality signal |
| `date_bucket` | `55일 이내`, `55일 이후`, `미정` | Adlix eligibility quality |
| `contact_bucket` | `상담 가능`, `시간 제한`, `전화 불가` | rejection-risk filter |
| `session_id` | random UUID | dedupe without personal data |
| `ts` | ISO datetime | hourly/daily reporting |

Do not capture locally in v1:

- name,
- phone number,
- exact address,
- partner-form contents,
- cookies that identify a person across unrelated sites.

## Recommended Monitoring Stack

### Phase 1: No-backend / fastest

Use Vercel Web Analytics or equivalent page analytics plus manual Adlix dashboard checks.

Alerts are generated from a daily metrics CSV filled manually:

- `landing_visits`
- `outbound_clicks`
- `outbound_ctr`
- `adlix_db_count`
- `approved_count`
- `rejected_count`
- `rejection_notes`

Use this only until first 20 outbound clicks.

### Phase 2: Lightweight event collector

Add `/api/track` or a small external analytics sink.

Requirements:

- accept only campaign event payloads,
- strip or reject personal data,
- persist UTM + event + coarse diagnosis result,
- dedupe by session + event + timestamp bucket,
- expose a daily summary command or report.

Preferred output:

- `outputs/metrics/moving-quote-call-burden/daily-YYYY-MM-DD.json`
- `outputs/metrics/moving-quote-call-burden/weekly-summary.md`

### Phase 3: Alerting

Send notifications to one low-noise channel first: Slack, Telegram, Discord, or email.

Recommended alert cadence:

- hourly only for hard failures,
- daily for campaign performance,
- weekly for strategy decisions.

## Alert Rules

### Hard Failure Alerts

Send immediately:

1. Landing returns non-200 or contains no outbound CTA.
2. Outbound link is missing `appu.kr` promotion URL.
3. Event collector has zero `page_view` for 6 hours while published posts are live.
4. Event collector receives `outbound_cta_clicked` but cannot persist the event.
5. UTM source/content is missing from more than 20% of visits.

### Daily Performance Alerts

Send once per day:

1. `landing_visits >= 30` and `outbound_ctr < 4%`
   - Action: revise first-screen copy or CTA clarity.
2. `outbound_clicks >= 20` and `adlix_db_count = 0`
   - Action: inspect partner page handoff and CTA expectation mismatch.
3. `outbound_ctr >= 8%` and `rejected_count > approved_count`
   - Action: tighten 55-day and consultation-call qualification.
4. `naver_blog` produces visits but low selector completion.
   - Action: align article promise with landing hero.
5. `threads` produces clicks but short sessions / low ready result.
   - Action: reduce curiosity-bait hooks; prequalify in post copy.

### Positive Alerts

Send when:

1. first outbound click occurs,
2. first Adlix DB occurs,
3. first approved DB occurs,
4. a source reaches `20 outbound_clicks`,
5. a content variant beats baseline by 30%+ outbound CTR with at least 20 clicks.

## Decision Thresholds

| Condition | Decision |
| --- | --- |
| `<20 outbound_clicks` | keep collecting, do not scale |
| `outbound_ctr <4%` after 30+ visits | fix landing CTA / hero |
| `outbound_ctr 4-8%` | keep testing content angles |
| `outbound_ctr >8%` and DB quality weak | tighten qualification |
| `approved DB exists` | generate next queue from winning source/content |
| `20+ clicks with no DB` | inspect partner offer fit before more traffic |

## Channel Automation TODO

### Shared TODO

- [ ] Keep content generation draft-only by default.
- [ ] Require `[광고]` disclosure in title or first visible line.
- [ ] Generate UTM links per channel/content/CTA.
- [ ] Store published URL back into metrics ledger.
- [ ] Capture screenshot/text evidence after publication.
- [ ] Add a daily metrics summary job.
- [ ] Add alert delivery through one channel.
- [ ] Add per-post approval status: `draft`, `approved`, `published`, `paused`.

### Threads

Official feasibility:

- Meta's Threads API supports creating and publishing posts through official app/API flow.
- Threads API also exposes insights for the authenticated user's own Threads.

TODO:

- [ ] Create Meta developer app with Threads use case.
- [ ] Implement OAuth/token storage outside the repository.
- [ ] Add post container creation + publish only for `approved` queue items.
- [ ] Pull post insights daily: views, likes, replies, reposts, quotes when available.
- [ ] Map Threads post ID back to `utm_content`.
- [ ] Alert on replies that need human response; do not auto-reply.

Allowed automation:

- draft generation,
- scheduled post publishing through official API after approval,
- own-post insight retrieval,
- reply notification.

Not allowed:

- automated replies,
- automated follows/likes,
- mass mentions,
- scraping timelines or engaging with unrelated users.

### Naver Blog

Official feasibility:

- Naver official Blog Search API retrieves blog search results; it is not a publishing API.
- The currently documented official OpenAPI categories include Naver Cafe posting, but not a comparable Blog write endpoint in the inspected API list.

TODO:

- [ ] Keep Naver Blog as manual-publish until an official write API or approved partner workflow is verified.
- [ ] Automate draft creation, formatting checklist, UTM insertion, and publish reminder.
- [ ] After manual publish, paste the published URL into `metrics_template.csv`.
- [ ] Monitor Naver Blog search exposure through official Search API queries for target keywords.
- [ ] Capture rank/exposure snapshots for `이사 견적 신청`, `이사 견적 전화`, `포장이사 추가요금`.

Allowed automation:

- article drafts,
- title variants,
- UTM links,
- reminders,
- search monitoring,
- screenshot/evidence capture after manual URL input.

Not allowed until separately verified:

- browser-bot posting,
- account login automation,
- CAPTCHA/session bypass,
- automatic comments or neighbor activity.

### Naver Cafe

Official feasibility:

- Naver Cafe has an OAuth-based official API for joining a cafe and writing a cafe article.
- Even with an API, each cafe's rules and affiliate-link policy must be checked before posting.

TODO:

- [ ] Verify Naver Login API app approval and Cafe API permission.
- [ ] For each cafe, record `clubid`, `menuid`, posting rules, affiliate-link allowance, and disclosure rule.
- [ ] Add manual approval before each cafe post.
- [ ] Implement post creation only for approved cafes and approved queue items.
- [ ] Store returned article URL into metrics ledger.
- [ ] Add cooldown/rate limit per cafe.
- [ ] Prefer value-first posts with full checklist in body; landing link optional.

Allowed automation:

- draft generation,
- official API posting after explicit approval,
- published URL capture,
- monitoring own post URL availability.

Not allowed:

- bulk cafe joining,
- repeated link drops,
- comments/likes/DM automation,
- posting where affiliate/sponsored content is disallowed,
- scraping private cafe content into public assets.

## First Implementation Order

1. Add server-side outbound click logging.
2. Add daily metrics summary from event logs + manual Adlix fields.
3. Add alert rule engine with dry-run output.
4. Wire one notification channel.
5. Add Threads official API integration for approved posts only.
6. Keep Naver Blog manual; automate drafts and search monitoring.
7. Add Naver Cafe official API posting only after per-cafe rule registry exists.

## Source Notes

Official docs checked on 2026-06-13:

- Meta Threads API docs: https://developers.facebook.com/docs/threads/
- Meta Threads create posts docs: https://developers.facebook.com/docs/threads/create-posts/
- Meta Threads insights docs: https://developers.facebook.com/docs/threads/insights/
- Naver OpenAPI list: https://developers.naver.com/docs/common/openapiguide/apilist.md
- Naver Blog Search API: https://developers.naver.com/docs/serviceapi/search/blog/blog.md
- Naver Cafe join/write API: https://developers.naver.com/docs/login/cafe-api/cafe-api.md
