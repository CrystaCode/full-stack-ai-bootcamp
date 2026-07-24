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
The steps below outline the complete learning path structured directly around the primary resources, with optional secondary video, documentation, and framework resources:

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

7. **Video Timestamps**:
   - Include exact timestamp parameters (`&t=...s`) in YouTube URLs and display readable timestamp tags (`@ MM:SS` or `@ HH:MM:SS`) in link text.
   - *Example*: `[YouTube Crash Course @ 00:00](https://www.youtube.com/watch?v=holzuW1o6cs)`
