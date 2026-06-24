---
id: "arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp"
title: "Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs"
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
  - "p1-p15 full extracted text"
  - "Abstract, Sections 1-8, Algorithms 1-3, Figures 1-8, Tables 1-2, and references"
safe_for_absorption: true
canonical_url: "https://arxiv.org/abs/2311.15310v1"
doi: ""
arxiv_id: "2311.15310v1"
venue: "arXiv preprint"
year: "2023"
hierarchy_level: "source"
domain_id: "ml-systems"
direction_id: "privacy-and-trustworthy-ml"
topic_ids:
  - "federated-learning-integrity"
  - "secure-aggregation-input-validation"
  - "verifiable-aggregation"
ontology_path:
  - "ml-systems"
  - "privacy-and-trustworthy-ml"
  - "federated-learning-integrity"
primary_ontology_path: "ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity"
secondary_ontology_paths:
  - "zero-knowledge-proofs/zkml/verifiable-aggregation"
path_update_status: "propagated"
hierarchy_candidates:
  domains:
    - "ml-systems"
    - "zero-knowledge-proofs"
  directions:
    - "privacy-and-trustworthy-ml"
    - "zkml"
  topics:
    - "federated-learning-integrity"
    - "secure-aggregation-input-validation"
    - "verifiable-aggregation"
domains:
  - "ml-systems"
  - "zero-knowledge-proofs"
topics:
  - "federated-learning"
  - "federated-learning-integrity"
  - "secure-aggregation"
  - "input-validation"
  - "verifiable-aggregation"
  - "probabilistic-l2-norm-check"
  - "zero-knowledge-proofs"
aliases:
  - "RiseFL"
  - "Robust and Secure Federated Learning with Low-Cost Zero-Knowledge Proof"
  - "Secure and Verifiable Data Collaboration with Low-Cost ZKP"
tags:
  - "nahida/source"
  - "nahida/paper"
  - "nahida/ml-systems"
  - "nahida/zkp"
direction_facets:
  parent_domain:
    - "ml-systems"
    - "zero-knowledge-proofs"
  subdomain:
    - "privacy-and-trustworthy-ml"
    - "zkml"
  problem:
    - "secure federated learning with privacy and input integrity"
    - "malicious-client update filtering under secure aggregation"
    - "low-cost ZKP input validation"
  method_family:
    - "probabilistic L2-norm integrity check"
    - "Pedersen commitment"
    - "verifiable Shamir secret sharing"
    - "Sigma-protocol proof of relation"
    - "Bulletproofs range/bound proof"
    - "secure aggregation"
  system_layer:
    - "federated learning protocol"
    - "client update validation"
    - "secure aggregation"
  evaluation_context:
    - "OrganAMNIST"
    - "OrganSMNIST"
    - "Forest Cover Type"
    - "synthetic model parameter benchmarks"
    - "sign flip, scaling, label flip, and additive noise attacks"
  bridge:
    - "zkml-verifiable-aggregation-to-federated-learning-integrity"
created: "2026-06-23"
updated: "2026-06-23"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260623-risefl-low-cost-zkp"
source_refs:
  - "arxiv:2311.15310v1"
  - "sha256:4bec7aa8640e40e13f2180d540f8462382b7823d3cadd231cf933a111277ec00"
confidence: "high"
trust_tier: "primary"
primary_direction: "privacy-and-trustworthy-ml"
secondary_directions:
  - "zkml"
classification_status: "corrected_from_queue"
classification_confidence: "high"
classification_evidence:
  - "Title and abstract identify federated learning/data collaboration privacy plus integrity, not inference."
  - "Sections 3-4 formulate relaxed SAVI and RiseFL for secure aggregation with verified inputs."
  - "The paper explicitly uses Pedersen commitments, VSSS, Sigma-protocols and Bulletproofs; it states ordinary zkSNARK protocols are not additively homomorphic enough for this secure aggregation setting."
  - "Experiments evaluate FL input-integrity defenses under malicious-client attacks, not model inference proving."
