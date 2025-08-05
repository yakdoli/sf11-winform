---
title: singlelinechangedevent.md
original_path: WinForms_Docs/99_Uncategorized/singlelinechangedevent.md
created_at: 2025-08-05
---








  









### SingleLineChanged Event {#singlelinechanged-event style="tab-stops: 0pt"}

 

This event is fired when the value of the **SingleLineMode** property is changed. The SingleLineMode property specifies whether the single line mode is enabled.

 

The event handler receives an argument of type **EventArgs**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Handle the SingleLineChanged event.]                                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [this][.editControl1.SingleLineChanged+=[new] [EventHandler](editControl1_SingleLineChanged);]         |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [// Set the SingleLineMode property to True.]                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [this][.editControl1.SingleLineMode = [true];]                                                                              |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [private][ [void] editControl1_SingleLineChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [  // The below statement can be seen in the output window at runtime.]                                                                                                             |
|                                                                                                                                                                                                                                       |
| [Console][.WriteLine([\" SingleLineChanged event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Handle the SingleLineChanged event. ]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                             |
| [AddHandler][ [Me].editControl1.SingleLineChanged, [AddressOf] editControl1_SingleLineChanged ]                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Set the SingleLineMode property to True. ]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [Me][.editControl1.SingleLineMode = [True] ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] editControl1_SingleLineChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| [  \' The below statement can be seen in the output window at runtime.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine([\" SingleLineChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p171}[] 

[]{#related-topics}

