---
id: "nahida-knowledge-ml-training-systems"
title: "ML training systems"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "training-systems"
domain_id: "ml-systems"
direction_id: "training-systems"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems"
child_knowledge_refs:
  - "nahida-knowledge-dnn-training-parallelism"
ontology_path:
  - "ml-systems"
  - "training-systems"
primary_ontology_path: "ml-systems/training-systems"
secondary_ontology_paths:
  - "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
relation_edges:
  - from: "nahida-knowledge-ml-training-systems"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/training-systems.md"
      - "vault/04_Knowledge/ml-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-training-systems"
    relation: "has_child"
    to: "nahida-knowledge-dnn-training-parallelism"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/training-systems/dnn-training-parallelism.md"
      - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-training-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-training-systems"
    relation: "bridges_to"
    to: "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/dnn-training-parallelism-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
representative_source_refs:
  - "doi:10.1145/3341301.3359646"
query_keys:
  - "ML training systems"
  - "machine learning training systems"
  - "distributed training systems"
  - "DNN training parallelism"
  - "training throughput"
  - "pipeline parallelism"
  - "data parallelism"
  - "model parallelism"
  - "PipeDream"
aliases:
  - "machine learning training systems"
  - "训练系统"
  - "ML training infrastructure"
domains:
  - "ml-systems"
topics:
  - "training-systems"
  - "distributed-training-systems"
  - "dnn-training-parallelism"
  - "training-throughput"
  - "gpu-training"
  - "pipeline-parallelism"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-pipedream-dnn-training-parallelism"
source_refs:
  - "doi:10.1145/3341301.3359646"
confidence: "medium"
trust_tier: "primary"
---

# ML training systems

## 定义与范围

- 定义: ML training systems 研究机器学习模型训练如何在真实计算资源、通信拓扑、内存约束、调度策略、并行执行、checkpoint/recovery 和统计效率边界内完成。
- 不包含: 某个训练框架、某篇论文、某个 scheduler 名称、某个 benchmark 或某次模型训练实验；这些保留在 source notes。
- Canonical terms: `ML training systems`, `distributed training systems`
- Aliases/query keys: training systems, DNN training parallelism, pipeline parallelism, data parallelism, model parallelism
- Standalone completeness check: 本节点给出训练系统方向的定义、上层位置、核心问题、方法路线、代表 source 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 DNN 训练吞吐、GPU/accelerator 并行、训练通信瓶颈、模型/数据/流水线并行时，先读本节点，再进入 [[dnn-training-parallelism|DNN training parallelism]]。
- Update scope: 新 source 若涉及 distributed training, pipeline/model/data parallelism, optimizer/scheduler/runtime, checkpointing, memory optimization, large-model training infrastructure, training throughput，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: ML training systems 处在 machine learning、distributed systems、accelerator runtime 和 storage/network infrastructure 的交界。模型算法本身只定义了 forward、loss、backward 和 update；训练系统要回答这些计算如何被切分、调度、通信、容错、复现和评估。对于大模型或高吞吐训练，训练时间不只由 FLOPs 决定，还由参数/激活通信、GPU memory、network topology、batch size、pipeline stalls、checkpointing 和统计效率共同决定。

