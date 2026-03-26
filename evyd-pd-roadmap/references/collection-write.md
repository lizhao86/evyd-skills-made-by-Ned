# Collection + Write

Use this module when the user wants to brainstorm roadmap items from conversation and write them into a Feishu Bitable.

## Goal

Turn conversational product ideas into structured roadmap rows.

## Required precondition

The user must specify the target Bitable first.
Do not guess which Bitable to write into.

Minimum required input from user:
- a Feishu Bitable URL
- optionally the target table/view if multiple exist

## Collection workflow

1. Ask for the target Bitable if missing.
2. Read Bitable metadata and fields.
3. Confirm target schema if fields are unclear.
4. Let the user describe their scenario, problem, idea, or module.
5. Expand the scenario into one or more roadmap rows.
6. Write rows into the Bitable.

## Expansion rules

When the user gives a scenario, expand it into structured rows using these fields:
- `Module`
- `Problem`
- `Function`
- `Description`
- `Value`
- `Resource`
- optionally `startMonth`

### Expansion heuristics

- Split one broad scenario into multiple rows if it contains clearly separable capabilities.
- Prefer atomic roadmap rows over giant bundled entries.
- Keep `Function` as a single feature label.
- Keep `Description` richer than `Function`.
- Keep `Problem` problem-first.
- Keep `Value` concise.
- Keep `Resource` limited to deep-collaboration teams.

## Write behavior

Before creating records:
1. Read nearby existing rows when practical.
2. Avoid blindly creating duplicates.
3. If a likely duplicate exists, switch to duplicate-check workflow instead of immediate write.

## Recommended question flow

If the user gives an idea but not enough structure, ask only what is necessary:
1. Which Bitable should I write into?
2. Which module does this belong to?
3. Is this one roadmap item or several?
4. Do you want me to draft Problem / Function / Value / Resource for you?

## Output quality bar

- Do not write into an unspecified Bitable.
- Do not create duplicate rows silently.
- Prefer fewer, cleaner rows.
- Keep language consistent with the user’s planning language unless export requires normalization.
