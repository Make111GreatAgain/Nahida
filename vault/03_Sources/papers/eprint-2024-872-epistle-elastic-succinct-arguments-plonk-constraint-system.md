---
id: "eprint-2024-872-epistle-elastic-succinct-arguments-plonk-constraint-system"
title: "Epistle: Elastic Succinct Arguments for Plonk Constraint System"
type: "source"
source_type: "paper"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
safe_for_absorption: true
trust_tier: "primary"
source_identity:
  type: "pdf"
  key: "sha256:53510e799c45b46f70465f373d0347dfa64915fd3b8a05f8ef9785f45392d2d6"
source_refs:
  - "iacr:2024/872"
  - "sha256:53510e799c45b46f70465f373d0347dfa64915fd3b8a05f8ef9785f45392d2d6"
  - "filename:2024-872.pdf"
representative_source_refs:
  - "iacr:2024/872"
  - "sha256:53510e799c45b46f70465f373d0347dfa64915fd3b8a05f8ef9785f45392d2d6"
authors:
  - "Shuangjun Zhang"
  - "Dongliang Cai"
  - "Yuan Li"
  - "Haibin Kan"
  - "Liang Zhang"
year: "2024"
doi: ""
arxiv_id: ""
eprint_id: "2024/872"
canonical_url: ""
local_pdf: "~/Desktop/paper/2024-872.pdf"
pdf_sha256: "53510e799c45b46f70465f373d0347dfa64915fd3b8a05f8ef9785f45392d2d6"
extracted_text_path: "vault/02_Raw/pdf/extracted/2024-872-53510e799c45-pages.txt"
pages: 53
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "memory-efficient-snarks"
  - "elastic-snarks"
  - "plonk-constraint-system"
  - "hyperplonk"
  - "multivariate-piop"
  - "multilinear-kzg"
  - "sum-check-protocol"
  - "zk-snarks"
topic_ids:
  - "memory-efficient-snarks"
  - "elastic-snarks"
  - "plonkish-snarks"
  - "kzg-commitments"
  - "sum-check-protocol"
query_keys:
  - "Epistle"
  - "Elastic SNARKs for Plonk"
  - "elastic Plonk constraint system"
  - "HyperPlonk elastic prover"
  - "elastic multilinear KZG"
  - "streaming multivariate PIOP"
  - "space-efficient Plonk SNARK"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Abstract explicitly presents Epistle as an elastic SNARK for Plonk constraint system."
  - "Sections 2, 4, and 5 redesign HyperPlonk-style multivariate PIOP protocols in the streaming model."
  - "Section 6 provides an elastic multilinear KZG scheme used by the final argument."
  - "Section 7 reports Rust implementation and low-memory benchmark behavior."
parent_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-elastic-snarks"
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-kzg-commitments"
  - "nahida-knowledge-sum-check-protocol"
bridge_refs:
  - "nahida-bridge-memory-efficient-snarks-to-kzg-commitments"
  - "nahida-bridge-sum-check-protocol-to-memory-efficient-snarks"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks/elastic-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/polynomial-commitments/kzg-commitments.md"
  - "vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0085"
queue_rank: 85
run_ids:
  - "nahida-knowledge-20260623-epistle-elastic-snarks"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# Epistle: Elastic Succinct Arguments for Plonk Constraint System

## Paper Identity

