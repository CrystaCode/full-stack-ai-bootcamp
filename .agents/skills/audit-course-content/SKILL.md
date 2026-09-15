---
name: audit-course-content
description: Audit course lessons, numbered steps, and curriculum claims against every linked video, document, page, or local source. Use when asked to verify that linked resources actually teach the stated outcomes, identify misleading or stale links, or repair a course so its claims are defensible. Focused on source-content verification rather than ordinary curriculum drafting.
metadata:
  short-description: Verify course claims against source content
---

# Audit Course Content

Build a claim-level evidence chain from each learner-facing outcome to the actual content of its linked resources. A valid link is not proof of coverage.

Before assigning ratings, read [references/evidence-rubric.md](references/evidence-rubric.md) completely.

Resolve every relative skill resource against the directory containing this `SKILL.md`, not the repository working directory.

## Establish Scope and Authority

1. Read repository instructions and any curriculum schema or course-map conventions that govern the files.
2. Identify the learner-facing units, normally Study Items or lesson outcomes, and the linked resources beside each one.
3. Distinguish the requested mode:
   - **Audit:** inspect and report without changing course files.
   - **Repair:** audit, correct unsupported wording or resources, synchronize dependent curriculum files, and re-audit.
4. Record the audit date for version-sensitive products, APIs, packages, laws, policies, and interfaces.

The scope is established when every course file, Study Item, and expected dependent map or flow is named. Do not infer permission to create a report artifact; return findings in the conversation unless the user explicitly requests a file.

## Inventory the Course

For numbered Markdown steps that use `## Study Items`, run the deterministic inventory helper with an available Python 3 interpreter:

```text
<python-3> <skill-directory>/scripts/inventory_course.py <course-directory> --glob "step-*.md" --format json
```

Do not assume that `python` or `py` is a working command alias; locate an available interpreter when necessary. If Python 3 is unavailable, perform the same inventory manually. Adapt or inspect manually when the course uses a different schema. The helper inventories complete matching files, not individual item selectors; filter its JSON manifest for a subset audit. It inventories structure and links only and does not prove that a resource supports a claim.

Canonicalize repeated resources before acquisition. For YouTube, collapse timestamp variants to the video ID while retaining each timestamp occurrence for separate validation. Record exact duplicates, local targets, inaccessible resources, and items with no links.

Inventory is complete when every Study Item and link occurrence appears exactly once in the manifest and structural warnings have been explained.

## Acquire and Read the Sources

- Read the complete relevant source, not only its title, description, search snippet, thumbnail, or marketing copy.
- For videos, obtain metadata, duration, chapters, and the complete caption timeline when available. Prefer creator captions, then automatic captions. Inspect the complete video when captions are absent. Inspect the relevant visual intervals when a claim depends on visible code, UI state, diagrams, generated output, accessibility, build results, or other screen evidence, broadening to the complete video when the claim is global.
- Validate timestamp links against duration, chapter context, nearby transcript, and visible content when needed.
- For pages, follow redirects and inspect headings, body text, examples, warnings, version notes, and prerequisites. Treat a catalog, sales page, product homepage, or table of contents as evidence only for what it actually exposes.
- Prefer current primary sources for changing technical or product claims. Use secondary material as a demonstration, not as authority when it conflicts with current owner documentation.
- Keep downloaded captions and review media in an operating-system temporary directory. Respect authentication, enrollment, licensing, and copyright boundaries; record a blocker instead of bypassing it.

Acquisition is complete when every canonical resource is either read to the level required by its claim or explicitly classified as inaccessible with the reason.

## Build the Evidence Ledger

Split each Study Item into material clauses. For every clause, record the source, exact evidence location, source-level rating, and any visual or freshness caveat. Then assign a separate aggregate rating to the combined source set beside the item.

Evidence locations should be reproducible:

- video ID plus timestamp or interval;
- page URL plus heading, code symbol, warning, or version note;
- local file plus line or heading;
- access failure plus date and observed gate.

When work is parallelized, partition by non-overlapping step ranges or resource types, give every worker the same rubric, and reconcile ratings centrally. Do not merge conclusions without checking that every item is represented once.

The ledger is complete when every material clause is Full, Partial, Unsupported, or Inaccessible and no rating rests on a title-level inference.

## Repair Only When Authorized

Choose the smallest correction that preserves the intended outcome:

1. Fix a wrong target, label, chapter, or timestamp.
2. Add a current primary source for a missing material clause.
3. Narrow or split wording when the extra promise is not an intended outcome.
4. Replace stale or unsafe guidance and retain older demonstrations only when clearly labeled.
5. Make learner tasks produce the comparison, test, review, or decision evidence that a resource cannot provide by itself.
6. Synchronize source flows, course maps, indexes, and outcome IDs required by the repository schema.

Preserve unrelated and pre-existing user changes. Do not copy licensed text or commit downloaded media.

## Re-Audit and Validate

After repairs, repeat the aggregate audit against the current wording and current links. Also verify, where applicable:

- every Study Item has at least one link;
- external URIs parse and local targets exist;
- timestamp offsets are in range and context-aligned;
- required headings and task fields remain valid;
- source outcomes and coverage maps remain synchronized;
- temporary media did not enter the repository;
- formatting and repository checks pass.

Validation is complete only when the final counts reconcile with the manifest and every remaining Partial, Unsupported, or Inaccessible item is either intentionally accepted by the user or clearly reported.

## Deliver the Result

Lead with the current aggregate result, then distinguish it from the original or video-only baseline. Include:

- scope and acquisition totals;
- an item-level status matrix or a compact equivalent that accounts for every item;
- decisive evidence for failures and misleading links;
- corrections made, if authorized;
- access, visual, licensing, and freshness limitations;
- validation results and re-audit triggers.

State explicitly that **Full aggregate coverage does not mean every individual link covers every clause**. Create a standalone audit file only when the user asks for one.
