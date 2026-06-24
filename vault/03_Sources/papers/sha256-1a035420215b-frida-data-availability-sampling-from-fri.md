---
id: "sha256-1a035420215b"
title: "FRIDA: Data Availability Sampling from FRI"
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
  - "p1-p5 title, abstract, introduction, contributions, related work, and technical overview"
  - "p6-p9 preliminaries: erasure code commitments, position/code binding, IOPP syntax, query selection"
  - "p9-p16 compiler from opening-consistent IOPPs to erasure-code commitments and DAS"
  - "p17-p25 FRI construction, blockwise distance, correlated agreement, opening-consistency proof, batched FRI"
  - "p25-p28 asymptotic and concrete efficiency evaluation"
  - "p29-p46 references and appendices A-D: DAS background, Merkle extraction, batched FRI, parameter scripts"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "CRYPTO 2024 full version"
year: "2024"
pdf_pages: 46
pdf_sha256: "1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
local_pdf: "~/Desktop/paper/2024-248.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/frida-data-availability-sampling-from-fri-1a035420215b-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-availability-and-light-clients"
topic_ids:
  - "data-availability-sampling"
  - "fri-iopps"
  - "erasure-code-commitments"
ontology_path:
  - "blockchain-systems"
  - "data-availability-and-light-clients"
  - "data-availability-sampling"
primary_ontology_path: "blockchain-systems/data-availability-and-light-clients/data-availability-sampling/sha256-1a035420215b"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/fri-iopps/sha256-1a035420215b"
  - "zero-knowledge-proofs/polynomial-commitments/sha256-1a035420215b"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
    - "verifiable-computation"
  directions:
    - "data-availability-and-light-clients"
    - "proof-systems"
    - "polynomial-commitments"
  topics:
    - "data-availability-sampling"
    - "fri-iopps"
    - "erasure-code-commitments"
    - "interactive-oracle-proofs-of-proximity"
domains:
  - "blockchain-systems"
  - "zero-knowledge-proofs"
  - "verifiable-computation"
topics:
  - "data-availability-sampling"
  - "data-availability"
  - "light clients"
  - "FRI"
  - "IOPP"
  - "erasure-code-commitments"
  - "Reed-Solomon codes"
  - "Merkle commitments"
aliases:
  - "FRIDA"
  - "FRI-based DAS"
  - "Data Availability Sampling from FRI"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-availability"
  - "zero-knowledge-proofs"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "zero-knowledge-proofs"
  subdomain:
    - "data-availability-and-light-clients"
    - "proof-systems"
  problem:
    - "light clients need assurance that block contents are recoverable without downloading them"
    - "DAS constructions without trusted setup had square-root-size light-client overhead"
    - "IOPP proximity alone does not guarantee code-binding openings"
  method_family:
    - "data availability sampling"
    - "erasure code commitments"
    - "FRI interactive oracle proofs of proximity"
    - "batched FRI"
  system_layer:
    - "block header commitment"
    - "encoded data stored by network"
    - "light-client random sampling"
    - "Merkle-authenticated oracle openings"
  evaluation_context:
    - "asymptotic comparison"
    - "1 MB, 32 MB, 128 MB concrete tables"
    - "40-bit statistical reconstruction target"
    - "128-bit field"
  bridge:
    - "FRI IOPPs -> data availability sampling"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260620-frida-data-availability-from-fri"
source_refs:
  - "sha256:1a035420215b61a7bc4811911939b80755c5ef9b3390e1375980f27d893d2425"
  - "pdf:~/Desktop/paper/2024-248.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> data-availability-and-light-clients"
secondary_directions:
  - "zero-knowledge-proofs -> proof-systems"
  - "zero-knowledge-proofs -> polynomial-commitments"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "PDF title page and abstract"
  - "Sections 1-5 and Appendices A-D"
  - "local PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0037"
queue_status: "absorbed"
---

# FRIDA: Data Availability Sampling from FRI

## 论文身份

