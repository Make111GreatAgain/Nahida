---
id: "nahida-knowledge-smart-contract-execution"
title: "Smart contract execution"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "smart-contract-execution"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
parent_knowledge_refs:
  - "nahida-knowledge-blockchain-execution-and-transactions"
child_knowledge_refs:
  - "nahida-knowledge-nested-contract-transaction-execution"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "smart-contract-execution"
primary_ontology_path: "blockchain-systems/execution-and-transactions/smart-contract-execution"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-smart-contract-execution"
    relation: "is_a"
    to: "nahida-knowledge-blockchain-execution-and-transactions"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/smart-contract-execution.md"
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-smart-contract-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-smart-contract-execution"
    relation: "has_child"
    to: "nahida-knowledge-nested-contract-transaction-execution"
    evidence_refs:
      - "vault/04_Knowledge/blockchain-systems/execution-and-transactions/transaction-processing/nested-contract-transaction-execution.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-smart-contract-execution"
    relation: "bridges_to"
    to: "nahida-bridge-smart-contract-execution-to-transaction-processing"
    evidence_refs:
      - "vault/05_Bridges/smart-contract-execution-to-transaction-processing.md"
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-smart-contract-execution"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-smart-contract-execution-to-transaction-processing"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md"
  - "vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md"
representative_source_refs:
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
query_keys:
  - "smart contract execution"
  - "smart contract virtual machine"
  - "deterministic smart contract runtime"
  - "deterministic VM"
  - "WebAssembly smart contract runtime"
  - "EVM ABI compatibility"
  - "Solidity to Wasm"
  - "lazy JIT smart contracts"
  - "dWasm"
  - "dMIR"
  - "nested contract transaction execution"
  - "nested smart contract calls"
  - "smart contract concurrency control"
  - "subtransaction-level rollback"
  - "Loom"
aliases:
  - "智能合约执行"
  - "Smart contract runtime"
  - "Smart contract VM"
  - "Deterministic smart contract VM"
domains:
  - "blockchain-systems"
topics:
  - "smart-contract-execution"
  - "deterministic-runtime"
  - "smart-contract-vm"
  - "gas-metering"
  - "evm-compatibility"
  - "nested-contract-calls"
  - "smart-contract-concurrency-control"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-dtvm-smart-contract-execution"
  - "nahida-paper-intake-20260623-loom-nested-contract-transactions"
source_refs:
  - "arxiv:2504.16552v2"
  - "sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd"
confidence: "medium"
trust_tier: "primary"
---

# Smart contract execution

## 定义与范围

- 定义: Smart contract execution 关注区块链节点如何加载、验证、运行、计费并 sandbox 智能合约，使所有正确节点在同一输入和链上上下文下得到相同输出、状态更新、trap 和 gas 消耗。
- 核心对象: smart contract VM/runtime、bytecode/IR、gas/resource metering、host API、memory/table/stack management、trap semantics、ABI/language compatibility、runtime security 和 execution performance。
- 不包含: 单篇 VM 系统名、某个 benchmark 数字、交易排序、consensus safety、跨链调用协议或任意智能合约应用逻辑；这些分别留在 source note、transaction-processing、consensus 或 interoperability 节点中。
- Canonical terms: `smart contract execution`, `smart contract VM`, `deterministic runtime`, `gas metering`, `EVM compatibility`, `Wasm smart contract runtime`.
- Standalone completeness check: 本节点解释问题边界、方法族、DTVM source delta、与交易处理的区别和未来缺口；当前只有 DTVM 作为直接强 source，因此状态为 `foundation_thin`。
- Retrieval role: 当查询 EVM/Wasm VM、deterministic contract runtime、Solidity-to-Wasm、gas/trap/JIT、TEE-ready contract execution 时，从本节点进入，而不是直接进入某篇 source 或泛化到 transaction processing。
- Update scope: 新资料涉及 EVM/Wasm/RISC-V VM、parallel EVM、deterministic execution framework、runtime gas/trap rules、smart-contract JIT/AOT、Solidity compiler/runtime adaptation、zkVM contract execution 或 smart-contract execution security，应刷新本节点。

## 背景

