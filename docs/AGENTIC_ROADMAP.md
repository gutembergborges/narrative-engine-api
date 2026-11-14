# Agentic roadmap

How AI agents enter this project, in order. The principle: **an agent may only automate what
I already understand and could do by hand.** Each phase has an entry gate. If the gate is not
met, the phase does not start.

| Phase | Name | Agent's role | Starts when |
| --- | --- | --- | --- |
| 0 | By hand | Reviewer and teacher only | Now |
| 1 | `CLAUDE.md` | Follows written project rules | Milestone 2 is merged |
| 2 | Skills | Runs repeatable procedures | Phase 1 has been stable for a few pull requests |
| 3 | MCP servers | Reads project tools and data | A real need for outside context appears |
| 4 | Subagents | Owns narrow, reviewable jobs | Phases 1 to 3 are in daily use |

Phases 1 to 4 are Milestone 4 of the [roadmap](../README.md#roadmap). Phase 0 covers
Milestones 1 and 2.

## Phase 0 · I code by hand, the assistant reviews

**Goal:** understand and be able to edit every line.

How it works:

- I write the feature code: domain entities, use cases, endpoints and their tests.
- I ask an assistant to review a diff, explain a concept, or point to the official docs.
- The assistant does not write the feature for me. The starter [`CLAUDE.md`](../CLAUDE.md)
  already states this rule, so a Claude Code session in this repository follows it.

Allowed for the assistant: scaffolding, CI, documentation, review comments, questions.

**Done when:** Milestones 1 and 2 are merged, and I can explain the request flow and the layer
rule out loud without notes.

## Phase 1 · `CLAUDE.md`

**Goal:** the agent follows this project's rules without being told each time.

**Entry gate:** I have hit, by hand, the mistakes the rules are meant to prevent. A rule I
cannot justify from experience does not go in the file.

What to do:

- Change the "Current phase" section of `CLAUDE.md` from phase 0 to phase 1: the agent may now
  write code for small, well-specified issues, test-first, one pull request per issue.
- Add a rule only after the agent gets something wrong twice. Delete rules it never needs.
- Keep the file short. It is read on every session, so each line costs context.

Read first: [Memory](https://code.claude.com/docs/en/memory) ·
[Best practices](https://code.claude.com/docs/en/best-practices) ·
[CLAUDE_MD_EXPLAINED.md](CLAUDE_MD_EXPLAINED.md)

**Done when:** the agent completes one small issue end to end, the pull request passes CI, and
my review finds nothing that a `CLAUDE.md` rule should have prevented.

## Phase 2 · Skills

**Goal:** package procedures I repeat, so the agent performs them the same way every time.

**Entry gate:** I have done the procedure by hand at least three times and can write its steps
from memory.

Candidate skills for this repository:

| Skill | Procedure it packages |
| --- | --- |
| `new-use-case` | Port (if needed) → failing unit test → use case → wiring → API test |
| `new-migration` | Change the model → generate the Alembic migration → review the SQL → upgrade and downgrade locally |
| `new-adr` | Next number → template → link from the README table |
| `pr-ready` | Run Ruff and Pytest → check the diff for secrets → write the pull request description |

Read first: [Skills](https://code.claude.com/docs/en/skills)

**Done when:** two skills have each been used on a real issue, and I edited each one at least
once after seeing how the agent used it.

## Phase 3 · MCP servers

**Goal:** give the agent read access to the project's real tools, instead of pasting context.

**Entry gate:** I can name the specific question the agent could not answer without the tool.

Candidates, in order of usefulness:

| Server | What it enables | Guardrail |
| --- | --- | --- |
| GitHub | Read issues and pull requests, open pull requests | Scoped to this repository |
| PostgreSQL | Inspect the schema, run `EXPLAIN` on a query | Read-only role, local development database only |
| Documentation search | Look up current library docs | Read-only |

Rules: least privilege, read-only first, never a production credential, and every server is
listed in the repository so the setup is reviewable.

Read first: [MCP in Claude Code](https://code.claude.com/docs/en/mcp) ·
[Model Context Protocol](https://modelcontextprotocol.io/)

**Done when:** one MCP server is configured, documented, and has answered a real question
during a real issue.

## Phase 4 · Subagents

**Goal:** narrow agents with one job each. Their output is always a pull request or a comment
that I review. None of them merges anything.

**Entry gate:** I have done each job by hand, so I can judge the agent's result.

| Subagent | Job | Input | Output | I verify by |
| --- | --- | --- | --- | --- |
| PR reviewer | Review a diff against `CLAUDE.md` and the architecture rule | A pull request | Inline comments | Checking one finding by hand; rejecting noise |
| Changelog writer | Turn Conventional Commits since the last tag into release notes | Git history | A `CHANGELOG.md` pull request | Comparing with `git log` |
| Dependency fixer | Apply one dependency update and repair what breaks | A new version | A pull request with green CI | Reading the upstream release notes |
| Query optimizer | Find slow queries and propose an index or rewrite | A query and its `EXPLAIN` output | A pull request with before/after plans | Re-running `EXPLAIN ANALYZE` locally |

Read first: [Subagents](https://code.claude.com/docs/en/sub-agents) ·
[Hooks guide](https://code.claude.com/docs/en/hooks-guide)

**Done when:** each subagent has run once on a real task in this repository, and its result is
linked from this file.

## AI reviewer for pull requests

**Recommendation: Claude Code through the Claude Code GitHub Action.** It is the only one of
the three options (GitHub Copilot, Claude Code, Cursor) that the existing Claude subscription
already covers: the action authenticates with a `CLAUDE_CODE_OAUTH_TOKEN` secret created by
`claude setup-token`, so there is no separate API bill.

Things to know before turning it on (planned for Milestone 3):

- Setup is one command inside Claude Code in this repository: `/install-github-app`, then pick
  the review workflow. It installs the Claude GitHub App, stores the secret and opens a pull
  request with the workflow file.
- Review runs count against the subscription's usage limits.
- The managed "Code Review" product, which needs no workflow file, is for Team and Enterprise
  plans. On a Pro plan the GitHub Action is the route.
- The token is a secret. It lives in GitHub repository secrets, never in the repository.

Source: [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions), read on
2026-11-14. Plans and features change; read the page again before setup.

## Log

Record each phase change here with the date and the pull request that made it.

| Date | Phase | Change |
| --- | --- | --- |
| 2026-11-14 | 0 | Scaffold created with AI assistance. Feature code starts by hand. |
