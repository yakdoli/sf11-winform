---
title: chartcell.md
original_path: WinForms_Docs/04_Controls/Chart/chartcell.md
created_at: 2025-08-05
---






##### Chart Cell {#chart-cell style="tab-stops: 0pt"}

 

Essential Chart control can be embedded in grid cells by creating and registering a custom Chart Cell cell type. The **CellModel** class handles any serialization that a cell type requires, and also creates the CellRenderer class associated with the cell type.

 

The actions mentioned can be performed by using the following code example.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [ChartStyleProperties][ csp;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                              |
| [this][.gridControl1.CellModels.Add([\"ChartCell\"], [new] [GridChartCellModel]([this].gridControl1.Model));] |
|                                                                                                                                                                                                                                                                                              |
| [style = [this].gridControl1\[8, 2\];]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [style.CellType = [\"ChartCell\"];]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [csp = [new] [ChartStyleProperties](style);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| [csp.ChartType = ChartSeriesType.Column;]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| [csp.TitleText = [\"Chart Cell\"];]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [csp.Series3D = [false];]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| [csp.TitleAlignment = [StringAlignment].Center;]                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [Dim][ csp [As] ChartStyleProperties]                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [Me][.gridControl1.CellModels.Add([\"ChartCell\"], [New] GridChartCellModel([Me].gridControl1.Model))] |
|                                                                                                                                                                                                                                                               |
| [style = [Me].gridControl1(8, 2)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [style.CellType = [\"ChartCell\"]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [csp = [New] ChartStyleProperties(style)]                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [csp.ChartType = ChartSeriesType.Column]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [csp.TitleText = [\"Chart Cell\"]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [csp.Series3D = [False]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [csp.TitleAlignment = StringAlignment.Center]                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][115][: Chart Cell]*

 

[]{#p104} 

 

[]{#related-topics}

