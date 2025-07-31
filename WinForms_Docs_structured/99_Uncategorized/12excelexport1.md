---
title: 12excelexport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\12excelexport1.md
created_at: 2025-07-03
---








  









### 1.2 Excel Export {#excel-export style="tab-stops: 0pt"}

BI Pivot Grid for Silverlight can be exported as an XLS file using Essential XlsIO. The user can export the contents of the PivotGrid to the Excel document for further archival, references and analysis purposes.

 

Call Export Method

The [GridExcelExport][ ]class provides support for exporting data from a PivotGrid to an Excel spreadsheet for verification and/or computation. The following dlls should be added, along with the default dlls in the reference folder:

 

[·      ]Syncfusion.PivotGridConverter.Silverlight

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                               |
| [//// Export to Excel]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                               |
| [SaveFileDialog][ saveFileDialog = [new] [SaveFileDialog] { DefaultExt = [\".xls\"], Filter = [\"(\*.xls)\|\*.xls\"] };] |
|                                                                                                                                                                                                                                                                                                               |
| [if][ (saveFileDialog.ShowDialog() == [true])\                                                                                                                                                                                          |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [{\                                                                                                                                                                                                                                                                                                           |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [    [Stream] stream = saveFileDialog.OpenFile();\                                                                                                                                                                                                                                    |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [    [GridExcelExport] exportToXls = [new] [GridExcelExport]([this].pivotGrid1);\                                                                                                                                   |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [    exportToXls.Export(stream);\                                                                                                                                                                                                                                                                             |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [    stream.Close();\                                                                                                                                                                                                                                                                                         |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                   |
| [' Export to Excel]                                                                                                             |
|                                                                                                                                                                                   |
| [Dim][ saveFileDialog [As New] SaveFileDialog() With { \_]              |
|                                                                                                                                                                                   |
| [        Key .DefaultExt = [\".xls\"], \_]                                                                            |
|                                                                                                                                                                                   |
| [        Key .Filter = [\"(\*.xls)\|\*.xls\"] \_]                                                                     |
|                                                                                                                                                                                   |
| [}]                                                                                                                                           |
|                                                                                                                                                                                   |
| [If][ saveFileDialog.ShowDialog() = [True] [Then]] |
|                                                                                                                                                                                   |
| [        [Dim] stream [As ]Stream = saveFileDialog.OpenFile()]                                      |
|                                                                                                                                                                                   |
| [        [Dim] gridExcelExport  [As New] GridExcelExport([Me].pivotGrid1)]     |
|                                                                                                                                                                                   |
| [        gridExcelExport.Export(stream)]                                                                                                      |
|                                                                                                                                                                                   |
| [        stream.Close()]                                                                                                                      |
|                                                                                                                                                                                   |
| [End][ [If]]                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 17: Exported Excel document from PivotGrid

**[]** 

**[]** 

[]{#related-topics}

