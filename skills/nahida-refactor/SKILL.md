---
name: nahida-refactor
description: Use when safely renaming, splitting, merging, retiring, moving, or remapping managed Nahida notes after explicit confirmation.
---

# Nahida Refactor

Read `vault/00_System/NAHIDA_SPEC.md` before writing.

## Workflow

1. Confirm the requested refactor is explicit.
2. Identify affected IDs, paths, backlinks, source refs, maps, and ledgers.
3. Propose a migration plan before changing files.
4. Preserve stable IDs unless the user explicitly approves an ID remap.
5. Write migration ledger entries.
6. Update maps and references only within managed zones.

## Boundaries

- Requires `confirmed_refactor`.
- Must not delete, merge, rename IDs, or move notes across zones without confirmation.
