---
id: "sha256-dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
title: "The Sum-Check Protocol"
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
  - "p1-p2 protocol definition, verifier checks, final oracle evaluation"
  - "p2-p3 Proposition 1.1 completeness and soundness proof"
  - "p3-p4 communication, verifier/prover costs, multilinear-extension preview"
safe_for_absorption: true
canonical_url: "https://people.cs.georgetown.edu/jthaler/sumcheck.pdf"
doi: ""
arxiv_id: ""
venue: "COSC 544 Probabilistic Proof Systems lecture note"
year: "2017"
pdf_pages: 4
pdf_sha256: "dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
local_pdf: "~/Desktop/paper/sumcheck.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/sumcheck-dfbe6c185c1b-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "verifiable-computation"
direction_id: "interactive-proofs"
topic_ids:
  - "sum-check-protocol"
ontology_path:
  - "verifiable-computation"
  - "interactive-proofs"
  - "sum-check-protocol"
primary_ontology_path: "verifiable-computation/interactive-proofs/sum-check-protocol/sha256-dfbe6c185c1b"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/interactive-oracles/sha256-dfbe6c185c1b"
path_update_status: "propagated"
domains:
  - "verifiable-computation"
  - "zero-knowledge-proofs"
topics:
  - "sum-check-protocol"
  - "interactive-proofs"
aliases:
  - "sumcheck"
  - "LFKN sum-check protocol"
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
    - "verifying large finite-field sums without direct enumeration"
  method_family:
    - "sum-check protocol"
    - "low-degree polynomial testing"
    - "interactive proofs"
  system_layer:
    - "proof primitive"
    - "protocol subroutine"
  evaluation_context:
    - "communication complexity"
    - "soundness error"
    - "verifier time"
    - "prover time"
  application:
    - "GKR protocol"
    - "probabilistic proof systems"
    - "verifiable computation"
  bridge:
    - "interactive proofs -> zero-knowledge proof systems"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-sum-check-protocol"
source_refs:
  - "sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd"
  - "url:https://people.cs.georgetown.edu/jthaler/sumcheck.pdf"
  - "pdf:~/Desktop/paper/sumcheck.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "verifiable-computation -> interactive-proofs"
secondary_directions:
  - "zero-knowledge-proofs -> proof-systems"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "manual title"
  - "filename"
  - "canonical URL"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0005"
queue_status: "absorbed"
---

# The Sum-Check Protocol

## 论文身份

- 标题: The Sum-Check Protocol
- 作者/讲者: Justin Thaler
- 机构/课程: Georgetown University, COSC 544 Probabilistic Proof Systems
- 会议/期刊: lecture note
- 年份: 2017
- DOI: unknown
- arXiv: unknown
- 链接: https://people.cs.georgetown.edu/jthaler/sumcheck.pdf
- 本地 PDF: `~/Desktop/paper/sumcheck.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/sumcheck-dfbe6c185c1b-pages.txt`
- 代码/数据: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 4
- 已覆盖章节/页码: p1-p4 full text
- 已检查附录: 无附录
- 未覆盖章节/页码: 无
- Extraction gaps: 公式换行有轻微噪声，但协议、Proposition 1.1、cost table 和讨论可读
- 精读说明: 这是课程讲义而非正式论文；它是 sum-check protocol 的短而清晰的 foundation note，引用原始 LFKN92。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1 | 1 The Sum-Check Protocol | 问题设定: 对有限域多元多项式在 Boolean hypercube 上求和；协议目标 | 定义/动机 | 说明 verifier 不想直接枚举大和 |
| p1-p2 | Protocol description | 每轮 prover 发送 univariate polynomial，verifier 检查 degree 与相邻轮 consistency，最后随机点查询 `g` | 机制 | v rounds |
| p2-p3 | Proposition 1.1 | completeness error 0，soundness error `<= v d / |F|` | 正确性/安全性 | induction + polynomial identity bound |
| p3 | Costs table | communication `O(sum deg_i(g))` field elements, verifier time communication + one oracle query, prover time up to `O(2^v T)` | 成本边界 | constant-degree 时 communication `O(v)` |
| p3-p4 | MLE preview | multilinear extensions 可帮助 prover 消息快速计算；final verifier evaluation may be bottleneck | 应用边界 | 连接 GKR/VC |
| p4 | References | LFKN92 原始来源 | provenance | 后续可吸收原始 JACM paper |

