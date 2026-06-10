---
name: nahida-audit
description: Use when checking a Nahida vault for missing IDs, broken links, duplicate sources, claims without sources, stale indexes, unsafe writes, and unreviewed machine notes.
---

# Nahida Audit

Read `vault/00_System/NAHIDA_SPEC.md` before inspecting.

## Checks

- missing required frontmatter
- duplicate IDs
- source duplicates by canonical URL, DOI, arXiv ID, GitHub repo, checksum, or soft similarity
- claims without source refs
- broken wikilinks or ID refs
- stale generated indexes
- writes without ledgers
- unreviewed review queue items

## Boundaries

- Read broadly.
- Write only audit reports and review queues.
- Do not modify knowledge notes.
