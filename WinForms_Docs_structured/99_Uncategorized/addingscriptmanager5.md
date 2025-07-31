---
title: addingscriptmanager5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingscriptmanager5.md
created_at: 2025-07-03
---








  









### Adding ScriptManager {#adding-scriptmanager style="tab-stops: 0pt"}

 

**ScriptManager** is a new script resource manager that helps in registering the JavaScript files r. The ScriptManager registers only the Syncfusion.Mvc components script files. The files in ScriptManager resources are set to be combined, minified, and compressed (either gzip and deflate, depending on your browser) before sending to browser.[]

[] 

ScriptManager() extension has improved performance over the **RegisterStaticResource**() method. Hence, we always suggest this method in registering the scripts.[]

The ScriptManager() method should be placed after all the components on the page. Generally,  you can use this method at the end of the master page.

[] 

Methods

 


+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------+-------------------------------------------------------------------------------------+-----------------+
| Method                                                                                               | Description                                                                                                                                         | Parameters | Type            | Return Type                                                                         | Reference links |
+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------+-------------------------------------------------------------------------------------+-----------------+
| ScriptManager ()                                                                                     | Used to register the Syncfusion.Mvc component's script files. The files in ScriptManager resources are set to be combined, minified, and compressed | NA         | **Server-side** | [MvcResourceRenderer] | NA              |
+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+------------+-----------------+-------------------------------------------------------------------------------------+-----------------+
| [RegisterStaticResources()][] | [(Deprecated) ]Used to register the Syncfusion.Mvc component's script files                                                     | NA         | **Server-side** | [MvcResourceRenderer] | NA              |
|                                                                                                      |                                                                                                                                                     |            |                 |                                                                                     |                 |
|                                                                                                      |                                                                                                                                                     |            |                 |                                                                                     |                 |
+======================================================================================================+=====================================================================================================================================================+============+=================+=====================================================================================+=================+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                  |
|                                                                                                                                                                                                                       |
| [\<][body][\>][] |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                       |
| [...][]                                                                                                                           |
|                                                                                                                                                                                                                       |
| [...][]                                                                                                                           |
|                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().ScriptManager()[%\>]\                                 |
| [\</][body][\>]][]                                               |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note : Add this ScriptManager() at the end of body tag. Don't add this at the top of the  body tag.


 

[]{#related-topics}

