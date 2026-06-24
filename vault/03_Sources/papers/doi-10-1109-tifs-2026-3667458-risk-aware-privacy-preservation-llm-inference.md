---
id: "doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference"
title: "Risk-Aware Privacy Preservation for LLM Inference"
type: "source"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "absorbed"
source_kind: "pdf"
source_subtype: "paper_doi"
reading_depth: "deep_read"
reading_status: "deep_read_complete"
reading_coverage:
  - "p1-p16 full extracted text"
  - "Abstract, Sections I-VIII, Tables I-X, Figures 1-8, References, and author bios"
safe_for_absorption: true
canonical_url: "https://doi.org/10.1109/TIFS.2026.3667458"
doi: "10.1109/TIFS.2026.3667458"
arxiv_id: ""
venue: "IEEE Transactions on Information Forensics and Security"
year: "2025"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "llm-inference-privacy"
  - "privacy-preserving-prompt-engineering"
  - "local-differential-privacy"
  - "text-sanitization"
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "llm-inference-privacy"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-inference"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
  directions:
    - "privacy-and-trustworthy-ml"
  topics:
    - "llm-inference-privacy"
    - "privacy-preserving-prompt-engineering"
    - "risk-aware-local-differential-privacy"
    - "prompt-text-sanitization"
domains:
  - "ml-systems"
topics:
  - "llm-inference-privacy"
  - "privacy-preserving-prompt-engineering"
  - "local-differential-privacy"
  - "text-sanitization"
  - "personally-identifiable-information"
  - "prompt-privacy"
aliases:
  - "Rap-LI"
  - "Risk-aware privacy preservation for LLM inference"
  - "risk-aware LDP prompt sanitization"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/ml-systems"
  - "nahida/privacy-and-trustworthy-ml"
direction_facets:
  parent_domain:
    - "ml-systems"
  subdomain:
    - "privacy-and-trustworthy-ml"
  problem:
    - "llm-inference-privacy"
    - "prompt PII leakage"
    - "contextual privacy leakage"
  method_family:
    - "local differential privacy"
    - "risk-aware token sanitization"
    - "privacy-preserving prompt engineering"
    - "personalized differential privacy"
  system_layer:
    - "user-side prompt preprocessing"
    - "black-box cloud LLM inference"
    - "interactive privacy labeling"
  evaluation_context:
    - "AGNews"
    - "PIIDocs"
    - "SAMSum"
    - "SpamEmail"
    - "SynthPAI"
  application:
    - "cloud LLM inference"
    - "privacy-preserving LLM chat"
  bridge:
    - "llm-inference-privacy-to-zkml-verifiable-inference"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-risk-aware-llm-inference-privacy"
source_refs:
  - "doi:10.1109/TIFS.2026.3667458"
confidence: "high"
trust_tier: "primary"
primary_direction: "ml-systems -> privacy-and-trustworthy-ml"
secondary_directions:
  - "zero-knowledge-proofs -> zkml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "local PDF deep read p1-p16"
  - "Title, abstract and Sections I-V target prompt privacy for black-box/cloud LLM inference"
  - "The paper's core contribution is risk-aware LDP text sanitization, not distributed learning"
  - "The false arXiv id came from the DOI string and was cleared"
taxonomy_version: "1.0"
local_pdf_path: "~/Desktop/paper/Risk-Aware_Privacy_Preservation_for_LLM_Inference.pdf"
pdf_sha256: "a2dc5788140e910d188d479394c2326aa2e806a36d7ab04aabc16440af08de93"
pdf_pages: 16
pdf_size_bytes: 2730139
pdf_extracted_text_path: "vault/02_Raw/pdf/extracted/risk-aware-privacy-preservation-for-llm-inference-a2dc5788140e-pages.txt"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0112"
---

# Risk-Aware Privacy Preservation for LLM Inference

## 论文身份

