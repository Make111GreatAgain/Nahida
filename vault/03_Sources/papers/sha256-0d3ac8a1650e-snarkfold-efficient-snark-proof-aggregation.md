---
id: "sha256-0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
title: "SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation"
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
  - "p1-p4 abstract, introduction, motivation, related proof aggregation routes and contributions"
  - "p5-p7 preliminaries for SNARKs, proof aggregation, IVC, folding schemes and Groth16"
  - "p7-p11 split IVC technique overview, circuits, construction and theorem"
  - "p11-p15 SnarkFold construction from split IVC and soundness theorem"
  - "p16-p19 Groth16 folding relation, augmented relaxed Groth16 relation, evaluation complexity and conclusion"
  - "p20-p29 references and appendices for formal definitions, Groth16 details and proofs"
safe_for_absorption: true
canonical_url: "unknown"
doi: "unknown"
arxiv_id: "unknown"
venue: "unknown"
year: "2023"
pdf_pages: 29
pdf_sha256: "0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
local_pdf: "~/Desktop/paper/1946 (1).pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/1946-1-0d3ac8a1650e-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "recursion-and-folding"
topic_ids:
  - "snark-proof-aggregation"
  - "folding-schemes"
  - "zk-snarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
  - "snark-proof-aggregation"
primary_ontology_path: "zero-knowledge-proofs/recursion-and-folding/snark-proof-aggregation/sha256-0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
secondary_ontology_paths:
  - "zero-knowledge-proofs/recursion-and-folding/folding-schemes/sha256-0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "zero-knowledge-proofs/proof-systems/zk-snarks/sha256-0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "recursion-and-folding"
    - "proof-systems"
  topics:
    - "snark-proof-aggregation"
    - "folding-schemes"
    - "incrementally-verifiable-computation"
    - "Groth16"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "SNARK proof aggregation"
  - "split IVC"
  - "incrementally verifiable computation"
  - "folding schemes"
  - "Groth16"
  - "relaxed Groth16"
  - "augmented relaxed Groth16"
  - "GIPA"
  - "SnarkPack"
aliases:
  - "SnarkFold"
  - "split IVC"
  - "SNARK proof aggregation"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "recursion-and-folding"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "recursion-and-folding"
    - "proof-systems"
  problem:
    - "multiple SNARK proofs are expensive to verify independently"
    - "proof aggregation needs smaller proof size and verifier cost than checking all proofs"
    - "recursive circuits cannot cheaply encode pairing-heavy verification relations"
  method_family:
    - "proof aggregation"
    - "split incrementally verifiable computation"
    - "folding schemes"
    - "augmented relaxed Groth16 folding"
    - "Fiat-Shamir non-interactive folding"
  system_layer:
    - "aggregation prover"
    - "aggregation verifier"
    - "recursive circuit"
    - "Groth16 verifier"
  evaluation_context:
    - "communication and operation-count comparison with TIPP-based aggregation"
    - "Groth16 proof aggregation"
    - "blockchain verifier cost motivation"
  application:
    - "zkRollups"
    - "zkEVM"
    - "anonymous cryptocurrencies"
    - "blockchain transaction fee reduction"
  bridge:
    - "folding schemes to SNARK proof aggregation"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-snarkfold"
source_refs:
  - "sha256:0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04"
  - "pdf:~/Desktop/paper/1946 (1).pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "zero-knowledge-proofs -> recursion-and-folding"
secondary_directions:
  - "zero-knowledge-proofs -> proof-systems"
  - "verifiable-computation -> proof aggregation"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "Title and abstract identify SNARK proof aggregation from split IVC"
  - "Sections 4-5 formalize split IVC and SnarkFold"
  - "Section 6 compares proof size, proving cost and verification cost for Groth16 aggregation"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0026"
queue_status: "absorbed"
---

# SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation

## 论文身份

