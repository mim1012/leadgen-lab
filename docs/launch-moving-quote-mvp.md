# Moving Quote MVP Launch Plan

## Product

Name:

> 이사 견적 전화폭탄 줄이는 3분 준비표

Format:

- one-page decision-support pre-lander,
- static page,
- outbound CTA only,
- no local personal-data collection in v1.

Primary user:

> 이사를 앞두고 견적 비교는 해야 하지만, 여러 업체에서 전화가 쏟아질까 봐 신청을 망설이는 사람.

## Core Promise

Do not promise:

> 전화가 절대 오지 않습니다.

Promise:

> 견적 신청 전에 필요한 정보를 정리하고, 상담 범위와 비교 기준을 미리 정해서 불필요한 통화와 추가비용 리스크를 줄입니다.

## Page Structure

### 1. Hero

Headline:

> 이사 견적 신청 전, 전화폭탄 줄이는 3분 준비표

Subcopy:

> 이사 날짜, 짐 규모, 건물 조건, 추가비용 질문을 먼저 정리하면 상담이 짧아지고 비교가 쉬워집니다.

CTA:

> 3분 준비표 시작하기

### 2. Quick Selector

Inputs:

- 이사 유형: 원룸 / 투룸 / 아파트 / 사무실 / 보관이사
- 이사 예정일: 2주 이내 / 1개월 이내 / 아직 미정
- 견적 방식 선호: 전화 / 사진 / 방문
- 가장 걱정되는 것: 전화 많음 / 추가요금 / 업체 신뢰 / 일정 부족

Output:

- recommended checklist variant,
- CTA copy variant,
- tracking event only.

### 3. Checklist

Sections:

- 기본 정보: 출발지, 도착지, 이사 날짜, 엘리베이터, 사다리차 가능 여부
- 짐 정보: 큰 가구, 가전, 분해/설치 필요 품목
- 비용 질문: 추가요금, 식사비/수고비, 주말/손 없는 날 차이
- 업체 확인: 후기, 보험, 허가 여부, 계약서/견적서 확인
- 상담 통제: 몇 곳까지 상담할지, 연락 가능 시간, 사진 견적 가능 여부

### 4. Risk Warnings

Warnings:

- 너무 낮은 첫 견적만 보고 결정하지 않기
- 방문 견적이 필요한 상황인지 확인하기
- 추가비용 항목을 견적서에 남기기
- 개인정보 제공 범위와 마케팅 수신 동의 확인하기

### 5. CTA Block

Primary CTA:

> 준비표 확인하고 제한 비교 견적 보기

Secondary CTA:

> 아직 신청 전이면 체크리스트만 저장하기

CTA behavior:

- outbound affiliate or partner link,
- UTM parameters,
- outbound click event,
- no local lead form in v1.
- for Adlix Daisa, show that quote requests require a moving date within 55 days.

### 6. Disclosure

Required copy:

> [광고] 이 페이지는 이사 견적 비교 전 확인할 정보를 정리한 안내 페이지이며, 제휴 링크를 통한 신청 또는 클릭에 따라 운영자는 제휴 수익을 지급받습니다.

## Minimum Tracking

Events:

- `page_view`
- `selector_completed`
- `checklist_viewed`
- `outbound_cta_clicked`

UTM fields:

- `utm_source`
- `utm_medium`
- `utm_campaign=moving_quote_call_burden`
- `utm_content`

Success criteria for first test:

- outbound CTA click rate above 8 percent from warm traffic,
- checklist completion above 30 percent,
- at least 20 outbound clicks before judging the angle,
- comments or replies mentioning phone burden, added cost, or quote confusion.

## First Traffic Plan

Threads:

- short build-in-public posts,
- moving checklist snippets,
- "what to ask before quote request" posts,
- no spam replies or automated DMs.

Naver Blog:

- one SEO article: `이사 견적 전화폭탄 줄이는 체크리스트`
- one article: `포장이사 견적 신청 전 추가요금 질문 10가지`
- one article: `사진 견적 vs 방문 견적, 언제 뭐가 맞을까`

Naver Cafe / Communities:

- only where rules allow sharing resources,
- post as checklist/helpful guide,
- no hard-selling affiliate link in communities that prohibit it,
- use neutral checklist page first, then CTA on the page.

## Build Order

1. Confirm usable offer and traffic rules.
2. Create campaign record.
3. Build static page.
4. Add outbound tracking.
5. Publish one Naver Blog article and three Threads posts.
6. Capture page screenshot and source evidence.
7. Review clicks and qualitative replies after first 20 outbound clicks.

## Open Risks

- Affiliate campaign details may change after login.
- Some networks may disallow certain traffic sources or pre-landers.
- Moving quote platforms may prefer direct lead capture, but v1 should avoid storing personal information.
- Search snippets and affiliate posts can overstate demand; continue capturing non-promotional community evidence.
