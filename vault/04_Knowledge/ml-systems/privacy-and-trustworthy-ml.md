---
id: "nahida-knowledge-privacy-and-trustworthy-ml"
title: "Privacy and trustworthy ML"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "privacy-and-trustworthy-ml"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
parent_knowledge_refs:
  - "nahida-knowledge-ml-systems"
child_knowledge_refs:
  - "nahida-knowledge-federated-learning-integrity"
  - "nahida-knowledge-trustworthy-distributed-ml"
  - "nahida-knowledge-llm-inference-privacy"
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml"
relation_edges:
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "is_a"
    to: "nahida-knowledge-ml-systems"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
      - "vault/04_Knowledge/ml-systems.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "has_child"
    to: "nahida-knowledge-federated-learning-integrity"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "has_child"
    to: "nahida-knowledge-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "has_child"
    to: "nahida-knowledge-llm-inference-privacy"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "bridges_to"
    to: "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
    evidence_refs:
      - "vault/05_Bridges/blockchain-coordination-to-trustworthy-distributed-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "bridges_to"
    to: "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/05_Bridges/synthetic-data-generation-to-privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-and-trustworthy-ml"
    relation: "bridges_to"
    to: "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/llm-inference-privacy-to-zkml-verifiable-inference.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
  - "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
  - "nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml"
  - "nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml"
  - "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
  - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
  - "vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md"
  - "vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md"
  - "vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md"
  - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
representative_source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "doi:10.1145/3460120.3485379"
  - "arxiv:2311.15310v1"
  - "doi:10.1145/3617232.3624852"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "doi:10.1109/TIFS.2026.3667458"
query_keys:
  - "privacy and trustworthy ML"
  - "trustworthy machine learning"
  - "privacy-preserving machine learning"
  - "federated learning integrity"
  - "verifiable federated training"
  - "PZKP-FL"
  - "verifiable inference"
  - "model prediction integrity"
  - "zkCNN"
  - "zero-knowledge CNN inference"
  - "RiseFL"
  - "secure aggregation input validation"
  - "type-based zkNN optimization"
  - "ZK-friendly ML operators"
  - "trustworthy distributed ML"
  - "TDML"
  - "blockchain-coordinated distributed training"
  - "remote trainer validation"
  - "synthetic data privacy evaluation"
  - "similarity-based privacy metrics"
  - "synthetic data release privacy"
  - "ReconSyn"
  - "DifferenceAttack"
  - "collaborative synthetic data generation"
  - "input privacy output privacy"
  - "DP-in-MPC synthetic data"
  - "LLM inference privacy"
  - "prompt privacy"
  - "privacy-preserving prompt engineering"
  - "local differential privacy for LLM inference"
  - "risk-aware LDP"
  - "Rap-LI"
aliases:
  - "trustworthy ML"
  - "privacy-preserving ML"
domains:
  - "ml-systems"
topics:
  - "privacy-and-trustworthy-ml"
  - "federated-learning-integrity"
  - "verifiable-aggregation"
  - "verifiable-training"
  - "verifiable-inference"
  - "model-prediction-integrity"
  - "secure-aggregation-input-validation"
  - "zk-friendly-ml-operators"
  - "trustworthy-distributed-ml"
  - "blockchain-coordinated-training"
  - "remote-trainer-validation"
  - "synthetic-data-privacy-evaluation"
  - "synthetic-data-generation"
  - "membership-inference"
  - "reconstruction-attacks"
  - "collaborative-synthetic-data-generation"
  - "input-output-privacy"
  - "llm-inference-privacy"
  - "prompt-privacy"
  - "local-differential-privacy"
tags:
  - "nahida/knowledge"
  - "nahida/direction"
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
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
  - "nahida-knowledge-20260623-zeno-verifiable-inference"
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
  - "nahida-knowledge-20260623-synthetic-data-privacy-metrics"
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
  - "nahida-knowledge-20260623-risk-aware-llm-inference-privacy"