- 标题: FRIDA: Data Availability Sampling from FRI
- 作者: Mathias Hall-Andersen, Mark Simkin, Benedikt Wagner
- 机构: ZkSecurity; Ethereum Foundation
- 会议/期刊: full version of an article to appear in CRYPTO 2024
- 日期: June 6, 2024
- 年份: 2024
- DOI: unknown in PDF
- arXiv/ePrint: unknown in PDF; local filename is `2024-248.pdf`
- 链接: unknown in PDF
- 本地 PDF: `~/Desktop/paper/2024-248.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/frida-data-availability-sampling-from-fri-1a035420215b-pages.txt`
- 代码: Appendix D contains parameter-computation scripts; no public repository URL in PDF
- 数据: synthetic parameter/evaluation data generated by scripts in Appendix D
- License: IACR 2024 copyright notice in PDF

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 46
- 已覆盖章节/页码: p1-p46 full text, including appendices and scripts
- 已检查附录: Appendix A DAS background, Appendix B Merkle trees, Appendix C batched FRI, Appendix D parameter scripts
- 未覆盖章节/页码: 无
- Extraction gaps: 公式与代码列表有断词/空格噪声，但 theorem names、asymptotic table、concrete table、definitions 和 proof structure 可读。
- 精读说明: FRIDA 是 DAS + proof-system bridge source。吸收时不要把 FRIDA 当成新的区块链执行协议；它解决的是 light-client data availability assurance 的 commitment/opening route。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Title/Abstract / p1 | 身份与贡献 | 无 trusted setup、polylog overhead 的 FRI-based DAS；IOPP -> erasure code commitment -> DAS | 贡献定位 | keywords: DAS, IOPP, FRI, commitments, Reed-Solomon codes |
| §1 / p3-p5 | 动机、相关工作、技术概览 | light clients 只下载 headers 但需要数据可恢复；已有方案要么贵、要么 trusted setup、要么 sqrt overhead | 问题边界 | 明确不解决 full chain validity |
| §2 / p6-p9 | preliminaries | erasure code commitments、position-binding、code-binding、IOPP、query-selectable IOPP | 定义基础 | 引用 HASW23 DAS compiler |
| §3 / p9-p16 | IOPP 到 DAS | opening-consistency 定义；Merkle/Fiat-Shamir style compiler；Theorem 2 code-binding | 抽象贡献 | 这是最可复用的理论层 |
| §4.1-§4.2 / p17-p25 | FRI 实例化与证明 | Reed-Solomon/FRI folding；blockwise distance；lucky/bad sets；FRI opening-consistency | 技术核心 | Theorem 3 gives FRI opening-consistency |
| §4.3 / p25 | batched FRI | interleaved RS code、random linear combination、batched opening-consistency | 工程优化 | 降低 encoding size |
| §5 / p25-p28 | efficiency evaluation | asymptotic and concrete comparisons with Naive/Merkle/Tensor/Hash | trade-off 证据 | FRIDA improves commitment/query sizes but increases network encoding |
| Appendix A / p32-p33 | DAS background | formal DAS syntax and erasure-code-commitment transformation | definition anchor | Completeness/soundness/consistency |
| Appendix B / p33-p35 | Merkle trees | Merkle root/path/extraction under random oracle | security support | used in compiler proof |
| Appendix C / p35-p40 | batched FRI proof | interleaved RS, lucky/bad sets, no-luck/bad-rejected/inconsistent-rejected | technical support | Theorem 4 |
| Appendix D / p40-p46 | scripts | parameter scripts for tables/graphs | reproducibility | no repo URL in PDF |

## 一句话贡献

FRIDA 证明满足 opening-consistency 的 IOPP 可以编译成 erasure-code commitment，再由 HASW23 的变换得到 DAS；随后证明 FRI 和 batched FRI 满足该性质，从而给 light clients 一个无需 trusted setup、承诺和单次查询开销 polylogarithmic 的数据可用性抽样路线。

## 核心精读笔记

### 问题边界: light clients 需要数据可恢复，而不是验证状态正确

论文的出发点是区块链数据持续增长，资源受限客户端不能存储整条链。轻客户端可以只下载 block headers，但如果未来需要 block contents，就要确信这些内容原则上可获得。DAS 让轻客户端通过少量随机查询判断数据是否足够可恢复，而不是下载整块。证据锚点: Abstract, §1 p3。

