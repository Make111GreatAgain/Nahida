---
id: "nahida-knowledge-ml-systems"
title: "ML systems"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "domain"
hierarchy_level: "domain"
file_slug: "ml-systems"
domain_id: "ml-systems"
direction_id: ""
parent_knowledge_refs: []
child_knowledge_refs:
  - "nahida-knowledge-privacy-and-trustworthy-ml"
  - "nahida-knowledge-ml-systems-synthetic-data-generation"
  - "nahida-knowledge-ml-training-systems"
  - "nahida-knowledge-ml-systems-research-dynamics"
ontology_path:
  - "ml-systems"
primary_ontology_path: "ml-systems"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-ml-systems"
    relation: "has_child"
    to: "nahida-knowledge-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "has_child"
    to: "nahida-knowledge-ml-systems-research-dynamics"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems.md"
      - "vault/04_Knowledge/ml-systems/research-dynamics.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "has_child"
    to: "nahida-knowledge-ml-systems-synthetic-data-generation"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems.md"
      - "vault/04_Knowledge/ml-systems/synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "has_child"
    to: "nahida-knowledge-ml-training-systems"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems.md"
      - "vault/04_Knowledge/ml-systems/training-systems.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "bridges_to"
    to: "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/blockchain-coordination-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-generation-to-privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems"
    relation: "bridges_to"
    to: "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/dnn-training-parallelism-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
  - "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
  - "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
  - "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
  - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
  - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
representative_source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2311.15310v1"
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:1907.00503v2"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "doi:10.1145/3341301.3359646"
query_keys:
  - "ML systems"
  - "machine learning systems"
  - "trustworthy ML systems"
  - "federated learning integrity"
  - "RiseFL"
  - "secure aggregation input validation"
  - "synthetic data generation"
  - "time-series synthetic data generation"
  - "financial time series generation"
  - "FTS-Diffusion"
  - "tabular synthetic data generation"
  - "synthetic tabular data"
  - "CTGAN"
  - "conditional tabular GAN"
  - "SDGym"
  - "trustworthy distributed ML"
  - "TDML"
  - "blockchain-coordinated distributed training"
  - "remote trainer validation"
  - "synthetic data privacy evaluation"
  - "similarity-based privacy metrics"
  - "synthetic data release privacy"
  - "ReconSyn"
  - "collaborative synthetic data generation"
  - "privacy-preserving collaborative SDG"
  - "MPC synthetic data generation"
  - "ML training systems"
  - "DNN training parallelism"
  - "pipeline parallelism"
  - "PipeDream"
  - "training throughput"
aliases:
  - "machine learning systems"
  - "机器学习系统"
domains:
  - "ml-systems"
topics:
  - "privacy-and-trustworthy-ml"
  - "synthetic-data-generation"
  - "time-series-synthetic-data-generation"
  - "tabular-synthetic-data-generation"
  - "synthetic-data-evaluation"
  - "federated-learning-integrity"
  - "secure-aggregation-input-validation"
  - "trustworthy-distributed-ml"
  - "blockchain-coordinated-training"
  - "synthetic-data-privacy-evaluation"
  - "collaborative-synthetic-data-generation"
  - "privacy-and-trustworthy-ml"
  - "training-systems"
  - "dnn-training-parallelism"
  - "pipeline-parallelism"
tags:
  - "nahida/knowledge"
  - "nahida/domain"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-23"
created: "2026-06-20"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
  - "nahida-knowledge-20260623-fts-diffusion-financial-time-series"
  - "nahida-knowledge-20260623-ctgan-tabular-synthetic-data"
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
  - "nahida-knowledge-20260623-pipedream-dnn-training-parallelism"
source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2311.15310v1"
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:1907.00503v2"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "doi:10.1145/3341301.3359646"
confidence: "medium"
trust_tier: "primary"
---

# ML systems

## 定义与范围

