---
title: howtohidethefocusrectanglewhichgetsdisplayedontheselectedtab.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtohidethefocusrectanglewhichgetsdisplayedontheselectedtab.md
created_at: 2025-07-03
---






#### How to hide the Focus Rectangle which gets displayed on the selected Tab {#how-to-hide-the-focus-rectangle-which-gets-displayed-on-the-selected-tab style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The focus rectangle can be hidden by setting the **FocusOnTabClick** property to False. This can be done programmatically using the code snippet given below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| **[]**                                                                                                     |
|                                                                                                                                                              |
| [this][.tabControlAdv1.FocusOnTabClick = [false];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                            |
|                                                                                                                                                           |
| **[]**                                                                                                  |
|                                                                                                                                                           |
| [Me][.tabControlAdv1.FocusOnTabClick = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: The TabControlAdv.GetTabRect() method is used to get the Rectangle region of a Tab in client co-ordinates, given it\'s TabIndex.


 

 

 

[]{#p894} 

[]{#related-topics}

