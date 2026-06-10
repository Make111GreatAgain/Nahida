---
name: nahida-codegraph-digest
description: Use when reading repository code as implementation evidence for Nahida, especially when CodeGraph or structured symbol/file context is available.
---

# Nahida CodeGraph Digest

Read `vault/00_System/NAHIDA_SPEC.md` before writing.

## Workflow

1. Identify the target repo and the knowledge direction being investigated.
2. Prefer CodeGraph context for symbols, files, call paths, and project structure when available.
3. Summarize purpose, entry points, modules, implementation patterns, dependencies, and maintenance signals.
4. Compare README claims with code evidence where practical.
5. Write implementation digest reports under `90_Generated/reports/codegraph/`.
6. Hand source-backed implementation claims to `nahida-distill`.

## Boundaries

- Must not create durable truth claims directly.
- Must not change source identity fields.
