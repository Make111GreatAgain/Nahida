---
id: "doi-10-1145-3548606-3560653-succinct-zero-knowledge-floating-point-computations"
title: "Succinct Zero Knowledge for Floating Point Computations"
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
  - "p1-p14 full extracted text"
  - "Abstract, Sections 1-7, Figure 1, Tables 1-3, claims, and references"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3548606.3560653"
doi: "10.1145/3548606.3560653"
arxiv_id: ""
venue: "ACM CCS 2022"
year: "2022"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "floating-point-snarks"
  - "commit-and-prove-arguments"
  - "approximate-floating-point-proofs"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "floating-point-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/floating-point-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/commit-and-prove-arguments"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "proof-systems"
  topics:
    - "floating-point-snarks"
    - "commit-and-prove-arguments"
    - "batch-range-proofs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "floating-point-snarks"
  - "commit-and-prove"
  - "relative-error-model"
  - "batch-range-proofs"
  - "succinct-zero-knowledge"
aliases:
  - "Succinct ZK for Floating Point Computations"
  - "relative-error floating-point ZK"
  - "batch range proof without bit decomposition"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "proof-systems"
  problem:
    - "succinct proof systems for floating-point computations"
    - "floating-point arithmetic in zero-knowledge proofs"
  method_family:
    - "commit-and-prove compiler"
    - "relative-error verification model"
    - "batch range proof without bit decomposition"
    - "R1CS compiler"
  system_layer:
    - "arithmetization"
    - "proof-system compiler"
    - "range proof layer"
  evaluation_context:
    - "32-bit floating point"
    - "64-bit floating point"
    - "IEEE-754 exact binary-circuit baseline"
    - "optimized bit-decomposition range-proof baseline"
  application:
    - "machine learning"
    - "scientific computing"
  bridge:
    - "commit-and-prove-arguments-to-floating-point-snarks"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-succinct-zk-floating-point"
source_refs:
  - "doi:10.1145/3548606.3560653"
  - "sha256:7f315f880ed5a57e40cf84f09011073bb5a4c65ba1c794062c7a8730c286ba85"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "commit-and-prove-arguments"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Title/abstract and Sections 1-2 target succinct zero-knowledge proof systems for floating point computations, not a particular ML inference proof."
  - "Sections 2-6 present a generic commit-and-prove compiler, approximate floating-point circuit satisfiability definitions, batch range proof technique, and R1CS compiler."
  - "Machine learning and scientific computing are motivating applications, but the paper does not prove a specific model inference relation."
  - "The queued arXiv ID was a DOI-fragment false positive; the stable identity is DOI 10.1145/3548606.3560653."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0073"
local_pdf: "~/Desktop/paper/3548606.3560653.pdf"
pdf_sha256: "7f315f880ed5a57e40cf84f09011073bb5a4c65ba1c794062c7a8730c286ba85"
extracted_text_path: "vault/02_Raw/pdf/extracted/succinct-zero-knowledge-for-floating-point-computations-7f315f880ed5-pages.txt"
---

# Succinct Zero Knowledge for Floating Point Computations

## 论文身份

