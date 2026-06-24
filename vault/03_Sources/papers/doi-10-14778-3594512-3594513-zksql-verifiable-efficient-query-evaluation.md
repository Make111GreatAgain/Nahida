---
id: "doi-10-14778-3594512-3594513-zksql-verifiable-efficient-query-evaluation"
title: "ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs"
type: "source"
source_type: "paper"
source_kind: "pdf"
source_subtype: "paper_local"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "deep_read_complete"
reading_status: "deep_read_complete"
reading_depth: "deep_read"
safe_for_absorption: true
trust_tier: "primary"
source_identity:
  type: "doi"
  key: "doi:10.14778/3594512.3594513"
source_refs:
  - "doi:10.14778/3594512.3594513"
  - "sha256:4c00bad786942e3c09aa041be45a3fa7c53a3699f954290f89b3cf425b4e2d42"
  - "filename:p1804-li.pdf"
representative_source_refs:
  - "doi:10.14778/3594512.3594513"
authors:
  - "Xiling Li"
  - "Chenkai Weng"
  - "Yongxin Xu"
  - "Xiao Wang"
  - "Jennie Rogers"
year: "2023"
doi: "10.14778/3594512.3594513"
arxiv_id: ""
canonical_url: "https://doi.org/10.14778/3594512.3594513"
venue: "Proceedings of the VLDB Endowment 16(8):1804-1816"
artifact_url: "https://github.com/vaultdb/zksql"
local_pdf: "~/Desktop/paper/p1804-li.pdf"
pdf_sha256: "4c00bad786942e3c09aa041be45a3fa7c53a3699f954290f89b3cf425b4e2d42"
extracted_text_path: "vault/02_Raw/pdf/extracted/p1804-li-zksql-verifiable-efficient-4c00bad78694-pages.txt"
pages: 13
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
primary_ontology_path: "zero-knowledge-proofs/applications/verifiable-database-queries"
secondary_ontology_paths:
  - "verifiable-computation/verifiable-computation-systems"
  - "distributed-systems/data-management-and-storage"
domains:
  - "zero-knowledge-proofs"
  - "verifiable-computation"
  - "distributed-systems"
topics:
  - "verifiable-database-queries"
  - "zero-knowledge-sql"
  - "authenticated-query-evaluation"
  - "operator-at-a-time-proofs"
  - "volebased-zero-knowledge"
  - "relational-query-processing"
topic_ids:
  - "verifiable-database-queries"
  - "zero-knowledge-sql"
  - "authenticated-query-evaluation"
query_keys:
  - "ZKSQL"
  - "ZK SQL"
  - "zero-knowledge SQL"
  - "verifiable SQL query evaluation"
  - "authenticated SQL queries"
  - "operator-at-a-time proofs"
  - "set-based ZKSQL"
  - "VOLE SQL proofs"
  - "TPC-H zero-knowledge SQL"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "PDF page 1 title, abstract and PVLDB reference identify ZKSQL as zero-knowledge SQL query evaluation."
  - "Sections 3-4 define commit-and-prove query workflow, operator-level proofs and set-based protocols for SQL operators."
  - "Section 5 evaluates Project, Filter, Join, Sort and Aggregate over TPC-H queries."
  - "The queued distributed-transactions path is wrong: the paper does not address transaction commit, isolation, replication or concurrency control."
parent_knowledge_refs:
  - "nahida-knowledge-verifiable-database-queries"
  - "nahida-knowledge-zkp-applications"
  - "nahida-knowledge-verifiable-computation-systems"
  - "nahida-knowledge-data-management-and-storage"
bridge_refs:
  - "nahida-bridge-privacy-preserving-database-queries-to-verifiable-database-queries"
