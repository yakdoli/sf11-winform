---
title: howtohideacontrolwhenanapplicationloads.md
original_path: WinForms_Docs/99_Uncategorized/howtohideacontrolwhenanapplicationloads.md
created_at: 2025-08-05
---






##### How to hide a control when an application loads? {#how-to-hide-a-control-when-an-application-loads style="tab-stops: 0pt"}

**[]** 

This is done programmatically, by calling SetHiddenOnLoad method or through Designer, by setting **HiddenOnLoad** property to true.

[] 


+-----------------------------------+--------------------------------------------------------------------------+
| Method                            | Description                                                              |
+-----------------------------------+--------------------------------------------------------------------------+
| SetHiddenOnLoad                   | Hides the docked control when the application loads. The parameters are, |
|                                   |                                                                          |
|                                   | *[]*                               |
|                                   |                                                                          |
|                                   | *Ctrl* - Indicates the docked control.                                   |
|                                   |                                                                          |
|                                   | *bhidden* - Value indicating true or false.                              |
+-----------------------------------+--------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [this][.dockingManager1.SetHiddenOnLoad([this].listBox1, [true]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [Me][.dockingManager1.SetHiddenOnLoad([Me].listBox1, [True])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p156} 

[]{#related-topics}