| Field | Value |
| --- | --- |
| Title | Epistle: Elastic Succinct Arguments for Plonk Constraint System |
| Authors | Shuangjun Zhang; Dongliang Cai; Yuan Li; Haibin Kan; Liang Zhang |
| Date in PDF | June 1, 2024 |
| Local PDF | `~/Desktop/paper/2024-872.pdf` |
| Source key | `sha256:53510e799c45b46f70465f373d0347dfa64915fd3b8a05f8ef9785f45392d2d6` |
| ePrint identity | `iacr:2024/872`, inferred from filename and local queue identity; no web fetch was performed |
| Pages | 53 |
| Extracted text | `vault/02_Raw/pdf/extracted/2024-872-53510e799c45-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260623-epistle-elastic-snarks`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0085`
- Queue classification correction: 原队列的 `proof-system-foundations` 过宽；本论文主问题是 [[memory-efficient-snarks|Memory-efficient SNARKs]]，子层是 [[elastic-snarks|Elastic SNARKs]]，并作为 [[zk-snarks|zk-SNARKs]]、[[kzg-commitments|KZG commitments]]、[[sum-check-protocol|Sum-check protocol]] 的 source extension。

## 一句话贡献

Epistle 将 Gemini 的 elastic SNARK 思想从 R1CS 推到 Plonk constraint system: 它把 HyperPlonk 的 multivariate PIOP toolbox 改造成可流式证明的版本，并给出 elastic multilinear KZG，使 Plonkish/HyperPlonk 路线在 time-efficient 模式保持 `O_lambda(N)` prover work / `O(N)` memory，在 space-efficient 模式达到 `O_lambda(N log N)` prover work / `O(log N)` memory。

## 章节地图

| Section | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, 1 | 定义目标、对比 Plonk/HyperPlonk/Gemini，给出 Epistle 复杂度与实现结果。 | 支撑 [[elastic-snarks|Elastic SNARKs]] 的 Plonkish route。 |
| 2 | 技术概览: HyperPlonk gate/wiring relation、streaming model、SumCheck/ZeroCheck/Product/CyclicShift/Permutation、multilinear KZG、与 Gemini 对比。 | 提供可复用方法拆解。 |
| 3 | 预备知识: relation/language、多线性扩展、Schwartz-Zippel、streaming algorithm、polynomial IOP。 | 基础定义留在 source 内，避免污染知识节点。 |
| 4 | 把 SumCheck、ZeroCheck、cyclic shift left、product check、permutation check、prescribed permutation check 都改造成 elastic/streaming PIOP。 | 触发 [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] 桥更新。 |
| 5 | 构造 Plonk constraint system 的 elastic PIOP。 | 说明 Epistle 是 Plonkish low-memory SNARK，不是 R1CS-only Gemini 复述。 |
| 6 | Elastic multilinear KZG commitment/opening。 | 触发 [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]] 桥更新。 |
| 7 | Rust/arkworks/hyperplonk 实现、stream infrastructure、elastic prover 切换、batch multilinear KZG、benchmark。 | 作为实现证据，不升级为仓库分析。 |

## 解决的问题

Epistle 解决的是 Plonkish SNARK prover 的低内存弹性问题:

- Plonk/HyperPlonk 已能表达 Plonkish/custom-gate 约束，但常规 prover 需要持有 `O(N)` trace、selector、permutation 和 polynomial state。
- Gemini 已证明 R1CS 可以 elastic: 同一 proof/verifier interface 支持 time-efficient 与 space-efficient prover；但 Gemini 的 space-efficient prover 对 R1CS LinCheck 有 `O(N log^2 N)` 量级开销。
- 论文目标是在 Plonk constraint system 下保持同一 proof interface，同时给 prover 两种配置: 快速但线性内存，或低内存但准线性时间。
- 关键挑战是 HyperPlonk 的多线性 PIOP toolbox 和 multilinear KZG opening 也必须能在 streaming model 下工作，而不只是把输入向量包装成 iterator。

## 模型与假设

- Constraint system: `N=2^n` gates 的 Plonk constraint system，包含 addition、multiplication、input 和固定 degree custom gate。
- Trace/index streams: `l,r,o` witness streams，`s1,s2,s3` selector streams，public input stream，canonical injection `phi`，permutation `tau` 及其映射后的 `tau'` 都按 stream 访问。
- Streaming model: stream 支持 `init` 与 `next`，允许重放顺序扫描，不允许随机访问整个向量。
- Polynomial view: 各向量通过 multilinear extension 转成 Boolean hypercube 上的 polynomial oracles。
- Commitment layer: 使用 multilinear KZG，继承 trusted setup、pairing assumptions、SRS stream/order requirements。
- Scope limit: custom gate maximum degree 被当作常数；一般 lookup protocol 未被流式化；如果应用无法低内存生成 input streams，端到端内存结论不能直接外推。

## 核心方法

### 从 HyperPlonk 到 streaming Plonk relation

Epistle 复用 HyperPlonk 的两个 Plonkish relation:

- Gate identity: 通过 selector vectors `s1,s2,s3` 与 witness vectors `l,r,o` 表达 addition/multiplication/custom/input gates，再用 ZeroCheck 检查所有 gate relation 同时为零。
- Wiring identity: 把 `w=l||r||o||0` 作为所有 wire values，用 prescribed permutation check 证明 copy constraints，即 `w(v')=w(tau(v'))`。

