#!/usr/bin/env python3
"""Nahida PDF folder intake helper.

This helper is intentionally conservative: it inventories PDFs, extracts text
with bundled pypdf, builds a resumable queue, and writes rebuildable ledgers and
reports inside the Nahida managed zone. It does not mutate original PDFs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

try:
    from pypdf import PdfReader
except Exception as exc:  # pragma: no cover - runtime prerequisite check
    print(f"pypdf unavailable: {exc}", file=sys.stderr)
    raise


TODAY = date.today().isoformat()
RUN_ID = f"nahida-update-{TODAY.replace('-', '')}-paper-domain-serial-v2"
QUEUE_ID = f"nahida-paper-folder-{TODAY.replace('-', '')}-domain-serial-v2"
EXTRACTOR = "codex-bundled-python:pypdf"

GENERIC_TITLE_PATTERNS = [
    r"^proceedings of\b",
    r"^\d+(st|nd|rd|th)\s+usenix\b",
    r"^acm reference format\b",
    r"^permission to make digital\b",
    r"^this paper is included\b",
    r"^paper\.dvi$",
    r"^main$",
    r"^document$",
    r"^download$",
    r"^untitled$",
    r"^noname manuscript$",
    r"^journal of latex class files\b",
    r"^under review\b",
    r"^to appear in\b",
    r"^see discussions, stats\b",
    r"^august \d+",
]

MANUAL_OVERRIDES: dict[str, dict[str, Any]] = {
    "357172.357176.pdf": {
        "title": "The Byzantine Generals Problem",
        "authors": "Leslie Lamport; Robert Shostak; Marshall Pease",
        "year": "1982",
        "doi": "10.1145/357172.357176",
        "canonical_url": "https://dl.acm.org/doi/10.1145/357172.357176",
        "domain_id": "distributed-systems",
        "direction_id": "consensus",
        "topic_ids": ["byzantine-fault-tolerance"],
        "priority_score": 1000,
        "priority_reason": "foundation source for Byzantine fault tolerance and consensus",
        "classification_confidence": "high",
        "classification_evidence": ["title", "known DOI", "abstract", "local PDF"],
    },
    "PBFT1.pdf": {
        "title": "Practical Byzantine Fault Tolerance",
        "authors": "Miguel Castro; Barbara Liskov",
        "year": "1999",
        "doi": "10.5555/296806.296824",
        "canonical_url": "https://dl.acm.org/doi/10.5555/296806.296824",
        "domain_id": "distributed-systems",
        "direction_id": "consensus",
        "topic_ids": ["byzantine-fault-tolerance", "state-machine-replication"],
        "priority_score": 970,
        "priority_reason": "foundation source for practical BFT state-machine replication",
        "classification_confidence": "high",
        "classification_evidence": ["title", "known DOI", "abstract", "local PDF"],
    },
    "6477178.pdf": {
        "title": "Constant-Size Commitments to Polynomials and Their Applications",
        "year": "2010",
        "doi": "10.1007/978-3-642-17373-8_11",
        "canonical_url": "https://doi.org/10.1007/978-3-642-17373-8_11",
        "domain_id": "zero-knowledge-proofs",
        "direction_id": "polynomial-commitments",
        "topic_ids": ["kzg-commitments"],
        "priority_score": 940,
        "priority_reason": "foundation source for KZG polynomial commitments",
        "classification_confidence": "high",
        "classification_evidence": ["known DOI", "title", "abstract", "local PDF"],
    },
    "document.pdf": {
        "title": "Delegating Computation: Interactive Proofs for Muggles",
        "domain_id": "verifiable-computation",
        "direction_id": "interactive-proofs",
        "topic_ids": ["delegated-computation", "gkr-protocol"],
        "priority_score": 900,
        "priority_reason": "foundation source for verifiable computation and GKR-style protocols",
        "classification_confidence": "high",
        "classification_evidence": ["title", "filename", "local PDF"],
    },
    "sumcheck.pdf": {
        "title": "The Sum-Check Protocol",
        "domain_id": "verifiable-computation",
        "direction_id": "interactive-proofs",
        "topic_ids": ["sum-check-protocol"],
        "priority_score": 880,
        "priority_reason": "foundation concept source for sum-check protocol",
        "classification_confidence": "high",
        "classification_evidence": ["filename", "title", "local PDF"],
    },
    "raft.pdf": {
        "title": "In Search of an Understandable Consensus Algorithm",
        "domain_id": "distributed-systems",
        "direction_id": "consensus",
        "topic_ids": ["crash-fault-tolerance", "raft"],
        "priority_score": 860,
        "priority_reason": "foundation source for crash-fault tolerant consensus",
        "classification_confidence": "high",
        "classification_evidence": ["title", "filename", "local PDF"],
    },
}


@dataclass
class PdfRecord:
    path: Path
    rel: str
    filename: str
    size: int
    sha256: str
    metadata: dict[str, Any] = field(default_factory=dict)
    metadata_title: str = ""
    title: str = ""
    title_source: str = ""
    title_confidence: str = "low"
    title_warnings: list[str] = field(default_factory=list)
    authors: str = ""
    year: str = "unknown"
    doi: str = ""
    arxiv_id: str = ""
    canonical_url: str = ""
    pages: int = 0
    first_page_excerpt: str = ""
    abstract: str = ""
    section_headings: list[str] = field(default_factory=list)
    extract_error: str = ""
    extractor: str = EXTRACTOR
    extracted_text_path: str = ""
    identity_key: str = ""
    duplicate_paths: list[str] = field(default_factory=list)
    duplicate_sha256: list[str] = field(default_factory=list)
    queue_status: str = "pending"
    domain_id: str = ""
    direction_id: str = ""
    topic_ids: list[str] = field(default_factory=list)
    ontology_path: list[str] = field(default_factory=list)
    primary_ontology_path: str = ""
    domains: list[str] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)
    primary_direction: str = ""
    secondary_directions: list[str] = field(default_factory=list)
    classification_confidence: str = "medium"
    classification_status: str = "staged"
    classification_evidence: list[str] = field(default_factory=list)
    direction_facets: dict[str, list[str]] = field(default_factory=dict)
    priority_score: int = 100
    priority_reason: str = "queued by reliable local identity and classification evidence"
    priority_evidence_fields: list[str] = field(default_factory=list)
    source_note_path: str = ""
    absorption_run: str = ""
    failure_reason: str = ""
    processed_at: str = ""


def load_previous_queue(vault: Path) -> dict[str, dict[str, Any]]:
    prev_path = vault / "02_Raw/pdf/nahida-paper-domain-serial-queue-20260611.json"
    if not prev_path.exists():
        return {}
    try:
        data = json.loads(prev_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out: dict[str, dict[str, Any]] = {}
    for row in data.get("records", []):
        rel = row.get("rel")
        if rel:
            out[rel] = row
    return out


def apply_previous_queue_hint(rec: PdfRecord, prev: dict[str, Any]) -> None:
    """Use the older queue as a hint, not as truth.

    The previous queue contains many better title/classification overrides, but
    this v2 run still applies generic-title checks and then manual overrides.
    """
    if not prev:
        return
    prev_title = re.sub(r"</?monospace>", "", str(prev.get("title", "")).strip())
    cur_title_bad = (
        rec.title_confidence == "low"
        or is_generic_title(rec.title)
        or len(rec.title.split()) < 4
        or rec.title.lower().startswith("arxiv:")
        or rec.title.endswith(": A")
    )
    if prev_title and not is_generic_title(prev_title) and (cur_title_bad or len(prev_title) > len(rec.title) + 12):
        rec.title = prev_title
        rec.title_source = "previous_queue_hint"
        rec.title_confidence = prev.get("title_confidence", "medium")
        rec.title_warnings = [w for w in rec.title_warnings if w != "filename_fallback"]
    for key in ("authors", "year", "doi", "arxiv_id", "canonical_url"):
        value = prev.get(key)
        if value and (not getattr(rec, key) or getattr(rec, key) == "unknown"):
            setattr(rec, key, value)
    for key in (
        "domain_id",
        "direction_id",
        "topic_ids",
        "classification_confidence",
        "classification_evidence",
        "priority_score",
        "priority_reason",
        "priority_evidence_fields",
    ):
        value = prev.get(key)
        if value:
            setattr(rec, key, value)


def slugify(text: str, fallback: str = "untitled") -> str:
    text = text.lower()
    text = re.sub(r"[/\\:*?\"<>|\x00-\x1f]+", "-", text)
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-. ")
    return text or fallback


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_metadata(meta: Any) -> dict[str, str]:
    if not meta:
        return {}
    out: dict[str, str] = {}
    for key, value in dict(meta).items():
        k = str(key).lstrip("/")
        v = str(value).strip()
        if v:
            out[k] = v
    return out


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def is_generic_title(title: str) -> bool:
    t = re.sub(r"\s+", " ", title.strip().lower())
    if not t:
        return True
    if len(t) < 4:
        return True
    for pat in GENERIC_TITLE_PATTERNS:
        if re.search(pat, t):
            return True
    if re.fullmatch(r"[\d\s\-_.]+", t):
        return True
    return False


def extract_doi(text: str) -> str:
    patterns = [
        r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b",
        r"doi\.org/(10\.\d{4,9}/[-._;()/:A-Z0-9]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            doi = m.group(1) if m.lastindex else m.group(0)
            return doi.rstrip(".,);]").lower()
    return ""


def extract_arxiv(path: Path, text: str) -> str:
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", path.name)
    if m:
        return "".join([m.group(1), m.group(2) or ""])
    m = re.search(r"arxiv[:\s]+(\d{4}\.\d{4,5})(v\d+)?", text, re.I)
    if m:
        return "".join([m.group(1), m.group(2) or ""])
    return ""


def extract_year(text: str, metadata: dict[str, str]) -> str:
    for key in ("CreationDate", "ModDate"):
        val = metadata.get(key, "")
        m = re.search(r"D:(19|20)\d{2}", val)
        if m:
            return m.group(0)[2:6]
    years = re.findall(r"\b(19[5-9]\d|20[0-3]\d)\b", text[:4000])
    if years:
        return years[0]
    return "unknown"


def title_from_first_page(first: str) -> tuple[str, str, list[str]]:
    warnings: list[str] = []
    lines = [re.sub(r"\s+", " ", line).strip() for line in first.splitlines()]
    lines = [line for line in lines if line and len(line) > 3]
    joined = " ".join(lines[:8])
    # Prefer text before author/abstract markers.
    m = re.search(r"(.{8,220}?)(?:\b[A-Z][a-z]+ [A-Z][a-z]+|\bAbstract\b|\bABSTRACT\b)", joined)
    candidates = []
    if m:
        candidates.append(m.group(1).strip(" -:;"))
    candidates.extend(lines[:6])
    for cand in candidates:
        cand = re.sub(r"^(appears in|published in).{0,120}?\s", "", cand, flags=re.I).strip()
        if not is_generic_title(cand):
            conf = "medium"
            if cand.isupper() or len(cand.split()) >= 4:
                conf = "medium"
            return cand, conf, warnings
    warnings.append("filename_fallback")
    return "", "low", warnings


def abstract_from_text(text: str, first: str) -> str:
    m = re.search(r"\bAbstract\b\s*[:.\-]?\s*(.{120,2500}?)(?:\n\s*(?:1\.|I\.|Introduction|INTRODUCTION)\b)", text, re.S)
    if not m:
        m = re.search(r"\bABSTRACT\b\s*[:.\-]?\s*(.{120,2500}?)(?:\n\s*(?:1\.|I\.|INTRODUCTION)\b)", text, re.S)
    if m:
        return clean_text(m.group(1))[:1800]
    return clean_text(first)[:1600]


def extract_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            continue
        if re.match(r"^(\d+(\.\d+)*|[IVX]+)\.?\s+[A-Z][A-Za-z0-9 ,()/:;'\-]{3,90}$", line):
            headings.append(line)
        elif line.isupper() and 4 <= len(line) <= 90 and not re.search(r"^[\d\s.]+$", line):
            headings.append(line.title())
        if len(headings) >= 40:
            break
    deduped: list[str] = []
    seen = set()
    for h in headings:
        key = h.lower()
        if key not in seen:
            seen.add(key)
            deduped.append(h)
    return deduped


def read_pdf(path: Path, root: Path, extract_dir: Path) -> PdfRecord:
    rel = str(path.relative_to(root))
    rec = PdfRecord(path=path, rel=rel, filename=path.name, size=path.stat().st_size, sha256=sha256_file(path))
    pages_text: list[str] = []
    try:
        reader = PdfReader(str(path))
        rec.metadata = normalize_metadata(reader.metadata)
        rec.metadata_title = rec.metadata.get("Title", "").strip()
        rec.authors = rec.metadata.get("Author", "").strip()
        rec.pages = len(reader.pages)
        for idx, page in enumerate(reader.pages):
            try:
                page_text = page.extract_text() or ""
            except Exception as exc:
                page_text = f"[page_extract_error: {exc}]"
            pages_text.append(clean_text(page_text))
        full_text = "\n\n".join(f"===== PAGE {i + 1} =====\n{text}" for i, text in enumerate(pages_text))
        title_hint = rec.metadata_title if rec.metadata_title and not is_generic_title(rec.metadata_title) else ""
        stem = slugify(title_hint or path.stem, fallback="pdf")
        out_path = extract_dir / f"{stem}-{rec.sha256[:12]}-pages.txt"
        out_path.write_text(full_text, encoding="utf-8")
        rec.extracted_text_path = str(out_path)
        first = pages_text[0] if pages_text else ""
        first_for_title = first[:3500]
        rec.first_page_excerpt = clean_text(first)[:2200]
        rec.abstract = abstract_from_text("\n".join(pages_text[:8]), first)
        rec.section_headings = extract_headings("\n".join(pages_text[:20]))
        rec.doi = extract_doi(first + "\n" + rec.abstract)
        rec.arxiv_id = extract_arxiv(path, first + "\n" + rec.abstract)
        rec.year = extract_year(first, rec.metadata)
        if title_hint:
            rec.title = title_hint
            rec.title_source = "metadata"
            rec.title_confidence = "medium"
        else:
            title, conf, warnings = title_from_first_page(first_for_title)
            rec.title = title or path.stem
            rec.title_source = "first_page" if title else "filename"
            rec.title_confidence = conf if title else "low"
            rec.title_warnings.extend(warnings)
        if rec.metadata_title and is_generic_title(rec.metadata_title):
            rec.title_warnings.append("generic_metadata_title")
    except Exception as exc:
        rec.extract_error = str(exc)
        rec.title = path.stem
        rec.title_source = "filename"
        rec.title_confidence = "low"
        rec.title_warnings.append("extraction_error")
        rec.identity_key = f"sha256:{rec.sha256}"
    return rec


def classify_record(rec: PdfRecord) -> None:
    text = " ".join([rec.filename, rec.title, rec.abstract, " ".join(rec.section_headings)]).lower()
    if not rec.domain_id:
        if any(k in text for k in ["raft", "crash fault", "crash-fault", "paxos"]):
            rec.domain_id = "distributed-systems"
            rec.direction_id = "consensus"
            rec.topic_ids = ["crash-fault-tolerance"]
        elif any(k in text for k in ["byzantine", "bft", "tendermint", "consensus", "validated asynchronous"]):
            rec.domain_id = "distributed-systems" if any(k in text for k in ["lamport", "pbft", "raft"]) else "blockchain-systems"
            rec.direction_id = "consensus"
            rec.topic_ids = ["byzantine-fault-tolerance"]
        elif any(k in text for k in ["polynomial commitment", "kzg", "commitments to polynomials"]):
            rec.domain_id = "zero-knowledge-proofs"
            rec.direction_id = "polynomial-commitments"
            rec.topic_ids = ["kzg-commitments"]
        elif any(k in text for k in ["sum-check", "sumcheck", "interactive proof", "gkr", "delegating computation"]):
            rec.domain_id = "verifiable-computation"
            rec.direction_id = "interactive-proofs"
            rec.topic_ids = ["sum-check-and-gkr"]
        elif any(k in text for k in ["snark", "zero-knowledge", "zk", "proof aggregation", "folding", "plonk"]):
            rec.domain_id = "zero-knowledge-proofs"
            if any(k in text for k in ["folding", "recursive", "recursion", "accumulation"]):
                rec.direction_id = "recursion-and-folding"
                rec.topic_ids = ["folding-schemes"]
            elif any(k in text for k in ["cnn", "llm", "dnn", "federated", "machine learning", "neural"]):
                rec.direction_id = "zkml"
                rec.topic_ids = ["verifiable-inference"]
            elif any(k in text for k in ["cross-chain", "login", "blockchain"]):
                rec.direction_id = "applications"
                rec.topic_ids = ["blockchain-applications"]
            else:
                rec.direction_id = "proof-systems"
                rec.topic_ids = ["proof-system-foundations"]
        elif any(k in text for k in ["cross-chain", "sharding", "rollup", "data availability", "smart contract", "blockchain"]):
            rec.domain_id = "blockchain-systems"
            if "cross-chain" in text or "interoperability" in text:
                rec.direction_id = "interoperability"
                rec.topic_ids = ["cross-chain-protocols"]
            elif "shard" in text:
                rec.direction_id = "scaling-and-sharding"
                rec.topic_ids = ["sharded-ledgers"]
            elif "data availability" in text or "light client" in text:
                rec.direction_id = "data-availability-and-light-clients"
                rec.topic_ids = ["data-availability-sampling"]
            else:
                rec.direction_id = "execution-and-transactions"
                rec.topic_ids = ["transaction-processing"]
        elif any(k in text for k in ["lsm", "transaction", "crdt", "database", "storage", "calvin", "erasure"]):
            rec.domain_id = "distributed-systems"
            rec.direction_id = "data-management-and-storage"
            if "crdt" in text:
                rec.topic_ids = ["crdts"]
            elif "lsm" in text:
                rec.topic_ids = ["storage-engines"]
            else:
                rec.topic_ids = ["distributed-transactions"]
        elif any(k in text for k in ["synthetic data", "machine learning", "privacy", "llm inference", "financial time series"]):
            rec.domain_id = "ml-systems"
            rec.direction_id = "privacy-and-trustworthy-ml"
            rec.topic_ids = ["privacy-preserving-learning"]
        else:
            rec.domain_id = "review"
            rec.direction_id = "needs-review"
            rec.topic_ids = ["paper-intake-review"]
            rec.classification_confidence = "low"
            rec.classification_status = "review"
    if not rec.classification_evidence:
        evidence = []
        if rec.title_source in {"metadata", "first_page", "manual_override"}:
            evidence.append("title")
        if rec.abstract:
            evidence.append("abstract")
        if rec.doi or rec.arxiv_id:
            evidence.append("doi/arxiv")
        if not evidence:
            evidence.append("filename")
        rec.classification_evidence = evidence
    if rec.classification_confidence == "medium" and rec.title_confidence == "low":
        rec.classification_confidence = "low"
        rec.classification_status = "review"
    rec.ontology_path = [rec.domain_id, rec.direction_id, rec.topic_ids[0] if rec.topic_ids else "needs-review"]
    rec.primary_ontology_path = "/".join(rec.ontology_path)
    rec.domains = [rec.domain_id]
    rec.topics = rec.topic_ids
    rec.primary_direction = f"{rec.domain_id} -> {rec.direction_id}"
    rec.direction_facets = {
        "parent_domain": [rec.domain_id],
        "subdomain": [rec.direction_id],
        "problem": rec.topic_ids,
        "method_family": [],
        "system_layer": [],
        "evaluation_context": [],
        "application": [],
        "bridge": [],
    }
    if not rec.priority_evidence_fields:
        rec.priority_evidence_fields = rec.classification_evidence[:]
    if rec.priority_score == 100:
        base = 220
        if rec.classification_confidence == "high":
            base += 80
        if any(k in text for k in ["survey", "foundation", "practical byzantine", "byzantine generals", "raft", "kzg", "sum-check"]):
            base += 60
        if rec.classification_status == "review":
            base -= 80
        rec.priority_score = base

    override = MANUAL_OVERRIDES.get(rec.filename)
    if override:
        for key, value in override.items():
            setattr(rec, key, value)
        rec.title_source = "manual_override"
        rec.title_confidence = "high"
        rec.classification_status = "staged"

    rec.ontology_path = [rec.domain_id, rec.direction_id, rec.topic_ids[0] if rec.topic_ids else "needs-review"]
    rec.primary_ontology_path = "/".join(rec.ontology_path)
    rec.domains = [rec.domain_id]
    rec.topics = rec.topic_ids
    rec.primary_direction = f"{rec.domain_id} -> {rec.direction_id}"
    rec.direction_facets = {
        "parent_domain": [rec.domain_id],
        "subdomain": [rec.direction_id],
        "problem": rec.topic_ids,
        "method_family": [],
        "system_layer": [],
        "evaluation_context": [],
        "application": [],
        "bridge": [],
    }


def assign_identity(rec: PdfRecord) -> None:
    if rec.doi:
        rec.identity_key = f"doi:{rec.doi.lower()}"
    elif rec.arxiv_id:
        rec.identity_key = f"arxiv:{rec.arxiv_id.lower()}"
        rec.canonical_url = rec.canonical_url or f"https://arxiv.org/abs/{rec.arxiv_id}"
    else:
        rec.identity_key = f"sha256:{rec.sha256}"
    if rec.doi and not rec.canonical_url:
        rec.canonical_url = f"https://doi.org/{rec.doi}"


def record_to_dict(rec: PdfRecord) -> dict[str, Any]:
    d = rec.__dict__.copy()
    d["path"] = str(rec.path)
    return d


def build_queue(input_dir: Path, vault: Path, force: bool) -> dict[str, Any]:
    extract_dir = vault / "02_Raw/pdf/extracted"
    extract_dir.mkdir(parents=True, exist_ok=True)
    previous = load_previous_queue(vault)
    pdf_paths = sorted(input_dir.rglob("*.pdf")) + sorted(input_dir.rglob("*.PDF"))
    records = [read_pdf(path, input_dir, extract_dir) for path in pdf_paths]
    for rec in records:
        apply_previous_queue_hint(rec, previous.get(rec.rel, {}))
        classify_record(rec)
        assign_identity(rec)

    grouped: dict[str, list[PdfRecord]] = defaultdict(list)
    for rec in records:
        grouped[rec.identity_key].append(rec)

    unique: list[PdfRecord] = []
    duplicates: list[dict[str, Any]] = []
    for identity, group in grouped.items():
        group = sorted(group, key=lambda r: (0 if "/" not in r.rel else 1, r.rel))
        canonical = group[0]
        for dup in group[1:]:
            dup.queue_status = "duplicate"
            canonical.duplicate_paths.append(dup.rel)
            canonical.duplicate_sha256.append(dup.sha256)
            duplicates.append({
                "identity_key": identity,
                "canonical": canonical.rel,
                "duplicate": dup.rel,
                "dedupe_evidence": "exact DOI/arXiv/SHA identity",
                "dedupe_confidence": "high",
                "result": "duplicate",
            })
        unique.append(canonical)

    unique.sort(key=lambda r: (-r.priority_score, r.rel.lower()))
    for idx, rec in enumerate(unique, start=1):
        rec.queue_status = "pending"
        setattr(rec, "queue_id", QUEUE_ID)
        setattr(rec, "item_id", f"{QUEUE_ID}:item:{idx:04d}")
        setattr(rec, "queue_rank", idx)
        setattr(rec, "resume_command", "$nahida-update ~/Desktop/paper")

    queue = {
        "id": QUEUE_ID,
        "queue_id": QUEUE_ID,
        "run_id": RUN_ID,
        "created": TODAY,
        "updated": TODAY,
        "input_path": str(input_dir),
        "status": "partial_serial_pending",
        "queue_mode": "serial_auto",
        "total_pdf_count": len(records),
        "unique_identity_count": len(unique),
        "duplicate_count": len(duplicates),
        "soft_duplicate_review_count": 0,
        "processed_count": 0,
        "absorbed_count": 0,
        "remaining_count": len(unique),
        "current_item": "",
        "last_processed_item": "",
        "next_item": f"{QUEUE_ID}:item:0001" if unique else "",
        "next_pdf": unique[0].rel if unique else "",
        "failure_reason": "",
        "stop_reason": "queue_rebuilt_after_skill_review",
        "turn_item_budget": "small_batch_serial_quality",
        "continuation_required": bool(unique),
        "resume_command": "$nahida-update ~/Desktop/paper",
        "records": [record_to_dict(r) for r in unique],
        "duplicates": duplicates,
    }
    out = vault / "02_Raw/pdf/nahida-paper-domain-serial-queue-20260611-v2.json"
    if out.exists() and not force:
        raise SystemExit(f"queue exists; pass --force: {out}")
    out.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    write_ledgers(vault, queue)
    write_reports(vault, queue)
    return queue


def write_ledgers(vault: Path, queue: dict[str, Any]) -> None:
    class_path = vault / "90_Generated/ledgers/classification-ledger.jsonl"
    dedupe_path = vault / "90_Generated/ledgers/dedupe-ledger.jsonl"
    class_rows = []
    for r in queue["records"]:
        class_rows.append({
            "run_id": queue["run_id"],
            "queue_id": queue["queue_id"],
            "item_id": r["item_id"],
            "identity_key": r["identity_key"],
            "rel": r["rel"],
            "title": r["title"],
            "domain_id": r["domain_id"],
            "direction_id": r["direction_id"],
            "topic_ids": r["topic_ids"],
            "primary_ontology_path": r["primary_ontology_path"],
            "classification_status": r["classification_status"],
            "classification_confidence": r["classification_confidence"],
            "classification_evidence": r["classification_evidence"],
            "updated": TODAY,
        })
    class_path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in class_rows) + "\n", encoding="utf-8")
    dedupe_rows = queue.get("duplicates", [])
    dedupe_path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in dedupe_rows) + ("\n" if dedupe_rows else ""), encoding="utf-8")


def md_link(path: str) -> str:
    return f"`{path}`"


def write_reports(vault: Path, queue: dict[str, Any]) -> None:
    report = vault / "90_Generated/reports/intake/nahida-update-20260611-paper-domain-serial-v2.md"
    run_copy = vault / "90_Generated/runs/nahida-update-20260611-paper-domain-serial-v2.md"
    review = vault / "90_Generated/review-queues/paper-domain-serial-queue-20260611-v2.md"
    records = queue["records"]
    domains = Counter(r["domain_id"] for r in records)
    directions = Counter(f"{r['domain_id']}/{r['direction_id']}" for r in records)

    rows = []
    for r in records[:60]:
        rows.append(
            f"| {r['queue_rank']} | {r['queue_status']} | `{r['rel']}` | {r['title']} | "
            f"`{r['primary_ontology_path']}` | {r['priority_score']} | {r['classification_confidence']} | {r['priority_reason']} |"
        )
    dup_rows = [
        f"| {d['identity_key']} | `{d['canonical']}` | `{d['duplicate']}` | {d['dedupe_evidence']} | {d['result']} |"
        for d in queue.get("duplicates", [])
    ] or ["| none |  |  |  |  |"]
    domain_rows = [f"| `{k}` | {v} |" for k, v in domains.most_common()]
    direction_rows = [f"| `{k}` | {v} |" for k, v in directions.most_common()]

    frontmatter = f"""---