区块链智能合约执行层处在 consensus order 和 application logic 之间。Consensus 可以决定交易或区块顺序，但执行层必须把合约代码、状态读写、host API、gas、trap、内存访问和 ABI 都变成所有节点可重复的状态转移。

这使 smart contract execution 比普通 VM 更受约束：浏览器或服务器 VM 可以容忍部分平台差异、非确定性时间源或实现相关异常；链上 runtime 不能。一个节点因为 stack overflow depth、NaN payload、host function、out-of-bounds trap 或 gas 扣减差异而得到不同结果，就可能破坏状态一致性。

当前 vault 的直接证据首先来自 [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]]。DTVM 把该问题表达为“WebAssembly/EVM ABI compatibility + deterministic IR/runtime + lazy JIT + gas/trap/security/toolchain”的系统问题，因此足以把父方向中原先的 `smart-contract-execution` candidate 提升为 active problem node。

[[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] 补上第二类证据: 合约调用结构本身会进入交易处理层。Loom 不研究 VM 字节码或 gas/trap，而是说明多层 contract invocation 可以被表示成 nested transaction tree，并进一步决定 subtransaction-level conflict、partial rollback 和 re-execution schedule。它因此不改变本节点的 VM/runtime 定义，但推动 [[nested-contract-transaction-execution|Nested contract transaction execution]] 作为本节点与 [[transaction-processing|Blockchain transaction processing]] 之间的 child/bridge problem。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`。
- 为什么足够通用: 它覆盖 EVM、Wasm runtime、deterministic execution、gas/resource accounting、JIT/AOT、language/ABI compatibility、TEE deployment 与未来 zkVM contract execution 等多个 source family。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: DTVM 是一个代表系统；dMIR、dWasm、Zeta Engine、SmartCogent 是 DTVM 的 source-specific mechanisms，不应单独提升成上层节点，除非后续 source 重复使用这些抽象。
- 需要引用的更基础 Knowledge: [[execution-and-transactions|Blockchain execution and transactions]]；secondary adjacent node 是 [[transaction-processing|Blockchain transaction processing]]，但本节点不等于交易并发控制。
- 不应拆出的实例/来源: DTVM、Zeta Engine、SmartCogent、单次 benchmark 或某个语言 SDK 暂不建独立知识节点。

## 解决的问题

本节点回答: 智能合约 VM/runtime 如何在兼容现有合约生态的同时，提供高性能、可计费、可 sandbox、跨平台确定且可审计的执行。

典型子问题包括:

- 如何在 EVM/Solidity 生态兼容和 Wasm/RISC-V 等高性能 runtime 之间建立桥接。
- 如何规范 stack overflow、trap、NaN、浮点、host functions、resource limits 和 memory bounds，避免不同节点执行差异。
- 如何把 gas metering、integer overflow、memory boundary checks 放入解释器/JIT/AOT pipeline。
- 如何让 lazy JIT 或 AOT 性能优化不改变 deterministic execution semantics。
- 如何限制 JIT dynamic code generation 的攻击面，并支持 TEE 或其他硬件隔离环境。
- 如何让多语言合约 SDK、ABI、storage/events/host APIs 与链上执行模型一致。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[execution-and-transactions|Blockchain execution and transactions]] | child_of | DTVM source shows VM/runtime determinism and performance as an execution-layer problem distinct from transaction ordering. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| deterministic-smart-contract-runtime | method/problem candidate | dWasm/dMIR 类约束专门处理跨平台确定性、trap 和 host-function 边界 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] | review |
| wasm-smart-contract-runtime | method family candidate | Wasm 提供多语言和性能基础，但需要链上 deterministic/resource constraints | DTVM §2-§4 | review |
| evm-compatibility-layer | method family candidate | Solidity/EVM ABI 兼容决定迁移成本和 ecosystem adoption | DTVM §3-§4.7 | review |
| smart-contract-jit-aot | optimization candidate | JIT/AOT/interpretation 是合约性能与安全/信任模型的主要 tradeoff | DTVM §4.1-§4.2, §4.8 | review |
| [[nested-contract-transaction-execution|Nested contract transaction execution]] | bridge/problem child | 合约调用树会改变交易处理粒度，但问题核心仍是 deterministic transaction processing / rollback / re-execution，因此作为跨节点 child/bridge 保留。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | active_seed |
| zkvm-contract-execution | future bridge candidate | DTVM conclusion 提到 ZK-optimized VM variants，但无具体 construction | DTVM §6 only | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Interpreted EVM execution | 按 EVM bytecode stack semantics 解释执行，天然贴近 Ethereum compatibility。 | Solidity/EVM-first chains; 兼容优先。 | 复杂合约和 compute-heavy workload 性能受限。 | model_prior_background |
| General-purpose Wasm VM reuse | 使用 Wasmtime/Wasmer 等通用 Wasm runtime 获得多语言与 JIT 能力。 | 不需要严格链上确定性或愿意额外约束 runtime。 | standard Wasm 的 stack/trap/resource/host behavior 不直接满足共识确定性。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] related work |
| Deterministic Wasm/dMIR runtime | 在 module validation、IR generation、runtime stack/memory/trap/host API 上施加 deterministic constraints，再进入 JIT。 | 需要跨 CPU/OS/VM implementation 一致执行的链上 runtime。 | 需要维护专用规范、compiler pipeline 和 host API contract。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| Function-level lazy JIT | 先生成 stub，让函数首次调用时通过 trampoline/resolver 编译并 patch entry；热函数获得 native-code 性能，冷函数减少首次加载成本。 | 合约部署/首次调用 latency 敏感，且 runtime 可安全生成 native code。 | JIT code memory、patching、thread-safety 和 lifecycle synchronization 增加安全复杂度。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| JIT-integrated gas and trap checks | 在 basic block/IR/native code 中直接嵌入 gas 扣减、overflow trap、memory guard handling。 | 执行成本必须可计费且 deterministic。 | 编译器和 runtime 必须共同维护 gas state、host API synchronization 和 trap path。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| Solidity-to-Wasm / EVM ABI compatibility | 复用 Solidity/Yul frontend，将合约转为 Wasm，同时保留 ABI、storage、events 和 host API 兼容。 | 需要 Ethereum ecosystem 迁移和多语言 runtime。 | 编译器适配复杂；必须证明 ABI/storage semantics 不被破坏。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| TEE-ready minimal runtime | 减少 VM codebase/TCB，并用 sandbox, guard pages, constrained control flow 支持 TEE integration。 | 需要 confidential/secure execution 或硬件隔离 deployment。 | TEE threat model、side channels、attestation 与 consensus-layer trust 仍需单独处理。 | [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] |
| Nested call structure as execution granularity | 将多层跨合约调用视为 transaction tree/subtransactions，使交易处理层可以利用 weak/strong dependency 做 partial rollback 和 fine-grained re-execution。 | 执行框架能确定性捕获调用树、读写集和依赖类型。 | 不是 VM/runtime route；需要 transaction-processing 层保证 serializability、snapshot 和 rollback order。 | [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility]] | paper | 创建 smart-contract-execution 问题节点；补入 deterministic Wasm/dMIR、lazy JIT、hardware guard pages、gas metering、overflow hooks、Solidity-to-Wasm/EVM ABI compatibility、TEE-ready runtime 和 AI-assisted tooling。 | arXiv preprint; benchmark-based evidence; SmartCogent 指标是 source-local tool evaluation；zkVM/RISC-V 只是 future direction。 | Abstract, §3-§5, §6 |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom: A Deterministic Execution Framework Towards Nested Contract Transactions]] | paper | supporting structural evidence: nested contract calls define subtransaction boundaries and therefore connect smart-contract execution to transaction-processing conflict/rollback granularity。 | Primary placement is nested contract transaction execution under transaction-processing; not a VM/runtime paper. | p1-p14 |

## 当前综合

- Evidence window: `2026-06-23`。
- Freshness: `fresh` for current-vault evidence; not external latest check.
- Valid until: `2026-07-23`。
- 综合: 当前节点是 `foundation_thin`。DTVM 首次给 vault 提供完整 smart-contract runtime 证据：智能合约执行层不是简单 transaction-processing 的子句，而是由 VM semantics、determinism、gas、trap、host API、language/ABI compatibility、JIT performance 和 sandbox security 共同构成的独立问题。Loom 随后补上结构侧证据：智能合约调用树会进入交易处理层，形成 [[nested-contract-transaction-execution|Nested contract transaction execution]]。因此本节点需要同时保留两条边界: DTVM 类 runtime 机制属于本节点内部；Loom 类 nested-call scheduling 属于与 transaction-processing 的 bridge/child problem。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution|DTVM]] | 将 smart-contract-execution 从父方向 candidate 提升为 active problem；把 DTVM 作为 deterministic Wasm VM + lazy JIT + EVM ABI compatibility source extension。 | 定义、背景、解决的问题、方法族、代表 Sources、缺口 | yes | 后续吸收 Loom/parallel EVM/zkVM sources 时继续填充 child candidates |
| [[sha256-ad4df792f387-loom-deterministic-nested-contract-transactions|Loom]] | 增加 nested call structure 作为交易处理粒度的 source extension；创建 smart-contract-execution -> transaction-processing bridge 和 nested-contract child problem。 | 背景、下级结构、方法族、代表 Sources、当前综合、Bridge Links、关系图谱 | yes | 后续吸收 Block-STM/parallel EVM/EOR 时复核是否拆 smart-contract concurrency 子节点 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[smart-contract-execution-to-transaction-processing|Smart contract execution -> blockchain transaction processing]] | `blockchain-systems/execution-and-transactions/smart-contract-execution` -> `blockchain-systems/execution-and-transactions/transaction-processing` | dependency, granularity_shift, conflict_modeling, execution_cost_substrate | Contract runtime performance/gas/trap and nested call structure affect transaction execution cost/granularity; transaction ordering, concurrency control and consensus safety do not transfer back into VM semantics. | active_seed |
| smart-contract-execution -> verifiable computation / zkVM | pending | future_bridge_candidate | DTVM only states future ZK-optimized VM variants; no concrete source-backed transfer yet. | queued |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-smart-contract-execution | is_a | nahida-knowledge-blockchain-execution-and-transactions | DTVM source note; execution-and-transactions parent | high | active_seed |
| nahida-knowledge-smart-contract-execution | evidenced_by | vault/03_Sources/papers/arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution.md | DTVM Abstract, §3-§5 | high | active_seed |
| nahida-knowledge-smart-contract-execution | has_child | nahida-knowledge-nested-contract-transaction-execution | Loom source note | high | active_seed |
| nahida-knowledge-smart-contract-execution | bridges_to | nahida-bridge-smart-contract-execution-to-transaction-processing | bridge note | high | active_seed |
| nahida-knowledge-smart-contract-execution | evidenced_by | vault/03_Sources/papers/sha256-ad4df792f387-loom-deterministic-nested-contract-transactions.md | Loom nested call model | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| 缺少 EVM/Wasm smart-contract runtime survey 或 canonical foundation source。 | DTVM 已足以开节点，但不能替代 EVM/Wasm/runtime foundation。 | `nahida-research-search` foundation_pack or continue paper intake | high | queued |
| 缺少 parallel EVM / Block-STM / optimistic execution sources。 | 这些会决定是否拆 `parallel-smart-contract-execution` 或并入 transaction-processing。 | continue paper intake / web search | high | queued |
| 缺少 nested-call execution 对照源。 | Loom 建立 active seed，但还需要 EOR、Block-STM、parallel EVM、SChain 或 database nested transaction direct sources 验证方法谱系。 | continue paper intake / `nahida-research-search` | high | queued |
| DTVM repo 未单独分析。 | 论文提到开源 stack；repo source 可验证架构、模块边界和实现状态。 | `nahida-github-repo-analyze` | medium | queued |
| zkVM/RISC-V smart-contract execution 仍只是 future bridge。 | DTVM conclusion 暗示路线，但无 construction；需要 RISC0/SP1/Jolt/Valida/zkVM sources。 | continue paper intake / `nahida-research-search` | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-dtvm-smart-contract-execution | Created smart-contract-execution problem node from DTVM; separated VM/runtime determinism from generic transaction processing. | arxiv:2504.16552v2 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-loom-nested-contract-transactions | Added Loom as structural evidence that nested contract calls shape transaction-processing granularity; created bridge and child problem. | sha256:ad4df792f387b4509bffe4efebeada8c727f838beec9d895ed4a4ab0722180dd | codex |
