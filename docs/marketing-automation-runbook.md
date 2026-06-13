# Marketing Automation Runbook

## What Is Automated

This project automates the safe parts of marketing:

- 7-day content calendar generation,
- Naver Blog / Threads / community draft queue,
- source-specific UTM link generation,
- metrics collection template,
- compliance reminders.

It does not automate posting, comments, likes, DMs, cafe activity, or account actions.

## Command

Generate a new marketing queue:

```powershell
python src\marketing_automation.py --campaign data\campaigns\moving-quote-call-burden.yaml --start-date 2026-06-10
```

Output directory:

```text
outputs\marketing\moving-quote-call-burden\2026-06-10
```

Generated files:

- `content_calendar.md`: readable 7-day publishing plan with draft copy.
- `publish_queue.csv`: spreadsheet-friendly publishing queue.
- `utm_links.csv`: UTM links by source/content.
- `metrics_template.csv`: fill after publishing.
- `README.md`: output summary.

## Review Gate Before Publishing

Before any item is published:

1. Keep `[광고]` in the title or first line.
2. Confirm the channel allows affiliate or sponsored links.
3. Confirm the link uses the correct UTM source/content.
4. Confirm the copy does not promise "no calls".
5. Confirm the copy does not claim lowest price.
6. Confirm the copy routes strong CTA only to users with an expected move date within 55 days and willingness to receive consultation calls.

## Daily Flow

1. Open `content_calendar.md`.
2. Copy the next draft into the target channel manually.
3. Paste the published URL into `metrics_template.csv`.
4. Check landing/outbound metrics.
5. Check Adlix for DB count and approval/rejection signal.

## 20-Click Review Rule

Do not scale traffic until at least 20 outbound clicks are recorded.

Review:

- source,
- content item,
- landing visits,
- outbound clicks,
- outbound CTR,
- Adlix DB count,
- approval count,
- rejection count,
- rejection notes.

Decision:

- Low outbound CTR: revise headline, CTA, or first-screen copy.
- High outbound CTR but weak DB quality: tighten 55-day and consultation-call qualification.
- Good outbound CTR and DB quality: generate the next 7-day queue with the winning angle.


## Traffic Monitoring And Automation TODO

Detailed monitoring alert rules and channel-specific automation boundaries are maintained in:

- `docs/traffic-monitoring-and-automation-todo.md`

## Next Automation Layer

After one source produces approved DBs, add:

- server-side outbound click logging,
- weekly queue generation from winning angles,
- content variant scoring,
- automatic report generation.

Posting automation should wait for approved channel APIs, explicit account permissions, and per-post human approval.