related_paths:
  - "vault/04_Knowledge/zero-knowledge-proofs/applications/verifiable-database-queries.md"
  - "vault/04_Knowledge/zero-knowledge-proofs/applications.md"
  - "vault/04_Knowledge/verifiable-computation/verifiable-computation-systems.md"
  - "vault/04_Knowledge/distributed-systems/data-management-and-storage.md"
  - "vault/05_Bridges/privacy-preserving-database-queries-to-verifiable-database-queries.md"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0110"
queue_rank: 110
run_ids:
  - "nahida-knowledge-20260623-zksql"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/deep-read"
---

# ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs

## Paper Identity

| Field | Value |
| --- | --- |
| Title | ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs |
| Authors | Xiling Li; Chenkai Weng; Yongxin Xu; Xiao Wang; Jennie Rogers |
| Year | 2023 |
| Venue | Proceedings of the VLDB Endowment 16(8):1804-1816 |
| DOI | `10.14778/3594512.3594513` |
| Artifact | `https://github.com/vaultdb/zksql` |
| Local PDF | `~/Desktop/paper/p1804-li.pdf` |
| Source key | `sha256:4c00bad786942e3c09aa041be45a3fa7c53a3699f954290f89b3cf425b4e2d42` |
| Pages | 13 |
| Extracted text | `vault/02_Raw/pdf/extracted/p1804-li-zksql-verifiable-efficient-4c00bad78694-pages.txt` |

## 精读状态

- Reading status: `deep_read_complete`
- Absorption run: `nahida-knowledge-20260623-zksql`
- Queue item: `nahida-paper-folder-20260611-domain-serial-v2:item:0110`
- Queue title: `ZKSQL: Verifiable and Eﬀicient`
- Metadata correction: PDF metadata title is `Untitled`; title/authors/venue/year/DOI/artifact are corrected from page 1 and the PVLDB reference block.
- Classification correction: queue placed it under `distributed-systems/data-management-and-storage/distributed-transactions`. Deep read corrects the primary path to [[verifiable-database-queries|Verifiable database queries]] because the paper solves cryptographic correctness/completeness and privacy of SQL query answers, not transaction commit, isolation, replication or concurrency control.
- External fetch: not needed. DOI, venue and artifact URL are present in the PDF.

## 一句话贡献

ZKSQL 把关系数据库的 ad-hoc SQL 查询评估放入 commit-and-prove / zero-knowledge workflow 中：prover 对私有数据库作一次 commitment，随后按 query plan 的每个 operator 交互式证明输出正确、完整且不泄露输入记录；其关键效率点是用 set-based polynomial proofs 验证 sort/join 等中间结果性质，而不是把整个 DBMS 执行轨迹逐门电路化。

## 章节地图

| Section/page | 内容 | 对知识库的作用 |
| --- | --- | --- |
| Abstract, 1 / p1-p2 | 说明监管统计、外包数据库和私有数据共享中的 correctness/completeness + privacy 问题；提出 ZKSQL。 | 建立 SQL 级 [[verifiable-database-queries|Verifiable database queries]] source extension。 |
| 2.1 / p2-p3 | 回顾 ZK proofs、commit-and-prove、VOLE-based protocols 和 circuit API。 | 连接 [[verifiable-computation-systems|Verifiable computation systems]]。 |
| 2.2 / p3 | 说明 oblivious query evaluation，需要数据无关 transcript；引入 dummy tuples/tombstones。 | 记录 SQL privacy leakage boundary。 |
| 3 / p3-p5 | 定义 notation、安全模型、commitment workflow、SQL-to-ZK front/back end。 | 记录系统架构和安全假设。 |
| 4.1 / p5-p7 | 定义 ZK set operations: equality、disjoint、intersection、union；用 polynomial identity 与 Schwartz-Zippel 风格检查。 | 记录 set-based proof optimization。 |
| 4.2 / p7-p10 | 给出 Project、Filter、Aggregate 的 circuit route，以及 Sort、Join 的 set-based route。 | 记录 operator-at-a-time proof semantics。 |
| 5 / p10-p12 | EMP Toolkit + PostgreSQL prototype; TPC-H Q1/Q3/Q5/Q8/Q9/Q18 evaluation。 | 记录性能、开销和 scalability evidence。 |
| 6 / p12 | Related work: CorrectDB/VeriDB, IntegriDB/vSQL/zk-vSQL, ZK protocols。 | 校准与 vSQL/zk-vSQL、TEE database verification 的边界。 |
| 7 / p12 | 结论与 future work。 | 记录 limitations: operator order optimization, richer joins, cheaper verification routes。 |

