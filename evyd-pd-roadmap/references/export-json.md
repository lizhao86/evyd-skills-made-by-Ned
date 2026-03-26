# JSON Export

Use this module when the user wants the roadmap exported into a fixed JSON payload for another roadmap system.

## Current supported export

### JSON export schema

```json
{
  "year": 2026,
  "items": [
    {
      "module": "Routines",
      "title": "Reusable health plan system",
      "problem": "Routine capabilities are too tightly coupled to specific scenarios and cannot be reused across broader health management journeys.",
      "description": "Turn Routine capabilities into a reusable health plan system that can support broader health and disease-management scenarios.",
      "outcome": "Create a reusable health plan foundation that supports faster rollout across more health programs.",
      "collaborators": ["Medical"],
      "author": "lmh",
      "startMonth": 5,
      "duration": 3
    }
  ]
}
```

## Mapping

- `Module` -> `module`
- `Function` -> `title`
- `Problem` -> `problem`
- `Description` -> `description`
- `Value` -> `outcome`
- `Resource` -> `collaborators`
- `Name` -> `author`
- `startMonth` -> `startMonth`
- `duration` -> default `3`

## Rules

- Ignore empty rows
- Ignore actual KPI fabrication
- Use cleaned Bitable content as-is where possible
- Convert collaborators from separator form into arrays
- `-` or empty collaborators -> `[]`
- Default `duration = 3` unless user overrides

## Delivery order

Preferred delivery sequence:
1. Write local JSON file
2. If cloud upload works, upload there
3. If cloud upload fails, send as chat attachment

## Naming

Suggested local filename:
- `roadmap_export_<year>.json`
