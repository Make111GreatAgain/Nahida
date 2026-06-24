---
id: "pmlr-v162-alaa22a"
title: "How Faithful is your Synthetic Data? Sample-level Metrics for Evaluating and Auditing Generative Models"
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
  - "p1-p10 main paper"
  - "p11-p17 appendix"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
pmlr_volume: "162"
pmlr_id: "alaa22a"
venue: "Proceedings of the 39th International Conference on Machine Learning"
year: "2022"
authors:
  - "Ahmed M. Alaa"
  - "Boris van Breugel"
  - "Evgeny Saveliev"
  - "Mihaela van der Schaar"
local_pdf_path: "~/Desktop/paper/alaa22a.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/alaa22a-516321bcf894-pages.txt"
sha256: "516321bcf89499604bc83d4f25ee639bc837856841ee5652c8539e69577e5fc2"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0098"
queue_rank: 98
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
topic_ids:
  - "synthetic-data-evaluation"
  - "synthetic-data-privacy-evaluation"
  - "tabular-synthetic-data-generation"
  - "time-series-synthetic-data-generation"
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
primary_ontology_path: "ml-systems/synthetic-data-generation/synthetic-data-evaluation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
  - "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
  - "ml-systems/synthetic-data-generation/time-series-synthetic-data-generation"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "synthetic-data-generation"
  topics:
    - "synthetic-data-evaluation"
    - "synthetic-data-privacy-evaluation"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
  - "synthetic-data-privacy-evaluation"
aliases:
  - "How Faithful is your Synthetic Data?"
  - "Sample-level Metrics for Evaluating and Auditing Generative Models"
  - "alpha-Precision beta-Recall Authenticity"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
  - "synthetic-data/evaluation"
direction_facets:
  parent_domain:
    - "ml-systems"
  subdomain:
    - "synthetic-data-generation"
  problem:
    - "synthetic-data-evaluation"
    - "synthetic-data-privacy-evaluation"
  method_family:
    - "sample-level-generative-model-evaluation"
    - "precision-recall-generative-model-metrics"
    - "model-auditing"
  system_layer:
    - "evaluation"
  evaluation_context:
    - "fidelity"
    - "diversity"
    - "generalization"
    - "privacy-utility-tradeoff"
  application:
    - "clinical-tabular-synthetic-data"
    - "clinical-time-series-synthetic-data"
    - "image-generation-benchmark"
  bridge:
    - "synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-how-faithful-synthetic-data"
source_refs:
  - "pmlr:162:alaa22a"
  - "sha256:516321bcf89499604bc83d4f25ee639bc837856841ee5652c8539e69577e5fc2"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> synthetic-data-generation"
secondary_directions:
  - "ml-systems -> synthetic-data-generation -> synthetic-data-privacy-evaluation"
classification_status: "active"
classification_confidence: "high"
classification_evidence:
  - "title/subtitle"
  - "abstract"
  - "ICML/PMLR venue"
  - "main sections p1-p10"
  - "experiments p6-p8"
taxonomy_version: "1.0"
---

# How Faithful is your Synthetic Data?

## 论文身份

