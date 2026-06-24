---
id: "sha256-c081c745e120-generative-learning-financial-time-series-irregular-scale-invariant-patterns"
title: "Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns"
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
  - "p1-p12 full extracted text"
  - "Abstract, Sections 1-6, Figures 1-6, Table 1, and References"
  - "Appendices A-E are referenced by the paper but are not present in the local 12-page PDF/extraction"
safe_for_absorption: true
canonical_url: ""
doi: ""
arxiv_id: ""
venue: "ICLR 2024 under review"
year: "2023"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
topic_ids:
  - "time-series-synthetic-data-generation"
  - "financial-time-series-generation"
  - "diffusion-models-for-time-series"
  - "data-augmentation"
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "time-series-synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation/time-series-synthetic-data-generation"
secondary_ontology_paths: []
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "synthetic-data-generation"
    - "time-series-modeling"
  topics:
    - "time-series-synthetic-data-generation"
    - "financial-time-series-generation"
    - "irregular-scale-invariant-time-series"
    - "diffusion-models-for-time-series"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "time-series-synthetic-data-generation"
  - "financial-time-series-generation"
  - "diffusion-models-for-time-series"
  - "data-augmentation"
  - "scale-invariant-subsequence-clustering"
aliases:
  - "FTS-Diffusion"
  - "Generative Learning for Financial Time Series"
  - "financial time series generation"
  - "irregular and scale-invariant time series"
  - "Scale-Invariant Subsequence Clustering"
  - "SISC"
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
    - "time-series-synthetic-data-generation"
    - "financial-time-series-generation"
  method_family:
    - "diffusion-models-for-time-series"
    - "pattern-recognition-generation-evolution"
    - "scale-invariant-subsequence-clustering"
  system_layer:
    - "data-augmentation"
    - "downstream-prediction-evaluation"
  evaluation_context:
    - "financial asset returns"
    - "distribution fidelity"
    - "downstream forecasting utility"
  application:
    - "financial deep learning"
    - "synthetic financial data"
  bridge: []
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-fts-diffusion-financial-time-series"
source_refs:
  - "sha256:c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> synthetic-data-generation"
secondary_directions: []
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Title, abstract, Sections 1-4, and experiments all concern financial time-series generation and data augmentation"
  - "No blockchain, data availability, or light-client content appears in the paper body"
  - "The method is a synthetic-data generation framework using pattern recognition, diffusion generation, and Markov-style evolution"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/[ICLR 2024] GENERATIVE LEARNING FOR FINANCIAL TIME SERIES WITH IRREGULAR AND SCALE-INVARIANT PATTERNS(1).pdf"
pdf_sha256: "c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5"
pdf_pages: 12
pdf_size_bytes: 1241469
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/iclr-2024-generative-learning-for-financial-time-series-with-irregular-and-scale-invariant-patterns-1-c081c745e120-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0075"
---

# Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns

## 论文身份

