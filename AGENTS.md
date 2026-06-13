# Repository Guidelines

## Project Structure & Module Organization

This repository is a Python-based lead generation research and launch workspace.

- `src/` contains executable scripts:
  - `research_collect.py` collects Naver Blog/Cafe and Datalab research scaffolding.
  - `research_analyze.py` scores collected sources and writes rankings.
  - `cdp_capture_current_page.py` captures browser evidence through Chrome CDP.
  - `marketing_automation.py` generates manual publishing queues and UTM links.
- `data/campaigns/` stores campaign configuration YAML files.
- `RESEARCH/` stores topic research sessions, generated query sets, source lists, and scoring outputs.
- `docs/` contains PRDs, runbooks, launch notes, and research summaries.
- `evidence/` stores captured screenshots, HTML frames, text, and summaries.
- `outputs/` stores generated marketing assets and static landing pages, including `outputs/sites/moving-quote-call-burden/index.html`.

## Build, Test, and Development Commands

Run commands from the repository root.

```powershell
python src\research_collect.py --list-topics
python src\research_collect.py --topic moving-quote --display 10
python src\research_analyze.py
python src\marketing_automation.py --campaign data\campaigns\moving-quote-call-burden.yaml --start-date 2026-06-10
python src\cdp_capture_current_page.py --source korean-community --slug moving-quote --url-regex "naver|blog|cafe"
python -m py_compile src\*.py
```

`research_collect.py` uses `NAVER_CLIENT_ID` and `NAVER_CLIENT_SECRET` when available; without them, it still writes scaffolding with skipped API data.

## Coding Style & Naming Conventions

Use Python 3.11+ style with type hints where practical. Keep scripts simple and CLI-oriented with `argparse`, `Path`, dataclasses, and small pure helper functions. Use 4-space indentation, `snake_case` for functions and variables, `UPPER_CASE` for constants, and descriptive output directory names such as `moving-quote-call-burden`.

Generated files should be written with UTF-8 encoding. Avoid committing `__pycache__/`, browser logs, or one-off screenshots unless they are intentional evidence artifacts.

## Testing Guidelines

There is no formal test suite yet. For script changes, run `python -m py_compile src\*.py` and execute the affected CLI on a small input or existing fixture directory. For capture changes, verify the output directory contains `summary.json`, `frames.json`, `visible_text.txt`, and `screenshot.png`.

## Commit & Pull Request Guidelines

This workspace currently has no Git history. Use concise, imperative commit subjects when Git is initialized, for example `Add moving quote capture runbook`. Pull requests should include a short purpose statement, changed paths, commands run, generated output locations, and screenshots when landing page or capture output changes.

## Security & Configuration Tips

Keep API credentials in environment variables only. Do not commit secrets, private account cookies, or unredacted personal data. Marketing automation must remain draft-only: review channel rules, disclosures, and compliance claims before publishing manually.
