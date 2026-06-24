---
id: "doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits"
title: "Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_local"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p15 full extracted text"
  - "Sections 1-5, tables, and references"
canonical_url: "https://doi.org/10.1145/3658644.3690318"
doi: "10.1145/3658644.3690318"
arxiv_id: ""
venue: "ACM CCS 2024"
year: "2024"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "memory-efficient-snarks"
  - "space-efficient-sumcheck"
  - "data-parallel-circuits"
  - "verifiable-ml-training"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "memory-efficient-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
secondary_ontology_paths:
  - "verifiable-computation/interactive-proofs/sum-check-protocol"
  - "zero-knowledge-proofs/zkml/verifiable-training"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "proof-systems"
    - "interactive-proofs"
    - "zkml"
  topics:
    - "memory-efficient-snarks"
    - "sum-check-protocol"
    - "verifiable-ml-training"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "memory-efficient-snarks"
  - "space-efficient-sumcheck"
  - "sum-check-protocol"
  - "gkr"
  - "data-parallel-circuits"
  - "verifiable-ml-training"
aliases:
  - "Sparrow"
  - "space-efficient zkSNARKs"
  - "zero-knowledge forest training"
  - "zkFTP"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  subdomain:
    - "proof-systems"
    - "interactive-proofs"
    - "zkml"
  problem:
    - "SNARK prover memory overhead"
    - "space-efficient sumcheck"
    - "zero-knowledge ML training integrity"
  method_family:
    - "space-efficient sumcheck"
    - "space-efficient GKR"
    - "streaming oracles"
    - "sublinear public-parameter polynomial commitments"
  system_layer:
    - "proof system"
    - "ML training certification"
    - "decision-tree prediction proof"
  evaluation_context:
    - "data-parallel circuits"
    - "multiplication trees"
    - "batch SHA256"
    - "decision-tree and random-forest training"
  bridge:
    - "sum-check-protocol-to-memory-efficient-snarks"
    - "memory-efficient-snarks-to-verifiable-ml-training"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
source_refs:
  - "doi:10.1145/3658644.3690318"
  - "sha256:6c790245d67b7f28aac9cfde6b7d535a547e0c9adb57516f8cd039fbf28584de"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "interactive-proofs"
  - "zkml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Title and abstract introduce Sparrow as a space-efficient zkSNARK for data-parallel circuits."
  - "Section 3 gives the space-efficient sumcheck, GKR variant, and zkSNARK construction."
  - "Section 4 applies Sparrow to zero-knowledge forest training and prediction."
  - "Queue primary path sum-check-and-gkr captures an important dependency, not the paper's main problem layer."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0031"
local_pdf: "~/Desktop/paper/3658644.3690318.pdf"
pdf_sha256: "6c790245d67b7f28aac9cfde6b7d535a547e0c9adb57516f8cd039fbf28584de"
extracted_text_path: "vault/02_Raw/pdf/extracted/sparrow-space-efficient-zksnark-for-data-parallel-circuits-and-applications-to-zero-knowledge-decision-trees-6c790245d67b-pages.txt"
---

# Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees

## 论文身份

- 标题: Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees
- 作者: Christodoulos Pappas, Dimitrios Papadopoulos
- 机构: Hong Kong University of Science and Technology
- 会议/期刊: CCS '24, ACM SIGSAC Conference on Computer and Communications Security
- 年份: 2024
- DOI: 10.1145/3658644.3690318
- arXiv: unknown in local PDF
- 链接: https://doi.org/10.1145/3658644.3690318
- 本地 PDF: `~/Desktop/paper/3658644.3690318.pdf`
- 代码/数据: PDF references `https://github.com/anonymousg3bz6q2/Sparrow`; full version at `https://github.com/ChristodoulosPappas/Sparrow-Full-Version`; 未联网验证。
- License: Creative Commons Attribution International 4.0 License

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 15
- 已覆盖章节/页码: p1-p15, including introduction, preliminaries, Sparrow construction, zkFTP construction, evaluation, tables and references.
- 未覆盖章节/页码: none in the local CCS PDF. The paper points to a full version for formal proofs and pseudocode.
- Extraction gaps: figures/tables are text-extracted imperfectly but enough for all reported values.
- 精读说明: 队列路径 `verifiable-computation/interactive-proofs/sum-check-and-gkr` 只覆盖方法依赖。深读后主路径纠正为 `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`，secondary paths 为 sum-check/GKR 与 zkML training。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和结果 | Space-efficient zkSNARK for data-parallel circuits; applications to zero-knowledge decision trees | high | 主分类依据 |
| §1 / p1-p4 | 动机和贡献 | prover memory bottleneck, Sparrow, space-efficient sumcheck, zkFTP, evaluation | high | 贡献和边界 |
| §2 / p4-p5 | Preliminaries | sumcheck, GKR, polynomial commitments, argument systems, tree/forest training | medium | 方法依赖 |
| §3.1 / p5-p7 | Space-efficient sumcheck | high-degree variable replacement, two-phase reduction, O(sqrt N) buffer | high | reusable method |
| §3.2 / p7-p8 | Sparrow zkSNARK | space-efficient GKR, streaming oracles, depth reduction, Kopis PC, Fiat-Shamir | high | proof-system construction |
| §4 / p8-p11 | zkFTP | forest training/prediction proofs, certification algorithm, circuits, memory checks | high | zkML application |
| §5 / p11-p14 | Evaluation | C++ implementation, hardware, Sparrow/Gemini/GKR+Kopis comparison, zkFTP benchmarks | high | empirical evidence |
| References / p14-p15 | Context | Gemini, Ligetron, GKR, Libra, zkML, decision-tree proof works | medium | novelty boundary |

