from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_ROOT = ROOT / "RESEARCH" / "community-leadgen-20260610"


PAIN_TERMS = [
    "전화",
    "전화폭탄",
    "스팸",
    "개인정보",
    "스트레스",
    "후회",
    "호구",
    "바가지",
    "추가비용",
    "사기",
    "피해",
    "불안",
    "걱정",
    "주의",
    "실패",
    "귀찮",
    "지치",
]

INTENT_TERMS = [
    "견적",
    "비교",
    "상담",
    "신청",
    "체크리스트",
    "고르는",
    "선택",
    "비용",
    "가격",
    "후기",
    "질문",
    "계약",
]

COMMUNITY_TERMS = [
    "카페",
    "커뮤니티",
    "디시",
    "블라인드",
    "클리앙",
    "뽐뿌",
    "후기",
    "광고 아님",
    "솔직",
]

PROMO_TERMS = [
    "추천드",
    "추천드려요",
    "무료견적",
    "무료 상담",
    "최대",
    "혜택",
    "프로모션",
    "이벤트",
    "사전신청",
    "바로가기",
    "문의",
    "업체",
    "브랜드",
    "협찬",
    "광고",
    "제공받",
    "체험단",
    "파트너스",
]


@dataclass
class ScoredRecord:
    record: dict
    score: int
    reasons: list[str]


def load_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    if not path.exists():
        return records
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        records.append(json.loads(line))
    return records


def text_for(record: dict) -> str:
    return " ".join(str(record.get(key, "")) for key in ("query", "title", "snippet", "url"))


def count_terms(text: str, terms: list[str]) -> int:
    return sum(1 for term in terms if term in text)