## 核心精读笔记

### 背景、动机与问题边界

Sum-check protocol 解决的问题是: 给定有限域 `F` 上的 `v`-variate polynomial `g`，verifier 想确认
`H = sum_{b in {0,1}^v} g(b)`，但直接求和需要 `2^v` 项，可能远超 verifier 预算。Protocol 让 prover 逐轮给出部分求和后的 univariate polynomial，并通过随机挑战把全局求和声明压缩到最后一次随机点评估。

讲义强调，presentation 中先假设 verifier 有 oracle access to `g`，能在最后检查 `g(r_1,...,r_v)`；实际应用中如果 verifier 不能高效算这个值，就需要进一步让 prover 证明这个点值，或选择更 succinct 的 extension。证据锚点: p1, p3-p4。

### 模型、假设与定义

输入是 finite field `F` 上的 polynomial `g(x_1,...,x_v)`。常见应用求和域是 Boolean hypercube `{0,1}^v`，但 general version 可对 `B^m` 求和。`deg_i(g)` 表示变量 `i` 的 individual degree。Soundness bound 使用 field size `|F|`，field 越大，随机点撞上欺骗多项式一致点的概率越小。

Verifier 的核心能力是: 能检查 prover 发来的 univariate polynomial degree；能做少量 field arithmetic；能在最后对 `g` 做一次 oracle query 或等价的高效计算。证据锚点: p1-p2。

### 方法、协议或系统机制

第一轮，prover 发送 `g_1(X_1)`，声称它等于把 `x_2,...,x_v` 全部在 `{0,1}` 上求和后的 polynomial。如果该声明正确，则 `H = g_1(0) + g_1(1)`。Verifier 先检查 degree 和这个初始 sum consistency，然后发随机挑战 `r_1`。

第 `j` 轮，prover 发送 `g_j(X_j)`，声称它等于在前面变量绑定为 `r_1,...,r_{j-1}` 后，对剩余 Boolean variables 求和的 polynomial。Verifier 检查 `g_{j-1}(r_{j-1}) = g_j(0) + g_j(1)`，并检查 degree 不超过 `deg_j(g)`，再发随机 `r_j`。

最后一轮后，verifier 检查 `g_v(r_v) = g(r_1,...,r_v)`。如果所有 consistency checks 和 final evaluation 都通过，就接受。每轮只把一个多变量求和声明转为一个更低维的声明，直到只剩单点评估。证据锚点: p1-p2。

### 理论、证明或正确性论证

Proposition 1.1 说明 sum-check protocol 是 interactive proof system，completeness error `0`，soundness error `<= v d / |F|`。Completeness 直接来自 honest prover 每轮发送真实 partial-sum polynomial。Soundness 用 induction: 如果第一轮 polynomial 不是真实 partial sum，则两个 degree-`d` univariate polynomials 在随机 `r_1` 上仍相等的概率至多 `d/|F|`；一旦绑定点揭穿失败未发生，后续就是一个 `v-1` 变量的 false sum-check instance，套用归纳假设得到总错误概率 `vd/|F|`。

这个证明边界很重要: sum-check 的 soundness 来自 low-degree 和 random evaluation，不来自 cryptographic hardness。证据锚点: p2-p3。

### 实验、评估或案例

讲义没有实验。成本分析是渐近的:

- Rounds: `v`。
- Communication: `sum_i deg_i(g) + 1` 或 `v + sum_i deg_i(g)` field elements，constant individual degree 时为 `O(v)`。
- Verifier time: proportional to total communication plus one oracle query to `g`。
- Prover time: naive oracle model 下最多 `O(2^v * T)`，但实际应用的关键是利用 polynomial/extension 结构把 prover 消息算得接近这个枚举下界或更好。

证据锚点: p3 Table 1 和 discussion。

### 作者结论与我的判断

这份讲义是 `sum-check-protocol` 的清晰 seed source，适合作为 GKR 和大量 verifiable computation/ZKP 协议的基础概念笔记。它不替代 LFKN92 原始论文，也不覆盖现代 IOP/SNARK 中如何 commitment、Fiat-Shamir、batch、parallelize 或 optimize prover，但它足以支撑 Nahida 对 sum-check 的基本机制、soundness 和成本边界的 durable absorption。

## 层级候选分类

