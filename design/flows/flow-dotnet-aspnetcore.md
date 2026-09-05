## Overview
In this flow, we will explore backend development with modern **ASP.NET Core**. You will learn core web architecture, middleware pipeline request processing, data persistence with Entity Framework Core, authentication, security, and cloud deployment.

Following steps help you to master these topics:
  - Web Architecture & Middleware Pipeline
  - Minimal APIs & Web API Controllers
  - EF Core & Relational Data Access
  - Authentication, Authorization & Security
  - Deployment, DevOps & Cloud Services

## Resources
- **Primary Book Reference**: [ASP.NET Core in Action, 3rd Edition – Andrew Lock](https://www.manning.com/books/asp-net-core-in-action-third-edition)
- **Primary Video Courses**:
  - [ASP.NET Core Full Course For Beginners (.NET 10) – Julio Casal](https://www.youtube.com/watch?v=YbRe4iIVYJk)
  - [Build REST APIs in .NET 9 – freeCodeCamp](https://www.youtube.com/watch?v=38GNKtclDdE)
  - [Intro to .NET Aspire – Tim Corey](https://www.youtube.com/watch?v=x2KAfsFydIo)
  - [How to use routing in Minimal APIs – Round The Code](https://www.youtube.com/watch?v=KZYvpNgGBZI)
  - [OpenAPI Made Easy in .NET 9 – Milan Jovanović](https://www.youtube.com/watch?v=0qtwYT4n2CM)
  - [Minimal API filters: Run code before the endpoint handler – Round The Code](https://www.youtube.com/watch?v=2XoZOPrxegw)
  - [Adding JWT Authentication & Authorization in ASP.NET Core – Nick Chapsas](https://www.youtube.com/watch?v=mgeuh8k3I4g)
  - [The Logging Everyone Should Be Using in .NET – Nick Chapsas](https://www.youtube.com/watch?v=MHJ0BHfWhRw)
  - [ASP.NET Core Deep-Dive in .NET 11 (8 Hours) – Frank Liu](https://www.youtube.com/watch?v=E-RPvJnMBLU)
- **Documentation & Tutorials**:
  - [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
  - [FluentValidation Documentation](https://docs.fluentvalidation.net/)
  - [Mapperly Documentation](https://mapperly.riok.app/)
  - [Microsoft Learn: Host and deploy ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/?view=aspnetcore-10.0)
  - [Hangfire Documentation](https://docs.hangfire.io/en/latest/)
  - [Polly Documentation](https://www.pollydocs.org/)
  - [Playwright .NET Documentation](https://playwright.dev/dotnet/docs/intro)

## Steps
The steps below outline the complete learning path structured directly around the book chapters as primary resources, with secondary video courses and documentation linked for each topic:

1. [ ] Getting Started with ASP.NET Core ([Manning Book - Ch 1](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-1), [Julio Casal @ 00:00](https://www.youtube.com/watch?v=YbRe4iIVYJk))
2. [ ] Understanding ASP.NET Core & Your First Application ([Manning Book - Ch 2](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-2), [Manning Book - Ch 3](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-3), [Julio Casal @ 06:40](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=400s), [freeCodeCamp @ 02:02](https://www.youtube.com/watch?v=38GNKtclDdE&t=122s))
3. [ ] Handling Requests with the Middleware Pipeline ([Manning Book - Ch 4](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-4), [Microsoft: Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0))
4. [ ] Creating a JSON API with Minimal APIs ([Manning Book - Ch 5](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-5), [Julio Casal @ 36:12](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=2172s), [Minimal API Responses and `TypedResults`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/responses?view=aspnetcore-10.0))
5. [ ] Mapping URLs to Endpoints Using Routing ([Manning Book - Ch 5](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-5), [Manning Book - Ch 6](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-6), [Round The Code – Routing in Minimal APIs](https://www.youtube.com/watch?v=KZYvpNgGBZI))
6. [ ] Model Binding and Validation in Minimal APIs ([Manning Book - Ch 7](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-7), [Julio Casal @ 1:25:07](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=5107s), [FluentValidation Docs](https://docs.fluentvalidation.net/), [Microsoft: API Error Handling](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling-api?view=aspnetcore-10.0))
7. [ ] Dependency Injection in ASP.NET Core ([Manning Book - Ch 8](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-8), [Manning Book - Ch 9](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-9), [Julio Casal @ 2:26:52](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=8812s))
8. [ ] Configuring an ASP.NET Core Application ([Manning Book - Ch 10](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-10), [Julio Casal @ 2:17:46](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=8266s), [Microsoft: Options Validation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options?view=aspnetcore-10.0#validateonstart))
9. [ ] Documenting APIs with OpenAPI / Swagger ([Manning Book - Ch 11](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-11), [Milan Jovanović – OpenAPI Made Easy in .NET 9](https://www.youtube.com/watch?v=0qtwYT4n2CM), [Include OpenAPI Metadata](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/include-metadata?view=aspnetcore-10.0))
10. [ ] Saving Data with Entity Framework Core & SQL ([Manning Book - Ch 12](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-12), [Julio Casal @ 1:34:00](https://www.youtube.com/watch?v=YbRe4iIVYJk&t=5640s), [freeCodeCamp @ 32:42](https://www.youtube.com/watch?v=38GNKtclDdE&t=1962s), [W3Schools SQL Tutorial](https://www.w3schools.com/sql/))
11. [ ] Creating an HTTP API Using Web API Controllers and Comparing API Approaches ([Manning Book - Ch 20](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-20), [ASP.NET Core API Approaches](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/apis?view=aspnetcore-10.0), [freeCodeCamp @ 10:00](https://www.youtube.com/watch?v=38GNKtclDdE&t=600s))
12. [ ] Filter Pipelines and Custom Filters ([Manning Book - Ch 21](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-21), [Manning Book - Ch 22](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-22), [Round The Code – Minimal API filters](https://www.youtube.com/watch?v=2XoZOPrxegw))
13. [ ] Authentication and Authorization for APIs ([Manning Book - Ch 23](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-23), [Manning Book - Ch 24](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-24), [Manning Book - Ch 25](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-25), [Authorization Overview](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction?view=aspnetcore-10.0), [Roles](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/roles?view=aspnetcore-10.0), [Policies](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-10.0), [Nick Chapsas – JWT Authentication & Authorization](https://www.youtube.com/watch?v=mgeuh8k3I4g))
14. [ ] Monitoring and Troubleshooting Errors with Logging ([Manning Book - Ch 26](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-26), [Nick Chapsas – The Logging Everyone Should Be Using in .NET](https://www.youtube.com/watch?v=MHJ0BHfWhRw), [Microsoft: ASP.NET Core Logging](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-10.0))
15. [ ] Publishing and Deploying Applications ([Manning Book - Ch 27](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-27), [`dotnet publish`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish), [Microsoft: Host and Deploy ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/?view=aspnetcore-10.0), [Azure Deployment Slots Example](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots))
16. [ ] HTTPS and Security Hardening ([Manning Book - Ch 28](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-28), [Manning Book - Ch 29](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-29), [HTTPS and HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0), [Application Secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-10.0), [Review Vulnerable Packages](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-list), [OWASP HTTP Security Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html))
17. [ ] Calling Remote APIs and Object Mapping ([Manning Book - Ch 33](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-33), [`IHttpClientFactory`](https://learn.microsoft.com/en-us/dotnet/core/extensions/httpclient-factory), [HTTP Resilience](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience), [Mapperly Docs](https://mapperly.riok.app/))
18. [ ] Building Background Tasks and Services ([Manning Book - Ch 34](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-34), [Hosted Services](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-10.0), [Hangfire Docs](https://docs.hangfire.io/en/latest/))
19. [ ] Unit, Integration, API, and Browser Testing ([Manning Book - Ch 35](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-35), [Manning Book - Ch 36](https://livebook.manning.com/book/asp-net-core-in-action-third-edition/chapter-36), [ASP.NET Core Integration Tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-10.0), [Playwright .NET Docs](https://playwright.dev/dotnet/docs/intro), [Playwright API Testing](https://playwright.dev/dotnet/docs/api-testing))
20. [ ] Cloud-Native Integration: .NET Aspire Orchestration ([Tim Corey Video](https://www.youtube.com/watch?v=x2KAfsFydIo), [Add Aspire to an Existing App](https://learn.microsoft.com/en-us/dotnet/aspire/get-started/add-aspire-existing-app), [Dashboard Overview](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/overview), [Explore the Dashboard](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/explore))