## 背景、动机与问题边界

论文的 motivating case 是数据持有者既要给监管者或公众提供统计值，又不能直接释放个人记录。普通 DBMS 可以算出 SQL answer，却很难让 client 确信 answer 对私有数据库是正确且完整的；如果 client 直接查询底层数据库，又会带来隐私泄露风险。

ZKSQL 的目标是让 prover/data owner 对私有 relational database 先生成 public commitment，然后对 verifier/client 的 SQL 查询返回 answer 与 proof。Verifier 学到 schema、table cardinalities、query、query DAG 和最终 answer，但不学到输入记录和中间结果内容。论文强调这里支持的是 ad-hoc SQL queries，并覆盖 select/project/join/aggregate/group-by/sort/set-operation 风格的 operator，而不是只支持预先固定的函数。

明确不解决的问题:

- 不提供普通数据库事务隔离、并发控制、复制一致性或 commit protocol。
- 不隐藏表 schema、table cardinalities、query text、query DAG 或最终 answer。
- 不解决 query privacy，即 prover 会看到 verifier 提交的 SQL query；它保护的是 prover 的 input records 和中间结果。
- 不把完整 DBMS optimizer、storage layout 或 transaction semantics 证明为正确；它证明 canonicalized plan/operator pipeline 的 authenticated execution。

## 模型、假设与定义

| Element | 说明 | Evidence |
| --- | --- | --- |
| Prover `P` | 私有数据库持有者，能访问 plaintext database `D` 和自己的 commitment share。 | §3, Fig. 2 |
| Verifier `V` | 客户端/监管者，知道 schema/cardinalities/query/DAG/answer，持有 commitment share 和 authentication key。 | §3, Fig. 2 |
| Commitment `[D]` | 每个 bit 生成 authenticated tag，双方只持有 share；setup 一次可用于多个 query。 | §3.2 |
| `FZK` | ideal functionality: Input, Const, Compute, Verify，用于 circuit-based proofs。 | Fig. 1 |
| `FZKSET` | set operations ideal functionality: Equality, Disjoint, Intersection, Union。 | Fig. 3 |
| `FZKSQL` | operator-level ideal functionality: Project, Sort, Filter, Join, Aggregate, Query。 | Fig. 5 |
| Dummy tag | 每个 tuple 额外 bit，删除/过滤时变 tombstone，从而保持 oblivious transcript。 | §2.2, §4.2 |
| Adversary boundary | 支持 malicious prover 和 malicious verifier；基于 VOLE/circuit components 与 set-based protocols 的 simulation/soundness argument。 | §3.1, §4.1.1 |

安全性质:

- Correctness: honest parties 只让 verifier 接受真实 statement。
- Soundness: malicious prover 对 false query answer 几乎不可能通过验证。
- Zero knowledge: malicious verifier 除了 query answer 和其 truthfulness，不学到 witness/input rows。

## 系统机制

### Commit-and-prove workflow

ZKSQL 分成 setup 与 query 两阶段:

1. Setup: `P` 把 private database `D` 输入 commitment protocol，双方获得 authenticated tags `[D]` 的 shares；`P` 仍独自知道 plaintext `D`。
2. Query: `V` 提交 SQL statement；前端解析 schema、生成 operator DAG、canonicalize plan 并输出 verifiable plan JSON。
3. Back end: `P` 与 `V` 按 operator tree 自底向上交互执行 proof；每个 operator 输出 authenticated tags。
4. Answer verification: 根节点输出 answer `A` 后，双方用 `Const(A)` 生成 public answer tags，再用 equality circuit 检查 `[A]` 与 `[A']` 一致。

