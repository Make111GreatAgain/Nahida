---
id: "doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training"
title: "PipeDream: Generalized Pipeline Parallelism for DNN Training"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "normalized"
source_kind: "pdf"
source_subtype: "paper_doi"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p15 full extracted text"
  - "Abstract, Sections 1-8, Figures 1-14, Tables 1-4, and References"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1145/3341301.3359646"
doi: "10.1145/3341301.3359646"
arxiv_id: ""
venue: "SOSP 2019"
year: "2019"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "training-systems"
topic_ids:
  - "dnn-training-parallelism"
  - "pipeline-parallelism"
  - "distributed-training-systems"
  - "gpu-training-throughput"
ontology_path:
  - "ml-systems"
  - "training-systems"
  - "dnn-training-parallelism"
primary_ontology_path: "ml-systems/training-systems/dnn-training-parallelism"
secondary_ontology_paths:
  - "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "training-systems"
    - "distributed-training-systems"
  topics:
    - "dnn-training-parallelism"
    - "pipeline-parallelism"
    - "model-parallelism"
    - "data-parallelism"
    - "weight-stashing"
    - "one-forward-one-backward-scheduling"
domains:
  - "ml-systems"
topics:
  - "dnn-training-parallelism"
  - "distributed-training-systems"
  - "pipeline-parallelism"
  - "model-parallelism"
  - "data-parallelism"
  - "training-throughput"
  - "communication-overlap"
  - "weight-stashing"
aliases:
  - "PipeDream"
  - "Generalized Pipeline Parallelism for DNN Training"
  - "1F1B pipeline parallelism"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/ml-systems"
  - "nahida/training-systems"
direction_facets:
  parent_domain:
    - "ml-systems"
  subdomain:
    - "training-systems"
  problem:
    - "dnn-training-time"
    - "multi-accelerator-parallelization"
    - "communication-bottleneck"
    - "pipeline-scheduling-correctness"
  method_family:
    - "pipeline-parallelism"
    - "hybrid-data-model-parallelism"
    - "automatic-layer-partitioning"
    - "weight-stashing"
    - "1f1b-scheduling"
  system_layer:
    - "gpu-training-runtime"
    - "pipeline-scheduler"
    - "stage-partition-optimizer"
    - "parameter-version-manager"
  evaluation_context:
    - "VGG-16, ResNet-50, AlexNet, GNMT, AWD-LSTM, S2VT"
    - "Azure NC24 v3 V100, AWS p3.16xlarge V100, private Titan X cluster"
  bridge:
    - "ml-systems/training-systems/dnn-training-parallelism -> ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-pipedream-dnn-training-parallelism"
source_refs:
  - "doi:10.1145/3341301.3359646"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> training-systems"
secondary_directions:
  - "ml-systems -> privacy-and-trustworthy-ml -> trustworthy-distributed-ml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Title, abstract, and Sections 1-8 target DNN training throughput via pipeline parallelism"
  - "The PDF contains no consensus protocol, blockchain protocol, or BFT/CFT mechanism"
  - "Queue arXiv metadata was derived from DOI suffix and is not a paper arXiv ID"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/sosp_pipedream.pdf"
pdf_sha256: "d29b17c859a139df87f8b0c0634c757247a412ce9e3430d3361e077cc8bb95a9"
pdf_pages: 15
pdf_size_bytes: 1089427
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/pipedream-generalized-pipeline-parallelism-for-dnn-training-d29b17c859a1-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0113"
---

# PipeDream: Generalized Pipeline Parallelism for DNN Training

## 论文身份

