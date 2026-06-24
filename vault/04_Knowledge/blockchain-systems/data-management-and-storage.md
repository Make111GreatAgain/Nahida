---
id: "nahida-knowledge-blockchain-data-management-and-storage"
title: "Blockchain Data Management and Storage"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "data-management-and-storage"
domain_id: "blockchain-systems"
direction_id: "data-management-and-storage"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
child_knowledge_refs:
  - "nahida-knowledge-blockchain-state-storage"
  - "nahida-knowledge-blockchain-query-processing-and-indexing"
  - "nahida-knowledge-blockchain-off-chain-application-data-management"
  - "nahida-knowledge-decentralized-storage-networks"
ontology_path:
  - "blockchain-systems"
  - "data-management-and-storage"
primary_ontology_path: "blockchain-systems/data-management-and-storage"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage"
relation_edges:
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "part_of"
    to: "nahida-knowledge-blockchain-systems"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems.md"
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-state-storage"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-query-processing-and-indexing"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing.md"
      - "vault/03_Sources/papers/sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-off-chain-application-data-management"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage/off-chain-application-data-management.md"
      - "vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "has_child"
    to: "nahida-knowledge-decentralized-storage-networks"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage/decentralized-storage-networks.md"
      - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-data-management-and-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage.md"
    confidence: "medium"
    status: "supporting_seed"
bridge_refs:
  - "vault/05_Bridges/storage-engines-to-blockchain-state-storage.md"
  - "nahida-bridge-blockchain-state-storage-to-transaction-processing"
  - "nahida-bridge-decentralized-storage-networks-to-contingent-service-payments"
source_note_refs:
  - "vault/03_Sources/papers/sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval.md"
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
  - "vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md"
  - "vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md"
representative_source_refs:
  - "sha256:e52dd885d13f5be90c84ff96c0b20110fbeb5b82f7236460bb348d28fb9a44f1"
  - "arxiv:2306.10739v1"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "doi:10.3846/jcem.2023.18646"
  - "arxiv:2208.09937"
query_keys:
  - "blockchain data management"
  - "blockchain query processing"
  - "blockchain analytics query processing"
  - "account-specific transaction retrieval"
  - "transaction retrieval query"
  - "blockchain indexing"
  - "probabilistic data structures"
  - "Multi-Set Multi-Membership Query"
  - "blockchain storage"
  - "blockchain state storage"
  - "authenticated state storage"
  - "blockchain provenance query"
  - "区块链数据管理"
  - "区块链状态存储"
  - "stateless blockchain storage"
  - "off-chain state storage"
  - "partial Merkle trie"
  - "RSA accumulator state digest"
  - "state-subset commitment"
  - "off-chain application data management"
  - "blockchain IPFS data management"
  - "on-chain metadata off-chain files"
  - "decentralized storage network"
  - "proof of storage"
  - "storage service incentives"
  - "Filecoin Sia Storj Swarm"
aliases:
  - "区块链数据管理与存储"
  - "Blockchain storage management"
  - "Blockchain state storage direction"
  - "Blockchain query processing"
  - "Blockchain analytics indexing"
  - "Blockchain application data management"
  - "Decentralized storage networks"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "blockchain storage"
  - "blockchain query processing"
  - "transaction retrieval indexes"
  - "state storage"
  - "authenticated indexes"
  - "provenance queries"
  - "stateless blockchain"
  - "off-chain storage"
  - "partial Merkle trie"
  - "state-subset commitment"
  - "RSA accumulator"
  - "off-chain application data"
  - "content-addressed assets"
  - "decentralized storage"
  - "proof of storage"
  - "storage service incentives"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-22"
evidence_window_end: "2026-06-23"
created: "2026-06-22"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-cole-blockchain-storage"
  - "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
  - "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
  - "nahida-knowledge-20260623-blockchain-ipfs-construction-data-management"
  - "nahida-knowledge-20260623-incentive-compatible-decentralized-storage"
  - "nahida-knowledge-20260623-blocksketch-transaction-retrieval"
source_refs:
  - "sha256:e52dd885d13f5be90c84ff96c0b20110fbeb5b82f7236460bb348d28fb9a44f1"
  - "arxiv:2306.10739v1"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "doi:10.3846/jcem.2023.18646"
  - "arxiv:2208.09937"
confidence: "high"
trust_tier: "primary"
---

# Blockchain Data Management and Storage

## 定义与范围

