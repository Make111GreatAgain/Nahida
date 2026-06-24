---
id: "nahida-knowledge-blockchain-state-storage"
title: "Blockchain State Storage"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "blockchain-state-storage"
domain_id: "blockchain-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "blockchain-state-storage"
  - "authenticated-state-indexing"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-data-management-and-storage"
child_knowledge_refs: []
ontology_path:
  - "blockchain-systems"
  - "data-management-and-storage"
  - "blockchain-state-storage"
primary_ontology_path: "blockchain-systems/data-management-and-storage/blockchain-state-storage"
secondary_ontology_paths:
  - "distributed-systems/data-management-and-storage/storage-engines"
relation_edges:
  - from: "nahida-knowledge-blockchain-state-storage"
    relation: "part_of"
    to: "nahida-knowledge-blockchain-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-state-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-state-storage"
    relation: "bridged_from"
    to: "nahida-knowledge-storage-engines"
    evidence_refs:
      - "vault/05_Bridges/storage-engines-to-blockchain-state-storage.md"
      - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-state-storage"
    relation: "bridges_to"
    to: "nahida-bridge-blockchain-state-storage-to-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md"
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-state-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-state-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
      - "vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "vault/05_Bridges/storage-engines-to-blockchain-state-storage.md"
  - "nahida-bridge-blockchain-state-storage-to-transaction-processing"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
representative_source_refs:
  - "arxiv:2306.10739v1"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
query_keys:
  - "blockchain state storage"
  - "blockchain state index"
  - "authenticated state storage"
  - "Merkle state index"
  - "MPT storage overhead"
  - "COLE blockchain storage"
  - "state provenance query"
  - "区块链状态存储"
  - "stateless blockchain"
  - "off-chain state storage"
  - "partial Merkle trie"
  - "on-chain state commitment"
  - "RSA accumulator state digest"
  - "available state digest"
  - "split-execute-merge state commitment"
  - "L2chain state digest"
aliases:
  - "区块链状态存储"
  - "Authenticated blockchain state storage"
  - "Blockchain state indexing"
domains:
  - "blockchain-systems"
  - "distributed-systems"
topics:
  - "blockchain state storage"
  - "authenticated indexes"
  - "provenance queries"
  - "learned indexes"
  - "LSM-tree maintenance"
  - "stateless blockchain"
  - "off-chain storage"
  - "partial Merkle trie"
  - "RSA accumulator"
  - "state-subset digest"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
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
source_refs:
  - "arxiv:2306.10739v1"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
confidence: "high"
trust_tier: "primary"
---

# Blockchain State Storage

## 定义与范围

- 定义: Blockchain state storage 是区块链全节点保存、索引、验证和查询链上状态及其历史版本的问题层。它关注状态如何落盘、state root 如何承诺当前存储结构、历史版本如何查询并证明完整性，以及存储引擎技术如何适配区块链的可验证和确定性边界。
- 不包含: 共识协议、交易排序、data availability sampling、跨链消息协议或普通数据库所有查询优化；这些是邻层或 bridge endpoint。
- Canonical terms: `blockchain state storage`, `authenticated state index`, `state root`, `provenance query`
- Standalone completeness check: 本节点本地解释问题、方法路线、边界和 source delta；COLE 的 algorithm/evaluation 细节留在 source note。
- Retrieval role: 当问题是“状态/MPT/历史查询/存储膨胀/可验证状态索引”时，先读本节点，再按需打开 COLE。
- Update scope: MPT、Verkle trie、ForkBase、state pruning、state expiry、stateless clients、authenticated databases、blockchain query indexes、storage-engine optimized state backends。

## 背景

source_backed_background: COLE 说明全节点的存储压力不一定来自 raw state values，而可能主要来自 authenticated state index 的历史版本。MPT 通过持久化更新路径保留历史 integrity/provenance，但每次更新都复制 path nodes；在长链上，这会让 index storage 成为主瓶颈。普通存储引擎能提供更紧凑的 layout/index/merge，但区块链还要求 state root digest、proof completeness 和节点间确定性。SlimChain 补充另一条路线: consensus nodes 可以只保存 transaction digests 和 state roots，而 full state/MPT 与 full transactions 由 off-chain storage nodes 保存；此时 state storage 不只是落盘结构，还决定 transaction validation 需要哪些 read/write proofs 和 partial commitment updates。L2chain 再补一条 route: L1 只维护可用状态摘要，DApp executors 用 RSA accumulator 将受影响状态子集 split 出去、离线执行后再 merge 回来；因此 commitment format 直接决定 L2 DApp transaction processing 能否并行。

