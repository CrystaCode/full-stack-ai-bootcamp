---
name: flow-designer
description: Create, redesign, update, and format curriculum flow markdown files in bootcamp repositories. Trigger whenever the user asks to create a learning flow, update flow steps, structure a course curriculum, align flow files with reference books or video courses, or format flow-*.md files.
---

# Flow Designer

This skill provides standard guidelines, schemas, and workflows for designing, updating, and formatting curriculum learning flows (e.g. `design/flows/flow-<topic>.md`) for full-stack and developer bootcamps.

## When to Use This Skill

Use this skill when:
- Creating a new flow file under `design/flows/flow-<topic>.md`
- Redesigning or updating existing flow files (e.g. `flow-dotnet-aspnetcore.md`, `flow-dotnet-blazor.md`, `flow-dotnet-ai.md`, `flow-dotnet-ef.md`)
- Structuring a course outline into an actionable checklist of steps with primary and optional resources
- Mapping reference books or web resources to flow steps

---

## Flow File Structure & Formatting Rules

Every flow file MUST adhere to the following Markdown schema and formatting rules:

### 1. File Location & Naming
- Path: `design/flows/flow-<topic>.md` (e.g., `design/flows/flow-dotnet-blazor.md`).
- Keep distinct flow files modular and independent (e.g., backend flow is separate from frontend or AI integration flows).

### 2. Standard Markdown Schema

```markdown
## Overview
In this flow, we will explore [high-level technology goals, e.g., frontend web development using Blazor]. [General architectural overview covering core paradigms like WASM, Server, component engineering, without referencing specific resource names, books, or web providers].

Following steps help you to master these topics:
  - [High-level Topic 1]
  - [High-level Topic 2]
  - [High-level Topic 3]

## Resources
- **Primary Web / Book Reference**:
  - [Primary Resource Name](https://...)
- **Optional & Secondary Resources**:
  - [Documentation / Secondary Resource 1](https://...)
  - [Video Course / Crash Course](https://...)
  - [Framework / Platform Docs](https://...)

## Steps
The checklist below describes modular learning topics and outcomes. It does not prescribe course order unless ordering or prerequisites are explicitly requested:

1. [ ] [Step 1 Title] ([Topic Reference 1](https://...), [Topic Reference 2](https://...))
2. [ ] [Step 2 Title] ([Topic Reference](https://...))
...
N. [ ] (Optional) [Optional Advanced Step Title] ([Resource Link](https://...))
```

---

## Strict Formatting Guidelines

1. **General Conceptual Overview Section**:
   - The `## Overview` paragraph MUST be conceptual and high-level (discussing frameworks, paradigms like SPA/WASM/Minimal APIs/EF Core).
   - **CRITICAL**: DO NOT mention specific resource names, books, or external web providers (e.g. "Andrew Lock's book" or "Blazor University") in the `## Overview` paragraph.

2. **Dedicated Resources Section**:
   - Include a `## Resources` section right BEFORE `## Steps` clearly categorizing **Primary** and **Optional & Secondary Resources**.

3. **No Repetitive Resource Prefixes in Steps**:
   - DO NOT repeat the resource provider name in every step link title (e.g., avoid `[Blazor University: Overview](...)`).
   - Use clean, concise topic names in link titles: `([Overview](https://...), [Hosting Models](https://...))`.

4. **Optional Steps**:
   - Explicitly prefix optional extension steps with `(Optional)` (e.g., `19. [ ] (Optional) Production App Architecture and Cross-Platform UI ([bitplatform Documentation](https://bitplatform.dev/))`).

5. **No Em-Dashes (`—`)**:
   - DO NOT use em-dashes (`—`). Use standard colons (`:`) or parentheses `(...)` instead.
   - *Example*: `Minimal APIs: Modern default for lightweight APIs`

6. **No `Ch *:` Prefixes in Step Titles**:
   - Keep the step title clean. Place chapter citations inside resource link parentheses, not in the step title itself.
   - **Correct**: `1. [ ] Creating a JSON API with Minimal APIs ([Manning Book - Ch 5](https://...))`
   - **Incorrect**: `1. [ ] **Ch 5: Creating a JSON API with Minimal APIs**`

7. **Video Links and Timestamps**:
   - Link a complete YouTube video without a timestamp parameter or timestamp label.
   - Add a timestamp only when the link intentionally targets a specific chapter or segment within a video.
   - For a specific segment, include the exact timestamp parameter (`&t=...s`) in the URL and a readable timestamp tag (`@ MM:SS` or `@ HH:MM:SS`) in the link text.
   - Do not add `@ 00:00` or `&t=0s` to whole-video links.
   - *Complete-video example*: `[YouTube Crash Course](https://www.youtube.com/watch?v=holzuW1o6cs)`
   - *Segment example*: `[Dependency Injection @ 12:35](https://www.youtube.com/watch?v=holzuW1o6cs&t=755s)`

8. **Flow Topics Are Modular by Default**:
   - Treat flow steps as a catalog of competencies, activities, and resources that course designers can select and arrange.
   - Do not state or imply that a topic must be learned before another course or module unless the user explicitly requests an order or a genuine technical dependency requires it.
   - Avoid phrases such as "start with," "learn this first," or "before studying" when no dependency has been established.
