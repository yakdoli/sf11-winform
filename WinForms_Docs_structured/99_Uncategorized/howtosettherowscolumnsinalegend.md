---
title: howtosettherowscolumnsinalegend.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosettherowscolumnsinalegend.md
created_at: 2025-07-03
---






##### How to set the rows/columns in a legend? {#how-to-set-the-rowscolumns-in-a-legend style="tab-stops: 0pt"}

[] 

You can use the RowsCount and ColumnsCount property to create the rows or the columns of an OlapChart legend. The RowsCount and ColumnsCount will internally be used to create a Grid layout control to place the legends. The following code snippet shows how to set the number of rows or columns in an OlapLegend:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][OlapChart.Legend][\>]\                                                                                              |
| [    ][\<][baseChart][:][ChartLegend][ Background][=\"Transparent\"][ ] |
|                                                                                                                                                                                                                                                        |
| [                           RowsCount][=\"2\"][ ColumnsCount][=\"2\" /\>]\                                                                                           |
| [\</][syncfusion][:][OlapChart.Legend][\>]                                                                                              |
|                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------+
| **\[C#\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [this].olapChart.Legend.RowsCount = 2;\          |
| [this].olapChart.Legend.ColumnsCount = 2;        |
|                                                                       |
|                                                                       |
+-----------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------+
| **\[VB\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [Me].olapChart.Legend.RowsCount = 2              |
|                                                                       |
| [Me].olapChart.Legend.ColumnsCount = 2           |
|                                                                       |
|                                                                       |
+-----------------------------------------------------------------------+


 

[{border="0"}]Note: The RowsCount and the ColumnsCount is used to create the rows and the columns in the Grid layout control, which is used to place the legends. If you give extra row or column count than the legend availability then it will display empty spaces to fill the structure of the grid. The following illustration explains this in detail.


**** 

The following chart has only one legend, but we have set RowsCount = 2 and ColumnsCount = 2. Therefore, the resultant legend will appear as follows:

 

[] 

{border="0"}

Figure 38: Legend with RowsCount=2, ColumnsCount=2, and ChartDock.Top[]

[] 

***[]*** 

***[]*** 

{border="0"}

Figure 39:  Legend with RowsCount=2, ColumnsCount=2, and ChartDock.Right**[]**

***[]*** 

**[]** 

***[]*** 

***[]*** 

{border="0"}

Figure 40: Legend with RowsCount=2, ColumnsCount=2, and ChartDock.Left**[]**

***[]*** 

***[]*** 

{border="0"}

Figure 41: Legend with RowsCount=2, ColumnsCount=2, and ChartDock.Bottom**[]**

[] 

[]{#related-topics}

