---
title: tabsorderchangedevent.md
original_path: WinForms_Docs/99_Uncategorized/tabsorderchangedevent.md
created_at: 2025-08-05
---






#### TabsOrderChanged Event {#tabsorderchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs when the order of the tabs is changed in the TabControlAdv.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [// Set the UserMoveTabs property to True, to drag and drop tabs during runtime.]                                                                                                    |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.UserMoveTabs = [true];]                                                                               |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [// Handle the TabsOrderChanged event.]                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.TabsOrderChanged+=[new] [EventHandler](tabControlAdv1_TabsOrderChanged);]        |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [private][ [void] tabControlAdv1_TabsOrderChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [// Below line will be displayed in the output window at run-time, when a tab is dragged and dropped at another location.]                                                           |
|                                                                                                                                                                                                                                        |
| [Console][.Write([\"TabsOrderChanged event is raised\"]);]                                                                 |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Set the UserMoveTabs property to True, to drag and drop tabs during runtime. ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.tabControlAdv1.UserMoveTabs = [True] ]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the TabsOrderChanged event. ]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                              |
| [AddHandler][ [Me].tabControlAdv1.TabsOrderChanged, [AddressOf] tabControlAdv1_TabsOrderChanged ]                                                                                             |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] tabControlAdv1_TabsOrderChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [    [\' Below line will be displayed in the output window at run-time, when a tab is dragged and dropped at another location. ]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                              |
| [    Console.Write([\"TabsOrderChanged event is raised\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: The TabControlAdv.OnTabsOrderChanged() method raises the OnTabsOrderChanged event.


 

 

 

[]{#p884} 

[]{#related-topics}

