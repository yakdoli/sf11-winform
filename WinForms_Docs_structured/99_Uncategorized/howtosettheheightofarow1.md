---
title: howtosettheheightofarow1.md
original_path: WinForms_Docs/99_Uncategorized/howtosettheheightofarow1.md
created_at: 2025-08-05
---








  









### How to Set the Height of a Row {#how-to-set-the-height-of-a-row style="tab-stops: 0pt"}

[] 

Introduction

[] 

To explicitly set the height of a particular row, use the **Model.RowHeights** collection.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [// Set height of row 3 to 40.\                                                                                                                                                                                |
| ][this][.gridDataBoundGrid1.Model.RowHeights\[3\] = 40; ] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [// Set height of header row 30.]                                                                                                                            |
|                                                                                                                                                                                                                |
| [this][.gridDataBoundGrid1.Model.RowHeights\[0\] = 30; ]                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                        |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [\' Set height of row 3 to 40.\                                                                                                                                                                           |
| ][Me][.GridDataBoundGrid1.Model.RowHeights(3) = 40 ] |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [\' Set height of header row 30.]                                                                                                                       |
|                                                                                                                                                                                                           |
| [Me][.GridDataBoundGrid1.Model.RowHeights(0) = 30 ]                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p600} 

 

[]{#related-topics}

