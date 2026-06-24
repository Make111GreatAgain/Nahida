---
id: "arxiv-2304.05590v2"
title: "Zero-Knowledge Proof-based Practical Federated Learning on Blockchain"
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
  - "p1-p15 full extracted text"
  - "Abstract, Sections 1-9, algorithms, theorems, tables, figures, references and author bios"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2304.05590"
doi: ""
arxiv_id: "2304.05590v2"
venue: "arXiv preprint"
year: "2023"
hierarchy_level: "source"
domain_id: "zero-knowledge-proofs"
direction_id: "zkml"
topic_ids:
  - "verifiable-ml-training"
  - "verifiable-aggregation"
  - "federated-learning-integrity"
  - "blockchain-based-verification"
ontology_path:
  - "zero-knowledge-proofs"
  - "zkml"
  - "verifiable-training"
primary_ontology_path: "zero-knowledge-proofs/zkml/verifiable-training"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-aggregation"
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
  - "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
  - "blockchain-systems/execution-and-transactions"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "zero-knowledge-proofs"
    - "ml-systems"
    - "blockchain-systems"
  directions:
    - "zkml"
    - "privacy-and-trustworthy-ml"
    - "execution-and-transactions"
  topics:
    - "verifiable-ml-training"
    - "verifiable-aggregation"
    - "federated-learning-integrity"
    - "blockchain-based-verification"
domains:
  - "zero-knowledge-proofs"
  - "ml-systems"
  - "blockchain-systems"
topics:
  - "zkml"
  - "verifiable-ml-training"
  - "verifiable-aggregation"
  - "federated-learning"
  - "federated-learning-integrity"
  - "zk-snarks"
  - "groth16"
  - "sigma-protocol"
  - "secure-sum"
  - "blockchain-verification"
aliases:
  - "ZKP-FL"
  - "PZKP-FL"
  - "Practical ZKP-FL"
  - "Zero-Knowledge Proof-based Federated Learning"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/zkp"
  - "nahida/zkml"
  - "nahida/ml-systems"
direction_facets:
  parent_domain:
    - "zero-knowledge-proofs"
    - "ml-systems"
  subdomain:
    - "zkml"
    - "privacy-and-trustworthy-ml"
  problem:
    - "public verification of local federated training"
    - "public verification of global aggregation"
    - "privacy protection of local data and intermediate model parameters"
  method_family:
    - "Groth16"
    - "Sigma-protocol continuity proofs"
    - "circuit splitting"
    - "secure sum protocol"
    - "Paillier encryption"
    - "fixed-point integer mapping"
    - "Taylor approximation for nonlinear operators"
  system_layer:
    - "federated learning protocol"
    - "zkML proof system application"
    - "blockchain smart-contract aggregation verification"
  evaluation_context:
    - "iris classification"
    - "house price prediction"
    - "ZoKrates prototype"
  bridge:
    - "zk-snarks-to-zkml-verifiable-training"
    - "zkml-verifiable-training-to-federated-learning-integrity"
created: "2026-06-21"
updated: "2026-06-21"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260621-pzkp-fl"
source_refs:
  - "arxiv:2304.05590v2"
  - "sha256:20bee0d6122e02ccd69ea2178675f4c51d9382fe40d1e95f63baf6b6ba267f7e"
confidence: "high"
trust_tier: "primary"
primary_direction: "zkml"
secondary_directions:
  - "privacy-and-trustworthy-ml"
  - "blockchain-based-verification"
classification_status: "reclassified_from_queue"
classification_confidence: "high"
classification_evidence:
  - "The abstract and Sections 4-7 make local training-process verification and global aggregation verification the primary goals."
  - "The paper uses Groth16 and Sigma protocols to prove iterative training pieces and continuity between pieces."
  - "The secure sum and smart-contract route affects federated-learning integrity but is secondary to zkML training proof design."
  - "Queue path zero-knowledge-proofs/zkml/verifiable-inference was too narrow; this source concerns training and aggregation, not inference."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0039"
