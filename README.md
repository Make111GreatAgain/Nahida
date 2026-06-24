# Nahida

Nahida 是一个 AI-native Obsidian 知识库：Obsidian 是人类浏览和编辑界面，Markdown/YAML 是长期知识层，Codex skills 负责把论文、GitHub 仓库、网页和查询沉淀成可检索、可维护的分层记忆。

它不是论文摘要集合。当前设计遵循 `Source -> Knowledge -> Bridge`：

- `03_Sources/`: 外部来源的完整本地记忆，例如论文、仓库分析、网页资料。source note 要足够详细，普通问题不应重新打开原始 PDF/仓库。
- `04_Knowledge/`: 可复用的领域、方向、问题、方法族、应用场景和基础概念。这里不是复述单篇论文，而是说明问题如何被解决、哪些方案存在、每个来源贡献了什么 delta。
- `05_Bridges/`: 跨知识节点关系，例如依赖、应用、类比、边界、方法迁移和共同演化。

## 使用方式

### 1. 打开知识库

把 `vault/` 作为 Obsidian vault 打开。知识库笔记主要是中文，保留论文标题、协议名、API、repo 名、路径和 canonical English terms，方便检索。

### 2. 安装 Codex skills

```bash
./scripts/install-skills.sh
```

严格检查依赖时使用：

```bash
NAHIDA_STRICT_PREREQS=1 ./scripts/install-skills.sh
```

Nahida 完整工作流依赖这些 Obsidian/Codex 能力：

- 必需: `obsidian-markdown`, `obsidian-note`
- 推荐: `obsidian-bases`, `json-canvas`
- 任务相关: CodeGraph, GitHub connector/`gh`, PDF/document runtime, browser/web search

### 3. 日常入口

优先使用两个入口 skill：

- `nahida-update`: 加入或更新知识。适合论文、论文目录、GitHub 仓库、网页、段落、研究关键词、每日更新和已有笔记吸收。
- `nahida-query`: 只查询现有 vault。默认不联网、不抓 DOI/arXiv/GitHub、不读取 vault 外部文件，也不用模型常识补齐缺口。

在 Codex 里可以用自然语言写 `使用 nahida-update ...`，也可以显式写 `$nahida-update`、`$nahida-query` 这样的 skill 名。`/nahida-update` 只有在你的客户端把 slash command 映射到 skill 时才适用；本仓库示例统一使用 `$nahida-*`。

### 4. 科研与开发工作流示例

Nahida 可以配合科研使用：读论文、整理 related work、抽出研究问题、追踪 open problems、比较方法路线、生成后续调研队列。

Nahida 也可以配合开发使用：分析 GitHub 仓库、沉淀架构和模块模式、把工程实现挂到相关知识节点、查询某类系统设计的已有方案和边界。

#### 读一篇论文

```text
$nahida-update
把 /path/to/paper.pdf 加入 Nahida。需要 deep-read，不要只读摘要。
输出要求：
1. 写一个独立 paper source note。
2. 判断它解决的问题、所属 domain/direction/topic。
3. 如果缺 foundation，指出要补哪些基础概念或资料。
4. 吸收到 Source + Knowledge + Bridge 架构。
5. 最后给出新增/更新的 note 路径、关系路径、缺口和下一步建议。
```

适合科研场景：精读论文、整理创新点、把论文放进已有问题脉络。适合开发场景：从论文中抽取可实现的协议、系统设计、benchmark 和工程风险。

#### 导入一个论文目录

```text
$nahida-update
把 ~/Desktop/papers 下面的论文加入 Nahida。
先 inventory、去重、粗分类和排队；然后串行处理：
每次 deep-read exactly one PDF，写 source note，吸收到 knowledge/bridge，checkpoint 队列，再继续下一篇。
```

适合建立一个方向的本地 literature base。队列未完成时，Nahida 应该报告 next item、remaining count 和 resume command，而不是假装全部吸收完成。

#### 分析一个 GitHub 仓库

```text
$nahida-update
分析 https://github.com/owner/repo 并加入 Nahida。
重点看它解决的问题、架构、核心模块、入口/API、数据流、配置面、测试/示例、README 和代码是否一致，以及可复用实现模式。
不要把 clone 的仓库存进 vault，只保留结构化 repo source note 和证据引用。
```

