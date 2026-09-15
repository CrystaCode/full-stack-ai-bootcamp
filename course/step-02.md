# Step 02: Prompts and Web Requests

Apply deliberate prompting and source verification while learning how requests move through a styled ASP.NET Core application.

## Outcomes

- Construct and evaluate prompts with goals, context, constraints, examples, and output formats.
- Compare browser assistants using a technical source assigned in this step and a repeatable verification method.
- Explain middleware order and implement a small Minimal API.
- Apply CSS selectors and the box model to the product page.

## Study Items

### General AI

1. [ ] Open the [Microsoft: Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0) article assigned in this step in two available browser assistants. In fresh conversations, give both assistants the same source-bounded prompt set: summarize the pipeline, explain `Use`, `Run`, and short-circuiting, predict the request and response log order, and conduct a three-question quiz that asks one question at a time and checks each answer against a named article section. Record the page or tab context each assistant can access, verify substantive claims against the article, inspect any source links before relying on them, and correct unsupported answers ([Copilot in Edge](https://support.microsoft.com/en-us/microsoft-copilot/getting-started-with-copilot-in-microsoft-edge), [Gemini in Chrome](https://support.google.com/chrome/answer/16283624?hl=en), [Gemini source links](https://support.google.com/gemini/answer/14143489?co=GENIE.Platform%3DDesktop&hl=en), [Lateral reading](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/))
2. [ ] Design prompts with a goal, audience, context, constraints, examples, and output format, then evaluate them against varied inputs and explicit criteria ([Prompt Engineering Guide](https://www.youtube.com/watch?v=uDIW34h8cmM), [OpenAI prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering), [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices))

### ASP.NET Core

1. [ ] Trace a request through the middleware pipeline and explain why middleware order changes behavior ([Book: Chapter 4](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-4), [Microsoft: Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0))
2. [ ] Create JSON endpoints with route handlers, status codes, and typed results using Minimal APIs ([Book: Chapter 5](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-5), [Minimal APIs @ 36:12](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=2172s), [Minimal API responses and `TypedResults`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/responses?view=aspnetcore-10.0))

### Frontend

1. [ ] Apply CSS selectors, inheritance, units, colors, typography, spacing, borders, and the box model ([CSS Tutorial](https://www.w3schools.com/css/default.asp), [CSS Reference](https://cssreference.io/))

## Tasks

### Task 1: Build a Source-Grounded Prompt and Assistant Lab

**Goal:** Turn the step's technical readings into a verified learning artifact and a reusable source-to-implementation prompt.

**Deliverable:** `docs/prompt-lab.md` containing the source record, shared prompt set, browser-context record, assistant comparison, claim-verification table, corrected middleware trace, and three iterations of a source-to-implementation prompt with rubric results.

**Requirements:**

- Open [Microsoft: Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0) in both browser assistants. If the article or a named assistant is unavailable, record the limitation and use an instructor-approved equivalent with the same article, or another non-video reading linked in this step.
- Use a clean browser window containing only public course pages, and disable unrelated browsing context when the product allows it. Record the assistant, browser, access date, source URL, context setting, shared pages, and how the source was provided: current tab, selected tabs, URL, uploaded file, or pasted text.
- Start a fresh conversation in each assistant and use the same prompt set and questions from the study item.
- For each assistant, verify at least three substantive claims against a named heading or anchor in the article. Mark each claim `supported`, `contradicted`, or `not found`, then correct or reject the latter two.
- Record whether either assistant displays source or related links. Open every link used as evidence and confirm that it supports the associated claim. Record `none` when an assistant provides no links, and do not treat a displayed link as proof by itself.
- Apply the linked lateral-reading method once: leave the target page and check the publisher, currency, and authority of the middleware article using another trustworthy source. Keep this source-quality check separate from the page-grounded claim verdicts.
- Create a reusable prompt that turns a technical reading into an implementation checklist. Specify its goal, developer audience, source context, constraints, output structure, one worked example, evidence rule, and instruction to say `not found in the source` rather than guess.
- Run prompt version 1 on [Microsoft: Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0), score it, and revise one observed failure. Run version 2 on [Minimal API responses and `TypedResults`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/responses?view=aspnetcore-10.0), score it, and revise again. Regression-test version 3 on both articles and one non-video Frontend reading linked in this step. Use the same source-fidelity, completeness, format-compliance, and actionability rubric for every run.

**Acceptance criteria:**

- [ ] The report identifies the source by title, URL, and access date and shows that both assistants received the same prompt set and questions in fresh conversations.
- [ ] The context record states the context setting, shared pages, and source-delivery method for each assistant without exposing unrelated private browsing data.
- [ ] The verification table includes at least three claims per assistant, a source heading or anchor and verdict for each claim, and a correction or rejection for every contradicted or unlocated claim.
- [ ] Every assistant-provided link used as evidence was opened and checked, and the separate lateral-reading record evaluates the publisher, currency, and authority of the target article.
- [ ] The corrected middleware trace contains only source-supported claims and predicts the before-and-after logging order used in Task 2.
- [ ] The final reusable prompt specifies the audience, constraints, output structure, worked example, evidence rule, and `not found` behavior.
- [ ] The report shows the version 1 and version 2 failure-driven revisions and version 3 regression results for both ASP.NET Core articles and one linked Frontend reading, all scored with the same rubric.

### Task 2: Add a Styled Minimal API Slice

**Goal:** Introduce request processing, JSON behavior, and visual styling in the portfolio application.

**Deliverable:** Custom request-logging middleware with a predicted-versus-observed trace, in-memory Minimal API endpoints for one product resource, and a styled product page.

**Requirements:**

- Add list, details, and create endpoints for the selected resource.
- Return appropriate success and error status codes.
- Record method, path, status code, and elapsed time in the middleware.
- Before coding the middleware, use the verified trace from Task 1 to predict its before-and-after log order, then compare that prediction with the actual output for one request.
- Add a stylesheet that demonstrates selectors, spacing, typography, borders, and box sizing.

**Acceptance criteria:**

- [ ] Middleware produces one trace per request, and the observed before-and-after order is compared with the source-grounded prediction in `docs/prompt-lab.md`.
- [ ] Endpoints return valid JSON and distinguish missing resources from successful responses.
- [ ] The page remains readable without inline styles.
- [ ] Browser developer tools show the expected content-box or border-box calculations.

## Submission

- `docs/prompt-lab.md` with redacted response captures or transcripts and shared-context evidence for both assistant runs.
- API request examples for success and failure cases.
- Screenshots of the styled page, box-model inspection, and middleware output showing the predicted and observed order.
- Link to the step commit.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-04`
- `AI-09`
- `API-03`
- `API-04`
- `WEB-02`

## Navigation

[Course Index](README.md) | [Previous Step](step-01.md) | [Next Step](step-03.md)
