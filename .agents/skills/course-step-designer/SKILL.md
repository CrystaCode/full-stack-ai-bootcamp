---
name: course-step-designer
description: Design and maintain integrated, numbered bootcamp course steps from multiple curriculum flow Markdown files. Use when creating or updating course/README.md, course/step-NN.md files, cross-flow coverage maps, study items, practical tasks, submissions, or completion criteria for a course that combines topics such as AI, backend, frontend, and application development in each step.
---

# Course Step Designer

Turn modular curriculum flows into one progressive course made of numbered steps. Keep the flows independent as design inputs; combine their outcomes only in learner-facing course files.

Read [references/course-step-schema.md](references/course-step-schema.md) completely before creating or editing course files.

## Workflow

1. Inspect all source flow files, the root curriculum index, the design documentation, and existing course files.
2. Assign a stable ID to every source outcome using the prefixes defined in the schema reference.
3. Design a sequence of vertical steps. Combine outcomes from multiple flows when they contribute to a coherent learner milestone or evolving project.
4. Record every assignment in `design/course-map.md` before or alongside authoring the step files.
5. Create `course/README.md` as the learner-facing course index.
6. Create or update `course/step-NN.md` files using the required schema.
7. Validate coverage, links, task quality, ordering, and navigation.

## Design Rules

- Create one integrated course, not one course directory per flow.
- Use explicit ordering in the course when it reflects the intended learner journey or a technical dependency.
- Prefer a vertical slice in each step: knowledge, implementation, and verification should reinforce one another.
- Include outcomes from at least two flows in a step when they form a useful combination. Do not force a flow into a step where it has no meaningful role.
- Let later technologies enter when their genuine prerequisites have been introduced.
- Keep the workload balanced. Prefer 4 to 8 study items and 2 to 4 tasks per step, adjusting when an outcome is unusually large.
- Evolve a shared portfolio application across the steps instead of producing unrelated exercises.
- Preserve the source resource links. Add a resource link directly to every study item.
- Write study items as observable learning actions: study, explain, compare, diagram, evaluate, or demonstrate.
- Write tasks as artifact-producing work: build, configure, test, document, review, or present.
- Give every task a goal, deliverable, and objective acceptance criteria.
- Include at least one integration task whenever a step covers multiple technical tracks.
- Separate required work from optional extensions. Label extensions `(Optional)`.
- Do not mark learner checkboxes complete when authoring course material.
- Do not use em dashes. Use colons, commas, or parentheses.

## Traceability Rules

- Map each source outcome to one primary course step.
- Revisit an outcome only when later application is intentional; mark that mapping as `Reinforcement` rather than duplicating primary coverage.
- Do not leave an outcome unmapped.
- Do not silently add new curriculum outcomes. Record additions as course-specific supporting items in the coverage map.
- When a flow changes, update the coverage map and affected step files together.

## Validation Checklist

- Confirm `course/README.md` links every numbered step in order.
- Confirm every source outcome appears in `design/course-map.md`.
- Confirm every primary mapping points to an existing step file.
- Confirm each step follows the required heading order.
- Confirm every step contains study items, tasks, submission requirements, and completion criteria.
- Confirm every study item links to a supporting resource.
- Confirm every task produces a reviewable artifact and has acceptance criteria.
- Confirm prerequisites are introduced before dependent implementation work.
- Confirm no step is organized as several disconnected mini-courses.