- 标题: Generative Learning for Financial Time Series with Irregular and Scale-Invariant Patterns
- 作者: Anonymous authors
- 机构: unknown
- 会议/期刊: ICLR 2024 under review
- 年份: 2023 local PDF metadata; target venue header is ICLR 2024
- DOI: unknown
- arXiv: unknown
- 链接: unknown
- 本地 PDF: `~/Desktop/paper/[ICLR 2024] GENERATIVE LEARNING FOR FINANCIAL TIME SERIES WITH IRREGULAR AND SCALE-INVARIANT PATTERNS(1).pdf`
- SHA-256: `c081c745e120fb62972f9f746897bfc3c68666966c0744f880792c3f9d0652f5`
- 代码: unknown
- 数据: S&P 500, GOOG, and ZC=F financial asset time series from public historical prices, exact data URLs not provided in the local PDF.
- License: unknown

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: Codex bundled Python `pypdf`; queue extraction text available.
- 页数: 12
- 已覆盖章节/页码: p1-p12, Abstract, Sections 1-6, Figures 1-6, Table 1, References.
- 已检查附录: local PDF references Appendix A-E, but appendices are not present in this 12-page PDF/extraction.
- 未覆盖章节/页码: Appendix A-E details are unavailable.
- Extraction gaps: math symbols for scaling factors are partially garbled; no DOI/arXiv; no accepted venue metadata; authors are anonymous.
- 精读说明: 正文足以支持 source note 和上层 synthetic-data/time-series generation seed；附录细节、代码和外部元数据需要后续人工或 web/source verification。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 金融时序数据稀缺；难点是 irregular and scale-invariant patterns；提出 FTS-Diffusion 三模块框架；下游预测误差最高降低 17.9%。 | high | 摘要级主张，后文支撑。 |
| §1 / p1-p2 | 动机与贡献 | 金融数据不能像自然科学一样轻易做实验；return data 噪声高、历史有限；普通生成模型假设 regularity/uniformity。 | high | 定位为 synthetic financial data / data augmentation。 |
| §2 / p3 | 相关工作 | 对比 TimeVAE、RCGAN、TimeGAN、QuantGAN、CSDI、DiffWave 等时序生成路线。 | medium | 表明本文不是 GAN/VAE 基础，而是金融时序特性驱动的 generation framework。 |
| §3 / p3-p4 | 问题建模 | 将金融时序表示为多个 segment；每个 segment 由 pattern、duration scale、magnitude scale 决定；用 Markov chain 建模 pattern transition。 | high | 上层 time-series synthetic data generation 的关键问题定义。 |
| §4.1 / p4-p5 | Pattern recognition | Scale-Invariant Subsequence Clustering (SISC): greedy variable-length segmentation + DTW distance + K-means-style clustering + diverse centroid initialization。 | high | 方法局部机制。 |
| §4.2 / p5-p6 | Pattern generation | Pattern-conditioned DDPM + scaling autoencoder；loss 包括 reconstruction loss 和 denoising-gradient objective。 | high | 生成模块。 |
| §4.3 / p6-p7 | Pattern evolution | 用 neural network 学习下一 pattern、length scale、magnitude scale 的 Markov-style transition。 | high | 拼接 segment 成完整时序。 |
| §4.4 / p7 | End-to-end synthesis | 从 observed initial segment 开始，反复预测下一 state、生成下一 segment，直到达到目标长度。 | high | 系统流程。 |
| §5.1 / p7-p8 | 实验设置 | 数据集 S&P 500, GOOG, ZC=F；80/20 train-test；比较 return series；baselines 为 RCGAN、TimeGAN、CSDI、TimeVAE。 | high | 评估边界。 |
| §5.2 / p8 | Fidelity evaluation | 检查 heavy tails、absolute-return autocorrelation decay；用 KS/AD 比较合成与真实 return distribution。 | high | 生成质量证据。 |
| §5.3 / p8-p9 | Downstream utility | TMTR 和 TATR 两种设置；LSTM next-point prediction；FTS-Diffusion 在混合比例变化下更稳定，并通过 augmentation 降低 MAPE。 | high | 数据增强实用性证据。 |
| §6 / p9 | 结论与未来工作 | 总结三模块；未来方向包括 multivariate modeling、transition distribution shift、generation quality theory。 | medium | 限制与后续方向。 |
| References / p10-p12 | 参考文献 | GAN/VAE/diffusion/time-series/finance prior work。 | medium | 可作为后续 foundation/research queue 线索。 |

## 核心精读笔记

### 背景、动机与问题边界

这篇论文解决的是金融时序数据生成中的数据稀缺与模式复杂性问题。作者指出，金融研究很难像自然科学一样通过实验获得更多历史数据；价格和收益率序列又噪声高、样本有限，因此深度模型容易过拟合。常规 data augmentation 或 time-series generation 若假设周期性、固定窗口或规则模式，难以捕捉金融序列中“不定期重复但形状相似”的动态。

作者把金融时序的核心特征概括为两点:

- Irregularity: pattern recurrence interval 不固定，不像 ECG 或电力负载那样有清楚周期。
- Scale-invariance: pattern 的基本形状可相似，但持续时间和幅度会被拉伸、压缩或平移。

本文明确不解决的问题包括: 多变量金融资产交互、transition distribution shift 的完整处理、生成质量理论保证、真实交易收益/风险评估、隐私保护、合成数据泄露风险、金融市场制度变化和生产部署。

证据锚点: Abstract; §1 p1-p2; Figure 1; Figure 2; §6 p9.

### 模型、假设与定义

论文将一条时序 `X = {x1, ..., xM}` 表示为多个 variable-length segment。每个 segment `xm` 从条件分布中采样，该分布依赖:

- pattern `p`,
- duration scaling factor,
- magnitude scaling factor.

为了建模 segment 之间的连续动态，论文使用 Markov-chain-style state transition。state 包括 pattern、duration scale、magnitude scale；transition 表示从一个 segment state 到下一个 segment state 的概率或可学习预测。作者强调本文不是恢复某个未指定 latent state，而是明确建模 pattern、duration 和 magnitude 这三个方面。

证据锚点: §3.1 p3-p4; §3.2 p4; §4.3 p6-p7.

### 方法、协议或系统机制

FTS-Diffusion 被拆成 pattern recognition、pattern generation、pattern evolution 三个模块。

1. Pattern recognition module / SISC:
   - 目标: 将整条金融时序切分成 variable-length segments，并把 shape 相似但 duration/magnitude 不同的 segment 聚成 `K` 个 clusters。
   - Greedy segmentation: 在每个位置枚举 candidate length `l in [lmin, lmax]`，选择与最近 centroid 距离最小的长度。
   - 距离度量: 使用 dynamic time warping (DTW) 而不是 Euclidean distance，以比较不同长度、不同幅度但形状相似的 subsequences。
   - Clustering: 完成 greedy segmentation 后，按 K-means-like process 反复分配 segments 到最近 centroid 并更新 centroids。
   - Initialization: 使用 distance-weighted diverse centroid initialization，避免随机初始化带来的糟糕局部结果。
   - 复杂度: 论文声称 SISC computational complexity is `O(T K lmax)`，对整条时序长度线性。

2. Pattern generation module:
   - Pattern-conditioned diffusion network: 基于 DDPM，对 pattern representation 加噪并学习 denoising gradient，从 Gaussian noise 生成新的 pattern representation。
   - Scaling autoencoder: encoder 将 variable-length segments 拉伸到 fixed-length representation，decoder 从 fixed-length representation 重构 variable-length segments。
   - Joint training objective: reconstruction loss + denoising-gradient objective/unweighted ELBO variant。

3. Pattern evolution module:
   - 用 neural network 学习下一 segment state: next pattern、next duration scale、next magnitude scale。
   - Objective 包含 pattern 的 cross-entropy loss，以及 duration/magnitude scale 的 L2 loss。

4. End-to-end synthesis:
   - 从 observed data 中采样 initial segment。
   - 每一步由 pattern evolution network 预测下一 state。
   - 再由 pattern generation module 合成对应 segment。
   - 重复直到 synthetic time series 达到目标长度。

证据锚点: §4.1 p4-p5; Eq. 1-2; §4.2 p5-p6; Eq. 3-5; §4.3 p6-p7; Eq. 6-7; §4.4 p7; Figure 3-4.

### 理论、证明或正确性论证

正文没有给出正式定理或生成质量证明。它的正确性论证主要是机制合理性与实验验证:

- DTW 适合 variable-length subsequence alignment，因此适合识别 duration-scaled patterns。
- Diffusion model 的 denoising process 可从 Gaussian latent space 生成 pattern representation。
- Markov-style transition 将连续 segment 的 temporal correlation 显式建模。

作者在 §6 提到未来可加强 generation quality 的 theoretical guarantee，说明正文并未提供强理论保证。

证据锚点: §4.1-§4.4; §6 p9.