- 标题: Succinct Zero Knowledge for Floating Point Computations
- 作者: Sanjam Garg, Abhishek Jain, Zhengzhong Jin, Yinuo Zhang
- 机构: UC Berkeley and NTT Research; Johns Hopkins University
- 会议/期刊: ACM CCS 2022
- 年份: 2022
- DOI: 10.1145/3548606.3560653
- arXiv: none observed in PDF metadata/text; queue 中的 `8606.35606` 是 DOI 片段误识别。
- 链接: https://doi.org/10.1145/3548606.3560653
- 本地 PDF: `~/Desktop/paper/3548606.3560653.pdf`
- SHA-256: `7f315f880ed5a57e40cf84f09011073bb5a4c65ba1c794062c7a8730c286ba85`
- 页数: 14
- Keywords: Succinct Proof System; Zero-knowledge; Verifiable Computation.
- License: first page states Creative Commons Attribution International 4.0 License.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 已覆盖章节/页码: Abstract, §1 Introduction, §2 Our Contributions, §3 Technical Overview, §4 Preliminaries, §5 Definitions, §6 Commit-and-Prove for Floating Point Computations, §7 Conclusion, references.
- 已检查附录: local PDF has no appendix; several proof details and instantiations are deferred to the full version.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 数学符号存在少量 Unicode/OCR 噪声；章节、表格、主公式和构造步骤可读。
- 精读说明: 队列把本论文 staged 到 `zero-knowledge-proofs/zkml/verifiable-inference`。深读后改为 `zero-knowledge-proofs/proof-systems/floating-point-snarks`，因为核心是通用 floating-point ZK proof-system compiler，不是某个 ML inference proof。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 避免 IEEE-754 exact binary circuit 的 `poly(w)` prover overhead；提出 relative-error model、generic CP compiler、batch range proof；32-bit 场景约 57x faster | high | 主分类依据 |
| §1 / p1-p2 | 动机 | Succinct ZK proof 已用于 blockchain 等场景；floating point 在 ML/scientific computing 普遍存在；IEEE-754 exact conversion 太贵 | high | 应用动机，不等于 zkML source |
| §2.1 / p2-p3 | 模型 | 每个浮点 gate 只证明相对误差上界 `|c-g(a,b)| <= delta |g(a,b)|`，而不是精确证明 round-to-nearest | high | 与 ZKLP 的 exact IEEE route 形成对照 |
| §2.2 / p3-p4 | 构造与参数 | generic compiler from public-coin commit-and-prove ZKPoK for R1CS；R1CS size `O(log w + k) * |C|`；sublinear verification additive overhead `O(sqrt(|C|))` | high | 更新 CP bridge |
| Table 1 / p4 | 性能概览 | 32-bit add/mul: 89/35 R1CS vs bit decomposition 296/207 vs IEEE 2456/8854；64-bit add/mul: 115/24 vs 528/439 vs 15637/44899 | high | 结果数字 |
| §2.3 / p4 | Related work | Weng et al. 支持 non-succinct ZK floating point via IEEE binary circuits；Setty et al. 支持 rational/floating route but no rounding | medium | novelty boundary |
| §3 / p4-p7 | 技术概览 | 把 relative-error inequality 转为 positivity/range proof；用 Legendre three-square theorem；在 prime known-order groups 中用 small random linear combinations 做 batch range proof | high | 核心机制 |
| §4 / p6-p7 | Preliminaries | Legendre three-square theorem and randomized algorithm for `4k-3 = x^2+y^2+z^2` | medium | range proof 依赖 |
| §5 / p7-p8 | Definitions | fixed/floating point number, `delta`-approximate correctness, floating/fixed/real satisfiability, promise language, succinctness, Fiat-Shamir route | high | formal model and caveat |
| §6.1 / p8-p9 | Construction | R1CSCompiler, Figure 1 commit-and-prove protocol, variable sets `S1/S2`, range checks over random linear combinations | high | mechanism detail |
| §6.4 / p9 | Zero-knowledge | additively homomorphic commitment; commit to padded witness; hide random linear combinations with bit decomposition; produces ZK-SNARG via Fiat-Shamir | high | ZK boundary |
| §6.5 / p9-p12 | Floating point extension | addition/subtraction use exponent-case indicators and one bit decomposition; multiplication uses exponent relation `e_c-(e_a+e_b) in {w-1,w}` | high | floating-specific compiler |
| §6.7 / p12-p13 | Optimization/performance | small-p compiler, soundness amplification, comparisons vs bit-decomposition and IEEE-754 exact circuits; Tables 2-3 | high | performance caveats |
| §7 / p13 | Conclusion | Future work: polylog verification without prover blowup; exact-rounding-critical domains like finance/accounting | medium | gaps |

## 核心精读笔记

> 这篇论文提出的不是一个具体应用系统，而是一条 proof-system/compiler 路线: 不再证明浮点运算严格遵守 IEEE-754 每一步舍入，而是证明每个 gate 的相对误差被一个 `delta` 上界约束。这个模型牺牲了精确舍入语义，换来把 prover 的浮点约束开销从 IEEE binary circuit 的 `poly(w)` 降到大致 `log(w)` 级别，并可从已有 public-coin commit-and-prove R1CS proof systems 编译得到 succinct ZK proof。

### 背景、动机与问题边界

Succinct ZK proof systems 通常把 computation 编成 arithmetic/binary circuit；但真实软件、ML 和科学计算大量使用 floating point。标准做法是把 IEEE-754 浮点运算转成 binary circuit 并证明 exact rounding。论文指出该路线对 prover 极贵: 例如文献 [35] 把 32-bit floating multiplication 转成 8854 个 gates；这会把 prover running time 放大约 9000 倍。

