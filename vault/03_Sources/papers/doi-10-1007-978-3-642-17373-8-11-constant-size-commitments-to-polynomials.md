---
id: "doi-10-1007-978-3-642-17373-8-11"
title: "Constant-Size Commitments to Polynomials and Their Applications"
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
  - "p1-p4 introduction, related work, assumptions"
  - "p5-p10 definition, PolyCommitDL, PolyCommitPed, features, batch opening"
  - "p10-p16 applications to VSS, nearly ZKS/ZK-EDB, CES, credentials"
  - "p17-p18 open problems and references"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1007/978-3-642-17373-8_11"
doi: "10.1007/978-3-642-17373-8_11"
venue: "ASIACRYPT 2010"
year: "2010"
pdf_pages: 18
pdf_sha256: "8d28caed65d93892e1fc7fa255311d2710e60e86eae00c2f7bbdb510e4911104"
local_pdf: "~/Desktop/paper/6477178.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/6477178-8d28caed65d9-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "polynomial-commitments"
topic_ids:
  - "kzg-commitments"
ontology_path:
  - "zero-knowledge-proofs"
  - "polynomial-commitments"
  - "kzg-commitments"
primary_ontology_path: "zero-knowledge-proofs/polynomial-commitments/kzg-commitments/doi-10-1007-978-3-642-17373-8-11"
secondary_ontology_paths:
  - "cryptography/verifiable-secret-sharing/polynomial-commitments/doi-10-1007-978-3-642-17373-8-11"
path_update_status: "propagated"
domains:
  - "zero-knowledge-proofs"
topics:
  - "polynomial-commitments"
  - "kzg-commitments"
aliases:
  - "KZG"
  - "Kate-Zaverucha-Goldberg commitments"
tags:
  - "nahida/source"
  - "paper"
  - "zero-knowledge-proofs"
  - "polynomial-commitments"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "polynomial-commitments"
  problem:
    - "succinct polynomial evaluation proofs"
  method_family:
    - "pairing-based commitments"
    - "structured reference string"
  system_layer:
    - "cryptographic primitive"
  evaluation_context:
    - "communication complexity"
  application:
    - "verifiable secret sharing"
    - "zero-knowledge sets"
    - "credentials"
  bridge:
    - "cryptographic commitments -> ZKP proof systems"
created: "2026-06-11"
updated: "2026-06-11"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260611-kzg-polynomial-commitments"
source_refs:
  - "doi:10.1007/978-3-642-17373-8_11"
  - "pdf:~/Desktop/paper/6477178.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "zero-knowledge-proofs -> polynomial-commitments"
secondary_directions:
  - "cryptography -> verifiable-secret-sharing"
classification_status: "accepted"
classification_confidence: "high"
classification_evidence:
  - "title"
  - "known DOI"
  - "abstract"
  - "full PDF deep read"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0003"
queue_status: "absorbed"
---

# Constant-Size Commitments to Polynomials and Their Applications

## 论文身份

