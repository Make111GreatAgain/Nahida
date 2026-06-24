# Nahida 使用方式

Nahida 的日常使用只有两个入口：

- `nahida-update`: 把新东西加入知识库，或者让知识库自我更新。
- `nahida-query`: 查询知识库已有内容，要求它给出依据、相关方向和缺口；默认不联网、不抓取、不用模型常识补齐缺失内容。

底层的 `nahida-paper-read`、`nahida-github-repo-analyze`、`nahida-research-search`、`nahida-daily-fetch`、`nahida-knowledge-get` 通常由 `nahida-update` 调用或遵循，不需要用户手动选择。

## 存储方式

笔记本身不按方向存储。论文、仓库、网页、claim、concept、map 都按稳定身份和类型放在各自区域里。

方向由这些层表达：

- frontmatter: `domains`、`topics`、`tags`、`primary_direction`、`secondary_directions`、`direction_facets`
- Obsidian 结构: wikilinks、backlinks、Bases、Canvas
- Nahida 结构: maps、claims、concepts、bridges、indexes、ledgers、query reports

因此重分类时不默认移动文件，只更新 metadata、map、index 和 ledger。文件夹不是知识本体，方向是可变视图。

文件名必须使用安全 slug，不能直接使用原始标题。比如 bridge 标题可以是 `AI/ML x Zero-Knowledge Proofs`，但文件名应类似 `ai-ml-x-zero-knowledge-proofs.md`，否则 `/` 会被文件系统当成目录分隔符。原始标题保留在 `title`、`original_title` 或 aliases 里。

## 记忆分层

Nahida 应该像一个不断升级的记忆系统：

- 底层独立笔记：论文、仓库、网页、research note、claim、concept、bridge。每个笔记都要精准、细节充分、人类可读、可检索，并且能独立使用。
- 上层综合笔记：放在 `09_Syntheses/`，用于总结单方向发展、不同方向结合、新兴方向、最近热门话题、或反复被问到的问题。
- 导航层：`07_Maps/` 负责入口、索引和方向地图，不承载所有细节。
- 缓存层：query reports 和 indexes 用于节省检索成本，不是真值来源。

`nahida-update` 自底向上：先写好一个高质量底层笔记，再由 `nahida-knowledge-get` 更新 claim/concept/map/bridge/synthesis。  
`nahida-query` 自顶向下：先看 query memory、fresh synthesis、map；如果上层综合足够新且覆盖问题，就不深读大量底层笔记；如果超过约 30 天、标记 stale、或证据不足，再按需下钻或建议更新。

上层 synthesis 默认需要 freshness 字段：`last_synthesized`、`valid_until`、`freshness_status`、`evidence_window_start`、`evidence_window_end`。超过有效期不应被当作最新结论。

## Claim 与 Concept 放什么

`claim` 放可复用、可复核、可引用的原子断言，不是把论文每句话都拆出来。好的 claim 通常是定义、机制、定理、实验结果、实现模式、比较、限制、趋势、benchmark 或设计原则。`supported` claim 必须有来源和证据锚点；Codex 先验只能作为 `tentative/review`，不能当作证据。

`concept` 放基础知识和解释。它应该让人读完后理解这个概念：它是什么、为什么存在、解决什么问题、前置知识是什么、核心机制是什么、有哪些变体和例子、容易和什么混淆、什么时候适用、什么时候不适用。论文和项目是对 concept 的 `source_extension`，用于说明“这篇论文/这个仓库在已有概念上增加、修改、实现或挑战了什么”。

如果 vault 里缺基础知识，`nahida-update`/`nahida-knowledge-get` 应该用 Codex 先验搭结构，并通过 `nahida-research-search` 找稳定 foundation sources 校准；不要只从单篇论文硬抽一个薄 concept。

## 前置能力

Nahida 应该优先复用已有 Codex skill 和插件能力，而不是把 vault 当作普通文件夹粗暴读写：