- 标题: Risk-Aware Privacy Preservation for LLM Inference
- 作者: Zhihuang Liu; Zhangdong Wang; Tongqing Zhou; Yonghao Tang; Yuchuan Luo; Zhiping Cai
- 机构: College of Computer Science and Technology, National University of Defense Technology
- 会议/期刊: IEEE Transactions on Information Forensics and Security
- 年份: 2025
- DOI: `10.1109/TIFS.2026.3667458`
- arXiv: none in local PDF
- 链接: https://doi.org/10.1109/TIFS.2026.3667458
- 本地 PDF: `~/Desktop/paper/Risk-Aware_Privacy_Preservation_for_LLM_Inference.pdf`
- SHA-256: `a2dc5788140e910d188d479394c2326aa2e806a36d7ab04aabc16440af08de93`
- 代码: https://github.com/Cristliu/RapLI, not analyzed in this run.
- 数据: AGNews, PIIDocs, SAMSum, SpamEmail, SynthPAI.
- License: IEEE author version notice in local PDF; code license not checked.

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: bundled Python `pypdf`
- 页数: 16
- 已覆盖章节/页码: p1-p16, Abstract, Sections I-VIII, Tables I-X, Figures 1-8, References and author bios.
- 已检查附录: local PDF has no appendix pages despite text referring to appendices.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: Figures/tables contain PDF font encoding noise, but section text, formulas, tables and conclusions are readable.
- 精读说明: 正文足以支持 source note、新建 `llm-inference-privacy` 问题节点、刷新 `privacy-and-trustworthy-ml` 与 ML systems dynamics，并创建一条与 zkML verifiable inference 的边界 bridge。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | Cloud LLM prompt 会暴露 PII/contextual privacy；uniform-budget LDP text sanitization 可能在 `epsilon=0.1` 下仍有 71.74% sensitive leakage；提出 Rap-LI。 | high | 直接定位到 LLM inference privacy。 |
| §I / p1-p2 | 动机和挑战 | 黑盒/cloud LLM 无法要求服务端协作；简单 masking、local LLM rewrite、uniform LDP 都难同时满足隐私与 utility。 | high | 说明为什么是 user-side prompt protection。 |
| §II / p2-p3 | 相关工作 | 比较 DP-FUSION、SnD、InferDPT、SanText、CusText、HaS、Kan 等 prompt/text privacy 方法。 | high | 给出方法边界。 |
| §III / p3-p4 | 预备知识 | LLM inference prompt decomposition、epsilon-LDP、exponential mechanism、token sanitization。 | medium | 基础概念留给上层节点。 |
| §IV / p4-p6 | Threat model and limitations | 服务提供者/LLM API adversary；MaskInf、EmbInv、PII extraction/matching、personal attribute inference；uniform epsilon 导致 utility/privacy 和 sensitive leakage 矛盾。 | high | 问题定义最重要。 |
| §V / p6-p9 | Rap-LI framework | Risk identification + personalized labeling；risk-to-budget mapping；risk-adaptive candidate space；high-risk score reversal；token-level `epsilon(t,t')`-LDP；sentence-level `d*epsilon_S`-LDP；prompt engineering。 | high | 机制与证明。 |
| §VI / p9-p13 | Evaluation | AGNews、PIIDocs、SAMSum、SpamEmail、SynthPAI；对比 LDP/non-LDP baselines；报告 privacy/utility、time、diagnostics、user study。 | high | 量化证据。 |
| §VII / p13-p14 | Discussion | 强调 risk-aware + provable LDP + practical usability；NER dependency；cross-lingual adaptation；semantic coherence loss；text-only limitation。 | high | caveat 清楚。 |
| §VIII / p14 | Conclusion | Rap-LI 是 plug-and-play privacy-first LLM inference protection route。 | medium | 总结。 |

## 核心精读笔记

### 背景、动机与问题边界

