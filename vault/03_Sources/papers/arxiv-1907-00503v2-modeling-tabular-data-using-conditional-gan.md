---
id: "arxiv-1907-00503v2-modeling-tabular-data-using-conditional-gan"
title: "Modeling Tabular Data using Conditional GAN"
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
  - "Abstract, Sections 1-6, Tables 1-4, Algorithm 1, and References"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/1907.00503v2"
doi: ""
arxiv_id: "1907.00503v2"
venue: "NeurIPS 2019"
year: "2019"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
topic_ids:
  - "tabular-synthetic-data-generation"
  - "conditional-tabular-gan"
  - "synthetic-data-evaluation"
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "tabular-synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-evaluation"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "synthetic-data-generation"
  topics:
    - "tabular-synthetic-data-generation"
    - "conditional-tabular-gan"
    - "synthetic-data-evaluation"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "tabular-synthetic-data-generation"
  - "conditional-tabular-gan"
  - "mode-specific-normalization"
  - "training-by-sampling"
  - "synthetic-data-evaluation"
aliases:
  - "CTGAN"
  - "Conditional Tabular GAN"
  - "SDGym"
  - "tabular GAN"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/ml-systems"
  - "nahida/synthetic-data"
direction_facets:
  parent_domain:
    - "ml-systems"
  subdomain:
    - "synthetic-data-generation"
  problem:
    - "tabular-synthetic-data-generation"
    - "mixed-type-tabular-data-generation"
    - "imbalanced-categorical-data-generation"
  method_family:
    - "conditional-tabular-gan"
    - "mode-specific-normalization"
    - "training-by-sampling"
    - "wgan-gp"
    - "pacgan"
    - "tabular-vae-baseline"
  system_layer:
    - "data-synthesis"
    - "benchmark-and-evaluation"
  evaluation_context:
    - "simulated Gaussian mixtures and Bayesian networks"
    - "real tabular classification and regression datasets"
    - "likelihood fitness"
    - "machine-learning-efficacy"
  application:
    - "synthetic tabular data"
    - "data augmentation with selected discrete values"
  bridge:
    - "privacy-preserving synthetic data release candidate only"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-ctgan-tabular-synthetic-data"
source_refs:
  - "arxiv:1907.00503v2"
  - "github:https://github.com/DAI-Lab/CTGAN"
  - "github:https://github.com/DAI-Lab/SDGym"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> synthetic-data-generation"
secondary_directions:
  - "ml-systems -> synthetic-data-generation -> synthetic-data-evaluation"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Title, abstract, Sections 3-5, and experiments all concern synthetic tabular data generation"
  - "The paper is not about distributed learning; privacy is discussed only as an adjacent motivation because GAN generators can be easier to privatize than VAE decoders"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/1907.00503v2.pdf"
pdf_sha256: "eccc2ed8b33ddfb2efa31c171912ad3eca85888005ea61dbd58269b326cdda49"
pdf_pages: 15
pdf_size_bytes: 1849951
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/1907.00503v2-eccc2ed8b33d-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0080"
---

# Modeling Tabular Data using Conditional GAN

## 论文身份

