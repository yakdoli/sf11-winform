---
title: howtodisplaycontextmenuofadockedcontrolataspecifiedpoint.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodisplaycontextmenuofadockedcontrolataspecifiedpoint.md
created_at: 2025-07-03
---






##### How to display context menu of a docked control at a specified point? {#how-to-display-context-menu-of-a-docked-control-at-a-specified-point style="tab-stops: 0pt"}

[] 

This can be done using ShowMenu method.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------+
| Method                            | Description                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ShowMenu                          | Show\'s the docking caption context menu at the specified point (Pt). The parameters are, |
|                                   |                                                                                           |
|                                   | *[]*                                                |
|                                   |                                                                                           |
|                                   | *Ctrl* - Indicates the control for which dock / floating state is been queried.           |
|                                   |                                                                                           |
|                                   | *Pt* - Indicates the location of the menu to be displayed.                                |
+-----------------------------------+-------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)]             |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [this][.dockingManager1.ShowMenu([this].listBox1, [new] [Point](100,100)); ] |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                   |
| [Me][.dockingManager1.ShowMenu([Me].listBox1, [New] [Point](100,100))]                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

