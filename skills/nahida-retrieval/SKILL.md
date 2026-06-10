---
name: nahida-retrieval
description: Use when answering questions from a Nahida vault by assembling map, concept, claim, source, bridge, and freshness context with provenance.
---

# Nahida Retrieval

Read `vault/00_System/NAHIDA_SPEC.md` before retrieving.

## Retrieval Order

1. Exact IDs and canonical source keys.
2. Maps for the relevant domain/topic.
3. Concepts and bridges.
4. Claims and their source refs.
5. Source notes and raw provenance.
6. Generated indexes only as rebuildable caches.

## Output

Return a context bundle with:

- relevant notes,
- source chain,
- confidence and stale markers,
- missing evidence or review needs.

## Boundaries

- Read-only by default.
- Optional query logs may go under `90_Generated/runs/`.