taxonomy_version: "1.0"
queue_id: "nahida-paper-folder-20260611-domain-serial-v2"
queue_item_id: "nahida-paper-folder-20260611-domain-serial-v2:item:0072"
local_pdf: "~/Desktop/paper/2311.15310v1.pdf"
pdf_sha256: "4bec7aa8640e40e13f2180d540f8462382b7823d3cadd231cf933a111277ec00"
extracted_text_path: "vault/02_Raw/pdf/extracted/secure-and-verifiable-data-collaboration-with-low-cost-zero-knowledge-proofs-4bec7aa8640e-pages.txt"
---

# Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs

## 论文身份

- 标题: Secure and Verifiable Data Collaboration with Low-Cost Zero-Knowledge Proofs
- 系统/方案名: RiseFL
- 作者: Yizheng Zhu, Yuncheng Wu, Zhaojing Luo, Beng Chin Ooi, Xiaokui Xiao
- 机构: National University of Singapore
- 年份: 2023
- arXiv: 2311.15310v1
- 链接: https://arxiv.org/abs/2311.15310v1
- 本地 PDF: `~/Desktop/paper/2311.15310v1.pdf`
- SHA-256: `4bec7aa8640e40e13f2180d540f8462382b7823d3cadd231cf933a111277ec00`
- 页数: 15
- 备注: p1 footnote 写明这是参考文献 [73] 的 updated version，增加了 tabular 和 medical image datasets 上的实验评估。

## 精读状态

- Reading depth: `deep_read`
- Reading status: `deep_read_complete`
- Safe for absorption: true
- PDF extractor: `pypdf`
- 已覆盖章节/页码: Abstract, §1 Introduction, §2 Preliminaries, §3 System Overview, §4 RiseFL Design, §5 Analysis, §6 Experiments, §7 Related Works, §8 Conclusions, references.
- 未覆盖章节/页码: none in local PDF.
- Extraction gaps: 公式和表格中的特殊符号有少量 OCR/Unicode 噪声；主叙述、算法、表格数字和图注可读。
- 精读说明: 队列把本论文 staged 到 `zero-knowledge-proofs/zkml/verifiable-inference`。深读后纠正为 `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity`，因为核心是 federated learning 中在 secure aggregation 前提下同时保证 client update privacy 和 input integrity，不是证明一次 model inference。

## 章节地图

| 章节/页码 | 内容角色 | 关键内容 | 证据价值 | 备注 |
| --- | --- | --- | --- | --- |
| Abstract / p1 | 问题与贡献 | 数据协作、FL 隐私/完整性冲突；RiseFL；28x/53x/164x client computation speedup | high | 主分类依据 |
| §1 / p1-p2 | 动机与相关威胁 | FL 可避免 raw data exchange，但 server 可从 updates 推断隐私，malicious clients 可 poison model | high | ML systems problem |
| §2 / p2-p3 | Preliminaries | Pedersen commitments, VSSS, Sigma-protocol proof of square/relation, Bulletproofs bound proof | high | ZKP route，不是 zkSNARK route |
| §3 / p3-p4 | System Overview | malicious server for privacy, malicious clients for integrity, relaxed SAVI definition | high | threat model and formal problem |
| §4.1 / p5 | Rationale | probabilistic L2-norm check reduces group exponentiations from `O(d)` to `O(d/log d)` | high | method delta |
| §4.2-§4.5 / p5-p8 | RiseFL protocol | initialization, hybrid commitment, share verification, proof generation/verification, secure aggregation | high | core mechanism |
| §4.6 / p8 | Extensions | sphere defense, cosine similarity, Zeno++ can be converted/supported | medium | generality claim |
| §5 / p8-p10 | Security and cost analysis | Theorem 1 for relaxed SAVI; pass-rate bound; Table 1/2 cost comparison | high | evidence and caveats |
| §6 / p10-p12 | Experiments | synthetic and real datasets; baselines RoFL/EIFFeL/ACORN; microbenchmark and robustness | high | performance evidence |
| §7 / p12-p13 | Related works | secure aggregation, robust learning, input integrity with secure aggregation | medium | boundary against RoFL/ACORN/EIFFeL |
| §8 / p13 | Conclusion | hybrid commitment + probabilistic L2 check achieves low-cost privacy+integrity | medium | author summary |

## 核心精读笔记

