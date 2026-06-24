---
id: "nahida-knowledge-zkml"
title: "zkML"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "foundation_thin"
node_kind: "direction"
hierarchy_level: "direction"
file_slug: "zkml"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
parent_knowledge_refs:
  - "nahida-knowledge-zero-knowledge-proofs"
child_knowledge_refs:
  - "nahida-knowledge-zkml-verifiable-inference"
  - "nahida-knowledge-zkml-verifiable-training"
  - "nahida-knowledge-zkml-verifiable-aggregation"
  - "nahida-knowledge-zkml-zk-friendly-ml-operators"
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
primary_ontology_path: "zero-knowledge-proofs/zkml"
secondary_ontology_paths:
  - "zero-knowledge-proofs/applications"
relation_edges:
  - from: "nahida-knowledge-zkml"
    relation: "is_a"
    to: "nahida-knowledge-zero-knowledge-proofs"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
      - "vault/04_Knowledge/zero-knowledge-proofs.md"
    confidence: "medium"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "has_child"
    to: "nahida-knowledge-zkml-verifiable-inference"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "has_child"
    to: "nahida-knowledge-zkml-verifiable-training"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "bridges_to"
    to: "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/sum-check-protocol-to-zkml-verifiable-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "bridges_to"
    to: "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
    evidence_refs:
      - "vault/05_Bridges/memory-efficient-snarks-to-verifiable-ml-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "has_child"
    to: "nahida-knowledge-zkml-verifiable-aggregation"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-aggregation.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "bridges_to"
    to: "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
    evidence_refs:
      - "vault/05_Bridges/zkml-verifiable-aggregation-to-federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-zkml-verifiable-training.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "bridges_to"
    to: "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
    evidence_refs:
      - "vault/05_Bridges/zkml-verifiable-training-to-federated-learning-integrity.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "has_child"
    to: "nahida-knowledge-zkml-zk-friendly-ml-operators"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml/zk-friendly-ml-operators.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/zkml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-zkml"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
    evidence_refs:
      - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-inference"
  - "nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference"
  - "nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation"
  - "nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity"
  - "nahida-bridge-zk-snarks-to-zkml-verifiable-training"
  - "nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md"
  - "vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md"
  - "vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md"
  - "vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md"
  - "vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md"
  - "vault/03_Sources/papers/arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp.md"
  - "vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md"
  - "vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md"
representative_source_refs:
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3658644.3690318"
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
query_keys:
  - "zkML"
  - "zero-knowledge machine learning"
  - "zero-knowledge proofs for machine learning"
  - "verifiable inference"
  - "ZK proofs for LLMs"
  - "zkLLM"
  - "zkCNN"
  - "zero-knowledge CNN inference"
  - "CNN inference proof"
  - "convolution sumcheck"
  - "verifiable ML training"
  - "zero-knowledge forest training"
  - "proofs of training"
  - "zkFTP"
  - "verifiable aggregation"
  - "verifiable federated aggregation"
  - "federated learning integrity"
  - "zkFL"
  - "PZKP-FL"
  - "verifiable federated training"
  - "fixed-point zkML"
  - "RiseFL"
  - "secure aggregation input validation"
  - "ZK-friendly ML operators"
  - "ZENO"
  - "type-based zkNN optimizer"
  - "privacy-aware knit encoding"
  - "ZENO circuit"
  - "trustless DNN inference"
  - "ImageNet-scale ZK-SNARK inference"
  - "Halo2 DNN inference proofs"
  - "MLaaS prediction verification"
aliases:
  - "zero-knowledge machine learning"
  - "ZKML"
domains:
  - "zero-knowledge-proofs"
topics:
  - "zkml"
  - "verifiable-inference"
  - "cnn-inference-proofs"
  - "fft-convolution-sumcheck"
  - "verifiable-ml-training"
  - "proofs-of-training"
  - "machine-learning"
  - "verifiable-aggregation"
  - "federated-learning-integrity"
  - "federated-learning"
  - "fixed-point-zkml"
  - "secure-aggregation-input-validation"
  - "zk-friendly-ml-operators"
  - "type-based-zkml-optimization"
  - "zknn-inference-optimization"
  - "imagenet-scale-inference"
  - "halo2-plonkish-arithmetization"
  - "mLaaS-prediction-verification"
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
  - "nahida-knowledge-20260620-zkllm-verifiable-inference"
  - "nahida-knowledge-20260621-zkcnn-verifiable-inference"
  - "nahida-knowledge-20260620-sparrow-space-efficient-snarks"
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
  - "nahida-knowledge-20260621-pzkp-fl"
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
  - "nahida-knowledge-20260623-zeno-verifiable-inference"
  - "nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs"
