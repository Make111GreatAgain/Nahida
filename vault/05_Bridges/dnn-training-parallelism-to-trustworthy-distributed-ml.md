---
id: "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
title: "DNN training parallelism -> trustworthy distributed ML"
type: "bridge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
bridge_kind: "cross_direction_bridge"
endpoint_a: "nahida-knowledge-dnn-training-parallelism"
endpoint_b: "nahida-knowledge-trustworthy-distributed-ml"
endpoint_paths:
  - "ml-systems/training-systems/dnn-training-parallelism"
  - "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
relation_types:
  - "substrate"
  - "contrast"
  - "trust_boundary"
  - "implementation_reuse"
domain_id: "ml-systems"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
representative_source_refs:
  - "doi:10.1145/3341301.3359646"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
query_keys:
  - "DNN training parallelism trustworthy distributed ML"
  - "PipeDream TDML"
  - "pipeline parallelism remote trainers"
  - "distributed training trust boundary"
  - "parallel training substrate trust"
aliases:
  - "parallel training to trustworthy distributed ML"
domains:
  - "ml-systems"
topics:
  - "dnn-training-parallelism"
  - "trustworthy-distributed-ml"
  - "training-systems"
  - "trust-boundary"
tags:
  - "nahida/bridge"
  - "nahida/ml-systems"
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
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
confidence: "medium"
trust_tier: "primary"
---

# DNN training parallelism -> trustworthy distributed ML

## 桥接命题

PipeDream 和 TDML 都处在 ML training systems 的分布式训练问题域，但它们解决的核心问题不同:

- [[dnn-training-parallelism|DNN training parallelism]] 关注训练吞吐、通信瓶颈、资源利用率、pipeline scheduling 和参数版本一致性。
- [[trustworthy-distributed-ml|Trustworthy distributed ML]] 关注公开远程训练资源中的任务协调、训练 trace、malicious trainer detection、reward accountability 和 trust boundary。

因此，DNN training parallelism 可以为 trustworthy distributed ML 提供性能 substrate 和术语基础；但并行训练机制不会自动转移为 remote trainer honesty、privacy、hardware attestation、formal proof-of-training 或 reward fairness。

## Endpoint A: DNN training parallelism

| 属性 | 内容 |
| --- | --- |
| Knowledge node | [[dnn-training-parallelism|DNN training parallelism]] |
| Primary source | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] |
| 解决的问题 | 高 worker 数下的 DNN 训练通信瓶颈、pipeline stalls、stage partitioning、parameter versioning、time-to-accuracy。 |
| 代表机制 | data/model/pipeline parallelism, automatic layer partitioning, stage replication, 1F1B, weight stashing。 |
| 假设边界 | workers 处在受控或可信训练环境；不处理恶意远程节点、隐私泄露、硬件真实性或奖励结算。 |

## Endpoint B: Trustworthy distributed ML

| 属性 | 内容 |
| --- | --- |
| Knowledge node | [[trustworthy-distributed-ml|Trustworthy distributed ML]] |
| Primary source | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] |
| 解决的问题 | public remote trainers 的选择、任务协调、training trace、cross-validation、malicious trainer isolation、reward audit。 |
| 代表机制 | public/private blockchain coordination, IPFS references, encrypted RPC, validation trace, gradient clustering, top-K local model aggregation。 |
| 假设边界 | 更关注 trust orchestration；不直接优化 pipeline scheduling 的吞吐上限，也不等同 cryptographic proof-of-training。 |

## 关系类型

| Relation type | 说明 | Transfer | Non-transfer |
| --- | --- | --- | --- |
| substrate | TDML 这类远程训练系统仍需要 data/model/pipeline parallelism 承载实际训练 workload。 | parallelism vocabulary, model/stage partitioning, communication/memory tradeoff | trainer honesty, privacy, attestation |
| contrast | PipeDream 是 performance-first，TDML 是 trust/accountability-first。 | 可以比较系统目标和瓶颈。 | 不应把 PipeDream 当成可信训练协议。 |
| trust_boundary | PipeDream 的边界是受控 workers；TDML 的边界是 public remote resources。 | 有助于问“什么时候 parallelism 不够，需要 trust layer”。 | 不自动生成 threat model 或 formal proof。 |
| implementation_reuse | Pipeline/model parallel primitives 可作为可信分布式训练框架中的 execution substrate。 | stage partitioning, scheduling, checkpointing ideas | blockchain trace, reward, malicious detection |

