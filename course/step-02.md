# Step 02: Prompts and Web Requests

Apply deliberate prompting and source verification while learning how requests move through a styled ASP.NET Core application.

## Outcomes

- Construct and evaluate prompts with goals, context, constraints, examples, and output formats.
- Compare browser assistants using the same source and verification method.
- Explain middleware order and implement a small Minimal API.
- Apply CSS selectors and the box model to the product page.

## Study Items

### General AI

1. [ ] Compare two browser assistants on the same article or PDF, including what data is shared and whether answers match the source ([Copilot in Edge](https://support.microsoft.com/en-us/microsoft-copilot/getting-started-with-copilot-in-microsoft-edge), [Gemini in Chrome](https://support.google.com/chrome/answer/16283624?hl=en))
2. [ ] Design prompts with a goal, audience, context, constraints, examples, and output format, then evaluate them against varied inputs ([Prompt Engineering Guide](https://www.youtube.com/watch?v=uDIW34h8cmM))

### ASP.NET Core

1. [ ] Trace a request through the middleware pipeline and explain why middleware order changes behavior ([Book: Chapter 4](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Middleware @ 1:17:45](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=4665s))
2. [ ] Create JSON endpoints with route handlers, status codes, and typed results using Minimal APIs ([Book: Chapter 5](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Minimal APIs @ 36:12](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=2172s))

### Frontend

1. [ ] Apply CSS selectors, inheritance, units, colors, typography, spacing, borders, and the box model ([CSS Tutorial](https://www.w3schools.com/css/default.asp), [CSS Reference](https://cssreference.io/))

## Tasks

### Task 1: Run a Prompt and Assistant Lab

**Goal:** Establish a repeatable method for asking, testing, and verifying AI-assisted work.

**Deliverable:** `docs/prompt-lab.md` containing an assistant comparison and three iterations of a prompt relevant to the product.

**Requirements:**

- Use the same public source and questions with two browser assistants.
- Verify at least three claims directly against the source.
- Test the final prompt with at least three inputs and score it with a rubric.

**Acceptance criteria:**

- [ ] The comparison separates source-supported answers from unsupported claims.
- [ ] Prompt revisions respond to observed failures.
- [ ] The final prompt specifies an audience, constraints, and output format.

### Task 2: Add a Styled Minimal API Slice

**Goal:** Introduce request processing, JSON behavior, and visual styling in the portfolio application.

**Deliverable:** Custom request-logging middleware, in-memory Minimal API endpoints for one product resource, and a styled product page.

**Requirements:**

- Add list, details, and create endpoints for the selected resource.
- Return appropriate success and error status codes.
- Record method, path, status code, and elapsed time in the middleware.
- Add a stylesheet that demonstrates selectors, spacing, typography, borders, and box sizing.

**Acceptance criteria:**

- [ ] Middleware runs in the intended order and produces one trace per request.
- [ ] Endpoints return valid JSON and distinguish missing resources from successful responses.
- [ ] The page remains readable without inline styles.
- [ ] Browser developer tools show the expected content-box or border-box calculations.

## Submission

- `docs/prompt-lab.md`.
- API request examples for success and failure cases.
- Screenshot of the styled page and middleware output.
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