id: "{RUN_ID}"
title: "Nahida 更新：Desktop paper domain-first serial intake v2"
type: "run"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "partial_serial_pending"
run_id: "{RUN_ID}"
hierarchy_level: "run"
domain_id: ""
direction_id: ""
topic_ids: []
ontology_path: []
domains:
  - "distributed-systems"
  - "blockchain-systems"
  - "zero-knowledge-proofs"
  - "verifiable-computation"
  - "ml-systems"
tags:
  - "nahida/run"
  - "paper-intake"
  - "serial-auto"
created: "{TODAY}"
updated: "{TODAY}"
managed_by: "nahida"
run_ids:
  - "{RUN_ID}"
source_refs: []
confidence: "medium"
trust_tier: "unknown"
queue_id: "{QUEUE_ID}"
queue_mode: "serial_auto"
processed_count: 0
remaining_count: {queue['remaining_count']}
last_processed_item: ""
next_item: "{queue['next_item']}"
turn_item_budget: "small_batch_serial_quality"
continuation_required: true
resume_command: "$nahida-update ~/Desktop/paper"
---
"""
    body = f"""
# Nahida 更新：Desktop paper domain-first serial intake v2

## 输入识别

| 输入 | 类型 | 路由 skill | 置信度 | 说明 |
| --- | --- | --- | --- | --- |
| `~/Desktop/paper` | folder containing many PDFs | `nahida-update` -> serial paper queue -> `nahida-paper-read` -> `nahida-knowledge-get` | high | 重新读取 skill 后重建队列；{queue['total_pdf_count']} 个 PDF，{queue['unique_identity_count']} 个唯一 identity，{queue['duplicate_count']} 个 exact duplicate |

