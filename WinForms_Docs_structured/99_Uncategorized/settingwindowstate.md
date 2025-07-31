---
title: settingwindowstate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingwindowstate.md
created_at: 2025-07-03
---






#### Setting Window State {#setting-window-state style="tab-stops: 0pt"}

There are three possible window states of MDI windows for the Document Container control. They are as follows.

 

[·      ]Maximized

[·      ]Minimized

[·      ]Normal

 

To set the MDI window state to \"minimized\", use the below code snippet. FlowDocumentScrollViewer is considered as an element of the Document Container in the below mentioned example.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<!\-- Adding Document Container \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][DocumentContainer][ Name][=\"DocContainer\"][ Mode][=\"MDI\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][FlowDocumentScrollViewer][ syncfusion][:][DocumentContainer.MDIWindowState][=\"Minimized\" \>]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][FlowDocumentScrollViewer][\>]                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [...\....]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [...\....            ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][DocumentContainer][\>]                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 397: MDIWindowState = \"Minimized\"

 

[]{#p217} 

[]{#related-topics}