这个 workflow 的检索意义是: ZKSQL 把数据库查询 proof 从“证明一个巨大 monolithic function”改成“沿 SQL operator pipeline 逐步维护 authenticated intermediate results”。

### SQL front end and back end

前端由 Java 实现，使用 Apache Calcite 解析 SQL，而不是自写 parser。它会把 SQL 转为 DAG 并做 canonicalization:

- eager projection，尽早去掉后续不需要的 attributes；
- rewrite common table expressions；
- combine filters，减少 data pass；
- 为每个 operator 选择 proof template；
- 输出 JSON verifiable plan，让 prover/verifier 从同一个 plan 出发。

后端以 PostgreSQL 作为 private DB back-end，以 EMP Toolkit 的 VOLE-ZK protocols 作为 cryptographic backend。

## Set-based proof route

ZKSQL 的核心优化来自把 set/table 性质转为 polynomial checks，而不是用 circuit trace 执行 sort/join。

### Equality

给定两个 unordered tables `R={r_i}` 与 `S={s_i}`，verifier 抽随机点 `a`，双方在 authenticated values 上打开:

`product_i ([r_i] - a) - product_i ([s_i] - a)`。

如果两个 multiset 相等，则多项式恒为 0；否则随机点恰好为根的概率约 `n / 2^k`，实际取安全参数 `k=128`。为处理大 tuple，先用 universal hashing / Packing 把 `m`-bit tuple 压到 `k`-bit field elements。

### Disjoint / Intersection / Union

- Disjoint: prover 把 `R||S` 排序成 `T`，证明 `T` 与 `R||S` equality，并证明相邻元素严格有序，从而没有重叠。
- Intersection: prover 提供 `P = R \ T` 与 `Q = S \ T`，证明 `P||T = R`、`Q||T = S`，再证明 `P` 和 `Q` disjoint。
- Union: prover 提供 intersection `P = R ∩ S`，先证明 intersection，再证明 `R||S = P||T`。

这些 protocol 的复杂度随 set size 线性，而通用 sorting/comparison circuit 至少有 `n log n` 或实际 `n log^2 n` 成本。论文也指出这些 set operations 仍需要 dummy padding 来保持 obliviousness。

## Operator protocols

| Operator | Proof style | 机制 | 主要边界 |
| --- | --- | --- | --- |
| Project | circuit-based / copy tags | 复制列时几乎无成本；表达式投影用 circuit 计算并验证。 | 算术表达式很贵，实验中 `Project(revenue)` 占 Q3 很大成本。 |
| Filter | circuit-based + optional sort/truncate | 对每行验证 predicate；不满足或输入 dummy 时输出 dummy。为了不泄露 selectivity，默认输出 cardinality 等于输入。 | truncation 需要公共 bound；无 padding 会泄露中间结果 cardinality。 |
| Aggregate | sort + circuit aggregators | 先按 group-by attributes 排序；逐行累加 SUM/COUNT/AVG 等 aggregator；每组保留一个 non-dummy row。 | 输出 cardinality 与输入相同以隐藏 group count；浮点开销高，实验改成 64-bit integer。 |
| Sort | set-based + order circuit | prover 本地排序并重新 commit 输出；用 set equality 证明元素未增删改，再用相邻 comparison circuit 证明 order。 | sort 本身是其他 operator 的关键支撑；order check 仍有 circuit cost。 |
| Join | set-based + predicate circuit | prover 本地 hash join，padding 到 public cardinality bound；验证每个 non-dummy output 满足 predicate、输出元素来自输入、未遗漏匹配。 | 论文实现支持 two-way equi-join；复杂 predicate 可用 cross product + filter 但成本高。 |

