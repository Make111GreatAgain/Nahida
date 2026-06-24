---
id: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
title: "Database transaction processing -> blockchain execution"
original_title: "Database transaction processing -> blockchain execution"
file_slug: "database-transaction-processing-to-blockchain-execution"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
hierarchy_level: "bridge"
bridge_kind: "cross_domain_method_translation"
bridge_status: "active_seed"
endpoint_paths:
  - "distributed-systems/transaction-processing"
  - "blockchain-systems/execution-and-transactions/transaction-processing"
endpoint_knowledge_refs:
  - "nahida-knowledge-transaction-processing"
  - "nahida-knowledge-blockchain-transaction-processing"
from_domain: "distributed-systems"
to_domain: "blockchain-systems"
from_direction: "transaction-processing"
to_direction: "execution-and-transactions"
from_topic: "transaction-processing"
to_topic: "transaction-processing"
relation_types:
  - "translation"
  - "implementation_reuse"
  - "dependency"
  - "trust_model_shift"
directionality: "one_way_with_feedback"
relationship_thesis: "Database transaction processing mechanisms such as MVCC, Serializable Snapshot Isolation, optimistic concurrency control, nested transactions, partial rollback, transaction reordering, early abort, conflict/dependency-graph serializability analysis, address-level conflict graphs, deterministic input-order scheduling, stored procedures, access control, and provenance tables can be translated into permissioned, DAG-based, stateless, or nested-smart-contract blockchain execution only after the trust model is changed: every organization or honest node independently applies deterministic execution/reordering rules, consensus supplies transaction, block, epoch, or state-root ordering, and the execution/commit protocol must respect blockchain immutability, block/epoch/root order, authenticated state commitments, and consensus safety boundaries."
transferability: "high_for_execution_mechanisms_medium_for_security"
non_transfer_boundary: "Database serializability, MVCC, OCC, nested transactions, partial rollback, transaction reordering, early abort, SQL procedures, dependency/conflict graphs, address-level scheduling, deterministic input-order scheduling, and provenance support transfer as execution-layer mechanisms. They do not transfer blockchain consensus safety, Byzantine ordering, permissioning, Sybil resistance, incentive design, privacy channels, open-network governance, authenticated state storage, or storage-node availability. Calvin-style deterministic input ordering assumes deterministic replicas, crash/replay recovery and declared read/write sets; a blockchain orderer or consensus layer can play a sequencer-like role, but Byzantine validators, smart-contract nondeterminism, hidden state access and public verification change the boundary. Block-height SSI and block-aware abort rules are needed because ordinary replicated databases assume trusted masters or weaker failure models; Fabric++ block-local reordering cannot repair cross-block pending dependencies; EOV dependency reordering additionally cannot rewrite committed blocks and must handle transaction-detail disclosure, liveness, and deterministic orderer replication; Nezha's address-dependency scheduling assumes account-based DAG blockchains and cannot be treated as a general UTXO/natural-DAG concurrency solution; SlimChain's OCC/SSI route assumes recent-window read/write metadata and verifiable off-chain execution against a state root; Loom's nested-transaction adaptation assumes all replicas can deterministically observe contract invocation trees, dependency types and read/write sets before applying the same rollback/reschedule rules."
evidence_window_start: "2012"
evidence_window_end: "2022"
domains:
  - "distributed-systems"
  - "blockchain-systems"
topics:
  - "transaction-processing"
  - "blockchain execution"
  - "serializable snapshot isolation"
  - "blockchain relational database"
  - "optimistic concurrency control"
  - "execute-order-validate"
  - "transaction reordering"
  - "early abort"
  - "DAG-based blockchain concurrency control"
  - "address-based conflict graph"
  - "stateless blockchain execution"
  - "off-chain smart contract execution"
  - "recent-window OCC"
  - "deterministic transaction scheduling"
  - "transaction input replication"
  - "nested transactions"
  - "nested contract transactions"
  - "subtransaction-level rollback"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
  - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
  - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
  - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
  - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
knowledge_refs:
  - "nahida-knowledge-transaction-processing"
  - "nahida-knowledge-blockchain-transaction-processing"
relation_edges:
  - from: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    relation: "connects"
    to: "nahida-knowledge-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    relation: "connects"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/database-transaction-processing-to-blockchain-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-e1d0bc04b53e-calvin-fast-distributed-transactions.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-bridge-database-transaction-processing-to-blockchain-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