## 去重结果

| Identity | Canonical | Duplicate | Evidence | Result |
| --- | --- | --- | --- | --- |
{os.linesep.join(dup_rows)}

## 输入队列

> [!info]
> 这是 `serial_auto` staging queue。pending PDF 只有完成 `deep_read` 并经过 `nahida-knowledge-get` 后才会变成 durable evidence。队列由 v2 重建，修正了旧队列里部分身份/分类噪声。

| Rank | Status | PDF | Title | Candidate hierarchy | Score | Class confidence | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
{os.linesep.join(rows)}

完整队列见 `vault/02_Raw/pdf/nahida-paper-domain-serial-queue-20260611-v2.json`。

## 串行队列状态

- Queue mode: `serial_auto`
- Queue ID: `{QUEUE_ID}`
- Processed count: 0
- Remaining count: {queue['remaining_count']}
- Current item: none
- Next item: `{queue['next_item']}` / `{queue['next_pdf']}`
- Stop reason: `queue_rebuilt_after_skill_review`
- Resume command: `$nahida-update ~/Desktop/paper`
- Turn item budget: `small_batch_serial_quality`
- Continuation required: true

## 层级分布

### L1 Domains

| Domain ID | Count |
| --- | --- |
{os.linesep.join(domain_rows)}

### Top L2 Directions

