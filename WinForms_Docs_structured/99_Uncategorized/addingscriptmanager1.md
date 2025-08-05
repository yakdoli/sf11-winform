---
title: addingscriptmanager1.md
original_path: WinForms_Docs/99_Uncategorized/addingscriptmanager1.md
created_at: 2025-08-05
---






#### Adding ScriptManager {#adding-scriptmanager style="tab-stops: 0pt"}

**ScriptManager** is a new script resource manager that helps in registering JavaScript files. The ScriptManager registers only the Syncfusion.Mvc components script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip and deflate, depending on your browser) before sending to browser.

 

The **ScriptManager()** extension has improved performance over the **RegisterStaticResource()** method, hence we always suggest this method in registering the scripts.

 

The **ScriptManager()** method should be placed after all the components on the page. Generally, you can use this method at the end of the master page.

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
| [\<%][=][Html.Syncfusion().ScriptManager()[%\>]\                     |
| [\</][body][\>]]                                                                                     |
|                                                                                                                                                                                                           |
| []                                                                                                                                                |
|                                                                                                                                                                                                           |
|                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Add this ScriptManager() at the end of a [\<][body][\>] tag. Don't add this in the top of a [\<][body][\>] tag.


 

[]{#related-topics}