- 定义: `blockchain-systems/data-management-and-storage` 关注区块链系统如何组织、索引、持久化、证明和查询链上/链下数据，尤其是状态、历史版本、authenticated indexes、state roots、provenance queries、账户/交易历史检索，以及应用层大文件/数字资产的链上元数据与链下内容寻址管理。
- 不包含: 共识安全、mempool ordering、data availability sampling、跨链协议本身或普通数据库全部事务机制；这些通过父节点、邻节点或 bridge 连接。
- Canonical terms: `blockchain storage`, `state storage`, `authenticated state index`, `provenance query`
- Standalone completeness check: 本节点解释方向边界、问题、方法路线和下级结构；具体 source/system 细节留在 source note。
- Retrieval role: 当查询“区块链数据怎么存、历史状态怎么查、state root 怎么验证、为什么 MPT 膨胀、如何按账户/时间检索历史交易、链上只存 CID/hash 而文件放 IPFS/链下”时，先进入此方向，而不是误落到 consensus。
- Update scope: MPT/ForkBase/stateless clients/state expiry/state pruning/authenticated databases/blockchain indexes/source-specific storage engines、IPFS/content-addressed application assets 和链上元数据/链下文件工作流都可挂到本方向或子节点。

## 背景

source_backed_background: `COLE` 暴露了当前 vault 中缺失的一条区块链系统方向: 全节点不只需要共识和执行，还需要能长期保存、索引、验证和查询状态历史的 storage layer。它显示 MPT-style authenticated indexes 会让历史 index nodes 成为存储主成本，而普通 learned index/LSM 机制直接迁移到区块链时又必须处理 integrity、provenance 和 state-root determinism。`BlockSketch` 补入另一条 query/indexing route: 区块链分析经常按账户和时间范围检索交易所在区块，不能总靠全链扫描或完整 off-chain database 同步；它把该问题建模为 MS-MMQ，并用 Bloom filter + Sketch 的冷热账户窗口索引降低误报与内存成本。`SlimChain` 补充了同一方向的另一条路线: 不优化所有节点的历史索引，而是把 full state/full transactions 移到 off-chain storage nodes，让 consensus nodes 只保留 transaction digests 和 state roots。`L2chain` 补入 accumulator commitment route: L1 只维护 available-state digest，DApp executors 用 membership witness split/merge 受影响状态子集。`Blockchain + IPFS construction data management` 再补入应用层路线: 对照片、视频、BIM/as-built assets 等大对象，链上保存业务元数据和 CID，链下用 private IPFS/IPFS-Cluster 负责内容寻址、复制、pinning 和生命周期管理。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction`。
- 为什么足够通用: 它承接多类 source 的共同问题: 状态存储、authenticated indexes、历史版本、proofs、pruning、query integrity、存储引擎迁移，以及应用大对象的链上/链下拆分。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `COLE` 只是第一个强 source；方向本身能容纳 MPT、ForkBase、state expiry、stateless clients、authenticated query systems、IPFS/content-addressed asset workflows 等未来来源。
- 需要引用的更基础 Knowledge: [[04_Knowledge/blockchain-systems|Blockchain systems]] 与 [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]。
- 不应拆出的实例/来源: COLE、COLE*、MPT、LIPP、CMI 当前默认作为 source/system instance 或方法路线，不直接升格为独立基础概念。

## 解决的问题

- 全节点如何保存随区块增长的状态和历史版本。
- 状态索引如何同时支持 point lookup、历史/provenance range query 和可验证证明。
- 交易历史如何支持按账户、时间范围、事件或合约的高效查询，而不是依赖全链扫描或完整链外同步。
- 存储结构如何把 state root digest 与内部 compaction/merge/flush 保持一致。
- 数据库存储引擎技术如何迁移到区块链场景，同时不破坏 integrity、determinism 和 proof completeness。
- 当 consensus nodes 不保存 full state 时，off-chain storage、proofs 和 partial commitments 如何支撑交易验证与提交。
- 当应用有照片、视频、BIM、文档等大对象时，哪些内容应留链上，哪些内容应放链下，以及 CID/hash、pinning、权限和生命周期如何组合。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems|Blockchain systems]] | `part_of` | COLE source note; blockchain storage problem | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain state storage]] | problem | 状态存储同时涉及 authenticated index、历史版本、state root、provenance query 和存储引擎迁移，足以成为可复用 problem node | COLE §1-§8 | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-query-processing-and-indexing|Blockchain query processing and indexing]] | problem | 账户/交易历史查询需要独立的数据访问路径、误报/内存/同步权衡和查询验证边界，不应混入 consensus 或 state storage | BlockSketch | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/off-chain-application-data-management|Off-chain application data management]] | problem | 应用大文件和数字资产需要链上元数据/CID 与链下内容寻址存储协同，不应混入 state storage 或 consensus | Blockchain + IPFS construction data management | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/decentralized-storage-networks|Decentralized Storage Networks]] | problem / application area | 外包存储市场需要证明 provider 保存/返回数据，并把 premium、collateral、challenge cost、request pricing 和争议处理接到链上结算。 | ICM-DSN | active_seed |
| Authenticated blockchain query systems | candidate | 当前只有 COLE 的 provenance query 和 Blockchain Meets Database 的 provenance signal；需更多 authenticated SQL/query source | COLE; Blockchain Meets Database | queued |
| State pruning / stateless clients / state expiry | candidate | 这是区块链存储压力的另一条路线；SlimChain 给出 stateless consensus/storage split 信号，但还不是完整 stateless-client foundation。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Authenticated trie/state root storage | 用 Merkleized index 直接认证当前状态和证明路径 | 需要简单 state root 和 membership proof | 历史更新路径节点会膨胀；长期 archival storage 压力大 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] 背景/MPT 对比 |
| Column-based historical state storage | 按状态 key 聚拢历史版本，把 `<addr, blk>` 作为可排序 compound key | 需要 provenance/range history query 和更小历史索引 | fork/rewind 支持仍缺；proof size 对小区间可能不占优 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| Storage-engine mechanism reuse | 将 learned index、LSM-like runs、Bloom filters、Merkle files 和 async merge 引入区块链 state storage | full-node storage/index bottleneck 明显 | 必须重新处理 state root determinism、proof completeness 和 integrity boundary | [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] |
| Account-centric probabilistic query indexing | 将账户交易检索建模为 MS-MMQ，用 Bloom filter、Sketch、冷热账户分类和时间窗口树减少误报、内存和同步开销 | 需要按账户/时间查历史或近期交易，且账户访问呈 power-law 分布 | 低频账户可能不如专用 sketch；Bloom/Sketch 组合需要 re-entry 避免 false negative；不是查询完整性证明 | [[sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval|BlockSketch]] |
| Stateless consensus storage with off-chain full state | consensus nodes 只保留 state root/transaction digests；storage nodes 保存 full state 并提供 read/write proofs 和 write proofs。 | 希望降低 consensus-node storage/execution burden 的 smart-contract blockchain。 | 依赖 execution proof、storage-node availability、proof compression 和 recent-window metadata；不等于 DA 或 consensus sharding。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] |
| Accumulator state-subset commitments | L1 只维护 available-state digest，DApp executors 通过 RSA accumulator witness split 出状态子集并在处理后 merge 回摘要。 | L2 DApp execution 需要减少 L1 状态/交易内容暴露，同时允许不同状态子集并行。 | 依赖 TEE、accumulator witness cache 和 split conflict resolution；不是通用存储引擎或 DA 方案。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] |
| On-chain metadata with off-chain application assets | 链上保存业务元数据、版本、时间戳、权限和 CID；链下保存照片、视频、BIM、文档等大对象。 | 多组织应用需要可审计工作流，但数据本体太大不适合写入 block。 | CID 只绑定内容，不保证可用性；需要 pinning/replication/GC 和访问控制。 | [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Blockchain + IPFS construction data management]] |
| Decentralized storage service incentives | 用 storage contract、proof of storage、collateral 和 challenge path 组织陌生 storage provider 的存储/检索服务。 | 客户端外包数据给 DSN provider，且希望减少持续证明成本。 | 单篇 source seed；oracle trust、PoR foundation 和真实 Filecoin/Sia/Storj 对照仍缺。 | [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | paper | 首次建立 blockchain data-management/storage 方向和 state-storage problem node；提供 column-based learned storage、Merkle files、checkpoint async merge 和 provenance proof 路线 | non-forking blockchain；不支持 rewind；single paper/source; artifact repo 未分析 | Abstract, §1-§8 |
| [[sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval|BlockSketch: A Hybrid Tree-based Sketch for Account-Specific Transaction Retrieval Query]] | paper | 建立 blockchain query-processing/indexing problem node；提供 account-specific transaction retrieval、MS-MMQ、Bloom/Sketch 热冷账户索引和窗口缓存路线 | venue/DOI unknown in local PDF；不是 authenticated query proof；single source seed | Abstract, §II-§V |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | paper | 补入 stateless/off-chain full-state route：state commitments、partial Merkle trie 和 storage-layer sharding 如何支撑交易提交 | SGX-centered prototype；storage-node availability/incentives unresolved；storage sharding does not shard consensus | p1-p13 |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | paper | 补入 accumulator state-subset commitment route：available-state digest 可被 split/merge 来支撑 L2 DApp execution。 | TEE trust; accumulator witness overhead; not a DA/rollup foundation | p1-p14 |
| [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Decentralized System for Construction Projects Data Management Using Blockchain and IPFS]] | paper | 补入 application-data route：Fabric 链上记录进度/资产元数据和 IPFS CID，private IPFS/IPFS-Cluster 管理视觉/as-built 大对象 | construction case study；CFT Fabric assumption；manual data capture；availability depends on private cluster operations | p1-p18 |
| [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|An Incentive-Compatible Mechanism for Decentralized Storage Network]] | paper | 补入 DSN route：持续 PoS 成本、service-denial attack、challenge-based verification、smart-contract/oracle storage contract 和 request counting | single source seed；PoS/PoR/Filecoin/Sia/Storj foundation 仍缺；oracle boundary 未深入 | p1-p13 |

## 当前综合

- Evidence window: `2026-06-22` to `2026-06-23`。
- Freshness: `fresh` for new source-backed seed; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 当前本方向是 COLE 引出的 active_seed，并由 BlockSketch、SlimChain、L2chain、Blockchain + IPFS construction data management 和 ICM-DSN 补强。COLE 把区块链系统中的“数据怎么存”从 execution/consensus 中拆出来，强调 full-node state history、authenticated index、state root digest、provenance proof 和 storage-engine mechanism reuse 是独立问题。BlockSketch 把“历史交易怎么查”拆成 query-processing/indexing 子问题：账户检索既不能等同于 state storage，也不能误归入 consensus；其关键权衡是内存、同步、误报、热点账户和时间窗口。SlimChain 显示另一路 storage pressure response: 让 consensus nodes 保持 state-root-only/stateless，把 full state 和 full transaction data 移到 off-chain storage nodes，再用 proofs 和 partial Merkle trie 支持 transaction commit。L2chain 显示 state commitment 也可以为 L2 execution 主动设计：available-state digest 可被 split/merge，状态子集证明直接参与交易处理。Blockchain + IPFS construction data management 说明应用大对象需要链上元数据和链下内容寻址存储共同管理。ICM-DSN 再补入外包存储市场 route：当数据交给陌生 provider 时，关键问题变成 proof frequency、retrieval service availability、premium/collateral 和 challenge/dispute 激励，而不是 consensus。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | 新建 blockchain data-management/storage 方向，并把 COLE 从 queue 的 consensus path 纠正到 state storage path | 定义、下级结构、方法族、代表 Sources、Bridge Links | yes | 后续吸收 MPT/ForkBase/stateless/state expiry/authenticated query sources |
| [[sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval|BlockSketch]] | 新建 blockchain query-processing/indexing problem node，并把 BlockSketch 从 queue 的 consensus path 纠正到 account-specific transaction retrieval path。 | 定义、下级结构、方法族、代表 Sources、当前综合 | yes, creates query/indexing child | 后续吸收 EtherQL/The Graph/BlockSci/authenticated query/probabilistic-data-structure sources |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | 补入 stateless/off-chain full-state route，并建立 state-storage 与 transaction-processing 的 bridge。 | 背景、解决的问题、方法族、代表 Sources、Bridge Links | no new direction child | 后续吸收 stateless clients/Verkle/state expiry/storage incentives 后复核 child split |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | 补入 accumulator state-subset commitment route，并强化 state-storage 与 transaction-processing 的 bridge。 | 背景、方法族、代表 Sources、当前综合、Bridge Links | no new direction child | 后续吸收 RSA accumulator 和 L2/rollup foundation 后复核 child split |
| [[doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs|Blockchain + IPFS construction data management]] | 补入链上元数据/链下应用大对象 route，并纠正 queue 的 consensus 误分类。 | 定义、下级结构、方法族、代表 Sources、当前综合 | yes, creates application-data child | 后续吸收 IPFS/Filecoin/Arweave 或其他大对象应用 source 后复核 child split |
| [[arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network|ICM-DSN]] | 补入 decentralized-storage-networks route，并纠正 queue 的 consensus 误分类。 | 定义、下级结构、方法族、代表 Sources、Bridge Links | yes, creates DSN child | 后续吸收 Filecoin/Sia/Storj/Swarm 和 PoS/PoR foundation source |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] | `distributed-systems/data-management-and-storage/storage-engines` -> `blockchain-systems/data-management-and-storage/blockchain-state-storage` | method_translation | learned index/LSM/Bloom/Merkle mechanisms transfer; consensus safety, DA, fork/rewind, state-root determinism do not transfer automatically | active_seed |
| [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage` -> `blockchain-systems/execution-and-transactions/transaction-processing` | dependency, shared_state_commitment, implementation_reuse, tension | state commitment/proof format constrains validation and commit; storage does not provide execution correctness or consensus safety by itself | active_seed |
| [[decentralized-storage-networks-to-contingent-service-payments|Decentralized storage networks -> contingent service payments]] | `blockchain-systems/data-management-and-storage/decentralized-storage-networks` -> `blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | application, shared_pattern, tension | storage proof/service availability can inform service-payment disputes; fair payment does not by itself guarantee storage or oracle availability | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-data-management-and-storage | part_of | nahida-knowledge-blockchain-systems | COLE source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | has_child | nahida-knowledge-blockchain-state-storage | COLE source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | has_child | nahida-knowledge-blockchain-query-processing-and-indexing | BlockSketch source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | has_child | nahida-knowledge-blockchain-off-chain-application-data-management | Blockchain + IPFS construction data-management source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | has_child | nahida-knowledge-decentralized-storage-networks | ICM-DSN source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md | COLE source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md | SlimChain source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md | L2chain source note | medium | supporting_seed |
| nahida-knowledge-blockchain-data-management-and-storage | evidenced_by | vault/03_Sources/papers/doi-10-3846-jcem-2023-18646-decentralized-system-construction-projects-data-management-blockchain-ipfs.md | Blockchain + IPFS construction data-management source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | evidenced_by | vault/03_Sources/papers/arxiv-2208-09937-incentive-compatible-mechanism-decentralized-storage-network.md | ICM-DSN source note | high | active_seed |
| nahida-knowledge-blockchain-data-management-and-storage | evidenced_by | vault/03_Sources/papers/sha256-e52dd885d13f-blocksketch-account-specific-transaction-retrieval.md | BlockSketch source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| MPT/state trie foundation source 缺失 | 当前 MPT 只作为 COLE 背景出现，缺少独立 source-backed 解释 | `nahida-research-search` or future source | high | queued |
| Fork/rewind/state reorg storage route 缺失 | COLE 明确不支持 rewind，但实际区块链常有 reorg | future paper/repo intake | high | queued |
| Stateless clients/state expiry/state pruning 未吸收 | SlimChain 给出 stateless consensus/storage split，但还缺 stateless-client/state-expiry foundation source | `nahida-research-search` | medium | queued |
| Learned index 基础节点缺失 | COLE 的 learned index 只作为 source method，可复用概念还没建 | future PGM/ALEX/LIPP source | medium | queued |
| 区块链 query/indexing 直接来源不足 | BlockSketch 已建 account-specific retrieval seed，但 EtherQL/The Graph/BlockSci/authenticated query systems 还只是相关工作信号 | future paper/repo/web intake | high | queued |
| Probabilistic data structures 基础节点缺失 | BlockSketch 使用 Bloom filter、Sketch、RAMBO、CSC 和 MS-MMQ，但这些还没有独立 foundation/source-backed method node | `nahida-research-search` or future source | medium | queued |
| IPFS/content-addressed application storage 基础来源缺失 | 当前 IPFS/IPFS-Cluster 只由应用论文支撑，缺少独立基础概念或仓库/文档 source | `nahida-research-search` or future repo/source intake | medium | queued |
| Filecoin/Sia/Storj/Swarm 和 PoS/PoR foundation sources 缺失 | ICM-DSN 创建 DSN 子节点，但 related-work landscape 和 proof semantics 仍需要直接来源支撑 | `nahida-update` or `nahida-research-search` | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-cole-blockchain-storage | Created blockchain data-management/storage direction and attached COLE as first representative source. | arxiv:2306.10739v1 | codex |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Added SlimChain as stateless/off-chain storage route and linked storage commitments to transaction processing. | doi:10.14778/3476249.3476283 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Added L2chain as accumulator state-subset commitment route and strengthened state-storage bridge. | doi:10.14778/3574245.3574278 | codex |
| 2026-06-23 | nahida-knowledge-20260623-blockchain-ipfs-construction-data-management | Added off-chain application data-management child for on-chain metadata and off-chain content-addressed assets. | doi:10.3846/jcem.2023.18646 | codex |
| 2026-06-23 | nahida-knowledge-20260623-incentive-compatible-decentralized-storage | Added decentralized-storage-networks child for DSN storage-service incentives and challenge-based proof verification. | arxiv:2208.09937 | codex |
| 2026-06-23 | nahida-knowledge-20260623-blocksketch-transaction-retrieval | Added blockchain query-processing/indexing child for account-specific transaction retrieval and corrected BlockSketch away from consensus. | sha256:e52dd885d13f5be90c84ff96c0b20110fbeb5b82f7236460bb348d28fb9a44f1 | codex |
