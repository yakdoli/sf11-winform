---
title: addscriptmanagertoanapplication4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addscriptmanagertoanapplication4.md
created_at: 2025-07-03
---






#### Add ScriptManager to an Application {#add-scriptmanager-to-an-application style="tab-stops: 0pt"}

The **ScriptManager()** method can be added after all the components on the page. Generally, you can use this method at the end of the master page.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                   |
|                                                                                                                                                                      |
| [\<][body][\>]  |
|                                                                                                                                                                      |
| [...]                                                                                                                            |
|                                                                                                                                                                      |
| [    [\<%]{ Html.MobSyncfusion().ScriptManager().Render(); } [%\>]]      |
|                                                                                                                                                                      |
| [\</][body][\>] |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| **[\[Razor\]]**                                                                                                                  |
|                                                                                                                                                                      |
| [\<][body][\>]  |
|                                                                                                                                                                      |
| [...]                                                                                                                            |
|                                                                                                                                                                      |
| [\@{]                                                                                                        |
|                                                                                                                                                                      |
| [        Html.MobSyncfusion().ScriptManager().Render();]                                                                         |
|                                                                                                                                                                      |
| [    [}]]                                                                                            |
|                                                                                                                                                                      |
| [\</][body][\>] |
|                                                                                                                                                                      |
| []                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Methods


  **[Method]**        **[Description]**                                                                                                                                       **[Parameters]**   **[Type ]**                                                                       **[Return Type ]**
  ------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  [ScriptManager()]   [Used to register the Syncfusion.Mvc component's script files. The files in ScriptManager resources are set to be combined, minified, and compressed]   [NA]               **[Server-side]**[]   [MvcResourceRenderer]


 

 

Customization

**Minify---**To enable or disable the minify feature, use the **Minify()** method. Minify is enabled by default.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                              |
|                                                                                                                                                                                                 |
| [\<][body][\>]                             |
|                                                                                                                                                                                                 |
| [...]                                                                                                                                                       |
|                                                                                                                                                                                                 |
| [    [\<%]{]                                                                                                                    |
|                                                                                                                                                                                                 |
| [          Html.MobSyncfusion().ScriptManager()]                                                                                                            |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [                 .Minify([false])]                                                                                                    |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [                 .Render();]                                                                                                                               |
|                                                                                                                                                                                                 |
| [      } [%\>]]                                                                                                                 |
|                                                                                                                                                                                                 |
| [\</][body][\>]                            |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| **[\[Razor\]]**                                                                                                                                             |
|                                                                                                                                                                                                 |
| [\<][body][\>]                             |
|                                                                                                                                                                                                 |
| [...]                                                                                                                                                       |
|                                                                                                                                                                                                 |
| [    [\@{]]                                                                                                                     |
|                                                                                                                                                                                                 |
| [        Html.MobSyncfusion().ScriptManager()]                                                                                                              |
|                                                                                                                                                                                                 |
| [            ]                                                                                                                                              |
|                                                                                                                                                                                                 |
| [            .Minify([false])]                                                                                                         |
|                                                                                                                                                                                                 |
| [            ]                                                                                                                                              |
|                                                                                                                                                                                                 |
| [            .Render();]                                                                                                                                    |
|                                                                                                                                                                                                 |
| [    [}]]                                                                                                                       |
|                                                                                                                                                                                                 |
| [\</][body][\>][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

