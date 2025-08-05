---
title: updatepanel.md
original_path: WinForms_Docs/99_Uncategorized/updatepanel.md
created_at: 2025-08-05
---








  





### UpdatePanel {#updatepanel style="tab-stops: 0pt"}

The OlapGrid control allows codeless support to work with the ASP.NET AJAX UpdatePanel. Place the OlapGrid inside the UpdatePanel to enable AJAX.

 

All the default functionalities like drill up/down and layout changes would work normally with the UpdatePanel.

The following code snippet illustrates how to place the OlapGrid inside the UpdatePanel:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[ ]**[\<][asp][:][ScriptManager][ [ID][=\"ScriptManager1\"] [runat][=\"server\"] [EnablePartialRendering][=\"true\"] [/\>]][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][asp][:][UpdatePanel][ [ID][=\"UP\"] [runat][=\"server\"] [ChildrenAsTriggers][=\"true\"] [UpdateMode][=\"Conditional\"\>]][]               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][ContentTemplate][\>][]                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [   [\<][syncfusion][:][OlapGrid] [ID][=\"OlapGrid1\"] [runat][=\"server\"] [/\>]][]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][ContentTemplate][\>][]                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][asp][:][UpdatePanel][\>][]                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

