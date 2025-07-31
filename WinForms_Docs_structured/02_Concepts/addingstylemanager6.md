---
title: addingstylemanager6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\addingstylemanager6.md
created_at: 2025-07-03
---






#### Adding StyleManager {#adding-stylemanager style="tab-stops: 0pt"}

**StyleManager** is a new CSS resource manager that helps in registering CSS files which enables Minification, Compression, Combination of CSS resources for ASP.NET MVC web applications. The files in StyleManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before sending to browser. All are done using a single HTTP request per resource set.[]

[ ]Add the StyleManager extension method in the HEAD tag of the View pages (in most cases, it is reasonable to call it within the Site.Master page). Use Register method to register Grid component.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                     |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                                   |
| [   ][    [@(]Html.Syncfusion().StyleManager()]       |
|                                                                                                                                                                                                   |
| [        .Theme([Skins].Almond)[// Specify Theme to all components]]                               |
|                                                                                                                                                                                                   |
| [        .Register(styleSheet =\>]                                                                                                               |
|                                                                                                                                                                                                   |
| [            {]                                                                                                                                  |
|                                                                                                                                                                                                   |
| [                styleSheet.Add([ComponentType].Scheduele).Theme([Skins].Blend).DontOverride();] |
|                                                                                                                                                                                                   |
| [                styleSheet.Add([\"\~/Content/Site.css\"]);]                                                             |
|                                                                                                                                                                                                   |
| [            })[)]]                                                                                                  |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

