# Step 07: Identity, Navigation, and Visual Communication

Protect product capabilities, create reusable routed UI, and generate a reviewed visual asset that supports a real communication goal.

## Outcomes

- Generate image variations, compare them with an explicit rubric, and document the final human choice.
- Authenticate users and authorize protected API behavior.
- Build generic templated components.
- Implement parameterized routes and deliberate navigation behavior.

## Study Items

### General AI

1. [ ] Generate image variations for a communication goal, inspect visible strengths and errors, compare the variations with an explicit rubric, and record the final human choice ([Image Creation Examples](https://www.youtube.com/watch?v=EUEsvyEMRzY), [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices))

### ASP.NET Core

1. [ ] Implement authentication and authorization, distinguish roles from policies, and protect API operations consistently ([Book: Chapter 23](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-23), [Chapter 24](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-24), [Chapter 25](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-25), [Authorization overview](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction?view=aspnetcore-10.0), [Role-based authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/roles?view=aspnetcore-10.0), [Policy-based authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-10.0), [JWT Authentication and Authorization](https://www.youtube.com/watch?v=mgeuh8k3I4g))

### Blazor

1. [ ] Build a reusable templated component with `RenderFragment` and a generic type parameter ([RenderFragments](https://blazor-university.com/templating-components-with-renderfragements/), [Generic Components](https://blazor-university.com/templating-components-with-renderfragements/using-typeparam-to-create-generic-components))
2. [ ] Define routes and route parameters for list, details, and editing experiences ([Defining Routes](https://blazor-university.com/routing/defining-routes), [Route Parameters](https://blazor-university.com/routing/route-parameters))
3. [ ] Use HTML and programmatic navigation and respond intentionally to navigation events across current Blazor navigation modes ([HTML Navigation](https://blazor-university.com/routing/navigating-our-app-via-html), [Code Navigation](https://blazor-university.com/routing/navigating-our-app-via-code), [Navigation Events](https://blazor-university.com/routing/detecting-navigation-events), [Current Blazor navigation](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/navigation?view=aspnetcore-10.0))

## Tasks

### Task 1: Create a Reviewed Product Visual

**Goal:** Produce a useful visual asset without losing human editorial control.

**Deliverable:** Image brief, at least three generated variations, selected final asset, evaluation rubric, and selection rationale under `docs/visuals/`.

**Requirements:**

- Define the communication goal, audience, placement, and dimensions.
- Inspect each variation for visible strengths and errors, then compare all variations with the same rubric.
- Record why a person selected the final asset over the alternatives.

**Acceptance criteria:**

- [ ] The selected asset fulfills the documented communication goal.
- [ ] Visible errors and unsupported claims have been removed.
- [ ] The final selection is supported by the documented evaluation rubric and human review.

### Task 2: Build a Secured Navigable Experience

**Goal:** Give authenticated users access to appropriate product actions through reusable UI.

**Deliverable:** Authentication flow, protected API operations, parameterized Blazor pages, and a generic list or table component.

**Requirements:**

- Protect at least one write operation and one role or policy-specific operation.
- Handle unauthorized and forbidden results distinctly.
- Use the generic component for at least two data types or views.
- Add details and edit routes and protect unsaved work during navigation.

**Acceptance criteria:**

- [ ] Anonymous, authenticated, and insufficiently authorized requests behave differently.
- [ ] Direct URLs with valid and invalid parameters are handled safely.
- [ ] The generic component contains no product-specific type dependency.
- [ ] Navigation behavior is keyboard accessible and does not silently discard edits.

## Submission

- Visual brief, variants, final image, and evaluation rubric.
- Authentication and authorization test evidence.
- Screenshots of routed UI states.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-14`
- `API-13`
- `BLAZOR-09`
- `BLAZOR-10`
- `BLAZOR-11`

## Navigation

[Course Index](README.md) | [Previous Step](step-06.md) | [Next Step](step-08.md)
