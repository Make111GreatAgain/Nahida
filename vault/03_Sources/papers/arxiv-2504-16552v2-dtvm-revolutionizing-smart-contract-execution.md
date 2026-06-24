---
id: "arxiv-2504-16552v2-dtvm-revolutionizing-smart-contract-execution"
title: "DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility"
type: "source"
source_kind: "paper"
source_subtype: "local_pdf"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
hierarchy_level: "source"
created: "2026-06-23"
updated: "2026-06-23"
authors:
  - "Wei Zhou"
  - "Xiong Xu"
  - "Changzheng Wei"
  - "Ying Yan"
  - "Wei Tang"
  - "Zhihao Chen"
  - "Xuebing Huang"
  - "Wengang Chen"
  - "Jie Zhang"
  - "Yang Chen"
  - "Xiaofu Zheng"
  - "Hanghang Wu"
  - "Shenglong Chen"
  - "Ermei Wang"
  - "Xiangfei Chen"
  - "Yang Yu"
  - "Meng Wu"
  - "Tao Zhu"
  - "Liwei Yuan"
  - "Feng Yu"
  - "Alex Zhang"
  - "Wei Wang"
  - "Ji Luo"
  - "Zhengyu He"
  - "Wenbiao Zhao"
year: 2025
venue: "arXiv:2504.16552v2"
publisher: "arXiv"
source_refs:
  - "arxiv:2504.16552v2"
  - "doi:10.48550/arXiv.2504.16552"
  - "sha256:ec497e17bf9a59bc1023598e8263ce16cca62239cedb90e332a0b65e67653a24"
canonical_url: "https://arxiv.org/abs/2504.16552v2"
doi: "10.48550/arXiv.2504.16552"
arxiv_id: "2504.16552v2"
local_pdf_path: "~/Desktop/paper/dtvm.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/dtvm-ec497e17bf9a-pages.txt"
pages: 33
page_count: 33
reading_depth: "deep_read"
reading_status: "deep_read_complete"
safe_for_absorption: true
classification_status: "corrected_absorbed"
classification_confidence: "high"
primary_domain: "blockchain-systems"
primary_direction: "execution-and-transactions"
domain_id: "blockchain-systems"
direction_id: "execution-and-transactions"
primary_ontology_path: "blockchain-systems/execution-and-transactions/smart-contract-execution"
ontology_path:
  - "blockchain-systems"
  - "execution-and-transactions"
  - "smart-contract-execution"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/transaction-processing"
topic_ids:
  - "smart-contract-execution"
  - "deterministic-virtual-machine"
  - "webassembly-smart-contract-runtime"
  - "evm-abi-compatibility"
  - "lazy-jit-compilation"
  - "deterministic-gas-metering"
  - "tee-ready-smart-contract-runtime"
  - "ai-assisted-smart-contract-development"
domains:
  - "blockchain-systems"
topics:
  - "smart contract execution"
  - "deterministic virtual machine"
  - "WebAssembly smart contract runtime"
  - "EVM ABI compatibility"
  - "lazy JIT compilation"
  - "dMIR"
  - "dWasm"
aliases:
  - "DTVM"
  - "DeTerministic Virtual Machine Stack"
  - "DTVM Stack"
tags:
  - "nahida/source"
  - "nahida/source/paper"
  - "blockchain-systems"
  - "smart-contract-execution"
classification_evidence:
  - "local PDF deep read p1-p33"
  - "Title and abstract identify smart contract execution, determinism, EVM ABI compatibility, WebAssembly, lazy JIT and runtime compatibility as the main problem."
  - "Sections 3-4 define DTVM Engine, dMIR/dWasm, Zeta Engine, VM Runtime, gas metering, boundary checks, integer-overflow traps, deterministic execution constraints and Solidity-to-Wasm tooling."
  - "Section 5 evaluates EVM/Wasm VM execution and first-invocation latency rather than transaction ordering, concurrency control, or consensus safety."