- 标题: How Faithful is your Synthetic Data? Sample-level Metrics for Evaluating and Auditing Generative Models
- 作者: Ahmed M. Alaa, Boris van Breugel, Evgeny Saveliev, Mihaela van der Schaar
- 机构: Broad Institute of MIT and Harvard; MIT; Cambridge University; UCLA
- 会议/期刊: Proceedings of the 39th International Conference on Machine Learning, PMLR 162, 2022
- 年份: 2022
- DOI: not recorded in local PDF metadata
- arXiv: not recorded in local PDF metadata
- 链接: not verified in this run; local PDF is the evidence source
- 本地 PDF: `~/Desktop/paper/alaa22a.pdf`
- 提取文本: `vault/02_Raw/pdf/extracted/alaa22a-516321bcf894-pages.txt`
- 代码: paper lists `github.com/ahmedmalaa/evaluating-generative-models` and `https://github.com/vanderschaarlab/evaluating-generative-models` on p8; repository code was not analyzed in this run.
- License: not specified in local PDF.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: queue metadata says `codex-bundled-python:pypdf`; extracted text covers all 17 pages.
- 页数: 17
- 已覆盖章节/页码: p1 abstract/introduction; p2-p3 evaluation/auditing desiderata; p3-p6 definitions and estimators; p6-p8 experiments; p8-p9 conclusion/references; p11-p17 appendix/literature review/proof/experimental details.
- 已检查附录: yes; appendix covers metric taxonomy, theorem proof, support-estimation alternative, data/embedding details and full tables.
- 未覆盖章节/页码: none.
- Extraction gaps: headings after tables are noisy, but formulas, section content, experiment narratives and tables are readable enough for absorption.
- 精读说明: 本笔记重建论文的问题设定、三维指标、估计流程、实验结论和隐私/泛化边界；具体代码实现未打开。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| p1-p2 Abstract and Introduction | Problem and contribution | 提出 `(α-Precision, β-Recall, Authenticity)`，用 fidelity、diversity、generalization 三维评价生成模型；强调 sample-level evaluation and auditing。 | high | 直接决定知识归属为 synthetic-data-evaluation。 |
| p2-p3 Section 2 | Evaluation/auditing desiderata | 好的 synthetic data set 应同时满足 fidelity、diversity、generalization；metric 需能 sample-wise 计算，支持过滤低质量样本。 | high | 上层可复用为 sample-level evaluation route。 |
| p3-p5 Section 3 | Metric definitions | 用 minimum volume sets 定义 α-support/β-support；`α-Precision` 衡量 synthetic samples 是否落入 real α-support；`β-Recall` 衡量 real samples 是否被 synthetic β-support 覆盖；`Authenticity` 衡量非复制训练样本概率。 | high | 核心方法。 |
| p4-p5 Theorem 1 and integrated metrics | Theory | 若 `Pα/α = Rβ/β = 1` 对所有 α,β 成立，当且仅当生成分布等于真实分布；定义 integrated precision/recall 作为曲线偏离度。 | high | 支撑该指标比单点 precision/recall 更能检测 density mismatch。 |
| p5-p6 Section 4 | Estimation | 训练 one-class evaluation embedding，把 real data 映射到 hypersphere；用 quantile radius 估计 α-support；用 k-NN local coverage 估计 recall；用最近邻距离假设检验识别 copied samples。 | high | 机制细节保留在源笔记，上层只写路线。 |
| p6-p8 Section 5 | Experiments/use cases | COVID-19 tabular predictive modeling、ADS-GAN privacy-utility tuning、post-hoc auditing、MNIST mode dropping、Hide-and-Seek time-series、CIFAR-10 StyleGAN/DDPM comparison。 | high | 说明跨模态可用，但不构成全部模态综述。 |
| p8-p9 Conclusion | Limitations/future | 指标适合临床合成数据；typical/outlier 区分可能支持 fairness evaluation，但 fairness 只是未来工作。 | medium | 不应把 fairness 节点直接提升。 |
| p11-p17 Appendices | Related metrics/proof/details | 对 divergence metrics 与 precision/recall metrics 的限制做系统对照，给出 theorem proof、数据/embedding 和完整实验表。 | high | 补全 deep-read completeness。 |

## 核心精读笔记

### 背景、动机与问题边界

