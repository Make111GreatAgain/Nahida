---
id: doi-10-1145-2339530-2339722-streaming-graph-partitioning-large-distributed-graphs
title: "Streaming Graph Partitioning for Large Distributed Graphs"
type: source
source_kind: paper
source_subtype: local_pdf
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: active
hierarchy_level: source
authors:
  - Isabelle Stanton
  - Gabriel Kliot
year: 2012
venue: "KDD 2012"
publisher: "ACM"
status: absorbed
reading_status: deep_read_complete
reading_depth: deep_read
safe_for_absorption: true
classification_status: corrected_from_noisy_metadata
classification_confidence: high
primary_domain: algorithm-engineering
primary_direction: graph-algorithms
domain_id: algorithm-engineering
direction_id: graph-algorithms
topic_ids:
  - graph-partitioning
  - streaming-graph-partitioning
  - distributed-graph-processing
  - graph-data-layout
primary_knowledge_path: "[[graph-partitioning|Algorithm engineering / Graph algorithms / Graph partitioning]]"
primary_ontology_path: "algorithm-engineering/graph-algorithms/graph-partitioning"
ontology_path:
  - algorithm-engineering
  - graph-algorithms
  - graph-partitioning
secondary_knowledge_paths:
  - "distributed-systems/distributed-graph-processing"
secondary_ontology_paths:
  - "distributed-systems/distributed-graph-processing"
source_refs:
  - "doi:10.1145/2339530.2339722"
  - "sha256:204bff1f6801b8e5764e2fac54252b59cea1dbf3ac666072cf2eb1e750fce647"
local_path: "~/Desktop/paper/LDG.pdf"
local_pdf_path: "~/Desktop/paper/LDG.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/ldg-204bff1f6801-pages.txt"
page_count: 10
pages: 10
canonical_url: "https://doi.org/10.1145/2339530.2339722"
doi: "10.1145/2339530.2339722"
arxiv_id: ""
knowledge_node_refs:
  - "[[algorithm-engineering]]"
  - "[[graph-algorithms]]"
  - "[[graph-partitioning]]"
bridge_refs: []
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "item0107"
run_id: "nahida-paper-intake-20260623-streaming-graph-partitioning"
run_ids:
  - "nahida-paper-intake-20260623-streaming-graph-partitioning"
managed_by: nahida
confidence: high
trust_tier: primary
created: 2026-06-23
updated: 2026-06-23
domains:
  - algorithm-engineering
  - distributed-systems
topics:
  - graph partitioning
  - streaming graph partitioning
  - large distributed graphs
  - graph data layout
  - PageRank on Spark
aliases:
  - LDG paper
  - Linear Deterministic Greedy graph partitioning paper
  - Streaming graph partitioning for large distributed graphs
tags:
  - nahida/source/paper
  - nahida/domain/algorithm-engineering
  - nahida/graph-algorithms/graph-partitioning
---

# Streaming Graph Partitioning for Large Distributed Graphs

## Paper Identity

- **Corrected title:** Streaming Graph Partitioning for Large Distributed Graphs.
- **Authors:** Isabelle Stanton and Gabriel Kliot.
- **Venue:** KDD 2012, Beijing, China.
- **Year:** 2012.
- **DOI:** `10.1145/2339530.2339722`.
- **Canonical URL:** https://doi.org/10.1145/2339530.2339722.
- **Local PDF:** `~/Desktop/paper/LDG.pdf`.
- **Checksum:** `sha256:204bff1f6801b8e5764e2fac54252b59cea1dbf3ac666072cf2eb1e750fce647`.
- **Queue correction:** 队列标题 `https://www.researchgate.net/publication/233415975` 是 ResearchGate 封面噪声；PDF 第 2 页给出真实论文题名、作者、摘要和 KDD 2012 出版信息。队列原分类 `distributed-systems/consensus/needs-review` 也不正确；本文核心是 graph partitioning / streaming algorithms / distributed graph data layout，不是 consensus。

## Reading Coverage