| Domain/Direction | Count |
| --- | --- |
{os.linesep.join(direction_rows)}

## 深化门

| 条目 | 来源类型 | Deepening decision | Target path candidates | Next skill owner | Durable absorption eligible | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| all pending PDFs | paper/pdf | `deep_paper_required` | per queue JSON | `nahida-paper-read` | false until deep_read_complete/scoped_deep_read accepted | folder intake is staging only |

## 能力使用记录

| 能力 | 用途 | 状态 | 说明 |
| --- | --- | --- | --- |
| `nahida-update` | folder router + serial queue | used | skill re-read on {TODAY} |
| `nahida-paper-read` | per-paper deep read | queued | starts with next pending item |
| `nahida-knowledge-get` | absorption and pack propagation | queued | after each source note |
| `obsidian-markdown` / `obsidian-note` | Obsidian YAML/wikilinks/notes | used | hard prerequisite satisfied |
| `obsidian-bases` | paper serial dashboard | available | existing base retained |
| Codex bundled Python + pypdf | inventory/extraction | used | no system Poppler required |

## 知识库写入

- Queue JSON: `vault/02_Raw/pdf/nahida-paper-domain-serial-queue-20260611-v2.json`
- Intake report: `vault/90_Generated/reports/intake/nahida-update-20260611-paper-domain-serial-v2.md`
- Run copy: `vault/90_Generated/runs/nahida-update-20260611-paper-domain-serial-v2.md`
- Review queue: `vault/90_Generated/review-queues/paper-domain-serial-queue-20260611-v2.md`
- Ledgers: `classification-ledger.jsonl`, `dedupe-ledger.jsonl`

