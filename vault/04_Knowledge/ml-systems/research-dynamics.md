---
id: "nahida-knowledge-ml-systems-research-dynamics"
title: "ML systems Research Dynamics"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "review"
node_kind: "domain_dynamics"
hierarchy_level: "domain_dynamics"
file_slug: "research-dynamics"
domain_id: "ml-systems"
direction_id: ""
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
primary_ontology_path: "ml-systems/research-dynamics"
secondary_ontology_paths: []
relation_edges:
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "part_of"
    to: "nahida-knowledge-ml-systems"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/research-dynamics.md"
      - "vault/04_Knowledge/ml-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-ml-systems-research-dynamics"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
  - "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
  - "nahida-bridge-dnn-training-parallelism-to-trustworthy-distributed-ml"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
  - "vault/03_Sources/papers/sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns.md"
  - "vault/03_Sources/papers/arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan.md"
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
  - "vault/03_Sources/papers/doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training.md"
representative_source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:1907.00503v2"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "doi:10.1109/TIFS.2026.3667458"
  - "doi:10.1145/3341301.3359646"
query_keys:
  - "ML systems latest progress"
  - "ML systems research trends"
  - "trustworthy ML open problems"
  - "secure aggregation input validation"
  - "RiseFL"
  - "synthetic data generation"
  - "time-series synthetic data generation"
  - "FTS-Diffusion"
  - "tabular synthetic data generation"
  - "CTGAN"
  - "SDGym"
  - "synthetic data evaluation"
  - "trustworthy distributed ML"
  - "TDML"
  - "remote trainer validation"
  - "synthetic data privacy evaluation"
  - "similarity-based privacy metrics"
  - "ReconSyn"
  - "synthetic data release privacy"
  - "collaborative synthetic data generation"
  - "privacy-preserving collaborative SDG"
  - "MPC synthetic data generation"
  - "LLM inference privacy"
  - "prompt privacy"
  - "privacy-preserving prompt engineering"
  - "local differential privacy for LLM inference"
  - "Rap-LI"
  - "ML training systems"
  - "DNN training parallelism"
  - "pipeline parallelism"
  - "PipeDream"
  - "training throughput"
aliases:
  - "ML systems trends"
domains:
  - "ml-systems"
topics:
  - "research dynamics"
  - "trustworthy ML"
  - "synthetic data generation"
  - "time-series synthetic data generation"
  - "tabular synthetic data generation"
  - "synthetic data evaluation"
  - "federated learning integrity"
  - "secure aggregation input validation"
  - "trustworthy distributed ML"
  - "blockchain-coordinated distributed training"
  - "synthetic data privacy evaluation"
  - "synthetic data release privacy"
  - "privacy and trustworthy ML"
  - "collaborative synthetic data generation"
  - "input/output privacy"
  - "llm inference privacy"
  - "prompt privacy"
  - "local differential privacy"
  - "training systems"
  - "DNN training parallelism"
  - "pipeline parallelism"
tags:
  - "nahida/knowledge"
  - "nahida/domain-dynamics"
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
  - "nahida-knowledge-20260621-pzkp-fl"
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
  - "nahida-knowledge-20260623-fts-diffusion-financial-time-series"
  - "nahida-knowledge-20260623-ctgan-tabular-synthetic-data"
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
  - "nahida-knowledge-20260623-risk-aware-llm-inference-privacy"
  - "nahida-knowledge-20260623-pipedream-dnn-training-parallelism"
source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
  - "arxiv:1907.00503v2"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "doi:10.1109/TIFS.2026.3667458"
  - "doi:10.1145/3341301.3359646"
confidence: "low"
trust_tier: "primary"
---

# ML systems Research Dynamics

## 领域范围与新鲜度

- Parent domain: [[ml-systems|ML systems]]
- Evidence window: `2026-06-20` to `2026-06-23`，只代表当前 vault 已吸收资料。
- Last synthesized: `2026-06-23`
- Valid until: `2026-07-23`
- Freshness status: `fresh` for current-vault synthesis；不是外部最新趋势判断，因为本次没有运行 daily-fetch、web research 或最新资料核验。
- Retrieval role: 回答 ML systems 的已记录研究倾向、已有证据范围和待补来源，避免 query 直接扫全部 source notes。
- Update scope: 新论文、仓库、web research、daily freshness signals、bridge notes、问题节点重大变化。

