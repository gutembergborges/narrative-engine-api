# Learning path

What each milestone teaches, where the official documentation is, and how to know it has
landed. Every milestone ends with the same check: **explain it out loud, in English, without
notes.** That is also interview practice.

All links point to official sites and were written on 2026-11-14. The Claude Code links were
opened and confirmed that day; the others were not opened one by one. Documentation moves: if
a link is dead, search the same site for the page title, then fix the link in a small
`docs:` pull request.

## M0 · Bootstrap

You learn how a modern Python project is put together and how its services run in Docker.

| Topic | What to understand | Official docs |
| --- | --- | --- |
| uv | Virtual environment, `pyproject.toml`, lockfile, `uv sync`, `uv run`, `uv add` | [Working on projects](https://docs.astral.sh/uv/guides/projects/) |
| Project layout | Why `src/` layout, what a build backend does | [Project configuration](https://docs.astral.sh/uv/concepts/projects/config/) |
| FastAPI basics | App object, path operation, automatic docs | [Tutorial: first steps](https://fastapi.tiangolo.com/tutorial/first-steps/) |
| Pytest | Test discovery, plain `assert`, reading a failure | [Get started](https://docs.pytest.org/en/stable/getting-started.html) |
| Testing FastAPI | `TestClient`, testing without a running server | [Testing](https://fastapi.tiangolo.com/tutorial/testing/) |
| Ruff | Linter versus formatter, rule selection | [Ruff docs](https://docs.astral.sh/ruff/) |
| Docker concepts | Image, container, volume, port, network | [Docker overview](https://docs.docker.com/get-started/docker-overview/) |
| Docker Compose | Services, environment interpolation, named volumes, healthchecks | [Compose file reference](https://docs.docker.com/reference/compose-file/) |
| GitHub Actions | Workflow, job, step, trigger, permissions | [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions) |
| Conventional Commits | Types, scope, breaking changes | [Specification](https://www.conventionalcommits.org/en/v1.0.0/) |
| Branch protection | Rulesets, required checks | [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) |

You have it when you can:

- Explain what happens, step by step, between `uv sync` and a green `uv run pytest`.
- Explain every block of `docker-compose.yml`, and what `docker compose down -v` deletes.
- Break the health test on purpose, read the failure, and fix it.

## M1 · First narrative endpoint

You learn test-first development, ports and adapters, and how to call an LLM safely.

| Topic | What to understand | Official docs |
| --- | --- | --- |
| Dockerfile | Layers, build cache, multi-stage builds, non-root user | [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) |
| uv in Docker | Installing dependencies in an image, caching | [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/) |
| FastAPI in containers | How the app is served in an image | [FastAPI in containers](https://fastapi.tiangolo.com/deployment/docker/) |
| Settings | Typed configuration from environment variables | [Settings and environment variables](https://fastapi.tiangolo.com/advanced/settings/) · [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| Protocols | Structural typing, defining a port | [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol) |
| Dependency injection | `Depends`, overriding dependencies in tests | [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) · [Testing with overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/) |
| Request and response models | Pydantic schemas, validation errors | [Request body](https://fastapi.tiangolo.com/tutorial/body/) · [Response model](https://fastapi.tiangolo.com/tutorial/response-model/) |
| Error handling | Turning failures into clean HTTP errors | [Handling errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) |
| App structure | Routers, multiple files | [Bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| Pytest fixtures | Shared setup, scopes | [How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) |
| Twelve-factor config | Why config lives in the environment | [III. Config](https://12factor.net/config) |
| LLM API | Chosen in ADR 0002; read that provider's official API reference | Linked from ADR 0002 |

You have it when you can:

- Explain red, green, refactor using your own commits as the example.
- Explain why the use case imports a port and not the LLM client.
- Swap the real adapter for the fake one and say exactly which line makes the switch.

## M2 · Domain core

You learn domain modeling, relational design and persistence behind repositories.

| Topic | What to understand | Official docs |
| --- | --- | --- |
| Dataclasses | Entities and value objects in plain Python | [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) |
| PostgreSQL | Types, constraints, indexes, transactions | [Tutorial](https://www.postgresql.org/docs/18/tutorial.html) · [Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html) |
| SQLAlchemy 2 | Engine, session, mapping, the 2.x query style | [Unified tutorial](https://docs.sqlalchemy.org/en/latest/tutorial/) |
| Alembic | Migrations, autogenerate, upgrade and downgrade | [Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) |
| psycopg 3 | The driver, connection strings | [psycopg 3 docs](https://www.psycopg.org/psycopg3/docs/) |
| SQL databases in FastAPI | Session per request | [SQL databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| Clean Architecture | The dependency rule, in the author's words | [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) |
| Hexagonal architecture | Ports and adapters, the original article | [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/) |
| Patterns in Python | Repository, unit of work, service layer (free book, not official docs) | [Architecture Patterns with Python](https://www.cosmicpython.com/) |

You have it when you can:

- Draw the schema from memory and justify each constraint.
- Show one business rule, its unit test, and prove the test runs with Docker stopped.
- Explain the difference between Active Record (Eloquent) and Data Mapper (SQLAlchemy).

## M3 · Documentation and quality

You learn to make the API understandable to others and to automate quality checks.

| Topic | What to understand | Official docs |
| --- | --- | --- |
| OpenAPI metadata | Tags, summaries, examples, response descriptions | [Metadata and docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/) · [OpenAPI specification](https://spec.openapis.org/oas/latest.html) |
| Type checking | What a static type checker catches that tests do not | [Python typing documentation](https://typing.python.org/en/latest/) |
| Coverage | What coverage measures and what it does not | [coverage.py](https://coverage.readthedocs.io/) |
| Redis | Caching patterns, expiration | [Redis docs](https://redis.io/docs/latest/) · [redis-py](https://redis.readthedocs.io/en/stable/) |
| AI review on pull requests | Running Claude Code in GitHub Actions | [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions) |
| Semantic Versioning | When to bump major, minor, patch | [SemVer](https://semver.org/) |

You have it when you can:

- Hand `/docs` to someone who has never seen the project and they can call every endpoint.
- Explain one finding from the AI reviewer that you rejected, and why.

## M4 · Agents for the whole lifecycle

You learn to direct coding agents instead of only prompting them. The order and the entry
criteria are in [AGENTIC_ROADMAP.md](AGENTIC_ROADMAP.md).

| Topic | What to understand | Official docs |
| --- | --- | --- |
| `CLAUDE.md` | Persistent project instructions, what belongs there | [Memory](https://code.claude.com/docs/en/memory) |
| Skills | Packaged procedures the agent loads on demand | [Skills](https://code.claude.com/docs/en/skills) |
| MCP | Connecting an agent to tools and data | [MCP in Claude Code](https://code.claude.com/docs/en/mcp) · [Model Context Protocol](https://modelcontextprotocol.io/) |
| Subagents | Specialized agents with their own context | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| Hooks | Rules that must run every time, without exceptions | [Hooks guide](https://code.claude.com/docs/en/hooks-guide) |
| Working practices | Giving context, giving a check to run | [Best practices](https://code.claude.com/docs/en/best-practices) |

You have it when you can:

- Show an agent's pull request that you sent back, and the instruction change that fixed the cause.
- Explain when a rule belongs in `CLAUDE.md`, in a Skill, or in a hook.

## M5 · Front end and Game Master

You learn to consume your own API from a typed client.

| Topic | What to understand | Official docs |
| --- | --- | --- |
| React | Components, state, effects | [React: learn](https://react.dev/learn) |
| Vite | Dev server, build | [Vite guide](https://vite.dev/guide/) |
| TypeScript | Typing API responses | [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html) |
| CORS | Why the browser blocks the call, and the fix | [CORS in FastAPI](https://fastapi.tiangolo.com/tutorial/cors/) |

You have it when you can play one short session in the browser and explain the path of one
click from the button to the database and back.
