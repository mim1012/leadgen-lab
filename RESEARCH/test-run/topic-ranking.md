# Korean Community Topic Ranking

This is a heuristic ranking from Naver Blog/Cafe search results. It is not a final market decision.
Use the high-signal source lists to open and capture primary evidence before committing to a landing theme.

## Ranking

| Rank | Topic | Score | Records | Unique URLs | High Signal | Top Pain Terms |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `moving-quote` | 0.0 | 0 | 0 | 0 |  |

## First-Pass Interpretation

- Current heuristic winner: `moving-quote`
- Prioritize topics with repeated pain language and cafe/community results, not just high-volume promotional blog posts.
- Open and CDP-capture the top 5 to 10 sources for the top 2 topics before deciding what to build.

## Suggested Capture Command

```powershell
python src\cdp_capture_current_page.py --source korean-community --slug <topic> --url-regex "naver|threads|dcinside|clien|ppomppu|teamblind|tistory|blog"
```