- 标题: Constant-Size Commitments to Polynomials and Their Applications
- 作者: Aniket Kate, Gregory M. Zaverucha, Ian Goldberg
- 机构: MPI-SWS, Certicom Research, University of Waterloo
- 会议/期刊: ASIACRYPT 2010
- 年份: 2010
- DOI: `10.1007/978-3-642-17373-8_11`
- 链接: https://doi.org/10.1007/978-3-642-17373-8_11
- 本地 PDF: `~/Desktop/paper/6477178.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/6477178-8d28caed65d9-pages.txt`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 18
- 已覆盖章节/页码: p1-p18 full text
- 未覆盖章节/页码: extended version 中的完整 proofs 未读取，本文多处说明 proofs 在 extended version
- Extraction gaps: 数学公式抽取存在换行/上标丢失，但核心算法和定理可读

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1-p3 | Introduction | 定义 polynomial commitment 需求，说明 constant-size commitment/opening/batch opening 和四个应用 | 贡献定位 | PCS foundation |
| p4-p5 | Preliminaries | pairing groups, DL, t-SDH, t-polyDH, t-BSDH assumptions | 安全假设 | 后续 theorem 边界 |
| p5-p7 | Definition / PolyCommitDL | 六个算法定义，`C=g^{phi(alpha)}`，quotient witness，VerifyEval pairing equation | KZG 核心构造 | binding under t-SDH, hiding under DL |
| p8-p9 | PolyCommitPed / features | Pedersen-style random polynomial, unconditional hiding, homomorphism, trapdoor, indistinguishability | 隐私增强 | PolyCommitDL/Ped distinction |
| p9-p10 | Batch opening | 对一组 evaluation 用单个 witness 和 remainder polynomial 证明 | 扩展机制 | binding under t-BSDH |
| p10-p13 | VSS | 用 single polynomial commitment 替换 Feldman VSS 的 O(n) commitments，使 broadcast O(1) | 应用一 | eVSS |
| p13-p15 | Nearly ZKS/ZK-EDB | 放松隐藏集合大小，得到 constant/short proof size | 应用二 | Communication reduction |
| p15-p16 | CES / credentials | 签名 polynomial commitment 支持 selective disclosure | 应用三/四 | Batch opening useful |
| p17 | Open problems | 更弱假设、更多协议、计算成本优化 | 限制 | 未来方向 |

## 核心精读笔记

### 背景、动机与问题边界

传统 commitment 可以对消息 binding/hiding，但对 polynomial 只提交整体字符串会迫使 opening 暴露整个 polynomial；而 VSS、credential、ZK database 等应用常常只需要证明某个点的 evaluation `phi(i)` 与 committed polynomial 一致。对 coefficients 分别 commitment 可验证 evaluation，但 commitment size 随 degree 线性增长。

本文的目标是通信复杂度: 用 constant-size commitment 和 constant-size opening/witness 来证明 polynomial evaluation，同时允许 batch opening 仍保持 constant communication overhead。它不主张消除 setup 成本，反而明确 global system parameters 大小为 `O(t)`。证据锚点: p1-p3。

### 模型、假设与定义

Polynomial commitment scheme 包含 `Setup`, `Commit`, `Open`, `VerifyPoly`, `CreateWitness`, `VerifyEval` 六个算法。安全性包括 correctness、polynomial binding、evaluation binding、hiding。scheme 允许把一组 messages 与唯一 indices 关联后插值为 polynomial，从而把 vector/list commitment 转化为 polynomial commitment。

本文使用 symmetric bilinear pairing group，并依赖 DL、t-SDH、t-polyDH、t-BSDH 等假设。`Setup` 输出 `PK=<G,g,g^alpha,...,g^{alpha^t}>`，`SK=alpha` 不在后续算法中使用，但构成 structured reference string/trapdoor。证据锚点: p4-p6。

### 方法、协议或系统机制

PolyCommitDL 基于一个简单代数事实: 对任意 index `i`，`x-i` 整除 `phi(x)-phi(i)`。commitment 是 `C=g^{phi(alpha)}`，witness 是 quotient polynomial `psi_i(x)=(phi(x)-phi(i))/(x-i)` 在 secret point `alpha` 的承诺 `w_i=g^{psi_i(alpha)}`。验证等式用 pairing 检查 `e(C,g)` 是否等于 witness 对 `alpha-i` 的贡献再乘 evaluation term。这样 verifier 不知道 `alpha` 或 polynomial 全体，也能检查 `phi(i)`。

PolyCommitPed 在 DL construction 基础上加入随机 polynomial `hat_phi(x)`，commitment 变为 `g^{phi(alpha)} h^{hat_phi(alpha)}`，以获得 unconditional hiding。两种 construction 都有 homomorphism 特性。batch opening 针对一组 indices `B`，用 remainder polynomial `r(x)` 和单个 witness `w_B` 一次证明所有 opened evaluations；其 binding 依赖 t-BSDH。

