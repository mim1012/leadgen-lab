from __future__ import annotations

import json
import re
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


CDP_URL = "http://127.0.0.1:9222"
TARGET_RE = re.compile(r"cafe\.naver\.com/vibemoney/3|cafe\.naver\.com/ArticleRead", re.I)
ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "evidence"


def safe_name(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z가-힣._-]+", "-", value).strip("-")
    return value[:80] or "page"


def frame_snapshot(frame) -> dict:
    text = ""
    html = ""
    links: list[dict] = []
    images: list[dict] = []
    controls: list[dict] = []
    meta: dict = {}
    try:
        text = frame.locator("body").inner_text(timeout=3000)
    except Exception:
        pass
    try:
        html = frame.content()
    except Exception:
        pass
    try:
        links = frame.eval_on_selector_all(
            "a[href]",
            """els => els.slice(0, 500).map(a => ({
                text: (a.innerText || a.textContent || '').trim(),
                href: a.href,
                title: a.title || ''
            }))""",
        )
    except Exception:
        pass
    try:
        images = frame.eval_on_selector_all(
            "img[src]",
            """els => els.slice(0, 300).map(img => ({
                alt: img.alt || '',
                src: img.currentSrc || img.src,
                width: img.naturalWidth || img.width || 0,
                height: img.naturalHeight || img.height || 0
            }))""",
        )
    except Exception:
        pass
    try:
        controls = frame.eval_on_selector_all(
            "input, textarea, select, button",
            """els => els.slice(0, 300).map((el, i) => ({
                index: i,
                tag: el.tagName.toLowerCase(),
                type: el.getAttribute('type') || '',
                name: el.getAttribute('name') || '',
                id: el.id || '',
                aria: el.getAttribute('aria-label') || '',
                text: (el.innerText || el.value || el.placeholder || '').trim(),
                disabled: !!el.disabled
            }))""",
        )
    except Exception:
        pass
    try:
        meta = frame.evaluate(
            """() => ({
                title: document.title || '',
                canonical: document.querySelector('link[rel=canonical]')?.href || '',
                h1: [...document.querySelectorAll('h1')].map(e => e.innerText.trim()),
                h2: [...document.querySelectorAll('h2')].map(e => e.innerText.trim()).slice(0, 20),
                articleText: document.querySelector('article')?.innerText || '',
                ogTitle: document.querySelector('meta[property="og:title"]')?.content || '',
                ogDescription: document.querySelector('meta[property="og:description"]')?.content || ''
            })"""
        )
    except Exception:
        pass
    return {
        "url": frame.url,
        "name": frame.name,
        "text": text,
        "text_length": len(text),
        "html": html,
        "html_length": len(html),
        "links": links,
        "images": images,
        "controls": controls,
        "meta": meta,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture the currently open browser page through Chrome CDP without interacting with the page."
    )
    parser.add_argument("--cdp-url", default=CDP_URL, help="Chrome CDP URL. Default: http://127.0.0.1:9222")
    parser.add_argument("--source", default="naver-cafe", help="Evidence source directory name.")
    parser.add_argument("--slug", default="capture", help="Human-readable evidence slug.")
    parser.add_argument(
        "--url-regex",
        default=TARGET_RE.pattern,
        help="Regex used to choose the target tab/frame URL.",
    )
    parser.add_argument(
        "--out-root",
        default=str(OUT_ROOT),
        help="Evidence root directory. Default: project evidence/.",
    )
    return parser.parse_args()


def find_target_page(pages, target_re: re.Pattern):
    for page in pages:
        if target_re.search(page.url):
            return page
    for page in pages:
        parsed = urlparse(page.url)
        if parsed.netloc:
            return page
    return None


def main() -> int:
    args = parse_args()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target_re = re.compile(args.url_regex, re.I)
    out_dir = Path(args.out_root) / safe_name(args.source) / f"{safe_name(args.slug)}-{stamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(args.cdp_url)
        contexts = browser.contexts
        pages = [page for ctx in contexts for page in ctx.pages]
        target = find_target_page(pages, target_re)
        if target is None:
            raise RuntimeError(f"No browser tab matched --url-regex: {args.url_regex}")

        target.bring_to_front()
        target.wait_for_load_state("domcontentloaded", timeout=10_000)
        target.wait_for_timeout(1500)
        screenshot_path = out_dir / "screenshot.png"
        target.screenshot(path=str(screenshot_path), full_page=True)

        snapshots = [frame_snapshot(frame) for frame in target.frames]
        best = max(snapshots, key=lambda item: item["text_length"], default={})
        summary = {
            "captured_at": stamp,
            "source": args.source,
            "slug": args.slug,
            "page_url": target.url,
            "page_title": target.title(),
            "frame_count": len(target.frames),
            "best_frame_url": best.get("url", ""),
            "best_frame_name": best.get("name", ""),
            "screenshot": str(screenshot_path),
            "frames": [
                {
                    "url": item["url"],
                    "name": item["name"],
                    "text_length": item["text_length"],
                    "html_length": item["html_length"],
                    "link_count": len(item["links"]),
                    "image_count": len(item["images"]),
                    "control_count": len(item["controls"]),
                    "meta": item["meta"],
                }
                for item in snapshots
            ],
        }

        (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        (out_dir / "frames.json").write_text(json.dumps(snapshots, ensure_ascii=False, indent=2), encoding="utf-8")
        (out_dir / "visible_text.txt").write_text(
            "\n\n".join(
                f"===== FRAME {idx} {item['name']} {item['url']} =====\n{item['text']}"
                for idx, item in enumerate(snapshots)
            ),
            encoding="utf-8",
        )
        for idx, item in enumerate(snapshots):
            name = safe_name(item["name"] or f"frame-{idx}")
            (out_dir / f"{idx:02d}-{name}.html").write_text(item["html"], encoding="utf-8")

        print(str(out_dir))
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