本文问题是: 能否为 floating point computations 构造 prover-efficient succinct ZK proof systems?

论文明确不解决:

- 不证明每一步都按 IEEE-754 exact round-to-nearest 语义执行。
- 不覆盖 zeros, infinities, NaN 等 corner cases 的完整电路；正文说这些可以 separate treatment。
- 不给出 finance/accounting 这类精确舍入至关重要场景的最终方案；结论把它列为 future work。
- 不证明某个具体 ML model 的 inference correctness；ML/scientific computing 是动机和潜在应用。

### 相对误差模型

论文的核心模型是 `delta`-approximate correctness。对每个 floating/fixed point addition/subtraction/multiplication gate，输入为 `a,b`，输出为 `c`，精确函数为 `f(a,b)`，要求:

```text
|c - f(a,b)| < delta * |f(a,b)|
```

这个模型来自 numerical analysis。作者的论证是: 很多数值算法的 output accuracy 本来就是通过每一步 relative error bound 做 backward/forward error analysis 得到；因此对 ML/scientific computing 类应用，比起证明 precise IEEE rounding，证明每步相对误差上界可能更有意义和更便宜。

关键边界:

- Completeness 针对 floating `delta`-satisfiable circuits。
- Soundness 针对 not real `delta`-satisfiable circuits。
- 因为 real numbers 与 fixed-precision floating numbers 之间存在表示差异，论文承认 completeness/soundness 之间有 theoretical gap；作者认为实践中对 rounding perturbation 鲁棒的程序里 gap 较窄。

### Generic commit-and-prove compiler

论文把多数现有 succinct ZK proof systems 抽象为 public-coin commit-and-prove systems for R1CS。给定 precision `w`、exponent bit-length `k` 和 floating point circuit `C`，compiler 的核心代价是:

- Prover time 等价于底层 CP protocol 证明一个大小 `|X| = O(log w + k) * |C|` 的 R1CS instance。
- Proof size 是底层 proof size 加 `O(1)` field elements；ZK version 约需要两份 commitment/proof，所以实际估计约 2x proof size。
- Verification time 是底层 CP verifier 加 `O(sqrt(|X|))` group operations。
- 若底层 CP system 是 public-coin and succinct，则 compiler 产物也是 public-coin succinct；可用 Fiat-Shamir 变成 non-interactive ZK argument in random oracle model。

这使本论文对 [[commit-and-prove-arguments|Commit-and-prove arguments]] 的贡献很明确: CP 不只是应用组合接口，也可以作为 floating-point proof compiler 的 backend abstraction。

### Batch range proof without bit decomposition

为了证明相对误差 inequality，论文把 `|x| < |y|` 转为 `z = (x+y)(y-x) > 0`。证明 positivity 时使用 Legendre three-square theorem:

```text
z > 0  iff  4z - 3 > 0
4z - 3 = gamma_1^2 + gamma_2^2 + gamma_3^2
```

难点在于 succinct proof systems 多在 finite field 中工作，Equation 只在 mod `p` 下成立时可能发生 wrap-around，不能直接推出整数/实数上的 positivity。论文的解决路线:

1. 选择足够大的 prime known-order field，使 small values 不 wrap around。
2. 对 batch values 使用 small random linear combinations，而不是逐个 open commitments。
3. 证明如果某个值太大，则小范围随机线性组合也以 overwhelming probability 变大。
4. 处理“fraction mod p” counterexample: 若 cheating proof 通过，则可抽取出 small numerator/denominator fraction 形式；在足够大的 `p` 下把 mod equations 提升到 reals。

这得到一个不用 bit decomposition 的 batch range proof route。相比 unknown-order groups/RSA/class groups，它保持在 standard prime known-order groups。

### Fixed-point 到 floating-point extension

固定点计算中，`a = a' 2^-w, b = b' 2^-w, c = c' 2^-w`。对 multiplication，令:

```text
x = Delta_2 * (2^w c' - a'b')
y = Delta_1 * a'b'
z = (x+y)(y-x)
```

再用 three-square equality 证明 `z > 0`。

浮点计算的额外问题是 exponent。论文用浮点数 `(s,e)` 表示 `s * 2^(e-w)`，其中 significand normalized。

对 addition/subtraction:

- 证明 Claim 1: 若 approximate correctness 成立，则 `min(e_a-e_b, e_b-e_c, e_a-e_c) in {-1,0,1}`。
- 用三个 relaxed indicator variables 表示三种 exponent 近邻情形。
- 只对一个选中的 exponent difference 做 bit decomposition，并对小 `theta` 用 repeated squaring；对大 `theta` 把 inequality 替换成 reject/equality cases，避免 modulus bit length 随 `2^k` 膨胀。

对 multiplication:

- 证明 Claim 2: 若 approximate correctness 成立，则 `e_c - (e_a+e_b) in {w-1,w}`。
- 如果不在该集合内直接 reject；否则通过 Lagrange interpolation 计算 `2^theta` 并接入 range proof。

### Zero-knowledge 改造

基础协议会把 random linear combinations `v_i` 发给 verifier。为了 ZK，论文假设底层 commitment additively homomorphic，并修改 protocol:

1. Prover 先 commit `W_R1CS || 0^m`。
2. 对每个 `v_i` 做 bit decomposition 和 sign 表示，但不明文发送 `v_i`。
3. 发送一个 commitment `c'` 到 padding/witness 结构。
4. 在 R1CS 中加入 range constraints 和 format checking，确保 `c'` 不改变初始 witness。
5. 用底层 ZK commit-and-prove protocol 同时检查两个 R1CS instances。

Fiat-Shamir 后得到 ZK-SNARG for floating/fixed point computations。

### 性能与代价

论文主要比较三种路线:

- This work: relative-error + batch range proof without bit decomposition。
- Bit.: 用 optimized bit decomposition 做 range proofs。
- IEEE-754: 把 floating point add/mul 转成 exact IEEE binary circuit。

主要表格结果:

| Setting | This work R1CS per add/mul | Bit. R1CS per add/mul | IEEE-754 R1CS per add/mul | Notes |
| --- | --- | --- | --- | --- |
| 32-bit, large group | 89 / 35 | 296 / 207 | 2456 / 8854 | Table 1/2, `log2 p = 384` |
| 64-bit, large group | 115 / 24 | 528 / 439 | 15637 / 44899 | Table 1/2, `log2 p = 384` |
| 32-bit, small group | 108 / 25 | 296 / 207 | 2456 / 8854 | Table 3, `log2 p = 256` |

作者综合估计:

- 32-bit/64-bit large-group setting 下，R1CS per gate 比 IEEE exact route 小约 91x / 432x，比 optimized bit-decomposition 小约 4x / 7x。
- 考虑 group size 后，prover efficiency 对 32-bit 约 45x faster than IEEE、2x faster than bit-decomposition；64-bit 约 216x faster than IEEE、3.5x faster than bit-decomposition。
- Abstract/§2 还报告 32-bit 约 57x faster than IEEE exact route，64-bit 约 236x faster；差异来自比较口径和 group-size accounting。
- proof size 约为其他两种方法的 2x，因为 ZK protocol 发送两份 commitments/proofs。
- sublinear verification non-ZK variant 相比 optimized bit-decomposition 的 prover efficiency 只提升 53%/28%，说明 sublinear verifier route 会吃掉一部分 prover 优势。

### 作者结论与我的判断

作者明确声称两项贡献:

- 新的 relative-error model for verifying floating point computations。
- 高效 succinct ZK proof system with sublinear verification。

基于证据的判断:

- 本文应该作为 [[floating-point-snarks|Floating-point SNARKs]] 的核心 source extension，补齐“approximate relative-error route”。
- 它也应该更新 [[commit-and-prove-arguments|Commit-and-prove arguments]]，因为 generic compiler 的输入就是 public-coin commit-and-prove ZKPoK for R1CS。
- 它不应该作为 [[verifiable-inference|Verifiable inference]] 的代表 source；没有 model commitment、具体 ML architecture、operator proof 或 inference statement。

仍需谨慎:

- 正文多处把 full security proof、sublinear verification details、instantiation 交给 full version；本地 PDF 只能记录主构造和作者给出的概要/参数。
- exact IEEE-754 route 和 relative-error route 解决的问题不同，不能直接说本文完全替代 ZKLP/IEEE-compliant FP circuits。
- 对 finance/accounting 这种 precise rounding matters 的应用，作者自己也列为 future work。

## 层级候选分类

