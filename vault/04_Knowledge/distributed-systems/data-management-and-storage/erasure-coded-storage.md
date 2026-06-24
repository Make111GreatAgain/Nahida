---
id: "nahida-knowledge-erasure-coded-storage"
title: "Erasure-coded Storage"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "erasure-coded-storage"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
parent_knowledge_refs:
  - "nahida-knowledge-data-management-and-storage"
child_knowledge_refs: []
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "erasure-coded-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/erasure-coded-storage"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-erasure-coded-storage"
    relation: "part_of"
    to: "nahida-knowledge-data-management-and-storage"
    evidence_refs:
      - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
      - "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-erasure-coded-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-erasure-coded-storage"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md"
    confidence: "high"
    status: "active_seed"
bridge_refs: []
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md"
  - "vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md"
representative_source_refs:
  - "doi:10.1109/INFOCOM53939.2023.10228984"
  - "usenix:fast18-vajha"
  - "sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a"
query_keys:
  - "erasure-coded storage"
  - "erasure coding in distributed storage"
  - "repair bandwidth"
  - "sub-packetization"
  - "Reed-Solomon storage"
  - "MSR codes"
  - "Clay codes"
  - "Coupled-Layer codes"
  - "vector erasure codes"
  - "Ceph vector codes"
  - "sub-chunk repair"
  - "minimum storage regenerating codes"
  - "access-optimal MSR"
  - "locally repairable codes"
  - "Hitchhiker erasure code"
  - "HashTag erasure code"
  - "OpenEC"
  - "HDFS erasure coding"
  - "纠删码存储"
  - "修复带宽"
aliases:
  - "Erasure coding for distributed storage"
  - "纠删码存储"
  - "Repair-efficient erasure codes"
domains:
  - "distributed-systems"
topics:
  - "data management"
  - "storage"
  - "erasure-coded storage"
  - "storage repair optimization"
  - "MSR codes"
  - "vector erasure codes"
  - "Ceph erasure coding"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-elastic-transformation-erasure-coded-storage"
  - "nahida-paper-intake-20260623-clay-codes"
source_refs:
  - "doi:10.1109/INFOCOM53939.2023.10228984"
  - "usenix:fast18-vajha"
  - "sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a"
confidence: "medium"
trust_tier: "primary"
---

# Erasure-coded Storage

## 定义与范围

- 定义: `erasure-coded storage` 是分布式存储中用纠删码而非简单复制来提供容错的一类数据冗余路线。它把数据拆成若干 data packets 和 parity/coded packets，使系统在部分节点或块丢失时仍能重建数据，并以较低存储开销换取更复杂的修复、读写和编码代价。
- 不包含: 单个 code construction、单个 HDFS/OpenEC 实现、单次 repair-time benchmark 或区块链 data availability sampling。RS、LRC、MSR、Hitchhiker、HashTag、Elastic Transformation 等应作为方法路线或代表来源。
- Canonical terms: `erasure-coded storage`, `erasure coding`, `Reed-Solomon codes`, `repair bandwidth`, `sub-packetization`, `MSR codes`, `LRC`
- Aliases/query keys: `纠删码存储`, `erasure coding for distributed storage`, `repair-efficient erasure codes`, `OpenEC`
- Standalone completeness check: 本节点能解释纠删码存储的核心目标、常见方法、修复瓶颈和带宽/I/O权衡；Clay 已补入 MSR/vector-code/Ceph 实践证据，但仍缺独立 RS/LRC/MDS foundation pack，所以状态为 `active_seed` 而非 evergreen。
- Retrieval role: 让“存储修复为什么慢”“RS/MSR/LRC 有什么区别”“sub-packetization 为什么影响系统性能”等查询直接落到可复用问题节点，而不是落到某篇 Elastic Transformation 论文。
- Update scope: 新的 erasure-coded storage、repair-efficient codes、production storage repair、OpenEC/HDFS/Ceph/object-store repair、degraded reads 或 multi-failure recovery source 会触发本节点刷新。
- Domain dynamics note: 非 L1 domain，`not_applicable`。

## 背景

