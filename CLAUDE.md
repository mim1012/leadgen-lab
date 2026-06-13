# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

**Leadgen Lab** is a local-first campaign workbench for building and testing niche lead-generation funnels. The core workflow:

1. Research a pain-point topic using Korean community signals (Naver Blog/Cafe, Threads, etc.)
2. Identify a matching CPA/affiliate offer and record its compliance restrictions
3. Generate a static landing page that acts as a consent-first pre-lander (checklist/diagnosis → outbound CTA)
4. Produce a manually-reviewed content calendar
5. Publish traffic content manually; track outbound clicks and iterate

The first live campaign is **이사 견적 신청 가능 여부 30초 진단** (moving-quote-call-burden), deployed to Vercel at `moving-quote-call-burden.vercel.app`.

## Commands

### Research pipeline

```powershell
# List built-in research topics
python src\research_collect.py --list-topics

# Collect Naver Blog/Cafe results and Datalab trend data for a topic
$env:NAVER_CLIENT_ID="..."; $env:NAVER_CLIENT_SECRET="..."
python src\research_collect.py --topic moving-quote --display 10

# Score and rank all collected topics
python src\research_analyze.py

# Capture the currently open Chrome tab via CDP (Chrome must be running with --remote-debugging-port=9222)
python src\cdp_capture_current_page.py --source korean-community --slug moving-quote --url-regex "naver|threads|dcinside"
```

### Marketing automation

```powershell
# Generate a 7-day content calendar for a campaign (outputs to outputs/marketing/<campaign>/<date>/)
python src\marketing_automation.py --campaign data/campaigns/moving-quote-call-burden.yaml --start-date 2026-06-12
```

### Landing site (static HTML)

The current landing page is `outputs/sites/moving-quote-call-burden/index.html` — a single self-contained HTML file. To serve it locally:

```powershell
python -m http.server 4180 --directory outputs/sites/moving-quote-call-burden
```

Deploy to Vercel by pointing the project root at `outputs/sites/moving-quote-call-burden/`.

## Architecture

### Directory layout

| Path | Purpose |
|---|---|
| `src/` | Python CLI tools (research, capture, analysis, marketing) |
| `data/campaigns/*.yaml` | Campaign registry — one file per CPA/affiliate campaign |
| `RESEARCH/community-leadgen-<date>/topics/<topic>/` | Per-topic research artifacts (queries, sources, analysis, scoring) |
| `evidence/` | CDP-captured screenshots and DOM snapshots from research browsing |
| `outputs/sites/<campaign>/` | Generated static landing pages (deployable to Vercel/Netlify) |
| `outputs/marketing/<campaign>/<date>/` | Generated content calendar CSVs and markdown |
| `docs/` | PRD, launch plans, research findings, and compliance notes |

### Core Python scripts

- **`research_collect.py`** — Queries Naver Search API (blog + cafearticle) and Naver Datalab for each topic's keyword set. Writes `sources.jsonl`, `datalab.json`, `capture-queue.md`, and `scoring-template.csv` per topic. Requires `NAVER_CLIENT_ID` and `NAVER_CLIENT_SECRET` env vars; runs in scaffold-only mode without them.

- **`research_analyze.py`** — Scores each collected source record with a heuristic (pain terms × 4, intent terms × 2, promo terms −2, cafearticle +3, rank bonus). Produces `analysis.json` and `high-signal-sources.md` per topic, then `topic-ranking.md` at the session root.

- **`cdp_capture_current_page.py`** — Attaches to a Chrome CDP port (`localhost:9222` by default) and does a **read-only** capture of the current tab: screenshot, full DOM, visible text, links, images, and form controls. Writes everything under `evidence/<source>/<slug>-<timestamp>/`. Requires `playwright` (`pip install playwright && playwright install chromium`).

- **`marketing_automation.py`** — Reads a campaign YAML file and generates a 7-day draft content calendar (Naver Blog posts, Threads posts, community checklist share, internal review). All items are marked `requires_human_review: yes` and `auto_post_allowed: no`. Outputs to `outputs/marketing/`.

### Campaign YAML schema (`data/campaigns/*.yaml`)

Key fields: `id`, `status` (researching → ready_for_traffic → launched → paused), `offer_candidates` with network/payout/rejection rules, `landing.production_url`, `landing.disclosure`, `landing.primary_cta_url`, `tracking.events`, `success_criteria`, and `restrictions`.

### Landing page pattern

Current pages are single-file static HTML. The pattern is a **diagnosis pre-lander**: a short selector or checklist that qualifies the user (e.g., moving date within 55 days, able to receive calls) before routing them to the affiliate CTA. No personal data is stored locally in v1.

## Compliance Rules (non-negotiable)

- Every piece of content linking to an affiliate offer must include `[광고]` in the title or first line.
- Disclosure must use definite language ("수익이 지급됩니다") not weak language ("받을 수 있음").
- The Adlix Daisa campaign requires the user's moving date to be within 55 days — route only qualifying users to the outbound CTA.
- Do not automate community posting, comments, likes, DMs, or cafe activity.
- Do not collect personal data locally until privacy/consent copy is finalized and reviewed.
- Do not promise that users will receive no calls.

## Environment Variables

| Variable | Used by | Purpose |
|---|---|---|
| `NAVER_CLIENT_ID` | `research_collect.py` | Naver Open API app ID |
| `NAVER_CLIENT_SECRET` | `research_collect.py` | Naver Open API secret |

Scripts run without API credentials but skip live API calls and write placeholder files.
