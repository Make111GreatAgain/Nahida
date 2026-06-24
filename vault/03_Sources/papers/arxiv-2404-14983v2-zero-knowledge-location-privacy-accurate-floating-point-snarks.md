---
id: "arxiv-2404-14983v2-zero-knowledge-location-privacy-accurate-floating-point-snarks"
title: "Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs"
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
  - "p1-p19 full extracted text"
  - "Appendix A integer circuits"
  - "Appendix B floating-point division"
  - "Appendix C authentic location information"
canonical_url: "https://arxiv.org/abs/2404.14983v2"
doi: ""
arxiv_id: "2404.14983v2"
venue: "arXiv"
year: "2024"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
topic_ids:
  - "privacy-preserving-location-proofs"
  - "floating-point-snarks"
  - "location-privacy"
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
  - "privacy-preserving-location-proofs"
primary_ontology_path: "zero-knowledge-proofs/applications/privacy-preserving-location-proofs"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/floating-point-snarks"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
  directions:
    - "applications"
    - "proof-systems"
  topics:
    - "privacy-preserving-location-proofs"
    - "floating-point-snarks"
    - "location-privacy"
domains:
  - "zero-knowledge-proofs"
topics:
  - "privacy-preserving-location-proofs"
  - "floating-point-snarks"
  - "location-privacy"
  - "ieee-754"
aliases:
  - "ZKLP"
  - "Zero-Knowledge Location Privacy"
  - "accurate floating-point SNARKs"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
  subdomain:
    - "applications"
    - "proof-systems"
  problem:
    - "privacy-preserving location proofs"
    - "accurate floating-point arithmetic in SNARKs"
    - "geospatial proof utility and privacy"
  method_family:
    - "IEEE 754 compliant floating-point circuits"
    - "lookup arguments"
    - "nondeterministic programming"
    - "trigonometric elimination"
  system_layer:
    - "application circuit"
    - "proof-system engineering"
  evaluation_context:
    - "Groth16"
    - "Plonk"
    - "BN254"
    - "Uber H3"
  bridge:
    - "floating-point-snarks-to-privacy-preserving-location-proofs"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zklp-floating-point-snarks"
source_refs:
  - "arxiv:2404.14983v2"
  - "sha256:32ae5b49af7af72b840fe07e6cd4be8fa93ff96b2cc9e5ba3010ab85eb4775b6"
confidence: "high"
trust_tier: "primary"
primary_direction: "applications"
secondary_directions:
  - "proof-systems"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Abstract introduces ZKLP as a location privacy application"
  - "Sections 3 and 5 provide reusable IEEE 754 floating-point SNARK circuits"
  - "Section 4 applies them to H3/DGGS geospatial proofs"
  - "Queue path zkml/verifiable-inference is only a possible future use, not the paper primary problem"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0029"
local_pdf: "~/Desktop/paper/2404.14983v2.pdf"
pdf_sha256: "32ae5b49af7af72b840fe07e6cd4be8fa93ff96b2cc9e5ba3010ab85eb4775b6"
extracted_text_path: "vault/02_Raw/pdf/extracted/2404.14983v2-32ae5b49af7a-pages.txt"
---

# Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs

## 论文身份

