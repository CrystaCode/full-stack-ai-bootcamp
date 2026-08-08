# Step 05: Persistent and Responsive Applications

Move from temporary behavior to a documented, persistent, responsive product while applying bounded AI loops and richer component interactions.

## Outcomes

- Design an AI loop with evaluation, limits, stop conditions, and human approval.
- Document an API and persist its data with EF Core and SQL.
- Verify responsive behavior across defined viewport sizes.
- Build Blazor components that communicate through events, cascading values, and extensible attributes.

## Study Items

### General AI

1. [ ] Design and test a bounded AI loop with planning, action, observation, evaluation, revision, iteration limits, stop conditions, and human approval ([Agent-First Development](https://www.youtube.com/watch?v=uu4sf8z9n8c))

### ASP.NET Core

1. [ ] Generate, inspect, and improve OpenAPI documentation for the application endpoints ([Book: Chapter 11](https://www.manning.com/books/asp-net-core-in-action-third-edition), [OpenAPI in .NET](https://www.youtube.com/watch?v=0qtwYT4n2CM))
2. [ ] Model relational data, use EF Core migrations, and explain the SQL operations behind persistent CRUD behavior ([Book: Chapter 12](https://www.manning.com/books/asp-net-core-in-action-third-edition), [EF Core @ 1:34:00](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=5640s), [SQL Tutorial](https://www.w3schools.com/sql/))

### Frontend

1. [ ] Apply fluid sizing, media queries, responsive layout changes, and mobile-first checks to the product UI ([Responsive Web Design](https://www.youtube.com/watch?v=zF6VSky4SIc))

### Blazor

1. [ ] Handle component events and browser DOM events while keeping behavior testable and accessible ([Component Events](https://blazor-university.com/components/component-events), [Browser DOM Events](https://blazor-university.com/components/component-events/browser-dom-events))
2. [ ] Use cascading values for shared UI context and capture unmatched attributes for extensible components ([Cascading Values](https://blazor-university.com/components/cascading-values), [Capturing Unexpected Parameters](https://blazor-university.com/components/capturing-unexpected-parameters))

## Tasks

### Task 1: Specify and Test a Bounded AI Loop

**Goal:** Define a safe iterative workflow for improving product content or data.

**Deliverable:** `docs/ai/bounded-loop.md` and a run log for a writer, critic, and reviser workflow.

**Requirements:**

- Define inputs, evaluation rubric, maximum iterations, stop conditions, and human approval points.
- Run one successful case and one case that stops because a limit or quality rule is reached.
- Record every iteration without hiding failed outputs.

**Acceptance criteria:**

- [ ] The loop cannot continue indefinitely.
- [ ] A human approves any result selected for product use.
- [ ] The run log demonstrates both success and controlled stopping.

### Task 2: Build the Persistent Responsive Feature

**Goal:** Replace in-memory behavior with a usable database-backed vertical slice.

**Deliverable:** EF Core model and migration, documented CRUD API, and responsive Blazor list and details components.

**Requirements:**

- Persist the primary product resource in a relational database.
- Expose and review the OpenAPI document.
- Use events for user actions and a cascading value for shared display context.
- Verify the UI at small, medium, and large viewport widths.

**Acceptance criteria:**

- [ ] Data remains after the application restarts.
- [ ] A clean database can be created using committed migrations.
- [ ] OpenAPI describes the implemented success and error responses.
- [ ] The UI has no horizontal page overflow at the tested widths.
- [ ] Reusable components accept standard HTML attributes where appropriate.

## Submission

- AI loop specification and run log.
- Migration files and database setup instructions.
- OpenAPI document or screenshot.
- Responsive screenshots at three viewport widths.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-12`
- `API-09`
- `API-10`
- `WEB-05`
- `BLAZOR-05`
- `BLAZOR-06`

## Navigation

[Course Index](README.md) | [Previous Step](step-04.md) | [Next Step](step-06.md)