source_refs:
  - "doi:10.1145/3658644.3670334"
  - "doi:10.1145/3460120.3485379"
  - "doi:10.1145/3658644.3690318"
  - "doi:10.1109/TBDATA.2024.3403370"
  - "arxiv:2304.05590v2"
  - "arxiv:2311.15310v1"
  - "doi:10.1145/3617232.3624852"
  - "arxiv:2210.08674"
confidence: "medium"
trust_tier: "primary"
---

# zkML

## 定义与范围

- 定义: zkML 指把 zero-knowledge proofs / verifiable computation 用于 machine-learning computation 的方向，目标是在不公开某些敏感 witness、model parameters、inputs 或 intermediate states 的前提下，证明 ML inference、training step、evaluation 或 model-related claim 的正确性。
- 不包含: 单个模型、单篇系统论文、某次 benchmark、某个 attention gadget 或某个仓库实现细节；这些留在 `03_Sources` source note。
- Canonical terms: `zkML`, `zero-knowledge machine learning`
- Aliases/query keys: ZKML, zero-knowledge proofs for machine learning, verifiable inference
- Standalone completeness check: 本节点给出本地定义、边界、下级问题、方法族、代表 source 和缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“ZK 怎么用于 ML/LLM”“如何验证模型推理”“模型参数隐私和证明如何组合”时先读本节点。
- Update scope: 新 source 若涉及 verifiable inference、proof of training、proof of unlearning、private model evaluation、ZK-friendly ML operators、zkML repository architecture，应刷新本节点。
- Domain dynamics note: [[research-dynamics|Zero-knowledge proofs Research Dynamics]].

## 背景

ML computation 通常包含 matrix multiplication、activation、normalization、attention、quantization 和大量 tensor operations。ZKP 原生处理 finite-field arithmetic；ML/LLM 的非线性函数、lookup-heavy operations、floating/fixed-point semantics 和巨大参数规模会把 proof generation 推到系统瓶颈。zkML 因此不是“把普通 SNARK 套在模型上”这么简单，而是需要在 proof-system route、numeric representation、operator decomposition、hardware proving 和 privacy boundary 之间做工程组合。

当前 vault 的 primary sources 覆盖多类 seed 路线: zkCNN 展示 CNN inference/accuracy proof，用 FFT/convolution sumcheck、generalized GKR、polynomial commitments 和 quantized CNN semantics 证明 committed CNN output；zkLLM 展示 LLM inference proof，用 tensor lookup、attention-specific proof、sumcheck 和 homomorphic commitments 证明 committed LLM output；ZENO 展示 zkNN inference proof generation 的 type-preserving compiler route，用 privacy/tensor type、ZENO circuit、knit encoding、layer scheduler 和 NN-centric reuse/fusion 优化 zkSNARK NN；Scaling up Trustless DNN Inference with Zero-Knowledge Proofs 展示 Halo2/Plonkish ImageNet-scale DNN route，用 custom gates、lookup nonlinearities、fixed-point quantization、sub-circuit reuse 和 Poseidon commitments 证明 MobileNet inference，并把 proof 接到 MLaaS prediction/accuracy/retrieval protocols；Sparrow 展示 tree/forest training proof，用 zkFTP/certification algorithm 和低内存 SNARK backend 证明 decision tree / random forest training relation；PZKP-FL 展示 federated/iterative training proof，用 Groth16 piece proofs、Sigma continuity proofs、fixed-point/Taylor numeric adaptation 和 secure sum 证明 local training 与 aggregation；zkFL 展示 ML aggregation proof，用 commitments、signatures 和 zk-SNARK 证明 federated learning updates 被正确聚合；RiseFL 展示 secure aggregation input-validation route，用 Pedersen/VSSS/Sigma/Bulletproofs-style proofs 低成本过滤 malformed client updates。

