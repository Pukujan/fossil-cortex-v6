# Cortex V6 / FOSSIL decision lineage

Pack: `pack_a4b5515c4c6a4f38ac433e04b03ab406` (dedicated Cortex V6 project pack)

## Current authority rule

The original 2026-08-17/18 locked-plan evidence remains preserved. The **fresh-session audit does not erase it**. Instead, it records a partial supersession:

- vendor-independent kernel/ownership invariants remain current;
- the #2 → #3 → #4/#7 minimal-kernel floor remains current;
- later implementation-specific architecture choices are reopened as hypotheses until their new qualification gates pass.

Primary fresh-audit snapshot: `snap_94484b6649c7963f3ca2034d` / `art_7d72739f9b5c2b1ac15facdae459a3e8`.

Machine-readable current-position graph: `lineages/lin_cortex_v6_fresh_session_audit_20260818.json`.

## Current evidence states

### Stable / current

- **Primary / supported:** project artifacts own current project truth and acceptance meaning.
- **Primary / supported:** Cortex V6 owns authoritative requirement/work/generation identity, authority, evidence admission, and lifecycle transitions.
- **Primary / supported:** external runtime/model/FOSSIL/assurance outputs cannot directly complete V6 work.
- **Primary / supported:** FOSSIL owns durable knowledge/evidence/provenance/lineage, not active V6 lifecycle state.
- **Primary / supported:** GitHub/CI remains an independent merge boundary.
- **Primary / supported:** the first implementation floor remains #2 → #3 → #4/#7.
- **Primary / supported:** PR #23/#24 behavior must be combined and qualified on one exact production SHA before later architecture. (`clm_v6_combined_kernel_gate_20260818`)
- **Primary / supported:** external qualification and serious simpler-baseline falsification must happen before accumulating major later abstractions.

### Superseded in part / reopened

- The original "Microsoft-first/AWS-portable runtime" direction is no longer treated as one peer runtime-substitution axis.
- A generic `AgentRuntime` seam is not automatically required merely because the old roadmap named it.
- Generalized `AssurancePlan`/provider machinery must earn itself against direct/simple assurance invocation.
- Exact multi-agent role vocabulary/topology remains experimental.
- Project-only/FOSSIL-only/hybrid context remains an Issue #17 bakeoff; hybrid is not preselected.
- The 3-probe / 30-normal retry policy is an unqualified target hypothesis, not inherited truth. (`clm_v6_retry_policy_hypothesis_20260818`)

### Corrected architecture distinctions

- **Primary / supported:** agent/orchestration framework portability and hosting/runtime portability are separate axes. (`clm_v6_framework_hosting_axes_separate_20260818`)
- Microsoft Agent Framework remains a plausible **application framework/orchestration candidate**, to be compared with a simpler direct/local baseline.
- AWS AgentCore is a **managed hosting/runtime candidate**; it may host application code using Microsoft Agent Framework or another framework rather than replacing the framework itself.
- `no new abstraction needed yet` is a valid result for either axis.

### Temporary OpenCode bootstrap lane

Primary OpenCode snapshot: `snap_1a288e71f09eb31a06678d5b` / `art_989e7eae6135c3315d07c4d6d6d2069e`.

- **Primary / supported:** OpenCode is a temporary bounded external execution shell only. (`clm_v6_opencode_external_shell_20260818`)
- It may execute one pre-granulated authorized worker/test-writer packet in an isolated workspace or one read-oriented reviewer/researcher/evaluator packet.
- It is **not** authoritative Cortex state, project planner, recursive orchestrator, hidden model router, completion authority, native #19 implementation, or a permanent dependency.
- **Primary / supported:** read authority does not automatically grant external-model egress authority. (`clm_v6_external_egress_gate_20260818`)
- #30 owns data classification/secret/egress policy; #33 owns OpenCode bootstrap qualification.

### LiteLLM / model transport

Primary transport snapshot: `snap_b15574fb4de0a21bc491c86f` / `art_9dff33a1689dd66e296c1fe77eead990`.

