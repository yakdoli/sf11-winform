---
title: labeleditchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\labeleditchangedevent.md
created_at: 2025-07-03
---






#### LabelEditChanged Event {#labeleditchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is triggered when the **LabelEdit** property is changed in the TabControlAdv.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [// Set the LabelEdit property.]                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.LabelEdit = [true];]                                                                                  |
|                                                                                                                                                                                                                                        |
| [// Handle the LabelEditChanged event.]                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| [this][.tabControlAdv1.LabelEditChanged+=[new] [EventHandler](tabControlAdv1_LabelEditChanged);]        |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [private][ [void] tabControlAdv1_LabelEditChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                         |
|                                                                                                                                                                                                                                        |
| [Console][.Write([\"LabelEditChanged event is raised\"]);]                                                                 |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Set the LabelEdit property. ]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.tabControlAdv1.LabelEdit = [True] ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the LabelEditChanged event. ]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                              |
| [AddHandler][ [Me].tabControlAdv1.LabelEditChanged, [AddressOf] tabControlAdv1_LabelEditChanged ]                                                                                             |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] tabControlAdv1_LabelEditChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                              |
| [    Console.Write([\"LabelEditChanged event is raised\"])]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

