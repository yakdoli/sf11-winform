---
title: howtochangethebackcolorofactiveandinactivetabs.md
original_path: WinForms_Docs/99_Uncategorized/howtochangethebackcolorofactiveandinactivetabs.md
created_at: 2025-08-05
---






#### How to change the backcolor of Active and Inactive tabs {#how-to-change-the-backcolor-of-active-and-inactive-tabs style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

You can change the tab back color for active tabs and inactive tabs using **ActiveTabColor** and **InactiveTabColor** properties. The following code snippet illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [private][ [void] tabbedMDIManager_TabControlAdded([object] sender, [TabbedMDITabControlEventArgs] args)] |
|                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [    args.TabControl.ActiveTabColor = [Color].Red;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
| [    args.TabControl.InactiveTabColor = [Color].Green;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] tabbedMDIManager_TabControlAdded([ByVal] sender [As] [Object], [ByVal] args [As] TabbedMDITabControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    args.TabControl.ActiveTabColor = Color.Red]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    args.TabControl.InactiveTabColor = Color.Green]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: ActiveTabColor property work only for 2D, 3D, Workbook Mode, OneNoteStyle and not for other tabStyles.


 

 

 

[]{#p941} 

[]{#related-topics}