- 标题: SnarkFold: Efficient SNARK Proof Aggregation from Split Incrementally Verifiable Computation
- 作者: Xun Liu, Shang Gao, Tianyu Zheng, Bin Xiao
- 机构: Department of Computing, The Hong Kong Polytechnic University
- 年份/Venue: 2023 / unknown
- DOI: unknown
- arXiv: unknown
- 本地 PDF: `~/Desktop/paper/1946 (1).pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/1946-1-0d3ac8a1650e-pages.txt`
- SHA-256: `0d3ac8a1650e6a0b2debbefa1141c201beac1fe4a197ab5d98ba3882d6460f04`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 29
- 已覆盖章节/页码: Abstract, Introduction, Related Work, Preliminaries, Split IVC, SnarkFold, Groth16 folding, Evaluation, Conclusion, appendices
- Extraction gaps: PDF metadata 只包含 TeX 生成信息，未提供 DOI/Venue；未联网补元数据，按 `unknown` 记录。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, §1 / p1-p4 | 问题与贡献 | 多 SNARK proofs 独立验证昂贵；SnarkFold 用 split IVC 做常数 proof size 与常数 verification cost | high |
| §2 / p4-p5 | 相关工作 | accumulator-based aggregation、GIPA/TIPP、SnarkPack、IVC/folding routes | high |
| §3 / p5-p7 | 预备知识 | SNARK/proof aggregation/IVC/folding/Groth16 接口与性质 | high |
| §4 / p7-p11 | Split IVC | 两类 running instances、F-friendly/Fold-friendly 分离、hash claim、完整构造和 Theorem 1 | high |
| §5 / p11-p15 | SnarkFold | 用 split IVC 折叠 SNARK instance-proof pairs，最终聚合证明压缩为一个 SNARK' proof，Theorem 2 | high |
| §5.2 / p16-p18 | Groth16 folding | relaxed Groth16、augmented relaxed Groth16、deferred pairings、Fiat-Shamir folding，Theorem 3 | high |
| §6-§7 / p18-p19 | 复杂度评估与结论 | 与 TIPP-based 方案比较；SnarkFold 常数大小证明与常数验证时间；无实测 wall-clock benchmark | high |
| Appendices / p22-p29 | 形式定义与证明 | SNARK、proof aggregation、IVC、folding definitions；Groth16 QAP details；Theorem 1/3 proofs | medium-high |

## 一句话贡献

SnarkFold 把“验证多个 SNARK proofs”改写为 folding/IVC aggregation 问题，并提出 split IVC: 在递归电路里同时维护 F-friendly 与 Fold-friendly running instances，避免把 pairing-heavy Groth16 verification 硬转成同一种电路关系，从而让聚合证明达到常数 proof size 和常数 verification cost。

## 核心精读笔记

### 问题设定: 多个 SNARK proofs 独立验证会把 verifier 端成本线性放大

论文从区块链场景引入问题: zkRollups、zkEVM、anonymous cryptocurrencies 等应用大量使用 SNARK，但如果每个 proof 都独立验证，节点负载和用户交易费都会上升。作者举例说，2023 年 12 月 TornadoCash deposit 操作在 Ethereum 上需要约 80 USD 交易费，用来说明 proof verification 的链上成本压力。

Proof aggregation 的目标是把 `(u_i, pi_i)` 多个 instance-proof pairs 聚合成一个 `(u, pi)` 和一个 aggregation proof `pi_AGG`。`pi_AGG` 证明聚合过程正确；真实 verifier 还需要验证最终 `(u, pi)`，由两者合起来推出所有输入 proofs 有效。

### 相关工作边界: GIPA/SnarkPack 是对数级，SnarkFold 追求常数级

论文把既有路线分成几类:

- accumulator-based membership/non-membership proof aggregation: 可以达到常数 proof size/verifier time，但只适合特定 accumulator 关系，不适合一般 Groth16/Plonk proofs。
- GIPA/TIPP/SnarkPack: 把 Groth16 verification 转成 generalized inner product，再用 Bulletproofs-like compression 和 KZG commitment，把 proof size 和 verification cost 降到 `O(log n)`；但 pairing-based operations 仍然昂贵。
- IVC/folding: 适合 repeated computation，proof size 不随 iteration 增长；但传统 IVC/folding 要求新 proof/instance 与 running instance 进入同一种关系结构，导致昂贵转换。

