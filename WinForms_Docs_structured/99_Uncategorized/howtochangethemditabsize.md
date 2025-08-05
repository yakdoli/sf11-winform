---
title: howtochangethemditabsize.md
original_path: WinForms_Docs/99_Uncategorized/howtochangethemditabsize.md
created_at: 2025-08-05
---






#### How to change the MDI tab size {#how-to-change-the-mdi-tab-size style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

You should handle the TabControlAdded event handler and use **ItemSize** property to change the tab size.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Handle the TabControlAdded event. ]                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [this][.tabbedMDIManager.TabControlAdded += [new] TabbedMDITabControlEventHandler(tabbedMDIManager_TabControlAdded); ]        |
|                                                                                                                                                                                                                                         |
| [private][ [void] tabbedMDIManager_TabControlAdded([object] sender, TabbedMDITabControlEventArgs args) ] |
|                                                                                                                                                                                                                                         |
| [{ ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [// To change the size. ]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [args.TabControl.ItemSize = [new] [Size](40, 40); ]                                                                                                       |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\' Handle the TabControlAdded event. ]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [AddHandler][ tabbedMDIManager.TabControlAdded, [AddressOf] tabbedMDIManager_TabControlAdded]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] tabbedMDIManager_TabControlAdded([ByVal] sender [As] [Object], [ByVal] args [As] TabbedMDITabControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\' To change the size. ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [args.TabControl.ItemSize = [New] Size(40, 40)]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p935} 

[]{#related-topics}

