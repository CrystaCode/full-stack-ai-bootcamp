# Step 06: Content, Controllers, and Rendering

Create verified communication artifacts and a maintainable content-management slice while examining controller filters and Blazor rendering behavior.

## Outcomes

- Transform one verified source brief for several audiences without inventing claims.
- Implement controller-based endpoints and reusable cross-cutting filters.
- Explain Blazor lifecycle events and safe rendering synchronization.
- Diagnose unnecessary rendering and preserve component identity with keys.

## Study Items

### General AI

1. [ ] Transform a verified content brief into an article, email, and social post while preserving facts, adapting voice, and recording human edits ([Gemini Practical Course](https://www.youtube.com/watch?v=-_FizlRlfYs))

### ASP.NET Core

1. [ ] Compare controller-based APIs with Minimal APIs and implement a cohesive controller endpoint set ([Book: Chapter 20](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Controller APIs @ 10:00](https://www.youtube.com/watch?v=38GNKtclDdE&t=600s))
2. [ ] Apply filters for reusable cross-cutting behavior and explain their execution order ([Book: Chapters 21 and 22](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Minimal API Filters](https://www.youtube.com/watch?v=2XoZOPrxegw))

### Blazor

1. [ ] Observe component lifecycle methods and update rendered state safely when work completes asynchronously ([Component Lifecycles](https://blazor-university.com/components/component-lifecycles), [Multi-Threaded Rendering](https://blazor-university.com/components/multi-threaded-rendering))
2. [ ] Explain render-tree comparison and use `@key` where stable component identity matters ([Render Trees](https://blazor-university.com/components/render-trees), [Optimizing with @key](https://blazor-university.com/components/render-trees/optimising-using-key))

## Tasks

### Task 1: Produce a Verified Content Pack

**Goal:** Communicate the product accurately to three audiences.

**Deliverable:** A source brief, article, email, social post, fact-check table, and human edit record under `docs/content/`.

**Requirements:**

- Base every version on the same verified brief.
- Define the audience, action, tone, and length for each format.
- Flag or remove claims that the source material does not support.

**Acceptance criteria:**

- [ ] All factual claims trace back to the brief or its sources.
- [ ] Each format has a visibly different audience-appropriate structure.
- [ ] The edit record explains at least three human corrections.

### Task 2: Build an Efficient Content Management Slice

**Goal:** Manage content artifacts through controller endpoints and a rendering-aware Blazor UI.

**Deliverable:** Controller-based content endpoints, a filter for one cross-cutting concern, and a Blazor content list with lifecycle and render observations.

**Requirements:**

- Implement list, details, create, and update controller actions.
- Add a filter for validation, timing, auditing, or another justified concern.
- Record relevant lifecycle calls during initial load and refresh.
- Demonstrate a reordered list with and without `@key`.

**Acceptance criteria:**

- [ ] Controller responses follow the existing API error conventions.
- [ ] The filter behavior is visible and does not duplicate controller logic.
- [ ] UI updates occur without cross-thread rendering errors.
- [ ] The render comparison explains when `@key` preserves identity.

## Submission

- Verified content pack and edit record.
- API request examples for the controller endpoints.
- Filter and lifecycle evidence.
- Render behavior comparison.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-13`
- `API-11`
- `API-12`
- `BLAZOR-07`
- `BLAZOR-08`

## Navigation

[Course Index](README.md) | [Previous Step](step-05.md) | [Next Step](step-07.md)
