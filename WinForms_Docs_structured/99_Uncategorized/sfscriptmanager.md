---
title: sfscriptmanager.md
original_path: WinForms_Docs/99_Uncategorized/sfscriptmanager.md
created_at: 2025-08-05
---








  









## SFScriptManager {#sfscriptmanager style="tab-stops: 0pt"}

 

SFScriptManager control is inherited from the ASP.NET ScriptManager control which has some additional functionalities like MinifyJavascript, LoadStartupScriptsInSeparateFile and CombineScriptsHandlerUrl.

[] 

[]{#DDE_LINK}The SFScriptManager control manages client-script for Microsoft ASP.NET AJAX pages, and it combines the scripts that are loaded dynamically. By default, the SFScriptManager control registers the script for the Microsoft AJAX Library with the page. This enables client-script to use the type system extensions and to support features such as partial-page rendering and Web-service calls.

[] 

Why Use the SFScriptManager Control?

[] 

You must use a SFScriptManager control on a page to enable the following features.

[] 

[·      ]To combine the scripts that are loaded dynamically.

[·      ]To indicate whether syncfusion controls startup scripts loads in separate file or not.

[·      ]Client-script functionality of the Microsoft AJAX Library, and any custom script that you want to send to the browser.

[·      ]Partial-page rendering, which enables regions on the page to be independently refreshed without a postback. The ASP.NET AJAX UpdatePanel, UpdateProgress, and Timer controls require a SFScriptManager control to support partial-page rendering.

More:





