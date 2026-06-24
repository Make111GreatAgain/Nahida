---
id: "sha256-0aebec128887-pianist-scalable-zkrollups-distributed-zkp"
title: "Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs"
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
  - "p1-p17 full extracted text"
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown"
year: "2023"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
topic_ids:
  - "distributed-proof-generation"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications/blockchain-applications"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "proof-systems"
    - "applications"
    - "polynomial-commitments"
  topics:
    - "distributed-proof-generation"
    - "zkrollup-prover-scaling"
    - "bivariate-kzg"
domains:
  - "zero-knowledge-proofs"
topics:
  - "distributed-proof-generation"
  - "zkrollups"
  - "plonk"
  - "bivariate-kzg"
aliases:
  - "Pianist"
  - "fully distributed ZKPs"
  - "distributed Plonk"
  - "zkRollup prover scaling"
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
    - "ZKP prover scalability"
    - "zkRollup proof generation bottleneck"
  method_family:
    - "distributed proof generation"
    - "bivariate constraint systems"
    - "distributed bivariate KZG"
  system_layer:
    - "prover"
    - "proof-system engineering"
  evaluation_context:
    - "zkRollups"
    - "general circuits"
    - "AWS multi-machine experiments"
  application:
    - "zkRollup transaction batching"
    - "zkEVM prover scaling"
  bridge:
    - "distributed-proof-generation-to-zkrollups"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-pianist"
source_refs:
  - "sha256:0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
  - "filename:2023-1271.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "proof-systems"
secondary_directions:
  - "applications"
  - "polynomial-commitments"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "title and abstract state fully distributed ZKPs for zkRollups and zkEVM"
  - "Sections 3-5 define bivariate constraint systems, distributed IOP, DKZG, and RCPS"
  - "Section 6 evaluates zkRollup and general-circuit proving"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0027"
local_pdf: "~/Desktop/paper/2023-1271.pdf"
pdf_sha256: "0aebec128887036bbdc8a877dadc9d4fa69ca39278bf18c98d94c6803ba09f06"
extracted_text_path: "vault/02_Raw/pdf/extracted/2023-1271-0aebec128887-pages.txt"
---

# Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs

## 论文身份

- 标题: Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs
- 作者: Tianyi Liu, Tiancheng Xie, Jiaheng Zhang, Dawn Song, Yupeng Zhang
- 机构: University of Illinois Urbana-Champaign; UC Berkeley; Berkeley Center for Responsible, Decentralized Intelligence (RDI)
- 会议/期刊: unknown
- 年份: 2023
- DOI: unknown
- arXiv: unknown
- 链接: unknown
- 本地 PDF: `~/Desktop/paper/2023-1271.pdf`
- 代码: unknown from extracted PDF
- 数据: experiments use Polygon Hermez rollup circuit conversion and random general circuits; no dataset artifact URL found
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 17
- 已覆盖章节/页码: p1-p17, including abstract, introduction, related work, preliminaries, data-parallel protocol, general-circuit protocol, distributed bivariate KZG, robust collaborative proving, evaluation, discussion, conclusion, references, appendix pseudocode.
- 已检查附录: appendix pseudocode for protocol details was covered from extracted text.
- 未覆盖章节/页码: none known.
- Extraction gaps: no visible OCR/scanned gap. PDF metadata lacks title/authors/DOI/arXiv; ePrint identifier is not explicit in extracted text.
- 精读说明: 队列原先把本文归到 `recursion-and-folding/folding-schemes`。深读后纠正为 `zero-knowledge-proofs/proof-systems/distributed-proof-generation`，因为核心机制是 Plonk/bivariate-KZG 上的 fully distributed proof generation，不是 folding/recursion 或 proof aggregation。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和贡献 | zkRollups/zkEVM 的 proof generation 是瓶颈；提出 fully distributed ZKPs，Plonk-based，per-machine communication `O(1)`，proof/verifier `O(1)` | high | 给出分类和主张 |
| §1 / p1-p3 | 引言 | 公司需要 TB 级内存机器；Pianist 把 proof generation 分给多机器或类似 mining pool 的参与者 | high | 应用动机 |
| §1.1 / p3-p4 | Related work | 对比 DIZK、deVirgo、PCD/IVC、aPlonk、Gemini、Caulk+ 等 | high | 边界和非目标 |
| §2 / p4-p5 | Preliminaries | notation、Plonk、KZG 和 polynomial IOP 背景 | medium | foundation 依赖 |
| §3 / p5-p9 | Data-parallel circuits | bivariate constraint system、distributed polynomial IOP、per-party slice commitment/evaluation | high | 核心协议 |
| §4 / p9-p10 | General circuits | 用 `sigmaY/sigmaX` 和 helper polynomial `W(Y)` 支持 arbitrary connections | high | 泛化能力 |
| §4.2 / p10-p11 | DKZG compilation | distributed bivariate KZG 的 KeyGen/Commit/Open/Verify | high | KZG source extension |
| §5 / p11-p12 | Robust Collaborative Proving | 恶意机器下 master 检查 partial messages/proofs，排除 bad sub-provers | high | robustness 边界 |
| §6 / p12-p14 | Evaluation | Go/Gnark/BN254 实现，zkRollup 与 general circuits 结果 | high | 性能证据 |
| §7 / p14-p15 | Discussion | 与 PCD/IVC、Nova/SuperNova、aPlonk、custom gates 的边界 | high | 防止错归类 |
| §8 / p15 | Conclusion | 总结 scalable ZKP/zkRollup/zkEVM proving | medium | 结论 |
| References/Appendix / p15-p17 | 引用和伪代码 | DKZG/Open/Protocol flow pseudocode | medium | 支撑实现细节 |

