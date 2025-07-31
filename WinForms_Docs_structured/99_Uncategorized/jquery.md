---
title: jquery.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\jquery.md
created_at: 2025-07-03
---








  









## jQuery {#jquery style="tab-stops: 0pt"}

[] 

jQuery is a fast and concise JavaScript library that simplifies HTML document traversing, event handling, animating, and AJAX interactions for rapid web development. jQuery is designed to change the writing style of JavaScript.

[] 

jQuery Manager

[] 

A jQuery manager is used to register all the common library Plug-ins. It can be used inside any Web control to register the items in the control. It enables the Script Manager to render JavaScript code for the jQuery.

You can use the below code instead of the ScriptControlDescriptor / ScriptComponentDescriptor that you normally use with the IScriptControl implementation on the server-side.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [IEnumerable\<ScriptDescriptor\> IScriptControl.GetScriptDescriptors() ]                                                                                                         |
|                                                                                                                                                                                                                      |
| [{   ]                                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [jQueryComponentDescriptor jDesc = [new] jQueryComponentDescriptor([\"somejQueryPlugin\"], [this].ClientID);  ] |
|                                                                                                                                                                                                                      |
| [jDesc.AddProperty([\"positiveTextColor\"], [this].PositiveTextColor);  ]                                                            |
|                                                                                                                                                                                                                      |
| [jDesc.AddProperty([\"negativeTextColor\"], [this].NegativeTextColor);  ]                                                            |
|                                                                                                                                                                                                                      |
| [yield][ [return] jDesc;   ]                                                                               |
|                                                                                                                                                                                                                      |
| [} ]                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 Once this is done, the ASP.NET Script Manager automatically creates the load-up script code as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Sys.Application.add_init(function()]                                                                                                                               |
|                                                                                                                                                                                                         |
| [{]                                                                                                                                                                 |
|                                                                                                                                                                                                         |
| [\$([\'#something\']).somePlugin({negativeTextColor:[\"Red\"],positiveTextColor:[\"Blue\"]});] |
|                                                                                                                                                                                                         |
| [});]                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

