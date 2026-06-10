---
name: nahida-paper-import
description: Use when importing local PDFs, XiaoLvJing exports, Zotero exports, BibTeX/RIS/CSL JSON, or newly discovered papers into a Nahida vault.
---

# Nahida Paper Import

Read `vault/00_System/NAHIDA_SPEC.md` before writing.

## Workflow

1. Identify paper source: local PDF, XiaoLvJing, Zotero, BibTeX/RIS/CSL JSON, or emerging paper feed.
2. Fingerprint by DOI, arXiv ID, checksum, title/authors/year, then soft similarity.
3. Create or update `03_Sources/papers/` source notes.
4. Preserve local file provenance and remote metadata.
5. Extract keywords, method, limitation, and candidate directions.
6. Hand claims to `nahida-distill` and direction candidates to `nahida-direction-evolver`.

## Boundaries

- May write paper source notes and paper ledgers.
- Must not promote new research directions without review or configured support thresholds.
