<!-- SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Contributing

Mixar is publishing the Blender-side client source first. External pull requests are not open for general contribution yet.

For questions, build help, and general discussion, the fastest channel is the **Mixar Discord**: https://discord.gg/YVqvkQx8rX. Use GitHub issues for the specific reports listed under "Before Opening An Issue" below.

## Current Contribution Status

- Public source: open
- Public issues: limited to source-availability, build, license, and security-process questions
- External pull requests: not accepted until Mixar publishes the CLA workflow
- Contributor agreement: CLA required before Mixar accepts substantial external contributions

Pull requests opened before the CLA process is published may be closed without review.

## Repository Access and Authorization

The public source license and access to the official GitHub repository are separate things.

The GPL license may allow you to copy, modify, and redistribute covered source under its terms. It does **not** grant permission to push changes, alter settings, publish releases, access secrets, or otherwise administer the official `aimcrazyxx/mixar-app` repository.

For this official repository:

- Direct pushes require explicit write, maintain, or admin permission from the repository owner.
- Do not push to protected or release branches unless the owner has specifically authorized that access.
- Do not force-push, rewrite shared history, delete branches/tags, or bypass required checks without explicit maintainer approval.
- Changes to GitHub Actions, release/signing logic, build infrastructure, secrets handling, authentication, BYOK/providers, update mechanisms, or security-sensitive code require owner review.
- Repository secrets, environment secrets, signing material, deployment credentials, API keys, tokens, and private infrastructure details must never be copied, exposed, or used without authorization.
- Creating or publishing an official release, package, installer, container image, or signed binary requires explicit maintainer authorization.
- External contributors must use a fork and pull request when public contributions are enabled; a pull request does not grant repository write access.
- Automated agents, bots, CI jobs, and AI coding tools must operate only with the permissions intentionally granted to them and must not attempt to bypass repository protections.

The repository uses `.github/CODEOWNERS` to identify required owners for review-sensitive paths. GitHub branch/ruleset protection should be configured to require those reviews before merging into protected branches.

If you believe you need additional repository access, ask the owner first. Do not work around missing permissions.

## Before Opening An Issue

Check whether the issue is about this public client repository.

Use this repository for:

- Client-side build problems
- Source availability questions
- License and notice questions
- Blender-side client behavior that can be reproduced from public source

Do not post:

- Security vulnerabilities or suspected secrets; follow [SECURITY.md](SECURITY.md)
- Mixar account credentials, API keys, tokens, logs containing secrets, or private scene data
- Requests for Mixar backend source code

## Development Rules

Follow the same structure used by the repo:

- Put durable Mixar source changes under `src/`
- Put Python module code under `src/scripts/mixar/modules/`
- Put C/C++ Blender customizations under `src/source/blender/`
- Keep reusable logic in the relevant module or `common`
- Use the build scripts instead of building directly from generated `source/`
- Keep environment variables in `.env` locally and never commit `.env`

## License Requirements

Every new file must carry SPDX license metadata.

For source files, add an inline SPDX header. For binary assets or formats that cannot carry comments, add an entry to `REUSE.toml`.

### How SPDX Headers Get Added

Add the SPDX header to each new file yourself (see existing files for the
format). CI runs `reuse lint` on every PR and will fail the build if any file
lacks copyright or license information.

### Optional: Local Pre-Commit Hook

```bash
pip install pre-commit
pre-commit install
```

This runs the same `reuse` compliance check locally before each commit so you
catch missing headers early. It is purely a developer convenience and is not
required. Configured hooks live in `.pre-commit-config.yaml`.

### Manual Commands

```bash
# Full REUSE compliance check (same as CI)
reuse --no-multiprocessing lint
```

If `reuse lint` reports a file missing copyright or license info, add an SPDX
header to the top of the file (see existing files for the format) or record it
in `REUSE.toml`.
