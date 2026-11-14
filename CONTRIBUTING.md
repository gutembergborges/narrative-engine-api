# Contributing

This is a solo portfolio project, but it follows the same workflow a team would use. The goal
is that every change is small, reviewed and easy to explain.

## The loop

1. Pick one issue. One issue is one small outcome.
2. Create a branch from an up-to-date `main`.
3. Make the change in small commits.
4. Run the checks locally.
5. Open a pull request, let CI run, review your own diff, then merge.

`main` is protected: changes arrive only through pull requests with a green CI.

## Branch names

`<type>/<short-description>`, lowercase, words separated by hyphens.

```text
feat/narrative-endpoint
fix/health-status-code
docs/adr-0002-llm-provider
chore/scaffold
```

## Commit messages: Conventional Commits

Format: `<type>(optional scope): <description>` in the imperative mood ("add", not "added").
Specification: <https://www.conventionalcommits.org/en/v1.0.0/>

| Type | Use it when |
| --- | --- |
| `feat` | You add behavior a user of the API can see |
| `fix` | You correct a bug |
| `docs` | You change documentation only |
| `test` | You add or change tests only |
| `refactor` | You change code structure without changing behavior |
| `build` | You change dependencies, Docker or packaging |
| `ci` | You change the CI workflow |
| `chore` | Maintenance that fits none of the above |

Examples:

```text
feat(api): add narrative generation endpoint
test(application): cover empty prompt in generate narrative
build: add Dockerfile for the API
docs(adr): record LLM provider decision
```

A breaking change adds `!` after the type and a `BREAKING CHANGE:` footer:

```text
feat(api)!: rename narrative response field

BREAKING CHANGE: `text` is now `narrative`.
```

Why this matters: the history becomes readable, and a changelog can later be generated from it
(see the changelog writer in [docs/AGENTIC_ROADMAP.md](docs/AGENTIC_ROADMAP.md)).

## Checks before you push

```bash
uv run ruff check .            # lint
uv run ruff format .           # format (CI runs it with --check)
uv run pytest                  # tests
```

CI runs the same three checks on every pull request.

## Pull requests

- The title follows Conventional Commits, because it becomes the merge commit message.
- Fill in the template: what, why, how to test.
- Keep it small. If the description needs the word "and" three times, split it.
- Squash-merge, then delete the branch.

## Tests

- Unit tests for domain rules and use cases run without a database, network or Docker.
- Tests never call a real LLM provider. Use a fake adapter that implements the port.
- Write the test first when you can: red, green, refactor.

## Architecture rule

Dependencies point inward: `api` → `application` → `domain`. `infrastructure` implements the
ports that `application` defines. `domain` imports only the standard library. Details in
[docs/architecture.md](docs/architecture.md).

## Secrets

Never commit secrets. Configuration comes from environment variables. `.env.example` lists the
variables with safe placeholder values; your real `.env` is ignored by Git.

## Decisions

A decision that is hard to reverse gets an Architecture Decision Record in `docs/adr/`,
numbered in order (`0002-llm-provider.md`). Format: context, decision, options considered,
consequences. See [ADR 0001](docs/adr/0001-stack.md) for an example.
