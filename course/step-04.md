# Step 04: Context and Component Architecture

Create reusable context for reliable AI work while introducing application configuration, dependency injection, component composition, and deliberate visual interaction.

## Outcomes

- Build a prompt-based tool with structured output and human review.
- Measure the effect of a reusable context pack.
- Configure services and options through ASP.NET Core dependency injection.
- Build reusable Blazor components and layouts with accessible visual feedback.

## Study Items

### General AI

1. [ ] Build a prompt-based application that summarizes, infers, transforms, or expands text with structured output and edge-case review ([Prompt Engineering for Developers](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/dfbds/introduction))
2. [ ] Create a reusable context pack and compare results with and without project goals, sources, examples, constraints, vocabulary, and completion criteria ([Context Engineering with Copilot](https://www.youtube.com/watch?v=0jEzUhU8bLc))

### ASP.NET Core

1. [ ] Explain dependency injection, register services, select lifetimes, and consume dependencies without service location ([Book: Chapters 8 and 9](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Dependency Injection @ 2:26:52](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=8812s))
2. [ ] Load environment-aware configuration and bind validated options for application behavior ([Book: Chapter 10](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Configuration @ 2:17:46](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=8266s))

### Frontend

1. [ ] Apply positioning, transitions, and animations with attention to focus, reduced motion, and content readability ([CSS Reference](https://cssreference.io/))

### Blazor

1. [ ] Create application and nested feature layouts that separate shared navigation from page content ([Creating a Blazor Layout](https://blazor-university.com/layouts/creating-a-blazor-layout), [Nested Layouts](https://blazor-university.com/layouts/nested-layouts))
2. [ ] Build reusable components and demonstrate one-way and two-way data binding ([Creating a Component](https://blazor-university.com/components/creating-a-component), [One-Way Binding](https://blazor-university.com/components/one-way-binding), [Two-Way Binding](https://blazor-university.com/components/two-way-binding))

## Tasks

### Task 1: Build and Evaluate a Prompt Tool

**Goal:** Turn one repeated product workflow into a bounded, reviewable prompt tool.

**Deliverable:** Prompt template, context pack, test inputs, structured outputs, rubric results, and human-review checklist under `docs/ai/`.

**Requirements:**

- Require a predictable output structure.
- Test normal, empty, ambiguous, and adversarial inputs.
- Compare at least three results with and without the context pack.

**Acceptance criteria:**

- [ ] Output can be parsed or reviewed consistently.
- [ ] The context comparison identifies measurable improvements and remaining failures.
- [ ] Human approval is required before generated material enters the application.

### Task 2: Create the Configurable Component Shell

**Goal:** Give the portfolio application reusable UI and backend boundaries.

**Deliverable:** Configured application service, validated options, nested Blazor layout, and at least two reusable bound components.

**Requirements:**

- Place product logic behind an injected interface.
- Bind configuration to a typed options class and fail clearly when required values are absent.
- Add shared and feature layouts.
- Add a focused transition or animation with a reduced-motion fallback.

**Acceptance criteria:**

- [ ] Service registration uses an intentional lifetime documented in `docs/architecture.md`.
- [ ] Development and production configuration can differ without code changes.
- [ ] Components receive data through parameters or binding rather than global mutable state.
- [ ] Keyboard focus and reduced-motion behavior remain usable.

## Submission

- Prompt tool and context pack under `docs/ai/`.
- Architecture update describing dependency and configuration decisions.
- Screenshots or recording of the component layouts and visual interaction.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-10`
- `AI-11`
- `API-07`
- `API-08`
- `WEB-04`
- `BLAZOR-03`
- `BLAZOR-04`

## Navigation

[Course Index](README.md) | [Previous Step](step-03.md) | [Next Step](step-05.md)
