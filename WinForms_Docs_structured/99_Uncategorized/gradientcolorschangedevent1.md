---
title: gradientcolorschangedevent1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\gradientcolorschangedevent1.md
created_at: 2025-07-03
---






##### GradientColorsChanged Event {#gradientcolorschanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **GradientColors** property is changed. The GradientColors property specifies the color array that defines the gradient.

 

The event handler receives an argument of type **EventArgs**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [private][ [void] statusBarAdvPanel1_GradientColorsChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [// Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [Console][.WriteLine([\" GradientColorsChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] statusBarAdvPanel1_GradientColorsChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                       |
| [Console.WriteLine([\" GradientColorsChanged event is raised \"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

