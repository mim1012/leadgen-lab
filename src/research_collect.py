from __future__ import annotations

import argparse
import csv
import html
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_ROOT = ROOT / "RESEARCH" / "community-leadgen-20260610"
NAVER_SEARCH_URLS = {
    "blog": "https://openapi.naver.com/v1/search/blog.json",
    "cafearticle": "https://openapi.naver.com/v1/search/cafearticle.json",
}
NAVER_DATALAB_URL = "https://openapi.naver.com/v1/datalab/search"


TOPICS: dict[str, dict[str, object]] = {
    "wedding-fair-privacy": {
        "label": "웨딩박람회 개인정보/전화 부담",
        "queries": [
            "웨딩박람회 전화 많이 와요",
            "웨딩박람회 개인정보 후기",
            "웨딩박람회 호구 안되는법",
            "웨딩박람회 상담 전화 후기",
            "웨딩박람회 신청 전 체크리스트",
            "결혼준비 카페 웨딩박람회 후기 광고 아님",
            "웨딩박람회 스팸 전화",
            "웨딩박람회 플래너 상담 후기",
        ],
    },
    "moving-quote": {
        "label": "이사 견적 비교/상담 부담",
        "queries": [
            "이사 견적 전화 스트레스",
            "포장이사 견적 비교 후기",
            "이사 업체 견적 추가요금 후기",
            "반포장이사 포장이사 선택 기준",
            "이사 견적 상담 전화 많이 와요",
            "이사 견적 받기 전 체크리스트",
        ],
    },
    "interior-estimate": {
        "label": "인테리어 견적/추가비용 불안",
        "queries": [
            "인테리어 견적 추가비용 후기",
            "인테리어 업체 상담 전 체크리스트",
            "인테리어 견적 비교 후기",
            "인테리어 업체 고르는 기준 커뮤니티",
            "인테리어 상담 후회 후기",
            "아파트 인테리어 견적 질문 리스트",
        ],
    },
    "appliance-rental": {
        "label": "정수기/가전 렌탈 상담 부담",
        "queries": [
            "정수기 렌탈 전화 상담 후기",
            "정수기 렌탈 비교 후기",
            "가전 렌탈 상담 전화 많이 와요",
            "정수기 렌탈 개인정보 후기",
            "정수기 렌탈 고르는 기준",
        ],
    },
    "telecom-install": {
        "label": "인터넷 설치/통신 변경 비교",
        "queries": [
            "인터넷 설치 현금지원 후기",
            "인터넷 가입 상담 전화 후기",
            "인터넷 통신사 변경 비교 커뮤니티",
            "인터넷 설치 사은품 사기 후기",
            "인터넷 가입 전 체크리스트",
        ],
    },
    "vibecoding-gtm": {
        "label": "바이브코딩 수익화/마케팅",
        "queries": [
            "바이브코딩 수익화 후기",
            "바이브코딩 랜딩페이지 수익화",
            "바이브코딩 마케팅 어려움",
            "AI 코딩 서비스 출시 후기 수익화",
            "사이드프로젝트 마케팅 첫 유저",
        ],
    },
}


@dataclass(frozen=True)
class NaverCredentials:
    client_id: str
    client_secret: str


def safe_name(value: str) -> str:
    allowed = []
    for char in value.strip():
        if char.isalnum() or char in "._-":
            allowed.append(char)
        elif char.isspace():
            allowed.append("-")
    slug = "".join(allowed).strip("-._")
    return slug[:80] or "research"


def strip_tags(value: str) -> str:
    text = value.replace("<b>", "").replace("</b>", "")
    return html.unescape(text)


def get_credentials() -> NaverCredentials | None:
    client_id = os.environ.get("NAVER_CLIENT_ID", "").strip()
    client_secret = os.environ.get("NAVER_CLIENT_SECRET", "").strip()
    if not client_id or not client_secret:
        return None
    return NaverCredentials(client_id=client_id, client_secret=client_secret)


def naver_get(url: str, params: dict[str, str | int], credentials: NaverCredentials) -> dict:
    request_url = f"{url}?{urlencode(params)}"
    request = Request(
        request_url,
        headers={
            "X-Naver-Client-Id": credentials.client_id,
            "X-Naver-Client-Secret": credentials.client_secret,
        },
    )
    with urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def naver_post(url: str, payload: dict, credentials: NaverCredentials) -> dict:
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-Naver-Client-Id": credentials.client_id,
            "X-Naver-Client-Secret": credentials.client_secret,
        },
    )
    with urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def collect_search_results(
    topic: str,
    queries: list[str],
    display: int,
    credentials: NaverCredentials | None,
) -> list[dict]:
    if credentials is None:
        return []

    collected_at = datetime.now().isoformat(timespec="seconds")
    records: list[dict] = []
    for query in queries:
        for source_type, url in NAVER_SEARCH_URLS.items():
            try:
                data = naver_get(
                    url,
                    {
                        "query": query,
                        "display": display,
                        "start": 1,
                        "sort": "sim",
                    },
                    credentials,
                )
            except Exception as exc:
                records.append(
                    {
                        "topic": topic,
                        "query": query,
                        "source_type": source_type,
                        "rank": "",
                        "title": "",
                        "snippet": "",
                        "url": "",
                        "postdate": "",
                        "collected_at": collected_at,
                        "error": str(exc),
                    }
                )
                continue
            for rank, item in enumerate(data.get("items", []), start=1):
                records.append(
                    {
                        "topic": topic,
                        "query": query,
                        "source_type": source_type,
                        "rank": rank,
                        "title": strip_tags(item.get("title", "")),
                        "snippet": strip_tags(item.get("description", "")),
                        "url": item.get("link", ""),
                        "postdate": item.get("postdate", ""),
                        "collected_at": collected_at,
                    }
                )
    return records


