---
id: "doi-10-1109-tc-2023-3235975-split-hash-based-memory-optimization-zksnark"
title: "Split: A Hash-Based Memory Optimization Method for Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (zk-SNARK)"
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
  key: "doi:10.1109/TC.2023.3235975"
source_refs:
  - "doi:10.1109/TC.2023.3235975"
  - "sha256:679d6716d278cf348c932c4d42cc0f69956d44a59ad2229e335e05f4f247b15e"
  - "filename:SPLITA_1.pdf"
representative_source_refs:
  - "doi:10.1109/TC.2023.3235975"
authors:
  - "Huayi Qi"
  - "Ye Cheng"
  - "Minghui Xu"
  - "Dongxiao Yu"
  - "Haipeng Wang"
  - "Weifeng Lyu"
year: "2023"
doi: "10.1109/TC.2023.3235975"
arxiv_id: ""
canonical_url: "https://doi.org/10.1109/TC.2023.3235975"
venue: "IEEE Transactions on Computers, 72(7)"
local_pdf: "~/Desktop/paper/SPLITA_1.pdf"
pdf_sha256: "679d6716d278cf348c932c4d42cc0f69956d44a59ad2229e335e05f4f247b15e"
extracted_text_path: "vault/02_Raw/pdf/extracted/split-a-hash-based-memory-optimization-method-for-zero-knowledge-succinct-non-interactive-argument-of-knowledge-zk-snark-679d6716d278-pages.txt"
pages: 14
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
  - "zero-knowledge-proofs/proof-systems/proof-system-benchmarking"
domains:
  - "zero-knowledge-proofs"
topics:
  - "memory-efficient-snarks"
  - "front-end-circuit-partitioning"
  - "r1cs"
  - "hash-bound-subcircuits"
  - "zk-snarks"
  - "proof-system-benchmarking"
topic_ids:
  - "memory-efficient-snarks"
  - "front-end-circuit-partitioning"
  - "r1cs"
  - "hash-bound-subcircuits"
query_keys:
  - "Split hash-based memory optimization"
  - "n-Split"
  - "Good Split"
  - "R1CS circuit partitioning"
  - "hash-bound zkSNARK subcircuits"
  - "single-machine zkSNARK memory optimization"
aliases:
  - "Split"
  - "n-Split"
  - "Good Split"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Abstract and Section I frame the paper as reducing zk-SNARK prover memory for resource-constrained single-machine provers."
  - "Section III defines Split, Good Split and n-Split as circuit partitioning mechanisms."
  - "Section IV analyzes memory/time overhead and security; Section V evaluates proof memory/time."
  - "Queue path proof-system-foundations is too broad; the precise reusable problem is memory-efficient SNARK proving."
parent_knowledge_refs:
  - "nahida-knowledge-memory-efficient-snarks"
  - "nahida-knowledge-zk-snarks"
  - "nahida-knowledge-distributed-proof-generation"
  - "nahida-knowledge-proof-system-benchmarking"
bridge_refs:
  - "nahida-bridge-memory-efficient-snarks-to-distributed-proof-generation"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/proof-system-benchmarking.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0053"
queue_rank: 53
run_ids:
  - "nahida-knowledge-20260622-split-hash-memory-optimization"
created: "2026-06-22"
updated: "2026-06-22"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# Split: A Hash-Based Memory Optimization Method for Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (zk-SNARK)

## Paper Identity