## 核心精读笔记

> 本文的核心不是把多个已有 proof 聚合，也不是 recursive/folding IVC。它把一个大 ZKP proving task 拆成多台机器共同完成的 Plonk-like protocol，同时保持最终 proof size 和 verifier time 不随机器数增长。

### 背景、动机与问题边界

- 背景脉络: zkRollups 和 zkEVM 用 ZKP 批处理交易并把验证压力转移到 succinct proof verification，但 proof generation 本身成为瓶颈。论文称现有公司需要 TB 级内存机器来批量生成大 proof。
- 现有方法不足:
  - 原始 Plonk 单机 proving 对大电路的时间和内存需求随总电路规模增长。
  - DIZK 能分布式生成 proof，但 communication cost 高。
  - deVirgo 对 data-parallel workload 有线性扩展，但通信和 proof/verifier 成本仍随机器数或问题规模增长。
  - PCD/IVC/recursive proof 可以避免一次性存完整电路，但证明生成顺序化、需要递归电路和额外假设，且不一定适合把多个机器并行起来。
  - aPlonk 也是分布式 Plonk-like 路线，但论文指出它主要 data-parallel、涉及 shared Fiat-Shamir randomness/generalized IPA，最终 verifier cost 仍随 parties 对数增长。
- 本文问题定义: 在 `M` 台机器上生成一个大计算或 `M` 个子电路组成的 proof，使单机 prover time 和 memory 降低，同时保持 proof size/verifier time 常数级，并让机器之间的通信最小。
- 明确不解决的问题:
  - 不证明 zkRollup 的经济激励或 mining-pool 奖励分配机制。
  - general circuits 情况假设 witness 已经分布到各机器，论文没有把 witness generation/evaluation 作为瓶颈来解决。
  - zero-knowledge 细节没有完整展开，只说明可用 known transformations/random masks 获得。
  - 评估使用 BN254/Gnark/Plonk 转换，不代表所有生产 zkEVM/custom-gate 电路。
- 证据锚点: Abstract, §1, §1.1, §7。

### 模型、假设与定义

- 系统/安全/评估模型:
  - 有 `M` 个子电路，每个大小约为 `T`。
  - Data-parallel 情况中每台机器负责一个相同结构子电路的 witness/prover work。
  - General circuits 允许 arbitrary connections，但假设 witness 已经 distributed。
  - Robust setting 使用 master node 检查 sub-provers 的 partial proof/message，排除 malicious participants。
