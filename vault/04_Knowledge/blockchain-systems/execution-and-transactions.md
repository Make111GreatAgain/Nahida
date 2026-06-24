---
id: "nahida-knowledge-blockchain-execution-and-transactions"
title: "Blockchain execution and transactions"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "execution-and-transactions"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-systems"
child_knowledge_refs:
  - "nahida-knowledge-blockchain-fair-exchange-protocols"
  - "nahida-knowledge-cross-shard-transaction-execution"
  - "nahida-knowledge-smart-contract-execution"
  - "nahida-knowledge-blockchain-transaction-processing"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
primary_ontology_path: "blockchain-systems/execution-and-transactions"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-systems"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
      - "vault/04_Knowledge/blockchain-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-transaction-processing"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "has_child"
    to: "nahida-knowledge-blockchain-fair-exchange-protocols"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/fair-exchange-protocols.md"
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "has_child"
    to: "nahida-knowledge-cross-shard-transaction-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/cross-shard-transaction-execution.md"
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "has_child"
    to: "nahida-knowledge-smart-contract-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/smart-contract-execution.md"
      - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-blockchain-execution-and-transactions"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-commit-and-prove-arguments-to-fair-exchange-protocols"
  - "nahida-bridge-permissioned-consensus-to-transaction-execution"
  - "nahida-bridge-database-transaction-processing-to-blockchain-execution"
  - "nahida-bridge-blockchain-state-storage-to-transaction-processing"
  - "nahida-bridge-verifiable-computation-systems-to-contingent-service-payments"
  - "nahida-bridge-smart-contract-execution-to-transaction-processing"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md"
  - "vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md"
  - "vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md"
  - "vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md"
  - "vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md"
  - "vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md"
  - "vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md"
  - "vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md"
  - "vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md"
  - "vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md"
  - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
  - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
representative_source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "arxiv:1804.00399v4"
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
  - "arxiv:2208.00283v2"
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
query_keys:
  - "blockchain execution"
  - "blockchain transaction execution"
  - "execution-and-transactions"
  - "区块链执行层"
  - "区块链交易处理"
  - "blockchain fair exchange"
  - "ZKCPlus"
  - "ZKCP"
  - "blockchain relational database"
  - "database-backed blockchain execution"
  - "execute-order-validate"
  - "FabricSharp"
  - "Fabric++"
  - "Hyperledger Fabric transaction reordering"
  - "early transaction abort"
  - "Nezha"
  - "DAG-based blockchain execution"
  - "address-based conflict graph"
  - "hierarchical sorting"
  - "SlimChain"
  - "stateless blockchain execution"
  - "off-chain smart contract execution"
  - "on-chain state commitment"
  - "L2chain"
  - "layer-2 DApp execution"
  - "split-execute-merge"
  - "RSA accumulator state digest"
  - "cross-shard smart contract execution"
  - "LightCross"
  - "contingent service payment"
  - "recurring contingent service payment"
  - "RC-S-P"
  - "smart contract execution"
  - "smart contract virtual machine"
  - "deterministic smart contract runtime"
  - "WebAssembly smart contract runtime"
  - "EVM ABI compatibility"
  - "DTVM"
  - "dMIR"
  - "dWasm"
  - "RC-PoR-P"
  - "nested contract transaction execution"
  - "smart contract concurrency control"
  - "subtransaction-level rollback"
  - "Loom"
aliases:
  - "区块链执行与交易"
  - "Blockchain execution layer"
domains:
  - "blockchain-systems"
topics:
  - "execution-and-transactions"
  - "fair-exchange-protocols"
  - "transaction-processing"
  - "blockchain-relational-databases"
  - "execute-order-validate"
  - "transaction-reordering"
  - "early-abort"
  - "dag-based-blockchain-execution"
  - "concurrency-control"
  - "stateless-blockchain"
  - "off-chain-storage"
  - "partial-merkle-trie"
  - "layer-2-dapp-execution"
  - "split-execute-merge"
  - "rsa-accumulator-state-digest"
  - "cross-shard-transaction-execution"
  - "smart-contract-sharding"
  - "contingent-service-payments"
  - "smart-contract-execution"
  - "deterministic-vm"
  - "wasm-smart-contract-runtime"
  - "evm-abi-compatibility"
  - "nested-contract-transaction-execution"
  - "smart-contract-concurrency-control"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-zkcplus-fair-exchange"
  - "nahida-knowledge-20260620-tell-leaderless-consensus-execution"
  - "nahida-knowledge-20260621-ahl-sharding"
  - "nahida-knowledge-20260622-blockchain-meets-database"
  - "nahida-knowledge-20260622-transactional-perspective-eov"
  - "nahida-knowledge-20260622-fabric-plus-plus-transaction-processing"
  - "nahida-knowledge-20260622-nezha-dag-transaction-processing"
  - "nahida-knowledge-20260622-slimchain-stateless-execution-storage"
  - "nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution"
  - "nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts"
  - "nahida-knowledge-20260623-recurring-contingent-service-payment"
  - "nahida-knowledge-20260623-dtvm-smart-contract-execution"
  - "nahida-paper-intake-20260623-loom-nested-contract-transactions"
