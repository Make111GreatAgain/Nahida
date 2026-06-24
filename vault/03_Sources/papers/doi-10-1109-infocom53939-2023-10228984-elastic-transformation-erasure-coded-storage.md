---
id: "doi-10-1109-infocom53939-2023-10228984"
title: "Balancing Repair Bandwidth and Sub-Packetization in Erasure-Coded Storage via Elastic Transformation"
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
  - "p1-p10 main paper"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1109/INFOCOM53939.2023.10228984"
doi: "10.1109/INFOCOM53939.2023.10228984"
arxiv_id: ""
venue: "IEEE INFOCOM 2023 - IEEE Conference on Computer Communications"
year: "2023"
authors:
  - "Kaicheng Tang"
  - "Keyun Cheng"
  - "Helen H. W. Chan"
  - "Xiaolu Li"
  - "Patrick P. C. Lee"
  - "Yuchong Hu"
  - "Jie Li"
  - "Ting-Yi Wu"
local_pdf_path: "~/Desktop/paper/Balancing_Repair_Bandwidth_and_Sub-Packetization_.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/balancing-repair-bandwidth-and-sub-packetization-in-erasure-coded-storage-via-elastic-transformation-c6f5dc936d84-pages.txt"
sha256: "c6f5dc936d847cbf8c821dc55dc87fc23be6e1aaee9c29f3416042a8022251ec"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0099"
queue_rank: 99
hierarchy_level: "source"
domain_id: "distributed-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "erasure-coded-storage"
  - "storage-repair-optimization"
ontology_path:
  - "distributed-systems"
  - "data-management-and-storage"
  - "erasure-coded-storage"
primary_ontology_path: "distributed-systems/data-management-and-storage/erasure-coded-storage"
secondary_ontology_paths: []
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "distributed-systems"
  directions:
    - "data-management-and-storage"
  topics:
    - "erasure-coded-storage"
    - "storage-repair-optimization"
domains:
  - "distributed-systems"
topics:
  - "erasure-coded-storage"
  - "storage-repair-optimization"
aliases:
  - "Elastic Transformation"
  - "OpenEC-ET"
  - "RS-ET"
  - "LRC-ET"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
  - "storage/erasure-coding"
direction_facets:
  parent_domain:
    - "distributed-systems"
  subdomain:
    - "data-management-and-storage"
  problem:
    - "erasure-coded-storage"
    - "storage-repair-optimization"
  method_family:
    - "erasure-code-transformation"
    - "repair-bandwidth-optimization"
    - "sub-packetization-tradeoff"
  system_layer:
    - "storage-redundancy"
    - "failure-repair"
  evaluation_context:
    - "HDFS"
    - "OpenEC"
    - "single-block-repair-time"
  application:
    - "distributed-storage-systems"
  bridge: []
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-elastic-transformation-erasure-coded-storage"
source_refs:
  - "doi:10.1109/INFOCOM53939.2023.10228984"
  - "sha256:c6f5dc936d847cbf8c821dc55dc87fc23be6e1aaee9c29f3416042a8022251ec"
confidence: "high"
trust_tier: "primary"
primary_direction: "distributed-systems -> data-management-and-storage"
secondary_directions: []
classification_status: "active"
classification_confidence: "high"
classification_evidence:
  - "title"
  - "abstract"
  - "IEEE INFOCOM venue"
  - "Sections II-V"
taxonomy_version: "1.0"
---

# Balancing Repair Bandwidth and Sub-Packetization in Erasure-Coded Storage via Elastic Transformation

## 论文身份