Join 的 completeness proof 比普通 predicate satisfaction 更强: 它用 projected contributing tuples `U,V` 与剩余 tuples `R-U, S-V` 做 set-difference checks，随后把未选中 tuples 的 join key 投影为 `KR, KS`，证明 `KR` 和 `KS` disjoint，从而说明没有被遗漏的匹配。

## 实验与性能记录

### Setup

- Prototype: EMP Toolkit + PostgreSQL + Java front end / Apache Calcite。
- Workload: TPC-H Q1, Q3, Q5, Q8, Q9, Q18。
- 数据规模: lineitem 60k, 120k, 240k rows，dimension tables 按 TPC-H 比例缩放。
- 机器: two AWS EC2 r6i.4xlarge, Ubuntu 22.04, 128 GiB RAM, 16 vCPUs, up to 12.5 Gbps。
- 实验限制: 浮点操作改为 64-bit integer；Q9 的 string pattern matching predicate 被省略。

### Baseline and set-based speedup

Table 2 显示 plain SQL 与 naive circuit-only proof 相差 5-6 个数量级。例如 60k Rows 下 Q3 明文约 `0.02s`，Circuit-Only 约 `24,130s`。ZKSQL 的 set-based operator route 相比 Circuit-Only 有显著改善:

- 除 Q1 外，所有 query 相比 Circuit-Only 至少有两数量级 speedup。
- Q18 最大 speedup 约 `410x`，因为它有多个 joins 和 aggregates，正好受益于 set-based sort/join。
- Q1 set operations 少，speedup 约 `2x`。

### Padding overhead

Obliviousness 需要用 dummy tuples/padding 隐藏中间结果 cardinalities。与不 padding 的版本相比，Q8 和 Q18 由于多 join 且 true intermediate cardinality 较小，分别有约 `12x` 和 `10.5x` padding overhead。Q1 与 no-padding 接近，因为固定表达式证明成本占比高；Q9 因 primary key-foreign key join 链条使 true cardinality 接近 oblivious bound，也较接近。

### Operator cost

Q3 operator breakdown 显示:

- `Project(revenue)` 计算 `l_extendedprice * (1 - l_discount)`，由于算术表达式 ZK 成本高，占接近三分之一 runtime。
- Filters 主要是 boolean expressions，占约 3%。
- 两个 joins 仍占约 57%，因为每个 output tuple 都要验证 join predicate。
- Sort 与 aggregate 在优化后占比较小，各约 4% 与 3%。

### Network/scalability/cost

- Bandwidth: 从 12.5Gbps 降到 20Mbps 影响不大，到 5Mbps 才约 2x slowdown，说明当前 cloud setup 下不是主要瓶颈。
- Scalability: 大多数 query 随 input size 近似线性增长；Q9 因 wide rows/cache paging 出现 3x slowdown。
- Memory: 60k Rows query 使用最多约 18 GB；240k Rows 下 Q9 可到约 69 GB。
- Monetary cost: 60k Rows 下 Circuit-Only 总成本约 `$74.28`，ZKSQL 约 `$0.89`；ZKSQL 120k Rows 约 `$2.23`，240k Rows 约 `$6.30`。

## 创新点与相对边界

| 相对对象 | ZKSQL 的改进 | 边界 |
| --- | --- | --- |
| Naive circuit-only SQL proof | 不逐门追踪完整 query execution，而是按 operator 证明中间结果性质。 | 仍比明文 SQL 慢多个数量级。 |
| IntegriDB / vSQL | ZKSQL 提供 zero-knowledge property，保护输入记录和中间结果。 | vSQL/IntegrityDB 相关路线仍需独立 source 校准；ZKSQL 不等于 vSQL 的 zero-knowledge extension。 |
| zk-vSQL | ZKSQL 面向 practical ad-hoc SQL query translation and execution; zk-vSQL formalizes vSQL zero-knowledge but不解决 arbitrary ad-hoc SQL translation/implementation。 | ZKSQL 使用 interactive VOLE-based backend，不是通用 SNARK。 |
| TEE systems CorrectDB / VeriDB | 不依赖 trusted hardware，基于 cryptographic protocols。 | 性能不如 TEE route，且仍公开 schema/cardinality/query/answer。 |
| ZK-FEDB | ZKSQL 支持 SQL operators、query plan 和 TPC-H route。 | ZKSQL 不提供 database-size hiding like ZK-FEDB; table cardinalities public。 |

