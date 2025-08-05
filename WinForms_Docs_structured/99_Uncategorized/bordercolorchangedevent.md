---
title: bordercolorchangedevent.md
original_path: WinForms_Docs/99_Uncategorized/bordercolorchangedevent.md
created_at: 2025-08-05
---






##### BorderColorChanged Event {#bordercolorchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **BorderColor** property is changed. The BorderColor property indicates the color of the 2D border.

 

The event handler receives an argument of type **EventArgs**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [// Set the BorderStyle property to \'FixedSingle\' to view the 2D border color. ]                                                                                                    |
|                                                                                                                                                                                                                                         |
| [this][.statusBarAdv1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]                                          |
|                                                                                                                                                                                                                                         |
| [// Set the border color for the StatusBarAdv control using the BorderColor property.]                                                                                                |
|                                                                                                                                                                                                                                         |
| [this][.statusBarAdv1.BorderColor = System.Drawing.[Color].DeepPink;]                                                         |
|                                                                                                                                                                                                                                         |
| [// Handle the BorderColorChanged event.]                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [this][.statusBarAdv1.BorderColorChanged+=[new] [EventHandler](statusBarAdv1_BorderColorChanged);]       |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [private][ [void] statusBarAdv1_BorderColorChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [// Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                         |
|                                                                                                                                                                                                                                         |
| [Console][.WriteLine([\" BorderColorChanged event is raised \"]);]                                                          |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Set the BorderStyle property to \'FixedSingle\' to view the 2D border color. ]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [Me][.statusBarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Set the border color for the StatusBarAdv control using the BorderColor property. ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                               |
| [Me][.statusBarAdv1.BorderColor = System.Drawing.Color.DeepPink ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Handle the BorderColorChanged event. ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                               |
| [AddHandler][ [Me].statusBarAdv1.BorderColorChanged, [AddressOf] statusBarAdv1_BorderColorChanged ]                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] statusBarAdv1_BorderColorChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                               |
| [    [\' Below line will be displayed in the output window at run-time, when this event is fired. ]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [    Console.WriteLine([\" BorderColorChanged event is raised \"])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

