# Moving Offer Verification 2026-06-10

## Result

The moving-quote monetization path is viable enough to proceed to MVP planning.

Publicly visible evidence confirms that Korean affiliate/CPA networks expose moving-related campaigns, including:

- `서경석의 이사방`
- `서경석의 이사방-원룸/용달 전용`
- `24번가, 합리적인 이사`
- `다이사 이사 가격비교`

However, final launch still requires login-level confirmation of campaign rules, traffic-source restrictions, and approved promotional URLs.

Latest check:

- Public pages confirm campaign existence, payout, approval-rate style metrics, and channel separation.
- Campaign detail pages for both Adpot and Adlix require login before rule details can be read.
- Chrome CDP was opened on port `9222` and screenshots/text captures were saved under `evidence/affiliate-offer/`.

## Publicly Verified Signals

### 1. Adpot - 서경석의 이사방

Source:

- `https://adpot.kr/pc/center/notice_view.html?code=4693`

Observed:

- Adpot published a 2025-08-29 notice for `서경석의 이사방` CPA campaign channel separation.
- Campaigns are split into:
  - `[메타 전용] 서경석의 이사방`
  - `[당근 전용] 서경석의 이사방`
  - `[구글애즈 전용] 서경석의 이사방`
  - `[기타] 서경석의 이사방`
- The notice says each ad channel requires a new promotional URL.

Implication:

- This confirms the exact campaign exists and has channel-specific routing.
- It also means Leadgen Lab must not publish one generic affiliate URL across all sources.
- The MVP needs a campaign rule field for `traffic_channel` and `promotion_url`.
- Direct visit to `[기타] 서경석의 이사방` detail URL redirects to Adpot login, so detailed media rules are not publicly readable.

### 2. DBSense - 이사 CPA campaign list

Source:

- `https://dbsense.kr/pc/camp/camp_cpa.html`

Observed public list:

- `[구글애즈 전용] 서경석의 이사방` CPA 20,000원, average 72%, today remaining count visible
- `[메타 전용] 서경석의 이사방` CPA 20,000원, average 72%
- `[당근 전용] 서경석의 이사방` CPA 20,000원, average 72%
- `[기타] 서경석의 이사방` CPA 20,000원, average 72%
- `24번가, 합리적인 이사` CPA 19,000원, average 40%
- `서경석의 이사방-원룸/용달 전용` CPA 8,500원, average 36%

Implication:

- Moving quote/consultation has active-looking CPA economics in public listings.
- General moving and one-room/small moving may need separate landing variants.
- The first MVP can target the broader moving quote page first, then split small-move traffic later.

### 3. Adlix - 다이사 이사 가격비교

Sources:

- `https://www.adlix.co.kr/cpa/applist.asp`
- `https://www.adlix.co.kr/app/applist.asp?c_sort_num=1&icon_num=0`

Observed search result snippets:

- `다이사 이사 가격비교` CPA listing with approval rate around 78-79%.
- DB payout shown around `20,000 p`.
- App/CPC listing shows `다이사 이사 가격비교` click payout around `360 p`.

Observed by browser on 2026-06-10:

- Adlix CPA list page shows `다이사 이사 가격비교`, approval rate `78%`, DB payout `20,000 p`, and promotion `+4,000p`.
- Clicking the campaign opens `https://adlix.co.kr/cpa/appview.asp?idx=6936747`, but an alert requires login before detail access.

Implication:

- Daisa can be a strong alternate offer if Adpot/DBSense approval is blocked.
- CPC version may allow earlier click validation, while CPA version is better for revenue per conversion.
- Like Adpot, Adlix needs login-level rule confirmation before public traffic is sent.

### 4. Tenping business model

Source:

- `https://biz.tenping.net/`

Observed:

- Tenping publicly describes CPA, CPE, CPC, CPS products.
- CPA/TP supports content spread and contact submission tracking.
- Submitted contact leads are later contacted and validated as valid/invalid.
- CPC products charge on click or click plus dwell time.

Implication:

- Tenping validates the broader monetization mechanism.
- Specific moving campaign availability must still be checked in the logged-in marketer dashboard.

## Launch Decision

Proceed with the MVP, but do not publish traffic until one campaign is confirmed at login level.

Preferred first campaign:

> `[기타] 서경석의 이사방`

Reason:

- It appears designed for non-Meta, non-Danggeun, non-Google traffic.
- The planned first channels are Naver Blog, Threads, and community-safe checklist traffic.

Fallback:

> `다이사 이사 가격비교`

Reason:

- Public snippets show both CPA and CPC style options.
- Daisa's offer maps naturally to comparison/checklist copy.

## Required Login-Level Checks

Before publishing affiliate links, confirm:

1. Whether Naver Blog traffic is allowed.
2. Whether Threads/SNS traffic is allowed.
3. Whether community/cafe traffic is allowed.
4. Whether a pre-lander is allowed.
5. Whether the ad copy may mention call burden, limited vendors, phone calls, or added-cost prevention.
6. Whether disclosure text is required.
7. Whether separate URLs are needed per channel.
8. Whether `outbound_cta_clicked` tracking can be used before affiliate handoff.

## Product Changes Required

Add these fields to each campaign:

- `network`
- `campaign_sid`
- `traffic_channel`
- `promotion_url`
- `payout`
- `approval_rate`
- `daily_remaining`
- `forbidden_claims`
- `required_disclosure`
- `prelander_allowed`

The current campaign record should remain `researching` until one offer passes these checks.

## Current Verification Status

| Network | Campaign | Publicly Confirmed | Detail Rules |
| --- | --- | --- | --- |
| Adpot | `[기타] 서경석의 이사방` | Channel split and detail URL confirmed | Login required |
| DBSense | `[기타] 서경석의 이사방` | CPA 20,000원, average 72%, daily remaining shown | Login likely required |
| DBSense | `24번가, 합리적인 이사` | CPA 19,000원, average 40%, daily remaining shown | Login likely required |
| DBSense | `서경석의 이사방-원룸/용달 전용` | CPA 8,500원, average 36%, daily remaining shown | Login likely required |
| Adlix | `다이사 이사 가격비교` | CPA 20,000p, approval 78%, promotion +4,000p shown | Login required |
| Adlix | `다이사 이사 가격비교` CPC | Click payout 360p shown in public listing/search result | Login required |

Updated after signup:

- Adlix `다이사 이사 가격비교` detail is now readable after login.
- Campaign detail confirms consultation-request CPA, `20,000p`, approval `78%`, promotion `+4,000p`, rejection conditions, required fields, and paid relationship disclosure guidance.
- See `docs/research/adlix-daisa-campaign-detail-20260610.md`.

## CDP Evidence Captures

Captured through Chrome CDP on 2026-06-10:

- `evidence/affiliate-offer/adpot-login-20260610-205132`
- `evidence/affiliate-offer/adlix-cpa-list-20260610-205132`
- `evidence/affiliate-offer/dbsense-cpa-list-20260610-205132`

Observed from captures:

- Adpot target is currently at `애드팟 로그인`; login is required before campaign detail can be read.
- Adlix CPA list is publicly readable and contains the campaign list page.
- DBSense redirects unauthenticated access to the membership/signup flow in the CDP browser session.
