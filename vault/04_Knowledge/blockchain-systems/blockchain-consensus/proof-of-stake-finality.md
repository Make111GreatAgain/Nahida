---
id: "nahida-knowledge-proof-of-stake-finality"
title: "Proof-of-stake finality"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "proof-of-stake-finality"
domain_id: "blockchain-systems"
direction_id: "consensus"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-consensus"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "consensus"
  - "proof-of-stake-finality"
primary_ontology_path: "blockchain-systems/consensus/proof-of-stake-finality"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-proof-of-stake-finality"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-consensus"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus/proof-of-stake-finality.md"
      - "vault/04_Knowledge/blockchain-systems/blockchain-consensus.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-of-stake-finality"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-of-stake-finality"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-of-stake-finality"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-proof-of-stake-finality"
    relation: "bridges_to"
    to: "nahida-bridge-distributed-bft-to-blockchain-finality"
    evidence_refs:
      - "vault/05_Bridges/distributed-bft-to-blockchain-finality.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-proof-of-stake-finality"
    relation: "bridges_to"
    to: "nahida-bridge-proof-of-stake-finality-to-cross-chain-protocols"
    evidence_refs:
      - "vault/05_Bridges/proof-of-stake-finality-to-cross-chain-protocols.md"
      - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-distributed-bft-to-blockchain-finality"
  - "nahida-bridge-proof-of-stake-finality-to-cross-chain-protocols"
source_note_refs:
  - "vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md"
  - "vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md"
  - "vault/03_Sources/papers/doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems.md"
representative_source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
query_keys:
  - "Proof-of-stake finality"
  - "proof-of-stake-finality"
  - "PoS finality"
  - "finality gadget"
  - "FedChain"
  - "federated-blockchain systems"
  - "PVSS leader selection"
  - "CP CG CQ"
  - "weakest chain security"
aliases:
  - "PoS finality"
  - "finality gadget"
  - "FedChain PoS consensus"
domains:
  - "blockchain-systems"
topics:
  - "proof-of-stake-finality"
  - "cross-chain-incentives"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-22"
valid_until: "2026-07-22"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-22"
created: "2026-06-20"
updated: "2026-06-22"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260622-fedchain"
source_refs:
  - "sha256:9fd9aff8070924cbdfb565238284ae8ffea9261319c1aa40c5330bc8b405b635"
  - "arxiv:1710.09437v4"
  - "doi:10.1109/tsc.2023.3240235"
confidence: "medium"
trust_tier: "primary"
---

# Proof-of-stake finality

## 定义与范围

- 定义: Proof-of-stake finality 让 stake-weighted validators 对区块形成最终确认，并通过 locking、slashing 和 unbonding 处理冲突 finality。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `proof-of-stake-finality`
- Aliases/query keys: PoS finality, finality gadget
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `proof-of-stake-finality`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

Tendermint 和 Casper FFG 是当前 source seed；BFT quorum intuition 可迁移，但经济惩罚、validator churn 和 long-range assumptions 是区块链特有边界。

FedChain 补充了一条 federated-blockchain PoS route：用 PVSS 生成 randomness、FTS 按 stake 选择 leaders/committee，并用 CP/CG/CQ 与 attack-prevention analysis 说明 individual-chain security。它的重要增量是把 PoS finality 明确接到 cross-chain SPV transfer：跨链系统的安全不强于最弱源链。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-consensus|blockchain-consensus]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在 PoS validator set 下获得可追责 finality，防止 conflicting commits 或让它们变成 slashable evidence。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-consensus|blockchain-consensus]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Tendermint propose/prevote/precommit and proof-of-lock | Tendermint propose/prevote/precommit and proof-of-lock | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| Casper FFG finality overlay and slashing commandments | Casper FFG finality overlay and slashing commandments | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| validator bonding/unbonding and inactivity leak | validator bonding/unbonding and inactivity leak | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| PVSS/FTS federated PoS consensus | 用 PVSS 生成 unbiased randomness，FTS 按 stake 选 leader/committee，I1-I4 rules 处理 leader list、empty blocks、block immutability 和 longest valid fork。 | 多条 PoS/federated chains，需要 source-chain confirmation 支撑 cross-chain transfer。 | adversary >50% stake 时 PVSS 假设失效；详细 proofs 在 supplemental appendix；reward/stake dynamics 影响 weakest-chain security。 | [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper the Friendly Finality Gadget]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | paper | 新增 PoS finality source extension：PVSS/FTS leader selection、CP/CG/CQ、attack prevention、confirmation-time analysis 和 Stackelberg stake distribution | simulation/analysis; supplemental proofs not local; not Ethereum/CometBFT spec evidence | `p1-p13` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-20`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: PoS finality 是 BFT 到 blockchain 的应用 translation，不应被经典 BFT 定义吞掉。

- FedChain delta: PoS finality 不是孤立链内性质；在 federated transfer 中，source-chain finality、adversarial stake ratio 和 stake distribution 会直接决定 destination-chain 是否能安全接受 SPV evidence。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing-notes-only; no external latest evidence was fetched.
- Latest industrial focus summary: repository/implementation evidence is sparse unless source notes say otherwise.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: new deep-read source or daily/foundation fetch.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-9fd9aff80709-tendermint-consensus-without-mining|Tendermint: Consensus without Mining]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[arxiv-1710-09437v4-casper-friendly-finality-gadget|Casper the Friendly Finality Gadget]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[doi-10-1109-tsc-2023-3240235-fedchain-secure-proof-of-stake-framework-federated-blockchain-systems|FedChain]] | 新增 PVSS/FTS + CP/CG/CQ PoS route，并把 PoS finality 作为 cross-chain SPV transfer 的 security substrate。 | 背景; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 Ouroboros/PoS sidechains/IBC light-client sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[distributed-bft-to-blockchain-finality|Distributed BFT -> blockchain finality]] | `distributed-systems/consensus/byzantine-fault-tolerance; blockchain-systems/consensus/proof-of-stake-finality` | application, dependency, translation | Classical BFT quorum and safety arguments transfer; token economics, validator churn, unbonding periods, light-client trust, and long-range attacks require blockchain-specific assumptions. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-proof-of-stake-finality | is_a | nahida-knowledge-blockchain-consensus | vault/04_Knowledge/blockchain-systems/blockchain-consensus/proof-of-stake-finality.md; vault/04_Knowledge/blockchain-systems/blockchain-consensus.md | medium | active_seed |
| nahida-knowledge-proof-of-stake-finality | evidenced_by | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | vault/03_Sources/papers/sha256-9fd9aff80709-tendermint-consensus-without-mining.md | medium | active_seed |
| nahida-knowledge-proof-of-stake-finality | evidenced_by | vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md | vault/03_Sources/papers/arxiv-1710-09437v4-casper-friendly-finality-gadget.md | medium | active_seed |
| nahida-knowledge-proof-of-stake-finality | bridges_to | nahida-bridge-distributed-bft-to-blockchain-finality | vault/05_Bridges/distributed-bft-to-blockchain-finality.md | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 现代 Ethereum consensus spec、CometBFT、long-range/light-client sources 缺。 | 影响本节点 foundation 完整性 | nahida-research-search or nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 2 source notes; 3 legacy notes | codex |