local_pdf: "~/Desktop/paper/2304.05590v2.pdf"
pdf_sha256: "20bee0d6122e02ccd69ea2178675f4c51d9382fe40d1e95f63baf6b6ba267f7e"
extracted_text_path: "vault/02_Raw/pdf/extracted/2304.05590v2-20bee0d6122e-pages.txt"
---

# Zero-Knowledge Proof-based Practical Federated Learning on Blockchain

## 论文身份

- 标题: Zero-Knowledge Proof-based Practical Federated Learning on Blockchain
- 作者: Zhibo Xing, Zijian Zhang, Meng Li, Jiamou Liu, Liehuang Zhu, Giovanni Russello, Muhammad Rizwan Asghar
- 机构: Beijing Institute of Technology; Hefei University of Technology; The University of Auckland; University of Surrey 等
- 会议/期刊: arXiv preprint; PDF 页眉仍是 LaTeX journal template，不可当作正式 venue。
- 年份: 2023
- arXiv: 2304.05590v2
- DOI: unknown
- Canonical URL: https://arxiv.org/abs/2304.05590
- 本地 PDF: `~/Desktop/paper/2304.05590v2.pdf`
- PDF SHA-256: `20bee0d6122e02ccd69ea2178675f4c51d9382fe40d1e95f63baf6b6ba267f7e`

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf` via bundled Python; queue extracted text reused for deep reading.
- 页数: 15
- 已覆盖章节/页码: Abstract, 1 Introduction, 2 Related Works, 3 Preliminaries, 4 Models and Goals, 5 ZKP-FL Scheme, 6 PZKP-FL Scheme, 7 Security Analysis, 8 Performance Analysis, 9 Conclusions, references.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 图 4-6 的坐标轴文本抽取有 `/s48` 之类编码噪声；表格正文和数值可读。PDF metadata title/author 为空，身份以第一页正文和 arXiv 文件名为准。
- 精读说明: 队列把本论文 staged 到 `zero-knowledge-proofs/zkml/verifiable-inference`。深读后修正为 `zero-knowledge-proofs/zkml/verifiable-training`，因为核心是证明 federated learning 本地训练过程与聚合过程，而不是证明一次 inference output。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 提出 ZKP-FL 和 PZKP-FL；用 ZKP 验证 local computation 和 global aggregation，同时保护 local data | high | 主分类依据 |
| 1 Introduction / p1-p2 | 背景与动机 | FL 面临本地训练不可验证、gradient/model leakage、中心方不可靠；ZKP 可证明训练 relation，但直接用于 ML 成本太高 | high | threat/problem framing |
| 2 Related Works / p2-p3 | 相关工作边界 | 区分 FL、隐私保护、ZK prediction/training verification；Ruckel 等只支持 linear regression | medium | novelty boundary |
| 3 Preliminaries / p3-p4 | 基础工具 | Groth16、Sigma protocol、secure sum、Paillier、blockchain/smart contract | high | method dependencies |
| 4 Models and Goals / p4 | 系统/威胁/目标 | Publisher + trainers；lazy but curious trainer；curious/unreliable publisher；三目标: local computation verification, global aggregation verification, local-data privacy | high | durable FL integrity mapping |
| 5 ZKP-FL / p4-p9 | 核心协议 | Model distribution, training-piece proof, modified statement/vk, continuity Sigma proof, secure sum aggregation and proof | high | main technical mechanism |
| 6 PZKP-FL / p9 | 实用扩展 | Fraction-Integer mapping 和 Taylor expansion 支持小数和非线性函数 | high | numeric semantics contribution |
| 7 Security Analysis / p9-p11 | 安全证明 | 三个定理覆盖 local computation verification、global aggregation verification、privacy | medium | proof sketches, source-authored |
| 8 Performance / p11-p13 | 实验 | Iris classification, house price prediction, ZoKrates, setup/proving/verification costs, piece-size trade-off | high | cost boundaries |
| 9 Conclusion / p13 | 总结 | ZKP + secure MPC 证明 local/global 参数正确；PZKP-FL 支持 fraction/non-linear | medium | source-authored synthesis |

## 结构化摘要

### 解决的问题

这篇论文解决的是 federated learning 中的 training integrity + privacy gap:

- Trainer 可能懒惰，只提交随机或伪造的 local parameters，而不是实际在 local data 上训练。
- Publisher 或其他 participants 希望验证 local training computation 和 global aggregation 是否正确。
- Local data、local model/intermediate gradients 和 aggregated parameters 可能泄露隐私。
- 普通 ZKP 可以证明 circuit satisfiability，但完整 ML training circuit 太大，且 ML 里有小数与非线性函数。

### 核心方法

论文分两层:

1. `ZKP-FL`: 把训练算法切成多个 piece，用 Groth16 证明每个 piece 的电路满足性；用 noise 修改 statement 和 verification key，避免 verification 时暴露中间输入/输出；再用 Sigma protocol 证明修改有效且相邻 piece 的 output/input 连续；最后用 secure sum + Paillier + smart contract 做全局聚合，并用 Sigma proof 证明参与聚合的值与之前提交的 modified statement 一致。
2. `PZKP-FL`: 为了让 scheme 更接近真实 ML，增加 Fraction-Integer mapping，把小数按最大可行 scale 转为整数；用 Taylor expansion 近似 non-linear operations，例如 Sigmoid。

### 创新点

- 不是只证明 prediction/inference，而是验证 federated learning 的 local training process。
- 把大 training circuit 拆成可并行证明的小 piece，并用额外 continuity proof 绑定 piece 之间的状态。
- 同时覆盖 local computation verification、global aggregation verification 和 local data/intermediate parameter privacy。
- 明确处理 ZKP 对 ML 小数和非线性算子的适配问题。

### 主要限制

- Groth16 trusted setup 由 publisher 执行，且每个 piece 的 setup/proving 仍然很重。
- 证明数量可能极大；iris task 中生成 90,000 个 proofs，虽然可并行，但总体资源需求仍高。
- Taylor approximation 和 fixed-point scaling 会引入 numeric semantics/accuracy trade-off。
- 安全分析是论文内 proof sketch，依赖 Groth16、Sigma protocol、Paillier、smart contract/consensus 的安全假设。
- 实验模型较小，只覆盖 iris classification 和 house price prediction，不代表大模型或生产 FL 部署。

## 系统模型、威胁模型与目标

| 维度 | 内容 | Source anchor |
| --- | --- | --- |
| Participants | Publisher 发布模型和训练任务；多个 trainers 本地训练并提交 proofs/modified outputs | §4.1 / p4 |
| Communication / audit layer | 区块链和 smart contract 用于 secure sum / aggregation verification | §4.1, §5.3 |
| Lazy but curious trainer | 想少做计算但拿奖励；也可能试图从其他 trainers 的参数中推断数据 | §4.2 / p4 |
| Curious and unreliable publisher | 可能给出错误 global aggregation，也可能从 local parameters 推断数据 | §4.2 / p4 |
| Goal 1 | Public verification of local computation | §4.3 / p4 |
| Goal 2 | Public verification of global aggregation | §4.3 / p4 |
| Goal 3 | Privacy protection of local data | §4.3 / p4 |

## ZKP-FL 协议细节

### Model distribution

- Publisher 将训练算法 `F` 切成 `q` 个相同的 piece `P`。
- 每个 piece 被转换成 Groth16 arithmetic circuit constraints `R`。
- Publisher 运行 `Groth16.Setup()` 得到 CRS，包括 proving key 和 verification key，然后发送 `P`, CRS 和 constraints 给 trainers。
- 切分的动机是避免整个训练过程变成不可承受的大电路。论文用 gradient descent 例子说明不切分时 setup 可能需要极大内存。

### Model training

- Trainer 用 local data 逐 piece 训练，并保留每轮 input/output statements。
- Algorithm 1 是 modified Groth16 proof generation:
  - 先对原 statement 生成 Groth16 proof `pi_i`。
  - 对 explicit input/output statement 加随机 noise `t`，得到 `phi'_i`。
  - 对 verification key 做对应修改，使 publisher 仍可用 Groth16 verification equation 验证 proof。
  - 对每个 piece 记录 noise list 和 checker。