- L1 Domain candidate: `zero-knowledge-proofs`
- L2 Direction candidate: `proof-systems`
- L3 Topic/content cluster candidates: `floating-point-snarks`, `commit-and-prove-arguments`, `batch-range-proofs`
- Ontology path: `zero-knowledge-proofs/proof-systems/floating-point-snarks`
- 备选归属:
  - `zero-knowledge-proofs/zkml/verifiable-inference`: rejected as primary; only application motivation.
  - `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments`: secondary method dependency.
- 父级领域: zero-knowledge proof systems / verifiable computation
- 学术子领域: succinct zero-knowledge proof systems, R1CS, commit-and-prove, range proofs
- 任务/问题: efficient ZK proofs for floating-point computations
- 方法族: relative-error model, generic CP compiler, batch range proof without bit decomposition
- 评测场景: 32-bit and 64-bit floating-point addition/multiplication circuits
- 应用: machine learning and scientific computing as motivating domains; not primary evidence for zkML inference
- 别名: relative-error floating-point ZK; succinct ZK floating point
- 相邻方向: IEEE 754 SNARK circuits, zkML numeric semantics, commit-and-prove arguments
- 置信度: high
- 分类状态: corrected_from_queue
- 分类证据: Abstract, §2.1, §2.2, §6.1-§6.7, Tables 1-3

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | zero-knowledge-proofs | CCS security/cryptography venue; succinct ZK proof systems and CP protocols throughout | high | durable parent |
| Research background | Floating-point arithmetic is common in ML/scientific computing but exact IEEE circuits are prover-expensive | §1, §2.1 | high | knowledge background |
| Research problem | Succinct ZK proofs for floating-point computations with low prover overhead | Abstract, §1, §2 | high | update floating-point-snarks |
| Foundation concepts | zk-SNARKs / succinct ZK, commit-and-prove, R1CS, range proofs | §1-§6 | high | existing nodes; CP bridge update |
| Method family | relative-error compiler + batch range proof without bit decomposition | §2.2, §3, §6 | high | source extension; bridge |
| Application/evaluation context | 32-bit/64-bit floating add/mul; ML/scientific computing motivation | Tables 1-3; §2.1 | high | evaluation/source-only |
| Artifact/source instance | CCS 2022 paper and generic compiler | whole paper | high | representative source |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: [[floating-point-snarks|Floating-point SNARKs]]。
- 它能帮助未来哪些问题少读 source notes:
  - “浮点数 ZK 一定要严格 IEEE-754 吗?”
  - “relative-error floating-point proof 是什么?”
  - “commit-and-prove 怎样编译到 floating point proofs?”
  - “为什么 floating-point ZK 可以比 IEEE binary circuit 快?”
- 留在 source note 的内容:
  - Claim 1/Claim 2 的具体推导、indicator constraints、small/large `theta` cases、Table 1-3 具体数字、full construction caveats。
- 不创建的新节点:
  - 不建 paper-specific compiler node。
  - 不把 batch range proof 单独建为 node，暂作为 `floating-point-snarks` / `commit-and-prove` 的 source extension；如果后续多源复用再拆。
  - 不作为 zkML verifiable inference source。

## 一句话贡献

本文把 floating-point ZK proof 的目标从 exact IEEE-754 rounding proof 改写成 relative-error bounded proof，并给出从 public-coin commit-and-prove R1CS systems 到 succinct ZK floating-point proof 的 generic compiler，核心优化是不依赖 bit decomposition 的 batch range proof。

## 连接

- 相关 Knowledge nodes:
  - [[floating-point-snarks|Floating-point SNARKs]]
  - [[commit-and-prove-arguments|Commit-and-prove arguments]]
  - [[proof-systems|Proof systems]]
  - [[zk-snarks|zk-SNARKs]]
- 相关 Bridges:
  - [[commit-and-prove-arguments-to-floating-point-snarks|Commit-and-prove arguments -> Floating-point SNARKs]]