- 背景脉络: 生成模型评价长期依赖 likelihood、statistical divergence、image-oriented scores 或 standard precision/recall。论文认为这些指标要么模型依赖、要么高维不稳定、要么把不同 failure modes 压缩成一个数，难以诊断 mode collapse、mode invention、density shift、training-data copying 等问题。
- 现有方法不足: standard precision/recall 只看 support，可能在 `Pr` 与 `Pg` 支持集相同但密度完全不匹配时给出完美分数；divergence/FID/MMD 等单数指标难以分辨 fidelity 和 diversity；很多图像指标依赖预训练 embedding，迁移到临床表格或时序数据时不自然。
- 本文问题定义: 构造一个 domain- and model-agnostic evaluation metric `E(Dreal, Dsynth)`，既能整体评价生成模型，又能对单个 synthetic sample 给出质量判断，从而支持 post-hoc auditing/filtering。
- 明确不解决的问题: 论文不是新的 generator 训练算法；不是 Differential Privacy 机制；不是合成数据发布的完整隐私保证；代码仓库未在本轮分析。
- 证据锚点: p1-p3; appendix p11-p12.

### 模型、假设与定义

- 数据模型: 真实数据 `Xr ~ Pr`，生成数据 `Xg ~ Pg`，样本集为 `Dreal` 和 `Dsynth`；评价通常先通过 embedding `Φ` 映射到 feature space，再比较分布。
- 三个评价质量:
  - Fidelity: synthetic samples 是否像真实样本，本文用 `α-Precision` 表示。
  - Diversity: synthetic samples 是否覆盖真实数据变化范围，本文用 `β-Recall` 表示。
  - Generalization: generator 是否真的产生新样本，而不是复制训练数据，本文用 `Authenticity` 表示。
- `α-support`: 一个分布中承载概率质量 α 的最小体积子集；直觉上是最典型、密度最高的区域，剩余部分可视为 outlier 区域。
- `β-support`: 对生成分布同理，用来判断真实样本是否被生成分布的典型区域覆盖。
- `Authenticity` 的 copying 模型: 将生成分布写成“创新样本分布”和“训练样本加微小噪声”的混合；`A` 越低，生成样本越可能是训练记录的复制或近复制。
- 假设条件: 需要一个可用的 feature embedding 和距离度量；one-class hypersphere 近似需要训练/验证；authenticity 依赖最近邻距离假设检验，对高维 embedding 质量敏感。
- 证据锚点: p2-p6.

### 方法、协议或系统机制

- `α-Precision`: 对每个 synthetic sample 检查它是否落在真实分布的 `α-support` 内。与 standard precision 不同，它不是只看完整 support，而是随着 α 扫描 typical-to-outlier 区域，得到整条 precision curve。
- `β-Recall`: 对每个 real sample 检查它是否被生成分布 `β-support` 的典型 synthetic samples 局部覆盖。它用来识别 mode dropping 和 diversity loss。
- Integrated metrics: 论文用曲线相对理想直线的平均绝对偏离定义 `IPα` 和 `IRβ`，便于把整条曲线压成可比较单数，但仍保持 fidelity/diversity 分离。
- `Authenticity`: 对 synthetic sample 找最近训练样本 `i*`，比较 synthetic-to-nearest-real 距离与该真实样本到其他真实样本的最近邻距离；若 synthetic 比真实样本之间还更靠近某个训练点，则判为 unauthentic。
- Evaluation embedding: 用 one-class neural network / Deep SVDD 风格 loss 把 real data 压到最小体积 hypersphere，从而用分位数半径估计 `α-support`。对 time-series 使用 Seq2Seq/LSTM embedding，对 image 可用 InceptionV3 embedding。
- Auditing pipeline: 先计算 sample-level precision/authenticity，再丢弃低 precision 或低 authenticity 样本；若能持续访问 generator，可作为 rejection sampler 反复生成直到接受高质量样本。
- 复杂度/资源: 需要训练 embedding、计算最近邻和 k-NN coverage；附录给出 `k=5` 等实验设置，但没有给出完整复杂度分析。
- 证据锚点: p3-p6, p12-p17.

### 理论、证明或正确性论证

