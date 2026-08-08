# Step 10: Reliable and Automated Workflows

Make the application dependable through background processing, test automation, correct dependency lifetimes, and observable multi-stage AI workflows.

## Outcomes

- Compare reviewed Copilot workflows in Visual Studio and VS Code.
- Implement an observable and recoverable background process.
- Test backend and browser behavior at appropriate levels.
- Select Blazor service lifetimes based on ownership and scope.
- Build an agent workflow with middleware, clear stages, and failure behavior.

## Study Items

### General AI

1. [ ] Use GitHub Copilot in Visual Studio for codebase questions, edits, refactoring, tests, review, and agent tasks, then compare the experience with VS Code ([Agent Mode in Visual Studio](https://www.youtube.com/watch?v=7_duh0HoT9o))

### ASP.NET Core

1. [ ] Implement background tasks or services with retries, idempotency, cancellation, failure visibility, and operational ownership ([Book: Chapter 34](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Hangfire Documentation](https://www.hangfire.io/))
2. [ ] Select unit, integration, and browser tests for application risks and keep test setup repeatable ([Book: Chapters 35 and 36](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Playwright .NET](https://playwright.dev/dotnet/))

### Blazor

1. [ ] Inject application services into components without coupling UI code to infrastructure ([Injecting Dependencies](https://blazor-university.com/dependency-injection/injecting-dependencies-into-blazor-components))
2. [ ] Compare component-scoped, scoped, transient, and singleton lifetimes and test the selected behavior ([Component Scoped Dependencies](https://blazor-university.com/dependency-injection/component-scoped-dependencies), [Dependency Lifetimes](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes))

### .NET AI

1. [ ] Use Agent Framework middleware for cross-cutting behavior such as telemetry, policy checks, or approvals ([Agent Framework Middleware](https://www.youtube.com/watch?v=v7VLSZqAssU))
2. [ ] Design a multi-stage Agent Framework workflow with observable transitions and controlled failures ([Agent Framework Workflows](https://www.youtube.com/watch?v=2BB9-kWb1Tc))

## Tasks

### Task 1: Build a Recoverable AI Workflow

**Goal:** Process a longer-running AI job without tying its lifetime to one web request.

**Deliverable:** Background job, Agent Framework workflow, middleware, persisted status, retry behavior, and operational runbook.

**Requirements:**

- Define at least three workflow stages with explicit inputs and outputs.
- Make retries safe for the selected operation.
- Support cancellation or a documented stop mechanism.
- Add middleware for logging plus one policy or human-approval concern.

**Acceptance criteria:**

- [ ] The job can be observed from queued through completed or failed states.
- [ ] Repeating a failed operation does not duplicate committed results.
- [ ] Workflow failure identifies the stage and preserves useful diagnostics.
- [ ] Human approval is enforced at the documented boundary.

### Task 2: Build the Reliability Suite

**Goal:** Verify important application behavior from services through the browser.

**Deliverable:** Unit tests, API integration tests, a browser smoke test, dependency-lifetime test, and test-running instructions.

**Requirements:**

- Unit test one decision-heavy service.
- Integration test one success and two failure API paths.
- Browser test one critical authenticated workflow.
- Demonstrate that the chosen UI service lifetime matches the intended scope.

**Acceptance criteria:**

- [ ] Tests run from a clean checkout using documented commands.
- [ ] Tests do not depend on execution order or shared mutable data.
- [ ] Failures produce actionable output.
- [ ] The lifetime test would fail if the service were registered incorrectly.

### Task 3: Compare AI-Assisted IDE Workflows

**Goal:** Evaluate where each IDE supports or hinders controlled C# development.

**Deliverable:** `docs/ai/ide-comparison.md` with the same bounded task attempted in Visual Studio and VS Code.

**Requirements:**

- Record prompts, suggestions, accepted and rejected changes, review effort, and check results.
- Use the same repository context and definition of done in both tools.

**Acceptance criteria:**

- [ ] The comparison uses observable evidence rather than preference alone.
- [ ] No suggested change is accepted without diff review and relevant checks.

## Submission

- Workflow implementation and operational runbook.
- Automated test suite and test output.
- Dependency-lifetime evidence.
- IDE comparison report.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-19`
- `API-18`
- `API-19`
- `BLAZOR-17`
- `BLAZOR-18`
- `DOTNET-AI-05`
- `DOTNET-AI-06`

## Navigation

[Course Index](README.md) | [Previous Step](step-09.md) | [Next Step](step-11.md)
