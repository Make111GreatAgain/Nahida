---
id: "doi-10-1109-access-2022-3144765-multidimensional-synthetic-data-generators"
title: "A Multi-Dimensional Evaluation of Synthetic Data Generators"
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
  - "Abstract, Sections I-V, Tables 1-13, Figures 1-5, Abbreviations, References"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1109/ACCESS.2022.3144765"
doi: "10.1109/ACCESS.2022.3144765"
arxiv_id: ""
venue: "IEEE Access"
year: "2022"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
topic_ids:
  - "synthetic-data-evaluation"
  - "tabular-synthetic-data-generation"
  - "synthetic-data-privacy-evaluation"
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
primary_ontology_path: "ml-systems/synthetic-data-generation/synthetic-data-evaluation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "synthetic-data-generation"
  topics:
    - "synthetic-data-evaluation"
    - "tabular-synthetic-data-generation"
    - "privacy-utility-tradeoff"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "synthetic-data-evaluation"
  - "tabular-synthetic-data-generation"
  - "data-utility"
  - "privacy-enhancing-technologies"
aliases:
  - "Multi-Dimensional Evaluation of Synthetic Data Generators"
  - "synthetic data utility dimensions"
  - "attribute fidelity bivariate fidelity population fidelity application fidelity"
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
    - "synthetic-data-evaluation"
    - "masked-data-utility-evaluation"
    - "synthetic-generator-comparison"
  method_family:
    - "multi-dimensional-utility-metrics"
    - "attribute-fidelity"
    - "bivariate-fidelity"
    - "population-fidelity"
    - "application-fidelity"
  system_layer:
    - "benchmark-and-evaluation"
    - "data-sharing"
  evaluation_context:
    - "19 tabular datasets"
    - "DataSynthesizer"
    - "Synthetic Data Vault"
    - "Synthpop parametric"
    - "Synthpop nonparametric"
    - "Hellinger distance"
    - "pairwise correlation difference"
    - "propensity score"
    - "classification accuracy and F1"
  bridge:
    - "synthetic-data-evaluation-to-synthetic-data-privacy-evaluation"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation"
source_refs:
  - "doi:10.1109/ACCESS.2022.3144765"
  - "sha256:72d0969739cec83ef8efbd094593096ac2b78ea7844a1337eb913bd784e8e237"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> synthetic-data-generation -> synthetic-data-evaluation"
secondary_directions:
  - "ml-systems -> synthetic-data-generation -> tabular-synthetic-data-generation"
  - "ml-systems -> synthetic-data-generation -> synthetic-data-privacy-evaluation"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read"
  - "Title, abstract, Methods, Results, Discussion and Conclusion all concern synthetic/masked data utility evaluation"
  - "The paper is not an arXiv paper despite queue inventory misreading DOI 10.1109/ACCESS.2022.3144765 as arxiv:2022.31447"
  - "The durable path is synthetic-data-generation/synthetic-data-evaluation, not privacy-and-trustworthy-ml/distributed-learning"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/A_Multi-Dimensional_Evaluation_of_Synthetic_Data_Generators.pdf"
pdf_sha256: "72d0969739cec83ef8efbd094593096ac2b78ea7844a1337eb913bd784e8e237"
pdf_pages: 12
pdf_size_bytes: 1644903
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/A_Multi-Dimensional_Evaluation_of_Synthetic_Data_Generators-72d0969739ce.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0097"
---

# A Multi-Dimensional Evaluation of Synthetic Data Generators

## 论文身份

