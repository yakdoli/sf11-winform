---
title: settingcolumnwidthsandrowheights.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingcolumnwidthsandrowheights.md
created_at: 2025-07-03
---






##### Setting Column Widths and Row Heights {#setting-column-widths-and-row-heights style="tab-stops: 0pt"}

[] 

The **GridControl.ColWidths** and **GridControl.RowHeights** collections will allow you to programmatically set the width of a column and / or the height of a row.

[] 


{border="0"}Note:[ ]Before you can use GridDataBoundGrid.Model.ColWidths to explicitly set column widths in a Grid Data Bound Grid, you must first set GridDataBoundGrid.AllowResizeToFit to false. Otherwise, the grid will try to size columns based on the width of the header text.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                  |
|                                                                                                                                                 |
| []                                                                                            |
|                                                                                                                                                 |
| [// Set the width of column 3.       ]                                                        |
|                                                                                                                                                 |
| [this][.gridControl1.ColWidths\[3\] = 40; ]  |
|                                                                                                                                                 |
| []                                                                                            |
|                                                                                                                                                 |
| [// Set the height of row 4.     ][   ]     |
|                                                                                                                                                 |
| [this][.gridControl1.RowHeights\[4\] = 40; ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| []                                                                                          |
|                                                                                                                                               |
| [\' Set the width of column 3.   ][     ] |
|                                                                                                                                               |
| [Me][.GridControl1.ColWidths(3) = 40   ]   |
|                                                                                                                                               |
| []                                                                                          |
|                                                                                                                                               |
| [\' Set the height of row 4.]                                                               |
|                                                                                                                                               |
| [Me][.GridControl1.RowHeights(4) = 40 ]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[{border="0"}][]

[] 

*[Figure ][175][: Grid After Sizing Column 3 and Row 4]*

 

[]{#p330} 

 

[]{#related-topics}