> 这篇论文的主线是: 在 federated learning 中，secure aggregation 能隐藏 client update，但无法判断 masked/encrypted update 是否恶意；robust aggregation 能过滤 malformed updates，但通常需要 server 看到 plaintext updates。RiseFL 用 Pedersen commitment + VSSS + ZKP proof over probabilistic L2 checks，在单 server FL 设置中同时追求 input privacy 和 input integrity，并把昂贵的严格 L2 proof 换成低成本的概率检查。

### 问题、动机与边界

论文关注的是多组织数据协作中的 federated learning。FL 避免 raw data 直接交换，但仍有两个风险:

- input privacy: server 可能从 client 上传的 gradients/model updates 中恢复敏感数据。
- input integrity: malicious clients 可能上传 malformed updates，造成 backdoor、accuracy degradation 或其他 poisoning。

已有 secure aggregation 可以隐藏 local updates，但 server 很难判断 encrypted/masked update 是否恶意。已有 Byzantine-robust aggregation 可以识别异常 updates，但需要 server 看到 plaintext updates。EIFFeL/RoFL/ACORN 等把 secure aggregation 与 ZKP 结合，但作者认为 proof generation/verification 太慢，难以部署。

RiseFL 的问题定义是 `{D, F}`-relaxed SAVI: 它保持 input privacy，但把 strict input integrity 放宽为一个 pass-rate function `F(D(u))`。直觉是 malformed 程度越大，通过概率越低；轻微越界可能通过，这是性能换来的显式边界。

### Threat model

论文把 threat model 拆成两部分:

- Privacy side: server 可以恶意偏离协议，甚至与部分 malicious clients collude，目标是推断 honest clients 的 updates。
- Integrity side: 最多 `m < n/2` 个 malicious clients 可以任意偏离协议，例如提交 malformed updates 或诬告 honest clients。

一个重要边界: 论文不考虑 server 对 input integrity 作恶，因为其 primary goal 是确保 uploaded update 的 well-formedness。这与 zkFL 的 malicious aggregator threat model 不同，后续知识层不能把二者混成一个攻击模型。

### 密码学组件

RiseFL 使用的 ZKP 组件不是普通 zkSNARK。p3 明确指出 zkSNARK protocols 不具备所需 additive homomorphism，因此不能直接支持本文的 secure aggregation 设置。论文使用:

- Pedersen commitment: 对每个 update coordinate 形成 commitment，并依赖 additive homomorphism。
- Verifiable Shamir secret sharing (VSSS): 分享 Pedersen commitment 的 blind `r_i`，并让 clients 验证 share authenticity。
- Sigma-protocol proof of square / proof of relation: 证明 committed values 的平方关系、同一 hidden value 在不同 commitments 之间一致。
- Bulletproofs-style bound proof: 证明 committed value 落在给定区间内。
- Diffie-Hellman secure channel: 用于 clients 间 secret share 通过 server 转发时的加密。

因此，本 source 对 ZKP 侧的贡献是 `commitment-compatible ZKP for FL input validation`，不是 `SNARK-based aggregation proof`。

### RiseFL protocol

每轮训练分四部分:

1. System initialization: 所有 parties 确认 clients 数量 `n`、最大恶意 clients 数量 `m`、inner product bit bound、random sample count `k`、group elements、discretization factor `M`、hash function 等。
2. Commitment generation: client `C_i` 本地训练得到 update `u_i`，生成 random secret `r_i`，用 Pedersen commitment `y_i = C(u_i, r_i)` 承诺每个 coordinate；同时用 VSSS 把 `r_i` 分给其他 clients，server 只负责转发 encrypted shares 和 check strings。
3. Proof generation and verification:
   - clients 先验证收到的 shares 是否匹配 VSSS check strings；server 根据超过 `m` 的诬告/被告规则标记恶意 clients。
   - server 与 clients 用 hash seed 共同生成 random vectors；client 对 inner products 生成 relation proofs、square proofs 和 bound proofs；server 验证 proof 后把未通过者加入 malicious list。
4. Secure aggregation: honest clients 聚合来自未被标记 clients 的 secret shares，server reconstructs sum of blinds `r`，再用 homomorphic commitments 计算 honest clients update sum。

这个流程把 update plaintext 保留在 commitment/VSSS/ZKP 结构里，server 最终只恢复 valid clients 的 aggregate。

