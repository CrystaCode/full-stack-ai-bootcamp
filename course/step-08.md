# Step 08: Forms, Observability, and the First AI Feature

Add trustworthy data entry, structured diagnostics, and the first provider-neutral AI capability while communicating the product through a verified presentation.

## Outcomes

- Create and rehearse a source-grounded presentation.
- Use GitHub Copilot in VS Code while reviewing every accepted change.
- Diagnose application behavior with structured logging.
- Build Blazor forms with custom validation and explicit form state.
- Add a provider-neutral generative AI service to a .NET application.

## Study Items

### General AI

1. [ ] Create a presentation from verified sources with an audience goal, story outline, accessible visuals, speaker notes, fact-checking, and rehearsal ([Gemini Notebook Integration](https://www.youtube.com/watch?v=Y-LTxr1bv9M), [Presentations with Microsoft 365 Copilot](https://www.youtube.com/watch?v=ioV4kREDrso))
2. [ ] Use GitHub Copilot in VS Code for explanation, design, debugging, refactoring, tests, documentation, and review while verifying suggested changes ([Getting Started with GitHub Copilot](https://www.youtube.com/watch?v=n0NlxUyA7FI))

### ASP.NET Core

1. [ ] Use structured logging to monitor requests, correlate operations, and diagnose an application failure ([Book: Chapter 26](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Structured Logging](https://www.youtube.com/watch?v=MHJ0BHfWhRw))

### Blazor

1. [ ] Build forms that edit application data through Blazor input components ([Forms](https://blazor-university.com/forms/), [Editing Form Data](https://blazor-university.com/forms/editing-form-data))
2. [ ] Apply data annotations and custom validation with clear accessible feedback ([Validation](https://blazor-university.com/forms/validation), [Custom Validation](https://blazor-university.com/forms/writing-custom-validation))
3. [ ] Use `EditContext`, field identifiers, and field state to manage validation and unsaved changes ([EditContext and Field State](https://blazor-university.com/forms/editcontext-fieldidentifiers-and-fieldstate))

### .NET AI

1. [ ] Identify Microsoft Extensions AI abstractions and implement a first AI-backed .NET feature ([Building AI Apps in .NET](https://www.youtube.com/watch?v=4B3ppx2U8bE))
2. [ ] Add generative AI through provider-neutral services and configuration rather than provider-specific application logic ([Adding GenAI to .NET Apps](https://www.youtube.com/watch?v=sgrsopf-fzo))

## Tasks

### Task 1: Present the Product Story

**Goal:** Explain the product problem, evidence, current solution, risks, and next milestone to a defined audience.

**Deliverable:** A concise slide deck, speaker notes, source list, fact-check record, accessibility check, and rehearsal notes.

**Requirements:**

- Use verified material already created during the course.
- Keep one main message per slide and provide accessible alternatives for important visuals.
- Rehearse and revise for the intended time limit.

**Acceptance criteria:**

- [ ] Claims are traceable to listed sources or project evidence.
- [ ] Slides support rather than duplicate the spoken explanation.
- [ ] Rehearsal notes identify and resolve at least two clarity problems.

### Task 2: Build a Validated and Observable Editing Flow

**Goal:** Make data changes safe for users and diagnosable for developers.

**Deliverable:** Blazor create or edit form, custom validation, unsaved-change feedback, structured server logs, and a diagnosed failure note.

**Requirements:**

- Show field-level and summary validation without losing user input.
- Track modified state through `EditContext`.
- Add correlation or operation context to relevant logs.
- Use Copilot for one bounded change and record prompts, accepted edits, rejected suggestions, and verification.

**Acceptance criteria:**

- [ ] Invalid data cannot be persisted.
- [ ] Unsaved changes are visible before navigation.
- [ ] Logs identify the request or operation without exposing secrets or sensitive form data.
- [ ] The Copilot log shows human review and successful checks.

### Task 3: Add the First AI Capability

**Goal:** Integrate a bounded generative feature without coupling the application to one provider.

**Deliverable:** An injected AI service, configuration, API endpoint or application service, reviewed output, and non-AI fallback.

**Requirements:**

- Use Microsoft Extensions AI abstractions.
- Keep credentials outside source control.
- Constrain the feature to a clear input and output purpose.
- Validate and review output before it changes persisted or user-visible data.

**Acceptance criteria:**

- [ ] Provider-specific code is isolated from product logic.
- [ ] Missing configuration produces a clear failure or documented fallback.
- [ ] Inputs and outputs are logged safely without secrets.
- [ ] The feature has at least three recorded evaluation cases.

## Submission

- Presentation package and rehearsal notes.
- Form validation and logging evidence.
- Copilot work log and reviewed diff.
- AI feature evaluation cases and configuration instructions.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-15`
- `AI-16`
- `API-14`
- `BLAZOR-12`
- `BLAZOR-13`
- `BLAZOR-14`
- `DOTNET-AI-01`
- `DOTNET-AI-02`

## Navigation

[Course Index](README.md) | [Previous Step](step-07.md) | [Next Step](step-09.md)
