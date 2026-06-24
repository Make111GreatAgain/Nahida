---
id: "doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning"
title: "zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning"
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
  - "p1-p14 full extracted text"
  - "Abstract, Sections I-VII, tables, figures, references, and author-version caveats"
canonical_url: "https://doi.org/10.1109/TBDATA.2024.3403370"
doi: "10.1109/TBDATA.2024.3403370"
arxiv_id: ""
venue: "IEEE Transactions on Big Data"
year: "2024"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "federated-learning-integrity"
  - "verifiable-federated-aggregation"
  - "zkml"
  - "blockchain-based-verification"
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "federated-learning-integrity"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-aggregation"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "zero-knowledge-proofs/applications/blockchain-applications"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
    - "zero-knowledge-proofs"
    - "blockchain-systems"
  directions:
    - "privacy-and-trustworthy-ml"
    - "zkml"
    - "applications"
  topics:
    - "federated-learning-integrity"
    - "verifiable-federated-aggregation"
    - "blockchain-based-verification"
domains:
  - "ml-systems"
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "federated-learning"
  - "federated-learning-integrity"
  - "verifiable-aggregation"
  - "zkml"
  - "zk-snarks"
  - "blockchain-verification"
aliases:
  - "zkFL"
  - "Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning"
  - "verifiable federated aggregation"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/ml-systems"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "ml-systems"
    - "zero-knowledge-proofs"
  subdomain:
    - "privacy-and-trustworthy-ml"
    - "zkml"
  problem:
    - "malicious aggregator in federated learning"
    - "verifiable gradient aggregation"
    - "outsourced aggregation verification"
  method_family:
    - "Pedersen commitments"
    - "digital signatures"
    - "zk-SNARK aggregation proof"
    - "blockchain-based proof verification"
  system_layer:
    - "federated learning protocol"
    - "proof system application"
    - "blockchain verification layer"
  evaluation_context:
    - "FedAvg"
    - "CIFAR-10 image classification"
    - "PTB language modeling"
    - "ResNet, DenseNet, and LSTM models"
  bridge:
    - "zk-snarks-to-zkml-verifiable-aggregation"
    - "zkml-verifiable-aggregation-to-federated-learning-integrity"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zkfl-verifiable-federated-aggregation"
source_refs:
  - "doi:10.1109/TBDATA.2024.3403370"
  - "sha256:2938d2d14b22c5458468332c5115955bdc4f406e9f30f5617bd192187df21927"
confidence: "high"
trust_tier: "primary"
primary_direction: "privacy-and-trustworthy-ml"
secondary_directions:
  - "zkml"
  - "blockchain-applications"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The paper's problem statement targets malicious aggregation in federated learning, not ML inference proving."
  - "The protocol proves that the aggregate update equals the sum of signed client updates and that each commitment opens correctly."
  - "The blockchain variant outsources proof verification and stores a hash of the encrypted aggregate, without on-chain aggregation."
  - "Queue path zero-knowledge-proofs/zkml/verifiable-inference is a useful ZKP-side application hint but not the paper's primary problem layer."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0032"
local_pdf: "~/Desktop/paper/zkFL_Zero-Knowledge_Proof-based_Gradient_Aggregation_for_Federated_Learning.pdf"
pdf_sha256: "2938d2d14b22c5458468332c5115955bdc4f406e9f30f5617bd192187df21927"
extracted_text_path: "vault/02_Raw/pdf/extracted/monospace-zkfl-monospace-zero-knowledge-proof-based-gradient-aggregation-for-federated-learning-2938d2d14b22-pages.txt"
---

# zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning

## 论文身份