这个边界很重要: FRIDA 不验证交易执行正确性，也不让轻客户端变成 full validator。它保证的是某个承诺下的编码数据足够可恢复；validity、execution、fraud/validity proofs 或 rollup state transition 仍需其他机制。证据锚点: Abstract p1, Appendix A p32-p33。

### 现有 DAS 路线的痛点

论文把已有 route 分成几类。SNARK/vector-commitment 方案有大计算开销和强假设；2D Reed-Solomon + KZG/tensor route 实用但需要 trusted setup，并与 Ethereum 方向相关；hash/random-oracle route 无 trusted setup，但 commitment 或 light-client download overhead 随数据大小呈 square-root 量级。FRIDA 的目标是保留 hash/random-oracle/transparent flavor，同时把 light-client relevant overhead 降到 polylog。证据锚点: §1 p3-p4。

这里的比较不是说 FRIDA 在所有指标上胜出。§5 明确说明 Hash 的总通信和 encoding size 更好，Tensor/KZG 在某些 concrete light-client query 指标上仍很强；FRIDA 的优势集中在无 trusted setup 且 commitment/query symbol 随数据大小扩展更慢。证据锚点: §5 p25-p28。

### Erasure code commitment 是 DAS 的中间抽象

HASW23 的关键抽象是 erasure code commitment。给定 code `C: Gamma^k -> Lambda^n`，commitment 需要保证:

- position-binding: 同一位置不能被成功打开为两个不同值。
- code-binding: 已打开的任意 symbol 集合必须与某个合法 codeword 一致；达到 reception threshold 后与唯一 codeword 一致。

有了 position-binding + code-binding，就能把 code commitment 转成 DAS: `Encode(data)` 输出 codeword symbols 和每个 symbol 的 opening；轻客户端查询随机 indices 并验证 openings；收集足够 accepting transcripts 后可由 extractor 重建数据。证据锚点: §2 p6-p8, Appendix A p32-p33。

### 为什么普通 IOPP soundness 不够

IOPP 证明一个 oracle vector 接近某个 code，但 DAS 需要的是打开的 base-layer symbols 与唯一最近 codeword 一致。若初始 oracle 在 unique decoding radius 内但含有少量错误位置，prover 可能让 verifier 接受 proximity proof，却在某些位置打开与唯一 codeword 不一致的值，从而破坏 code-binding。证据锚点: §1.3 p5, §3 p9-p11。

FRIDA 为此定义 opening-consistency。它用 Lucky/Bad/suitable transcripts 分解风险，并要求四个性质:

- No Luck: 随机 challenge 落入 lucky transcript 的概率小。
- Bad is Rejected: bad transcript 被最终查询接受的概率低。
- Suitable is Close: suitable transcript 的初始 oracle 在 unique decoding radius 内。
- Inconsistent is Rejected: 若查询位置与唯一最近 codeword 不一致，verifier 必须拒绝。

这组条件比普通 round-by-round soundness 更强，正好对准 erasure-code commitment 的 code-binding 需求。证据锚点: Definition 9-10, §3 p9-p11。

### IOPP -> erasure-code commitment 的 compiler

§3 给出通用 compiler: 对 IOPP proof oracles 建 Merkle trees，用 random oracle 派生 Fiat-Shamir-like challenges，用 `QSelect` 强制 verifier 在 opening 时查询目标 index，并把多次 final query authentications 放进 commitment。opening 包含目标 symbol 和相关 Merkle authentication paths；verification 重放 challenge derivation、检查 proof transcript 和目标路径。证据锚点: §3 p11-p14。

Security 分成 position-binding 和 code-binding。position-binding 来自 Merkle collision/extractability bound。code-binding 用 Theorem 2 证明: 若 IOPP non-adaptive、query-selectable 且 opening-consistent，则 compiler 输出的 erasure code commitment 满足 code-binding，优势由 random-oracle collision/extraction 项与 `epsilon_1`、`epsilon_2^L` 控制。证据锚点: Lemma 1, Theorem 2, §3 p14-p16。

