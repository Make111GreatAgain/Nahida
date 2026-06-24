---
id: "sha256-d6c935fe1d1a-mangrove-scalable-framework-folding-based-snarks"
title: "Mangrove: A Scalable Framework for Folding-based SNARKs"
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
  - "p1-p69 full extracted text"
  - "Appendix A.1-A.7 deferred proofs and extractor argument"
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown"
year: "2024"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "memory-efficient-snarks"
  - "folding-schemes"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "memory-efficient-snarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/memory-efficient-snarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/recursion-and-folding/folding-schemes"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/proof-systems/modular-zksnarks"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "proof-systems"
    - "recursion-and-folding"
  topics:
    - "memory-efficient-snarks"
    - "folding-schemes"
    - "proof-carrying-data"
    - "commit-and-prove-snarks"
domains:
  - "zero-knowledge-proofs"
topics:
  - "memory-efficient-snarks"
  - "folding-schemes"
  - "proof-carrying-data"
  - "plonkish-arithmetization"
aliases:
  - "Mangrove"
  - "folding-based SNARKs"
  - "memory-efficient SNARKs"
  - "streaming SNARKs"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "proof-systems"
    - "recursion-and-folding"
  problem:
    - "SNARK prover memory"
    - "streaming proving"
    - "folding-based SNARK construction"
  method_family:
    - "uniform compiler"
    - "proof-carrying data"
    - "commit-and-fold"
    - "folding schemes for polynomial relations"
  system_layer:
    - "prover"
    - "proof-system engineering"
  evaluation_context:
    - "Plonkish arithmetization"
    - "large Plonkish instances"
    - "MacBook Pro performance estimates"
  application:
    - "generic NP/SNARK proving"
    - "commit-and-prove witness reuse"
  bridge:
    - "folding-schemes-to-memory-efficient-snarks"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-mangrove"
source_refs:
  - "sha256:d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
  - "filename:2024-416.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "recursion-and-folding"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "title and abstract state scalable folding-based SNARKs"
  - "Sections 2 and 6 construct a SNARK from uniform chunks and PCD"
  - "Section 6.4 evaluates prover memory, proving time, and proof size"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0028"
local_pdf: "~/Desktop/paper/2024-416.pdf"
pdf_sha256: "d6c935fe1d1ac826fb061425d7087b32163cd161fe6d103efc0f3663aacb49a9"
extracted_text_path: "vault/02_Raw/pdf/extracted/2024-416-d6c935fe1d1a-pages.txt"
---

# Mangrove: A Scalable Framework for Folding-based SNARKs

## 论文身份