- 必需：`obsidian-markdown`、`obsidian-note`
- 推荐：`obsidian-bases`、`json-canvas`
- 任务相关：CodeGraph、GitHub plugin/connector、Codex bundled PDF runtime、web/browser search

安装时可以启用严格检查：

```bash
NAHIDA_STRICT_PREREQS=1 ./scripts/install-skills.sh
```

如果关键前置缺失，Nahida skill 应该报告 `prerequisite_gap`，而不是静默降级成低质量 Markdown。

## 加入一篇论文

对 Codex 说：

```text
使用 nahida-update，把 /path/to/paper.pdf 这篇论文加入 Nahida。需要精读，方向不要太泛；如果所属方向缺基础知识，先补 foundation 再吸收论文。
```

预期流程：

1. 扫描这个 PDF，提取标题、作者、年份、DOI/arXiv、摘要、checksum。
2. 运行 `nahida-paper-read` 做单篇精读，不只读摘要或首页。
3. 选 canonical direction 和 `direction_facets`。
4. 缺基础知识时，用 `nahida-research-search` 找 foundational sources。
5. 用 `nahida-knowledge-get` 写入 claims、concepts、directions、maps、bridges，并刷新受影响的 `09_Syntheses/` 上层综合。

如果给的是论文目录，Nahida 默认先做 inventory、去重、粗分方向和优先级，生成待读队列；随后进入串行自动处理：一次只精读一篇、吸收一篇、checkpoint 一篇，然后继续下一篇。队列里的论文在各自完成精读和吸收前不算已吸收。

## 加入 GitHub 仓库

```text
使用 nahida-update，分析 https://github.com/owner/repo 并加入 Nahida。重点看它解决的领域、架构、主要模块、API、数据流和可复用实现模式。
```

`nahida-update` 会路由到 `nahida-github-repo-analyze`，必要时 clone 仓库并优先使用 CodeGraph。

注意：GitHub 仓库本体不进入 Nahida vault。临时 clone 应放在 `.nahida/tmp/repos/` 或系统临时目录，用完删除；知识库只保留分析笔记、commit/ref、关键文件/符号引用和证据摘要。

仓库分析默认是 `deep_repo_read`：不能只看 README。应读 docs、manifest/config、entry points、核心模块、tests/examples、API/CLI/config surface，并尽量用 CodeGraph 追踪主要流程。大仓库可以做 scoped deep analysis，但必须写清楚覆盖范围和未覆盖模块。

如果给多个 GitHub 仓库，Nahida 默认只做去重、粗分类和优先级队列；然后选择一个仓库进入 `nahida-github-repo-analyze`。队列里的仓库不算已分析。

## 加入网页、段落或资料

```text
使用 nahida-update，把下面这段内容加入 Nahida，并判断它属于哪个方向、是否需要补充基础资料。
```

如果是 URL，会分类为 reference、concept、blog 或 news。如果只是段落，会先保留来源上下文；不确定来源时进入 review queue。

## 调研一个方向

```text
使用 nahida-update，调研 LLM agent memory，整理成 Nahida 知识库内容。
```

这会路由到 `nahida-research-search`，再通过 `nahida-knowledge-get` 进入结构化知识层。

## 查询知识库

```text
使用 nahida-query，Nahida 里关于 zkML proof systems 已经有什么？有哪些论文、仓库、概念和缺口？
```

`nahida-query` 默认只读且只查 Nahida vault。它应该返回中文答案、查询模式、覆盖状态、证据链、相关方向、缺口和建议更新动作。

如果知识库没有覆盖，`nahida-query` 应该明确说：

- `知识库没有记录`: 没有相关 note/source/claim/map。
- `知识库只有部分记录`: 有线索或候选，但不足以回答。
- `知识库没有足够新近资料`: 询问“最新/最近/当前进展”时，vault 里没有足够新的 daily report 或 dated source。

它不应该自动去搜网页、抓 arXiv、clone GitHub 仓库，或读取 vault 之外的本地文件。需要外部资料时，应由用户显式使用 `nahida-update`，例如：

```text
使用 nahida-update，更新 zkML proof systems 的最新进展，然后吸收进 Nahida。
```

