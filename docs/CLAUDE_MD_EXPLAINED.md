# `CLAUDE.md`, line by line

[`CLAUDE.md`](../CLAUDE.md) is a file Claude Code reads at the start of every session in this
repository. It is a prompt, not documentation: everything in it is loaded into the agent's
context each time. That is why the explanations live here and not inside the file.

Three rules for editing it:

1. **Short.** Each line costs context on every session. If a line would not change the agent's
   behavior, delete it.
2. **Specific.** "Run `uv run pytest`" works. "Make sure the code is tested" does not.
3. **Earned.** Add a rule after the agent gets something wrong, not before.

Official reference: [Memory](https://code.claude.com/docs/en/memory)

## Project

| Line | Why it is there |
| --- | --- |
| `Narrative/RPG engine API: character sheets, world state, inventory, LLM narration.` | One sentence of orientation, so the agent does not have to infer the product from the code. |
| `FastAPI, PostgreSQL, Redis, Clean Architecture.` | Names the stack, so suggestions use these tools and not Flask or Django habits. |
| `The repository is safe-for-work.` | A content boundary for examples, fixtures and test data. |

## Current phase: 0

| Line | Why it is there |
| --- | --- |
| `Do not write feature code: no domain entities, use cases, endpoints or their tests.` | The core rule of phase 0. Without it, an agent's default is to implement whatever is asked. |
| `Review, explain and ask questions instead. Explain the concept first, then link the official docs.` | Says what to do instead, so the agent is useful as a reviewer and teacher. |
| `Scaffolding, CI and documentation edits are allowed when asked.` | Draws the line, so the agent does not refuse work that is fine. |

This section is the one that changes as the project moves through the phases in
[AGENTIC_ROADMAP.md](AGENTIC_ROADMAP.md).

## Commands

| Line | Why it is there |
| --- | --- |
| `Install: uv sync` | Stops the agent from reaching for `pip install`, which would bypass the lockfile. |
| `Run the API: uv run fastapi dev src/narrative_engine/api/main.py` | The exact path, because the `src/` layout makes it non-obvious. |
| `Tests: uv run pytest` | Gives the agent a check it can run to verify its own work. |
| `Lint: uv run ruff check .` | Same check CI runs, so problems surface before the push. |
| `Format: uv run ruff format .` | Keeps the agent from hand-formatting or adding another formatter. |
| `Services: docker compose up -d` | How to get PostgreSQL and Redis when a task needs them. |

Commands are the highest-value lines in the file: an agent that can run the checks can catch
its own mistakes.

## Architecture rules

| Line | Why it is there |
| --- | --- |
| `Dependencies point inward: api -> application -> domain. infrastructure implements application ports.` | The rule a tool cannot infer from an almost-empty codebase, and the easiest one to break. |
| `domain/ imports only the standard library.` | A concrete, checkable version of the rule for the most important layer. |
| `LLM providers are called only through a port. Tests never call a real provider.` | Protects the two things that cost money or break CI: real API calls in tests. |

## Conventions

| Line | Why it is there |
| --- | --- |
| `Conventional Commits. One small pull request per issue. Never push to main.` | Matches the workflow in `CONTRIBUTING.md` and the branch protection on `main`. |
| `Never commit secrets. Configuration comes from environment variables; .env.example lists them.` | A safety rule that must hold even when a task seems to need a key "just for now". |
| `English for code, comments, commits and docs.` | The repository targets international reviewers. |

## What is deliberately not in the file

- **Long explanations.** They belong in `docs/`. The agent can read them when a task needs them.
- **Things the code already says.** Folder listings and dependency lists go stale and waste context.
- **Style rules a tool enforces.** Ruff handles formatting and import order.
- **Secrets or personal paths.** This file is committed and public. Personal preferences
  belong in your own user-level Claude Code settings, not here.
