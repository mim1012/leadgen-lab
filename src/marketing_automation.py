from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode


@dataclass(frozen=True)
class Campaign:
    campaign_id: str
    name: str
    production_url: str
    promotion_url: str
    disclosure: str
    date_rule: str
    primary_cta: str


def extract_scalar(text: str, key: str, default: str = "") -> str:
    pattern = rf"^\s*{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else default


def extract_landing_value(text: str, key: str, default: str = "") -> str:
    landing = re.search(r"^landing:\s*$([\s\S]*?)(?:^\S|\Z)", text, re.MULTILINE)
    source = landing.group(1) if landing else text
    return extract_scalar(source, key, default)


def load_campaign(path: Path) -> Campaign:
    text = path.read_text(encoding="utf-8")
    return Campaign(
        campaign_id=extract_scalar(text, "id", path.stem),
        name=extract_scalar(text, "name", path.stem),
        production_url=extract_landing_value(text, "production_url"),
        promotion_url=extract_scalar(text, "promotion_url"),
        disclosure=extract_landing_value(text, "disclosure"),
        date_rule=extract_scalar(text, "date_rule", "55일 이내 이사날짜만 견적 신청 가능"),
        primary_cta=extract_landing_value(text, "primary_cta", "준비한 조건으로 비교 견적 확인하기"),
    )


def utm_url(base_url: str, source: str, medium: str, campaign: str, content: str) -> str:
    separator = "&" if "?" in base_url else "?"
    return base_url + separator + urlencode(
        {
            "utm_source": source,
            "utm_medium": medium,
            "utm_campaign": campaign,
            "utm_content": content,
        }
    )