- **Primary / supported target:** one V6/OpenCode model-request ceiling: **600 seconds**. (`clm_v6_transport_600s_exact_model_20260818`)
- **Primary / supported target:** exact requested model identity; hidden cross-model fallback below Cortex is off by default. (`clm_v6_transport_no_hidden_fallback_20260818`)
- Model retry/cross-vendor switch returns to bootstrap/Cortex seating policy.
- Transport/rate-limit/tool/policy failures are not automatically model-capability failures.
- **Implementation remains unqualified:** `Pukujan/litellm-ckff-ops#24` must align and prove the actual LiteLLM/bridge/OpenCode path.

## Updated decision tree

```text
V6 durable invariants (CURRENT)
├─ Project owns CURRENT TRUTH / acceptance meaning
├─ Cortex V6 owns CONTROL
│  ├─ requirement/work/generation identity
│  ├─ authority
│  ├─ evidence admission
│  └─ lifecycle transitions
├─ FOSSIL owns KNOWLEDGE / provenance / lineage
├─ GitHub/CI owns independent merge gate
└─ external providers return results/evidence, not completion

Minimal kernel floor (CURRENT)
#2 ordinary SWE foundation
  -> #3 walking skeleton
  -> #4 stable task/context invariants
     + #7 adversarial composition regressions
          |
          v
       #26 COMBINE #4/#7 ON ONE EXACT SHA
          |
          v
       #29 Phase A: independent external kernel qualification
          |
          v
       #28 Gate A: serious simpler-baseline value test
          |
          v
       #32: prove SSC v1 absent from live kernel path

Future architecture (REOPENED / MUST EARN ITSELF)
├─ application framework axis
│  ├─ direct/local baseline
│  └─ Microsoft Agent Framework candidate
├─ hosting/runtime axis
│  ├─ local/container baseline
│  └─ AWS AgentCore candidate
├─ assurance-provider abstraction
├─ role/topology routing
├─ #17 context bakeoff
│  ├─ live-project only
│  ├─ FOSSIL-only control/special case
│  └─ hybrid live-authoritative + durable history
└─ #31/#19 model seating + retry policy
   └─ 3 probes / 30 normal retries = HYPOTHESIS until budgeted/qualified

External bootstrap lane used to BUILD V6 (NOT native V6)
#30 data-egress/secret authority
  + litellm-ckff-ops#24 transport implementation qualification
        |
        v
#33 OpenCode bootstrap qualification
├─ pre-granulated packet
├─ exact model seat
├─ 600s request target
├─ hidden fallback OFF
├─ isolated mutation workspace / read-only review mode
├─ independent project checks/CI
└─ return control to bootstrap controller between granules
```

## Corrected near-term execution order

```text
1. Review/accept #21 (#2)
2. Rebase/review/accept #22 (#3)
3. Integrate #23 + #24 and prove combined production composition (#26)
4. Run independent bootstrap kernel qualification (#29 Phase A)
5. Run minimal-kernel simpler-baseline/value gate (#28 Gate A)
6. Prove SSC v1 is absent from the live kernel path (#32 early phase)
7. Resolve framework-vs-hosting architecture (#27) before redefining #10-#12
8. Qualify data egress + actual LiteLLM transport (#30 + litellm-ckff-ops#24)
9. Qualify the external OpenCode bootstrap lane (#33)
10. Qualify only V5 donors actually needed (#5 / #31)
11. Expand later mechanisms one at a time behind progressive gates
```

`clm_v6_corrected_execution_order_20260818` captures the key supersession: **do not start by implementing #10.**

## Provenance

Original evidence remains preserved:

- reconstructed shared-chat checkpoint in `conversations/` and its original lineage;
- pinned original locked plan, Issue #9, and PR #20–#24 snapshots;
- original append-only claim/relation events.

Fresh audit evidence adds, without rewriting those records:

- version-pinned fresh audit artifact/snapshot;
- version-pinned OpenCode bootstrap contract artifact/snapshot;
- version-pinned LiteLLM 600-second exact-model contract artifact/snapshot;
- append-only fresh-audit claim events in `events/`;
- `lineages/lin_cortex_v6_fresh_session_audit_20260818.json` describing preserved, superseded-in-part, current, and unresolved positions.

When an older implementation-specific "locked" choice conflicts with this fresh audit, treat the older choice as **historical rationale under revalidation** unless Issue #25 later records an explicit disposition restoring it. Stable invariants are not superseded by that rule.