- 标题: Balancing Repair Bandwidth and Sub-Packetization in Erasure-Coded Storage via Elastic Transformation
- 作者: Kaicheng Tang, Keyun Cheng, Helen H. W. Chan, Xiaolu Li, Patrick P. C. Lee, Yuchong Hu, Jie Li, Ting-Yi Wu
- 机构: The Chinese University of Hong Kong; Huazhong University of Science and Technology; Huawei Technologies Co., Ltd., Hong Kong
- 会议/期刊: IEEE INFOCOM 2023 - IEEE Conference on Computer Communications
- 年份: 2023
- DOI: `10.1109/INFOCOM53939.2023.10228984`
- arXiv: not applicable; queue metadata had a false arXiv-like parse from DOI and was corrected during absorption.
- 链接: `https://doi.org/10.1109/INFOCOM53939.2023.10228984`
- 本地 PDF: `~/Desktop/paper/Balancing_Repair_Bandwidth_and_Sub-Packetization_.pdf`
- 提取文本: `vault/02_Raw/pdf/extracted/balancing-repair-bandwidth-and-sub-packetization-in-erasure-coded-storage-via-elastic-transformation-c6f5dc936d84-pages.txt`
- 代码: paper lists `http://adslab.cse.cuhk.edu.hk/software/openec-et`; code was not opened in this run.
- License: not specified in local PDF.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: queue metadata says `codex-bundled-python:pypdf`; extracted text covers all 10 pages.
- 页数: 10
- 已覆盖章节/页码: p1 abstract/introduction; p2-p3 background and related work; p3-p6 elastic transformation construction and applications; p6-p8 numerical analysis; p8-p9 testbed evaluation; p9-p10 conclusion and references.
- 已检查附录: no appendix in local PDF.
- 未覆盖章节/页码: none.
- Extraction gaps: figure labels and formulas are noisy in places, but section text, theorem statements, experimental setup and headline results are readable.
- 精读说明: 本笔记保留论文的 code-transformation 构造、故障容忍论证、修复带宽/修复时间模型和 HDFS/OpenEC 实验结果；OpenEC-ET 代码仓库未在本轮分析。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1 Abstract and Introduction | Problem and contribution | Erasure coding 低冗余但修复带宽高；access-optimal codes 理论上降低修复带宽/磁盘读，但高 sub-packetization 导致 non-sequential I/O；提出 elastic transformation。 | high | 决定归属为 erasure-coded storage repair optimization。 |
| p2-p3 Section II | Background and related work | RS、MSR/access-optimal MSR、LRC、Hitchhiker、HashTag、Li et al. generic transformation、repair-efficient algorithms。 | high | 给上层知识节点提供方法路线。 |
| p3 Motivating examples | Motivation | RS-ET(9,6) 以 `alpha=3` 在修复带宽和子分包之间取中间点；LRC-ET 优化 global parity repair。 | high | 说明论文不是单纯追求最小带宽，而是系统性能折中。 |
| p3-p6 Section III | Method | Transformation arrays: square/non-square arrays, rotation, pairwise coupling, systematic transformation; 应用于 RS、LRC、Hitchhiker、HashTag；证明 MDS fault tolerance field-size bound。 | high | 核心机制。 |
| p6-p8 Section IV | Numerical analysis | Theorem 2/3 给 RS-ET/LRC-ET repair bandwidth lower bound；修复时间模型把 network transmission 和 I/O time 合并，显示 alpha 过大时 I/O 反噬。 | high | 上层知识节点应吸收为 tradeoff model。 |
| p8-p9 Section V | Testbed evaluation | OpenEC-ET on Hadoop 3.0.0 HDFS, 17-machine cluster; 比较 RS、Hitchhiker、HashTag、LRC；测 network bandwidth 和 packet size 的影响。 | high | 工程证据。 |
| p9 Section VI | Conclusion | Elastic transformation 可把 base code 转成低修复带宽、可配置 sub-packetization 的 code；理论与实测均支持收益。 | medium | 结论摘要。 |

## 核心精读笔记

### 背景、动机与问题边界

- 背景脉络: 生产级分布式存储常用 erasure coding 以低冗余获得高可靠性，RS codes 是典型选择。相比复制，纠删码可以在同等冗余下获得更高可靠性，但单个 packet/block 丢失时通常需要从多个节点读取并传输大量数据来重建。
- 现有方法不足: access-optimal MSR codes 能把 repair bandwidth 和 disk reads 推到理论最优，但常需要很高 sub-packetization。高 `alpha` 把 packet 切得很细，导致更多 non-sequential I/O；在真实存储系统中，网络节省可能被磁盘读开销抵消。
- 本文问题定义: 给定一个 base erasure code，构造一个 transformed code，在保持原有 fault tolerance 的前提下，用可配置 `alpha` 降低单 packet/block 修复带宽，并避免被 access-optimal MSR 的高 sub-packetization 固定住。
- 明确不解决的问题: 论文主要优化 single lost packet/block repair；不把多故障并发恢复作为主问题。它不是新的完整存储系统，也没有重新设计 HDFS/OpenEC 的复制、调度或一致性机制。
- 证据锚点: Abstract, §I, §II-C, §III opening.