- 标题: zkFL: Zero-Knowledge Proof-based Gradient Aggregation for Federated Learning
- 作者: Zhipeng Wang, Nanqing Dong, Jiahao Sun, William Knottenbelt, Yike Guo
- 机构: Imperial College London; University of Oxford; Shanghai AI Laboratory; FLock.io; Hong Kong University of Science and Technology
- 会议/期刊: IEEE Transactions on Big Data
- 年份: 2024
- DOI: 10.1109/TBDATA.2024.3403370
- 链接: https://doi.org/10.1109/TBDATA.2024.3403370
- 本地 PDF: `~/Desktop/paper/zkFL_Zero-Knowledge_Proof-based_Gradient_Aggregation_for_Federated_Learning.pdf`
- License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License
- 备注: 本地 PDF 是 accepted author version。页眉仍有 `MONTH 2020` 占位符，年份以 DOI/venue metadata 的 2024 为准。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 页数: 14
- 已覆盖章节/页码: Abstract, I Introduction, II Related Work, III Preliminaries, IV zkFL protocol, V Analysis, VI Experiments and Evaluation, VII Conclusion, references and tables.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 图表文本抽取可读但排版有噪声；Table I 中个别符号与正文叙述存在歧义；PyTorch 版本和 ResNet50 通信量数字存在论文内不一致。
- 精读说明: 队列把本论文 staged 到 `zero-knowledge-proofs/zkml/verifiable-inference`。深读后纠正为 `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity`，因为主问题是 malicious aggregator 操纵 federated learning 聚合，而不是证明一次模型 inference。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题和方案 | 用 ZKP 防止 federated learning aggregator 作恶；给出 blockchain-based zkFL | high | 主分类依据 |
| §I / p1-p3 | 动机和威胁模型 | Aggregator 可抛弃、替换、插入 client updates；clients 需要验证聚合正确性 | high | 问题域证据 |
| §II / p3-p4 | Related work | RoFL/RiseFL/PZKP-FL 等多数关注 malicious clients 或 on-chain aggregation | medium | novelty boundary |
| §III / p4-p5 | Preliminaries | Hash, Pedersen commitments, zk-SNARK algorithms | medium | 方法依赖 |
| §IV / p5-p7 | Protocol | Setup, client commitment/signature, aggregator proof, client/miner verification | high | 核心机制 |
| §V / p7-p8 | Analysis | Completeness, security, privacy, efficiency | high | threat boundary |
| §VI / p8-p13 | Evaluation | FedAvg on CIFAR-10/PTB; ResNet/DenseNet/LSTM; Halo2; communication/gas | high | 实验和代价 |
| §VII / p13 | Discussion | Decentralized storage, recursive ZKPs, power consumption | medium | future work |

## 核心精读笔记

> 这篇论文的主线是: 在 federated learning 中，central aggregator 可能伪造或篡改梯度/模型更新；zkFL 用 commitment、signature 和 zk-SNARK 证明聚合结果确实来自全部合法 client updates，并用 blockchain 版本把验证工作交给 miners 而不是让每个 client 自行验证。

### 问题、动机与边界

Federated learning 让 clients 在本地训练模型，central aggregator 周期性收集 local updates 并计算 global update。论文关注的失效点不是 client privacy，而是 aggregator integrity:

- aggregator 可以丢弃 honest client 的 update，使聚合结果偏离真实 FedAvg/FedSum。
- aggregator 可以用 fake update 替换某个 client update。
- aggregator 可以插入 fake clients 或 fake updates。
- clients 如果只接收 aggregator 返回的 aggregated model，很难独立确认聚合是否包含了正确的 signed updates。

因此 zkFL 的 durable problem 不是“ZK inference”，而是“federated learning aggregation integrity”。ZK 只是解决路线之一。

边界需要保留:

- zkFL 不解决 malicious clients / model poisoning；related work 中 RoFL、RiseFL 等更偏 client-side 问题。
- base zkFL 中 aggregator 接收 plaintext local update `w_i` 和 randomness `s_i`；论文把 aggregator model inversion 作为 future work，而不是已解决隐私问题。
- blockchain-based zkFL 让 miners 验证 proof 和 hash/commitment，但不在链上执行 aggregation。
- proof generation 对大模型很重，论文报告的 ResNet50 proof generation 约 54.72 分钟，不能把它误读为低成本 production-ready route。

### 协议对象和密码学组件

zkFL 使用三类对象:

- Pedersen commitment: `Enc(w_i)=g^{w_i} h^{s_i}`。论文称为 encrypted model update，但机制上是 commitment-style binding/hiding 对象。
- Client signature: 每个 client 对 encrypted update 签名，防止 aggregator 替换 statement 中的 update。
- zk-SNARK proof: aggregator 证明 witness 中的 updates/randomness/aggregate 满足 commitment、signature 和 sum relation。

证明关系可概括为:

1. 对每个 client `i`，`Enc(w_i)` 是 `w_i, s_i` 的合法 commitment。
2. 每个 `Enc(w_i)` 携带 client `i` 的有效 signature。
3. 聚合结果 `w` 等于所有 client updates 的求和。
4. 公开的 `Enc(w)` 与聚合结果一致。