### 实验、评估或案例

实验目标是检验合成金融时序是否像真实数据，并是否能改善 downstream prediction。

- 数据集:
  - S&P 500, 1980-01-01 to 2020-01-01。
  - GOOG, 2005-01-01 to 2020-01-01。
  - ZC=F corn futures, 1980-01-01 to 2020-01-01。
- 数据处理: 用 return series 而非 raw prices，因为 raw prices 近似 non-stationary random walk，而 returns 的统计性质更稳定。
- Split: first 80% training, last 20% testing；generator 和 downstream model 都不见 test set。
- Baselines: RCGAN, TimeGAN, CSDI (generative), TimeVAE。
- Fidelity metrics:
  - stylized facts: heavy tails, slow decay in autocorrelation of absolute returns。
  - KS/AD goodness-of-fit tests, larger value means synthetic distribution closer to observed distribution。
- Utility metrics:
  - LSTM-based downstream predictor。
  - one-day ahead prediction with 64 previous historical values。
  - MAPE averaged over multiple runs。
  - TMTR: train on observed/synthetic mixture, test on real。
  - TATR: start with 10 years observed data, append synthetic data, test on real。

Table 1 reports FTS-Diffusion as best among listed baselines:

| Dataset | FTS-Diffusion KS | FTS-Diffusion AD | strongest baseline KS/AD in table |
| --- | --- | --- | --- |
| S&P 500 | `.327 ± .003` | `.128 ± .003` | TimeGAN `.293 ± .004` / `.115 ± .006` |
| GOOG | `.324 ± .004` | `.119 ± .002` | TimeGAN `.288 ± .007` / `.108 ± .005` |
| ZC=F | `.325 ± .003` | `.121 ± .003` | TimeGAN `.287 ± .007` / `.103 ± .005` |

Figure 6 reports downstream utility:

- TMTR: FTS-Diffusion maintains comparable prediction accuracy as the proportion of synthetic data changes; baselines degrade when observed-data proportion decreases.
- TATR: appending 100 years of FTS-Diffusion synthetic data reduces MAPE by `17.9%`, `15.3%`, and `17.4%` on the three assets.

证据锚点: §5.1 p7-p8; Table 1 p8; §5.2 p8; §5.3 p8-p9; Figure 5-6.

### 作者结论与我的判断

- 作者明确声称: FTS-Diffusion 是一个面向 irregular and scale-invariant financial time series 的 generation framework；它能生成更贴近真实金融 returns 的合成时序，并在下游预测任务中缓解数据不足。
- 由证据支持的判断: 在本文三个单变量金融资产数据集与给定 baselines/metrics 下，pattern-recognition-generation-evolution 结构比普通 RCGAN/TimeGAN/CSDI/TimeVAE 更适合 preserve distribution fidelity and utility。
- 仍需谨慎的推断: 论文处于 anonymous under-review 状态；没有附录细节、代码或外部复现；评估不覆盖 multivariate portfolios、regime shift、交易收益、风险控制、合成数据隐私泄露或跨市场泛化。

## 层级候选分类