- 标题: Modeling Tabular Data using Conditional GAN
- 作者: Lei Xu, Maria Skoularidou, Alfredo Cuesta-Infante, Kalyan Veeramachaneni
- 机构: MIT; University of Oxford; Rey Juan Carlos University
- 会议/期刊: NeurIPS 2019
- 年份: 2019
- DOI: unknown
- arXiv: `1907.00503v2`
- 链接: https://arxiv.org/abs/1907.00503v2
- 本地 PDF: `~/Desktop/paper/1907.00503v2.pdf`
- SHA-256: `eccc2ed8b33ddfb2efa31c171912ad3eca85888005ea61dbd58269b326cdda49`
- 代码: https://github.com/DAI-Lab/CTGAN
- Benchmark: https://github.com/DAI-Lab/SDGym
- License: unknown in local PDF

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: Codex bundled Python `pypdf`; queue extraction text available.
- 页数: 15
- 已覆盖章节/页码: p1-p15, Abstract, Sections 1-6, Tables 1-4, Algorithm 1, References.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 部分表格和数学符号有 OCR/抽取噪声；supplementary Table 2 有 `TGAN` row naming/OCR ambiguity，但正文模型名和代码链接均为 CTGAN。
- 精读说明: 正文足以支持 source note、tabular synthetic data generation topic seed、synthetic data generation parent refresh 和 ML systems domain refresh。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 表格数据混合离散/连续列；连续列非 Gaussian/multimodal；类别列高度不平衡；提出 CTGAN 并开源 benchmark。 | high | 直接定位为 tabular synthetic data generation。 |
| §1 / p1-p2 | 动机与贡献 | 合成表格数据可用于数据共享、仿真和 ML；现有 statistical/deep approaches 在真实数据上不足；贡献包括 CTGAN、TVAE adaptation 和 benchmark。 | high | 上层问题边界。 |
| §2 / p2 | 相关工作 | 对比 decision trees、Bayesian networks、spatial decomposition trees、copulas、MedGAN、ehrGAN、TableGAN、PATE-GAN。 | medium | 表明 CTGAN 是 tabular synthetic data generator，而不是通用 GAN foundation。 |
| §3 / p2-p4 | 挑战与任务定义 | mixed data types、non-Gaussian/multimodal continuous columns、sparse one-hot、imbalanced categorical columns；定义 likelihood fitness 与 ML efficacy。 | high | 可抽象成 tabular synthetic data generation 的核心问题。 |
| §4.1 / p4-p5 | Mode-specific normalization | 用 variational Gaussian mixture 为每个 continuous column 建模 modes，用 `alpha` scalar + `beta` one-hot mode 表示数值。 | high | CTGAN 解决连续列分布问题的关键机制。 |
| §4.2-§4.3 / p5-p6 | Conditional generator + training-by-sampling | 用 `cond` vector 选择离散列与类别；训练时对离散列均匀、对类别按 log frequency 采样；真实 batch 按同一条件抽取。 | high | 解决 imbalanced categorical columns 的核心机制。 |
| §4.4 / p6 | Network | Fully connected generator/critic，Gumbel softmax，WGAN-GP，PacGAN，Adam。 | medium | 工程机制，留在 source note。 |
| §4.5 / p6 | TVAE baseline | 用同一 preprocessing 改造 VAE，作为深度生成 baseline。 | medium | 解释 TVAE 与 CTGAN 的比较边界。 |
| §5.1-§5.2 / p6-p9 | Benchmark | 7 个模拟数据集、8 个真实数据集；CLBN、PrivBN、MedGAN、VEEGAN、TableGAN、TVAE、CTGAN；likelihood fitness 与 ML efficacy。 | high | 创建 synthetic data evaluation 轴的证据。 |
| §5.3-§5.4 / p9-p10 | 结果与 ablation | CTGAN/TVAE 在真实数据上优于 Bayesian baselines；mode-specific normalization、conditional vector、training-by-sampling 对性能关键。 | high | 方法有效性与局限。 |
| §6 / p10 | 结论与未来工作 | CTGAN 针对混合连续/离散表格数据；未来需要解释 GAN 为什么能处理 mixed distributions。 | medium | 理论边界。 |
| References / p10-p15 | 参考文献与 supplementary tables | prior work、数据集与完整结果表。 | medium | 后续 foundation/research queue 线索。 |

## 核心精读笔记

### 背景、动机与问题边界

这篇论文解决的是静态表格数据的合成生成问题。表格数据通常同时包含连续列、二元列和多类别离散列；连续列可能是多峰分布，离散列可能高度不平衡。把这些列简单 min-max normalize 或 one-hot 后交给普通 GAN/VAE，会带来 vanishing gradient、mode collapse、minor category 学不到、以及 discriminator 过早利用 sparse one-hot 形态区分真假样本等问题。

论文把合成表格数据的目标定义为: 给定真实训练表 `Ttrain`，训练 synthesizer `G`，生成 `Tsyn`，并用两类方式评估:

- Likelihood fitness: synthetic data 是否让 oracle/statistical model 认为接近真实分布。
- Machine learning efficacy: 在 synthetic data 上训练分类/回归模型，再在真实 test set 上评估。

本文不是 privacy-preserving synthetic data release 论文。作者提到 CTGAN 的 generator 在训练过程中不直接访问 real data，因此相比 TVAE 更容易接入 differential privacy；但论文没有隐私定义、攻击模型或隐私实验，不能把 CTGAN 自动当作隐私方案。

证据锚点: Abstract; §1; §3; §5.

### 模型、假设与定义

论文把每一行表格表示为多段拼接:

- 每个 continuous column `Ci` 经过 mode-specific normalization，表示为 scalar `alpha` 和 mode indicator `beta`。
- 每个 discrete column `Di` 表示为 one-hot vector。
- Generator 的目标不是一次性无条件生成整行，而是可按某个 discrete condition `Di*=k*` 生成满足条件的 row distribution。