### 模型、假设与定义

- 基本存储模型: 一个 `(n,k)` erasure code 把 `k` 个 data packets 编成 `n-k` 个 parity packets，任意 `k` 个 packets 可重建原始数据。每个 packet 可以按 sub-packetization level `alpha` 切为 `alpha` 个 sub-packets，多个 sub-stripes 独立编码。
- Repair bandwidth: 修复一个 lost packet/block 时从 surviving nodes 读取并传输的数据量。论文把它作为理论模型的核心目标，也在 HDFS prototype 中用 single-block repair time 间接体现。
- Sub-packetization: packet 被切成多少 sub-packets。较高 `alpha` 往往给 code construction 更多自由度，从而降低 repair bandwidth，但会带来更细碎的 reads 和 non-sequential I/O。
- 主要 baseline family:
  - RS codes: 存储开销低且生产常用，但修复一个 lost packet 通常需要读取 `k` 个 packets。
  - MSR/access-optimal MSR: 理论上最小 repair bandwidth 和 disk reads，但 `alpha` 常呈指数级增长。
  - LRC: 让 data/local parity 局部修复，但 global parity 仍可能需要像 RS 一样读 `k` 个 packets。
  - Hitchhiker/HashTag: 通过 piggybacking 或 code design 降低 data repair bandwidth，但 parity repair 仍有空间。
- 证据锚点: §II-A, §II-B.

### 方法、协议或系统机制

- 总体思想: Elastic transformation 把 base code 转成新的 repair-friendly code；它不只给一个固定 `alpha`，而是在 `alpha` 从 2 起的一组可配置点上做 bandwidth/I/O tradeoff。它既可作用于所有 nodes，也可只覆盖 subset nodes，例如 LRC global parity packets 或 Hitchhiker/HashTag parity packets。
- Square transformation array: 对一个 `alpha x alpha` sub-packet array 先按行循环旋转，再对轴对称位置做 pairwise coupling，最后用 systematic transformation 把 non-systematic form 转回 data sub-packets 并重算 parity sub-packets。直观效果是修复某个 node 时可以用更少 sub-packets 恢复相应输入。
- Non-square transformation array: 当 `(n,k)` code 不能整齐分成 square arrays 时，论文用两个重叠 square arrays 形成 `alpha x gamma` non-square array，其中 `alpha < gamma < 2alpha`。这让 transformation 适用于一般参数，而不是只适合整除情形。
- RS-ET application: 对 RS(n,k) 的所有 packets 应用 transformation arrays。修复 lost packet 时先选择 major sub-stripe，再读取三类 sub-packets: major sub-stripe 中的 `S1`、与 `S1` coupled 的 `S2`、以及与 lost sub-packets coupled 的 `S3`，然后恢复 data-vector inputs 和 lost sub-packets。
- Larger alpha construction: 当 `alpha > n-k` 且是可分解的 composite number，论文把 `alpha` 写成若干 `alpha_i` 的乘积，逐步对剩余 nodes 应用 transformation。`alpha=(n-k)^{ceil(n/(n-k))}` 时可达到 Li et al. access-optimal MSR construction 的点。
- Other code families: 对 LRC，只需覆盖 global parity packets；对 Hitchhiker/HashTag，可覆盖 parity packets。因为 parity packets 本来就是 coded packets，应用到 parity subset 时不需要 systematic transformation。
- 证据锚点: §III-A, §III-B, Figures 3-7.

### 理论、证明或正确性论证

- Fault tolerance theorem: 若 base code 是 MDS code，且 finite field size `q` 大于论文给出的组合式下界，则存在 coupling coefficients 使 transformed code 仍保持 MDS。证明把 transformed code 看成 `k alpha` 个变量到 `n alpha` 个 encoded sub-packets 的线性系统，并要求任意 `k` 个 nodes 的 coefficient matrix determinant 非零。
- 实用性判断: 虽然 theorem 给出充分条件，作者通过枚举 `n choose k` combinations 发现中等规模参数如 `(16,12)` 可在 `GF(2^8)` 且 `e_{i,j}=2` 下保持 MDS，说明实现上不必依赖巨大 field。
- Repair bandwidth lower bound: Theorem 2 对 RS-ET 给出 single lost packet repair bandwidth 下界，按 `S1/S2/S3` 计数；Theorem 3 对 LRC-ET global parity repair 给出 `k + alpha - 1` 形式下界。
- Repair time model: 论文把 repair time 写成 network term 与 I/O term 之和。`R(alpha)` 降低会减少网络传输，但 `tau(alpha)` 和 sub-packet reads 会让 I/O 在大 `alpha` 时上升。该模型解释了 access-optimal MSR 点不一定是实际 repair time 最优点。
- 证据锚点: §III-C, §IV-A, §IV-B.

