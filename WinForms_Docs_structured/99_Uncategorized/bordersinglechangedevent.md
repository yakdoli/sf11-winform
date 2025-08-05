---
title: bordersinglechangedevent.md
original_path: WinForms_Docs/99_Uncategorized/bordersinglechangedevent.md
created_at: 2025-08-05
---






##### BorderSingleChanged Event {#bordersinglechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is handled, when the value of the **BorderSingle** property is changed. The BorderSingle property indicates the 2D border style.

 

The event handler receives an argument of type **EventArgs**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [// Set the BorderStyle property to \'FixedSingle\' to view the 2D border style. ]                                                                                                     |
|                                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]                                           |
|                                                                                                                                                                                                                                          |
| [// Set the new 2D border style for the StatusBarAdv control using the BorderStyle property.]                                                                                          |
|                                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dotted;]                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [// Handle the BorderSingleChanged event.]                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [this][.statusBarAdv1.BorderSingleChanged+=[new] [EventHandler](statusBarAdv1_BorderSingleChanged);]      |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [private][ [void] statusBarAdv1_BorderSingleChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [Console][.WriteLine([\" BorderSingleChanged event is raised \"]);]                                                          |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Set the BorderStyle property to \'FixedSingle\' to view the 2D border style. ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.statusBarAdv1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle ]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Set the new 2D border style for the StatusBarAdv control using the BorderStyle property. ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.statusBarAdv1.BorderSingle = System.Windows.Forms.ButtonBorderStyle.Dotted ]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Handle the BorderSingleChanged event. ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| [AddHandler][ [Me].statusBarAdv1.BorderSingleChanged, [AddressOf] statusBarAdv1_BorderSingleChanged ]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] statusBarAdv1_BorderSingleChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [    [\' The below line will be displayed in the output window at runtime. ]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [    Console.WriteLine([\" BorderSingleChanged event is raised \"])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

