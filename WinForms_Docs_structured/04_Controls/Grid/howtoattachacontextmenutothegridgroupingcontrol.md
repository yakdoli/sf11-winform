---
title: howtoattachacontextmenutothegridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtoattachacontextmenutothegridgroupingcontrol.md
created_at: 2025-08-05
---






#### How to attach a context menu to the GridGrouping control {#how-to-attach-a-context-menu-to-the-gridgrouping-control style="tab-stops: 0pt"}

[] 

This can be done using the below code snippet.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                                            |
| [//Add items to context menu]                                                                                            |
|                                                                                                                                                                            |
| [this][.contextMenu1.MenuItems.Add([\"One\"]);]                |
|                                                                                                                                                                            |
| [this][.contextMenu1.MenuItems.Add([\"Two\"]);]                |
|                                                                                                                                                                            |
| [this][.contextMenu1.MenuItems.Add([\"Three\"]);]              |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [//Assign it to the GridGroupingControl]                                                                                 |
|                                                                                                                                                                            |
| [this][.gridGroupingControl1.ContextMenu = [this].contextMenu1;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                                       |
| [\'Add items to context menu]                                                                                       |
|                                                                                                                                                                       |
| [Me][.contextMenu1.MenuItems.Add([\"One\"])]              |
|                                                                                                                                                                       |
| [Me][.contextMenu1.MenuItems.Add([\"Two\"])]              |
|                                                                                                                                                                       |
| [Me][.contextMenu1.MenuItems.Add([\"Three\"])]            |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'Assign it to the GridGroupingControl]                                                                            |
|                                                                                                                                                                       |
| [Me][.gridGroupingControl1.ContextMenu = [Me].contextMenu1] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p685} 

 

[]{#related-topics}

