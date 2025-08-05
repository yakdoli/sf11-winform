---
title: howtodetectthedockingstyleassignedtoacontrol.md
original_path: WinForms_Docs/02_Concepts/howtodetectthedockingstyleassignedtoacontrol.md
created_at: 2025-08-05
---






##### How to detect the docking style assigned to a control[]{#p124}? {#how-to-detect-the-docking-style-assigned-to-a-control style="tab-stops: 0pt"}

 You can detect the Docking style that is assigned to the control, at run time, using GetDockingStyle method.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                            | Description                                                                                                                                                                                                                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetDockingStyle                   | Returns the current docking style of the control. The return value for this method would be docking style value, that specifies the dock type / position. The docked control for which the dock style is to be identified should be passed as a parameter to this method. The parameter is, |
|                                   |                                                                                                                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                                                                                             |
|                                   | *Ctrl* - Indicates the docked control for which the DockStyle needs to be retrieved.                                                                                                                                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [//Getting the docking style]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [private][ [void] button1_Click([object] sender, [EventArgs] e)]                              |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [this][.dockingManager1.GetDockStyle([this].panel1);]                                                                                   |
|                                                                                                                                                                                                                                                   |
| [Console][.Write([\"Dock style :\"] + [this].dockingManager1.GetDockStyle([this].panel1));] |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [\'Getting the docking style]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] button1_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                   |
| [Me][.dockingManager1.GetDockStyle([this].panel1)]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                   |
| [Console][.Write([\"Dock style :\"] + [this].dockingManager1.GetDockStyle([this].panel1))]                                                                 |
|                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p125}[]{#_How_to_Enable} 

[]{#related-topics}

