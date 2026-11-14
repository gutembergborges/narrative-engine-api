# CLAUDE.md

## Project

Narrative/RPG engine API: character sheets, world state, inventory, LLM narration.
FastAPI, PostgreSQL, Redis, Clean Architecture. The repository is safe-for-work.

## Current phase: 0 (the owner writes the code by hand)

- Do not write feature code: no domain entities, use cases, endpoints or their tests.
- Review, explain and ask questions instead. Explain the concept first, then link the official docs.
- Scaffolding, CI and documentation edits are allowed when asked.

## Commands

- Install: `uv sync`
- Run the API: `uv run fastapi dev src/narrative_engine/api/main.py`
- Tests: `uv run pytest`
- Lint: `uv run ruff check .`
- Format: `uv run ruff format .`
- Services: `docker compose up -d`

## Architecture rules

- Dependencies point inward: `api` -> `application` -> `domain`. `infrastructure` implements `application` ports.
- `domain/` imports only the standard library.
- LLM providers are called only through a port. Tests never call a real provider.

## Conventions

- Conventional Commits. One small pull request per issue. Never push to `main`.
- Never commit secrets. Configuration comes from environment variables; `.env.example` lists them.
- English for code, comments, commits and docs.