## 解决的问题

- 如何在长期运行的全节点中保存 current state 与历史版本。
- 如何让 point lookup 和 provenance/range history query 都能被 state root 验证。
- 如何减少 MPT-style path-copying 的历史 index overhead。
- 如何引入 learned index、LSM-like merge、Bloom filters 等存储引擎机制，同时保持 proof 和 state digest。
- 如何处理后台 merge/compaction 对区块链节点间一致性的影响。
- 如何在 stateless consensus node 不保存 full state 时，用 authenticated proof 和 partial state structure 支持交易提交。
- 如何把状态摘要设计成可 split/merge 的子集 commitment，让 L2 DApp 执行并行处理不同状态集合。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]] | `part_of` | COLE §1-§3 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Merkleized state tries | candidate method child | MPT/Verkle 等 state commitment route 需要专门 source 支撑 | COLE background only | queued |
| Column-based authenticated state history | method section | 当前只有 COLE 一篇 source，先保留在本节点方法段 | COLE §3-§6 | section |
| Stateless commitments / off-chain state storage | method/problem candidate | SlimChain 已直接显示 consensus-state slimming 路线，但仍需要 stateless clients、Verkle、state expiry 等更多 source 判断是否独立成 child。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | review |
| Accumulator-based state-subset commitments | method/problem candidate | L2chain 说明 RSA accumulator 能让 L1 available-state digest 支持状态子集 split/merge，但当前缺 accumulator foundation 和其他 blockchain accumulator source。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | review |
| State pruning/stateless clients | candidate problem child | 与 state storage 压力同源，但机制不同 | SlimChain gives adjacent signal, but pruning/stateless-client foundation still missing | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| MPT-style authenticated state index | 用 Merkle Patricia Trie 承诺 key-value state，更新时持久化路径节点并可生成 membership proof | 需要简洁 state root 和路径证明 | 历史 path-copying 造成大 index overhead；provenance/range query 成本高 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] 背景 |
| Column-based learned state storage | 将历史 state values 按 `<addr, blk>` 排序，使用 learned index 定位并用 Merkle file 认证 value file | full-node historical state storage 和 provenance query | 不支持 fork/rewind；learned index 只定位不认证；小区间 proof size 可能较大 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| LSM-like run maintenance | L0 MB-tree flush 为 on-disk runs，多层 merge 管理写入和空间 | 写密集区块链状态更新 | merge 线程会影响 root-hash determinism，必须 checkpoint 化 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| Checkpointed asynchronous merge | 用 start/commit checkpoints、writing/merging group 和同步 root_hash_list update 降低 tail latency | merge stall 明显且节点需要一致 state digest | 后台 merge 不得直接修改 state digest；写组填满时仍可能等待前次 merge | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| Boundary-key provenance proofs | 对查询区间额外证明左右边界 key，结合 Merkle paths 和未搜索 root hashes 验证完整性 | 需要证明某地址在区块区间内的所有历史版本 | proof size 与 Merkle fanout、层数和区间共享路径相关 | [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] |
| Stateless on-chain commitments with off-chain full state | consensus nodes 只存 state root/transaction digests；storage nodes 保存 full MPT/full transactions，并提交 read/write evidence、write proof 和 partial Merkle trie update。 | smart-contract blockchain 希望降低 consensus-node storage/execution burden，同时保持 state root commitment。 | 依赖 execution proof、storage-node availability、proof compression 和 recent-window metadata；不是 full data availability 或 consensus scaling solution。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] |
| Accumulator-based split/merge state digest | 用 RSA accumulator 承诺当前 available states；DApp executor 生成状态子集 membership witness，L1 split 后让 L2 执行，最后 merge updated subset digest。 | L2 DApp execution 需要 L1 只验证摘要和 proof，同时允许不同状态子集并行处理。 | 依赖 trusted setup-free accumulator assumptions、hash-to-prime、witness cache、TEE execution proof；状态子集冲突会导致 split discard。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] |