- 定理 1: 若对所有 α,β 都有 `Pα/α = Rβ/β = 1`，当且仅当 `Pg = Pr`。这说明 α/β 曲线的理想状态对应真实/生成分布相等，而 standard precision/recall 的单点完美分数不能保证密度匹配。
- 证明思路: 当 `Pg = Pr` 时，两者的 α-support/β-support 相同，因此 synthetic/real 样本落入对应 support 的概率等于 α/β。反向证明利用嵌套 support 的概率质量相等，推出两分布在 support 的细分区域上质量相同。
- 理论边界: 该定理建立在理想分布和 support 定义上；实际估计依赖 embedding、样本量、one-class support estimator 和最近邻参数。
- 证据锚点: p4 and appendix p12.

### 实验、评估或案例

- COVID-19 clinical tabular data: 用 SIVEP-Gripe COVID-19 patient data 训练 VAE、GAN、WGAN-GP、ADS-GAN 等 synthetic datasets，再用 synthetic data 训练 logistic regression 预测死亡率，并在 real data 上测 AUC-ROC。`IPα` 与 `IRβ` 比若干 baseline 更能恢复下游模型表现排名；尤其 `IPα` 精确匹配四个 generator 的 ground-truth ranking。
- ADS-GAN privacy-utility tuning: ADS-GAN 有隐私正则超参数 `λ`；论文显示 `λ` 增大提高 authenticity 但降低 precision，因此 `(precision, authenticity)` 图能解释 privacy-utility tradeoff。作者把低 authenticity 解释为更多病人信息可能暴露，但这仍是 overfitting/copying 指标，不是 DP guarantee。
- Post-hoc auditing: 对 ADS-GAN 生成样本按 precision/authenticity 过滤后，curated data 的 precision/authenticity 接近最优，下游 predictive AUC 有小幅提升。这个结果说明 sample-level metric 不只是报告工具，还能作为 filtering/auditing mechanism。
- MNIST mode dropping: 论文人为删除 1-9 数字样本并用 0 填补，模拟 mode dropping。standard precision/recall 对非极端 mode dropping 不敏感，而 `IRβ` 随 dropping 变严重而下降，`IPα` 基本不受影响，显示 fidelity/diversity 分离。
- Hide-and-Seek time-series: 重新评估 NeurIPS 2020 Hide-and-Seek challenge 的 ICU time-series submissions。比赛获胜的 Gaussian-noise-style submission 在 precision/recall 上可竞争，但 authenticity 很低，被论文解释为“高 utility 但接近复制真实数据”的风险。
- CIFAR-10 image generation: 比较 StyleGAN2-ADA 与 DDPM；FID 排 StyleGAN 更好，但 `IPα/IRβ` 给出更细分图景：DDPM 在 overlap 区域 fidelity 更好，StyleGAN diversity 更好。
- 数据与附录细节: p13-p17 记录 SIVEP-GRIPE、AmsterdamUMCdb、MNIST 数据规模、embedding 方式和完整 metric 表。
- 证据锚点: p6-p8, p13-p17.

### 作者结论与我的判断

- 作者明确声称: 三维指标能同时评价 fidelity、diversity、generalization，并支持 sample-level auditing；该指标可跨 tabular、time-series、image domains 使用。
- 由证据支持的判断: 本文是合成数据评价轴的重要 source extension，因为它把“合成数据质量”从 dataset-level utility/fidelity 推进到 sample-level diagnostics，并把 training-data copying 纳入 generative-model evaluation。
- 仍需谨慎的推断: `Authenticity` 与隐私泄露有关，但不是正式 privacy guarantee；过滤低 authenticity 样本也不等于发布过程满足 Differential Privacy。论文代码和工程可复现性未在本轮验证。
- 证据锚点: p1-p8, p11-p17.

## 层级候选分类