## 基础概念判断

- 是否是基础概念/方向/问题: `direction`
- 为什么足够通用: 它组织 ML/LLM computation 与 ZK proof-system 的交叉问题，可容纳 verifiable inference、proof of training/unlearning、private model evaluation、ZK-friendly operators 等多个下级节点。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: zkLLM、zkCNN、ZENO、Sparrow、zkFL、PZKP-FL 都是代表 source；`tlookup`、`zkAttn`、FFT convolution sumcheck、ZENO circuit、knit encoding、zkFTP、OPT/LLaMa-2/VGG16 benchmarks 保留在 source note 或方法路线。
- 需要引用的更基础 Knowledge: [[zero-knowledge-proofs|Zero-knowledge proofs]], [[proof-systems|Proof systems]], [[zk-snarks|zk-SNARKs]]。
- 不应拆出的实例/协议/来源: zkLLM、zkCNN、ZEN、Mystique、某个模型架构或某个 GitHub 仓库默认作为 source/repository instances，除非多来源证明需要独立节点。

## 解决的问题

zkML 解决的是 ML computation 与 proof systems 之间的映射问题:

- 如何证明模型 inference/output 的正确性。
- 如何证明多方 updates、gradients 或 partial results 被正确聚合。
- 如何在证明中隐藏模型参数、输入、intermediate tensors 或用户数据。
- 如何把 activation、normalization、attention、floating/fixed-point arithmetic 等 ML operator 转换成可证明关系。
- 如何让 proof size、verification time、prover time 和 memory 在模型规模上可接受。
- 如何明确证明对象的边界，避免把 inference correctness 误读为训练数据合法性、模型公平性或输出安全性。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[zero-knowledge-proofs|Zero-knowledge proofs]] | child_of | zkLLM source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| [[verifiable-inference|Verifiable inference]] | child / problem | zkCNN、zkLLM、ZENO 与 trustless DNN inference 共同覆盖“证明 committed model 的 inference output 正确，同时隐藏 weights/input/witness”的问题域；CNN route 强调 convolution/operator proving，LLM route 强调 lookup/attention，ZENO route 强调保留 privacy/tensor semantics 的 zkNN proof generation optimization，trustless DNN inference 强调 Halo2/Plonkish ImageNet-scale DNN proof 和 MLaaS trust protocols。 | [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]]; [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]]; [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]]; [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Trustless DNN inference]] | active_seed |
| [[verifiable-training|Verifiable ML training]] | child / problem | Sparrow/zkFTP 覆盖 tree/forest certification route；PZKP-FL 补充 federated iterative training route。训练证明与 inference proof 的 statement、隐私边界和资源瓶颈不同。 | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]]; [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] | active_seed |
| proof of unlearning | candidate problem | 当前 vault 尚无深读 primary source，不能由 training proof 直接外推。 | none | queued |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | child / method_family | zkCNN 的 convolution/operator proof、zkLLM 的 lookup/attention route、ZENO 的 type-preserving zkNN compiler/IR route、trustless DNN inference 的 Halo2 custom-gate/lookup route 已足以形成可复用方法族，而不是单篇 source summary。 | zkLLM; zkCNN; ZENO; Trustless DNN inference | active_seed |

