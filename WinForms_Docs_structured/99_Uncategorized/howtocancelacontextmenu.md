---
title: howtocancelacontextmenu.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocancelacontextmenu.md
created_at: 2025-07-03
---






##### How to cancel a context menu {#how-to-cancel-a-context-menu style="tab-stops: 0pt"}

 

We can cancel the context menu from being shown by handling the ParentBarItem.BeforePopup menu.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [this][.parentBarItem1.BeforePopup += [new] [CancelEventHandler](PopupMenu_BeforePopup);]             |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [private][ [void] PopupMenu_BeforePopup([object] sender, [CancelEventArgs] arg)] |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [      [// Check for a condition and cancel if necessary]]                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [      arg.Cancel = [true];]                                                                                                                                                |
|                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] PopupMenu_BeforePopup([ByVal] sender [As] [Object], [ByVal] arg [As] CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                            |
| [    [\' Check for a condition and cancel if necessary ]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [    arg.Cancel = [True]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Events of ParentBarItem]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