| Field | Value |
| --- | --- |
| Title | Split: A Hash-Based Memory Optimization Method for Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (zk-SNARK) |
| Authors | Huayi Qi; Ye Cheng; Minghui Xu; Dongxiao Yu; Haipeng Wang; Weifeng Lyu |
| Venue | IEEE Transactions on Computers, Vol. 72, No. 7, pp. 1857-1870 |
| Year | 2023 |
| DOI | 10.1109/TC.2023.3235975 |
| Canonical URL | https://doi.org/10.1109/TC.2023.3235975 |
| Local PDF | `~/Desktop/paper/SPLITA_1.pdf` |
| Source key | `sha256:679d6716d278cf348c932c4d42cc0f69956d44a59ad2229e335e05f4f247b15e` |
| Pages | 14 |
| Extracted text | `vault/02_Raw/pdf/extracted/split-a-hash-based-memory-optimization-method-for-zero-knowledge-succinct-non-interactive-argument-of-knowledge-zk-snark-679d6716d278-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Reading depth: `deep_read`
- Safe for absorption: true
- PDF extractor: `pypdf`; Table II/III numeric values were checked from a rendered page image because text extraction did not preserve table cells reliably.
- 已覆盖章节/页码: p1-p14, including Abstract, Introduction, Related Work and Preliminaries, Split Design, Analysis, Evaluation, Conclusion and References.
- 未覆盖章节/页码: none.
- Extraction gaps: figures are described from captions and surrounding text; table values were manually checked from rendered p11.
- Absorption run: `nahida-knowledge-20260622-split-hash-memory-optimization`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0053`
- Classification correction: queue classified the paper as `proof-system-foundations`; deep reading shows the primary path is [[memory-efficient-snarks|Memory-efficient SNARKs]], with [[zk-snarks|zk-SNARKs]] as foundation context and [[distributed-proof-generation|Distributed proof generation]] as a contrast route.

## 一句话贡献

Split 提出一种面向 zk-SNARK 前端/R1CS 电路的 hash-bound circuit partitioning 方法，把大电路切成可顺序证明的子电路，并用 hash digest 绑定跨切分中间变量，从而让资源受限的单机 prover 在保留底层 zk-SNARK 安全性质的前提下降低 peak memory。

## 章节地图

| Section / pages | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, I / p1-p2 | 问题、动机和贡献 | R1CS 必须保留中间变量；个人电脑/手机级 prover 内存不足；Split/n-Split 用 hash circuit 绑定分片 | high |
| II-A / p2 | Related work | QAP/IOP zk-SNARKs；SafetyNets/ZEN/DIZK 等相邻方案 | medium |
| II-B / p3-p5 | Preliminaries | zk-SNARK Setup/Prove/Verify，R1CS/circuit，front-end/back-end，loop unrolling，QAP | high |
| III-A / p5-p6 | Split and Good Split | 定义 Split、SetupS/ProveS/VerifyS；把 split search 约化成 DAG cut；定义 Good Split | high |
| III-B / p6-p7 | n-Split | 多个子电路、连续 hash-bound intermediates、SetupMS/ProveMS/VerifyMS | high |
| III-C-D / p7-p8 | Why memory is reduced + examples | obsolete variables 不再跨全程保留；Fibonacci/LIS 作为 Good Split 示例 | high |
| IV-A / p8-p10 | Security analysis | 基于底层 zk-SNARK 完备性/可靠性/零知识和 hash preimage/second-preimage security 证明性质保持 | high |
| IV-B / p10 | Performance analysis | hash circuit overhead；memory becomes max subcircuit size；verify/proof count grow with split number | high |
| V / p10-p12 | Evaluation | xJsnark/libsnark/QAP-based setup；loop circuit；Table II/III memory/time results；QAP padding explanation | high |
| VI / p12 | Conclusion and future work | MiMC/Poseidon 可降低 hash overhead；Good Split finding remains hard | high |
| References / p12-p14 | Context | DIZK, xJsnark, Groth16, Pinocchio, Aurora, MiMC, Poseidon | medium |

## 核心精读笔记

### 背景、动机与问题边界

论文从 zk-SNARK 的 front-end/R1CS 视角切入。普通程序中的临时变量可以被编译器或 garbage collector 回收，但 R1CS solution vector 需要在 Prove 阶段为所有变量提供 witness，因此循环、条件和随机访问被展开后会产生大量中间变量，并在证明过程中持续占用内存。作者给出的简单例子是循环更新 `x <- a*x + b`: 10,000 次迭代需要 1.173GB memory，300,000 次迭代需要 32.513GB memory。

