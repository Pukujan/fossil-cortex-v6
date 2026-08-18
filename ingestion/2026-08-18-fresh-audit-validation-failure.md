# Fresh-audit staging validation — FAILED

Date: 2026-08-18  
Pack: `pack_a4b5515c4c6a4f38ac433e04b03ab406`  
Tracking: #1

## Verdict

**FAILED / QUARANTINED. The 2026-08-18 fresh-audit append has not passed the real FOSSIL durable-event boundary and must not be represented as active ingested knowledge.**

The original initial Cortex V6 pack was built through FOSSIL `ArtifactStore`, `SourceSnapshotStore`, and `DurableEventStore` via `tools/build_pack.py`. The later fresh-audit append was written directly as repository JSON/files and bypassed that executable FOSSIL commit path.

## Mechanical failure

FOSSIL derives event identity from the stable logical operation:

```text
evt_ + sha256(pack_id + NUL + idempotency_key)[:32]
```

`DurableEventStore.prepare()` rejects a supplied `event_id` that does not equal the deterministic identity for the pack/idempotency key.

All nine fresh-audit event files fail this check:

| Staged file/event | Idempotency key | Expected FOSSIL event ID |
|---|---|---|
| `evt_06686b87506bce89ec27be6fd6dc76f4` | `cortex-v6:clm_v6_audit_reopens_future_architecture_20260818:proposed` | `evt_c388ac4b168c9b8b0acbdbef60748abe` |
| `evt_626efe71b1d395d7e88261b72b133108` | `cortex-v6:clm_v6_framework_hosting_axes_separate_20260818:proposed` | `evt_eaa107dcfcb81e6f40e8a9fa5812ecf9` |
| `evt_611d83a4bc1c0c5793544e818f5ada2e` | `cortex-v6:clm_v6_opencode_external_shell_20260818:proposed` | `evt_8c0aeef937809a847cc9a03aae5752dd` |
| `evt_b23baae96184cfe28fd3dc4dea30ba5e` | `cortex-v6:clm_v6_corrected_execution_order_20260818:proposed` | `evt_806c32ce6c9ac8c19a7bf87e2c34f323` |
| `evt_dbb2782830d05674ace76b42c32e9843` | `cortex-v6:clm_v6_transport_no_hidden_fallback_20260818:proposed` | `evt_1212b2a91e338a4572995adb1c46a385` |
| `evt_b6c6a3f113a81fb6e734e8df460632df` | `cortex-v6:clm_v6_external_egress_gate_20260818:proposed` | `evt_5d2abe439c0ae3886a2bbf32bad62c7a` |
| `evt_daf76cb2b8b842de1f7444ed46406d23` | `cortex-v6:clm_v6_combined_kernel_gate_20260818:proposed` | `evt_b9acba981adc475db670158275404ee3` |
| `evt_58db3116c2cf354a0272f7601005c46f` | `cortex-v6:clm_v6_retry_policy_hypothesis_20260818:proposed` | `evt_aaf17d59d16acbf414af8fcc21dbcd5b` |
| `evt_9f0ecd575eec1f35fb17f4610907dff4` | `cortex-v6:clm_v6_transport_600s_exact_model_20260818:proposed` | `evt_44f661215b1a383c58369701144ffb2d` |

The mismatched files remain in Git as evidence of the rejected staging attempt. **Do not rename them and treat that as ingestion.** Rebuild the append through the FOSSIL stores/contracts so identities, schemas, citations, content hashes, authorization, idempotency, and immutable commit behavior are generated/verified by code.

## Evidence-layer status

The fresh-audit source layer appears structurally stronger than the event layer: for example, `snap_94484b6649c7963f3ca2034d` pins an exact Cortex-v6 commit and references a content-addressed artifact under the same full SHA-256 digest. This observation is not a full validation receipt.

Issue #1 requires mechanical validation of every pack manifest, source snapshot, citation byte span/hash, artifact digest, event envelope, reference, and lineage before any promotion claim.

## Epistemic status

The old initial pack remains historical evidence. The fresh-session audit is preserved as a **proposal artifact**. It is already superseded in part by a subsequent adversarial planning campaign in `Pukujan/Cortex-v6#25` that found additional issues #34–#41.

Therefore repairing the nine event IDs and promoting the old fresh-audit conclusions unchanged would itself be wrong. The intended intellectual lineage is:

```text
original long-session plan
  -> fresh-session audit proposal
  -> adversarial challenges / counterexamples
  -> independent critic + adjudication
  -> canonical current plan
  -> FOSSIL-validated proposed/support/supersession events
```

## Exit gate

See #1. Until it closes with an actual FOSSIL validation/authorization/commit receipt (and projection/rebuild receipt if applicable), this repository is **durable staged evidence only**, not proof that active DICS/Graphiti contains the fresh/adversarial plan.