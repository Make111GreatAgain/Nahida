---
id: "doi:10.3846/jcem.2023.18646"
title: "Decentralized System for Construction Projects Data Management Using Blockchain and IPFS"
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
  - "p1 abstract, contribution, construction progress-control problem"
  - "p1-p5 literature review on blockchain, Hyperledger Fabric, construction BT use cases and IPFS/IPFS-Cluster"
  - "p5-p9 proposed system design, stakeholders, chaincodes, channels, IPFS/private-cluster architecture and data flow"
  - "p9-p12 system development, chaincode functions, network configuration, private IPFS setup and UI layer"
  - "p12-p15 mosque-project case study, progress-record and as-built-asset update workflow"
  - "p15-p17 latency, block-size reduction, generalization, security/privacy and adoption discussion"
  - "p17-p18 conclusions, limitations, future work"
safe_for_absorption: true
canonical_url: "https://doi.org/10.3846/jcem.2023.18646"
doi: "10.3846/jcem.2023.18646"
arxiv_id: ""
venue: "Journal of Civil Engineering and Management"
year: "2023"
pdf_pages: 18
pdf_sha256: "d508c2337642e174613521518148aa1b20f4d582248a64c9bfd8f04c5bb0be61"
local_pdf: "~/Desktop/paper/18646-Article Text-74016-2-10-20230321.pdf"
extracted_text_path: "vault/02_Raw/pdf/extracted/18646-article-text-74016-2-10-20230321-d508c2337642-pages.txt"
pdf_extractor: "codex-bundled-python:pypdf"
hierarchy_level: "source"
domain_id: "blockchain-systems"
direction_id: "data-management-and-storage"
topic_ids:
  - "off-chain-application-data-management"
  - "blockchain-ipfs-data-management"
  - "construction-project-data-management"
ontology_path:
  - "blockchain-systems"
  - "data-management-and-storage"
  - "off-chain-application-data-management"
primary_ontology_path: "blockchain-systems/data-management-and-storage/off-chain-application-data-management/doi-10-3846-jcem-2023-18646"
secondary_ontology_paths:
  - "blockchain-systems/execution-and-transactions/permissioned-application-workflows/doi-10-3846-jcem-2023-18646"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "blockchain-systems"
    - "construction-informatics"
  directions:
    - "data-management-and-storage"
    - "off-chain-application-data-management"
  topics:
    - "blockchain-IPFS application data management"
    - "content-addressed off-chain assets"
    - "permissioned blockchain workflow"
    - "construction progress monitoring"
domains:
  - "blockchain-systems"
  - "construction-informatics"
topics:
  - "off-chain application data management"
  - "IPFS"
  - "IPFS-Cluster"
  - "Hyperledger Fabric"
  - "construction progress monitoring"
  - "as-built digital assets"
  - "content-addressed storage"
  - "permissioned blockchain"
aliases:
  - "Blockchain-IPFS construction data management"
  - "Decentralized construction project data management"
  - "Fabric + IPFS construction progress system"
tags:
  - "nahida/source"
  - "paper"
  - "blockchain-systems"
  - "data-management-and-storage"
  - "off-chain-application-data-management"
  - "construction-informatics"