论文明确把目标限定为单机、资源受限 prover 的 memory reduction: 它不是为了降低 verifier 成本、不是 proof aggregation、也不是把任务分发到 cluster。作者把 Wu et al. 的 DIZK 作为相邻工作: DIZK 用多机 cluster 扩展可证明电路规模，但对没有 cluster 的普通个人电脑或笔记本不适用。本文的问题是: zk-SNARK 是否能在单机上支持更大电路，代价如何同时体现在 CPU time 和 memory 上。

### 模型、假设与定义

论文使用通用 zk-SNARK 接口:

- `Setup(1^K, F) -> (pk, vk)`: 针对电路生成证明/验证 key。
- `Prove(F, x_pub, x_priv, y_pub, y_priv, pk) -> pi`: prover 给出 proof。
- `Verify(x_pub, y_pub, pi, vk) -> {0,1}`: verifier 检查 proof。

电路使用 R1CS / arithmetic circuit 作为 front-end/back-end 之间的接口。电路 `G=(V,E)` 是有向无环图，变量和约束分别为 node 类型。论文把 `|F|` 定义为变量数 `N`，并用它代表 circuit size / memory 主要驱动因素。QAP-based zk-SNARKs 把 R1CS 转成 QAP；QAP degree 影响 Setup/Prove 的 time 和 memory，libsnark 的 FFT padding 会让 split 后的 QAP degree 与 R1CS constraint count 不完全线性对应。

### Split 机制

Split 把原电路 `F` 切成两个 split circuits `F1, F2`:

- `F1(x_pub, x_priv) -> (h, m)`: 计算跨切分的中间变量集合 `m`，并输出 public hash `h <- H(m)`。
- `F2(x_pub, m) -> (h', y_pub, y_priv)`: 以 `m` 作为第二段输入，重新计算 `h' <- H(m)`，并完成原始输出。
- verifier 检查两段 proofs，并要求公共 hash 一致；`pi_S = (pi_1, pi_2)`。

这个 hash 是必要的，因为 prover 可以任意选择第二段输入。如果没有 hash binding，恶意 prover 可能把第一段实际输出的 `m` 换成另一个 `m'` 交给 `F2`，从而破坏原始电路语义。hash digest 将跨段变量公开绑定，而 `m` 本身仍是 secret。

Split 的核心不是任意切割，而是寻找 Good Split:

- `|m| << |F|`: 跨切分变量很少，避免 hash circuit 过大。
- `max{|F1|, |F2|}` relatively small: 最大子电路明显小于原电路，才会降低 peak memory。

论文把寻找 split 的问题约化成 DAG cut: 在从变量图中删除 public inputs 后，选择 source/sink cut `(S,T)`，目标大致是最小化 `max{|S|, |T|} + H * capacity(S,T)`，其中 `capacity` 是跨 cut 的边数，`H` 表示 hash overhead。作者也指出该图问题难求，因此用 Good Split 作为可用设计准则。

### n-Split 机制

n-Split 把电路切成 `n` 段:

- 第一段输出 `h1, m1`；
- 中间段同时验证上一个 hash `h'_{i-1}` 并产生下一个 `hi, mi`；
- 最后一段验证 `h'_{n-1}` 并输出最终 `y_pub, y_priv`；
- proof 是 `pi_MS = (pi_i)`，verify 对每段依次验证。

n-Split 可以进一步降低 peak memory，因为内存约为 `max{|Fi|}`，但代价是更多 hash circuits、更多 proofs、更多 verification steps 和更多 setup/proving material。论文强调 split number 需要在 memory 与 computational overhead 之间权衡。

### 为什么能降低内存

Split 让第一段中已经 obsolete 的变量不用在第二段证明时继续保留。对循环结构尤其有效，因为 loop unrolling 会产生大量只在某一迭代附近有用的变量；如果在迭代边界切分，只需要保留少数跨段 state variables，并用 hash digest 绑定它们。