- Algorithm 2/3 用 Sigma protocol 证明:
  - modified verification key/statement 确实来自合法 noise 修改。
  - piece `i-1` 的 output 与 piece `i` 的 input 使用一致的 noise，因此相邻 piece 连续。
- 设计目的: 避免 publisher 看到 intermediate gradients/local model，同时防止 trainer 在 piece 之间换状态。

### Model aggregation

- Publisher 生成 Paillier public/secret key，并部署 smart contract。
- Trainers 环形交换 random mask `s_i`，然后提交 `Enc_pk(a_i + s_i - s_{i-1})`。
- Smart contract / publisher 计算密文和，mask 项相互抵消，得到 global model average。
- Algorithm 4/5 用 Sigma proof 证明 trainer 参与 secure sum 的明文值和之前提交的 modified statement 中的 local model output 对应。
- 这个聚合过程解决的是 global aggregation correctness 与 local parameter privacy，不是 malicious client poisoning。

## PZKP-FL 实用化扩展

| 机制 | 解决的问题 | 方法 | 代价/边界 | Anchor |
| --- | --- | --- | --- | --- |
| Fraction-Integer mapping | ZKP circuit 只处理整数，ML 参数常为小数 | 训练一次获得 intermediate values，根据 `[-2^63, 2^63-1]` 约束选择最大 scale `10^rat` | scale/truncation 可能影响精度；bit range 成为约束 | Algorithm 6 / §6.1 |
| Taylor expansion for nonlinear ops | Sigmoid/tanh/exp/sqrt 等非线性不便直接进 arithmetic circuit | 对 complex operation 用 Taylor expansion 替换，直到 approximation error 小于阈值 | approximation degree 与精度/电路大小 trade-off；论文示例用 Sigmoid | Algorithm 7 / §6.2 |
| Same-operation same-expansion | 避免同一非线性函数生成太多不同 circuits | 取满足所有训练值精度要求的最大阶 Taylor expansion | 可能为部分输入引入过高电路成本 | §6.2 |