- 关键定义:
  - Fully distributed ZKPs: 多台机器协作完成一个 ZKP proof generation，最终 verifier 看到的是常数大小 proof 和常数级验证开销。
  - Bivariate constraint system: 用 `Y` 维组织 machine/sub-circuit index，用 `X` 维组织每个子电路内的 witness/constraint index。
  - DKZG: distributed bivariate KZG commitment scheme，每个 party commit/evaluate 自己的 polynomial slice，master 聚合 commitments/opening proofs。
  - RCPS: Robust Collaborative Proving Scheme，允许 master 在恶意 sub-prover 存在时验证 partial proof 并排除作恶者。
- 符号与参数: `M` 是机器/子电路数量，`T` 是单个子电路大小；`A(Y,X), B(Y,X), C(Y,X)` 是聚合后的 bivariate witness polynomials；`R_i(Y)` 是 Y 维 Lagrange basis。
- 假设条件:
  - KZG/DKZG 需要 pairing-friendly group 和 trusted setup/SRS。
  - 使用 Fiat-Shamir transcript 编译交互式 polynomial IOP。
  - Robust protocol 中 master 能收集、验证并拒绝 bad sub-prover messages。
- 证据锚点: §2, §3, §4.2, §5。

### 方法、协议或系统机制

#### Bivariate representation

Pianist 不把全部 witness 展开为一个巨大 univariate polynomial，而是把每个 party 的 local witness polynomial `a_i(X)` 通过 Y 维 Lagrange basis 聚合为:

```text
A(Y, X) = sum_i R_i(Y) a_i(X)
```

这样 `Y=i` 对应第 `i` 个 machine/sub-circuit，`X` 对应局部电路位置。用 Lagrange basis 而不是 naive powers of Y 的关键原因是避免在 gate constraint 中产生跨 party 的交叉项。

#### Data-parallel circuits

在 data-parallel 设置中，每个子电路结构相同，Plonk gate/copy/permutation constraints 可以按 `Y` 维批量表达。协议的关键是:

- 每个 machine 本地生成 witness slice 和 partial polynomial commitment。
- Master 聚合 commitments、challenge 和 opening requests。
- 对 quotient/check polynomial，Pianist 避免完整构造某些 bivariate object。例如对 `HY(Y,X)`，只在 verifier 给出 `X=alpha` 后构造 univariate `HY,alpha(Y)`，从而保持 communication 常数级。
- 最终 proof size 和 verifier time 与机器数无关。

#### General circuits

对于 arbitrary connection 的 general circuits，Pianist 增加跨子电路的 routing constraints:

- 使用 `sigmaY` 和 `sigmaX` 描述一个 wire copy 约束要跳到哪个子电路和局部位置。
- 引入 helper polynomial `W(Y)` 与额外 product constraints 来处理跨 `Y` 的 copy 关系。
- 保持相同复杂度阶，但 protocol 比 data-parallel 情况多一些 commitments/elements。

#### DKZG compilation

Pianist 把 distributed polynomial IOP 编译为 concrete proof 时使用 DKZG:

- `DKZG.KeyGen(1^lambda, M, T)` 生成支持 `Y` 维和 `X` 维的 public parameters。
- `DKZG.Commit(f, pp)` 中每个 `P_i` 对自己的 slice 计算 commitment，master 聚合为全局 commitment。
- `DKZG.Open(f, beta, alpha, pp)` 中每个 party 计算本地 evaluation 和 opening proof，master 组合。
- `DKZG.Verify` 通过 pairing equation 检查 bivariate evaluation opening。

这不是 KZG foundational definition，而是 KZG 在 distributed/bivariate proof generation 中的 usage extension。

#### Robust Collaborative Proving

论文定义 RCPS 来处理 malicious machines。核心思想是 master node 对 sub-provers 的 partial commitments/messages/openings 做额外验证，必要时借助 inner-product argument 或额外 checks 定位并排除无效 sub-prover。Theorem 5 给出 data-parallel circuits 的 robust collaborative proving security statement。

### 理论、证明或正确性论证

- Theorem 1/2/3/4 系列支撑 data-parallel/general-circuit polynomial IOP 与 DKZG 编译后的 completeness/soundness/efficiency。
- Theorem 5 支撑 robust collaborative proving in malicious setting for data-parallel circuits。
- 证明思路: 把 Plonk 约束提升到 bivariate polynomial identity，然后通过 polynomial IOP/KZG opening 的 soundness 把约束满足性归约到低度多项式关系；robust 部分通过验证 partial messages/openings 排除 inconsistent sub-prover。
- 正文没有展开的证明: extracted text 中部分证明较压缩，appendix 主要提供 protocol pseudocode。
- 依赖的外部材料: Plonk、KZG、Fiat-Shamir、polynomial IOP、pairing assumptions。
- 证据锚点: §3, §4, §4.2, §5, Appendix。

