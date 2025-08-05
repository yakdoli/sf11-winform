---
title: addstylemanagerandscriptmanager9.md
original_path: WinForms_Docs/02_Concepts/addstylemanagerandscriptmanager9.md
created_at: 2025-08-05
---








  









###  StyleManager and ScriptManager {#add-stylemanager-and-scriptmanager style="tab-stops: 0pt"}

 

Adding StyleManager

**StyleManager** is a new CSS resource manager that helps in registering CSS files which enables minification, compression, and combination of CSS resources for ASP.NET MVC Web applications. The files in StyleManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before being sent to the browser. All are done using a single HTTP request per resource set.

Add the StyleManager extension method in the HEAD tag of the **view** pages (in most cases, it is reasonable to call it within the Site.Master page). Use the **Register** method to register grid component.

 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                |
|                                                                                                                                    |
| [    [\@{]]                                                        |
|                                                                                                                                    |
| [        Html.MobSyncfusion().StyleManager()]                                                  |
|                                                                                                                                    |
| [        .Register(stylesheets =\>]                                                            |
|                                                                                                                                    |
| [            {]                                                                                |
|                                                                                                                                    |
| [                stylesheets.Add([MobComponentType].{ComponentName});] |
|                                                                                                                                    |
| [            }).Render();]                                                                     |
|                                                                                                                                    |
| [    [}]][]                               |
+------------------------------------------------------------------------------------------------------------------------------------+

 

Adding ScriptManager

**ScriptManager** is a new script resource manager that helps in registering the JavaScript files. The ScriptManager registers only the **Syncfusion.Mvc** component script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip and deflate, depending on your browser) before being sent to the browser.

The **ScriptManager()** method should be placed after all the components on the page. Generally, you can use this method at the end of the master page.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                 |
|                                                                                                                                                                     |
| [\<][body][\>] |
|                                                                                                                                                                     |
|                                                                                                                                                                     |
|                                                                                                                                                                     |
| [...]                                                                                                                           |
|                                                                                                                                                                     |
| [...]                                                                                                                           |
|                                                                                                                                                                     |
| [    [\@{]]                                                                                         |
|                                                                                                                                                                     |
| [        Html.MobSyncfusion().ScriptManager()]                                                                                  |
|                                                                                                                                                                     |
| [            .Render();]                                                                                                        |
|                                                                                                                                                                     |
| [    [}]]                                                                                           |
|                                                                                                                                                                     |
| [\                                                                                                                                                                  |
| [\</][body][\>]][]                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[{border="0"}][Note: Add this **ScriptManager()** at the end of the **body** tag. Do not add this in the top of the **body** tag.]

[]{#related-topics}