论文的两个示例:

- Fibonacci series: 在 loop 中间切分，只需保留 `m` 中少量状态变量；`|m|=4 << |F|≈4n`，可近似减半 memory。
- Longest Increasing Subsequence: 表面上可能依赖很多历史变量，但 front-end unrolling 会为每次 update 产生 obsolete variables；可在迭代边界找到 Good Splits。

### 安全性分析

Theorem IV.1 说明: 若底层 zk-SNARK 满足 completeness、soundness、zero-knowledge，hash function 满足 second preimage security 和 preimage security，则 Split 构造也满足这三种性质。

关键 Lemma IV.1 是原电路满足性与两个 split circuits 满足性加 `h=h'` 的等价关系:

- second-preimage security 阻止 prover 找到不同 `m' != m` 但 hash 相同；
- 因而 `F1` 输出和 `F2` 输入被绑定；
- completeness 来自两段底层 proofs 的 completeness；
- soundness 通过两段 soundness 和 hash binding 推出；
- zero-knowledge 依赖底层 proof 的 zero-knowledge 以及 hash preimage security，使 verifier 不能从 `h` 学到 secret intermediate `m`。

注意边界: 论文证明的是在底层 zk-SNARK 与 hash assumptions 成立时的 Split security；它并未把 SHA256/MiMC/Poseidon 的具体实现安全或 circuit correctness 重新证明成通用结论。

### 性能分析

论文把 hash circuit overhead 写成:

- Split overhead: `2 * ceil(m_bits / H_bits) * H_overhead`
- n-Split overhead: `sum_{i=1}^{n-1} 2 * ceil(m_bits,i / H_bits) * H_overhead`

以 SHA256 为例，论文报告 xJsnark 的 SHA256 circuit per input chunk 会带来 34,324 constraints，因此 `|m|` 必须小。memory usage 则从原始 `|F|` 变成 `max{|F1|, |F2|}` 或 `max{|Fi|}`。对 QAP-based zk-SNARKs，Setup/Prove time 和 memory 与 QAP degree 有关；split 后 R1CS constraints 总数增加，但 libsnark FFT padding 可能让某些 split cases 的 QAP degree 反而不增加，解释了实验中少数 proof time 略降的现象。

## 实验与结果

### 实验设置

- Hardware: dual Intel Xeon E5-2620 v4 @ 2.10GHz, 128GB RAM, Ubuntu 20.04.2 LTS；实验只用单核运行 zk-SNARK toolchain。
- Backend: QAP-based zk-SNARK system from [14]，xJsnark front-end，libsnark QAP reduction/proving。
- Workload: loop circuit `x <- a*x + b`，不同 iteration counts。
- Hash circuit: SHA256。
- Metrics: R1CS constraints, QAP degree, Prove time, Prove memory, Verify time。

### Table II: 2-Split

Table II 显示六个 circuit sizes。随着 circuit 变大，2-Split 的 memory reduction 越接近 50%。

| Case | Original constraints | Original prove time | Original memory | Split constraints | Split prove time | Split memory |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Circuit 1 | 383,381 | 10.0336s | 1,173MB | 501,306 | 12.7547s | 851MB |
| Circuit 2 | 1,150,037 | 30.8620s | 3,486MB | 1,267,930 | 33.7338s | 2,221MB |
| Circuit 3 | 1,916,725 | 50.6133s | 5,742MB | 2,034,618 | 50.5976s | 3,258MB |
| Circuit 4 | 3,833,381 | 104.3493s | 10,763MB | 3,951,306 | 101.2589s | 5,901MB |
| Circuit 5 | 7,666,725 | 212.2286s | 21,413MB | 7,784,618 | 208.8059s | 10,918MB |
| Circuit 6 | 11,500,037 | 341.2828s | 32,513MB | 11,617,930 | 336.5552s | 16,421MB |

Verify time after Split roughly doubles, but仍在毫秒级；论文认为可接受。

