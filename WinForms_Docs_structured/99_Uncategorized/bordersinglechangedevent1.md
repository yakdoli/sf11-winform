---
title: bordersinglechangedevent1.md
original_path: WinForms_Docs/99_Uncategorized/bordersinglechangedevent1.md
created_at: 2025-08-05
---






##### BorderSingleChanged Event {#bordersinglechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **BorderSingle** property is changed. The BorderSingle property indicates the 2D border style.

 

The event handler receives an argument of type **EventArgs**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [// Set the new 2D border style for the StatusBarAdvPanel control using the BorderStyle property.]                                                                                          |
|                                                                                                                                                                                                                                               |
| [this][.statusBarAdvPanel1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dotted;]                                         |
|                                                                                                                                                                                                                                               |
| [// Set the BorderStyle property to \'FixedSingle\' to view the 2D border style. ]                                                                                                          |
|                                                                                                                                                                                                                                               |
| [this][.statusBarAdvPanel1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]                                           |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [// Handle the BorderSingleChanged event.]                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| [this][.statusBarAdvPanel1.BorderSingleChanged+=[new] [EventHandler](statusBarAdvPanel1_BorderSingleChanged);] |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [private][ [void] statusBarAdvPanel1_BorderSingleChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [Console][.WriteLine([\" BorderSingleChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Set the new 2D border style for the StatusBarAdvPanel control using the BorderStyle property. ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                     |
| [Me][.statusBarAdvPanel1.BorderSingle = System.Windows.Forms.ButtonBorderStyle.Dotted ]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Set the BorderStyle property to \'FixedSingle\' to view the 2D border style. ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [Me][.statusBarAdvPanel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle ]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Handle the BorderSingleChanged event. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                     |
| [AddHandler][ [Me].statusBarAdvPanel1.BorderSingleChanged, [AddressOf] statusBarAdvPanel1_BorderSingleChanged ]                                                                                      |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] statusBarAdvPanel1_BorderSingleChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                     |
| [    [\' The below line will be displayed in the output window at runtime. ]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                     |
| [    Console.WriteLine([\" BorderSingleChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