| [[verifiable-aggregation|Verifiable aggregation]] | child / problem | zkFL 完整覆盖“证明 federated learning updates 被正确聚合”的问题域；它既不同于 inference，也不同于完整 training provenance。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] | active_seed |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| [[verifiable-inference|Verifiable inference]] | 证明给定 input/output 与 committed model 的 inference computation 一致，并在需要时隐藏 model/input/intermediate witness。 | 模型 architecture、commitment 和 computation relation 可被公开定义。 | 只证明 inference relation；不证明训练数据、版权、fairness 或 safety。 | [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]]; [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]]; [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Trustless DNN inference]] |
| [[zk-friendly-ml-operators|ZK-friendly ML operators]] | 把 ML tensor/linear/nonlinear/layer operators 转换成 ZK-friendly relation，并在降到 constraints 前保留可优化语义。 | ML computation 是 inference/training/aggregation proof 的主要 relation bottleneck。 | Operator route 不等于完整 proof statement；numeric semantics、privacy boundary 和 backend cost 仍需单独处理。 | [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]]; [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM]]; [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]]; [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Trustless DNN inference]] |
| Tensor/linear-operator proofs | 用 sumcheck/MLE/GKR 等 route 证明 matrix multiplication、convolution 和 tensor linear algebra。 | 大量线性代数是计算主干，且可编码成 field relations。 | 非线性、normalization、Softmax、pooling 仍需 gadgets/lookup/approximation route。 | zkCNN source note; zkLLM source note |
| Type-preserving zkNN compiler frontend | 在生成 constraints 前保留 privacy type、tensor type 和 layer structure，用于 privacy-adaptive circuit generation、ZENO circuit IR、scheduler、reuse/fusion。 | zkNN/zkML inference 需要证明 NN computation，且 public/private boundary 明确。 | 不改变 proof-system foundation；误标 privacy 会改变被证明 statement；CPU benchmark 不自动迁移到其他 backend。 | [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO]] |
| Halo2/Plonkish DNN arithmetization | 用 custom gates、lookup arguments、fixed-point quantization 和 sub-circuit reuse 把 ImageNet-scale MobileNet inference 编码成 Halo2 circuit。 | DNN operator set 可被 TFLite-to-Halo2 translator 覆盖，architecture/commitment statement 可公开定义。 | Prover cost 仍高；证明的是量化/定点语义；trust protocols 还依赖 sampling/escrow。 | [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Trustless DNN inference]] |
| CNN convolution proof route | 把 2-D convolution 转成 FFT/Hadamard/IFFT relation，并用 sumcheck/GKR 接入完整 prediction proof。 | CNN inference proof 的 bottleneck 是 convolutional layers。 | 依赖量化语义、FFT-friendly backend 和 memory/prover budget；不自动覆盖 transformer attention。 | [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN]] |
| Lookup-based nonlinear operators | 把 activation、rescaling、inverse/sqrt、Softmax exponent 等函数转成 table/function lookup relation。 | 函数域可量化或分解成可承受 table。 | table size、rounding、approximation error 和 backend 支持是主要限制。 | zkLLM source note |
| Hardware-aware proving | 用 GPU/CUDA 并行化 prover-heavy tensor work。 | 模型规模大、prover cost 是瓶颈。 | 结果依赖硬件、implementation 和 memory budget。 | zkLLM evaluation |
| [[verifiable-training|Verifiable ML training]] | 证明模型训练/认证 relation 与 committed data、model、seed 一致，并在需要时隐藏数据或模型。 | 训练算法可形式化，且 proof backend 能承载大数据集 relation。 | 不证明数据合法性、公平性、泛化能力或输出安全性；Sparrow 当前是 tree/forest route。 | [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow]] |
| Federated iterative training proofs | 把 local FL training 拆成 piece，证明每个 piece 正确并用 continuity proof 绑定中间状态。 | 需要防止 lazy trainers 伪造 local parameters，同时隐藏 local data/intermediate values。 | Proof 数量和 setup/proving 成本大；fixed-point/Taylor approximation 改变 numeric semantics。 | [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|PZKP-FL]] |

