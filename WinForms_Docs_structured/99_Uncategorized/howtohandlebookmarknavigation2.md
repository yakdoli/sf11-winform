---
title: howtohandlebookmarknavigation2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtohandlebookmarknavigation2.md
created_at: 2025-07-03
---








  









## How to Handle Bookmark Navigation {#how-to-handle-bookmark-navigation style="tab-stops: 0pt"}

 

You can handle the bookmark navigation in application level and prevent it from navigation. To achieve this set the *e.Handle* to true.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [spreadControl.CellRequestNavigate += [new] [CellRequestNavigateEventHandler](spreadControl_CellRequestNavigate);]                                          |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [void][ spreadControl_CellRequestNavigate([object] sender, [CellRequestNavigateEventArgs] e)] |
|                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [   e.Handled = [true];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \[VB\]]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ spreadControl.CellRequestNavigate += [New] CellRequestNavigateEventHandler([AddressOf] spreadControl_CellRequestNavigate)]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] spreadControl_CellRequestNavigate([ByVal] sender [As] [Object], [ByVal] e [As] CellRequestNavigateEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [         e.Handled = [True]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

