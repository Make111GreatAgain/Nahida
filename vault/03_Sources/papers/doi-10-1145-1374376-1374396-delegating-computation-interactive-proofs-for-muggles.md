---
id: "doi-10-1145-1374376-1374396"
title: "Delegating Computation: Interactive Proofs for Muggles"
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
  - "p1-p3 abstract, motivation, delegation setting, prior-work contrast, main theorem"
  - "p4-p6 non-interactive certificates, log-space verifier characterization, non-uniform circuits, zero-knowledge/IPCP/PCA implications"
  - "p6-p9 main technique overview and bare-bones protocol"
  - "p9-p10 references checked for provenance"
safe_for_absorption: true
canonical_url: "https://dl.acm.org/doi/10.1145/1374376.1374396"
doi: "10.1145/1374376.1374396"
venue: "STOC 2008"
year: "2008"
pdf_pages: 10
pdf_sha256: "5ce8a350963e9c5272cd33c7c631440ada481997539c5a33fa04c4b5807fe7f2"
local_pdf: "~/Desktop/paper/document.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/document-5ce8a350963e-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "verifiable-computation"
direction_id: "interactive-proofs"
topic_ids:
  - "delegated-computation"
  - "gkr-protocol"
ontology_path:
  - "verifiable-computation"
  - "interactive-proofs"
  - "delegated-computation"
primary_ontology_path: "verifiable-computation/interactive-proofs/delegated-computation/doi-10-1145-1374376-1374396"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/interactive-proof-transformations/doi-10-1145-1374376-1374396"
path_update_status: "propagated"
domains:
  - "verifiable-computation"
  - "zero-knowledge-proofs"
topics:
  - "delegated-computation"
  - "gkr-protocol"
  - "interactive-proofs"
aliases:
  - "GKR"
  - "Interactive Proofs for Muggles"
  - "Goldwasser-Kalai-Rothblum protocol"
tags:
  - "nahida/source"
  - "paper"
  - "verifiable-computation"
  - "interactive-proofs"
direction_facets:
  parent_domain:
    - "verifiable-computation"
  subdomain:
    - "interactive-proofs"
  problem:
    - "delegating polynomial-time computation to an untrusted server"
    - "super-efficient verification with efficient honest prover"
  method_family:
    - "public-coin interactive proofs"
    - "low-degree extensions"
    - "sum-check protocol"
    - "layer-by-layer circuit verification"
  system_layer:
    - "proof system"
    - "complexity-theoretic protocol"
  evaluation_context:
    - "asymptotic verifier time"
    - "communication complexity"
    - "honest prover time"
  application:
    - "delegated computation"
    - "succinct certificates"
    - "zero-knowledge proofs"
    - "interactive PCP and probabilistically checkable arguments"
  bridge:
    - "interactive proofs -> verifiable computation"
    - "interactive proofs -> zero-knowledge proofs"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-interactive-proofs-for-muggles"
source_refs:
  - "doi:10.1145/1374376.1374396"
  - "pdf:~/Desktop/paper/document.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "verifiable-computation -> interactive-proofs"
secondary_directions:
  - "zero-knowledge-proofs -> proof-systems"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title"
  - "known DOI"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0004"
queue_status: "absorbed"
---

# Delegating Computation: Interactive Proofs for Muggles

## 论文身份

