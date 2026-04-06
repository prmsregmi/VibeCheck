# VibeCheck

Agentic code analysis for vibe-coded projects. Know whether your AI-generated
codebase is ready to ship or heading for a headline.

## The Problem

Vibe coding changed who can build software. Cursor, Lovable, Bolt, Replit Agent
and friends let anyone go from idea to working prototype in hours. But "working"
and "production-ready" are very different things:

- **45% of AI-generated code** contains OWASP Top 10 vulnerabilities (Veracode, 2025)
- **53% of teams** that shipped AI-generated code later found security issues that passed initial review
- **96% of developers** don't fully trust AI code output, yet only **48% verify it** — the "verification gap" (Sonar, Jan 2026)
- Georgia Tech's Vibe Security Radar tracked **35 CVEs caused by AI-generated code** in March 2026 alone, up from 6 in January
- AI now accounts for **42% of all committed code** while refactoring dropped from 25% to under 10% of changes

The result: hardcoded API keys, missing auth, zero tests, dependency bloat, and
patchwork architectures that break the moment real users show up.

## What VibeCheck Does

VibeCheck is an agentic system that analyzes your entire project and returns a
single, plain-English verdict. No CVSS scores. No rule IDs. Just a clear answer
on whether your code is safe to deploy.

### The Verdicts

| Verdict | What It Means |
|---|---|
| **Ship It** | Production-ready. No critical issues found. Go live. |
| **Not Bad** | Solid foundation with minor issues. Fix the short list, then ship. |
| **Sketchy** | Significant problems across security, quality, or structure. Needs real work. |
| **Bust** | Critical vulnerabilities, exposed secrets, or fundamental architectural failures. Do not deploy. |

### Analysis Categories

- **Secrets & Credentials** — Hardcoded API keys, database URIs, tokens in source
- **Authentication & Authorization** — Missing RLS, unprotected routes, no access control
- **Test Coverage** — Existence and quality of test files, untested critical paths
- **Dependency Health** — Known CVEs, typosquatting risk, bloat, outdated packages
- **Code Structure** — Duplication, dead code, file size, architectural coherence
- **Error Handling** — Unhandled exceptions, missing validation at system boundaries
- **Deployment Readiness** — Environment config, CORS, debug flags, logging

Each category gets a score and plain-language findings. The overall verdict is
derived from the worst-performing categories because your app is only as strong
as its weakest point.

## Why Not SonarQube / Snyk / Semgrep?

Those tools are built for engineers who can read the output. VibeCheck is built
for the person who **wrote zero lines of the code they're about to deploy**.

| | Enterprise SAST | Developer Tools | VibeCheck |
|---|---|---|---|
| **Target user** | Security teams | Engineers | Anyone who vibe-codes |
| **Scope** | File/function level | CI pipeline | Whole project |
| **Output** | CVSS scores, rule IDs | PR annotations | Plain English verdict |
| **Vibe-code patterns** | Not detected | Not detected | Purpose-built |
| **Setup** | Hours/days | Config files | Point at a repo |

Existing vibe-specific tools (vibe-poo, sober-coding, VibeCheck.expert) are
either snippet-level, single-language, or narrow in scope. VibeCheck analyzes
the full project across all the ways AI-generated code fails in production.

## Getting Started

Requires Python 3.12+.

```bash
git clone https://github.com/prmsregmi/VibeCheck.git
cd VibeCheck
uv sync
```

Run the API server:

```bash
uv run uvicorn vibecheck.api.app:app --reload
```

Run tests:

```bash
uv run pytest
```

Lint:

```bash
uv run ruff check src/ tests/
```

## Project Structure

```
src/vibecheck/
  api/          # FastAPI endpoints
  analyzers/    # Analysis agents (secrets, auth, tests, deps, structure)
  models/       # Pydantic models and verdict definitions
tests/          # Test suite
```

## Roadmap

- [ ] Core analysis agents for each category
- [ ] CLI interface (`vibecheck /path/to/project`)
- [ ] GitHub App integration (auto-check on PR)
- [ ] LLM-powered plain-English report generation
- [ ] Support for JS/TS, Python, Go, Rust projects
- [ ] CI/CD pipeline integration
- [ ] Self-hosted and cloud-hosted options

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