## 转移矩阵

| PipeDream 概念 | 可转移到 TDML 吗 | 转移后含义 | 注意边界 |
| --- | --- | --- | --- |
| Data parallelism | yes | parameter servers / workers 可并行训练不同 data shards。 | 仍需验证 local models 和 participant behavior。 |
| Model parallelism | yes | remote trainers 可接收不同 model shards/layers。 | model shard transfer 引入 privacy/IP protection 问题。 |
| Pipeline parallelism | yes | remote trainers 可组成 training pipeline，提高 utilization。 | pipeline correctness 不等于 trainer honesty。 |
| 1F1B scheduling | partial | 可作为 runtime schedule candidate。 | public network latency、failures 和 adversarial behavior 会破坏 schedule 假设。 |
| Weight stashing | partial | 可用于保持 stage-level gradient correctness。 | 不防止恶意 trainer 伪造 tensor/gradient。 |
| Automatic layer partitioning | yes | 可按 remote hardware spec 做分片决策。 | 需要可信硬件规格或 attestation；TDML 只注册 hardware specs。 |
| Checkpointing | yes | 可支持 failure recovery 和 audit trace。 | checkpoint 可追溯不等于 checkpoint 内容可信。 |

## 证据集

| Evidence | 支持的桥接点 | Caveat |
| --- | --- | --- |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] | 证明 DNN training parallelism 的系统问题包括 communication bottleneck、pipeline stalls、partitioning 和 parameter versioning。 | 假设受控 workers；没有 trust/privacy threat model。 |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] | 证明公开远程训练需要 task/resource coordination、validation trace、malicious trainer detection 和 reward audit，并在背景中引用 data/model/pipeline parallelism。 | TDML 的 proof-of-training 是 trace audit，不是 ZK/VC proof。 |

## 不转移边界

- Performance 不转移为 trust: PipeDream 的高吞吐不能证明 remote trainer 诚实执行。
- Schedule correctness 不转移为 computation correctness: weight stashing 保证 stage-level forward/backward 参数版本一致，不证明 worker 没有篡改 tensor。
- Communication optimization 不转移为 privacy: activation/gradient 更少或更局部地传输，不等于数据或模型隐私。
- Hardware fit 不转移为 hardware truth: PipeDream optimizer 假设硬件拓扑已知；TDML 公共节点场景需要 hardware attestation 或其他验证。
- Audit trace 不转移为 statistical efficiency: TDML 的链上 trace 不能替代 PipeDream 式 throughput/time-to-accuracy 评估。

## 检索用法

- 用户问“PipeDream 和 TDML 有什么关系”: 先读本 bridge，再读两个 endpoint source。
- 用户问“能不能用 pipeline parallelism 做可信远程训练”: 本 bridge 的回答是可以作为 execution substrate，但必须额外解决 trainer trust、privacy、attestation、validation 和 incentives。
- 用户问“TDML 的 pipeline/model parallelism 是不是和 PipeDream 一样”: 本 bridge 的回答是术语和目标部分相通，但 TDML 关注 public remote-resource trust orchestration，PipeDream 关注受控集群吞吐优化。

## 刷新触发器

| Trigger | Why | Suggested action |
| --- | --- | --- |
| 新 pipeline/tensor/model parallelism source 吸收 | 可能改变 Endpoint A 的方法族边界。 | nahida-update |
| 新 decentralized/remote training trust source 吸收 | 可能强化 Endpoint B 或建立 attestation/proof-of-training 子节点。 | nahida-update |
| 新训练框架 repo 分析 | 可验证 PipeDream ideas 在现代 PyTorch/DeepSpeed/Megatron/PiPPy 中的实现状态。 | nahida-github-repo-analyze |
| 用户询问最新训练系统趋势 | 需要外部 freshness，不应只用当前 vault。 | nahida-daily-fetch / nahida-research-search |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Created bridge between DNN training parallelism and trustworthy distributed ML after PipeDream absorption. | PipeDream; TDML | codex |