适合开发场景：快速理解开源项目、比较架构选择、沉淀实现模式。适合科研场景：把论文系统和真实实现对应起来，找到 artifact/reproducibility gap。

#### 加入网页、博客或技术文档

```text
$nahida-update
把 https://example.com/article 加入 Nahida。
先判断它是 official docs、reference、concept explainer、engineering blog 还是 news。
如果是稳定资料，写 source note 并吸收到相关 knowledge node；如果只是新闻或弱信号，放入 freshness/watch/review，不要直接改 evergreen knowledge。
```

适合补基础概念、官方 API、标准、工程实践和近期动向。网页如果只是热度信号，应该进入 watchlist 或 review queue。

#### 调研一个方向

```text
$nahida-update
调研 data availability sampling。
目标是补 foundation sources，整理核心问题、方法族、代表论文/仓库、评测轴和 open problems，并吸收到 Nahida。
```

适合从一个关键词启动新方向。这个模式允许联网搜索；和 `nahida-query` 的 vault-only 查询不同。

#### 查询知识库已有内容

```text
$nahida-query
zk-SNARKs 有哪些可以优化的地方？
请只基于 Nahida 现有笔记回答，给出结论、覆盖状态、依据、关系路径、缺口和建议更新。
```

`nahida-query` 的重点是复用上层分层，而不是扫所有 source notes。它应该优先走：

```text
domain knowledge -> direction knowledge -> problem/method/application knowledge -> bridge -> selected source notes
```

#### 查询输出示例

实际 Codex 会在答案前后出现一些运行话语；README 里只展示核心输出形状：

```text
结论
按 Nahida 当前库内资料，zk-SNARKs 的优化空间主要分成这些方向：

1. 证明生成时间
   优化 prover 的主耗时模块，尤其是 NTT/FFT、MSM、有限域运算和椭圆曲线运算。
   相关路线包括 GPU、多 GPU、ASIC、硬件感知调度。库内证据主要来自 GZKP、PipeZK、zk-Bench。

2. 证明生成内存
   降低峰值内存、减少 pass 数、支持 streaming witness/R1CS。
   相关路线包括 memory-efficient SNARKs、elastic SNARKs、folding-based constructions、hash-bound circuit partitioning。

3. 分布式证明生成
   把大电路、大批量证明、zkRollup prover workload 拆到多机或多阶段执行。
   目标通常是提升吞吐量，而不只是优化单机延迟。

4. 递归、聚合与 folding
   用 proof aggregation 或 folding schemes 降低批量验证成本，或把长计算压缩成递归/增量证明。

5. 电路与算术层优化
   优化 arithmetization、constraint 数量、lookup、range proof、hash gadget、浮点运算、ML operator。

查询模式
vault_only。只查本地 Nahida vault，没有联网，也没有把它当作“最新全网综述”。

覆盖状态
能回答主要优化方向，但基础综述还不完整。核心节点 zk-SNARKs 当前仍标注 foundation/review 相关缺口。

依据
- vault/04_Knowledge/zero-knowledge-proofs/proof-systems/zk-snarks.md
- vault/04_Knowledge/zero-knowledge-proofs/proof-systems.md
- vault/04_Knowledge/zero-knowledge-proofs/research-dynamics.md
- vault/04_Knowledge/zero-knowledge-proofs/proof-systems/hardware-accelerated-proving.md
- vault/04_Knowledge/zero-knowledge-proofs/proof-systems/memory-efficient-snarks.md
- vault/04_Knowledge/zero-knowledge-proofs/proof-systems/distributed-proof-generation.md

关系路径
zero-knowledge-proofs -> proof-systems -> zk-snarks
主要分支包括 hardware-accelerated-proving、memory-efficient-snarks、distributed-proof-generation、proof-aggregation、commit-and-prove、zkML、proof-system-benchmarking。

新近性
库内 ZKP 研究动态的 evidence window 是 2026-06-11 到 2026-06-23，最后综合时间是 2026-06-23。
这说明 Nahida 当前笔记是较新的本地综合，但不是外部最新趋势检索。

缺口
Groth16、Pinocchio、PLONK、STARK 等基础源不全；SnarkPack/TIPP/Groth16 aggregation 源不全；
当前 GPU/FPGA/ASIC prover 生态、生产级 repo 和横向 benchmark 仍需要补。

建议更新
后续最值得补三包：基础 proof system pack，聚合/递归/folding pack，硬件与 benchmark pack。
可以用 nahida-research-search 补 foundation/search，用 nahida-github-repo-analyze 补实现与复现证据。
```