应用层面，eVSS 用单个 polynomial commitment 替换 Feldman VSS 中对所有 coefficients 的 commitments，使 dealer broadcast 从 O(n) 降到 O(1)。Nearly ZKS/ZK-EDB 放松“不隐藏集合大小”需求，得到更短 membership/non-membership proofs。CES/credentials 中，issuer 对 commitment 签名，holder 可选择性展示若干 attributes，并用 batch opening 降低通信。证据锚点: p5-p16。

### 理论、证明或正确性论证

本文正文给出 security theorems，完整证明放在 extended version。Theorem 1 说明 PolyCommitDL 在 DL 和 t-SDH 假设下是 secure polynomial commitment；Theorem 2 说明 PolyCommitPed 在 t-SDH 下安全且 hiding unconditional；Theorem 3 说明 batch opening binding 依赖 t-BSDH；Theorem 4 说明 strong correctness 依赖 t-polyDH；Theorem 5 说明 eVSS 在 DL、t-SDH、t-polyDH 下实现 synchronous VSS 的 secrecy/strong correctness 等性质。

需要注意，正文多处安全证明不完整展开，精读结论对 theorem statement 和 construction details 高置信，但对 reduction proof 细节需读取 extended version 才能升级为完整 proof note。证据锚点: p7-p13。

### 实验、评估或案例

本文没有实现 benchmark，评估主要是 asymptotic communication comparison。核心量化结论包括: commitment 是 single group element；single evaluation witness 是 single group element；batch opening 的 communication overhead constant；eVSS broadcast size 从 O(n) 降到 O(1)；nearly ZK-EDB proof size 相比文献中短 proof ZK-EDB 至少小约 16 倍。证据锚点: p1-p3, p10-p15。

### 作者结论与我的判断

这篇论文是 `polynomial commitments` 的 foundation source，也是后续常称 KZG commitments 的原始来源。它直接支持 ZKP/SNARK/rollup 中“短 commitment + 短 evaluation proof”的核心 primitive，但本文本身主要写在通用 cryptographic applications 语境中，不是现代 SNARK protocol paper。Nahida 中应把它作为 `zero-knowledge-proofs/polynomial-commitments/kzg-commitments` 的 topic seed，并在后续用 IPA/FRI/PCS comparison、PLONK/KZG usage、trusted setup ceremony 和 pairing assumptions 补全。

## 层级候选分类

- L1 Domain candidate: `zero-knowledge-proofs`
- L2 Direction candidate: `polynomial-commitments`
- L3 Topic/content cluster candidates: `kzg-commitments`
- Ontology path: `zero-knowledge-proofs/polynomial-commitments/kzg-commitments/doi-10-1007-978-3-642-17373-8-11`
- 备选归属: `cryptography/verifiable-secret-sharing/polynomial-commitments`
- 任务/问题: succinct commitment to polynomial and verifiable evaluations
- 方法族: pairing-based polynomial commitments, structured reference string
- 应用: VSS, ZKS/ZK-EDB, CES, credentials, later SNARK PCS
- 置信度: high
- 分类状态: accepted
- 分类证据: title, abstract, §3 construction, applications

## 一句话贡献

本文定义 polynomial commitment schemes，并给出 pairing-based constant-size constructions，使 verifier 可用短 witness 验证 committed polynomial 的 claimed evaluation，且 batch opening 仍可保持常数通信开销。

## 问题设定

需要对 degree 至多 `t` 的 polynomial `phi(x)` 做 commitment，使 commitment 不随 degree 线性增长，同时支持只打开/验证某些 evaluation points。安全性要保证 committer 不能对同一 commitment 打开两个冲突 polynomial 或冲突 evaluation，并且未打开点保持隐藏。

## 方法概览

### 组成部分

- Trusted/distributed setup 生成 `g, g^alpha, ..., g^{alpha^t}`。
- Commitment: `C = g^{phi(alpha)}`。
- Witness: `w_i = g^{(phi(x)-phi(i))/(x-i) evaluated at alpha}`。
- VerifyEval: 用 pairing equation 检查 witness、index、evaluation 和 commitment 一致。
- Pedersen variant: 加入随机 polynomial 提升 hiding。
- Batch opening: 用 remainder polynomial 和单个 witness 一次证明多个 indices。