- 标题: PipeDream: Generalized Pipeline Parallelism for DNN Training
- 作者: Deepak Narayanan, Aaron Harlap, Amar Phanishayee, Vivek Seshadri, Nikhil R. Devanur, Gregory R. Ganger, Phillip B. Gibbons, Matei Zaharia
- 机构: Stanford University, Carnegie Mellon University, Microsoft Research
- 会议/期刊: SOSP 2019
- 年份: 2019
- DOI: `10.1145/3341301.3359646`
- 链接: `https://doi.org/10.1145/3341301.3359646`
- 本地 PDF: `~/Desktop/paper/sosp_pipedream.pdf`
- SHA-256: `d29b17c859a139df87f8b0c0634c757247a412ce9e3430d3361e077cc8bb95a9`
- 代码: unknown in local PDF
- 数据/任务: ImageNet, WMT16 EN-De, Penn Treebank, MSVD; image classification, translation, language modeling, video captioning
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: Codex bundled Python `pypdf`; extracted text stored in `vault/02_Raw/pdf/extracted/pipedream-generalized-pipeline-parallelism-for-dnn-training-d29b17c859a1-pages.txt`.
- 页数: 15
- 已覆盖章节/页码: p1-p15, Abstract, Sections 1-8, Figures 1-14, Tables 1-4, References.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 抽取文本有少量连词粘连、数学符号和表格格式损失；核心算法、表格结果和结论可由正文与表格交叉确认。
- 分类纠正: 队列把本文放入 `distributed-systems/consensus/needs-review`，且把 DOI 后缀误读为 `arxiv_id=1301.33596`。精读确认本文是 ML training systems 论文，不是共识、区块链或 BFT/CFT 论文。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | DNN 训练耗时，需要多加速器并行；现有 intra-batch parallelism 在 worker 数增加时收益递减；PipeDream 引入 inter-batch pipelining，版本化参数并自动划分层。 | high | 明确 primary domain 是 ML training systems。 |
| §1 / p1-p2 | 动机 | Data parallelism 在 32 GPUs 上可能让 communication stalls 占到大部分时间；更快 GPU 会放大通信瓶颈。 | high | 支撑 DNN training parallelism 问题节点。 |
| §2 / p2-p4 | 背景与相关工作 | Data parallelism, model parallelism, hybrid OWT/FlexFlow, GPipe 等路线及限制。 | high | 给出方法族边界。 |
| §3 / p4-p5 | Opportunity | Pipeline parallelism 可以减少跨 worker 通信并重叠 computation/communication；对部分模型通信量可降超过 85%。 | high | 解释为什么不是纯 data parallelism。 |
| §4 / p5-p8 | Challenges and design | 自动层划分、stage replication、1F1B/1F1B-RR 调度、weight stashing、VerticalSync 和 memory tradeoff。 | high | 核心系统机制。 |
| §5 / p8-p9 | Implementation | 约 3000 LOC Python library，基于 PyTorch autograd/operators；profile、optimize、partition、runtime schedule、parameter/intermediate state management、checkpointing。 | high | 工程实现证据。 |
| §6 / p9-p13 | Evaluation | 7 个 DNN、3 类集群；最高 5.3x image classification、3.1x translation、4.3x language modeling、3x video captioning；优于 model parallelism、hybrid 和 GPipe-like scheduling。 | high | 性能主张证据。 |
| §7 / p13 | Discussion | 讨论 memory footprint、pipeline depth、mixed precision/LARS 等。 | medium | 限制与适用边界。 |
| §8 / p13 | Conclusion | PipeDream 自动把 DNN training workload 分布到 workers，并结合 inter-batch pipelining 与 intra-batch parallelism。 | medium | 总结。 |
| References / p13-p15 | 相关工作 | TensorFlow, PyTorch, NCCL, GPipe, FlexFlow, data/model parallelism, optimization 等。 | medium | 后续 search 线索。 |

## 核心精读笔记

### 背景、动机与问题边界

本文解决的是 DNN 训练系统的并行化与吞吐问题。DNN 训练迭代包含 forward pass、loss 计算、backward pass 和参数更新；随着模型变大、训练数据变多，单 GPU 或少量 GPU 训练时间很长。最常见的 data parallelism 会把同一个 minibatch 或不同 minibatches 的训练拆给多个 workers，然后通过 all-reduce 或 parameter server 同步梯度/参数。该路线简单、适合许多模型，但 worker 数增加后通信开销快速成为瓶颈，尤其是跨服务器和网络带宽较弱时。

PipeDream 的问题定义不是“如何让远程 trainer 可信”，也不是“如何证明训练正确”。它面向同一管理域或可控集群里的多 GPU 训练性能，目标是在保持模型达到同等精度所需 epoch 数接近 data parallelism 的前提下，提高 hardware utilization、减少跨 worker 通信并缩短 time-to-accuracy。

### 基础概念与方法边界

本文区分了四类训练并行路线:

- Data parallelism: 每个 worker 持有完整模型，在不同数据分片上训练，再同步梯度或参数。优点是模型代码改动小；限制是通信量与模型参数大小相关，worker 数越高，通信 stall 越明显。
- Model parallelism: 把模型层或算子切到多个 worker，每个 worker 只计算一部分。优点是可训练单卡放不下的模型；限制是传统 naive model parallelism 容易让 worker 空闲，并要求手工划分。
- Hybrid parallelism: 把 data parallelism 和 model parallelism 混合，例如部分层复制、部分层切分。FlexFlow/OWT 是相关背景；PipeDream 认为它们没有充分利用 inter-batch pipelining。
- Pipeline parallelism: 把模型划分为按层顺序连接的 stages，让不同 minibatches 的 forward/backward 在不同 stages 上重叠执行。PipeDream 的核心贡献是在 DNN 的双向 forward/backward 结构中实现低 stall 的 pipeline schedule，并处理参数版本一致性。