- 标题: Mangrove: A Scalable Framework for Folding-based SNARKs
- 作者: Wilson Nguyen, Trisha Datta, Binyi Chen, Nirvan Tyagi, Dan Boneh
- 机构: Stanford University
- 会议/期刊: unknown from extracted PDF
- 年份: 2024
- DOI: unknown
- arXiv: unknown
- 链接: unknown; filename suggests a possible ePrint identifier, but the extracted PDF does not expose a canonical URL
- 本地 PDF: `~/Desktop/paper/2024-416.pdf`
- 代码: no Mangrove artifact URL found in extracted PDF; evaluation bootstraps the Nova implementation reference
- 数据: synthetic Plonkish instance estimates and circuit synthesis/benchmarking from a modified Nova implementation
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 69
- 已覆盖章节/页码: p1-p69, including abstract, introduction, technical overview, preliminaries, generalized folding schemes, SNARK construction, performance evaluation, lookup and commit-and-prove extensions, bibliography, and deferred proofs.
- 已检查附录: Appendix A.1-A.7 covered, including proofs for polynomial witness testing, Theorem 2, Theorem 3, multi-instance folding extraction, Theorem 4, and Theorem 5 knowledge soundness.
- 未覆盖章节/页码: none known.
- Extraction gaps: no visible scanned/OCR gap. PDF metadata lacks title/authors/DOI/arXiv; canonical identifier should be verified externally if needed.
- 精读说明: 队列原先把本文归到 `zero-knowledge-proofs/recursion-and-folding/folding-schemes`。深读后纠正主路径为 `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`，因为论文目标是把 folding/PCD 用来构造低内存、少遍历、可并行的 SNARK；`folding-schemes` 是方法依赖和桥接端点，不是论文主问题层。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和贡献 | uniformizing compiler, PCD/folding optimizations, constant transparent CRS, low memory, two-pass prover, parallelizable SNARK | high | 主分类依据 |
| §1 / p4-p8 | 引言 | monolithic SNARK memory bottleneck, streaming/IVC alternatives, Mangrove-Basic and Mangrove-Tree positioning | high | 问题边界和相关工作 |
| §2.1 / p9-p11 | Uniform compiler | Plonkish trace chunking, local gate constraints, copy constraints partial product, Merkle commitments, two passes | high | 核心编译器机制 |
| §2.2 / p11-p13 | SNARK from PCD | 用 PCD tree 合并 uniform chunks，root proof 证明全局满足 | high | 将 chunked NP 变成 SNARK 的路线 |
| §2.3 / p13-p20 | PCD reduced overhead | decoupling PCD computation/control tree; commit-and-fold over committed values | high | 论文主要优化 |
| §3 / p20-p29 | Preliminaries | NARK/SNARK, commitments, Merkle commitments, folding schemes, PCD, tree evaluation | medium | 依赖定义 |
| §4 / p29-p31 | Polynomial relations | 把 polynomial map relation 与 opening/collision relation 组织成 foldable relation pair | high | commit-and-fold 基础 |
| §5 / p31-p35 | Folding schemes for polynomial relations | homogeneous opening protocol, arbitrary polynomial maps Protocol 2, heuristic standard-model discussion | high | 理论贡献 |
| §6 / p35-p45 | Plonkish SNARK | NARK for Plonkish, PCD predicate, TreeEval helper, Construction 2, Theorem 5, performance estimates | high | 最终构造与实验 |
| §7 / p45-p49 | Extensions | lookup tables and commit-and-prove SNARK extension | medium | 可扩展性和组合性 |
| Appendix / p57-p69 | Deferred proofs | special soundness, Fiat-Shamir folding scheme, extractor construction, knowledge soundness | high | 安全/正确性骨架 |

## 核心精读笔记

> Mangrove 的核心不是证明聚合，也不是分布式 proving。它把 folding schemes 和 PCD 作为构造低内存 SNARK 的内部机制：先把 Plonkish NP 关系 uniformize 成许多相同小块，再用树形 PCD 和 folding 将这些小块证明压成一个 succinct proof。

### 背景、动机与问题边界

- 背景脉络: SNARK 研究不只追求 verifier succinctness，还要降低 prover time 和 peak memory。monolithic SNARK 通常需要持有完整 computation trace，并执行全局 FFT/MSM/proximity-proof 类操作；电路变大时内存成为主要瓶颈。
- 现有方法不足:
  - chunk global computations 或 streaming polynomial commitments 可以降内存，但会带来多 pass 或时间开销。
  - piecewise SNARKs/IVC 可分块证明，但 universal circuit/CPU 路线有较大 overhead，Nova-UC 还存在 constant-length computation security 限制。
  - 直接把 PCD 用于 uniform chunks 会让 leaf 节点也承担递归控制逻辑，leaf 数量远大于 internal nodes 时 overhead 被放大。
  - 直接在 folding relation 里编码 commitment opening constraints 会让 Pedersen/hash 类 commitment 成本压过真正的 leaf computation。
