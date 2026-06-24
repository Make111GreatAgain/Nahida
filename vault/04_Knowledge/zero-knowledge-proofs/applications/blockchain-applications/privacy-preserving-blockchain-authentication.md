---
id: "nahida-knowledge-privacy-preserving-blockchain-authentication"
title: "Privacy-preserving blockchain authentication"
type: "knowledge"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "active_seed"
node_kind: "problem"
hierarchy_level: "problem"
file_slug: "privacy-preserving-blockchain-authentication"
domain_id: "zero-knowledge-proofs"
direction_id: "applications"
parent_knowledge_refs:
  - "nahida-knowledge-zkp-blockchain-applications"
child_knowledge_refs: []
ontology_path:
  - "zero-knowledge-proofs"
  - "applications"
  - "blockchain-applications"
  - "privacy-preserving-blockchain-authentication"
primary_ontology_path: "zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication"
secondary_ontology_paths:
  - "zero-knowledge-proofs/proof-systems/zk-snarks"
relation_edges:
  - from: "nahida-knowledge-privacy-preserving-blockchain-authentication"
    relation: "is_a"
    to: "nahida-knowledge-zkp-blockchain-applications"
    evidence_refs:
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication.md"
      - "vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-blockchain-authentication"
    relation: "evidenced_by"
    to: "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
    evidence_refs:
      - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
    confidence: "high"
    status: "active_seed"
  - from: "nahida-knowledge-privacy-preserving-blockchain-authentication"
    relation: "bridges_to"
    to: "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
    evidence_refs:
      - "vault/05_Bridges/zk-snarks-to-privacy-preserving-blockchain-authentication.md"
    confidence: "high"
    status: "active_seed"
bridge_refs:
  - "nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication"
source_note_refs:
  - "vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md"
representative_source_refs:
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "doi:10.1145/3658644.3690356"
query_keys:
  - "Privacy-preserving blockchain authentication"
  - "blockchain authentication with existing credentials"
  - "keyless blockchain accounts"
  - "social login wallet privacy"
  - "zkLogin"
aliases:
  - "keyless blockchain accounts"
  - "privacy-preserving social login wallet"
  - "blockchain authentication with existing credentials"
domains:
  - "zero-knowledge-proofs"
  - "blockchain-systems"
topics:
  - "blockchain-applications"
  - "privacy-preserving-blockchain-authentication"
  - "wallet-onboarding"
  - "OpenID Connect"
tags:
  - "nahida/knowledge"
  - "nahida/problem"
freshness_status: "fresh"
last_synthesized: "2026-06-20"
valid_until: "2026-07-20"
evidence_window_start: "2026-06-20"
evidence_window_end: "2026-06-20"
created: "2026-06-20"
updated: "2026-06-20"
managed_by: "nahida"
run_ids:
  - "nahida-knowledge-20260620-zklogin"
source_refs:
  - "sha256:6021df5c4aa232e3fe17ec783dbdb92619a57f9c5fc14c192a428e2f05c67089"
  - "doi:10.1145/3658644.3690356"
confidence: "high"
trust_tier: "primary"
---

# Privacy-preserving blockchain authentication

## 定义与范围

- 定义: Privacy-preserving blockchain authentication 研究如何用现有身份凭证、短期 witness、零知识证明和链上验证逻辑来认证区块链交易，同时避免把 off-chain identity 与 on-chain account 公开绑定。
- 不包含: 单个产品名、某条链的部署参数、一次 ceremony、某个 ZK service 配置、某个 JWT parsing trick；这些留在 `03_Sources` source note。
- Canonical terms: `privacy-preserving blockchain authentication`
- Aliases/query keys: keyless blockchain accounts, social login wallet privacy, blockchain authentication with existing credentials
- Standalone completeness check: 本节点给出本地定义、边界、问题、方法族、代表 sources、缺口和更新记录；链接用于深入，不作为唯一解释。
- Retrieval role: 让查询优先从本节点理解 ZKP 如何支撑钱包 onboarding/认证，再按需打开 zkLogin source。
- Update scope: 新 source 若改变身份凭证、salt、proof delegation、wallet security 或 privacy boundary，应刷新本节点。
- Domain dynamics note: not_applicable

