# ADR 0001: Stack and architecture style

- **Status:** Accepted
- **Date:** 2026-11-14
- **Deciders:** Gutemberg Borges

An Architecture Decision Record (ADR) captures one decision that is expensive to reverse: the
context, what was decided, what else was considered, and what follows from it. Background:
<https://adr.github.io/>

## Context

The project is a narrative/RPG engine exposed as an HTTP API. It manages character sheets,
world state and inventory, and calls a language model to generate narration.

It has two purposes, and both shape the decision:

1. A portfolio project for international remote Senior Software Engineer roles. It must show
   API design, architecture, testing, CI/CD, Docker and applied AI in a reviewable form.
2. A learning project. The author is strong in PHP/Laravel and Vue/Quasar, intermediate in
   Python, and wants to understand every line before AI agents are added.

Constraints:

- One developer, short focus blocks. Small moving parts beat clever ones.
- The development laptop has 8 GB of RAM, so the local stack must stay light.
- The LLM provider is undecided and may become a local model later.

## Decision

Build a **modular monolith in Clean Architecture** with this stack:

| Concern | Choice | Role |
| --- | --- | --- |
| Language | Python 3.14 | Main language of the applied-AI ecosystem |
| Web framework | FastAPI | HTTP layer, validation and OpenAPI docs from type hints |
| Validation | Pydantic v2 | Request/response schemas and settings |
| Server | Uvicorn | ASGI server (comes with `fastapi[standard]`) |
| Database | PostgreSQL 18 | System of record |
| Data access | SQLAlchemy 2.x + Alembic + psycopg 3 | ORM (Data Mapper), migrations, driver |
| Cache | Redis 8 | LLM response cache and rate limiting, when a milestone needs them |
| Local services | Docker Compose | One command to start PostgreSQL and Redis |
| Dependencies | uv | Virtual environment, lockfile, Python installation |
| Lint and format | Ruff | One fast tool for both |
| Tests | Pytest + FastAPI `TestClient` (HTTPX) | Unit, integration and API tests |
| CI | GitHub Actions | Lint, format check and tests on every pull request |
| Work tracking | GitHub Issues + Projects | Milestones and small issues |

Architecture rules:

- Four layers: `domain`, `application`, `infrastructure`, `api`. Dependencies point inward.
- The LLM sits behind a port (an interface defined in `application`). Tests use a fake adapter.
- Configuration comes from environment variables.

Deliberately **not** included now:

- **Message broker.** Nothing needs background jobs yet. It is added when a milestone does.
- **Type checker.** Joins in Milestone 3, after there is enough code to make it worthwhile.
- **Front end.** React + Vite + TypeScript in its own repository, in Milestone 5.
- **SQLAlchemy, Alembic, psycopg, redis-py as dependencies.** They are decided here but added
  with `uv add` by the issue that first uses them, so `pyproject.toml` lists only what the
  code really imports.

## Versions checked on 2026-11-14

Source: the release tags of each project's official repository, plus the Docker Official Image
pages for PostgreSQL and Redis.

| Tool | Latest release seen | Used here |
| --- | --- | --- |
| Python | 3.15.2 (3.14 line: 3.14.10) | 3.14 |
| FastAPI | 0.163.0 | `>=0.163.0,<0.164.0` |
| Uvicorn | 0.54.0 | via `fastapi[standard]` |
| Pydantic | 2.14.3 | via FastAPI |
| Pytest | 9.2.0 | `>=9.2.0` |
| HTTPX | 0.28.1 | `>=0.28.1` |
| Ruff | 0.17.5 | `>=0.17.5` |
| uv | 0.13.8 | build backend `>=0.13.8,<0.14.0` |
| PostgreSQL | 18.7 (19 is at release candidate 2) | image `postgres:18-alpine` |
| Redis | 8.10.3 | image `redis:8-alpine` |
| SQLAlchemy | 2.1.8 | added in Milestone 2 |
| Alembic | 1.20.1 | added in Milestone 2 |
| psycopg | 3.3.9 | added in Milestone 2 |
| pydantic-settings | 2.16.3 | added in Milestone 1 |
| redis-py | 8.1.0 | added when Redis is first used |
| `actions/checkout` | v7.0.1 | `@v7` |
| `astral-sh/setup-uv` | v10.3.3 | `@v10.3.3` |

Why not the newest Python and PostgreSQL: Python 3.15.0 was released in October 2026 and
PostgreSQL 19 is not final yet. A portfolio project gains nothing from first-month releases
and can lose time to missing wheels or image changes. Revisit both in early 2027.

## Options considered

### Framework

| Option | For | Against | Verdict |
| --- | --- | --- | --- |
| **FastAPI** | Type-hint driven, OpenAPI for free, async, small surface, strong in AI back ends | Fewer batteries than Django; architecture is your job | **Chosen**: the missing batteries are exactly what this project is meant to teach |
| Django + DRF | Batteries included, mature ORM and admin | Active Record ORM couples rules to the framework, which fights Clean Architecture | Rejected for this project |
| NestJS (Node.js) | Opinionated structure, TypeScript | Moves away from Python, where the LLM tooling is richest | Rejected |
| Laravel | The author's strongest stack | Shows nothing new; weaker fit for LLM libraries | Rejected |

### Architecture style

| Option | Verdict |
| --- | --- |
| **Modular monolith, Clean Architecture** | **Chosen**: one deployable, clear boundaries, testable rules |
| Layered MVC around the ORM | Rejected: fast to start, but rules end up inside models and routes |
| Microservices | Rejected: operational cost with no benefit for one developer |

### Data access

SQLAlchemy 2.x is a Data Mapper: entities can be plain Python objects and the mapping lives in
the infrastructure layer. That is the property that keeps `domain` free of framework imports.
psycopg 3 serves both the application and Alembic, so there is one driver to learn.

### Dependency tool

uv replaces pip, venv, pip-tools and pyenv with one tool and one lockfile. The alternative,
Poetry, is mature but slower and does not install Python itself.

## Consequences

Good:

- Business rules can be unit-tested without a database, a web server or an LLM.
- The LLM provider can change (hosted, local, fake) by writing one adapter.
- The repository demonstrates the skills listed in the context, each in a visible place.

Costs:

- More files and indirection than a simple FastAPI app. For a pure CRUD service this would be
  over-engineering; here the indirection is part of what is being practiced.
- FastAPI is 0.x, so minor upgrades are deliberate: read the release notes, bump the pin, run
  the tests.
- The layer rules are enforced by discipline and review for now. An import linter can enforce
  them automatically later.

## Open decisions

| Decision | When | Where it will be recorded |
| --- | --- | --- |
| First LLM provider (hosted API or local model) | Milestone 1 | ADR 0002 |
| Database schema for characters, world state, inventory | Milestone 2 | ADR 0003 |
| Message broker, if any | When a milestone needs background work | New ADR |
| Front-end framework details | Milestone 5 | New ADR |