source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "doi:10.1145/3460120.3485379"
  - "arxiv:2311.15310v1"
  - "doi:10.1145/3617232.3624852"
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
  - "arxiv:2312.05114v2"
  - "arxiv:2412.03766v1"
  - "doi:10.1109/TIFS.2026.3667458"
confidence: "medium"
trust_tier: "primary"
---

# Privacy and trustworthy ML

## 定义与范围

- 定义: Privacy and trustworthy ML 组织 ML systems 中与隐私、完整性、可验证性、审计性、安全威胁和多参与方信任边界有关的问题。
- 不包含: 某个算法名、某个协议实例、单篇 paper 的局部 gadget 或一次 benchmark；这些保留在 source note。
- Canonical terms: `privacy and trustworthy ML`, `trustworthy ML`
- Aliases/query keys: privacy-preserving machine learning, federated learning integrity
- Standalone completeness check: 本节点给出方向范围、下级问题、方法族、代表 source、当前综合和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询 ML 系统中的隐私、完整性、可验证训练/推理、federated learning security 或公开远程训练可信性时，先读本节点。
- Update scope: 新 source 若涉及 secure aggregation、robust FL、private inference、verifiable training/inference、model integrity、remote trainer validation、auditability，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

model_prior_background: Trustworthy ML 不是单一技术，而是一组 threat-model-driven 问题。隐私路线可能保护数据/模型不被看到；完整性路线要求输出、更新或聚合不能被篡改；可验证路线让外部 verifier 检查计算关系；鲁棒性路线处理 poisoned/adversarial inputs。不同路线经常互相牵制。