## 背景

区块链账户通常由长期私钥控制，UX 门槛高且丢失不可恢复；custodial wallet 又把资产控制权交给平台。OAuth/OIDC 账户有成熟 UX，但直接把 JWT 或 OAuth result 交给链上验证会暴露敏感 claims，或需要额外 trusted oracle/server。zkLogin 作为当前 seed，把 OpenID Provider 的 JWT 作为隐藏 witness，通过 ZK proof 证明身份凭证、地址和 ephemeral key 的关系，避免 JWT payload 上链。

## 基础概念判断

- 是否是基础概念/方向/问题: `problem` / `problem`。
- 为什么足够通用: 它能组织 zkLogin、ZK address abstraction、Aptos Keyless、OpenPubkey-style credentials、content credentials、未来 passkey/ZK wallet sources。
- 为什么不是单篇论文/单个协议/单个仓库的局部概念: `zkLogin`、Tagged Witness Signature、具体 Sui deployment、AWS Nitro salt service 都留在 source note；本节点只沉淀可复用问题结构和方法族。
- 需要引用的更基础 Knowledge: [[blockchain-applications|ZKP blockchain applications]], [[zk-snarks|zk-SNARKs]]。
- 不应拆出的实例/协议/来源: zkLogin、Aptos Keyless、Bonsai Pay、specific salt services 默认作为 source/system instances。

## 解决的问题

在不要求用户管理长期私钥、不把 Web2 身份细节公开上链、且不让新中介获得 custody/signing power 的前提下，认证链上交易并可选地支持账户 discoverability、匿名性和 claimability。

## 上层位置

| Parent knowledge | Relation | Evidence | Status |
| --- | --- | --- | --- |
| [[blockchain-applications|ZKP blockchain applications]] | child_of | zkLogin source classification | active_seed |

## 下级结构

| Child candidate/node | Kind | 为什么需要拆分 | Evidence | Status |
| --- | --- | --- | --- | --- |
| tagged witness signatures | section | 当前只有 zkLogin 一个 source，先作为方法族，不拆独立 cryptographic primitive node。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | source_extension |
| salt/privacy management for wallet identity | section | 当前只有 zkLogin 一个 source，先作为本节点边界章节。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] | source_extension |

## 方法族与解决路线

| 方法/路线 | 核心思想 | 适用条件 | 代价/限制 | 代表来源 |
| --- | --- | --- | --- | --- |
| JWT-as-witness authentication | 把 OP 签发的 JWT 放入 ZK witness，链上只验证 proof，不公开 JWT payload。 | 身份凭证本身有 provider signature，且链/validator 可获得 provider public key。 | 仍信任 OP authentication；需要 JWK oracle/key rotation 处理。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |
| Nonce-bound ephemeral key | 在 OIDC nonce 中绑定 ephemeral public key、expiry 和 randomness，使 JWT 成为 session key certificate。 | Provider 支持 nonce，交易可由 ephemeral key 授权。 | Nonce-less provider 版本安全性更弱，尤其不适合普通 proof delegation。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |
| Salted address derivation | 用 `H(stid, aud, iss, salt)` 派生地址，salt 隐藏 stable identifier 与链上地址的关系。 | 用户或 app 能可靠管理 salt。 | 丢失 salt 可能锁定资产；salt service 会影响 unlinkability，甚至在弱策略下影响 OP 安全边界。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |
| Delegated proving with local signing | ZK service 只生成 proof，用户本地持有 ephemeral private key 完成交易签名。 | Proof generation 对用户设备太重，但用户能验证返回 proof。 | 安全不等于隐私；普通 delegation 会泄露 JWT/salt 给 service。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |
| Selective identity reveal | 用户可选择公开 stable ID、部分 ID 或 anonymity set，支持 discoverability、partial reveal、anonymous accounts。 | 应用需要身份可验证或组织归属证明。 | 公开越多，unlinkability 越弱；匿名集合设计需要额外审查。 | [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin]] |