本文解决的是 cloud/black-box LLM inference 中用户 prompt 的隐私泄漏。用户为了获得更好回答，会把医疗、身份、业务或上下文信息放进 prompt；服务提供者能看到动态 user prompt，API adversary 也可能通过输出和攻击 prompt 推断原始信息。由于 cloud LLM 的内部参数和服务端流程不可控，依赖服务端协作的同态加密、模型改造或 fine-tuning privacy route 在本文场景下不实用。

作者把本文定位为 user-side prompt protection: 在 prompt 发给第三方 LLM 前，本地先做 text sanitization。简单 masking 只能遮住显式实体，无法防止 contextual leakage；local LLM rewrite/anonymization 缺少严格隐私保证，也引入本地资源和延迟；uniform-budget LDP text sanitization 有形式化保证，但所有 token 用同一 epsilon，会把高风险 PII 和普通上下文词同等对待。

队列原分类把本论文放到 `distributed-learning`，这是误分。正文没有分布式训练、FL 协议或 remote trainer coordination；核心问题是 `ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy`。

### Threat Model 与攻击

论文考虑两类 adversary:

- `A_srv`: LLM service provider，能直接访问 user prompt 和 response。
- `A_api`: 只能访问 LLM inference API，但可以构造 prompt，从 response 中推断或诱导泄露信息。

针对 sanitized prompt，作者定义和评估五类攻击:

- MaskInf: 用 BERT-style masked-token prediction 重建原始 token。
- EmbInv: 利用 embedding space 做 nearest-neighbor inversion。
- PII extraction: 从 sanitized text 中抽取仍然显式保留的 PII。
- PII matching: 将 sanitized PII embedding 和外部 PII database 匹配，链接到真实 record。
- Personal attribute inference: 用强 LLM 从多个 sanitized texts 中推断 age、location、occupation 等隐式属性。

最重要的分析是 uniform token-level LDP 的敏感泄漏问题。若每个 token 保留概率相同，sentence 中有 `h` 个 sensitive tokens，则至少一个 sensitive token 泄漏的概率是 `1 - (1 - Pr_keep)^h`。为了 utility 提高 epsilon 时，敏感 token 的保留概率也同步上升；即使 epsilon 很小，多个敏感 token 组合也会带来可观泄漏。作者报告在 PIIDocs 等实验中，CusText+ 在 `epsilon=0.1` 下仍可能出现 71.74% PII extraction leakage。

### Rap-LI 方法

Rap-LI 是 risk-aware privacy preservation framework for LLM inference，放在用户侧，包含三步。

第一步是 risk identification and personalized labeling。系统用 NER/Presidio/Flair/transformer taggers 抽取 PII，并把 token 分成 high-risk、medium-risk、low/no-risk。用户可以本地调整标签，把业务词、敏感名词或特定合规字段升级/降级。每个 token 的风险等级映射到不同隐私预算，风险越高 epsilon 越小。sentence-level budget `epsilon_S` 是 token budget 的平均值，最终 token budget 取 `min(token_budget, epsilon_S)`。

第二步是 risk-aware LDP text sanitization。Rap-LI 先按 token embedding similarity 构造候选 token space，但候选空间大小随 epsilon 调整: 低 epsilon 对应更大的 candidate set，增强遮蔽。对 high-risk token，作者指出传统 similarity-based exponential mechanism 会优先选等价或近似原 token，导致 PII 保留概率高；Rap-LI 对 high-risk token 的 score row 做 reverse，使最高相似度 token 得到更低 sampling score。Medium-risk token 不反转，因为它们承载语义 utility，更多依赖候选空间和概率扰动保护。

第三步是 task-aware prompt engineering。系统 prompt 明确 LLM 角色、任务和输入可能含噪，并使用 CoT-style reasoning 来提高被扰动 prompt 的下游可用性。作者强调 Rap-LI 是 training-free 和 denoising-free；local denoising/post-processing 只是可选增强。

### 隐私定义和证明