def collect_datalab(topic: str, queries: list[str], credentials: NaverCredentials | None) -> dict:
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=365)
    payload = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "timeUnit": "month",
        "keywordGroups": [{"groupName": topic, "keywords": queries[:20]}],
        "device": "",
        "ages": [],
        "gender": "",
    }
    if credentials is None:
        return {"skipped": True, "reason": "NAVER_CLIENT_ID/NAVER_CLIENT_SECRET are not set", "payload": payload}
    return naver_post(NAVER_DATALAB_URL, payload, credentials)


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_jsonl(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_capture_queue(path: Path, topic: str, queries: list[str], records: list[dict]) -> None:
    lines = [
        f"# Capture Queue: {topic}",
        "",
        "Open high-signal URLs manually in Chrome, then run:",
        "",
        "```powershell",
        f"python src\\cdp_capture_current_page.py --source korean-community --slug {safe_name(topic)} --url-regex \"naver|threads|dcinside|clien|ppomppu|teamblind|tistory|blog\"",
        "```",
        "",
        "## Query List",
        "",
    ]
    lines.extend(f"- {query}" for query in queries)
    lines.extend(["", "## Candidate URLs", ""])
    if records:
        for record in records:
            lines.append(f"- [{record['source_type']}] {record['title']} - {record['url']}")
    else:
        lines.append("- No API results collected yet. Set `NAVER_CLIENT_ID` and `NAVER_CLIENT_SECRET`, then rerun.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_scoring_template(path: Path) -> None:
    fields = [
        "source_id",
        "url",
        "topic",
        "pain_intensity_1_5",
        "purchase_intent_1_5",
        "lead_value_1_5",
        "search_demand_1_5",
        "community_density_1_5",
        "compliance_risk_1_5",
        "content_originality_1_5",
        "landing_feasibility_1_5",
        "marketing_channel_fit_1_5",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()


def write_session_readme(path: Path, topic: str, label: str, credentials: NaverCredentials | None) -> None:
    api_status = "enabled" if credentials else "skipped; missing NAVER_CLIENT_ID/NAVER_CLIENT_SECRET"
    path.write_text(
        "\n".join(
            [
                f"# Research Topic: {topic}",
                "",
                f"Label: {label}",
                f"Created at: {datetime.now().isoformat(timespec='seconds')}",
                f"Naver API collection: {api_status}",
                "",
                "## Files",
                "",
                "- `queries.json`: generated Korean query set",
                "- `sources.jsonl`: Naver Blog/Cafe result records when API credentials exist",
                "- `datalab.json`: Naver Datalab response or skipped payload",
                "- `capture-queue.md`: manual browser capture queue",
                "- `scoring-template.csv`: scoring sheet for captured evidence",
                "",
                "## Next Step",
                "",
                "Review `capture-queue.md`, open the strongest pages manually, and capture them with `src/cdp_capture_current_page.py`.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def resolve_topic(topic: str) -> tuple[str, list[str]]:
    if topic in TOPICS:
        item = TOPICS[topic]
        return str(item["label"]), list(item["queries"])  # type: ignore[arg-type]
    return topic, [topic]


def list_topics() -> None:
    for key, item in TOPICS.items():
        print(f"{key}\t{item['label']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect Korean community research scaffolding and optional Naver API data.")
    parser.add_argument("--topic", help="Topic key or raw Korean query.")
    parser.add_argument("--display", type=int, default=10, help="Naver results per query/source. Default: 10")
    parser.add_argument("--list-topics", action="store_true", help="List built-in topic keys.")
    parser.add_argument("--out-root", default=str(RESEARCH_ROOT), help="Research output root.")
    args = parser.parse_args()

    if args.list_topics:
        list_topics()
        return 0
    if not args.topic:
        parser.error("--topic is required unless --list-topics is used")

    label, queries = resolve_topic(args.topic)
    topic_slug = safe_name(args.topic)
    out_dir = Path(args.out_root) / "topics" / topic_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    credentials = get_credentials()
    write_json(out_dir / "queries.json", {"topic": args.topic, "label": label, "queries": queries})
    records = collect_search_results(args.topic, queries, args.display, credentials)
    try:
        datalab = collect_datalab(args.topic, queries, credentials)
    except Exception as exc:
        print(f"datalab collection failed: {exc}", file=sys.stderr)
        datalab = {"error": str(exc)}

    write_jsonl(out_dir / "sources.jsonl", records)
    write_json(out_dir / "datalab.json", datalab)
    write_capture_queue(out_dir / "capture-queue.md", args.topic, queries, records)
    write_scoring_template(out_dir / "scoring-template.csv")
    write_session_readme(out_dir / "README.md", args.topic, label, credentials)

    print(str(out_dir))
    print(f"queries: {len(queries)}")
    print(f"sources: {len(records)}")
    print("naver_api:", "enabled" if credentials else "skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
