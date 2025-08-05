---
title: themechangedevent1.md
original_path: WinForms_Docs/02_Concepts/themechangedevent1.md
created_at: 2025-08-05
---






##### ThemeChanged Event {#themechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **ThemesEnabled** property is changed. The ThemesEnabled property indicates if the background color will be set to \'Transparent\' ( Indicated Settings: BorderSides = Right, BorderStyle = Fixed3D, Border3DStyle = Etched).

 

The event handler receives an argument of type **EventArgs**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [private][ [void] statusBarAdvPanel1_ThemeChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [// Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                        |
|                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\" ThemeChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] statusBarAdvPanel1_ThemeChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                              |
| [Console.WriteLine([\" ThemeChanged event is raised \"])]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