这些概念是上层知识应保留的通用概念；PipeDream、1F1B、weight stashing 是本文的系统实例与机制细节，默认留在 source note 和 `dnn-training-parallelism` 的方法路线中，不单独升级为基础概念节点。

### PipeDream 的系统机制

PipeDream 把模型层切成连续 stages，并允许某些 stages 被复制形成 stage-level data parallelism。它先用短暂 single-GPU profiling 获取每层 forward/backward 计算时间、activation/output size 和 weight size，然后运行 optimizer 决定 layer partition、每个 stage 的 replication factor 和 pipeline 内需要的 in-flight minibatches 数。

优化目标是降低 pipeline 中最慢 stage 的时间，同时考虑硬件拓扑和跨 stage 通信。对一个 stage 使用 `m` 个 replicas 时，optimizer 估计 data-parallel synchronization communication cost 近似为 `(m-1)/m * |weights|` 的 send/receive。论文使用按硬件层级展开的 dynamic programming，复杂度写作 `sum_k O(N^3 m_k^2)`，实验中 optimizer 运行时间小于 8 秒。

PipeDream 的运行时调度用 1F1B:

- Startup 阶段注入足够 minibatches，让 pipeline 填满。
- Steady state 中，每个 worker 交替做一个 minibatch 的 forward 和较早 minibatch 的 backward。
- 当 stage 有 replicas 时，1F1B-RR 用 deterministic round-robin 根据 minibatch ID 分配 worker；同一个 minibatch 的 forward/backward 回到同一个 worker，以复用 parameter state 和 intermediate state。
- 论文把需要填满 pipeline 的 minibatch 数称为 NOAM，计算与 workers 数和输入 stage replicas 数有关。

DNN pipeline 的关键难点是 backward pass 依赖 forward pass 的中间状态和参数版本。如果 forward 使用某一版本权重、backward 使用另一版本权重，梯度可能不是任何真实参数向量下的 loss 梯度，训练会失效。PipeDream 用 weight stashing 为每个 minibatch 保留其 forward pass 使用过的 weight version，使 backward pass 在该 stage 使用同一版本权重。它还讨论了 VerticalSync，把不同 stages 对同一 minibatch 使用的权重版本同步起来，但默认不启用，因为元数据成本较高。

### 实现细节

PipeDream 是约 3000 行 Python library，使用 PyTorch autograd 和 operators。它的 workflow 是:

1. Profiling: 在单 GPU 上 profile 每层计算时间、activation size 和 weight size。
2. Optimization: 使用 profile 和 cluster/topology 信息输出 annotated computation graph。
3. Partitioning: 对每个 stage 生成对应 `torch.nn.Module`。
4. Runtime: 按 1F1B-RR schedule forward/backward，管理 parameters、intermediate states 和 communication。

Parameter state 方面，PipeDream 在 GPU memory 中维护多个版本。每次 optimizer step 更新最新版本，旧版本只在确定不再有更晚到达的 backward pass 需要时丢弃。Intermediate state 方面，forward 输出和中间激活保持到同一 minibatch 的 backward 完成；backward 用完或发送之后释放。

Stage replication 使用 PyTorch DistributedDataParallel 同步同一 stage 的 replicas。PipeDream 也把普通 data parallelism 看成只有一个 replicated stage 的特例。实验中 data-parallel baselines 使用 NCCL；pipeline 小 tensor 通信使用 Gloo，因为当时 PyTorch DistributedDataParallel 不支持在同一模型中混用 Gloo 和 NCCL。Checkpointing 以 stage 为单位在 epoch 结束时写出，失败恢复时所有 stages 回到最后成功 checkpoint。

### 实验与结果

论文评估了 7 个模型和 3 类硬件环境:

| 模型/任务 | 代表数据集 | PipeDream 主要结果 | 备注 |
| --- | --- | --- | --- |
| VGG-16 / image classification | ImageNet | 在 Cluster-A 4x4 V100 PCIe/10Gbps 上最高 5.28x epoch/time-to-accuracy speedup；在 Cluster-B 2x8 V100 NVLink/25Gbps 上 2.98x epoch speedup、2.46x time-to-accuracy speedup。 | optimizer 选择 `15-1` config，即大部分卷积层复制，通信重的 fully-connected 层不复制。 |
| ResNet-50 / image classification | ImageNet | PipeDream optimizer 选择纯 data parallelism，速度约 1x。 | ResNet-50 参数较少、activation 较大，非 data-parallel partition 反而通信更差。 |
| AlexNet / image classification | synthetic | Cluster-A 最高 4.92x epoch speedup，Cluster-B 2.04x。 | 同样受益于减少跨服务器通信。 |
| GNMT-8/16 / translation | WMT16 EN-De | GNMT-16 在 Cluster-B 最高约 3.14x；Cluster-A 上 16 GPUs 约 2.92x time-to-accuracy。 | RNN/translation workloads 展示 pipeline 适用性。 |
| AWD-LSTM / language modeling | Penn Treebank | 1x4 Cluster-A 上 4.25x speedup。 | 论文称通信降低约 88%。 |
| S2VT / video captioning | MSVD | 4x1 Cluster-C 上 3.01x speedup。 | 配置 `2-1-1`，通信降低约 85%。 |

对比结论:

- 相比 naive model parallelism，PipeDream 的 pipelining alone 对四个模型都有 2x 以上提升；对 VGG/AlexNet，stage replication 进一步带来最高 14.9x/6.5x 的差距。
- 相比 hybrid/FlexFlow-style partitioning，加入 pipelining 可让 throughput 最多增加 80%；对 AlexNet Cluster-B，PipeDream 比较简单 hybrid route 快约 1.9x。
- 相比 GPipe-like frequent flushing，PipeDream 的 1F1B schedule 避免频繁 pipeline flush；在 GNMT-16 上，GPipe-like schedule 比 PipeDream 慢 35% 到 71%，取决于 pipeline depth 和 cluster。
- 相比 asynchronous data parallelism，ASP 在 VGG-16/Cluster-B 上到 48% accuracy 需要 PipeDream 的约 7.4x 时间，体现 staleness 对统计效率的风险。
- 相比大 batch/LARS，PipeDream 在 VGG-16/Cluster-C 上比最快 data-parallel batch size route 还快 2.4x 以上；过大 batch size 还可能达不到目标精度。

论文强调 PipeDream 的 time-to-accuracy speedup 主要来自系统吞吐，而不是减少收敛所需 epoch。实验中 PipeDream 达到目标精度所需 epoch 数与 data parallelism 接近。

### 限制与适用边界

- 适用边界: 适合模型参数通信成为瓶颈、且模型可按层切分为相对均衡 stages 的 DNN 训练。对于 ResNet-50 这种参数较少、activation communication 更重的模型，optimizer 会退化到 data parallelism。
- 统计边界: Weight stashing 修复每个 stage 内 forward/backward 权重版本不一致问题，但不同 stages 之间仍可能有 bounded staleness。VerticalSync 可以收紧该问题，但默认关闭。
- 信任边界: PipeDream 假设 workers 在同一可控训练系统内，未解决 malicious trainer、remote hardware attestation、数据隐私、梯度泄露或可验证训练。
- 工程边界: 实现依赖 PyTorch runtime 和当时通信后端限制；结果基于论文中的硬件、模型与 fp32 设置。
- 不是基础概念: PipeDream 是 pipeline-parallel training system source；`training-systems`、`dnn-training-parallelism`、`pipeline parallelism` 才是可复用知识层对象。

## 吸收到知识库的结论

### 新增/刷新的 Knowledge nodes

| Knowledge node | 更新类型 | 吸收内容 | Source role |
| --- | --- | --- | --- |
| [[training-systems|ML training systems]] | new direction | 新增训练系统方向，覆盖训练吞吐、资源调度、parallelism、communication/memory/statistical-efficiency tradeoff。 | PipeDream 提供第一个 training throughput seed。 |
| [[dnn-training-parallelism|DNN training parallelism]] | new problem/method-family node | 定义 data/model/pipeline/hybrid parallelism 及其问题边界；记录 PipeDream 的 automatic partitioning、1F1B schedule、weight stashing。 | PipeDream 是代表 source。 |
| [[ml-systems|ML systems]] | domain refresh | 把 ML systems 从 trust/privacy + synthetic data 扩到 training systems。 | Source-backed domain child。 |
| [[trustworthy-distributed-ml|Trustworthy distributed ML]] | bridge refresh | 区分 performance parallelism 与 remote trainer trust；PipeDream 作为 TDML 背景里 pipeline/model parallelism 的性能系统来源。 | Bridge evidence, not trust solution。 |

### Cold-Start Hierarchy Discovery