source_refs:
  - "doi:10.1145/3460120.3484558"
  - "sha256:69daae93b34aa60f6a601001af7438c9d24ddcee151eba477f0b0c9f2d2e6d9e"
  - "arxiv:1804.00399v4"
  - "arxiv:1903.01919v2"
  - "arxiv:2003.10064v1"
  - "doi:10.1145/3299869.3319883"
  - "doi:10.1109/icdcs54860.2022.00034"
  - "doi:10.14778/3476249.3476283"
  - "doi:10.14778/3574245.3574278"
  - "sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2"
  - "arxiv:2208.00283v2"
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
confidence: "medium"
trust_tier: "primary"
---

# Blockchain execution and transactions

## 定义与范围

- 定义: Blockchain execution and transactions 关注区块链在 ordering/finality 之外如何执行交易、更新状态、处理并发冲突、提交/回滚结果，并把执行层与 consensus、mempool、sharding、state storage 的边界衔接起来。
- 不包含: 单篇论文的具体系统名、某个 smart contract runtime 的局部实现、一次 benchmark 结果；这些应留在 source note 或 source-extension 行中。
- Canonical terms: `execution-and-transactions`, `blockchain execution`, `transaction execution`.
- Standalone completeness check: 本节点给出本地方向定义、边界、问题、方法族、代表来源、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询能从 `blockchain-systems` 进入执行层，而不是把所有执行问题塞进 consensus、mempool 或 sharding 节点。
- Update scope: 新 source 若涉及 transaction execution、smart contract execution、state access、concurrency control、commit/re-execution、cross-shard/cross-chain transaction execution、blockchain-mediated fair exchange 或 transaction-lock payment protocol，应刷新本方向。

## 背景

区块链系统常把 consensus 描述为决定交易或区块顺序的层，把 execution 描述为按该顺序更新状态的层。但在高性能许可链、并行 consensus、shared mempool、sharding 或 rollup 场景中，execution 并不是简单顺序回放: execution layer 可能需要并行执行、检测冲突、重执行 abort 交易、处理 out-of-order blocks、合并多个执行分支，并用确定性规则保证所有节点得到同一状态。

