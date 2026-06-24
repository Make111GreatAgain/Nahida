---
id: "nahida-knowledge-privacy-preserving-location-proofs"
title: "Privacy-preserving location proofs"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "privacy-preserving-location-proofs"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
parent_knowledge_refs:
  - "nahida-knowledge-zkp-applications"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
  - "privacy-preserving-location-proofs"
primary_ontology_path: "zero-knowledge-proofs/applications/privacy-preserving-location-proofs"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/floating-point-snarks"
relation_edges:
  - from: "nahida-knowledge-privacy-preserving-location-proofs"
    relation: "is_a"
    to: "nahida-knowledge-zkp-applications"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/privacy-preserving-location-proofs.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-location-proofs"
    relation: "uses"
    to: "nahida-knowledge-floating-point-snarks"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
      - "vault/05_Bridges/floating-point-snarks-to-privacy-preserving-location-proofs.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-location-proofs"
    relation: "depends_on"
    to: "nahida-knowledge-zk-snarks"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md"
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-location-proofs"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-location-proofs"
    relation: "bridges_to"
    to: "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
    evidence_refs:
      - "vault/05_Bridges/floating-point-snarks-to-privacy-preserving-location-proofs.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs"
source_note_refs:
  - "vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md"
representative_source_refs:
  - "arxiv:2404.14983v2"
query_keys:
  - "Privacy-preserving location proofs"
  - "zero-knowledge location privacy"
  - "ZKLP"
  - "location privacy proofs"
  - "private proximity testing"
  - "geolocation ZKP"
aliases:
  - "ZKLP"
  - "Zero-Knowledge Location Privacy"
  - "zero-knowledge location proofs"
  - "private geolocation proofs"
domains:
  - "zero-knowledge-proofs"
topics:
  - "privacy-preserving-location-proofs"
  - "location-privacy"
  - "floating-point-snarks"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
source_refs:
  - "arxiv:2404.14983v2"
confidence: "medium"
trust_tier: "primary"
---

# Privacy-preserving location proofs

## 定义与范围

- 定义: Privacy-preserving location proofs 研究如何让 prover 证明自己满足某个地理位置、区域、距离或邻近关系约束，同时隐藏精确位置坐标和不必要的移动轨迹信息。
- 不包含: 单个应用名、某个 H3 cell、某个 proof-system 实现、单次 proximity benchmark 或 location provenance 设备本身。这些应保留在 source note 或更具体的系统笔记中。
- Canonical terms: `privacy-preserving-location-proofs`, `zero-knowledge location privacy`
- Aliases/query keys: ZKLP, private geolocation proofs, private proximity testing
- Standalone completeness check: 本节点本地解释应用问题、威胁边界、方法路线、代表 source、bridge 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“怎么证明人在某区域内但不暴露精确位置”“ZKLP 属于什么问题层”“location privacy 和 SNARK 怎么结合”时先读本节点。
- Update scope: 新 source 若提出 location/region/proximity proofs、location provenance、geospatial ZKP、private proximity testing 或可验证地理凭证，应刷新本节点。
- Domain dynamics note: parent domain dynamics remains [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

Location-based services 需要位置数据，但精确经纬度会泄露习惯、偏好、社交关系和行为轨迹。传统 location privacy 机制常在 utility 和 privacy 之间折中: obfuscation 降低精度，MPC/anonymization 方案可能依赖第三方或交互。ZKP 路线试图把“位置满足某约束”变成可验证 statement，让 precise location 作为 hidden witness。

当前 vault 的 primary source 是 [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]]，它把 H3/DGGS geospatial indexing 与 IEEE 754 compliant floating-point SNARK circuits 结合。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它不等于 ZKLP 这篇论文。它组织 region membership, proximity testing, geospatial index proof, location provenance, proof granularity 和 authenticity gap 等可复用问题。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: ZKLP 是当前代表 source；本节点组织的是“隐私保护位置证明”这个应用问题层。
- 需要引用的更基础 Knowledge: [[applications|ZKP applications]], [[zk-snarks|zk-SNARKs]], [[floating-point-snarks|Floating-point SNARKs]]。
- 不应拆出的实例/协议/来源: ZKLP、Uber H3、C2PA integration、OSNMA、TLS oracle routes 默认作为 source/route elements，除非后续多来源证明需要独立子节点。

## 解决的问题

Privacy-preserving location proofs 解决的是应用层验证目标与隐私之间的冲突:

- verifier 想知道 prover 是否在某个区域、距离范围或 proximity relation 内。
- prover 不希望暴露精确经纬度、完整轨迹或不相关位置属性。
- 证明要保持 utility，例如允许不同 resolution/ granularity。
- 如果位置由 prover 自报，还需要额外 provenance 才能防止伪造。
- 地理计算通常依赖 floating-point 和 geospatial libraries，近似误差会影响 completeness/soundness。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[applications|ZKP applications]] | child_of / application_problem | ZKLP source absorption | active_seed |
| [[zero-knowledge-proofs|Zero-knowledge proofs]] | domain context | ZKP hides location witness while proving location predicate | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| region membership proofs | route section | 证明位置在给定区域或 cell 内 | ZKLP H3/DGGS circuit | active_seed |
| private proximity testing | route section | 证明/测试双方距离或 cell boundary proximity | ZKLP P2P evaluation | active_seed |
| authentic location provenance | candidate problem | 真实位置来源不是 ZKLP 主协议自动保证 | ZKLP Appendix C | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Region/cell membership over DGGS | 把精确经纬度作为 private witness，证明其转换后的 cell/index 等于公开目标。 | 应用能接受 cell/resolution 粒度，且 geospatial transform 可被电路化。 | 粒度选择影响 privacy/utility；需要处理 floating-point 精度和 rounding。 | [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] |
| Private proximity testing | 证明某位置与 peer 或区域边界的近邻关系，让 verifier 只得到 proximity 判断。 | verifier 需要距离/近邻结论而非精确坐标。 | proximity policy、cell shape 和 boundary distance 仍是应用层设计。 | [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|ZKLP]] |
| Floating-point SNARK route | 用 IEEE 754 compliant circuits 复现 geospatial library 的数值语义，避免 fixed-point mismatch。 | 原应用依赖 floating-point 地理库，如 H3。 | 需要 lookup/hints 和 abnormal/subnormal/rounding 处理；具体实现依赖 proof system/circuit framework。 | [[floating-point-snarks|Floating-point SNARKs]] |
| Location provenance integration | 证明 location witness 来自可信来源，例如 offline finding network、authenticated GNSS、TLS oracle 或 signed media metadata。 | 应用需要防止 prover 自报假位置。 | 可能引入 AES/ECDSA/TLS/non-native arithmetic 成本；GNSS 转发/原子性仍可能未解。 | ZKLP Appendix C |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | paper | 创建本问题节点；给出 H3/DGGS location proof circuit、private proximity testing、IEEE 754 floating-point SNARK dependency | 主协议不保证位置真实性；代码 URL 未联网验证；novelty claim 按论文自述 | `p1-p19` |

## 正反例约束

- 正确: 把 ZKLP 作为 privacy-preserving location proofs 的代表 source。
- 正确: 把 floating-point SNARKs 写成方法依赖和 bridge endpoint，不把应用问题混到 proof-system foundation 里。
- 正确: 把 authenticity/provenance 作为限制和未来路线单列。
- 错误: 把本文归为 zkML/verifiable inference 主源。论文只在 future work 中提到 ML adaptation。
- 错误: 因为使用 Groth16/Plonk 就把它当作 zk-SNARK foundation source；它是应用和数值电路 source。

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-20`，仅覆盖当前 vault 已深读 ZKLP。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-20`。
- 综合: 当前节点是 foundation_thin seed。ZKLP 显示 ZKP 可把“在某地理区域内”转化为隐私保护 statement，但 geospatial computation 的数值语义是核心难点。它通过 [[floating-point-snarks|Floating-point SNARKs]] 与 H3/DGGS route 解决 utility/completeness 问题，并在 P2P proximity testing 上给出实践证据。位置真实性仍是外部 provenance 问题，不能由 ZKLP 主电路自动推出。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks|Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs]] | 创建隐私保护位置证明问题节点；补充 H3/DGGS、private proximity testing、authenticity gap | 定义; 方法族与解决路线; 代表 Sources; Bridge Links | yes | 吸收 location provenance/private proximity/geo-indistinguishability primary sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[floating-point-snarks-to-privacy-preserving-location-proofs|Floating-point SNARKs -> privacy-preserving location proofs]] | `zero-knowledge-proofs/proof-systems/floating-point-snarks; zero-knowledge-proofs/applications/privacy-preserving-location-proofs` | application, method_transfer, numerical_soundness, dependency | IEEE 754 circuits transfer to geospatial proof accuracy; location authenticity/provenance and policy granularity do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-privacy-preserving-location-proofs | is_a | nahida-knowledge-zkp-applications | vault/04_Knowledge/zero-knowledge-proofs/applications/privacy-preserving-location-proofs.md | high | active_seed |
| nahida-knowledge-privacy-preserving-location-proofs | uses | nahida-knowledge-floating-point-snarks | ZKLP §3-§5 | high | active_seed |
| nahida-knowledge-privacy-preserving-location-proofs | depends_on | nahida-knowledge-zk-snarks | ZKLP uses Groth16/Plonk as proof-system backends | high | active_seed |
| nahida-knowledge-privacy-preserving-location-proofs | evidenced_by | vault/03_Sources/papers/arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks.md | full source note | high | active_seed |
| nahida-knowledge-privacy-preserving-location-proofs | bridges_to | nahida-bridge-floating-point-snarks-to-privacy-preserving-location-proofs | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Location provenance primary sources 缺。 | 需要区分“证明位置关系”与“证明位置真实来源”。 | nahida-research-search or nahida-update | high | queued |
| Private proximity testing prior work 缺。 | 需要校准 ZKLP 与 MPC/proximity protocols 的边界。 | nahida-research-search | medium | queued |
| H3/DGGS foundation source 缺。 | 地理索引假设目前只来自 ZKLP source。 | nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zklp-floating-point-snarks | Created privacy-preserving location proofs problem node from ZKLP source absorption. | 1 source note | codex |
