## What

<!-- One or two sentences: what does this pull request change? -->

Closes #

## Why

<!-- The reason for the change. Link the issue, ADR or doc that explains it. -->

## How to test

<!-- The exact commands or steps a reviewer can run. -->

```bash
uv run pytest
```

## Checklist

- [ ] The title follows Conventional Commits (for example `feat: add narrative endpoint`)
- [ ] `uv run ruff check .` and `uv run ruff format --check .` pass
- [ ] `uv run pytest` passes
- [ ] New behavior has a test
- [ ] Docs or ADR updated if a decision changed
- [ ] No secrets, tokens or `.env` in the diff
- [ ] I can explain every line of this change out loud, in English