本文把 standard uniform `epsilon`-LDP 扩展为 token-level `epsilon(t,t')`-LDP。对于共享同一 sanitized token set 的 token pair `t, t'`，机制需要满足:

`Pr[M(t)=tau] <= exp(epsilon(t,t')) Pr[M(t')=tau]`

在 Rap-LI 的 exponential mechanism 下，作者证明 score-reverse 不改变归一化 score 的敏感度上界，`Delta(u*) = 1`。随后证明 token-level mechanism 满足 `epsilon(t,t') = (epsilon_t + epsilon_t') / 2` 的 LDP。

句子层面，Rap-LI 定义 sentence-level `d * epsilon_S`-LDP。两个句子若只在 high/medium-risk token 位置差异，低风险 token 不参与邻接定义；若有 `d` 个差异位置，则整个 sanitized sentence 满足 `d * epsilon_S` bound。这个定义把 heterogeneous token budgets 汇总为一个可解释的 prompt-level privacy bound。

### 实验与结果

任务覆盖 NLU 和 NLG:

- Topic classification: AGNews.
- PII document classification: PIIDocs.
- Chinese spam detection: SpamEmail.
- Multi-turn dialogue summarization: SAMSum.
- Contextual/personal attribute inference: SynthPAI.

Baselines 包括 SanText+、CusText+、RanText/InferDPT、SnD/dX，以及 non-LDP 的 HaS 和 Kan methods。中文 SpamEmail 上，DP baselines 因词表/tokenizer/similarity computation 主要面向英文而不可靠，所以只和 HaS/Kan 比较。

关键结果:

- Rap-LI 相比 utility 可比的 CusText+，平均提升 PII privacy 51.68%，具体为 AGNews 31.57%、PIIDocs 67.47%、SAMSum 56.01%。
- CusText+ 在 PIIDocs 上即便 `epsilon=0.1` 仍有 71.74% PII extraction leakage；原因包括 whitespace tokenization 不能处理特殊字符/PII 组合，以及 OOV token 直接保留。
- Ours1/Ours2 在不同 utility/privacy 权重下 overall score 更稳定；NLG/SAMSum 的 ROUGE 因 token perturbation 较敏感，是薄弱项。
- Rap-LI 用户侧总开销平均约 0.1s，远小于 LLM inference 约 2-3s；non-LDP local LLM methods 往往有更高本地延迟和恢复开销。
- 更强 LLM 如 GPT-4o、GPT-4-Turbo、DeepSeek-R1 能缓解 sanitized prompt 的 utility loss；local denoising 对低效方法帮助较大，对 Rap-LI 这类高 utility 方法收益有限且会增加约 4s 延迟。
- SynthPAI 上，Rap-LI 降低 personal attribute inference 成功率，尤其对 Location、Occupation、Place of Birth 等开放类别更有效。
- 用户研究中，10 名常用 LLM 用户在 5 类任务上给出较高满意度；平均 privacy-adjustment time 约 18.30s，平均调整 token 数 4.82。

### 限制与未来工作

Rap-LI 的限制也很明确:

- Token-level sanitization 可能破坏语义连贯性，尤其影响 summarization 等 NLG task。作者用保留 low/no-risk token、prompt engineering 和可选 post-processing 缓解，但不是根治。
- PII/risk identification 依赖 NER 或规则/模型质量。跨语言可用，但需要特定语言模型、regex 或用户自定义规则。
- 当前只处理文本 prompt，不覆盖 image/audio/video multimodal input。作者提出可以把 risk-aware paradigm 扩到 vision/audio/multimodal sanitization，但本文未实现。
- 本文保护的是 prompt 内容暴露，不验证 LLM 输出正确性、模型来源、训练数据合规、公平性或安全性。
- Code repository 未在本次吸收中分析；实现质量、license、reproducibility 和 UI 细节仍待 repo analysis。

## Knowledge 吸收判断

