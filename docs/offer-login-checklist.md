# Offer Login Checklist

## Goal

Confirm one usable moving quote offer before public traffic is sent.

Preferred campaign:

> `[기타] 서경석의 이사방`

Fallback:

> `다이사 이사 가격비교`

## Check These Fields

For each candidate campaign, record:

- network
- campaign name
- campaign id or sid
- payout
- approval rate
- remaining daily cap
- allowed traffic sources
- prohibited traffic sources
- whether pre-landers are allowed
- whether Naver Blog is allowed
- whether Threads/SNS is allowed
- whether community traffic is allowed
- required disclosure
- forbidden phrases
- promotion URL per channel
- tracking script or postback requirements

## Must Pass

The first public launch requires:

1. Naver Blog or organic content traffic allowed.
2. A pre-lander/checklist page allowed.
3. No ban on educational checklist copy.
4. No required local lead-form capture.
5. A unique promotion URL can be generated.
6. Required disclosure text is known.

## Reject If

Reject the offer for v1 if:

- only paid Meta/Danggeun/Google traffic is allowed,
- pre-landers are prohibited,
- the campaign requires claims like "lowest price guaranteed",
- the campaign requires collecting phone numbers on our page,
- the platform prohibits affiliate disclosure,
- traffic from blogs or SNS is not allowed.

## Result Template

```yaml
network:
campaign:
campaign_id:
status: approved | rejected | waiting
payout:
approval_rate:
allowed_traffic:
prohibited_traffic:
prelander_allowed:
required_disclosure:
forbidden_claims:
promotion_url:
notes:
```