query_keys:
  - "database transaction processing blockchain execution"
  - "blockchain relational database"
  - "Serializable Snapshot Isolation blockchain"
  - "block height SSI"
  - "execute and order in parallel"
  - "execute-order-validate OCC"
  - "FabricSharp"
  - "blockchain transaction serializability"
  - "Fabric++"
  - "Hyperledger Fabric transaction reordering"
  - "early transaction abort"
  - "Nezha"
  - "address-based conflict graph"
  - "DAG blockchain concurrency control"
  - "SlimChain"
  - "stateless blockchain OCC SSI"
  - "off-chain smart contract execution"
  - "Calvin deterministic transaction scheduling"
  - "deterministic input ordering blockchain execution"
  - "transaction input replication"
  - "nested transaction blockchain execution"
  - "nested contract transaction execution"
  - "subtransaction-level rollback"
  - "Loom"
created: "2026-06-22"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260622-blockchain-meets-database"
  - "nahida-knowledge-20260622-transactional-perspective-eov"
  - "nahida-knowledge-20260622-fabric-plus-plus-transaction-processing"
  - "nahida-knowledge-20260622-nezha-dag-transaction-processing"
  - "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
  - "nahida-paper-intake-20260623-calvin"
  - "nahida-paper-intake-20260623-loom-nested-contract-transactions"
source_refs:
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "sha256:e1d0bc04b53e5702d2f0d52b5bb1e561ff25fdf3490402c98abdb94c81281818"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
confidence: "high"
trust_tier: "primary"
---

# Database transaction processing -> blockchain execution

## 命名与路径

- Original title: Database transaction processing -> blockchain execution
- File slug: `database-transaction-processing-to-blockchain-execution`
- Path safety check: created under `05_Bridges`.

## 端点基础说明

`distributed-systems/transaction-processing` 关注事务执行、并发控制、隔离级别、commit/abort 和恢复边界。`blockchain-systems/execution-and-transactions/transaction-processing` 关注区块链节点如何执行交易、检测冲突、提交或中止，并在 consensus order、epoch order 或 state-root commitment 下形成确定性状态。

这条 bridge 记录的不是“数据库就是区块链”，而是一个更窄的迁移命题: 数据库事务/并发控制机制可以成为 blockchain execution layer 的实现基础，但必须补上互不信任副本、外部 ordering service、签名交易、确定性 stored procedure、block/epoch/root-order-aware commit rules，以及在 EOV/DAG/stateless 架构中已经 committed blocks、epoch order 或 state roots 不可随意重写的边界。

## 连接命题

- From: `distributed-systems/transaction-processing`
- To: `blockchain-systems/execution-and-transactions/transaction-processing`
- Relation types: translation, implementation_reuse, dependency, trust_model_shift
- Directionality: `one_way_with_feedback`
- Relationship thesis: Database transaction processing mechanisms such as MVCC, Serializable Snapshot Isolation, optimistic concurrency control, transaction reordering, early abort, conflict/dependency-graph serializability analysis, address-level conflict graphs, deterministic input-order scheduling, stored procedures, access control, and provenance tables can be translated into permissioned or DAG-based blockchain execution only after the trust model is changed: every organization or honest node independently applies deterministic execution/reordering rules, consensus supplies transaction, block, or epoch ordering, and the execution/commit protocol must respect blockchain immutability, block/epoch order, and consensus safety boundaries.

## 端点范围