- 标题: Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs
- 作者: Jens Ernstberger, Chengru Zhang, Luca Ciprian, Philipp Jovanovic, Sebastian Steinhorst
- 机构: Technical University of Munich, The University of Hong Kong, University College London
- 会议/期刊: arXiv preprint
- 年份: 2024
- DOI: unknown
- arXiv: 2404.14983v2
- 链接: https://arxiv.org/abs/2404.14983v2
- 本地 PDF: `~/Desktop/paper/2404.14983v2.pdf`
- 代码/数据: PDF 声称 floating-point and ZKLP implementation / measurement data open-sourced at an anonymous 4open.science URL; 未联网验证。
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 19
- 已覆盖章节/页码: p1-p19, including introduction, preliminaries, floating-point circuits, ZKLP construction, empirical evaluation, related work, discussion, integer-operation appendix, division appendix, and authentic-location appendix.
- 未覆盖章节/页码: none known.
- Extraction gaps: Figure 13 heatmap is text-extracted imperfectly, but caption and qualitative discussion are readable.
- 精读说明: 队列原路径是 `zero-knowledge-proofs/zkml/verifiable-inference`。深读后纠正为 `zero-knowledge-proofs/applications/privacy-preserving-location-proofs`，因为论文主问题是位置隐私证明；`floating-point-snarks` 是方法层第二主线，`zkML/verifiable-inference` 只是论文未来适用方向之一。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和结果 | 定义 ZKLP，证明用户在某区域内但不泄露精确位置；提出 IEEE 754 compliant floating-point ZKP circuits | high | 主分类依据 |
| §1 / p1-p3 | 动机和贡献 | location privacy, authenticity, fixed-point limitations, IEEE 754 compatibility, contributions | high | 解释为何不是普通 fixed-point circuit |
| §2 / p3-p5 | Preliminaries | floating-point format, DGGS/H3, SNARKs, lookup arguments, nondeterministic programming | medium | 上层概念依赖 |
| §3 / p5-p9 | Primitive floating-point operations | init, rounding, add/sub, multiplication/division, sqrt, comparison | high | floating-point SNARKs 方法核心 |
| §4 / p9-p12 | ZKLP construction | H3 coordinate transform, eliminate trig functions, hints for sin/cos/tan half-angle values, IJK conversion | high | application circuit 核心 |
| §5 / p12-p14 | Evaluation | TestFloat compliance, constraint counts, baseline comparison, P2P proximity test | high | 性能和准确性证据 |
| §6 / p14 | Related work | floating-point secure computing, location privacy, proximity testing | medium | novelty boundary |
| §7 / p14-p15 | Discussion | C2PA, authentic location, ML future, proof-of-personhood future | medium | 应用边界和未来方向 |
| Appendix A-B / p16-p18 | Integer/division circuits | range check, sign/abs, shifting, division gadget | high | circuit completeness |
| Appendix C / p18-p19 | Authentic location information | offline finding networks, authenticated GNSS/OSNMA, TLS oracles | high | 重要限制和系统边界 |

## 核心精读笔记

> 这篇论文的主线是: 用准确、IEEE 754 compliant 的 floating-point SNARK circuits 支撑位置隐私证明，使用户能证明自己落在某个 H3/DGGS 区域内，而不泄露精确经纬度。

### 问题、动机与边界

- Location-based services 需要空间信息，但精确位置泄露个人习惯、偏好和行为轨迹。
- 传统 LPPM 有两类: obfuscation 和 cryptographic methods。前者会损失 utility；后者常依赖 anonymization 或 MPC/第三方假设。
- 理想机制需要让用户自己提交可验证位置证明，支持可调粒度，保护精确位置，并尽量防止伪造位置。
- ZKLP 的应用陈述: 用户证明自己在指定地理区域或 hexagonal cell 中，但精确经纬度作为 private witness 不暴露。
- 重要边界: 主协议只保护 user-provided location 的隐私和电路正确性，不自动证明位置来源真实。Appendix C 才讨论如何桥接 cyber-physical authenticity。

### 为什么需要 floating-point SNARKs

- 地理计算包含经纬度、平方根、三角函数、坐标变换等实数运算；实际地理库例如 Uber H3 使用 IEEE 754 floating-point。
- fixed-point 在 ZKLP 里有两个问题:
  - 同时处理很大值和很小值时需要更多 bit 或损失精度。论文指出在某些场景 fixed-point 接近 FP64 两倍 bit-width 仍更低精度。
  - 与已有 IEEE 754 实现不一致会破坏 completeness；更严重时，精度/舍入差异可被 adversary 用来构造恶意 statement，让 soundness 受损。