- L1 Domain candidate: `verifiable-computation`
- L2 Direction candidate: `interactive-proofs`
- L3 Topic/content cluster candidates: `sum-check-protocol`
- Ontology path: `verifiable-computation/interactive-proofs/sum-check-protocol/sha256-dfbe6c185c1b`
- 备选归属: `zero-knowledge-proofs/proof-systems/interactive-oracles`
- 父级领域: verifiable computation
- 学术子领域: probabilistic proof systems, interactive proofs
- 任务/问题: verifying large finite-field sums over Boolean hypercubes
- 方法族: sum-check protocol, low-degree random checks
- 模型/协议/算法族: LFKN-style algebraic interactive proof
- 评测场景: communication, rounds, verifier time, prover time, soundness error
- Benchmark/应用: GKR, MLE-based VC protocols, probabilistic proof systems
- 别名: sumcheck, LFKN sum-check
- 相邻方向: low-degree extensions, GKR protocol, multilinear extensions, IOP/SNARK proof systems
- 置信度: high
- 分类理由: 标题、全文定义和成本讨论均围绕 sum-check protocol
- 分类状态: accepted
- 分类证据: manual title, filename, canonical URL, full PDF deep read

## 一句话贡献

这份讲义给出 sum-check protocol 的标准 v-round 形式、completeness/soundness bound 和通信/时间成本，使 Nahida 可以把 sum-check 作为 GKR/verifiable computation 的可复用基础 primitive。

## 问题设定

Verifier 需要确认 `H = sum_{b in {0,1}^v} g(b)`，但直接枚举 `2^v` 个 Boolean inputs 太贵。Prover 可以做更多工作，但 verifier 希望只通过短交互和一次随机点评估来确认求和声明。

## 方法概览

### 组成部分

- Finite field `F`。
- v-variate polynomial `g`。
- Claimed sum `H`。
- 每轮 univariate partial-sum polynomial `g_j(X_j)`。
- Random challenges `r_1,...,r_v`。
- Final evaluation `g(r_1,...,r_v)`。

### 流程或协议

1. Prover 发送 `g_1(X_1)`，verifier 检查 `H = g_1(0)+g_1(1)`。
2. Verifier 随机选择 `r_1`。
3. 第 `j` 轮 prover 发送 `g_j(X_j)`，verifier 检查 degree 和 `g_{j-1}(r_{j-1}) = g_j(0)+g_j(1)`。
4. 最后一轮后 verifier 随机选择 `r_v`，检查 `g_v(r_v)=g(r_1,...,r_v)`。

### 关键定义、公式、算法或定理

- Proposition 1.1: completeness error `0`，soundness error `<= v d / |F|`。
- Communication: `O(sum_i deg_i(g))` field elements；constant-degree case `O(v)`。
- Verifier time: communication plus one oracle query/evaluation of `g`。

### 假设条件

- Polynomial degree bounds known and checked。
- Field size 足够大以使 `vd/|F|` 小。
- Verifier 能最终高效评估或验证 `g(r_1,...,r_v)`。

## 创新点

- 新思想: 用逐变量随机绑定把指数规模求和声明变成一个随机点值声明。
- 对已有工作的扩展: 作为 LFKN92 algebraic interactive proof machinery 的核心子例程。
- 工程或实证贡献: 无工程实现，但给出 VC/ZKP 系统常用的 verifier/communication/prover 成本模板。
- 依赖的 prior work: Lund, Fortnow, Karloff, Nisan 1992。

## 实验与结果

无实验。成本结果见 p3 Table 1:

- Communication: `O(sum_i deg_i(g))` field elements。
- Rounds: `v`。
- Verifier: at most `O(sum_i deg_i(g)) + T`，其中 `T` 是一次 `g` oracle query cost。
- Prover: at most `O(2^v * T)` in the direct oracle model。

## 局限性

### 作者明确说明

- Presentation 假设 verifier 有 oracle access to `g`；实际应用中可能不成立。
- 使用 multilinear extension 时，verifier 计算 `tilde f(r)` 可能需要 `O~(2^v)`，当 `v` 较大时不可接受。
- 有些应用必须使用 succinct representation 或 higher-degree extension，而不是直接使用 MLE。

### 基于证据的推断

- 这份讲义适合 foundation concept，不适合单独作为现代 proof system implementation guide。
- 原始 LFKN92、GKR、以及现代 sum-check-based SNARK/IOP papers 仍需吸收以补完整历史和工程路径。

## 可复用思路

