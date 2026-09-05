# Step 13: Integrated Capstone

Complete, evaluate, demonstrate, and reflect on the full-stack AI product and the evidence accumulated throughout the course.

## Outcomes

- Deliver a coherent portfolio application rather than a collection of disconnected exercises.
- Demonstrate source-grounded research, verified AI outputs, human review, and non-AI fallbacks.
- Defend the product architecture and show automated and operational evidence.
- Communicate results, limitations, corrections, and future work to a technical audience.

## Study Items

### Capstone Review

1. [ ] Review the integrated portfolio outcome and identify missing research, educational, communication, application, prompt, context, source, check, correction, or human-decision evidence ([General AI Flow](../design/flows/flow-ai-general.md))
2. [ ] Re-run hallucination and verification checks against the completed product, verify important AI-generated claims against known facts or inspectable sources, record corrections, and identify the person accountable for each final decision ([Hallucinations @ 01:20:44](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=4844s), [Testing Known Answers @ 01:26:09](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=5169s), [Human Responsibility @ 03:09:21](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11361s))
3. [ ] Review the test strategy and close gaps in critical API and browser journeys ([ASP.NET Core integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0), [Playwright .NET introduction](https://playwright.dev/dotnet/docs/intro), [API testing](https://playwright.dev/dotnet/docs/api-testing), [CI guidance](https://playwright.dev/dotnet/docs/ci))
4. [ ] Revisit the AI opportunity map and confirm with repeatable evaluations that implemented AI features still outperform their documented non-AI alternatives for the intended cases ([AI for Application Developers](https://www.youtube.com/watch?v=awztkr8n0AA), [NIST AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook), [Agent Framework evaluation](https://learn.microsoft.com/en-us/agent-framework/agents/evaluation))

## Tasks

### Task 1: Complete the Capstone Release

**Goal:** Produce a stable, reviewable release of the integrated portfolio application.

**Deliverable:** Versioned source code, release notes, deployment instructions, architecture documentation, database setup, automated checks, and a known-limitations list.

**Requirements:**

- Remove unfinished required paths or mark them clearly as excluded from the release.
- Run formatting, build, test, security, and secret checks appropriate to the repository.
- Verify the application from a clean setup using the learner documentation.
- Tag or otherwise identify the exact capstone revision.

**Acceptance criteria:**

- [ ] The documented setup produces a running complete system.
- [ ] Required automated checks pass on the capstone revision.
- [ ] No secrets, private data, or unsupported claims are included.
- [ ] Known limitations and fallback behavior are visible to reviewers.

### Task 2: Assemble the Evidence Portfolio

**Goal:** Make the learning process, AI assistance, verification, and human judgment auditable.

**Deliverable:** Portfolio index linking the research brief, learning artifact, prompt and context records, content and visual artifacts, architecture decisions, source code, tests, evaluations, corrections, and human-controlled decisions.

**Requirements:**

- Include representative failed attempts and explain what changed.
- Trace important claims to sources and important product decisions to evidence.
- Distinguish AI-generated suggestions from learner-authored decisions and final responsibility.

**Acceptance criteria:**

- [ ] Every portfolio link resolves to an included or publicly accessible artifact.
- [ ] The portfolio demonstrates all primary outcome groups in the coverage map.
- [ ] Corrections and rejected AI suggestions are represented honestly.
- [ ] A reviewer can identify where human approval controls product state.

### Task 3: Demonstrate and Defend the Product

**Goal:** Present the product as a working system and defend its technical, verification, and human-accountability decisions.

**Deliverable:** Live or recorded demonstration, concise presentation, question-and-answer notes, retrospective, and prioritized next-step list.

**Requirements:**

- Demonstrate one standard user journey, one AI-assisted journey, one failure or fallback, and one operational signal.
- Explain architecture, data flow, security boundary, evaluation method, and human approval point.
- Record feedback and identify what should be kept, changed, or stopped.

**Acceptance criteria:**

- [ ] The demonstration uses the submitted capstone revision.
- [ ] Claims made during the presentation are supported by product or evaluation evidence.
- [ ] The retrospective names concrete technical and learning improvements.
- [ ] Future work is prioritized by value, risk, and dependency.

## Submission

- Link to the identified capstone revision and release documentation.
- Portfolio evidence index.
- Demonstration recording or presentation details.
- Retrospective and prioritized next-step list.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- Primary: `AI-21`
- Reinforcement: `AI-03`, `AI-20`, `API-16`, `API-19`

## Navigation

[Course Index](README.md) | [Previous Step](step-12.md)