### 实验、评估或案例

- 实现:
  - 系统名: Pianist, expanded in paper as `Plonk vIA uNlimited dISTribution`。
  - 代码规模: `3700+` lines Go。
  - 基础库: Gnark。
  - Curve: BN254, chosen partly because Solidity supports pairing operations on BN254。
  - 环境: AWS `m6i.16xlarge`, 64 vCPU, 256 GiB memory, 2 to 64 machines across California/Oregon。
- zkRollup workload:
  - 使用 Polygon Hermez rollup circuit，从 Circom 转 R1CS 再转 Gnark Plonk constraints。
  - 论文报告每笔交易约 `86k` R1CS constraints，转成 Plonk 后约 `660k` constraints/tx。
  - 作者说明开源自定义 Plonk gates/lookup zkEVM circuits 不可得，因此有 conversion overhead，但这不影响展示 scaling。
- zkRollup results:
  - 64 machines 上，Pianist 可在 `313s` 内证明 `8192` transactions。
  - 原始 Plonk baseline 单机 32 tx 需要 `95s`。
  - 32 tx 时，Pianist 用 4 machines 需要 `17.5s`，约 `5.4x` faster。
  - Master `P0` final proof generation extra time 约 `2-16ms`。
  - Data-parallel communication per machine: sends `1984 bytes`, receives `160 bytes`, total `2144 bytes`, in 4 rounds。
  - Proof size: `27 G1 + 15 F = 2208 bytes`。
  - Verifier time: about `3.5ms`，independent of transaction count。
  - 与原始 Plonk 相比，bivariate polynomials 增加 `18 G1 + 7 F` proof size 和 `2` pairings verifier overhead。
- General-circuit results:
  - Random circuits sizes from `2^21` to `2^25`。
  - `2^25` gate example: original Plonk single machine `121s`; Pianist 2 machines `76.9s` (`1.57x` faster), 32 machines `5s` (`24.2x` faster)。
  - Memory for `2^24`: Plonk `70.7GB`; Pianist 2 machines `31.7GB`; Pianist 32 machines `1.92GB` (`36.8x` smaller)。
  - General-circuit communication per machine: `2336 bytes`; proof size `2816 bytes`; verifier time about `3ms`。
- 证据锚点: §6.1, §6.2, figures/tables around p12-p14。

### 作者结论与我的判断

- 作者明确声称: Pianist 提供 fully distributed ZKP schemes，能在 zkRollups/zkEVM 证明生成中用多台机器近线性扩展，并保持 O(1) communication/proof/verifier asymptotics。
- 由证据支持的判断:
  - Pianist 是 `distributed proof generation` 方法族的强 source，它足够支撑把 deVirgo seed 升级为独立 knowledge node。
  - 它是 Plonk/KZG 方向的分布式 proving 工程，而不是 folding schemes。
  - 对 zkRollups，Pianist 的主要价值是 prover scalability 和 memory reduction，而不是改变 rollup 安全模型。
- 仍需谨慎的推断:
  - 论文使用 BN254 和 Gnark/R1CS-to-Plonk conversion，不等于所有生产 zkEVM/custom-gate workload 的真实性能。
  - mining-pool-like participation 是动机，不是完整 incentive protocol。
  - malicious robustness 主要在 data-parallel RCPS 中说明，general-circuit robustness 和生产容错还需更多 source。
- 证据锚点: §6, §7, §8。

## 层级候选分类

- L1 Domain candidate: `zero-knowledge-proofs`
- L2 Direction candidate: `proof-systems`
- L3 Topic/content cluster candidates: `distributed-proof-generation`, `zkrollup-prover-scaling`, `bivariate-kzg`
- Ontology path: `zero-knowledge-proofs/proof-systems/distributed-proof-generation`
- 备选归属:
  - `zero-knowledge-proofs/applications/blockchain-applications` as application context.
  - `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` as DKZG usage extension.
  - Not `zero-knowledge-proofs/recursion-and-folding/folding-schemes`.
