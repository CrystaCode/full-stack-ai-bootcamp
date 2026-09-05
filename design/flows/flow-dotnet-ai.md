## Overview
In this flow, we will explore how to integrate AI capabilities into .NET applications. You will learn the Microsoft Extensions AI abstractions, how to build agents and workflows in C#, how agents call tools and other agents, and how to connect those agents to generative user interfaces.

Following steps help you to master these topics:
  - Microsoft Extensions AI
  - Microsoft Agent Framework
  - Tools, MCP, and Skills
  - Multi-agent systems and workflows
  - Generative UI with AG-UI and A2UI

## Resources
- **Primary Video Courses**:
  - [Building AI Apps in .NET Just Got 10x Easier](https://www.youtube.com/watch?v=4B3ppx2U8bE)
  - [Easily Add GenAI to .NET Apps using MEAI](https://www.youtube.com/watch?v=sgrsopf-fzo)
  - [AI in C#](https://www.youtube.com/playlist?list=PLhGl0l5La4sYXjYOBv7h9l7x6qNuW34Cx)
  - [Demystifying Microsoft Agent Framework Middleware](https://www.youtube.com/watch?v=v7VLSZqAssU)
  - [Microsoft Agent Framework WorkFlows Explained](https://www.youtube.com/watch?v=2BB9-kWb1Tc)
  - [Generative UI with AG-UI & A2UI](https://www.youtube.com/watch?v=aYe12ryuB4s)
- **Documentation**:
  - [Microsoft Extensions AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai)
  - [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-csharp)
  - [Agent Framework releases](https://github.com/microsoft/agent-framework/releases)
  - [Agent tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/)
  - [Agent Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
  - [Workflow concepts](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/)

## Steps
The steps below outline the complete learning path, grouped by outcome, with the AI in C# series as the primary Microsoft Agent Framework resource:

1. [ ] Add GenAI to a .NET app with Microsoft Extensions AI ([Building AI Apps in .NET](https://www.youtube.com/watch?v=4B3ppx2U8bE), [Easily Add GenAI](https://www.youtube.com/watch?v=sgrsopf-fzo), [Documentation](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai), [Use `IChatClient`](https://learn.microsoft.com/en-us/dotnet/ai/ichatclient))
2. [ ] Understand the Microsoft Agent Framework landscape ([Introduction](https://www.youtube.com/watch?v=9RNF9GsB8PU), [Agent Framework vs Semantic Kernel vs Extensions.AI](https://www.youtube.com/watch?v=6ue9SmEtG9k), [GA Part 1](https://www.youtube.com/watch?v=2ZwxQmT1l7s))
3. [ ] Create a first agent in C# ([Getting Started](https://www.youtube.com/watch?v=HHy0-sXlmUY), [Zero to First OpenAI Agent](https://www.youtube.com/watch?v=CvA69UyqJ7U), [Using other LLMs](https://www.youtube.com/watch?v=GbyEQWwBMFk), [Current C# Quickstart](https://learn.microsoft.com/en-us/agent-framework/get-started/))
4. [ ] Persist state, configure settings and memory, and apply observable middleware ([Agent Sessions](https://www.youtube.com/watch?v=p5AvoMbgPtI), [AIAgent settings](https://www.youtube.com/watch?v=6i1Rs0MkBDQ), [User Memory](https://www.youtube.com/watch?v=AndCk0HeddQ), [Memory Guidance](https://learn.microsoft.com/en-us/agent-framework/get-started/memory), [Middleware](https://www.youtube.com/watch?v=v7VLSZqAssU), [Middleware Concepts](https://learn.microsoft.com/en-us/agent-framework/concepts/agents/middleware/))
5. [ ] Call controlled tools from an agent ([Tool Calling](https://www.youtube.com/watch?v=gJTodKpv8Ik), [Advanced Tool Calling](https://www.youtube.com/watch?v=dCtojrK8bKk), [MCP Tool Calling](https://www.youtube.com/watch?v=Y5IKdt9vdJM), [AIAgent vs ChatClientAgent](https://www.youtube.com/watch?v=pN-WV5FD_-Y), [Current Tools Guidance](https://learn.microsoft.com/en-us/agent-framework/agents/tools/))
6. [ ] Package reusable capabilities with the current Agent Skills provider and distinguish it from earlier Toolkit demonstrations ([Earlier Toolkit Demonstration](https://www.youtube.com/watch?v=_vAr693wM3o), [Skills in C#](https://www.youtube.com/watch?v=KHfJko3msLw), [Current Agent Skills Guidance](https://learn.microsoft.com/en-us/agent-framework/agents/skills))
7. [ ] Coordinate multi-agent systems with validated contracts ([Multi-Agent and Workflows](https://www.youtube.com/watch?v=lIXJovzXNh4), [Structured Output](https://www.youtube.com/watch?v=2YzjRZTZxUo), [Agent as a tool](https://www.youtube.com/watch?v=wL4V78s_wI4))
8. [ ] Build Agent Framework workflows and justify sequential, concurrent, or handoff patterns ([Workflows Explained](https://www.youtube.com/watch?v=2BB9-kWb1Tc), [First Sample](https://www.youtube.com/watch?v=KaEefBTKBeE), [Sequential](https://www.youtube.com/watch?v=nPhpIciKfFs), [Concurrent](https://www.youtube.com/watch?v=qYxGJ-D3Tl0), [Handoff](https://www.youtube.com/watch?v=VInKZ45YKAM), [Current Workflow Concepts](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/))
9. [ ] Explain reasoning effort, overthinking, latency, token cost, and exposed reasoning, then distinguish private reasoning from auditable inputs, outputs, tool calls, results, retries, and traces ([Reasoning Deep Dive Part 1](https://www.youtube.com/watch?v=pD3A3rC_D5Q), [Agent Tracing Overview](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept), [AI-System Observability](https://learn.microsoft.com/en-us/security/zero-trust/sfi/observability-ai-systems))
10. [ ] Build generative UI and use agent protocols ([How to use AG-UI](https://www.youtube.com/watch?v=tDQc6lZUbYc), [Advanced AG-UI](https://www.youtube.com/watch?v=9nEcVoQCkYA), [AG-UI and A2UI](https://www.youtube.com/watch?v=aYe12ryuB4s), [AG-UI Documentation](https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/), [A2A Protocol](https://www.youtube.com/watch?v=g72ks3rY9qQ), [A2A Documentation](https://learn.microsoft.com/en-us/agent-framework/integrations/a2a))
11. [ ] Review the date-pinned current Agent Framework package set, release status, and breaking-change risk ([GA Part 2](https://www.youtube.com/watch?v=UaRB9uC1rTI), [Documentation](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-csharp), [Official Releases](https://github.com/microsoft/agent-framework/releases))
