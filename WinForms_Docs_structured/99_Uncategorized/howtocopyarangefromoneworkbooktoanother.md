---
title: howtocopyarangefromoneworkbooktoanother.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocopyarangefromoneworkbooktoanother.md
created_at: 2025-07-03
---








  









### How to copy a range from one workbook to another? {#how-to-copy-a-range-from-one-workbook-to-another style="tab-stops: 0pt"}

 

The Range and CopyTo methods include overloads for copying the Source Worksheet range to the Destination Worksheet range. The following code example illustrates how to copy a range from one workbook to another workbook.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [// The first worksheet object in the worksheets collection in the Source Workbook is accessed. ]             |
|                                                                                                                                                                 |
| [IWorksheet][ SourceWorksheet = SourceWorkbook.Worksheets\[0\];]           |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [// The first worksheet object in the worksheets collection in the Destination Workbook is accessed. ]        |
|                                                                                                                                                                 |
| [IWorksheet][ DestinationWorksheet = DestinationWorkbook.Worksheets\[0\];] |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [// Assigning an object to the range of cells (90 rows) both for source and destination.]                     |
|                                                                                                                                                                 |
| [IRange][ source = SourceWorksheet.Range\[1, 1, 90, 100\];]                |
|                                                                                                                                                                 |
| [IRange][ des = DestinationWorksheet.Range\[1, 1, 90, 100\];]              |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [// Copying (90 rows) from Source to Destination worksheet.]                                                  |
|                                                                                                                                                                 |
| [source.CopyTo(des);]                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                        |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' The first worksheet object in the worksheets collection in the Source Workbook is accessed. ]                                                         |
|                                                                                                                                                                                                             |
| [Dim][ SourceWorksheet [As] Syncfusion.XlsIO.IWorksheet = SourceWorkbook.Worksheets(0)]           |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' The first worksheet object in the worksheets collection in the Destination Workbook is accessed. ]                                                    |
|                                                                                                                                                                                                             |
| [Dim][ DestinationWorksheet [As] Syncfusion.XlsIO.IWorksheet = DestinationWorkbook.Worksheets(0)] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' Assigning an object to the range of cells (90 rows) both for source and destination. ]                                                                |
|                                                                                                                                                                                                             |
| [Dim][ source [As] Syncfusion.XlsIO.IRange = SourceWorksheet.Range(1, 1, 90, 100)]                |
|                                                                                                                                                                                                             |
| [Dim][ des [As] Syncfusion.XlsIO.IRange = DestinationWorksheet.Range(1, 1, 90, 100)]              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' Copying (90 rows) from Source to Destination worksheet. ]                                                                                             |
|                                                                                                                                                                                                             |
| [source.CopyTo(des)]                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

