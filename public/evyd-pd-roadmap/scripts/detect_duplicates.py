#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with",
    "ai", "system", "platform", "capability", "feature"
}


def normalize_text(text):
    if text is None:
        return ""
    s = str(text).lower().strip()
    s = re.sub(r"[^\w\s\u4e00-\u9fff]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def tokenize(text):
    s = normalize_text(text)
    return [t for t in s.split() if t and t not in STOPWORDS]


def similarity(a, b):
    return SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()


def overlap_score(a_tokens, b_tokens):
    if not a_tokens or not b_tokens:
        return 0.0
    a = set(a_tokens)
    b = set(b_tokens)
    return len(a & b) / max(1, min(len(a), len(b)))


def get_field(fields, *names):
    for name in names:
        if name in fields:
            return fields.get(name)
    return None


def is_empty_record(fields):
    for key in ["Function", "Problem", "Description", "Module", "title", "problem", "description", "module"]:
        if fields.get(key) not in (None, ""):
            return False
    return True


def likely_duplicate(a, b):
    af = a.get("fields", {})
    bf = b.get("fields", {})

    a_func = get_field(af, "Function", "title") or ""
    b_func = get_field(bf, "Function", "title") or ""
    a_problem = get_field(af, "Problem", "problem") or ""
    b_problem = get_field(bf, "Problem", "problem") or ""
    a_desc = get_field(af, "Description", "description") or ""
    b_desc = get_field(bf, "Description", "description") or ""
    a_module = get_field(af, "Module", "module") or ""
    b_module = get_field(bf, "Module", "module") or ""

    func_sim = similarity(a_func, b_func)
    problem_sim = similarity(a_problem, b_problem)
    desc_sim = similarity(a_desc, b_desc)
    token_overlap = overlap_score(tokenize(a_desc + " " + a_problem), tokenize(b_desc + " " + b_problem))
    same_module = normalize_text(a_module) == normalize_text(b_module) and a_module != ""

    reasons = []
    score = 0

    if func_sim >= 0.72:
        score += 2
        reasons.append("similar function/title")
    if problem_sim >= 0.72:
        score += 2
        reasons.append("similar problem")
    if desc_sim >= 0.72:
        score += 2
        reasons.append("similar description intent")
    if token_overlap >= 0.5:
        score += 1
        reasons.append("high keyword overlap")
    if same_module and (func_sim >= 0.55 or problem_sim >= 0.55 or desc_sim >= 0.55):
        score += 1
        reasons.append("same module with overlapping intent")

    return score >= 3, reasons


def main():
    if len(sys.argv) < 2:
        print("Usage: detect_duplicates.py <input-records.json> [output.json]", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else None
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(2)
    data = json.loads(input_path.read_text())
    records = data.get("records", data)
    records = [r for r in records if not is_empty_record(r.get("fields", {}))]

    groups = []
    seen_pairs = set()
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            a = records[i]
            b = records[j]
            dup, reasons = likely_duplicate(a, b)
            if not dup:
                continue
            pair = (a.get("record_id") or a.get("id"), b.get("record_id") or b.get("id"))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            groups.append({
                "recordA": pair[0],
                "recordB": pair[1],
                "moduleA": get_field(a.get("fields", {}), "Module", "module"),
                "moduleB": get_field(b.get("fields", {}), "Module", "module"),
                "titleA": get_field(a.get("fields", {}), "Function", "title"),
                "titleB": get_field(b.get("fields", {}), "Function", "title"),
                "reasons": reasons,
            })

    result = {"duplicates": groups, "count": len(groups)}
    if output_path:
        output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print(f"Wrote {len(groups)} duplicate groups to {output_path}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