- L1 Domain candidate: `ml-systems`
- L2 Direction candidate: `synthetic-data-generation`
- L3 Topic/content cluster candidates: `synthetic-data-evaluation`; secondary `synthetic-data-privacy-evaluation`
- Ontology path: `ml-systems/synthetic-data-generation/synthetic-data-evaluation`
- 备选归属: `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation`; modality-specific evaluation for tabular/time-series/image synthetic data.
- 父级领域: ML systems
- 学术子领域: synthetic data generation; generative model evaluation
- 任务/问题: evaluation of synthetic data fidelity/diversity/generalization; model auditing
- 方法族: sample-level generative model evaluation; precision-recall curves over minimum-volume supports; data-copying authenticity test
- 模型/协议/算法族: VAE, GAN, WGAN-GP, ADS-GAN, DDPM, StyleGAN2-ADA as evaluated instances
- 评测场景: clinical tabular data, clinical time-series data, MNIST, CIFAR-10
- Benchmark/应用: SIVEP-Gripe, AmsterdamUMCdb Hide-and-Seek challenge, MNIST, CIFAR-10
- 别名: `α-Precision`, `β-Recall`, `Authenticity`, `model auditing`
- 相邻方向: synthetic data privacy evaluation; tabular synthetic data generation; time-series synthetic data generation
- 置信度: high
- 分类理由: paper title/subtitle, abstract and all main experiments focus on synthetic/generative data evaluation, not distributed learning.
- 分类状态: active
- 分类证据: p1 abstract; p2 desiderata; p6-p8 experiments.
- Taxonomy version: 1.0
- Direction facets: see frontmatter.
- Tags: `nahida/source`, `nahida/paper`, `synthetic-data/evaluation`
- Map memberships: `Synthetic data generation`; `Synthetic data evaluation`
- 归属说明: 这篇论文不是 privacy/trustworthy ML 的主线论文，也不是 distributed learning。它的 primary path 是 synthetic data evaluation；privacy evaluation 只吸收 `Authenticity` 对 data copying 和 sensitive-data release 的边界提醒。

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `ml-systems` | ICML/PMLR paper; evaluates generative models for synthetic data | high | existing domain |
| Research background | generative model evaluation; synthetic data utility/fidelity; privacy-sensitive data modeling | intro and related metrics appendix | high | update knowledge background |
| Research problem | sample-level synthetic data evaluation and auditing | p1-p3 desiderata | high | source extension to `synthetic-data-evaluation` |
| Foundation concepts | precision/recall for generative models; minimum volume sets; one-class support estimation; data-copying/generalization | p3-p6 and appendix | medium | keep concise in knowledge node; do not create separate foundation node yet |
| Method family | `α-Precision`, `β-Recall`, `Authenticity`, integrated curve metrics, post-hoc auditing | p3-p8 | high | method route/source extension |
| Application/evaluation context | clinical tabular, clinical time-series, image generation | p6-p8 | high | secondary tags; no new modality node |
| Artifact/source instance | ICML 2022 paper and listed evaluation code | p8 code lines | high | source note only; repo analysis queued only if user requests |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `ml-systems/synthetic-data-generation/synthetic-data-evaluation`
- 它能帮助未来哪些问题少读 source notes:
  - “合成数据评价为什么要 sample-level？”
  - “α-Precision / β-Recall / Authenticity 分别评价什么？”
  - “如何发现生成模型复制训练数据？”
  - “合成数据 high utility 是否可能仍有隐私风险？”
  - “如何用 auditing/filtering 改善 synthetic samples？”
- 哪些内容应留在 source note，而不是创建上层节点: theorem proof details, one-class loss formula details, exact table values, exact dataset preprocessing, all baseline metric rows, code repository names before repo analysis.
- 哪些上层节点过薄、缺失或需要 foundation_pack: generative model evaluation metrics taxonomy; Differential Privacy synthetic data release; fairness evaluation for synthetic data.
- 哪些候选只是别名/query key/watch term: `IPα`, `IRβ`, `Authenticity score`, `model auditing`, `minimum volume set metrics`.

## 一句话贡献

本文提出 `(α-Precision, β-Recall, Authenticity)` 三维 sample-level 指标，把 synthetic/generative data evaluation 从“整体分布像不像”细化为 fidelity、diversity 和是否复制训练数据，并用同一套指标支持 post-hoc model auditing。

## 问题设定