## 核心精读笔记

> 这篇论文的主线是: 把 zkSNARK prover 的内存开销降到接近原生计算空间，针对 layered data-parallel arithmetic circuits 构造 Sparrow，并用它让 decision tree / random forest training 的 ZK proof 可扩展到大数据集。

### 问题、动机与边界

- 论文指出现代 zkSNARK 的实际部署瓶颈不只是 prover time，还有 prover memory。例子包括 VGG16 prediction proof 需要 24GB memory 而 plaintext computation 小于 200MB；16KB SHA256 preimage 在 Plonk/Groth16 下可需要 128GB/40GB 级别空间。
- 既有 space-efficient arguments 有若干限制:
  - RAM-model schemes 可能 verifier 不够 succinct 或依赖 hidden-order groups。
  - Ligetron 面向 arithmetic circuits 但 proof size/verification 不 succinct。
  - Gemini 工作在 external streaming oracle 设定下，working buffer 小，但如果把 public parameters 和 stream instantiation 计入总空间，KZG public parameters 仍是 `O(|C|)`。
- Sparrow 只支持 layered data-parallel arithmetic circuits，而不是任意 arithmetic circuits。这是一个刻意的 tradeoff: 用更强结构假设换取低于 circuit size 的 prover space。

### Sparrow 的核心贡献

- 针对 data-parallel arithmetic circuits 的 space-efficient zkSNARK:
  - Prover field operations: `O(|C| log log |C|)`。
  - Proof size / verifier complexity: `O(log |C|)`。
  - Prover space: roughly `O(sqrt(|C|) + |inp(C)|)`，更完整形式包含 streaming-oracle space、sub-circuit description space 和 witness/input commitment space。
- Novel space-efficient sumcheck:
  - 处理 `K = sum_{x in {0,1}^n} f(x) g(x)` 这类 PIOP/GKR 需要的 product-of-polynomials instance。
  - 相比重复扫描多线性多项式的 streaming sumcheck，减少扫描轮次。
  - Achieves `O(N log log N)` field operations with `O(sqrt(N))` buffer for `N=2^n`。
- Space-efficient GKR variant:
  - 用 streaming oracles 访问每层的 data-parallel sub-circuit evaluations。
  - 对深电路做 flattening/depth reduction，避免 prover overhead 随 depth 恶化。
- Space-efficient polynomial commitment route:
  - 不使用 Gemini 那种 public parameters 线性于 witness/circuit size 的 multilinear KZG。
  - 使用 Kopis / Dory-like PC route，public parameters 和 buffer 约 `O(sqrt(N))`。

### Space-efficient sumcheck

标准 streaming sumcheck 在每轮需要扫描完整 `A_f, A_g`，对 `log N` 轮导致 `O(N log N)` prover time。Sparrow 的思路是减少变量数，从而减少必须扫描的轮数。

核心技术:

- 把原始 multilinear `f, g : F^n -> F` 替换成等价的 higher-degree polynomials `hat f, hat g`。
- 只替换前 `log N / 2` 个变量，保留后半部分让 reduced polynomial 能放进 `O(sqrt N)` buffer。
- 在实践参数中，把前半变量替换成两个高阶变量，degree 大致为 `log N` 和 `sqrt(N)/log N`，并按 degree 从小到大处理。
- Phase 1 在 `hat f, hat g` 上做 sumcheck；前两轮通过 streaming pass 计算高阶 univariate polynomials，剩余多线性部分放入 buffer 后用 standard sumcheck。
- Phase 2 把 `hat f, hat g` 的 evaluation claims 还原为原始 `f, g` 的 evaluation claims，再用 sumcheck 和 PC 验证。

