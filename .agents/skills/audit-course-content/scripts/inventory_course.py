#!/usr/bin/env python3
"""Inventory Markdown course Study Items and their linked resources.

This helper is intentionally offline. It validates course structure, parses links,
canonicalizes YouTube IDs, and reports local-link problems. It does not decide
whether a linked resource actually supports a learning claim.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import parse_qs, unquote, urlsplit


ITEM_RE = re.compile(r"^\s*(\d+)\.\s+\[\s*[xX ]?\s*\]\s+(.+?)\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
H3_RE = re.compile(r"^###\s+(.+?)\s*$")
OPTIONAL_TITLE_RE = re.compile(
    r"^(.*?)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))\s*$"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory Study Items and links in Markdown course files."
    )
    parser.add_argument("course_directory", type=Path)
    parser.add_argument(
        "--glob",
        default="step-*.md",
        help='Course file pattern (default: "step-*.md").',
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Search recursively instead of only in the course directory.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Output format (default: json).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with status 1 when structural or link issues are found.",
    )
    return parser.parse_args()


def markdown_links(text: str) -> Iterator[tuple[str, str]]:
    """Yield Markdown links while preserving balanced parentheses in targets."""

    index = 0
    while index < len(text):
        start = text.find("[", index)
        if start < 0:
            return
        if start > 0 and text[start - 1] == "!":
            index = start + 1
            continue

        label_end = text.find("]", start + 1)
        if label_end < 0 or label_end + 1 >= len(text) or text[label_end + 1] != "(":
            index = start + 1
            continue

        cursor = label_end + 2
        depth = 1
        quote: str | None = None
        while cursor < len(text):
            char = text[cursor]
            if char == "\\":
                cursor += 2
                continue
            if quote:
                if char == quote:
                    quote = None
            elif char in ('"', "'"):
                quote = char
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    label = text[start + 1 : label_end]
                    target = text[label_end + 2 : cursor]
                    yield label, normalize_target(target)
                    index = cursor + 1
                    break
            cursor += 1
        else:
            return


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    match = OPTIONAL_TITLE_RE.match(target)
    if match and match.group(1).strip():
        return match.group(1).strip()
    return target


def youtube_id(target: str) -> str | None:
    parsed = urlsplit(target)
    host = (parsed.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]

    if host == "youtu.be":
        return parsed.path.strip("/").split("/")[0] or None

    if host in {"youtube.com", "m.youtube.com", "music.youtube.com"}:
        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [None])[0]
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) >= 2 and parts[0] in {"embed", "live", "shorts"}:
            return parts[1]
    return None


def timestamp_seconds(target: str) -> int | None:
    parsed = urlsplit(target)
    values = parse_qs(parsed.query)
    raw = (values.get("t") or values.get("start") or [None])[0]
    if raw is None and parsed.fragment.startswith("t="):
        raw = parsed.fragment[2:]
    if not raw:
        return None

    raw = raw.strip().lower()
    if raw.isdigit():
        return int(raw)
    if ":" in raw:
        parts = raw.split(":")
        if all(part.isdigit() for part in parts) and len(parts) <= 3:
            total = 0
            for part in parts:
                total = total * 60 + int(part)
            return total

    match = re.fullmatch(
        r"(?:(?P<hours>\d+)h)?(?:(?P<minutes>\d+)m)?(?:(?P<seconds>\d+)s)?",
        raw,
    )
    if not match or not any(match.groupdict().values()):
        return None
    return (
        int(match.group("hours") or 0) * 3600
        + int(match.group("minutes") or 0) * 60
        + int(match.group("seconds") or 0)
    )


def extract_items(
    path: Path, course_directory: Path, issues: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        issues.append(
            {
                "code": "encoding_error",
                "file": str(path),
                "line": None,
                "message": str(exc),
            }
        )
        return []

    lines = text.splitlines()
    study_start = next(
        (index for index, line in enumerate(lines) if line.strip() == "## Study Items"),
        None,
    )
    relative = str(path.relative_to(course_directory))
    if study_start is None:
        issues.append(
            {
                "code": "missing_study_items_heading",
                "file": relative,
                "line": None,
                "message": "Missing exact '## Study Items' heading.",
            }
        )
        return []

    section_end = next(
        (
            index
            for index in range(study_start + 1, len(lines))
            if H2_RE.match(lines[index])
        ),
        len(lines),
    )
    if not any(line.strip() == "## Tasks" for line in lines[section_end:]):
        issues.append(
            {
                "code": "missing_tasks_heading",
                "file": relative,
                "line": None,
                "message": "No '## Tasks' heading follows Study Items.",
            }
        )

    items: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    track = "Uncategorized"
    track_counts: Counter[str] = Counter()

    def flush() -> None:
        nonlocal current
        if current is None:
            return
        current["text"] = " ".join(current.pop("parts")).strip()
        parsed_links = [
            {"label": label, "target": target}
            for label, target in markdown_links(current["text"])
        ]
        current["links"] = parsed_links
        candidate_links = len(
            re.findall(r"(?<!!)\[[^\]\n]+\]\(", current["text"])
        )
        if candidate_links != len(parsed_links):
            issues.append(
                {
                    "code": "possible_malformed_markdown_link",
                    "file": relative,
                    "line": current["line"],
                    "message": (
                        f"Found {candidate_links} link starts but parsed "
                        f"{len(parsed_links)} complete links."
                    ),
                }
            )
        if not parsed_links:
            issues.append(
                {
                    "code": "study_item_without_link",
                    "file": relative,
                    "line": current["line"],
                    "message": "Study Item contains no parsed Markdown link.",
                }
            )
        items.append(current)
        current = None

    for index in range(study_start + 1, section_end):
        line = lines[index]
        track_match = H3_RE.match(line)
        if track_match:
            flush()
            track = track_match.group(1).strip()
            continue

        item_match = ITEM_RE.match(line)
        if item_match:
            flush()
            track_counts[track] += 1
            current = {
                "file": relative,
                "line": index + 1,
                "number": int(item_match.group(1)),
                "track": track,
                "track_item": track_counts[track],
                "parts": [item_match.group(2)],
            }
            continue

        if current is not None and line.strip():
            current["parts"].append(line.strip())

    flush()
    if not items:
        issues.append(
            {
                "code": "empty_study_items",
                "file": relative,
                "line": study_start + 1,
                "message": "Study Items section contains no numbered checkbox items.",
            }
        )
    return items


def build_inventory(course_directory: Path, pattern: str, recursive: bool) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    iterator = course_directory.rglob(pattern) if recursive else course_directory.glob(pattern)
    files = sorted(path for path in iterator if path.is_file())
    if not files:
        raise ValueError(f"No files match {pattern!r} under {course_directory}")

    items: list[dict[str, Any]] = []
    file_rows: list[dict[str, Any]] = []
    for path in files:
        file_items = extract_items(path, course_directory, issues)
        items.extend(file_items)
        file_rows.append(
            {
                "file": str(path.relative_to(course_directory)),
                "study_items": len(file_items),
            }
        )

    link_occurrences: list[dict[str, Any]] = []
    external_targets: list[str] = []
    non_youtube_targets: list[str] = []
    youtube_ids: list[str] = []
    local_targets: list[str] = []
    canonical_resources: set[str] = set()
    timestamped_links: list[dict[str, Any]] = []

    for item in items:
        for link in item["links"]:
            target = link["target"]
            occurrence = {
                "file": item["file"],
                "line": item["line"],
                "track": item["track"],
                "track_item": item["track_item"],
                "label": link["label"],
                "target": target,
            }
            link_occurrences.append(occurrence)
            parsed = urlsplit(target)

            if parsed.scheme in {"http", "https"}:
                external_targets.append(target)
                if not parsed.netloc or any(char.isspace() for char in target):
                    issues.append(
                        {
                            "code": "invalid_external_uri",
                            "file": item["file"],
                            "line": item["line"],
                            "message": f"Absolute URI has no host: {target}",
                        }
                    )
                video_id = youtube_id(target)
                if video_id:
                    youtube_ids.append(video_id)
                    canonical_resources.add(f"youtube:{video_id}")
                    offset = timestamp_seconds(target)
                    if offset is not None:
                        timestamped_links.append({**occurrence, "offset_seconds": offset})
                else:
                    non_youtube_targets.append(target)
                    canonical_resources.add(target)
                continue

            if parsed.scheme:
                issues.append(
                    {
                        "code": "unsupported_link_scheme",
                        "file": item["file"],
                        "line": item["line"],
                        "message": f"Unsupported Study Item link scheme: {target}",
                    }
                )
                continue

            local_targets.append(target)
            path_part = unquote(target.split("#", 1)[0])
            if not path_part:
                continue
            owner = course_directory / item["file"]
            resolved = (owner.parent / path_part).resolve()
            canonical_resources.add(str(resolved))
            if not resolved.exists():
                issues.append(
                    {
                        "code": "missing_local_target",
                        "file": item["file"],
                        "line": item["line"],
                        "message": f"Missing local target: {target}",
                    }
                )

    occurrence_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for occurrence in link_occurrences:
        occurrence_groups[occurrence["target"]].append(
            {
                "file": occurrence["file"],
                "line": occurrence["line"],
                "track": occurrence["track"],
                "track_item": occurrence["track_item"],
            }
        )
    duplicates = [
        {"target": target, "count": len(locations), "locations": locations}
        for target, locations in sorted(occurrence_groups.items())
        if len(locations) > 1
    ]

    summary = {
        "files": len(files),
        "study_items": len(items),
        "link_occurrences": len(link_occurrences),
        "external_link_occurrences": len(external_targets),
        "unique_external_targets": len(set(external_targets)),
        "local_link_occurrences": len(local_targets),
        "youtube_link_occurrences": len(youtube_ids),
        "unique_youtube_video_ids": len(set(youtube_ids)),
        "timestamped_youtube_links": len(timestamped_links),
        "non_youtube_external_link_occurrences": len(non_youtube_targets),
        "unique_non_youtube_external_targets": len(set(non_youtube_targets)),
        "canonical_resources": len(canonical_resources),
        "exact_duplicate_target_groups": len(duplicates),
        "issues": len(issues),
    }
    return {
        "course_directory": str(course_directory),
        "glob": pattern,
        "summary": summary,
        "files": file_rows,
        "items": items,
        "timestamped_links": timestamped_links,
        "duplicate_targets": duplicates,
        "issues": issues,
    }


def markdown_report(inventory: dict[str, Any]) -> str:
    summary = inventory["summary"]
    lines = ["# Course Inventory", "", "| Metric | Count |", "|---|---:|"]
    for key, value in summary.items():
        lines.append(f"| {key.replace('_', ' ').title()} | {value} |")

    lines.extend(["", "## Files", "", "| File | Study Items |", "|---|---:|"])
    for row in inventory["files"]:
        lines.append(f"| `{row['file']}` | {row['study_items']} |")

    lines.extend(["", "## Issues", ""])
    if inventory["issues"]:
        for issue in inventory["issues"]:
            location = issue["file"]
            if issue.get("line"):
                location += f":{issue['line']}"
            lines.append(f"- `{issue['code']}` at `{location}`: {issue['message']}")
    else:
        lines.append("None.")

    lines.extend(["", "## Exact Duplicate Targets", ""])
    if inventory["duplicate_targets"]:
        for duplicate in inventory["duplicate_targets"]:
            lines.append(f"- {duplicate['count']} occurrences: `{duplicate['target']}`")
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    course_directory = args.course_directory.resolve()
    if not course_directory.is_dir():
        print(f"error: not a directory: {course_directory}", file=sys.stderr)
        return 2

    try:
        inventory = build_inventory(course_directory, args.glob, args.recursive)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(inventory, indent=2, ensure_ascii=False))
    else:
        print(markdown_report(inventory), end="")
    return 1 if args.strict and inventory["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