- 标题: A Multi-Dimensional Evaluation of Synthetic Data Generators
- 作者: Fida K. Dankar, Mahmoud K. Ibrahim, Leila Ismail
- 机构: United Arab Emirates University; KU Leuven; INDUCE Research Laboratory
- 会议/期刊: IEEE Access
- 年份: 2022
- DOI: `10.1109/ACCESS.2022.3144765`
- 链接: https://doi.org/10.1109/ACCESS.2022.3144765
- 本地 PDF: `~/Desktop/paper/A_Multi-Dimensional_Evaluation_of_Synthetic_Data_Generators.pdf`
- SHA-256: `72d0969739cec83ef8efbd094593096ac2b78ea7844a1337eb913bd784e8e237`
- License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0, as stated on p1.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: Codex bundled Python `pdfplumber`
- 页数: 12
- 已覆盖章节/页码: p1-p12, Abstract, I Introduction, II Methods, III Results, IV Discussion, V Conclusion, Tables 1-13, Figures 1-5, References.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 表格数值在纯文本抽取中结构较差，source note 只记录正文可确认的核心表结论，不重建每个 table cell。
- 精读说明: 正文足以支持 source note、`synthetic-data-evaluation` evaluation-axis node、`tabular-synthetic-data-generation` refresh、以及 utility-vs-privacy bridge。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 既有 synthetic data generator 评价指标会产生冲突结论；论文把 utility metrics 分类为 attribute、bivariate、population、application 四个维度。 | high | 直接定位为 synthetic data evaluation。 |
| I Introduction / p1-p2 | 动机与贡献 | 数据共享受隐私与行政约束阻碍；synthetic data 被视为数据共享方案，但 generator utility 证据不足；贡献是多维评价与相关性分析。 | high | 解释为何不是新 generator 论文。 |
| II.A / p2 | SDG 介绍 | 比较四类开源 generator: DataSynthesizer, SDV, Synthpop parametric, Synthpop nonparametric。 | high | generator 是被评估对象，不是本文贡献。 |
| II.B-II.C / p2-p4 | 指标分类与定义 | 从 broad/specific utility measures 出发，形成四个 quality dimensions；代表指标是 Hellinger, PCD, propensity score, prediction accuracy/F1。 | high | 上层知识节点的核心。 |
| II.D-II.E / p5-p6 | 实验流程与设置 | 19 个数据集；4 次 70/30 holdout；每 split 每 generator 重复生成 5 次，共 20 个 synthetic datasets；AWS r5a.8xlarge。 | high | 支撑比较结论。 |
| III.A / p6-p7 | generator 比较 | SP-np 在平均结果和稳定性上总体最好；SDV 在 PCD 上接近 SP-np，DS 在 accuracy 上接近。 | high | source-specific evaluation result。 |
| III.A.2 / p7 | metric agreement | 四个指标很少完全同意同一个 winner；多数投票 63% 指向 SP-np，10.5% 指向 DS，另有 tie。 | high | 支持“单指标不足”。 |
| III.B / p8 | overall utility measure | 除 PCD-Hellinger 外，指标间相关性低于 0.4；没有单一指标可预测多维质量。 | high | 上层 synthesis 的关键 caveat。 |
| III.C-III.D / p8-p10 | application fidelity | SP-np 平均 accuracy loss 小于 3.5%，range 小于 6.5%；winning classifier 与真实数据匹配 79%，SDV 为 53%。 | high | application fidelity 细节。 |
| IV-V / p10 | 讨论与结论 | 多维指标都需要；本文能提示 multi-dimensional utility，但不能回答 utility 是否达到可接受水平，也不能回答 privacy trade-off。 | high | 连接 privacy evaluation bridge 的证据。 |
| References / p11-p12 | 参考文献 | 指向 CTGAN、DataSynthesizer、SDV、Synthpop、utility/privacy references。 | medium | 后续 foundation/research queue 线索。 |

## 核心精读笔记

### 背景、动机与问题边界

论文的问题不是“怎样设计新的 synthetic data generator”，而是“当多个 generator 都能生成 synthetic/masked data 时，怎样比较它们的 utility”。作者指出，合成数据被用作敏感数据共享的候选方案，尤其在医疗等受隐私法律、数据泄露担忧和数据访问行政流程影响的场景中很有吸引力；但 generator 的 utility 还没有被充分理解。

作者把现有研究的问题概括为: 不同论文使用不同 utility metrics，且这些指标可能给出冲突结论，因此很难直接比较 synthetic data generators。本文的贡献是把 utility metrics 按想要保留的性质分类，并用四个代表性指标在 19 个数据集上比较四个 generator。

重要边界:

- 本文把 synthetic data 视为 privacy enhancing technology (PET) 的一种使用场景，但没有提出新的隐私机制。
- 本文评价的是 utility/quality，不证明 synthetic data 一定匿名，也不提供 DP 或攻击模型。
- 本文使用 classification 作为 application fidelity 的代表应用，因此不能覆盖所有下游分析类型。

证据锚点: p1 Abstract; p1-p2 Introduction; p10 Discussion/Conclusion.

### 评价维度与代表指标

论文把 masked/synthetic data utility 拆成四个 quality dimensions。

| Dimension | 论文定义 | 代表指标 | 指标含义 | 方向 |
| --- | --- | --- | --- | --- |
| Attribute fidelity / univariate fidelity | 每个属性的基本结构、类型、范围、均值或单变量分布是否与真实数据接近。 | Hellinger distance | 对每个变量比较原始列和合成列的分布，再取平均。 | 越小越好 |
| Bivariate fidelity | 变量对之间的相关结构是否保留。 | Pairwise Correlation Difference (PCD) | 比较真实矩阵与合成矩阵的 pairwise correlation matrix，使用 Frobenius norm。 | 越小越好 |
| Population fidelity | 整体分布是否相似，尤其 synthetic rows 是否能被分类器与 real rows 区分。 | Propensity score / pMSE | 合并真实与合成数据，训练二分类器判断 row 来源；越不可区分越接近 0。 | 越小越好 |
| Application fidelity | 合成数据在具体分析/应用中能否替代真实数据训练模型或产生一致 inference。 | Prediction accuracy and F1 | 在 synthetic train set 上训练 LR/SVM/RF/DT，在 real test set 上测试。 | accuracy/F1 越接近真实训练越好 |