- 将全局求和声明拆成一串局部一致性检查。
- 用 field randomness 和低度多项式相等性界保证 soundness。
- 设计 VC 协议时，核心难点经常转移到 final point evaluation 是否对 verifier 便宜。
- Multilinear extension 有利于 prover 消息计算，但不总是 verifier-friendly。

## 术语表

| Term | 解释 | 备注 |
| --- | --- | --- |
| Sum-check protocol | 证明多元多项式在有限集合上求和结果的交互协议 | LFKN-style primitive |
| Boolean hypercube | `{0,1}^v` | 最常见求和域 |
| Partial-sum polynomial | 绑定前缀变量后，对剩余变量求和得到的一元多项式 | 每轮 prover 消息 |
| Soundness error | cheating prover 让 false claim 被接受的概率上界 | `<= vd/|F|` |
| Multilinear extension | Boolean function 的多线性低度扩展 | 常用于 GKR/VC |

## Connections

- Supports: [[delegated-computation|GKR protocol]]
- Extends topic: [[sum-check-protocol|Sum-check protocol]]
- Related source: [[doi-10-1145-1374376-1374396-delegating-computation-interactive-proofs-for-muggles|Delegating Computation: Interactive Proofs for Muggles]]
- Original reference to queue/fetch later: LFKN92, Algebraic methods for interactive proof systems.

## Evidence Table

| Claim | Evidence anchor | Claim type | Confidence |
| --- | --- | --- | --- |
| Sum-check verifies `H = sum_{b in {0,1}^v} g(b)` without verifier enumerating all `2^v` terms. | p1 | definition/problem | high |
| The protocol has one round per variable and checks degree plus adjacent-round consistency. | p1-p2 protocol description | mechanism | high |
| The final check reduces the full sum claim to evaluating `g(r_1,...,r_v)`. | p1-p2 | mechanism | high |
| Completeness error is 0 and soundness error is at most `vd/|F|`. | p2-p3 Proposition 1.1 | theorem | high |
| Communication is `O(sum_i deg_i(g))` field elements, and `O(v)` when individual degrees are constant. | p3 Discussion of costs/Table 1 | cost | high |
| Verifier cost is communication plus one oracle query to `g`; if final evaluation is expensive, extension choice becomes a bottleneck. | p3-p4 | limitation/design principle | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| Sum-check communication is proportional to the sum of individual degrees, so for constant-degree variables it uses O(v) field elements and verifier time is communication plus one evaluation of g. | `sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd#p3` | folded_into_meta_note |
| In sum-check applications, the verifier's efficiency often hinges on whether the final random-point evaluation of the extension polynomial can be computed or verified succinctly. | `sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd#p3-p4` | folded_into_meta_note |
| For a v-variate polynomial with degree at most d in each variable over a finite field F, the sum-check protocol has completeness error 0 and soundness error at most vd/\|F\|. | `sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd#p2-p3` | folded_into_meta_note |
| The sum-check protocol lets a verifier check a claimed sum of a v-variate polynomial over the Boolean hypercube through v rounds of univariate partial-sum checks and one final random point evaluation. | `sha256:dfbe6c185c1bd88156331f8169c6dcab3b26011fbd274ac86ecd6d546489c6bd#p1-p2` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `sum-check-verifies-exponential-sums-with-v-rounds`: sum-check reduces a Boolean hypercube sum claim to v rounds and one final point evaluation.
- `sum-check-soundness-vd-over-field-size`: soundness error is bounded by `vd/|F|` under degree bound `d`.
- `sum-check-communication-linear-for-constant-degree`: communication is linear in variables for constant individual degree.
- `sum-check-final-evaluation-is-key-bottleneck`: verifier efficiency depends on being able to evaluate or verify `g(r)` cheaply.

### Concepts to update

- `sum-check-protocol`: create foundation concept seed.
- `gkr-protocol`: update relation that GKR depends on sum-check.

### Missing foundations

- LFKN92 original JACM paper.
- Low-degree extensions and multilinear extensions as standalone concepts.
- Modern sum-check-based SNARK/IOP systems.

## Synthesis Handoff

- Create `vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md`.
- Refresh `vault/04_Knowledge/verifiable-computation/interactive-proofs.md`.
- Create `vault/04_Knowledge/verifiable-computation/interactive-proofs/sum-check-protocol.md`.
- Keep `foundation_thin` until original LFKN92 and later implementation sources are absorbed.
