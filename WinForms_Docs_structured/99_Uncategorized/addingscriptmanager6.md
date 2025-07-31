---
title: addingscriptmanager6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingscriptmanager6.md
created_at: 2025-07-03
---






#### Adding ScriptManager {#adding-scriptmanager style="tab-stops: 0pt"}

**ScriptManager** is a new script resource manager that helps in registering JavaScript files. The ScriptManager registers only the Syncfusion.Mvc component script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip or deflate, depending on your browser) before being sent to the browser.

 

The **ScriptManager()** extension has improved performance over the **RegisterStaticResource()** method, hence we always suggest this method in registering the scripts.

 

The **ScriptManager()** method should be placed after all the components on the page. Generally, you can use this method at the end of the master page.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][cshtml][\]]**                                                                          |
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
| [\@{][Html.Syncfusion().ScriptManager().Render();[}]][\ |
| [\</][body][\>]]                                                                                     |
|                                                                                                                                                                                                           |
| []                                                                                                                                                |
|                                                                                                                                                                                                           |
|                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Add this ScriptManager() at the end of the [\<][body][\>] tag. Don't add this in top of the [\<][body][\>] tag.


 

[]{#related-topics}

