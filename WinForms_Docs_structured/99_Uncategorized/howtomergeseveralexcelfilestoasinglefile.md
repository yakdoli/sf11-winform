---
title: howtomergeseveralexcelfilestoasinglefile.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtomergeseveralexcelfilestoasinglefile.md
created_at: 2025-07-03
---








  









### How to merge several Excel files to a single file? {#how-to-merge-several-excel-files-to-a-single-file style="tab-stops: 0pt"}

 

XlsIO provides support to merge several Excel files to a single file. The following code example illustrates how to do this.

 

+----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                          |
| []                                                     |
|                                                                                                          |
| [// Merging worksheets.]                               |
|                                                                                                          |
| [destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets);] |
+----------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                    |
|                                                                                                         |
| []                                                                  |
|                                                                                                         |
| [\' Merging worksheets.]                              |
|                                                                                                         |
| [destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets)] |
+---------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