当前 vault 的直接证据来自 TELL、AHL、ZKCPlus、Blockchain Meets Database、Fabric++、A Transactional Perspective on EOV Blockchains、Nezha、SlimChain、L2chain、LightCross、RC-S-P、DTVM 和 Loom。TELL 不是一个新的 consensus protocol，而是说明 execution layer 可以利用 leaderless consensus 的 instance 结构做协同优化。AHL 不是执行层 foundation，但它说明 general workload sharding 需要把 cross-shard transaction execution、2PC/2PL 和 BFT coordinator availability 一起处理。LightCross 进一步把 cross-shard smart-contract execution 从 candidate 推到正式问题层: 它不要求把任意合约逻辑拆成 shard-local fragments，而是把复杂执行放到 TEE executor，再用 R-shard 批量排序和 S-shard bitmap validation 提交。DTVM 则把另一个长期缺口补成正式问题层: 智能合约执行不只是交易处理，而是 VM/runtime determinism、gas/trap/resource accounting、EVM ABI compatibility、Wasm/JIT、host API 和 sandbox security 的组合问题。Loom 补上 DTVM 没覆盖的结构侧执行问题: 当一笔交易触发多层 contract invocation 时，执行层要按 subtransaction 捕获依赖、选择部分回滚并确定性重执行。ZKCPlus 说明 execution-and-transactions 还包括应用级 payment/lock/finalize 协议: 链上合约或脚本只处理锁、退款和结算，链下证明/密文负责商品正确性。RC-S-P 补充了服务型 payment/finalize 协议: 链上合约托管 masked deposits、记录加密/填充的 query/proof，并在 private time bubble 后按争议归责分配 coins。Blockchain Meets Database 则说明 execution layer 还可以由关系数据库 substrate 承担: 共识只负责 block ordering，数据库用 SSI/MVCC/stored procedures/provenance 处理执行与提交。Fabric++ 展示了保留 Fabric simulate-order-validate 管线时的更窄迁移: 用 block-local read/write conflict graph 重排和 early abort 减少 late validation abort。A Transactional Perspective on EOV Blockchains 进一步把这条路线推进到跨 pending transactions 的 OCC/serializability dependency analysis。Nezha 则说明 DAG/parallel-chain block production 下，execution layer 需要在 epoch-level concurrent blocks 上做地址级冲突检测和确定性排序。SlimChain 说明当 full state 和 execution 被移到 off-chain storage nodes 时，execution layer 还要处理证明携带、recent-window conflict metadata、partial commitment update 和 state-storage boundary。L2chain 说明当 DApp 交易移到 L2 时，execution layer 需要通过 L1 split/merge state digest、L2 local ordering、TEE two-step execution 和 witness cache 一起维护 confidentiality 与 state consistency。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction`。
- 为什么足够通用: 它覆盖 transaction execution、state update、parallel execution、commit/re-execution、execution-consensus boundary 等可复用问题，未来可承接 Fabric、EVM execution、parallel VM、cross-shard transaction 和 rollup execution 资料。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: TELL 只是首个 source extension；SHT/DCE 留在 source note 和 child problem 方法行。
- 需要引用的更基础 Knowledge: [[blockchain-systems|Blockchain systems]]；相邻方向包括 [[blockchain-consensus|Blockchain consensus]]、[[mempool-and-networking|Mempool and networking]]、[[scaling-and-sharding|Scaling and sharding]]。

## 解决的问题

本方向回答: 区块链节点在已有或正在形成的交易/区块顺序下，如何用确定性且高吞吐的方式执行交易并更新状态，同时不破坏 consensus 的 safety/finality 假设。

典型问题包括:

- 并行执行与确定性重放之间的张力。
- 交易读写冲突、abort/re-execution 和 commit latency。
- 多 consensus instances、multi-chain、DAG 或 sharding 下的执行结果合并。
- execution layer 对 consensus/mempool/storage 的依赖边界。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-systems|Blockchain systems]] | child_of | TELL source exposes missing execution direction | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] | problem | transaction execution/concurrency/commit 是当前 source 的实际问题层 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | active_seed |
| [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] | problem | ZKCPlus and FDE show transaction locks/contracts can mediate fair exchange of data, models, query results or committed-data retrieval. | [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]]; [[fair-data-exchange|Fair data exchange for committed data]] | active_seed |
| [[cross-shard-transaction-execution|Cross-shard transaction execution]] | problem | 多篇 sharding source 已经共同指向跨片交易/智能合约执行的原子性、隔离、执行位置和通信开销问题 | AHL, ByShard, RingBFT, LightCross | active_seed |
| [[smart-contract-execution|Smart contract execution]] | problem | EVM/Wasm/VM/runtime 资料已经形成独立问题层：determinism、gas、trap、ABI/language compatibility 和 JIT/security 不是普通交易并发控制 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] | active_seed |
| execution-state-storage | candidate | execution 与 stateDB/Merkle/state storage 的边界可能形成独立问题 | current evidence only mentions LevelDB/stateDB | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Sequential execution | 按 consensus order 顺序执行全部交易 | 低并发、简单状态模型 | 吞吐低，不能利用多核/多实例 | model_prior_background |
| Parallel execution with deterministic serialization | 并行执行交易，再用确定规则检测冲突、abort、重执行 | 读写集合可追踪，节点需确定性回放 | 冲突检测/重执行开销随 skew 增加 | [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] |
| Consensus-aware execution | execution layer 读取 consensus instance 状态、block-producing interval 或 ordering unit，减少跨层等待 | leaderless/multi-leader consensus 或 parallel consensus | 绑定 consensus 特征，跨协议迁移需重审 | [[permissioned-consensus-to-transaction-execution|Permissioned consensus -> transaction execution]] |
| Cross-shard transaction coordination | 将跨片交易拆成 prepare/commit/abort execution steps，并用 reference committee 防止 malicious coordinator blocking | general workload sharded blockchain | 应用 refactoring、2PL contention、reference committee bottleneck | [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] |
| TEE-backed cross-shard smart-contract execution | 在 TEE executor 中执行复杂 CSTx，R-shard 批量排序 certified results，S-shards 验证 stale reads 并提交 write sets | permissioned smart-contract sharding; TEE acceptable | TEE/R-shard/executor availability 成为边界；stale reads 仍可能 abort | [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] |
| Deterministic smart-contract VM/runtime | 约束 Wasm/EVM runtime 的 validation、IR、stack/memory/trap、gas、host API 和 JIT code generation，使合约在多节点/多架构下得到一致状态转移。 | 需要兼容 Solidity/EVM 生态，同时追求 Wasm/JIT 性能和确定性执行。 | 专用 VM/compiler/runtime 复杂度高；zkVM/RISC-V 仍是 future route；不替代 transaction ordering 或 consensus safety。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| Nested contract subtransaction execution | 将智能合约跨合约调用树拆为 subtransactions，并用 deterministic rollback/reschedule 保持 serializability 与并发度。 | Permissioned blockchain 中存在长 nested call chain 和高冲突 smart-contract workloads。 | 不解决 VM runtime/gas/trap 或 consensus ordering；依赖确定性捕获调用树、读写集和依赖类型。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] |
| Fair exchange transaction locks | 用 hash lock、commitment lock、timeout/refund 或 smart contract finalize 让付款与 key/opening/reveal 绑定。 | 交易数字商品、模型、查询结果或 committed data，且大数据/证明链下完成。 | 锁和结算不证明商品正确性；商品正确性依赖 ZK/VE/commitment 等 proof layer。 | [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] |
| Recurring service-payment escrow | 合约托管客户端/服务器 deposits，记录加密且填充的 service queries/proofs，等隐私窗口结束后按 arbiter 或 smart contract 的归责结果分配 coins。 | 需要为 PoR、verifiable computation、searchable encryption 等可验证服务重复付款。 | 通用版本引入 offline arbiter、masked deposit 和更多消息；service correctness 仍由 VS/VSID/PoR/VC 层提供。 | [[contingent-service-payments|Contingent service payments for verifiable services]] |
| Database-backed blockchain execution | 用关系数据库的 SSI/MVCC、stored procedures、ACL 和历史版本作为 permissioned blockchain execution substrate | known-but-mutually-distrustful organizations; SQL-rich applications | 必须改变数据库默认复制信任模型；需确定性 procedure、block-height snapshots、block-aware abort rules | [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] |
| Fabric++ transaction reordering and early abort | 保留 Hyperledger Fabric simulate-order-validate pipeline，在 block 内用 read/write conflict graph 重排交易，并提前 abort cycle 或 stale-version 交易 | Fabric-style permissioned chains with endorsement readsets/writesets and visible transaction access sets | 只做 block-local reordering；cycle breaking 是启发式；不替代 consensus/endorsement safety | [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] |
| EOV dependency-graph reordering | 保留 execute-order-validate pipeline，在 orderer 中用 OCC/serializability dependency graph 提前过滤不可重排交易，再拓扑排序剩余 pending transactions | Fabric/FastFabric-style permissioned chains with endorsement readsets/writesets | 交易细节披露、Bloom filter false positives、stale snapshot pruning 都会影响 liveness/effective abort | [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] |
| DAG epoch-level concurrent execution | 对 DAG/parallel-chain 产生的同一 epoch blocks，延迟到共识后并发模拟交易，再用 address-based conflict graph 和 hierarchical sorting 得到可并发提交的 deterministic order。 | account-based DAG-based blockchains，block concurrency 高，交易 read/write addresses 可记录。 | 不解决 consensus safety、mempool/relayer/network liveness；不适用于 UTXO/natural DAG 的 irregular topology。 | [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] |
| Stateless off-chain smart-contract execution | storage nodes 保存 full state 并执行交易，consensus nodes 只保存 transaction digest/state root，并用 read/write evidence、TEE/VC/policy proof、write proof 和 partial commitment update 验证提交。 | 节点存储压力大、希望 consensus layer 保持 compact state commitment 的 smart-contract blockchain。 | 依赖 execution proof、off-chain storage availability、`k`-block freshness window 和 proof compression；不替代 consensus sharding 或 DA。 | [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] |
| Layer-2 DApp split-execute-merge | DApp executors 在 L2 排序并 TEE 执行交易批次，L1 只验证 split/merge state digest 和执行证明。 | 希望减少 L1 共识/执行压力，同时保持 DApp transaction confidentiality 和 order correctness。 | 依赖 TEE、RSA accumulator、witness cache 和 L1 split/merge latency；不覆盖 DA、rollup fraud/validity proof 或完整 L2 economics。 | [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL: Efficient Transaction Execution Protocol Towards Leaderless Consensus]] | paper | 新增 execution-and-transactions 方向；展示 transaction execution 可针对 leaderless consensus instances 做 intra-instance execution、inter-instance merging 和 dynamic commitment | same data-center experiments; throughput excludes consensus latency; SHT/DCE 是 TELL-specific mechanisms | p1-p13 |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|Towards Scaling Blockchain Systems via Sharding]] | paper | 为 execution-and-transactions 补入 cross-shard/general-workload transaction route：2PC/2PL + BFT reference committee + chaincode locks | sharding source extension; not a full execution-layer foundation | §6.1-§6.4 |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross: Sharding with Lightweight Cross-Shard Execution for Smart Contracts]] | paper | 将 arbitrary smart-contract CSTx 路线补入执行层，并触发 [[cross-shard-transaction-execution|Cross-shard transaction execution]] 独立问题节点。 | TEE/R-shard/executor assumptions; permissioned FISCO-BCOS prototype; workload-dependent contract migration. | §III-§V, Appendix |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange]] | paper | 新增 fair-exchange-protocols 子问题：commit/validate/deliver/reveal/finalize、commitment lock、timeout/refund 和 proof-before-payment route | proof-system details route through [[commit-and-prove-arguments|Commit-and-prove arguments]]; direct ZKCP/FairSwap sources still missing | p1-p20 |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | paper | 将 fair-exchange 的 service-payment variants 提升为 [[contingent-service-payments|Contingent service payments for verifiable services]] 子问题。 | PoR/VSID details route through source note and VC bridge; ZKCSP/FairSwap direct sources still missing | p1-p15; Appendix E-L |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility]] | paper | 将 smart-contract-execution 提升为执行层下的 active child problem，并补入 deterministic Wasm/dMIR、lazy JIT、gas/trap、Solidity-to-Wasm 和 EVM ABI compatibility route。 | arXiv preprint; benchmark evidence; SmartCogent and zkVM directions remain source-local/future-candidate evidence | Abstract, §3-§5 |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom: A Deterministic Execution Framework Towards Nested Contract Transactions]] | paper | 将 nested smart-contract call execution 补入执行层，创建 [[nested-contract-transaction-execution|Nested contract transaction execution]]，并建立 smart-contract execution 到 transaction processing 的 bridge。 | Permissioned prototype; TPC-C-like smart contracts; assumes deterministic ordering service; not a VM runtime or consensus paper. | p1-p14 |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database: Design and Implementation of a Blockchain Relational Database]] | paper | 新增 database-backed execution route：PostgreSQL + SSI/MVCC + block ordering + SQL smart contracts + provenance queries | permissioned setting; checkpoint flow not implemented; index/determinism constraints | p1-p15 |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Blurring the Lines between Blockchains and Database Systems: the Case of Hyperledger Fabric]] | paper | 补入 Fabric++ block-local transaction reordering 和 early abort 路线，说明数据库事务管理思想可在 Fabric EOV 管线内减少 invalid transactions | Fabric/Fabric++ source instance; block-local reordering; permissioned LAN evaluation | p1-p18 |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on Execute-Order-Validate Blockchains]] | paper | 新增 Fabric/FastFabric EOV 交易处理路线：用 OCC-style dependency analysis 和 reordering 减少 invalid transactions | permissioned EOV setting; source-specific systems are FabricSharp/FastFabricSharp | p1-p17 |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha: Exploiting Concurrency for Transaction Processing in DAG-based Blockchains]] | paper | 新增 DAG-based blockchain transaction-processing route：ACG + HS 在 epoch-level concurrent blocks 上降低 conflict detection/sorting 开销并保持 commit concurrency | OHIE/EVM prototype; account-based DAG; SmallBank workload; no production deployment evidence | p1-p11 |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing]] | paper | 新增 stateless/off-chain execution route：consensus nodes 用 compact commitments、read/write evidence、partial Merkle trie 和 OCC/SSI 验证并提交 smart-contract 交易 | SGX-centered prototype; storage-node availability/incentives outside core solution; storage sharding does not scale consensus layer | p1-p13 |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain: Towards High-performance, Confidential and Secure Layer-2 Blockchain Solution for Decentralized Applications]] | paper | 新增 layer-2 DApp SEM route：L2 local ordering/TEE execution 与 L1 accumulator split/merge state digest 共同定义执行边界。 | TEE trust; accumulator witness overhead; state contention and L1 latency; not a full rollup/DA/fraud-proof foundation | p1-p14 |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`。
- Freshness: `fresh` for current-vault evidence, not a latest-news claim。
- 综合: 当前 blockchain execution 方向是 `foundation_thin`。TELL 提供了一个清晰信号: 当 consensus 由多个 instances 并行运行时，execution layer 的问题从“按顺序回放交易”变成“如何在不破坏确定性的前提下，避免慢 consensus instance 阻塞快速 instance，并把多个实例的执行结果合并为一致状态”。AHL 提供的信号是: general-workload sharding 下，execution 还要处理跨 shard prepare/commit/abort、locks 和 coordinator availability。LightCross 使 cross-shard transaction execution 升级为正式 child problem: 任意智能合约跨片调用可以通过 TEE executor、R-shard 排序和 S-shard bitmap validation 处理，而不是只靠 2PC/2PL 式手工拆分。ZKCPlus 与 RC-S-P 共同扩展了执行/交易方向中的应用级 payment/lock/finalize 子问题: 前者面向数字商品/数据/模型/SQL 结果交换，后者面向 recurring verifiable service payment，并把 proof-status privacy、malicious-client security 和 dispute attribution 拉入交易协议层。Blockchain Meets Database 则把 execution substrate 拉到关系数据库侧: SQL smart contracts、SSI/MVCC 和 provenance 可以服务区块链执行，但要受共识 block order 和互不信任副本模型约束。Fabric++ 与 A Transactional Perspective on EOV Blockchains 共同说明另一条更轻的迁移路径: 不替换 Fabric/FastFabric substrate，而是在 EOV ordering/validation 边界迁移数据库式 conflict graph、early abort 和 OCC/serializability 分析来减少无效交易。Nezha 进一步把执行层并发路线扩展到 DAG block production: 共识阶段只产生并发 blocks，执行阶段再对 epoch 内交易做并发模拟、地址级冲突图和层级排序。SlimChain 进一步说明 execution layer 也可以围绕 stateless consensus node 重构: full state 和执行搬到 off-chain storage nodes 后，交易处理协议必须把可验证执行、read/write set、partial Merkle trie 和 state-root update 绑定在一起。L2chain 进一步说明 execution layer 可以围绕 layer-2 DApp network 重构: L1 只维护 available-state digest，L2 负责 local ordering 和 TEE execution，并通过 split/merge 事务回写摘要。
- DTVM delta: DTVM 将 smart-contract-execution 从 review candidate 推成 active child problem。它补入 deterministic VM、Wasm/EVM ABI compatibility、gas/trap/resource accounting、JIT performance、host API 与 sandbox security，说明智能合约执行层不能继续只归为普通 transaction-processing。
- Loom delta: Loom 将 smart-contract-execution 与 transaction-processing 的交界具体化。DTVM 证明 VM/runtime 是独立问题；Loom 则证明合约调用树会改变交易处理的 conflict/rollback/re-execution granularity。因此 Loom 不成为顶层 child，而是推动 [[nested-contract-transaction-execution|Nested contract transaction execution]] 成为 transaction-processing 下的 active child problem，并通过 bridge 回连 smart-contract-execution。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus|TELL]] | 创建执行与交易方向，并把 leaderless consensus-aware execution 作为首个 source-backed problem | 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 Fabric/parallel EVM/cross-shard execution sources 时扩展 child nodes |
| [[arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding|AHL sharding]] | 增加 cross-shard transaction coordination route，作为 cross-shard transaction execution 的数据库式方法证据 | 方法族; 代表 Sources; 当前综合 | no | 已由 LightCross 触发独立 child node，后续比较 Chainspace/CAPER/SharPer |
| [[sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts|LightCross]] | 新增 TEE-backed smart-contract CSTx route，并将 cross-shard transaction execution 提升为 active child problem。 | 下级结构; 方法族; 代表 Sources; 当前综合 | yes | 细节进入 [[cross-shard-transaction-execution|Cross-shard transaction execution]] |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] | 新增 deterministic smart-contract VM/runtime route，并把 smart-contract-execution 从 candidate 提升为 active child problem。 | 下级结构; 方法族; 代表 Sources; 当前综合; 缺口 | yes | 通过 [[smart-contract-execution|Smart contract execution]] 维护，避免塞进普通 transaction-processing |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | 新增 nested contract transaction execution route，并建立 smart-contract-execution -> transaction-processing bridge。 | 方法族; 代表 Sources; 当前综合; Bridge Links; 缺口 | yes | 通过 [[nested-contract-transaction-execution|Nested contract transaction execution]] 维护，避免新建 Loom 节点 |
| [[doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol|ZKCPlus]] | 新增 blockchain-mediated fair exchange problem：交易锁/commitment opening/finalize 与链下 proof-of-delivery 配合。 | 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 通过 [[fair-exchange-protocols|Blockchain-based fair exchange protocols]] 维护，避免塞进 DA-only FDE 节点 |
| [[arxiv-2208-00283v2-recurring-contingent-service-payment|Recurring Contingent Service Payment]] | 新增 recurring verifiable-service payment route，并把 service-payment variants 提升为 fair-exchange 子问题。 | 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 通过 [[contingent-service-payments|Contingent service payments for verifiable services]] 维护 |
| [[arxiv-1903-01919v2-blockchain-meets-database-relational-database|Blockchain Meets Database]] | 新增 database-backed execution route，并建立 database transaction processing -> blockchain execution bridge。 | 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续用 Fabric++/parallel execution/database-backed blockchain sources 继续复核 bridge 边界 |
| [[doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric|Fabric++]] | 补入 Hyperledger Fabric 的 block-local transaction reordering、unique-key batch cutting 和 early abort 作为 EOV source extension。 | 方法族; 代表 Sources; 当前综合; Bridge Links | no | 继续用 Nezha/parallel execution/modern Fabric sources 判断是否拆 `execute-order-validate` child |
| [[arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains|A Transactional Perspective on EOV Blockchains]] | 新增 EOV dependency-graph reordering route，作为 transaction-processing 子问题下的 source extension。 | 方法族; 代表 Sources; 当前综合; Bridge Links | no | 等 Fabric++/Nezha/parallel execution sources 后复核 child split |
| [[doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing|Nezha]] | 新增 DAG-based blockchain execution route：address-based conflict graph、hierarchical sorting、epoch-level concurrent block execution。 | 方法族; 代表 Sources; 当前综合; Bridge Links | no | 通过 [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] 维护，不新建 Nezha 节点 |
| [[doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing|SlimChain]] | 新增 stateless/off-chain smart-contract execution route，并把 state-storage commitment 与 transaction-processing commit/abort 的关系显式化。 | 方法族; 代表 Sources; 当前综合; Bridge Links | yes, creates bridge | 通过 [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] 和 [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] 维护 |
| [[doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps|L2chain]] | 新增 layer-2 DApp split-execute-merge execution route，并强化 state-storage commitment 与 transaction-processing 的 bridge。 | 方法族; 代表 Sources; 当前综合; Bridge Links | no, strengthens bridge | 通过 [[04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing|Blockchain transaction processing]] 和 [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] 维护 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[permissioned-consensus-to-transaction-execution|Permissioned consensus -> transaction execution]] | `blockchain-systems/consensus/permissioned-blockchain-consensus; blockchain-systems/execution-and-transactions/transaction-processing/leaderless-consensus-execution` | dependency, co_evolution, implementation_reuse, tension | 可迁移的是 consensus instance 状态对 execution scheduling/commit 的约束；不能把 execution 优化当成 consensus safety 证明。 | active_seed |
| [[commit-and-prove-arguments-to-fair-exchange-protocols|Commit-and-prove arguments -> blockchain fair exchange protocols]] | `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments; blockchain-systems/execution-and-transactions/fair-exchange-protocols` | dependency, application, proof_protocol_enabler | CP-NIZK 证明 committed data / ciphertext / predicate consistency；交易锁、超时退款和付款公平性仍是 fair-exchange 协议层。 | active_seed |
| [[database-transaction-processing-to-blockchain-execution|Database transaction processing -> blockchain execution]] | `distributed-systems/transaction-processing; blockchain-systems/execution-and-transactions/transaction-processing` | translation, implementation_reuse, dependency, trust_model_shift | 可迁移的是 SSI/MVCC/stored procedures/provenance；共识安全、开放网络治理和 Byzantine ordering 仍属于区块链系统层。 | active_seed |
| [[blockchain-state-storage-to-transaction-processing|Blockchain state storage -> transaction processing]] | `blockchain-systems/data-management-and-storage/blockchain-state-storage; blockchain-systems/execution-and-transactions/transaction-processing` | dependency, shared_state_commitment, implementation_reuse, tension | state commitment/proof format constrains validation and commit; execution proof, storage-node liveness, DA and consensus safety remain separate. | active_seed |
| [[verifiable-computation-systems-to-contingent-service-payments|Verifiable computation systems -> contingent service payments]] | `verifiable-computation/verifiable-computation-systems; blockchain-systems/execution-and-transactions/fair-exchange-protocols/contingent-service-payments` | dependency, application, payment_finality_boundary | VC/VS/PoR proof validity transfers into service payment only as correctness evidence; escrow, deposits, privacy window and coin distribution remain execution/fair-exchange responsibilities. | active_seed |
| [[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/smart-contract-execution; blockchain-systems/execution-and-transactions/transaction-processing` | dependency, granularity_shift, conflict_modeling, execution_cost_substrate | Smart-contract runtime/call structure affects transaction-processing cost and granularity; VM semantics, serializability and consensus ordering stay bounded. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-blockchain-execution-and-transactions | is_a | nahida-knowledge-blockchain-systems | vault/04_Knowledge/blockchain-systems/execution-and-transactions.md | medium | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | has_child | nahida-knowledge-blockchain-transaction-processing | vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing.md | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | has_child | nahida-knowledge-blockchain-fair-exchange-protocols | ZKCPlus source note and fair-exchange-protocols node | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | has_child | nahida-knowledge-cross-shard-transaction-execution | cross-shard-transaction-execution node and LightCross source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | has_child | nahida-knowledge-smart-contract-execution | smart-contract-execution node and DTVM source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/sha256-69daae93b34a-tell-efficient-transaction-execution-protocol-leaderless-consensus.md | TELL source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/arxiv-1804-00399v4-towards-scaling-blockchain-systems-via-sharding.md | AHL source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3484558-zkcplus-optimized-fair-exchange-protocol.md | ZKCPlus source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/arxiv-1903-01919v2-blockchain-meets-database-relational-database.md | Blockchain Meets Database source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/doi-10-1145-3299869-3319883-blurring-lines-blockchains-database-systems-hyperledger-fabric.md | Fabric++ source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/arxiv-2003-10064v1-transactional-perspective-execute-order-validate-blockchains.md | A Transactional Perspective on EOV Blockchains source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/doi-10-1109-icdcs54860-2022-00034-nezha-dag-blockchain-transaction-processing.md | Nezha source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/doi-10-14778-3476249-3476283-slimchain-off-chain-storage-parallel-processing.md | SlimChain source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/doi-10-14778-3574245-3574278-l2chain-layer-2-blockchain-solution-dapps.md | L2chain source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/sha256-565707d2339b-lightcross-sharding-lightweight-cross-shard-execution-smart-contracts.md | LightCross source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/arxiv-2208-00283v2-recurring-contingent-service-payment.md | RC-S-P source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md | DTVM source note | high | active_seed |
| nahida-knowledge-blockchain-execution-and-transactions | evidenced_by | vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md | Loom source note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少区块链执行层 foundation source/survey。 | 目前方向已有 TELL/Fabric++/EOV/database-backed/DAG/stateless evidence，但仍不能替代 Fabric/EVM/parallel execution/stateless-client 等更广泛基础。 | `nahida-research-search` foundation_pack or continue paper intake | high | queued |
| smart contract VM / runtime / nested execution sources 仍然偏薄。 | DTVM 已推动 smart-contract-execution 成为 active child problem，Loom 已补 nested-call execution seed；还需要 EVM/Wasm foundation、parallel EVM、Block-STM、EOR、zkVM/RISC-V runtime sources 来细分方法族。 | `nahida-update` / `nahida-research-search` | high | partially_seeded |
| cross-shard transaction execution 的细分方法族仍少。 | LightCross 已足以拆出 child problem，但 Chainspace/CAPER/SharPer/OptChain 等还缺，暂不拆更细节点。 | continue paper intake | medium | queued |
| Fair exchange landscape 缺原始 ZKCP/FairSwap/FileBounty/FairDownload sources。 | ZKCPlus 足以创建 fair-exchange-protocols seed，但 strong/weak fairness 和 dispute route 比较仍薄。 | continue paper intake / nahida-research-search | high | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-tell-leaderless-consensus-execution | Created execution-and-transactions direction from TELL source; added first child transaction-processing and consensus-execution bridge. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-ahl-sharding | Added AHL as cross-shard transaction coordination source extension. | arxiv:1804.00399v4 | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcplus-fair-exchange | Added blockchain fair exchange protocols as an execution-and-transactions child problem. | doi:10.1145/3460120.3484558 | codex |
| 2026-06-22 | nahida-knowledge-20260622-blockchain-meets-database | Added database-backed blockchain execution route and database transaction-processing bridge. | arxiv:1903.01919v2 | codex |
| 2026-06-22 | nahida-knowledge-20260622-transactional-perspective-eov | Added EOV dependency-graph reordering as a transaction-processing source extension. | arxiv:2003.10064v1 | codex |
| 2026-06-22 | nahida-knowledge-20260622-fabric-plus-plus-transaction-processing | Added Fabric++ block-local transaction reordering and early abort as an EOV transaction-processing source extension. | doi:10.1145/3299869.3319883 | codex |
| 2026-06-22 | nahida-knowledge-20260622-nezha-dag-transaction-processing | Added Nezha as DAG epoch-level concurrent execution and address-dependency concurrency-control source extension. | doi:10.1109/icdcs54860.2022.00034 | codex |
| 2026-06-22 | nahida-knowledge-20260622-slimchain-stateless-execution-storage | Added SlimChain as stateless/off-chain smart-contract execution route and linked execution to state-storage commitments. | doi:10.14778/3476249.3476283 | codex |
| 2026-06-23 | nahida-knowledge-20260623-l2chain-layer-2-blockchain-solution | Added L2chain as layer-2 DApp split-execute-merge execution route and strengthened state-storage bridge. | doi:10.14778/3574245.3574278 | codex |
| 2026-06-22 | nahida-knowledge-20260622-lightcross-cross-shard-smart-contracts | Added LightCross and promoted cross-shard transaction execution to an active child problem under execution-and-transactions. | sha256:565707d2339b7b44f2437db61030c765bacce1f34e243a5c339ef1a2f97442a2 | codex |
| 2026-06-23 | nahida-knowledge-20260623-recurring-contingent-service-payment | Added RC-S-P as recurring verifiable-service payment route under fair exchange. | arxiv:2208.00283v2 | codex |
| 2026-06-23 | nahida-knowledge-20260623-dtvm-smart-contract-execution | Added DTVM and promoted smart-contract-execution to an active child problem under execution-and-transactions. | arxiv:2504.16552v2 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-loom-nested-contract-transactions | Added Loom as nested contract transaction execution route and bridge between smart-contract execution and transaction processing. | sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd | codex |
