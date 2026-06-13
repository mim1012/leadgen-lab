# Landing Persona Feedback 2026-06-10

## Reviewed Page

- Page: `outputs/sites/moving-quote-call-burden/index.html`
- Production: `https://moving-quote-call-burden.vercel.app`
- Campaign: Adlix `다이사 이사 가격비교`
- Revenue event: approved partner-side moving quote consultation DB

This is a multi-persona review of the current landing page. It is not an external model output. Claude CLI timed out in non-interactive mode, and Gemini/Antigravity CLI are not installed in the current environment.

## Executive View

The page is directionally right: it avoids local personal data collection, has clear ad disclosure, and frames the offer as a preparation/checklist tool instead of a hard-sell lead form.

The biggest weakness is that the page still behaves like a helpful checklist more than a conversion bridge. The user can learn from it and leave without feeling that the next step is natural, urgent, and appropriate. The next iteration should make the page behave like:

> "If your move is within 55 days and you are willing to receive quote consultation, use this checklist and then request comparison quotes."

## Persona 1: Anxious Mover

Primary thought:

> "전화가 많이 올까 봐 무서운데, 이 페이지는 그 걱정을 알아준다."

What works:

- `전화폭탄` pain is immediately recognizable.
- The page admits that calls can still happen, so it does not feel deceptive.
- Checklist and risk-signal sections reduce anxiety.

What blocks conversion:

- The user may think the page is only an informational checklist.
- `견적 상담 연락을 받을 수 있는 경우` is honest, but it can make anxious users stop unless paired with a control mechanism.
- There is no concrete "how to keep calls manageable" step before the CTA.

Recommended fix:

- Add a small "상담 통제 규칙" block before final CTA:
  - 연락 가능한 시간 정하기
  - 상담받을 업체 수 정하기
  - 추가요금 질문 3개 준비하기

## Persona 2: Ready-To-Move User

Primary thought:

> "나는 곧 이사해야 하는데, 빨리 견적 비교로 가고 싶다."

What works:

- The new hero CTA `내 조건 정리하고 비교 견적 확인하기` is closer to action.
- The 55-day eligibility rule correctly tells this user whether they fit.

What blocks conversion:

- The CTA path still makes ready users scroll through too much educational content.
- The selector is useful, but not required enough to feel like a quote-prep step.
- The final CTA is the strongest monetization path, but it appears late.

Recommended fix:

- Add a second above-the-fold CTA after eligibility:
  - Primary: `내 조건 정리하고 비교 견적 확인하기`
  - Secondary: `이미 준비됨: 바로 견적 비교하기`

Risk:

- This may increase low-quality outbound clicks. Pair it with the 55-day and consultation-call condition.

## Persona 3: Conversion Copywriter

Primary thought:

> "The promise is good, but the page needs a sharper before/after."

What works:

- Clear pain: phone overload.
- Clear mechanism: prepare conditions before applying.
- Safer than generic "lowest price" copy.

What blocks conversion:

- The benefit is abstract: "상담이 짧아지고 비교가 쉬워집니다."
- The CTA does not show what happens after click.
- `제한 비교 견적` language is less natural than `비교 견적 신청`.

Recommended copy direction:

- Hero subcopy:
  - Current: `상담이 짧아지고 비교가 쉬워집니다.`
  - Test: `업체마다 같은 조건을 전달할 수 있게 정리한 뒤, 비교 견적 신청으로 이동합니다.`
- CTA:
  - `준비한 조건으로 비교 견적 신청하기`
- CTA helper:
  - `다이사 제휴 페이지로 이동하며, 신청 후 견적 상담 연락이 올 수 있습니다.`

## Persona 4: CPA Affiliate Manager

Primary thought:

> "Outbound CTR보다 승인 가능한 DB 비율이 더 중요하다."

What works:

- Local form capture is avoided, reducing privacy and consent risk.
- `[광고]` disclosure is visible.
- 55-day rule is now above the fold and near CTA.

What blocks revenue:

- Users who hate all phone contact may still click because the pain angle attracts them.
- Users with no date or date outside 55 days may click unless eligibility is enforced in the selector.
- Duplicate users or casual browsers may reduce approval quality.

Recommended fix:

- Add selector question:
  - `이사 예정일이 55일 이내인가요?`
  - Options: `예`, `아직 미정`, `55일 이후`
- If `아직 미정` or `55일 이후`, show checklist-only recommendation first and soften outbound CTA.
- If `예`, show strong CTA.

## Persona 5: Compliance Reviewer

Primary thought:

> "The page is safer than most CPA pre-landers, but the pain angle must not imply no calls."

What works:

- Top disclosure exists.
- Final disclosure exists.
- The page says calls can still happen.
- It does not claim lowest price.
- It does not collect local personal data.

Potential risks:

- `전화폭탄 줄이는` can be interpreted as a strong promise.
- Community posts must not look like neutral personal recommendations if monetized.
- If future automation posts to cafes/communities, platform and affiliate rules may be violated.

Recommended fix:

- Keep phrasing as "줄이는 준비표" rather than "막는 방법".
- Use `[광고]` in title or first line for every external content post.
- Do not automate comments, DMs, likes, cafe posts, or repeated link drops.

## Persona 6: Korean Community Marketer

Primary thought:

> "카페/커뮤니티에서는 링크보다 내용 자체가 먼저 살아야 한다."

What works:

- Checklist content is useful enough to stand alone.
- The topic has real pain: phone burden, additional fees, unreliable quotes.

What blocks traffic:

- A direct link-first post will look like affiliate spam.
- `다이사` or 제휴 링크를 너무 빨리 꺼내면 방어 반응이 생길 수 있다.
- Same copy copied across communities will be flagged or ignored.

Recommended posting pattern:

1. First 80 percent: useful checklist inside the post.
2. Then disclosure.
3. Then optional link:
   - `제가 정리한 3분 준비표 페이지도 같이 남깁니다. 제휴 링크가 포함되어 있어 신청/클릭 시 수익이 발생합니다.`

Best first channels:

- Naver Blog first.
- Threads second.
- Communities third, only if rules allow external links and affiliate disclosure.

## Persona 7: SEO / Naver Blog Editor

Primary thought:

> "The landing is not enough. Naver Blog articles should be the searchable front door."

What works:

- The page has a focused title.
- The topic maps to long-tail search intent.

What blocks organic traffic:

- Static Vercel page alone is unlikely to rank quickly in Naver.
- Blog posts need separate intent angles, not just landing copy repeated.

Recommended first 3 article titles:

1. `[광고] 이사 견적 전화폭탄 줄이는 체크리스트: 신청 전 정리할 7가지`
2. `[광고] 포장이사 견적 신청 전 꼭 물어볼 추가요금 질문 10가지`
3. `[광고] 사진 견적 vs 방문 견적, 이사할 때 어떤 방식이 맞을까?`

CTA placement:

- Do not put the CTA only at the top.
- Put one CTA after the checklist and one at the bottom.

## Persona 8: UX Designer

Primary thought:

> "The flow is understandable, but the page needs stronger progress and decision states."

What works:

- Layout is simple.
- The selector gives interaction.
- Cards are readable.

What blocks conversion:

- The page does not show progress such as "1. 조건 선택 -> 2. 체크 -> 3. 견적 비교".
- The selector result does not visually feel like a next step.
- The final CTA band is strong but visually disconnected from the selector.

Recommended fix:

- Add a three-step progress row:
  - `조건 선택`
  - `질문 정리`
  - `비교 견적 확인`
- Make selector result a stronger decision panel after 3 selections.

## Persona 9: Data Analyst

Primary thought:

> "현재 localStorage 이벤트만으로는 유입별 수익 판단이 어렵다."

What works:

- Events exist:
  - `page_view`
  - `selector_choice`
  - `selector_completed`
  - `outbound_cta_clicked`
  - `selector_cta_clicked`

What blocks learning:

- Events stay in the browser unless captured elsewhere.
- There is no server-side click log.
- There is no source-level review loop unless UTM is preserved and inspected.

Recommended fix:

- Add a lightweight outbound click endpoint or analytics sink before scaling.
- Track:
  - source
  - medium
  - content
  - CTA position
  - selector state at outbound click

Minimum decision rule:

- Do not judge before 20 outbound clicks.
- Do not scale before at least one source shows partner-side conversion signal.

## Persona 10: Founder / Operator

Primary thought:

> "This can make money, but only if treated as a measured distribution experiment, not a one-page asset."

What works:

- A real offer is connected.
- The page is already publishable.
- The first traffic channels are clear.

What blocks business value:

- No repeatable distribution loop yet.
- No direct feedback from Adlix approval/rejection data yet.
- No automation should be built until manual source quality is known.

Operating recommendation:

1. Ship the improved landing.
2. Publish 1 Naver Blog article.
3. Publish 3 Threads posts.
4. Get 20 outbound clicks.
5. Check Adlix conversion and approval signals.
6. Only then automate content drafting and reporting.

## Prioritized Feedback

Must change before meaningful traffic:

1. Add `55일 이내인가요?` as a selector question.
2. Add stronger selector-complete decision panel.
3. Remove any copy that still sounds like a placeholder.
4. Make CTA helper text explicit about partner page and consultation calls.

High-value next iteration:

1. Add three-step progress row.
2. Add "상담 통제 규칙" block.
3. Add source/CTA-position click logging.
4. Create Naver Blog article from the first content pack.

Do later:

1. A/B test headline and CTA variants.
2. Build content automation.
3. Add multi-offer routing across Daisa, Adpot, DBSense, or direct partners.
4. Add approval-quality dashboard after enough DB data exists.

## Final Recommendation

The current landing should not be judged by whether people like the checklist. It should be judged by whether the checklist creates enough confidence for eligible users to submit a valid quote request on the partner page.

The next best product move is not more design. It is better qualification:

> 55-day eligibility + willingness to receive consultation + prepared move details.

