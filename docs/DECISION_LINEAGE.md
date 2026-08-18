# Cortex V6 / FOSSIL decision lineage

Pack: `pack_a4b5515c4c6a4f38ac433e04b03ab406` (dedicated Cortex V6 project pack; staged locally, not an upstream FOSSIL pack write)

## Evidence states

- **Primary / supported:** V6 is a small portable engineering-assurance and lifecycle kernel. (`clm_v6_portable_assurance_kernel_20260818`)
- **Primary / supported:** Cortex V6 owns operational control. (`clm_v6_control_ownership_20260818`)
- **Primary / supported:** FOSSIL owns durable knowledge/evidence/provenance/lineage, not active V6 work lifecycle. (`clm_v6_fossil_knowledge_ownership_20260818`)
- **Primary / supported:** FOSSIL is deliberately deferred from the first #3 kernel proof. (`clm_v6_fossil_attachment_deferred_20260818`)
- **Primary / supported:** project-only vs FOSSIL-only vs hybrid context remains an Issue #17 bakeoff; hybrid is not yet a settled decision. (`clm_v6_context_bakeoff_open_20260818`)
- **Primary / supported at snapshot:** PRs #21–#24 document the intended foundation → walking-skeleton → context/adversarial sequence and are still open drafts. (`clm_v6_execution_chain_draft_20260818`)
- **Derived / proposed:** no FOSSIL-core schema, storage, pack, or ingestion contract change is prescribed by this V6 evidence; revisit after #17. (`clm_v6_fossil_core_impact_assessment_20260818`)

## Decision tree

```text
V6 portable lifecycle/assurance kernel
├─ Cortex owns CONTROL
├─ FOSSIL owns KNOWLEDGE
│  └─ does not own active V6 task/lifecycle state
├─ First prove the #3 irreducible kernel
│  └─ defer FOSSIL/runtime/model/provider attachments
└─ Then measure context strategy in Issue #17
   ├─ project-only
   ├─ FOSSIL-only
   └─ hybrid live project + FOSSIL (plausible, unproven)

Derived current assessment: ownership boundary YES; FOSSIL core-contract change NO.
```

## Provenance

- The public share-chat checkpoint is in `conversations/` and `lineages/`; its source status is `reconstructed` and it has no primary-authority role.
- The version-pinned locked plan, Issue #9, and PRs #20–#24 are source snapshots in `sources/snapshots/` with immutable content-addressed artifacts.
- Claim and relation events in `events/` are append-only and cite the corresponding snapshot bytes.