- 父级领域: zero-knowledge proofs
- 学术子领域: proof-system engineering, polynomial IOPs, distributed proving
- 任务/问题: ZKP prover scalability for large circuits and rollup batching
- 方法族: bivariate constraint systems, distributed polynomial IOP, distributed bivariate KZG
- 模型/协议/算法族: Plonk-based SNARK, KZG/DKZG, RCPS
- 评测场景: zkRollups, general circuits, AWS multi-machine experiments
- Benchmark/应用: Polygon Hermez-derived rollup circuit; random general circuits
- 别名: Pianist, fully distributed ZKPs, distributed Plonk
- 相邻方向: DIZK, deVirgo, aPlonk, proof aggregation, recursion/IVC
- 置信度: high
- 分类理由: 论文题名、摘要、协议主体和评估均围绕 distributed proof generation，而非 proof aggregation/recursion。
- 分类状态: corrected_from_queue
- 分类证据: abstract, §3-§6, §7 discussion
- Taxonomy version: 1.0
- Direction facets: proof-systems/prover-scaling/application-to-zkrollups/polynomial-commitment-backend
- Tags: `nahida/source`, `nahida/paper`, `nahida/zkp`
- Map memberships: `zero-knowledge-proofs`, `proof-systems`, `distributed-proof-generation`, `ZKP blockchain applications`
- 归属说明: Pianist 自身保持 source note；上层新增/更新的是 `distributed proof generation` 方法族节点与 `distributed proof generation -> zkRollup prover scaling` bridge。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | zero-knowledge proofs | ZKP, Plonk, KZG, zkRollup proof generation | high | durable parent |
| Research background | zkRollup/zkEVM prover bottleneck | Abstract/§1: proof generation bottleneck and TB-memory machines | high | knowledge background |
| Research problem | distributed proof generation / prover scalability | Abstract complexity claims, §3-§6 mechanisms/evaluation | high | new method-family node |
| Foundation concepts | zk-SNARKs, Plonk, KZG commitments, polynomial IOPs | §2 preliminaries, DKZG compilation | medium | existing foundation nodes plus gaps |
| Method family | fully distributed ZKPs via bivariate constraint systems and DKZG | §3-§4.2 | high | source extension under distributed-proof-generation |
| Application/evaluation context | zkRollups and zkEVM proof generation | title, abstract, §6.1 | high | bridge/application source extension |
| Artifact/source instance | Pianist | title and implementation section | high | source extension / representative source |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `zero-knowledge-proofs/proof-systems/distributed-proof-generation`
- 它能帮助未来哪些问题少读 source notes:
  - “ZKP proof generation 怎么横向扩展?”
  - “Pianist 和 deVirgo/DIZK/aPlonk 有什么区别?”
  - “zkRollup prover bottleneck 可以怎么处理?”
  - “KZG 在 distributed proving 里怎么用?”
- 哪些内容应留在 source note，而不是创建上层节点:
  - 具体公式、Protocol 1/2/3/4/5 步骤、AWS 机器型号、Polygon Hermez conversion 细节、每个实验数字。
- 哪些上层节点过薄、缺失或需要 foundation_pack:
  - Plonk foundation source missing.
  - DIZK/aPlonk primary sources missing.
  - Production zkRollup prover engineering/repos missing.
- 哪些候选只是别名/query key/watch term:
  - Pianist, fully distributed ZKPs, distributed Plonk, bivariate Plonk.

## 一句话贡献

Pianist 把 Plonk-style ZKP proof generation 重新组织成 bivariate/distributed protocol，使多台机器可协作生成一个常数 proof size 和常数 verifier time 的 proof，并在 zkRollup workload 上展示近线性扩展和显著内存下降。

## 问题设定

zkRollups/zkEVM 希望把更多交易批进一个 proof，但大电路单机 proving 需要高时间和高内存。目标是在 `M` 台机器上让每台机器只承担约一个子电路的 work，同时不把 proof size/verifier time/communication 变成新的瓶颈。

## 方法概览

### 组成部分

