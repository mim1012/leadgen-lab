# Adlix Daisa Campaign Detail 2026-06-10

## Campaign

Network:

- Adlix

Campaign:

- `다이사 이사 가격비교`

Captured evidence:

- `evidence/affiliate-offer/adlix-daisa-detail-after-signup-20260610-205601`

Campaign URL:

- `https://adlix.co.kr/cpa/appview.asp?idx=6936747`

## Confirmed Terms

Confirmed from logged-in campaign detail:

- Campaign type: CPA
- Action: consultation request DB
- Payout: `20,000p` per consultation request DB
- Approval rate shown: `78%`
- Promotion: `+4,000p`
- Promotion period: `2024-07-17 ~ 종료 시까지`

## Offer Positioning

The campaign describes Daisa as:

- moving-company comparison platform,
- compare up to 3 moving companies at once,
- free visit estimate,
- nationwide moving-company pool,
- review-based comparison.

This supports the current landing angle:

> 견적 신청 전에 정보를 정리하고, 비교 업체 수와 상담 포인트를 통제한다.

## Rejection Conditions

Visible rejection conditions:

- 오류
- 결번
- 중복
- 미성년자
- 장기부재
- 상담거절
- 본인아님

Implication:

- Traffic should avoid curiosity-only users.
- Copy must pre-qualify users who actually plan to move.
- The landing should keep the `55일 이내 이사날짜` rule visible near CTA.

## Required Lead Fields

The campaign form requests:

- 이름
- 핸드폰번호
- 이사 날짜
- 출발지
- 출발지 상세주소
- 도착지
- 도착지 상세주소

Rule:

- `이사 날짜` must be within 55 days for quote request eligibility.

## Disclosure Requirement

The campaign requires paid relationship disclosure in promotional posts.

Adlix examples include:

- `이 포스팅은 애드릭스 수익이 발생합니다.`
- `이 포스팅은 애드릭스 수익을 위해 작성되었습니다.`
- `이 포스팅은 애드릭스 커미션을 얻습니다.`
- `이 포스팅은 애드릭스 포인트를 받습니다.`
- `이 포스팅은 애드릭스 이벤트 참여를 위해 작성되었습니다.`

The detail page also notes the 2024-12-01 disclosure guidance change:

- put disclosure at the beginning of the post content or expose it in the title with `[광고]`,
- avoid weak phrasing such as `받을 수 있음`,
- use definite wording such as `지급받음` or `받았음`.

## Implementation Decision

Use this as the first executable offer.

Status:

- offer detail verified,
- channel registered with `https://moving-quote-call-burden.vercel.app`,
- phone verification completed by the account owner,
- promotion URL generated: `https://appu.kr/?i=12518178`,
- landing CTA can now be wired to the campaign.

Landing requirement:

- Add `[광고]` or equivalent disclosure before traffic content.
- Keep local v1 outbound-only unless embedding the Adlix form is intentionally chosen later.
