---
id: "nahida-knowledge-data-availability-and-light-clients"
title: "Data availability and light clients"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "data-availability-and-light-clients"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
child_knowledge_refs:
  - "nahida-knowledge-data-availability-sampling"
  - "nahida-knowledge-fraud-proofs"
  - "nahida-knowledge-fair-data-exchange"
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-systems"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
      - "vault/04_Knowledge/blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "has_child"
    to: "nahida-knowledge-data-availability-sampling"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/data-availability-sampling.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "has_child"
    to: "nahida-knowledge-fair-data-exchange"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fair-data-exchange.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "has_child"
    to: "nahida-knowledge-fraud-proofs"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md"
      - "vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fraud-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "bridges_to"
    to: "nahida-bridge-fri-iopps-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fri-iopps-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "bridges_to"
    to: "nahida-bridge-kzg-commitments-to-fair-data-exchange"
    evidence_refs:
      - "vault/05_Bridges/kzg-commitments-to-fair-data-exchange.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-data-availability-and-light-clients"
    relation: "bridges_to"
    to: "nahida-bridge-fraud-proofs-to-data-availability-sampling"
    evidence_refs:
      - "vault/05_Bridges/fraud-proofs-to-data-availability-sampling.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-fri-iopps-to-data-availability-sampling"
  - "nahida-bridge-kzg-commitments-to-fair-data-exchange"
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
  - "Data availability and light clients"
  - "data-availability-and-light-clients"
  - "data availability"
  - "light clients"
  - "FRI-based data availability"
  - "transparent DAS"
  - "FRIDA"
  - "fair data exchange"
  - "FDE"
  - "expired blob retrieval"
  - "fraud proofs"
  - "light-client fraud proofs"
  - "data availability proofs"
aliases:
  - "data availability"
  - "light clients"
domains:
  - "blockchain-systems"
topics:
  - "data-availability-and-light-clients"
  - "data-availability-sampling"
  - "fair-data-exchange"
  - "fri-iopps"
  - "fraud-proofs"
  - "light-client-security"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
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

# Data availability and light clients

## 定义与范围

- 定义: Data availability and light clients 关注客户端如何在不执行或下载所有交易的情况下确认数据已经发布且可恢复。
- 不包含: 单篇论文、单个协议实例、一次实验结果或某个仓库模块的局部细节；这些留在 `03_Sources` source note 或本节点的 Source Extensions 行里。
- Canonical terms: `data-availability-and-light-clients`
- Aliases/query keys: data availability, light clients
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 `data-availability-and-light-clients`，再按需打开少量 source notes。
- Update scope: 新 source 若改变定义、方法族、代表 source、bridge 或 open problem，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