- L1 Domain candidate: `ml-systems`
- L2 Direction candidate: `synthetic-data-generation`
- L3 Topic/content cluster candidates: `time-series-synthetic-data-generation`, `financial-time-series-generation`, `diffusion-models-for-time-series`
- Ontology path: `ml-systems/synthetic-data-generation/time-series-synthetic-data-generation`
- 备选归属: `ml-systems/time-series-modeling` could be created later if more forecasting/modeling sources arrive.
- 父级领域: machine learning systems / applied ML data generation
- 学术子领域: synthetic data generation, time-series generation, financial machine learning
- 任务/问题: generate realistic and useful synthetic financial time series under irregularity and scale-invariance
- 方法族: pattern-aware diffusion generation, SISC, Markov-style pattern evolution
- 模型/协议/算法族: DDPM, scaling autoencoder, DTW clustering, LSTM downstream evaluation
- 评测场景: financial return distribution fidelity and downstream stock/futures prediction
- Benchmark/应用: S&P 500, GOOG, ZC=F; TMTR/TATR
- 别名: FTS-Diffusion, SISC
- 相邻方向: privacy/trustworthy ML synthetic data, time-series forecasting, financial ML
- 置信度: high
- 分类理由: 正文全篇围绕 financial time-series synthetic data generation；队列旧分类 `blockchain-systems/data-availability-and-light-clients/data-availability-sampling` 与内容无关，应更正。
- 分类状态: `corrected_from_queue`
- 分类证据: title, abstract, Sections 1-5, datasets, baselines and evaluation.
- Taxonomy version: `1.0`
- Direction facets: synthetic data generation / time-series generation / data augmentation.
- Tags: `nahida/source`, `nahida/paper`, `nahida/ml-systems`, `nahida/synthetic-data`
- Map memberships: ML systems domain; synthetic data generation direction; time-series synthetic data generation topic.

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | ML systems | 论文目标是为金融深度学习生成训练数据；实验关注 augmentation utility。 | high | durable parent update |
| Research background | synthetic data for data scarcity; time-series generation; financial ML | §1 and §2 discuss scarcity, noise, GAN/VAE/diffusion time-series generation. | high | knowledge background |
| Research problem | time-series synthetic data generation under irregularity and scale-invariance | Abstract; §3 problem statement. | high | create topic seed |
| Foundation concepts | synthetic data generation, diffusion models, time-series modeling, dynamic time warping, financial returns | §2-§5. | medium | foundation_thin; queue broader foundation sources |
| Method family | pattern-recognition-generation-evolution; pattern-aware diffusion generation | §4. | high | source extension under synthetic data/time-series generation |
| Application/evaluation context | financial return generation and downstream prediction augmentation | §5. | high | application/evaluation section |
| Artifact/source instance | FTS-Diffusion, SISC | §4 and §5. | high | source extension, not upper concept |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `ml-systems/synthetic-data-generation/time-series-synthetic-data-generation`
- 它能帮助未来哪些问题少读 source notes:
  - “金融时序合成数据怎么做？”
  - “time-series synthetic data generation 目前有哪些路线？”
  - “合成数据怎样评估 fidelity 和 downstream utility？”
  - “FTS-Diffusion 和 TimeGAN/CSDI/TimeVAE 的差异是什么？”
- 哪些内容应留在 source note，而不是创建上层节点:
  - SISC 的具体伪代码、Eq. 1-7 细节、Figure 5/6 具体曲线、Table 1 数值、三资产实验细节。
- 哪些上层节点过薄、缺失或需要 foundation_pack:
  - `synthetic-data-generation` 需要 broad foundation sources。
  - `time-series-synthetic-data-generation` 需要 TimeGAN/CSDI/TimeVAE/QuantGAN 等代表 source。
  - synthetic data 的 privacy/fidelity/utility evaluation 与 trustworthy ML 关系需要单独 sources 支撑。
- 哪些候选只是别名/query key/watch term:
  - `FTS-Diffusion`, `SISC`, `irregular and scale-invariant patterns`, `TMTR`, `TATR`。

## 一句话贡献

FTS-Diffusion 将金融时序生成拆成 pattern recognition、pattern generation、pattern evolution 三步，用 SISC 识别 variable-length/scale-invariant patterns，再用 pattern-conditioned diffusion 和 Markov-style transition 生成可用于下游预测增强的合成金融 return series。

## 创新点

- 新思想: 将金融时序的 irregularity 与 scale-invariance 变成显式建模对象，而不是把数据切成固定窗口后交给通用 generator。
- 对已有工作的扩展: 在 GAN/VAE/diffusion time-series generation 之上加入 SISC pattern discovery 和 transition evolution。
- 工程或实证贡献: 在 S&P 500、GOOG、ZC=F 三个金融资产上，FTS-Diffusion 在 KS/AD 和下游 LSTM prediction utility 上优于 RCGAN、TimeGAN、CSDI、TimeVAE。
- 依赖的 prior work: DDPM, DTW, K-means-style clustering, time-series GAN/VAE/diffusion models, financial stylized facts.

