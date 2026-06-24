---
id: "sha256-846f1fed9110-tdml-trustworthy-distributed-machine-learning-framework"
title: "TDML - A Trustworthy Distributed Machine Learning Framework"
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
  - "p1-p11 full extracted text"
  - "Abstract, Sections 1-5, Figures 1-9, Algorithm 1, and References"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "unknown; local PDF says preprint submitted to Elsevier and filename contains FGCS24"
year: "2024"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "trustworthy-distributed-ml"
  - "blockchain-coordinated-training"
  - "distributed-training-integrity"
  - "malicious-node-detection"
  - "large-model-training-systems"
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "trustworthy-distributed-ml"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
secondary_ontology_paths:
  - "blockchain-systems"
  - "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
    - "blockchain-systems"
  directions:
    - "privacy-and-trustworthy-ml"
    - "distributed-training-systems"
  topics:
    - "trustworthy-distributed-ml"
    - "blockchain-coordinated-training"
    - "remote-computing-resource-coordination"
    - "distributed-training-integrity"
domains:
  - "ml-systems"
  - "blockchain-systems"
topics:
  - "trustworthy-distributed-ml"
  - "distributed-machine-learning"
  - "blockchain-coordinated-training"
  - "remote-trainer-validation"
  - "malicious-node-detection"
  - "model-parallelism"
  - "data-parallelism"
aliases:
  - "TDML"
  - "Trustworthy Distributed Machine Learning"
  - "blockchain-based distributed machine learning"
  - "blockchain-coordinated remote trainers"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/ml-systems"
  - "nahida/trustworthy-ml"
direction_facets:
  parent_domain:
    - "ml-systems"
  subdomain:
    - "privacy-and-trustworthy-ml"
  problem:
    - "trustworthy-distributed-ml"
    - "remote-training-integrity"
    - "public-computing-resource-coordination"
  method_family:
    - "blockchain-coordinated-training"
    - "cross-validation-based-malicious-node-detection"
    - "top-k-local-model-aggregation"
    - "pipeline-model-parallelism"
  system_layer:
    - "public-blockchain-job-discovery"
    - "private-blockchain-training-trace"
    - "ipfs-data-batch-reference"
    - "encrypted-rpc-tensor-transfer"
  evaluation_context:
    - "ResNet50 on CIFAR-10"
    - "single GPU vs pipeline parallelism vs FedAvg vs TDML"
    - "zero-gradient, mean-shift, and Gaussian gradient attacks"
  application:
    - "large-model training over public remote computing resources"
  bridge:
    - "blockchain-systems -> ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-tdml-trustworthy-distributed-ml"
source_refs:
  - "sha256:846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> privacy-and-trustworthy-ml"
secondary_directions:
  - "blockchain-systems"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Title, abstract, Sections 1-5, and experiments target distributed ML training over public remote computing resources"
  - "Blockchain is used as coordination, traceability, validation, and incentive infrastructure rather than as a ZK proof system"
  - "No zkML inference or zero-knowledge proof construction appears in the paper body"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/_FGCS24__TDML___Trustworthy_Distributed_Machine_Learning.pdf"
pdf_sha256: "846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921"
pdf_pages: 11
pdf_size_bytes: 7694262
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/tdml-a-trustworthy-distributed-machine-learning-framework-846f1fed9110-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0076"
---

# TDML - A Trustworthy Distributed Machine Learning Framework

## 论文身份

- 标题: TDML - A Trustworthy Distributed Machine Learning Framework
- 作者: Zhen Wang, Qin Wang, Guangsheng Yu, Shiping Chen
- 机构: CSIRO Data61, Australia
- 会议/期刊: unknown；本地 PDF 页脚为 `Preprint submitted to Elsevier`，文件名含 `FGCS24`，但正文未给出可确认 venue。
- 年份: 2024
- DOI: unknown
- arXiv: unknown
- 链接: unknown
- 本地 PDF: `~/Desktop/paper/_FGCS24__TDML___Trustworthy_Distributed_Machine_Learning.pdf`
- SHA-256: `846f1fed9110f9b5b613305aba4d3f7e7bbc7000cd4a453616ba5428d011e921`
- 代码: unknown
- 数据: CIFAR-10 in experiments
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: Codex bundled Python `pypdf`; queue extraction text available.
- 页数: 11
- 已覆盖章节/页码: p1-p11, Abstract, Sections 1-5, Figures 1-9, Algorithm 1, References, author bios.
- 已检查附录: 本地 PDF 未包含附录。
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 抽取文本存在英文单词粘连和少量数学符号/公式格式损失；Figures 2-3/5-9 的视觉曲线只通过 caption 和正文描述读取；无 DOI/arXiv/canonical URL。
- 精读说明: 正文足以支持 `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml` 的 source extension 和一个 blockchain-coordination bridge；不支持把它归为 zkML/verifiable-inference。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | GPU/大模型算力瓶颈；DML/FL 能分摊计算但实践复杂；TDML 用 blockchain 协调 remote trainers、验证 workload、提供 privacy/transparency/training efficiency。 | high | 明确 primary domain 是 ML systems。 |
| §1 / p1-p2 | 动机与贡献 | 大模型训练受 GPU 稀缺影响；现有 DML/FL/model parallelism 依赖 managed environments 或本地边缘数据；BFL 主要聚焦 data parallelism；本文面向 public remote computing resources。 | high | 给出分类纠正证据。 |
| §2.1 / p2-p3 | DNN training parallelism 背景 | 解释 data parallelism、model parallelism、ZeRO/FSDP、FL、tensor/pipeline parallelism、Pippy/Megatron-LM 和 SplitFed。 | medium | 作为 source 内部背景，不单独建立 foundation。 |
| §2.2 / p3 | Blockchain benefits 背景 | 用 blockchain 的 immutability、traceability、smart contracts 作为分布式训练中的数据交换和审计基础；综述 blockchain + FL prior work。 | medium | 作为 bridge 背景。 |
| §3.1 / p4 | Identified challenges | Llama2 70B half precision 例子说明单 batch 可占 150GB GPU memory；列出 manual model adjustment、传输 privacy/security、global model/backprop security、fake computing rewards 四类问题。 | high | 上层问题节点的核心“解决的问题”。 |
| §3.2 / p4-p6 | TDML framework | 三组件: blockchain-based data parallelism, blockchain-based model parallelism, gradient-based malicious node detection。 | high | 核心机制。 |
| §3.2.1 / p4 | Blockchain-based data parallelism | Client 上传 batches 到 IPFS；通过 public chain 发布 job；选择 N parameter servers；private chain 协调；local models 上链；idle PS cross-validate；top-K aggregation。 | high | 可复用的 remote training integrity route。 |
| §3.2.2 / p4-p5 | Blockchain-based model parallelism | Parameter server 发布 trainer hiring request；trainers 注册硬件；PS 按硬件切分 model layers/graph；encrypted shards/RPC；gradients/local params 通过 private chain transaction 交回。 | high | 与 data parallelism 配套。 |
| §3.2.3 / p5-p6 | Task publishing | Client 和 parameter server 在 public/private blockchain 上发布 task metadata、reward budget、baseline computing capability、sharded model list 等。 | medium | 支撑 coordination/incentive 机制。 |
| §3.3.1 / p6-p7 | Gradient-based malicious node detection | 跨验证发现低性能 local model；投影各层 gradients 到低维空间并 K-means 聚类，定位 malicious layer/trainer；Top-K 过滤 attacked models。 | high | 安全机制核心。 |
| §3.3.2 / p7 | Proof of Training | 用 private blockchain 记录 trainer outputs、parameter-server validation results 和 data/activity traces，使训练过程可追溯和可复现。 | high | 注意不是 ZK proof，也不是形式化 proof-of-computation。 |
| §3.3.3 / p7 | Incentive | 训练结束后按 private-chain transaction trace 分配 rewards；认为低成功率/高风险会激励诚实行为。 | medium | game-theoretic 论证较薄。 |
| §4 / p7-p10 | Experiments | ResNet50/CIFAR-10；比较 single GPU、pipeline model parallelism、FedAvg、TDML；评估 convergence/loss/accuracy 和 zero/mean-shift/Gaussian attacks。 | high | 经验性 evidence。 |
| §5 / p9-p10 | Conclusion | TDML 面向 LM public network training；作者声称聚合方法相对 FedAvg accuracy 提升超过 10%，接近 single computing node baseline。 | medium | 总结性主张。 |
| References / p10-p11 | 相关工作 | FL survey, BFL, Pippy, DeepSpeed, Megatron-LM, ZeRO/FSDP, MANDERA 等。 | medium | 后续 foundation/search 线索。 |

## 核心精读笔记

### 背景、动机与问题边界

这篇论文的直接问题不是“如何证明 ML 推理正确”，而是“当训练者和算力来自公共远程资源时，如何组织一个可信的 distributed machine learning training system”。作者的动机来自大模型训练的 GPU 资源稀缺: 大厂大量采购 GPU，较小组织难以承担训练大模型所需的资源。Distributed Machine Learning (DML) 可以把数据或模型分散到多个节点，但实践上会遇到两类障碍: 训练代码/模型并行配置复杂，以及远程节点不可信。

论文把现有路线分成 data parallelism 和 model parallelism。FL 是 data parallelism 的代表，但作者认为它更适合本地 edge data 和 standalone models；ZeRO/FSDP/Pippy/Megatron-LM 等 model-parallel/optimization 框架能缓解 memory pressure，但需要 managed environment 或手工配置。Blockchain-based FL 已用 blockchain 降低单点 aggregator 风险，但作者认为现有研究主要停在 data parallelism，不足以支撑 public remote computing resources 上的大模型训练。

