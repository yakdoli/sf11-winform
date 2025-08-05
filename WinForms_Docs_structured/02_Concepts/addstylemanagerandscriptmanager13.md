---
title: addstylemanagerandscriptmanager13.md
original_path: WinForms_Docs/02_Concepts/addstylemanagerandscriptmanager13.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Add StyleManager and ScriptManager {#add-stylemanager-and-scriptmanager style="tab-stops: 0pt"}

Adding StyleManager

**StyleManager** is a new CSS resource manager that helps in registering CSS files which enables Minification, Compression, Combination of CSS resources for ASP.NET MVC web applications. The files in StyleManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before sending to browser. All are done using a single HTTP request per resource set.

Add the StyleManager extension method in the HEAD tag of the View pages (in most cases, it is reasonable to call it within the Site.Master page). Use Register method to register Grid component.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [    [\@{]]                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [        Html.MobSyncfusion().StyleManager()]                                                                                                                                |
|                                                                                                                                                                                                                  |
| [        .Register(stylesheets =\>]                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [            {]                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [                stylesheets.Add([MobComponentType].] [{ComponentName}] [);] |
|                                                                                                                                                                                                                  |
| [            }).Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| [    [}]]                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Adding ScriptManager

**ScriptManager** is a new script resource manager that helps in registering the JavaScript files. The ScriptManager registers only the Syncfusion.Mvc components script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip and deflate, depending on your browser) before sending to browser.

 

The ScriptManager() method should be placed after all the components on the page. Generally, you can use this method at the end of the master page.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [\<] [body] [\>] [] |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [    [\@{]]                                                                                                                                  |
|                                                                                                                                                                                                              |
| [        Html.MobSyncfusion().ScriptManager()]                                                                                                                           |
|                                                                                                                                                                                                              |
| [            .Render();]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [    [}]]                                                                                                                                    |
|                                                                                                                                                                                                              |
| [\                                                                                                                                                                                                           |
| [\</] [body] [\>] ]                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note : Add this ScriptManager() at the end of body tag. Don't add this in top of body tag.


[] 

[]{#related-topics}

