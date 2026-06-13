# Growth Conversion Review 2026-06-10

## Scope

Campaign:

- `moving-quote-call-burden`
- Production: `https://moving-quote-call-burden.vercel.app`
- Offer: Adlix `다이사 이사 가격비교`
- Revenue event: valid partner-side consultation request DB
- Payout: `20,000p` per approved DB, visible approval rate around `78%`

Current funnel:

1. Naver Blog, Threads, or community-safe educational post.
2. Static pre-lander with checklist and selector.
3. Outbound CTA to Adlix Daisa promotion URL.
4. Partner-side quote request form.
5. Revenue only when the DB is valid and approved.

## CLI Council Status

Requested participants:

- Claude CLI
- Gemini CLI
- Antigravity CLI

Environment result:

- Claude CLI exists at `D:\claudecode\claude.cmd`, version `2.1.158`, but non-interactive `-p` calls timed out and did not return an answer.
- Gemini CLI is not installed or not on PATH. `omx ask gemini` failed with `Missing required local CLI binary: gemini`.
- Antigravity CLI is not installed or not on PATH under `antigravity`, `antigravity-cli`, or `ag`.

Decision:

- Do not invent external model opinions.
- Use the current landing, campaign docs, and known CPA constraints to produce the actionable review below.

## Main Diagnosis

The landing is useful, compliant, and safe, but it is still too educational relative to the monetization event.

The current page lowers anxiety before application, but the CTA is late and the page does not strongly filter for users who can become valid approved DBs. For this offer, conversion quality matters as much as outbound CTR because rejected leads include wrong number, duplicate, long absence, refusal, and non-user submissions.

The page should therefore optimize for:

- people moving within 55 days,
- people willing to receive consultation contact,
- people who understand this is a quote comparison request,
- people who have enough move details ready to complete the partner form.

## Highest-Impact Bottlenecks

1. The hero CTA says `3분 준비표 시작하기`, but the revenue path needs users to understand the next step is a quote comparison request.
2. The `55일 이내 이사날짜` eligibility rule appears only near the final CTA, too late in the page.
3. The selector collects intent, but it does not produce a strong CTA state after selection.
4. The final CTA copy `제한 비교 견적 보기` is cautious, but not concrete enough for users who are ready.
5. The page has no compact "who this is for / not for" filter, so low-quality clicks may reach the partner form.
6. The warning about phone calls is honest, but the page can make the desired action clearer: "상담 받을 시간과 업체 수를 정한 뒤 신청".
7. There is no visible proof or neutral trust explanation for why Daisa/comparison is the next step.
8. Local tracking is only browser-local, so actual source-to-click learning is weak unless Vercel/analytics logs are reviewed separately.

## Landing Changes To Make Before Traffic

### 1. Add eligibility strip above the fold

Add a short strip directly under the hero lead:

> 신청 전 확인: 이사 예정일이 55일 이내이고, 견적 상담 연락을 받을 수 있는 경우에만 신청하세요.

Reason:

- Increases approved DB quality.
- Reduces 상담거절, 장기부재, date-ineligible traffic.
- Makes the monetization event more aligned with user intent.

### 2. Change primary hero CTA

Current:

> 3분 준비표 시작하기

Test variant:

> 내 조건 정리하고 비교 견적 확인하기

Reason:

- Still starts with preparation.
- But connects preparation to the revenue CTA earlier.

### 3. Add a selector-complete CTA

After the user selects at least 3 selector options, show a direct CTA under the recommendation:

> 선택한 조건으로 비교 견적 보러가기

Reason:

- The highest-intent moment is immediately after interaction, not necessarily at the bottom.

### 4. Add "신청하면 연락이 올 수 있음" near CTA

Use direct but non-alarming copy:

> 견적 비교 신청 후 상담 연락이 올 수 있습니다. 연락 가능한 시간과 상담받을 업체 수를 먼저 정해두세요.

Reason:

- Prevents misleading "전화폭탄 방지" interpretation.
- Filters users who will reject consultation calls.

### 5. Replace stale placeholder copy

Current final CTA subcopy still says:

> 실제 제휴 링크는 홍보 URL 생성 후 연결됩니다.

Change to:

> 다이사 제휴 견적 신청으로 이동합니다. 이사 예정일은 55일 이내일 때 신청 가능합니다.

Reason:

- The promotion URL is already generated.
- Placeholder language reduces trust.

## First 7-Day Traffic Plan

### Day 1: Tracking baseline and first article

Publish one Naver Blog post:

- Title: `[광고] 이사 견적 전화폭탄 줄이는 체크리스트: 신청 전 정리할 7가지`
- CTA position: after the useful checklist, not at the top only.
- CTA wording: `3분 준비표로 내 조건 먼저 정리하기`

Goal:

- Warm, search-compatible traffic.
- Avoid community spam.

### Day 2: Threads pain hooks

Post 3 short Threads:

- "이사 견적 신청할 때 제일 먼저 정해야 하는 건 업체가 아니라 몇 곳까지 상담받을지임."
- "사다리차/주말/분해설치 빠진 견적은 싸 보여도 최종 비용이 달라질 수 있음."
- "전화가 부담스러우면 신청 전에 연락 가능 시간부터 적어두는 게 낫다."

CTA:

- Comment or profile link to landing.
- Do not mass-post or automate replies.

### Day 3: Community-safe value post

Use only communities where affiliate disclosure and external links are allowed.

Recommended structure:

- Start with `[광고]`.
- Share the checklist content in the post itself.
- Add landing as optional source, not as the whole post.

Avoid:

- fake personal review,
- pretending to be a neutral customer,
- repeated link drops,
- copied posts across many cafes.

### Day 4: Publish second Naver Blog article

Title:

- `[광고] 포장이사 견적 신청 전 꼭 물어볼 추가요금 질문 10가지`

CTA:

- `추가요금 질문까지 정리하고 비교 견적 확인하기`

### Day 5: Review first signals

Minimum metrics:

- landing visits,
- hero CTA clicks,
- selector interactions,
- outbound CTA clicks,
- outbound CTR by source,
- visible Adlix DB count if available.

Decision rule:

- If outbound CTR is under 4%, fix CTA clarity.
- If outbound CTR is high but DB approval is weak, add stronger eligibility and call-consent filtering.

### Day 6: Third content angle

Title:

- `[광고] 사진 견적 vs 방문 견적, 이사할 때 어떤 방식이 맞을까?`

Use this to capture higher-intent users with more complex moves.

### Day 7: Double down

Keep the best source and best post angle.

Do not scale until:

- at least 20 outbound clicks,
- source-level CTR is known,
- no obvious compliance issue,
- at least some Adlix-side conversion signal is visible.

## A/B Test Backlog

### Headline

A:

> 이사 견적 신청 전, 전화폭탄 줄이는 3분 준비표

B:

> 이사 견적 신청 전에 정리하면 상담이 짧아지는 7가지

C:

> 포장이사 견적 비교 전, 추가요금 질문부터 정리하세요

Hypothesis:

- A has stronger pain.
- B is safer and more practical.
- C may attract higher purchase intent.

### CTA

A:

> 제한 비교 견적 보기

B:

> 준비한 조건으로 비교 견적 확인하기

C:

> 다이사 견적 비교 신청하러 가기

Hypothesis:

- B is best balance between trust and intent.
- C may lift CTR but could increase low-quality clicks unless paired with eligibility copy.

### Selector

A:

- Current 4 groups.

B:

- Add first question: `이사 예정일이 55일 이내인가요?`

C:

- Add final selector result CTA.

Hypothesis:

- B improves DB approval quality.
- C improves outbound CTR.

### Trust/Disclosure

A:

- Current top disclosure only.

B:

- Disclosure plus "개인정보는 이 페이지에서 수집하지 않습니다" near CTA.

C:

- Add "신청 후 상담 연락이 올 수 있습니다" near CTA.

Hypothesis:

- B improves landing trust.
- C reduces partner-side 상담거절.

## Later Automation Plan

Only automate after the manual loop proves at least one source converts.

Phase 1:

- Generate content briefs from winning angle.
- Keep manual publishing.
- Track source UTM and outbound click events server-side.

Phase 2:

- Create weekly content calendar.
- Auto-draft Naver Blog and Threads variants.
- Human review before publishing.

Phase 3:

- Build source-quality scoring:
  - visits,
  - selector completion,
  - outbound CTR,
  - partner DB count,
  - approval/rejection feedback if available.

Do not automate:

- cafe account activity,
- comments,
- fake reviews,
- DMs,
- repeated link posting.

## Immediate Execution Order

1. Fix final CTA placeholder copy.
2. Add 55-day eligibility strip above the fold.
3. Add selector-complete CTA.
4. Publish the first Naver Blog article.
5. Publish 3 Threads posts.
6. Review after 20 outbound clicks.
7. Only then decide whether to add more traffic channels or automate content generation.