TDML 试图解决四个系统问题:

- Manual model adjustment and maintenance: 分布式训练常要手工 shard layers、parameters、datasets。
- Transmission privacy/security: 模型层、training data、intermediate tensors 和 parameters 会在 public network 中传输，可能被修改、截获或用于推断数据/复制模型。
- Global model/back-propagation integrity: 恶意节点可以扰动 local gradients，误导 global model convergence。
- Rewards on faked computing resources: 恶意节点可能伪造 tensor outputs 或 gradients 以骗取 reward。

证据锚点: Abstract p1; §1 p1-p2; §3.1 p4.

### 模型、假设与定义

TDML 的参与方包括 client、parameter servers、remote trainers、public blockchain service、private blockchain service 和 IPFS file server。

- Client 初始化训练任务，把训练数据打成 batches 并上传到 IPFS，获得 content IDs (CIDs)。
- Public blockchain 用于发布 client job request、parameter server registration、trainer hiring request、hardware specifications 和 reward budget。
- Private blockchain 用于被选中的 parameter servers/trainers 之间的训练过程记录、local model publishing、validation results、gradient/local parameter transaction trace。
- Parameter server 负责为 data parallelism 组织 local training pipeline，也负责在 model parallelism 中选择 trainers、按硬件规格切分 global model layers/structural graph，并聚合 gradients/local models。
- Remote trainers 提供公开远程算力，接受 encrypted model shards，经 encrypted RPC 传递 intermediate tensors，并向 parameter server/private chain 提交 gradients/local parameters。

威胁模型没有形式化到密码学级别，而是围绕 public remote computing nodes 的 Byzantine-style malicious behavior: 修改/截获数据，扰动 gradients，伪造 tensor outputs 或 fake gradients，骗取 reward。论文假设传输可加密，blockchain consensus 可维护交易/状态一致性，test dataset 可用于 cross-validation，且 manipulated gradients 与 benign gradients 在聚类空间中可分离。

证据锚点: §3.1 p4; §3.2.1 p4; §3.2.2 p4-p5; §3.3.1 p6-p7; §3.3.2 p7.

### 方法、协议或系统机制

TDML 由三条机制线组成。

1. Blockchain-based data parallelism:
   - Client 把 datasets packaging into batches 后上传 IPFS，使用 CIDs 引用数据。
   - Client 在 public blockchain 上发布需要 `N` 个 independent parameter servers 的 job request。
   - Parameter servers 在 public chain 注册基本信息，client 选择 N 个并执行 key exchange，然后发送 encrypted private blockchain information。
   - 每个 parameter server 连接 private blockchain，并启动自己的 pipeline model parallelism training workflow。
   - Parameter servers 通过 CIDs 加载 encrypted training data，开始 local model training，并在每个 epoch 将 local model information 上传 private chain。
   - 空闲 parameter server 可作为 validating parameter server，用 test dataset 验证其他 parameter servers 发布的 local models，并把 test results 写入 private chain。
   - 当前 epoch 所有 local models 验证后，validation server 选择 top-K best local models 求平均形成新的 global model。若某些 test results 明显低于均值，则触发 malicious node detection。

2. Blockchain-based model parallelism:
   - 被 client 配置的 parameter server 在 public chain 发布 computing job request。
   - Remote trainers 注册 hardware specifications 和 network details。
   - Parameter server 根据 global model 与候选硬件规格判断需要多少 trainers，选择满足要求的 top-K trainers，执行 key exchange，并发放 encrypted private blockchain information。
   - Parameter server 连接 private chain，根据 trainers 规格自动 split global model layers and structural graph，目标是不修改 original model code。
   - Trainers 进入 private chain，接收 encrypted model shards，初始化对应 layers/weights。
   - Trainer #1 从 IPFS CID 加载 batch，training loop 中各 trainer 的 edge layer 通过 encrypted RPC 向下一 trainer 发送 intermediate output tensors。
   - Epoch 结束后，trainers 加密 local gradients 并通过 private blockchain transactions 发给 parameter server；parameter server 聚合 gradients、计算 loss/local gradients、更新 local model parameters，再将 updated local model 上传 private chain 等待 cross-validation。

3. Task publishing / resource selection:
   - Client task transaction 包含 timestamp、client UUID、task name、reward budget、baseline computing capability 和 data-parallel split number。
   - Parameter server hiring message 包含 timestamp、PS UUID、baseline computing capability、reward budget。
   - Remote candidates 自评硬件满足条件后响应；parameter server 根据模型 layer memory consumption 和硬件规格选择 top-K。
   - 私链任务详情包含 encrypted sharded model list、model structural graph 和 reward。

