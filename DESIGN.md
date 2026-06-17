# Design

## Source of truth

- Status: Active
- Last refreshed: 2026-06-17
- Primary product surfaces:
  - Static pre-lander: `outputs/sites/moving-quote-call-burden/index.html`
  - Campaign config: `data/campaigns/moving-quote-call-burden.yaml`
- Evidence reviewed:
  - Current landing HTML/CSS/JS in `outputs/sites/moving-quote-call-burden/index.html`
  - Campaign terms in `data/campaigns/moving-quote-call-burden.yaml`
  - Adlix Daisa notes in `docs/research/adlix-daisa-campaign-detail-20260610.md`
  - 2026-06-17 browser verification: Appu promotion URL redirects to Adlix Daisa form with publisher/campaign parameters.
  - External research direction: people-first helpful content, trust-first UX, landing clarity/message match, and friction reduction before form handoff.

## Brand

- Personality: practical, calm, transparent, and utility-first.
- Trust signals:
  - Make `[광고]` and 제휴 수익 disclosure visible without making the page feel like a bait ad.
  - Explain that the local page does not collect personal data.
  - Explain application readiness in user language, not affiliate-platform language.
  - Keep internal routing terms like Adlix/Appu/DB out of the main body copy; reserve legal/affiliate disclosure for disclosure areas.
- Avoid:
  - Coupon/urgency aesthetics.
  - Fake neutrality.
  - “최저가”, “전화 없음”, “무조건 절약” claims.
  - A mandatory quiz that does not actually prefill or submit the partner form.

## Product goals

- Goals:
  - Give users a real reason to pass through the pre-lander before Daisa: reduce additional-fee anxiety and clarify application readiness.
  - Send qualified users to the Adlix/Appu Daisa offer with minimal friction.
  - Preserve compliance: disclose affiliate relationship, route 55-day moving-date users, avoid local personal-data capture.
  - Improve outbound CTA quality, not just raw clicks.
- Non-goals:
  - Do not collect name, phone, exact address, or partner form data locally.
  - Do not automate Daisa form submission or prefill personal data unless campaign terms and privacy handling are explicitly approved later.
  - Do not pretend the local checklist is the actual quote request.
- Success signals:
  - Outbound click rate reaches at least the campaign baseline target in `data/campaigns/moving-quote-call-burden.yaml`.
  - Adlix dashboard shows valid DBs after traffic starts.
  - Rejection reasons do not cluster around date ineligibility, duplicate/invalid phone, or consultation refusal.
  - Users click from content variants that match the landing promise: “additional-fee checklist before moving quote request”.

## Personas and jobs

- Primary personas:
  - Near-term mover: has a moving date within 55 days and is ready to receive consultation calls.
  - Anxious comparer: wants quotes but fears extra fees, too many calls, or unclear consent.
  - Research-stage mover: date is not fixed; should save the checklist, not be pushed hard into the CPA flow.
- User jobs:
  - “Before I submit my phone number, tell me what will happen.”
  - “Tell me what extra fees I should ask about.”
  - “Help me decide whether I should apply now or later.”
- Key contexts of use:
  - Mobile social traffic from Threads.
  - Mobile/desktop search traffic from Naver Blog.
  - Users arrive skeptical because the page is between content and the known Daisa form.

## Information architecture

- Primary navigation:
  - No broad navigation. Use a single-page funnel with anchored sections.
- Core routes/screens:
  - Hero/decision block.
  - “신청 전에 준비할 것” readiness explainer.
  - Additional-fee checklist.
  - Optional readiness self-check.
  - Trust/disclosure block.
  - Final CTA.
- Content hierarchy:
  1. Direct reason to stay: “견적 신청 전 당일 추가요금 6가지만 확인하세요.”
  2. Immediate qualified CTA: “55일 이내 이사라면 다이사 가격비교 신청하기.”
  3. Readiness transparency: “연락처, 이사 날짜, 주소, 큰 짐, 상담 가능 시간을 미리 준비합니다.”
  4. Checklist value: 사다리차, 주말/손 없는 날, 분해설치, 대형가전, 층수/엘리베이터, 상담 가능 시간.
  5. Optional self-check, not a gate.
  6. Final sponsored CTA and disclosure.

