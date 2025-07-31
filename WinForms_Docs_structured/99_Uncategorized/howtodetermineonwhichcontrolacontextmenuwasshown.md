---
title: howtodetermineonwhichcontrolacontextmenuwasshown.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodetermineonwhichcontrolacontextmenuwasshown.md
created_at: 2025-07-03
---






##### How to determine on which control a context menu was shown {#how-to-determine-on-which-control-a-context-menu-was-shown style="tab-stops: 0pt"}

[] 

We can identify the control on which the context menu was shown by using the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [// The PopupMenu\'s SourceControl specifies its target control]                                                  |
|                                                                                                                                                                     |
| [Control][ srcControl = [this].popupMenu1.SourceControl;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [\' The PopupMenu\'s SourceControl specifies its target control ]                                                                            |
|                                                                                                                                                                                                |
| [Dim][ srcControl [As] Control = [Me].popupMenu1.SourceControl] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

