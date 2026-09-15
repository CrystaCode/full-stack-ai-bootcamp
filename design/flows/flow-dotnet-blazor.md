## Overview
In this flow, we will explore frontend web application development using **Blazor**. You will learn component-based UI engineering, data binding, state management, routing, forms validation, JavaScript interop across current hosting and render modes, and evidence-based production architecture choices. Bit Platform is included as one optional case study, not as the source of truth for Blazor architecture.

Following steps help you to master these topics:
  - Blazor Hosting and Render Modes
  - Component Architecture & Data Binding
  - Layouts, Templating & RenderFragments
  - SPA Routing & Navigation
  - Forms & Input Validation
  - JavaScript Interop & Dependency Injection
  - Production and Cross-Platform Architecture Options

## Resources
- **Primary Web Reference**:
  - [Blazor University](https://blazor-university.com/)
  - [Microsoft Learn: Blazor Documentation](https://learn.microsoft.com/en-us/aspnet/core/blazor/?view=aspnetcore-10.0)
- **Optional & Secondary Resources**:
  - [Bit Platform Documentation](https://bitplatform.dev/)
  - [Web Development with Blazor – Packt Publishing](https://www.packtpub.com/en-us/product/web-development-with-blazor-9781806112883)
  - [Blazor Deep Dive in .NET 10 – YouTube](https://www.youtube.com/watch?v=holzuW1o6cs)

## Steps
The steps below outline the complete learning path structured directly around the Blazor University modules as primary resources, with optional secondary video, documentation, and framework resources:

1. [ ] Explain current Blazor hosting and render modes and record a product-specific choice ([Overview](https://blazor-university.com/overview/), [Historical Hosting Models](https://blazor-university.com/overview/blazor-hosting-models), [Current Hosting Models](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0), [Current Render Modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0), [Blazor Deep Dive in .NET 10](https://www.youtube.com/watch?v=holzuW1o6cs))
2. [ ] Creating Blazor Projects and Pages ([Creating a New Project](https://blazor-university.com/overview/creating-a-new-project), [Creating a Page](https://blazor-university.com/overview/creating-a-page))
3. [ ] Layouts and Nested Layouts ([Creating a Blazor Layout](https://blazor-university.com/layouts/creating-a-blazor-layout), [Nested Layouts](https://blazor-university.com/layouts/nested-layouts))
4. [ ] Component Basics and Data Binding ([Creating a Component](https://blazor-university.com/components/creating-a-component), [One-Way Binding](https://blazor-university.com/components/one-way-binding), [Two-Way Binding](https://blazor-university.com/components/two-way-binding))
5. [ ] Handle and test component and DOM events, including keyboard interaction paths ([Component Events](https://blazor-university.com/components/component-events), [Browser DOM Events](https://blazor-university.com/components/component-events/browser-dom-events), [bUnit Event Tests](https://bunit.dev/docs/interaction/trigger-event-handlers.html), [WAI Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/))
6. [ ] Cascading Values and Attributes ([Cascading Values](https://blazor-university.com/components/cascading-values), [Capturing Unexpected Parameters](https://blazor-university.com/components/capturing-unexpected-parameters))
7. [ ] Component Lifecycles and Multi-Threaded Rendering ([Component Lifecycles](https://blazor-university.com/components/component-lifecycles), [Multi-Threaded Rendering](https://blazor-university.com/components/multi-threaded-rendering))
8. [ ] Render Trees and Performance Optimization ([Render Trees](https://blazor-university.com/components/render-trees), [Optimizing Using @key](https://blazor-university.com/components/render-trees/optimising-using-key))
9. [ ] Templating Components with RenderFragments ([RenderFragments](https://blazor-university.com/templating-components-with-renderfragements/), [Generic Components with @typeparam](https://blazor-university.com/templating-components-with-renderfragements/using-typeparam-to-create-generic-components))
10. [ ] Routing and Route Parameters ([Defining Routes](https://blazor-university.com/routing/defining-routes), [Route Parameters](https://blazor-university.com/routing/route-parameters))
11. [ ] Implement app navigation and event handling across current navigation modes ([Navigating via HTML](https://blazor-university.com/routing/navigating-our-app-via-html), [Navigating via Code](https://blazor-university.com/routing/navigating-our-app-via-code), [Detecting Navigation Events](https://blazor-university.com/routing/detecting-navigation-events), [Current Navigation Guidance](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/navigation?view=aspnetcore-10.0))
12. [ ] Forms and Data Editing ([Forms](https://blazor-university.com/forms/), [Editing Form Data](https://blazor-university.com/forms/editing-form-data))
13. [ ] Apply standard and custom validation with accessible feedback ([Validation](https://blazor-university.com/forms/validation), [Writing Custom Validation](https://blazor-university.com/forms/writing-custom-validation), [Current Validation Guidance](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/validation?view=aspnetcore-10.0), [Accessible Error Notifications](https://www.w3.org/WAI/tutorials/forms/notifications/))
14. [ ] Manage modified and validation state through public `EditContext` APIs and protect unsaved changes ([EditContext Concepts](https://blazor-university.com/forms/editcontext-fieldidentifiers-and-fieldstate), [`EditContext` API](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.forms.editcontext?view=aspnetcore-10.0), [Current Blazor Validation](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/validation?view=aspnetcore-10.0), [Navigation and `NavigationLock`](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/navigation?view=aspnetcore-10.0))
15. [ ] Call .NET safely from JavaScript and dispose references correctly ([Calling .NET from JavaScript](https://blazor-university.com/javascript-interop/calling-dotnet-from-javascript), [Current Guidance](https://learn.microsoft.com/en-us/aspnet/core/blazor/javascript-interoperability/call-dotnet-from-javascript?view=aspnetcore-10.0))
16. [ ] Call JavaScript from .NET and handle `JSException` and disconnected-circuit failures ([Calling JavaScript from .NET](https://blazor-university.com/javascript-interop/calling-javascript-from-dotnet), [Call JavaScript from .NET](https://learn.microsoft.com/en-us/aspnet/core/blazor/javascript-interoperability/call-javascript-from-dotnet?view=aspnetcore-10.0), [Disconnected-Circuit Guidance](https://learn.microsoft.com/en-us/aspnet/core/blazor/javascript-interoperability/?view=aspnetcore-10.0))
17. [ ] Inject dependencies into Blazor components without coupling UI code to infrastructure ([Injecting Dependencies](https://blazor-university.com/dependency-injection/injecting-dependencies-into-blazor-components), [Current Guidance](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/dependency-injection?view=aspnetcore-10.0))
18. [ ] Select and test component scopes and service lifetimes across render modes ([Component Scoped Dependencies](https://blazor-university.com/dependency-injection/component-scoped-dependencies), [Dependency Lifetimes and Scopes](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes), [Current Guidance](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/dependency-injection?view=aspnetcore-10.0))
19. [ ] (Optional in this flow) Evaluate production hosting, render, Hybrid, and framework options against product requirements ([Hosting Models](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-10.0), [Render Modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0), [Blazor Hybrid](https://learn.microsoft.com/en-us/aspnet/core/blazor/hybrid/?view=aspnetcore-10.0), [Bit Platform Case Study](https://bitplatform.dev/))