CTGAN 的关键假设是: 表格数据中的连续列多峰性和类别列不平衡是普通 GAN 失败的主要来源；如果训练过程显式覆盖 rare categories，并让真实/生成 batch 在同一条件下比较，就能降低 minor category 被忽略的概率。

证据锚点: §3.2; §3.3; §4.1-§4.3.

### 方法、协议或系统机制

CTGAN 的方法可以拆成三块。

1. Mode-specific normalization:
   - 对每个 continuous column 用 variational Gaussian mixture 估计若干 modes。
   - 对每个真实值，计算其属于各 mode 的概率，并采样一个 mode。
   - 用 `(value - mode_mean) / (4 * mode_std)` 得到 bounded scalar `alpha`，再用 one-hot `beta` 表示所选 mode。
   - 这样连续列不再被单一 min-max range 强行压缩，GAN 更容易学习 multimodal/non-Gaussian structure。

2. Conditional generator:
   - 构造 `cond` vector，表示当前希望生成的 discrete column/category。
   - Generator 输入 `noise + cond`；loss 加入 cross-entropy，使生成样本在被选中的 discrete column 上匹配 condition。
   - 生成阶段可以指定某个 discrete value，支持按类别定向生成或数据增强。

3. Training-by-sampling:
   - 每个 batch 随机均匀选择一个 discrete column。
   - 在该列内部按 log-frequency probability 选择 category，而不是按原始频率抽样。
   - fake samples 由 generator 条件生成；real samples 从 `Ttrain` 中满足同一 condition 的 rows 抽取。
   - Critic 比较的是同一条件下的 real/fake conditional distributions，因此 minor categories 更容易被训练到。

网络层面，CTGAN 使用 fully connected generator/critic、Gumbel softmax 输出离散变量、WGAN-GP loss、Adam，以及 PacGAN 的 packing trick 来缓解 mode collapse。论文还把同一 preprocessing 用于 TVAE，形成一个深度 VAE baseline。

证据锚点: §4.1-§4.5; Algorithm 1.

### 实验、评估或案例

Benchmark 覆盖 7 个模拟数据集和 8 个真实数据集。

- 模拟数据:
  - Gaussian mixture: grid, gridr, ring。
  - Bayesian network: asia, alarm, child, insurance。
- 真实数据:
  - adult, census, covertype, credit, intrusion, MNIST12, MNIST28, news。
- Baselines:
  - Bayesian/statistical: CLBN, PrivBN。
  - Deep models: MedGAN, VEEGAN, TableGAN, TVAE, CTGAN。
- Evaluation:
  - Simulated data: `Lsyn` and `Ltest` likelihood fitness；`Ltest` 用 synthetic data 重新训练 oracle 后在 real test set 上算 likelihood，以避免只奖励 overfitting。
  - Real data: machine learning efficacy；synthetic train set 上训练分类/回归模型，real test set 上用 accuracy/F1 或 R2 评估。

论文结论可以拆开读:

- 在模拟 Gaussian mixture 上，mode-specific normalization 明显重要；普通深度 GAN 容易 mode collapse，Bayesian networks 对连续列离散化会受损。
- 在模拟 Bayesian network 上，CLBN/PrivBN 有天然优势，CTGAN 相比 MedGAN/TableGAN 更稳但不是全场景最优。
- 在真实表格数据上，TVAE 和 CTGAN 是主要赢家；CTGAN 相比 CLBN 在 7/8 个真实数据集上更好，相比 PrivBN 在 8/8 个真实数据集上更好。MedGAN、VEEGAN、TableGAN 在这些 real datasets 上整体弱于 Bayesian baselines。
- TVAE 在若干 aggregate real-data metrics 上也非常强，甚至在部分表中优于 CTGAN；作者因此强调不要把 CTGAN 读成所有深度生成器上的绝对最优，而应看它在 conditional sampling 和可接入 differential privacy 方面的优势。

Ablation 显示:

- 把 mode-specific normalization 换成 fixed GMM 或 MinMax 会降低性能，MinMax 最差。
- 去掉 training-by-sampling，平均性能下降明显；在 credit 等高度不平衡数据上可能让 F1 接近 0。
- 去掉 conditional vector 影响更大，说明仅靠重采样不够，generator 必须看见条件。
- WGAN-GP 比 vanilla GAN 更适合该设置；PacGAN 对 vanilla GAN 帮助更明显，对 WGAN-GP 不是决定性因素。