## 限制与开放问题

- ZKSQL 公开 schema、table cardinalities、query、query DAG 和最终 answer；仅保护 input records 和 intermediate results。
- Padding 是主要 overhead，尤其在 join-heavy query 中。
- Join 当前支持 two-way equi-join；更丰富 join predicate 是 future work。
- 浮点与复杂字符串 predicate 不是本文重点；实验中为避开浮点成本做了整数化处理，并省略 Q9 的 pattern matching。
- 当前 operator-at-a-time sequential execution 可能需要 query optimization / execution-order optimization。
- 未来可探索不逐个 operator 证明 SQL query results 的路线，以及 MPC-in-the-head 等其他 ZK paradigms。

## 层级候选分类

| Candidate | Decision | Reason |
| --- | --- | --- |
| [[verifiable-database-queries|Verifiable database queries]] | primary | 论文核心问题是 SQL answer correctness/completeness + input-record zero knowledge。 |
| [[applications|ZKP applications]] | parent direction | SQL query proof 是 ZKP application problem，不是 proof-system foundation。 |
| [[verifiable-computation-systems|Verifiable computation systems]] | secondary | 使用 commit-and-prove、operator computation proofs、VOLE-ZK backend，是 VC system evidence。 |
| [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]] | secondary / boundary | 论文借用 relational query processing 和 SQL operator algebra，但不解决普通 DBMS transaction/storage foundation。 |
| [[privacy-preserving-database-queries|Privacy-preserving database queries]] | adjacent, not primary | ZKSQL hides prover's input records from verifier, not verifier query/access pattern from server. |
| `distributed-transactions` | reject | 没有 commit protocol、isolation level、MVCC/OCC、serializability、replication ordering。 |
| `ZKSQL` standalone knowledge node | reject for now | ZKSQL 是 source/system instance；先作为 verifiable SQL route 的 source extension。 |

## 冷启动分层发现

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | `zero-knowledge-proofs` | title/abstract/§2-§4 use ZK proof protocols for SQL answers | high | durable parent |
| Research background | `commit-and-prove verifiable computation` + relational query processing | §2-§3, Fig. 1-2 | high | source-backed background in target nodes |
| Research problem | `verifiable database queries` | abstract, §1, §3.2, §7 | high | update problem node |
| Foundation concepts | zero-knowledge proofs, VOLE-based ZK, commit-and-prove, SQL query plans, oblivious execution | §2-§4 | medium | cite as prerequisites; no new foundation node here |
| Method family | operator-at-a-time proofs; set-based polynomial verification of SQL operators | §4.1-§4.2 | high | source extension route |
| Application/evaluation context | regulatory/statistical database answers; TPC-H query evaluation | §1, §5 | high | representative source + evaluation evidence |
| Artifact/source instance | ZKSQL prototype | PVLDB artifact statement, §5 | high | source instance, not upper foundation |

## 检索优化判断

- 本论文最应该更新的 Knowledge path: `zero-knowledge-proofs/applications/verifiable-database-queries`。
- 它能帮助未来问题少读 source notes:
  - “ZKSQL 和 ZK-FEDB 有什么区别?”
  - “如何证明 SQL query answer 正确且不泄露输入记录?”
  - “ZK database query 的 SQL/operator route 有哪些成本瓶颈?”
  - “ZKSQL 为什么比 circuit-only 快?”