### FRI 满足 opening-consistency

FRIDA 使用 FRI IOPP for Reed-Solomon code。FRI 通过逐轮 folding 降低 degree bound: 对 `G_{i-1}: L_{i-1} -> F`，verifier 给随机 `rho_i`，prover 返回 folded oracle `G_i = H_{rho_i}[G_{i-1}]`，查询阶段沿 `s_i = q(s_{i-1})` 检查每层一致性。证据锚点: §4.1 p17-p18。

证明 opening-consistency 的核心不是重述 FRI soundness，而是构造适合 FRIDA compiler 的 Lucky 和 Bad sets。Lucky 包含两类: folded value 与 closest codeword 的碰撞，以及 distance 在 folding 后“幸运”下降。Bad 包含 final oracle 不在 code、某层 blockwise distance 太远、或者 closest-codeword folding 与 prover folding 不可交换。证据锚点: Definition 12-13, p20-p21。

证明路线依赖 blockwise distance 和 correlated agreement。Lemma 4 说明若某层 blockwise distance 超过 unique decoding radius，则随机 folding 后接近 code 的概率受 `(F-1)|L_i|/|F|` 控制。随后 Lemma 5-10 分别证明 no-luck、bad-rejected、suitable-close、inconsistent-rejected。Theorem 3 总结 FRI opening-consistency: `epsilon_1 <= 2(F-1)|L_0|/|F|`, `epsilon_2 <= 1 - delta*`。证据锚点: Lemma 2-10, Theorem 3, p18-p25。

### Batched FRI 是为了控制 encoding size

直接用 FRI 会得到小 commitment 但 encoding 很大。FRIDA 用 batched FRI / interleaved Reed-Solomon code: 将 data 分成多条多项式 `G_j`，先用随机 `xi` 做线性组合 `G_0 = sum xi^{j-1} G_j`，再对 `G_0` 跑 FRI；查询时额外检查 batch layer 与 `G_0` 的一致性。证据锚点: §4.3 p25, Appendix C p35-p40。

Appendix C 将 non-batched 的 Lucky/Bad 思路扩展到 batching step，加入 batch collision 和 batch distortion。Theorem 4 得到 batched FRI opening-consistency: `epsilon_1 <= 2(max{F,B}-1)|L_0|/|F|`, `epsilon_2 <= 1 - delta*`。证据锚点: Theorem 4, Definition 18-19, Lemma 14-17。

### 效率与取舍

§5 比较 Naive、Merkle、Hash、Tensor 和 FRIDA。以数据大小 `D` 和 security parameter `lambda` 表示，FRIDA 的 asymptotic table 给出:

| Scheme | Commitment | Encoding | Symbol / query download | Samples |
| --- | --- | --- | --- | --- |
| Hash | `lambda sqrt(D)` | `D` | `sqrt(D)` | `lambda + sqrt(D)` |
| FRIDA | `lambda^2 log^2(D)` | `D lambda log^2(D)` | `lambda log^2(D)` | `lambda + D` |

论文强调 FRIDA 在 commitment size 和单个 encoding symbol / per-query communication 上相对 Hash 有指数级 asymptotic 改进，但 sample count 和 total communication 不一定更好。证据锚点: Table 1, §5 p25-p26。

Concrete table 中，`D=32 MB` 时 Hash commitment 约 1448.45 KB、per query 约 11.32 KB、encoding 约 128.05 MB；FRIDA commitment 约 464.83 KB、per query 约 3.94 KB、encoding 约 1031.80 MB。`D=128 MB` 时 Hash per query 约 22.63 KB，FRIDA 约 4.19 KB；但 FRIDA encoding 约 4395.63 MB。证据锚点: Table 2 p27。

我的判断: FRIDA 是 light-client-bandwidth / transparent-setup 优化，而不是 network-storage 优化。对于 DA layer，若瓶颈是大量轻客户端查询与 trusted setup 风险，FRIDA 的路线有吸引力；若瓶颈是网络总存储和总恢复通信，Hash/Tensor/KZG-like routes 仍需一起比较。

## 层级候选分类

