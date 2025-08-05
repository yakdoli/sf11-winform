---
title: pdfexport2.md
original_path: WinForms_Docs/99_Uncategorized/pdfexport2.md
created_at: 2025-08-05
---








  









### PDF Export {#pdf-export style="tab-stops: 0pt"}

BI Grid for Silverlight can be exported as a PDF file using Essential PDF.

 

Call Export method

The GridPdfExport class provides support for exporting data from OLAP Grid to a PDF document for verification. The following dll should be added, along with the default dlls  in the reference folder:

 

[·      ]Syncfusion.OlapGridConverter.Silverlight

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                               |
| [//// Export to PDF.]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                               |
| [SaveFileDialog][ saveFileDialog = [new] [SaveFileDialog] { DefaultExt = [\".pdf\"], Filter = [\"(\*.pdf)\|\*.pdf\"] };] |
|                                                                                                                                                                                                                                                                                                               |
| [if][ (saveFileDialog.ShowDialog() == [true])\                                                                                                                                                                                          |
| {\                                                                                                                                                                                                                                                                                                            |
|     [Stream] stream = saveFileDialog.OpenFile();\                                                                                                                                                                                                                                     |
|     [GridPdfExport] exporttopdf = [new] [GridPdfExport]([this]. olapGrid.OlapDataManager.PivotEngine, [this].olapGrid.GridStyleInfo);]                     |
|                                                                                                                                                                                                                                                                                                               |
| [    exporttopdf.Export(stream);\                                                                                                                                                                                                                                                                             |
|     stream.Close();\                                                                                                                                                                                                                                                                                          |
| }]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [' Export to PDF.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [Dim][ saveFileDialog [As New] SaveFileDialog() With { \_]                                                                                     |
|                                                                                                                                                                                                                                                          |
| [        Key .DefaultExt = ][\".pdf\"][, \_]                                                                                 |
|                                                                                                                                                                                                                                                          |
| [        Key .Filter = ][\"(\*.pdf)\|\*.pdf\"][ ][\_]                                    |
|                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [If][ saveFileDialog.ShowDialog() = [True] [Then]]                                                                        |
|                                                                                                                                                                                                                                                          |
| [        [Dim] stream [As ]Stream = saveFileDialog.OpenFile()]                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [        [Dim] gridPdfExport [As New \_ ]GridPdfExport([Me].olapGrid.OlapDataManager.PivotEngine, [Me].olapGrid.GridStyleInfo);] |
|                                                                                                                                                                                                                                                          |
| [        ][gridPdfExport][.Export(stream)]                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [        stream.Close()]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