direction_facets:
  parent_domain:
    - "blockchain-systems"
    - "construction-informatics"
  subdomain:
    - "data-management-and-storage"
    - "off-chain-application-data-management"
  problem:
    - "construction progress monitoring produces large textual and visual data flows that are slow, error-prone and centrally mediated"
    - "large visual/as-built assets stored directly on-chain would bloat blocks and degrade blockchain performance"
    - "on-chain hashes alone do not provide off-chain file availability, replication or lifecycle management"
    - "multi-stakeholder construction workflows need traceability, authorization, non-repudiation and privacy boundaries"
  method_family:
    - "permissioned Hyperledger Fabric ledger for textual progress metadata and IPFS content identifiers"
    - "private IPFS network for large progress visuals and as-built digital assets"
    - "IPFS-Cluster pinning, replication, unpinning and garbage-collection lifecycle"
    - "channel separation and chaincodes for progress records and as-built asset updates"
  system_layer:
    - "application data-management layer"
    - "permissioned blockchain workflow"
    - "off-chain content-addressed storage"
    - "project progress monitoring and asset handover"
  evaluation_context:
    - "mosque facade construction case study in Egypt"
    - "Hyperledger Fabric network hosted via IBM Blockchain Platform"
    - "private IPFS plus IPFS-Cluster"
    - "latency monitoring with IBM Cloud Function"
    - "block-size reduction calculation for smartphone progress images and as-built assets"
  bridge:
    - "permissioned blockchain workflows to construction project controls"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-update-20260611-paper-domain-serial-v2"
  - "nahida-knowledge-20260623-blockchain-ipfs-construction-data-management"
source_refs:
  - "doi:10.3846/jcem.2023.18646"
  - "pdf:~/Desktop/paper/18646-Article Text-74016-2-10-20230321.pdf"
confidence: "high"
trust_tier: "primary"
primary_direction: "blockchain-systems -> data-management-and-storage"
secondary_directions:
  - "construction-informatics -> progress-monitoring"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "abstract and introduction target progress data exchange and as-built digital asset management rather than consensus"
  - "system design stores textual data and IPFS CIDs on Hyperledger Fabric while storing large visuals/assets off-chain"
  - "evaluation measures transaction latency and block-size reduction, not consensus safety or throughput under faults"
  - "queue path corrected from blockchain-systems/consensus/consensus-foundations to blockchain-systems/data-management-and-storage/off-chain-application-data-management"
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0079"
queue_status: "absorbed"
---

# Decentralized System for Construction Projects Data Management Using Blockchain and IPFS

## 论文身份

- 标题: Decentralized System for Construction Projects Data Management Using Blockchain and IPFS
- 作者: Kareem Adel, Ahmed Elhakeem, Mohamed Marzouk
- 期刊: Journal of Civil Engineering and Management, 2023, 29(4): 342-359
- DOI: `10.3846/jcem.2023.18646`
- 本地 PDF: `~/Desktop/paper/18646-Article Text-74016-2-10-20230321.pdf`
- 抽取文本: `vault/02_Raw/pdf/extracted/18646-article-text-74016-2-10-20230321-d508c2337642-pages.txt`
- SHA-256: `d508c2337642e174613521518148aa1b20f4d582248a64c9bfd8f04c5bb0be61`
- 备注: 队列原始 title 被第一页 CC BY 许可文本误污染；本 note 已按论文首页标题修正。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `codex-bundled-python:pypdf`
- 页数: 18
- 已覆盖章节/页码: Abstract, Introduction, Literature review, Proposed system design, System development, Testing, Performance evaluation, Discussion, Conclusions。
- Extraction gaps: 图中界面截图和架构图按正文描述吸收；未重新运行作者系统或读取外部网页。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 |
| --- | --- | --- | --- |
| Abstract, Introduction / p1-p2 | 问题与目标 | 施工进度跟踪存在中心化、中介化、人工错误、延迟、不完整和视觉数据管理问题；目标是用 BT + IPFS 支撑 P2P 数据流 | high |
| §1.1-§1.3 / p2-p5 | 技术背景 | 说明 BT、Hyperledger Fabric、施工领域 BT 研究、IPFS 和 IPFS-Cluster | high |
| §2 / p5-p9 | 系统设计 | 三类组织、两条 Fabric channel、两个 chaincode、private IPFS/IPFS-Cluster、十步数据处理流程 | high |
| §3 / p9-p12 | 系统开发 | chaincode functions 和字段、Fabric/IBM Blockchain Platform 配置、private IPFS/bootstrap/swarm key/cluster setup、serverless UI | high |
| §4 / p12-p14 | 测试案例 | 埃及清真寺项目 facade works；现场图片/日报进入 progress chaincode，as-built XER/4D/5D BIM 进入 asset chaincode | high |
| §5 / p14-p16 | 性能评估 | 写/读延迟、两条 chaincode 的平均操作时间、block-size reduction 公式和结果 | high |
| §6-Conclusion / p16-p18 | 讨论与边界 | 理论/实践意义、TOE 采纳因素、CFT 共识和人工采集限制、未来 DCPS/IoT/AI/digital twins | high |