| Endpoint knowledge | Path | Scope in bridge | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | `distributed-systems/transaction-processing` | MVCC, SSI, OCC, nested transactions, partial rollback, transaction reordering, early abort, isolation, commit/abort, recovery, provenance-supporting transaction logs, conflict/dependency graph scheduling, deterministic input-order scheduling | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]]; [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]]; [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective]]; [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]]; [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin]]; [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/transaction-processing` | block/epoch/root ordered execution, deterministic commit/reordering, block-height snapshots, Fabric simulate-order-validate validation, DAG concurrent-block execution, stateless smart-contract commitment, nested contract subtransaction execution, blockchain smart contract execution over SQL procedures | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]]; [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]]; [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective]]; [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]]; [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]]; [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | active_seed |

## 可迁移知识/模式

| Pattern | Transfer target | Evidence | Boundary |
| --- | --- | --- | --- |
| Serializable Snapshot Isolation | block-internal parallel execution and serializable commit | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] §3.2-§3.4 | Plain SSI is insufficient when nodes execute at different block heights; block-height visibility and block-aware abort rules are required. |
| MVCC row versions | ledger history and provenance queries | paper §2, §4.1-§4.2 | Provenance queries do not by themselves prove query-result integrity against a malicious peer. |
| Stored procedures | SQL smart contracts | paper §2, §3.7, §4.3 | Non-deterministic functions and unordered limited reads must be constrained. |
| Access control and user catalogs | permissioned chain identity and ACL | paper §2, §3.7, §4.2 | Database ACL does not replace transaction signatures and network-level permissioning. |
| Write-set tracking | checkpoint hash and deterministic recovery | paper §3.3.4, §3.6, §4.2 | The prototype had not implemented checkpoint flow at evaluation time. |
| Transaction reordering over read/write sets | Fabric block-local invalid-transaction reduction | [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] §3 | Reordering must be deterministic across peers/orderers; Fabric++ only reorders within a block and uses heuristic cycle breaking. |
| Early abort | Fabric simulation/order pipeline | Fabric++ §3.3 | Early abort reduces wasted network/validation work, but cannot replace endorsement-policy or consensus safety checks. |
| OCC dependency-graph analysis | EOV invalid-transaction reduction and pending transaction reordering | [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] §3-§4 | Ordinary OCC can reorder uncommitted transactions, but blockchains cannot rewrite committed blocks; orderer-side logic must be deterministic and disclosure-safe. |
| Address-based conflict graph and hierarchical sorting | DAG epoch-level concurrent-block execution | [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] §III-§VI | Transfers conflict/dependency scheduling, not DAG consensus safety; assumes account-based addresses and deferred execution after block consensus. |
| OCC/SSI over recent state-root window | Stateless smart-contract commit/abort without full validator state | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] Algorithm 2 | Transfers concurrency-control logic only after adding authenticated state roots, execution evidence, write proofs, and bounded read/write metadata. |
| Deterministic input order and locking | order-then-execute blockchain transaction execution | [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin]] §3-§6 | Transfers as from-side database evidence only: blockchain consensus/orderer can supply a sequencer-like order, but Byzantine execution, smart-contract determinism, read/write-set availability and public state commitments must be handled separately. |
| Nested transaction partial rollback | nested smart-contract transaction execution | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] §II-§IV | Transfers the idea of parent/child subtransactions and partial rollback, but blockchain execution must add deterministic serializability, replica agreement on rollback choices and contract-call read/write provenance. |

## 迁移矩阵

| 可迁移对象 | From path | To path | 迁移方式 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| SSI abort during commit | `distributed-systems/transaction-processing` | `blockchain-systems/execution-and-transactions/transaction-processing` | block 内并行执行后按共识顺序串行 commit/abort | paper §3.3 | SSI 的本地时序若不受控会导致不同节点 abort 集合不同 |
| Block-height snapshot visibility | transaction isolation | blockchain block processing | 用 creator/deleter block number 让交易在指定 snapshot-height 读取同一状态 | paper §3.4.1, §4.3 | 需要保留多版本，predicate reads 依赖索引 |
| Block-aware conflict abort | SSI conflict resolution | decentralized replicas | 若冲突在同一 block 按 block order 决策；若 nearConflict 跨 block 则 abort 以保持各节点一致 | paper §3.4.3 | 会牺牲部分可提交交易以换确定性一致 |
| PL/SQL procedures | stored procedures | smart contracts | 将 smart contract 映射为受约束的 procedure invocation | paper §2, §3.7, §4.3 | random/time/sequence 等非确定性能力必须禁用 |
| Ledger/provenance table | transaction logs/history | blockchain audit/query | `pgLedger` 连接交易、用户、block 和历史行版本 | paper §4.2, Table 3 | 单节点 query result 仍可能被恶意 peer 篡改，需要多节点查询或 authenticated query |
| Block-local conflict graph | read/write set transaction reordering | Fabric simulate-order-validate pipeline | 在 orderer/validator 能看到 readset/writeset 时，为 block 内交易建立冲突图，删除 cycle 中交易并重排剩余交易以减少 validation abort | Fabric++ §3 | 仅覆盖 block 内并发；cycle-breaking 不保证最少 abort；read/write set 可见性有隐私边界 |
| Early abort for stale reads/version mismatch | OCC validation shortcut | Fabric simulation and ordering phases | Simulation 阶段用 version number/last-block-ID 发现 stale read，ordering 阶段发现同 block 读同 key 不同版本的 doomed 交易并提前中止 | Fabric++ §3.3 | 提前中止只是节省 pipeline 成本，不能证明剩余交易全局最优 |
| Snapshot timestamp model | OCC transaction timestamps | EOV transaction lifecycle | 将 blockchain snapshot、transaction start timestamp 和 consensus-determined end timestamp 对齐，用 dependency graph 判断 serializability/reorderability | A Transactional Perspective §3.1-§3.3 | committed blocks 不可重排，且同 block concurrency 不等于所有 concurrency；Fabric++ 的 block-scope reordering 会漏跨 block 依赖 |
| Dependency cycle filtering | serializability graph analysis | orderer-side pre-ordering abort | 若 dependency cycle 中没有 pending `c-ww`，交易调度无法通过重排串行化；arrival 时提前 abort 新交易，block formation 时拓扑排序剩余交易 | A Transactional Perspective §3.4 | Bloom filter false positives 和 `max_span` pruning 可能额外 abort；算法可能牺牲 Fabric validity/liveness |
| Address-level conflict graph | conflict graph / concurrency control | DAG concurrent-block execution | 用 address read/write sets 替代 transaction-pair dependency graph，降低高 block concurrency 下的构图和 cycle removal 开销 | Nezha §IV | 只迁移执行层 scheduling；不能替代共识、mempool 或 UTXO/natural-DAG ordering |
| Recent-window OCC/SSI | OCC/SSI commit/abort | stateless blockchain execution | 对基于旧 state root 执行的交易，consensus nodes 只保留最近 `k` blocks 的 read/write maps；OCC 以更强隔离换更多 abort，SSI 以 serializability 换更高 success rate | SlimChain §3-§6 | 依赖 state-root mapping、write proofs、TEE/VC/policy execution evidence 和 `k`-block freshness；不能单独保证 data availability 或 storage-node liveness |
| Input sequence before execution | deterministic scheduling | order-then-execute blockchain processing | Calvin 证明数据库侧可以先复制/排序事务输入，再确定性获取锁和执行，从而减少事务尾部协调对锁持有窗口的影响 | Calvin §3-§6 | 只能作为结构迁移；区块链还需要处理 Byzantine order/execution、智能合约非确定性、state-root commitment 和读写集不可预知问题 |
| Nested transaction tree and partial abort | nested transaction model | nested contract transaction execution | Loom 将数据库 nested transaction 的 parent/child、linear/parallel nesting 和 partial rollback 思想迁移到智能合约调用树，用 weak/strong dependency 区分可独立移动的子调用和 parent-critical 子调用。 | Loom §II-§IV | 只能迁移 execution/scheduling 结构；普通数据库的 non-deterministic scheduling、trusted coordinator 和自由 commit-order 不能直接迁移到 blockchain replicas。 |

## 类比、依赖或关系边界

这条 bridge 的核心边界是 trust model 和 immutability。传统复制数据库通常信任 master 或协调器，或者只处理 crash failures；Calvin 进一步说明，数据库侧可以把输入排序/复制放在执行之前，并让确定性锁管理保证副本按同一序列演进。区块链可以借鉴这种 order-then-execute 结构，但不能直接继承 Calvin 的 failure model、读写集提前声明和副本确定性假设。Blockchain relational database 要求每个组织在本地独立执行，并通过共识得到共同 block order。EOV/Fabric-style 系统还要求 orderer 在相同 transaction stream 上确定性执行 reordering，且不能改变已经 committed block 的历史。Fabric++ 进一步说明，哪怕只做 block-local reordering，算法仍必须尊重 endorsement read/write sets、block cutting、ledger 中 valid/invalid 交易记录和 peer validation。Nezha 则说明，DAG-based blockchains 可以把 consensus 与 execution 解耦为 epoch-level deferred execution，但 execution scheduler 必须尊重 account-address dependencies 和 deterministic commit order。SlimChain 进一步说明，stateless consensus nodes 可以复用 OCC/SSI 思想，但前提是执行证明、read/write set、state-root mapping、write proof 和 partial state commitment 都进入交易处理协议。Loom 又补上 nested transaction 边界: 数据库的 nested/parallel transaction 模型可以启发智能合约调用树的 partial rollback，但区块链副本必须对调用树、读写集、rollback list 和重执行顺序达成确定性一致。因此，可迁移的是 transaction-processing 机制，不可迁移的是“谁可信”、共识如何排序、state commitment 如何认证、VM/host call 如何确定、以及开放网络如何激励/准入的系统假设。

## 证据

| Source | Evidence role | Status |
| --- | --- | --- |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database]] | direct evidence for translating relational database transaction processing into permissioned blockchain execution | active_seed |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric]] | direct evidence for translating transaction reordering, conflict-graph analysis and early abort into Hyperledger Fabric's EOV pipeline | active_seed |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on Execute-Order-Validate Blockchains]] | direct evidence for translating OCC/serializability/reorderability analysis into Fabric-style EOV transaction scheduling | active_seed |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains]] | direct evidence for translating conflict graph and deterministic scheduling into DAG-based blockchain epoch-level execution | active_seed |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | direct evidence for translating OCC/SSI commit/abort logic into stateless blockchain execution backed by authenticated state commitments and off-chain execution evidence | active_seed |
| [[sha256-e1d0bc04b53e-calvin-fast-distributed-transactions|Calvin: Fast Distributed Transactions for Partitioned Database Systems]] | from-side database evidence for deterministic input ordering, deterministic locking and input-log replication; not direct blockchain evidence | active_seed |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom: A Deterministic Execution Framework Towards Nested Contract Transactions]] | direct evidence for translating nested-transaction partial rollback and parallel nesting ideas into deterministic smart-contract transaction execution | active_seed |

## 路径传播

| Endpoint path | Propagation | Status |
| --- | --- | --- |
| `distributed-systems/transaction-processing` | add bridge link, relation edge, source extension and method row | active_seed |
| `blockchain-systems/execution-and-transactions/transaction-processing` | add bridge link, relation edge, source extension and method rows | active_seed |

## 查询入口

- blockchain relational database 如何用 PostgreSQL 实现?
- block-height SSI 和普通 SSI 有什么不同?
- 数据库 transaction processing 如何迁移到 blockchain execution?
- execute-and-order-in-parallel 为什么需要 block-aware abort rule?
- FabricSharp 如何用 OCC 思想减少 EOV invalid transactions?
- Fabric++ 如何通过 transaction reordering 和 early abort 减少 Fabric invalid transactions?
- execute-order-validate 和数据库 OCC 的对应关系是什么?
- Nezha 的 address-based conflict graph 如何把并发控制迁移到 DAG blockchain execution?
- SlimChain 如何在 stateless consensus node 上使用 OCC/SSI?
- state root/windowed read-write metadata 如何改变 blockchain transaction processing?
- Calvin 的 deterministic input-order scheduling 对 blockchain order-then-execute 有什么启发和边界?
- Loom 如何把 database nested transactions 的 partial rollback 思路迁移到 nested smart-contract transaction execution?
- 为什么 nested transaction 的自由调度不能直接迁移到 blockchain replicas?

## 复核笔记

- Maturity: `active_seed`.
- Refresh triggers: 后续 Veritas、BigchainDB、parallel execution、authenticated SQL/query integrity、database-backed blockchain source、EOV/Fabric/FastFabric/Nezha-like DAG execution source 改变任一端点、relation type、transfer boundary 或 bridge maturity。

## 影响的 Knowledge Nodes

| Knowledge node | Section/update | Reason | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | Methods, representative sources, bridge links | Blockchain Meets Database gives direct source-backed transaction-processing migration evidence | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | Adds database-backed execution, SSI, and execute-order-in-parallel route | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions|Blockchain execution and transactions]] | Source extension | Places relational database substrate under execution layer rather than consensus | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | Methods, representative sources, bridge links | Fabric++ adds transaction reordering/conflict-graph/early-abort adaptation evidence | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | Adds Fabric++ block-local EOV reordering and early abort route | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | Methods, representative sources, bridge links | A Transactional Perspective adds OCC/serializability dependency-analysis adaptation evidence | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | Adds EOV dependency-graph reordering route and FabricSharp/FastFabricSharp source instance | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | Adds Nezha DAG-based address-dependency scheduling route | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | Adds SlimChain stateless OCC/SSI and off-chain execution route | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | Methods, representative sources, bridge links | Adds Loom nested-transaction partial rollback and subtransaction scheduling route | active_seed |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution|Nested contract transaction execution]] | Bridge link | Loom creates a child problem at the bridge between database nested transaction ideas and blockchain deterministic execution | active_seed |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | Bridge link | SlimChain shows transaction-processing logic depends on state commitment and proof design | active_seed |
| [[04_Knowledge/distributed-systems/transaction-processing|Transaction processing]] | From-side method evidence | Calvin strengthens deterministic input-order scheduling and transaction input replication as database-side mechanisms | active_seed |

## 刷新规则

- Last checked: `2026-06-23`
- Valid until: `2026-07-22`
- Refresh triggers: 新 source 改变任一 endpoint、relation type、transfer boundary 或 bridge maturity；尤其 parallel blockchain execution、DAG-based execution、database-backed blockchain、stateless execution 或 authenticated SQL/query integrity sources。