model_prior_background: 分布式存储通常要在可靠性、存储开销、修复成本和访问性能之间折中。复制简单且修复成本低，但存储开销高；纠删码用少量 parity/coded data 获得更低冗余，但 repair 时需要从多个 surviving nodes 读取并传输数据。`Balancing Repair Bandwidth and Sub-Packetization...` 为当前 vault 提供了第一个直接 source-backed 入口，特别强调理论上最小 repair bandwidth 的 code 在真实系统中可能因为 high sub-packetization 和 non-sequential I/O 变慢。`Clay Codes` 进一步补入 MSR/vector erasure code 的实践证据：通过 coupled-layer construction 和 Ceph sub-chunk support，把 MDS code mould 成可实现的 MSR code，并在真实 Ceph repair 中降低 network traffic、disk read 和 repair time。

## 基础概念判断

- 是否是基础概念/方向/问题: 是。它是 distributed data/storage systems 中稳定可复用的冗余与修复问题，不属于单篇论文或单个协议实例。
- 为什么足够通用: RS、LRC、MSR、Hitchhiker、HashTag、OpenEC/HDFS repair 等都围绕“低冗余容错和修复成本”展开；未来区块链 DA、异步广播、对象存储等也会复用 erasure-code 概念，但边界不同。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Elastic Transformation 只是该问题下的一种 code-transformation solution；OpenEC-ET 只是实现 artifact。
- 需要引用的更基础 Knowledge: [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]
- 不应拆出的实例/协议/来源: `RS-ET`, `LRC-ET`, `OpenEC-ET`, `Elastic Transformation` 暂不建独立 foundation node；它们应保留为 source extension 或方法实例。

| 候选 | 判断 | 正确处理 | 错误处理 |
| --- | --- | --- | --- |
| Erasure-coded storage | foundation/problem knowledge | 独立解释纠删码存储的容错目标、repair bandwidth、sub-packetization、vector-code/sub-chunk repair 和系统 tradeoff | 只写某篇 ET 或 Clay 论文摘要 |
| Reed-Solomon codes | method/foundation candidate | 作为代表基础 code，未来可在更多 source 支持下拆 foundation | 把 RS-ET 当成全部 RS 知识 |
| Elastic Transformation | representative solution | 放在方法族与代表 sources，说明它解决 bandwidth/sub-packetization tradeoff | 直接提升为上层领域 |
| Clay codes | representative solution/source instance | 放在方法族与代表 sources，说明 MSR/vector code 如何在 Ceph 中实践 | 把 Clay 直接提升为上层领域 |
| Blockchain data availability erasure coding | adjacent application | 通过 bridge 候选或相邻方向连接，需保留 availability/security 边界 | 把 storage repair 和 DA sampling 视为同一问题 |

## 解决的问题

