# Korean Community Research Tooling

## Purpose

Leadgen Lab should research Korean community demand before choosing the first landing-page theme.

This document records useful skills, APIs, GitHub repositories, and open-source options for Korean community research.

## Recommended Research Stack

### 1. Query Discovery

Use this stage to find candidate topics before collecting individual posts.

Best sources:

- Naver Search API: blog and cafe article search
- Naver Datalab Search Trend API
- Naver Search Ads API or keyword planner data when available
- Google/Bing web search for public community pages

Why:

- safer than crawling first,
- gives query volume and result density,
- helps compare themes such as wedding fair, moving quote, interior estimate, appliance rental, and vibe-coding monetization.

Official references:

- Naver Blog Search API: `https://developers.naver.com/docs/serviceapi/search/blog/blog.md`
- Naver Cafe Article Search API: `https://developers.naver.com/docs/serviceapi/search/cafearticle/cafearticle.md`
- Naver Datalab Search Trend API: `https://developers.naver.com/docs/serviceapi/datalab/search/search.md`
- Naver Search Ad API docs: `https://naver.github.io/searchad-apidoc/`

### 2. Read-Only Evidence Capture

Use this stage after a human opens the relevant community pages in a browser.

Current local asset:

- `src/cdp_capture_current_page.py`

Why:

- works with pages already opened by the operator,
- avoids credential automation,
- captures DOM text, links, images, metadata, screenshots, and frames,
- fits Naver Cafe pages with iframe-heavy layouts.

Recommended direction:

- generalize the current script from one hardcoded Naver Cafe URL to a reusable `capture-current-page` command,
- save every capture under `evidence/<source>/<slug>-<timestamp>/`,
- add a source registry so each evidence item links back to a research question.

### 3. Community-Specific Crawlers

Use these as references, not as direct production dependencies.

They may be old, brittle, or unsuitable for logged-in/private content.

#### Naver Cafe

- `https://github.com/lasagnaphil/naver-cafe-archiver`
- `https://github.com/lynn-hong/naverCafeCrawler`
- `https://github.com/LydiaYoon/naver-cafe-crawler`
- `https://github.com/wallypark710/puppeteer-naver-cafe-crawler`
- `https://github.com/dev-jaemin/Naver-Cafe-Crawling`
- `https://github.com/hyunnnn98/Node.js-project-NCafeCrawlingBOT`

Assessment:

- useful for parsing ideas,
- risky as drop-in tools because Naver markup and access controls change,
- avoid login automation or bulk crawling.

#### Naver Blog

- GitHub topic: `https://github.com/topics/naver-blog`
- `https://github.com/Lenir/Naver-Blog-Backup`
- external skill reference found: `https://claudemarketplaces.com/skills/nomadamas/k-skill/naver-blog-research`

Assessment:

- blog content is easier than cafe content because many posts are public,
- Naver mobile blog pages can be easier to parse than desktop iframe pages,
- official Search API should be the first discovery layer.

#### DCInside

- `https://github.com/j1wan/dcoutside`
- `https://github.com/ji1kang/dcinside-scraper`
- `https://github.com/hanel2527/dcinside-crawler`
- `https://github.com/seunghyukcho/dc-crawler`
- `https://github.com/eunchuldev/dcinside-python3-api`

Assessment:

- DCInside has accessible public pages,
- signal can be noisy and adversarial,
- useful for raw pain language, but weak as definitive market proof.

#### Multi-Community Korean Crawlers

- `https://github.com/dev-Lesser/online-community-crawler`

Covered sources in the project description:

- Ilbe
- DCInside
- Inven
- MLBPark
- Ppomppu
- Clien

Assessment:

- useful reference for normalized community post schema,
- source mix should be filtered carefully for brand safety,
- do not blindly include all communities in product research.

#### Clien and Ppomppu

- Clien topic: `https://github.com/topics/clien`
- `https://github.com/chanhee-kang/clien_community_cralwer`
- `https://github.com/KimDoKy/Ppomppu_check`

Assessment:

- better for consumer purchase, device, telecom, and service-deal signals,
- likely useful for rental, internet, moving, appliance, and home-service topics.

## General Web/LLM Crawling Tools

### Crawl4AI

- `https://github.com/unclecode/crawl4AI`

Use when:

- public pages need to be converted into LLM-friendly Markdown,
- source pages are not heavily login-gated,
- the goal is structured extraction and summarization.

Do not rely on it for:

- private Naver Cafe pages,
- bypassing bot checks,
- account-gated communities.

### Firecrawl MCP

- `https://github.com/firecrawl/firecrawl-mcp-server`

Use when:

- external hosted crawling is acceptable,
- API keys and paid usage are acceptable,
- broad web search plus scrape is needed.

Current recommendation:

- not required for the first local prototype.

## Korean NLP and Analysis Assets

Potential uses:

- cluster posts by pain theme,
- extract keywords,
- classify sentiment,
- summarize objections,
- identify repeated decision criteria.

Reference repositories:

- Korean text mining basics: `https://github.com/buomsoo-kim/Web-Crawling-and-Text-mining-with-Python-in-Korean`
- Korean sentiment example: `https://github.com/Huffon/pytorch-sentiment-analysis-kor`
- Korean multi-label sentiment: `https://github.com/amy-hyunji/korean_multi_label_SA`
- Korean instruction model reference: `https://github.com/davidkim205/komt`

Practical recommendation:

- do not start with model training,
- start with LLM-assisted tagging plus a fixed scoring schema,
- add Korean NLP libraries only when volume grows.

## Installed Skills to Use

### `deep-research`

Use for:

- citation-backed topic research,
- source triangulation,
- long-form market research reports.

Current session:

- `RESEARCH/community-leadgen-20260610/`

### `browse`

Use for:

- web page inspection when simple HTTP search is insufficient.

### `analyze`

Use for:

- read-only synthesis of local research files after captures are collected.

### Custom Skill Recommendation

Create a project-specific skill later:

`korean-community-research`

Responsibilities:

- generate Korean search queries,
- call Naver Search/Datalab APIs,
- guide manual CDP capture,
- normalize evidence,
- score candidate topics,
- produce a launch-theme recommendation.

Do not build this skill before the first manual research loop proves the schema.

## Recommended Research Workflow

### Step 1. Topic Candidate List

Start with 5 to 8 candidate leadgen categories:

- wedding fair / wedding preparation,
- moving quote,
- interior estimate,
- internet installation / telecom change,
- appliance rental,
- pet insurance or pet care service,
- study abroad / language school consultation,
- vibe-coding monetization.

### Step 2. Query Expansion

For each category, generate Korean query groups:

- problem keywords,
- fear keywords,
- review keywords,
- quote/price keywords,
- phone-call/privacy keywords,
- community-specific keywords.

Examples:

- `웨딩박람회 전화 많이 와요`
- `웨딩박람회 개인정보 후기`
- `이사 견적 전화 스트레스`
- `인테리어 견적 추가비용 후기`
- `정수기 렌탈 전화 상담 후기`

### Step 3. Search API Collection

Use official APIs first:

- Naver Blog Search API,
- Naver Cafe Article Search API,
- Naver Datalab Search Trend API.

Store:

- query,
- title,
- snippet,
- URL,
- source type,
- date,
- rank,
- collected_at.

### Step 4. Manual Evidence Capture

For high-signal pages:

- open manually in Chrome,
- run CDP read-only capture,
- save screenshot and visible text,
- tag source to candidate topic.

### Step 5. Scoring

Score every candidate from 1 to 5:

- pain intensity,
- purchase intent,
- lead value,
- search demand,
- community discussion density,
- compliance risk,
- content originality,
- landing feasibility,
- marketing channel fit.

### Step 6. Recommendation

Output:

- top 3 candidate themes,
- first landing concept,
- target persona,
- source evidence,
- CTA approach,
- compliance warnings,
- what to research next.

## Current Recommendation

Build the first research tool around official search and read-only capture, not around full crawlers.

Minimum useful tool:

`research collect --topic wedding-fair-privacy`

Output:

- query set,
- Naver Search API result JSON,
- Datalab trend result JSON,
- evidence capture references,
- scored source table.

This gives enough evidence to decide the first landing theme without overbuilding a fragile crawler.

## Local Prototype Commands

List built-in research topics:

```powershell
python src\research_collect.py --list-topics
```

Create a research pack without API keys:

```powershell
python src\research_collect.py --topic wedding-fair-privacy
```

Create a research pack with Naver API collection:

```powershell
$env:NAVER_CLIENT_ID="..."
$env:NAVER_CLIENT_SECRET="..."
python src\research_collect.py --topic wedding-fair-privacy --display 10
```

Required Naver app APIs:

- `검색`
- `데이터랩 (검색어트렌드)`

If `sources.jsonl` contains `HTTP Error 401: Unauthorized`, the Naver app usually has not enabled the `검색` API yet, or the Client ID/Secret pair is from a different app.

If `datalab.json` has an empty `data` array, authentication worked but the query group may be too long-tail or too low-volume for Naver Datalab. Use shorter trend terms such as `웨딩박람회`, `이사견적`, `인테리어견적`, `정수기렌탈`, and keep detailed pain phrases for Blog/Cafe search.

Capture a manually opened high-signal community page through Chrome CDP:

```powershell
python src\cdp_capture_current_page.py --source korean-community --slug wedding-fair-privacy --url-regex "naver|threads|dcinside|clien|ppomppu|teamblind|tistory|blog"
```

The collection command writes to:

```text
RESEARCH/community-leadgen-20260610/topics/<topic>/
```

Each topic folder includes:

- `queries.json`
- `sources.jsonl`
- `datalab.json`
- `capture-queue.md`
- `scoring-template.csv`
- `README.md`

Analyze collected topic packs:

```powershell
python src\research_analyze.py
```

This writes:

- `RESEARCH/community-leadgen-20260610/topic-ranking.md`
- `RESEARCH/community-leadgen-20260610/topic-ranking.json`
- `RESEARCH/community-leadgen-20260610/topics/<topic>/analysis.json`
- `RESEARCH/community-leadgen-20260610/topics/<topic>/high-signal-sources.md`