## 后续动作

1. 当前下一篇：`{queue['next_pdf']}`。
2. 对该 PDF 执行 `nahida-paper-read` deep read。
3. 交给 `nahida-knowledge-get`，创建/更新 Domain Pack -> Direction Pack -> Topic Pack -> Source Extension。
4. 更新 checkpoint 后继续下一篇。

## 处理日志

- {TODAY}: 重新读取 `nahida-update`/`nahida-paper-read`/`nahida-knowledge-get` 规则。
- {TODAY}: 使用 Codex bundled Python + pypdf 重建 PDF inventory、保守去重和 v2 队列。
"""
    content = frontmatter + body
    report.write_text(content, encoding="utf-8")
    run_copy.write_text(content, encoding="utf-8")

    review_rows = []
    for r in records:
        review_rows.append(f"| {r['queue_rank']} | `{r['rel']}` | {r['title']} | `{r['primary_ontology_path']}` | {r['queue_status']} | {r['classification_confidence']} | |")
    review_content = f"""---
id: "nahida-review-20260611-paper-domain-serial-queue-v2"
title: "Paper domain-first serial queue 2026-06-11 v2"
type: "review_queue"
schema_version: "1.0"
ontology_version: "1.0"
lifecycle: "active"
status: "open"
hierarchy_level: "run"
created: "{TODAY}"
updated: "{TODAY}"
managed_by: "nahida"
run_ids:
  - "{RUN_ID}"
