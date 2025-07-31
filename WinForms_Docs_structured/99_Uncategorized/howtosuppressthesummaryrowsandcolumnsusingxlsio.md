---
title: howtosuppressthesummaryrowsandcolumnsusingxlsio.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosuppressthesummaryrowsandcolumnsusingxlsio.md
created_at: 2025-07-03
---








  









### How to suppress the summary rows and columns using XlsIO? {#how-to-suppress-the-summary-rows-and-columns-using-xlsio style="tab-stops: 0pt"}

 

You can suppress the summary rows and columns by using the IsSummaryRowBelow and IsSummaryColumnRight properties. The following code example illustrates this.

 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                            |
| []                                                       |
|                                                                                                            |
| [// Suppress the summary rows at the bottom.]            |
|                                                                                                            |
| [sheet.PageSetup.IsSummaryRowBelow = [false];]    |
|                                                                                                            |
| [// Suppress the summary columns to the right.]          |
|                                                                                                            |
| [sheet.PageSetup.IsSummaryColumnRight = [false];] |
+------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                      |
|                                                                                                           |
| []                                                                    |
|                                                                                                           |
| [\' Suppress the summary rows at the bottom.]           |
|                                                                                                           |
| [sheet.PageSetup.IsSummaryRowBelow = [False]]    |
|                                                                                                           |
| [\' Suppress the summary columns to the right.]         |
|                                                                                                           |
| [sheet.PageSetup.IsSummaryColumnRight = [False]] |
+-----------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