证据锚点: §3.2.1 p4; §3.2.2 p4-p5; §3.2.3 p5-p6; Eq. 1.

### 安全分析、检测与审计

论文的 malicious node detection 是两阶段:

1. Parameter-server-level cross-validation:
   - Idle parameter server 将待验证 local model 加载到自己的 pipeline，用 test dataset 计算 performance result `H`。
   - 如果某个或少数 local model 的 result 显著低于 majority，就把它们标记为 suspicious/malicious model，并触发 trainer-level detection。

2. Trainer-level gradient clustering:
   - Validation server 在 suspicious local model 之外随机选择 `K` 个 local models。
   - 对每个 layer 的 gradients 投影到低维空间 `R`。
   - 对每层 gradients 做 K-means，寻找 manipulated gradients 与 benign gradients 的分离。
   - 论文用式 (5) 选择最可能 malicious 的 layer，并把 `L_malicious` 映射回对应 remote trainer，最后 block malicious trainer。
   - Top-K local model aggregation 进一步过滤 poor-performing/attacked local models。

作者把 §3.3.2 称为 Proof of Training，但这里的 proof 不是 zero-knowledge proof，也不是 cryptographic proof-of-computation。它的含义是: private blockchain 记录每个 epoch 中 trainer outputs、local parameters、validation results 和相关活动，使训练过程可追溯、可复现，并能支撑 reward settlement。该机制提供 auditability/traceability，而不是在 verifier 不重算训练的情况下证明计算正确。

证据锚点: §3.3.1 p6-p7; Algorithm 1 p7; §3.3.2 p7; §3.3.3 p7.

### 实验、评估或案例

论文用 ResNet50/CIFAR-10 做实验，并非真实大模型训练实验。设置包括:

- Baseline single-node training: local computer with Nvidia A6000 GPU。
- Pipeline model parallelism baseline: 将 ResNet50 layers split into 2, 4, 8 shards，用 PyTorch distributed package 加载到不同 GPU servers。
- FedAvg baseline: 使用 2, 4, 8 个 remote computing nodes/clients。
- TDML: 组合 data parallelism (DP) 和 pipeline model parallelism (MP)。例如 `2 DP + MP, client[2]` 表示 training set 分成两个独立模型，每个模型又被 split 到两个 computing nodes。
- 共同设置: ResNet50, CIFAR-10 fixed split training/test sets, learning rate 0.1。

主要结果:

- Pipeline model parallelism 与 single GPU training 的 accuracy/loss convergence 相近，说明模型切分本身在该设置下没有明显损伤。
- FedAvg 在 CIFAR-10 上 best/real-time accuracy 只到约 83%，低于 pipeline model 和 single GPU model，并且 remote nodes 增多时 loss 更高、收敛更慢。
- TDML 的 testing accuracy 接近 single computing node baseline，作者描述约为 90%；DP 数量增多会降低 convergence performance，8 DP + MP 需要约 100 epochs 达到 90%，其他设置约 75 epochs。
- Top-K aggregation (`K = M/2`) 让 loss curve 比 FedAvg 更平滑；作者在结论中声称 TDML 相比 FedAvg accuracy 提升超过 10%，并匹配 single computing node baseline。
- Malicious node detection 实验覆盖 zero-gradient attack、mean-shift attack 和 Gaussian attack。正文称 Figure 9(a)-(c) 都显示方法能把 malicious trainers 与 benign nodes 分开；Gaussian attack 按 MANDERA 设置 `Sigma = 30 I`。

证据锚点: §4 p7-p10; Figure 5-9; §5 p9-p10.

### 作者结论与我的判断

作者明确声称 TDML 是一个利用 blockchain 协调和验证 remote trainers workload 的 trustworthy DML framework，可实现 privacy、transparency、data traceability，并在 ResNet50/CIFAR-10 上接近 single-node baseline、超过 FedAvg，同时检测 malicious trainers。

由证据支持的判断:

- 论文提供了一个可重用系统路线: 用 public chain 做 job/resource discovery，用 private chain 做 training trace、validation result 和 reward audit，用 IPFS/CIDs 做数据批次引用，用 encrypted RPC 做 pipeline tensor transfer。
- 论文把可信分布式 ML 的问题边界从传统 FL aggregation 扩到“public remote trainers 是否真实、诚实、可验证地完成训练 workload”。
- 论文的实验能说明该机制在 ResNet50/CIFAR-10 原型设置中比 FedAvg 表现更接近 single GPU，并能在构造攻击中分离 malicious gradients。

仍需谨慎的推断:

- 论文没有实测 Llama/GPT 级大模型，也没有量化 blockchain/IPFS/RPC/consensus 的吞吐、延迟、成本和故障恢复。
- Proof of Training 是 trace-based audit，不是 ZK proof；它不能替代 verifiable computation。
- 论文没有形式化 privacy proof；encrypted transmission 与 private-chain trace 不能自动防止梯度泄露、模型反演、数据重识别或 trainer collusion。
- Malicious detection 依赖 test dataset、cross-validation majority 和 manipulated gradients 可聚类分离；对 stealthy poisoning、predicate-passing attack、data-quality attack 或 colluding trainers 的边界不充分。
- Incentive 论证偏直觉，没有完整博弈模型或机制设计证明。

## 层级候选分类

- L1 Domain candidate: `ml-systems`
- L2 Direction candidate: `privacy-and-trustworthy-ml`
- L3 Topic/content cluster candidates: `trustworthy-distributed-ml`, `distributed-training-integrity`, `blockchain-coordinated-training`, `remote-computing-resource-coordination`
- Ontology path: `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml`
- 备选归属:
  - `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity`: secondary/adjacent only, because TDML compares against FedAvg and includes data-parallel aggregation integrity but its core target is broader public remote distributed training.
  - `blockchain-systems`: bridge endpoint, because blockchain is infrastructure method, not the primary research problem.
  - `zero-knowledge-proofs/zkml/verifiable-inference`: rejected; the paper contains no ZK proof construction and no ML inference proof.
