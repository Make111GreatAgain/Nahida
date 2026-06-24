---
name: nahida-research-search
description: Use when the user asks to search the web for a research keyword, concept, emerging topic, technical question, comparison, or domain survey that should become Nahida web source notes.
---

# Nahida Research Search

Read `vault/00_System/NAHIDA_SPEC.md` before writing. This skill searches web sources and writes structured web source/research notes under `03_Sources/web/`. It does not directly create durable knowledge nodes or bridges; it hands accepted notes to `nahida-knowledge-get`.

## Current Architecture

- Output lane: `03_Sources/web/` and `03_Sources/web/research/`.
- Handoff lane: `nahida-knowledge-get` updates `04_Knowledge/` and `05_Bridges/`.
- Search can propose paper/repo candidates, but papers and repositories require `nahida-paper-read` or `nahida-github-repo-analyze` before durable absorption.

## Core Standard

Do not produce a generic search summary. A useful research note separates source types, freshness, evidence quality, definitions, debates, applications, representative sources, gaps, and target knowledge paths.

Use Chinese as the main language. Preserve source titles, organization names, project names, protocols, APIs, standards, and canonical English terms for retrieval.

Research search may use the web to fill missing foundations during update/research mode. Prefer stable sources: official docs/specs, surveys, canonical papers, textbooks, standards, or well-maintained references. Do not let a blog/news item define a foundation by itself.

Correct foundation targets include CFT, BFT, zk-SNARKs, polynomial commitments, consensus, verifiable computation, agent memory, and multi-agent orchestration when the source set supports them. Protocol instances such as Raft, PBFT, Groth16, one repo, one benchmark, or one product release are not foundational by default; treat them as representatives, examples, or source extensions unless repeated evidence/user scope justifies a scoped node.

## Cold-Start Handoff Standard

Research search often creates the first stable picture of an area. When existing hierarchy is absent or thin, the research note must extract a reusable parent-first structure from multiple sources, not from a single blog/news item:

- research field/domain,
- background, history, motivation, and constraints,
- reusable research/practice problems,
- foundation concepts supported by stable sources,
- method/protocol/model/architecture families,
- application, benchmark, dataset, deployment, and evaluation contexts,
- source instances or freshness signals such as papers, repos, releases, product announcements, or news.

State how the proposed hierarchy will help future query read fewer web/source notes and how it helps summarize or refresh the field/direction. Hot terms and news remain watch terms or freshness signals until stable evidence supports a durable knowledge node.

## Source Lanes

Classify each web result:

- `official_reference`: official docs, standards, specs, project docs, release notes.
- `academic_reference`: surveys, canonical papers, textbooks, lecture notes.
- `web_concept`: stable concept/tutorial/explainer.
- `web_blog_practice`: engineering/practice blog.
- `web_news`: news, announcements, time-sensitive commentary.
- `paper_candidate`: paper that needs `nahida-paper-read`.
- `repo_candidate`: repository that needs `nahida-github-repo-analyze`.

For current/latest/news-sensitive queries, browse and record exact access date. Prefer primary sources and official/upstream material when accuracy matters.

## Deepening Gate

Every accepted item needs a decision:

- `foundation_pack_research_ok`: stable source cluster can support a missing foundation in `04_Knowledge/`.
- `web_research_note_ok`: source cluster can become a structured web note and handoff.
- `deep_paper_required`: queue/run `nahida-paper-read` before durable knowledge.
- `deep_repo_required`: queue/run `nahida-github-repo-analyze` before durable implementation knowledge.
- `freshness_signal_only`: news/release/hot term should update watchlists/review/daily context, not evergreen knowledge.
- `discard_or_review`: low-quality, duplicate, ambiguous, or off-scope.

## Required Procedure

1. Scope the search:
   - Normalize keywords, aliases, target domain/direction/problem, time window, and expected output.
   - Check existing `04_Knowledge/`, `05_Bridges/`, `03_Sources/web/`, watchlists, and generated indexes to avoid duplicate work.
2. Search by source lane:
   - Foundation/reference.
   - Concept/tutorial.
   - Engineering practice.
   - Papers.
   - GitHub/projects.
   - News/announcements when freshness matters.
3. Evaluate sources:
   - authority, date, evidence quality, bias, duplicate status, relation to target path.
   - distinguish definition, claim, example, implementation, debate, timeline, and open question.
   - extract cold-start hierarchy facets and separate durable foundations from source/news instances.
4. Write source note:
   - Use `vault/00_System/templates/research_search.md` or `source.md`.
   - Store under `03_Sources/web/` with path-safe slug.
   - Include source set, access dates, trust tiers, deepening decisions, and target knowledge paths.
5. Handoff:
   - `foundation_pack_research_ok` and `web_research_note_ok` go to `nahida-knowledge-get`.
   - Paper/repo candidates go to the deep source skill or review queue.
   - Freshness-only items go to watchlists/daily review, not evergreen knowledge.

## Output Contract

The research note must include:

- `Research Scope`: question, keywords, aliases, time window, target knowledge path.
- `Source Set`: title, URL, author/org, publication/update/access date, source subtype, trust tier, selection reason, duplicate status.
- `Findings`: definitions, mechanisms, applications, representative papers/repos, disagreements, gaps.
- `Evidence Quality`: primary/secondary/tertiary, freshness, corroboration, caveats.
- `Deepening Decisions`: for every accepted item.
- `Knowledge Handoff`: target knowledge nodes/sections, source-extension deltas, foundation gaps.
- `Cold-Start Hierarchy Discovery`: field, background, problems, foundation concepts, method families, application/evaluation contexts, source/news instances, evidence, confidence.
- `Retrieval Optimization`: future queries helped, web notes avoided, summary/update benefit, source-only or watch-term decisions.
- `Domain Dynamics Impact`: whether the source set should create/refresh `04_Knowledge/<domain>/research-dynamics.md`, and which academic/industrial/open-problem signals it supports.
- `Foundation Candidate Judgment`: candidate, correct handling, incorrect handling to avoid.
- `Bridge Candidates`: endpoint knowledge paths, relation type, thesis, evidence, transfer limits.
- `Follow-up`: paper reads, repo analyses, daily watch terms, searches to run next.

## Quality Gate

Before finishing:

- Current/latest facts have access dates and source dates when available.
- Paper/repo candidates were not treated as durable evidence without deep source notes.
- News/hype was not promoted to evergreen foundation.
- Foundation content is backed by stable sources or clearly marked tentative.
- Handoff uses Source + Knowledge + Bridge terms.

## Boundaries

- May write `02_Raw/web/`, `03_Sources/web/`, generated reports, ledgers, indexes, review queues, watchlists.
- Must not update `04_Knowledge/` or `05_Bridges/` directly; use `nahida-knowledge-get`.
