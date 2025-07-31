---
title: howtomakeadockedcontrolfloatonly.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtomakeadockedcontrolfloatonly.md
created_at: 2025-07-03
---






##### How to make a docked control Float Only? {#how-to-make-a-docked-control-float-only style="tab-stops: 0pt"}

[] 

The docked control can also be only floating and cannot be docked, by calling the SetFloatOnly method.

[] 


+-----------------------------------+----------------------------------------------------------------------+
| Parameter                         | Description                                                          |
+-----------------------------------+----------------------------------------------------------------------+
| SetFloatOnly                      | Make the docked control a float only control.                        |
|                                   |                                                                      |
|                                   |                                                                      |
|                                   |                                                                      |
|                                   | *Ctrl* - The control for which docking is enabled.                   |
|                                   |                                                                      |
|                                   | *bFloating* - Represents a boolean value, TRUE, to disabled docking. |
+-----------------------------------+----------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [this][.dockingManager1.SetFloatOnly([this].listBox2, [true]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                         |
|                                                                                                                                                                                            |
| []                                                                                                                                                                 |
|                                                                                                                                                                                            |
| [Me][.dockingManager1.SetFloatOnly([Me].listBox2, [True]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 106: Float Only Enabled

[]{#related-topics}