区别在于 Epistle 要求这些向量以 streams 形式提供，并把 ZeroCheck、product/permutation 等子协议改写为低工作内存的 streaming prover。

### Elastic multivariate PIOP toolbox

论文逐个重写 HyperPlonk 需要的 PIOP 子协议:

| Toolbox protocol | 作用 | Streaming prover result | 为什么重要 |
| --- | --- | --- | --- |
| SumCheck | 将多项式求和声明逐轮降维到 point evaluation | `O(N log N)` arithmetic, `O(log N)` space, `O(log N)` passes | 基础递归扫描机制，来自 Gemini/streaming IP 思路 |
| ZeroCheck | 检查 polynomial 在 Boolean hypercube 上处处为零 | `O(N log N)` arithmetic, `O(log N)` space | gate identity 的核心 |
| Cyclic shift left check | 证明一个向量是另一个向量的循环左移 | `O(N log N)` arithmetic, `O(log N)` space | product check 的 streaming-friendly 改造需要它 |
| Product check | 证明两个向量的点乘积全局乘积为一 | `O(N log N)` arithmetic, `O(log N)` space | 避免 Quark/HyperPlonk 旧 route 在 streaming 下退化到 `O(N log^2 N)` |
| Permutation / prescribed permutation | 证明两个向量相差一个给定/隐藏 permutation | `O(N log N)` arithmetic, `O(log N)` space | wiring/copy constraint 的核心 |

关键设计是 product check: 论文不沿用会产生 `O(log^2 N)` passes 的 Quark route，而是构造 prefix-product 向量 `g` 和 cyclic-shift 向量 `g_sigma`，再用 ZeroCheck 验证 `f * g = g_sigma`。因为 `g` 与 `g_sigma` 可以从原输入 stream 顺序生成，所以总开销保持 `O(N log N)`。

### Plonk constraint system PIOP

在 Section 5，论文把上述 toolbox 组合成 Plonk relation:

- Offline phase 构造一个 7-variable polynomial `F(X1,...,X7)`，统一表达 selector、left/right wire、output wire 和 padded public input 的 gate relation。
- Online phase 先让 prover 给出 `l,r,o` 的 polynomial oracles，再调用 ZeroCheck 检查 gate identity。
- Wiring identity 通过 prescribed permutation check 处理 `w=l||r||o||0`。
- Theorem 5.1 给出 holographic PIOP: round/message `O(log N)`，query `O(1)`，verifier time `O(|x|+log N)`；random-access prover `O(N)`/`O(N)`，streaming prover `O(N log N)`/`O(log N)`。

### Elastic multilinear KZG

Epistle 使用 multilinear KZG 编译 PIOP:

- Commitment: 对 vector `f` 的 multilinear extension `f_hat` 承诺为 `g^{f_hat(tau)}`；streaming commit 只需顺序扫描 SRS/key stream 与 `f` stream。
- Opening: 根据 multilinear decomposition，把 `f_hat(z)-mu` 分解为若干 `(X_i-z_i) * f_i` 项；streaming open 用 stack 合并相邻元素，生成所有 `f_i` 的 KZG witnesses。
- Theorem 6.1: commitment size `O(1)`，proof size `O(log N)`，check time `O_lambda(log N)` group operations；streaming commit/open 都可用 `O(log N)` 或更低工作空间。
- Implementation 还加入 HyperPlonk-style batch opening，降低多 polynomial/multi-point opening 的开销。

## 主要结果

| Result | Time-efficient configuration | Space-efficient configuration | Verifier / proof | Evidence |
| --- | --- | --- | --- | --- |
| Epistle elastic SNARK for Plonk constraint system | `O_lambda(N)` cryptographic operations, `O(N)` memory | `O_lambda(N log N)` cryptographic operations, `O(log N)` memory | verifier `O_lambda(|x|+log N)`, proof `O(log N)` | Theorem 1.1 / Table 1 |
| Plonk constraint system holographic PIOP | `O(N)` arithmetic, `O(N)` space | `O(N log N)` arithmetic, `O(log N)` space, `O(log N)` passes | verifier `O(|x|+log N)` | Theorem 5.1 |
| Elastic multilinear KZG | random-access commit/open optimized for memory-rich prover | streaming commit one pass with `O(1)` space; streaming open one pass with `O(log N)` space | commitment `O(1)`, proof `O(log N)` | Theorem 6.1 |