| [[verifiable-aggregation|Verifiable aggregation]] | 证明多方 ML updates/gradients/partial results 按公开规则聚合，典型做法是 commitments + signatures + proof relation。 | Aggregation rule 可形式化，verifier 不应信任 aggregator 或重做完整 witness 检查。 | 不证明 update quality、client honesty、privacy boundary 或 convergence。 | [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | paper | 创建 zkML/verifiable inference seed；展示 LLM inference ZK proof、model parameter hiding、tlookup/zkAttn route 和 13B-scale evaluation | semi-honest verifier; public architecture; committed model only; quantization/approximation; not training provenance | `p1-p16` |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | paper | 补充 CNN verifiable inference seed；展示 FFT/convolution sumcheck、generalized GKR、model-parameter hiding 和 LeNet/VGG/VGG16 evaluation | public architecture; quantized CNN computation; no architecture hiding; prover/memory still costly | `p1-p18` |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | paper | 补充 zkNN inference optimization seed；创建 ZK-friendly ML operators 方法族节点，展示 type-preserving compiler frontend、privacy/tensor-driven optimization、ZENO circuit 和 NN-centric reuse/fusion | inference-only; CPU evaluation; no new proof-system security; privacy type must be specified correctly | `p1-p15` |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | paper | 补充 Halo2/Plonkish ImageNet-scale DNN seed；展示 MobileNet inference proof、lookup nonlinearities、sub-circuit reuse、MLaaS prediction/accuracy/retrieval protocols | quantized/fixed-point DNN semantics; hardware-dependent proving; escrow/sampling assumptions; not training provenance | `p1-p12` |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | paper | 创建 verifiable ML training seed；展示 zkFTP、forest training certification、dataset/model commitments 与低内存 proof backend | tree/forest-specific; deterministic training/seed assumption; quantized histograms; not fairness/generalization/data legality | `p1-p15` |

| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | paper | 创建 verifiable aggregation seed；展示 commitments/signatures/zk-SNARK route for malicious aggregator in FL | aggregator sees local updates; no malicious-client defense; proof generation heavy | `p1-p14` |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | paper | 补强 verifiable training；展示 PZKP-FL for local training computation proof、secure-sum aggregation proof、fixed-point/Taylor numeric adaptation | small ML tasks only; many proofs; trusted setup by publisher; no poisoning defense | `p1-p15` |

## 当前综合

- Evidence window: `2026-06-20` to `2026-06-23`，覆盖当前 vault 已深读 zkCNN、zkLLM、ZENO、trustless DNN inference、Sparrow、zkFL、PZKP-FL、RiseFL。
- Freshness: `fresh` for source-backed seed; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: 当前 zkML 节点仍是 foundation_thin seed，但已覆盖 inference、training 与 aggregation 三类核心 problem，并新增 [[zk-friendly-ml-operators|ZK-friendly ML operators]] 作为方法族。zkCNN 说明 CNN inference proof 的难点在 convolutional layers、quantized CNN semantics、GKR layer composition 和 model-parameter privacy；zkLLM 说明 LLM/transformer route 的瓶颈转向 non-arithmetic ML operators、attention/Softmax、privacy boundary 和 large-model proving；ZENO 说明 zkNN inference proof generation 还需要在 compiler/frontend 层保留 privacy/tensor/layer semantics，否则 circuit generation、constraint generation 和 parallel scheduling 会错过主要优化机会；trustless DNN inference 说明 Halo2/Plonkish custom gates、lookup nonlinearities、fixed-point quantization、sub-circuit reuse 和 commitments 可以把 ImageNet-scale MobileNet inference 接入 MLaaS verification protocols。Sparrow 说明 tree/forest training proof 可以通过 certification algorithm 和低内存 proof backend 承载；PZKP-FL 说明 federated iterative training proof 需要切分训练过程、证明状态连续、处理 fixed-point/non-linear numeric semantics，并把 local training proof 接到 secure-sum aggregation；zkFL 和 RiseFL 说明 aggregation/input-validation proof 的难点在于把多方 updates、commitments、signatures/predicates 和 threat model 绑定清楚。zkCNN、zkLLM、ZENO、trustless DNN inference、zkFTP、PZKP-FL、ZKP-FL、zkFL 和 RiseFL protocol details 都保留为 source 内机制，只有 `verifiable inference`、`verifiable ML training`、`verifiable aggregation` 与 `ZK-friendly ML operators` 作为可复用上层节点落地。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models|zkLLM: Zero Knowledge Proofs for Large Language Models]] | 新增 zkML 方向和 verifiable inference 问题节点；补充 LLM inference proof route | 定义; 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 zkML/zkCNN/ZEN/Mystique/proof-of-training sources 后校准 |
| [[doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy|zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy]] | 补充 CNN inference proof route；把 FFT/convolution sumcheck 与 generalized GKR 纳入 zkML 方法路线 | 背景; 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 ZEN/Mystique/ezDPS 后校准 |
| [[doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference|ZENO: A Type-based Optimization Framework for Zero Knowledge Neural Network Inference]] | 补充 type-preserving zkNN compiler/frontend route；将 ZK-friendly ML operators 从 review candidate 升级为 active_seed 方法族 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; relation graph | yes | 后续吸收 ZEN/Mystique/ezDPS/trustless DNN inference sources 后校准 |
| [[arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs|Scaling up Trustless DNN Inference with Zero-Knowledge Proofs]] | 补充 Halo2/Plonkish ImageNet-scale DNN inference route；把 lookup nonlinearities、sub-circuit reuse 和 MLaaS trust protocols 纳入 zkML 方法路线 | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; relation graph | yes | 后续吸收 ZEN/Mystique/ezDPS/private inference repositories 后校准 |
| [[doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits|Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees]] | 新增 verifiable ML training 问题节点；补充 zkFTP/forest training certification 与低内存 proving route | 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 neural-network proof-of-training / proof-of-learning / proof-of-unlearning sources 后校准 |
| [[doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning|zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning]] | 新增 verifiable aggregation 问题节点；把 zkML 与 ML systems/federated learning integrity 桥接 | 下级结构; 方法族; 代表 Sources; Bridge Links | yes | 后续吸收 RoFL/ACORN/EIFFeL/secure aggregation sources 后校准 |
| [[arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain|Zero-Knowledge Proof-based Practical Federated Learning on Blockchain]] | 补充 federated iterative training proof、secure-sum aggregation verification 与 fixed-point/Taylor numeric route | 背景; 下级结构; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL/secure aggregation/numeric zkML sources 后校准 |
| [[arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp|Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs]] | 补充 non-SNARK secure aggregation input-validation route；把 relaxed SAVI/probabilistic L2 check 挂到 [[verifiable-aggregation|Verifiable aggregation]] | 背景; 方法族; 代表 Sources; 当前综合; Bridge Links | no | 后续吸收 RoFL/ACORN/EIFFeL primary sources |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-zkml-verifiable-inference|zk-SNARKs -> zkML verifiable inference]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-inference` | application, verifiable_computation, privacy, implementation_reuse | Succinctness, soundness and hiding transfer to inference relation; model legality, training provenance and output safety do not. | active_seed |
| [[sum-check-protocol-to-zkml-verifiable-inference|Sum-check protocol -> zkML verifiable inference]] | `verifiable-computation/interactive-proofs/sum-check-protocol; zero-knowledge-proofs/zkml/verifiable-inference` | application, method_transfer, verifiable_computation, operator_proving | Sumcheck/GKR helps prove encoded ML operator relations; commitment, ZK, non-interactivity and numeric semantics require extra components. | active_seed |
| [[memory-efficient-snarks-to-verifiable-ml-training|Memory-efficient SNARKs -> verifiable ML training]] | `zero-knowledge-proofs/proof-systems/memory-efficient-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, scalability_enabler, privacy, implementation_reuse | Low-memory proving transfers to training-certification scalability; model fairness, data legality, accuracy and production governance do not. | active_seed |