tags:
  - "nahida/review"
  - "paper-intake"
  - "serial-auto"
queue_id: "{QUEUE_ID}"
processed_count: 0
remaining_count: {queue['remaining_count']}
last_processed_item: ""
next_item: "{queue['next_item']}"
turn_item_budget: "small_batch_serial_quality"
continuation_required: true
---

# Paper domain-first serial queue 2026-06-11 v2

## 摘要

- 输入 PDF: {queue['total_pdf_count']}
- 唯一 identity: {queue['unique_identity_count']}
- 已深读并吸收: 0
- 待处理: {queue['remaining_count']}
- exact duplicate path: {queue['duplicate_count']}
- 当前状态: `partial_serial_pending`
- 下一篇: `{queue['next_pdf']}`

## 待处理队列

| Rank | PDF | Title | Candidate ontology path | Queue status | Class confidence | Output |
| --- | --- | --- | --- | --- | --- | --- |
{os.linesep.join(review_rows)}

## 去重项

| Identity | Canonical | Duplicate | Status |
| --- | --- | --- | --- |
{os.linesep.join(f"| {d['identity_key']} | `{d['canonical']}` | `{d['duplicate']}` | duplicate |" for d in queue.get('duplicates', [])) or "| none | | | |"}

## Review Items

| 条目 | 原因 | 风险 | 建议动作 |
| --- | --- | --- | --- |
| all pending PDFs | 只有 inventory，没有 deep read | 不能作为 durable evidence | 按 serial queue 逐篇运行 `nahida-paper-read` |
| missing Foundation Packs | vault 的 Domain/Direction/Topic packs 仍很薄 | source-driven 上层过薄 | 每篇吸收时 parent-first 创建 seed pack |
| low-confidence classifications | 标题/抽取噪声或 filename-only | 方向归属可能漂移 | deep read 时复核 frontmatter 与 queue JSON |
"""
    review.write_text(review_content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir")
    parser.add_argument("--vault", default="vault")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    queue = build_queue(Path(args.input_dir).expanduser().resolve(), Path(args.vault), args.force)
    print(json.dumps({
        "queue_id": queue["queue_id"],
        "run_id": queue["run_id"],
        "total_pdf_count": queue["total_pdf_count"],
        "unique_identity_count": queue["unique_identity_count"],
        "duplicate_count": queue["duplicate_count"],
        "next_pdf": queue["next_pdf"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
