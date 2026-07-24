---
name: flow-designer
description: Create, redesign, update, and format curriculum flow markdown files in bootcamp repositories. Trigger whenever the user asks to create a learning flow, update flow steps, structure a course curriculum, align flow files with reference books or video courses, or format flow-*.md files.
---

# Flow Designer

This skill provides standard guidelines, schemas, and workflows for designing, updating, and formatting curriculum learning flows (e.g. `design/flows/flow-<topic>.md`) for full-stack and developer bootcamps.

## When to Use This Skill

Use this skill when:
- Creating a new flow file under `design/flows/flow-<topic>.md`
- Redesigning or updating existing flow files (e.g. `flow-dotnet-aspnetcore.md`, `flow-dotnet-ai.md`, `flow-dotnet-ef.md`)
- Structuring a course outline into an actionable checklist of steps with primary and secondary resources
- Mapping reference books (such as *ASP.NET Core in Action*) or video courses (such as Julio Casal, freeCodeCamp) to flow steps

---

## Flow File Structure & Formatting Rules

Every flow file MUST adhere to the following Markdown schema and formatting rules:

### 1. File Location & Naming
- Path: `design/flows/flow-<topic>.md` (e.g., `design/flows/flow-dotnet-aspnetcore.md`).
- Keep distinct flow files modular and independent (e.g., backend flow is separate from AI integration flow).

### 2. Standard Markdown Schema

```markdown
## Overview
In this flow, we will explore [brief summary of what the flow covers and its primary goals].

Following steps help you to master these topics:
  - Part 1: [Module / Topic 1]
  - Part 2: [Module / Topic 2]
  - Part 3: [Module / Topic 3]

## Steps
The steps below outline the complete learning path structured directly around the primary resources, with secondary video courses and documentation linked for each topic:

1. [ ] [Step 1 Title] ([Primary Resource - Ch/Sec], [Secondary Resource @ MM:SS])
2. [ ] [Step 2 Title] ([Primary Resource - Ch/Sec], [Secondary Resource @ MM:SS])
```

---

## Strict Formatting Guidelines

1. **No Em-Dashes (`—`)**:
   - DO NOT use em-dashes (`—`). Use colons (`:`) or parentheses `(...)` instead.
   - *Example*: `Minimal APIs: Modern default for lightweight APIs`

2. **No `Ch *:` Prefixes in Step Titles**:
   - Keep the step title clean. Place chapter citations inside the resource link parentheses, not in the step title itself.
   - **Correct**: `1. [ ] Creating a JSON API with Minimal APIs ([Manning Book - Ch 5](https://www.manning.com/books/asp-net-core-in-action-third-edition))`
   - **Incorrect**: `1. [ ] **Ch 5: Creating a JSON API with Minimal APIs**`

3. **Resource Ordering (Primary First, Secondary Second)**:
   - Always place the **Primary Book Chapter / Book Reference FIRST**, followed by **Secondary Resources** (Video courses, timestamps, official documentation).
   - *Example*: `([Manning Book - Ch 4](https://www.manning.com/books/asp-net-core-in-action-third-edition), [Julio Casal @ 1:17:45](https://...))`

4. **Video Timestamps**:
   - Include exact timestamp parameters (`&t=...s`) in YouTube URLs and display readable timestamp tags (`@ MM:SS` or `@ HH:MM:SS`) in the link text.
   - *Example*: `[Julio Casal @ 36:12](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=2172s)`

---

