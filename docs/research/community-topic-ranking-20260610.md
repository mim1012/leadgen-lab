# Community Topic Ranking 2026-06-10

## Summary

Naver Blog/Cafe search results were collected for six Korean lead-generation candidate topics and scored with a first-pass heuristic.

The current strongest candidates are:

1. `wedding-fair-privacy`
2. `moving-quote`
3. `interior-estimate`

This ranking is not final. It is a source-prioritization pass for deciding which community pages to open and capture next.

## Ranking

| Rank | Topic | Score | Records | Unique URLs | High-Signal Sources | Top Pain Terms |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `wedding-fair-privacy` | 75.53 | 160 | 152 | 99 | 전화, 호구, 스팸, 개인정보, 주의 |
| 2 | `moving-quote` | 64.36 | 120 | 114 | 89 | 전화, 스트레스, 걱정, 전화폭탄, 바가지 |
| 3 | `interior-estimate` | 61.64 | 120 | 116 | 86 | 후회, 추가비용, 걱정, 전화, 실패 |
| 4 | `appliance-rental` | 49.89 | 100 | 96 | 61 | 전화, 개인정보, 후회, 귀찮, 사기 |
| 5 | `telecom-install` | 41.17 | 100 | 99 | 45 | 전화, 사기, 피해, 귀찮, 걱정 |
| 6 | `vibecoding-gtm` | 26.92 | 100 | 93 | 25 | 주의, 실패 |

Source artifact:

- `RESEARCH/community-leadgen-20260610/topic-ranking.md`

## Interpretation

### 1. Wedding Fair Privacy

The strongest repeated pain is not "wedding planning is fun." It is:

- phone calls after application,
- spam concerns,
- personal information exposure,
- fear of bad contracts or being treated like a "호구",
- need for comparison before consultation.

This supports a landing concept such as:

> 웨딩박람회 신청 전 전화폭탄 방지 체크리스트

Possible first page:

- short checklist,
- "what to ask before submitting your phone number",
- "how to compare fair offers",
- "what not to sign on-site",
- CTA to a vetted comparison or consultation page.

Risk:

- Many search results are promotional wedding posts. Capture real cafe posts and non-promotional reviews before finalizing.

### 2. Moving Quote

The strongest repeated pain is:

- too many calls after quote requests,
- stress from comparing vendors,
- uncertainty about price differences,
- concern about added costs or bad providers.

This supports a landing concept such as:

> 이사 견적 전화폭탄 줄이는 3분 준비표

Possible first page:

- moving type selector,
- inventory checklist,
- building/date constraints,
- questions to ask before quote request,
- CTA to limited-vendor quote comparison.

Risk:

- Strong demand, but partner/CPA campaign availability must be verified before choosing this as the first monetization theme.

### 3. Interior Estimate

The strongest repeated pain is:

- regret after renovation,
- added cost,
- confusing quote comparisons,
- uncertainty about what to ask vendors.

This supports a landing concept such as:

> 인테리어 상담 전 추가비용 방지 질문지

Possible first page:

- scope checklist,
- budget range selector,
- hidden-cost warning list,
- vendor consultation question generator,
- CTA to interior estimate consultation.

Risk:

- Higher ticket value but higher trust burden. Content must be more accurate than a simple viral quiz.

## Lower Priority Topics

### Appliance Rental

There is clear phone/personal-info friction, but results look heavily promotional and product-specific.

Use later for:

- comparison templates,
- affiliate content,
- search-intent experiments.

### Telecom Install

There is pain around scams and incentives, but the market is crowded and offer trust is hard.

Use later after the research system can filter promotional posts better.

### Vibe-Coding GTM

This is strategically relevant to Leadgen Lab itself, but it is weaker as a CPA/pre-lander category. It may be better as:

- Leadgen Lab's buyer persona,
- content marketing theme,
- future product positioning.

## Recommended Next Captures

Open and capture the top 5 to 10 sources from:

- `RESEARCH/community-leadgen-20260610/topics/wedding-fair-privacy/high-signal-sources.md`
- `RESEARCH/community-leadgen-20260610/topics/moving-quote/high-signal-sources.md`
- `RESEARCH/community-leadgen-20260610/topics/interior-estimate/high-signal-sources.md`

Use:

```powershell
python src\cdp_capture_current_page.py --source korean-community --slug wedding-fair-privacy --url-regex "naver|threads|dcinside|clien|ppomppu|teamblind|tistory|blog"
```

Change `--slug` per topic.

## Recommendation

Do not build a generic tarot or relationship quiz first.

The best first launch direction is:

> A decision-support pre-lander that protects users before they submit personal information.

First candidate after the first primary capture:

> 이사 견적 전화폭탄 줄이는 3분 준비표

Reason:

- The captured moving-quote source explicitly connects the pain, CTA, and affiliate monetization model.
- The user pain is concrete: quote comparison is useful, but many unknown calls are stressful.
- The landing promise can be specific: prepare once, compare fewer vetted vendors, reduce call burden.

Second candidate:

> 웨딩박람회 신청 전 전화폭탄 방지 체크리스트

Reason:

- Search and pain-term volume are currently strongest.
- The captured wedding source shows a monetization pattern, but it is promotional.
- This needs more non-promotional cafe/community evidence before choosing it as the first launch.

The next decision should happen after capturing more primary evidence from the top sources, because the current ranking may still over-weight SEO/promotional posts.

See also:

- `docs/research/captured-evidence-20260610.md`
