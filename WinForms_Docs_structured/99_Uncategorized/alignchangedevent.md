---
title: alignchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\alignchangedevent.md
created_at: 2025-07-03
---






##### AlignChanged Event {#alignchanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is fired when the value of the **Alignment** property is changed. The Alignment property indicates the alignment type of the text and icon of the panel.

 

The event handler receives an argument of type **EventArgs**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [// Set the alignment type for the text and icon of the StatusBarAdvPanel.]                                                                                                          |
|                                                                                                                                                                                                                                        |
| [this][.statusBarAdvPanel1.Alignment = System.Windows.Forms.[HorizontalAlignment].Right;]                                    |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [// Handle the AlignChanged event.]                                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [this][.statusBarAdvPanel1.AlignChanged+=[new] [EventHandler](statusBarAdvPanel1_AlignChanged);]        |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [private][ [void] statusBarAdvPanel1_AlignChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [// Below line will be displayed in the output window at runtime, when this event is fired.]                                                                                         |
|                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\" AlignChanged event is raised \"]);]                                                               |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Set the alignment type for the text and icon of the StatusBarAdvPanel. ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.statusBarAdvPanel1.Alignment = System.Windows.Forms.HorizontalAlignment.Right ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the AlignChanged event. ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [AddHandler][ [Me].statusBarAdvPanel1.AlignChanged, [AddressOf] statusBarAdvPanel1_AlignChanged ]                                                                                             |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] statusBarAdvPanel1_AlignChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [    [\' Below line will be displayed in the output window at runtime, when this event is fired. ]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                              |
| [    Console.WriteLine([\" AlignChanged event is raised \"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

