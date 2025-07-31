---
title: docking.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\docking.md
created_at: 2025-07-03
---






##### Docking {#docking style="tab-stops: 0pt"}

[]{#p47}[] 

Docked control can be docked to any of the four sides of the container control, i.e., to Left, Right, Top and Bottom. DockingManager lets you specify the type of docking and the bounds of the docked control using the **DockControl** method. This method also sets Tabbed style for the controls.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [// Tab the docked controls]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| [this][.dockingManager.DockControl([this].listBox1, [this].listBox2,Syncfusion.Windows.Forms.Tools.DockingStyle.Left,200,[true]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [\' Tab the docked controls]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [Me][.dockingManager.DockControl([Me].listBox1, [Me].listBox2,Syncfusion.Windows.Forms.Tools.DockingStyle.Left,200,[True])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 45: Controls docked to Left, Right, Top and Bottom

[] 

At runtime, docking style can be selected easily using the context menu.

[] 

{border="0"}

***[]*** 

Figure 46: Docking Style selected at Run Time

[] 


{border="0"} Note:[ ]At run time, docking style can also be set with the help of Dock Arrows provided by the DragProviderStyle property.


[]{#related-topics}