- 父级领域: `ML systems`
- 学术子领域: distributed machine learning, trustworthy ML, blockchain-based federated/distributed learning
- 任务/问题: trustworthy training over public remote computing resources
- 方法族: blockchain-coordinated distributed training, cross-validation-based malicious node detection, top-K local model aggregation
- 模型/协议/算法族: data/model/pipeline parallelism, gradient-based malicious node detection, blockchain transaction trace audit
- 评测场景: ResNet50/CIFAR-10, FedAvg comparison, synthetic gradient attacks
- Benchmark/应用: large-model training resource scarcity, remote GPU resource coordination
- 别名: TDML, Trustworthy Distributed Machine Learning
- 相邻方向: blockchain systems, federated learning integrity, distributed systems resource coordination, verifiable computation
- 置信度: high
- 分类理由: 标题、摘要、§3 和 §4 全部围绕 distributed ML training system；blockchain 是协调/审计手段；没有 ZK/zkML inference 内容。
- 分类状态: corrected_from_queue
- 分类证据: Abstract p1; §1 p1-p2; §3.1-§3.3 p4-p7; §4 p7-p10.

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `ml-systems` | 标题、摘要和实验都围绕 distributed ML training framework | high | durable parent candidate / update existing domain |
| Research background | 大模型 GPU 稀缺、DML/FL/model parallelism、public remote computing resources | Abstract; §1; §2 | high | knowledge background/source extension |
| Research problem | Trustworthy distributed ML training over untrusted remote trainers | §3.1 challenges; §3.2 framework | high | create problem node `trustworthy-distributed-ml` |
| Foundation concepts | distributed machine learning, data parallelism, model parallelism, federated learning, blockchain, smart contracts, Byzantine attacks in FL | §2; §3.3 | medium | current run uses concise local background; queue deeper foundation only if repeated |
| Method family | Blockchain-coordinated training + trace-based validation + malicious-gradient detection | §3.2-§3.3 | high | method section/source extension, not standalone method node yet |
| Application/evaluation context | Large-model training using public remote computing resources; ResNet50/CIFAR-10 prototype | §1; §4 | high | problem-node evaluation/application row |
| Artifact/source instance | TDML framework | title; §3 | high | source extension / representative source; do not create a TDML upper concept |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml`
- 它能帮助未来哪些问题少读 source notes:
  - “公共远程 GPU/Trainer 上如何做可信训练?”
  - “blockchain 在 distributed ML 里能提供什么，不能提供什么?”
  - “TDML 和 FedAvg / blockchain-based FL 的区别是什么?”
  - “Proof of Training 和 ZK proof of training 是不是一回事?”
  - “分布式训练里如何检测 malicious trainer?”
- 哪些内容应留在 source note，而不是创建上层节点:
  - TDML 的 10-step/8-step workflow、Algorithm 1 细节、ResNet50/CIFAR-10 具体结果、Equation 1-5、Figures 5-9 的原型结果。
- 哪些上层节点过薄、缺失或需要 foundation_pack:
  - `trustworthy-distributed-ml` 是新 problem seed，需要更多 remote training, blockchain FL, robust distributed training sources。
  - `distributed-systems/resource-marketplace` 或 `decentralized-computing` 目前不是已建节点，先放 expansion candidate。
- 哪些候选只是别名/query key/watch term:
  - `TDML`, `proof of training`, `blockchain-based distributed training`, `remote trainer validation`, `public remote computing resources`.

## 一句话贡献

TDML 把 public remote computing resources 上的大模型/分布式训练问题，组织成 blockchain-coordinated data/model parallelism + cross-validation + malicious-gradient detection + reward trace 的可信训练框架。

## 问题设定

用户/Client 想训练大模型，但缺少足够 GPU 或托管环境资源，只能使用公共远程算力。远程 trainers 可能不可信: 可能截获/篡改数据、伪造 tensor outputs、提交恶意 gradients 或骗取 reward。系统需要在不完全信任 trainers/parameter servers 的情况下协调任务、验证训练进展、追踪责任和分配奖励。

## 方法概览

### 组成部分

- Public blockchain: 发布 job request、parameter-server registration、trainer hiring and hardware-spec transactions。
- Private blockchain: 记录 selected participants 的 training trace、local model updates、validation results、gradients/local parameter transactions、reward evidence。
- IPFS file server: 存储训练 batch，返回 CIDs。
- Parameter servers: data-parallel pipelines 的 local training coordinator；model-parallel trainers 的选择、模型切分、gradient aggregation 和 validation actor。
- Remote trainers: 承载 model shards，执行 pipeline layer computation，向 parameter server 提交 gradients/local parameters。
- Cross-validation server: 空闲 parameter server 验证其他 local models，并触发 malicious detection。

### 流程或协议

TDML 的高层流程是:

1. Client 把数据批次上传 IPFS 并在 public chain 发布训练任务。
2. Parameter servers 和 trainers 用 public chain 注册/竞标。
3. Client/parameter server 选择满足条件的节点，发送 private-chain access information。
4. Parameter server 按硬件能力拆分模型，将 encrypted model shards 发给 trainers。
5. Trainers 经 encrypted RPC 串联 pipeline，执行 forward/backward，并提交 gradients/local parameters。
6. Parameter servers 每个 epoch 发布 local model 到 private chain。
7. Idle parameter server 用 test dataset cross-validate local models。
8. 系统 top-K 聚合 best local models；低性能 outlier 触发 gradient clustering 以定位 malicious trainers。
9. Training trace 和 validation transactions 支撑 reward settlement。

### 关键定义、公式、算法或定理

- Eq. 1: 按 layer weights 和 bytes per parameter 估算每层 memory consumption，用于根据 trainers hardware specs 切分模型。
- Eq. 2-4: 描述 trainer local layer computation、back-propagation local gradient 和 global model update。
- Eq. 5 / Algorithm 1: 对 suspicious model 的 layer gradients 投影、聚类，选择最可能的 malicious layer，再映射到 malicious trainer。
- Proof of Training: private blockchain trace + validation results 的可追溯性机制，不是形式化 cryptographic proof。

### 假设条件

- 公链/私链服务可用，且 consensus 能保证交易记录的一致性和不可篡改性。
- Client/parameter server 能通过加密信道交换 private-chain information。
- IPFS/CID 能稳定引用训练 batch。
- Validation test dataset 能代表模型质量，并能发现 attacked local models。
- Manipulated gradients 在投影/聚类空间中足够区别于 benign gradients。
- Top-K local model aggregation 足以过滤 poor/malicious local models。
- Remote trainers 响应的 hardware specs 和网络 details 至少可用于初筛；论文没有完整解决硬件真实性证明。

## 创新点

- 新思想: 将 blockchain 从“FL aggregation audit”扩到 public remote distributed training 的任务协调、训练记录、validation trace 和 reward settlement 层。
- 对已有工作的扩展: 现有 BFL 多聚焦 data parallelism 和本地 edge/federated data；TDML 同时覆盖 data parallelism 和 model/pipeline parallelism。
- 工程或实证贡献: 用 ResNet50/CIFAR-10 原型对比 single GPU、pipeline parallelism、FedAvg 与 TDML，并展示恶意梯度攻击检测。
- 依赖的 prior work: FL, BFL, Pippy, Megatron-LM, ZeRO/FSDP, SplitFed, MANDERA malicious node detection。

## 实验与结果

### 实验设置

- Model: ResNet50
- Dataset: CIFAR-10
- GPU: local Nvidia A6000 for single-node baseline
- Distributed implementation: PyTorch distributed package for model shards
- Learning rate: 0.1
- Remote computing node counts: 2, 4, 8
- Compared techniques: single GPU, pipeline model parallelism, FedAvg, TDML DP+MP

### Baseline

- Single-node training: local A6000 GPU baseline。
- Pipeline model parallelism: ResNet50 layers split into 2/4/8 shards。
- FedAvg: 2/4/8 remote clients。

### 指标

- Testing accuracy
- Training loss
- Convergence speed
- Malicious/benign trainer separation under constructed attacks

### 主要结果

- Pipeline model parallelism 接近 single GPU accuracy/loss convergence。
- FedAvg accuracy 约 83%，低于 single GPU 和 pipeline model baseline。
- TDML accuracy 约 90%，接近 single computing node；作者声称相比 FedAvg accuracy over 10% improvement。
- DP 数量越多，收敛越慢；8 DP + MP 约 100 epochs 到 90%，较小 DP 设置约 75 epochs。
- Top-K aggregation 使 TDML loss curve 比 FedAvg 更平滑。
- Zero-gradient、mean-shift 和 Gaussian attacks 在 Figure 9 中都被正文描述为可与 benign nodes 分离。

### 结果 caveat

- 实验不是大模型；ResNet50/CIFAR-10 只能证明原型趋势。
- 没有真实 public blockchain/private blockchain deployment cost。
- 没有端到端测量 IPFS、encrypted RPC、chain finality、trainer churn、fault recovery。
- Attack evaluation 是构造场景，不覆盖所有 stealthy poisoning 或 collusion。

## 局限性

### 作者明确说明或正文暴露

- Blockchain-based FL 仍缺 practical DML guidance，TDML 是一个 proposed framework；正文没有给出生产系统实现细节。
- 大模型训练动机用 Llama2 70B 举例，但实验使用 ResNet50/CIFAR-10。
- DP 增多会拖慢 convergence；8 DP + MP 明显慢于较小 DP。

### 基于证据的推断

- 没有形式化 security theorem，也没有 privacy leakage 定量评估。
- “Proof of Training” 是 traceability/reproducibility 论证，不是 cryptographic proof。
- Reward/incentive mechanism 需要更强的 game-theoretic 或 mechanism-design 分析。
- Hardware specs、trainer identity、remote environment integrity 没有用 TEE/attestation/ZKP 等方式证明。
- Private blockchain 的节点集合、consensus、访问控制、数据可见性与隐私边界没有展开。

## 可复用思路

- 把“远程训练节点可信性”拆成 discovery/selection、data/model transfer integrity、local computation trace、cross-validation、aggregation filtering、reward settlement 六个子问题。
- 用 public chain 做开放招募与元数据发布，用 private chain 做一次训练任务内的 audit trail。
- 将 test-dataset cross-validation 和 gradient clustering 结合: 先从模型级 performance outlier 缩小范围，再从 layer-level gradients 定位 malicious trainer。
- 对上层知识库而言，TDML 是 trustworthy distributed ML 的代表 source，不应作为基础概念独立提升。

## 术语表

| Term | 解释 |
| --- | --- |
| TDML | 本文提出的 Trustworthy Distributed Machine Learning framework。 |
| Parameter server | 协调 local model/pipeline/trainer 的服务器，负责模型切分、gradient aggregation、validation 等。 |
| Remote trainer | 提供公开远程算力的训练节点，承载 model shard 并提交 gradients/local parameters。 |
| Public blockchain | 用于 job/resource discovery、registration、hiring request 和 reward budget 的公开协调层。 |
| Private blockchain | 用于一次训练任务内部的 trace、validation result、local model 和 reward evidence 的任务链。 |
| Proof of Training | 本文的训练过程可追溯/可复现记录，不是 ZK proof。 |
| Top-K aggregation | 选择 top-K best local models 进行平均，以过滤 poor-performing/malicious local models。 |

## 连接

- 相关论文: BlockFL, LDP-Fed, ShareChain, BC-FL, MANDERA, Pippy, Megatron-LM, ZeRO/FSDP, SplitFed.
- 相关仓库: Pippy (`https://github.com/pytorch/PiPPy`) 作为论文引用的 pipeline parallelism tool；本次未打开外部仓库。
- 相关 Knowledge nodes:
  - [[ml-systems|ML systems]]
  - [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]
  - [[trustworthy-distributed-ml|Trustworthy distributed ML]]
  - [[federated-learning-integrity|Federated learning integrity]]
  - [[blockchain-systems|Blockchain systems]]