| Candidate | Level | 判断 | 是否建节点 | 理由 |
| --- | --- | --- | --- | --- |
| ML systems | domain | 已存在 | refresh | PipeDream 是 ML systems 的训练系统方向 evidence。 |
| ML training systems | direction | 可复用方向 | yes | 可组织 distributed training, training throughput, scheduling, resource efficiency, checkpointing 等多个问题。 |
| DNN training parallelism | problem/method-family | 可复用问题层 | yes | Data/model/pipeline/hybrid parallelism 是多个 sources 可复用的系统问题，不等同 PipeDream。 |
| Pipeline parallelism | method family | 候选 | no for now | 当前只由 PipeDream 强 evidence 支撑，先作为 DNN training parallelism 的方法路线。 |
| PipeDream | source/system instance | source note | no | 单篇论文/系统名，应保留在 source。 |
| 1F1B / weight stashing | mechanism | source extension | no | 是 PipeDream 的关键机制；未来多 source 复用后可拆。 |

### Bridge 判断

PipeDream 与 [[trustworthy-distributed-ml|Trustworthy distributed ML]] 有明确 cross-link，但不是同一问题。PipeDream 证明在受控集群中可通过 pipeline parallelism、stage replication、1F1B scheduling 和 weight stashing 提升 DNN 训练吞吐；TDML 讨论公共远程算力里的任务协调、trainer validation、malicious trainer detection 和 reward audit。前者的 parallelism 可以作为后者的性能 substrate，后者的 trust mechanisms 不从前者自动获得。

## 关键术语

| Term | 本文含义 | 上层处理 |
| --- | --- | --- |
| PipeDream | 本文提出的 pipeline-parallel DNN training system。 | source/system instance。 |
| Data parallelism | workers 持有完整模型，在不同数据上训练并同步梯度。 | `dnn-training-parallelism` 方法路线。 |
| Model parallelism | 模型层/算子跨 worker 划分。 | `dnn-training-parallelism` 方法路线。 |
| Pipeline parallelism | 模型 stages 形成流水线，不同 minibatches 在不同 stages 并发。 | `dnn-training-parallelism` 方法路线。 |
| 1F1B | 每个 worker 在 steady state 交替执行 one forward and one backward。 | PipeDream mechanism。 |
| Weight stashing | 为 minibatch 保留 forward 使用的权重版本，保证对应 backward 使用同版本。 | PipeDream mechanism。 |
| VerticalSync | 让不同 stages 对同一 minibatch 使用一致的权重版本。 | PipeDream optional mechanism。 |
| NOAM | 填满 pipeline 所需的最小 in-flight minibatches 数。 | PipeDream scheduling detail。 |

## 证据锚点

| Claim | Evidence | Confidence |
| --- | --- | --- |
| PipeDream 目标是多加速器 DNN 训练吞吐，不是共识或区块链。 | Abstract p1; §1 p1-p2 | high |
| Data parallelism 在高 worker 数下受通信瓶颈限制。 | §1 p1-p2; Figure 2 | high |
| PipeDream 自动 partition layers，并考虑 stage replication 与硬件拓扑。 | §4.1 p5-p6 | high |
| 1F1B/1F1B-RR 降低 pipeline stalls。 | §4.2 p6-p7 | high |
| Weight stashing 修复同一 stage 内 forward/backward 权重版本 mismatch。 | §4.3 p7-p8 | high |
| PipeDream 在多模型/多集群上最高达到 5.3x 左右加速。 | §6 p9-p13; Table 1 | high |
| ResNet-50 是反例，optimizer 选择 data parallelism。 | §6.2 p10; Table 1 | high |
| PipeDream 不解决 remote trainer trust/privacy/hardware attestation。 | Scope inference from absence of threat model and comparison with TDML | high |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training | evidences | nahida-knowledge-ml-training-systems | source note | high | active_seed |
| doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training | evidences | nahida-knowledge-dnn-training-parallelism | source note | high | active_seed |
| doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training | bridges_to | nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml | source note + TDML source | high | active_seed |

## 检索优化

- Query keys: PipeDream, DNN training parallelism, pipeline parallelism, model parallelism, data parallelism, 1F1B, weight stashing, inter-batch pipelining, training throughput, distributed DNN training.
- 应先读: [[dnn-training-parallelism|DNN training parallelism]]
- 上层入口: [[training-systems|ML training systems]], [[ml-systems|ML systems]]
- Cross-domain: [[trustworthy-distributed-ml|Trustworthy distributed ML]]

## 更新记录

| Date | Run ID | Change | Reviewer |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Deep-read PipeDream, corrected queue metadata/classification, created source-backed training systems absorption. | codex |