- 本文问题定义: 对任意 poly-time computation，能否编译为 uniform simple steps，并用 folding-based PCD 构造一个 memory-efficient SNARK，使 prover 只需常数级内存参数、少量 passes、可并行，同时 proof/verifier 仍 succinct。
- 明确不解决的问题:
  - 不完整展开 zero-knowledge masking，只说可用已有技术适配。
  - 不给完整生产实现；性能是基于 Nova implementation/circuit synthesis 的估计。
  - 不解决 witness generation 本身的 streaming/分布式问题。
  - 不声称所有 folding schemes 都无需 heuristic；用于 PCD 的 standard-model folding scheme仍通过 random-oracle instantiation 的启发式安全处理。
- 证据锚点: Abstract, §1, §2.3, §5.3, §6.4。

### 模型、假设与定义

- 目标关系: Section 6 使用 Plonkish arithmetization `plk := (sigma, s, G)`，要求 value vector `z = (x, w)` 同时满足 global copy constraints 和 local gate constraints。
- memory parameter `m`: chunk size 和 prover/verifier memory driver，要求 `|x| <= m <= n`；当 `m = O_lambda(1)` 时 proof size 可为 `O_lambda(1)`。
- arity parameter `k`: PCD/Merkle tree arity，`k = O(lambda)`，影响 PCD node 数、递归电路大小、proof size 和 peak memory。
- commitment assumptions: 需要 binding、linearly homomorphic、succinct commitments；Merkle commitment 需要 collision-resistant hash；PCD 和 folding scheme 需要相应知识可靠性。
- folding relation: Section 4 把 polynomial map `f`、linear maps `Lx`/`Le`、opening relation `Ropen` 和 collision relation组合起来，允许对 committed values 做 folding。
- PCD model: proof-carrying data 把树形计算图的每个 node 视为 carrying proof/data label；root proof 证明整棵树 compliance。
- 证据锚点: §3, Definition 18-22, Theorem 5。

### 方法、协议或系统机制

#### Uniform compiler: 把 Plonkish NP statement 变成 uniform chunks

Mangrove 利用 Plonkish arithmetization 的规则结构: selector vector 和 permutation/copy constraints 是全局对象，但每个 gate/chunk 的局部检查长得一样。编译器把 extended witness `z` 和 index data 分为大小 `m` 的 chunks。每个 chunk 做三件事:

- 检查 local gate constraints，例如 gate polynomial `G(s_i, z_i) = 0`。
- 计算 global permutation/copy constraint 的 partial product，而不是一次性检查全局乘积。
- 对 chunk 的 index/wire data 形成 commitment，并用 Merkle root 把所有 chunk commitments 绑定到一起。

论文的两遍 prover 结构是: 第一遍 committed witness wire vector 并产生 verifier challenges；第二遍用 PCD over chunks 合并 partial products、Merkle roots 和 folded leaf relation。这个设计让 verifier 不必直接读取所有 chunks。

证据锚点: §2.1, §6.1-§6.2。

#### PCD from chunks: 让 root proof 代表整棵 chunk tree

基础 PCD predicate `phi_snark` 需要检查:

- leaf/node 的 Merkle commitments 是否按树结构正确合并；
- partial products 是否在父节点按乘法合并，并在 root 等于目标值；
- leaf computation 的 folding proof 是否把 child leaf instances 正确折叠到 parent instance。

如果直接用通用 PCD relation，每个 node 都要处理 leaf 逻辑和 merge/control 逻辑。Mangrove 观察到 high arity 时 internal nodes 数量远小于 leaves；例如 `k = 128`, `T = 2^21` leaves 时 internal nodes 只有 16513。因此 leaf-level 的递归控制 overhead 是主要浪费。

证据锚点: §2.2-§2.3, Fig. 4, Definition 21-22。

#### Decoupling PCD computation tree and control tree

第一项 PCD 优化是 decoupling:

- 把 leaf computation 独立成 `Rleaf`，专门证明 uniform chunk 的 gate/copy/product computation。
- 新 PCD predicate `phi_decouple` 不再把 leaf computation 直接塞进主 PCD relation，而是验证 leaf relation 的 folding proof，并只在 control tree 中处理 merge constraints。
- 这样 merging overhead 从所有 `T + (T - 1)/(k - 1)` 个 nodes 降到约 `(T - 1)/(k - 1)` 个 internal nodes。

直观上，leaf computation 和递归控制被拆开，leaf 密集部分做真正局部计算，较稀疏的 control tree 才承担递归合并。

证据锚点: §2.3, Fig. 5。

#### Commit-and-fold: 在 committed values 上折叠，避免把 opening constraints 编进电路

第二项优化是 commit-and-fold。论文指出，如果为了证明 leaf computation 读取了正确的 committed values，就在 leaf relation 中编码 Pedersen/hash opening constraints，约束数量会比实际 gate/copy checks 大 100-200 倍。Mangrove 改为对 commitment image 中的 relation 做 folding:

- `Lx` 把 witness 向量线性映射到 commitments 和少量公开元素，例如 `Commit(i, sigma, s)`, `Commit(z)`, `Commit(L, R)`, `p`, `mu`。
- `Le` 把 error/evaluation 向量也线性映射到 commitment。
- relation 检查的是 `(x, e)` 是否是某个 witness 的 committed image，而不是在递归电路中展开 commitment opening。
- 对非齐次 polynomial map，论文给出 homogeneous transform 或 Protocol 2 的 arbitrary polynomial maps 方案。

这使 Mangrove 更像“在 commitment 层折叠证明义务”，而不是“把所有 commitment 验证都转成 arithmetic circuit”。

证据锚点: §2.3, §4, Definition 20, §5.1-§5.2。

#### Folding schemes for polynomial relations

Section 5 给出两类 folding scheme:

- Homogeneous opening protocol: 先把非齐次 polynomial map 通过 `hat f(x, mu)` 齐次化，然后用多轮开口协议折叠 `ell` 个 instances。Theorem 2 给出基于 adaptive Fiat-Shamir 的 secure folding scheme。
- Arbitrary polynomial maps Protocol 2: 直接处理任意 polynomial map `f: F^m -> F^n`，用 Lagrange basis 和 cross-term vectors `q_j` 让 verifier 随机抽点 `r` 后检查折叠后的 instance。Theorem 3 给出 security；Remark 4 说明 Protocol 2 只需两轮，verifier 操作约减半，但 prover field operations 是 `O(k^2 m)`，FFT-friendly field 可降为 `O(k log k m)`。

Section 5.3 明确把 standard-model 折叠用于 PCD 时依赖一个 heuristic conjecture: random-oracle folding scheme 可通过合适 hash instantiation 获得 standard-model folding scheme。这是重要安全边界。

证据锚点: Definition 17, Protocol 2, Theorem 2, Theorem 3, Remark 4, Conjecture 1。

#### Final Plonkish SNARK construction

Construction 1 先定义一个 NARK for `Rplk`: prover 直接给出 extended witness `z`、permutation argument 的 `L/R` vectors，verifier 检查 local gate constraints 和 grand product permutation check。这个 NARK 不 succinct，但 verifier checks 很 uniform，适合 chunk/folding。

Construction 2 用 PCD 把该 NARK verifier work 外包给 prover:

- indexer 预处理 Plonkish index chunks，计算 `hplk` Merkle commitment。
- prover 对 `z` chunks 做 commitments，生成 `hz`，用 `ro(hplk, x, hz)` 导出 `alpha, beta`。
- 每个 chunk 产生 leaf relation witness `Wi` 和 instance `Xi`。
- `TreeEval(Jnpk, ...)` streaming 评估 PCD tree，生成 root label `Z`、PCD proof 和 final folded witness。
- verifier 检查 root `p = 1`, `hplk' = hplk`, `hz' = hz`, PCD proof, final folded leaf relation, first chunk contains public input `x`。

