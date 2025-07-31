---
title: addstylemanagerandscriptmanager11.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\addstylemanagerandscriptmanager11.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Add StyleManager and ScriptManager {#add-stylemanager-and-scriptmanager style="TEXT-INDENT: -36pt; MARGIN-LEFT: 36pt; tab-stops: 36.0pt"}

Adding ScriptManager

**ScriptManager** is a new script resource manager that helps in registering the JavaScript files. The ScriptManager registers only the Syncfusion.Mvc components script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip and deflate, depending on your browser) before sending to browser.

 

ScriptManager() extension has improved performance over the **RegisterStaticResource**() method. Hence we always suggest this method in registering the scripts.

 

The ScriptManager() method should be placed after all the components on the page. Generally, you can use this method at the end of the master page.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                           |
|                                                                                                                                                                                                              |
| [\<] [body] [\>] [] |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [...]                                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [    [\<%]{]                                                                                                                                 |
|                                                                                                                                                                                                              |
| [          Html.MobSyncfusion().ScriptManager()]                                                                                                                         |
|                                                                                                                                                                                                              |
| [                 .Render();]                                                                                                                                            |
|                                                                                                                                                                                                              |
| [      } [%\>]]                                                                                                                              |
|                                                                                                                                                                                                              |
| [\                                                                                                                                                                                                           |
| [\</] [body] [\>] ]                                                                                     |
|                                                                                                                                                                                                              |
| []                                                                                                                                                   |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


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
|                                                                                                                                                                                                              |
|                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note : Add this ScriptManager() at the end of body tag. Don't add this in top of body tag.


[] 

[]{#related-topics}

