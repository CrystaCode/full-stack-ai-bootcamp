# Step 09: Agent-Assisted Integration

Use bounded agent assistance and persistent repository context to integrate remote services, browser capabilities, and richer C# AI patterns without surrendering review or control.

## Outcomes

- Scope and verify an agent-mode feature from issue through tested diff.
- Improve AI-assisted development with persistent repository instructions.
- Integrate a remote API behind an application model.
- Implement JavaScript interoperability in both directions.
- Configure and evaluate Microsoft Extensions AI patterns in the application.

## Study Items

### General AI

1. [ ] Build a bounded feature with agent mode by defining an issue, completion criteria, command boundaries, diff review, and verification checks ([Agent-First Development](https://www.youtube.com/watch?v=uu4sf8z9n8c), [Build an App with Agent Mode](https://www.youtube.com/watch?v=hmfldW7dmgw))
2. [ ] Add persistent repository context for architecture, conventions, commands, safety, and completion, then compare agent work with and without it ([Context Engineering with Copilot](https://www.youtube.com/watch?v=0jEzUhU8bLc))

### ASP.NET Core

1. [ ] Build a typed remote API client, handle transient and permanent failures, and map transport objects into application models ([Book: Chapter 33](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Mapperly Documentation](https://mapperly.riok.app/))

### Blazor

1. [ ] Expose a safe .NET method to JavaScript and manage references and lifetimes correctly ([Calling .NET from JavaScript](https://blazor-university.com/javascript-interop/calling-dotnet-from-javascript))
2. [ ] Invoke browser APIs from .NET and handle asynchronous JavaScript failures ([Calling JavaScript from .NET](https://blazor-university.com/javascript-interop/calling-javascript-from-dotnet))

### .NET AI

1. [ ] Apply Microsoft Extensions AI abstractions, options, middleware, and telemetry patterns from the official documentation ([Microsoft Extensions AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai))
2. [ ] Implement and compare practical C# AI patterns relevant to the portfolio feature ([AI in C#](https://www.youtube.com/playlist?list=PLhGl0l5La4sYXjYOBv7h9l7x6qNuW34Cx))

## Tasks

### Task 1: Establish the Agent Development Contract

**Goal:** Make agent-assisted changes bounded, repeatable, and reviewable.

**Deliverable:** Persistent repository instructions, a bounded feature issue, agent plan, command log, reviewed diff, and verification results.

**Requirements:**

- Document architecture, conventions, build and test commands, safety rules, and definition of done.
- Run a small comparison with and without repository context.
- Reject or revise at least one unsuitable suggestion when present, or explain why all suggestions were acceptable.

**Acceptance criteria:**

- [ ] The issue states scope, exclusions, and objective completion checks.
- [ ] Repository instructions contain no secrets or machine-specific credentials.
- [ ] The final diff contains only intended changes and passes its checks.
- [ ] The comparison identifies the observable effect of persistent context.

### Task 2: Build the Integration Feature

**Goal:** Combine external data, AI processing, and a browser capability through explicit boundaries.

**Deliverable:** Typed remote client, mapping layer, Microsoft Extensions AI service, and a Blazor interaction that demonstrates both JavaScript-to-.NET and .NET-to-JavaScript calls.

**Requirements:**

- Map remote DTOs into internal models without leaking transport concerns into the UI.
- Handle timeout, invalid response, and unavailable-provider cases.
- Add one justified AI transformation or analysis of external data.
- Use JavaScript interop for a browser-only capability such as clipboard, focus, storage, or download.

**Acceptance criteria:**

- [ ] Remote failures produce controlled application behavior.
- [ ] Product code depends on application abstractions rather than provider SDK types.
- [ ] JavaScript references are released where required and errors are handled.
- [ ] AI output is evaluated against at least three representative cases.

## Submission

- Repository instructions and agent-development evidence.
- Remote API contract and mapping notes.
- Failure-case and AI-evaluation results.
- Short recording or screenshots of the interop behavior.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-17`
- `AI-18`
- `API-17`
- `BLAZOR-15`
- `BLAZOR-16`
- `DOTNET-AI-03`
- `DOTNET-AI-04`

## Navigation

[Course Index](README.md) | [Previous Step](step-08.md) | [Next Step](step-10.md)