### 实验、评估或案例

- Prototype: OpenEC-ET 基于 OpenEC 实现，运行在 Hadoop 3.0.0 HDFS 上，支持 RS、LRC、Hitchhiker、HashTag，并使用 ISA-L 做 coding operations。论文称新增 4.8K LoC。
- Testbed: 17 台机器，一台 NameNode，剩余为 DataNodes；每台机器 quad-core 3.4 GHz Intel Core i5、32 GiB RAM、7200 RPM 1 TB SATA disk；10 Gb/s switch；默认 network bandwidth 通过 Wondershaper 设为 1 Gb/s，HDFS block size 64 MiB，packet size 1 MiB。
- Metric: single-block repair time，从发起 repair request 到 failed block repaired；每个 stripe 擦除一个 block，确保每个 node 有一个 erased block，平均修复所有 `n` 个 blocks；10 次运行并给出 95% confidence interval。
- Overall repair performance: 对 `(14,10)`，elastic transformation 将 RS、Hitchhiker、HashTag 的 repair time 分别降低 26.2-39.8%、13.9-21.6%、11.3-18.6%。
- Network/sub-packetization sensitivity: 对 RS(14,10)，1 Gb/s 下 RS-ET `alpha=64` 相比 RS `alpha=1` 降低 repair time 56.3%，相比 access-optimal MSR point `alpha=256` 降低 18.3%。10 Gb/s 下网络不再是主要瓶颈，`alpha=64` 相比 access-optimal point 降低 51.4%，显示过高 `alpha` 的 I/O overhead 更明显。
- Packet size sensitivity: packet size 越小，non-sequential I/O overhead 越严重。对 RS(14,10)，`alpha=64` 在 256 KiB packet size 下相比 access-optimal MSR point 降低 repair time 40.1%。
- 证据锚点: §V, Figures 10-12.

### 作者结论与我的判断

- 作者明确声称: Elastic transformation 可以把 base code 转为 repair bandwidth 更小且 sub-packetization 可配置的 code，并能在理论和 HDFS 实测中取得更好的 repair performance。
- 由证据支持的判断: 本文最值得吸收的上层知识不是 “Elastic Transformation” 本身，而是 erasure-coded storage 中 repair bandwidth、disk read/I/O locality 和 sub-packetization 的系统性 tradeoff。Elastic Transformation 是这个问题下的一条代表性 code-transformation 路线。
- 仍需谨慎的推断: 结果主要针对 single-block repair，且 testbed 是 HDD + HDFS/OpenEC 环境；SSD、对象存储、跨机房、后台 repair scheduling、concurrent failures 和 degraded reads 需要其他 sources 校准。
- 证据锚点: Abstract, §IV-B, §V, §VI.

## 层级候选分类