- 相关 Bridges:
  - [[blockchain-coordination-to-trustworthy-distributed-ml|Blockchain coordination -> trustworthy distributed ML]]
- Bridge 候选:
  - Endpoint paths: `blockchain-systems`; `ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml`
  - Relation types: `application`, `auditability`, `coordination`, `incentive`
  - Relationship thesis: blockchain can coordinate remote participants and record training/validation traces for trustworthy distributed ML, but it does not by itself prove ML computation, privacy, convergence, or trainer honesty.
  - Transfer boundary: consensus/audit trace transfers; model quality, stealthy poisoning resistance, hardware attestation, privacy proof and training correctness do not transfer automatically.

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| trustworthy-distributed-ml | problem node | TDML §3.1-§3.3 defines reusable public remote training trust problem | active_seed | create/update knowledge node |
| blockchain-coordinated-training | method family candidate | TDML combines public/private chain, IPFS, validation, reward trace | candidate | keep as method route until more sources |
| remote-computing-resource-marketplace | adjacent topic | public remote trainers, reward budget, hardware specs | review | queue only; TDML evidence too narrow |
| proof-of-training | watch term | TDML §3.3.2 uses trace-based training record | watch | distinguish from ZK proof-of-training |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| TDML 主问题是可信分布式 ML 训练，而非 zkML inference | classification | Abstract; §1; §3; §4 | 摘要和实验均围绕 distributed training framework | high | 队列路径需纠正 |
| Blockchain 在 TDML 中主要承担 coordination/audit/incentive role | source_claim | §2.2; §3.2; §3.3.2 | public/private chain workflows and transaction traces | high | 不等于计算正确性证明 |
| TDML 同时覆盖 data parallelism 和 model parallelism | source_claim | §3.2.1-§3.2.2 | independent pipelines + pipeline model splitting | high | 与传统 BFL 区分 |
| Malicious detection 使用 cross-validation + layer-gradient clustering | source_claim | §3.3.1; Algorithm 1 | suspicious model -> gradient projection/K-means -> malicious trainer | high | 依赖可分离性 |
| ResNet50/CIFAR-10 中 TDML 接近 single-node accuracy 且高于 FedAvg | source_claim | §4.1-§4.3; Figure 5-8; §5 | FedAvg ~83%; TDML ~90%; author claims >10% over FedAvg | medium | 图中数值需要视觉复核 |
| 构造攻击中 malicious trainers 可分离 | source_claim | §4.4; Figure 9 | zero-gradient, mean-shift, Gaussian attacks | medium | 主要依赖图示和作者描述 |

