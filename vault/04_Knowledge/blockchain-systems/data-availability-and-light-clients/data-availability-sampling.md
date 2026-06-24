---
id: "nahida-knowledge-data-availability-sampling"
title: "Data availability sampling"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "data-availability-sampling"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
parent_knowledge_refs:
  - "nahida-knowledge-data-availability-and-light-clients"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "data-availability-sampling"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/data-availability-sampling"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "is_a"
    to: "nahida-knowledge-data-availability-and-light-clients"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/data-availability-sampling.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "applied_by"
    to: "nahida-knowledge-fair-data-exchange"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fair-data-exchange.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "uses"
    to: "nahida-knowledge-fri-iopps"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
      - "vault/05_Bridges/fri-iopps-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "uses"
    to: "nahida-knowledge-fraud-proofs"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
      - "vault/05_Bridges/fraud-proofs-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "bridges_to"
    to: "nahida-bridge-data-availability-to-sharded-ledgers"
    evidence_refs:
      - "vault/05_Bridges/data-availability-to-sharded-ledgers.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-sampling"
    relation: "bridges_to"
    to: "nahida-bridge-fraud-proofs-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fraud-proofs-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-data-availability-to-sharded-ledgers"
  - "nahida-bridge-fri-iopps-to-data-availability-sampling"
  - "nahida-bridge-fraud-proofs-to-data-availability-sampling"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
  - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
  - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
  - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
representative_source_refs:
  - "arxiv:1905.09274v4"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "arxiv:1809.09044v1"
query_keys:
  - "Data availability sampling"
  - "data-availability-sampling"
  - "DAS"
  - "data availability"
  - "FRIDA"
  - "FRI-based DAS"
  - "transparent data availability commitments"
  - "erasure code commitments"
  - "opening-consistency"
  - "expired blob retrieval"
  - "fair data exchange"
  - "fraud proofs"
  - "data availability proofs"
  - "2D Reed-Solomon DAS"
  - "codec fraud proofs"
aliases:
  - "DAS"
  - "data availability"
domains:
  - "blockchain-systems"
topics:
  - "data-availability-sampling"
  - "fri-iopps"
  - "erasure-code-commitments"
  - "fair-data-exchange"
  - "fraud-proofs"
  - "2d-reed-solomon"
  - "codec-fraud-proofs"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-21"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-11"
evidence_window_end: "2026-06-21"
created: "2026-06-20"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-consolidate-20260620-legacy-to-knowledge-migration"
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
  - "nahida-knowledge-20260620-atomic-fair-data-exchange"
  - "nahida-knowledge-20260621-fraud-proofs-data-availability"
source_refs:
  - "arxiv:1905.09274v4"
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "sha256:fbf32cf4ed7d85774f6509f0df27f4af5dc23ed0d2429e5622a318b75750d6c9"
  - "arxiv:1809.09044v1"
  - "doi:10.48550/arxiv.1809.09044"
confidence: "medium"
trust_tier: "primary"
---

# Data availability sampling

## 定义与范围

- 定义: Data availability sampling (DAS) 让轻客户端通过随机抽样和编码证明确认区块数据足够可用，而不下载完整数据。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `data-availability-sampling`
- Aliases/query keys: DAS, data availability
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `data-availability-sampling`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

LazyLedger、FRIDA 和 Fraud Proofs 是当前 DAS 算法/承诺/安全边界 source seeds。LazyLedger 提供 availability-only ledger、namespaced Merkle trees 与 client-side state sovereignty 的系统 seed；FRIDA 提供 transparent/no-trusted-setup DAS 的 proof-system route，把 opening-consistent FRI IOPPs 编译为 erasure-code commitments，再服务 light-client sampling；Fraud Proofs 提供 2D Reed-Solomon DAS、codec fraud proofs、missing-share detection probability 和“先可用、后可反证”的 light-client security boundary。Atomic and Fair Data Exchange via Blockchain 不是新的 DAS 构造，但它补上了 commitment 留存后的 retrieval/service-incentive 层: 过期 blob 或分散存储的数据如何被公平付费取回。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[data-availability-and-light-clients|data-availability-and-light-clients]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

