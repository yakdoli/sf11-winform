---
title: iconchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\iconchangedevent.md
created_at: 2025-07-03
---






##### IconChanged Event {#iconchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **Icon** property is changed. The Icon property indicates the icon of the panel.

 

The event handler receives an argument of type **EventArgs**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [private][ [void] statusBarAdvPanel1_IconChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [// Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                       |
|                                                                                                                                                                                                                                       |
| [Console][.WriteLine([\" IconChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] statusBarAdvPanel1_IconChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Below line will be displayed in the output window at run-time, when this event is fired. ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine([\" IconChanged event is raised \"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