## 安全分析

| Theorem | 目标 | 证明结构 | 依赖 | 备注 |
| --- | --- | --- | --- | --- |
| Theorem 1 | Public verification of local computation | Groth16 证明每个 piece 的 circuit satisfiability；Sigma protocol 证明 vk/statement 修改合法和 piece 连续 | Groth16 soundness; Sigma special soundness | proof sketch |
| Theorem 2 | Public verification of global aggregation | Smart contract 执行 secure sum；Sigma proof 绑定 submitted model 和 secure sum 中的 value | Blockchain/smart contract correctness; Sigma protocol | assumes consensus/smart contract soundness |
| Theorem 3 | Privacy protection of local data | Modified statement 被 random noise 掩盖；ciphertext 被 Paillier/secure sum mask 保护；proofs zero-knowledge | Random masks; Paillier; ZK of Groth16/Sigma | 不覆盖 poisoning/update quality |

## 实验与性能

| 实验 | 设置 | 结果 | 解释 |
| --- | --- | --- | --- |
| Iris classification | 75 training samples, 75 test samples, 1,200 training rounds, each sample in each round as one piece, scale 10,000,000 | setup 950.34s; proof generation 89.99s/proof; verification 25.75s/proof; 90,000 proofs; accuracy 96% | 证明数量很大，但 piece 可并行 |
| House price prediction | 90 training samples, 10 test samples, 500 rounds, each round as one piece, scale 10,000,000 | setup 514.19s; proof generation 50.09s/proof; verification 1.55s/proof; 500 proofs; accuracy 88% | 更少 piece，因此 proof count 低 |
| Piece-size study | house-price task; piece size 1,2,3,5,10,15 epochs | setup/proving time、constraints、CRS/circuit/proving-key size随 piece size 上升；verification/proof size基本稳定 | 小 piece 更利于并行，但 proof 数增加 |