- Page 1: ResearchGate 包装页，只用于确认获取日期和噪声来源，不作为论文身份主证据。
- Page 2: 正文首页，题名、作者、摘要、关键词、KDD 2012 元数据和引言开头。
- Pages 2-4: 引言、应用动机、理论困难、streaming model、贡献。
- Pages 4-6: related work、heuristics、stream order 定义。
- Pages 6-9: 数据集、实验方法、边界、主要实验结果、规模扩展实验。
- Pages 9-10: Spark/PageRank 真实系统实验、结论、未来工作、参考文献。
- Extraction quality: `pypdf` 文本可读，公式和图表标签有轻微排版噪声，但核心机制、指标、数值和章节均可重建。
- Safe for absorption: true.

## One-Sentence Contribution

本文把 balanced graph partitioning 放到 graph loading 的 one-pass streaming 场景中，比较一组轻量启发式，并显示 Linear Deterministic Greedy 可以在大规模分布式图计算中显著减少 edge cut 和 PageRank 通信时间。

## Structured Summary

### Background, Motivation, and Problem Boundary

大型 Web、社交网络、生物网络等图通常无法放在单机上处理。分布式图计算系统如果按 vertex ID hash 布局，通常可以负载均衡，但会切断大量跨分区边，使 PageRank 这类迭代图算法被网络通信拖慢。传统 graph partitioning 方法，例如 spectral partitioning 或 METIS-style offline partitioning，需要完整图信息和额外预处理；当图本来就要从磁盘加载到集群时，作者提出一个自然问题：能否在加载每个顶点时顺手做轻量 partitioning，从而避免昂贵的离线分区成本。

本文明确不把 streaming partitioning 视为 full-information partitioning 的替代品。它更像 preprocessing/data layout 优化：如果后续仍要运行完整离线重分区，初始布局已经更接近好切分，可以减少通信和迁移。

### Model, Assumptions, and Definitions

论文使用 one-pass streaming graph model:

- 集群有 `k` 台机器，每台容量 `C`，总容量足以容纳图。
- 图 `G=(V,E)` 的顶点以 stream 到达；每个顶点到达时携带它相关的边。
- partitioner 在顶点到达时决定放入哪个 partition，已放置顶点不再移动。
- 算法可访问已经到达顶点诱导出的子图；论文实际评估的启发式只需要局部 depth-1 信息。
- 扩展模型允许大小为 `C` 的 buffer，使算法可在 buffer 内选择下一个放置顶点。
- stream order 包括 random、BFS、DFS；BFS/DFS 用来模拟 crawler-like graph loading 中保留局部性的线性化。

理论部分给出负面边界：在 adversarial order 和 random order 下，one-pass streaming balanced graph partitioning 都不能在 `o(n)` 内近似最优。论文没有展开完整证明，而是用 cycle 例子和 random-order 下早期看不到边的现象说明困难。

### Methods and Heuristics

论文比较十类启发式，目标都是在 balance constraint 下减少 edge cut:

- **Balanced:** 忽略边，放到当前最小 partition。
- **Chunking:** 按容量连续填满 partition。
- **Hashing:** 用 vertex ID hash 分配，代表许多系统默认方案。
- **Weighted Deterministic Greedy:** 把顶点放到已有邻居最多的 partition，并用容量惩罚函数降低大 partition 吸引力。
- **Weighted Randomized Greedy:** 按邻居数和容量惩罚形成概率分布。
- **Weighted Triangles:** 通过邻居之间的已完成三角形捕捉社交网络聚簇结构。
- **Balance Big / Prefer Big / Avoid Big:** 根据高低度顶点采用不同策略。
- **Greedy EvoCut:** 在 buffer 上运行 EvoCut 找局部 sparse cut，再用 greedy 选择 partition。

核心代表算法是 **Linear Deterministic Greedy (LDG)**:

```text
score(i) = |P_t(i) cap Gamma(v)| * (1 - |P_t(i)| / C)
```

它把“邻居已经在哪个 partition”与“partition 还有多少容量”线性合成。论文解释说，unweighted greedy 的惩罚只在 partition 满时才生效，exponential penalty 又太晚显著变化；linear penalty 更早、更平滑地把负载信息纳入决策。

### Evaluation Design

实验用 Hashing 作为实践上常见的上界基线，用 METIS 4.0.3 作为高质量 offline lower-bound comparator。作者没有宣称 METIS 最优，而是把它作为实际可运行、质量较高的离线启发式参照。

