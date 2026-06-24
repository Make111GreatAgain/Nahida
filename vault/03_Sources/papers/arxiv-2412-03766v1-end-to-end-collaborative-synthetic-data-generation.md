---
id: "arxiv-2412-03766v1-end-to-end-collaborative-synthetic-data-generation"
title: "End to End Collaborative Synthetic Data Generation"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
source_kind: "pdf"
source_subtype: "paper_arxiv"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p15 full extracted text"
  - "Abstract, Sections 1-5, Algorithms 1-6, Tables 1-2, References, and Appendix A"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2412.03766v1"
doi: ""
arxiv_id: "2412.03766v1"
venue: "arXiv preprint"
year: "2024"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "synthetic-data-generation"
topic_ids:
  - "collaborative-synthetic-data-generation"
  - "privacy-preserving-synthetic-data"
  - "synthetic-data-privacy-evaluation"
  - "tabular-synthetic-data-generation"
ontology_path:
  - "ml-systems"
  - "synthetic-data-generation"
  - "collaborative-synthetic-data-generation"
primary_ontology_path: "ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation"
secondary_ontology_paths:
  - "ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation"
  - "ml-systems/synthetic-data-generation/tabular-synthetic-data-generation"
  - "ml-systems/privacy-and-trustworthy-ml"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "synthetic-data-generation"
    - "privacy-and-trustworthy-ml"
  topics:
    - "collaborative-synthetic-data-generation"
    - "privacy-preserving-synthetic-data"
    - "MPC-based synthetic data generation"
    - "DP synthetic data release"
domains:
  - "ml-systems"
topics:
  - "synthetic-data-generation"
  - "collaborative-synthetic-data-generation"
  - "privacy-preserving-synthetic-data"
  - "synthetic-data-privacy-evaluation"
  - "tabular-synthetic-data-generation"
  - "secure-multiparty-computation"
  - "differential-privacy"
aliases:
  - "EndSDG"
  - "collaborative private synthetic data generation"
  - "privacy-preserving collaborative SDG"
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
    - "collaborative-synthetic-data-generation"
    - "multi-custodian synthetic data publishing"
    - "input-and-output-private synthetic data release"
  method_family:
    - "secure multiparty computation"
    - "DP-in-MPC"
    - "select-measure-generate synthetic data"
    - "Private-PGM"
    - "privacy-preserving hyperparameter tuning"
  system_layer:
    - "MPC-as-a-service"
    - "privacy-preserving preprocessing"
    - "privacy-preserving evaluation"
    - "synthetic data publishing pipeline"
  evaluation_context:
    - "synthetic genomic data for leukemia"
    - "quantile binning"
    - "workload error"
    - "logistic regression utility"
    - "MP-SPDZ runtime"
  application:
    - "rare disease data collaboration"
    - "genomic data sharing"
    - "regulated multi-organization data release"
  bridge:
    - "synthetic-data-generation-to-privacy-and-trustworthy-ml"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-collaborative-synthetic-data-generation"
source_refs:
  - "arxiv:2412.03766v1"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> synthetic-data-generation"
secondary_directions:
  - "ml-systems -> privacy-and-trustworthy-ml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p15"
  - "Title, abstract and Algorithm 1 define an end-to-end synthetic data generation pipeline over multiple data custodians"
  - "The paper's core contribution is collaborative SDG with MPC input privacy, DP output privacy, preprocessing, evaluation and hyperparameter tuning"
  - "It is not just generic distributed learning; the durable problem is privacy-preserving collaborative synthetic data publishing"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/2412.03766v1.pdf"
pdf_sha256: "57ff6c267317d2640930123a87d20691075446a41b7a7fa92707adfa6dbe2a79"
pdf_pages: 15
pdf_size_bytes: 341833
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/2412.03766v1-57ff6c267317-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0094"
---

# End to End Collaborative Synthetic Data Generation

## 论文身份