作者强调，如果不切分 iris 训练过程，setup 需要至少 30 TiB memory，runtime 近 1000 天；即使拿到电路，proof generation 和 verification 也要数十天级别。这说明切分不是优化细节，而是让 proof-of-training 可运行的前提。

## 与现有 Nahida 知识的关系

| 目标节点 | 关系 | Source delta | 是否新建节点 |
| --- | --- | --- | --- |
| [[verifiable-training|Verifiable ML training]] | primary source extension | 从 Sparrow 的 tree/forest certification 扩展到 federated neural-network/iterative training route；引入 piece splitting + continuity Sigma proof | no |
| [[verifiable-aggregation|Verifiable aggregation]] | secondary source extension | 提供 secure sum + smart-contract + Sigma proof 的 FL aggregation verification route | no |
| [[federated-learning-integrity|Federated learning integrity]] | cross-domain application | 解决 lazy trainer local computation cheating 与 unreliable publisher aggregation cheating 的一部分 | no |
| [[zk-snarks|zk-SNARKs]] | application evidence | Groth16 用作 local training computation proof backend | no |
| [[zkml|zkML]] | direction update | 补足 queued `neural-network proof-of-training` evidence | no |

## Cold-Start Hierarchy Discovery

| Facet | Result | Evidence | Confidence | Durable handling |
| --- | --- | --- | --- | --- |
| Research field/domain | zero-knowledge-proofs; ml-systems | title, abstract, Sections 3-6 | high | primary ZKP/zkML, secondary ML systems |
| Research background | Federated learning privacy and integrity; ZKP for ML computation | Introduction and related work | high | update zkML and FL integrity nodes |
| Research problem | Verifiable federated training and aggregation without exposing local data | §4 goals | high | source extension under [[verifiable-training]] and [[verifiable-aggregation]] |
| Foundation concepts | zk-SNARKs/Groth16, Sigma protocol, secure sum, Paillier, smart contracts, federated learning | §3 | high | update/query keys; no new foundation node |
| Method family | circuit splitting, modified statements/vk, continuity Sigma proof, secure sum, fixed-point mapping, Taylor approximation | §5-§6 | high | method rows, not standalone nodes yet |
| Application/evaluation context | blockchain-audited federated learning; iris classification; house price prediction | §8 | high | source-only details and source-extension rows |
| Source instance | ZKP-FL / PZKP-FL | Abstract, §5-§6 | high | paper source instance, not knowledge node |

## 检索优化

- 以后问“PZKP-FL 是什么”应先读本 source note。
- 以后问“ZK 如何证明联邦学习训练过程”应先读 [[verifiable-training|Verifiable ML training]]，再打开本 source。
- 以后问“FL 里 lazy trainer 怎么防”应从 [[federated-learning-integrity|Federated learning integrity]] 进入。
- 以后问“ML 里的小数/非线性怎么进 ZKP”可从本 source 的 PZKP-FL 扩展和 zkML 缺口进入；目前还不应建立独立 `fixed-point-zkml-numeric-semantics` 节点。

## Foundation Candidate Judgment