当前 vault 中 PipeDream 是本方向的第一个 source-backed seed。它表明 ML systems 不只有隐私、可验证性和 synthetic data，也包括训练 runtime 的资源效率问题: 当 data parallelism 在高 worker 数下被 communication stalls 限制时，可以通过 layer partitioning、stage replication、inter-batch pipeline schedule 和 parameter versioning 把训练吞吐提升到更高区间。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction`
- 为什么足够通用: 它可组织 DNN training parallelism、large-model training memory optimization、training scheduler/runtime、checkpoint/recovery、communication compression、distributed optimizer 和 training observability 等多个问题。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: PipeDream 只是第一个 source seed；本节点持久对象是训练系统方向，不是 PipeDream 系统名。
- 需要引用的更基础 Knowledge: [[ml-systems|ML systems]], [[distributed-systems|Distributed systems]].
- 不应拆出的实例/协议/来源: PipeDream、GPipe、Megatron-LM、ZeRO、FSDP、PiPPy、某个 PyTorch runtime 默认作为 source/system instance，除非多来源证明需要独立方法节点。

## 解决的问题

| 子问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Training throughput | 如何提高单位时间处理的 minibatches/tokens/samples，并缩短 time-to-accuracy。 | PipeDream |
| Communication bottleneck | 多 worker 训练中参数、梯度、activation 和 intermediate tensors 如何通信，通信是否会压倒计算。 | PipeDream |
| Parallelism strategy | 何时使用 data parallelism、model parallelism、pipeline parallelism 或混合策略。 | PipeDream |
| Work partitioning | 如何把模型层、算子或参数划分给不同 workers，兼顾负载均衡和拓扑通信。 | PipeDream |
| Scheduling correctness | forward/backward 双向计算在 pipeline 中并发时，如何避免参数版本 mismatch 或过多 pipeline flush。 | PipeDream |
| Statistical efficiency | 系统加速是否以更多 epochs、stale gradients 或更差收敛为代价。 | PipeDream |
| Memory footprint | pipeline depth、activation stash、parameter versions 和 checkpointing 如何影响 GPU memory。 | PipeDream |
| Trust and accountability | 如果训练跨公共远程资源运行，如何验证参与方和训练 trace。 | TDML bridge; not solved by PipeDream |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[ml-systems|ML systems]] | child_of | PipeDream source classification and ML systems domain update | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[dnn-training-parallelism|DNN training parallelism]] | problem/method-family | 当前 source 明确围绕 data/model/pipeline/hybrid parallelism 展开，且这个问题层可复用到未来 large-model training sources。 | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] | active_seed |
| large-model memory optimization | problem candidate | ZeRO/FSDP/recomputation/offloading 可能需要单独节点，但当前 PipeDream 只做背景引用。 | PipeDream related work only | queued |
| training scheduler/runtime | problem candidate | 训练 runtime scheduling 可能跨 PipeDream、PiPPy、Megatron、DeepSpeed 等 sources。 | PipeDream implementation seed | watch |
| training checkpoint/recovery | problem candidate | PipeDream 有 per-stage checkpoint seed，但证据不足以单独建节点。 | PipeDream §5 | watch |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Data parallelism | workers 复制完整模型，在不同数据分片上训练，并同步梯度/参数。 | 模型可放入单 worker，网络通信足够支撑同步。 | worker 数高时 all-reduce/parameter communication 可能成为瓶颈；large batch 可能影响统计效率。 | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] as comparison |
| Model parallelism | 把模型层或算子切到多个 workers。 | 模型无法单 worker 容纳，或某些层/算子计算可分割。 | 传统 naive route 容易 worker 空闲，且需要 partitioning。 | PipeDream background |
| Pipeline parallelism | 把连续层切成 stages，不同 minibatches 在 stages 间并发流动。 | 模型可按阶段划分，activation communication 可控，pipeline stalls 可被调度控制。 | 需要处理 forward/backward 双向依赖、参数版本、pipeline flush 和 memory stash。 | PipeDream |
| Hybrid stage replication | 结合 model/pipeline partition 和 stage-level data parallelism。 | 某些 stages 计算重或通信轻，复制能提高吞吐。 | 需要同步 replicated stage 的梯度；优化空间更复杂。 | PipeDream |
| Trustworthy remote training orchestration | 当训练资源来自公共远程节点时，用审计、验证、激励或 attestation 管理参与方行为。 | remote trainers 不完全可信，训练 accountability 是目标。 | 不等于训练吞吐优化；可能引入链上/验证开销。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] via bridge |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | paper | 创建 ML training systems direction seed；把 DNN training parallelism、communication bottleneck、pipeline scheduling correctness、weight stashing 和 automatic partitioning 纳入 ML systems。 | 不解决 remote trainer trust/privacy/attestation；对 ResNet-50 会退化到 data parallelism；实验基于特定模型和硬件。 | `p1-p13`; §4-§6 |

## 当前综合

- Evidence window: `2026-06-23` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for current-vault source absorption; not an external latest claim.
- Valid until: `2026-07-23`.
- 综合: ML training systems 当前是 active_seed 方向节点。PipeDream 表明，训练系统问题不仅是“把模型训练跑起来”，而是要在计算、通信、内存和收敛之间做系统级 tradeoff。Data parallelism 的简单性会在高 worker 数和慢网络下被通信瓶颈限制；model parallelism 能缓解单卡内存但可能低利用率；pipeline parallelism 用 inter-batch overlap 提高利用率，但必须处理 DNN forward/backward 的参数版本一致性和 pipeline stalls。PipeDream 的自动 layer partitioning、stage replication、1F1B scheduling 和 weight stashing 是一个代表性系统实例。后续需要吸收 ZeRO/FSDP/Megatron-LM/PiPPy/DeepSpeed/communication compression/checkpointing 等 sources，才能把本方向从 PipeDream seed 扩展为完整训练系统知识。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | 新增 ML training systems direction 和 DNN training parallelism problem/method node；纠正队列中 consensus 误分；通过 bridge 连接 trustworthy distributed ML。 | 定义; 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 GPipe/PiPPy/Megatron/ZeRO/FSDP/DeepSpeed sources 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[dnn-training-parallelism-to-trustworthy-distributed-ml|DNN training parallelism -> trustworthy distributed ML]] | `ml-systems/training-systems/dnn-training-parallelism; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | substrate, contrast, trust_boundary | Pipeline/data/model parallelism transfers performance substrate and terminology; it does not transfer remote trainer trust, privacy, hardware attestation, malicious-node detection or reward accountability. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-ml-training-systems | is_a | nahida-knowledge-ml-systems | vault/04_Knowledge/ml-systems.md | high | active_seed |
| nahida-knowledge-ml-training-systems | has_child | nahida-knowledge-dnn-training-parallelism | vault/04_Knowledge/ml-systems/training-systems/dnn-training-parallelism.md | high | active_seed |
| nahida-knowledge-ml-training-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md | source note | high | active_seed |
| nahida-knowledge-ml-training-systems | bridges_to | nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Training systems foundation sources thin | 当前只有 PipeDream seed，不能代表完整训练系统 taxonomy。 | nahida-update / nahida-research-search | high | active_seed_gap |
| Large-model training memory optimization | ZeRO/FSDP/offloading/recomputation 是训练系统重要方向，当前只有背景引用。 | nahida-update | high | queued |
| Modern pipeline parallelism sources | PipeDream 是 2019 source，需要 GPipe/PiPPy/Megatron/DeepSpeed 等 sources 校准。 | nahida-update / nahida-github-repo-analyze | high | queued |
| Training trust boundary | PipeDream 不解决 remote trainer trust；需要和 TDML/attestation/proof-of-training sources 分开维护。 | nahida-update | medium | active_seed_gap |
| Production/repo evidence | 当前没有 PipeDream repo 或现代 framework implementation audit。 | nahida-github-repo-analyze | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Created training systems direction and DNN training parallelism child from PipeDream. | 1 source note | codex |
