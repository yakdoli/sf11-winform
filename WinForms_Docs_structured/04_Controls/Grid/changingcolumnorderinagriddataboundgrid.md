---
title: changingcolumnorderinagriddataboundgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\changingcolumnorderinagriddataboundgrid.md
created_at: 2025-07-03
---






#### Changing Column Order in a Grid Data Bound Grid {#changing-column-order-in-a-grid-data-bound-grid style="tab-stops: 0pt"}

[] 

The simplest way to change the column order in a Grid Data Bound Grid is to use the **GridDataBoundGrid.Model.Cols.MoveRange** method. This method will rearrange the columns that are based on from and to and count the parameters passed into it.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                                                      |
|                                                                                                                                                               |
| [// Move columns 4 and 5, to column 1.]                                                                     |
|                                                                                                                                                               |
| [this][.gridDataBoundGrid1.Model.Cols.MoveRange(4, 2, 1);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [\' Move columns 4 and 5, to column 1.]                                                                  |
|                                                                                                                                                            |
| [Me][.GridDataBoundGrid1.Model.Cols.MoveRange(4, 2, 1)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p373} 

 

[]{#related-topics}

