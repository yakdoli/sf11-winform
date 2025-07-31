---
title: gradientbackgroundchangedevent1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\gradientbackgroundchangedevent1.md
created_at: 2025-07-03
---






##### GradientBackgroundChanged Event {#gradientbackgroundchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **GradientBackground** property is changed. The GradientBackground property indicates whether the background will be drawn with the gradient.

 

The event handler receives an argument of type **EventArgs**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [private][ [void] statusBarAdvPanel1_GradientBackgroundChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [// Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [Console][.WriteLine([\" GradientBackgroundChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] statusBarAdvPanel1_GradientBackgroundChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                           |
| [\' Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\" GradientBackgroundChanged event is raised \"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

