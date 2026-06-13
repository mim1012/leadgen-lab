# Launch Execution Log 2026-06-10

## Current State

The first MVP is deployed and wired to a generated Adlix promotion URL.

Campaign:

- `moving-quote-call-burden`

Landing:

- `outputs/sites/moving-quote-call-burden/index.html`
- `https://moving-quote-call-burden.vercel.app`

Content pack:

- `docs/content/moving-quote-content-pack.md`

Offer checklist:

- `docs/offer-login-checklist.md`

## Completed

1. Public offer evidence reviewed.
2. First campaign record created.
3. Static one-page pre-lander built.
4. Selector, checklist, CTA, disclosure, and UTM placeholder added.
5. Local event tracking added through `localStorage`.
6. Initial Naver Blog, Threads, and cafe-safe content pack drafted.
7. Browser verification completed through local server.
8. Adlix `다이사 이사 가격비교` campaign detail captured after signup.
9. Disclosure copy updated to avoid weak `받을 수 있음` wording.
10. Landing now shows `[광고]` disclosure at the top of the first screen.
11. Landing deployed to Vercel production.
12. Adlix channel registered as `기타` with the Vercel landing URL.
13. Adlix phone verification completed by the account owner.
14. Adlix promotion URL generated: `https://appu.kr/?i=12518178`.
15. Landing CTA updated to use the generated promotion URL.
16. Vercel production redeployed and verified to contain the generated promotion URL.
17. Growth/conversion review documented in `docs/growth-conversion-review-20260610.md`.
18. Landing conversion copy updated with above-the-fold 55-day eligibility, clearer CTA wording, selector-complete CTA, and partner-call expectation copy.
19. Multi-persona landing feedback documented in `docs/landing-persona-feedback-20260610.md`.
20. Landing selector updated so strong selector CTA appears only for `55일 이내` moving-date users.
21. Vercel production redeployed after selector qualification update.
22. Manual publish pack created at `docs/content/moving-quote-publish-pack-20260610.md`.
23. Landing redesigned with a stronger conversion-first visual system, phone-control hero, 3-step journey, and refreshed mobile layout.
24. Redesigned landing deployed to Vercel production.
25. Marketing automation CLI added at `src/marketing_automation.py`.
26. First 7-day draft queue generated at `outputs/marketing/moving-quote-call-burden/2026-06-10`.
27. Marketing automation runbook added at `docs/marketing-automation-runbook.md`.
28. Landing repositioned from a checklist page to a `30초 신청 가능 진단` decision tool.
29. Marketing automation copy regenerated so content links promise diagnosis, not another checklist.
30. Diagnosis landing deployed to Vercel production.
31. Diagnosis hero strengthened with `신청하면 전화 옵니다.` headline, larger CTA, and first-screen three-question impact card.
32. Mobile section heading layout fixed after visual verification.
33. Visual hierarchy pass applied: shortened hero copy, added red/yellow emphasis, simplified first-screen card, and reduced mobile headline size.

## Verification

Local server:

- `http://127.0.0.1:4176`

Verified:

- Page loads with title `이사 견적 전화폭탄 줄이는 3분 준비표`.
- Hero CTA and checklist CTA render.
- Selector buttons update the recommendation copy.
- `selector_completed` is recorded after enough selector choices.
- `outbound_cta_clicked` is recorded before partner handoff.
- Desktop and mobile viewport checks were opened through Playwright.

Known test note:

- The CTA now points to `https://appu.kr/?i=12518178`.
- The landing no longer contains the stale `홍보 URL 생성 후 연결` placeholder copy.
- The landing now shows the `55일 이내` eligibility rule above the fold and near the final CTA.
- Latest production deployment:
  - `dpl_ELvLkuHyrb7WBPspdt7JRfBvdaTL`
  - `https://moving-quote-call-burden-qhdcs9nzx-dksk0359-7464s-projects.vercel.app`
  - Aliased to `https://moving-quote-call-burden.vercel.app`
- Production HTML verification found:
  - `55일 이내`
  - `준비한 조건으로 비교 견적 확인하기`
  - `selector_cta`
- Browser snapshot saved through Playwright:
  - `.playwright-mcp/moving-quote-prod-snapshot-20260610.md`
- Latest redesign production deployment:
  - `dpl_H2Bq8QSnY1q2n39tXq3jnQyivgwq`
  - `https://moving-quote-call-burden-520q1xv4g-dksk0359-7464s-projects.vercel.app`
  - Aliased to `https://moving-quote-call-burden.vercel.app`
- Redesign verification:
  - Production HTML contains `이사 통화 줄임표`, `CALL CONTROL PREP`, `견적 신청 전에`, and `55일 이내`.
  - Desktop screenshot: `moving-quote-redesign-final-desktop-20260610.png`
  - Mobile screenshot: `moving-quote-redesign-final-mobile-20260610.png`
- Marketing automation verification:
  - `python -m py_compile src\marketing_automation.py`
  - `python src\marketing_automation.py --campaign data\campaigns\moving-quote-call-burden.yaml --start-date 2026-06-10`
  - Generated `content_calendar.md`, `publish_queue.csv`, `utm_links.csv`, `metrics_template.csv`, and `README.md`.
- Diagnosis landing verification:
  - Production deployment: `dpl_EeU85xWTVS2rPo4jKCdn2ncLPULk`
  - Aliased to `https://moving-quote-call-burden.vercel.app`
  - Browser title: `이사 견적 신청 가능 여부 30초 진단`
  - Desktop screenshot: `moving-quote-diagnosis-desktop-20260610.png`
  - Mobile screenshot: `moving-quote-diagnosis-mobile-20260610.png`
- Latest impact-focused production deployment:
  - Production deployment: `dpl_2XFgXCaCCSV3HoDruFdRVgpEXKbD`
  - Aliased to `https://moving-quote-call-burden.vercel.app`
  - Mobile screenshot: `moving-quote-impact-final-mobile-20260610.png`
- Latest visual hierarchy deployment:
  - Production deployment: `dpl_EGbtbj3Q222k8459LxD6eV8R7tbT`
  - Aliased to `https://moving-quote-call-burden.vercel.app`
  - Mobile screenshot: `moving-quote-visual-final-mobile-2-20260610.png`

## Revenue Status

Traffic can now be sent to the Vercel landing.

Selected executable candidate:

- `다이사 이사 가격비교`

Already confirmed:

- CPA consultation DB payout `20,000p`
- approval rate shown `78%`
- promotion `+4,000p`
- required disclosure at the beginning of content or title `[광고]`
- rejection conditions captured
- eligible moving date within `55일`

Revenue is expected only when users click through and complete valid Daisa consultation request DBs that are not rejected.

Current Adlix balance:

- `11,000p`

Source:

- `애드릭스 회원가입 이벤트`: `10,000p`
- `첫 게시물(가입인사) 이벤트`: `1,000p`

Withdrawal status:

- Not withdrawable yet under the visible validation rule.
- First withdrawal requires at least `50,000p`.
- Bank, account holder, identity, and account verification must also be completed before withdrawal.

## Next Agent Step

1. Capture final landing screenshot.
2. Manually publish the first Naver Blog article from `docs/content/moving-quote-publish-pack-20260610.md`.
3. Manually publish the three Threads posts from `docs/content/moving-quote-publish-pack-20260610.md`.
4. Start first metric review after 20 outbound clicks.
5. Use `outputs/marketing/moving-quote-call-burden/2026-06-10/metrics_template.csv` as the first tracking ledger.
