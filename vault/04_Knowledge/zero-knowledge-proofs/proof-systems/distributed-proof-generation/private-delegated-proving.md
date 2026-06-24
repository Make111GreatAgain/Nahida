---
id: "nahida-knowledge-private-delegated-proving"
title: "Private delegated proving"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "subproblem"
hierarchy_level: "subproblem"
file_slug: "private-delegated-proving"
domain_id: "zero-knowledge-proofs"
direction_id: "proof-systems"
parent_knowledge_refs:
  - "nahida-knowledge-distributed-proof-generation"
child_knowledge_refs:
  - "nahida-knowledge-split-prover-zksnarks"
ontology_path:
  - "zero-knowledge-proofs"
  - "proof-systems"
  - "distributed-proof-generation"
  - "private-delegated-proving"
primary_ontology_path: "zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/polynomial-commitments/kzg-commitments"
relation_edges:
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "is_a"
    to: "nahida-knowledge-distributed-proof-generation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "depends_on"
    to: "nahida-knowledge-kzg-commitments"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
      - "vault/05_Bridges/private-delegated-proving-to-kzg-commitments.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "bridges_to"
    to: "nahida-bridge-private-delegated-proving-to-kzg-commitments"
    evidence_refs:
      - "vault/05_Bridges/private-delegated-proving-to-kzg-commitments.md"
      - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
      - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "has_child"
    to: "nahida-knowledge-split-prover-zksnarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-private-delegated-proving"
    relation: "bridges_to"
    to: "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
    evidence_refs:
      - "vault/05_Bridges/split-prover-zksnarks-to-recursion-and-folding.md"
      - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-private-delegated-proving-to-kzg-commitments"
  - "nahida-bridge-split-prover-zksnarks-to-recursion-and-folding"
source_note_refs:
  - "vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md"
  - "vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md"
  - "vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md"
representative_source_refs:
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
query_keys:
  - "Private delegated proving"
  - "private delegation of zkSNARK prover"
  - "privacy-preserving zkSNARK delegation"
  - "delegated zkSNARK prover"
  - "Siniel"
  - "EOS"
  - "zkSaaS"
  - "collaborative zkSNARKs"
  - "Efficient Outsourcing of SNARKs"
  - "PIOP consistency checker"
  - "isolated delegated SNARK protocol"
  - "collaborative delegated SNARK protocol"
  - "universal-setup zkSNARK delegation"
  - "witness-hiding prover delegation"
  - "split prover zkSNARKs"
  - "partial witness zkSNARK delegation"
  - "two-phase zkSNARK proving"
aliases:
  - "privacy-preserving proof delegation"
  - "private zkSNARK prover delegation"
  - "delegated proving with hidden witness"
  - "partial-witness delegated proving"
domains:
  - "zero-knowledge-proofs"
topics:
  - "private-delegated-proving"
  - "distributed-proof-generation"
  - "zk-snarks"
  - "kzg-commitments"
  - "eos"
  - "piop-based-zksnark-delegation"
  - "malicious-secure-prover-delegation"
  - "universal-setup-zksnark-delegation"
  - "split-prover-zksnarks"
tags:
  - "nahida/knowledge"
  - "nahida/subproblem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-21"
evidence_window_end: "2026-06-23"
created: "2026-06-21"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-siniel-private-delegated-proving"
  - "nahida-knowledge-20260623-eos-private-delegated-proving"
  - "nahida-knowledge-20260621-split-prover-zksnarks"
source_refs:
  - "sha256:f45eb8cc0d43b8c90247106c3728eee60b2d462f50d10cfdf6ad0f9ff406e552"
  - "sha256:c13a2c3e26f0c7a11a46b4050540dbddbc3efe7fa36a2188182867b86bbb47c4"
  - "sha256:5714931881cf7552ba2387ec83bd20467425dd84fbb249bc725e222bcd3d41f0"
confidence: "medium"
trust_tier: "primary"
---

# Private delegated proving

## 定义与范围