- 标题: Delegating Computation: Interactive Proofs for Muggles
- 作者: Shafi Goldwasser, Yael Tauman Kalai, Guy N. Rothblum
- 机构: MIT and Weizmann Institute; Georgia Tech; MIT
- 会议/期刊: STOC 2008
- 年份: 2008
- DOI: `10.1145/1374376.1374396`
- 链接: https://dl.acm.org/doi/10.1145/1374376.1374396
- 本地 PDF: `~/Desktop/paper/document.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/document-5ce8a350963e-pages.txt`
- 代码/数据: unknown
- License: ACM permission text on first page

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 10
- 已覆盖章节/页码: p1-p10 full text
- 已检查附录: 本 PDF 无附录；多处核心证明细节 deferred to full version
- 未覆盖章节/页码: full version 中的完整协议细节和证明未在该 PDF 内
- Extraction gaps: 字体 ligature 和公式换行有少量噪声，但 theorem statements、复杂度和协议概览可读
- 精读说明: 这是 STOC 扩展摘要，适合吸收 main theorem、模型、技术路线和应用推论；细节证明需要后续 full version 或后续 GKR 资料补证。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1 | Abstract | efficient prover, nearly-linear verifier, public-coin IP for log-space uniform circuits | main contribution | 直接给出复杂度 |
| p1-p3 | Introduction | delegated computation 场景、efficient prover 与 unconditional soundness 的动机 | problem setting | BOINC、weak devices |
| p3 | 1.1 Our Main Result | Theorem 1 和 Corollary 1 | theorem anchor | GKR foundation |
| p3-p4 | Prior Work | PCP/holographic proofs、Kilian/Micali arguments 与标准 IP 差异 | boundary | soundness/model contrast |
| p4-p5 | 1.2 Non-Interactive CS Certificates | public-key designated-verifier certificate via Kalai-Raz PIR transform | implication | computational soundness |
| p5 | 1.3-1.4 | public-coin log-space verifiers for P; non-uniform online/offline protocol | implication/model variant | one-time offline info caveat |
| p5-p6 | 1.5-1.6 | short ZK proofs, IPCP, PCA consequences | application bridge | ZKP/proof-system bridge |
| p6-p8 | 2 Main Techniques Overview | layer-by-layer low-degree-extension checking, sum-check, uniformity handling | mechanism | core GKR intuition |
| p8-p9 | 3 Bare-Bones Protocol | formal objects `V_i`, `add_i`, `mult_i`, LDE, phase reduction | protocol sketch | oracle abstraction |
| p9-p10 | References | provenance only | background | no new claims |

## 核心精读笔记

### 背景、动机与问题边界

本文研究的是“可计算语言的 interactive proofs”，重点不是让 unbounded prover 证明 intractable language，而是让一个 polynomial-time 的 honest prover 证明它已经正确执行了某个 tractable computation。作者把这个 prover 称为 “muggle”，强调它没有魔法般的无限算力，也没有关于输入的辅助秘密。

应用动机是 delegated computation: 弱客户端或 delegator 把大计算交给更强或更多的 delegatee，但希望验证时间显著小于自己重新执行计算。论文明确要求 soundness against arbitrary cheating prover，因此不同于 Kilian/Micali 等 computationally sound arguments，也不同于需要 proof string 不被自适应修改的 PCP/holographic setting。证据锚点: p1-p4。

### 模型、假设与定义

核心模型是 public-coin interactive proof。主定理覆盖由 `O(log(S(n)))`-space uniform boolean circuits 计算的语言，电路 size 为 `S(n)`、depth 为 `d(n)`。Verifier 的目标是时间接近输入长度加电路深度，而不是电路 size；honest prover 要保持 `poly(S(n))`，通信复杂度按 depth 而非 size 增长。

对 L-uniform NC，Corollary 1 给出 prover `poly(n)`、verifier `n * polylog(n)` time、`O(log n)` space、communication `polylog(n)`。这也是后来 GKR-style delegated computation 协议的基础来源。证据锚点: p3。

### 方法、协议或系统机制

技术核心是对 layered arithmetic circuit 做 layer-by-layer 证明。Verifier 不是一次性检查整个 computation transcript，而是在第 `i` phase 把“`V_{i-1}` 的某个 low-degree extension 点值正确”归约为“`V_i` 的某个点值正确”。这个过程从输出层向输入层推进，最后 verifier 只需自己计算 input layer 的 low-degree extension 某一点。

每层转换使用 sum-check protocol。对 layer `i`，门连接关系由 `add_i`、`mult_i` 的低度扩展表示，门值向量的低度扩展为 `V_i`。Verifier 通过 sum-check 检查一个大求和等式；sum-check 末端需要两个下一层 LDE 点值，论文再用交互把两个点值验证压缩成一个点值验证，从而保持跨层递归形态。

