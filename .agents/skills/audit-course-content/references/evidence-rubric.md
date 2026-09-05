# Course Content Evidence Rubric

Use this rubric for both baseline and post-repair judgments.

## Units of Judgment

Keep three levels separate:

1. **Material clause:** one independently meaningful promise inside a Study Item.
2. **Source:** one linked video, page, document, or local file.
3. **Aggregate item:** the combined accessible source set linked beside the current Study Item.

A source can be Partial while the aggregate item is Full. Record both so supplemental documentation does not hide an overstated video label.

## Ratings

| Rating | Source-level meaning | Aggregate-item meaning |
|---|---|---|
| **Full** | Directly teaches, demonstrates, or documents every material clause in the Study Item. | Every material clause has direct, accessible support somewhere in the linked set. |
| **Partial** | Supports at least one material clause but omits, merely implies, or contradicts another. | At least one material clause remains only partly supported after all links are combined. |
| **Unsupported** | Is adjacent to the topic but directly supports none of the Study Item's material clauses. | At least one essential clause has no supporting linked source. |
| **Inaccessible** | Cannot be inspected because of credentials, enrollment, paywall, region, removal, or an unrecoverable media failure. | An essential clause depends only on inaccessible material. |

Use **Not audited** internally until acquisition and review are complete. Never convert it to Full because the title looks plausible.

## Material Clauses

Split on outcomes that could fail independently. Examples:

- “build, test, and review a diff” contains implementation, executed checks, and human review;
- “health, logs, traces, and metrics” contains four observable dashboard claims;
- “privacy, fairness, copyright, disclosure, and accountability” contains distinct governance decisions;
- “compare A with B using the same task and criteria” contains both tool coverage and a controlled comparison method.

Do not split incidental wording that does not change what a learner must know or demonstrate.

## Evidence Standards

### Videos

Accept spoken or caption evidence for narrated concepts and actions. Require visual inspection for claims about:

- exact on-screen code, package names, or configuration;
- successful compilation, tests, or runtime state;
- UI fidelity, generated images, slides, charts, or accessibility;
- dashboard health, logs, traces, metrics, or diffs;
- actions that narration mentions but the screen may not perform.

For each timestamped claim, check duration, the chapter boundary, nearby cues, and the screen where material. A timestamp that lands on an adjacent chapter is misleading even when the full video discusses the topic elsewhere.

Captions are evidence of narration, not proof that visible code compiles. A visible result is evidence of that recorded run, not proof that current packages still behave the same way.

### Pages and Documents

Read the body and relevant examples. Use the following limits:

- A title, search snippet, or link label proves nothing about detailed coverage.
- A sales page or catalog can prove availability and table-of-contents scope, not chapter contents.
- A marketing homepage can support product positioning, not a technical decision matrix.
- A warning inside a tutorial is material evidence and can invalidate the surrounding example.
- Current owner documentation governs version-sensitive behavior when an older tutorial conflicts.
- A date-pinned release page supports only that point in time; do not silently call it current later.

For PDFs, inspect the relevant text and visually verify pages when layout, figures, tables, or scan quality matter.

### Access Boundaries

Record the exact gate and date. Do not bypass licenses, authentication, enrollment, or regional controls. If a paid source remains linked, a freely readable source must independently support every essential clause before the aggregate item can be Full.

## Acquisition Order

1. Deduplicate exact URLs and canonicalize known variants.
2. Capture metadata and access status.
3. Prefer official transcripts or creator captions; use automatic captions as a fallback.
4. Inspect full media for captionless or visual-dependent claims.
5. Use audio transcription only when no usable captions exist and audio carries the claim.
6. Keep all temporary media outside the repository and record tool/version caveats that affect coverage.

For very long media, full-timeline captions can establish narrated coverage. Sampled frames are insufficient for a claim that depends on a specific visible action; inspect that interval or the full media when necessary.

## Evidence Ledger

Use at least these fields:

| Field | Required content |
|---|---|
| Step / item | Stable file and item identifier |
| Current claim | Exact learner-facing wording |
| Material clause | One independently auditable promise |
| Source | Exact URL or local target |
| Evidence | Timestamp/interval, heading, symbol, warning, or access error |
| Source rating | Full, Partial, Unsupported, or Inaccessible |
| Aggregate rating | Rating after all links beside the item are combined |
| Caveat | Visual, version, licensing, region, or inference boundary |
| Action | Keep, relabel, deep-link, supplement, narrow, split, replace, or accept |

Preserve a baseline ledger before repairs and a current aggregate ledger afterward. This makes the correction defensible instead of erasing the original defect.

## Repair Decisions

| Finding | Preferred correction |
|---|---|
| Wrong timestamp or target | Point to the correct interval/page or remove the misleading link. |
| Useful but Partial demonstration | Keep it and add a focused primary source for the missing clause. |
| Inflated wording | Narrow or split the claim if the extra promise is not a required outcome. |
| Generic landing page | Deep-link the actual lesson/chapter and add accessible evidence when the body is gated. |
| Stale API or product behavior | Add current owner documentation and date-pin any retained historical demo. |
| Unsafe or contradictory tutorial | Link the current safe guidance and state the lifetime, disposal, security, or version constraint explicitly. |
| Comparison or evaluation absent from sources | Make the learner task define the same inputs, criteria, checks, and evidence for both runs. |
| Essential source inaccessible | Report the blocker or add an independently sufficient accessible source; never assume the hidden content. |

## Completion Tests

An audit is defensible only when:

- every Study Item is represented once in the final matrix;
- every material clause has evidence or an explicit gap;
- source-level limitations remain visible beneath aggregate ratings;
- no Full rating relies on an inaccessible essential source;
- every changed claim, link, and dependent mapping has been re-audited;
- totals for files, items, links, canonical resources, ratings, and blockers reconcile;
- the output states what was not visually, legally, or technically verified.

Re-run at least the link, access, and version-status checks before each cohort. Repeat claim-level review when wording, resources, or major platform versions change.
