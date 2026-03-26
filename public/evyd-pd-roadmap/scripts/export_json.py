#!/usr/bin/env python3
import json
import sys
from pathlib import Path

SEPARATORS = ["|", ",", ";", "/"]


def split_collaborators(value):
    if value is None:
        return []
    s = str(value).strip()
    if not s or s == "-":
        return []
    parts = [s]
    for sep in SEPARATORS:
        next_parts = []
        for p in parts:
            next_parts.extend(p.split(sep))
        parts = next_parts
    cleaned = []
    seen = set()
    for p in parts:
        item = p.strip()
        if item and item != "-" and item not in seen:
            seen.add(item)
            cleaned.append(item)
    return cleaned


def get_field(fields, *names):
    for name in names:
        if name in fields:
            return fields.get(name)
    return None


def is_empty_record(fields):
    keys = [
        "Name", "Module", "Problem", "Function", "Description", "Value", "Resource", "startMonth",
        "author", "module", "problem", "title", "description", "outcome", "collaborators"
    ]
    for k in keys:
        v = fields.get(k)
        if v not in (None, "", [], {}):
            return False
    return True


def to_int(value, default=None):
    if value in (None, ""):
        return default
    try:
        return int(str(value).strip())
    except Exception:
        return default


def normalize_record(record, default_duration=3):
    fields = record.get("fields", {})
    if is_empty_record(fields):
        return None

    module = get_field(fields, "Module", "module")
    title = get_field(fields, "Function", "title")
    problem = get_field(fields, "Problem", "problem")
    description = get_field(fields, "Description", "description")
    outcome = get_field(fields, "Value", "outcome")
    collaborators = get_field(fields, "Resource", "collaborators")
    author = get_field(fields, "Name", "author")
    start_month = get_field(fields, "startMonth")

    if not any([module, title, problem, description, outcome, author, start_month]):
        return None

    return {
        "module": module,
        "title": title,
        "problem": problem,
        "description": description,
        "outcome": outcome,
        "collaborators": split_collaborators(collaborators),
        "author": author,
        "startMonth": to_int(start_month),
        "duration": default_duration,
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: export_json.py <input-records.json> <output.json> [year] [duration]", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    year = int(sys.argv[3]) if len(sys.argv) >= 4 else 2026
    duration = int(sys.argv[4]) if len(sys.argv) >= 5 else 3

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(2)
    data = json.loads(input_path.read_text())
    records = data.get("records", data)
    items = []
    for record in records:
        normalized = normalize_record(record, default_duration=duration)
        if normalized:
            items.append(normalized)

    payload = {
        "year": year,
        "items": items,
    }
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"Wrote {len(items)} items to {output_path}")


if __name__ == "__main__":
    main()
