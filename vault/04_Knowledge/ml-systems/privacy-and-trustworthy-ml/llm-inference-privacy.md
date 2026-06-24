---
id: "nahida-knowledge-llm-inference-privacy"
title: "LLM inference privacy"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "llm-inference-privacy"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
parent_knowledge_refs:
  - "nahida-knowledge-privacy-and-trustworthy-ml"
child_knowledge_refs: []
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "llm-inference-privacy"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-inference"
relation_edges:
  - from: "nahida-knowledge-llm-inference-privacy"
    relation: "is_a"
    to: "nahida-knowledge-privacy-and-trustworthy-ml"
    evidence_refs:
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy.md"
      - "vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-llm-inference-privacy"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
    evidence_refs:
      - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-llm-inference-privacy"
    relation: "bridges_to"
    to: "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
    evidence_refs:
      - "vault/05_Bridges/llm-inference-privacy-to-zkml-verifiable-inference.md"
    confidence: "medium"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference"
source_note_refs:
  - "vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md"
representative_source_refs:
  - "doi:10.1109/TIFS.2026.3667458"
query_keys:
  - "LLM inference privacy"
  - "prompt privacy"
  - "privacy-preserving prompt engineering"
  - "prompt text sanitization"
  - "local differential privacy for LLM inference"
  - "risk-aware LDP"
  - "Rap-LI"
  - "PII leakage in LLM prompts"
  - "contextual privacy leakage"
  - "personal attribute inference"
aliases:
  - "prompt privacy"
  - "privacy-preserving LLM inference"
  - "privacy-preserving prompt engineering"
domains:
  - "ml-systems"
topics:
  - "llm-inference-privacy"
  - "privacy-and-trustworthy-ml"
  - "local-differential-privacy"
  - "text-sanitization"
  - "prompt-engineering"
  - "personally-identifiable-information"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-23"
valid_until: "2026-07-23"
evidence_window_start: "2026-06-23"
evidence_window_end: "2026-06-23"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-risk-aware-llm-inference-privacy"
source_refs:
  - "doi:10.1109/TIFS.2026.3667458"
confidence: "medium"
trust_tier: "primary"
---

# LLM inference privacy

## 定义与范围

- 定义: LLM inference privacy 研究用户把 prompt 发给 cloud/black-box LLM 做推理时，如何在本地或协议层保护 prompt 中的 PII、敏感上下文、个人属性、业务秘密和交互轨迹，同时保留足够 task utility。
- 不包含: 模型训练隐私、训练数据合规性、输出事实性、模型参数产权、inference correctness proof、prompt injection 防御、LLM safety alignment；这些需要单独问题节点或 bridge。
- Canonical terms: `LLM inference privacy`, `prompt privacy`
- Aliases/query keys: privacy-preserving prompt engineering, prompt text sanitization, local differential privacy for LLM inference, Rap-LI
- Standalone completeness check: 本节点解释问题边界、攻击面、方法路线、代表 source、与 zkML/verifiable inference 的区别和当前缺口；链接用于深入，不作为唯一解释。
- Retrieval role: 查询“如何在使用云端 LLM 前保护 prompt 隐私”“LDP prompt sanitization 是什么问题”“Rap-LI 属于哪个方向”时先读本节点。
- Update scope: 新 source 若涉及 prompt sanitization、privacy-preserving prompt engineering、black-box LLM inference privacy、local DP text sanitization、PII leakage in prompts、contextual attribute inference 或 cryptographic/private inference comparison，应刷新本节点。
- Domain dynamics note: [[research-dynamics|ML systems Research Dynamics]].

## 背景

Cloud LLM inference 的信任边界很薄: 用户的动态 prompt 往往同时包含任务输入和敏感信息，而服务端、日志、API integration 或响应泄露都可能暴露这些信息。与训练阶段隐私不同，inference prompt 往往是即时、用户定制、任务相关的文本，不能简单用“不要上传敏感信息”来解决，因为敏感上下文本身可能正是任务需要。

