# Korean Community Topic Ranking

This is a heuristic ranking from Naver Blog/Cafe search results. It is not a final market decision.
Use the high-signal source lists to open and capture primary evidence before committing to a landing theme.

## Ranking

| Rank | Topic | Score | Records | Unique URLs | High Signal | Top Pain Terms |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `wedding-fair-privacy` | 75.53 | 160 | 152 | 99 | 전화:104, 호구:50, 스팸:41, 개인정보:25, 주의:13 |
| 2 | `moving-quote` | 64.36 | 120 | 114 | 89 | 전화:83, 스트레스:55, 걱정:6, 전화폭탄:2, 바가지:2 |
| 3 | `interior-estimate` | 61.64 | 120 | 116 | 86 | 후회:47, 추가비용:20, 걱정:7, 전화:2, 실패:2 |
| 4 | `appliance-rental` | 49.89 | 100 | 96 | 61 | 전화:69, 개인정보:26, 후회:6, 귀찮:2, 사기:1 |
| 5 | `telecom-install` | 41.17 | 100 | 99 | 45 | 전화:46, 사기:33, 피해:3, 귀찮:3, 걱정:2 |
| 6 | `vibecoding-gtm` | 26.92 | 100 | 93 | 25 | 주의:1, 실패:1 |

## First-Pass Interpretation

- Current heuristic winner: `wedding-fair-privacy`
- Prioritize topics with repeated pain language and cafe/community results, not just high-volume promotional blog posts.
- Open and CDP-capture the top 5 to 10 sources for the top 2 topics before deciding what to build.

## Suggested Capture Command

```powershell
python src\cdp_capture_current_page.py --source korean-community --slug <topic> --url-regex "naver|threads|dcinside|clien|ppomppu|teamblind|tistory|blog"
```