- 标题: End to End Collaborative Synthetic Data Generation
- 作者: Sikha Pentyala; Geetha Sitaraman; Trae Claar; Martine De Cock
- 机构: University of Washington Tacoma
- 会议/期刊: arXiv preprint
- 年份: 2024
- DOI: unknown
- arXiv: `2412.03766v1`
- 链接: https://arxiv.org/abs/2412.03766v1
- 本地 PDF: `~/Desktop/paper/2412.03766v1.pdf`
- SHA-256: `57ff6c267317d2640930123a87d20691075446a41b7a7fa92707adfa6dbe2a79`
- 代码: paper footnote gives an anonymous work-in-progress repository URL; not analyzed in this run.
- 数据: leukemia bulk RNA-seq dataset from PRO-GENE-GEN is used only as demonstration evidence.
- License: unknown in local PDF

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: queue extraction text
- 页数: 15
- 已覆盖章节/页码: p1-p15, Abstract, Sections 1-5, Algorithms 1-6, Tables 1-2, References, Appendix A.
- 已检查附录: yes, Appendix A covers MPC threat models, primitives, Gaussian noise and DP quantile-binning caveat.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: algorithms contain line-wrap and bracket noise, but the framework, protocol roles, experiments and caveats are readable.
- 精读说明: 正文足以支持 source note、collaborative synthetic data generation problem node、synthetic-data/privacy bridge refresh 和 ML systems dynamics refresh。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 多 data custodians 需要协作生成合成数据；现有 federated SDG 多只覆盖 synthesizer training；本文给出包含 preprocessing、evaluation、hyperparameter tuning 的端到端框架。 | high | 直接定位为 collaborative SDG。 |
| §1 / p1-p4 | 动机和系统边界 | rare disease/regulated data sharing 场景；input privacy 由 MPC，output privacy 由 DP；不发布中间输出以避免多轮 tuning 累积隐私预算。 | high | 上层问题定义。 |
| §2 / p4 | 预备知识 | MPC secret sharing、DP、select-measure-generate SDG、Private-PGM。 | medium | 基础概念留给上层短定义；细节不升节点。 |
| §3 / p5-p6 | Framework | Algorithm 1: data custodians secret-share data/thresholds；MPC servers concat, k-fold train/evaluate, private threshold voting, final preprocess/train/reverse-preprocess/publish。 | high | 可复用 pipeline 结构。 |
| §4 / p6-p10 | Leukemia genomic use case | 958 genes + labels；quantile binning；Private-PGM noisy marginals；MPC protocols for binning, inverse binning, noisy marginals, workload error and LR evaluation。 | high | Source-specific instantiation。 |
| §4.4 / p10-p11 | Empirical evaluation | Utility/fidelity table and MP-SPDZ runtime table; 3PC passive is far faster than 2PC passive for key protocols; framework feasible but computationally heavy。 | medium | 实验数值留在 source。 |
| §5 / p11 | Conclusion | Framework produces synthetic data across silos with MPC input privacy and DP output privacy; genomic synthetic data quality remains open; optimized protocols are future work。 | high | caveat 清楚。 |
| Appendix A / p13-p15 | MPC/DP implementation notes | threat models, replicated sharing, MPC primitives, Gaussian noise, fixed-point DP implementation, DP quantile binning caveat。 | medium | 支撑安全/限制边界。 |

## 核心精读笔记

### 背景、动机与问题边界

这篇论文处理的是多数据持有方场景下的合成数据发布。单个机构可以在本地训练 synthesizer 并发布合成数据，但 rare disease、跨医院 genomics、金融或合规场景经常需要多个 custodians 汇总数据规模和覆盖度。直接集中原始数据会违反隐私、治理或商业约束。

作者把隐私拆成两层:

- Input privacy: 数据持有方不向任何单个实体披露原始数据；本文用 MPC servers 计算 secret-shared data 来实现。
- Output privacy: 最终发布的 synthetic data 或 generator 不泄露单个训练记录；本文用 DP 机制处理 preprocessing/training 中会影响最终发布数据的步骤。