## 局限性

### 作者明确说明

- 未来需要处理 multivariate modeling with dependencies across multiple time series。
- 方法可处理 number of patterns 变化导致的 distribution shifts，但 transition shifts 还需扩展。
- generation quality 的 theoretical guarantee 仍待加强。

### 基于证据的推断

- Anonymous under-review paper: 作者、接收状态、最终版本未知。
- 附录不在 local PDF 中: SISC pseudo-code、network structure、ablation details、additional metrics 仅被正文引用，无法在本地 source note 中复核。
- 评估只覆盖三个金融资产和 LSTM next-point prediction；没有 portfolio PnL、risk-adjusted returns、transaction cost、market impact、out-of-regime robustness。
- 没有 privacy evaluation；不能把 synthetic financial data 等同于 privacy-preserving data release。
- 没有代码和复现实验脚本；结果可复现性需要后续 source。

## 可复用思路

- 对复杂时序生成，可以先显式识别可重复但 variable-scale 的 pattern，再生成 segment，再学习 segment transition。
- Synthetic data evaluation 不应只看 distribution fidelity，还应看 downstream utility。
- 金融时序生成尤其需要检查 stylized facts，如 heavy tails 和 volatility clustering/absolute-return autocorrelation decay。

## 术语表

| Term | Local meaning |
| --- | --- |
| FTS-Diffusion | 本文提出的 financial time-series generation framework。 |
| SISC | Scale-Invariant Subsequence Clustering，用 DTW + greedy segmentation + K-means-style clustering 识别 scale-invariant patterns。 |
| Irregularity | pattern recurrence intervals are indeterminate rather than fixed-frequency。 |
| Scale-invariance | pattern shape can remain similar under duration/magnitude scaling。 |
| TMTR | Training on Mixture, Test on Real；训练集混合 observed and synthetic data。 |
| TATR | Training on Augmentation, Test on Real；用 synthetic data 扩充 observed training set。 |

## 连接

- 相关 Knowledge nodes: [[ml-systems|ML systems]], [[synthetic-data-generation|Synthetic data generation]], [[time-series-synthetic-data-generation|Time-series synthetic data generation]]
- 相关 Bridges: none promoted in this run.
- Bridge 候选:
  - `synthetic-data-generation -> privacy-and-trustworthy-ml`: candidate only. 本文不评估隐私或匿名性，不能把 synthetic data 直接提升为 privacy-preserving route。
  - `synthetic-data-generation -> financial ML`: candidate only. 当前 vault 尚无 financial ML direction，后续若吸收更多金融 ML sources 可创建。

## 扩展候选

| 候选 | 类型 | 证据 | 状态 | 建议动作 |
| --- | --- | --- | --- | --- |
| synthetic data generation | direction | 本文和队列后续多篇 synthetic/tabular/privacy papers | active_seed | 创建 direction node，后续 foundation_pack |
| time-series synthetic data generation | topic/problem | 本文完整围绕 time-series generation and evaluation | active_seed | 创建 topic node |
| financial time-series generation | application subtopic | 本文唯一 source; finance-specific | candidate | 暂不单独建节点，作为 topic node 的 application route |
| synthetic data privacy/fidelity/utility evaluation | adjacent problem | 本文只评估 fidelity/utility，不评估 privacy | watching | 后续吸收 synthetic data evaluation/privacy papers |

## 证据记录