- L1 Domain candidate: `distributed-systems`
- L2 Direction candidate: `data-management-and-storage`
- L3 Topic/content cluster candidates: `erasure-coded-storage`; `storage-repair-optimization`
- Ontology path: `distributed-systems/data-management-and-storage/erasure-coded-storage`
- 备选归属: `distributed-systems/data-management-and-storage/storage-engines` as an adjacent implementation layer, but the paper's main object is erasure-coded redundancy and repair.
- 父级领域: distributed systems
- 学术子领域: erasure-coded distributed storage; storage repair optimization
- 任务/问题: reducing repair bandwidth while controlling sub-packetization and non-sequential I/O
- 方法族: erasure-code transformation; pairwise coupling; repair-bandwidth modeling; HDFS/OpenEC prototype evaluation
- 模型/协议/算法族: RS-ET, LRC-ET, transformed Hitchhiker, transformed HashTag, access-optimal MSR comparison
- 评测场景: HDFS single-block repair, OpenEC middleware, bandwidth/packet-size sensitivity
- Benchmark/应用: distributed storage repair testbed
- 别名: `Elastic Transformation`, `OpenEC-ET`, `RS-ET`, `LRC-ET`
- 相邻方向: storage engines; blockchain data availability erasure coding; asynchronous reliable broadcast using erasure coding
- 置信度: high
- 分类理由: title, abstract, background, construction, model and evaluation all target erasure-coded distributed storage repair.
- 分类状态: active
- 分类证据: Abstract, §I-§V.
- Taxonomy version: 1.0
- Direction facets: see frontmatter.
- Tags: `nahida/source`, `nahida/paper`, `storage/erasure-coding`
- Map memberships: `Distributed systems -> Data management and storage -> Erasure-coded storage`
- 归属说明: 该论文不是 distributed transactions；queue 原来的 `distributed-transactions` topic 是 DOI/abstract 冷启动误分，本轮吸收已修正。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `distributed-systems` | Production storage systems, HDFS/OpenEC, repair over distributed nodes | high | existing domain |
| Research background | erasure-coded storage; RS codes; MSR/access-optimal repair; LRC; piggybacking | §I-§II | high | create/update knowledge node |
| Research problem | storage repair optimization under repair-bandwidth/sub-packetization/I/O tradeoff | Abstract, §II-C, §IV-B | high | new problem node |
| Foundation concepts | erasure coding, repair bandwidth, sub-packetization, MSR codes, LRC | §II | medium | keep in `erasure-coded-storage` foundation_thin node; future sources can split |
| Method family | erasure-code transformation via transformation arrays and pairwise coupling | §III | high | source extension under method route |
| Application/evaluation context | HDFS/OpenEC single-block repair | §V | high | source-only and evaluation context |
| Artifact/source instance | `Elastic Transformation`, `OpenEC-ET`, `RS-ET`, `LRC-ET` | §III-§V | high | source extension, not standalone foundation node |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `distributed-systems/data-management-and-storage/erasure-coded-storage`
- 它能帮助未来哪些问题少读 source notes: “纠删码存储为什么修复慢”“repair bandwidth 和 sub-packetization 怎么权衡”“MSR 理论最优为什么不一定系统最快”“HDFS/OpenEC 下 erasure-code repair 怎么评估”。
- 哪些内容应留在 source note，而不是创建上层节点: transformation array 公式、Theorem 1 的 field-size bound、Theorem 2/3 的具体计数证明、HDFS testbed 机器配置和 exact performance numbers。
- 哪些上层节点过薄、缺失或需要 foundation_pack: `erasure-coded-storage` 新建后仍是 `foundation_thin`，需要 future source 补齐 RS/LRC/MSR/Clay/OpenEC/production storage foundations。
- 哪些候选只是别名/query key/watch term: `Elastic Transformation`, `RS-ET`, `LRC-ET`, `OpenEC-ET`。

## 一句话贡献

Elastic Transformation 用可配置 sub-packetization 的 code transformation，在保持 erasure-code fault tolerance 的同时，在 repair bandwidth 和 non-sequential I/O 之间提供比固定 access-optimal MSR 点更实用的系统折中。

## 问题设定

Erasure-coded storage 在低冗余可靠性和修复成本之间有长期张力。RS codes 可靠且常用，但修复任意 lost packet 需要读 `k` 个 packets；MSR/access-optimal codes 理论上节省网络和磁盘读取，但高 `alpha` 带来的随机/非顺序 I/O 可能让真实 repair time 变差。本文设定的目标是: 对任意 base code，用一组可配置 `alpha` 的 transformation 降低 repair bandwidth，并让系统可以按网络和 I/O 条件选中间点。

## 方法概览

### 组成部分

- Transformation arrays: square array 和 non-square array 是构造核心。
- Pairwise coupling: 通过对旋转后的对称位置做线性组合，让修复某个 lost packet 时能从 coupled sub-packets 中恢复必要输入。
- Systematic transformation: 对 data sub-packets 重新映射，保证 transformed code 保持 systematic form。
- Repair procedure: 根据 lost node 选择 major sub-stripe，读取 `S1/S2/S3` 三类 sub-packets，恢复 data-vector inputs，再恢复 lost sub-packets。
- OpenEC-ET implementation: 在 OpenEC/HDFS 上实现 RS、LRC、Hitchhiker、HashTag 的 elastic transformation variants。

