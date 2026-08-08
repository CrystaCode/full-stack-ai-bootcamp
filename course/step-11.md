# Step 11: Production AI Applications

Prepare the portfolio application for real operation by evaluating its AI opportunities, hardening and orchestrating its services, and adding a bounded agent and generative interface.

## Outcomes

- Decide where AI creates product value and where a non-AI solution is safer.
- Publish, secure, and operationally verify the application.
- Orchestrate application resources with .NET Aspire.
- Evaluate production Blazor architecture options.
- Build a bounded Agent Framework feature and a validated generative UI interaction.

## Study Items

### General AI

1. [ ] Create an AI opportunity map covering intelligent features, smaller models, multimodal interfaces, tool use, agents, evaluation, risk, and non-AI fallback ([AI for Application Developers](https://www.youtube.com/watch?v=awztkr8n0AA))

### ASP.NET Core

1. [ ] Publish an ASP.NET Core application and document a repeatable deployment and rollback process ([Book: Chapter 27](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Deployment Learning Path](https://learn.microsoft.com/en-us/training/paths/aspnet-core-web-app/))
2. [ ] Apply HTTPS, secret handling, secure headers, least privilege, dependency review, and production hardening ([Book: Chapters 28 and 29](https://www.manning.com/books/asp-net-core-in-action-third-edition))
3. [ ] Model and run the application resources through a .NET Aspire AppHost and inspect their health and telemetry ([Introduction to .NET Aspire](https://www.youtube.com/watch?v=x2KAfsFydIo))

### Blazor

1. [ ] Evaluate production application architecture and cross-platform UI options against the product requirements ([Bit Platform Documentation](https://bitplatform.dev/))

### .NET AI

1. [ ] Build a bounded tool-using feature with Microsoft Agent Framework and explicit approval points ([Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-csharp))
2. [ ] Implement and validate a generative UI interaction using AG-UI or A2UI concepts ([Generative UI with AG-UI and A2UI](https://www.youtube.com/watch?v=aYe12ryuB4s))

## Tasks

### Task 1: Approve the Production AI Architecture

**Goal:** Make evidence-based decisions about AI, UI, security, and operational boundaries.

**Deliverable:** AI opportunity map, architecture decision record, threat and failure review, evaluation plan, and non-AI fallbacks.

**Requirements:**

- Score opportunities for user value, feasibility, evidence quality, cost, latency, privacy, and harm.
- Select one agent feature and one generative UI interaction that fit the product.
- Define human approval points and behavior when AI is unavailable.
- Evaluate the current Blazor architecture and record whether a production framework change is justified.

**Acceptance criteria:**

- [ ] Rejected AI opportunities include a clear reason.
- [ ] Each selected feature has measurable evaluation criteria.
- [ ] The architecture record distinguishes current decisions from future options.
- [ ] Every critical AI path has a safe fallback or controlled failure.

### Task 2: Orchestrate and Harden the Application

**Goal:** Make all application resources repeatable, observable, and suitable for deployment.

**Deliverable:** Aspire AppHost, health checks, secure configuration, publish instructions, rollback procedure, and production-readiness checklist.

**Requirements:**

- Model the web UI, API, database, and supporting resources in the AppHost.
- Keep secrets outside source control and use least-privilege access.
- Enforce HTTPS and review public endpoints and error details.
- Capture resource health, logs, and one distributed operation where available.

**Acceptance criteria:**

- [ ] A new developer can start the complete system from documented commands.
- [ ] The Aspire dashboard shows expected resources as healthy.
- [ ] Repository history and configuration contain no committed secrets.
- [ ] Publish and rollback instructions are executable and unambiguous.

### Task 3: Add the Intelligent Interaction

**Goal:** Implement the approved agent and generative UI features within the documented safety boundaries.

**Deliverable:** Agent feature, tool contracts, approval flow, generative UI component, evaluation cases, and fallback behavior.

**Requirements:**

- Restrict tools to the minimum operations required.
- Validate generated UI data before rendering or acting on it.
- Make agent progress, approval requests, failures, and completion visible to the user.
- Test normal, invalid, unavailable-provider, and denied-approval scenarios.

**Acceptance criteria:**

- [ ] The agent cannot perform an approval-gated action without approval.
- [ ] Invalid generated UI data fails safely.
- [ ] The user can distinguish generated suggestions from committed application state.
- [ ] Evaluation results meet the thresholds defined in the architecture task.

## Submission

- Opportunity map and architecture decision record.
- Production-readiness and security checklist.
- AppHost and deployment evidence.
- Agent and generative UI evaluation results.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-20`
- `API-15`
- `API-16`
- `API-20`
- `BLAZOR-19`
- `DOTNET-AI-07`
- `DOTNET-AI-08`

## Navigation

[Course Index](README.md) | [Previous Step](step-10.md) | [Next Step](step-12.md)