- 主归属: [[llm-inference-privacy|LLM inference privacy]]
- 父方向: [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]]
- 相关但不等价: [[verifiable-inference|Verifiable inference]]
- Bridge: [[llm-inference-privacy-to-zkml-verifiable-inference|LLM inference privacy -> zkML verifiable inference]]

## 方法与问题映射

| Source-specific item | 抽象到的 Knowledge | 保留在 Source 的细节 | 说明 |
| --- | --- | --- | --- |
| Rap-LI | [[llm-inference-privacy|LLM inference privacy]] | NER taggers、score reverse、datasets、exact metrics、user study numbers | 系统名不升为 Knowledge 节点。 |
| Risk-aware LDP prompt sanitization | [[llm-inference-privacy|LLM inference privacy]] method route | `K(epsilon)` formula、Ours1/Ours2 vocabulary choices | 可复用方法族。 |
| `epsilon(t,t')`-LDP | [[llm-inference-privacy|LLM inference privacy]] method/foundation candidate | proof algebra and exact theorem text | 当前单源，不单独建 foundation node。 |
| Privacy-preserving prompt engineering | [[llm-inference-privacy|LLM inference privacy]] route | exact prompt templates in appendix not present in local PDF | 需要后续 survey/foundation source。 |
| Prompt privacy vs inference correctness | [[llm-inference-privacy-to-zkml-verifiable-inference|LLM inference privacy -> zkML verifiable inference]] | Rap-LI and zkLLM protocol specifics | 桥接用于防混淆。 |

## 分类修正

- 队列原路径: `ml-systems/privacy-and-trustworthy-ml/distributed-learning`
- 修正路径: `ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy`
- 修正理由: 正文围绕 user-side prompt sanitization、PII/contextual privacy leakage、local differential privacy 和 cloud LLM inference；不涉及 distributed learning protocol。
- arXiv 修正: 队列从 DOI 中误抽出 `2026.36674`，正文和元数据未提供 arXiv ID。

## 关系与桥接

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference | evidences | nahida-knowledge-llm-inference-privacy | Sections I-VII | high | active_seed |
| doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference | corrects_queue_path | ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy | full-text deep read | high | done |
| doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference | bridges_boundary_with | nahida-knowledge-zkml-verifiable-inference | prompt privacy versus committed-model correctness | medium | active_seed |

## 术语表

| Term | 本文含义 | 上层处理 |
| --- | --- | --- |
| Rap-LI | Risk-aware privacy preservation framework for LLM inference | source-specific system |
| LDP | 用户本地扰动 prompt/token 后再发送给服务端 | method family under LLM inference privacy |
| PII leakage | sanitized prompt 中仍能抽取或匹配真实 PII | threat model/evaluation |
| Contextual privacy leakage | 从非显式 PII 的上下文、风格、组合信息推断属性 | threat model/evaluation |
| Risk-aware labeling | NER + user customization 给 token 分配风险等级 | reusable design route |
| Score reversal | 对 high-risk token 的 similarity scores 反转，降低等价 token 概率 | Rap-LI mechanism detail |

## 后续动作

| Action | Why | Skill |
| --- | --- | --- |
| Analyze `Cristliu/RapLI` repo | Source claims code is available; implementation architecture and reproducibility not checked. | nahida-github-repo-analyze |
| Absorb privacy-preserving prompt engineering survey | 当前只有 Rap-LI 引用 survey，缺 foundation source for prompt privacy taxonomy. | nahida-research-search / nahida-update |
| Build local differential privacy concept/foundation note if more sources arrive | `epsilon(t,t')` and personalized/context-aware LDP may need foundation split after additional primary sources. | nahida-knowledge-get |
| Compare with cryptographic private inference and ZK verifiable inference | Avoid conflating prompt hiding, model hiding and output correctness. | nahida-update |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-risk-aware-llm-inference-privacy | Deep-read local PDF, corrected queue classification from distributed-learning to LLM inference privacy, created source note and handed off to Source + Knowledge + Bridge absorption. | local PDF | codex |