- 定义: Private delegated proving 是 distributed proof generation 的一个子问题，目标是让弱 delegator 把昂贵的 proof generation 外包给多个 worker，同时不向 worker 泄露 private witness，并尽量减少 delegator 在线交互。
- 不包含: 单纯把 prover work 分给多台自有机器但允许机器看到 witness 分片的 distributed ZKP；单个系统名 Siniel/EOS/zkSaaS；单次 AWS benchmark；通用 secure multiparty computation 全景。
- Canonical terms: `private delegated proving`, `private delegation of zkSNARK prover`
- Aliases/query keys: privacy-preserving proof delegation, delegated zkSNARK prover, witness-hiding prover delegation, Siniel, EOS, zkSaaS
- Standalone completeness check: 本节点说明该子问题的边界、威胁模型、方法路线、代表来源和与 KZG/distributed proving 的关系；Siniel 协议细节仍在 source note。
- Retrieval role: 查询“怎么外包 zkSNARK prover 但不泄露 witness”“Siniel 和 EOS/zkSaaS/DIZK/Pianist 区别”时优先读本节点。
- Update scope: EOS、zkSaaS、collaborative zkSNARKs、private delegation、MPC/FHE delegated proving、distributed ZKP privacy-preserving extension sources。
- Domain dynamics note: not_applicable; parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

ZK proof systems 往往把 verifier cost 压得很低，但 prover cost 可能高到移动设备、浏览器客户端或普通用户设备无法承担。普通 distributed proving 主要关心 prover-side time/memory 横向扩展；private delegated proving 额外要求 worker 不应学到 witness，且 delegator 不应因为在线参与 MPC/consistency checking 而重新成为瓶颈。

