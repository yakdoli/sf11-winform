---
title: howtoopenanexcelfilefromstream.md
original_path: WinForms_Docs/99_Uncategorized/howtoopenanexcelfilefromstream.md
created_at: 2025-08-05
---








  









### How to open an Excel file from Stream? {#how-to-open-an-excel-file-from-stream style="tab-stops: 0pt"}

 

XlsIO provides support for opening a template spreadsheet that is stored as a stream. The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [// Opening a File from a Stream.]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [FileStream fs = [new] FileStream([@\"..\\..\\..\\..\\..\\Data\\OpenFromStreamTemplate.xls\"], FileMode.Open, FileAccess.ReadWrite, FileShare.ReadWrite);] |
|                                                                                                                                                                                                                                             |
| [fs.Seek(0, SeekOrigin.Begin);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [IWorkbook][ workbook = application.Workbooks.Open(fs);]                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Opening a File from a Stream.]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [Dim][ fs [As] FileStream = [New] FileStream([\"..\\..\\..\\..\\..\\Data\\OpenFromStreamTemplate.xls\"], FileMode.Open, FileAccess.ReadWrite, FileShare.ReadWrite)] |
|                                                                                                                                                                                                                                                                                                                           |
| [fs.Seek(0, SeekOrigin.Begin)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| [Dim][ workbook [As] IWorkbook = application.Workbooks.Open(fs)]                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