## 代表 Sources

| Source | Source kind | 贡献 delta | 假设/限制 | Evidence anchors |
| --- | --- | --- | --- | --- |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | paper | 建立 privacy-preserving blockchain authentication seed：JWT witness、TWS、salted address、nonce-bound ephemeral key、delegated proving | 单一 source；依赖 OP authentication、JWK oracle、Groth16 ceremony、salt management；Sui deployment/latency 不可泛化 | `p1-p20` |

## 当前综合

- Evidence window: `2026-06-20`，仅覆盖当前 vault 已有 source。
- Freshness: `fresh` for current source absorption; not a latest-news claim.
- Valid until: `2026-07-20`。
- 综合: 当前节点由 zkLogin seed 支撑。可复用结构是: 用 ZK hiding 保护 JWT/stable identifier/salt，用 proof verification 让链验证 credential-to-address-to-ephemeral-key 的关系，用 ephemeral signing 避免每笔交易都生成 proof。安全与隐私必须分开判断: ZK service/salt service 可能不能偷资产，但能破坏 unlinkability；OP 是身份认证信任根，不是 custodian。

## Source Extensions

| Source | 新增/修正内容 | 影响的章节 | 是否改变上层结构 | Next action |
| --- | --- | --- | --- | --- |
| [[sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication|zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials]] | 新建 privacy-preserving blockchain authentication problem node and routes | 定义与范围; 方法族与解决路线; 代表 Sources; 当前综合; Bridge Links | yes | 吸收 ZK Address Abstraction、Aptos Keyless、OpenPubkey/CanDID 后复核分类 |

## Bridge Links

| Bridge | Endpoint path | Relation type | Transfer boundary | Status |
| --- | --- | --- | --- | --- |
| [[zk-snarks-to-privacy-preserving-blockchain-authentication|zk-SNARKs -> privacy-preserving blockchain authentication]] | `zero-knowledge-proofs/proof-systems/zk-snarks; zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication` | application, privacy, authentication, implementation_reuse | ZK hiding/succinctness transfers; OP trust, salt recovery, JWK oracle, app liveness and UX recovery are system-specific. | active_seed |

## 关系图谱

| From | Relation | To | Evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- |
| nahida-knowledge-privacy-preserving-blockchain-authentication | is_a | nahida-knowledge-zkp-blockchain-applications | vault/04_Knowledge/zero-knowledge-proofs/applications/blockchain-applications/privacy-preserving-blockchain-authentication.md | high | active_seed |
| nahida-knowledge-privacy-preserving-blockchain-authentication | evidenced_by | vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md | vault/03_Sources/papers/sha256-6021df5c4aa2-zklogin-privacy-preserving-blockchain-authentication.md | high | active_seed |
| nahida-knowledge-privacy-preserving-blockchain-authentication | bridges_to | nahida-bridge-zk-snarks-to-privacy-preserving-blockchain-authentication | vault/05_Bridges/zk-snarks-to-privacy-preserving-blockchain-authentication.md | high | active_seed |

## 缺口与队列

| Gap | Why it matters | Proposed skill | Priority | Status |
| --- | --- | --- | --- | --- |
| ZK Address Abstraction、Aptos Keyless、OpenPubkey、CanDID、passkey-based wallets 缺 source。 | 需要比较 OAuth/ZK/MPC/passkey 钱包认证设计的 security/liveness/privacy 边界。 | nahida-update / nahida-research-search | high | queued |
| OpenID Connect/JWT foundation source 缺。 | 若后续要回答 Web identity/OIDC 标准细节，需要基础概念 source。 | nahida-research-search | medium | queued |

## 更新记录

| Date | Run ID | Change | Sources | Reviewer |
| --- | --- | --- | --- | --- |
| 2026-06-20 | nahida-knowledge-20260620-zklogin | Created privacy-preserving blockchain authentication problem node from zkLogin source. | 1 source note | codex |
