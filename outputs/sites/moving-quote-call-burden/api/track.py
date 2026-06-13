from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler
from typing import Final
from urllib.parse import parse_qs, urlparse

MAX_BODY_BYTES: Final[int] = 8192
MAX_TEXT_LENGTH: Final[int] = 180
ALLOWED_EVENTS: Final[frozenset[str]] = frozenset(
    {
        "page_view",
        "selector_choice",
        "diagnosis_completed",
        "diagnosis_ready_cta_clicked",
        "diagnosis_prepare_cta_clicked",
        "checklist_toggled",
        "outbound_cta_clicked",
    }
)
ALLOWED_PAYLOAD_KEYS: Final[frozenset[str]] = frozenset(
    {
        "href",
        "path",
        "referrer",
        "result",
        "date",
        "contact",
        "address",
        "inventory",
        "group",
        "value",
        "item",
        "checked",
        "cta_position",
    }
)
ALLOWED_UTM_KEYS: Final[frozenset[str]] = frozenset(
    {"utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"}
)


def _short_text(value: str) -> str:
    return value[:MAX_TEXT_LENGTH]


def _safe_text(value: object) -> str:
    if isinstance(value, str):
        return _short_text(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float):
        return _short_text(str(value))
    return ""


def _safe_map(value: object, allowed_keys: frozenset[str]) -> dict[str, str]:
    if not isinstance(value, dict):
        return {}

    result: dict[str, str] = {}
    for key in allowed_keys:
        if key in value:
            result[key] = _safe_text(value[key])
    return result


def _first_query_values(path: str) -> dict[str, str]:
    parsed = urlparse(path)
    values = parse_qs(parsed.query, keep_blank_values=False)
    result: dict[str, str] = {}
    for key in ALLOWED_UTM_KEYS:
        candidates = values.get(key, [])
        if candidates:
            result[key] = _short_text(candidates[0])
    return result


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self) -> None:
        self._send_json(204, {})

    def do_GET(self) -> None:
        self._send_json(200, {"ok": True, "service": "leadgen-track"})

    def do_POST(self) -> None:
        event = self._read_event()
        if event == {}:
            self._send_json(400, {"ok": False})
            return

        print(json.dumps(event, ensure_ascii=False, separators=(",", ":")), flush=True)
        self._send_json(202, {"ok": True})

    def _read_event(self) -> dict[str, str | dict[str, str]]:
        raw_length = self.headers.get("content-length", "0")
        try:
            content_length = min(int(raw_length), MAX_BODY_BYTES)
        except ValueError:
            return {}

        raw_body = self.rfile.read(content_length)
        try:
            decoded = json.loads(raw_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return {}

        if not isinstance(decoded, dict):
            return {}

        event_name = _safe_text(decoded.get("event"))
        if event_name not in ALLOWED_EVENTS:
            return {}

        payload = _safe_map(decoded.get("payload"), ALLOWED_PAYLOAD_KEYS)
        utm = _safe_map(decoded.get("utm"), ALLOWED_UTM_KEYS)
        query_utm = _first_query_values(self.path)
        for key, value in query_utm.items():
            utm.setdefault(key, value)

        return {
            "type": "leadgen_event",
            "event": event_name,
            "campaign": _safe_text(decoded.get("campaign")) or "moving_quote_call_burden",
            "session_id": _safe_text(decoded.get("session_id")),
            "ts": _safe_text(decoded.get("ts")),
            "path": _safe_text(decoded.get("path")),
            "utm": utm,
            "payload": payload,
        }

    def _send_json(self, status_code: int, body: dict[str, str | bool]) -> None:
        encoded = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("cache-control", "no-store")
        self.send_header("access-control-allow-origin", "*")
        self.send_header("access-control-allow-methods", "GET,POST,OPTIONS")
        self.send_header("access-control-allow-headers", "content-type")
        self.send_header("content-length", str(len(encoded)))
        self.end_headers()
        if status_code != 204:
            self.wfile.write(encoded)
