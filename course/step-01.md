# Step 01: Foundations

Establish a shared understanding of generative AI while creating the first backend and frontend artifacts for the portfolio application.

## Outcomes

- Explain in plain language how generative AI and large language models generate outputs, including important limitations.
- Recognize hallucinations, verify important model outputs, and explain why final decisions remain a human responsibility.
- Run a first ASP.NET Core application and explain its basic structure.
- Create a semantic HTML page that communicates the product idea.

## Study Items

### General AI

1. [ ] Explain generative AI, common model types, capabilities, limitations, useful applications, and decisions that should remain human-controlled ([Generative AI in a Nutshell](https://www.youtube.com/watch?v=2IK3DFHRFfw))
2. [ ] Explain in plain language how a large language model generates a response and why that response can be wrong ([Large Language Models](https://www.youtube.com/watch?v=osKyvYJ3PRM), [LLM Deep Dive](https://www.youtube.com/watch?v=7xTGNNLPyMI))
3. [ ] Explain how hallucinations can produce fluent but false or unsupported answers, verify a model answer against a known fact or inspectable source, and explain why a person remains responsible for using the result ([Hallucinations @ 01:20:44](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=4844s), [Testing Known Answers @ 01:26:09](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=5169s), [Human Responsibility @ 03:09:21](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11361s))

### ASP.NET Core

1. [ ] Identify the purpose, project structure, and development workflow of ASP.NET Core ([Book: Chapter 1](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-1), [.NET 10 course](https://www.youtube.com/watch?v=YbRe4iIVYJk))
2. [ ] Explain application startup and create a first running web application ([Book: Chapter 2](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-2), [Book: Chapter 3](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-3), [First application @ 06:40](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=400s), [ASP.NET Core setup @ 02:02](https://www.youtube.com/watch?v=38GNKtclDdE&t=122s))

### Frontend

1. [ ] Demonstrate HTML document structure, semantic elements, headings, links, lists, forms, and accessible content organization ([HTML Tutorial](https://www.w3schools.com/html/default.asp))

## Tasks

### Task 1: Create an AI Foundations Pack

**Goal:** Document the AI concepts, verification habits, and human responsibility that will guide the project.

**Deliverable:** `docs/ai-foundations.md` containing a short plain-language LLM explanation, five possible AI applications, three decisions that remain human-controlled, and a hallucination and verification test table.

**Requirements:**

- Run two model checks whose answers can be verified: one normal factual question and one question with a false premise or nonexistent detail.
- For each check, record the prompt, response, source or known answer, unsupported or invented details, correction, and final human decision.
- Explain briefly how an LLM generates text and why its answer may be wrong.

**Acceptance criteria:**

- [ ] The explanation describes next-token prediction in plain language and states that a plausible response may still be wrong.
- [ ] The report lists five possible applications and three decisions that remain human-controlled.
- [ ] The test table contains both required checks.
- [ ] Each checked claim has evidence and a verdict of verified, contradicted, or not verifiable.
- [ ] Unsupported or invented details are identified as possible hallucinations and are corrected or rejected.
- [ ] Each check records who owns the final decision and whether the model output is used, corrected, or rejected.

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
