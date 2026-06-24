---
name: nahida-query
description: Use when the user asks a vault-only question, asks what Nahida knows, wants sources, related directions, latest recorded progress, or gaps in the Nahida knowledge base.
---

# Nahida Query

Read `vault/00_System/NAHIDA_SPEC.md` before retrieving. Query is read-only and vault-only by default. It answers from existing Nahida notes and explicitly reports missing or stale coverage.

## Current Architecture

Retrieve top-down through:

1. `04_Knowledge/`: domain, direction, problem/topic, method/application nodes and their current synthesis sections.
2. `04_Knowledge/<domain>/research-dynamics.md`: domain-level latest recorded research dynamics, academic focus, industrial focus, emerging topics, open problems, and trend judgments.
3. `05_Bridges/`: cross-node relationships, transfer limits, endpoint evidence.
4. `03_Sources/`: papers, GitHub repository analyses, web notes, daily freshness notes, and source evidence.
5. `90_Generated/`: query reports, indexes, ledgers, review queues as caches/support, not truth.

Legacy lanes (`04_Claims/`, `05_Concepts/`, `06_Bridges/`, `07_Maps/`, `08_Projects/`, `09_Syntheses/`) may be read as compatibility context, but new answers should frame the result in the Source + Knowledge + Bridge model.

## Core Standard

Do not answer as if Nahida were a flat folder of summaries. Start from knowledge nodes, use bridges for cross-node questions, and open source notes only when details or evidence are needed.

If the vault does not contain the answer, say so. Do not fill gaps with model memory, web search, GitHub inspection, arXiv/Crossref metadata, or local files outside the vault.

Use Chinese as the main language. Preserve exact English names, protocols, APIs, paper titles, repo names, code symbols, paths, IDs, and URLs when they are retrieval keys.

Query may use existing `04_Knowledge/` notes even if they were originally improved by web research during an update run. Query itself must not perform that web research. If a foundational concept such as CFT, BFT, or zk-SNARKs is missing or thin, report `基础知识缺失` or `知识库只有部分记录` and suggest `nahida-update`/`nahida-research-search`; do not improvise the missing foundation.

## Vault-Only Contract

Default `query_mode` is `vault_only`.

In `vault_only` mode, do not:

- browse the web,
- call external APIs,
- fetch DOI/arXiv/Crossref/GitHub metadata,
- clone repositories,
- inspect remote websites,
- read raw PDFs or local files outside the Nahida vault/repository.

Use one of these explicit coverage statements when needed:

- `知识库没有记录`: no relevant knowledge/source/bridge/index entry exists.
- `知识库只有部分记录`: lower-layer evidence exists but upper knowledge is missing/thin, or coverage is incomplete.
- `知识库没有足够新近资料`: the user asks for latest/recent/current progress but existing dated sources/daily notes are absent or stale.
- `上层记忆缺失`: source notes exist but matching `04_Knowledge/` nodes are absent or too thin.

Then suggest an exact `nahida-update`, `nahida-consolidate`, `nahida-paper-read`, `nahida-github-repo-analyze`, `nahida-research-search`, or `nahida-daily-fetch` action. Do not run it unless the user explicitly authorizes update mode.

## Capability Orchestration

Use Obsidian-aware capabilities when available:

- `obsidian-markdown` for YAML, wikilinks, headings, tags, callouts.
- `obsidian-note` for graph-friendly note interpretation.
- `obsidian-bases` for existing `.base` dashboards/tables.
- `json-canvas` for existing visual graphs.
- Generated indexes as caches, but prefer source/knowledge/bridge notes as evidence.
- `rg` and filesystem search as fallback/complement.

Report important capability gaps when they affect confidence.

## Retrieval Strategy

For every non-trivial query:

1. Normalize the question:
   - canonical query,
   - query key,
   - domain/direction/problem candidates,
   - aliases,
   - time window,
   - expected answer shape.
2. Check query memory:
   - `90_Generated/reports/queries/`,
   - query ledgers,
   - semantically similar prior reports.
   - Reuse only as retrieval hints unless evidence is still fresh.
3. Retrieve knowledge nodes:
   - exact IDs/aliases first,
   - then domain/direction/problem hierarchy,
   - then parent/child/relation edges.
4. Retrieve domain dynamics when the query asks about latest/current progress, trends, academic/industrial focus, emerging topics, or open problems:
   - `04_Knowledge/<domain>/research-dynamics.md`,
   - freshness fields,
   - evidence window and cited source refs.
5. Retrieve bridges for cross-node questions:
   - endpoint knowledge refs,
   - relation types,
   - transfer boundaries,
   - bridge evidence.
6. Retrieve sources as needed:
   - source refs cited by the knowledge/bridge node,
   - paper/repo/web notes requested by the user,
   - freshness/daily notes for "latest" questions.