| 层级 | 候选 | 证据 | 状态 |
| --- | --- | --- | --- |
| L1 domain | `blockchain-systems` | problem is light-client block data availability in blockchains | accepted |
| L2 direction | `data-availability-and-light-clients` | abstract/introduction directly address light nodes and block contents | accepted |
| L3 topic | `data-availability-sampling` | title, abstract, §5, Appendix A | accepted |
| Secondary domain | `zero-knowledge-proofs` | FRI/IOPP, proof-system compiler, commitments | accepted as secondary |
| Candidate knowledge node | `FRI IOPPs` | FRI is a reusable proof-system family; FRIDA proves opening-consistency for FRI/batched FRI | split as foundation_thin |
| Bridge | `FRI IOPPs -> data availability sampling` | IOPP opening-consistency transfers into erasure-code commitments and DAS | create bridge |

## 与现有 Nahida 笔记的关系

- 扩展 [[data-availability-sampling|Data availability sampling]]: 从 LazyLedger 的 availability-only ledger / erasure coding seed，补入 transparent FRI-based erasure-code commitment route。
- 扩展 [[data-availability-and-light-clients|Data availability and light clients]]: 增加“light-client bandwidth vs network storage”的 DAS engineering trade-off。
- 新建/扩展 [[fri-iopps|FRI IOPPs]]: FRIDA 不是 FRI 原始论文，但提供 FRI folding、Reed-Solomon proximity 和 opening-consistency 的可复用 proof-system seed。
- 扩展 [[polynomial-commitments|Polynomial commitments]]: FRIDA 说明 FRI 也可被看作 commitment/proximity machinery 的来源，但本文选择 erasure-code commitments；若直接把 FRI 当 polynomial commitment 用，opening overhead 会更高。
- 新建 [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] bridge: 记录 proof-system 方法如何迁移到 blockchain data availability。

## Evidence Table

| Claim / observation | Source location | Claim type | Confidence | Notes |
| --- | --- | --- | --- | --- |
| FRIDA gives efficient DAS without trusted setup and only polylogarithmic overhead | Abstract p1; §1.1 p4 | contribution | high | main claim |
| The generic route is opening-consistent IOPP -> erasure-code commitment -> DAS | Abstract p1; §3 p9-p16; Appendix A | theoretical construction | high | uses HASW23 DAS compiler |
| Ordinary IOPP proximity is insufficient because openings can be inconsistent with the unique closest codeword | §1.3 p5; §3 p9-p11 | security motivation | high | motivates opening-consistency |
| FRI is non-adaptive, query-selectable, and opening-consistent under the defined Lucky/Bad sets | §4 p17-p25; Theorem 3 | proof result | high | full proof given |
| Batched FRI reduces encoding overhead and remains opening-consistent | §4.3 p25; Appendix C; Theorem 4 | extension | high | interleaved RS code |
| FRIDA improves commitment/per-query size relative to Hash but increases encoding/total storage | §5 p25-p28; Tables 1-2 | efficiency/trade-off | high | concrete data included |
| FRIDA is information-theoretically secure in the random oracle model | §1.1 p4 | assumption/security model | high | no trusted setup |
| DAS does not prove state validity or transaction correctness | Abstract p1; Appendix A p32-p33 | boundary | high | light-client availability only |

## 创新点

- 新抽象: opening-consistency for IOPPs, designed specifically to make IOPP transcripts support erasure-code commitment code-binding.
- 新 compiler: non-adaptive, query-selectable, opening-consistent IOPP can become an erasure-code commitment using Merkle trees and random oracles.
- 新 proof result: FRI and batched FRI satisfy opening-consistency.
- DAS construction: FRIDA uses FRI/batched FRI plus HASW23 transformation to obtain transparent DAS with polylog light-client overhead.
- Evaluation: compares Naive/Merkle/Hash/Tensor/FRIDA asymptotically and concretely, showing where FRIDA wins and loses.

## 局限性

### 作者明确说明或表中可见