- 应留在 source note 的内容:
  - 每个 operator protocol 的细节、表格数字、TPC-H setup、AWS 机器配置、Q3 breakdown。
  - ZKSQL artifact URL；不能当作 repo analysis。
- 上层只需吸收:
  - verifiable database queries 新增 SQL/ad-hoc route；
  - set-based operator proof route；
  - 与 privacy-preserving query 的边界修正；
  - database systems/query-processing foundation 仍薄，应排队。

## Knowledge Handoff

### 应更新的 Knowledge

- [[verifiable-database-queries|Verifiable database queries]]: 新增 ZKSQL SQL-operator route，移除 `ZKSQL source pending` gap，补充 query privacy boundary。
- [[applications|ZKP applications]]: 新增 source note ref、代表 source 与 query keys。
- [[verifiable-computation-systems|Verifiable computation systems]]: 作为 commit-and-prove / VOLE-based VC system source extension，新增 operator-at-a-time route。
- [[04_Knowledge/distributed-systems/data-management-and-storage|Data Management and Storage]]: 作为 secondary signal，说明 relational query processing / SQL operator algebra 可作为 ZK database query proof object，但不能混入 distributed transactions。

### Bridge 判断

- 不新建 bridge。当前缺少独立的 relational query processing knowledge endpoint；直接创建 broad `data-management-and-storage -> verifiable-database-queries` bridge 会过宽。
- [[privacy-preserving-database-queries-to-verifiable-database-queries|Privacy-preserving database queries -> verifiable database queries]] 可轻量刷新: ZKSQL 提供 answer correctness + input-record zero knowledge，但不提供 query/access privacy，因此加强 complement boundary。
- [[zero-knowledge-sets-to-verifiable-database-queries|Zero-knowledge sets -> verifiable database queries]] 不作为 ZKSQL 的主 bridge，因为 ZKSQL 的 set-based proofs是 polynomial multiset verification for SQL operator outputs，不是 ZKS/ZK-EDB primitive transfer；它只关闭该 bridge 中“SQL semantics 需要 separate sources”的 refresh trigger。

### 不应新建的 Knowledge

- 不新建 `ZKSQL` 论文同名知识页。
- 不新建 `zero-knowledge SQL` standalone node；当前作为 [[verifiable-database-queries|Verifiable database queries]] 的方法路线即可。
- 不创建 `distributed-transactions` 相关更新。

## Evidence Notes

| Evidence anchor | Observation | Absorption target |
| --- | --- | --- |
| p1 Abstract | ZKSQL provides authenticated answers to ad-hoc SQL queries with ZK proofs; proofs show answers correct/sound and reveal no input records. | [[verifiable-database-queries|Verifiable database queries]] |
| p2 Contributions | First work on ZK proofs for ad-hoc SQL queries; operator-at-a-time proofs; set-based protocols; up to two orders speedup over naive baseline. | [[verifiable-database-queries|Verifiable database queries]] |
| p3-p5 §3 | Commit-and-prove workflow, public schema/cardinality/query/DAG/answer boundary, VOLE-based interactive protocols. | [[verifiable-computation-systems|Verifiable computation systems]] |
| p5-p7 §4.1 | Set equality/disjoint/intersection/union protocols using polynomial checks and Packing. | source note + target method route |
| p7-p10 §4.2 | Project/Filter/Aggregate circuit route; Sort/Join set-based route. | [[verifiable-database-queries|Verifiable database queries]] |
| p10-p12 §5 | TPC-H evaluation, set-based speedups, padding overhead, operator bottlenecks, network/scalability/cost. | target current synthesis |
| p12 §6-§7 | Boundary against CorrectDB/VeriDB, IntegriDB/vSQL, zk-vSQL; future work on joins, optimization, alternative proof paradigms. | gaps and review queue |

## 处理日志

- 2026-06-23: Deep-read 13 pages from local PDF with bundled `pypdf`; wrote this source note; ready for `nahida-knowledge-get`.
