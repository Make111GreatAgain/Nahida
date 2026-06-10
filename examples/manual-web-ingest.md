# Manual Web Ingest Example

1. Classify a URL as `web_reference`, `web_concept`, `web_blog`, or `web_news`.
2. Create a source note from `vault/00_System/templates/source.md`.
3. Add a fetch ledger line in `vault/90_Generated/ledgers/fetch-ledger.jsonl`.
4. Distill one claim from `vault/00_System/templates/claim.md`.
5. Link the claim from `vault/07_Maps/Domains/AI.md`.
6. Run `nahida-audit` conceptually: check required properties, source refs, duplicates, and links.