### 概率 L2-norm integrity check

RiseFL 的核心优化是把严格检查 `||u||_2 <= B` 改成随机投影检查:

- 采样 `k` 个随机向量 `a_1, ..., a_k`。
- 计算每个 inner product `<a_t, u>`。
- 检查 `sum_t <a_t, u>^2 <= B^2 * gamma_{k,epsilon}`。

因为 `1 / ||u||_2^2 * sum_t <a_t,u>^2` 服从 chi-square distribution，若 `||u||_2 <= B`，honest update 以至少 `1-epsilon` 通过。若 malicious update 的 norm 明显超过 bound，通过概率快速下降。

代价边界:

- 轻微越界向量可能通过，这是 relaxed SAVI 的本质。
- `k` 越大，恶意 update 造成的 expected damage 越接近 strict L2 check，但 client/server cost 也上升。
- 文中以 `epsilon = 2^-128`，`M = 2^24`，`k = 1K/3K/9K` 分析；对应 maximum expected damage ratio 约 1.24/1.13/1.08。

### Cryptographic operation optimization

直接为每个 random vector 和 update coordinate 做 proof 会带来高 group exponentiation cost。作者观察到 inner-product commitment verification 中反复出现:

```text
e_t = product_l y_{il}^{a_{tl}} = g^{<a_t,u_i>} * (product_l w_l^{a_{tl}})^{r_i}
```

于是定义 `h_t = product_l w_l^{a_{tl}}`，让 server 预计算并广播 `h_t`。为了防止 malicious server 伪造特殊 `h_t` 来泄漏 update，client 用 batch verification `VerCrt(w,h,A)` 检查 `h_t` 的正确性。另一个 `a_0` / `e_0` 用来证明 client 确实持有与 `y_i` 一致的 update witness。

这使 client-side expensive group exponentiations 从 `O(d)` 降到 `O(d/log d)`，但仍有 `O(kd)` finite field operations。

### Security analysis

Theorem 1 声明: 选取 `epsilon = negl(kappa)` 和合适的 `B0` 后，RiseFL 满足 `{D, F_{k,epsilon,d,M}}`-SAVI，其中 `D(u)=||u||_2/B`。证明分三部分:

- server 以高概率计算某个包含所有 honest clients 的集合 `H'` 上的 aggregate。
- 对 honest clients，除了 honest aggregate `sum_{C_i in C_H} u_i` 外不泄露更多信息。
- 对 malicious client，如果 `D(u_i)=c>1`，通过 integrity check 的概率被 `F(c)` 约束。

Security caveats:

- 保证是 relaxed/probabilistic，不是 strict validation。
- 若 malicious update 在 public predicate 内，ZKP 不判断其语义是否 poisoning。
- 假设最多 `m < n/2` malicious clients，且 secure channels / VSSS / commitment / ZKP assumptions 成立。

### Cost analysis

Table 1 对比 EIFFeL、RoFL、ACORN、RiseFL:

- EIFFeL client proof verification cost 随 `n*m*d` 上升，通信约 `2dnb` group elements。
- RoFL/ACORN 不支持 Byzantine-robust aggregation；ACORN 通信更低但缺 Byzantine robustness。
- RiseFL client proof generation 的主要 group exponentiation cost 约 `O(d/log d)`，server cost 包含 `k` 个 `h_t` 预计算和 per-client proof verification，communication per client 约 `d` group elements。

Table 2 关键数字:

- `d=100K, k=1000` 时，RiseFL client total 约 9.3s，ACORN 261s，RoFL 502s，EIFFeL 1536s。
- 作者总结 RiseFL client computation 相比 ACORN/RoFL/EIFFeL 分别最高快 28x/53x/164x。
- `d=1M` 时其他三者 OOM，RiseFL client total 约 79.3s，server total 约 1338s，per-client communication 约 30.9MB。

### Experiments

Implementation:

- C/C++ implementation，约 9K LOC。
- libsodium / Ristretto group on Curve25519，126-bit security。
- micro-benchmark server: Intel i7-8550U, 16GB RAM。
- FL tasks simulated on Intel Xeon W-2133, 64GB RAM, GeForce RTX 2080 Ti。
- fixed-point integer default 16 bits，`epsilon=2^-128`，`M=2^24`。