def content_items(campaign: Campaign, start: date) -> list[dict[str, str]]:
    cid = campaign.campaign_id.replace("-", "_")
    landing = campaign.production_url
    items = [
        {
            "day": 1,
            "channel": "naver_blog",
            "medium": "post",
            "content": "checklist_7",
            "title": "[광고] 이사 견적 신청 전 준비할 7가지: 상담을 짧게 끝내는 체크리스트",
            "angle": "준비하면 상담이 짧아진다 — 사전 정리 체크리스트",
            "body": "\n\n".join(
                [
                    campaign.disclosure,
                    "이사 견적을 알아볼 때 가장 힘든 부분은 업체마다 같은 질문을 반복해서 받는 상황입니다. 미리 정리해두면 상담 시간을 줄이고 추가요금 리스크에 대비할 수 있습니다.",
                    "준비할 항목: 이사일, 출발지/도착지 주소와 층수, 큰 가구와 가전 목록, 사다리차·주말·분해설치 추가요금 질문, 연락 가능한 시간.",
                    f"참고: {campaign.date_rule}. 아직 일정이 멀다면 체크리스트만 정리해두고 일정이 확정됐을 때 신청하는 편이 낫습니다.",
                    f"체크리스트 정리 후 지금 준비된 상태인지 30초로 확인하세요: {utm_url(landing, 'naver_blog', 'post', cid, 'checklist_7')}",
                ]
            ),
        },
        {
            "day": 2,
            "channel": "threads",
            "medium": "social",
            "content": "thread_call_control",
            "title": "[광고] 견적 신청 전에 먼저 정해야 하는 것",
            "angle": "준비 순서 — 업체보다 내 조건이 먼저",
            "body": "\n\n".join(
                [
                    "[광고] 이사 견적 신청할 때 업체보다 먼저 정해야 하는 게 있습니다. 몇 곳까지 상담받을지, 연락 가능한 시간이 언제인지입니다.",
                    "이걸 먼저 정리하지 않으면 비교가 아니라 통화 관리가 일이 됩니다.",
                    f"30초 준비 상태 확인: {utm_url(landing, 'threads', 'social', cid, 'thread_call_control')}",
                    "제휴 링크 포함. 신청/클릭 시 수익이 지급됩니다. 이사 예정일 55일 이내 + 상담 연락 가능할 때 적합합니다.",
                ]
            ),
        },
        {
            "day": 3,
            "channel": "threads",
            "medium": "social",
            "content": "thread_extra_fee",
            "title": "[광고] 낮은 첫 견적 전에 확인할 것",
            "angle": "추가요금 대비 — 첫 가격 ≠ 최종 금액",
            "body": "\n\n".join(
                [
                    "[광고] 포장이사 견적이 낮게 나왔다면 사다리차, 주말, 손 없는 날, 분해·설치 비용이 포함됐는지 먼저 확인하세요. 빠져 있으면 최종 금액이 달라집니다.",
                    "신청 전에 이 질문 리스트를 준비해두면 추가요금 리스크에 미리 대비할 수 있습니다.",
                    f"준비 상태 확인 후 비교 견적으로: {utm_url(landing, 'threads', 'social', cid, 'thread_extra_fee')}",
                    "제휴 링크 포함. 신청/클릭 시 수익이 지급됩니다.",
                ]
            ),
        },
        {
            "day": 4,
            "channel": "naver_blog",
            "medium": "post",
            "content": "extra_fee_10",
            "title": "[광고] 이사 견적 신청 전 준비할 추가요금 질문 10가지",
            "angle": "첫 가격과 최종 비용 차이를 줄이는 사전 질문 리스트",
            "body": "\n\n".join(
                [
                    campaign.disclosure,
                    "이사 견적은 첫 가격보다 조건 확인이 더 중요합니다. 아래 질문을 미리 준비해두면 업체별 비교가 쉬워지고 추가요금 리스크에 대비할 수 있습니다.",
                    "확인할 항목: 사다리차 비용, 주말·손 없는 날 추가비, 분해·설치, 큰 가전 이동, 보관 여부, 폐기물 처리, 장거리 추가비, 주차 가능 여부, 엘리베이터 사용, 방문 견적 필요 여부.",
                    f"질문 준비 후 지금 신청 가능한 상태인지 확인하세요: {utm_url(landing, 'naver_blog', 'post', cid, 'extra_fee_10')}",
                ]
            ),
        },
        {
            "day": 5,
            "channel": "community",
            "medium": "post",
            "content": "checklist_share",
            "title": "[광고] 이사 견적 신청 전 준비 체크리스트 공유합니다",
            "angle": "본문 자체가 가치 있는 커뮤니티 안전 공유",
            "body": "\n\n".join(
                [
                    campaign.disclosure,
                    "이사 견적 알아볼 때 업체마다 물어보는 내용이 달라서, 같은 조건을 말하지 않으면 가격 비교가 어렵더라고요. 미리 정리해두면 상담이 짧아집니다.",
                    "준비할 것: 이사 예정일, 출발지/도착지 주소와 층수, 엘리베이터/주차/사다리차 여부, 큰 가구와 가전, 추가요금 질문, 연락 가능 시간, 상담받을 업체 수.",
                    f"정리 후 지금 준비된 상태인지 30초로 확인할 수 있습니다: {utm_url(landing, 'community', 'post', cid, 'checklist_share')}",
                    "카페/커뮤니티 규칙상 제휴 링크가 허용되는 곳에서만 사용하세요.",
                ]
            ),
        },
        {
            "day": 6,
            "channel": "threads",
            "medium": "social",
            "content": "thread_contact_time",
            "title": "[광고] \"아무 때나 연락 주세요\"가 힘든 이유",
            "angle": "연락 시간 미리 정하기 — 준비의 일부",
            "body": "\n\n".join(
                [
                    "[광고] 이사 견적 상담이 부담스럽다면 신청 전에 연락 가능한 시간을 먼저 정해두세요.",
                    "\"아무 때나 연락 주세요\"로 신청하면 통화 관리가 일이 될 수 있습니다. 업체 수, 연락 시간, 추가요금 질문을 미리 준비하는 게 낫습니다.",
                    f"30초 준비 상태 확인: {utm_url(landing, 'threads', 'social', cid, 'thread_contact_time')}",
                    "제휴 링크 포함. 이사 예정일 55일 이내이고 상담 연락을 받을 수 있는 경우에 적합합니다.",
                ]
            ),
        },
        {
            "day": 7,
            "channel": "review",
            "medium": "internal",
            "content": "metrics_review",
            "title": "20 outbound clicks review",
            "angle": "성과 점검 및 다음 액션 결정",
            "body": "방문수, outbound click, Adlix DB 발생 여부, 승인/거절 사유를 기록하고 다음 주 콘텐츠 각도를 결정합니다.",
        },
    ]

    for item in items:
        item["publish_date"] = (start + timedelta(days=int(item["day"]) - 1)).isoformat()
        item["utm_url"] = utm_url(landing, item["channel"], item["medium"], cid, item["content"])
        item["status"] = "draft" if item["channel"] != "review" else "scheduled_review"
        item["requires_human_review"] = "yes"
        item["auto_post_allowed"] = "no"
    return items


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, campaign: Campaign, items: list[dict[str, str]]) -> None:
    lines = [
        f"# Marketing Automation Queue - {campaign.name}",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Safety Rules",
        "",
        "- This queue drafts content only. It does not post automatically.",
        "- Keep `[광고]` in the title or first line.",
        "- Do not automate community posts, comments, likes, DMs, or repeated link drops.",
        "- Route strong CTA only to users whose moving date is within 55 days and who can receive consultation calls.",
        "",
        "## Queue",
        "",
    ]
    for item in items:
        lines.extend(
            [
                f"### Day {item['day']} - {item['channel']} - {item['title']}",
                "",
                f"- Date: `{item['publish_date']}`",
                f"- Status: `{item['status']}`",
                f"- UTM: `{item['utm_url']}`",
                f"- Angle: {item['angle']}",
                "",
                "```text",
                item["body"],
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_metrics_template(path: Path) -> None:
    fields = [
        "date",
        "source",
        "content",
        "published_url",
        "landing_visits",
        "outbound_clicks",
        "outbound_ctr",
        "adlix_db_count",
        "approved_count",
        "rejected_count",
        "rejection_notes",
        "next_action",
    ]
    write_csv(path, [], fields)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate safe marketing automation assets for one campaign.")
    parser.add_argument("--campaign", default="data/campaigns/moving-quote-call-burden.yaml")
    parser.add_argument("--start-date", default=date.today().isoformat())
    parser.add_argument("--out-dir", default="")
    args = parser.parse_args()

    campaign_path = Path(args.campaign)
    campaign = load_campaign(campaign_path)
    start = date.fromisoformat(args.start_date)
    out_dir = Path(args.out_dir) if args.out_dir else Path("outputs/marketing") / campaign.campaign_id / start.isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)

    items = content_items(campaign, start)
    queue_fields = [
        "publish_date",
        "day",
        "channel",
        "medium",
        "content",
        "title",
        "angle",
        "utm_url",
        "status",
        "requires_human_review",
        "auto_post_allowed",
        "body",
    ]
    link_fields = ["channel", "medium", "content", "utm_url"]

    write_csv(out_dir / "publish_queue.csv", items, queue_fields)
    write_csv(out_dir / "utm_links.csv", items, link_fields)
    write_metrics_template(out_dir / "metrics_template.csv")
    write_markdown(out_dir / "content_calendar.md", campaign, items)
    (out_dir / "README.md").write_text(
        "\n".join(
            [
                f"# Marketing Automation Output - {campaign.campaign_id}",
                "",
                "Generated files:",
                "",
                "- `publish_queue.csv`: draft queue for manual publishing.",
                "- `utm_links.csv`: source/content-specific UTM links.",
                "- `metrics_template.csv`: copy and fill after publishing.",
                "- `content_calendar.md`: readable 7-day content plan.",
                "",
                "Posting is intentionally manual. Review every item before publishing.",
            ]
        ),
        encoding="utf-8",
    )

    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