## 知识交接

- 留在本文元笔记的证据: TDML workflow steps, equations, algorithm details, ResNet50/CIFAR-10 results, specific attacks and figures.
- 待更新 Knowledge node:
  - `vault/04_Knowledge/ml-systems.md`
  - `vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md`
  - `vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/trustworthy-distributed-ml.md`
  - `vault/04_Knowledge/ml-systems/research-dynamics.md`
  - `vault/04_Knowledge/blockchain-systems.md`
- 作为哪些 Knowledge node 的 source extension:
  - ML systems
  - Privacy and trustworthy ML
  - Trustworthy distributed ML
  - Blockchain systems as bridge evidence
- 需要补的 foundation knowledge/source:
  - distributed machine learning foundation
  - blockchain-based federated learning survey/foundation
  - decentralized compute/resource marketplace
  - robust distributed training / Byzantine-resilient ML
- 待新增或复核 domain/direction/problem:
  - `trustworthy-distributed-ml` should be an active seed problem.
  - `blockchain-coordinated-training` should remain a method route, not a standalone node yet.
- Bridge 候选: `blockchain-coordination-to-trustworthy-distributed-ml`
- Watchlist 词条: TDML, proof of training, blockchain-based distributed training, remote trainer validation, public remote computing resources.
- 后续论文: MANDERA, BlockFL, IronForge, BFL surveys, robust distributed learning sources.
- 后续仓库: Pippy, DeepSpeed, Megatron-LM if user wants implementation evidence.
- Review queue:
  - Venue/canonical URL unknown.
  - Filename suggests FGCS24 but PDF does not confirm final venue.
  - Figures were not visually measured; numeric results rely on text descriptions.
  - Queue classification corrected from `zero-knowledge-proofs/zkml/verifiable-inference`.

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Distributed machine learning | foundation_knowledge_candidate | 作为 ML systems 基础背景，必要时补 foundation note | 让 TDML 成为 DML 的唯一解释 | §1-§2 |
| Federated learning | foundation/adjacent problem | 保留在 privacy/trustworthy ML 与 FL integrity 相关节点；TDML 是相邻 source | 把 TDML 简化成 FL 论文 | §2.1, §4.2 |
| Blockchain coordination | method_family_candidate | 作为 trustworthy distributed ML 的方法路线和 bridge | 建一个只有 TDML 的基础概念 | §2.2, §3.2 |
| TDML | source instance | 作为代表 source extension | 当成上层基础概念或方向 | Title, §3 |
| Proof of Training | watch term/source-specific mechanism | 在 source/knowledge 中解释为 trace-based audit | 误归为 ZK proof/verifiable computation | §3.3.2 |

## Knowledge 综合交接

- 应创建 Knowledge node: `trustworthy-distributed-ml`
- 应刷新 Knowledge synthesis section: `ML systems`, `Privacy and trustworthy ML`, `ML systems Research Dynamics`
- 应标记过期: none
- 无需更新的理由: `federated-learning-integrity` 可暂不重写，TDML 与 FL integrity 相邻但不是 narrow FL aggregation/integrity source。
- 建议 node kind: `problem`

## 处理日志

| Date | Run ID | Action |
| --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-tdml-trustworthy-distributed-ml | Deep-read exact pending PDF, corrected queue classification, prepared Source + Knowledge + Bridge handoff. |