Datasets and models:

- OrganAMNIST: medical image, CNN, 31K parameters。
- OrganSMNIST: medical image, ResNet-18, 11M parameters。
- Forest Cover Type: tabular, TabNet, 471K parameters。
- Synthetic models: 1K/10K/100K/1M parameters。

Baselines:

- RoFL: ElGamal commitments + strict ZKP input validation; no Byzantine robustness。
- EIFFeL: VSSS + SNIP; Byzantine robustness but low efficiency。
- ACORN: PRG-SecAgg + strict ZKP input validation; no Byzantine robustness。
- NP-SC: non-private strict checking。
- NP-NC: non-private no checking。

Robustness:

- Attacks: sign flip, scaling, label flip, additive noise。
- Defenses: L2 norm, sphere defense, cosine similarity。
- Figure 8 shows RiseFL training curves close to NP-SC and better than NP-NC, supporting that probabilistic check can preserve model accuracy under tested malformed-update attacks。

### Related-work boundary

论文把相关工作分成三类:

- Secure aggregation: protects privacy but not integrity。
- Robust learning: handles Byzantine/malicious updates but often needs plaintext updates。
- Input integrity check with secure aggregation: Prio/Elsa need multiple non-colluding servers; RoFL/ACORN/EIFFeL are single-server but either lack Byzantine robustness or are inefficient。

RiseFL 的位置是 single-server, secure aggregation + verified inputs, Byzantine-robust, low-cost probabilistic input validation。

## 分层吸收判断

| 层级 | 结论 | 原因 | 写入位置 |
| --- | --- | --- | --- |
| Source | 创建独立 paper source note | RiseFL 的 threat model、protocol、probabilistic check、security/cost/evaluation 必须完整保留 | 本文件 |
| Knowledge primary | 更新 `federated-learning-integrity` | 主问题是 FL 中 malicious clients / malformed updates 在 secure aggregation 下如何被识别 | [[federated-learning-integrity|Federated learning integrity]] |
| Knowledge secondary | 更新 `verifiable-aggregation` | ZKP/commitment route 验证 update well-formedness 并支撑 secure aggregation | [[verifiable-aggregation|Verifiable aggregation]] |
| Bridge | 更新 existing bridge | 这篇补充 `zkML verifiable aggregation -> federated learning integrity` 的 client-side input validation route | [[zkml-verifiable-aggregation-to-federated-learning-integrity|zkML verifiable aggregation -> federated learning integrity]] |
| Not promoted | 不新建 RiseFL 知识节点 | RiseFL 是 source/system instance；上层应保留为 secure aggregation input validation / FL integrity method row | source extension |
| Not promoted | 不写入 `zk-SNARKs -> verifiable aggregation` bridge | 论文明确说 zkSNARK protocols are not additively homomorphic and cannot support required secure aggregation | boundary only |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp | evidences | nahida-knowledge-federated-learning-integrity | Abstract, §3-§6 | high | active_seed |
| arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp | evidences | nahida-knowledge-zkml-verifiable-aggregation | §4.4-§4.5, §5 | high | active_seed |
| arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp | contrasts_with | nahida-knowledge-zk-snarks | p3 says zkSNARK protocols are not additively homomorphic for this setting | medium | source_extension |
| arxiv-2311-15310v1-secure-verifiable-data-collaboration-low-cost-zkp | bridges_to | nahida-bridge-zkml-verifiable-aggregation-to-federated-learning-integrity | source handoff | high | active_seed |

## Knowledge Handoff

### Target knowledge paths

- Primary: `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity`
- Secondary: `zero-knowledge-proofs/zkml/verifiable-aggregation`
- Bridge: `zero-knowledge-proofs/zkml/verifiable-aggregation` -> `ml-systems/privacy-and-trustworthy-ml/federated-learning-integrity`

### Source-extension deltas

