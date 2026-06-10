---
name: nahida-intake
description: Use when adding web, newsletter, or manually supplied source material to a Nahida vault; creates source notes and ledgers without distilling durable claims directly.
---

# Nahida Intake

Read `vault/00_System/NAHIDA_SPEC.md` before writing.

## Workflow

1. Classify the source as `web_reference`, `web_concept`, `web_blog`, or `web_news`.
2. Normalize canonical URL and source metadata.
3. Check `90_Generated/ledgers/fetch-ledger.jsonl` and source notes for duplicates.
4. Create or update a `source` note under `03_Sources/web/`.
5. Append fetch/write ledger entries.
6. Hand claim extraction to `nahida-distill`.

## Boundaries

- May write `02_Raw/web/`, `03_Sources/web/`, and generated ledgers.
- Must not rewrite concept maps directly.
- `web_news` should go to review unless corroborated.