这个分类的上层价值是: synthetic data evaluation 不应只问“像不像真实数据”，也不应只问“下游任务是否可用”。单变量分布、变量间关系、整体分布可区分性、下游应用表现是不同对象，可能不一致。

证据锚点: p2-p4 Methods; Table 1; Figure 1.

### generator 对象与实验流程

本文比较四个 synthetic data generators。

| Generator | 论文中的简称 | 类别 | 机制概括 |
| --- | --- | --- | --- |
| DataSynthesizer | DS | Bayesian network statistical method | 学习属性间相关结构的 Bayesian network，再从模型采样。 |
| Synthetic Data Vault | SDV | Gaussian copula statistical method | 从 marginal distributions 和 Gaussian copula 估计 joint distribution，再采样。 |
| Synthpop parametric | SP-p | parametric ML/statistical synthesis | 按属性顺序合成，使用线性回归估计 conditional distributions。 |
| Synthpop nonparametric | SP-np | non-parametric tree-based synthesis | 按属性顺序合成，使用 CART 估计 conditional distributions。 |

实验设计:

- 数据集: 19 个不同大小和特征数的数据集，来源包括 UCI、OpenML、Datasphere、Cerner clinical database 和 Kaggle。
- 切分: 对每个真实数据集做 4 次随机 70%/30% holdout。
- 重复: 每个 split 上每个 generator 生成 5 个 synthetic datasets，因此每个 dataset-generator pair 有 20 个 synthetic datasets。
- 长度: 合成数据集长度与真实训练数据相同。
- 输入: 使用 raw unprocessed real datasets 作为 synthesizer 输入。
- 工具: AWS r5a.8xlarge；R `mice` 做 imputation；R `twang` 的 GBM propensity score；Python scikit-learn 做分类模型；Python Kmodes/Kprototype 支持混合数值/类别数据聚类。

证据锚点: p2 SDG descriptions; p5-p6 data generation process and setup.

### 主要结果

1. SP-np 是本文实验中的总体赢家。
   - SP-np 在四个 quality metrics 的平均表现上最好，并在 application fidelity、population fidelity、bivariate fidelity 的稳定性上最好。
   - SDV 在 PCD 上接近 SP-np；DS 在 accuracy 上接近。
   - 作者建议，如果私有数据要公开共享且用途未知或多样，SP-np 生成多个 synthetic datasets 的 ensemble 可能提供最高质量。

2. 指标之间不总是同意。
   - 在逐数据集、逐指标判断 winner 时，四个指标很少完全一致；完全一致的例外只有 D8、D11 和 D19。
   - 多数投票时，63% 指向 SP-np，10.5% 指向 DS，另有 SP-np/DS 或 SP-np/SDV tie。
   - exact winner 的 Cohen kappa 从 slight 到 moderate；若放宽到 top-two agreement，则指标间接近 substantial 或 almost perfect。

3. 没有单一 overall utility metric。
   - 除 PCD 和 Hellinger 之间存在中等相关外，其他 pairwise correlations 都较低，正文给出的阈值是 `<0.4`。
   - 作者结论是所有 quality metrics 都需要；PCD-Hellinger 的关系可能提示未来某些数据集不必同时计算二者，但仍需更多实验验证。

4. application fidelity 结果支持 SP-np。
   - 如果用 prediction accuracy 作为性能指标，SP-np 在 DT、LR、RF 上 accuracy loss 最低，在 SVM 上 DS 略优但 SP-np 相差不到 1 个百分点。
   - SP-np 平均 accuracy loss 小于 3.5%，跨所有数据集的 range 小于 6.5%。
   - winning classifier 与真实数据训练结果的匹配率中，SP-np 最高为 79%，SDV 为 53%。

证据锚点: p6-p10 Results; p10 Discussion.

### 限制与 caveat

- utility 不等于 privacy: 论文反复在 PET/data sharing 背景下讨论合成数据，但实验证据只覆盖 utility dimensions，不覆盖 membership/attribute inference、DP 或 release workflow。
- representative metric 不等于全部指标: 每个 dimension 只选一个代表性指标，适合作为本文比较框架，但不能替代完整 evaluation toolbox。
- application fidelity 只选 classification: 作者选择 LR/SVM/RF/DT 和 accuracy/F1，因为 classification 常用于 synthetic data evaluation；这不代表所有下游统计分析、因果分析、回归或业务规则。
- 表格/结构化数据语境更强: 本文 generator 和数据集主要是 tabular/microdata style；不要直接外推到图像、文本、时序或 relational/multi-table synthetic data。
- 不能回答 acceptable threshold: 结论能帮助判断哪个 SDG multi-dimensional utility 更好，但不能回答在医疗等应用中保留多少 utility 才可接受，或在不损害 privacy 下可保留多少 utility。

