---
title: bordersideschangedevent.md
original_path: WinForms_Docs/99_Uncategorized/bordersideschangedevent.md
created_at: 2025-08-05
---






##### BorderSidesChanged Event {#bordersideschanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

This event is fired when the value of the **BorderSides** property is changed. The BorderSides property indicates the border sides of the panel.

 

The event handler receives an argument of type **EventArgs**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [// Draw border sides for the StatusBarAdv control using the BorderSides property.]                                                                                                   |
|                                                                                                                                                                                                                                         |
| [this][.statusBarAdv1.BorderSides = System.Windows.Forms.[Border3DSide].Top;]                                                 |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Handle the BorderSidesChanged event.]                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [this][.statusBarAdv1.BorderSidesChanged+=[new] [EventHandler](statusBarAdv1_BorderSidesChanged);]       |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [private][ [void] statusBarAdv1_BorderSidesChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                |
|                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\" BorderSidesChanged event is raised \"]);]                                                          |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Draw border sides for the StatusBarAdv control using the BorderSides property. ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [Me][.statusBarAdv1.BorderSides = System.Windows.Forms.Border3DSide.Top ]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Handle the BorderSidesChanged event. ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                               |
| [AddHandler][ [Me].statusBarAdv1.BorderSidesChanged, [AddressOf] statusBarAdv1_BorderSidesChanged ]                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] statusBarAdv1_BorderSidesChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                               |
| [    [\' The below line will be displayed in the output window at runtime. ]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                               |
| [    Console.WriteLine([\" BorderSidesChanged event is raised \"])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