## 研究动态摘要

| 动态 | 类型 | 影响的方向/问题 | 证据 | Confidence |
| --- | --- | --- | --- | --- |
| 新增 ML systems cold-start 主干。 | intake_state | ML systems / trustworthy ML | zkFL source absorption | medium |
| 当前证据集中在 federated learning aggregator integrity。 | source_window | federated-learning-integrity | zkFL | high |
| 新增 PZKP-FL 后，当前证据窗口扩展到 trainer local-computation integrity 和 publisher/global aggregation verification。 | source_window | federated-learning-integrity / verifiable federated training | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] | high |
| 新增 RiseFL 后，当前证据窗口覆盖 secure aggregation input validation: 在隐藏 individual updates 的同时过滤 malformed client updates。 | source_window | federated-learning-integrity / secure aggregation input validation | [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] | high |
| 新增 FTS-Diffusion 后，ML systems 从 trust/privacy seed 扩展到 synthetic data generation：用生成数据缓解真实数据稀缺，并要求同时评估 fidelity 与 downstream utility。 | source_window | synthetic-data-generation / time-series-synthetic-data-generation | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] | high |
| 新增 CTGAN 后，synthetic data generation 从 time-series seed 扩展到 tabular synthetic data：mixed-type columns、multimodal continuous columns、imbalanced categories 和 ML efficacy benchmark 成为数据层系统问题。 | source_window | synthetic-data-generation / tabular-synthetic-data-generation | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] | high |
| 新增 TDML 后，ML systems 的 trust/privacy seed 扩展到 trustworthy distributed ML：公开远程 trainers 的任务协调、训练 trace、cross-validation、malicious trainer isolation 和 reward audit 成为系统问题。 | source_window | trustworthy-distributed-ml / blockchain-coordinated-training | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] | high |
| 新增 SBPM attacks paper 后，synthetic data generation 的评价轴扩展到 privacy release boundary：similarity-based privacy metrics、filters 和 metric APIs 可能泄露 membership、attributes 与 train outliers。 | source_window | synthetic-data-generation / synthetic-data-privacy-evaluation / privacy-and-trustworthy-ml | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] | high |
| 新增 EndSDG 后，synthetic data generation 扩展到 collaborative multi-custodian publishing：MPC input privacy、DP output privacy、private preprocessing/evaluation/tuning 和 final-output-only release 成为系统问题。 | source_window | synthetic-data-generation / collaborative-synthetic-data-generation / privacy-and-trustworthy-ml | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] | high |
| 新增 Rap-LI 后，privacy-and-trustworthy-ML 扩展到 cloud/black-box LLM inference prompt privacy：PII/contextual leakage、user-side risk labeling、LDP text sanitization 和 prompt utility tradeoff 成为系统问题。 | source_window | privacy-and-trustworthy-ml / llm-inference-privacy | [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Rap-LI]] | high |
| 新增 PipeDream 后，ML systems 扩展到 training systems：DNN 训练吞吐、communication bottleneck、pipeline scheduling、stage partitioning 和 parameter versioning 成为系统问题。 | source_window | training-systems / dnn-training-parallelism | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] | high |
| 研究动态需要后续 `nahida-daily-fetch` 或 `nahida-research-search` 验证。 | freshness_gap | domain dynamics | no daily evidence in current run | high |

## 学术关注

