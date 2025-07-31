---
title: silentprinting1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\silentprinting1.md
created_at: 2025-07-03
---






#### Silent Printing {#silent-printing style="tab-stops: 0pt"}

PrintDocument property of PdfViewerControl returns System.Windows.Documents.FixedDocument that helps to complete print using PrintDialog. The following are the code snippets.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| [PrintDialog][ dialog = [new] [PrintDialog]();] |
|                                                                                                                                                                                      |
| [dialog.PageRangeSelection = [PageRangeSelection].AllPages;]                                                             |
|                                                                                                                                                                                      |
| [            dialog.PrintDocument(pdfViewerControl1.PrintDocument.DocumentPaginator, [\"PDF\"]);]                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                        |
| [Dim][ dialog [As] [New] PrintDialog()] |
|                                                                                                                                                                        |
| [dialog.PageRangeSelection = PageRangeSelection.AllPages]                                                                          |
|                                                                                                                                                                        |
| [      ]                                                                                                                           |
|                                                                                                                                                                        |
| [dialog.PrintDocument(pdfViewerControl1.PrintDocument.DocumentPaginator, [\"PDF\"])]                       |
|                                                                                                                                                                        |
| []                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