```text
使用 nahida-update，分析 https://github.com/owner/repo 并加入 Nahida。
```

```text
使用 nahida-update，把 /path/to/paper.pdf 这篇论文加入 Nahida。
```

复杂查询会做智能统筹，而不是只找一个文件夹。例如：

```text
使用 nahida-query，根据最新的知识库，最新的 zk-SNARKs 做了哪些优化？
```

预期行为：

1. 把问题规范化成 query key，识别 `zk-SNARKs`、`SNARK`、`proof systems`、`recursive SNARK`、`lookup arguments`、`polynomial commitments`、`folding schemes` 等知识库已有 alias/facet。
2. 先检查 `90_Generated/reports/queries/` 和 `query-ledger.jsonl` 里有没有类似问题，避免从头扫描。
3. 先读取 fresh synthesis 和 maps；必要时才基于已有 vault 内容下钻到 papers、claims、concepts、daily reports、repo analyses。
4. 按优化类型回答，例如 prover time、proof size、verifier cost、recursion/folding、lookup/arithmetization、polynomial commitment、parallelism/hardware、trusted setup 等，但每一类都必须有知识库证据。
5. 如果知识库没有新近资料，明确说 `知识库没有足够新近资料`，并建议用 `nahida-update` 做 freshness update。

问过的问题可以记录成 query report。query report 是缓存和路线图，不是真值来源；最终答案仍要回链到 source/claim/concept/map/synthesis。

## 每日更新

```text
使用 nahida-update，做一次今日更新，关注当前 watchlist 和已有地图里的方向，去重，不要重复抓旧资料。
```

这会路由到 `nahida-daily-fetch`。它只接受高信号条目，并给出后续 `paper-read`、`repo-analyze`、`research-search` 或 `knowledge-get` 任务。

## 方向原则

- 方向必须比 `AI`、`Blockchain`、`ZKP` 更细。
- 不要一篇论文一个方向。
- 新方向要有可复用检索价值：术语明确、领域认可、多来源支持、或用户明确长期关注。
- 缺基础知识时先补 foundation，再把具体论文/仓库挂进去。
- 论文 note 的路径和 ID 应该稳定，不要因为方向变动就搬文件；方向归属放在 frontmatter、map 和分类台账里。
- 低置信度或交叉方向论文先标记 `classification_status: review`，不要硬塞进单一方向。
- 论文和仓库是高价值证据，进入 claims/concepts/maps 前必须精读；粗读、metadata、README-only 只能作为 staged 或 review 信息。

## 论文目录队列

给一个论文目录时，不应该批量吸收，也不应该直接按文件名生成方向目录。推荐流程：

1. 先做 inventory：checksum、DOI/arXiv、标题、作者、年份、摘要、首页文本、提取质量。
2. 用 DOI/arXiv/公开元数据补标题和作者，但正文判断仍以本地 PDF 为证据。
3. 用多标签 facets 分类：父领域、子领域、任务、方法族、系统层、应用/评测场景、bridge。
4. 每篇论文有一个 `primary_direction`，可以有多个 `secondary_directions`。
5. 每个分类都要有 `classification_confidence` 和 `classification_evidence`。
6. 人工修正优先级最高，文件名只作为弱证据。
7. 后续重分类只更新 frontmatter、map、index、ledger；不要默认移动/重命名 note。
8. 默认串行自动推进：一次只精读并吸收一篇论文，但完成后继续处理下一篇；如果中断，必须记录 next item、remaining count 和 resume command。

## 自升级原则

每次 `nahida-update` 都应该产生一小组扩展候选，而不是只把当前资料塞进库里。候选可以是：

- 子方向
- 相邻方向
- 基础依赖
- 代表论文
- 代表仓库
- 标准、协议、dataset、benchmark、工具
- Bridge 候选
- Daily-fetch 监控词

这些候选需要有状态：`candidate`、`watching`、`active`、`evergreen` 或 `rejected`。弱候选先进入 watchlist 或 review queue，不能直接污染地图。