| 关注点 | 为什么重要 | 代表 Sources | 影响的 Knowledge nodes | 未解决点 |
| --- | --- | --- | --- | --- |
| Federated learning aggregation integrity | FL 的隐私优势不能保证 aggregator 正确聚合；aggregation correctness 需要独立验证。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] | [[federated-learning-integrity|Federated learning integrity]] | malicious clients, secure aggregation privacy, production cost |
| Verifiable federated training integrity | FL 的参与方也可能 lazy，不真实执行本地训练；local computation correctness 需要独立证明。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] | [[federated-learning-integrity|Federated learning integrity]], [[verifiable-training|Verifiable ML training]] | poisoning, data quality, large-model practicality |
| Secure aggregation input validation | Secure aggregation 隐藏 update 后会让 server 难以做 robust filtering；需要把 privacy 和 input integrity 联合建模。 | [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] | [[federated-learning-integrity|Federated learning integrity]], [[verifiable-aggregation|Verifiable aggregation]] | predicate-passing poisoning, secure aggregation foundation, server cost |
| Synthetic data generation for scarce temporal data | 数据稀缺、高噪声和难以复现实验会限制 ML 训练；合成数据需要保留真实结构并改善下游任务。 | [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|FTS-Diffusion]] | [[synthetic-data-generation|Synthetic data generation]], [[time-series-synthetic-data-generation|Time-series synthetic data generation]] | privacy leakage, multivariate dependencies, regime shifts, reproducibility |
| Tabular synthetic data generation and evaluation | 静态表格数据生成需要处理混合列类型、多峰连续列、类别不平衡，并用 likelihood/ML efficacy 区分 fidelity 与 utility。 | [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|CTGAN]] | [[synthetic-data-generation|Synthetic data generation]], [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | privacy leakage, rare subgroup fidelity, relational data, modern benchmarks |
| Trustworthy distributed training over public remote resources | 当训练算力来自公开远程节点时，系统要验证 workload、隔离 malicious trainers、追踪训练过程并处理奖励。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] | [[trustworthy-distributed-ml|Trustworthy distributed ML]], [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]] | hardware attestation, chain overhead, formal privacy/security, real large-model deployment |
| Synthetic data privacy release boundary | 合成数据发布不能只看 fidelity/utility/similarity；需要明确 threat model、DP/process-level guarantees 或 attack auditing。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] | [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]], [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | DP synthetic data foundations, production privacy reports, non-tabular privacy |
| Collaborative synthetic data release | 多机构不能集中原始数据但需要共享 synthetic data 时，preprocessing、evaluation、hyperparameter tuning 和 final release 都进入 input/output privacy boundary。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] | [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]], [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | DP preprocessing, CaPS/FLAIM primary sources, production governance |
| LLM prompt privacy before cloud inference | 用户 prompt 同时是任务输入和敏感信息载体；黑盒服务端不可控时，需要 user-side protection，并区分 PII extraction、PII matching 和 contextual attribute inference。 | [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Rap-LI]] | [[llm-inference-privacy|LLM inference privacy]], [[llm-inference-privacy-to-zkml-verifiable-inference|LLM inference privacy -> zkML verifiable inference]] | prompt privacy survey, SanText/CusText/InferDPT/SnD primary sources, Rap-LI repo, cryptographic private inference comparison |
| DNN training throughput and parallelism | 多 GPU/多服务器训练受 communication、pipeline stalls、memory 和 parameter versioning 约束；系统吞吐和 time-to-accuracy 需要独立建模。 | [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream]] | [[training-systems|ML training systems]], [[dnn-training-parallelism|DNN training parallelism]], [[dnn-training-parallelism-to-trustworthy-distributed-ml|DNN training parallelism -> trustworthy distributed ML]] | modern pipeline/tensor parallelism, ZeRO/FSDP, DeepSpeed/Megatron/PiPPy repo evidence |

## 工业与工程关注

| 关注点 | 工程动机 | 代表仓库/标准/实现/新闻 | 约束或瓶颈 | 影响的 Knowledge nodes |
| --- | --- | --- | --- | --- |
| Verifiable FL prototype cost | Proof generation、communication 和 chain finality 会决定是否可部署。 | none in vault beyond paper prototype | 缺 repo/production benchmark | [[federated-learning-integrity|Federated learning integrity]] |

## 新兴方向与热词