Theorem 5 证明该 construction 是 `Rplk` 的 secure SNARK。proof size 为 `O(m + k log_k(n/m))`，若 `m = O_lambda(1)` 且 `k = O(lambda)`，则 proof size 可为 `O_lambda(1)`。

证据锚点: Construction 1, Theorem 4, Construction 2, Theorem 5。

### 理论、证明或正确性论证

- Lemma 5 / Appendix A.1: polynomial witness testing 的正确性依赖 `Lx'` 和 `Le` binding；如果 projection 或 evaluation 不匹配，可以构造 binding collision adversary。
- Theorem 2 / Appendix A.2: homogeneous opening protocol 通过 special soundness 与 adaptive Fiat-Shamir 转成 folding scheme；special soundness 证明通过多 transcript 解出原始 openings 或得到 `Lx` collision。
- Theorem 3 / Appendix A.3: arbitrary polynomial Protocol 2 的 special soundness 依赖 Lagrange interpolation 和 Lemma 6 的 cross-term decomposition；`d(ell-1)+1` 个 accepting transcripts 可抽取所有 inputs 或 collision。
- Theorem 4 / Appendix A.5: Plonkish NARK knowledge soundness 用 trivial extractor 从 proof 中 parse `z=(x,w)`，再用 zero-finding game 约束 permutation grand product false positive。
- Theorem 5 / Appendix A.6-A.7: SNARK knowledge soundness 通过 PCD extractor 抽出 compliant tree，再逐层调用 folding extractor，最终把 leaf witnesses 拼接成完整 `z`，借助 Merkle/commitment binding 和 polynomial witness testing 证明 `(idx, x, w) in Rplk`。
- 证据锚点: Appendix A.1-A.7。

### 实验、评估或案例

- Evaluation methodology:
  - 使用 generic PCD construction from BCL+21；
  - 用 Section 5 的 generalized folding/accumulation scheme；
  - 只评估 degree-2 Plonkish circuits，即 addition/multiplication gates；
  - 基于 Nova implementation，Pallas-Vesta curve cycle，synthesize leaf/primary/secondary circuits and benchmark prove/fold costs；
  - 实验机器: MacBook Pro, Apple M2 Pro, 16 GB。
- Asymptotic table:
  - Native prover total `G-ops: O(n)`, `F-ops: O(n)`, hash `O(n/m)`。
  - Per-node recursive cost roughly depends on `k`, degree `d`, and node circuits。
  - Prover memory `O(k(m+k) log_k(n/m))`。
  - Verifier work `O(m+k)` field operations plus constant group operations。
  - Proof size `O(m+k)` field elements plus constant group elements after optimization.
- Concrete estimates:
  - Instance size `2^24`, `k = 4`: proving time about 2 minutes, peak memory 390 MB.
  - Same `2^24` comparison: Spartan about 10 minutes; Gemini about 19 minutes with logarithmic passes.
  - Instance size `2^32`: Mangrove about 8 hours with 800 MB; Gemini over 80 hours; monolithic Spartan memory becomes prohibitive and running time not reported.
  - Proof size for evaluated configurations: about 34 MB before compression; wrapping/compressing with Spartan reduces to about 12 KB, with compression under one minute.
- Parameter sensitivity:
  - Larger `m` reduces number of leaves/PCD nodes and improves time, but increases memory.
  - Larger `k` reduces PCD nodes but increases memory because parent proving stores children.
- 证据锚点: §6.4, Fig. 7-11。

### Extensions: lookups and commit-and-prove

- Lookups: Section 7.1 extends Plonkish arithmetization with lookup tables using Habock-style logarithmic derivative argument. Lookup summations can be chunked using the memory parameter; leaf relation adds constraints for `L'`, `R'`, multiplicity vector `mul`, table chunks, and partial summation `p'`。Asymptotic prover efficiency remains the same, but very large lookup tables may need sublinear lookup protocols.
- Commit-and-prove: Section 7.2 shows Mangrove's witness chunk commitments can be pulled into the statement, enabling committed witness subdomains to be reused across proofs. Boundary: committed witness subdomains must align with PCD subtrees; very uneven sizes can unbalance the tree and reduce parallelism.
- 证据锚点: §7.1-§7.2。

