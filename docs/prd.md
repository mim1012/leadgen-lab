# Leadgen Lab PRD

## Source Capture

- Source URL: `https://cafe.naver.com/vibemoney/3`
- Captured at: `20260610-172217`
- Capture directory: `.omc/naver-cafe/capture/vibemoney-3-20260610-172217`
- Main frame: `cafe_main`
- Article theme: CPA/lead generation funnel using a lightweight landing site, viral content, and traffic channels such as Threads, SEO, and low-cost ads.

## Working Thesis

Small operators can launch many narrow landing pages faster than they can manually research, write, design, deploy, and measure them. The opportunity is not "scrape personal data"; it is a consent-first funnel builder that turns affiliate/CPA campaign requirements into compliant landing pages, viral content prompts, keyword sets, and measurement loops.

## Product Concept

Leadgen Lab is a local-first campaign workbench for building and testing niche lead-generation funnels.

It helps the operator:

- choose a CPA/affiliate campaign and record its restrictions,
- generate a persona and content angle,
- create a landing page brief and copy,
- generate Threads/SEO/ad keyword content plans,
- deploy static landing pages,
- track visits, clicks, form starts, and outbound lead handoff events,
- keep compliance notes and evidence per campaign.

## Non-Goals

- No credential stuffing, bot posting, spam comments, or mass DM automation.
- No scraping or storing third-party personal data without user consent.
- No bypassing captcha, login walls, or platform restrictions.
- No automatic submission of false or misleading leads.
- No copying private cafe content into public outputs verbatim.

## MVP Scope

### 1. Campaign Registry

Fields:

- campaign name
- network/source
- category
- payout range
- approval conditions
- prohibited traffic sources
- required disclaimers
- target persona
- destination URL
- status: `researching`, `ready`, `launched`, `paused`, `rejected`

### 2. Landing Brief Generator

Inputs:

- campaign category
- persona
- user pain point
- desired action
- prohibited claims

Outputs:

- landing page headline options
- section outline
- FAQ
- CTA copy
- form fields recommendation
- disclaimer checklist

### 3. Viral Content Planner

Channels:

- Threads
- Naver Blog/Cafe research notes
- SEO article topics
- optional search-ad keyword sets

Outputs:

- hook ideas
- content series plan
- safe CTA patterns
- keyword clusters
- experiment backlog

### 4. Static Landing Page Builder

Initial stack:

- Next.js or simple static HTML generator
- deploy target: Netlify/Vercel
- optional database: Neon/Supabase only if form capture is required

MVP can start with static page plus outbound CTA tracking. Direct lead form capture should wait until privacy/consent copy is finalized.

### 5. Tracking and Evidence

Track:

- page URL
- source channel
- UTM
- outbound CTA clicks
- form events if enabled
- screenshot evidence
- campaign rule notes

Store locally first:

- SQLite database
- JSON exports
- screenshots under `.omc/leadgen-lab/evidence`

### 6. Launch Marketing Plan

See `docs/marketing.md` for the first launch offer, channel strategy, manual-before-automated marketing workflow, and future marketing automation modules.

The first launch should validate a service-assisted starter kit before the full platform is productized. This does not reduce the long-term product scope; it shortens the path to evidence about which campaign categories, content formats, and buyer segments actually convert.

## Workflow

1. Research campaign and restrictions.
2. Enter campaign into registry.
3. Generate persona, landing brief, and content plan.
4. Produce landing page.
5. Human reviews claims, disclaimers, and campaign restrictions.
6. Deploy.
7. Publish traffic content manually or through approved channel APIs only.
8. Collect analytics.
9. Iterate copy/angle/keyword clusters.

## Automation Architecture

### Browser Capture Layer

Use CDP Chrome for research capture:

- operator logs in manually,
- agent attaches to CDP port,
- read-only DOM/text/link/screenshot capture,
- no save/comment/like/join/post actions.

This should be shared with `kmong`, `wishcat`, `soomgo`, and Naver Cafe research flows.

### Core Modules

- `capture`: CDP page capture and extraction
- `campaigns`: campaign registry and restrictions
- `briefs`: persona, landing, and content brief generation
- `builder`: static landing page generation
- `tracking`: UTM and event tracking plan
- `evidence`: screenshots and source notes

### Safety Gates

- `draft`: generated but not approved
- `reviewed`: human checked copy and restrictions
- `deployable`: approved for deployment
- `launched`: live
- `paused`: stopped due to policy, performance, or quality concerns

## Initial Project Ideas From Capture

### A. Moving Quote Call-Burden Funnel

Rationale:

- latest community research shows repeated pain around quote-request calls, stress, added costs, and vendor comparison,
- captured source explicitly connects moving-quote pain, CTA, and affiliate/CPA monetization,
- the page can launch as outbound-only, avoiding local personal-data capture in v1.

Possible content:

- moving quote call-burden checklist
- inventory preparation sheet
- added-cost question list
- visit-estimate vs photo-estimate explainer
- limited-vendor comparison CTA

Recommended first launch:

- `이사 견적 전화폭탄 줄이는 3분 준비표`

See:

- `docs/launch-moving-quote-mvp.md`
- `docs/research/moving-offer-shortlist-20260610.md`
- `docs/research/captured-evidence-20260610.md`

### B. Wedding Event Guide Funnel

Rationale:

- source article used a wedding/event theme,
- search ranking and pain terms are strong,
- high-intent users can engage with checklist/test content,
- needs more non-promotional community evidence before first launch.

Possible content:

- wedding style quiz
- venue checklist
- budget calculator
- event comparison landing page

### C. Relationship/Tarot Viral Funnel

Rationale:

- comments and article mention tarot/test-style content as a simple viral wrapper,
- interactive content increases dwell time and sharing.

Possible content:

- relationship tarot
- compatibility quiz
- result cards for sharing

Risk:

- must avoid medical, financial, or guaranteed-outcome claims.
- weaker direct monetization fit than moving quote because curiosity traffic may not have purchase intent.

### D. Recovery/Finance Consultation Funnel

Rationale:

- comments mention personal recovery/debt examples as CPA category.

Risk:

- high compliance sensitivity,
- must avoid deceptive targeting, predatory language, and unsupported financial claims.

Recommendation:

- do not start here until compliance templates exist.

## Recommended MVP Pick

Start with `Moving Quote Call-Burden Reducer`.

Why:

- strongest captured money logic among researched candidates,
- high-intent problem close to a quote/consultation action,
- clear user pain around unwanted calls and added-cost risk,
- good fit for a static decision-support pre-lander,
- v1 can use outbound CTA tracking without storing personal information.

## First 7-Day Plan

Day 1:

- create repo skeleton and shared CDP capture utility
- define campaign registry schema
- confirm usable moving quote CPA/CPC/partner offer

Day 2:

- build landing brief generator from structured YAML/JSON
- create first moving quote checklist landing page template

Day 3:

- generate 20 content hooks and 5 CTA/checklist variants
- add UTM builder

Day 4:

- implement local static export
- deploy one test site manually

Day 5:

- add screenshot/evidence capture
- build analytics checklist

Day 6:

- produce Threads and Naver Blog content calendar manually reviewed before posting

Day 7:

- review metrics and decide whether to add form capture or stay outbound-only

## Immediate Next Step

Create a new project scaffold named `leadgen-lab` with:

- Python or Node CLI for campaign registry and CDP capture
- `data/campaigns/*.yaml`
- `templates/landing/`
- `outputs/sites/`
- `evidence/`
- a first sample campaign: `moving-quote-call-burden`
