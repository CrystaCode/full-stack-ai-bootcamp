# Step 01: Foundations

Establish a shared understanding of generative AI while creating the first backend and frontend artifacts for the portfolio application.

## Outcomes

- Explain how generative AI and large language models work, including important limitations.
- Identify privacy, bias, copyright, verification, and human-accountability concerns.
- Run a first ASP.NET Core application and explain its basic structure.
- Create a semantic HTML page that communicates the product idea.

## Study Items

### General AI

1. [ ] Explain generative AI, common model types, capabilities, limitations, useful applications, and decisions that should remain human-controlled ([Generative AI in a Nutshell](https://www.youtube.com/watch?v=2IK3DFHRFfw))
2. [ ] Diagram training data, tokens, next-token prediction, parameters, inference, fine-tuning, and output limitations ([Large Language Models](https://www.youtube.com/watch?v=osKyvYJ3PRM), [LLM Deep Dive](https://www.youtube.com/watch?v=7xTGNNLPyMI))
3. [ ] Evaluate factual errors, ambiguous instructions, sensitive data, bias, copyright, disclosure, and accountability through small model tests ([LLM Deep Dive](https://www.youtube.com/watch?v=7xTGNNLPyMI))

### ASP.NET Core

1. [ ] Identify the purpose, project structure, and development workflow of ASP.NET Core ([Book: Chapter 1](https://www.manning.com/books/asp-net-core-in-action-third-edition), [.NET 10 course](https://www.youtube.com/watch?v=YbRe4iIVYJk))
2. [ ] Explain application startup and create a first running web application ([Book: Chapters 2 and 3](https://www.manning.com/books/asp-net-core-in-action-third-edition), [First application @ 06:40](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=400s))

### Frontend

1. [ ] Demonstrate HTML document structure, semantic elements, headings, links, lists, forms, and accessible content organization ([HTML Tutorial](https://www.w3schools.com/html/default.asp))

## Tasks

### Task 1: Create an AI Foundations Pack

**Goal:** Document the AI concepts and responsible-use boundaries that will guide the project.

**Deliverable:** `docs/ai-foundations.md` containing a one-page LLM diagram, five possible AI applications, three human-controlled decisions, and a responsible-use test table.

**Requirements:**

- Test at least one factual, one ambiguous, and one sensitive-data scenario.
- Record the prompt, observed result, risk, and required human response.
- Explain the LLM diagram in your own words.

**Acceptance criteria:**

- [ ] The diagram includes tokens, prediction, parameters, training, and inference.
- [ ] The report distinguishes useful assistance from human accountability.
- [ ] No real private or sensitive information appears in the tests.

### Task 2: Start the Portfolio Application

**Goal:** Create the first vertical slice of the product.

**Deliverable:** A repository containing a running ASP.NET Core application, an information endpoint, and a semantic HTML product page.

**Requirements:**

- Choose a product domain and state its user, problem, and proposed value.
- Add an endpoint that returns the product name, purpose, and current version as JSON.
- Add a semantic HTML page with header, navigation, main content, feature list, and footer.
- Add run instructions to the project README.

**Acceptance criteria:**

- [ ] The application starts without unhandled errors.
- [ ] The information endpoint returns valid JSON.
- [ ] The HTML uses semantic elements and has a logical heading order.
- [ ] Another learner can follow the README to run the application.

## Submission

- Link to the portfolio repository and the commit for this step.
- `docs/ai-foundations.md`.
- Screenshot or response capture for the information endpoint and HTML page.
- Short note describing the chosen product domain.

## Completion Criteria

- [ ] All required study items are complete.
- [ ] All required tasks meet their acceptance criteria.
- [ ] The submission contains the required evidence.

## Source Outcomes

- `AI-01`
- `AI-02`
- `AI-03`
- `API-01`
- `API-02`
- `WEB-01`

## Navigation

[Course Index](README.md) | [Next Step](step-02.md)
