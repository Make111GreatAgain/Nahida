---
name: nahida-direction-evolver
description: Use when mining Nahida sources, claims, papers, GitHub digests, and retrieval misses for emergent keywords, subdirections, aliases, bridges, and watchlist updates.
---

# Nahida Direction Evolver

Read `vault/00_System/NAHIDA_SPEC.md` before writing.

## Workflow

1. Collect recent terms from new sources, claims, paper keywords, GitHub digests, and retrieval misses.
2. Normalize aliases and cluster co-occurring terms.
3. Compare candidates with existing maps and watchlists.
4. Score candidates by source diversity, recency, and domain relevance.
5. Propose subdirections, aliases, merges, bridges, or watchlist changes.
6. Patch only machine-owned map sections unless review confirms a durable taxonomy change.

## Boundaries

- May write direction reports and review queue items.
- May patch machine-owned `Emerging Directions` or `Watchlist` sections.
- Must not promote weak hot terms to durable maps without review.
