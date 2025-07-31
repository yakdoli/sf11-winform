---
title: wordexport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\wordexport1.md
created_at: 2025-07-03
---








  









### Word Export {#word-export style="tab-stops: 0pt"}

BI Grid for Silverlight can be exported as a Word document using Essential DocIO.

 

Call Export method

The GridWordExport class provides support for exporting data from OLAP Grid to a Word document for verification. The following dll should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.OlapGridConverter.Silverlight

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                        |
| [//// Export to Word Document.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| [SaveFileDialog][ saveFileDialog  = [new] [SaveFileDialog] { DefaultExt = [\".doc\"], Filter = [\"(\*.doc)\|\*.doc\"] };\             |
| [if] (saveFileDialog.ShowDialog() == [true])\                                                                                                                                                                                                |
| {\                                                                                                                                                                                                                                                                                     |
|     [Stream] stream = saveFileDialog.OpenFile();\                                                                                                                                                                                                              |
|     [GridWordExport] gridWordExport = [new] [GridWordExport]([this].olapGrid.OlapDataManager.PivotEngine, [this].olapGrid.Layout);] |
|                                                                                                                                                                                                                                                                                        |
| [    gridWordExport.Export(stream, [this].olapGrid.GridStyleInfo);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                        |
| [    stream.Close();\                                                                                                                                                                                                                                                                  |
| }]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [' Export to Word.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                  |
| [Dim][ saveFileDialog [As New ]SaveFileDialog() With { \_]                                                                             |
|                                                                                                                                                                                                                                                  |
| [        Key .DefaultExt = ][\".doc\"][, \_]                                                                         |
|                                                                                                                                                                                                                                                  |
| [        Key .Filter = ][\"(\*.doc)\|\*.doc\"][ ][\_]                            |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [If][ saveFileDialog.ShowDialog() = [True] [Then]]                                                                |
|                                                                                                                                                                                                                                                  |
| [        [Dim] stream [As ]Stream = saveFileDialog.OpenFile()]                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [        [Dim] gridWordExport  [As New ]GridWordExport([Me].olapGrid.OlapDataManager.PivotEngine, [Me].olapGrid.Layout)] |
|                                                                                                                                                                                                                                                  |
| [        gridWordExport.Export(stream, [Me].olapGrid.GridStyleInfo);]                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [        stream.Close()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[]{#related-topics}