SnarkFold 的定位是把 folding 当作 aggregation function，同时避免直接把 pairing verification relation 转进 relaxed R1CS 或类似结构。

### Split IVC: 两类 running instances 避免昂贵 relation transformation

传统 folding-based IVC 在每轮把前一轮 running instance 与当前 accumulated instance 折叠到同一种 relation。问题在于: 如果函数 `F` 包含 pairing 等 algebraic relation，把它转换成 relaxed R1CS 会非常贵。论文引用 `zkpairing` 说明单个 pairing operation 可达约 2500 万 gates，编译时间可到 4.2 小时。

Split IVC 的核心变化:

- 维护 `F-friendly` running instance `u*_F,i`，直接表示 `F` 的正确执行。
- 维护 `Fold-friendly` running instance `u*_Fold,i`，表示 folding circuit 自己的正确执行。
- `Fold-circuit` 同时检查 `FoldF.V(vk_F, u_F,i, u*_F,i-1)` 和 `Fold.V(vk_Fold, u_Fold,i-1, u*_Fold,i-1)`，然后只输出一个 hash claim `u_Fold,i.h`。
- hash claim 解决了输出结构不一致的问题: 不把 `u*_F,i` 和 `u*_Fold,i` 直接作为下一轮可折叠 instance 的结构字段，而是用 `Hash(vk, i, z0, z_i, u*_F,i, u*_Fold,i)` 绑定。

这样，若 `F` 是 pairing relation，可以用 algebraic group elements 表示 F-friendly instance，folding 只需要 group operations；递归电路不用实现完整 pairing relation。

论文还指出，多 running instances 的思路可推广到多个实例类型: 一个 circuit instance 证明 hash/Fiat-Shamir，另一个 algebraic instance 证明 commitments 被正确折叠。这可能优化 Nova、HyperNova、ProtoStar、KiloNova 等 commitment-based folding schemes。

### Split IVC 构造与安全性质

Split IVC proof 在第 `i` 步包含三类 instance-witness pairs:

- `(u*_F,i, w*_F,i)`: F-friendly running instance/witness。
- `(u_Fold,i, w_Fold,i)`: 本轮 Fold-circuit 的非 relaxed claim。
- `(u*_Fold,i, w*_Fold,i)`: Fold-friendly running instance/witness。

`IVC.V` 检查 hash binding、三个 witness 的 satisfiability，以及 `u_Fold,i` 是 non-relaxed instance。Theorem 1 给出: 若 `FoldF` 与 `Fold` 满足 perfect completeness 和 knowledge soundness，则 split IVC 满足 perfect completeness、knowledge soundness 和 succinctness。Appendix C.2 用 recursive extraction 证明 soundness。

### SnarkFold: 把 SNARK proof 作为 split IVC 中的 F-friendly witness

SnarkFold 把每个 SNARK instance-proof pair `(u_i, pi_i)` 看作 split IVC 中的 F-friendly instance/witness pair，其中 `pi_i` 是 secret witness。每轮使用 `FoldSNARK` 把新的 `(u_i, pi_i)` 与前一轮 aggregated pair `(u*_{i-1}, pi*_{i-1})` 折叠成 `(u*_i, pi*_i)`。

为了避免 aggregation proof 本身太大，最终还会:

1. 把 `u_Fold,n` 和 `u*_Fold,n` 再折叠成 `u'`。
2. 用 `SNARK'` 对 Fold-circuit 的 witness `w'` 生成 proof `pi'`。
3. 输出 `pi_AGG = (u_Fold,n, u*_Fold,n, pi')`。

Verifier 做三件事:

- 检查 `u_Fold,n.h = Hash(vk_IVC, n, u, u*_Fold,n)`。
- 本地运行 `Fold.V` 得到 `u'`。
- 验证 `SNARK'.V(vk_SNARK', u', pi') = 1`，并检查 `u_Fold,n` 是 non-relaxed instance。