Rap-LI 当前给出第一个 strong seed。它把问题明确为 user-side local protection: 在 prompt 发给第三方服务前，本地识别高风险 token、让用户调整风险标签，然后用 risk-aware LDP text sanitization 改写 prompt。该路线适用于黑盒 LLM，因为它不要求服务端支持 homomorphic encryption、secure inference、fine-tuning 或模型内部访问。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem`
- 为什么足够通用: 它组织一类 cloud LLM 交互中的隐私问题，包括 prompt PII leakage、contextual attribute inference、text sanitization、privacy-preserving prompt engineering、local DP 和用户交互式风险控制。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: Rap-LI 是代表 source instance；score reversal、Ours1/Ours2、具体 NER tagger 和 user study UI 留在 source note。
- 需要引用的更基础 Knowledge: [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]], [[ml-systems|ML systems]]。
- 不应拆出的实例/协议/来源: Rap-LI、SanText、CusText、InferDPT、SnD、HaS、Kan methods 默认作为 source/method instances；除非后续多源证明某个方法族需要单独节点。

## 解决的问题

| 问题 | 说明 | 当前 evidence |
| --- | --- | --- |
| Prompt PII leakage | prompt 中的姓名、年龄、医疗、地址、账号等显式 PII 在 sanitization 后仍可能被抽取或匹配。 | Rap-LI reports CusText+ can reach 71.74% PII extraction leakage at `epsilon=0.1` on PIIDocs. |
| Contextual privacy leakage | 即使显式 PII 被 masking，攻击者仍可能从上下文、写作风格、任务内容推断年龄、location、occupation 等属性。 | Rap-LI evaluates SynthPAI personal attribute inference. |
| Utility/privacy tradeoff | 普通 token-level LDP 用同一 epsilon 扰动所有 token，保护敏感词会损伤语义，保护语义又会提高敏感泄漏概率。 | Rap-LI §IV theoretical analysis and §VI experiments. |
| Black-box deployment constraint | 用户通常不能修改或信任 cloud LLM service provider，也不能要求其执行 cryptographic protocol。 | Rap-LI positions itself as user-side, training-free, denoising-free framework. |
| User-specific sensitivity | 不同用户/行业对词的敏感性不同，固定规则或统一 privacy budget 很难表达实际需求。 | Rap-LI personalized labeling and privacy budget mapping. |

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[privacy-and-trustworthy-ml|Privacy and trustworthy ML]] | child_of | Rap-LI source classification | active_seed |
| [[verifiable-inference|Verifiable inference]] | contrasted_with | Both involve LLM/ML inference trust, but protect different assets and use different guarantees. | active_seed_bridge |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| Privacy-preserving prompt engineering | route section | 组织 masking、rewriting、sanitization、prompt templates 和 local post-processing；当前只有 Rap-LI 引用 survey，foundation source 未吸收。 | Rap-LI §II/§V/§VII | queued |
| Local DP text sanitization | method family candidate | SanText/CusText/InferDPT/SnD/Rap-LI 都使用 token perturbation 和 privacy budget，但当前 sources 多为 Rap-LI 引用。 | Rap-LI related work | foundation_gap |
| Risk-aware LDP prompt sanitization | route section | Rap-LI 给出风险分级、异构 budget、high-risk score reversal 和 sentence-level LDP route。 | Rap-LI §V | active_seed |
| Contextual privacy attack evaluation | evaluation axis candidate | SynthPAI/attribute inference 说明 prompt privacy 不只看 PII extraction；后续需要更多 attack/audit source。 | Rap-LI §IV/§VI-C | active_seed |
| Cryptographic/private inference | sibling candidate | 本文说明 HE/server collaboration 在黑盒 cloud setting 中不实用；但 cryptographic private inference 是相邻路线，不应混在本节点内部。 | Rap-LI §I | queued |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| Simple masking/anonymization | 把显式 PII 替换为 `[PERSON]` 等标签。 | 只需要粗粒度隐藏实体，任务不依赖原词。 | 无严格隐私保证；上下文仍可泄露；utility 可能丢失。 | Rap-LI related work |
| Local LLM rewriting/filtering | 用本地 LLM 或小模型重写 prompt，再把响应中的实体恢复。 | 用户有本地模型资源，且可接受额外延迟。 | 依赖模型能力；隐私保证不严格；恢复过程容易不稳定。 | HaS/Kan in Rap-LI §II |
| Uniform LDP text sanitization | 对所有 token 使用同一 epsilon 和相同 sampling rule。 | 需要形式化 LDP，且任务能忍受同质扰动。 | 高风险 token 和普通词同等处理，utility/privacy tradeoff 难缓解。 | SanText/CusText/InferDPT/SnD in Rap-LI |
| Risk-aware LDP prompt sanitization | 先识别 token risk 并允许用户调整，再用异构 privacy budget、risk-adaptive candidate set 和 high-risk score reversal 做 token sampling。 | 黑盒 cloud LLM；prompt 是文本；本地可运行 NER/embedding/sampling。 | 依赖 NER/risk labels；NLG 语义连贯性仍受损；当前单源。 | [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Rap-LI]] |
| Task-aware prompt engineering | 在 system prompt 中声明输入可能含噪、指定角色/任务，并用 reasoning-style prompt 提高 sanitized prompt 的下游 utility。 | 目标 LLM 对指令/role/CoT-style prompt 有响应能力。 | 不是隐私保证；可能增加延迟或改变输出风格。 | Rap-LI §V-C/§VI-C |
| Optional local post-processing | 用本地 LLM 对 LLM response 做 denoising/recovery，提高 NLG utility。 | 语义敏感任务且用户有本地模型资源。 | 增加约数秒延迟；高 utility methods 收益有限。 | Rap-LI §VI-C |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Risk-Aware Privacy Preservation for LLM Inference]] | paper | 创建 LLM inference privacy 问题节点；展示 risk-aware LDP prompt sanitization、token/sentence-level LDP guarantee、PII/contextual attack evaluation 和 plug-and-play user-side deployment route。 | text-only; NER dependency; token-level sanitization hurts NLG coherence; code repo not analyzed; does not prove model correctness or training provenance. | `p1-p16` |

## 正反例约束

- 正确: 把 Rap-LI 作为 prompt privacy/source-specific system，不把 Rap-LI 系统名升级为基础概念。
- 正确: 把 `epsilon(t,t')`-LDP 写成 risk-aware LDP route；等更多 LDP/persona/context-aware DP sources 后再考虑基础概念节点。
- 正确: 区分 prompt privacy 和 verifiable inference: 前者保护用户输入不被 cloud provider/API adversary 看见或推断，后者证明输出来自 committed model/input relation。
- 错误: 声称 prompt sanitization 能证明 LLM output 事实正确或模型执行正确。
- 错误: 声称 ZK verifiable inference 自动保护 prompt PII；很多 zkML inference proof 的 prompt/output 是 public statement。
- 错误: 把 masking 或 high BLEU/ROUGE 当作隐私 guarantee。

## 当前综合

- Evidence window: `2026-06-23`，当前只有 Rap-LI 一篇 primary source。
- Freshness: `fresh` for local source absorption; not an external latest claim.
- Valid until: `2026-07-23`。
- 综合: LLM inference privacy 当前是 active_seed 问题节点。Rap-LI 说明 cloud/black-box LLM 的 prompt 隐私不能只靠 masking、local rewriting 或 uniform LDP；真正的问题是 token sensitivity 不均、用户隐私偏好不同、PII/contextual leakage 与 utility 同时存在。Rap-LI 的 risk-aware route 把 NER/user labeling、异构 LDP budget、candidate space sizing、high-risk score reversal 和 prompt engineering 组合成 user-side plug-and-play workflow，并用 token-level `epsilon(t,t')`-LDP 和 sentence-level `d*epsilon_S`-LDP 给出形式化边界。该节点仍很薄，因为 prompt privacy survey、local DP text sanitization 原论文、cryptographic private inference、production prompt governance 和 repo implementation 尚未吸收。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference|Risk-Aware Privacy Preservation for LLM Inference]] | 新建 LLM inference privacy 问题节点；把队列误分的 distributed-learning 修正为 prompt privacy/risk-aware LDP；创建与 zkML verifiable inference 的边界 bridge。 | 定义; 解决的问题; 方法族; 代表 Sources; Bridge Links; 关系图谱 | yes | 分析 Rap-LI repo；吸收 prompt privacy survey 和 LDP text sanitization foundations |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[llm-inference-privacy-to-zkml-verifiable-inference|LLM inference privacy -> zkML verifiable inference]] | `ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy; zero-knowledge-proofs/zkml/verifiable-inference` | contrast, complementary, trust_boundary, privacy_boundary | Prompt privacy hides/sanitizes user input before black-box LLM; verifiable inference proves committed-model computation. Neither guarantee automatically transfers. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-llm-inference-privacy | is_a | nahida-knowledge-privacy-and-trustworthy-ml | vault/04_Knowledge/ml-systems/privacy-and-trustworthy-ml/llm-inference-privacy.md | high | active_seed |
| nahida-knowledge-llm-inference-privacy | evidenced_by | vault/03_Sources/papers/doi-10-1109-tifs-2026-3667458-risk-aware-privacy-preservation-llm-inference.md | source note | high | active_seed |
| nahida-knowledge-llm-inference-privacy | bridges_to | nahida-bridge-llm-inference-privacy-to-zkml-verifiable-inference | bridge note | medium | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| Privacy-preserving prompt engineering survey 未吸收 | 需要把 masking、rewriting、DP、cryptographic/private inference、governance 放入完整 taxonomy。 | nahida-research-search / nahida-update | high | queued |
| Local DP text sanitization foundations 未吸收 | Rap-LI 引用 SanText/CusText/InferDPT/SnD，但 vault 还缺这些 primary source。 | nahida-update | high | foundation_gap |
| Rap-LI repository 未分析 | Paper claims code and system videos; implementation architecture/reproducibility/license 未核。 | nahida-github-repo-analyze | medium | queued |
| Multimodal prompt privacy 缺 | 当前节点 text-only，不能覆盖 image/audio/video prompt。 | nahida-research-search | medium | queued |
| Cryptographic private inference comparison 缺 | HE/MPC/TEE/private inference 与 user-side text sanitization 的边界还薄。 | nahida-research-search / nahida-update | medium | queued |
| Prompt privacy governance/production logging 缺 | 实际 cloud LLM privacy 还涉及日志、retention、enterprise policy、redaction pipeline。 | nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-risk-aware-llm-inference-privacy | Created LLM inference privacy problem node from Rap-LI source absorption and corrected queue classification. | 1 source note | codex |