证据锚点: §5.1-§5.4; Table 1-4.

### 作者结论与我的判断

- 作者明确声称: CTGAN 用 mode-specific normalization 处理任意连续分布，用 conditional generator/training-by-sampling 处理 imbalanced discrete columns，并在真实 tabular datasets 上优于 Bayesian baselines；同时开源 CTGAN 和 SDGym benchmark。
- 由证据支持的判断: CTGAN 是 tabular synthetic data generation 的代表性 source，因为它把“混合连续/离散列 + 多峰连续列 + 类别不平衡 + fidelity/utility evaluation”合并成了清楚的问题定义和 benchmark。
- 仍需谨慎的推断: 本文没有隐私保证；没有证明 GAN 为什么适合 mixed distributions；数据集和 metrics 不能代表所有 tabular data release 场景；TVAE 在部分结果中强于 CTGAN，因此不能简单说 CTGAN 全面支配所有 tabular synthesizers。

## 层级候选分类

- L1 Domain candidate: `ml-systems`
- L2 Direction candidate: `synthetic-data-generation`
- L3 Topic/content cluster candidate: `tabular-synthetic-data-generation`
- Ontology path: `ml-systems/synthetic-data-generation/tabular-synthetic-data-generation`
- 备选归属: `privacy-and-trustworthy-ml` 只作为相邻问题，因为本文未给出 privacy mechanism/evaluation。
- 父级领域: machine learning systems / data generation for ML workflows
- 学术子领域: synthetic tabular data generation, generative models for structured data
- 任务/问题: generate mixed-type synthetic tabular rows preserving distribution and downstream ML utility
- 方法族: conditional tabular GAN, mode-specific normalization, training-by-sampling, WGAN-GP, PacGAN
- Benchmark/应用: SDGym, 7 simulated datasets, 8 real tabular datasets
- 别名: CTGAN, Conditional Tabular GAN, tabular GAN
- 相邻方向: synthetic data evaluation, privacy-preserving synthetic data release, data augmentation
- 置信度: high
- 分类理由: 正文全篇围绕 synthetic tabular data generation；队列旧分类 `ml-systems/privacy-and-trustworthy-ml/distributed-learning` 与内容不匹配。
- 分类状态: `corrected_from_queue`
- Taxonomy version: `1.0`

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | ML systems | 论文关注生成数据如何服务 ML training/evaluation/workflows。 | high | parent refresh |
| Research background | synthetic tabular data; data sharing; benchmark evaluation | §1-§2; SDGym links。 | high | direction/topic background |
| Research problem | mixed-type tabular synthetic data generation | §3 challenges and task definition。 | high | create topic seed |
| Foundation concepts | synthetic data generation, tabular data, GAN, VAE, Bayesian networks, likelihood/utility evaluation | §2-§5。 | medium | concepts stay in source/knowledge; broader foundations still queued |
| Method family | conditional tabular GAN with mode-specific normalization and training-by-sampling | §4。 | high | source extension |
| Application/evaluation context | real tabular classification/regression synthetic train set evaluation | §5。 | high | topic evaluation section |
| Artifact/source instance | CTGAN, TVAE adaptation, SDGym benchmark | §4-§5 and code links。 | high | source extension, not upper concept |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `ml-systems/synthetic-data-generation/tabular-synthetic-data-generation`
- 它能帮助未来哪些问题少读 source notes:
  - “表格合成数据为什么难？”
  - “CTGAN 解决了哪些 tabular data 特有问题？”
  - “合成表格数据应该怎么评估？”
  - “mode-specific normalization 和 training-by-sampling 分别解决什么？”
- 哪些内容应留在 source note，而不是创建上层节点:
  - Algorithm 1 的逐步训练循环、Table 2/3 的全部数值、每个 dataset 的逐项得分、Gumbel softmax temperature 等实现细节。
- 哪些上层节点过薄、缺失或需要 foundation_pack:
  - `synthetic-data-generation` 仍缺 broader foundation sources。
  - `synthetic-data-evaluation` 可以作为评价轴候选，需更多 fidelity/utility/privacy/fairness/robustness sources。
  - `privacy-preserving synthetic data release` 需要 DP synthetic data/PATE-GAN/PrivBayes 等 sources。
- 哪些候选只是别名/query key/watch term:
  - `CTGAN`, `SDGym`, `mode-specific normalization`, `training-by-sampling`, `TVAE`。

## 一句话贡献

