---
title: addingscriptmanagertoanapplication1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingscriptmanagertoanapplication1.md
created_at: 2025-07-03
---






#### Adding ScriptManager to an Application {#adding-scriptmanager-to-an-application style="tab-stops: 0pt"}

 

The **ScriptManager()** method can be added after all the components on the page. Generally, you can use this method at the end of the master page.

***[]*** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                        |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [\<][body][\>][] |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [...]                                                                                                                                                                 |
|                                                                                                                                                                                                           |
| [...]                                                                                                                                                                 |
|                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().ScriptManager()[%\>]\                     |
| [\</][body][\>]]                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customization

[] 

**Minify** - To enable or disable the minify feature, use **Minify()** method. Minify is enabled by default.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                        |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [\<][body][\>][] |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [...]                                                                                                                                                                 |
|                                                                                                                                                                                                           |
| [...]                                                                                                                                                                 |
|                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().ScriptManager()]                  |
|                                                                                                                                                                                                           |
| [.Minify([true])]                                                                                                                                |
|                                                                                                                                                                                                           |
| [%\>][\                                                                                                                                           |
| [\</][body][\>]]                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

 

[]{#related-topics}