当前 evidence seed 来自 LazyLedger、FRIDA、Atomic and Fair Data Exchange via Blockchain 和 Fraud Proofs。LazyLedger 的核心是 availability-only ledger、erasure coding、random sampling 和 namespaced Merkle trees；FRIDA 的核心是用 opening-consistent FRI IOPPs 构造 transparent erasure-code commitments，让 light clients 在无 trusted setup 的前提下降低 commitment/per-query overhead；FDE 新增的是已承诺数据的付费检索/服务激励路线，尤其适用于 EIP-4844/Danksharding 这类 commitment 留存但 blob data 可能过期或分散存储的场景；Fraud Proofs 则补上 light clients 在 dishonest majority 下如何依靠 fraud proofs + DAS 拒绝无效区块的安全边界。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction` / `direction`。
- 为什么足够通用: 它组织多个 source、legacy map/concept/synthesis 或未来 query 路径，而不是复述单篇论文。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: 具体 source 只作为 representative source 或 source extension。
- 需要引用的更基础 Knowledge: [[blockchain-systems|blockchain-systems]]。
- 不应拆出的实例/协议/来源: Raft、PBFT、Tendermint、Casper、Cobalt、Stratus、Nova、LegoSNARK、Geppetto 等默认作为 source/representative instance，除非后续多来源证明需要独立 protocol-instance 节点。

## 解决的问题

把数据发布/可用性与执行正确性分离，让轻客户端或 client-side applications 只验证必要的可用性和命名空间证明。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-systems|blockchain-systems]] | child_of | legacy hierarchy and source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[data-availability-sampling|data-availability-sampling]] | child | split gate passed or legacy migration target | legacy map/concept/synthesis | active_seed |
| [[fraud-proofs|Fraud proofs]] | child | light-client invalidity detection 是可复用机制；它依赖 DA，但不等同于 DAS | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | active_seed |
| [[fair-data-exchange|Fair data exchange for committed data]] | child | 已承诺数据的服务访问/付费检索是独立问题，不等同于 DAS 抽样算法 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| data availability sampling | data availability sampling | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| erasure coding | erasure coding | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| namespaced Merkle trees | namespaced Merkle trees | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| client-side state sovereignty | client-side state sovereignty | existing-notes-only seed | 证据有限，需后续 source 扩展 | source-backed or model_prior_background |
| fraud-proof-backed light-client security | 让 full nodes 对无效状态转换或错误编码生成短反证，light clients 验证后拒绝 block/header。 | 至少一个 honest full node 能看到数据并传播 proof；block data 必须 available。 | 需要 DAS、anti-eclipse、sampling/gossip 假设；absence of fraud proof 不自动等于 validity。 | [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] |
| transparent FRI-based DAS commitments | 用 [[fri-iopps|FRI IOPPs]] 的 folding/query/opening-consistency machinery 生成 DAS 所需的 erasure-code commitments。 | 需要 light-client availability assurance，且希望避免 KZG-style trusted setup。 | 不证明 execution validity；FRIDA 的 network encoding size 较大。 | [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA]] |
| committed-data fair exchange | 用 VECK 证明 ciphertext 加密了承诺下的数据，再让链上合约或 adaptor signature 只负责 payment/key-release 原子性。 | 客户端持有短承诺，服务器持有数据或片段，需要按下载/服务收费。 | 链下 proof/bandwidth 开销仍大；服务定价和 server griefing 仍是开放问题。 | [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts|LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts]] | paper | 作为本节点的 source extension / representative evidence | 仅代表已读 source 的覆盖，不等同完整领域综述 | `source note` |
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | paper | 新增 transparent/no-trusted-setup DAS commitment route，补充 light-client bandwidth vs network storage trade-off | 不替代 execution validity/fraud proofs；FRI foundation 仍薄 | `§3-§5` |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | paper | 新增 committed-data paid retrieval route：FDE/VECK/payment-for-key atomicity，可服务 expired blob 和 Danksharding fragments | 不改写 DAS 抽样算法；VECK/fair exchange foundation 仍需更多 source | `§1`, `§3-§8`, `Appendix B-C` |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs: Maximising Light Client Security and Scaling Blockchains with Dishonest Majorities]] | paper | 新增 fraud proofs + data availability proofs route：state transition fraud proofs、2D RS DAS、codec fraud proofs 和 light-client security assumptions | 需要 honest full node、honest light-client sampling mass、bounded delay、anti-eclipse；现代 rollup/Celestia source 仍缺 | `§3-§7` |

## 正反例约束

- 正确: 本节点完整解释一个可复用概念/方向/问题；论文、仓库、网页只是 evidence/source extension。
- 正确: 引用其他基础概念时，给出本地短定义和明确链接；被引用笔记本身完整。
- 错误: 本节点只有一个 source summary，缺少定义、背景、边界、方法族和当前综合。
- 错误: 把 Raft、Groth16、某仓库模块、单次实验结果当成基础概念，除非它们被明确标为 protocol/repository/source instance。

## 当前综合

- Evidence window: `2026-06-11` to `2026-06-21`，仅覆盖当前 vault 已有 source/legacy notes。
- Freshness: `fresh` for migration structure; not a latest-news claim.
- Valid until: `2026-07-21`。
- 综合: 当前 direction 由 LazyLedger、FRIDA、FDE 和 Fraud Proofs 四类证据支撑。LazyLedger 把 execution 移到 client side，并用 namespaced Merkle tree 和 sampling 组织 availability-only ledger；FRIDA 把 proof-system 方法引入 DAS commitment/opening 层，用 opening-consistent FRI/batched FRI 得到 transparent erasure-code commitments；Atomic/Fair Data Exchange 把问题推进到服务层: 当承诺仍存在而数据可能过期、分散或由 archive servers 持有时，客户端如何公平地为正确数据或片段付款；Fraud Proofs 则补齐 invalidity-detection 层: light clients 不能只相信 header，也不能只等待 fraud proof，必须先保证数据可用，才能让 honest full nodes 构造状态转换或编码错误的反证。这个方向仍然不等于 validity proof 或 rollup execution proof；它关注的是 block contents 是否可恢复、可验证、可经济地获得，以及 light-client/network 的带宽、存储、setup、反证和激励 trade-off。

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
| [[sha256-1a035420215b-frida-data-availability-sampling-from-fri|FRIDA: Data Availability Sampling from FRI]] | source extension | transparent FRI/IOPP route for DAS and erasure-code commitments | 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route technical details through [[data-availability-sampling|Data availability sampling]] and [[fri-iopps|FRI IOPPs]] |
| [[sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain|Atomic and Fair Data Exchange via Blockchain]] | source extension + child split trigger | committed-data paid retrieval, VECK, payment/key-release atomicity, expired blob and Danksharding fragment service incentives | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[fair-data-exchange|Fair data exchange for committed data]] and [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] |
| [[arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security|Fraud Proofs]] | source extension + child split trigger | fraud proofs as reusable light-client invalidity-detection mechanism; DAS dependency and codec fraud proofs | 下级结构; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | route details through [[fraud-proofs|Fraud proofs]] and [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] | `zero-knowledge-proofs/proof-systems/fri-iopps; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | method_transfer, application, dependency, transparent_commitment_route | Proof-system machinery transfers to the DAS commitment/opening layer, not to blockchain execution validity. | active_seed |
| [[kzg-commitments-to-fair-data-exchange|KZG commitments -> fair data exchange]] | `zero-knowledge-proofs/polynomial-commitments/kzg-commitments; blockchain-systems/data-availability-and-light-clients/fair-data-exchange` | dependency, application, cryptographic_enabler | KZG commitment/opening supports committed-data correctness and selective retrieval; payment fairness comes from VECK + blockchain key release. | active_seed |
| [[fraud-proofs-to-data-availability-sampling|Fraud proofs -> data availability sampling]] | `blockchain-systems/data-availability-and-light-clients/fraud-proofs; blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | dependency, complementarity, validation_boundary | Fraud proofs require available data before honest challengers can prove invalidity; DAS does not prove execution validity. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-data-availability-and-light-clients | is_a | nahida-knowledge-blockchain-systems | vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md; vault/04_Knowledge/blockchain-systems.md | medium | active_seed |
| nahida-knowledge-data-availability-and-light-clients | has_child | nahida-knowledge-data-availability-sampling | vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients.md; vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/data-availability-sampling.md | medium | active_seed |
| nahida-knowledge-data-availability-and-light-clients | has_child | nahida-knowledge-fair-data-exchange | vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fair-data-exchange.md | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | has_child | nahida-knowledge-fraud-proofs | vault/04_Knowledge/blockchain-systems/data-availability-and-light-clients/fraud-proofs.md | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | evidenced_by | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | vault/03_Sources/papers/arxiv-1905-09274v4-lazyledger-data-availability-ledger-client-side-smart-contracts.md | medium | active_seed |
| nahida-knowledge-data-availability-and-light-clients | evidenced_by | vault/03_Sources/papers/sha256-1a035420215b-frida-data-availability-sampling-from-fri.md | FRIDA source note | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | evidenced_by | vault/03_Sources/papers/sha256-fbf32cf4ed7-atomic-and-fair-data-exchange-via-blockchain.md | FDE source note | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | evidenced_by | vault/03_Sources/papers/arxiv-1809-09044v1-fraud-proofs-maximising-light-client-security.md | Fraud Proofs source note | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | bridges_to | nahida-bridge-fri-iopps-to-data-availability-sampling | bridge note | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | bridges_to | nahida-bridge-kzg-commitments-to-fair-data-exchange | bridge note | high | active_seed |
| nahida-knowledge-data-availability-and-light-clients | bridges_to | nahida-bridge-fraud-proofs-to-data-availability-sampling | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| optimistic rollup fraud proofs、validity proofs、Celestia docs/papers、EIP-4844/data blobs 缺 source。 | Fraud Proofs 已补入早期 light-client seed，但现代工程路径与 deployment evidence 仍薄。 | nahida-research-search or nahida-update | medium | queued |
| HASW23 Foundations of DAS、original FRI/DEEP-FRI 和 DA deployment sources 缺。 | FRIDA 引入 transparent commitment route，但还需要基础与部署侧来源校准。 | nahida-update or nahida-research-search | high | queued |
| Fair exchange / verifiable encryption / DA service markets 仍只有 FDE 一篇 seed。 | 影响付费检索、VECK、server griefing 和 pricing route 的成熟度判断。 | nahida-update | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-consolidate-20260620-legacy-to-knowledge-migration | Legacy concept/map/synthesis content migrated into current `04_Knowledge` architecture. | 1 source notes; 1 legacy notes | codex |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Added FRIDA as transparent/no-trusted-setup DAS commitment route and linked to FRI IOPPs. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-atomic-fair-data-exchange | Added committed-data fair exchange topic and KZG bridge from 2024/418. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-fraud-proofs-data-availability | Added Fraud Proofs as a reusable light-client invalidity-detection method family and linked it to DAS. | 1 source note | codex |