Uniformity 用来解决 verifier 不能读取整张电路的问题。对特殊 log-space computations，连接谓词的 LDE 可在 polylog time 内计算；对一般 log-space uniform circuits，verifier 让 prover 计算连接谓词，再用前述 log-space computation 的 IP 迫使它证明计算正确。对 non-uniform circuits，则允许一次性 offline preprocessing 计算少量连接谓词 LDE evaluations。证据锚点: p6-p9。

### 理论、证明或正确性论证

Theorem 1 声称对 `O(log(S(n)))`-space uniform circuits 存在 perfect completeness、soundness `1/2` 的 public-coin IP，复杂度为: prover `poly(S(n))`，verifier `(n+d(n)) * polylog(S(n))` time and `O(log(S(n)))` space，communication `d(n) * polylog(S(n))`。

Theorem 2 把 public-coin IP 经 Kalai-Raz transformation 转为 public-key 模型下一轮 designated-verifier argument/certificate，依赖 poly communication PIR；这不是 unconditional IP，soundness 只对 bounded cheating prover。Theorem 3 给出 P 中语言都有 public-coin IP with log-space verifier。Theorem 5 用 standard public-coin to zero-knowledge transformation，把 AC0 可验证关系的短 ZK 结果扩到 NC 可验证关系，假设 one-way functions。证据锚点: p3-p6。

### 实验、评估或案例

本文没有实验系统或 benchmark；评估是渐近复杂度和模型比较。主要“结果”是 verifier time、space、communication、honest prover time 的 asymptotic bound，以及对 BOINC/weak-device 场景的概念性应用。证据锚点: p1-p6。

### 作者结论与我的判断

这篇论文是 verifiable computation 与 GKR-style protocols 的 foundation source。它的重要性在于把 classical IP/PCP 的代数化工具改造成“honest prover efficient + verifier super-efficient”的 delegation protocol。由于 PDF 是短会议版，Nahida 中应把它标为 strong seed/foundation source，但对 full protocol proof、soundness amplification、实现成本、现代 SNARK/IOP 化路线，需要后续吸收 sum-check、Thaler GKR、Libra/Spartan/Brakedown 等来源补全。

## 层级候选分类

- L1 Domain candidate: `verifiable-computation`
- L2 Direction candidate: `interactive-proofs`
- L3 Topic/content cluster candidates: `delegated-computation`, `gkr-protocol`
- Ontology path: `verifiable-computation/interactive-proofs/delegated-computation/doi-10-1145-1374376-1374396`
- 备选归属: `zero-knowledge-proofs/proof-systems/interactive-proof-transformations`
- 父级领域: verifiable computation, complexity theory
- 学术子领域: interactive proofs, proof verification
- 任务/问题: delegated computation with super-efficient verification
- 方法族: public-coin IP, low-degree extensions, sum-check, layered circuit arithmetization
- 模型/协议/算法族: GKR protocol
- 评测场景: asymptotic complexity for uniform circuits and NC computations
- Benchmark/应用: BOINC-like volunteer computing, weak devices, succinct certificates, zero-knowledge for NC-verifiable relations
- 别名: GKR, Interactive Proofs for Muggles
- 相邻方向: sum-check protocol, IOP/PCP, succinct arguments, zero-knowledge proofs
- 置信度: high
- 分类理由: 标题、abstract、Theorem 1、Section 2/3 的机制均指向 delegated/verifiable computation through interactive proofs
- 分类状态: accepted
- 分类证据: title, DOI, abstract, Theorem 1, Sections 2-3
- Taxonomy version: 1.0
- Map memberships: `verifiable-computation`, `interactive-proofs`, `delegated-computation`

## 一句话贡献

本文给出 GKR-style public-coin interactive proof，使 log-space uniform low-depth circuit computation 可由 polynomial-time prover 证明，并由 nearly-linear time、log-space verifier 检查，从而为 delegated computation 建立 complexity-theoretic foundation。

## 问题设定

给定一个 tractable language 或 circuit computation，client/verifier 希望确认 server/prover 返回的计算结果正确，但不想花费接近完整计算的时间。协议需要同时满足:

- honest prover 仍为 polynomial time；
- verifier 时间远小于计算大小，最好接近输入长度和 circuit depth；
- communication polylog 或按 depth polylog；
- soundness 不依赖 cheating prover 的计算受限假设。

