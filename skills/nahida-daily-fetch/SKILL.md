---
name: nahida-daily-fetch
description: Use when the user asks Nahida to run a daily, periodic, scheduled, recent, latest, or freshness-oriented fetch for papers, web/news, GitHub repos, or emerging terms relevant to the vault.
---

# Nahida Daily Fetch

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This skill monitors recent/fresh material relevant to existing Nahida knowledge and writes freshness-oriented source notes or reports. It does not directly promote news into evergreen knowledge.

## Current Architecture

- Freshness source lane: `03_Sources/web/daily/` or generated daily reports under `90_Generated/reports/daily/`.
- Durable knowledge lane: `nahida-knowledge-get` updates `04_Knowledge/` and `05_Bridges/` only after source quality/deepening gates pass.
- Existing interest scope comes from `04_Knowledge/`, `05_Bridges/`, watchlists, review queues, recent sources, and query gaps. Legacy maps/syntheses may be read as compatibility context.

## Core Standard

Daily fetch is an attention and freshness system, not a truth factory. It should find relevant new papers, repos, releases, posts, news, and hot terms; deduplicate them; classify them; and decide whether deeper source work is needed.

Use Chinese as the main language. Preserve exact English titles, repo names, protocol names, release names, URLs, and dates.

Daily fetch must not create foundational knowledge from recent attention alone. A hot term, release, new repo, or news item is a freshness signal until corroborated by stable sources or deep source notes.

Examples:

- Correct: a new Groth16 optimization paper becomes `deep_paper_required` and a possible source extension under zk-SNARKs/Groth16.
- Wrong: a news item makes Groth16 a new foundational concept.
- Correct: repeated BFT-related releases may mark the BFT knowledge node for refresh.
- Wrong: daily fetch rewrites BFT from release notes only.

## Cold-Start And Emerging-Term Handling

When daily fetch sees a high-signal area that has no usable hierarchy, it may propose cold-start candidates but must not treat freshness as durable taxonomy by itself. Record:

- likely research/practice field,
- background or motivation suggested by the signal,
- reusable problem or method family,
- foundation concepts that require stable corroboration,
- application/evaluation context,
- source/news/release/repo/paper instance,
- retrieval benefit if this becomes a knowledge path.

If the candidate would help future query read fewer notes, mark `knowledge_refresh_candidate`, `foundation_pack_needed`, `deep_paper_required`, `deep_repo_required`, or `web_research_note_ok`. If it is only a hot term or one announcement, keep it as `freshness_signal_only` or review.

## Scope Selection

If no explicit scope is provided, infer from:

- active `04_Knowledge/` nodes,
- `04_Knowledge/<domain>/research-dynamics.md` notes, especially stale or near-expiry notes,
- `05_Bridges/`,
- watchlists,
- stale/expired freshness fields,
- recent query gaps,
- recent source notes,
- review queues,
- user-defined domains such as blockchain, zero-knowledge proofs, and AI subdomains.

Do not broaden into the entire internet. Keep the fetch bounded by current Nahida interests and high-signal emerging terms.

## Item Decisions

Each found item must receive one decision:

- `deep_paper_required`: high-value paper candidate; route to `nahida-paper-read`.
- `deep_repo_required`: high-value GitHub repository; route to `nahida-github-repo-analyze`.
- `web_research_note_ok`: stable web/reference item or cluster; route to `nahida-research-search` or source note.
- `freshness_signal_only`: news/release/hot term; record as signal/watchlist, do not promote to evergreen knowledge.
- `knowledge_refresh_candidate`: existing knowledge node may need refresh because multiple reliable signals accumulated.
- `domain_dynamics_refresh`: a domain's `research-dynamics.md` should be refreshed because reliable signals change academic focus, industrial focus, emerging topics, open problems, or directional tendency.
- `bridge_candidate`: recent material indicates cross-node relation worth review.
- `discard_or_review`: duplicate, weak, hype-only, off-scope, or ambiguous.

## Required Procedure

1. Build fetch scope:
   - Target knowledge nodes, bridge endpoints, watch terms, stale nodes, known gaps, date window.
2. Search/fetch:
   - Papers/preprints.
   - GitHub repositories/releases when relevant.
   - Official docs/specs/releases.
   - Engineering blogs/practice notes.
   - News/announcements/hot terms.
3. Deduplicate:
   - Use canonical URLs, DOI/arXiv, GitHub owner/repo/ref, titles with caution, and previous daily reports.
   - Do not repeatedly fetch the same item unless there is a material update.
4. Evaluate:
   - relevance to knowledge node/bridge,
   - source quality,
   - novelty,
   - urgency/freshness,
   - need for deeper source skill.
   - cold-start hierarchy candidate and retrieval benefit when no target path exists.
5. Write report/source notes:
   - Record accepted/rejected/review items, dates, URLs, evidence, target paths, and next skill owner.
6. Handoff:
   - Route accepted deep items to paper/repo/search skills or `nahida-knowledge-get`.
   - Refresh or queue affected domain dynamics notes when the signal is domain-level.
   - Keep weak recent items as watchlist/review signals.

## Output Contract

Daily fetch output must include:

- `Run Identity`: date, time window, scope, watchlists/knowledge nodes used.
- `Interest Scope`: target domains/directions/problems/bridges.
- `Fetched Items`: title, URL, date, source type, target path, duplicate status.
- `Decisions`: deep paper, deep repo, web research, freshness-only, knowledge refresh, bridge candidate, discard/review.
- `Freshness Signals`: affected knowledge node, signal type, evidence, expected durability, next action.
- `Domain Dynamics`: affected L1 domains, whether `research-dynamics.md` was refreshed/queued/stale/unchanged, academic/industrial signals, open problems, emerging terms, evidence window.
- `Cold-Start Hierarchy Candidates`: field, background, problem, foundation concepts, method family, application/evaluation context, source instance, confidence, handling.
- `Retrieval Optimization`: whether a proposed path would reduce future source-note reads or should stay as watch/review.
- `Knowledge Refresh Candidates`: nodes that may need `nahida-knowledge-get` or `nahida-consolidate`.
- `Bridge Candidates`: endpoint knowledge paths, relation type, evidence, maturity.
- `Risk And Review`: hype-only, conflicting claims, weak evidence, taxonomy changes.
- `Capability Usage`: web/search/browser/GitHub tools, indexes, Obsidian tools, fallbacks.

## Quality Gate

Before finishing:

- The run did not promote news/hype directly to evergreen knowledge.
- Duplicates and previously seen items were handled.
- Every accepted item has a target knowledge path or review reason.
- Papers/repos are routed to deep source skills before durable absorption.
- Freshness-only signals include dates and expiry/refresh implications.
- Domain-level latest/trend/open-problem signals update or queue the matching `research-dynamics.md`.

## Boundaries

- May write daily reports, freshness source notes, watchlists, generated indexes, ledgers, and review queues.
- Must not update `04_Knowledge/` or `05_Bridges/` directly unless the item has passed the same source-readiness requirements used by `nahida-knowledge-get`.