论文要解决的是 domain- and model-agnostic generative model evaluation：给定真实数据集和生成数据集，评价生成模型是否生成真实、覆盖充分且非训练样本复制的 synthetic data，并能对单个样本做 accept/reject 判断。

## 方法概览

### 组成部分

- `α-Precision`: 以真实分布的 α-support 为基准，衡量 synthetic samples 中有多少落入真实数据的典型区域。
- `β-Recall`: 以生成分布的 β-support 为基准，衡量真实样本有多少被生成分布的典型区域覆盖。
- `Authenticity`: 以最近邻距离检验 synthetic sample 是否比真实样本之间还更接近某个训练样本，从而判断是否疑似 copying。
- Integrated scores: `IPα` and `IRβ` 把整条曲线压成单值，便于排序，但仍保留 fidelity/diversity 分离。
- Auditing/filtering: 对 synthetic samples 进行 sample-level 检查，过滤低 precision 或低 authenticity 样本。

### 流程或协议

1. 训练或选取 evaluation embedding `Φ`，使不同数据模态能进入可比较 feature space。
2. 在 embedded real data 上估计 `α-support`，并用 synthetic samples 计算 `α-Precision`。
3. 在 embedded synthetic data 上估计 `β-support`，并用 real samples 计算 `β-Recall`。
4. 用最近邻距离检验计算 synthetic samples 的 `Authenticity`。
5. 需要整体评价时报告 curves/integrated scores；需要 auditing 时按 sample-level precision/authenticity 过滤。

### 关键定义、公式、算法或定理

- `Sα`: 支撑概率质量 α 的最小体积集合。
- `Pα = P(Xg in Sα_r)`: synthetic sample 落入 real α-support 的概率。
- `Rβ = P(Xr in Sβ_g)`: real sample 被 synthetic β-support 覆盖的概率。
- `IPα = 1 - 2∫|Pα - α|dα`, `IRβ = 1 - 2∫|Rβ - β|dβ`: 曲线偏离理想直线的综合分数。
- Theorem 1: `Pα/α = Rβ/β = 1` for all α,β iff `Pg = Pr`.
- Authenticity classifier: 若 synthetic sample 到最近训练样本的距离小于该训练样本到其他训练样本的最近邻距离，则判为 unauthentic。

### 假设条件

- 需要 meaningful embedding；否则 support/nearest-neighbor 检查不可靠。
- 需要训练数据或其 embedding 用于 support estimation 和 authenticity test。
- Authenticity 是 copying/generalization diagnostic，不是 formal privacy guarantee。

## 创新点

- 新思想: 把 fidelity/diversity/generalization 写成可 sample-level 计算的三维指标，而不是单个 aggregate score。
- 对已有工作的扩展: 将 standard precision/recall 从 full-support comparison 扩展到 minimum-volume `α/β-support` curves，从而检测 density mismatch、mode dropping 和 outlier sensitivity。
- 评价用途扩展: 用 sample-level metric 支持 model auditing 和 rejection sampling，使评价指标可以直接改善已生成 synthetic dataset。
- 隐私相关补充: 用 Authenticity 把 generative-model overfitting / training-data copying 明确纳入 synthetic data evaluation。

## 实验与结果摘要

| 场景 | 数据/模型 | 核心观察 | 上层处理 |
| --- | --- | --- | --- |
| Clinical tabular predictive modeling | SIVEP-Gripe COVID-19; VAE/GAN/WGAN-GP/ADS-GAN | `IPα` 更好恢复 synthetic-data-trained classifier 的 real-test AUC 排名；support-only metrics 会误判。 | synthetic-data-evaluation route |
| ADS-GAN tuning | ADS-GAN privacy regularization scale `λ` | `λ` 增加提升 authenticity 但降低 precision，形成可解释 privacy-utility tradeoff。 | bridge to privacy evaluation |
| Post-hoc auditing | audited ADS-GAN samples | 过滤低 precision/authenticity 样本可提升 synthetic dataset quality 和 downstream AUC。 | model-auditing route |
| MNIST mode dropping | CGAN + controlled digit dropping | `IRβ` 对 mode dropping 敏感，`IPα` 主要保持 fidelity，standard precision/recall 不敏感。 | diversity diagnostic |
| Hide-and-Seek time-series | AmsterdamUMCdb submissions | 竞赛 winner 在 authenticity 上很低，可能是 noisy copy route，说明 utility-only ranking 有发布风险。 | privacy boundary bridge |
| CIFAR-10 image generation | StyleGAN2-ADA vs DDPM | FID 与 `IPα/IRβ` 给出不同排序维度：DDPM overlap fidelity 更好，StyleGAN diversity 更高。 | cross-modal evidence only |

