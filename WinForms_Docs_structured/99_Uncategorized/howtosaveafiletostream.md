---
title: howtosaveafiletostream.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosaveafiletostream.md
created_at: 2025-07-03
---








  









### How to save a file to stream? {#how-to-save-a-file-to-stream style="tab-stops: 0pt"}

 

XlsIO provides support to save a spreadsheet to a .NET stream. The following code example illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [// Save the workbook to stream.]                                                                                                                          |
|                                                                                                                                                                                                              |
| [FileStream fs = [new] FileStream([\"FileStreamSample.xls\"], FileMode.Create, FileAccess.ReadWrite, FileShare.ReadWrite);] |
|                                                                                                                                                                                                              |
| [workbook.SaveAs(fs);]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [workbook.Close();]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                             |
| [\' Save the workbook to stream.]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [Dim][ fs [As] FileStream = [New] FileStream([\"FileStreamSample.xls\"], FileMode.Create, FileAccess.ReadWrite, FileShare.ReadWrite)] |
|                                                                                                                                                                                                                                                                                             |
| [workbook.SaveAs(fs)]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                             |
| [workbook.Close()]                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

