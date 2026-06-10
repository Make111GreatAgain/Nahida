---
name: nahida-collab-sync
description: Use when maintaining a Git-backed Nahida vault with pull, audit, daily update, commit, and push coordination while avoiding multi-agent conflicts.
---

# Nahida Collab Sync

Read `vault/00_System/NAHIDA_SPEC.md` before syncing.

## Workflow

1. Pull latest state.
2. Check dirty files and conflict risk.
3. Run requested Nahida maintenance skills.
4. Rebuild or verify generated indexes if applicable.
5. Run `nahida-audit`.
6. Commit with a run ID if validation passes.
7. Push only when credentials and policy allow.

## Boundaries

- Does not edit knowledge content directly.
- Blocks push on conflicts, failed audit, or dirty human edits.