7. Assess coverage:
   - found, partial, missing, stale,
   - source coverage,
   - upper knowledge coverage,
   - bridge coverage,
   - freshness.
8. Answer with evidence and gaps.

Do not read every source note just because it exists. Use knowledge node freshness, source refs, relation edges, and indexes to select the smallest honest evidence bundle.

## Retrieval-Efficient Hierarchy Rule

The goal of query is to exploit Nahida's hierarchy, not to simulate a full vault scan. Prefer this path:

```text
domain knowledge -> direction knowledge -> problem/method/application knowledge -> bridge if cross-node -> selected source notes
```

If the hierarchy is missing or too coarse, state the gap explicitly:

- `上层分层缺失`: source notes exist, but domain/direction/problem nodes are absent.
- `分层过粗`: only broad labels such as AI/Blockchain/ZKP exist, so the answer would require reading too many source notes.
- `检索成本过高`: the vault has sources, but no reusable node that narrows the evidence set.

Then suggest `nahida-consolidate` when existing source notes can be reorganized without rereading raw artifacts, or `nahida-update`/`nahida-research-search` when foundation research is missing. Do not silently compensate with web search or model memory.

## Query Types

| Query | Behavior |
| --- | --- |
| "Nahida 里有没有 X" | existence, coverage, exact paths |
| "解释 X" | knowledge node first; if absent, report missing/partial |
| "X 和 Y 的关系" | bridge first; endpoint knowledge second; sources only for evidence |
| "某方向有哪些论文/仓库/资料" | knowledge node source-extension lists plus source inventory |
| "最新/最近/当前进展" | domain `research-dynamics.md` first, then dated knowledge synthesis/daily notes/source dates; no external freshness |
| "学术界/工业界现在关注什么" | domain `research-dynamics.md`; if missing/stale, report gap and suggest daily fetch/consolidate |
| "还有哪些待解决问题" | domain or direction knowledge gaps plus domain dynamics open-problem section |
| "某篇论文/某个仓库" | source note only if already in `03_Sources/`; otherwise report not in Nahida |
| "现有笔记要不要整合/优化" | route write-capable part to `nahida-consolidate` |
| "把网页/段落/论文/仓库加入知识库" | route to `nahida-update` |

Examples:

| Query | Correct | Incorrect |
| --- | --- | --- |
| `解释 zk-SNARKs` | Use existing `04_Knowledge/.../zk-snarks.md`; if absent, say the vault lacks the foundation and propose update. | Browse the web or answer from model memory. |
| `Raft 和 CFT 是什么关系` | Traverse knowledge edges/source refs; explain Raft as protocol instance/representative under CFT if recorded. | Treat Raft as the foundational concept without vault evidence. |
| `最新的 Groth16 优化` | Use dated Nahida sources/daily notes only; if stale/absent, say no fresh evidence. | Fetch current papers/news during query. |

## Evidence Rules

- Query reports and indexes are retrieval aids, not evidence.
- Knowledge nodes are preferred for structure and current synthesis.
- Bridges are preferred for cross-node relations.
- Source notes are evidence anchors.
- Legacy notes may support an answer, but identify them as legacy if they are the only coverage.
- General inference may connect cited vault evidence, but must be labeled as inference.

## Output Contract

Scale the response to the question, but include:

- `结论`: direct answer.
- `查询模式`: normally `vault_only`.
- `覆盖状态`: found, partial, missing, stale.
- `依据`: knowledge nodes, bridges, sources, and dates used.
- `关系路径`: important hierarchy/bridge path, when relevant.
- `领域态势`: domain dynamics note, evidence window, freshness status, when relevant.
- `新近性`: source dates, freshness status, valid-until when relevant.
- `缺口`: missing nodes, missing source coverage, stale evidence.
- `建议更新`: exact next Nahida action when coverage is missing/stale.

When writing a generated query report is useful and allowed, use `vault/00_System/templates/query_report.md` and record query key, aliases, evidence set, coverage, freshness, answer summary, and suggested updates.

## Quality Gate

Before finishing:

- No external retrieval was used in `vault_only` mode.
- Query memory was checked before broad retrieval unless trivial.
- Knowledge nodes were checked before deep source reads for broad/domain questions.
- Domain dynamics was checked before scanning many sources for latest/trend/open-problem questions.
- Bridges were checked before scanning both sides of a cross-node question.
- The answer used the most specific available domain/direction/problem path, or reported that the path is missing/thin.
- Missing/stale knowledge is stated plainly.
- The answer remains Chinese-first and cites local vault evidence.

## Boundaries

- Read-only and vault-only by default.
- May write query reports/ledgers only when useful and allowed.
- Must not create source, knowledge, or bridge notes directly; use `nahida-update`, `nahida-knowledge-get`, or `nahida-consolidate`.