这个输出模式对科研有用，因为它不只回答“有哪些论文”，还会暴露研究问题、路线分叉和缺口。对开发也有用，因为它会把算法/系统优化落到工程瓶颈、benchmark、repo evidence 和复现风险上。

### 5. 更新与查询的区别

`nahida-update` 是 bottom-up：先把一个来源读成完整 source note，再把它对领域、问题、方法族和 bridge 的影响吸收到上层。

`nahida-query` 是 top-down：先读 `04_Knowledge/` 的领域/方向/问题节点，再读 `05_Bridges/`，只有需要证据细节时才打开少量 `03_Sources/`。如果 vault 没有覆盖，它应该明确说 `知识库没有记录`、`知识库只有部分记录` 或 `知识库没有足够新近资料`，然后建议具体 update 动作。

### 6. 批量论文目录

给一个论文目录时，Nahida 应该先做 inventory、去重、粗分类和队列，然后串行处理：

1. 每次只 deep-read 一个 PDF。
2. 写一个独立 paper source note。
3. 吸收到相关 `04_Knowledge/` 和 `05_Bridges/`。
4. checkpoint 队列、报告和 review queue。
5. 继续下一个 pending item，直到队列完成、用户设限或遇到 blocker。

## 仓库结构

```text
vault/
  00_System/       Nahida 规范、schemas、templates、Obsidian Bases
  01_Inbox/        临时入口
  02_Raw/          raw/staging 占位；本公开仓库不保存本地 PDF 原文
  03_Sources/      paper/repo/web 等来源笔记
  04_Knowledge/    分层知识节点
  05_Bridges/      跨知识节点关系
  90_Generated/    共享索引和本地运行产物
    indexes/       可入库的检索索引
    reports/       本地报告；git ignore
    runs/          本地运行记录；git ignore
    ledgers/       本地 ledger；git ignore
    review-queues/ 本地 review queue；git ignore
skills/            nahida-* Codex skills
docs/              使用说明和 skill 说明
scripts/           本地安装/辅助脚本
```

`90_Generated/indexes/` 会进入 Git，因为它是跨环境可复用的检索辅助。`90_Generated/reports/`、`runs/`、`ledgers/`、`review-queues/`、PDF 抽取全文、运行日志、报告和队列文件不会进入 Git。公开仓库保留的是可读的结构化知识、共享索引和 skill，不包含本地论文 PDF 文件。

## 现有内容梗概

当前快照包含约 118 篇 paper source notes、115 个 knowledge nodes、68 个 bridge notes。覆盖重点集中在区块链系统、分布式系统、零知识证明、可验证计算、机器学习系统和算法工程。

### Zero-Knowledge Proofs

`zero-knowledge-proofs` 是目前最重的知识域，覆盖：

- proof systems: zk-SNARKs、modular zkSNARKs、commit-and-prove arguments、memory-efficient SNARKs、distributed proof generation、hardware-accelerated proving、proof-system benchmarking、verifiable encryption。
- polynomial commitments: KZG commitments、FRI/IOPPs，以及它们和 data availability、recursion、aggregation 的关系。
- recursion and folding: Halo/Nova-style recursive proof composition、folding schemes、accumulation schemes、SNARK proof aggregation。
- zkML: verifiable inference、verifiable training、verifiable aggregation、zk-friendly ML operators。
- applications: verifiable database queries、privacy-preserving blockchain authentication、location proofs、cross-chain privacy/auditing。

代表来源包括 Nova、LegoSNARK、Geppetto、DIZK、GZKP、SAVER、zk-Bench、Hekaton、Siniel、Split Prover SNARKs、PipeZK、Gemini、Epistle、Hobbit、ZKSQL、vSQL、zkCNN、ZENO、zkLLM、Sparrow 等论文笔记。

### Blockchain Systems

`blockchain-systems` 组织区块链系统问题，而不是按单篇论文建目录。当前覆盖：