数据集覆盖 SNAP 图、Graph Partitioning Archive 的 FEM 图、astroph、celegans、Marvel social network、BA/Watts-Strogatz/RMAT/power-law synthetic graphs，以及真实系统实验中的 LiveJournal 和 Twitter 大图。

小中型实验在 2、4、8、16 partitions 上运行，每组重复 5 次，imbalance 设置为 5%。真实系统实验在 Spark 上跑 PageRank，并根据 power-law 图的 workload 特点使用 edge-balanced LDG。

### Main Results

平均结果显示 LDG 是最稳健的启发式:

- 所有数据集和 partition size 上，LDG 的平均 gain 为 BFS 76%、DFS 73%、Random 75.3%。
- FEM 图上，BFS/DFS 的 Chunking 意外很好，因为图拓扑与 BFS 局部性配合，但 random order 下 Chunking 几乎无增益。
- 社交网络上，Prefer Big 和 Avoid Big 反而显著差于 Hashing；LDG 仍是最佳。
- synthetic graph scaling 实验显示，在相同生成模型下，edge-cut fraction 随图规模基本稳定。
- partitions 数量增加时，各启发式 edge-cut fraction 随之增加，但趋势跟 METIS 相近。

Spark/PageRank 真实系统实验给出工程意义:

| Dataset | Partitions | Hash cut | LDG cut | PageRank result |
| --- | ---: | ---: | ---: | --- |
| LiveJournal | 100 | 76,234,872 | 47,361,254 | naive PR 38.7% faster; combiner PR 28.8% faster |
| Twitter | 400 | 1.464B | 1.341B | naive PR 19.1% faster; combiner PR 18.8% faster |

作者强调，这些速度提升来自 data layout 改善而非 PageRank 算法本身改变；loading time 约 80s/200s，未受 partitioning 方法影响。

## Detailed Outline

| Section/Page | Role | Key Content | Evidence Value |
| --- | --- | --- | --- |
| p1 | wrapper metadata | ResearchGate page and retrieval date | 说明队列标题噪声 |
| p2 | abstract/introduction | graph loading, communication bottleneck, lightweight streaming partitioning | 真实题名、作者、venue、问题动机 |
| p2-p3 | motivation/applications | large graph datasets, distributed graph computation systems, Pregel/GraphLab/Spark-like systems | 连接 graph partitioning 和 distributed graph processing |
| p3-p4 | theory/model | adversarial/random lower bound; streaming model; stream orders | 说明理论困难和假设边界 |
| p4-p6 | algorithms | ten heuristic families; LDG formula; BFS/DFS/random orders | 核心机制 |
| p6-p9 | experiments | datasets, METIS/hash baselines, gains, scalability | 主要证据 |
| p9-p10 | system evaluation | Spark PageRank on LiveJournal/Twitter | 工程效果证据 |
| p10 | conclusion | LDG as low-cost preprocessing; future theory and parallel loaders | 限制与后续方向 |

## Evidence Table

| Observation | Type | Location | Evidence | Confidence |
| --- | --- | --- | --- | --- |
| 真实论文题名是 `Streaming Graph Partitioning for Large Distributed Graphs`。 | identity | p2 | 正文首页给出题名、作者、摘要、KDD 2012。 | high |
| 本文解决的是 graph loading 期间的 streaming balanced graph partitioning。 | problem | p2-p4 | 引言与 streaming model 定义。 | high |
| LDG 是实验中最稳健启发式。 | result | p8 Table 2 | 所有数据集平均 gain: BFS 76%、DFS 73%、Random 75.3%。 | high |
| Spark PageRank 受益来自 edge cut 减少。 | system evidence | p9-p10 Table 3 | LiveJournal/Twitter 上 LDG 降低 cut 并加速 naive/combiner PageRank。 | high |
| 本文不替代 full-information partitioning。 | limitation | p4, p10 | 作者说可作为 preprocessing，完整 repartitioning 仍可能需要。 | high |

## Limitations and Caveats