### 作者结论与我的判断

- 作者明确声称:
  - Mangrove gives folding-based SNARKs with constant-size transparent CRS, low prover memory, two passes over data, and high parallelizability.
  - For `2^24` and `2^32` gate estimates, Mangrove has much lower memory and better time than the cited streaming/monolithic baselines.
  - Decoupling PCD and commit-and-fold reduce recursive overhead materially.
- 由证据支持的判断:
  - Mangrove 应归入 `memory-efficient-snarks`，并桥接到 `folding-schemes`；它不是 proof aggregation source，也不是 distributed proof generation source。
  - `commit-and-fold` 是 folding schemes 向 modular/commit-and-prove SNARK 方向迁移的一个重要模式，但仍以 Mangrove source extension 处理。
  - `memory-efficient-snarks` 通过 Mangrove 已具备独立问题节点的价值，因为它组织 prover memory/pass/parallelism tradeoff，未来能承接 Gemini、DARK、streaming commitments、Nova-UC、other low-memory SNARKs。
- 仍需谨慎的推断:
  - 性能数字是估计和合成电路 benchmark，不是完整生产实现。
  - Field/hash/commitment instantiation 和 heuristic standard-model step 需要后续 source 校准。
  - 不能从 Mangrove 推断所有 folding-based SNARKs 都 zero-knowledge 或 production-ready。

## 层级候选分类

- L1 Domain candidate: `zero-knowledge-proofs`
- L2 Direction candidate: primary `proof-systems`; secondary `recursion-and-folding`
- L3 Topic/content cluster candidates: `memory-efficient-snarks`, `folding-schemes`, `commit-and-prove-snarks`, `plonkish-arithmetization`
- Ontology path: `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`
- 备选归属:
  - `zero-knowledge-proofs/recursion-and-folding/folding-schemes` as method dependency and bridge endpoint.
  - `zero-knowledge-proofs/proof-systems/modular-zksnarks` as commit-and-prove extension, not primary.