论文强调，aggregation verifier 只验证 aggregation process；真实应用仍需进一步验证最终 aggregated `(u, pi)`。

### Groth16 folding: relaxed 与 augmented relaxed relation

Groth16 proof 是 `(A, B, C)`，verification relation 含 pairing equation。直接随机线性组合 `A* = A1 * A2^r` 等会产生 cross-terms，导致 folded verification equation 不成立。

论文先定义 relaxed Groth16 proof relation，给 instance 加入:

- `mu`: 吸收额外因子。
- `H`: public input 部分对应的 group element。
- `E`: 吸收 folding 产生的 cross-term。

传统 non-relaxed Groth16 可以看作 `E = [0]_T`、`mu = 1` 的特例。但这个 first attempt 每轮需要为 cross-item `T` 计算四个 pairings。

为降低 prover local pairing cost，论文进一步定义 augmented relaxed Groth16 proof relation，把 `R`、`S`、`kappa` 加进 instance，让部分 pairing work 延迟到最终步骤。这样折叠 `n` 个 proofs 的 pairing 数从 `4n` 降到 `2n + 2`。Theorem 3 在 random oracle model 下，通过 interactive protocol 的 forking lemma 和 Fiat-Shamir transform 给出 knowledge soundness。

### 复杂度评估

论文提供的是 operation-count/complexity comparison，不是实测运行时间。表 1 中 SnarkFold 对 Groth16 aggregation 的聚合证明大小为:

- `6G1, 1G2, 4Zp`

也就是常数大小；相比 TIPP-based/GIPA 路线的 proof size `6G1, 6G2, 12 log n GT`，不会随 `n` 增长。

SnarkFold verifier local work 为:

- `3P, 3H, 2G1, 1RO`

其中 `P` 是 pairing，`H` 是 hash，`RO` 是 random oracle query；recursive-circuit verification cost 为空。TIPP-based 路线仍有 `16P, n*l G1, 12 log n GT` 类验证开销。Prover 端仍随 `n` 增长，包括 `2nP`、若干 group exponentiations/hash/random-oracle work 和 Fold-circuit witness/circuit computation。

### 限制与开放问题

- 论文没有给出工程实现 wall-clock benchmark、gas benchmark 或开源实现验证；§6 是理论/操作计数比较。
- Groth16 aggregation 构造依赖对 Groth16 verification relation 的专门 relaxed/augmented relaxed 设计；不直接等于任意 SNARK 系统可无成本适配。
- 证明使用 Fiat-Shamir/random oracle model；具体 hash/RO instantiation、trusted setup、curve/precompile 成本需要应用环境评估。
- SnarkFold 解决 aggregation proof 的 verifier cost/proof size，但最终 `(u, pi)` 的验证仍是应用 verifier 的责任。
- 要形成完整 proof aggregation 版图，还需要吸收 SnarkPack/TIPP primary sources、Hekaton、Mangrove 等后续 aggregation sources。Pianist 已在后续深读中归入 distributed proof generation，不作为 proof aggregation source。

## 可复用知识与来源内边界

### 可上升为 knowledge/source-extension 的内容

- SNARK proof aggregation: 多个 SNARK proofs 合并成低 verifier cost 聚合对象的问题。
- Split IVC: 用不同类型 running instances 避免昂贵 relation transformation 的 folding/IVC route。
- Folding as aggregation: 把每个 input proof 当作 folding input，最终用 IVC 保持 proof size/verifier cost 不随 iteration 增长。
- Augmented relaxed Groth16: 为 Groth16 proof aggregation 设计的 source-backed specialized relation。

### 不应上升为独立基础概念的内容

- `SnarkFold` 是 source/system instance，不是上层概念节点。
- `augmented relaxed Groth16 proof relation` 当前是本文技术构造，先作为 source detail 和 method route，不单独建 foundation node。
- `TornadoCash $80 fee`、`25 million gates`、`4.2 hours compile` 是本文动机/引用性证据，不能泛化为当前链上成本结论。
- §6 的 operation-count comparison 是理论/模型层证据，不是生产性能 benchmark。

