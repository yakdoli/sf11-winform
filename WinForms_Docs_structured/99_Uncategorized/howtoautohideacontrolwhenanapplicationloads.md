---
title: howtoautohideacontrolwhenanapplicationloads.md
original_path: WinForms_Docs/99_Uncategorized/howtoautohideacontrolwhenanapplicationloads.md
created_at: 2025-08-05
---






##### How to auto hide a control when an application loads {#how-to-auto-hide-a-control-when-an-application-loads style="tab-stops: 0pt"}

 

A control can be autohidden on loading, by enabling the **AutoHideOnLoad** property through designer or by calling **SetAutoHideOnLoad** method programmatically.

 


+-----------------------------------+------------------------------------------------------------------------------+
| Method                            | Description                                                                  |
+-----------------------------------+------------------------------------------------------------------------------+
| SetAutoHideOnLoad                 | AutoHides the docked control when the application loads. The parameters are, |
|                                   |                                                                              |
|                                   | *[]*                                   |
|                                   |                                                                              |
|                                   | *Ctrl* - Indicates the docked control.                                       |
|                                   |                                                                              |
|                                   | *bautohide* - Value indicating true or false.                                |
+-----------------------------------+------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.dockingManager1.SetAutoHideOnLoad([this].listBox1, [true]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [Me][.DockingManager1.SetAutoHideOnLoad([Me].ListBox1, [True])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p154} 

[]{#related-topics}