- Plonk-based distributed polynomial IOP。
- Bivariate constraint system: `Y` 维分机器，`X` 维分局部电路位置。
- DKZG: distributed bivariate KZG commitment/opening。
- RCPS: robust collaborative proving for malicious sub-provers。
- Master/aggregator: 聚合 commitments、messages、openings，并生成最终 proof。

### 流程或协议

1. 每个 machine 生成本地 witness slice 和 local polynomial commitments。
2. Master 聚合 commitments 并运行 Fiat-Shamir transcript。
3. Provers 回应 opening/challenge，master 组合 partial evaluations/opening proofs。
4. Verifier 检查常数数量的 commitments/openings 和 Plonk-derived identities。
5. 在 robust setting，master 对 partial messages 做额外验证并排除 invalid participants。

### 关键定义、公式、算法或定理

- `A(Y,X)=sum_i R_i(Y)a_i(X)` 是 bivariate witness aggregation 的核心形状。
- `HY,alpha(Y)` 技巧避免完整 materialize expensive bivariate quotient。
- DKZG Verify 使用 pairing equation 检查 bivariate evaluation。
- Theorem 5 提供 RCPS malicious participant setting 的 security statement。

### 假设条件

- KZG-style SRS/trusted setup 和 pairing assumptions。
- BN254/Solidity pairing support 是实现选择，不是协议必然条件。
- General circuits 的 witness 已经 distributed。
- Zero-knowledge 需要加 random masking/known transformations。

## 创新点

- 新思想: 用 bivariate constraint system 把 Plonk proving 在机器维度和电路维度分开，从源头避免多 proof 或大 proof 的 verifier/proof-size 膨胀。
- 对已有工作的扩展: 相对 DIZK/deVirgo/aPlonk，Pianist 追求 per-machine O(1) communication 和 O(1) proof/verifier asymptotics，并支持 general circuits。
- 工程或实证贡献: Go/Gnark 实现和 AWS 2-64 machines evaluation；zkRollup 8192 tx/64 machines/313s；general-circuit memory reduction。
- 依赖的 prior work: Plonk, KZG, DIZK, deVirgo, PCD/IVC, aPlonk, Nova/SuperNova, Gemini/Caulk+ as related work.

## 实验与结果

### 实验设置

- Implementation: 3700+ lines Go, Gnark, BN254.
- Hardware: AWS `m6i.16xlarge`, 64 vCPU, 256 GiB memory.
- Network: machines across California/Oregon.

### 数据集或 Benchmark

- zkRollup transaction verification circuit derived from Polygon Hermez via Circom/R1CS/Gnark Plonk conversion.
- Random general circuits from `2^21` to `2^25`.

### Baseline

- Original Plonk single-machine baseline.
- Related-work asymptotic comparison against DIZK and deVirgo.

### 指标

- Prover time.
- Memory usage.
- Communication per machine.
- Proof size.
- Verifier time.
- Master final proof generation overhead.

### 主要结果

| Setting | Pianist result | Baseline/comparison | Interpretation |
| --- | --- | --- | --- |
| zkRollup 8192 tx, 64 machines | 313s | Original Plonk only reported 32 tx/95s single machine | 扩展批量规模 |
| zkRollup 32 tx, 4 machines | 17.5s | Plonk 95s | 约 5.4x faster |
| Data-parallel communication | 2144 bytes/machine | independent of tx count/machines in experiment | O(1) communication signal |
| Data-parallel proof | 2208 bytes | 27 G1 + 15 F | constant-size proof |
| General circuit `2^25` | 5s on 32 machines | Plonk 121s | 24.2x faster |
| Memory `2^24` | 1.92GB on 32 machines | Plonk 70.7GB | 36.8x lower |

### 消融实验

Extracted text does not show a classic ablation table. The main comparison varies machine count, transaction count, and circuit size.

### 效率、成本或安全性

- Efficiency: single-machine prover time and memory scale down with machines.
- Cost: proof/verifier constants increase relative to original Plonk due to bivariate machinery.
- Security: DKZG soundness and RCPS robustness arguments; production malicious/fault model still needs implementation evidence.

### 结果 caveat