现有 collaborative/federated SDG 工作常只处理 synthesizer training，而且假设预处理后的数据已经可用、一次性生成并发布。作者指出这与真实 SDG pipeline 不符: 数据通常要 discretization/binning，生成质量要用真实 held-out data 评估，hyperparameter tuning 可能需要多轮迭代。如果每轮都发布模型、metrics 或 synthetic data，就会消耗 DP privacy budget 或直接泄露隐私。

本文明确不解决所有合成数据问题。它不是新的通用 synthesizer，也不是 optimized MPC library；genomic SDG 的质量仍有限，DP quantile binning 也被列为 ongoing work。

证据锚点: Abstract; §1; §3; Appendix A.5.

### 模型、假设与定义

系统包含 `n` 个 data custodians `C1..Cn` 和 `m` 个 non-colluding independent MPC servers `S1..Sm`。每个 custodian 将私有数据 `Di` 和质量阈值 `Ti` secret-share 给 MPC servers。MPC servers 在 secret-shared combined dataset `D = union Di` 上运行 pipeline，模拟 centralized setting，但任何服务器都不能单独恢复原始输入。

框架中有三类协议:

- `pi_PREPROCESS`: 对 secret-shared data 做 privacy-preserving preprocessing。
- `pi_SDG`: 在 secret-shared preprocessed data 上训练 synthetic data generator 或生成 noisy measurements。
- `pi_EVAL`: 在 MPC 中评估 synthetic data 的质量，不发布 evaluation metrics。

DP budget 被分成 preprocessing budget `(epsilon_p, delta_p)` 和 SDG training budget `(epsilon_s, delta_s)`。关键点是: k-fold tuning 期间运行的 DP preprocessing/training 不发布 outputs，也不发布 metrics；只有最后满足 threshold 后在完整 combined data 上用选定 hyperparameters 运行一次并发布最终 synthetic data。因此作者声称整体发布消耗保持为目标 epsilon，而不是每次 tuning loop 叠加。

证据锚点: §2; Algorithm 1; §3 narrative.

### 方法、协议或系统机制

Algorithm 1 是本文最重要的系统结构:

1. Data custodians secret-share data 和 quality thresholds。
2. MPC servers 用 `pi_CONCAT` 拼接 secret shares，得到 combined dataset 的 secret shares。
3. 每个 hyperparameter candidate 触发一次 k-fold loop。
4. 每个 fold 内，对 train split 运行 `pi_PREPROCESS`，再运行 `pi_SDG`，然后用 `pi_EVAL` 在 secret shares 上计算质量指标。
5. MPC servers 对 k-fold metrics 做平均，但不发布平均值。
6. 每个 custodian 的阈值也保持 secret-shared；servers 只做 privacy-preserving comparison/voting，判断是否所有 custodians 都接受当前结果。
7. 若通过 threshold，使用当前 hyperparameters 在完整 combined data 上重新运行 preprocess + SDG + reverse preprocess，并只 reveal 最终 synthetic data。
8. 若未通过，换 hyperparameters 继续；若达到 max loops 或无候选，则不发布。

Leukemia genomic use case 中，作者将 continuous gene expression values 做 quantile binning，把每个 gene 变成 4 个离散 bins，label 仍是 5 类。之后用 Private-PGM 风格的 select-measure-generate route: 计算所有 1-way marginals 和 label 相关 2-way marginals，共 1,917 个 noisy marginals。隐私预算均匀分给这些 measurements。

MPC 协议细节包括:

- `pi_BIN`: 用 MPC sorting 计算 quantiles，再用 secure less-than comparison 将每个 gene expression 值映射到 bin，并记录每个 bin 的原始均值用于 de-binning。
- `pi_INV-BIN`: 将合成数据中的 bin value 替换为对应 secret-shared mean。
- `pi_NOISY-MARG`: 用 indicator polynomials 替代 expensive equality tests，计算 gene/label 1-way and 2-way marginals，并在 MPC 内加入 Gaussian noise。
- `pi_WLE`: 在 MPC 内计算 synthetic 与 real 的 normalized workload error。
- Logistic regression evaluation: 使用 MP-SPDZ 中 Dense/Softmax 相关 primitives 训练和评估多分类模型。