knowledge_node_refs:
  - "[[smart-contract-execution|Smart contract execution]]"
  - "[[execution-and-transactions|Blockchain execution and transactions]]"
  - "[[transaction-processing|Blockchain transaction processing]]"
bridge_refs: []
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0105"
run_id: "nahida-knowledge-20260623-dtvm-smart-contract-execution"
managed_by: "nahida"
confidence: "high"
trust_tier: "primary"
---

# DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility

## Paper Identity

| 字段 | 内容 |
| --- | --- |
| 论文 | DTVM: Revolutionizing Smart Contract Execution with Determinism and Compatibility |
| 副标题 | Featuring EVM Compatibility, Multi-Language Support, Diverse Security Hardware Integration, and AI-Ready Extensions for Enhanced Smart Contract Execution |
| 作者 | Wei Zhou; Xiong Xu; Changzheng Wei; Ying Yan; Wei Tang; Zhihao Chen; Xuebing Huang; Wengang Chen; Jie Zhang; Yang Chen; Xiaofu Zheng; Hanghang Wu; Shenglong Chen; Ermei Wang; Xiangfei Chen; Yang Yu; Meng Wu; Tao Zhu; Liwei Yuan; Feng Yu; Alex Zhang; Wei Wang; Ji Luo; Zhengyu He; Wenbiao Zhao |
| 年份 | 2025 |
| arXiv | `2504.16552v2` |
| DOI | `10.48550/arXiv.2504.16552` |
| 本地 PDF | `~/Desktop/paper/dtvm.pdf` |
| 校验和 | `sha256:ec497e17bf9a59bc1023598e8263ce16cca62239cedb90e332a0b65e67653a24` |

## Reading Coverage

| 范围 | 覆盖 |
| --- | --- |
| PDF extraction | `pypdf` extraction usable; 33 pages. |
| 覆盖章节 | Abstract, §1 Introduction, §2 Related Work, §3 Architecture, §4 Technical Implementation, §5 Evaluation, §6 Conclusion, Appendix A-B. |
| 元数据修正 | Queue title/authors/year/arXiv metadata match the first page and PDF metadata. DOI was normalized from metadata URL to `10.48550/arXiv.2504.16552`. |
| 分类修正 | Queue staged path was `blockchain-systems/execution-and-transactions/transaction-processing`; deep read shows the primary problem is [[smart-contract-execution|smart contract execution]], with transaction processing only secondary. |

## One-Sentence Takeaway

DTVM 是一个面向区块链智能合约的确定性 VM/runtime stack：它用 dMIR/dWasm、hybrid lazy-JIT、hardware-backed sandboxing、deterministic gas/trap rules 和 Solidity-to-Wasm/EVM ABI compatibility，把高性能 JIT 执行与跨节点确定性放在同一个执行层问题中处理。

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | blockchain systems | smart contract execution, Ethereum compatibility, blockchain determinism, gas and host API constraints | high | existing domain |
| Direction | execution and transactions | source targets execution runtime after ordering, not consensus safety or bridge protocol | high | existing direction |
| Research problem | smart contract execution | paper's title/abstract/§3-§5 center VM/runtime, determinism, ABI/language compatibility and performance | high | create problem node |
| Secondary problem | transaction processing | gas/resource accounting, contract invocation, host state access and execution latency affect transaction processing | medium | secondary evidence only |
| Method family | deterministic WebAssembly VM; deterministic middle IR; lazy JIT; EVM ABI compatible runtime | §3-§4 | high | source extension under problem node |
| Bridge candidate | zkVM / verifiable computation | conclusion proposes future ZK-optimized VM variants, but no construction is given | low | keep as queued bridge candidate, not a durable bridge |
| Source instance | DTVM Stack | named system/open-source stack | high | source note, not a standalone knowledge node |

## Structured Summary

### Problem

区块链智能合约执行层需要同时满足几个互相牵制的约束：所有验证节点必须在相同输入上得到相同状态变化和 gas 结果；执行性能不能停留在低效解释器；Ethereum/Solidity/EVM ABI 生态不能被完全抛弃；运行时还需要 sandbox、安全边界、host API、gas accounting 和开发工具。