zkFL、PZKP-FL、zkCNN、RiseFL、ZENO、TDML、SBPM attacks paper、EndSDG 和 Rap-LI 当前给出九条 seed: zkFL 用 ZKP 证明 federated learning aggregation correctness，防止 malicious aggregator 改写 global update；PZKP-FL 用 Groth16/Sigma proofs 验证 trainer 本地训练过程，并用 secure sum/smart contract 验证 global aggregation，防止 lazy trainer 和 unreliable publisher；zkCNN 用 ZK proof 证明 CNN prediction/accuracy relation，面向 MLaaS prediction integrity 和 proprietary model confidentiality；RiseFL 用 secure aggregation + probabilistic ZKP input validation 过滤 malformed client updates，同时保护 individual updates；ZENO 从 proof-generation cost 角度说明可验证 NN 推理要保留 privacy/tensor/layer semantics，才能让 integrity proof 走向可用系统；TDML 则把 trust boundary 扩展到公开远程算力上的 distributed training，用 blockchain coordination、training trace、cross-validation 和 malicious trainer detection 管理 remote trainer workload；SBPM attacks paper 把 trust boundary 扩展到 synthetic data release，说明 similarity metrics、filters 和 metric APIs 不能替代端到端 DP 或攻击审计；EndSDG 进一步说明 multi-custodian synthetic data release 需要同时处理 MPC input privacy、DP output privacy、private evaluation/tuning 和 final-output-only release boundary；Rap-LI 把 trust boundary 扩展到 cloud/black-box LLM prompt inference，说明 prompt PII/contextual leakage 需要 user-side risk-aware LDP sanitization，而不能只靠 masking、local rewriting 或 uniform budget。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction`
- 为什么足够通用: 它可组织 federated learning integrity、secure aggregation、private inference、verifiable training、remote trainer validation、robustness/auditability 等问题。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkFL 是代表 source，不是方向名。
- 需要引用的更基础 Knowledge: [[ml-systems|ML systems]]。
- 不应拆出的实例/协议/来源: zkFL、某个 secure aggregation protocol、某个 privacy framework 默认作为 source instance，除非多来源复用证明需要独立方法节点。

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Privacy boundary | 谁能看到数据、模型、更新和中间状态 | zkFL 只覆盖 miners/outsiders，不覆盖 aggregator inversion |
| Integrity boundary | 谁可能篡改训练、聚合、推理或评估结果 | zkFL 覆盖 malicious aggregator；PZKP-FL 覆盖 lazy trainer local computation 与 publisher aggregation |
| Verifiability | 能否用短证据检查计算或系统行为 | zkFL 用 zk-SNARK aggregation proof；PZKP-FL 用 Groth16/Sigma proof；zkCNN/ZENO 用 NN inference proof 与 proof-generation optimization |
| Accountability/auditability | 结果能否被第三方或链上记录追溯 | zkFL blockchain variant stores hash of committed aggregate；PZKP-FL uses smart contract for aggregation |
| Remote trainer trust boundary | 公开远程算力节点是否真实执行训练 workload，能否被筛选、验证、追责和奖励 | TDML 用 public/private blockchain coordination、cross-validation、gradient clustering 和 reward trace 建立 active seed |
| Synthetic data release privacy | 合成数据、隐私指标、filters 和发布流程是否泄露训练记录、属性或 outliers | SBPM attacks paper 用 DifferenceAttack/ReconSyn 证明相似性指标不能作为匿名保证 |
| Collaborative synthetic data input/output privacy | 多数据持有方协作发布合成数据时，谁能看到原始数据、中间 metrics/thresholds、调参结果和最终发布数据 | EndSDG 用 MPC secret shares 保护 input privacy，并用 DP/final-output-only route 管理 output privacy |
| LLM prompt/inference privacy | 用户把 prompt 发给 cloud/black-box LLM 前，如何保护 PII、上下文属性和任务相关敏感信息，同时保留 utility | Rap-LI 用 risk-aware LDP text sanitization 和 personalized labeling 建立 active seed |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[ml-systems|ML systems]] | child_of | zkFL cold-start classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[federated-learning-integrity|Federated learning integrity]] | child / problem | zkFL 完整围绕 malicious aggregator and aggregation verification；该问题可容纳更多 FL integrity sources。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] | active_seed |
| [[trustworthy-distributed-ml|Trustworthy distributed ML]] | child / problem | TDML 暴露了公开远程算力训练中的 workload traceability、remote trainer validation、malicious trainer detection 和 reward audit 问题。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] | active_seed |
| [[llm-inference-privacy|LLM inference privacy]] | child / problem | Rap-LI 暴露了 cloud/black-box LLM prompt 中 PII/contextual privacy leakage、uniform LDP tradeoff 和 user-side sanitization 问题。 | [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Rap-LI]] | active_seed |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | cross-direction evaluation_axis | 合成数据发布的隐私风险属于 synthetic data generation，但其 guarantee、attack auditing 和 release-process boundary 属于 trustworthy ML。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] | active_seed_bridge |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]] | cross-direction problem | 多方合成数据发布把 input privacy、output privacy、private evaluation 和 tuning governance 接入 ML trust boundary。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] | active_seed_bridge |
| secure aggregation privacy | candidate problem | 与 zkFL 的 aggregator-integrity 相邻但目标不同；当前 source 不足以建节点。 | none | queued |
| robust federated learning | candidate problem | malicious client/model poisoning 不是 zkFL 解决的问题；需独立 sources。 | none | queued |
| verifiable inference/training | cross-domain problem | ZKP side 已有 [[zkml|zkML]] 子节点；在 ML systems 侧需要更多 non-ZKP evidence 再决定是否拆 child。 | zkCNN/zkLLM/Sparrow/zkFL | review |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| [[federated-learning-integrity|Federated learning integrity]] | 检查 global update 是否由合法 client updates 正确聚合而来。 | FL 中存在 aggregator/coordinator，且 participants 需要验证其行为。 | 不自动保护 local data privacy 或 malicious clients。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |
| ZKP-based verification | 用 commitments、signatures 和 proof relation 证明 ML system event 的正确性。 | 计算关系可电路化，verifier 不应重做完整计算。 | Proving cost、circuit correctness 和 statement design 是瓶颈。 | [[verifiable-aggregation|Verifiable aggregation]] |
| ZK verifiable prediction | 用 model commitment 和 inference proof 检查 prediction/accuracy claim 是否来自指定模型，并通过保留 ML operator semantics 降低 proof-generation cost。 | MLaaS 或模型拥有者需要隐藏 weights，但外部 verifier 需要检查输出真实性。 | 不证明训练来源、模型质量、公平性或输出安全；architecture、privacy annotation 和 quantization assumptions 需明确。 | [[verifiable-inference|Verifiable inference]]; [[zk-friendly-ml-operators|ZK-friendly ML operators]]; [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]]; [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]] |
| Blockchain-based audit/verification | 用链上 hash/verification 记录降低单点验证或篡改风险。 | 需要公开验证或跨轮可追溯记录。 | Finality、gas、data availability 和 chain trust boundary 仍是系统问题。 | zkFL blockchain variant |
| ZK verifiable local training | 用 training proof 检查 trainer 是否真实执行本地训练，并在必要时隐藏 local data/intermediate values。 | FL threat model 包含 lazy trainers 或 outsourced/local computation cheating。 | 不证明数据质量、poisoning 或模型泛化。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |
| Secure aggregation input validation | 在 server 看不到 individual update 的前提下，用 ZKP predicate 过滤 malformed updates，然后只聚合 valid clients。 | FL 同时要求 privacy 与 malicious-client filtering。 | relaxed/probabilistic；不处理 predicate-passing poisoning、fairness 或 convergence。 | [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|RiseFL]] |
| [[trustworthy-distributed-ml|Blockchain-coordinated remote training]] | 用 public chain 发现/选择远程训练资源，用 private chain 记录训练 trace/validation results/reward evidence，并用 cross-validation + gradient clustering 隔离 malicious trainers。 | 训练算力来自 public remote computing resources，系统需要 auditability 和 participant coordination。 | trace audit 不等于 cryptographic proof；不证明隐私、硬件真实性、模型质量或大模型生产成本。 | [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML]] |
| [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] | 对合成数据发布流程做 threat-model-driven 隐私评估，检查 metrics、filters、query access 和 DP boundary。 | 合成数据用于敏感数据共享、匿名化、合规或外部发布。 | similarity-based metrics 是 heuristic；攻击审计不能替代 formal guarantee；DP 后处理/metric access 需要 budget/process 约束。 | [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|SBPM attacks paper]] |
| [[collaborative-synthetic-data-generation|Collaborative synthetic data release privacy]] | 用 MPC 管理多方 input privacy，用 DP 管理最终 output privacy，并把 preprocessing/evaluation/tuning 留在私有流水线中。 | 多 data custodians 需要发布合成数据，但不能集中原始数据或公开中间质量指标。 | MPC secrecy、DP release guarantee、DP preprocessing 和治理/审计可解释性必须分别成立。 | [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|EndSDG]] |
| [[llm-inference-privacy|Risk-aware LDP prompt sanitization]] | 在用户侧识别 prompt token 风险、允许用户调节标签，再用异构 privacy budget、candidate space sizing 和 high-risk score reversal 扰动文本。 | 用户调用 black-box/cloud LLM，不能要求服务端协作，且 prompt 中同时包含任务语义和敏感信息。 | 依赖 NER/risk labels；token-level sanitization 会损伤 NLG 语义；不能证明模型推理正确。 | [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Rap-LI]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 创建 federated learning integrity seed；展示 ZKP/blockchain route for malicious aggregator | 不解决 malicious clients；aggregator sees local updates; proof generation heavy | `p1-p14` |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 补充 local training verification、secure-sum aggregation verification 和 FL local-data privacy route | 不解决 poisoning/data quality；实验小；proof count high | `p1-p15` |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | paper | 补充 MLaaS prediction integrity seed；展示 private CNN weights 下的 prediction/accuracy proof route | public architecture; quantized CNN computation; not training provenance/fairness/safety | `p1-p18` |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | paper | 补充 RiseFL secure aggregation input-validation route；用 relaxed SAVI 组织 privacy + malicious-client integrity | single-server and `m < n/2`; predicate-passing poisoning 未解决 | `p1-p15` |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | paper | 补充 verifiable NN inference 的 systems feasibility 证据；用 privacy/tensor types、ZENO circuit、knit encoding 和 NN-centric reuse/fusion 降低 zkSNARK NN proving cost | inference-only; not training provenance/fairness/safety; correctness depends on compiler semantics and privacy annotations | `p1-p15` |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | paper | 新增 trustworthy distributed ML 问题 seed；展示 blockchain coordination、training trace audit、remote trainer validation 和 malicious-gradient detection route | ResNet50/CIFAR-10 原型；proof-of-training 是 trace audit 不是 ZK proof；无 formal privacy/security proof | `p1-p11` |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | paper | 补充 synthetic data release privacy seed；证明 SBPMs/filters/metric APIs 不能替代 DP 或攻击审计；通过 DifferenceAttack/ReconSyn 展示 membership、attribute 和 outlier reconstruction risk。 | tabular synthetic data focused; assumes generator/metric access; not a DP synthetic data construction | `p1-p19` |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | paper | 补充 collaborative synthetic data input/output privacy seed；展示 MPC + DP-in-MPC + private evaluation/tuning 的合成数据发布路线。 | arXiv preprint; DP quantile binning not complete; code not analyzed; genomic use case preliminary | `p1-p15` |
| [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Risk-Aware Privacy Preservation for LLM Inference]] | paper | 新增 LLM inference privacy seed；展示 user-side risk-aware LDP prompt sanitization、PII/contextual attack evaluation、token/sentence-level LDP guarantee 和 interactive labeling route。 | text-only; NER dependency; token-level sanitization hurts NLG coherence; code repo not analyzed; not inference correctness proof | `p1-p16` |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，仅覆盖当前 vault 已深读 source。
- Freshness: `fresh` for local source absorption; not an external latest claim.
- 综合: 本方向目前是 foundation_thin seed。zkFL 让“联邦学习聚合是否可信”成为可检索问题节点；PZKP-FL 进一步把“trainer 是否真实本地训练”和“publisher 是否正确聚合”接入同一 integrity 视角；zkCNN 补充“模型预测/accuracy claim 是否可信”的 inference integrity 视角；RiseFL 补足“secure aggregation 下如何低成本过滤 malformed client updates”的输入验证路线；ZENO 进一步说明 verifiable inference 的可信性不能只停在 proof statement，还要处理 proof-generation 性能瓶颈，否则系统不可用；TDML 把可信性扩展到 public remote computing resources 上的分布式训练，强调 participant coordination、training trace audit、malicious trainer detection 和 reward accountability。SBPM attacks paper 把可信性扩展到 synthetic data release: 数据生成质量、统计相似性和 privacy pass/fail 不能自动构成匿名保证，train-data-dependent metrics 和 filters 本身也可能泄露信息。EndSDG 则给出建设性补充: 多方合成数据发布要同时管理 input privacy、output privacy、中间 evaluation/tuning 以及最终 release budget。Rap-LI 再把可信性扩展到 cloud/black-box LLM prompt inference: 保护对象是 user prompt 中的 PII 和 contextual attributes，机制是在本地做 risk-aware LDP sanitization；这和 zkML verifiable inference 的 committed-model correctness 是相邻但不等价的问题。privacy/trustworthy ML 的全貌还缺 secure aggregation foundation、robust FL、DP synthetic data、private inference、model provenance、remote hardware attestation、prompt privacy survey、audit/governance 等 sources。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 federated learning integrity 问题节点；把 ZKP route 连接到 zkML verifiable aggregation | 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 RoFL/ACORN/EIFFeL/secure aggregation sources 后校准 |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 补充 verifiable federated training 与 secure-sum aggregation verification route | 解决的问题; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL/secure aggregation sources 后校准 |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | 补充 ML prediction/inference integrity route；把 MLaaS prediction correctness 与 proprietary model hiding 纳入 trustworthy ML 侧的 cross-domain evidence | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合 | no | 后续吸收 private inference / model audit / non-ZKP trustworthy ML sources 后校准 |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | 补充 RiseFL secure aggregation input-validation route，明确 malicious-client malformed-update filtering 与 aggregator correctness 的区别 | 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL primary sources |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | 补充 verifiable NN inference 的 proof-generation feasibility route，把 ZK-friendly ML operators 作为跨 zkML/ML systems 的方法族证据 | 背景; 解决的问题; 方法族; 代表 Sources; 当前综合 | no | 后续吸收更多 private/verifiable inference systems 后校准 |
| [[sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework|TDML - A Trustworthy Distributed Machine Learning Framework]] | 新增 trustworthy distributed ML 问题节点；把 blockchain coordination/audit trace 与 remote trainer validation 接到 ML trust 方向；纠正队列中 zkML/verifiable-inference 误分。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 blockchain-based DML、robust distributed training 和 attestation sources 后校准 |
| [[arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets|The Inadequacy of Similarity-based Privacy Metrics: Privacy Attacks against "Truly Anonymous" Synthetic Datasets]] | 补充 synthetic data release privacy 边界；把 SBPM、DifferenceAttack、ReconSyn 与 DP pipeline break 纳入 trustworthy ML 视角；纠正队列误分到 ZK proof foundations。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 DP synthetic data/privacy audit sources 后校准 |
| [[arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation|End to End Collaborative Synthetic Data Generation]] | 补充 collaborative synthetic data release 的 input/output privacy 边界；把 private preprocessing、evaluation、threshold voting 和 hyperparameter tuning 纳入 trustworthy ML 视角。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 DP synthetic data、CaPS/FLAIM 和 privacy-preserving preprocessing sources 后校准 |
| [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Risk-Aware Privacy Preservation for LLM Inference]] | 新增 LLM inference privacy 问题节点；把 prompt PII/contextual leakage、risk-aware LDP text sanitization、personalized labeling 和 prompt utility tradeoff 纳入 trustworthy ML 视角。 | 背景; 解决的问题; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | yes | 后续吸收 prompt privacy survey、SanText/CusText/InferDPT/SnD 和 Rap-LI repo 后校准 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-aggregation; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, verification_transfer | ZKP can verify aggregation relation; ML threat model, poisoning, privacy, convergence and deployment constraints remain separate. | active_seed |
| [[zkml-verifiable-training-to-federated-learning-integrity|zkML verifiable training -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-training; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, privacy, cross_domain_mapping | Training proof detects lazy local computation; poisoning, data quality and convergence do not transfer automatically. | active_seed |
| [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]] | `blockchain-systems; ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` | application, coordination, auditability, incentive | Blockchain coordination transfers task/resource discovery and trace audit; ML correctness, privacy, hardware attestation and convergence do not transfer automatically. | active_seed |
| [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]] | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation; ml-systems/privacy-and-trustworthy-ml` | tension, privacy_boundary, evaluation_transfer, construction_route | Synthetic data can support sharing, but privacy does not transfer from similarity/fidelity metrics; DP or threat-model-specific attack evaluation is required. Collaborative release adds an input/output privacy split: MPC protects inputs, DP protects final outputs, and intermediate metrics/tuning must stay inside the trust boundary. | active_seed |
| [[llm-inference-privacy-to-zkml-verifiable-inference|LLM inference privacy -> zkML verifiable inference]] | `ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy; zero-knowledge-proofs/zkml/verifiable-inference` | contrast, complementary, trust_boundary, privacy_boundary | Prompt sanitization/LDP protects user input before black-box LLM; zkML verifiable inference proves committed-model computation. Prompt privacy and inference correctness do not transfer automatically. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-privacy-and-trustworthy-ml | is_a | nahida-knowledge-ml-systems | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md | medium | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | has_child | nahida-knowledge-federated-learning-integrity | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity.md | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | has_child | nahida-knowledge-trustworthy-distributed-ml | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml.md | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | medium | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md | source note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | bridges_to | nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md | source note | medium | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md | source note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md | source note | medium | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework.md | source note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | bridges_to | nahida-bridge-blockchain-coordination-to-trustworthy-distributed-ml | bridge note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/arxiv-2312-05114v2-inadequacy-similarity-based-privacy-metrics-synthetic-datasets.md | source note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation.md | source note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | bridges_to | nahida-bridge-synthetic-data-generation-to-privacy-and-trustworthy-ml | bridge note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | has_child | nahida-knowledge-llm-inference-privacy | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy.md | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | evidenced_by | vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md | source note | high | active_seed |
| nahida-knowledge-privacy-and-trustworthy-ml | bridges_to | nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference | bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| secure aggregation / privacy-preserving FL sources | RiseFL 给出一条 source-backed route，但完整 secure aggregation foundation 仍不足 | nahida-update | high | active_seed_gap |
| robust FL / malicious clients sources | RiseFL 只处理 predicate-defined malformed updates，不处理 predicate-passing poisoning | nahida-update | high | active_seed_gap |
| private/verifiable inference sources | zkCNN/ZENO 仍主要覆盖 ZKP-based prediction integrity 与 proving performance，需要 non-ZKP private inference、model audit 和 broader verification sources。 | nahida-update / nahida-research-search | medium | queued |
| ML auditing/governance sources | trustworthiness 不只有 cryptographic verification | nahida-research-search | medium | queued |
| Remote trainer attestation / distributed training trust sources | TDML 暴露公开远程训练可信性，但 hardware truth、chain overhead、privacy leakage 和 adaptive attack 仍缺证据 | nahida-update / nahida-research-search | high | active_seed_gap |
| DP synthetic data and privacy release sources | SBPM attacks paper 说明相似性指标不够，但仍缺 DP synthetic data foundation 和生产发布治理证据 | nahida-update / nahida-research-search | high | active_seed_gap |
| Collaborative SDG privacy sources | EndSDG 创建 active seed，但 CaPS/FLAIM、DP preprocessing 和 production governance 仍缺 primary sources。 | nahida-update / nahida-research-search | high | active_seed_gap |
| LLM prompt privacy foundations | Rap-LI 创建 active seed，但 privacy-preserving prompt engineering survey、SanText/CusText/InferDPT/SnD 原始 sources 和 production prompt governance 仍缺。 | nahida-update / nahida-research-search / nahida-github-repo-analyze | high | active_seed_gap |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Created privacy and trustworthy ML direction from zkFL source absorption. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL as verifiable federated training and secure-sum aggregation route. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Added zkCNN as MLaaS prediction integrity and verifiable inference cross-domain evidence. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risefl-low-cost-zkp | Added RiseFL as secure aggregation input-validation route under trustworthy ML. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zeno-verifiable-inference | Added ZENO as verifiable NN inference feasibility evidence and linked it to ZK-friendly ML operators. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Added trustworthy distributed ML problem seed and blockchain coordination bridge from TDML. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-synthetic-data-privacy-metrics | Added synthetic data release privacy boundary and bridge from SBPM attacks paper. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | Added collaborative synthetic data release input/output privacy route from EndSDG. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-risk-aware-llm-inference-privacy | Added LLM inference privacy child route from Rap-LI and created prompt privacy versus verifiable inference bridge. | 1 source note | codex |