这让 verifier 不必看到全部 witness 细节即可拒绝错误聚合，但 statement/witness 的隐私边界要按论文设置理解。

### Base zkFL protocol

Protocol flow:

1. Setup: `N` clients 和 aggregator 生成 key pairs；通过 PKI 分发公钥。
2. Local training: client 在本地数据上训练，得到 model update `w_i`。
3. Commitment and signature: client 随机选 `s_i`，计算 `Enc(w_i)=g^{w_i}h^{s_i}`，再对 encrypted update 签名。
4. Submission: client 把 `w_i, s_i, Enc(w_i), sig_i` 发送给 aggregator。
5. Aggregation and proving: aggregator 计算 `w=sum_i w_i` 和 `Enc(w)=prod_i Enc(w_i)`，生成 zk-SNARK proof `pi`，证明每个 signed commitment 和求和关系正确。
6. Verification: aggregator 把 `w, Enc(w), pi` 发回 clients；clients verify proof，只有验证通过才使用 `w` 继续下一轮训练。

这条路线把 trust in aggregator 改成 proof verification。它仍假设 clients 接收到的是同一个 statement/proof，并且 proof circuit 正确编码了 commitment、signature 和 sum relation。

### Blockchain-based zkFL

Blockchain-based zkFL 的目标不是“把模型聚合搬到链上”，而是把 proof verification 和公开可审计记录移给 miners:

1. 从 `N` 个 clients 中通过 VRF 选出本轮 `n` 个 participants。
2. Clients 训练、commit、sign 后把数据发给 aggregator。
3. Aggregator 计算 aggregate 并生成 proof。
4. Aggregator 把 `w, Enc(w)` 发给 clients，同时把 `pi, Enc(w)` 广播给 miners。
5. Miners verify proof；若通过，把 `H(Enc(w))` 写入 blockchain。
6. 下一轮被选中的 clients 检查链上 hash 是否匹配当前 aggregate，再继续训练。

论文把该版本的主要收益表述为:

- clients 不再承担 per-round ZKP verification。
- miners 只能看到 encrypted/committed updates、aggregate commitment 和 proof，不看到 plaintext local/global updates。
- 链上只存 `H(Enc(w))`，因此避免 on-chain aggregation 的 `O(n*m)` computation 和 `O(m)` storage。

### Security and privacy analysis

论文证明/论证覆盖三类 aggregator 攻击:

- abandoned update: aggregator 把某个合法 update 排除在求和之外。
- replaced update: aggregator 用 fake update 替换某个 signed client update。
- inserted update: aggregator 加入 fake client/update。

在上述情况下，sum relation、commitment opening 或 signature check 会失败，因此 proof 无法通过。该论证依赖 zk-SNARK soundness、signature unforgeability、commitment binding 和正确 circuit。

Privacy claim 需要窄读:

- base zkFL: aggregated updates 只在 aggregator 和 clients 内部流动，但 aggregator 已经收到 local updates。
- blockchain-based zkFL: miners 验证 encrypted/committed values 与 proof，不获得 plaintext local/global updates。
- 论文明确把 aggregator model inversion attack 留作 future work。

### 实验设置与结果

Implementation:

- Rust prototype with Python/PyTorch interface。
- Curve25519 dalek, 126-bit security。
- Pedersen commitments over elliptic curves。
- Halo2 as ZKP system。
- NVIDIA Tesla T4 GPU with 16GB memory。
- 文中同时出现 PyTorch 1.13 和 PyTorch 1.10.1，应保留为论文内版本不一致。

Evaluation workloads:

- CIFAR-10 image classification，FedAvg，Adam learning rate 0.001，batch size 50，10% validation split per client。
- Models: ResNet18/34/50, DenseNet121/169/201。
- PTB language modeling，LSTM 1/2/3 layers，650 neurons per layer，Adam learning rate 0.001，batch size 20，dropout 0.5。
- Clients: 1, 4, 8, 16, 32。

Key results:

- zkFL 不改变 underlying training process，因此 per-epoch accuracy/perplexity trend 与 FL 相同；convergence speed 主要由 client count 影响。
- Local training 仍是 conventional FL 的主要 per-epoch 时间；zkFL 额外增加 commitment/encryption、proof generation 和 verification。
- Encryption/commitment communication grows with model parameter count；table 中 ResNet50 plaintext/encrypted 各 497MB，proof 628KB。
- Halo2 proof generation/verification time 随参数规模增长；ResNet50 proof generation 约 `54.72 +/- 0.12 mins`，verification roughly half of generation time。
- Blockchain-based zkFL 可减少单个 client running time，因为 client 不再做 proof verification；但 blockchain finality 会引入 wall-clock delay。论文例子写 Bitcoin 约 6 blocks/1 hour，Ethereum 约 15 minutes。
- Gas example: 1MB model update on Ethereum full storage 约 625M gas；只存 SHA-256 hash 约 20,000 gas。

数字 caveats:

- Table II 写 ResNet50 plaintext/encrypted 是 497MB，但正文通信例子写 491MB + 491MB + 628KB = 982.61MB。知识节点采用 table value，同时保留不一致。
- Finality 数字反映论文写作时的简化假设，不应作为当前链参数事实。

### 贡献与局限

主要贡献:

- 把 malicious aggregator integrity 明确作为 federated learning 中的 verification problem。
- 用 commitments + signatures + zk-SNARK relation 把 aggregation correctness 转成可验证 statement。
- 给出 blockchain-based verification variant，避免把 large model aggregation 上链。
- 在 CNN/LSTM/FedAvg benchmark 上量化 proof/communication/gas tradeoff。

主要局限:

- 不处理 malicious clients 和 poisoned updates。
- 不处理 aggregator 对 plaintext local updates 的 model inversion。
- Proof generation 对大模型非常重，且 communication 需要传输 plaintext/commitment-sized data。
- Blockchain version 依赖链 finality、miner verification、hash anchoring 和 off-chain data availability。
- Evaluation 是 prototype/benchmark evidence，不是生产系统证据。

## 分层吸收判断

| 层级 | 结论 | 原因 | 写入位置 |
| --- | --- | --- | --- |
| Source | 创建独立 paper source note | 论文细节、协议、实验和 caveats 应完整留在底层 | 本文件 |
| Knowledge/domain | 新建 `ml-systems` | 当前 vault 没有 ML systems 主干，zkFL 的主问题属于 FL/ML system integrity | [[ml-systems|ML systems]] |
| Knowledge/direction | 新建 `privacy-and-trustworthy-ml` | 需要组织 privacy、trust、auditability、integrity 等 ML 系统问题 | [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] |
| Knowledge/problem | 新建 `federated-learning-integrity` | 恶意 aggregator 是可复用问题域，不是 zkFL 专属名称 | [[federated-learning-integrity|Federated learning integrity]] |
| Knowledge/ZKP side | 新建 `verifiable-aggregation` | 在 zkML 侧作为 ZK proof application route，区别于 inference/training | [[verifiable-aggregation|Verifiable aggregation]] |
| Bridge | 新建 two bridges | 连接 proof-system capability、zkML application route、ML systems problem | [[zk-snarks-to-zkml-verifiable-aggregation|zk-SNARKs -> zkML verifiable aggregation]]; [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning | evidences | nahida-knowledge-federated-learning-integrity | zkFL §I-§V | high | active_seed |
| doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning | evidences | nahida-knowledge-zkml-verifiable-aggregation | zkFL §III-§VI | high | active_seed |
| doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning | uses | nahida-knowledge-zk-snarks | zkFL §III-§VI, Halo2 evaluation | medium | source_extension |
| doi-10-1109-tbdata-2024-3403370-zkfl-zero-knowledge-gradient-aggregation-federated-learning | extends | nahida-knowledge-zkp-blockchain-applications | blockchain-based zkFL | medium | source_extension |

## 后续复核

| Gap | Why it matters | Suggested action |
| --- | --- | --- |
| PZKP-FL / RoFL / RiseFL 等相关 FL/ZKP sources 未吸收 | 需要区分 malicious client、malicious aggregator、privacy-preserving FL 和 blockchain FL 的边界 | 继续 serial queue 或 `nahida-research-search` |
| Aggregator privacy/model inversion 未解决 | zkFL 的 privacy claim 容易被过宽理解 | 后续吸收 secure aggregation / DP-FL / TEEs / MPC-FL sources |
| Blockchain finality/current gas facts 未联网更新 | 论文数字是 source evidence，不是当前链参数 | 只有用户请求 freshness 时用 `nahida-daily-fetch` 或 web |

