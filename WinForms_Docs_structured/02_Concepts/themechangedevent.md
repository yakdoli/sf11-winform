---
title: themechangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\themechangedevent.md
created_at: 2025-07-03
---






##### ThemeChanged Event {#themechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **ThemesEnabled** property is changed. The ThemesEnabled property indicates if the StatusBar will draw a themed background ( Indicated Settings: BorderStyle = None ).

 

The event handler receives an argument of type **EventArgs**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [private][ [void] statusBarAdv1_ThemeChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [// Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                   |
|                                                                                                                                                                                                                                   |
| [Console][.WriteLine([\" ThemeChanged event is raised \"]);]                                                          |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] statusBarAdv1_ThemeChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                         |
| [\' Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\" ThemeChanged event is raised \"])]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