## Design principles

- Principle 1: CTA-first for ready users.
  - If the user is already qualified, do not force a local quiz before the partner CTA.
- Principle 2: Utility-first for skeptical users.
  - The pre-lander earns its place by answering “what should I check before giving my phone number?”
- Principle 3: Natural transparency.
  - Explain what users need to prepare without making the page sound like an affiliate routing notice.
- Principle 4: Reduce form shock.
  - Before the CTA, show what fields the partner page asks for and why.
- Tradeoffs:
  - More explanation can reduce impulsive clicks but should improve DB quality.
  - The optional self-check may help anxious users, but if it dominates the first viewport it hurts conversion.

## Visual language

- Color:
  - Background: `#f7f5ef`
  - Surface: `#ffffff`
  - Subtle surface: `#fcfbf7`
  - Primary text: `#18201c`
  - Secondary text: `#53615a`
  - Muted text: `#768078`
  - Border: `#ddd8cd`
  - Primary action: `#17624f`
  - Primary dark: `#0d4035`
  - Primary soft: `#e7f2ed`
  - Affiliate/accent: `#d8662f`
  - Accent soft: `#fff0e5`
  - Warning soft: `#fff8e8`
- Typography:
  - Use Korean system sans-serif fonts: `"Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif`.
  - Headlines should be short, concrete, and action-oriented.
- Spacing/layout rhythm:
  - Mobile-first; first CTA should appear without long scrolling on mobile.
  - Use full-width sections with constrained inner content.
- Shape/radius/elevation:
  - Radius around 8-10px.
  - Shadow sparingly, max around `0 18px 48px rgba(24, 32, 28, 0.10)`.
- Motion:
  - Minimal. Avoid decorative motion that makes the page feel like a sales funnel.
- Imagery/iconography:
  - Use functional checklist icons only if they clarify the field/category. Avoid generic moving-truck stock visuals unless they add trust.

## Components

- Existing components to reuse:
  - Header/brand badge.
  - Primary/secondary buttons.
  - Checklist rows.
  - Risk cards.
  - Diagnostic chips as optional self-check.
  - Tracking hooks: `outbound_cta_clicked`, `diagnosis_completed`, `checklist_toggled`.
- New/changed components:
  - Hero readiness card: “신청 전에 준비할 것”.
  - Extra-fee checklist module with six concrete questions.
  - “Apply now / save checklist” split CTA.
  - Optional readiness self-check moved below checklist or visually secondary.
- Variants and states:
  - Ready CTA: strong, direct, uses Appu URL.
  - Not-ready CTA: checklist/save guidance, not partner CTA pressure.
  - Disclosure state: visible near first CTA and full wording near final CTA.
- Token/component ownership:
  - Keep tokens inline in the static HTML for MVP. Do not introduce a design-system dependency.

## Accessibility

- Target standard: practical WCAG 2.1 AA alignment for contrast, keyboard, and semantics.
- Keyboard/focus behavior:
  - All CTAs and chips must be keyboard reachable.
  - Selected chips must expose `aria-pressed`.
- Contrast/readability:
  - Avoid pale text over gradients for critical disclosure or CTA-supporting copy.
- Screen-reader semantics:
  - Use clear section headings.
  - Do not rely on emoji alone to convey status.
- Reduced motion and sensory considerations:
  - No essential motion.

## Responsive behavior

- Supported breakpoints/devices:
  - Mobile first: 360px and up.
  - Desktop: hero can use two columns, but the primary CTA remains visually dominant.
- Layout adaptations:
  - On mobile, hero order should be: headline, proof/checklist promise, primary CTA, handoff explainer, optional sections.
  - Diagnostic should not push the primary CTA below the first mobile screen.
- Touch/hover differences:
  - Buttons need large tap targets.
  - Checklist rows should be easy to tap without accidental CTA clicks.

## Interaction states

- Loading:
  - Static page should show immediately; avoid blocking scripts.
