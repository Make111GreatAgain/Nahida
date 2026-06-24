---
id: "nahida-knowledge-split-prover-zksnarks"
title: "Split prover zkSNARKs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "method_family"
hierarchy_level: "method_family"
file_slug: "split-prover-zksnarks"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-private-delegated-proving"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
  - "private-delegated-proving"
  - "split-prover-zksnarks"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/recursion-and-folding"
relation_edges:
  - from: "nahida-knowledge-split-prover-zksnarks"
    relation: "is_a"
    to: "nahida-knowledge-private-delegated-proving"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-split-prover-zksnarks"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-split-prover-zksnarks"
    relation: "contrasts_with"
    to: "nahida-knowledge-recursion-and-folding"
    evidence_refs:
      - "vault/05_Bridges/split-prover-zksnarks-to-recursion-and-folding.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-split-prover-zksnarks"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-split-prover-zksnarks"
    relation: "bridges_to"
    to: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    evidence_refs:
      - "vault/05_Bridges/split-prover-zksnarks-to-recursion-and-folding.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
source_note_refs:
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
representative_source_refs:
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
query_keys:
  - "Split prover zkSNARKs"
  - "split prover"
  - "partial witness zkSNARK"
  - "two-phase zkSNARK proof generation"
  - "Groth16 split prover"
  - "delegatable payments zkSNARK"
  - "split zero-knowledge"
aliases:
  - "split prover zkSNARK"
  - "two-phase zkSNARK proving"
  - "partial-witness delegated proving"
domains:
  - "zero-knowledge-proofs"
topics:
  - "split-prover-zksnarks"
  - "private-delegated-proving"
  - "distributed-proof-generation"
  - "zk-snarks"
tags:
  - "nahida/knowledge"
  - "nahida/method-family"
freshness_status: "fresh"
last_synthesized: "2026-06-21"
valid_until: "2026-07-21"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-21"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-split-prover-zksnarks"
source_refs:
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
confidence: "high"
trust_tier: "primary"
---

# Split prover zkSNARKs

## 定义与范围

- 定义: Split prover zkSNARKs 是一种二阶段 zkSNARK proving 方法族：第一阶段 prover 在只知道早到 witness 的情况下生成隐私保护的 aux state，第二阶段 prover 在晚到 witness 出现后完成标准 zkSNARK proof，且 verifier 不需要知道 proof 是否被拆分生成。
- 不包含: 普通多机 distributed proving、完整 witness 的私有外包、SNARK proof aggregation、任意 recursive/IVC proof system，或某篇论文里的 Groth16 公式细节。
- Canonical terms: `split prover zkSNARKs`, `split prover`
- Aliases/query keys: partial-witness delegated proving, two-phase zkSNARK proving, Groth16 split prover
- Standalone completeness check: 本节点说明问题、边界、方法路线、代表 source、与 private delegated proving / recursion 的关系；Groth16 构造细节留在 source note。
- Retrieval role: 查询“witness 分两次才知道时如何提前算 zkSNARK”“Bob 代 Alice 完成 proof 但不能盗用 witness”“split prover 和 recursive SNARK 区别”时优先读本节点。
- Update scope: 新 split prover construction、PLONK/STARK/transparent split proving、delegatable payments implementation、Groth16/ROM lower-bound follow-up。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[04_Knowledge/zero-knowledge-proofs/research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

Private delegated proving 之前在 vault 中主要由 [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]] 支撑: delegator 已经拥有完整 witness，但希望把 prover computation 外包给多个 worker，同时隐藏 witness。Split prover zkSNARKs 打开的是另一个常见场景: witness 本身按时间分段到达。Alice 可以先用早到 witness 做大部分工作，再把一个不会泄露早到 witness 的 aux state 给 Bob；Bob 等晚到 witness 出现后完成 proof。

这个问题在支付、匿名凭证、密文有效性证明中很自然。比如支付系统里，旧 coin membership/ownership 可能早就知道，但最终金额和新输出要到交易时才确定。Split prover 的核心不是“让 Bob 更快”，而是“让 Alice 预先完成授权相关证明工作，同时不让 Bob 获得伪造授权的能力”。