- 定义: ML systems 组织机器学习系统在训练、推理、部署、协作、隐私、可验证性、资源效率和运维治理中的问题层。它关注模型算法如何在真实系统边界内运行，而不只是模型结构本身。
- 不包含: 单个模型、单篇论文、某个 benchmark、某个训练脚本或某个协议名；这些保留在 `03_Sources` source notes。
- Canonical terms: `ML systems`, `machine learning systems`
- Aliases/query keys: machine learning systems, trustworthy ML systems, federated learning integrity
- Standalone completeness check: 本节点给出定义、边界、当前子方向、代表 source、缺口和刷新条件；链接用于深入，不作为唯一解释。
- Retrieval role: 当查询涉及 ML 系统的隐私、验证、协作训练、部署信任边界时，先读本节点，再进入下级方向。
- Update scope: 新 source 若涉及 distributed/federated learning、model serving、ML privacy/security、verification, data governance, deployment reliability，应刷新本节点或其 child。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: ML systems 处在 machine learning、distributed systems、security/privacy 和 infrastructure 的交界。它不只回答模型“能不能达到高准确率”，还回答训练数据怎样分布、计算如何调度、谁能看到什么、结果能否被验证、系统失败时谁承担信任边界。

当前 vault 的 source-backed seed 来自 zkFL、PZKP-FL、RiseFL、FTS-Diffusion、CTGAN、TDML、SBPM attacks paper、EndSDG 和 PipeDream。zkFL 把 federated learning 的 central aggregator 从 trusted component 改写成可验证 component；PZKP-FL 进一步把 trainer local computation 和 publisher/global aggregation 也改写成可验证 protocol relation；RiseFL 则把 secure aggregation 下的 client input validation 做成低成本、概率完整性检查路线。FTS-Diffusion、CTGAN 和 EndSDG 把 ML systems 的范围从 trust/privacy 扩到 synthetic data generation：当真实数据稀缺、表格结构复杂、数据共享受限或多机构不能集中原始数据时，系统问题包括如何生成 fidelity 足够、对下游任务有用且处在输入/输出隐私边界内的数据。SBPM attacks paper 进一步说明 synthetic data release 的 privacy boundary 不能从相似性指标推出，metric/filter access 本身可能成为泄露通道。TDML 又把 ML systems 的 trust boundary 扩到 public remote computing resources：训练任务、模型切分、远程 trainer、validation trace 和 rewards 都成为系统可信性问题。PipeDream 则把 ML systems 扩到 training systems：当多 GPU/多服务器训练受通信、调度、内存和参数版本一致性限制时，训练 runtime 本身成为可建模的系统问题。

## 基础概念判断

- 是否是基础概念/方向/问题: `domain`
- 为什么足够通用: 它可组织 federated learning integrity、privacy-preserving ML、verifiable inference/training、model serving reliability、ML data governance 等多个方向。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkFL 只是第一个 ML systems source seed；协议细节留在 source note。
- 需要引用的更基础 Knowledge: 暂无更高层 domain；与 [[zero-knowledge-proofs|Zero-knowledge proofs]]、[[distributed-systems|Distributed systems]]、[[blockchain-systems|Blockchain systems]] 可通过 bridges 交叉。
- 不应拆出的实例/协议/来源: zkFL、RoFL、RiseFL、PZKP-FL、某个 FedAvg 实现默认作为 source/system instance，除非多来源证明需要独立方法节点。

## 解决的问题

ML systems 解决的是模型算法进入多参与方或生产环境后的系统问题:

- 数据、模型、更新和 inference request 分散在多个主体时，如何定义正确性和信任边界。
- 训练计算分布到多个 accelerators/workers 时，如何平衡 throughput、communication、memory、scheduler correctness 和 statistical efficiency。
- 训练/聚合/推理结果如何被审计或验证。
- 隐私、机密性、完整性和可用性如何与性能成本折中。
- 评估指标如何同时覆盖 accuracy、latency、throughput、communication、energy、privacy leakage 和 security assumptions。

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | direction | 当前 sources 进入的是 ML trust/privacy/integrity 问题，而不是模型架构或 serving throughput。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]]; [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] | active_seed |
| [[synthetic-data-generation|Synthetic data generation]] | direction | FTS-Diffusion、CTGAN、SBPM attacks paper 与 EndSDG 暴露了 ML systems 的数据层方向：生成 synthetic data 以缓解数据稀缺或支持数据共享，并需要同时评估 fidelity、downstream utility、privacy boundary 和多方 input/output privacy。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]]; [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]]; [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]]; [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] | active_seed |
| [[training-systems|ML training systems]] | direction | PipeDream 暴露了训练 runtime 层方向：DNN 训练吞吐不只由算法决定，还受 parallelism、communication、pipeline scheduling、parameter versioning 和 hardware topology 约束。 | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] | active_seed |
| [[research-dynamics|ML systems Research Dynamics]] | domain_dynamics | 领域层需要单独记录研究动态、缺口和 freshness；当前仅为本地 seed，不是外部最新趋势。 | current vault state | active_seed |
| model serving systems | candidate direction | 未来若吸收 serving/inference repo 或论文，可单独建立。 | none | queued |
| ML data governance | candidate direction | 数据来源、授权、quality、privacy route 需要更多 source。 | none | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | 把 ML system 中的数据、更新、模型和结果放进隐私/完整性/可验证性边界中分析。 | 多主体协作训练、外包计算、私有数据或模型不可公开。 | 需要明确 threat model；不同隐私/完整性目标可能冲突。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]]; [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| [[federated-learning-integrity|Federated learning integrity]] | 让多 client 训练中的聚合、更新来源和 global update 可验证。 | Federated learning 依赖 aggregator 或 coordinating service。 | 不自动解决 malicious clients、隐私泄露或模型质量。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |
| Verifiable federated training | 让 trainer 的本地训练过程也可验证，避免只验证 global aggregation。 | FL threat model 包含 lazy trainers 或 local computation cheating。 | 不证明数据质量、poisoning、泛化能力或生产可行性。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| Secure aggregation input validation | 在保护 individual updates 的同时过滤 malformed client updates。 | FL 同时需要 privacy 与 malicious-client input integrity。 | relaxed/probabilistic；不能证明语义质量、收敛或公平性。 | [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] |
| [[synthetic-data-generation|Synthetic data generation]] | 通过生成 synthetic data 缓解真实数据不足、支持仿真/共享，并用 fidelity/utility/privacy 等评价轴约束其可用性。 | 数据采集昂贵、历史有限、表格结构复杂、隐私/共享受限或需要 simulation。 | 生成数据可能不保留下游信号、泄露训练数据、忽略少数类或跨分布失效。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]]; [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | 把 synthetic data generator、metrics、filters、query access 和 release workflow 放入同一 privacy threat model。 | 合成数据用于敏感数据共享、匿名化、合规或外部发布。 | 相似性指标不是隐私证明；攻击审计不能替代 formal guarantee；DP pipeline 需要端到端预算/后处理约束。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | 在多 data custodians 场景中，把 preprocessing、evaluation、threshold voting、hyperparameter tuning 和 final release 作为一个 input/output privacy pipeline 管理。 | 多机构不能集中原始数据，但需要发布有用合成数据。 | MPC cost、DP preprocessing、治理可解释性和中间结果泄露边界仍需补 source。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |
| [[trustworthy-distributed-ml|Trustworthy distributed ML]] | 分析公开远程算力参与训练时，任务发布、资源选择、训练 trace、cross-validation、malicious trainer detection 和 reward audit 如何组织。 | 训练跨组织/公开节点运行，且 workload integrity 与 accountability 是系统目标。 | Blockchain trace 不等于训练正确性证明；缺 hardware attestation、privacy proof 和真实大模型部署证据。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] |
| [[training-systems|ML training systems]] / [[dnn-training-parallelism|DNN training parallelism]] | 分析模型训练如何跨 accelerators/workers 并行执行，并控制 communication、pipeline stalls、memory footprint、parameter versioning 和 time-to-accuracy。 | 训练耗时受计算资源和通信拓扑限制，尤其是多 GPU/多服务器 DNN training。 | 性能并行不自动解决 remote trainer trust、privacy、hardware attestation 或 proof-of-training。 | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 创建 ML systems 主干 seed；把 federated learning aggregator integrity 作为可验证系统问题 | 单一 source；只覆盖 malicious aggregator，不覆盖全部 trustworthy ML | `p1-p14` |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 补充 verifiable federated training、secure-sum aggregation verification 和 local-data privacy route | 小模型实验；大量 proofs；不覆盖 poisoning/data quality | `p1-p15` |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | paper | 补充 RiseFL secure aggregation input-validation route；把 malicious-client malformed updates 纳入本方向 | relaxed SAVI；predicate-passing poisoning 未解决 | `p1-p15` |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | paper | 新增 synthetic data generation direction seed；把 financial time-series data scarcity、fidelity and downstream utility 纳入 ML systems。 | anonymous under-review; appendices unavailable; no privacy/production evaluation | `p1-p12` |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | paper | 补充 tabular synthetic data generation topic；把 mixed-type tabular data、conditional generation、training-by-sampling 和 ML efficacy benchmark 纳入 ML systems。 | no privacy guarantee; TVAE competitive; no repo analysis in this run | `p1-p15` |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | paper | 新增 trustworthy distributed ML problem seed；把 public remote trainer coordination、training trace audit、malicious trainer detection 和 reward accountability 纳入 ML systems。 | ResNet50/CIFAR-10 原型；proof-of-training 是 trace audit 不是 ZK proof；无 hardware attestation/large-model deployment evidence | `p1-p11` |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | paper | 新增 synthetic data privacy evaluation seed；把 synthetic data release 的 metric leakage、membership/attribute inference、outlier reconstruction 和 DP pipeline boundary 纳入 ML systems。 | tabular-focused; attack model assumes generator/metric access; not a DP synthetic data construction | `p1-p19` |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 新增 collaborative synthetic data generation seed；把多 data custodians 的 MPC input privacy、DP output privacy、private evaluation/tuning 和 final release budget 纳入 ML systems。 | arXiv preprint; DP quantile binning not complete; code not analyzed; genomic use case preliminary | `p1-p15` |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | paper | 新增 training systems direction 和 DNN training parallelism problem seed；把 pipeline scheduling、stage partitioning、weight stashing 和 training throughput 纳入 ML systems。 | 受控集群性能系统；不解决远程训练可信性、隐私或 hardware attestation；对 ResNet-50 退化到 data parallelism。 | `p1-p13` |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，只代表当前 vault 已深读 source。
- Freshness: `fresh` for this local absorption; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: 当前 ML systems 节点是 cold-start seed，但已从单一 trustworthy/federated learning 分支扩展到 synthetic data generation、synthetic data privacy evaluation、collaborative synthetic data generation、trustworthy distributed training 和 training systems。zkFL 说明 federated learning 的系统信任边界不仅在 client privacy，也在 aggregator 是否正确执行 aggregation；PZKP-FL 说明 trainer 是否真实执行本地训练、publisher 是否正确聚合也可成为可验证对象；RiseFL 说明 secure aggregation 与 malicious-client input validation 可以组合，但需要接受 relaxed/probabilistic predicate 边界。FTS-Diffusion 和 CTGAN 说明 ML systems 还包括数据层问题：当真实数据稀缺或表格结构复杂时，合成数据生成需要根据数据模态保留关键结构，并用 fidelity + downstream utility 共同评估。SBPM attacks paper 说明数据层系统问题还包括发布隐私: similarity-based metrics、filters 和 metric APIs 不能直接证明匿名，甚至可能泄露 membership、attributes 和 train outliers。EndSDG 则说明多机构合成数据发布还要把 input privacy、output privacy、private preprocessing/evaluation/tuning 和 release budget 放进同一系统边界。TDML 说明训练系统本身的资源和参与者边界也会成为 trust problem：当算力来自公开远程 trainers 时，系统要处理任务协调、模型切分、训练 trace、validation、malicious trainer isolation 和 reward audit。PipeDream 说明即使在受控集群中，训练 runtime 也有独立系统问题：data/model/pipeline parallelism、stage partitioning、communication overlap、parameter versioning 和 time-to-accuracy。这个节点后续需要 secure aggregation、privacy-preserving FL、robust aggregation、synthetic data foundations、DP synthetic data、collaborative SDG primary sources、remote training trust、training runtime/large-model infrastructure、model serving and governance sources 才能成为更完整的领域知识。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 ML systems domain、privacy/trustworthy ML direction 和 federated learning integrity problem node | 定义; 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 FL security/privacy sources 后校准 |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 补充 verifiable federated training 和 secure-sum aggregation verification route | 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL/secure aggregation/robust FL sources 后校准 |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | 补充 secure aggregation input-validation route；不改变 ML systems 上层结构 | 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL/secure aggregation foundation sources |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | 新增 synthetic data generation direction 和 time-series synthetic data generation topic；纠正队列误分到 blockchain/data availability。 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合 | yes | 后续吸收 synthetic data foundation/evaluation sources |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | 补充 tabular synthetic data generation topic 和 synthetic data evaluation 候选轴；纠正队列误分到 privacy/distributed learning。 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合 | yes | 后续吸收 tabular/DP/evaluation sources 后校准 |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | 新增 trustworthy distributed ML problem seed；纠正队列误分到 zkML/verifiable-inference；通过 bridge 连接 blockchain coordination 与 ML training trust。 | 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 BFL/DML/attestation/decentralized compute sources |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | 新增 synthetic data privacy evaluation seed；纠正队列误分到 ZK proof foundations；通过 bridge 连接 synthetic data generation 与 privacy/trustworthy ML。 | 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 DP synthetic data/privacy audit sources |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 新增 collaborative synthetic data generation seed；纠正队列中过宽 distributed-learning 归属；通过 bridge 补充 synthetic data release 的 input/output privacy route。 | 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 CaPS/FLAIM/DP preprocessing/collaborative SDG sources |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | 新增 training systems direction 和 DNN training parallelism problem seed；纠正队列中 consensus 误分；通过 bridge 区分性能并行与可信远程训练。 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 GPipe/PiPPy/Megatron/DeepSpeed/ZeRO/FSDP sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-aggregation; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, verification_transfer | ZKP aggregation proof transfers correctness verification; FL privacy, client poisoning, selection fairness and convergence remain ML systems concerns. | active_seed |
| [[zkml-verifiable-training-to-federated-learning-integrity|zkML verifiable training -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-training; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, privacy, cross_domain_mapping | ZK training proof transfers local-computation integrity; client poisoning, data quality and convergence remain ML systems concerns. | active_seed |
| [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]] | `blockchain-systems; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | application, coordination, auditability, incentive | Blockchain coordination transfers task/resource discovery and audit trace; training correctness, privacy, hardware truth and model quality remain ML systems/security concerns. | active_seed |
| [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation; ml-systems/privacy-and-trustworthy-ml` | tension, privacy_boundary, evaluation_transfer, construction_route | Synthetic data can support sharing, but privacy does not transfer from similarity/fidelity metrics; DP or threat-model-specific attack evaluation is required. Collaborative release further separates input privacy from final output privacy. | active_seed |
| [[dnn-training-parallelism-to-trustworthy-distributed-ml|DNN training parallelism -> trustworthy distributed ML]] | `ml-systems/training-systems/dnn-training-parallelism; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | substrate, contrast, trust_boundary, implementation_reuse | Parallel training transfers performance substrate and terminology; it does not transfer remote trainer trust, privacy, hardware attestation, malicious-node detection or reward accountability. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-ml-systems | has_child | nahida-knowledge-privacy-and-trustworthy-ml | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md | medium | active_seed |
| nahida-knowledge-ml-systems | has_child | nahida-knowledge-ml-systems-synthetic-data-generation | vault/04_Knowledge/ml-systems/synthetic-data-generation.md | high | active_seed |
| nahida-knowledge-ml-systems | has_child | nahida-knowledge-ml-systems-research-dynamics | vault/04_Knowledge/ml-systems/research-dynamics.md | medium | active_seed |
| nahida-knowledge-ml-systems | has_child | nahida-knowledge-ml-training-systems | vault/04_Knowledge/ml-systems/training-systems.md | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | medium | active_seed |
| nahida-knowledge-ml-systems | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md | source note | medium | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md | source note | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md | source note | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md | source note | high | active_seed |
| nahida-knowledge-ml-systems | bridges_to | nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml | bridge note | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md | source note | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md | source note | high | active_seed |
| nahida-knowledge-ml-systems | bridges_to | nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml | bridge note | high | active_seed |
| nahida-knowledge-ml-systems | evidenced_by | vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md | source note | high | active_seed |
| nahida-knowledge-ml-systems | bridges_to | nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Trustworthy ML foundation sources 缺失 | 当前只有 zkFL seed，不能代表完整 ML systems taxonomy | nahida-research-search / nahida-update | high | queued |
| Federated training/input-integrity source coverage thin | PZKP-FL 与 RiseFL 形成两个 seed，但仍需 RoFL/ACORN/EIFFeL/robust FL/secure aggregation sources | nahida-update | high | active_seed_gap |
| Federated learning privacy/robustness sources 缺失 | 需要把 malicious aggregator、malicious clients、secure aggregation、DP、MPC/TEE routes 分开 | nahida-update | high | queued |
| Synthetic data generation foundation sources 缺失 | FTS-Diffusion 创建了方向 seed，但不能代表 synthetic data generation 全景 | nahida-update / nahida-research-search | high | active_seed_gap |
| Synthetic data privacy/evaluation sources 缺失 | 已有 SBPM attacks seed 覆盖相似性指标风险，但 DP synthetic data、attack taxonomy、fairness/robustness 和生产评估仍不足。 | nahida-update / nahida-research-search | high | active_seed_gap |
| Collaborative synthetic data sources 缺失 | EndSDG 创建多方合成数据发布 seed，但 CaPS/FLAIM、DP preprocessing 和 production governance 仍缺 primary evidence。 | nahida-update / nahida-research-search | high | active_seed_gap |
| Tabular synthetic data sources still thin | CTGAN 创建 tabular seed，但还缺 DP synthetic tabular data、tabular diffusion、relational/multi-table synthesis 和 modern benchmarks。 | nahida-update / nahida-research-search | high | active_seed_gap |
| Trustworthy distributed training sources 缺失 | TDML 创建了公开远程训练可信性 seed，但仍缺 attestation、chain overhead、robust DML 和真实大模型部署证据 | nahida-update / nahida-research-search | high | active_seed_gap |
| Training systems sources 缺失 | PipeDream 创建训练系统 seed，但还缺 GPipe/PiPPy/Megatron/DeepSpeed/ZeRO/FSDP 等现代训练系统证据 | nahida-update / nahida-github-repo-analyze | high | active_seed_gap |
| 工业/repo evidence 缺失 | ML systems 需要工程实现、benchmark 和 deployment constraints | nahida-github-repo-analyze / nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Created ML systems domain seed from zkFL cold-start classification correction. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL as verifiable federated training and secure-sum aggregation route. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risefl-low-cost-zkp | Added RiseFL as secure aggregation input-validation route without splitting a new top-level node. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-fts-diffusion-financial-time-series | Added synthetic data generation direction and time-series synthetic data generation topic from FTS-Diffusion. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Added trustworthy distributed ML problem seed and blockchain coordination bridge from TDML. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-ctgan-tabular-synthetic-data | Added tabular synthetic data generation topic and refreshed ML systems data-layer synthesis from CTGAN. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Added synthetic data privacy evaluation seed and bridge from SBPM attacks paper. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Added collaborative synthetic data generation problem seed and refreshed ML systems data-layer privacy synthesis from EndSDG. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Added training systems direction and DNN training parallelism problem seed from PipeDream. | 1 source note | codex |
