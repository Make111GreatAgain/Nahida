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

常用请求示例：

```text
使用 nahida-update，把 /path/to/paper.pdf 这篇论文加入 Nahida。需要精读，并吸收到 Source + Knowledge + Bridge 架构。
```

```text
使用 nahida-update，分析 https://github.com/owner/repo 并加入 Nahida。重点看它解决的问题、架构、核心模块、API、数据流和可复用实现模式。
```

```text
使用 nahida-update，调研 data availability sampling，补充 foundation sources 并吸收到知识库。
```

```text
使用 nahida-query，Nahida 里关于 zk-SNARK proof aggregation 已经有什么？请给出来源、关系路径和缺口。
```

```text
使用 nahida-consolidate，只基于现有笔记优化当前知识库，不重新读论文、仓库或网页。
```

```text
使用 nahida-audit，检查重复 ID、坏 wikilink、弱 knowledge node、bridge 质量和 legacy 输出。
```

### 4. 更新与查询的区别

`nahida-update` 是 bottom-up：先把一个来源读成完整 source note，再把它对领域、问题、方法族和 bridge 的影响吸收到上层。

`nahida-query` 是 top-down：先读 `04_Knowledge/` 的领域/方向/问题节点，再读 `05_Bridges/`，只有需要证据细节时才打开少量 `03_Sources/`。如果 vault 没有覆盖，它应该明确说 `知识库没有记录`、`知识库只有部分记录` 或 `知识库没有足够新近资料`，然后建议具体 update 动作。

### 5. 批量论文目录

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
  90_Generated/    本地生成缓存、日志、报告、ledger、队列；已被 git ignore
skills/            nahida-* Codex skills
docs/              使用说明和 skill 说明
scripts/           本地安装/辅助脚本
```

`90_Generated/`、PDF 抽取全文、运行日志、报告、队列文件不会进入 Git。公开仓库保留的是可读的结构化知识和 skill，不包含本地论文 PDF 文件。

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