### 流程或协议

1. 选择 base erasure code 和 sub-packetization level `alpha`。
2. 把 data/parity packets 划分为 square 或 non-square transformation arrays。
3. 对每个 array 执行 rotation 和 pairwise coupling。
4. 对涉及 data packets 的 arrays 执行 systematic transformation，并更新 parity sub-packets。
5. 修复时选择 major sub-stripe，读取最少 coupled sub-packets 组合，完成 lost packet/block recovery。

### 关键定义、公式、算法或定理

- `alpha`: sub-packetization level，越大越有机会降低 repair bandwidth，但也会提高 non-sequential I/O 风险。
- Theorem 1: 在足够大 finite field 上，elastic transformation 可以保持 MDS fault tolerance。
- Theorem 2/3: 分别给 RS-ET 和 LRC-ET 的 single-packet repair bandwidth lower bound。
- Repair time model: `T = network transmission term + I/O term`，用于解释最小 repair bandwidth 不等于最短 repair time。

### 假设条件

- 主要面向 single lost packet/block repair，且单失效比多失效并发更常见。
- Coding computation 相比 network transmission 和 I/O 被视为可忽略。
- Field size 和 coefficients 需要足以保持 fault tolerance；实现中作者用 `GF(2^8)` 和固定 coefficient 经验验证中等规模参数。

## 创新点

- 新思想: 把 erasure-code transformation 做成可调 `alpha` 的 elastic family，而不是只追求 access-optimal MSR 的单一高 `alpha` 点。
- 对已有工作的扩展: 相比 Li et al. generic transformation 只能得到较稀疏的 `alpha` 点，本文通过 square/non-square transformation arrays 提供更宽 `alpha` 范围；还可作用于 LRC、Hitchhiker、HashTag 的未优化节点子集。
- 工程或实证贡献: OpenEC-ET 在 HDFS/OpenEC 上验证理论 tradeoff，显示在真实网络/I/O条件下中间 `alpha` 可优于 access-optimal MSR。
- 依赖的 prior work: RS codes, access-optimal MSR/Clay, LRC, Hitchhiker, HashTag, OpenEC, Li et al. generic transformation。

## 实验与结果

### 实验设置

本地 17-machine cluster，HDFS atop Hadoop 3.0.0，OpenEC middleware，ISA-L coding operations；默认 block size 64 MiB，packet size 1 MiB，network bandwidth 1 Gb/s。

### 数据集或 Benchmark

实验是 storage-system repair workload，不是外部数据集 benchmark。写入 `n` stripes 后，每个 stripe 擦除一个 block，使每个 node 恰有一个 erased block，再测平均 single-block repair time。

### Baseline

RS、Hitchhiker、HashTag、LRC 以及 access-optimal MSR point；对应的 transformed variants 包括 RS-ET、HH-ET、HTEC-ET、LRC-ET。

### 指标

- Theoretical/numerical: normalized repair bandwidth, modeled repair time, network/I/O breakdown.
- System evaluation: single-block repair time, sensitivity to `alpha`, network bandwidth and packet size.

### 主要结果

- RS-ET、HH-ET、HTEC-ET 在多个 `(n,k)` 参数下均能降低 repair time。
- 对 RS(14,10)，1 Gb/s 下 `alpha=64` 比 RS `alpha=1` 快 56.3%，比 access-optimal point `alpha=256` 快 18.3%。
- 对 10 Gb/s 网络，I/O 成为更主要瓶颈，`alpha=64` 比 access-optimal point 快 51.4%。
- 小 packet size 会放大 non-sequential I/O overhead，进一步支持“中间 alpha 可能最佳”的结论。

### 消融实验

论文没有按 ML 式 ablation 拆掉组件，但用三类敏感性实验替代: 不同 `alpha`、不同 network bandwidth、不同 packet size。

### 效率、成本或安全性

主要效率收益来自减少 repair bandwidth 同时控制 sub-packetization。安全性/正确性层面，论文证明 MDS fault tolerance 可保持，但不讨论恶意节点、数据完整性认证或 Byzantine repair。

### 结果 caveat

结论对 HDFS/OpenEC/HDD testbed 有较强证据；迁移到 SSD、NVMe、对象存储、跨区域网络或多故障修复时需要新 source 佐证。
