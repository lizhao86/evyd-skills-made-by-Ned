# Duplicate Check

Use this module when the user wants to inspect roadmap rows for duplicates or near-duplicates.

## Goal

Detect likely duplicate roadmap items and ask the user to decide whether to:
- keep both
- update the original
- merge conceptually and replace one

## What counts as a duplicate

A duplicate is any row where at least one of these is substantially overlapping:
- same `Function`
- same `Problem`
- same `Description` intent
- same module + same outcome direction

Duplicates do not need to be exact text matches.
Near-duplicates are often more important than exact duplicates.

## Detection heuristics

Check for overlap by:
1. same or very similar `Function`
2. same `Module` plus similar `Problem`
3. same solution intent phrased differently
4. one row being a narrower restatement of another

## Review workflow

1. Read all non-empty rows.
2. Group likely duplicates.
3. Present them in a compact comparison.
4. Do not delete or overwrite automatically.
5. Ask the user to choose one of:
   - keep both
   - update original
   - merge into original

## Recommended output format

For each duplicate group, show:
- record ids
- module
- function/title
- short reason why they look duplicated

Example:
- `recA` vs `recB`
- Module: Routines
- Likely duplicate reason: both describe reusable logging across modules
- Decision needed: keep both / update original / merge

## Safety rule

Never silently remove a row.
Never silently overwrite an original row unless the user explicitly approved the update.