- 因此论文把 IEEE 754 compliant floating-point operations 本身作为独立贡献，而不是只为 ZKLP 写一个专用近似。

### Floating-point SNARK circuits

论文定义 over prime field `Fp` 的 floating-point representation `(s, e, m, a)`:

- `s`: sign bit。
- `e`: circuit-efficient unbiased exponent。
- `m`: explicit-leading-bit mantissa；subnormal 被归一化。
- `a`: abnormal bit，标记 NaN 或 infinity 类边界。

主要 circuit/gadget:

- `CFpInit`: 检查输入形状，处理 normal/subnormal/zero/infinity/NaN，并转换成 circuit-efficient form。
- `CFpRound`: 实现 IEEE 754 binary "round half to even"，包含 subnormal 精度处理；用 hints 拆分 mantissa，减少 variable-bound range check。
- Addition/subtraction: exponent alignment、signed mantissa addition、normalization、rounding、edge cases。
- Multiplication/division: mantissa product 或 quotient hint，MSB normalization，rounding；division 用 quotient/remainder hint 保留 sticky-bit 信息。
- Square root: 用 nondeterministic hint 提供 integer square root，电路只验证 `n^2 <= x < (n+1)^2`，避免 Newton iteration 的循环和 division 成本。
- Comparison: 处理 NaN、signed zero、sign/exponent/mantissa 组合，支持 strict equality 和 fuzzy equality。

关键工程思想:

- lookup arguments 用于 range checks 和 powers of two，降低 bit decomposition 成本。
- nondeterministic programming 把难算但易验的计算放到 circuit 外，用 predicate 验证。
- 对 NaN、infinity、subnormal、signed zero 进行显式边界处理，支撑 IEEE 754 compliance。

### ZKLP circuit

ZKLP 采用 DGGS/H3 的 hexagonal hierarchical spatial indexing:

- 公开 statement: resolution `res` 与目标 H3 cell 的 `(I, J, K)` 或区域索引。
- private witness: 用户精确经纬度 `(theta, phi)`。
- 电路目标: 验证经纬度按 H3 转换后落在目标 cell，同时隐藏经纬度。

H3 传统转换路线:

1. 经纬度转 radians。
2. spherical coordinates 转 3D Cartesian。
3. 找最近 icosahedron face。
4. 计算 radial distance。
5. 计算角度 `sigma`。
6. 转 2D Cartesian。
7. 转 `(i, j, k)` hex-grid coordinates。

直接在 circuit 中实现三角函数会很贵。论文用两类优化消掉三角函数:

- 用三角恒等式把 `tan(arccos(1-d^2/2))` 等表达式改写成 sqrt/div/mul 组合。
- 对初始 `sin/cos/tan(theta/2)` 和 `sin/cos/tan(phi/2)` 用 hints，并在 circuit 里验证恒等式，例如 `gamma^2 + delta^2 = 1`、`delta * alpha = gamma`、`2 * gamma * delta = beta`。

因此，ZKLP 的核心不是“证明近似三角函数正确”，而是把 geospatial transform 改写成 floating-point primitive operations 和可验证 hints。

### 实验与性能

实验设置:

- 实现语言/框架: gnark reusable library。
- Proof systems: Groth16 和 Plonk over BN254。
- Lookup: gnark LogUp 风格 range checks。
- Compliance test: Berkeley TestFloat 生成每个 binary operation 46464 个测试用例，sqrt 600 个测试用例；实现通过含 abnormal values 的测试。
- ZKLP test: 对 H3 resolution 0 到 15，每个 resolution 16 个距离，每个距离 100 个随机点。

关键结果:

- Primitive floating-point circuits 能明显 amortize lookup cost。论文给出的示例是 FP32 multiplication: 2^1 次乘法约 209 constraints/op，2^15 次约 64 constraints/op。
- End-to-end Groth16 over BN254:
  - fixed-point baseline P20: 309.6k constraints, prover 1.75 s, memory 517.3 MB, SRS 52.4 MB。
  - ZKLP FP32: 19.5k constraints, prover 0.26 s, memory 248.7 MB, SRS 4.6 MB。
  - ZKLP FP64: 25.5k constraints, prover 0.32 s, memory 246.7 MB, SRS 6.2 MB。
- Plonk:
  - baseline P20: 570.9k constraints, prover 38.42 s。
  - ZKLP FP32: 55.5k constraints, prover 2.19 s。
  - ZKLP FP64: 81.3k constraints, prover 4.41 s。
- 与 fixed-point baseline 相比，ZKLP FP32 constraints 约 15.9x less，FP64 约 12.2x less。
- 准确性:
  - fixed-point P20 在 resolution 3 后开始频繁错误，resolution 11 以上大多失败。
  - P40 显著改善，但仍有边界错误。
  - FP64 与 Uber H3 data format/rounding mode 对齐，测试全通过。
- P2P proximity testing:
  - Bob 生成 proximity/non-proximity proof 约 0.26 s。
  - Alice 可约每秒验证 470 个 peers。
  - 证明通信量在 Groth16 下约 200 Byte。

### Authentic location information

主协议只证明 private location witness 与公开 cell 的关系，不能证明 witness 是真实物理位置。Appendix C 给出三类可能来源:

- Offline finding networks: 证明多份 location reports 的 key derivation/decryption 和 triangulation，再接 ZKLP。好处是不要求新硬件；代价是 AES/key derivation/triangulation 等额外 circuit。
- Authenticated GNSS signals: 例如 OSNMA，验证 TESLA chain、MAC、ECDSA 等。论文估计在 gnark 中对 circuit-unfriendly secp256k1 做 ECDSA emulation 约需 `4 * 10^6` constraints；还存在第三方转发 GNSS signal 的 atomicity/open problem。
- TLS oracles: 证明 location API 返回数据的 provenance，再接 ZKLP。论文只提出方向，没有完整系统设计。

### 相关工作边界

- Floating-point secure computing:
  - MPC/2PC 有 IEEE 754 或部分 compliant 路线，但 circuit/通信成本高或只部分处理 subnormal/NaN。
  - Succinct floating-point ZK prior work 支持有限操作或没有 concrete implementation；本文主张是 first fully IEEE 754 compliant floating-point operations for succinct proof systems。
- Location privacy:
  - 既有 proximity testing 常是 interactive 或通信大。
  - 本文主张 ZKLP 是 first non-interactive, publicly verifiable and privacy-preserving proof of geolocation paradigm。
- 与 zkML:
  - 论文在 discussion 中说方法可适配 ML training/inference proofs，因为 ML 参数常为 floating-point。
  - 这不是本文 primary source role；只能作为 future bridge/gap。

## 方法与机制速查

| 机制 | 解决的问题 | 关键做法 | 代价/限制 | 证据 |
| --- | --- | --- | --- | --- |
| IEEE 754 compliant FP circuits | fixed-point 不准确、不兼容地理库 | circuit-efficient `(s,e,m,a)` representation; rounding half-to-even; abnormal/subnormal handling | lookup setup 和 amortization 假设；实现绑定 gnark/BN254 实验 | §3, Appendix A-B |
| Lookup-based range checks | bit decomposition 成本高 | `TRC` range table, `TPow2` powers-of-two table | lookup identity 在 gnark 中转成 constraints，有 operation-agnostic overhead | §2.5, §5.1 |
| Nondeterministic hints | sqrt/division/MSB/trig values难算但易验 | prover 给 hints，circuit 验证 predicate | soundness 依赖 predicate 完整；不是信任 hints | §2.5, §3.5, §4 |
| Trigonometric elimination | H3 transform 直接三角函数太贵 | 恒等式 + half-angle hints + precomputed face constants | 需要严格验证 hint relation；仍要处理 floating-point rounding | §4 |
| ZKLP over H3 | 证明位置在 cell 内但隐藏精确位置 | private `(theta, phi)` -> verified `(I,J,K)` | 不自动证明位置真实性 | §4, Appendix C |
| P2P proximity testing | Alice/Bob 证明近邻关系不泄露额外位置 | Bob 证明 cell，Alice 本地计算 boundary distance | 依赖 cell granularity 与 proximity policy | §5.2 |