- Bridge 候选:
  - `floating-point-snarks -> zkML verifiable inference`: review only; 需要具体 zkML source，而不是本文的 motivating examples。

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| Relative-error floating-point proofs | method route | §2.1, §5, §6 | active_seed | 写入 floating-point-snarks 方法族 |
| Batch range proofs without bit decomposition | method candidate | §2.2, §3, §6.1 | watching | 后续多源复用后考虑拆节点 |
| Exact rounding vs approximate correctness taxonomy | taxonomy update | §2.1, §7 | active_seed | 写入 floating-point-snarks 正反例/方法路线 |
| Floating-point zkML numeric semantics | application bridge candidate | ML motivation only | review | 等 ZKML floating-point primary source |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| IEEE-754 exact binary circuit route causes high prover overhead | author claim + example | §1, p2 | 32-bit multiplication in [35] uses 8854 gates | high | queue classification correction evidence |
| Relative-error model verifies `|c-g(a,b)| <= delta |g(a,b)|` | formal definition | §2.1, §5.1 | `delta`-approximate correctness definition | high | core model |
| Generic compiler targets public-coin commit-and-prove systems for R1CS | construction | §2.2, §6.1 | compiler parameters and Figure 1 | high | bridge evidence |
| Compiler prover cost is underlying CP on `O(log w + k) * |C|` R1CS | complexity | §2.2 | explicit parameter statement | high | source-level detail |
| Batch range proof avoids bit decomposition in prime known-order groups | method | §2.2, §3 | Legendre three-square + small random linear combinations | high | method route |
| ZK version roughly doubles proof size | cost caveat | §6.4, §6.7, Tables 1-3 | two commitments/proofs `c,c'` and `Pi,Pi'` | high | knowledge boundary |
| 32-bit large-group R1CS add/mul are 89/35 vs IEEE 2456/8854 | evaluation | Table 1/2 | table values | high | exact numeric evidence |
| Not a zkML verifiable inference source | classification judgment | whole paper | no ML model/proof statement; ML is application motivation | high | queue correction |

## 知识交接

- 留在本文元笔记的证据: relative-error definitions, R1CSCompiler steps, three-square/range proof reasoning, performance tables, exact caveats about full-version proofs.
- 待更新 Knowledge node:
  - [[floating-point-snarks|Floating-point SNARKs]]
  - [[commit-and-prove-arguments|Commit-and-prove arguments]]
  - [[proof-systems|Proof systems]]
  - [[research-dynamics|Zero-knowledge proofs Research Dynamics]]
- 作为哪些 Knowledge node 的 source extension:
  - `zero-knowledge-proofs/proof-systems/floating-point-snarks`
  - `zero-knowledge-proofs/proof-systems/commit-and-prove-arguments`
- 需要补的 foundation knowledge/source:
  - Weng et al. [35] / IEEE exact floating point ZK route if not already represented by ZKLP.
  - Setty et al. [31] and range-proof prior sources if future taxonomy needs them.
- Bridge 候选:
  - Create `commit-and-prove-arguments -> floating-point-snarks`.
  - Queue/review `floating-point-snarks -> zkML verifiable inference` until a concrete ML floating-point proof source appears.
- Watchlist 词条: `relative-error ZK`, `floating-point ZK`, `batch range proof`, `IEEE-754 exact ZK`, `approximate correctness`.
- Review queue: queued arXiv false positive should be corrected in queue/ledger.

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Floating-point SNARKs | existing method_family | 更新完整 Knowledge node，加入 relative-error route | 只把本论文当作 zkML inference paper | Abstract, §2, §6 |
| Commit-and-prove arguments | existing method_family | 添加 generic compiler source extension and bridge | 把 CP 当成本论文私有机制 | §2.2, Figure 1 |
| Batch range proof without bit decomposition | source extension / watching | 暂放 floating-point-snarks/CP 方法路线，后续多源再拆 | 单源直接建 foundation node | §2.2, §3 |
| Relative-error model | method route | 写入 floating-point-snarks 的方法路线和边界 | 声称替代所有 IEEE exact proof needs | §2.1, §7 |
| zkML verifiable inference | rejected primary | 作为 future bridge candidate only | 把 ML motivation 当作吸收证据 | §1-§2 |

## Knowledge 综合交接

- 应创建 Knowledge node: none.
- 应刷新 Knowledge synthesis section: `floating-point-snarks`, `commit-and-prove-arguments`, `proof-systems`.
- 应创建 Bridge: `commit-and-prove-arguments-to-floating-point-snarks`.
- 应标记过期: none.
- 无需更新的理由: `verifiable-inference` 不更新为 source evidence，因为本文没有具体 ML inference proof statement。
- 建议 node kind: source extension + bridge.

## 处理日志

- 2026-06-23: extracted metadata/text with bundled Python/pypdf; deep-read p1-p14; wrote source note; prepared knowledge handoff.