## 一句话贡献

这篇论文把施工项目的进度文本、现场视觉证据和 as-built 数字资产拆成“链上可审计元数据 + 链下内容寻址文件”的两层数据管理系统，用 Hyperledger Fabric 记录进度/资产事务和 IPFS CIDs，用 private IPFS/IPFS-Cluster 存储、复制、pin/unpin 大文件，从而在不把照片、视频、BIM 等大对象直接写入区块链的前提下保留可追溯性和多方信任。

## 核心问题设定

施工进度控制是重复、数据密集且跨组织的流程。现场人员需要持续采集日报、照片、视频、laser scans、nD BIM 相关文件和合同/图纸状态，并把这些信息传给业主、咨询方、承包商、供应商、金融机构和争议处理方。传统系统通常依赖中心化平台、邮件或人工交接，容易出现单点故障、篡改风险、同步不及时、视觉数据积累失控和信息缺口。

论文的核心问题不是区块链共识，而是 [[04_Knowledge/blockchain-systems/data-management-and-storage/off-chain-application-data-management|Off-chain Application Data Management]]: 应用领域的大文件和多方工作流如何在链上保持可审计、不可抵赖和可授权的元数据，同时把大容量内容放到可验证、可复制、可生命周期管理的链下存储中。

## 系统设计

### 参与者和权限边界

系统把参与者分成三类组织:

| 组织 | 角色 | 访问能力 |
| --- | --- | --- |
| Organization I | Portfolio Manager, Project Manager, Project Team, System Developer | 读写进度数据和资产更新 |
| Organization II | Client, Consultant | 读写/验证进度数据和资产更新 |
| Organization III | Suppliers, Financial Institutions, Claim-dispute Adjudicators, Sub-Contractors | 只读相关数据 |

每个参与节点同时配置 blockchain node、IPFS node 和 IPFS-Cluster node。Fabric 的 CA/MSP/证书用于身份认证和授权，channel 用于隔离数据可见性。

### 两条链上数据流

系统定义两个 chaincode 和两个 channel:

| Chaincode / channel | 数据对象 | 参与范围 | 链上保存内容 |
| --- | --- | --- | --- |
| Progress chaincode / C01 | 施工进度记录 | 所有组织 | progress textual fields、唯一 progress code、相关视觉数据 CID |
| As-built Asset chaincode / C02 | as-built 数字资产更新 | Organization I 和 II | asset update metadata、版本/类别/状态、关联进度记录范围、数字资产 CID |

这种切分让公开度更高的进度证据和更敏感的 as-built asset 演进分离，避免把所有项目数据暴露给所有参与方。

### 链上/链下拆分流程

论文的十步流程可以压缩成两段:

1. 现场采集文本、图片、视频、laser scan 等进度信息。
2. 大型视觉文件进入 private IPFS/IPFS-Cluster，系统取得 CID。
3. 文本进度数据、进度编号和 CID 提交到 Fabric 的 progress channel。
4. chaincode 验证、timestamp、打包成区块并分发到 channel ledger。
5. 链上 progress records 导出为 JSON，用于更新 XER schedule、4D/5D BIM 或其他 as-built 数字资产。
6. 更新后的 as-built digital assets 进入 private IPFS/IPFS-Cluster，系统取得 CID。
7. 资产更新元数据、关联进度范围和 CID 提交到 asset channel。
8. 若链上事务未通过验证，相关链下视觉/资产通过 IPFS-Cluster unpin 并经 garbage collection 移除。