### 假设条件

- Pairing group and structured reference string.
- DL/t-SDH for PolyCommitDL security.
- t-SDH for PolyCommitPed.
- t-BSDH for batch opening binding.
- t-polyDH for strong correctness.

## 创新点

- 新思想: 将 polynomial evaluation consistency 通过 quotient polynomial 和 pairing check 压缩为 constant-size witness。
- 对已有工作的扩展: 比 coefficient-wise commitments 减少 communication，从 O(t) commitment/opening 降到 single group element 级别。
- 应用贡献: VSS broadcast O(1)、nearly ZKS/ZK-EDB short proofs、CES/credential selective disclosure。
- 限制: setup parameters O(t)，依赖 pairing/SRS 和较强 assumptions，证明多在 extended version。

## Evidence Table

| Claim | Evidence anchor | Claim type | Confidence |
| --- | --- | --- | --- |
| Polynomial commitment lets a verifier confirm claimed evaluations of a committed polynomial using a short commitment/witness. | p1-p2 | definition | high |
| PolyCommitDL commits as `g^{phi(alpha)}` and verifies evaluation using quotient witness and pairing equation. | p6-p7 | mechanism | high |
| PolyCommitPed adds random polynomial for unconditional hiding. | p8 | mechanism | high |
| Batch opening can open multiple evaluations with a single witness and constant communication overhead. | p9-p10 | mechanism | high |
| eVSS replaces Feldman VSS coefficient commitments with one polynomial commitment, reducing broadcast to O(1). | p11-p13 | application | high |
| The scheme trades communication for O(t) public parameters and nontrivial computation. | p2, p10, p17 | limitation | high |

## 证据记录

> [!note]
> 本节保留该来源内部证据，供上层 map/synthesis 以 source-extension 形式引用；默认引用本元笔记或对应父概念。

| 证据点 | 原证据锚点 | 处理 |
| --- | --- | --- |
| KZG batch opening can prove multiple evaluations with one witness and a remainder polynomial, keeping communication overhead constant while relying on t-BSDH for binding. | `doi:10.1007/978-3-642-17373-8_11#p9-p10` | folded_into_meta_note |
| KZG/PolyCommitDL commits to a polynomial as g^{phi(alpha)} and proves an evaluation phi(i) using a quotient-polynomial witness, so commitment and single-point opening are constant-size group elements. | `doi:10.1007/978-3-642-17373-8_11#p5-p7` | folded_into_meta_note |
| 用 PolyCommitDL 替换 Feldman VSS 中的 coefficient commitments 后，dealer broadcast 由 O(n) commitments 降为一个 polynomial commitment，即 O(1) broadcast size。 | `doi:10.1007/978-3-642-17373-8_11#p11-p13` | folded_into_meta_note |

## Knowledge Handoff

### 可吸收的来源内判断

- `kzg-constant-size-polynomial-evaluation-proof`: KZG/PolyCommitDL uses `g^{phi(alpha)}` and quotient witness to verify evaluations with constant-size communication.
- `kzg-batch-opening-constant-communication`: batch opening uses a remainder polynomial and one witness for multiple points.
- `kzg-evss-reduces-broadcast`: PolyCommitDL reduces Feldman VSS broadcast from O(n) to O(1).

### Concepts to update

- `polynomial-commitments`: create foundation concept seed.
- `kzg-commitments`: create topic concept seed.

### Missing foundations

- IPA commitments, FRI commitments, Merkle/vector commitments comparison.
- Trusted setup/SRS threat model.
- Modern SNARK protocols using KZG.

## Synthesis Handoff

- Create `09_Syntheses/Topics/kzg-commitments-state-2026-06-11.md`.
- Create maps for `zero-knowledge-proofs`, `polynomial-commitments`, and `kzg-commitments`.
- Keep foundation status `foundation_thin` pending comparison sources.
