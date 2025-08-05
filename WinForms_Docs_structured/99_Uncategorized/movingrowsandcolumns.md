---
title: movingrowsandcolumns.md
original_path: WinForms_Docs/99_Uncategorized/movingrowsandcolumns.md
created_at: 2025-08-05
---






##### Moving Rows and Columns {#moving-rows-and-columns style="tab-stops: 0pt"}

[] 

The methods **GridControl.Rows.MoveRange** and**[ ]GridControl.Cols.MoveRange** are used to move rows and columns in a grid. The **MoveRange** method takes three parameters that are used to determine the start position, number of items to move and the target position.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [// Starting at row 7, move 2 rows to row 4.  ][      ] |
|                                                                                                                                                             |
| [this][.gridControl1.Rows.MoveRange(7, 2, 4); ]          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                                |
| []                                                                                           |
|                                                                                                                                                |
| [\' Starting at row 7, move 2 rows to row 4.      ]                                          |
|                                                                                                                                                |
| [Me][.GridControl1.Rows.MoveRange(7, 2, 4)] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[{border="0"}][]

[] 

*[Figure ][174][: Grid After Moving Rows 7 and 8 to Row 4]*

 

[]{#p329} 

 

[]{#related-topics}