- consensus/finality: Tendermint、Casper FFG、Cobalt、permissioned blockchain consensus、BFT governance。
- scaling and sharding: OmniLedger、ByShard、RingBFT、LightCross、cross-shard execution。
- data availability and light clients: LazyLedger/Celestia-style DA、fraud proofs、data availability sampling、FRIDA。
- mempool and networking: Narwhal/Tusk-style shared mempool。
- execution and transactions: smart contract execution、nested contract transaction、leaderless execution、fair exchange、contingent service payments。
- interoperability: cross-chain protocols、atomic cross-chain transactions、cross-chain messaging、bridge/auditing、smart contract invocation。
- data management and storage: blockchain relational database、state storage、query/indexing、off-chain data management、decentralized storage networks。

### Distributed Systems

`distributed-systems` 是很多区块链和数据库问题的基础层。当前覆盖：

- consensus: CFT、BFT、Raft、PBFT、asynchronous BFT、validated asynchronous Byzantine agreement。
- asynchronous primitives: reliable broadcast、verifiable secret sharing、distributed key generation、asynchronous data dissemination。
- transaction processing: distributed transactions、replicated database concurrency control、Calvin/C5/Starry 等 source extensions。
- data management and storage: LSM-tree storage engines、CRDT/CALM、content-addressed storage、erasure-coded storage、privacy-preserving database queries。

这层负责把 Raft/PBFT/Tendermint/ByShard 等具体协议挂到更通用的 fault model、consensus 和 transaction-processing 问题上。

### Verifiable Computation

`verifiable-computation` 覆盖委托计算和低成本验证问题，当前重点是：

- interactive proofs、GKR protocols、sum-check protocol。
- delegated computation 和 QAP-based verifiable computation systems。
- 与 SNARK、memory-efficient proving、polynomial commitments 的 bridge。

代表来源包括 Interactive Proofs for Muggles、Sum-check Protocol、Geppetto、Time-Optimal Interactive Proofs for Circuit Evaluation 等。

### ML Systems

`ml-systems` 目前主要覆盖可信机器学习、合成数据和训练系统：

- privacy and trustworthy ML: federated learning integrity、trustworthy distributed ML、LLM inference privacy。
- synthetic data generation: tabular/time-series synthetic data、collaborative synthetic data generation、synthetic data evaluation、privacy evaluation。
- training systems: DNN training parallelism，例如 PipeDream。
- 与 zkML、blockchain coordination、synthetic data privacy 的 bridge。

代表来源包括 zkFL、TDML、CTGAN、FTS-Diffusion、EndSDG、How Faithful is your Synthetic Data?、Risk-Aware Privacy Preservation for LLM Inference 等。

### Algorithm Engineering

`algorithm-engineering` 当前是较小但有明确边界的 seed domain，覆盖 graph algorithms 和 graph partitioning：

- multilevel graph partitioning。
- streaming graph partitioning。
- METIS-style implementation/evaluation patterns。

它未来可以向分布式图处理、调度、证明生成 pipeline 优化等方向建立 bridge，但当前仍标记为窄覆盖。

### Bridges

`05_Bridges/` 记录跨节点关系，避免把不同领域混成一团。当前 bridge 包括：

- BFT/CFT 与 permissioned blockchain、sharded ledgers、shared mempool 的关系。
- data availability、FRI、fraud proofs、sharding 和 light clients 的关系。
- zk-SNARKs 与 zkML、cross-chain bridges、privacy-preserving authentication、verifiable encryption 的关系。
- folding schemes、polynomial commitments、sum-check、memory-efficient SNARKs 和 proof aggregation 的关系。
- distributed transactions 与 atomic cross-chain transactions、smart contract invocation 的关系。
- synthetic data generation、privacy evaluation、trustworthy ML、LLM inference privacy 与 zkML/verifiable inference 的边界关系。

## 质量状态与边界

这个仓库是一个持续更新的研究知识库快照，不是完整百科。很多顶层域仍标记为 `foundation_thin`，意思是已有 source-backed 结构和代表来源，但仍需要更多 foundation sources、仓库分析、标准/教材/综述资料或 freshness update 来变成更稳的 evergreen coverage。

查询时请以 vault 内已有证据为准。需要最新进展、未导入论文、未分析 GitHub 仓库或缺失基础概念时，应显式使用 `nahida-update`、`nahida-research-search`、`nahida-paper-read` 或 `nahida-github-repo-analyze`。

## License

No license has been selected yet.