## 证据表

| Claim | Evidence | Confidence | Notes |
| --- | --- | --- | --- |
| ZKLP 允许证明用户在地理区域内而不泄露精确位置 | Abstract, §1, §4 | high | 主贡献 |
| 论文提出 IEEE 754 compliant floating-point SNARK circuits | Abstract, §1.1, §3, §5.1 | high | "first" 是作者声称，未外部验证 |
| fixed-point 对 ZKLP 有 accuracy/completeness/soundness 风险 | §1, §5.2 | high | 与 Uber H3 格式/rounding 对齐是关键 |
| ZKLP 优化消除 trigonometric operations | §4 | high | 恒等式与 hints |
| FP32/FP64 ZKLP 比 fixed-point baseline 约束少 15.9x/12.2x | Table 2 / §5.2 | high | 基于论文实验 |
| FP64 测试全通过，P20/P40 fixed-point 有失败 | Figure 13 / §5.2 | high | Figure text extraction 不完整，但正文结论明确 |
| 位置真实性不是主协议保证 | Limitations / Appendix C | high | 必须写入上层限制 |

## 吸收到知识库的增量

| Layer | Target | Delta | Boundary |
| --- | --- | --- | --- |
| Knowledge | [[privacy-preserving-location-proofs|Privacy-preserving location proofs]] | 新建应用问题节点: 证明地理区域/近邻关系而隐藏精确位置 | 不把 ZKLP 当成唯一概念本体 |
| Knowledge | [[floating-point-snarks|Floating-point SNARKs]] | 新建 proof-system 方法节点: IEEE 754 compliant arithmetic circuits in SNARKs | 不替代 zk-SNARK foundation |
| Bridge | [[floating-point-snarks-to-privacy-preserving-location-proofs|Floating-point SNARKs -> privacy-preserving location proofs]] | 记录 floating-point circuits 如何支撑 geospatial ZKP 应用 | authenticity 来源不自动迁移 |
| Knowledge | [[zk-snarks|zk-SNARKs]] | 增加 application/method extension: accurate FP circuits and location proof use case | 不升级 foundation status |

## 质量复核

- 完整性: 覆盖 motivation, FP circuits, ZKLP construction, evaluation, related work, discussion, integer/division/authenticity appendices。
- 分层性: source note 保留 circuit 细节和数字；knowledge node 只吸收应用问题、方法族和边界。
- 分类纠偏: 从 `zero-knowledge-proofs/zkml/verifiable-inference` 改为 `zero-knowledge-proofs/applications/privacy-preserving-location-proofs`；`floating-point-snarks` 为 secondary proof-system method。
- 风险: 未联网验证代码 URL；"first" novelty claim 仅按论文自述；location authenticity 需要外部 provenance system。

## 关系与链接

- Primary: [[privacy-preserving-location-proofs|Privacy-preserving location proofs]]
- Method: [[floating-point-snarks|Floating-point SNARKs]]
- Parent: [[applications|ZKP applications]] -> [[zero-knowledge-proofs|Zero-knowledge proofs]]
- Proof-system context: [[zk-snarks|zk-SNARKs]]
- Bridge: [[floating-point-snarks-to-privacy-preserving-location-proofs|Floating-point SNARKs -> privacy-preserving location proofs]]
- Nearby application sources: [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]], [[sha256-7ab37dce93ba-zkcross-cross-chain-privacy-preserving-auditing|zkCross]]