## 分层吸收映射

| Knowledge/Bridge target | 更新方式 | 吸收内容 | Source boundary |
| --- | --- | --- | --- |
| [[snark-proof-aggregation|SNARK proof aggregation]] | new problem node | 多 SNARK proofs 聚合问题、GIPA/SnarkPack vs IVC/folding 路线、split IVC 和 Groth16 relation specialization | 不复制完整构造/公式 |
| [[folding-schemes|Folding schemes]] | source extension | split IVC 作为 folding/IVC 的 multi-instance route | SnarkFold 不是 folding scheme foundation |
| [[recursion-and-folding|Recursion and folding]] | child + source extension | 新增 SNARK proof aggregation child problem 与 recursive/folding application | 不把所有 proof aggregation 放进 Nova |
| [[zk-snarks|zk-SNARKs]] | dependency/source extension | 聚合验证多个 SNARK proofs 的 verifier-cost problem | 不升级 zk-SNARK foundation status |
| [[folding-schemes-to-snark-proof-aggregation|Folding schemes -> SNARK proof aggregation]] | new bridge | folding/IVC 如何转化为 proof aggregation 方法，以及不迁移的边界 | Groth16-specific relaxed relation 不自动迁移到其他 SNARKs |

## 关键术语表

| Term | 本文含义 | 上层去向 |
| --- | --- | --- |
| proof aggregation | 将多个 proofs 合成一个 aggregated proof-instance pair 与 aggregation proof | [[snark-proof-aggregation|SNARK proof aggregation]] |
| split IVC | 用 F-friendly 与 Fold-friendly running instances 分离 relation 类型的 IVC 构造 | [[folding-schemes|Folding schemes]] source extension |
| Fold-circuit | 检查两类 folding 更新并输出 hash claim 的递归电路 | source detail |
| FoldSNARK | 用于折叠 SNARK instance-proof pairs 的 folding scheme | source detail |
| relaxed Groth16 | 为 folding cross-terms 增加 `mu/H/E` 的 Groth16 relation variant | source detail |
| augmented relaxed Groth16 | 进一步加入 `R/S/kappa` 以延迟 pairings 的 Groth16 relation variant | source detail |
| TIPP/GIPA/SnarkPack | 既有对数级 proof aggregation route | [[snark-proof-aggregation|SNARK proof aggregation]] comparison route |

## 关系与链接

- Primary: [[snark-proof-aggregation|SNARK proof aggregation]]
- Parent: [[recursion-and-folding|Recursion and folding]] -> [[zero-knowledge-proofs|Zero-knowledge proofs]]
- Method dependency: [[folding-schemes|Folding schemes]]
- Proof-system dependency: [[zk-snarks|zk-SNARKs]]
- Bridge: [[folding-schemes-to-snark-proof-aggregation|Folding schemes -> SNARK proof aggregation]]
- Nearby sources: [[eprint-2021-370-nova-recursive-zero-knowledge-arguments-from-folding-schemes|Nova: Recursive Zero-Knowledge Arguments from Folding Schemes]], [[sha256-fbf50bc93d96-zkbridge-trustless-cross-chain-bridges|zkBridge: Trustless Cross-chain Bridges Made Practical]]

## 质量复核

- 完整性: 覆盖 problem, related work, preliminaries, split IVC construction, SnarkFold construction, Groth16 folding, complexity comparison, appendices proofs。
- 分层性: source note 保留公式、algorithm interfaces、operation counts；knowledge node 只吸收 proof aggregation 问题与方法族。
- 概念边界: SnarkFold 不拆成 concept；split IVC 暂作为 folding-schemes route；SNARK proof aggregation 拆成问题节点，因为它能承接 SnarkPack/Hekaton 等后续 aggregation sources。Pianist 这种 distributed proving source 另走 [[distributed-proof-generation|Distributed proof generation]]；Mangrove 已纠偏为 [[memory-efficient-snarks|Memory-efficient SNARKs]] source。
- 风险: DOI/Venue unknown；没有联网补元数据；性能证据不是 wall-clock benchmark。