- 用低于复制的存储开销提供节点/块失效容忍。
- 在 block/packet 丢失后降低 repair bandwidth，避免修复时大量跨节点传输。
- 控制 disk reads、non-sequential I/O、sub-packetization 和编码计算，使理论带宽节省能转化为真实 repair-time 收益。
- 在不同 storage settings 下选择 code family: 例如 RS 的简单 MDS 容错、LRC 的 locality、MSR 的理论修复最优、piggybacking/HashTag 的工程折中、code transformation 的可调折中。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | `part_of` | Erasure-coded storage 是分布式数据持久化和恢复的冗余/修复层问题 | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Reed-Solomon and MDS storage codes | method_family/foundation candidate | RS/MDS 是多数纠删码存储讨论的基线 | Elastic Transformation §I-§II; future RS/production sources needed | queued |
| Repair-efficient erasure codes | method_family candidate | MSR, access-optimal MSR, piggybacking, Hitchhiker, HashTag 等专门优化 repair | Elastic Transformation §II-B | queued |
| Production erasure-coded storage repair | application/system candidate | HDFS/OpenEC/Ceph/object-store repair 需要独立系统 source | Elastic Transformation §V plus future systems sources | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Reed-Solomon/MDS storage codes | `k` 个 data packets 编成 `n-k` 个 parity packets，任意 `k` 个 packets 可重建数据 | 需要低冗余、高容错、简单成熟的 erasure coding | 修复一个 lost packet 通常读取 `k` 个 packets，repair bandwidth 高 | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |
| MSR/access-optimal repair codes | 从编码理论上最小化 repair bandwidth，access-optimal variants 还最小化 disk reads | 网络带宽是主要瓶颈，且系统能承受较高 sub-packetization | `alpha` 可能很高，真实系统中 non-sequential I/O 会抵消收益 | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |
| Clay/Coupled-Layer MSR codes | 叠加多个 MDS codeword layers，并用 pairwise coupling/PFT/PRT 让普通 scalar MDS code 变成支持低 repair bandwidth 的 vector MSR code | 需要 MDS code building block、可接受 vector-code/sub-chunk 实现复杂度、repair path 能选择合适 helper/sub-chunks | encode computation 增加；small stripe/sub-chunk size 会造成 fragmented reads；multi-failure savings pattern-dependent | [[sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code|Clay Codes]] |
| Locally repairable codes | 为 data/local parity 提供局部修复，减少常见修复路径读取范围 | 大规模云存储中常见单块修复，能接受非 MDS 或额外局部 parity | global parity 修复仍可能像 RS 一样昂贵 | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |
| Piggybacking/HashTag-style codes | 通过 piggybacking 或专门 construction 降低 data packet repair cost | 希望在保留 MDS 或低额外开销时改善 data repair | parity repair 可能未被优化；参数和实现复杂度需校准 | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |
| Elastic code transformation | 对 base code 应用 transformation arrays 和 pairwise coupling，用可配置 `alpha` 在 repair bandwidth 与 I/O overhead 之间取折中 | 需要从 base code 出发、优化 all nodes 或 subset nodes 的 repair | 主要证据来自 single-block repair；多故障/跨区域/SSD 场景需更多 source | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |
| Repair-time modeling | 把 network transmission term 和 I/O term 合并，选择实际 repair time 最优的 `alpha` | 系统 bottleneck 会在网络和磁盘之间移动 | 模型依赖 storage hardware、packet size、read scheduling 与 implementation | [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization in Erasure-Coded Storage via Elastic Transformation]] | paper | 创建本节点；把 repair bandwidth、sub-packetization、non-sequential I/O 的 tradeoff 作为纠删码存储修复优化问题吸收；提供 Elastic Transformation 和 OpenEC-ET 代表方案 | single lost packet/block repair；HDFS/OpenEC/HDD testbed；代码未分析 | Abstract; §II-B-C; §III; §IV; §V |
| [[sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code|Clay Codes: Moulding MDS Codes to Yield an MSR Code]] | paper | 补入 MSR/vector-code 实践路线：从任意 scalar MDS code 构造 coupled-layer Clay code，并修改 Ceph 支持 vector code/sub-chunk repair | single-node results strongest；multi-failure savings depend on pattern；Clay plugin at publication time not yet in Ceph master | Abstract; §2.2; §3; §4; §5; Appendix A |

## 正反例约束