### Table III: n-Split

Experiment II 使用 Experiment I 的 Circuit 4，并切成 2、3、4、5 components。

| n-Split | Constraints | QAP degree | Prove time | Memory |
| --- | ---: | ---: | ---: | ---: |
| Original | 3,833,381 | 4,194,304 | 104.4845s | 10,763MB |
| 2 | 3,951,306 | 4,194,304 | 101.6369s | 5,901MB |
| 3 | 4,069,199 | 4,718,592 | 121.1280s | 4,016MB |
| 4 | 4,187,092 | 4,259,840 | 108.9389s | 3,494MB |
| 5 | 4,305,049 | 5,242,880 | 126.2172s | 2,919MB |

论文正文总结: 5-Split 将 memory usage 优化到原来的 27%，同时对该示例电路只带来约 20% additional CPU time。随着 split components 增加，memory 继续下降但边际收益变慢，computational overhead 继续增加；verify time 近似随 split number 线性增加。

### QAP padding caveat

libsnark 使用 step radix-2 FFT，QAP degree 会被 padding 到特定形状。因为 padding 非线性，split 后虽然 R1CS constraints 增加，但 `M_QAP^(1)+M_QAP^(2)` 不一定大于原始 `M_QAP`，所以一些 split cases 中 Prove time 可能略低。这个现象不应被泛化为 Split 必然加速；可靠结论是降低 peak memory，time 需要看 split、hash overhead 和 backend padding。

## 局限性

- Good Split 并不保证存在。没有小 cross-cut state 的电路可能不适合 Split。
- finding Good Split 本身是 hard graph partitioning problem；论文给出定义和准则，但没有通用近似算法。
- hash circuit overhead 可能很大，SHA256 在 SNARK 中并不便宜；论文建议未来使用 MiMC/Poseidon 等 SNARK-friendly hash。
- proof/output 变成多个 component proofs，verification 和 setup/proving material 随 split number 增加。
- 实验是 proof-of-concept loop workload，不覆盖真实 zkRollup、zkML 或 arbitrary application circuits。
- 论文优化的是 front-end/R1CS/circuit partitioning，不等于 backend FFT/MSM acceleration，也不等于 distributed proving。

## 层级候选分类

- L1 Domain candidate: `zero-knowledge-proofs`
- L2 Direction candidate: `proof-systems`
- L3 Topic/content cluster candidates: `memory-efficient-snarks`, `proof-system-benchmarking`
- Primary ontology path: `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`
- Secondary paths: `zero-knowledge-proofs/proof-systems/zk-snarks`; `zero-knowledge-proofs/proof-systems/distributed-proof-generation`; `zero-knowledge-proofs/proof-systems/proof-system-benchmarking`
- 备选归属: `distributed-proof-generation` 只是论文对比路线；`proof-system-foundations` 过宽。
- 置信度: high
- 分类理由: title/abstract/Section I-V 均围绕 prover memory reduction，核心机制为 circuit partitioning + hash binding。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | zero-knowledge-proofs | Title, abstract, zk-SNARK/R1CS/QAP context | high | existing domain |
| Research background | zk-SNARK prover memory bottleneck from R1CS variable retention and loop unrolling | §I, §II-B5 | high | background in [[memory-efficient-snarks|Memory-efficient SNARKs]] |
| Research problem | single-machine zk-SNARK memory optimization | §I asks whether larger circuits can be proved on a single machine | high | problem source extension |
| Foundation concepts | zk-SNARKs, R1CS, QAP, hash functions | §II-B, §IV | high | existing/thin knowledge refs; no new foundation node |
| Method family | front-end circuit partitioning with hash-bound intermediate variables | §III | high | source extension route under memory-efficient SNARKs |
| Application/evaluation context | loop-based R1CS circuits in xJsnark/libsnark; resource-constrained provers | §V | high | proof-system benchmarking source evidence |
| Source instance | Split / n-Split / Good Split | §III-V | high | source instance, not foundation node |

