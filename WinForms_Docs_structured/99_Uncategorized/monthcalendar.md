---
title: monthcalendar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\monthcalendar.md
created_at: 2025-07-03
---






##### Month Calendar {#month-calendar style="tab-stops: 0pt"}

[] 

The **MonthCalendar** cell type lets you pick dates. To make use of this cell type in grid, set the **CellType** property to *MonthCalendar* and **CellValue** property to *DateTime* object.

[] 

The following code example illustrates how to set the cell type to MonthCalendar.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [// Set Cell Type.]                                                            |
|                                                                                                                                  |
| [gridControl1\[rowIndex, colIndex\].CellType = [\"MonthCalendar\"];] |
|                                                                                                                                  |
| []                                                                                           |
|                                                                                                                                  |
| [// Assign initial value.]                                                     |
|                                                                                                                                  |
| [gridControl1\[rowIndex, colIndex\].CellValue = [DateTime].Now;]     |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [\' Set Cell Type.]                                                         |
|                                                                                                                               |
| [gridControl1(rowIndex, colIndex).CellType = [\"MonthCalendar\"]] |
|                                                                                                                               |
| []                                                                        |
|                                                                                                                               |
| [\' Assign initial value.]                                                  |
|                                                                                                                               |
| [gridControl1(rowIndex, colIndex).CellValue = DateTime.Now]                               |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][84][: Month Calendar Cells]*

 

[]{#p60} 

 

[]{#related-topics}