## 基础概念判断

- 是否是基础概念/方向/问题: `method_family` under [[private-delegated-proving|Private delegated proving]].
- 为什么足够通用: 它组织一类可复用目标组合：partial witness availability、early proving、late completion、aux privacy、unchanged verifier。后续 Groth16/PLONK/STARK split proving 都可进入同一框架。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] 是当前代表 source；本节点保存的是问题族与比较轴。
- 需要引用的更基础 Knowledge: [[private-delegated-proving|Private delegated proving]], [[distributed-proof-generation|Distributed proof generation]], [[zk-snarks|zk-SNARKs]]。
- 不应拆出的实例/协议/来源: 当前 Groth16 split prover construction、`H` matrix optimization、lower bound 只留在 source note，除非后续多来源证明需要独立 Groth16-specific child。

## 解决的问题

Split prover zkSNARKs 解决的是“proof generation 的时间结构”和“委托授权边界”:

- Early witness utilization: `wI` 很早可用，不能等完整 witness 到齐后才开始全部 prover work。
- Late witness completion: `wII` 在交易/查询/消息确定后才出现，第二阶段必须能补齐 proof。
- Aux privacy: 给 Bob 的 aux 不能泄露 `wI`，除了第二阶段继续计算必须知道的 `CI(xI,wI)` 输出。
- Authorization boundary: Bob 不应能凭 aux 独立发起 Alice 未授权的 proof/transaction。
- Verifier compatibility: verifier 不应知道 proof 是 split 生成的；部署方最好保留原 proof/verifier 接口。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[private-delegated-proving|Private delegated proving]] | child_of / phase-aware delegation route | Split Prover defines private aux handoff to a second prover; Siniel defines full-witness private outsourcing. | active_seed |
| [[zk-snarks|zk-SNARKs]] | depends_on | Current construction is Groth16-based and preserves Groth16 verification. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Groth16 split prover | protocol-instance child candidate | 当前只有单篇 primary source，细节放在 source note 即可；若后续 Groth16 split proving 被多来源复用，可拆。 | [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | review |
| transparent / Fiat-Shamir-ROM split proving | open route | 论文指出 random-oracle Fiat-Shamir challenges 依赖整段 transcript，split precomputation 不明显。 | Split Prover Section 1.3 | gap |
| delegatable payments | application route | 论文给出 Zerocash-style 应用动机，但没有实现/benchmark。 | Split Prover Section 1.2 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Two-phase prover interface | 把 prover 拆成 `PI(xI,wI)->aux` 与 `PII(xII,wII,aux)->pi`，verifier 保持原样。 | 计算自然能分成早到 witness 和晚到 witness 两部分。 | 需要定义可泄露的第一阶段输出；不是任意电路都天然有好的 split。 | [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| Split zero-knowledge for aux | aux 应可由 simulator 从 public data 与 `CI(xI,wI)` 生成，避免泄露 `wI`。 | Bob 需要继续计算但不应学习 Alice 的授权 witness。 | `CI` 输出本身可能泄露，需要应用层谨慎选择 boundary。 | [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| Groth16 quotient decomposition | 把 Groth16 `pi3` 的 quotient contribution 拆成 first-only、cross 和 second-only 项。 | 目标 proof system 是 Groth16/R1CS/QAP-like route。 | Groth16-specific；不自动迁移到 PLONK/STARK/FRI。 | [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| Small-second-witness precomputation | 当晚到 witness/circuit 小时，在 setup 中预计算二阶段 quotient quadratic form material。 | `m2` 足够小，且可接受 specialized setup material。 | 第二阶段可到 `O(m2^2)`，但 setup/aux 结构和 lower bound 都是 Groth16-specific。 | [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| Recursive/IVC alternative | 用 IVC/recursive SNARKs 按步骤证明，再递归压缩。 | 多阶段 computation 和递归 verifier 可接受。 | verifier/proof semantics、assumption model、challenge dependency 和 split privacy 都不同；通过 bridge 比较而非替代。 | [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | paper | Initiates split prover zkSNARKs; defines split correctness/ZK; gives Groth16 construction and tight second-phase lower bound. | Single primary source; implementation/evaluation not provided; Groth16-specific construction; canonical URL not fetched. | p1-p23 |

## 正反例约束

- 正确: 把 Split Prover 当作 private delegated proving 的 phase-aware child：它强调 partial witness 和 aux privacy。
- 正确: 把 Groth16 construction 细节留在 source note；上层只保存方法族和边界。
- 正确: 通过 bridge 比较 IVC/recursive SNARKs，而不是把 split prover 归入 folding schemes。
- 错误: 把 split prover 等同于 Siniel/EOS/zkSaaS；这些处理完整 witness 外包、MPC/worker privacy 与在线交互问题。
- 错误: 把 split prover 当成 proof aggregation；它生成一个 proof，不是聚合多个 proofs。

## 当前综合

- Evidence window: `2026-06-21` to `2026-06-21`.
- Freshness: `fresh` for source absorption; not a latest-news claim.
- Valid until: `2026-07-21`.
- 综合: Split prover zkSNARKs 给 private delegated proving 增加了“witness arrival time”这一轴。Siniel-style route 处理完整 witness 的隐私外包；Split Prover route 处理早到 witness 的预计算和晚到 witness 的安全补全。Groth16 construction 表明这种 split 可以在保持 verifier 不变的前提下完成，并且二阶段复杂度对 Groth16 已接近最优。它也暴露一个重要边界：IVC/recursive SNARKs 能做多阶段证明，但 verifier semantics、cryptographic model 和 transcript/challenge 依赖不同，不能直接替代 split-prover aux privacy。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing source only; no external latest evidence fetched.
- Latest industrial focus summary: no implementation/repository evidence in this run.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: PLONK/STARK split proving source, Groth16 implementation, delegatable-payment prototype, or follow-up addressing random-oracle Fiat-Shamir barriers.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | Creates phase-aware delegated proving route; adds Groth16-compatible two-phase proving and tight second-phase lower bound. | 定义; 解决的问题; 方法族; Bridge Links; 缺口与队列 | yes | Absorb Groth16 foundation and later split-prover follow-ups. |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks; zero-knowledge-proofs/recursion-and-folding` | contrast, design_boundary, phase_decomposition, non_transfer_boundary | Both split work over time, but split prover preserves the original verifier and aux privacy; recursive/IVC systems change proof/verifier composition and do not automatically provide authorization-preserving aux handoff. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-split-prover-zksnarks | is_a | nahida-knowledge-private-delegated-proving | Split Prover p1-p11 | high | active_seed |
| nahida-knowledge-split-prover-zksnarks | depends_on | nahida-knowledge-zk-snarks | Split Prover Groth16 construction p7-p20 | high | active_seed |
| nahida-knowledge-split-prover-zksnarks | contrasts_with | nahida-knowledge-recursion-and-folding | Split Prover p6-p7; bridge note | high | active_seed |
| nahida-knowledge-split-prover-zksnarks | evidenced_by | vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md | source note | high | active_seed |
| nahida-knowledge-split-prover-zksnarks | bridges_to | nahida-bridge-split-prover-zksnarks-to-recursion-and-folding | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Groth16 primary source/foundation thin. | 当前 construction 依赖 Groth16，但 Split Prover 不是 Groth16 foundation source。 | nahida-update / nahida-research-search | high | queued |
| PLONK/STARK/transparent split proving sources 缺。 | 论文指出 random-oracle Fiat-Shamir route 有 precomputation barrier；后续来源可能改变 taxonomy。 | nahida-daily-fetch / nahida-research-search | high | watch |
| Implementation/repository evidence 缺。 | 需要判断 setup material、aux size、二阶段 runtime 在真实 circuits 上是否实用。 | nahida-github-repo-analyze / nahida-research-search | medium | queued_if_repo_known |
| Delegatable payments application source 缺。 | 论文给出 Zerocash-style motivating example，但没有完整 system design/evaluation。 | nahida-update | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-split-prover-zksnarks | Created split prover zkSNARKs child node under private delegated proving from deep-read absorption. | 1 source note | codex |