- R1CS-to-Plonk conversion inflates constraint count because open-source custom-gate zkEVM circuits were unavailable.
- BN254 offers only around 100-bit security in common assessments; the paper uses it for Solidity support.
- Real rollup prover pipelines include witness generation, scheduling, data availability, sequencer/prover market and reliability concerns not evaluated here.

## 局限性

### 作者明确说明

- General circuits assume distributed witness already exists.
- Zero-knowledge can be obtained by known transformations but is not the central protocol exposition.
- Custom Plonk gates/lookups for real zkEVM were unavailable, so evaluation uses conversion overhead.
- PCD/IVC, Nova/SuperNova, aPlonk and other adjacent routes have different tradeoffs rather than being strictly dominated.

### 基于证据的推断

- The `mining pool` analogy is motivational; the paper does not solve incentives, slashing, scheduling or availability.
- Robustness evidence is stronger for data-parallel RCPS than for all production distributed deployments.
- Need DIZK/aPlonk/deVirgo primary sources to make a complete method-family comparison.

## 可复用思路

- 用额外维度表达 parallelism，避免 naive aggregation 造成 cross terms。
- 把 expensive global polynomial construction delay 到 verifier challenge 后的一维 slice。
- 让 commitment/opening protocol 自身分布式化，而不是生成多个完整 proofs 再聚合。
- 对区块链系统，prover scaling 是独立于 verifier/gas optimization 的工程轴。

## 术语表

| Term | Meaning | Handling |
| --- | --- | --- |
| Pianist | 论文系统名 | source instance/source extension |
| Fully distributed ZKP | 多机协作生成一个 proof 的方法族表述 | alias/query key under distributed proof generation |
| DKZG | distributed bivariate KZG commitment scheme | KZG source extension, not foundation by itself |
| RCPS | Robust Collaborative Proving Scheme | source-specific robustness model, possible future subtopic |
| zkRollup prover scaling | 应用问题: rollup proof generation bottleneck | bridge/application route |
| bivariate constraint system | method mechanism for distributed Plonk | source extension under distributed proof generation |

## 连接

- 相关论文: DIZK, deVirgo/zkBridge, aPlonk, Plonk, KZG, Nova/SuperNova.
- 相关仓库: unknown from PDF.
- 相关 Knowledge nodes:
  - [[distributed-proof-generation|Distributed proof generation]]
  - [[proof-systems|Proof systems]]
  - [[zk-snarks|zk-SNARKs]]
  - [[blockchain-applications|ZKP blockchain applications]]
  - [[kzg-commitments|KZG commitments]]
- 相关 Bridges:
  - [[distributed-proof-generation-to-zkrollups|Distributed proof generation -> zkRollup prover scaling]]
- Bridge 候选: endpoint `zero-knowledge-proofs/proof-systems/distributed-proof-generation` to `zero-knowledge-proofs/applications/blockchain-applications`; relation types `applies_to`, `scalability_enabler`, `implementation_reuse`; transfer boundary: prover scaling transfers, rollup security/economics/finality do not.

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| distributed proof generation | knowledge_node | Pianist plus existing zkBridge/deVirgo source | active_seed | created/updated |
| zkRollup prover scaling | bridge/application section | Title, abstract, §6.1 | active_seed | bridge to blockchain applications |
| bivariate KZG/DKZG | source_extension | §4.2 | active_seed | update KZG node as usage extension |
| Pianist | source instance | whole paper | source_only | keep details here |
| Plonk foundation | foundation_gap | Pianist depends on Plonk but vault lacks foundation source | queued | foundation_pack or future paper |
| DIZK/aPlonk primary comparison | expansion source | related work table/discussion | pending_queue | absorb queued PDFs if present |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| zkRollups/zkEVM 的 proof generation 是瓶颈 | author_claim | Abstract/§1 | companies need powerful machines with TB memory; proof generation bottleneck | high | source claim |
| Pianist per-machine prover time for M sub-circuits size T is `O(T log T + M log M)` | author_claim | Abstract | compared to Plonk `O(MT log(MT))` | high | asymptotic claim |
| Communication per machine is O(1), proof size and verifier time O(1) | author_claim | Abstract/Table 1 | comparison with DIZK/deVirgo | high | asymptotic claim |
| Bivariate representation is the core mechanism | synthesis | §3 | `A(Y,X)=sum R_i(Y)a_i(X)` style construction | high | protocol mechanism |
| DKZG is a distributed KZG usage extension | synthesis | §4.2 | KeyGen/Commit/Open/Verify for bivariate polynomials | high | update KZG node |
| 8192 tx on 64 machines in 313s | experiment_result | §6.1 | zkRollup evaluation | high | workload caveat |
| 32 machines reduce `2^24` memory from 70.7GB to 1.92GB | experiment_result | §6.2 | general-circuit memory evaluation | high | random circuits |
| Queue classification should be corrected away from folding schemes | nahida_judgment | full paper | no folding/IVC main mechanism; related work contrasts PCD/IVC | high | taxonomy correction |

