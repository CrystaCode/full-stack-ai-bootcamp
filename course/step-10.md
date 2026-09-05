# Step 10: Reliable and Automated Workflows

Make the application dependable through background processing, test automation, correct dependency lifetimes, and observable multi-stage AI workflows.

## Outcomes

- Compare reviewed Copilot workflows in Visual Studio and VS Code.
- Implement an observable and recoverable background process.
- Test backend and browser behavior at appropriate levels.
- Select Blazor service lifetimes based on ownership and scope.
- Persist agent state and memory, apply middleware, and run an observable sequential agent workflow with controlled failures.

## Study Items

### General AI

1. [ ] Use GitHub Copilot in Visual Studio for codebase questions, edits, refactoring, tests, local-change review, and agent tasks, then compare the same bounded task and checks with VS Code ([Agent Mode in Visual Studio](https://www.youtube.com/watch?v=7_duh0HoT9o), [Copilot Chat in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=vs-2022), [Visual Studio custom agents](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio), [Manage chat and Git context](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context-references?view=vs-2022), [Build with agents in VS Code](https://code.visualstudio.com/docs/agents/overview), [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices))

### ASP.NET Core

1. [ ] Implement background tasks or services with visible retries, idempotent or reentrant handlers, cancellation, and failure diagnostics ([Book: Chapter 34](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-34), [Hosted services](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-10.0), [Hangfire background methods](https://docs.hangfire.io/en/latest/background-methods/index.html), [Hangfire exception and retry behavior](https://docs.hangfire.io/en/latest/background-processing/dealing-with-exceptions.html), [Hangfire cancellation tokens](https://docs.hangfire.io/en/latest/background-methods/using-cancellation-tokens.html), [Hangfire best practices](https://docs.hangfire.io/en/latest/best-practices.html))
2. [ ] Select unit, integration, API, and browser tests by application risk and keep test setup repeatable ([Book: Chapter 35](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-35), [Chapter 36](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-36), [Testing in .NET](https://learn.microsoft.com/en-us/dotnet/core/testing/), [ASP.NET Core integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0), [Playwright .NET introduction](https://playwright.dev/dotnet/docs/intro), [API testing](https://playwright.dev/dotnet/docs/api-testing), [CI guidance](https://playwright.dev/dotnet/docs/ci))

### Blazor

1. [ ] Inject application services into components without coupling UI code to infrastructure ([Injecting Dependencies](https://blazor-university.com/dependency-injection/injecting-dependencies-into-blazor-components), [Current Blazor dependency injection](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/dependency-injection?view=aspnetcore-10.0))
2. [ ] Compare component-scoped, scoped, transient, and singleton lifetimes, account for render-mode and disposal behavior, and test the selected behavior ([Component Scoped Dependencies](https://blazor-university.com/dependency-injection/component-scoped-dependencies), [Dependency Lifetimes](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes), [Current Blazor dependency injection](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/dependency-injection?view=aspnetcore-10.0))

### .NET AI

1. [ ] Persist agent state with sessions and user memory, configure behavior through settings, and control what is stored ([Agent Sessions](https://www.youtube.com/watch?v=p5AvoMbgPtI), [AIAgent settings](https://www.youtube.com/watch?v=6i1Rs0MkBDQ), [User Memory](https://www.youtube.com/watch?v=AndCk0HeddQ), [Current memory guidance](https://learn.microsoft.com/en-us/agent-framework/get-started/memory))
2. [ ] Apply Agent Framework middleware for observable cross-cutting behavior such as telemetry, policy checks, or approvals ([Middleware](https://www.youtube.com/watch?v=v7VLSZqAssU), [Current middleware concepts](https://learn.microsoft.com/en-us/agent-framework/concepts/agents/middleware/))
3. [ ] Build a first sequential, multi-stage Agent Framework workflow with explicit stage contracts and failure visibility ([Workflows Explained](https://www.youtube.com/watch?v=2BB9-kWb1Tc), [First Sample](https://www.youtube.com/watch?v=KaEefBTKBeE), [Sequential](https://www.youtube.com/watch?v=nPhpIciKfFs), [Current workflow concepts](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/))

## Tasks

### Task 1: Build a Recoverable AI Workflow

**Goal:** Process a longer-running AI job without tying its lifetime to one web request.

**Deliverable:** Background job, Agent Framework workflow, middleware, persisted status, retry behavior, and operational runbook.

**Requirements:**

- Define at least three workflow stages with explicit inputs and outputs.
- Persist workflow or agent state so an interrupted or completed run can be inspected or resumed after a restart.
- Store user preferences or memory that the workflow or agent uses in later runs.
- Make retries safe for the selected operation.
- Support cancellation or a documented stop mechanism.
- Add middleware for logging plus one policy or human-approval concern.

**Acceptance criteria:**

- [ ] The job can be observed from queued through completed or failed states.
- [ ] A second run reflects state or memory persisted by an earlier run.
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
- Session, state, and memory persistence evidence.
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
- `DOTNET-AI-04`
- `DOTNET-AI-08`

## Navigation

[Course Index](README.md) | [Previous Step](step-09.md) | [Next Step](step-11.md)
