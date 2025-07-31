---
title: silentprinting.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\silentprinting.md
created_at: 2025-07-03
---






#### Silent Printing {#silent-printing style="tab-stops: 0pt"}

PrintDocument property of PdfViewerControl returns System.Drawing.Printing.PrintDocument that helps to complete print using PrintDialog. The following are the code snippets:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| [PrintDialog][ dialog = [new] [PrintDialog]();] |
|                                                                                                                                                                                      |
| [dialog.AllowPrintToFile = [true];         ]                                                                                |
|                                                                                                                                                                                      |
| [dialog.Document = viewer.PrintDocument;]                                                                                                        |
|                                                                                                                                                                                      |
| [dialog.Document.Print();]                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                        |
| [Dim][ dialog [As] [New] PrintDialog()] |
|                                                                                                                                                                        |
| [dialog.AllowPrintToFile = [True]]                                                                            |
|                                                                                                                                                                        |
| [dialog.Document = viewer.PrintDocument]                                                                                           |
|                                                                                                                                                                        |
| [dialog.Document.Print()]                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

