---
title: insertmodechangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\insertmodechangedevent.md
created_at: 2025-07-03
---








  









### InsertModeChanged Event {#insertmodechanged-event style="tab-stops: 0pt"}

 

This event is fired when the value of the **InsertMode** property changes. The InsertMode property specifies the insert mode state.

 

The event handler receives an argument of type **EventArgs**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Handle the InsertModeChanged event.]                                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [this][.editControl1.InsertModeChanged+=[new] [EventHandler](editControl1_InsertModeChanged);]         |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [// Set the value of the InsertMode property.]                                                                                                                                      |
|                                                                                                                                                                                                                                       |
| [this][.editControl1.InsertMode = [false];]                                                                                 |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [private][ [void] editControl1_InsertModeChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [// The below statement can be seen in the output window at runtime.]                                                                                                               |
|                                                                                                                                                                                                                                       |
| [Console][.WriteLine([\" InsertModeChanged event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Handle the InsertModeChanged event.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [AddHandler][ [Me].editControl1.InsertModeChanged, [AddressOf] editControl1_InsertModeChanged ]                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Set the value of the InsertMode property.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [Me][.editControl1.InsertMode = [False]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] editControl1_InsertModeChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| [The below statement can be seen in the output window at runtime.]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine([\" InsertModeChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p144} 

[]{#related-topics}

