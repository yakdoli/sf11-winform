---
title: addingstylemanager1.md
original_path: WinForms_Docs/02_Concepts/addingstylemanager1.md
created_at: 2025-08-05
---






#### Adding StyleManager {#adding-stylemanager style="tab-stops: 0pt"}

 

**StyleManager** is a new CSS resource manager that helps in registering CSS files which enables the minification, compression, and combination of CSS resources for ASP.NET MVC Web applications. The files in StyleManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before being sent to the browser. All are done using a single HTTP request per resource set.[]

[] 

Add the **StyleManager** extension method in the HEAD element of the view pages (in most cases, it is reasonable to call it within the Site.Master page). Use the **Register** method to register the Grid component.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                   |
|                                                                                                                                                                      |
| [\<%][=][Html.Syncfusion().StyleManager()\                  |
|         .Register(styleSheet =\> \                                                                                                                                   |
|             {\                                                                                                                                                       |
|                 styleSheet.Add([ComponentType].Grid);][] |
|                                                                                                                                                                      |
| [            })  [%\>]][]                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