这不是对基础 sumcheck 定义的替代，而是面向 streaming prover memory 的 sumcheck specialization。它适合 Sparrow/GKR/PIOP 需要的 product-of-polynomials instance，区别于只证明 `sum f(x)` 的某些并发路线。

### Sparrow zkSNARK construction

Sparrow 的 circuit class 是 layered data-parallel arithmetic circuits:

- 每层由多个相同或少数 sub-circuit copies 构成。
- Verifier/prover 可以用短描述和 streaming oracle 生成或访问 layer evaluations。
- 这种结构覆盖 SQL queries、zkRollup/bridge circuits、ML training/prediction、batch hashing 等数据并行任务。

构造路线:

1. 为单层 GKR relation 构造 space-efficient protocol。对乘法部分，将 GKR sumcheck 分成两个 `sum f*g` 形式的 phase，再调用 Sparrow sumcheck。
2. 用 streaming oracle `S(V_i)` 递归生成每层输入/输出 sub-array；利用 data-parallel wiring 高效生成 `A_h`、`A_g` 等辅助 streams。
3. 将每层 protocol 串起来得到 space-efficient GKR。通过 flattening 将 depth 压到 `< log log |C|`，避免 depth 成为主导成本。
4. 用 space-efficient PC commitment witness polynomial，并通过 evaluation proof 绑定最终 GKR claim。
5. 用 Fiat-Shamir heuristic 变成 non-interactive zkSNARK；zero-knowledge 使用 Libra-style 技术和 ZK sumcheck/PC route。

### zkFTP: zero-knowledge forest training and prediction

Sparrow 的主要应用是 zkFTP: zero-knowledge proofs of forest training and predictions。

目标:

- Prover commit to dataset `D` and forest `F`。
- ProveTrain 证明 `F = Train(D)`，不泄露 dataset 和 forest beyond allowed metadata。
- ProvePred 证明给定 test point `x` 的 prediction `y = Predict(F,x)`。
- Security includes forest/data extractability and training zero-knowledge。

关键设计不是在 circuit 里完整重跑训练，而是引入 decision-tree certification algorithm:

- 训练 decision tree 通常需要按节点反复扫描和比较，代价约 `O(h|D|)`。
- Certification 给定 tree `T` and dataset `D`，验证 `T` 是否为训练算法输出。
- 它先把数据点分配到 leaves，计算 leaf histograms，再利用 histograms 的 homomorphic property 从 leaves 聚合到 internal nodes，最后检查每个 node split 是否是 Gini index 下的最优 split。
- 在实际假设 `2d|T|B < |D|` 下，certification 约 `O(|D|)`，比重新训练更适合作为 proof statement。

zkFTP 把 certification 拆成多个证明子任务:

- Assignment correctness: 每个点的 path 与 tree inference 一致，并且 path 出现在 committed tree rows 中。
- Leaf histograms: 用 offline memory consistency checks 证明 histogram updates，而不是 `O(BN)` one-hot route。
- Non-leaf histograms: 用 tree computation transcript 和 multiset check 证明从 leaves 聚合到 root。
- Node splits: 计算 Gini index 并验证 chosen split 是最优；range proofs/comparisons 使这一步较重，因此使用 Sparrow。
- Tree well-formedness: 检查树图结构和 path consistency。
- Prediction: 复用 decision-tree prediction proof 和 matrix lookup argument；由于 matrix lookup 假设 univariate commitment，ComForest 同时维护 univariate and multilinear commitment consistency。

### 实验设置和 Sparrow benchmark

Implementation:

- 约 9000 行 C++。
- Field/curve/pairing: mcl implementation of BN_SNARK1 over 254-bit prime。
- Uses Virgo implementation for standard GKR-based parts and circuit generation。
- Datasets generated via scikit-learn `make_classification`。
- Hardware: Ubuntu 20.04.6, 131GB RAM, Intel Xeon E-2174G, 8 cores at 3.80GHz; single thread。

Sparrow benchmark tasks:

- Rectangular data-parallel circuits: `2^25` to `2^30` gates, depth 16; depth-reduction variants.
- Multiplication trees: `2^24` to `2^28` leaves.
- Batch SHA256: `2^9` to `2^13` inputs, with XOR/inner-product optimizations.
- Space-efficient sumcheck stand-alone: polynomial degree `2^23` to `2^29`, buffer 4MB-4GB.

Key results:

- Sumcheck at `N=2^29`: Sparrow takes 404.5s vs prior streaming approach 846.5s; it remains about 2.6x slower than non-space-efficient linear sumcheck but uses far less space.
- Sparrow vs Gemini:
  - Prover time improvement: roughly 3.1-11.3x depending on task; text also reports 3.4-9.5x in one comparison framing.
  - Total prover space improvement: 3.2-28.7x.
  - 2048 SHA hashes: Sparrow 700MB / 13min vs Gemini 10.5GB / 46min.
  - `2^30` LDP circuits: Sparrow 2.7GB / 78min vs Gemini 80GB / 744min.
- Sparrow vs non-space-efficient GKR+Kopis:
  - Space reduction: 27.5-119x in Sparrow benchmark tasks.
  - Prover slowdown: at most 2.7x for large reported cases.
  - Proof size: about 42-94KB across benchmark tasks.
  - Largest verification overhead: under 15ms.

### zkFTP benchmark

Configuration:

- Histogram bin size `B=128`。
- Forest max height `h=5`。
- Variable points `n`, features `d`, and number of trees `K`。
- Comparison baseline: non-space-efficient GKR+Kopis。

Single-tree training:

- With `d=16`, points from `2^16` to `2^22`:
  - `n=2^20`: Sparrow 10.1min, 0.42GB, verify 0.19s, proof 389KB; GKR+Kopis 7.7min, 90GB, verify 0.18s, proof 374KB.
  - `n=2^22`: Sparrow 44.1min, 0.95GB, verify 0.20s, proof 449KB; baseline runs out of memory.
- With `n=2^20`, features from 8 to 64:
  - `d=64`: Sparrow 32min, 0.96GB, verify 0.20s, proof 484KB; baseline runs out of memory.
- Reported space reduction reaches up to 240x while proof size and verifier time stay close to baseline.

Random forest training:

- With `K=64`, `d=16`, varying `n`:
  - `n=2^16`: Sparrow 64.3min, 0.43GB; baseline 40.8min, 124.1GB.
  - `n=2^18`: Sparrow 221.7min, 0.5GB; baseline out of memory.
  - `n=2^20`: Sparrow 873min, 0.6GB; baseline out of memory.
- With `n=2^18`, varying `K`:
  - `K=128`: Sparrow 454.7min, 0.5GB, verify 0.29s, proof 888KB; baseline out of memory.
- Reported space reduction reaches up to 288x for forests.

Space vs native certification:

- For `K=1`, `n=2^22`, `d=16`, quantized dataset is about 400MB.
- Certification alone uses 676MB.
- Sparrow proof generation uses 950MB, about 1.4x native certification space.

### 局限和非目标

- Sparrow targets layered data-parallel arithmetic circuits, not arbitrary/non-layered circuits. SHA256 shows padding/layering can increase circuit size relative to R1CS encodings.
- Prover time can still be large. Forest training examples reach hours; the space gain does not make all workloads fast.
- Evaluation is single-thread CPU and implementation-specific, not a production deployment benchmark.
- zkFTP assumes deterministic training or explicit seed; quantized datasets and histogram-based tree training are part of the modeled statement.
- The local paper delegates pseudocode, formal proofs and some security details to the full version.
- "First" claims for space-efficient properties and zero-knowledge forest training are source-authored novelty claims, not independently verified here.
- Prediction proof relies on prior decision-tree prediction/matrix lookup works; Sparrow's main new application contribution is scalable training proof.

## 分类吸收

| Nahida layer | Decision | Reason |
| --- | --- | --- |
| Source note | keep as full paper memory | Sparrow construction, zkFTP details and numeric benchmarks stay in this note |
| Primary knowledge | [[memory-efficient-snarks|Memory-efficient SNARKs]] | Main paper problem is reducing SNARK prover memory while preserving succinct verification |
| Method dependency | [[sum-check-protocol|Sum-check protocol]] | Novel space-efficient sumcheck/GKR route is core building block |
| Application knowledge | [[verifiable-training|Verifiable ML training]] | zkFTP contributes a reusable ZK ML training-integrity problem |
| Bridge | [[sum-check-protocol-to-memory-efficient-snarks|Sum-check protocol -> memory-efficient SNARKs]] | Space-efficient sumcheck transfers to low-memory SNARK construction |
| Bridge | [[memory-efficient-snarks-to-verifiable-ml-training|Memory-efficient SNARKs -> verifiable ML training]] | Low-memory proof system enables large-dataset training proofs |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Deep-read Sparrow and absorbed it as memory-efficient SNARK / space-efficient sumcheck / verifiable ML training source. | codex |
