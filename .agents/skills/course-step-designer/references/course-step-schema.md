# Integrated Course Schema

## Source outcome IDs

Use these prefixes in `design/course-map.md` and step source notes:

- `AI-##`: General AI
- `API-##`: ASP.NET Core
- `WEB-##`: HTML and CSS frontend
- `BLAZOR-##`: Blazor
- `DOTNET-AI-##`: .NET AI

Numbers correspond to the numbered outcomes in each source flow.

## Course index

Use this structure for `course/README.md`:

```markdown
# Course Title

Concise learner-facing description of the integrated course and its evolving project.

## How the Course Works

Explain study items, tasks, submissions, and checkbox usage.

## Course Steps

1. [Step 01: Title](step-01.md)
2. [Step 02: Title](step-02.md)

## Final Outcome

Describe what learners will have built and demonstrated.
```

## Step file

Use this exact heading order for every `course/step-NN.md`:

```markdown
# Step NN: Title

Briefly explain the milestone and how its subjects connect.

## Outcomes

- Outcome the learner can demonstrate.

## Study Items

### Track Name

1. [ ] Observable learning activity ([Resource](https://example.com))

## Tasks

### Task 1: Artifact-oriented title

**Goal:** State the result.

**Deliverable:** State what must be submitted or committed.

**Requirements:**

- Requirement.

**Acceptance criteria:**

- [ ] Objective check.

## Submission

- Required files, links, screenshots, explanations, or test output.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `PREFIX-##`

## Navigation

[Course Index](README.md) | [Previous Step](step-NN.md) | [Next Step](step-NN.md)
```

Omit Previous Step in the first file and Next Step in the final file.

## Coverage map

Use a table in `design/course-map.md`:

```markdown
| Source ID | Source outcome | Primary step | Evidence |
|---|---|---|---|
| `AI-01` | Concise outcome | [Step 01](../course/step-01.md) | Diagram and explanation |
```

Group the table by flow. Keep outcome wording concise without changing its intent. Evidence must name the learner artifact or observable behavior used to verify coverage.
