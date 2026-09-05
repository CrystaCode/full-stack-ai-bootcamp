# Step 03: Research and Application Navigation

Use source-grounded AI research to define a better product feature, then introduce routing, validation, layout, and the first Blazor user experience.

## Outcomes

- Select appropriate AI learning and research tools and verify their evidence.
- Design API routes and reject invalid input predictably.
- Build a Flexbox or Grid layout for application content.
- Explain Blazor hosting choices and create navigable pages.

## Study Items

### General AI

1. [ ] Use Gemini text, file, image, model-selection, temporary-chat, Canvas, Guided Learning, and Deep Research features, then record which feature fits each learning or productivity goal ([Gemini Practical Course](https://www.youtube.com/watch?v=-_FizlRlfYs))
2. [ ] Conduct a guided Study Mode session with prior-knowledge questions, learner attempts, feedback, and a mastery check, then compare it with direct-answer chat using the same learning goal and criteria ([Introducing Study Mode](https://www.youtube.com/watch?v=XDYilxy1dn8), [Study Mode Guide](https://help.openai.com/en/articles/11780217-study-mode), [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices))
3. [ ] Build a source-grounded notebook, configure its sources and instructions, use cited chat, and verify important claims against the original material ([Gemini Notebook Integration](https://www.youtube.com/watch?v=Y-LTxr1bv9M), [Product Guide](https://support.google.com/gemininotebook/answer/16164461?hl=en))
4. [ ] Run the same question through two deep-research tools, then compare report scope, source selection and quality, citation traceability, and claims that fail source checks ([Gemini Practical Course](https://www.youtube.com/watch?v=-_FizlRlfYs), [Gemini Deep Research guide](https://support.google.com/gemini/answer/15719111?hl=en), [ChatGPT Deep Research](https://www.youtube.com/watch?v=YkCDVn3_wiw), [ChatGPT Deep Research guide](https://help.openai.com/en/articles/10500283-deep-research), [Lateral reading](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/), [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices))

### ASP.NET Core

1. [ ] Design literal, parameterized, constrained, and grouped routes for a coherent API ([Book: Chapter 5](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-5), [Book: Chapter 6](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-6), [Minimal API Routing](https://www.youtube.com/watch?v=KZYvpNgGBZI))
2. [ ] Apply model binding and validation, and design useful validation error responses ([Book: Chapter 7](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-7), [Validation @ 1:25:07](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=5107s), [Validation Documentation](https://docs.fluentvalidation.net/), [Microsoft: API error handling](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0))

### Frontend

1. [ ] Construct application layouts with Flexbox and Grid and explain why each layout model fits its selected region ([Flexbox Reference](https://cssreference.io/flexbox/), [Grid Reference](https://cssreference.io/css-grid/), [MDN: Grid compared with other layout methods](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods))

### Blazor

1. [ ] Compare current Blazor hosting and render modes and record a decision for the portfolio application ([Microsoft: Hosting Models](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0), [Microsoft: Render Modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0), [Blazor University: Hosting Models](https://blazor-university.com/overview/blazor-hosting-models), [Blazor Deep Dive in .NET 10](https://www.youtube.com/watch?v=holzuW1o6cs))
2. [ ] Create a Blazor project and add the first feature page ([Creating a New Project](https://blazor-university.com/overview/creating-a-new-project), [Creating a Page](https://blazor-university.com/overview/creating-a-page))

## Tasks

### Task 1: Produce a Source-Grounded Feature Brief

**Goal:** Use research evidence to choose and scope the next product feature.

**Deliverable:** `docs/feature-research.md`, a Gemini feature-selection log, a guided-versus-direct Study Mode comparison, and a shareable notebook link or export.

**Requirements:**

- Use a source-grounded notebook with organized sources and explicit notebook instructions, plus two deep-research tools.
- Verify at least five important claims against original sources.
- Include one Study Mode session with prior-knowledge questions, learner attempts, feedback, and a mastery check.
- Record which Gemini features were used, which were rejected, and why each selected interaction fit the learning goal.
- If a named tool is unavailable, document the limitation and use an instructor-approved equivalent with the same evidence requirements.

**Acceptance criteria:**

- [ ] Every central claim has a traceable source.
- [ ] The recommendation distinguishes evidence from inference.
- [ ] The brief records at least one limitation or unresolved question.
- [ ] The notebook exposes citations that resolve to its original sources.
- [ ] The Study Mode comparison distinguishes guided learning from direct-answer behavior.

### Task 2: Build a Navigable and Validated Product Shell

**Goal:** Connect a structured UI to a predictable API surface.

**Deliverable:** A Blazor application shell, responsive dashboard layout, and routed API endpoints with validation.

**Requirements:**

- Add list and details routes with constrained identifiers.
- Validate create or update input and return useful errors.
- Create at least two Blazor pages and navigation between them.
- Use Flexbox or Grid for the dashboard and document the hosting decision.

**Acceptance criteria:**

- [ ] Valid, invalid, and missing-resource requests have distinct responses.
- [ ] Direct navigation to each Blazor page works.
- [ ] The layout uses Flexbox or Grid without table-based positioning.
- [ ] `docs/architecture.md` records the Blazor hosting decision and tradeoffs.

## Submission

- `docs/feature-research.md`, Gemini feature-selection log, Study Mode comparison, notebook link or export, and the hosting decision.
- API request examples covering routing and validation.
- Screenshots of the Blazor pages at two viewport widths.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-05`
- `AI-06`
- `AI-07`
- `AI-08`
- `API-05`
- `API-06`
- `WEB-03`
- `BLAZOR-01`
- `BLAZOR-02`

## Navigation

[Course Index](README.md) | [Previous Step](step-02.md) | [Next Step](step-04.md)