## 成本模型与权衡

| 维度 | MPT-style path-copying | COLE-style column/runs | 解释 |
| --- | --- | --- | --- |
| Storage | `O(n*d_MPT)` | `O(n)` | MPT 每次更新保留路径节点；COLE 按记录保存历史 values 并压缩索引结构。 |
| Point lookup | 路径查找，证明自然对应 trie path | Bloom + learned index + value/Merkle lookup | COLE 多 run 查询更复杂，但能跳过无关 run。 |
| Provenance/range history | 需要沿历史结构或额外索引 | compound key range + boundary proofs | COLE 的 layout 更适合按账户历史区间查询。 |
| Integrity | Trie path proof | Merkle file + root_hash_list | COLE 让定位 index 与认证结构分离。 |
| Background maintenance | trie updates | LSM-like merge | merge 必须与 state digest checkpoint 同步。 |
| Fork/rewind | 取决于底层 trie/versioning | COLE 当前不支持 | 这是 COLE 明确的 future work/限制。 |

| 维度 | SlimChain stateless commitment | 解释 |
| --- | --- | --- |
| Consensus-node storage | state root + transaction digests + recent-window metadata | full state 与 full transaction data 移到 storage nodes。 |
| State update | partial Merkle trie + write proof | consensus node materializes only recent write paths and proof nodes needed for root update。 |
| Query/data service | off-chain storage nodes serve full state/data | state root authenticates commitment, but does not guarantee storage-node liveness。 |
| Sharding | storage-layer sharding only | global consensus remains unsharded, so cross-shard atomicity is simpler but consensus throughput is not horizontally scaled。 |

| 维度 | L2chain accumulator split/merge | 解释 |
| --- | --- | --- |
| L1 stored state | available-state digest plus split/merge transaction roots | L1 does not store private L2 transaction contents or every DApp state value. |
| Subset access | membership witness for affected states | DApp executors prove a state subset is in the current available digest before processing. |
| Update path | split digest out, execute off-chain, merge updated digest back | commitment format becomes part of transaction-processing protocol. |
| Performance bottleneck | witness generation/update and state contention | witness cache mitigates cost; overlapping split transactions are discarded. |
| Security boundary | TEE two-step execution and L1 split commitment | accumulator proves state-subset membership, not execution correctness or DA. |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE: A Column-based Learned Storage for Blockchain Systems]] | paper | 建立 column-based learned storage 路线；说明 learned index/LSM/Merkle file 如何组合进 blockchain state storage | non-forking; no rewind; single source; artifact repo not analyzed | Abstract, §1-§8 |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | paper | 建立 stateless/off-chain state-storage route：consensus nodes 只保存 commitments，storage nodes 保存 full state，并通过 partial Merkle trie/write proofs 支持 root update | SGX-centered execution proof; storage-node availability and incentives unresolved; storage sharding does not shard consensus | p1-p13 |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | paper | 建立 accumulator state-subset route：available-state digest 可被 split/merge，使 L2 DApp batches 可以按状态子集并行执行。 | TEE trust; RSA accumulator witness overhead; not a complete L2/rollup/data-availability foundation | p1-p14 |

## 当前综合