标准 EVM 的优点是确定性和生态兼容，但栈式解释执行容易成为复杂合约与高吞吐链的瓶颈。通用 WebAssembly runtime 有性能和多语言优势，但默认 Wasm 对浮点、trap、资源限制、host functions 和 stack overflow 等方面没有区块链共识所需的严格跨平台确定性。DTVM 的核心动机就是在这两个系统之间补上一个“面向链上合约的确定性高性能 VM”。

### Architecture

DTVM Stack 分为 Engine、SDK 和 Tools，并在 Engine 内分出 core、execution、adaptation、toolchain 等层次。

- **dMIR / dWasm:** Deterministic Middle IR 与 deterministic WebAssembly 约束层，把 Wasm、EVM 和未来 RISC-V frontends 统一到一个可优化但可确定验证的 IR。
- **Zeta Engine:** 多层优化/JIT 引擎，支持 O0/O1/O2 和 lazy compilation；以 dMIR 为输入，生成平台相关 CGIR 和 native code。
- **VM Runtime:** 提供 deterministic stack/memory/table/global 管理、host API、gas、trap 和 resource cleanup；通过 VM Native Interface 管理外部调用。
- **SDK / language support:** 支持 Solidity-to-Yul-to-Wasm、Rust、Go、C/C++、AssemblyScript、Java 等路线，同时保留 EVM ABI 互操作。
- **SmartCogent:** 用 LLM/RAG/多 agent 处理智能合约生成、编译、审计、修复、依赖分析与部署。

### Lazy JIT And Trampoline Hot-Switch

DTVM 的 JIT pipeline 先 decode/validate Wasm，再做 deterministic checks/transforms，生成 dMIR，随后映射到 CGIR/native code。它不是一次性急切编译所有函数，而是用 stub 函数和 trampoline resolver 延迟编译。

每个未编译函数先指向一个极小 stub；首次调用时进入 `stubResolver`，保存通用寄存器和浮点/向量寄存器，调用 `compileOnRequestTrampoline` 编译目标函数，把返回地址改写为新生成的 native code entry，然后恢复寄存器并 `ret` 到已编译代码。编译完成后，stub 的 patch point 会被原子更新，后续调用直接进入优化代码。

这条路线的系统含义是：合约部署/加载后可以快速进入可调用状态，把真实编译成本延迟到函数热路径；同时通过幂等编译、原子 patch 和 runtime lifecycle synchronization 处理多线程并发首次调用。

### Deterministic Runtime Constraints

DTVM 将标准 Wasm 可能导致不确定性的来源系统性收紧：

- 静态/加载期：固定 function 参数、locals、stack frame、instruction count、control-flow nesting、memory/table/import/export 等资源上限；严格验证顺序；不接受可导致实现差异的格式特征。
- 执行期：约束浮点、NaN、类型转换、host functions、memory/atomic operations；禁止非确定性 host input，或把它们替换为区块链上下文中的确定输入。
- trap/异常期：统一 stack overflow、out-of-bounds、division by zero、resource exhaustion 等 trap 类型和 gas 消耗边界。
- lazy JIT 边界：确定性检查提前到 dMIR generation 之前，避免模块在 lazy execution 时才因为不同编译模式暴露不一致。

Table 5 的例子显示，Wasmtime/Wasmer 在 x86-64 与 ARM 上的 stack overflow depth 不一致；DTVM 在相同递归场景下返回一致的 call stack/trap 行为。

### Memory Safety, Gas And Overflow

DTVM 用硬件页保护替代大量软件边界检查。它为每个 Wasm instance 预留 8GB virtual address space，仅实际线性内存区域用 `mprotect` 设为读写，其余区域保持 guard pages。JIT 生成直接 load/store；越界访问触发 SIGSEGV/page fault，再由 VM signal handler 判断 faulting address 和 JIT code region，转换为 deterministic Wasm trap。

Gas metering 直接嵌入 JIT 代码：