- 新增 `secure aggregation input validation` route: 在隐藏 local update 的同时，用 ZKP/probabilistic predicate 验证 update 是否 malformed。
- 修正 FL integrity taxonomy: zkFL = malicious aggregator correctness；PZKP-FL = lazy trainer/local training + global aggregation consistency；RiseFL = malicious client malformed-update filtering under secure aggregation。
- 修正 ZKP-side taxonomy: verifiable aggregation 不只包含 zk-SNARK sum relation，也包含 commitment-compatible ZKP input validation + secure aggregation route。
- 明确 non-transfer: RiseFL 不是 inference proof，不是 training proof，不是 SNARK aggregation proof；它也不保证 data quality、fairness、convergence 或 predicate-passing poisoning 被发现。

### Cold-Start Hierarchy Discovery

| Facet | Candidate | Evidence | Confidence | Handling |
| --- | --- | --- | --- | --- |
| Research field/domain | ML systems; zero-knowledge proofs as secondary method domain | Abstract, §1-§4 | high | update existing ML/ZKP bridge |
| Research background | FL data collaboration under privacy law; secure aggregation vs robust aggregation tension | p1-p2 | high | direction section |
| Research problem | Federated learning input privacy + input integrity under malicious clients | §3.2-§3.3 | high | source extension under [[federated-learning-integrity]] |
| Foundation concepts | secure aggregation, Pedersen commitments, VSSS, Sigma protocols, Bulletproofs, Byzantine robustness | §2-§4 | medium | no new foundation node in this run; queue foundation if repeatedly needed |
| Method family | Probabilistic L2-norm input validation with ZKP; hybrid commitment for secure aggregation | §4-§5 | high | method row, not a RiseFL node |
| Application/evaluation context | Healthcare data collaboration, FL on medical image/tabular datasets, malformed update attacks | p1, §6 | high | source-only details + source extension |
| Source instance | RiseFL | title/abstract/system design | high | paper source note only |

### Retrieval Optimization

- 以后问“FL 里 secure aggregation 下怎么检测恶意 client update”应从 [[federated-learning-integrity|Federated learning integrity]] 进入，再读 RiseFL source。
- 以后问“ZKP/commitment 如何支持 verifiable aggregation”应从 [[verifiable-aggregation|Verifiable aggregation]] 进入，但要区分 zkSNARK aggregation proof 与 RiseFL 的 Sigma/Bulletproofs route。
- 以后问“RiseFL 和 zkFL/PZKP-FL 区别”可通过 bridge 直接定位 threat model 差异。

## 证据表

| Claim / finding | Anchor | Confidence | Note |
| --- | --- | --- | --- |
| RiseFL simultaneously targets input privacy and input integrity in FL | Abstract, §3.3 | high | Primary classification |
| Existing secure aggregation protects privacy but not integrity; robust aggregation needs plaintext updates | §1, §7 | high | Problem motivation |
| zkSNARK protocols are not additively homomorphic for this secure aggregation setting | §2 / p3 | high | Prevent wrong bridge to zk-SNARKs |
| Probabilistic L2 check reduces expensive proof operations | §4.1-§4.4 | high | Method delta |
| RiseFL tolerates `m < n/2` malicious clients for input integrity | §3.2-§3.4 | high | Assumption |
| Theorem 1 proves relaxed SAVI with pass-rate function `F` | §5.1 | high | Security evidence |
| Slightly out-of-bound malicious vectors may pass; larger `k` reduces expected damage | §5.1/Figure 5 | high | Limitation |
| RiseFL outperforms ACORN/RoFL/EIFFeL on client computation under tested settings | Abstract, Table 2, §6.2 | high | Prototype evidence |
| RiseFL accuracy curves are close to strict-check NP-SC under tested attacks | §6.3/Figure 8 | high | Robustness evidence |

## Review Items

| Item | Why | Suggested action |
| --- | --- | --- |
| Venue/canonical publication status | Local PDF is arXiv and acmart-formatted; no DOI in PDF/queue. | Verify only if user requests publication metadata. |
| Foundation concepts for Bulletproofs/Sigma protocols | Current vault lacks full foundation nodes for these ZKP families. | Queue foundation pack if more non-SNARK ZKP/FL sources arrive. |
| Secure aggregation foundation | RiseFL provides strong source evidence but not a full secure aggregation survey. | Use future `nahida-research-search` / paper intake for foundation. |
| RoFL/ACORN/EIFFeL primary sources | RiseFL compares them, but this note should not absorb them as primary evidence. | Continue serial queue or run targeted paper intake. |