- Empty:
  - Optional self-check starts with “바로 신청해도 됩니다. 불안하면 확인하세요.”
- Error:
  - If tracking fails, CTA should still navigate to Appu.
- Success:
  - Tracking success is silent; the user should not wait for analytics.
- Disabled:
  - Do not disable partner CTA unless there is a real reason. Use copy to qualify instead.
- Offline/slow network:
  - Static content remains readable; partner click depends on network.

## Content voice

- Tone:
  - Direct, plain Korean, helper-like, not hype.
- Terminology:
  - Use “다이사 가격비교”, “견적 상담”, “추가요금”, “55일 이내 이사일”. Avoid “DB”, “Adlix/Appu 경유” in main body copy.
- Microcopy rules:
  - Say exactly what happens after click.
  - Use definite disclosure wording: “제휴 링크를 통한 신청 또는 클릭에 따라 운영자는 제휴 수익을 지급받습니다.”
  - Avoid “받을 수 있음”.
  - Avoid implying users will avoid all calls or always get the lowest price.

## Implementation constraints

- Framework/styling system:
  - Static HTML with inline CSS/JS under `outputs/sites/moving-quote-call-burden/index.html`.
- Design-token constraints:
  - Use existing CSS variables. No new dependency.
- Performance constraints:
  - No third-party UI libraries.
  - Tracking must not block CTA navigation.
- Compatibility constraints:
  - Vercel static page with `/api/track` serverless function.
  - CTA must preserve `https://appu.kr/?i=12518178` and UTM variants.
- Test/screenshot expectations:
  - Verify live or local HTTP page contains the hero CTA, Appu URL, disclosure, and readiness explanation.
  - Browser-click QA should confirm `/api/track` returns 202 and Appu redirects to Adlix Daisa.

## Recommended redesign for the current landing

1. Replace the first-screen promise:
   - From: “30초 진단/불안 진단”
   - To: “이사 견적 신청 전, 당일 추가요금 6가지만 확인하세요.”
2. Keep CTA above the diagnostic:
   - Primary: “55일 이내 이사라면 다이사 가격비교 신청하기”
   - Secondary: “추가요금 체크리스트 먼저 보기”
3. Add a compact readiness card before or beside the first CTA:
   - “준비할 것: 연락처, 55일 이내 이사 날짜, 출발지, 도착지, 큰 짐 목록, 상담 가능한 시간”
   - Avoid Adlix/Appu/DB routing language in the main body; keep formal affiliate disclosure in the disclosure area.
4. Make checklist the hero value, not the quiz:
   - 사다리차 필요 여부
   - 주말/손 없는 날 비용
   - 엘리베이터/층수
   - 대형가전/침대/에어컨 분해설치
   - 출발지/도착지 상세주소
   - 상담 가능한 시간
5. Move self-check lower and label it optional:
   - Use it to segment intent and improve tracking, not as a required user task.
6. Add a natural “신청 전에 준비할 것” trust section:
   - Focus on what the user should prepare for consultation.
   - Keep platform attribution and payout mechanics out of the user-facing persuasion copy.
7. Track content angles separately:
   - `utm_content=hero_cta`
   - `utm_content=fee_checklist_cta`
   - `utm_content=ready_after_check_cta`

## Open questions

- [ ] Should the landing include Daisa brand/logo screenshots? Owner: user. Impact: could improve trust, but may require brand/affiliate rule review.
- [ ] Can Adlix provide approved copy or creative assets for Daisa? Owner: user/Adlix dashboard. Impact: safer compliance and higher trust.
- [ ] Is a real downloadable/checkable moving checklist worth adding? Owner: implementation. Impact: gives a stronger reason to visit before clicking.
- [ ] Should we add a small FAQ schema block for SEO? Owner: implementation. Impact: may help search snippets, but copy must remain people-first.

## 2026-06-17 final CTA copy note

- Final CTA copy should feel like a calm readiness checkpoint, not a sales close.
- Prefer “날짜와 주소 확인”, “견적 상담 준비” language over “가격비교로 이동하세요”.
- Keep disclosure short, definite, and visually quiet near the final CTA.