- Evidence window: `2026-06-22` to `2026-06-23`。
- Freshness: `fresh` for source-backed seed; not a latest-news claim.
- Valid until: `2026-07-23`。
- 综合: 本节点当前的强证据是 COLE、SlimChain 和 L2chain。COLE 说明 blockchain state storage 需要在普通 storage-engine tradeoff 之外增加三条约束: state root determinism、proof completeness、historical provenance。可迁移的是 column layout、learned index、LSM-like runs、Bloom filters 和 async merge scheduling；不可直接迁移的是数据库/LSM 的普通后台维护语义，因为区块链节点还必须在同一 block height 形成一致 digest。SlimChain 说明另一条 route: 不直接优化全节点历史索引，而是让 consensus nodes 变成 state-root-only/stateless validators，用 off-chain full state、partial Merkle trie、read/write evidence 和 write proofs 支持交易提交。L2chain 则显示第三条 route: state digest 本身可以为了 L2 execution 被设计成可 split/merge 的 accumulator commitment；这时存储/承诺层不是被动记录状态，而是主动定义交易处理中的状态锁定、冲突检测和摘要合并边界。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems|COLE]] | 新建 blockchain-state-storage problem，补入 column-based learned storage、Merkle files、checkpoint async merge 和 provenance proof 路线 | 全文 | yes | 后续吸收 MPT/Verkle/ForkBase/stateless/state-pruning sources |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | 补入 stateless/off-chain full-state route，说明 state commitment/proof structure 会直接约束 transaction commit 协议。 | 背景; 方法族; 成本模型; 代表 Sources; Bridge Links | no new child yet, creates bridge | 等 stateless clients/Verkle/state expiry/source 后复核是否拆 `stateless-commitments` child |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | 补入 accumulator state-subset route，说明 available-state digest 可被 split/merge 并由 L2 DApp 执行工作流消费。 | 背景; 方法族; 成本模型; 代表 Sources; Bridge Links | no new child yet, strengthens bridge | 等 RSA accumulator foundation、state commitment 和 L2/rollup architecture sources 后复核是否拆 child |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[05_Bridges/storage-engines-to-blockchain-state-storage|Storage engines -> blockchain state storage]] | `distributed-systems/data-management-and-storage/storage-engines` -> `blockchain-systems/data-management-and-storage/blockchain-state-storage` | method_translation | storage-engine indexes/merge/filtering transfer only with added integrity/provenance/state-root constraints | active_seed |
| [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage` -> `blockchain-systems/execution-and-transactions/transaction-processing` | dependency, shared_state_commitment, implementation_reuse, tension | authenticated state commitments constrain transaction validation and commit; they do not prove execution correctness, DA, or storage-node liveness. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-state-storage | part_of | nahida-knowledge-blockchain-data-management-and-storage | COLE source note | high | active_seed |
| nahida-knowledge-blockchain-state-storage | evidenced_by | vault/03_Sources/papers/arxiv-2306-10739v1-cole-column-based-learned-storage-blockchain-systems.md | COLE source note | high | active_seed |
| nahida-knowledge-blockchain-state-storage | bridged_from | nahida-knowledge-storage-engines | storage-engines-to-blockchain-state-storage bridge | high | active_seed |
| nahida-knowledge-blockchain-state-storage | bridges_to | nahida-bridge-blockchain-state-storage-to-transaction-processing | vault/05_Bridges/blockchain-state-storage-to-transaction-processing.md | high | active_seed |
| nahida-knowledge-blockchain-state-storage | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md | SlimChain source note | high | active_seed |
| nahida-knowledge-blockchain-state-storage | evidenced_by | vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md | L2chain source note; state-storage bridge | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| MPT/Verkle trie source 缺失 | 需要直接解释当前 state commitment route，而不是只通过 COLE/SlimChain 背景描述 | future paper/web/repo intake | high | queued |
| Fork/reorg/rewind 支持缺失 | COLE 明确不解决，且实际链可能需要 | future source | high | queued |
| Learned index 基础 source 缺失 | COLE 依赖 PGM-like learned index，但 vault 尚无基础节点 | future PGM/ALEX/LIPP intake | medium | queued |
| Authenticated SQL/query integrity 与 state storage 的关系未稳 | Blockchain Meets Database 只有 provenance SQL signal，不等于 authenticated query proof | future source | medium | review |
| Storage-node availability/incentives 缺 source | SlimChain 把 full data 移到 off-chain storage nodes，但 data-serving liveness/incentives 仍需要额外路线。 | future paper/repo/web intake | medium | queued |
| RSA accumulator / accumulator commitment foundation 缺失 | L2chain 使用 accumulator 作为 state-subset commitment，但 vault 尚无独立基础概念或多来源比较。 | future paper/web intake | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-cole-blockchain-storage | Created blockchain-state-storage problem node from COLE. | arxiv:2306.10739v1 | codex |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Added SlimChain stateless/off-chain state-storage route and state-storage-to-transaction-processing bridge. | doi:10.14778/3476249.3476283 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Added L2chain accumulator split/merge state-digest route and strengthened state-storage-to-transaction-processing bridge. | doi:10.14778/3574245.3574278 | codex |