- 正确: 讨论 erasure-coded storage 时先定义容错/低冗余/repair 的系统问题，再把 RS、MSR、LRC、Elastic Transformation 放为路线。
- 正确: 引用区块链 data availability 或 async reliable broadcast 时，要明确那些场景使用 erasure coding 的目的可能是 availability/security，不等同于 storage repair bandwidth。
- 错误: 把 Elastic Transformation 笔记拆成上层领域，或让本节点只复述该论文实验数字。
- 错误: 把所有含 Reed-Solomon 的论文都归到本节点；例如 FRI/DA 中的 Reed-Solomon 主要属于证明/数据可用性上下文。

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`。
- Freshness: `fresh` for this vault seed; not a latest-survey claim.
- Valid until: `2026-07-23`。
- 综合: 当前 vault 的 erasure-coded storage 节点由 Elastic Transformation 和 Clay 两篇 direct sources 支撑。核心结构是: 纠删码存储用低冗余替代复制，但修复 lost packet/block 时会遭遇 repair bandwidth、disk read、I/O locality 和 sub-packetization 问题。Elastic Transformation 强调理论最小 repair bandwidth 不一定带来最短 repair time，因为 high sub-packetization 可能造成 non-sequential I/O；Clay 则展示 MSR/vector-code 路线可以通过 coupled-layer construction 和 Ceph sub-chunk support 转化为实际 repair traffic、disk read、repair time 降低。未来吸收 OpenEC、LRC、production erasure-coded systems 或 degraded-read sources 后，应把 RS/MDS、MSR/access-optimal、locality、production repair scheduling 拆得更完整。

## 领域态势

- Research dynamics note: `not_applicable`
- Dynamics freshness: `not_applicable`
- Latest academic focus summary: `not_applicable`
- Latest industrial focus summary: `not_applicable`
- Open-problem summary: `not_applicable`
- Next refresh trigger: more direct sources on RS/MDS foundations, Clay/MSR, production erasure-coded storage systems, degraded reads, multi-failure repair, or OpenEC/Ceph/HDFS implementations.

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage|Balancing Repair Bandwidth and Sub-Packetization]] | 新建 erasure-coded storage problem node；纠正 queue 原 `distributed-transactions` 误分；吸收 repair bandwidth/sub-packetization/I/O tradeoff | 定义、解决的问题、方法族、代表 Sources、缺口 | yes | 继续队列中 `Clay.pdf`、`BlockSketch.pdf` 等相邻 storage/query sources 时复核子结构 |
| [[sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code|Clay Codes]] | 增加 MSR/vector-code/Ceph 实践路线；纠正 queue 原标题和 distributed-transactions 误分；将 `Clay.pdf` 缺口改为已吸收代表 source。 | 背景、方法族、代表 Sources、当前综合、缺口、关系图谱 | no | 补 RS/MDS/LRC/MSR foundation pack；复核生产 Ceph/OpenEC/HDFS source |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| Erasure-coded storage -> data availability sampling | `distributed-systems/data-management-and-storage/erasure-coded-storage` -> `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` | adjacent_method_reuse_candidate | Both use erasure coding/Reed-Solomon concepts, but storage repair optimizes failure recovery while DAS optimizes light-client availability/security. | queued |
| Erasure-coded storage -> asynchronous reliable broadcast | `distributed-systems/data-management-and-storage/erasure-coded-storage` -> `distributed-systems/consensus/asynchronous-bft-consensus/asynchronous-reliable-broadcast` | adjacent_method_reuse_candidate | Erasure-coded RBC uses coding to disseminate large messages efficiently under Byzantine/asynchronous assumptions, not to repair storage blocks. | queued |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-erasure-coded-storage | part_of | nahida-knowledge-data-management-and-storage | Data management/storage parent; Elastic Transformation source note | high | active_seed |
| nahida-knowledge-erasure-coded-storage | evidenced_by | vault/03_Sources/papers/doi-10-1109-infocom53939-2023-10228984-elastic-transformation-erasure-coded-storage.md | Abstract, §II-§V | high | active_seed |
| nahida-knowledge-erasure-coded-storage | evidenced_by | vault/03_Sources/papers/sha256-b04fe9944676-clay-codes-moulding-mds-codes-to-yield-an-msr-code.md | Clay source note, Abstract, §3-§5, Appendix A | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| RS/MDS、LRC、MSR 的 foundation source 仍缺 | Clay 已补入 MSR/vector-code 实践，但基础 code family 的系统性解释仍不足以当完整教材型 foundation | `nahida-research-search` foundation_pack 或 future papers | high | queued |
| Production erasure-coded storage 系统 source 缺失 | HDFS/OpenEC testbed 只是一个 prototype context，生产系统还需要 Ceph/HDFS/Facebook/Google 等来源校准 | `nahida-research-search` or future papers/repos | medium | queued |
| Degraded reads、multi-failure repair、repair scheduling 未覆盖 | 当前源聚焦 single-block repair，实际存储系统还需要读降级与并发故障恢复 | future source intake | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-elastic-transformation-erasure-coded-storage | Created erasure-coded storage problem node and absorbed repair bandwidth/sub-packetization tradeoff from Elastic Transformation. | doi:10.1109/INFOCOM53939.2023.10228984 | codex |
| 2026-06-23 | nahida-paper-intake-20260623-clay-codes | Added Clay Codes as practical MSR/vector-code and Ceph sub-chunk repair evidence; corrected queue title/classification. | usenix:fast18-vajha; sha256:b04fe9944676db0a3a6da4091a54d6c57bce7ebee6f8058c4077c1b59e14880a | codex |
