---
title: textchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textchangedevent.md
created_at: 2025-07-03
---






#### TextChanged Event {#textchanged-event style="tab-stops: 0pt"}

 

This event is fired when the text in the Edit Control is changed.

 

The event handler receives an argument of type **EventArgs**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Handle the TextChanged event.]                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [this][.editControl1.TextChanged += [new] [EventHandler](editControl1_TextChanged);]             |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// Set the text of the EditControl.]                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [this][.editControl1.Text = [\"Sample Text\"];]                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [private][ [void] editControl1_TextChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [// The below statement can be seen in the output window at runtime.]                                                                                                         |
|                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\" TextChanged event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Handle the TextChanged event.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [AddHandler][ [Me].editControl1.TextChanged, [AddressOf] editControl1_TextChanged ]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Set the text of the EditControl.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.editControl1.Text = [\"Sample Text\"]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] editControl1_TextChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                       |
| [\' The below statement can be seen in the output window at runtime.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                       |
| [Console.WriteLine([\" TextChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p173} 

[]{#related-topics}

