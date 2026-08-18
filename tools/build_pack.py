"""Build the staged Cortex V6 decision-lineage pack through FOSSIL contracts."""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

PACK_ID = "pack_a4b5515c4c6a4f38ac433e04b03ab406"
RETRIEVED_AT = "2026-08-18T05:10:22Z"
PLAN_COMMIT = "49731f68f0843d368b4613774b57aa9ae48a4086"
PLAN_OCCURRED_AT = "2026-08-18T02:38:38Z"
WORKSPACE = Path(__file__).resolve().parents[2]
PACK_ROOT = Path(__file__).resolve().parents[1]
FOSSIL_CORE = WORKSPACE / "fossil-core"

sys.path[:0] = [str(FOSSIL_CORE / "src"), str(FOSSIL_CORE)]

from fossil_core.artifact_store import ArtifactStore
from fossil_core.event_store import DurableEventStore
from fossil_core.io import publish_immutable
from fossil_core.source import SourceSnapshotStore
from scripts.ingest_shared_chat_reconstructions import ingest_manifest


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def publish(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if publish_immutable(path, data):
        return
    if path.read_bytes() != data:
        raise RuntimeError(f"immutable output conflict: {path}")


def fetch_json(url: str) -> tuple[bytes, dict[str, str | None]]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "cortex-v6-decision-lineage-ingestor",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read(), {
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
        }


def quality(*, authority: float, directness: float, independence: float, reproducibility: float, timeliness: float, notes: str) -> dict[str, Any]:
    return {
        "authority": authority,
        "directness": directness,
        "independence": independence,
        "reproducibility": reproducibility,
        "timeliness": timeliness,
        "notes": notes,
    }


def phrase_citation(store: SourceSnapshotStore, snapshot: dict[str, Any], phrase: str) -> dict[str, Any]:
    data = store.artifact_store.read_bytes(snapshot["artifact_id"])
    needle = phrase.encode("utf-8")
    start = data.find(needle)
    if start < 0:
        raise ValueError(f"citation phrase not found in {snapshot['snapshot_id']}: {phrase!r}")
    return store.create_citation(snapshot["snapshot_id"], byte_start=start, byte_end=start + len(needle))


def event_base(*, event_type: str, subject_refs: list[str], occurred_at: str, recorded_at: str, idempotency_key: str, evidence_refs: list[str], source_snapshot_refs: list[str], payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "dkg.event.v1",
        "event_type": event_type,
        "occurred_at": occurred_at,
        "recorded_at": recorded_at,
        "pack_id": PACK_ID,
        "actor": {
            "actor_type": "importer",
            "actor_id": "cortex-v6-decision-lineage-ingestor",
            "harness_version": "cortex-v6-pack-ingest-v1",
            "skill_id": "skill_research-ingestion",
            "skill_version": "1.0.0",
        },
        "subject_refs": subject_refs,
        "idempotency_key": idempotency_key,
        "evidence_refs": evidence_refs,
        "source_snapshot_refs": source_snapshot_refs,
        "correlation_id": "cortex-v6-decision-lineage-2026-08-18",
        "payload": payload,
        "provenance": {
            "method": "cortex-v6-architecture-decision-lineage-ingestion",
            "prompt_or_policy_ref": "fossil-core/skills/research-ingestion/SKILL.md",
        },
    }


def build() -> dict[str, Any]:
    artifacts = ArtifactStore(PACK_ROOT / "artifacts")
    sources = SourceSnapshotStore(
        PACK_ROOT / "sources",
        artifacts,
        FOSSIL_CORE / "schemas" / "source-snapshot" / "v1.schema.json",
        FOSSIL_CORE / "schemas" / "citation" / "v1.schema.json",
    )
    events = DurableEventStore(PACK_ROOT / "events", FOSSIL_CORE / "schemas" / "events" / "v1.schema.json")

    plan = sources.put_snapshot(
        (WORKSPACE / "cortex-v6-source" / "docs" / "V6_LOCKED_PLAN.md").read_bytes(),
        locator={"url": f"https://raw.githubusercontent.com/Pukujan/Cortex-v6/{PLAN_COMMIT}/docs/V6_LOCKED_PLAN.md"},
        retrieved_at=RETRIEVED_AT,
        published_at=PLAN_OCCURRED_AT,
        source_role="primary",
        quality=quality(authority=1.0, directness=1.0, independence=0.5, reproducibility=1.0, timeliness=1.0, notes="Version-pinned first-party V6 locked plan."),
        version_metadata={"commit_sha": PLAN_COMMIT},
        media_type="text/markdown",
    )

    issue_bytes, issue_headers = fetch_json("https://api.github.com/repos/Pukujan/Cortex-v6/issues/9")
    issue = json.loads(issue_bytes)
    issue_snapshot = sources.put_snapshot(
        issue_bytes,
        locator={"url": "https://api.github.com/repos/Pukujan/Cortex-v6/issues/9"},
        retrieved_at=RETRIEVED_AT,
        published_at=issue["created_at"],
        source_role="primary",
        quality=quality(authority=1.0, directness=1.0, independence=0.5, reproducibility=1.0, timeliness=1.0, notes="First-party GitHub issue captured as raw API JSON."),
        version_metadata=issue_headers,
        media_type="application/json",
    )

    pr_snapshots: dict[int, dict[str, Any]] = {}
    for number in range(20, 25):
        data, headers = fetch_json(f"https://api.github.com/repos/Pukujan/Cortex-v6/pulls/{number}")
        payload = json.loads(data)
        pr_snapshots[number] = sources.put_snapshot(
            data,
            locator={"url": f"https://api.github.com/repos/Pukujan/Cortex-v6/pulls/{number}"},
            retrieved_at=RETRIEVED_AT,
            published_at=payload["created_at"],
            source_role="primary",
            quality=quality(authority=1.0, directness=1.0, independence=0.5, reproducibility=1.0, timeliness=1.0, notes="First-party GitHub pull-request record captured as raw API JSON."),
            version_metadata={**headers, "commit_sha": payload["head"]["sha"]},
            media_type="application/json",
        )

    observation = sources.put_snapshot(
        (PACK_ROOT / "recovery" / "2026-08-18-shared-page-observation.md").read_bytes(),
        locator={"identifier": "cortex-v6-fossil-shared-page-intake-observation-2026-08-18"},
        retrieved_at=RETRIEVED_AT,
        source_role="local",
        quality=quality(authority=0.4, directness=0.4, independence=0.2, reproducibility=0.7, timeliness=1.0, notes="Local intake observation of a rendered public page; not an original transcript export."),
        media_type="text/markdown",
    )
    reconstructed = sources.put_snapshot(
        (PACK_ROOT / "recovery" / "2026-08-18-cortex-v6-fossil-shared-chat-checkpoint.md").read_bytes(),
        locator={"url": "https://chatgpt.com/share/6a83d2c6-7d44-83ea-851f-48d98a6ac31f?ogimg=plain"},
        retrieved_at=RETRIEVED_AT,
        source_role="reconstructed",
        quality=quality(authority=0.3, directness=0.3, independence=0.2, reproducibility=0.6, timeliness=1.0, notes="Explicitly reconstructed checkpoint, preserved only as decision-lineage context."),
        derivation={"method": "rendered-public-share-page-checkpoint", "parent_snapshot_refs": [observation["snapshot_id"]]},
        media_type="text/markdown",
    )

    chat_result = ingest_manifest(
        PACK_ROOT / "ingestion" / "shared-chat-manifest.json",
        PACK_ROOT,
        repo_root=FOSSIL_CORE,
    )[0]

    sequence = 1
    committed: dict[str, dict[str, Any]] = {}

    def next_time() -> str:
        nonlocal sequence
        value = (datetime.fromisoformat(RETRIEVED_AT.replace("Z", "+00:00")) + timedelta(seconds=sequence)).isoformat().replace("+00:00", "Z")
        sequence += 1
        return value

    def commit_claim(claim_id: str, text: str, snapshot: dict[str, Any], phrase: str, *, additional_snapshots: list[dict[str, Any]] | None = None, state: str = "supported", occurred_at: str = PLAN_OCCURRED_AT) -> None:
        selected = [snapshot, *(additional_snapshots or [])]
        citation = phrase_citation(sources, snapshot, phrase)
        proposed = events.commit(event_base(
            event_type="claim.proposed",
            subject_refs=[claim_id],
            occurred_at=occurred_at,
            recorded_at=next_time(),
            idempotency_key=f"cortex-v6:{claim_id}:proposed",
            evidence_refs=[item["artifact_id"] for item in selected],
            source_snapshot_refs=[item["snapshot_id"] for item in selected],
            payload={"claim_text": text, "citation": citation},
        ))
        committed[claim_id] = proposed
        if state != "proposed":
            events.commit(event_base(
                event_type="claim.state_changed",
                subject_refs=[claim_id],
                occurred_at=occurred_at,
                recorded_at=next_time(),
                idempotency_key=f"cortex-v6:{claim_id}:{state}",
                evidence_refs=[snapshot["artifact_id"]],
                source_snapshot_refs=[snapshot["snapshot_id"]],
                payload={"from_state": "proposed", "to_state": state, "citation": citation},
            ))

    commit_claim(
        "clm_v6_portable_assurance_kernel_20260818",
        "The locked V6 plan defines Cortex V6 as a small portable engineering-assurance and lifecycle kernel over external runtime, model, tooling, and assurance systems.",
        plan,
        "Cortex V6 is being reduced to a **small portable engineering-assurance and lifecycle kernel**",
        additional_snapshots=[issue_snapshot],
    )
    commit_claim(
        "clm_v6_control_ownership_20260818",
        "The locked V6 plan assigns bounded operational control—state, scope, routing, assurance obligations, evidence binding, and lifecycle transitions—to Cortex V6.",
        plan,
        "### 3.2 Cortex V6 owns CONTROL",
        additional_snapshots=[issue_snapshot],
    )
    commit_claim(
        "clm_v6_fossil_knowledge_ownership_20260818",
        "The locked V6 plan assigns durable knowledge, evidence, provenance, lineage, reusable history, disagreement/supersession, and retrieval projections to FOSSIL—not active Cortex work lifecycle state.",
        plan,
        "FOSSIL owns durable knowledge/evidence semantics, not active work lifecycle:",
        additional_snapshots=[issue_snapshot],
    )
    commit_claim(
        "clm_v6_fossil_attachment_deferred_20260818",
        "The initial #3 walking-skeleton proof must not attach FOSSIL (or the other external platform subsystems) merely to appear production-complete; the irreducible kernel control semantics are proved first.",
        plan,
        "After #2, #3 must stay intentionally tiny. Do not attach Microsoft Agent Framework, AWS AgentCore, FOSSIL, LiteLLM, planner fanout, dynamic risk routing, or a general assurance-provider framework merely to make #3 look production-complete.",
    )
    commit_claim(
        "clm_v6_context_bakeoff_open_20260818",
        "The locked V6 plan leaves project-only, FOSSIL-only, and hybrid context as an Issue #17 measured bakeoff; hybrid is plausible but not settled architecture.",
        plan,
        "live project + FOSSIL hybrid is plausible, but #17 must test it.",
    )
    commit_claim(
        "clm_v6_execution_chain_draft_20260818",
        "At this snapshot, PR #21 (#2) through PR #24 (#7) describe the foundation → walking skeleton → stable-context/adversarial-regression proof chain, but remain open drafts rather than merged V6 implementation.",
        pr_snapshots[22],
        "This PR is intentionally stacked on `agent/swe-foundation` / #2",
        additional_snapshots=[pr_snapshots[21], pr_snapshots[23], pr_snapshots[24]],
        occurred_at="2026-08-18T02:52:48Z",
    )
    commit_claim(
        "clm_v6_fossil_core_impact_assessment_20260818",
        "Initial ingestion assessment: the V6 evidence establishes a Cortex↔FOSSIL ownership boundary, but does not prescribe a change to FOSSIL core storage, schema, pack, or ingestion contracts. Re-review this assessment when the Issue #17 context bakeoff is decided.",
        plan,
        "FOSSIL owns durable knowledge/evidence semantics, not active work lifecycle:",
        additional_snapshots=[issue_snapshot],
        state="proposed",
    )

    def commit_relation(relation_id: str, relation_type: str, source_ref: str, target_ref: str, snapshot: dict[str, Any], phrase: str) -> None:
        citation = phrase_citation(sources, snapshot, phrase)
        events.commit(event_base(
            event_type="relation.proposed",
            subject_refs=[relation_id, source_ref, target_ref],
            occurred_at=PLAN_OCCURRED_AT,
            recorded_at=next_time(),
            idempotency_key=f"cortex-v6:{relation_id}:proposed",
            evidence_refs=[snapshot["artifact_id"]],
            source_snapshot_refs=[snapshot["snapshot_id"]],
            payload={
                "relation_id": relation_id,
                "relation_type": relation_type,
                "source_ref": source_ref,
                "target_ref": target_ref,
                "state": "active",
                "citation": citation,
            },
        ))

    commit_relation(
        "rel_v6_control_refines_kernel_20260818",
        "REFINES",
        "clm_v6_control_ownership_20260818",
        "clm_v6_portable_assurance_kernel_20260818",
        plan,
        "### 3.2 Cortex V6 owns CONTROL",
    )
    commit_relation(
        "rel_v6_fossil_refines_kernel_20260818",
        "REFINES",
        "clm_v6_fossil_knowledge_ownership_20260818",
        "clm_v6_portable_assurance_kernel_20260818",
        plan,
        "FOSSIL owns durable knowledge/evidence semantics, not active work lifecycle:",
    )
    commit_relation(
        "rel_v6_fossil_deferral_depends_on_kernel_20260818",
        "DEPENDS_ON",
        "clm_v6_fossil_attachment_deferred_20260818",
        "clm_v6_portable_assurance_kernel_20260818",
        plan,
        "After #2, #3 must stay intentionally tiny. Do not attach Microsoft Agent Framework, AWS AgentCore, FOSSIL, LiteLLM, planner fanout, dynamic risk routing, or a general assurance-provider framework merely to make #3 look production-complete.",
    )
    commit_relation(
        "rel_v6_context_related_to_fossil_ownership_20260818",
        "RELATED_TO",
        "clm_v6_context_bakeoff_open_20260818",
        "clm_v6_fossil_knowledge_ownership_20260818",
        plan,
        "live project + FOSSIL hybrid is plausible, but #17 must test it.",
    )
    commit_relation(
        "rel_v6_core_impact_derived_from_boundary_20260818",
        "DERIVED_FROM",
        "clm_v6_fossil_core_impact_assessment_20260818",
        "clm_v6_fossil_knowledge_ownership_20260818",
        plan,
        "FOSSIL owns durable knowledge/evidence semantics, not active work lifecycle:",
    )
    commit_relation(
        "rel_v6_core_impact_depends_on_bakeoff_20260818",
        "DEPENDS_ON",
        "clm_v6_fossil_core_impact_assessment_20260818",
        "clm_v6_context_bakeoff_open_20260818",
        plan,
        "live project + FOSSIL hybrid is plausible, but #17 must test it.",
    )

    manifests = []
    for path in sorted((PACK_ROOT / "artifacts" / "manifests").glob("*/*.json")):
        manifests.append(json.loads(path.read_text(encoding="utf-8")))
    publish(PACK_ROOT / "artifacts" / "manifest.jsonl", b"".join(canonical(item) for item in manifests))

    decision_tree = f"""# Cortex V6 / FOSSIL decision lineage\n\nPack: `{PACK_ID}` (dedicated Cortex V6 project pack; staged locally, not an upstream FOSSIL pack write)\n\n## Evidence states\n\n- **Primary / supported:** V6 is a small portable engineering-assurance and lifecycle kernel. (`clm_v6_portable_assurance_kernel_20260818`)\n- **Primary / supported:** Cortex V6 owns operational control. (`clm_v6_control_ownership_20260818`)\n- **Primary / supported:** FOSSIL owns durable knowledge/evidence/provenance/lineage, not active V6 work lifecycle. (`clm_v6_fossil_knowledge_ownership_20260818`)\n- **Primary / supported:** FOSSIL is deliberately deferred from the first #3 kernel proof. (`clm_v6_fossil_attachment_deferred_20260818`)\n- **Primary / supported:** project-only vs FOSSIL-only vs hybrid context remains an Issue #17 bakeoff; hybrid is not yet a settled decision. (`clm_v6_context_bakeoff_open_20260818`)\n- **Primary / supported at snapshot:** PRs #21–#24 document the intended foundation → walking-skeleton → context/adversarial sequence and are still open drafts. (`clm_v6_execution_chain_draft_20260818`)\n- **Derived / proposed:** no FOSSIL-core schema, storage, pack, or ingestion contract change is prescribed by this V6 evidence; revisit after #17. (`clm_v6_fossil_core_impact_assessment_20260818`)\n\n## Decision tree\n\n```text\nV6 portable lifecycle/assurance kernel\n├─ Cortex owns CONTROL\n├─ FOSSIL owns KNOWLEDGE\n│  └─ does not own active V6 task/lifecycle state\n├─ First prove the #3 irreducible kernel\n│  └─ defer FOSSIL/runtime/model/provider attachments\n└─ Then measure context strategy in Issue #17\n   ├─ project-only\n   ├─ FOSSIL-only\n   └─ hybrid live project + FOSSIL (plausible, unproven)\n\nDerived current assessment: ownership boundary YES; FOSSIL core-contract change NO.\n```\n\n## Provenance\n\n- The public share-chat checkpoint is in `conversations/` and `lineages/`; its source status is `reconstructed` and it has no primary-authority role.\n- The version-pinned locked plan, Issue #9, and PRs #20–#24 are source snapshots in `sources/snapshots/` with immutable content-addressed artifacts.\n- Claim and relation events in `events/` are append-only and cite the corresponding snapshot bytes.\n"""
    publish(PACK_ROOT / "docs" / "DECISION_LINEAGE.md", decision_tree.encode("utf-8"))
    result = {
        "pack_id": PACK_ID,
        "chat": chat_result,
        "source_snapshots": [snapshot["snapshot_id"] for snapshot in [plan, issue_snapshot, *pr_snapshots.values(), observation, reconstructed]],
        "claim_event_ids": {claim_id: event["event_id"] for claim_id, event in committed.items()},
    }
    publish(PACK_ROOT / "ingestion" / "result.json", canonical(result))
    return result


if __name__ == "__main__":
    print(json.dumps(build(), indent=2, sort_keys=True))