证据锚点: Algorithm 1; Algorithms 2-5; §4.1-§4.3.

### 理论、证明或正确性论证

本文不是形式化安全证明论文。它依赖 MPC 的标准组合安全和 secret-sharing threat models，并在 Appendix A 回顾 passive/active adversary 设置与 replicated sharing。作者使用 universal composition theorem 说明模块化 MPC protocols 可组合。

DP 方面，本文的主要论证是 budget accounting 和 release boundary: 未发布的 intermediate synthetic data、models、metrics 和 votes 不构成公开输出，因此多轮 hyperparameter tuning 不像反复发布 DP synthetic datasets 那样累加公开 privacy loss。最终发布仍要通过 DP preprocessing/training 保护。这个论证依赖 implementation 不泄露中间结果和阈值/votes。

重要 caveat: Appendix A.5 明确说理想上需要 DP quantile binning；当前 `pi_BIN` 计算 exact quantiles but is not yet DP。作者正在探索 DP quantile methods 和 alternative preprocessing。实验中 generate step 也有部分 cleartext simplification，因此不能把本文读成完整优化、生产就绪的端到端实现。

证据锚点: §3; Appendix A; Appendix A.4-A.5; §4.4 footnotes.

### 实验、评估或案例

Use case 是 leukemia bulk RNA-seq:

- 1,181 samples，5 个 disease categories，其中 4 类 leukemia 和 1 类 Other。
- 原始 12k genes 降到 958 genes。
- Synthetic data quality 用两类指标观察:
  - Logistic regression/decision-tree downstream utility: 比较真实训练集和合成训练集训练出的模型在真实 test set 上的 accuracy/F1 difference。
  - Workload error: 对 1-way marginals 的 normalized marginal error。
- 实验模拟 2 个 data custodians 和 3 个 MPC servers；Private-PGM iterations 的候选 hyperparameters 是 `{10, 15, 25, 30}`。

Table 1 显示 combined preprocessing 对 logistic regression utility 有帮助: `Ours` 的 LR accuracy difference 为 0.003，而 local preprocessing 为 0.026；decision-tree/F1 结果仍有差异，作者因此强调 genomic synthetic data quality 仍是 open challenge。

Table 2 显示 MPC runtimes:

- 3PC passive 下关键 protocols 总体约 2.5 小时量级；`pi_BIN` 约 82.93 秒，`pi_NOISY-MARG` 约 249.50 秒，`pi_WLE` 约 158.66 秒，LR 150 epochs 约 15.42 秒。
- 2PC passive 明显更慢，`pi_BIN` 达 18,259.66 秒。
- active security 通常更贵；作者认为结果说明 feasible，但优化仍是 future work。

证据锚点: §4.4; Tables 1-2.

### 作者结论与我的判断

作者明确声称本文是首个面向多 silos、同时覆盖 preprocessing、evaluation、hyperparameter tuning、input privacy 和 output privacy 的 collaborative SDG framework。它通过 DP-in-MPC 追求类似 centralized global DP 的 fidelity/utility，同时避免依赖一个 trusted central aggregator。

由证据支持的判断: 本文应归入 `ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation`，并刷新 synthetic data privacy evaluation 与 privacy/trustworthy ML。它的持久贡献不是某个基因数据实验，而是把多数据持有方的合成数据发布从“只训练 synthesizer”扩成“预处理、调参、评估、最终发布都在隐私边界内”的 pipeline problem。

仍需谨慎的推断: 当前 implementation 是 work-in-progress；DP quantile binning 尚未完成；Private-PGM generate step 仍有 cleartext simplification；数据集单一且高维 genomics quality 仍困难；代码仓库未分析。因此上层应把它作为 active seed，而非成熟生产模式或完整 DP/MPC foundation。

## 层级候选分类

