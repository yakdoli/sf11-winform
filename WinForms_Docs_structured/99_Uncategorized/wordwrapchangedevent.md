---
title: wordwrapchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\wordwrapchangedevent.md
created_at: 2025-07-03
---








  









### WordWrapChanged Event {#wordwrapchanged-event style="tab-stops: 0pt"}

 

This event is fired when the value of the **WordWrapMode** property is changed. The WordWrapMode property specifies the mode of word wrapping.

 

The event handler receives an argument of type **EventArgs**.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [// Handle the WordWrapChanged event.]                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [this][.editControl1.WordWrapChanged+=[new] [EventHandler](editControl1_WordWrapChanged);]           |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [// Specify the mode of word wrapping.]                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [this][.editControl1.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.[WordWrapMode].WordWrapMargin;]                   |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [private][ [void] editControl1_WordWrapChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{  ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [// The below line will be displayed in the output window at runtime.]                                                                                                            |
|                                                                                                                                                                                                                                     |
| [Console][.WriteLine([\" WordWrapChanged event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Handle the WordWrapChanged event. ]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                           |
| [AddHandler][ [Me].editControl1.WordWrapChanged, [AddressOf] editControl1_WordWrapChanged ]                                                                                                |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Specify the mode of word wrapping. ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                           |
| [Me][.editControl1.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin ]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] editControl1_WordWrapChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                           |
| [\' The below line will be displayed in the output window at runtime.]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\" WordWrapChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p181} 

[] 

[]{#related-topics}