## 知识交接

- 留在本文元笔记的证据: protocol details, theorem list, exact benchmark numbers, implementation environment, R1CS-to-Plonk conversion caveat, RCPS details.
- 待更新 Knowledge node:
  - [[distributed-proof-generation|Distributed proof generation]]
  - [[proof-systems|Proof systems]]
  - [[blockchain-applications|ZKP blockchain applications]]
  - [[kzg-commitments|KZG commitments]]
- 作为哪些 Knowledge node 的 source extension:
  - `zero-knowledge-proofs/proof-systems/distributed-proof-generation`
  - `zero-knowledge-proofs/applications/blockchain-applications`
  - `zero-knowledge-proofs/polynomial-commitments/kzg-commitments`
- 需要补的 foundation knowledge/source:
  - Plonk foundation source.
  - DIZK/aPlonk/deVirgo primary comparison beyond zkBridge source.
  - zkRollup production prover pipeline sources.
- 待新增或复核 domain/direction/problem:
  - Create `distributed-proof-generation` as method-family node.
  - Do not create `Pianist` as knowledge node.
- Bridge 候选:
  - `distributed-proof-generation-to-zkrollups`
- Watchlist 词条:
  - fully distributed ZKPs
  - distributed Plonk
  - bivariate KZG
  - prover market / prover pool
  - zkRollup prover scaling
- 后续论文:
  - DIZK.
  - aPlonk.
  - Hekaton if queue contains it, with care to distinguish proof aggregation from distributed proving.
  - Mangrove has been routed to [[memory-efficient-snarks|Memory-efficient SNARKs]], not distributed proving.
- 后续仓库:
  - Pianist code if public.
  - Production rollup prover code/benchmark if available.
- Review queue:
  - Verify whether filename `2023-1271.pdf` corresponds to IACR ePrint 2023/1271; PDF text did not expose ePrint metadata.

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| distributed proof generation | knowledge_node | 建/更新完整 method-family node，并把 Pianist/deVirgo/DIZK/aPlonk 作为代表来源 | 把 Pianist 本身当成基础概念 | Pianist + zkBridge/deVirgo |
| zk-SNARKs | foundation_thin existing node | 作为 proof-system prerequisite，Pianist 是 source extension，不定义 zk-SNARKs | 用 Pianist 重新定义 zk-SNARKs | §2/related work |
| KZG commitments | existing foundation node | 添加 DKZG/bivariate KZG usage extension | 把 DKZG 单独升为基础概念 | §4.2 |
| Pianist | representative_instance_or_source_extension | 放入 source note 和 source extension | 独立建成上层 concept | whole paper |
| zkRollup prover scaling | bridge/application problem | 作为 application bridge/section，待多来源再考虑 child node | 把 zkRollup 当 proof-system foundation | Abstract/§6 |

## Knowledge 综合交接

- 应创建 Knowledge node: `zero-knowledge-proofs/proof-systems/distributed-proof-generation`
- 应刷新 Knowledge synthesis section: proof systems, ZKP applications/blockchain applications, KZG commitments, zero-knowledge-proofs top node.
- 应标记过期: domain dynamics remains stale for external freshness; add Pianist as recorded evidence but do not claim latest trend.
- 无需更新的理由: recursion-and-folding/folding-schemes 不更新，因为本文不是 folding route。
- 建议 node kind: `method_family`

## 处理日志

| Date | Run ID | Action |
| --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-pianist | Deep-read `2023-1271.pdf`, corrected queue classification, wrote source note, prepared knowledge/bridge absorption. |