| Candidate | Judgment | Reason |
| --- | --- | --- |
| PZKP-FL | source instance | 论文协议名，当前作为 source extension；未来多篇同类 source 可比较后再拆 method family |
| Circuit splitting for ML training proofs | method candidate | 有可复用性，但当前证据主要来自本 source 和 Sparrow 的另一种 scalability route；先写入 method row |
| Fraction-Integer mapping | method/source-local numeric route | 重要但仍是本论文实现路线；需要更多 fixed-point/quantization/floating-point zkML sources |
| Taylor approximation for nonlinear ML ops | method/source-local numeric route | 与 zkLLM/ZKLP numeric semantics 相邻，但证据不足以新建节点 |
| Verifiable ML training | existing knowledge node | 足够通用，已存在；本 source补强神经网络/FL training route |
| Federated learning integrity | existing knowledge node | 足够通用；本 source补强 lazy trainer + unreliable publisher route |

## Evidence Table

| Claim/Relation | Evidence anchor | Confidence | Notes |
| --- | --- | --- | --- |
| 本文 primary problem 是 verifiable federated training，不是 inference | Abstract, §4 goals, §5 protocol | high | 分类纠偏 |
| Circuit splitting makes proof-of-training feasible | §5.1; §8 performance discussion | high | iris no-split cost is author estimate |
| Modified statement/vk hides intermediate local parameters while keeping Groth16 verification valid | §5.2; Eq. 1-2; Algorithm 1 | high | security depends on random noise and verification key adjustment |
| Sigma protocols bind modifications and adjacent piece continuity | §5.2; Algorithm 2-3; Eq. 3-5 | high | prevents arbitrary piece splicing |
| Secure sum + smart contract verifies global aggregation without revealing local models | §5.3; Algorithm 4-5; Eq. 6-8 | high | blockchain consensus/smart contract correctness assumed |
| PZKP-FL handles fractions via scaling and nonlinear ops via Taylor expansion | §6.1-§6.2; Algorithm 6-7 | high | approximation/scaling trade-off |
| Experiments are small-scale feasibility evidence, not production proof | §8 Tables 1-3 | high | 90,000 proofs for iris highlights cost |

## Knowledge Handoff

- Primary path: `zero-knowledge-proofs/zkml/verifiable-training`.
- Secondary paths:
  - `zero-knowledge-proofs/zkml/verifiable-aggregation`
  - `zero-knowledge-proofs/proof-systems/zk-snarks`
  - `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity`
- Bridge updates:
  - `zk-SNARKs -> zkML verifiable training`
  - `zkML verifiable training -> federated learning integrity`
  - existing `zkML verifiable aggregation -> federated learning integrity` receives a source-extension boundary.
- Review/future:
  - Compare with RoFL/RiseFL and secure aggregation sources.
  - Decide whether `numeric semantics for zkML` deserves a method node after more sources.
  - Analyze any implementation repository only via `nahida-github-repo-analyze` if a repo is provided.

## 查询入口

- PZKP-FL 如何证明本地训练过程?
- ZKP-FL 为什么要把训练算法切成 pieces?
- Algorithm 1 如何隐藏 intermediate parameters?
- Sigma protocol 在 PZKP-FL 中证明什么?
- PZKP-FL 和 zkFL 的区别是什么?
- PZKP-FL 如何处理小数和 Sigmoid 等非线性函数?
- PZKP-FL 的实验成本和瓶颈在哪里?

## 局限与待复核

| Gap | 为什么重要 | 后续动作 |
| --- | --- | --- |
| 缺 RoFL/RiseFL 深读 | 需要区分 lazy trainer、malicious client、malicious aggregator、blockchain FL 的问题边界 | 继续 serial queue |
| 缺 secure aggregation / DP-FL primary sources | 本文 privacy route 不是完整 FL privacy landscape | `nahida-update` or `nahida-research-search` |
| 缺大模型/真实 FL production evidence | 实验小且 proof count 巨大，不足以证明可生产部署 | 后续 repo/benchmark source |
| Numeric semantics 仍薄 | Fixed-point/Taylor 与 zkLLM quantization、ZKLP floating-point 需要统一比较 | 后续 synthesis/bridge after more sources |