在不要求全节点执行交易的情况下，让客户端获得数据可用性保证。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[data-availability-and-light-clients|data-availability-and-light-clients]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| gap | none | 当前没有拆出的 child node | existing-notes-only | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| erasure coding and random sampling | erasure coding and random sampling | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| namespaced Merkle tree inclusion/range proofs | namespaced Merkle tree inclusion/range proofs | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| availability-only ledger and client-side execution | availability-only ledger and client-side execution | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| 2D Reed-Solomon DAS with codec fraud proofs | 把 block data 扩展成 2k x 2k row/column-encoded matrix，light clients 抽样 shares；若 producer 错误生成 extended data，则用 row/column codec fraud proof 反驳。 | 需要 row/column roots 进入 dataRoot，且网络能让足够多 honest clients sampling/gossip。 | 不证明 execution validity；selective share disclosure 需要额外网络假设；codec proof size 随 axis length 增长。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| FRI/IOPP-derived erasure-code commitments | 将满足 opening-consistency 的 [[fri-iopps|FRI IOPPs]] 编译成 erasure-code commitments，再用 DAS transformation 支持 light-client random sampling。 | 需要 transparent/no-trusted-setup route，且优先优化 commitment/per-query light-client bandwidth。 | network encoding/storage 和 total reconstruction communication 可能更大；不证明交易执行 validity。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| post-commitment data retrieval incentives | 在数据承诺仍可验证但数据本体过期或分散时，用 FDE/VECK 让客户端公平购买正确数据或片段。 | EIP-4844 expired blobs、Danksharding fragments、archival data services。 | 不改变 DAS sampling soundness；服务定价、server griefing 和带宽 overhead 仍需独立处理。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | paper | 新增 transparent FRI-based DAS route: opening-consistent IOPP -> erasure-code commitment -> DAS | 不替代 validity/fraud proofs；network encoding size trade-off 明显；FRI foundation 仍需原始来源 | `§3-§5`, `Appendix A-C` |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 作为 DAS-adjacent source extension：为 EIP-4844/Danksharding 数据过期或分片后的公平检索提供 FDE/VECK route | 不是 DAS 算法；不证明 sampling 或 reconstruction soundness | `§1`, `§8`, `Appendix A.3` |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities]] | paper | 新增 2D RS DAS、codec fraud proof、single/multi-client detection probability 和 selective-disclosure boundary | 需要 honest full node/light-client sampling mass；2018 seed 不等同现代 Celestia/EIP-4844 deployment | `§5-§7` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-21`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-21`。
- 综合: DAS 目前由 LazyLedger、FRIDA 和 Fraud Proofs 三条算法/承诺/安全边界 source-backed seed 支撑。LazyLedger 强调 availability-only ledger、namespaced Merkle trees 和 client-side execution；FRIDA 强调 transparent/no-trusted-setup commitment/opening backend，用 FRI/batched FRI 的 opening-consistency 支撑 erasure-code commitments；Fraud Proofs 强调 2D Reed-Solomon sampling、row/column roots、codec fraud proofs 和 light-client sampling probability，并把 DAS 明确放在 fraud-proof security 的前置条件上。Atomic/Fair Data Exchange 不改变 DAS 的抽样定义，但把“承诺存在之后如何付费取回数据或片段”作为相邻问题补进来。四者共同说明 DA 方向至少有三个不同层次: 轻客户端如何确信数据可恢复，数据结构/承诺如何支持抽样与反证，以及数据过期/分散后如何被经济地服务。

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
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | source extension | 代表来源增量 | 当前综合/代表 Sources | no | keep linked |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | source extension + bridge trigger | transparent DAS via opening-consistent FRI IOPPs and erasure-code commitments | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route proof-system details through [[fri-iopps|FRI IOPPs]] and [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | adjacent source extension | expired blob / Danksharding fragment retrieval incentives; FDE as service layer after DA commitment | 方法族与解决路线; 代表 Sources; 当前综合 | no | keep core protocol in [[fair-data-exchange|Fair data exchange for committed data]] |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | source extension + bridge trigger | 2D RS DAS, codec fraud proofs, data-available-before-fraud-proof boundary | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route invalidity-detection details through [[fraud-proofs|Fraud proofs]] and [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[data-availability-to-sharded-ledgers|Data availability -> sharded ledgers]] | `blockchain-systems/data-availability-and-light-clients/data-availability-sampling; blockchain-systems/scaling-and-sharding/sharded-ledgers` | dependency, shared_pattern | Shard-level execution, cross-shard atomicity, and validator assignment from OmniLedger do not transfer directly to LazyLedger; LazyLedger's namespace/data-availability model does not by itself validate application state or solve shard execution. | active_seed |
| [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] | `zero-knowledge-proofs/proof-systems/fri-iopps; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | method_transfer, application, dependency, transparent_commitment_route | FRI proximity/opening-consistency transfers to the DAS commitment/opening layer; network sampling, reconstruction and execution-validity boundaries remain blockchain-specific. | active_seed |
| [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] | `blockchain-systems/data-availability-and-light-clients/fraud-proofs; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | dependency, complementarity, validation_boundary | DAS makes fraud proofs actionable by making data available; fraud proofs/codec proofs reject invalid transitions or malformed coding, not arbitrary DA service failures. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-data-availability-sampling | is_a | nahida-knowledge-data-availability-and-light-clients | vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/data-availability-sampling.md; vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md | medium | active_seed |
| nahida-knowledge-data-availability-sampling | evidenced_by | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | medium | active_seed |
| nahida-knowledge-data-availability-sampling | evidenced_by | vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md | FRIDA source note | high | active_seed |
| nahida-knowledge-data-availability-sampling | evidenced_by | vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md | Fraud Proofs source note | high | active_seed |
| nahida-knowledge-data-availability-sampling | applied_by | nahida-knowledge-fair-data-exchange | FDE source note | medium | active_seed |
| nahida-knowledge-data-availability-sampling | uses | nahida-knowledge-fri-iopps | FRIDA source note; bridge note | high | active_seed |
| nahida-knowledge-data-availability-sampling | uses | nahida-knowledge-fraud-proofs | Fraud Proofs source note; bridge note | high | active_seed |
| nahida-knowledge-data-availability-sampling | bridges_to | nahida-bridge-data-availability-to-sharded-ledgers | vault/05_Bridges/data-availability-to-sharded-ledgers.md | medium | active_seed |
| nahida-knowledge-data-availability-sampling | bridges_to | nahida-bridge-fri-iopps-to-data-availability-sampling | vault/05_Bridges/fri-iopps-to-data-availability-sampling.md | high | active_seed |
| nahida-knowledge-data-availability-sampling | bridges_to | nahida-bridge-fraud-proofs-to-data-availability-sampling | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Celestia、EIP-4844、DA committees 和现代 DAS deployment source 缺。 | Fraud Proofs 已补 2018 seed，但现代部署与参数实践仍缺。 | nahida-research-search or nahida-update | medium | queued |
| HASW23 Foundations of DAS and original FRI/DEEP-FRI sources 缺。 | FRIDA 依赖 HASW23 compiler，并只从应用论文侧给出 FRI foundation-thin seed。 | nahida-update or nahida-research-search | high | queued |
| DA retrieval/service incentives 目前只有 FDE seed。 | 影响“数据可用之后如何被持续服务”的经济层理解。 | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 3 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Added transparent FRI/IOPP-derived erasure-code-commitment route and bridge to FRI IOPPs. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Added FDE as an adjacent retrieval/service-incentive route for committed DA data. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Added 2D RS DAS, codec fraud proofs and the data-available-before-challenge boundary. | 1 source note | codex |