- 理论上，作者只给出 one-pass adversarial/random order 的负面边界；LDG 的正向理论保证仍是未来工作。
- 模型假设 loader 可以访问已经到达子图的信息，并可维护 vertex-to-partition lookup；真实系统中这会带来分布式状态开销。
- 主要系统实验只覆盖 PageRank on Spark，不能直接推断所有图算法或所有图计算框架。
- 单 loader 模型不完全现实；作者提出 parallel loaders 作为未来工作。
- METIS 是强实践基线但不是最优解；gain 指标是相对 Hashing 到 METIS 的改善比例，不等于接近真正最优的比例。
- 2012 年 Spark/EC2/图处理系统环境已经历史化；工程决策需要后续当前系统来源刷新。

## Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | algorithm-engineering | 论文主要比较算法启发式、系统代价和经验结果。 | high | durable parent exists |
| Direction | graph-algorithms | 图是核心数据模型；目标是 graph partitioning。 | high | durable direction exists |
| Research problem | graph-partitioning | balanced graph partitioning with edge-cut objective。 | high | update existing problem node |
| Method family | streaming graph partitioning | one-pass loading-time partitioning; LDG/heuristic families。 | high | source extension / section under graph partitioning, not standalone node yet |
| Application context | distributed graph processing | Spark PageRank, Pregel, GraphLab, Trinity, Horton 等系统动机。 | medium | bridge candidate; endpoint knowledge missing |
| Artifact/source instance | LDG / Linear Deterministic Greedy | 论文提出并评估的最佳启发式。 | high | representative source extension, not foundation node |

## Retrieval Optimization

- 未来问 “LDG 是什么” 时，应先进入 [[graph-partitioning]]，再打开本文 source note。
- 未来问 “streaming graph partitioning 和 METIS 有什么区别” 时，[[graph-partitioning]] 可以直接给出 offline multilevel 与 loading-time streaming 的对照。
- 未来问 “图计算系统为什么需要 partitioning” 时，本文提供 Spark/PageRank 和 Hashing 对比证据，但 distributed graph processing 作为 Knowledge endpoint 仍缺 foundation。
- 不应新建 `LDG` 上层节点；LDG 是本文 source instance。
- 不应把本文归入 consensus；没有共识协议、fault model、replication 或 agreement 问题。

## Knowledge Handoff

- **Update Knowledge node:** [[graph-partitioning]].
- **Update Direction/domain seeds:** [[graph-algorithms]], [[algorithm-engineering]], [[04_Knowledge/algorithm-engineering/research-dynamics|algorithm-engineering-research-dynamics]].
- **Source extension:** streaming graph partitioning / LDG as loading-time graph data-layout heuristic.
- **Bridge candidate:** `algorithm-engineering/graph-algorithms/graph-partitioning` -> `distributed-systems/distributed-graph-processing`, relation type `applies_to` / `implementation_reuse`, pending until a distributed graph processing endpoint exists.
- **Foundation gap:** distributed graph processing / graph computation frameworks are not yet covered as a durable distributed-systems node.
- **Watch terms:** streaming graph partitioning, LDG, graph data layout, distributed graph processing, Pregel, GraphLab, Spark PageRank.

## Foundation Candidate Judgment

| Candidate | Judgment | Correct Handling | Wrong Handling | Evidence |
| --- | --- | --- | --- | --- |
| graph partitioning | foundation/problem node | update existing [[graph-partitioning]] with streaming setting | treat LDG as the whole concept | p2-p10 |
| streaming graph partitioning | method/problem setting | add section/source extension under graph partitioning; split later if more sources accumulate | create a broad top-level domain from one paper | p3-p6 |
| Linear Deterministic Greedy | representative instance | representative heuristic and query alias | foundation concept | p4-p8 |
| distributed graph processing | bridge/application candidate | queue endpoint/foundation before durable bridge | silently attach to consensus or generic distributed systems | p2-p3, p9-p10 |

## Review Items

- The queue's spurious arXiv id `9530.23397` is derived from DOI digits and should not be treated as an arXiv identifier.
- A future source/foundation pass should create or refresh a distributed graph processing knowledge node before promoting the cross-domain bridge.
- Current engineering guidance should not rely solely on 2012 Spark/PageRank timings.

## Processing Log

| Date | Run ID | Action |
| --- | --- | --- |
| 2026-06-23 | nahida-paper-intake-20260623-streaming-graph-partitioning | Deep-read local PDF, corrected noisy title/classification, and handed off to graph partitioning knowledge node. |