- 父级领域: Zero-knowledge proofs
- 学术子领域: SNARK proof systems, folding-based proof systems
- 任务/问题: low-memory and streaming SNARK proving for large NP statements
- 方法族: uniform compiler, PCD, folding schemes over polynomial relations, commit-and-fold
- 模型/协议/算法族: Plonkish arithmetization, PCD tree, polynomial opening relations
- 评测场景: large Plonkish instances, proof size compression, prover memory/time estimates
- Benchmark/应用: `2^24` and `2^32` gate estimates; Spartan/Gemini comparisons
- 别名: Mangrove, folding-based SNARKs, streaming SNARKs, memory-efficient SNARKs
- 相邻方向: distributed proof generation, SNARK proof aggregation, modular zkSNARKs
- 置信度: high
- 分类理由: title/abstract/§1 explicitly frame scalable folding-based SNARKs; §6.4 evaluates prover memory/time/proof size; folding is method, memory-efficient SNARK construction is problem.
- 分类状态: corrected_from_queue
- 分类证据: Abstract; §1; §2; §5; §6.4; §7.
- Taxonomy version: 1.0

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `zero-knowledge-proofs` | SNARKs, folding schemes, proof systems throughout | high | durable parent |
| Research background | prover memory/time bottleneck in monolithic SNARKs | §1 and §6.4 compare monolithic/streaming systems | high | knowledge background |
| Research problem | memory-efficient / streaming SNARK proving | abstract says low memory, two passes, constant CRS; §6.4 evaluates memory | high | create `memory-efficient-snarks` node |
| Foundation concepts | zk-SNARKs, Plonkish arithmetization, folding schemes, PCD, polynomial commitments | §3-§6 | high | existing nodes plus foundation gaps |
| Method family | uniform compiler + folding-based PCD + commit-and-fold | §2-§5 | high | source extension and bridge |
| Application/evaluation context | large Plonkish instances and low-memory prover estimates | §6.4 | high | evaluation section/source-only details |
| Artifact/source instance | Mangrove | title/abstract | high | source extension, not knowledge node |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`
- 它能帮助未来哪些问题少读 source notes:
  - “低内存 SNARK 有哪些路线?”
  - “Mangrove 和 Gemini/Spartan/Nova-UC 的关系是什么?”
  - “folding schemes 除了 IVC/aggregation 还能做什么?”
  - “commit-and-fold 是什么，为什么能减少 PCD overhead?”
- 哪些内容应留在 source note，而不是创建上层节点:
  - Protocol 2 transcript details, exact `q_j` equations, Theorem proof steps, concrete circuit constraint counts, appendix extractor construction, single-paper performance estimates.
- 哪些上层节点过薄、缺失或需要 foundation_pack:
  - `Plonkish arithmetization`, `Proof-carrying data`, `streaming SNARKs/Gemini`, `Spartan`, `DARK`, `Protostar/ProtoGalaxy` primary sources.
- 哪些候选只是别名/query key/watch term:
  - `Mangrove-Basic`, `Mangrove-Tree`, `Nova-UC`, `commit-and-fold`, `uniformizing compiler`.

## 一句话贡献

Mangrove 把 Plonkish NP statement 编译成 uniform chunks，并用 decoupled PCD 与 commit-and-fold 构造低内存、两遍、可并行的 folding-based SNARK，从而把 folding 从 IVC/proof aggregation 扩展到 memory-efficient SNARK construction。

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Mangrove 目标是 low-memory folding-based SNARK，不是 proof aggregation | classification | Abstract, §1, §6 | 论文讨论 generic NP/SNARK construction 和 prover memory/time | high | 主路径纠正 |
| Uniform compiler uses Plonkish chunking and two passes | mechanism | §2.1, §6.1-§6.3 | chunked gate/copy checks, Merkle commitments, PCD over chunks | high | source-specific detail |
| Decoupling reduces control overhead from all nodes to internal PCD nodes | contribution | §2.3, Fig. 4-5 | `T + (T-1)/(k-1)` to `(T-1)/(k-1)` intuition | high | exact overhead depends on instantiation |
| Commit-and-fold avoids encoding expensive opening constraints | contribution | §2.3, §4, §5 | folding over committed values via linear maps | high | important bridge pattern |
| The final SNARK proof size can be `O(m + k log_k(n/m))` | theory | Theorem 5 | succinctness argument | high | constant only when `m = O_lambda(1)` |
| For `2^24`, estimate is about 2 min and 390 MB | evaluation | §6.4, Fig. 9-10 | compared with Spartan/Gemini estimates | medium | not full production implementation |
| For `2^32`, estimate is about 8 hours and 800 MB | evaluation | §6.4 | compared with Gemini over 80 hours | medium | estimate |
| Proof size is about 34 MB before wrapping and 12 KB after Spartan compression | evaluation | §6.4, Fig. 11 | compression under one minute | medium | parameter-dependent |
| Lookup and CP-SNARK extensions are sketched | extension | §7 | lookup chunking and witness commitment reuse | medium | details not experimentally evaluated |

## 知识交接

- 留在本文元笔记的证据: exact protocol definitions, theorem proof sketches, parameter equations, performance figures, lookup/CP extension details.
- 待更新 Knowledge node:
  - [[memory-efficient-snarks|Memory-efficient SNARKs]]
  - [[folding-schemes|Folding schemes]]
  - [[recursion-and-folding|Recursion and folding]]
  - [[proof-systems|Proof systems]]
  - [[zk-snarks|zk-SNARKs]]
  - [[modular-zksnarks|Modular zkSNARKs]]
- 作为哪些 Knowledge node 的 source extension:
  - `memory-efficient-snarks`: representative source and split-trigger.
  - `folding-schemes`: commit-and-fold/folding polynomial relations source extension.
  - `modular-zksnarks`: commit-and-prove witness reuse extension.
- 需要补的 foundation knowledge/source:
  - Plonk/Plonkish arithmetization, Proof-Carrying Data, Gemini, Spartan, DARK, Protostar/ProtoGalaxy, HyperNova/SuperNova.
- 待新增或复核 domain/direction/problem:
  - Create `memory-efficient-snarks` as active seed.
  - Keep Mangrove out of `snark-proof-aggregation` and `distributed-proof-generation`.
- Bridge 候选:
  - [[folding-schemes-to-memory-efficient-snarks|Folding schemes -> memory-efficient SNARKs]]
- Watchlist 词条:
  - streaming SNARKs, folding-based SNARKs, commit-and-fold, polynomial relation folding, Nova-UC, Mangrove-Tree.
- 后续论文:
  - Gemini, Spartan, DARK, Protostar/ProtoGalaxy, HyperNova/SuperNova, Proof-carrying data without succinct arguments.
- 后续仓库:
  - Nova implementation reference if repository analysis is requested.
- Review queue:
  - Verify canonical URL/ePrint identifier for filename `2024-416.pdf`.
  - Validate whether later sources treat Mangrove as proof aggregation or memory-efficient SNARK; current deep read supports memory-efficient SNARK.

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Memory-efficient SNARKs | foundation_thin problem node | 建 `04_Knowledge/.../memory-efficient-snarks.md`，解释 prover memory/pass/parallelism 问题和路线 | 把 Mangrove 本身当上层概念 | Abstract, §1, §6.4 |
| Folding schemes | existing method-family/problem | 作为方法依赖和 bridge endpoint，补 commit-and-fold source extension | 把本文完全归入 folding-schemes，忽略 proof-system problem | §4-§5 |
| Proof-Carrying Data | foundation_gap/method dependency | 记录为缺口/后续 source，不从 Mangrove 一篇展开完整 foundation | 让 Mangrove 的 PCD section 代表整个 PCD 概念 | §3, §6 |
| Mangrove | representative_instance_or_source_extension | 留在 source note，作为 memory-efficient SNARKs 的代表来源 | 建一个 source-shaped Mangrove 概念页 | title/abstract |
| Commit-and-fold | source-backed method pattern | 作为 folding schemes/modular SNARKs 的 route/source extension | 直接建宽泛 foundation node | §2.3, §4-§5 |

## Knowledge 综合交接

- 应创建 Knowledge node: `zero-knowledge-proofs/proof-systems/memory-efficient-snarks`
- 应刷新 Knowledge synthesis section: `proof-systems`, `zk-snarks`, `folding-schemes`, `recursion-and-folding`, `modular-zksnarks`, ZKP domain seed sections.
- 应标记过期: none; domain dynamics remains stale because no web/daily freshness was fetched.
- 无需更新的理由:
  - `snark-proof-aggregation`: update only to remove/avoid Mangrove as aggregation source.
  - `distributed-proof-generation`: Mangrove is parallelizable, but not a multi-machine distributed proving protocol; no durable update needed beyond possible adjacent mention.
- 建议 node kind: `problem` / `method_family`, status `foundation_thin`, maturity `active_seed`.

## 处理日志

- 2026-06-20: full extracted text read from `vault/02_Raw/pdf/extracted/2024-416-d6c935fe1d1a-pages.txt`.
- 2026-06-20: queue classification corrected from `recursion-and-folding/folding-schemes` to `proof-systems/memory-efficient-snarks`.
- 2026-06-20: source note prepared for absorption with `safe_for_absorption: true`.
