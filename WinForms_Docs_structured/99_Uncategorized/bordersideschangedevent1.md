---
title: bordersideschangedevent1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\bordersideschangedevent1.md
created_at: 2025-07-03
---






##### BorderSidesChanged Event {#bordersideschanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired, when the value of the **BorderSides** property is changed. The BorderSides property indicates the border sides of the panel.

 

The event handler receives an argument of type **EventArgs**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [// Draw border sides for the StatusBarAdvPanel control using the BorderSides property.]                                                                                                   |
|                                                                                                                                                                                                                                              |
| [this][.statusBarAdv1Panel.BorderSides = System.Windows.Forms.[Border3DSide].Top;]                                                 |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [// Handle the BorderSidesChanged event.]                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [this][.statusBarAdvPanel1.BorderSidesChanged+=[new] [EventHandler](statusBarAdvPanel1_BorderSidesChanged);]  |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [private][ [void] statusBarAdvPanel1_BorderSidesChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [Console][.WriteLine([\" BorderSidesChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [\'Draw border sides for the StatusBarAdvPanel control using the BorderSides property. ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.statusBarAdv1Panel.BorderSides = System.Windows.Forms.Border3DSide.Top ]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [\'Handle the BorderSidesChanged event. ]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [AddHandler][ [Me].statusBarAdvPanel1.BorderSidesChanged, [AddressOf] statusBarAdvPanel1_BorderSidesChanged ]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] statusBarAdvPanel1_BorderSidesChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' The below line will be displayed in the output window at runtime. ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                    |
| [    Console.WriteLine([\" BorderSidesChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