| 术语/方向 | 信号来源 | 成熟度 | 是否应建 Knowledge node | Next action |
| --- | --- | --- | --- | --- |
| verifiable federated learning | zkFL + PZKP-FL + RiseFL sources | active_seed | 已建 [[federated-learning-integrity|Federated learning integrity]] | 吸收 RoFL/ACORN/EIFFeL/secure aggregation primary sources |
| secure aggregation input validation | RiseFL source | active_seed | 暂作为 [[federated-learning-integrity|Federated learning integrity]] 的方法路线，不单独建节点 | 吸收 RoFL/ACORN/EIFFeL primary sources 后复核 |
| blockchain-based FL verification | zkFL source | source_extension | 暂不单独建 ML child | 等更多 blockchain FL sources |
| synthetic data generation | FTS-Diffusion source and pending synthetic-data queue items | active_seed | 已建 [[synthetic-data-generation|Synthetic data generation]] | 吸收 tabular/time-series/evaluation/privacy synthetic data sources |
| time-series synthetic data generation | FTS-Diffusion source | active_seed | 已建 [[time-series-synthetic-data-generation|Time-series synthetic data generation]] | 吸收 TimeGAN/CSDI/TimeVAE/QuantGAN or evaluation sources |
| tabular synthetic data generation | CTGAN source | active_seed | 已建 [[tabular-synthetic-data-generation|Tabular synthetic data generation]] | 吸收 DP synthetic data、tabular diffusion、relational/multi-table synthesizers and evaluation sources |
| synthetic data privacy evaluation | SBPM attacks paper | active_seed | 已建 [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | 吸收 DP synthetic data、privacy attack/audit、collaborative synthetic data sources 后复核 |
| collaborative synthetic data generation | EndSDG source | active_seed | 已建 [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | 吸收 CaPS/FLAIM、DP preprocessing 和 production governance sources 后复核 |
| llm inference privacy | Rap-LI source | active_seed | 已建 [[llm-inference-privacy|LLM inference privacy]] | 吸收 privacy-preserving prompt engineering survey、LDP text sanitization primary sources 和 Rap-LI repo 后复核 |
| synthetic data evaluation | FTS-Diffusion + CTGAN + SBPM attacks paper | candidate_axis | 暂作为 synthetic data generation 下的总评价轴，不单独建节点 | 更多 fidelity/utility/privacy/fairness/robustness sources 后复核 |
| trustworthy distributed ML | TDML source | active_seed | 已建 [[trustworthy-distributed-ml|Trustworthy distributed ML]] | 吸收 blockchain-based DML、remote compute、attestation、robust distributed training sources |
| blockchain-coordinated distributed training | TDML source | candidate_method | 暂作为 [[trustworthy-distributed-ml|Trustworthy distributed ML]] 的方法路线和 bridge，不单独建节点 | 更多 source 后复核是否拆 method-family |
| ML training systems | PipeDream source | active_seed | 已建 [[training-systems|ML training systems]] | 吸收 GPipe/PiPPy/Megatron/DeepSpeed/ZeRO/FSDP sources |
| DNN training parallelism | PipeDream source | active_seed | 已建 [[dnn-training-parallelism|DNN training parallelism]] | 吸收 pipeline/tensor/data-parallel training sources 后复核是否拆 method-family |
| pipeline parallelism | PipeDream source | candidate_method | 暂作为 [[dnn-training-parallelism|DNN training parallelism]] 的方法路线，不单独建节点 | 多源支持后可拆为 method-family node |

## 待解决问题

| Open problem | 类别 | 为什么还没解决 | 当前路线 | 需要的新 source/skill |
| --- | --- | --- | --- | --- |
| Aggregator privacy/model inversion | privacy_gap | zkFL aggregator receives plaintext local updates | future work in zkFL | secure aggregation / DP-FL sources |
| Malicious clients/model poisoning | security_gap | RiseFL 过滤 predicate-defined malformed updates，但 predicate-passing poisoning 仍可能存在 | relaxed SAVI / input-validation route | robust FL sources |
| Proof generation cost | implementation_gap | Halo2 proof generation can be tens of minutes for large models | prototype evidence | repo/benchmark sources |
| Local training proof scalability | implementation_gap | PZKP-FL iris task needs 90,000 proofs and still uses small ML tasks | source evidence | larger-model proof-of-training sources |
| Secure aggregation foundation | foundation_gap | RiseFL 是强 source evidence，但不是 secure aggregation 全景综述 | source evidence | foundation pack/search |
| Synthetic data foundation | foundation_gap | FTS-Diffusion 是金融时序 seed，不是 synthetic data generation 全景综述 | source evidence | foundation pack/search |
| Synthetic data privacy/fidelity/utility tradeoff | evaluation_gap | 当前 source 覆盖部分 fidelity/utility 和 SBPM 隐私风险，但还缺 fairness、robustness 和 DP tradeoff foundation | FTS-Diffusion TMTR/TATR; CTGAN likelihood/ML efficacy; SBPM attack seed | synthetic data evaluation/privacy sources |
| Synthetic data release privacy guarantees | privacy_gap | SBPM attacks paper 说明相似性指标不构成 guarantee，但 DP synthetic data 和生产发布治理仍缺 source | SBPM attack/audit seed | DP synthetic data, privacy reports, attack/audit surveys |
| Collaborative synthetic data preprocessing/tuning privacy | privacy_gap | EndSDG 说明 exact MPC quantile binning 尚未 DP，且 private evaluation/tuning 的治理边界仍薄 | MPC + DP-in-MPC EndSDG route | CaPS/FLAIM, DP quantile/preprocessing, production governance sources |
| LLM prompt privacy taxonomy | foundation_gap | Rap-LI 给出 strong seed，但 masking、rewriting、LDP、cryptographic private inference、enterprise logging/governance 尚未系统化 | risk-aware LDP prompt sanitization | prompt privacy survey, SanText/CusText/InferDPT/SnD, Rap-LI repo, private inference sources |
| Multivariate temporal dependencies | method_limitation | FTS-Diffusion 正文把 multivariate modeling 列为 future work | pattern-aware time-series generation | more time-series generation sources |
| Tabular rare subgroup fidelity | evaluation_gap | CTGAN 针对 imbalanced categories 提供 sampling route，但没有 rare subgroup/fairness/privacy evaluation | conditional tabular generation | tabular synthetic data evaluation sources |
| Remote trainer/hardware trust | security_gap | TDML 让 trainers 注册 hardware specs，但没有 attestation 或 remote environment proof | blockchain-coordinated training trace | attestation/TEE/decentralized compute sources |
| Blockchain coordination overhead for ML training | implementation_gap | TDML 没有量化 chain finality、IPFS、encrypted RPC、private-chain storage 的端到端成本 | ResNet50 prototype | implementation/benchmark sources |
| Proof-of-training boundary | foundation_gap | TDML 的 proof-of-training 是 trace audit，不是 cryptographic proof；需避免与 ZK proof-of-training 混淆 | TDML §3.3.2 | proof-of-training/verifiable training sources |
| Training systems foundation | foundation_gap | PipeDream 创建训练系统 seed，但还缺 GPipe/PiPPy/Megatron/DeepSpeed/ZeRO/FSDP 等现代 sources | pipeline parallelism seed | training-system papers/repos |
| Parallelism vs trust boundary | bridge_gap | PipeDream 解决受控集群性能，TDML 解决公开远程训练可信性；二者不能混成一个问题 | bridge seed | remote training trust + modern training runtime sources |
| Current industrial trend unknown | freshness_gap | no web/daily fetch used | current-vault dynamics only | `nahida-daily-fetch` |

## 方向倾向判断

- 学术界倾向: 当前 vault 记录到的 seed 已从 aggregator correctness 扩展到 local training verification、secure aggregation input validation、synthetic data generation for scarce temporal/tabular data、synthetic data privacy evaluation、collaborative synthetic data release、trustworthy distributed training、LLM prompt/inference privacy 和 DNN training parallelism。
- 工业界倾向: 缺 repo/standard/release evidence，不能声称外部趋势。
- 二者一致的地方: 如果 FL 走向多机构协作或无信任 aggregator，aggregation correctness、client update validity 和 auditability 会成为系统问题；如果 ML 走向高价值低样本、结构化数据共享或多机构不能集中数据的场景，synthetic data 的 fidelity/utility/privacy boundary、input/output privacy split 和 private evaluation/tuning 也会成为系统问题，且相似性指标不能直接替代 DP/攻击审计；如果训练算力走向公开远程资源，participant coordination、training trace 和 reward audit 也会进入 ML systems 的可信性范围；如果训练本身走向更大模型和更多 accelerators，parallelism、communication overlap、memory footprint 和 scheduler correctness 会成为训练系统问题；如果 LLM 服务继续以 cloud/black-box inference 形态提供，prompt privacy 需要在服务端不可控条件下处理 user-side sanitization、contextual leakage 和 utility tradeoff。
- 二者张力: ZKP route 的证明成本、通信量和 chain finality 可能限制直接部署；synthetic data route 则可能在 fidelity、utility、privacy、相似性指标可解释性和 out-of-distribution robustness 之间产生冲突；blockchain-coordinated training route 需要在 auditability 与 chain/IPFS/RPC overhead、隐私泄露和硬件真实性之间折中；training parallelism route 需要在吞吐、通信、内存、调度复杂度和统计效率之间折中；prompt privacy route 则需要在 token perturbation、语义保真、用户调节成本和正式隐私保证之间折中。
- 需要谨慎的推断: 任何“最新/热门/主流”表述必须等 daily-fetch 或 research-search。

## 证据窗口

| Source/Note | Date | Kind | 支持了什么判断 | Caveat |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 2026-06-20 | source | federated learning integrity seed | not latest trend evidence |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 2026-06-21 | source | verifiable federated training and secure-sum aggregation integrity seed | not latest trend evidence |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | 2026-06-23 | source | secure aggregation input-validation and relaxed SAVI route | not latest trend evidence |
| [[sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns|Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns]] | 2026-06-23 | source | synthetic data generation and time-series synthetic data generation seed | not latest trend evidence; anonymous under-review |
| [[arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan|Modeling Tabular Data using Conditional GAN]] | 2026-06-23 | source | tabular synthetic data generation and synthetic data evaluation seed | not latest trend evidence |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | 2026-06-23 | source | trustworthy distributed ML and blockchain-coordinated training seed | not latest trend evidence; venue/canonical URL unknown |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | 2026-06-23 | source | synthetic data privacy evaluation seed and synthetic-data/privacy bridge | not latest trend evidence |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 2026-06-23 | source | collaborative synthetic data generation seed and synthetic-data/privacy bridge refresh | not latest trend evidence |
| [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Risk-Aware Privacy Preservation for LLM Inference]] | 2026-06-23 | source | LLM inference privacy seed and prompt-privacy/verifiable-inference boundary bridge | not latest trend evidence |
| [[doi-10-1145-3341301-3359646-pipedream-generalized-pipeline-parallelism-dnn-training|PipeDream: Generalized Pipeline Parallelism for DNN Training]] | 2026-06-23 | source | training systems and DNN training parallelism seed | not latest trend evidence |

## 刷新触发器

| Trigger | Why | Suggested action |
| --- | --- | --- |
| 新 FL security/privacy paper/repo 吸收 | 可能拆分 secure aggregation、robust FL、client-verification routes | nahida-update |
| 用户询问最新 trustworthy ML/FL 进展 | 需要外部 freshness，不应只用本 vault | nahida-daily-fetch / nahida-research-search |
| zkML 或 blockchain FL source 增加 | 可能改变 ZKP/ML bridge 和 application taxonomy | nahida-knowledge-get |
| 新 synthetic data / time-series / tabular generation / synthetic data privacy/evaluation source 吸收 | 可能补全 synthetic data generation direction、评价轴和 privacy/fidelity/utility bridge | nahida-update |
| 新 collaborative/federated synthetic data、DP preprocessing 或 privacy-preserving evaluation/tuning source 吸收 | 可能补全 collaborative synthetic data generation 和 input/output privacy taxonomy | nahida-update |
| 新 blockchain-based distributed ML、remote compute、trainer attestation 或 robust distributed training source 吸收 | 可能补全 trustworthy distributed ML 和 blockchain coordination bridge | nahida-update |
| 新 prompt privacy、LDP text sanitization、privacy-preserving prompt engineering 或 private LLM inference source/repo 吸收 | 可能补全 LLM inference privacy taxonomy，并校准与 zkML verifiable inference 的边界 | nahida-update / nahida-github-repo-analyze |
| 新 training systems、pipeline/tensor parallelism、large-model memory optimization 或 training framework repo 吸收 | 可能补全 training systems taxonomy，并校准 DNN training parallelism 与 trustworthy distributed ML 的边界 | nahida-update / nahida-github-repo-analyze |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Created stale domain dynamics note for ML systems cold-start. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risefl-low-cost-zkp | Refreshed current-vault dynamics with RiseFL secure aggregation input-validation route; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-fts-diffusion-financial-time-series | Refreshed current-vault dynamics with synthetic data generation and time-series synthetic data generation seed; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Refreshed current-vault dynamics with trustworthy distributed ML and blockchain-coordinated training seed; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-ctgan-tabular-synthetic-data | Refreshed current-vault dynamics with tabular synthetic data generation and synthetic data evaluation seed; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Refreshed current-vault dynamics with synthetic data privacy evaluation and synthetic-data/privacy bridge; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Refreshed current-vault dynamics with collaborative synthetic data generation and input/output privacy boundary; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risk-aware-llm-inference-privacy | Refreshed current-vault dynamics with LLM prompt privacy, risk-aware LDP sanitization and prompt-privacy/verifiable-inference boundary; no external freshness claim. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-pipedream-dnn-training-parallelism | Refreshed current-vault dynamics with training systems and DNN training parallelism; no external freshness claim. | 1 source note | codex |