CTGAN 把表格数据合成中的多峰连续列、混合离散/连续列和类别不平衡问题显式建模，用 mode-specific normalization、conditional generator 与 training-by-sampling 训练一个 tabular GAN，并用 SDGym 风格 benchmark 同时检验 simulated likelihood fitness 和 real-data ML efficacy。

## 创新点

- 新思想: 把表格数据的连续列多峰性和离散列类别不平衡作为 generator training 的一等约束，而不是只套用图像 GAN 结构。
- 对已有工作的扩展: 在 GAN/VAE/Bayesian synthetic data methods 上加入 tabular-specific preprocessing、conditional sampling 和 benchmark protocol。
- 工程或实证贡献: 开源 CTGAN 与 SDGym；在 15 个数据集、7 个 baseline、2 类评价机制下比较 synthetic tabular data generators。
- 依赖的 prior work: Bayesian networks, PrivBayes/PrivBN, MedGAN, VEEGAN, TableGAN, WGAN-GP, PacGAN, Gumbel softmax。

## 局限性

### 作者明确说明

- 尚缺理论解释: 为什么 GANs 能够很好处理 mixed discrete/continuous tabular distributions。
- CTGAN 不是在每个 synthetic-data setting 上支配 TVAE；TVAE 在部分数据集和 aggregate metrics 上很强。
- 隐私只是 future/adjacent motivation，正文没有 DP training 或 privacy leakage evaluation。

### 基于证据的推断

- Real-data benchmark 只用 downstream classifiers/regressors 的 aggregate score；不覆盖 fairness、rare subgroup fidelity、membership inference 或 attribute disclosure。
- Conditional generator 可按 discrete value 生成样本，但不等于解决 causal validity 或 real deployment sampling bias。
- Benchmark 数据集多为经典 tabular datasets；对现代高维业务表、关系型多表数据、文本/embedding columns 的泛化需要后续 source。
- SDGym/CTGAN repo 只作为论文链接记录，本次没有单独分析仓库代码或版本。

## 可复用思路

- 合成数据节点应该区分数据模态: tabular、time-series、image/audio 等模态的结构约束和评价方式不同。
- Tabular synthetic data 的核心不是“更深的 GAN”，而是 preprocessing、conditional training、sampling strategy 和评价协议一起设计。
- Synthetic data evaluation 至少要分成 distribution/lifetime fidelity 和 downstream task utility；privacy/fairness/robustness 需要额外 evidence，不能默认成立。

## 术语表

| Term | Local meaning |
| --- | --- |
| CTGAN | Conditional Tabular GAN，本文提出的 tabular synthetic data generator。 |
| Mode-specific normalization | 用 Gaussian mixture mode 表示连续列的局部位置，避免单一 min-max normalization 损害多峰分布。 |
| Conditional generator | 让 generator 按指定 discrete column/category 生成 rows。 |
| Training-by-sampling | 训练时均匀选择 discrete column，再按 log frequency 选择 category，以提高 minor categories 的训练曝光。 |
| ML efficacy | 用 synthetic train data 训练 ML model，再在 real test set 上评估 classification/regression utility。 |
| SDGym | 本文开源的 synthetic data benchmark 工具/数据集框架。 |

## 连接

- 相关 Knowledge nodes: [[ml-systems|ML systems]], [[synthetic-data-generation|Synthetic data generation]], [[tabular-synthetic-data-generation|Tabular synthetic data generation]]
- 相关 Bridges: none promoted in this run.
- Bridge 候选:
  - `synthetic-data-generation -> privacy-and-trustworthy-ml`: candidate only. CTGAN 可能比 TVAE 更容易接入 DP 训练，但本文没有隐私证明。
  - `synthetic-data-generation -> database systems`: candidate only. Tabular data 与数据库数据有关，但本文不是数据库系统论文。

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| tabular synthetic data generation | topic/problem | 本文完整围绕 mixed-type tabular data generation。 | active_seed | 创建 topic node |
| synthetic data evaluation | evaluation_axis | 本文同时使用 likelihood fitness 和 ML efficacy。 | queued | 等更多 evaluation/privacy/fairness sources 后拆节点 |
| privacy-preserving synthetic data release | adjacent problem | 相关工作包括 PrivBN/PATE-GAN，CTGAN 只提到 DP easier。 | review | 后续吸收 DP synthetic data sources |
| CTGAN | source instance / method | §4 算法。 | source_extension | 不单独建 foundation node |
| SDGym | benchmark artifact | §5 and code link。 | source_extension | 若后续分析仓库，可建 repo source note |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 表格合成难点包括 mixed data types、non-Gaussian/multimodal continuous columns、sparse one-hot 和 imbalanced categories。 | author claim + problem framing | §3 | 四个 challenges 被逐项列出。 | high | local PDF evidence |
| Mode-specific normalization 是 CTGAN 处理连续列分布的关键机制。 | method detail | §4.1 | VGM + alpha/beta representation。 | high | local PDF evidence |
| Conditional generator 与 training-by-sampling 解决类别不平衡。 | method detail | §4.2-§4.3 | condition vector + log-frequency category sampling。 | high | ablation supports |
| Benchmark 同时评估 likelihood fitness 和 ML efficacy。 | evaluation design | §5.1-§5.2 | simulated/real datasets use different evaluation mechanisms。 | high | local PDF evidence |
| CTGAN 在真实数据上优于 CLBN/PrivBN 大多数/全部数据集。 | experimental result | Table 1; §5.3 | 7/8 vs CLBN, 8/8 vs PrivBN。 | high | paper claim/table |
| 不能据此声称 CTGAN 是隐私保护方案。 | boundary judgment | whole paper | no DP training, threat model, or leakage metric。 | high | inference from absence |