| [[zk-snarks-to-zkml-verifiable-aggregation|zk-SNARKs -> zkML verifiable aggregation]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-aggregation` | application, verifiable_computation, integrity, implementation_reuse | Succinct proof and soundness transfer to aggregation relation; FL privacy/robustness do not. | active_seed |
| [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-aggregation; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, verification_transfer | ZKP route solves aggregator correctness subset; system-level FL concerns remain outside proof system. | active_seed |
| [[zk-snarks-to-zkml-verifiable-training|zk-SNARKs -> zkML verifiable training]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/zkml/verifiable-training` | application, verifiable_computation, privacy, training_integrity | Groth16 proof machinery supports training-piece correctness; numeric semantics, proof count and model quality do not transfer. | active_seed |
| [[zkml-verifiable-training-to-federated-learning-integrity|zkML verifiable training -> federated learning integrity]] | `zero-knowledge-proofs/zkml/verifiable-training; ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity` | application, integrity, privacy, cross_domain_mapping | Training proof detects lazy local computation; poisoning, data quality, convergence and production governance remain separate. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-zkml | is_a | nahida-knowledge-zero-knowledge-proofs | vault/04_Knowledge/zero-knowledge-proofs/zkml.md | medium | active_seed |
| nahida-knowledge-zkml | has_child | nahida-knowledge-zkml-verifiable-inference | vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-inference.md | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3670334-zkllm-zero-knowledge-proofs-for-large-language-models.md | source note | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/doi-10-1145-3460120-3485379-zkcnn-zero-knowledge-proofs-for-convolutional-neural-network-predictions-and-accuracy.md | source note | high | active_seed |
| nahida-knowledge-zkml | has_child | nahida-knowledge-zkml-zk-friendly-ml-operators | vault/04_Knowledge/zero-knowledge-proofs/zkml/zk-friendly-ml-operators.md | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/doi-10-1145-3617232-3624852-zeno-type-based-optimization-zk-neural-network-inference.md | source note | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/arxiv-2210-08674-scaling-up-trustless-dnn-inference-zk-proofs.md | source note | high | active_seed |
| nahida-knowledge-zkml | bridges_to | nahida-bridge-sum-check-protocol-to-zkml-verifiable-inference | bridge note | high | active_seed |
| nahida-knowledge-zkml | has_child | nahida-knowledge-zkml-verifiable-training | vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-training.md | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/doi-10-1145-3658644-3690318-sparrow-space-efficient-zksnark-data-parallel-circuits.md | source note | high | active_seed |
| nahida-knowledge-zkml | bridges_to | nahida-bridge-memory-efficient-snarks-to-verifiable-ml-training | bridge note | high | active_seed |

| nahida-knowledge-zkml | has_child | nahida-knowledge-zkml-verifiable-aggregation | vault/04_Knowledge/zero-knowledge-proofs/zkml/verifiable-aggregation.md | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning.md | source note | high | active_seed |
| nahida-knowledge-zkml | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-aggregation | bridge note | high | active_seed |
| nahida-knowledge-zkml | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | bridge note | high | active_seed |
| nahida-knowledge-zkml | evidenced_by | vault/03_Sources/papers/arxiv-2304-05590v2-zero-knowledge-proof-based-practical-federated-learning-on-blockchain.md | source note | high | active_seed |
| nahida-knowledge-zkml | bridges_to | nahida-bridge-zk-snarks-to-zkml-verifiable-training | bridge note | high | active_seed |
| nahida-knowledge-zkml | bridges_to | nahida-bridge-zkml-verifiable-training-to-federated-learning-integrity | bridge note | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| More zkML foundation/prior systems 未吸收。 | 需要比较 zkCNN/zkLLM/ZENO/trustless DNN inference 与 ZEN/Mystique/ezDPS、proof-of-unlearning 等路线，避免少数 source 过拟合。 | nahida-update / nahida-research-search | high | queued |
| More neural-network / federated proof-of-training sources 缺。 | PZKP-FL 补足第一条 federated iterative route，但仍不足以代表全部训练证明。 | nahida-update / nahida-research-search | medium | queued |
| Numeric semantics for ML proofs 未稳定。 | ZKLP 提到 floating-point future work，zkLLM 使用 quantization；二者需要更多 source 才能桥接。 | nahida-update | medium | review |

| Verifiable aggregation sources 仍是单一 seed。 | 需要比较 zkFL 与 secure aggregation、MPC/TEE/other ZK FL routes，避免把 aggregation integrity 等同于 zkFL。 | nahida-update | high | queued |
| Numeric semantics for zkML 仍薄。 | PZKP-FL fixed-point/Taylor、zkLLM quantization、ZKLP floating-point 暂未综合成独立方法节点。 | nahida-knowledge-get / nahida-research-search | medium | review |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zkllm-verifiable-inference | Created zkML direction node from zkLLM source absorption. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-zkcnn-verifiable-inference | Added zkCNN as CNN verifiable inference source and sum-check/GKR operator-proof bridge. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-zeno-verifiable-inference | Added ZENO as type-preserving zkNN inference optimization source and created ZK-friendly ML operators method-family node. | 1 source note | codex |
| 2026-06-23 | nahida-knowledge-20260623-trustless-dnn-inference-zk-proofs | Added trustless DNN inference as Halo2/Plonkish ImageNet-scale zkML source extension and MLaaS verification route. | 1 source note | codex |
| 2026-06-20 | nahida-knowledge-20260620-sparrow-space-efficient-snarks | Added verifiable ML training child node and memory-efficient SNARKs bridge from Sparrow/zkFTP. | 1 source note | codex |

| 2026-06-20 | nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation | Added verifiable aggregation child node and cross-domain FL integrity bridge from zkFL. | 1 source note | codex |
| 2026-06-21 | nahida-knowledge-20260621-pzkp-fl | Added PZKP-FL as federated iterative training proof source extension and bridge evidence. | 1 source note | codex |