## 方法概览

### 组成部分

- Layered arithmetic circuit representation.
- 每层 gate values 的 low-degree extension `V_i`。
- Gate wiring predicates `add_i` and `mult_i` 及其 low-degree extensions。
- Sum-check protocol for reducing a layer claim.
- Random linear/interactive reduction from two next-layer points to one point.
- Uniformity subprotocol for wiring-predicate access.

### 流程或协议

1. Prover 声称 output layer LDE 某点值对应 `C(x)`。
2. Phase `i` 用 sum-check 把 `V_{i-1}(z_{i-1}) = r_{i-1}` 归约到下一层点值。
3. Prover 提供下一层两个 LDE 点值，verifier 再把两个点约成一个点。
4. 重复直到 input layer。
5. Verifier 自己计算 input LDE 某点并接受或拒绝。

### 关键定义、公式、算法或定理

- `Theorem 1`: uniform circuits 的 public-coin IP with verifier `(n+d) * polylog(S)`、communication `d * polylog(S)`、prover `poly(S)`。
- `Corollary 1`: L-uniform NC 的 verifier `n * polylog(n)`、communication `polylog(n)`。
- Bare-bones protocol 中 `f_i(p, omega_1, omega_2)` 将 wiring predicates 和下一层 gate values 组合为上一层 LDE 的求和表达式。

### 假设条件

- 主 IP 依赖 log-space 或 `O(log S)`-space uniformity。
- Soundness 是 unconditional interactive proof soundness。
- Non-interactive certificates 和 PCA 等派生结果加入 computational assumptions，如 PIR、one-way functions 或 public-key model。

## 创新点

- 新思想: 不让 prover 生成整份 PCP transcript，而是让 proof 跟随 parallel computation 逐层推进。
- 对已有工作的扩展: 相比 LFKN/Shamir 等代数化 IP，关注并改进 honest prover time，使 tractable computations 的 prover 仍 efficient。
- 模型贡献: 把 delegated computation 作为 standard interactive proof 问题处理，避免 computational soundness 或 non-adaptivity 假设。
- 应用贡献: 支持 succinct certificates、log-space verifier characterization、short ZK for NC-verifiable relations、IPCP/PCA 的更优参数。

## 实验与结果

本文无实现实验。主要结果是:

- L-uniform NC: verifier quasi-linear in input, communication polylog, prover polynomial。
- General uniform circuit with depth `d`: verifier 和 communication 按 `d` 多项式/线性地增长，而非按 circuit size。
- Derived certificates: public-key designated-verifier one-round arguments with certificate size `poly(kappa, log n)` under PIR assumptions。
- ZK implication: NC-verifiable NP relations 的 communication quasi-linear in witness length under one-way functions。

## 局限性

### 作者明确说明

- 完整协议细节和证明 deferred to full version。
- Non-uniform circuits 需要 offline preprocessing，且保存的信息只能使用一次，否则 soundness compromised。
- Non-interactive certificates 是 computationally sound，不是 unconditional IP。

### 基于证据的推断

- 该会议版不适合作为实现细节或工程成本的唯一依据。
- Modern SNARK/IOP systems often reuse GKR/sum-check ideas, but the paper itself does not cover modern PCS, commitments, transcript compilers, or concrete prover optimizations.

## 可复用思路

- 用 low-degree extension 把大规模 layer values 变成少量随机点检查。
- 通过 sum-check 把指数/大规模求和转成短交互。
- 让 verifier 只维护当前待验证点，而不是保存完整计算历史。
- 把 uniformity/wiring predicate access 当作 proof obligation，而不是让 verifier 读取整张电路。

## 术语表

| Term | 解释 | 备注 |
| --- | --- | --- |
| GKR | Goldwasser-Kalai-Rothblum protocol family | 本文来源 |
| delegated computation | 客户端把计算外包给不可信执行者并验证结果 | verifiable computation 的核心问题 |
| low-degree extension | 把离散向量扩展成有限域上的低度多项式 | 支持随机点检查 |
| sum-check protocol | 证明多元多项式在布尔/有限域网格上求和的交互协议 | 下一篇 `sumcheck.pdf` 会作为 foundation |
| public-coin interactive proof | verifier 的消息都是公开随机挑战 | 用于 Kalai-Raz transform |