- FRIDA 的 network encoding size 明显大于 Hash 和 Tensor in concrete tables.
- FRIDA 的 total communication for reconstruction can be worse than Hash.
- Parameter selection uses a heuristic search over fan-in, batch size and base dimension; scripts are in Appendix D.
- Security is in the random oracle model and relies on Merkle extraction/collision bounds.
- The paper relies on HASW23 for the DAS compiler from erasure-code commitments.

### 基于证据的推断

- 论文没有评估生产网络中的 sampling scheduler、adversarial availability network、peer discovery、bandwidth pricing 或 blob market integration.
- FRIDA 的 DAS route is transparent/no-setup, but not automatically post-quantum or implementation-ready; actual hash/field/Merkle engineering remains open.
- FRI here is used as IOPP/proximity machinery for erasure-code commitments, not as a full polynomial commitment API over arbitrary field points.
- It should not be treated as a rollup validity-proof replacement.

## 可复用思路

- 当某个 cryptographic proof system 只证明“接近合法对象”时，要检查应用是否还需要 opening consistency、binding 或 extraction。
- DAS 设计可分成两层: commitment/opening layer 与 sampling/extraction layer；前者可从 proof-system research 借力，后者保留 blockchain/network assumptions。
- 对 light-client scheme 不能只看 per-query bandwidth，也要同时看 encoding size、total reconstruction communication、trusted setup 和 prover/encoder cost。
- 对 FRI/STARK-like tools 的迁移要问清楚: 迁移的是 transparent Merkle/IOPP/folding pattern，还是 full polynomial-commitment semantics。

## 术语表

| Term | 解释 | Source |
| --- | --- | --- |
| Data availability sampling | light clients 通过随机查询编码数据及 openings 判断数据是否可恢复 | Abstract; Appendix A |
| Erasure code commitment | 对 erasure codeword 的 commitment，支持 position-binding 和 code-binding openings | §2 |
| Position-binding | 同一 position 不能被打开成两个不同 symbol | §2 |
| Code-binding | 成功打开的 symbols 必须与某个合法 codeword 一致，足够多后唯一 | §2 |
| IOPP | interactive oracle proof of proximity，证明 oracle vector 接近某个 code/language | §2 |
| Opening-consistency | 保证被查询的初始 oracle symbols 与 unique closest codeword 一致的额外性质 | §3 |
| Query-selectable | 可通过 deterministic `QSelect` 让 verifier final query 包含指定 base position | §3 |
| FRI | Reed-Solomon proximity proof using recursive folding over evaluation domains | §4 |
| Batched FRI | 对 interleaved RS code 先随机线性组合，再运行 FRI | §4.3; Appendix C |
| Blockwise distance | 按 folding preimage groups 度量差异，用于 FRI opening-consistency proof | §4.2 |

## 吸收动作

| Target | Action | Status |
| --- | --- | --- |
| [[data-availability-sampling|Data availability sampling]] | Add FRIDA as representative source and FRI/erasure-code-commitment route | done |
| [[data-availability-and-light-clients|Data availability and light clients]] | Add transparent DAS route and light-client/storage trade-off | done |
| [[fri-iopps|FRI IOPPs]] | Create foundation-thin proof-system node seeded by FRIDA | done |
| [[polynomial-commitments|Polynomial commitments]] | Add FRI/erasure-code commitment relation with boundary against full PCS semantics | done |
| [[fri-iopps-to-data-availability-sampling|FRI IOPPs -> data availability sampling]] | Create bridge with transfer/non-transfer boundaries | done |

## 后续队列建议

| Gap | Why | Suggested action |
| --- | --- | --- |
| HASW23 Foundations of Data Availability Sampling | FRIDA relies on definitions/compiler and compares against Hash | queue/deep-read if available |
| Original FRI / DEEP-FRI sources | `FRI IOPPs` is only foundation_thin from FRIDA, not complete | queue/deep-read |
| Celestia / fraud and DA proofs / EIP-4844 | DAS node still lacks modern deployment/standard evidence | nahida-research-search or update |
| KZG/Tensor DA route | Needed to compare FRIDA with Ethereum-style trusted-setup DA commitments | continue queue / search |

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-frida-data-availability-from-fri | Deep-read source note created and absorbed into Source + Knowledge + Bridge architecture. | codex |
