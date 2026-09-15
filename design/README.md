# Design

This folder holds the design materials behind the bootcamp: the curriculum outlines, the resources each topic is built on, and the learning outcomes participants are expected to reach. It answers *what* is taught and *why*; the [course](../course/README.md) folder turns those decisions into the actual lessons and exercises.

## Structure

- **[flows](flows/)**: Completed learning flows, one per track. These are the reviewed documents linked from the curriculum in the [root README](../README.md).
- **[draft](draft/)**: Work in progress. Nothing here is linked from the curriculum yet.

## Flows

A flow is a self-contained learning path for one track. Every flow document follows the same three sections:

- **Overview**: What the track covers, what it deliberately leaves to other flows, and the list of topics it builds toward.
- **Resources**: The primary source the flow is structured around, plus optional and secondary material.
- **Steps**: A checklist of learning outcomes, each linked to the resource that supports it.

Current flows:

- [General AI](flows/flow-ai-general.md): AI literacy for learning, research, content, and development
- [ASP.NET Core](flows/flow-dotnet-aspnetcore.md): server-side web development with C# and .NET
- [Blazor](flows/flow-dotnet-blazor.md): interactive web UI with .NET
- [.NET and AI](flows/flow-dotnet-ai.md): building AI-powered features in C#
- [Frontend](flows/flow-frontend.md): HTML and CSS as the presentation layer

## Conventions

- Write steps as outcomes a participant can demonstrate, not as topics to read about.
- Link at least one resource from every step, so the path from outcome to material is never implicit.
- Prefer a single primary resource per flow and keep the step order aligned with it; secondary links are there for depth, not replacement.
- Move a draft into `flows/` once it is complete, then add it to the curriculum in the [root README](../README.md).