当前 source-backed evidence 有三条互补路线。[[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]] 处理 universal-setup PIOP+PCS zkSNARK 的私有委托证明：delegator 把 witness secret-share 给多 worker，并通过 PIOP/PCS consistency checker 防止恶意 worker 让最终 accept/reject 泄露 witness 信息。[[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]] 在同一 full-witness delegation 问题上调整交互边界：把 consistency checking 更大程度移到 worker 侧，降低 delegator 在线参与，但安全模型变为 honest-majority secure-with-abort。[[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] 处理“witness 自然分两阶段到达，早到 witness 要先预计算且不泄露给第二阶段 prover”的问题。zkSaaS、Ozdemir/Boneh collaborative zkSNARKs、FHE-based delegation 仍主要作为 related-work 对比，尚未成为独立 source evidence。

## 基础概念判断

- 是否是基础概念/方向/问题: `subproblem` under [[distributed-proof-generation|Distributed proof generation]].
- 为什么足够通用: 它组织一类反复出现的目标组合：prover outsourcing、witness privacy、worker malicious security、delegator online/offline cost。Siniel、EOS、zkSaaS、FHE-based delegation、collaborative zkSNARKs 都可进入同一比较框架。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Siniel 是 source instance；本节点保存的是“隐私保护的证明外包”问题族及比较轴。
- 需要引用的更基础 Knowledge: [[distributed-proof-generation|Distributed proof generation]], [[zk-snarks|zk-SNARKs]], [[kzg-commitments|KZG commitments]]。
- 不应拆出的实例/协议/来源: Siniel、EOS、zkSaaS 默认作为 representative/source instances，除非后续多来源和重复查询证明需要 protocol-instance child。

## 解决的问题

Private delegated proving 同时优化四个目标:

- Delegator resource: 弱设备不用本地运行完整 prover。
- Witness privacy: worker 不应看到 private witness 或可拼出的 witness 信息。
- Malicious-worker handling: worker 偏离协议、篡改 share、生成错误 prover polynomial 或错误 proof 时应被检测并中止。
- Online interaction: delegator 不应每个 PIOP round 都在线等待 worker 并运行 consistency checker。

这些目标彼此张力明显。EOS 安全更强但 delegator 在线交互重；zkSaaS 可全外包但只有 semi-honest 安全；Siniel 牺牲到 honest-majority secure-with-abort 模型，换取 delegator 在线阶段无需参与。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[distributed-proof-generation|Distributed proof generation]] | child_of / privacy-preserving subproblem | Siniel distinguishes private delegation from DIZK/deVirgo/Pianist-style distributed ZKP that does not hide witness portions. | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[split-prover-zksnarks|Split prover zkSNARKs]] | method_family | partial witness / two-phase proving 是可复用问题轴：它不是 Siniel-style full-witness outsourcing，也不是普通 proof aggregation。 | [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] p1-p23 | active_seed |
| EOS-style delegated proving | protocol instance | 已有 primary source，但目前仍可作为 method row 而不是独立 child；只有在后续出现多篇 EOS-family follow-up/实现查询时再拆。 | [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]] p1-p18 | active_seed |
| zkSaaS-style delegated proving | protocol instance | 需要 zkSaaS primary source 后才能拆；当前只来自 Siniel related work。 | Siniel p2-p5 | review |
| FHE-based oblivious proving | method section | 与 MPC/multi-worker route 不同，但当前只有 related-work mention。 | Siniel p2-p5 | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| EOS interactive PIOP consistency checking | Delegator participates during online PIOP rounds, using targeted PIOP/PCS consistency checks instead of generic malicious MPC for the entire prover. | Strong witness privacy against colluding workers is required and the delegator can remain online during checker rounds. | Delegator online interaction and waiting remain usability bottlenecks; benchmark values are MARLIN/arkworks/source-local. | [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS]] |
| Full outsourcing under semi-honest workers | Delegator sends shares/material and workers jointly compute without later delegator interaction. | Honest-majority and semi-honest assumptions are acceptable. | Malicious worker behavior can compromise protocol security/privacy. | zkSaaS as described by [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]] |
| Siniel worker-side consistency checking | Delegator provides offline shares, tags, keys and Beaver triples; workers run witness and PIOP consistency checkers using KZG openings and authentication tags. | Honest majority, secure-with-abort, PIOP+PCS zkSNARK setting; KZG instantiation evaluated. | Security weaker than EOS dishonest-majority; offline communication and worker checks add overhead; source evaluates Marlin/arkworks only. | [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel]] |
| Split prover zkSNARKs | Alice computes a privacy-preserving aux state from early witness; Bob later completes a standard Groth16 proof from late witness without learning the first witness. | Witness naturally arrives in two phases and the verifier must remain unchanged. | Current construction is Groth16-specific; setup is specialized; PLONK/STARK/ROM split proving remains open. | [[split-prover-zksnarks|Split prover zkSNARKs]]; [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover]] |
| FHE-based single-server delegation | Delegator outsources encrypted witness/computation to one server. | Multi-worker assumption is undesirable and FHE overhead is acceptable. | High computation overhead in the paper's related-work framing. | related-work mention only |
| Plain distributed ZKP | Split prover work across machines without witness privacy from those machines. | Prover time/memory is the main bottleneck and machines are trusted/owned. | Does not solve private delegated proving by itself; may be complementary to Siniel. | [[distributed-proof-generation|Distributed proof generation]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | paper | Creates first source-backed seed for private delegated proving: no delegator online interaction, worker-side witness/PIOP consistency checks, honest-majority malicious-worker security. | Single source; EOS/zkSaaS/DIZK primary sources not yet absorbed; performance is Marlin/arkworks/AWS source-local. | p1-p22, Appendices p24-p30 |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | paper | Adds primary evidence for strong private delegation of universal-setup zkSNARK provers: isolated/collaborative worker modes, PIOP consistency checker, efficient MPC circuits for PIOP/KZG prover operations, mobile/cloud evaluation. | Delegator remains online for consistency checks; implementation/evaluation are MARLIN/arkworks/source-local; repository not analyzed. | p1-p18 |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | paper | Adds phase-aware delegated proving: early witness precomputation, aux-state split zero-knowledge, late completion by Bob, unchanged Groth16 verifier, tight second-phase lower bound. | Single source; Groth16-specific construction; implementation and canonical URL not fetched. | p1-p23 |

## 正反例约束

- 正确: 把 Siniel/EOS/zkSaaS 当作 protocol/source instances，比较 delegator interaction、witness privacy、worker adversary model 和 performance。
- 正确: 与 [[distributed-proof-generation|Distributed proof generation]] 保持父子关系：private delegated proving 是 privacy-aware subproblem，不替代 data-parallel/distributed prover scalability。
- 错误: 把 Siniel 建成一个上层 foundation node；Siniel 是 source/system instance。
- 错误: 把 DIZK/deVirgo/Pianist 当成已经解决 witness privacy；Siniel 明确说这些路线不隐藏 worker 拿到的 witness portion。

## 当前综合

- Evidence window: `2026-06-21` to `2026-06-23`.
- Freshness: `fresh` for source absorption; not a latest-news claim.
- Valid until: `2026-07-23`.
- 综合: 当前节点有三类 source-backed private delegated proving。EOS 让 distributed proof generation 多出“在强隐私/恶意 worker 场景下，delegator 如何用 targeted PIOP/PCS consistency checking 私有外包 universal-setup zkSNARK prover”的轴；Siniel 在 full-witness outsourcing 上进一步把检查移动到 worker 侧，用 honest-majority secure-with-abort 换取 delegator 在线阶段更少参与；Split Prover 则多出“witness 分阶段到达时如何预计算且保持授权边界”的轴: early witness 是否能先证明、aux 是否泄露 `wI`、第二阶段 prover 是否能独立伪造 proof、verifier 是否保持不变。三者都不推翻 Pianist/Hekaton/DIZK 这类横向扩展路线；它们说明纯 distributed proving、full-witness private delegation、partial-witness split proving 是三个相邻但不同的问题。

## 领域态势

- Research dynamics note: not_applicable
- Dynamics freshness: not_applicable
- Latest academic focus summary: existing source only; no external latest evidence fetched.
- Latest industrial focus summary: repository/implementation evidence sparse; Siniel PDF does not provide a repository URL in extracted text.
- Open-problem summary: see `缺口与队列`.
- Next refresh trigger: EOS/zkSaaS/collaborative zkSNARKs/private delegation primary sources or Siniel repository analysis.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark|Siniel: Distributed Privacy-Preserving zkSNARK]] | Adds private delegated proving as a privacy-aware child route under distributed proof generation; introduces worker-side consistency checking through tags and KZG openings. | 定义; 解决的问题; 方法族; Bridge Links; 缺口与队列 | yes | Absorb zkSaaS/OB22 primary sources to mature comparison. |
| [[sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers|EOS: Efficient Private Delegation of zkSNARK Provers]] | Closes the EOS primary-source gap; adds isolated/collaborative delegated SNARK protocols, PIOP consistency checker, efficient PIOP/KZG prover circuits and mobile/cloud evaluation. | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links; 缺口与队列 | yes | Analyze EOS repo if available; compare with OB22/zkSaaS primary sources. |
| [[sha256-5714931881cf-split-prover-zero-knowledge-snarks|Split Prover Zero-Knowledge SNARKs]] | Adds partial-witness/two-phase delegated proving route; creates [[split-prover-zksnarks|Split prover zkSNARKs]] child and bridge to recursion/folding. | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | Track PLONK/STARK split proving and Groth16 implementation evidence. |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[private-delegated-proving-to-kzg-commitments|Private delegated proving -> KZG commitments]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving; zero-knowledge-proofs/polynomial-commitments/kzg-commitments` | dependency, verification_enabler, implementation_reuse | KZG commitments/openings help workers check share/prover-polynomial consistency; KZG does not provide MPC secrecy, honest-majority threshold, or full delegation protocol by itself. | active_seed |
| [[split-prover-zksnarks-to-recursion-and-folding|Split prover zkSNARKs -> Recursion and folding]] | `zero-knowledge-proofs/proof-systems/distributed-proof-generation/private-delegated-proving/split-prover-zksnarks; zero-knowledge-proofs/recursion-and-folding` | contrast, design_boundary, phase_decomposition | Both split work over time, but split prover preserves the original verifier and protects aux handoff; recursive/IVC systems change proof composition and do not automatically solve authorization-preserving aux privacy. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-private-delegated-proving | is_a | nahida-knowledge-distributed-proof-generation | Siniel p4-p5 related-work distinction | high | active_seed |
| nahida-knowledge-private-delegated-proving | depends_on | nahida-knowledge-zk-snarks | Siniel p1-p2, p5-p6 | high | active_seed |
| nahida-knowledge-private-delegated-proving | depends_on | nahida-knowledge-kzg-commitments | Siniel p10-p18 | high | active_seed |
| nahida-knowledge-private-delegated-proving | evidenced_by | vault/03_Sources/papers/sha256-f45eb8cc0d43-siniel-distributed-privacy-preserving-zksnark.md | source note | high | active_seed |
| nahida-knowledge-private-delegated-proving | evidenced_by | vault/03_Sources/papers/sha256-c13a2c3e26f0-eos-efficient-private-delegation-zksnark-provers.md | source note | high | active_seed |
| nahida-knowledge-private-delegated-proving | bridges_to | nahida-bridge-private-delegated-proving-to-kzg-commitments | bridge note | high | active_seed |
| nahida-knowledge-private-delegated-proving | has_child | nahida-knowledge-split-prover-zksnarks | [[split-prover-zksnarks|Split prover zkSNARKs]]; source note | high | active_seed |
| nahida-knowledge-private-delegated-proving | evidenced_by | vault/03_Sources/papers/sha256-5714931881cf-split-prover-zero-knowledge-snarks.md | source note | high | active_seed |
| nahida-knowledge-private-delegated-proving | bridges_to | nahida-bridge-split-prover-zksnarks-to-recursion-and-folding | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| zkSaaS primary sources 未吸收。 | 需要区分 semi-honest full outsourcing、FHE-based single-server delegation 与 Siniel。 | nahida-update / nahida-research-search | high | queued |
| Collaborative zk-SNARKs / Ozdemir-Boneh source 未吸收。 | 影响 private delegation 与 distributed secret/proof generation 的历史脉络。 | nahida-update | medium | queued |
| EOS repository/artifact 未分析。 | PDF 已补齐 primary protocol/evaluation evidence，但代码架构、API 和可复现实验还不在 vault。 | nahida-github-repo-analyze / nahida-research-search | medium | queued_if_repo_known |
| Siniel repository 未分析。 | PDF 只有实现描述；需要代码架构、可复现脚本、维护状态和实际 API。 | nahida-github-repo-analyze | medium | queued_if_repo_known |
| MPC foundations thin. | Shamir/authentication tags/Beaver triples 目前来自 Siniel source-local explanation，缺稳定 foundation。 | nahida-research-search | medium | foundation_gap |
| PLONK/STARK/transparent split prover sources 缺。 | Split Prover 当前 Groth16-specific；需要判断 partial-witness route 是否能迁移到其他 proof systems。 | nahida-daily-fetch / nahida-research-search | high | watch |
| Split prover implementation/repo evidence 缺。 | 需要检验 aux size、setup material 和 second-phase runtime 在真实 delegatable-payment circuits 上是否实用。 | nahida-github-repo-analyze / nahida-research-search | medium | queued_if_repo_known |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-21 | nahida-knowledge-20260621-siniel-private-delegated-proving | Created private delegated proving seed node from Siniel absorption. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-eos-private-delegated-proving | Added EOS primary source; closed the EOS missing-source gap and refined full-witness private delegation taxonomy. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-split-prover-zksnarks | Added phase-aware split prover child route and recursion/folding contrast bridge. | 1 source note | codex |