## 限制与 caveat

- `Authenticity` 与 privacy risk 有关，但不是 Differential Privacy、membership-inference bound 或 legal anonymization proof。
- 指标依赖 embedding 和 support estimator；不同数据模态的 embedding 选择会影响结果。
- Auditing/filtering 可能改善样本集质量，但若过滤规则访问训练数据或输出 pass/fail signal，在发布场景也需要放入 threat model。
- 论文实验覆盖 tabular/time-series/image，但不是所有 synthetic data types 的 benchmark standard。
- 代码未在本轮分析；工程可复现性、API、默认参数和维护状态仍需 repo note。

## 上层吸收决策

| 候选内容 | 类型 | 目标 knowledge/bridge | 证据 | 决策 |
| --- | --- | --- | --- | --- |
| `α-Precision / β-Recall / Authenticity` | method route | [[synthetic-data-evaluation|Synthetic data evaluation]] | p1-p6 | promote as source extension/method route |
| Sample-level model auditing | evaluation/auditing route | [[synthetic-data-evaluation|Synthetic data evaluation]] | p2, p6-p8 | promote as method route |
| Authenticity/data copying | privacy boundary evidence | [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]] and bridge | p2, p6-p8 | promote as boundary caveat, not guarantee |
| Minimum volume sets | prerequisite/math concept | no standalone node yet | p3-p5 | keep local; add query key only |
| Fairness of synthetic data | future application | review/gap | p8 conclusion | queue, do not promote |
| Code repositories | GitHub source candidates | `03_Sources/github/` if requested | p8 | not analyzed |

## 证据记录

| 事实/观察 | 证据位置 | 置信度 | 时效性 | 上层处理 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 论文提出三维指标 `(α-Precision, β-Recall, Authenticity)`，分别对应 fidelity、diversity、generalization。 | p1-p3 | high | evergreen | update `synthetic-data-evaluation` | 核心贡献。 |
| `α-Precision/β-Recall` 基于 minimum volume support，而不是完整 support，能检测 density mismatch 和 mode failure。 | p3-p5 | high | evergreen | update method route | 细节保留在源笔记。 |
| `Authenticity` 用最近邻距离测试 synthetic sample 是否疑似训练样本复制。 | p4-p6 | high | evergreen | update privacy bridge | 不等于 DP。 |
| Auditing/filtering 可以丢弃低 precision/authenticity 样本，从而改善 synthetic dataset quality。 | p2, p6-p8 | high | evergreen | update evaluation node | 发布场景需注意 metric leakage。 |
| ADS-GAN `λ` 实验展示 precision/authenticity tradeoff，可解释 privacy-utility boundary。 | p6-p7 | high | source-specific | bridge update | 数值留在源笔记。 |
| Hide-and-Seek winner 可能 high utility but low authenticity，说明 utility-only ranking 会隐藏 copying risk。 | p7-p8 | high | source-specific | bridge update | 不是正式攻击证明。 |

## 处理日志

- 2026-06-23: Deep-read local PDF, created source note, corrected queue classification from `ml-systems/privacy-and-trustworthy-ml/distributed-learning` to `ml-systems/synthetic-data-generation/synthetic-data-evaluation`, and handed off to `nahida-knowledge-get` absorption.