- FLAT/O0 侧用 dedicated physical register 记录 gas counter，在 basic block entry 生成扣减和 out-of-gas branch。
- FLAS/O1-O2 侧把 gas counter 表示为 dMIR virtual register，让 register allocation 和编译优化减少复杂函数中的内存访问。
- Host API 调用前后保存/恢复 gas，确保 host-side gas 更新和 VM-side counter 同步。

整数溢出检查则通过 hook functions 和 JIT inline specialization 完成。编译器识别 `checked_i32_add`、`checked_u64_mul` 等语义标记后，不生成普通函数调用，而是直接用 CPU arithmetic flags 与统一 trap path 生成紧凑检查。

### Solidity And Multi-Language Compatibility

DTVM 的 Solidity 支持走 Solidity -> Yul IR -> Wasm。Yul 层做类型推断/收窄、memory access mapping、function inlining、constant folding/propagation、dead code elimination 和 control-flow simplification，目标是在保留 EVM ABI 与 Solidity ecosystem 的同时绕过 EVM bytecode 的部分执行限制。

其他语言路线包括 C/C++ via Clang/LLVM, Rust via `wasm32-unknown-unknown`, Go via TinyGo, AssemblyScript, Java bytecode-to-Wasm 等。论文特别强调这些不是普通 Wasm language support，而是带有智能合约接口、storage model、events、ABI encoding/decoding 和 deterministic runtime 约束的开发栈。

### Security And TEE

论文把 AOT 与 JIT 的安全权衡显式化：AOT 可能需要所有节点信任相同编译器版本/配置，或只能优化 whitelist contracts；JIT 更通用，但动态代码生成扩大攻击面。

DTVM 的缓解路线包括 constrained control flow、JIT code 和 Wasm linear memory 隔离、短暂且受控的 code patching window、hardware-backed guard pages、dWasm deterministic foundation、JIT-integrated overflow/gas checks，以及更小的 TEE integration TCB。评估中 DTVM core codebase 为 69.5 KLoC，约为 Wasmtime 143.6 KLoC 的 48%。

### SmartCogent

SmartCogent 是 DTVM Stack 的 AI-assisted development/audit 工具层，不是 VM semantic core。它用 code generation agent、builder/deploy agent、audit plan/worker agents、RAG 和 dependency knowledge base 支持合约生成、编译、审计、修复和依赖抽取。论文报告安全审计 detection rate 81%、false positive rate 27%、code repair success 86%，并称 dependency extraction 通过 RAG 达到 95%+ accuracy。

这些结果应作为 source-local tool evaluation，不应提升为“AI 审计 foundation”节点；它主要说明智能合约执行栈正把开发/审计工具纳入 runtime ecosystem。

## Evaluation

| 维度 | 设置/结果 | 解释 |
| --- | --- | --- |
| Baselines | evmone v0.13.0, Revmc v0.1.0, Wasmtime v31.0.0, Wasmer v5.0.5 Singlepass/Cranelift/LLVM | 同时对比 EVM runtime 和 general-purpose Wasm runtime |
| Workloads | ERC20/ERC721/ERC1155/Counter/Integer Overflow; Fibonacci; PolyBench; WAPM | 覆盖语义丰富合约、计算密集合约和标准 Wasm benchmark |
| Language support | DTVM 支持 Solidity, C/C++, Java, Rust, Go, AssemblyScript；evmone/revmc 只支持 Solidity；Wasmtime/Wasmer 不提供智能合约语义适配的 Solidity support | DTVM 的主张是 runtime + ecosystem compatibility |
| Determinism | Wasmtime/Wasmer stack overflow depth 在 x86-64/ARM 不同；DTVM 返回一致 trap/backtrace | 支撑 dWasm/runtime constraint 的必要性 |
| Code size / TCB | DTVM object size 最低；core codebase 69.5 KLoC, CLI 31.8MB | 有利于 TEE 部署和最小化运行时复杂度 |
| Ethereum workloads | ERC20 transfer 约 6% latency reduction；ERC721/ERC1155 NFT transfer 分别 1.96x/2.01x；Fibonacci(25) 3.61x over evmone | 表明 EVM ABI compatible route 不是纯兼容层，也能带来性能收益 |
| JIT vs interpretation | Fibonacci(25) 58.54x; Counter 19.00x; ERC20 10.07x | 证明 lazy/JIT 对 compute-heavy 和部分合约路径有明显价值 |
| General Wasm workloads | Fibonacci(30) 11.73ms，比 Wasmtime/Wasmer variants 降低 11.8%-40.5%；Integer Overflow 5.5ms，比 Wasmtime 降低 20.6%，比 Wasmer variants 最高降低 64.6% | 支撑 DTVM 作为 Wasm runtime 的性能竞争力 |
| PolyBench | 对 Wasmtime 20/30 cases 更快，平均 speedup 1.20x；对 Wasmer variants 30/30 更快，平均 11.03x-12.14x | 简单计算 case 仍可能落后 Wasmtime，是后续优化空间 |
| First invocation latency | PolyBench 0.95-0.96ms vs Wasmtime 20.5-20.6ms；WAPM 约 23.36x-24.51x | trampoline hot-switch/lazy compilation 的核心实证 |