## 实现与评估

- Implementation: Rust, using `arkworks` and `hyperplonk`; implements Section 4 elastic PIOP protocols and Section 6 elastic multilinear KZG.
- Stream infrastructure: restartable wrapper over `iter::Iterator`; elements use Rust borrow abstraction to reduce copying.
- Elastic prover switch: when a SumCheck round fits under the memory threshold, prover can switch from space-efficient state to time-efficient proving for later rounds; final proof remains identical.
- Hardware in Section 7: 2023 Apple MacBook Pro, M3 Max, 14 cores, 36GB RAM, BLS12-381, vanilla Plonk gate mock circuit, instance sizes `2^18` to `2^26`.
- Memory result: elastic prover remains around 1.5GB for large instances; time-efficient prover OOMs at instance size `2^25` under 36GB RAM.
- Proving time: both modes grow nearly linearly in the reported range; elastic mode is about 2-8x slower than time-efficient mode for `2^18` to `2^24`.
- Proof size/verification: proof size about 14-19KB and verification around 10-15ms for tested sizes.

## 与 Gemini 的关系

Epistle is best recorded as the second source-backed branch of [[elastic-snarks|Elastic SNARKs]]:

- Gemini: R1CS route, streaming R1CS/elastic PIOP/elastic KZG, space-efficient prover around `O_lambda(M log^2 M)` with `O(log M)` memory.
- Epistle: Plonk/HyperPlonk route, streaming multivariate PIOP toolbox + elastic multilinear KZG, space-efficient prover `O_lambda(N log N)` with `O(log N)` memory.
- The durable concept is not `Gemini` or `Epistle`; it is elastic prover configurations under a stable proof/verifier interface.
- The durable split is now constraint-system family: R1CS elastic route vs Plonkish/HyperPlonk elastic route.

## 限制与边界

- Lookup gap: 论文没有在一般 streaming model 下构造 Plonkish lookup protocol；构造 `w=sort(f,g)` with limited space 被明确留作 future work。
- Constant-degree assumption: custom gate maximum degree is treated as constant.
- KZG trust boundary: multilinear KZG inherits trusted setup, pairings and SRS distribution assumptions.
- Streaming-input assumption: prover memory result assumes trace/index/witness/commitment-key streams can be generated/replayed without hidden large memory state.
- Evaluation boundary: benchmark uses vanilla Plonk gate mock circuits and one hardware/software stack; no repository-state audit or production deployment check was performed.
- Foundation boundary: Epistle does not replace PLONK, HyperPlonk, KZG or zk-SNARK foundation notes; it is a source extension for low-memory/elastic proving.

## 吸收交接

- Create/refresh [[elastic-snarks|Elastic SNARKs]] as child of [[memory-efficient-snarks|Memory-efficient SNARKs]] because Gemini + Epistle now give two source-backed elastic routes.
- Update [[memory-efficient-snarks|Memory-efficient SNARKs]]: add Plonkish/HyperPlonk elastic route and compare R1CS vs Plonkish low-memory tradeoff.
- Update [[zk-snarks|zk-SNARKs]]: record Epistle as prover-resource source extension, not foundation upgrade.
- Update [[kzg-commitments|KZG commitments]]: add elastic multilinear KZG source extension, distinct from Gemini's univariate KZG realization.
- Update [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] and [[memory-efficient-snarks-to-kzg-commitments|Memory-efficient SNARKs -> KZG commitments]].
- Do not create an `Epistle` knowledge node. Epistle remains a source note and representative evidence.

## 需要后续补的基础来源

| Gap | Why it matters | Suggested action |
| --- | --- | --- |
| PLONK / HyperPlonk foundation notes | Epistle relies on Plonkish and HyperPlonk machinery, but this source should not define them for the whole vault. | import foundation sources |
| Lookup under streaming Plonkish prover | Epistle leaves this open; future sources may alter elastic Plonkish boundaries. | research search |
| Non-KZG elastic PCS comparisons | Epistle and Gemini are KZG-heavy, so transparent/IPA/FRI/DARK routes need separate evidence. | research search / paper intake |