- L1 Domain candidate: `ml-systems`
- L2 Direction candidate: `synthetic-data-generation`
- L3 Topic/content cluster candidates: `collaborative-synthetic-data-generation`, `privacy-preserving-synthetic-data`, `synthetic-data-privacy-evaluation`
- Ontology path: `ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation`
- 备选归属: `ml-systems/privacy-and-trustworthy-ml`, `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation`, `ml-systems/synthetic-data-generation/tabular-synthetic-data-generation`
- 父级领域: ML systems
- 学术子领域: privacy-preserving data synthesis; secure collaborative analytics
- 任务/问题: 多 data custodians 在不集中原始数据、不泄露中间 metrics 的情况下调参并发布 DP synthetic data
- 方法族: MPC, DP-in-MPC, select-measure-generate SDG, Private-PGM, secure evaluation
- 模型/协议/算法族: `pi_BIN`, `pi_NOISY-MARG`, `pi_WLE`, private threshold voting
- 评测场景: leukemia genomic synthetic data, workload error, LR/DT utility, MP-SPDZ runtime
- Benchmark/应用: rare disease/genomic data sharing
- 别名: EndSDG; collaborative private synthetic data generation
- 相邻方向: privacy and trustworthy ML; tabular synthetic data; DP synthetic data release
- 置信度: high
- 分类理由: 全文目标是 synthetic data publishing pipeline；distributed/federated learning 只是数据分布形态，不是主要对象。
- 分类状态: corrected_from_queue
- 分类证据: abstract, Algorithm 1, §4 protocols and experiments.
- Taxonomy version: 1.0

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | ML systems | SDG pipeline, MPC servers, privacy budgets, evaluation, runtime. | high | durable parent |
| Research background | privacy-preserving synthetic data release across silos | rare disease and PETs Prize motivation; multi-custodian constraints. | high | knowledge background |
| Research problem | collaborative synthetic data generation | framework handles preprocessing, training, evaluation, tuning, final publishing. | high | create problem node |
| Foundation concepts | MPC; DP; synthetic data generation | Sections 2 and Appendix A. | high | link/short-define; do not create here |
| Method family | DP-in-MPC SDG pipeline | Algorithm 1 and protocols 2-5. | high | method route inside problem node |
| Application/evaluation context | synthetic genomic data for leukemia | Section 4 and Tables 1-2. | high | source extension |
| Artifact/source instance | this framework and naive protocols | Algorithm 1 plus MP-SPDZ implementation. | high | source-local instance |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]]
- 它能帮助未来哪些问题少读 source notes: “多个医院/机构如何协作生成合成数据”“synthetic data 的 input privacy/output privacy 区别是什么”“为什么 hyperparameter tuning 不能随便发布 metrics”“MPC 和 DP 如何组合到 SDG pipeline”
- 哪些内容应留在 source note，而不是创建上层节点: `pi_BIN` 算法细节、indicator polynomial 公式、leukemia dataset 数值、MP-SPDZ runtime 表格、Private-PGM 参数。
- 哪些上层节点过薄、缺失或需要 foundation_pack: DP synthetic data release、privacy-preserving data release、MPC foundation。
- 哪些候选只是别名/query key/watch term: EndSDG, CaPS, DP-in-MPC synthetic data, secure generation and publishing.

## 证据记录