## Limitations And Boundary

- 这篇论文是 DTVM Stack 的系统论文和 benchmark 报告，不是 consensus protocol、mempool protocol 或 transaction ordering paper。
- Evaluation 在虚拟机环境和 micro/benchmark workloads 上完成；生产链环境、真实节点异构性、长期合约 workload、stateDB/IO 成本和安全审计覆盖仍需独立来源验证。
- SmartCogent 的 AI 工具指标是 source-local evaluation；不能据此建立通用 LLM smart-contract audit 知识节点。
- 结论提到 RISC-V、zk-SNARK-friendly VM、ZK-optimized VM variants 和 AI/ML-enhanced blockchain ecosystems，但正文没有给出 zkVM construction；因此只进入 review queue / future bridge candidate。

## What This Source Adds To Nahida

- 将 `smart-contract-execution` 从父方向里的 review candidate 提升为 active problem node。
- 把智能合约执行问题从“交易处理的一部分”拆开：DTVM 关注 VM/runtime determinism、ABI/language compatibility、JIT、安全边界和工具链，而不是交易排序/并发控制。
- 为 [[execution-and-transactions|Blockchain execution and transactions]] 补上智能合约 runtime 路线，连接 EVM、Wasm、JIT、gas、trap 和 TEE deployment。
- 为未来吸收 `Loom: A Deterministic Execution Framework Towards Nested Contract Transactions`、parallel EVM、Block-STM、zkVM/RISC-V VM 等 sources 提供上层入口。

## Source-Backed Takeaways

- 区块链智能合约 VM 的核心约束不是单纯“快”，而是快、确定、可计费、可 sandbox、可复现且与现有生态兼容。
- 通用 Wasm runtime 不能直接替代链上 runtime，因为 standard Wasm 在资源上限、trap、stack overflow、host functions 和 floating-point behavior 上留下实现差异。
- Lazy JIT 适合合约环境的关键原因是它降低部署/首次可调用成本，并把编译开销推迟到函数级 hot path。
- Gas metering、integer overflow、memory boundary checks 不能作为普通库逻辑外挂；在 JIT VM 中应进入 IR/native-code generation 和 runtime trap path。
- EVM ABI compatibility 可以与 Solidity-to-Wasm、多语言 SDK 和 deterministic Wasm runtime 共存，但需要大量工具链与语义适配。

## Absorption Targets

- [[smart-contract-execution|Smart contract execution]]
- [[execution-and-transactions|Blockchain execution and transactions]]
- [[transaction-processing|Blockchain transaction processing]]

## Review Notes

- The queue's staged primary path was too broad. This source should not be absorbed as a generic `transaction-processing` paper.
- Future bridge candidate: `smart-contract-execution -> zkVM / verifiable computation`, but only after a source gives a concrete ZK-optimized VM construction or evaluation.
- Future source candidate: DTVMStack GitHub repository can be analyzed separately as a repo source note if the user later provides or requests repository intake.