def domain_of(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc.lower()


def score_record(record: dict) -> ScoredRecord:
    text = text_for(record)
    score = 0
    reasons: list[str] = []

    if record.get("error"):
        return ScoredRecord(record, -100, [f"error: {record['error']}"])

    pain = count_terms(text, PAIN_TERMS)
    intent = count_terms(text, INTENT_TERMS)
    community = count_terms(text, COMMUNITY_TERMS)
    promo = count_terms(text, PROMO_TERMS)

    if pain:
        score += pain * 4
        reasons.append(f"pain_terms={pain}")
    if intent:
        score += intent * 2
        reasons.append(f"intent_terms={intent}")
    if community:
        score += community
        reasons.append(f"community_terms={community}")
    if promo:
        score -= promo * 2
        reasons.append(f"promo_terms={promo}")

    source_type = record.get("source_type", "")
    if source_type == "cafearticle":
        score += 3
        reasons.append("cafearticle")
    elif source_type == "blog":
        score -= 1
        reasons.append("blog")

    rank = record.get("rank")
    if isinstance(rank, int):
        score += max(0, 4 - min(rank, 4))
        reasons.append(f"rank={rank}")

    domain = domain_of(str(record.get("url", "")))
    if "cafe.naver.com" in domain:
        score += 2
        reasons.append("naver_cafe")
    if "blog.naver.com" in domain:
        score -= 1
        reasons.append("naver_blog")

    return ScoredRecord(record, score, reasons)


def classify_topic(scored: list[ScoredRecord]) -> dict:
    valid = [item for item in scored if item.score > -100 and item.record.get("url")]
    top = sorted(valid, key=lambda item: item.score, reverse=True)[:20]
    urls = {item.record.get("url") for item in valid}
    source_counts = Counter(str(item.record.get("source_type", "")) for item in valid)
    domain_counts = Counter(domain_of(str(item.record.get("url", ""))) for item in valid)

    all_text = "\n".join(text_for(item.record) for item in valid)
    pain_hits = {term: all_text.count(term) for term in PAIN_TERMS if term in all_text}
    intent_hits = {term: all_text.count(term) for term in INTENT_TERMS if term in all_text}
    promo_hits = {term: all_text.count(term) for term in PROMO_TERMS if term in all_text}

    avg_top_score = round(sum(item.score for item in top[:10]) / max(1, len(top[:10])), 2)
    high_signal_count = sum(1 for item in valid if item.score >= 8)
    cafe_count = source_counts.get("cafearticle", 0)

    topic_score = avg_top_score + high_signal_count * 0.5 + cafe_count * 0.05 + len(urls) * 0.02
    promo_penalty = sum(promo_hits.values()) * 0.03
    topic_score = round(topic_score - promo_penalty, 2)

    return {
        "record_count": len(valid),
        "unique_url_count": len(urls),
        "source_counts": dict(source_counts),
        "top_domains": dict(domain_counts.most_common(10)),
        "pain_hits": pain_hits,
        "intent_hits": intent_hits,
        "promo_hits": promo_hits,
        "high_signal_count": high_signal_count,
        "avg_top_score": avg_top_score,
        "topic_score": topic_score,
        "top_records": [
            {
                "score": item.score,
                "reasons": item.reasons,
                "query": item.record.get("query", ""),
                "source_type": item.record.get("source_type", ""),
                "title": item.record.get("title", ""),
                "snippet": item.record.get("snippet", ""),
                "url": item.record.get("url", ""),
                "postdate": item.record.get("postdate", ""),
            }
            for item in top
        ],
    }


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_high_signal_markdown(path: Path, topic: str, analysis: dict) -> None:
    lines = [
        f"# High-Signal Sources: {topic}",
        "",
        f"- Topic score: `{analysis['topic_score']}`",
        f"- Records: `{analysis['record_count']}`",
        f"- Unique URLs: `{analysis['unique_url_count']}`",
        f"- High-signal count: `{analysis['high_signal_count']}`",
        "",
        "## Top Sources To Open And Capture",
        "",
    ]
    for idx, item in enumerate(analysis["top_records"][:15], start=1):
        lines.extend(
            [
                f"### {idx}. {item['title'] or '(untitled)'}",
                "",
                f"- Score: `{item['score']}`",
                f"- Source: `{item['source_type']}`",
                f"- Query: `{item['query']}`",
                f"- URL: {item['url']}",
                f"- Reasons: {', '.join(item['reasons'])}",
                f"- Snippet: {item['snippet']}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_ranking(path: Path, analyses: dict[str, dict]) -> None:
    ranked = sorted(analyses.items(), key=lambda item: item[1]["topic_score"], reverse=True)
    lines = [
        "# Korean Community Topic Ranking",
        "",
        "This is a heuristic ranking from Naver Blog/Cafe search results. It is not a final market decision.",
        "Use the high-signal source lists to open and capture primary evidence before committing to a landing theme.",
        "",
        "## Ranking",
        "",
        "| Rank | Topic | Score | Records | Unique URLs | High Signal | Top Pain Terms |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for idx, (topic, analysis) in enumerate(ranked, start=1):
        top_pain = ", ".join(
            f"{term}:{count}" for term, count in sorted(analysis["pain_hits"].items(), key=lambda x: x[1], reverse=True)[:5]
        )
        lines.append(
            f"| {idx} | `{topic}` | {analysis['topic_score']} | {analysis['record_count']} | "
            f"{analysis['unique_url_count']} | {analysis['high_signal_count']} | {top_pain} |"
        )

    lines.extend(["", "## First-Pass Interpretation", ""])
    winner = ranked[0][0] if ranked else ""
    lines.append(f"- Current heuristic winner: `{winner}`")
    lines.append("- Prioritize topics with repeated pain language and cafe/community results, not just high-volume promotional blog posts.")
    lines.append("- Open and CDP-capture the top 5 to 10 sources for the top 2 topics before deciding what to build.")
    lines.append("")
    lines.append("## Suggested Capture Command")
    lines.append("")
    lines.append("```powershell")
    lines.append(
        'python src\\cdp_capture_current_page.py --source korean-community --slug <topic> --url-regex "naver|threads|dcinside|clien|ppomppu|teamblind|tistory|blog"'
    )
    lines.append("```")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze Korean community research sources and rank launch topics.")
    parser.add_argument("--root", default=str(RESEARCH_ROOT), help="Research session root.")
    args = parser.parse_args()

    root = Path(args.root)
    topics_dir = root / "topics"
    analyses: dict[str, dict] = {}
    for topic_dir in sorted(path for path in topics_dir.iterdir() if path.is_dir()):
        records = load_jsonl(topic_dir / "sources.jsonl")
        scored = [score_record(record) for record in records]
        analysis = classify_topic(scored)
        analyses[topic_dir.name] = analysis
        write_json(topic_dir / "analysis.json", analysis)
        write_high_signal_markdown(topic_dir / "high-signal-sources.md", topic_dir.name, analysis)

    write_json(root / "topic-ranking.json", analyses)
    write_ranking(root / "topic-ranking.md", analyses)
    print(str(root / "topic-ranking.md"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
