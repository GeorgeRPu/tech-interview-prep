# Agent Instructions

@README.md

- After making code changes, check if `AGENTS.md` or `README.md` needs to be updated to reflect the new project state (e.g. new files, changed tools, updated commands)

## Before Implementing Features

Always check `ROADMAP.md` before implementing any new features. Use it to align your implementation with the project's direction and avoid duplicating or conflicting with planned work.

When a task from the roadmap is complete, update `ROADMAP.md` to reflect the new status.

## Solution Explanations

Never author the `explanation` or `complexity` fields in `meta.yaml`. These are written by the user. When adding a new solution or problem, leave those fields empty or omit them entirely and let the user fill them in.

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short summary>

- Bullet point describing one change
- Bullet point describing another change
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `build`, `chore`, `test`

**Scope:** optional, name of the affected area (e.g. `docs`, `scripts`, `solutions`)

**Rules:**
- Summary line is lowercase, no trailing period, under 72 characters
- Use bullet points for the body when there are multiple changes
- Do not add `Co-Authored-By` attribution