## 知识交接

- 留在本文元笔记的证据: CTGAN architecture、VGM/mode-specific normalization、conditional vector、training-by-sampling、WGAN-GP/PacGAN setup、dataset/baseline/table details、ablation 细节。
- 待更新 Knowledge node:
  - [[ml-systems|ML systems]]
  - [[synthetic-data-generation|Synthetic data generation]]
  - [[tabular-synthetic-data-generation|Tabular synthetic data generation]]
  - [[research-dynamics|ML systems Research Dynamics]]
- 作为哪些 Knowledge node 的 source extension:
  - `ml-systems/synthetic-data-generation`
  - `ml-systems/synthetic-data-generation/tabular-synthetic-data-generation`
- 需要补的 foundation knowledge/source:
  - synthetic data generation foundations
  - tabular synthetic data evaluation
  - privacy-preserving synthetic data release
  - modern tabular generative models beyond CTGAN/TVAE
- Bridge 候选: synthetic data generation to privacy/trustworthy ML remains review-only.
- Watchlist 词条: CTGAN, SDGym, TVAE, PrivBN, PATE-GAN, mode-specific normalization, training-by-sampling, machine learning efficacy.
- 后续论文: DP synthetic data/PATE-GAN/PrivBayes, more tabular diffusion/LLM/tabular data generation sources, SDGym/SDV repo if user provides repo source.
- Review queue: no blocker; queue classification corrected from distributed/privacy ML to tabular synthetic data generation.

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Synthetic data generation | direction_knowledge | 更新 ML systems 下的方向节点，解释生成、augmentation、fidelity/utility/privacy 评价。 | 让 CTGAN 独占 synthetic data 定义。 | §1-§5 |
| Tabular synthetic data generation | topic_knowledge_candidate | 新建 topic seed，组织 mixed-type tabular data、conditional sampling、benchmark evaluation。 | 把 CTGAN 当作上层概念。 | §3-§5 |
| CTGAN | representative_instance_or_source_extension | 留在 source note 和 source extension row。 | 单独提升成基础概念节点。 | §4 |
| Mode-specific normalization | method/source_extension | 作为 tabular synthetic data 的方法路线。 | 单独建成 foundation node。 | §4.1 |
| Training-by-sampling | method/source_extension | 作为 imbalanced categorical data 的方法路线。 | 当作通用采样理论节点。 | §4.3 |

## Knowledge 综合交接

- 应创建 Knowledge node:
  - `vault/04_Knowledge/ml-systems/synthetic-data-generation/tabular-synthetic-data-generation.md`
- 应刷新 Knowledge synthesis section:
  - `vault/04_Knowledge/ml-systems/synthetic-data-generation.md`
  - `vault/04_Knowledge/ml-systems.md`
  - `vault/04_Knowledge/ml-systems/research-dynamics.md`
- 应标记过期: none.
- 无需更新的理由: `privacy-and-trustworthy-ml` 不更新为 durable route，因为本文没有 privacy mechanism/evaluation。
- 建议 node kind: problem/topic.

## 处理日志

- 2026-06-23: Deep-read local 15-page PDF, corrected queue classification from privacy/distributed learning to ML systems synthetic data generation, wrote source note and handed off for knowledge absorption.
