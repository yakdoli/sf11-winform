---
title: 12excelexport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\12excelexport.md
created_at: 2025-07-03
---








  









### 1.2 Excel Export {#excel-export style="tab-stops: 0pt"}

BI Grid for Silverlight can be exported as an XLS file using Essential XlsIO.

 

Call Export method

The GridExcelExport class provides support for exporting data from OLAP Grid to an Excel spreadsheet for verification and/or computation. The following dll should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.OlapGridConverter.Silverlight

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [//// Export to Excel.]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [SaveFileDialog][ saveFileDialog = [new] [SaveFileDialog] { DefaultExt = [\".xls\"], Filter = [\"(\*.xls)\|\*.xls\"] };]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [if][ (saveFileDialog.ShowDialog() == [true])\                                                                                                                                                                                                                                                                                                                                                                                         |
| {\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     [Stream] stream = saveFileDialog.OpenFile();\                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     [GridExcelExport] gridExcelExport  = [new] [GridExcelExport]([this.] olapGrid.OlapDataManager.PivotEngine, [this].olapGrid.GridStyleInfo, [this].olapGrid.Layout, [this].olapGrid.OlapDataManager.ItemSource == [null] ? [false] : [true]);] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    gridExcelExport.Export(stream);\                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     stream.Close();\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [' Export to Excel.]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ saveFileDialog [As New] SaveFileDialog() With { \_]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        Key .DefaultExt = ][\".xls\"][, \_]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        Key .Filter = ][\"(\*.xls)\|\*.xls\"][ ][\_]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [If][ saveFileDialog.ShowDialog() = [True] [Then]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Dim] stream [As ]Stream = saveFileDialog.OpenFile()]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        [Dim] gridExcelExport  [As New] GridExcelExport([Me]. olapGrid.OlapDataManager.PivotEngine, Me.olapGrid.GridStyleInfo, [Me].olapGrid.Layout, If(Me.olapGrid.OlapDataManager.ItemSource Is Nothing, [False], [True]))] |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        ][gridExcelExport][.Export(stream)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        stream.Close()]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

*[]* 

[]{#related-topics}