| 事实/观察 | 证据位置 | 置信度 | 时效性 | 上层处理 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 本文核心问题是多 data custodians 协作生成并发布合成数据。 | Title, Abstract, §1 | high | stable | create collaborative synthetic data generation node | Queue 原分到 distributed learning 过宽。 |
| 框架覆盖 preprocessing、SDG training、evaluation、hyperparameter tuning 和 final publishing。 | Algorithm 1, §3 | high | stable | problem node 方法路线 | 这是相对既有 work 的主要 delta。 |
| Input privacy 通过 MPC servers 上的 secret-shared computation 实现。 | §2, §3, Appendix A | high | stable | privacy/trustworthy ML bridge | 依赖 non-colluding MPC server threat model。 |
| Output privacy 通过 DP preprocessing/training 保护最终发布数据。 | §1, §3 | high | stable | synthetic data privacy evaluation | DP quantile binning 仍未完成。 |
| Tuning 阶段不发布 synthetic data、models、metrics 或 votes，以避免多轮公开输出累加 privacy budget。 | §1, Algorithm 1 narrative | high | stable | knowledge node problem/method | 依赖实现不泄露中间结果。 |
| Leukemia genomic experiment 说明 combined privacy-preserving preprocessing 可改善部分 utility。 | §4.4 Table 1 | medium | source-specific | source-local evidence only | 不泛化到所有 genomics。 |
| MPC runtime feasible but expensive; 2PC passive especially慢。 | §4.4 Table 2 | medium | source-specific | limitations/source note | 后续需 optimized protocols。 |
| 当前 exact quantile binning 不是 DP，DP quantile binning 是 future work。 | Appendix A.5 | high | stable | caveat in knowledge node | 不能把框架写成完整生产 DP implementation。 |

## Knowledge/Bridge 候选

| 候选内容 | 类型 | 目标 knowledge/bridge | 证据 | 决策 |
| --- | --- | --- | --- | --- |
| Collaborative synthetic data generation | knowledge problem/topic | `ml-systems/synthetic-data-generation/collaborative-synthetic-data-generation` | 全文问题、Algorithm 1 和 use case | create active_seed |
| Synthetic data privacy evaluation | knowledge update | `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` | input/output privacy, DP budget, private metrics/tuning | update |
| Synthetic data generation -> privacy and trustworthy ML | bridge update | existing bridge | MPC + DP turn release pipeline into trust boundary | update |
| MPC-based Private-PGM protocols | method/source instance | source extension only | Algorithms 2-5 | do not create node yet |
| DP quantile binning | gap/foundation candidate | future DP synthetic data release/preprocessing node | Appendix A.5 | queued, no standalone node now |

## 基础概念候选判断

| 候选术语/方法 | 是否足够通用 | 正确处理 | 错误处理 | 证据 |
| --- | --- | --- | --- | --- |
| Collaborative synthetic data generation | yes, reusable problem | 建成 synthetic data generation 下的问题节点 | 只写成本文摘要 | Algorithm 1 and motivation |
| Secure multiparty computation | yes, foundation concept | 在 source 和上层短定义，未来可补 foundation | 把本文的 MPC protocols 当成 MPC 基础定义 | §2, Appendix A |
| Differential Privacy | yes, foundation concept | 作为 output privacy route and DP release boundary | 把本文当成完整 DP foundation | §2, §3 |
| `pi_BIN`, `pi_NOISY-MARG`, `pi_WLE` | source-specific protocol instances | 留在 source note，作为方法路线例子 | 独立升为通用概念 | §4 |
| Private-PGM | representative synthesizer family instance | 作为 select-measure-generate SDG route | 当作 synthetic data generation 本身 | §2, §4 |

## 连接

- 相关 Knowledge nodes:
  - [[synthetic-data-generation|Synthetic data generation]]
  - [[collaborative-synthetic-data-generation|Collaborative synthetic data generation]]
  - [[synthetic-data-privacy-evaluation|Synthetic data privacy evaluation]]
  - [[tabular-synthetic-data-generation|Tabular synthetic data generation]]
  - [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]
- 相关 Bridges:
  - [[synthetic-data-generation-to-privacy-and-trustworthy-ml|Synthetic data generation -> privacy and trustworthy ML]]
- Bridge 候选: existing bridge refresh; endpoints remain `ml-systems/synthetic-data-generation/synthetic-data-privacy-evaluation` and `ml-systems/privacy-and-trustworthy-ml`, with collaborative SDG as source-backed subproblem evidence.

## 处理日志

| Date | Run ID | Action | Notes |
| --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-collaborative-synthetic-data-generation | deep_read_complete | Full local extracted PDF read and absorbed into Source + Knowledge + Bridge architecture. |