## 检索优化判断

- Future queries helped: “SNARK prover 内存太大怎么优化”“Split 和 DIZK/Gemini/Sparrow 区别”“R1CS 电路能不能像程序一样释放临时变量”“Good Split 是什么”。
- Source notes avoided: future agent can start from [[memory-efficient-snarks|Memory-efficient SNARKs]] to compare Split, Gemini, Sparrow and Mangrove instead of scanning every low-memory paper.
- Source-only details: exact Fibonacci/LIS pseudocode, Table II/III raw numbers, proof equations and QAP padding explanation remain here.
- No new knowledge node: `Split`, `Good Split` and `n-Split` are paper-specific mechanism labels unless later sources reuse them.
- Bridge needed: [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]] because the paper explicitly contrasts single-machine memory optimization with DIZK-style cluster expansion.

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 |
| --- | --- | --- | --- | --- |
| zk-SNARK/R1CS 的 memory bottleneck 来自变量全程保留与 loop unrolling | author claim + explanation | §I, §II-B5 / p1-p5 | loop update example and R1CS/front-end discussion | high |
| Split 用 hash-bound intermediate variables 防止第二段输入被替换 | mechanism | §III-A-C / p5-p7 | `h <- H(m)`, F2 rechecks `h' <- H(m)` | high |
| Good Split 需要 `|m| << |F|` 且最大子电路小 | definition | Definition III.2 / p6 | paper definition | high |
| Split 保持 completeness/soundness/zero-knowledge | theorem | Theorem IV.1 / p8-p10 | depends on underlying zk-SNARK and hash assumptions | high |
| 2-Split 对大电路 memory 接近减半 | experiment | Table II / p11 | Circuit 6: 32,513MB -> 16,421MB | high |
| 5-Split 将示例 circuit memory 降至 27%，约 20% additional CPU time | experiment | §V-B2 / p11-p12 | Table III + author conclusion | high |
| proof time 不一定单调增加，因为 QAP padding 影响 degree | caveat | §V-C / p12 | libsnark step radix-2 FFT padding explanation | high |

## Knowledge 综合交接

- 待更新 Knowledge node: [[memory-efficient-snarks|Memory-efficient SNARKs]]
- 轻量更新 Knowledge nodes: [[zk-snarks|zk-SNARKs]], [[proof-systems|Proof systems]], [[distributed-proof-generation|Distributed proof generation]], [[proof-system-benchmarking|Proof-system benchmarking]]
- 应创建/更新 Bridge: [[memory-efficient-snarks-to-distributed-proof-generation|Memory-efficient SNARKs -> Distributed proof generation]]
- Foundation gaps: R1CS/arithmetic-circuit front-end foundation and SNARK-friendly hash functions are still thin; queue rather than invent.
- 不提升为独立节点: `Split`, `Good Split`, `n-Split`, Fibonacci/LIS examples, exact benchmark cases。

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| zk-SNARKs | foundation_knowledge | 作为基础 proof-system node 被引用 | 让本文定义整个 zk-SNARK 领域 | §II-B1 |
| R1CS / arithmetic circuit | foundation_gap_or_section | 在 proof-system/arithmetization foundation 中补齐，本文提供 front-end memory evidence | 把 R1CS 当成本文独有概念 | §II-B3 |
| Split / n-Split / Good Split | representative_instance_or_source_extension | 作为 memory-efficient SNARKs 的 source extension route | 单独创建 foundation node | §III |
| SNARK-friendly hash functions | foundation_gap | MiMC/Poseidon 可作为未来 foundation/search item | 直接把 SHA256 overhead 推广为所有 hash route | §VI |

## 处理日志

| Date | Run ID | Action | Notes |
| --- | --- | --- | --- |
| 2026-06-22 | nahida-knowledge-20260622-split-hash-memory-optimization | Deep-read SPLITA and prepared Source + Knowledge + Bridge handoff. | Corrected queue path from proof-system-foundations to memory-efficient-snarks. |
