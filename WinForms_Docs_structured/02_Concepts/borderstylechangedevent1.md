---
title: borderstylechangedevent1.md
original_path: WinForms_Docs/02_Concepts/borderstylechangedevent1.md
created_at: 2025-08-05
---






##### BorderStyleChanged Event {#borderstylechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **BorderStyle** property is changed. The BorderStyle property indicates whether the panel should have a border.

 

The event handler receives an argument of type **EventArgs**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [// 2D or 3D border can be set for the StatusBarAdvPanel control using the BorderStyle property. The StatusBarAdvPanel control can also be displayed borderless using this property.]      |
|                                                                                                                                                                                                                                              |
| [this][.statusBarAdvPanel1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]                                          |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [// Handle the BorderStyleChanged event.]                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [this][.statusBarAdvPanel1.BorderStyleChanged+=[new] EventHandler(statusBarAdvPanel1_BorderStyleChanged);]                         |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [private][ [void] statusBarAdvPanel1_BorderStyleChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                               |
|                                                                                                                                                                                                                                              |
| [Console][.WriteLine([\" BorderStyleChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' 2D or 3D border can be set for the StatusBarAdvPanel control using the BorderStyle property. The StatusBarAdvPanel control can also be displayed borderless using this property. ]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.statusBarAdvPanel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Handle the BorderStyleChanged event. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| [AddHandler][ [Me].statusBarAdvPanel1.BorderStyleChanged, [AddressOf] statusBarAdvPanel1_BorderStyleChanged ]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] statusBarAdvPanel1_BorderStyleChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                    |
| [    Console.WriteLine([\" BorderStyleChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

