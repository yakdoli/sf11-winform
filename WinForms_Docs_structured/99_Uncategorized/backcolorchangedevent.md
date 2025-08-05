---
title: backcolorchangedevent.md
original_path: WinForms_Docs/99_Uncategorized/backcolorchangedevent.md
created_at: 2025-08-05
---






#### BackColorChanged Event {#backcolorchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

This event is fired when the value of the **BackColor** property is changed in the TabControlAdv.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [// Set the new back color.]                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.BackColor = System.Drawing.[Color].Aqua;]                                                             |
|                                                                                                                                                                                                                                        |
| [// Set the active tab color for the TabControlAdv to highlight the activated tab in the control.]                                                                                   |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.ActiveTabColor = System.Drawing.[Color].Bisque;]                                                      |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [// Handle the BackColorChanged event.]                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.BackColorChanged+=[new] [EventHandler](tabControlAdv1_BackColorChanged);]        |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [private][ [void] tabControlAdv1_BackColorChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [Console][.Write([\"BackColorChanged event is raised\"]);]                                                                 |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Set the new back color. ]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.tabControlAdv1.BackColor = System.Drawing.Color.Aqua ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Set the active tab color for the TabControlAdv to highlight the activated tab in the control. ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.tabControlAdv1.ActiveTabColor = System.Drawing.Color.Bisque ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the BackColorChanged event. ]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                              |
| [AddHandler][ [Me].tabControlAdv1.BackColorChanged, [AddressOf] tabControlAdv1_BackColorChanged ]                                                                                             |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] tabControlAdv1_BackColorChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [    Console.Write([\"BackColorChanged event is raised\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