关键点是 CID 作为链上/链下边界: 链上记录“哪个版本、谁提交、何时提交、对应哪个内容地址”，链下负责实际大对象存储和复制。

## 方法与实现

### Hyperledger Fabric 侧

论文选择 Hyperledger Fabric 的理由是 permissioned、无挖矿、多 channel、可插拔和适合企业/施工场景。系统用 IBM Blockchain Platform/Kubernetes 配置 CA、MSP、peer、ordering service、channels、chaincodes 和 connection profiles，并通过 IBM Cloud Function/Node.js serverless UI 暴露用户界面。

两个 chaincode 都包含 `Exist`, `Add`, `Read`, `Update`, `Delete`, `Query` 操作。Progress 记录字段包括 progress code、cut-off date、activity code/name/status、engineer、remaining duration、actual cost、percent complete、data provider、labor/non-labor/material usage、remarks 和 CID。Asset update 记录字段包括 asset updating code、title、version、category、status、updating date、updator、on-chain records range 和 CID。

### IPFS/IPFS-Cluster 侧

系统使用 private IPFS 网络，而不是公共 IPFS。基本配置包括 `ipfs init`、生成 swarm key、移除公共 bootstrap 节点、添加系统开发者节点作为 bootstrap，再启动 daemon。IPFS-Cluster sidecar 通过 `ipfs-cluster-service init` 和 bootstrap 配置来管理 pinning。

IPFS-Cluster 在本论文中很重要，因为单纯把文件放进 IPFS 只能得到内容地址，不自动保证多节点长期可用。Cluster 提供 pin、replicate、unpin、propagation 和 garbage collection 的管理层，让系统可以在链上验证失败时撤销无效链下对象，也可以为有效对象提供复制和可用性。

## 测试与评估

### 案例

案例是埃及一个清真寺项目的 facade works，两层建筑、面积约 1041 m2，包含四个 facade activities 和 39 个工作日。测试数据包括现场手机图片和每日工作报告。流程是现场进度图片先存入 IPFS，CID 与文本进度一起上链；client representative 验证后写入 block/ledger；之后 Primavera P6 的 XER schedule 和 as-built 版本被更新，新的资产文件也以 CID 形式写入 asset channel。

### 延迟

论文用 IBM Cloud Function monitoring 统计 10 次操作的延迟:

| Chaincode | 写操作平均延迟 | 读操作平均延迟 | 备注 |
| --- | --- | --- | --- |
| Progress chaincode | Add 4389 ms; Update 4382 ms; Delete 4340 ms | Read 1666 ms; Query 1683 ms | 写操作最高约 4882 ms；读操作最高约 1718 ms |
| Asset chaincode | Add 4464 ms; Update 4367 ms; Delete 4395 ms | Read 1702 ms; Query 1737 ms | 写操作最高约 4711 ms；读操作最高约 1793 ms |

解释边界: 这些数值是特定 Fabric/IBM Cloud Function/案例原型的工程结果，不能直接外推为 Fabric 或 IPFS 的通用性能上限。

### Block-size reduction

论文用 `BCR = (OBS - CBS) / OBS * 100` 估计链上/链下拆分带来的 block-size reduction，其中 `CBS = FCS + TRS`，`OBS = FCS + ASV`。`FCS` 是固定链上字段大小，`TRS` 是文本记录大小，`ASV` 是链下 visual/asset 文件大小。

在案例中，固定链上字段约 719 bytes，progress textual record 约 500-1000 bytes，而手机图片约 2-3 MB。论文报告 channel 1 的 BCR 为 99.91%，channel 2 的 BCR 为 97.58%。这说明该系统的主要收益不是提高共识吞吐，而是避免把大型视觉/资产数据直接写入区块链 block，同时保留 CID 关联。

## 采纳与影响

论文用 TOE framework 总结采纳因素:

| 维度 | 因素 |
| --- | --- |
| Technological | relative advantage, compatibility, complexity |
| Organizational | top management support, organizational readiness |
| Environmental | competitive pressure, government policy/support, partner readiness/support |

实际影响包括: 提升项目 stakeholder coordination/trust；跟踪 as-built assets 演进并早发现缺陷；支撑 progress-based incremental payments；计算 AC/EV/PV、cost/schedule indices/variances；支持 productivity analysis；为 delay/claim/dispute 管理提供 tamper-proof log；把 construction phase 数据更平滑地交接到 operation and maintenance phase。

## 限制与边界

- Fabric 网络采用 CFT 共识假设。论文明确指出这有性能、可扩展性和 crash resilience 优势，但不能覆盖 malicious activity threats；未来需要比较不同 consensus algorithms 对 latency、scalability、privacy 和 security 的影响。
- Progress acquisition 和 digital asset updates 仍主要依赖人工输入和手动更新。未来可接入 DCPS、LADAR、RFID、IoT、reality capture、digital twins、AI text mining 和动态 web dashboard。
- 链上 CID 提供内容绑定和可审计引用，但不自动提供链下可用性、激励或长期保存；本论文通过 private IPFS + IPFS-Cluster 解决工程可用性，但不是通用数据可用性协议。
- 施工领域采纳速度慢，组织准备度、伙伴支持、政策环境和流程兼容性可能比技术可行性更关键。

## Knowledge Handoff

| Target | Role | Absorption decision |
| --- | --- | --- |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/off-chain-application-data-management|Off-chain Application Data Management]] | primary problem node | 新建 active_seed，吸收链上元数据/链下大对象、CID、private IPFS/IPFS-Cluster 和 permissioned workflow 的通用模式 |
| [[04_Knowledge/blockchain-systems/data-management-and-storage|Blockchain Data Management and Storage]] | parent direction | 增加 application-data route，区别于 state storage 和 stateless consensus storage |
| [[04_Knowledge/blockchain-systems/data-management-and-storage/blockchain-state-storage|Blockchain State Storage]] | sibling boundary | 不写入本节点；本论文处理 application files/assets，而不是 blockchain state/MPT/full-state commitments |
| [[04_Knowledge/blockchain-systems/blockchain-consensus/permissioned-blockchain-consensus|Permissioned Blockchain Consensus]] | contextual dependency | 只作为 Fabric/CFT assumption 的边界，不把论文归为 consensus |

## Source Extensions

| Knowledge path | 新增/修正内容 | 是否创建/更新 | 证据 |
| --- | --- | --- | --- |
| `blockchain-systems/data-management-and-storage/off-chain-application-data-management` | application data 的链上/链下拆分、CID、IPFS-Cluster lifecycle、permissioned access boundary | create | p1-p18 |
| `blockchain-systems/data-management-and-storage` | 从 state storage 扩展到 application-level large-object data management | update | p1-p18 |
| `blockchain-systems/consensus/consensus-foundations` | 从队列误分类中移除 | no write | 论文评估对象不是 consensus |

## 复核问题

- 是否需要未来建立 `construction-informatics/progress-monitoring` domain: 当前只有一篇 source，不创建 domain；后续若用户继续导入施工/工程管理论文，可再拆。
- 是否需要建立 `IPFS` 基础概念元笔记: 本文定义了 IPFS/IPFS-Cluster 的使用，但 vault 中还缺独立基础来源；如果后续多篇 paper/repo 复用 IPFS，应通过 `nahida-research-search` 或 repo/source intake 建基础概念。
- 是否要把 Hyperledger Fabric 作为基础概念: 当前已有 Fabric 交易处理 source；本论文只把 Fabric 当 permissioned workflow substrate，不新增 Fabric 节点。

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-23 | nahida-knowledge-20260623-blockchain-ipfs-construction-data-management | Created source note and classified paper under off-chain application data management. | doi:10.3846/jcem.2023.18646 | codex |