| 结论/观察 | 类型 | 位置 | 证据 | 置信度 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 金融时序生成难点是 irregular and scale-invariant patterns。 | author claim + motivation | Abstract; §1; Figure 1-2 | 与 ECG/solar/power consumption 对比。 | high | local PDF evidence |
| FTS-Diffusion 有三模块。 | method claim | Abstract; §4; Figure 3 | pattern recognition, generation, evolution。 | high | local PDF evidence |
| SISC 用 DTW 处理 variable-length/magnitude subsequences。 | method detail | §4.1; Eq. 1-2 | Euclidean distance 不适合 variable length。 | high | appendices unavailable |
| FTS-Diffusion 在 Table 1 的 KS/AD 指标上优于 baselines。 | experimental result | §5.2; Table 1 | 三个资产上 KS/AD 均最高。 | high | local PDF evidence |
| Synthetic augmentation 可降低预测误差最高 17.9%。 | experimental result | §5.3; Figure 6 | TATR setting, 100 years synthetic data。 | high | exact curves in figure only |
| 不能据此声称隐私保护。 | boundary judgment | whole paper | no privacy experiment/threat model。 | high | inference from absence |

## 知识交接

- 留在本文元笔记的证据: FTS-Diffusion architecture, SISC details, equations, baselines, Table 1 values, TMTR/TATR setup and caveats。
- 待更新 Knowledge node:
  - [[ml-systems|ML systems]]
  - [[synthetic-data-generation|Synthetic data generation]]
  - [[time-series-synthetic-data-generation|Time-series synthetic data generation]]
  - [[research-dynamics|ML systems Research Dynamics]]
- 作为哪些 Knowledge node 的 source extension:
  - `ml-systems/synthetic-data-generation`
  - `ml-systems/synthetic-data-generation/time-series-synthetic-data-generation`
- 需要补的 foundation knowledge/source:
  - synthetic data generation foundations
  - time-series generative modeling
  - synthetic data evaluation: fidelity, utility, privacy, robustness
- 待新增或复核 domain/direction/problem:
  - `ml-systems/synthetic-data-generation` created as foundation_thin direction.
  - `ml-systems/synthetic-data-generation/time-series-synthetic-data-generation` created as active_seed topic.
- Bridge 候选: synthetic data generation to trustworthy ML privacy remains review-only.
- Watchlist 词条: FTS-Diffusion, SISC, synthetic financial time series, TMTR, TATR, TimeGAN, CSDI, TimeVAE, QuantGAN.
- 后续论文: TimeGAN, CSDI, TimeVAE, QuantGAN, synthetic data evaluation papers in current queue.
- 后续仓库: none in vault.
- Review queue: no blocker; metadata unknown and appendix missing recorded as source caveats.

## 基础概念候选判断

| 候选术语/方法 | 判断 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Synthetic data generation | direction_knowledge_candidate | 创建/更新 ML systems 下的 direction，解释生成、augmentation、fidelity/utility/privacy 评价。 | 让 FTS-Diffusion 成为唯一解释。 | §1-§5; queue has adjacent synthetic-data sources |
| Time-series synthetic data generation | topic_knowledge_candidate | 创建 topic seed，组织 GAN/VAE/diffusion/pattern-aware methods。 | 把 financial-only paper 当作整个 time-series generation 全景。 | §2-§5 |
| FTS-Diffusion | representative_instance_or_source_extension | 放入 source note 与 representative source row。 | 独立提升为基础概念。 | §4 |
| SISC | method/source_extension | 作为 FTS-Diffusion 的局部方法和 query key。 | 单独建成 foundation node。 | §4.1 |

## Knowledge 综合交接

- 应创建 Knowledge node:
  - `vault/04_Knowledge/ml-systems/synthetic-data-generation.md`
  - `vault/04_Knowledge/ml-systems/synthetic-data-generation/time-series-synthetic-data-generation.md`
- 应刷新 Knowledge synthesis section: ML systems root and research dynamics.
- 应标记过期: none.
- 无需更新的理由: Privacy/trustworthy ML 不更新为 durable route，因为本文没有 privacy/trust model。
- 建议 node kind: direction + problem/topic.

## 处理日志

- 2026-06-23: Deep-read local 12-page PDF, corrected queue classification from blockchain data availability to ML systems synthetic data generation, wrote source note and handed off for knowledge absorption.