## Connections

- Extends: [[delegated-computation|Delegated computation]], [[delegated-computation|GKR protocol]]
- Related pending source: `sumcheck.pdf` should deepen the sum-check primitive.
- Bridge candidate: GKR to ZKP proof systems via public-coin transformations and later IOP/SNARK lines.
- Bridge candidate: GKR to distributed/cloud computation through delegated computation applications.

## Evidence Table

| Claim | Evidence anchor | Claim type | Confidence |
| --- | --- | --- | --- |
| GKR gives a public-coin IP for `O(log S)`-space uniform circuits with prover `poly(S)`, verifier `(n+d)polylog(S)`, and communication `d polylog(S)`. | p1, p3 Theorem 1 | theorem | high |
| For L-uniform NC, verifier time becomes `n polylog(n)` and communication `polylog(n)`. | p1, p3 Corollary 1 | corollary | high |
| The delegation setting demands verifier work much smaller than recomputation while soundness remains against unbounded cheating provers. | p2-p4 | problem/model | high |
| The protocol checks computation layer by layer using low-degree extensions and sum-check, reducing one layer-point claim to a lower layer-point claim. | p6-p9 | mechanism | high |
| Uniformity is used so the verifier need not read the whole circuit; wiring-predicate access can itself be proved. | p7-p8 | mechanism | high |
| Public-coin IP can be transformed into designated-verifier one-round arguments using Kalai-Raz/PIR assumptions. | p4-p5 Theorem 2 | implication | high |
| Short ZK proofs for NC-verifiable NP relations follow by applying public-coin to ZK transformations under one-way functions. | p5-p6 Theorem 5 | implication | medium-high |
| Full proof details are not in this STOC version. | p3, p5, p8 | limitation | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| GKR gives a public-coin interactive proof for log-space uniform circuits where the honest prover runs in polynomial time while the verifier runs in roughly input-plus-depth time and communicates depth times polylogarithmic size. | `doi:10.1145/1374376.1374396#p1`<br>`doi:10.1145/1374376.1374396#p3` | folded_into_meta_note |
| The GKR protocol verifies a circuit computation by reducing a claimed low-degree-extension value at one layer to a claimed value at the next layer, using sum-check and randomness until the verifier only checks an input-layer point. | `doi:10.1145/1374376.1374396#p6-p9` | folded_into_meta_note |
| Applying the Kalai-Raz PIR-based transformation to the GKR public-coin interactive proof yields one-round designated-verifier certificates for L-uniform NC computations with polylogarithmic certificate size, but only computational soundness. | `doi:10.1145/1374376.1374396#p4-p5` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `gkr-delegated-computation-nearly-linear-verifier`: GKR gives efficient-prover public-coin IP for uniform low-depth circuits with verifier time near input plus depth.
- `gkr-layer-by-layer-sum-check-reduction`: GKR verifies computation by reducing LDE claims from output layer to input layer using sum-check.
- `gkr-public-coin-ip-yields-succinct-certificates`: Kalai-Raz/PIR transform turns GKR public-coin IP into designated-verifier succinct certificates under computational assumptions.

### Concepts to update

- `delegated-computation`: create source-backed seed.
- `gkr-protocol`: create source-backed seed.

### Missing foundations

- Sum-check protocol as independent primitive.
- Full-version GKR proof details and later implementation-oriented expositions.
- IOP/PCP/SNARK transformations that connect GKR to modern proof systems.

## Synthesis Handoff

- Create `vault/04_Knowledge/verifiable-computation.md`.
- Create `vault/04_Knowledge/verifiable-computation/interactive-proofs.md`.
- Create `vault/04_Knowledge/verifiable-computation/interactive-proofs/delegated-computation.md`.
- Create `vault/04_Knowledge/verifiable-computation/interactive-proofs/delegated-computation.md`.
- Keep foundation status `foundation_thin` pending `sumcheck.pdf` and later verifiable computation system papers.