证据锚点: p5 application fidelity caveat; p10 Conclusion.

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Notes |
| --- | --- | --- | --- | --- |
| Research field/domain | `ml-systems` | Synthetic data generators are ML/data systems artifacts used for data sharing and downstream ML analysis. | high | 不是 distributed learning。 |
| Research background | synthetic data generation; privacy enhancing technologies; data sharing | p1-p2 motivation. | high | PET 背景是 motivation，不是主要贡献。 |
| Research problem | synthetic data evaluation / masked data utility evaluation | Abstract and Methods classify utility metrics. | high | 适合作为 evaluation_axis knowledge node。 |
| Foundation concepts | synthetic data generation; data utility; fidelity/utility/privacy distinction | p2-p4 metric classification; p10 caveat. | medium | `data utility` 可作为 query key，未单建 foundation。 |
| Method family | multi-dimensional utility metrics | four quality dimensions. | high | 上层吸收为方法路线。 |
| Application/evaluation context | tabular/microdata synthetic datasets; healthcare data sharing motivation | 19 datasets, generator list, p10 healthcare discussion. | high | 主要刷新 tabular synthetic data。 |
| Artifact/source instance | this IEEE Access paper | DOI and full PDF. | high | 留在 source note。 |

## 检索优化判断

- 这个 source 应该帮助哪些 Knowledge node 变得更容易查询: [[synthetic-data-evaluation|Synthetic data evaluation]], [[synthetic-data-generation|Synthetic data generation]], [[tabular-synthetic-data-generation|Tabular synthetic data generation]], [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]].
- 哪些未来问题可以因此少读 source: “synthetic data generator 怎么评估”, “fidelity/utility metrics 分几类”, “Hellinger/PCD/propensity/accuracy 分别衡量什么”, “为什么单一 utility metric 不够”, “utility 和 privacy 是不是一回事”.
- 哪些内容只应留在 source，不应进入上层: 本文 19 个数据集每个具体数值、所有 table cell、AWS instance、R/Python package 调用细节、SP-np 在本文实验中的具体排名细节。

## Knowledge/Bridge 候选

| 候选内容 | 类型 | 目标 knowledge/bridge | 证据 | 决策 |
| --- | --- | --- | --- | --- |
| Synthetic data evaluation | evaluation_axis knowledge | `ml-systems/synthetic-data-generation/synthetic-data-evaluation` | 四个 quality dimensions 和 correlation 结论 | create active_seed |
| Four utility dimensions | method route | `synthetic-data-evaluation` 方法族 | p2-p4 | promote as method table, not separate notes |
| SP-np as best generator in this experiment | source extension | source note and representative source row | p6-p10 | keep source-local; do not make SP-np foundation |
| Utility vs privacy boundary | bridge | [[synthetic-data-evaluation-to-synthetic-data-privacy-evaluation|Synthetic data evaluation -> synthetic data privacy evaluation]] | p10 states utility result does not set privacy trade-off | create active_seed bridge |
| DataSynthesizer / SDV / Synthpop | generator instances | tabular/synthetic data source extension | p2 | no standalone nodes yet |

## 可复用记忆

- 可更新 knowledge node: [[synthetic-data-generation|Synthetic data generation]], [[tabular-synthetic-data-generation|Tabular synthetic data generation]].
- 可新建 knowledge node: [[synthetic-data-evaluation|Synthetic data evaluation]].
- 可形成 bridge: [[synthetic-data-evaluation-to-synthetic-data-privacy-evaluation|Synthetic data evaluation -> synthetic data privacy evaluation]], relation types `tension`, `evaluation_transfer`, `privacy_boundary`.
- 应留在 source 内的内容: 全部 table-level numeric results、实验机器配置、每个数据集 winner。
- 需要联网补充的 foundation knowledge: 若未来要把 evaluation node 从 active_seed 提升为 evergreen，需要补 stable survey/foundation sources for SDMetrics/SDGym/utility evaluation guidelines。
- 后续应读: `alaa22a.pdf / How Faithful is your Synthetic Data?` 应优先接到同一 `synthetic-data-evaluation` 节点。

## 处理日志

| Date | Run ID | Action |
| --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-multidimensional-synthetic-data-evaluation | Deep-read local PDF, corrected queue identity from false arXiv to DOI, created source note, and handed off to knowledge absorption. |
