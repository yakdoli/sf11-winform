---
title: gridincell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\gridincell.md
created_at: 2025-07-03
---






##### GridInCell {#gridincell style="tab-stops: 0pt"}

[] 

The GridInCell cell type provide a covered range of cells to embed the grid, which is added as a control to the cells. The registered cell model will initialize the range by calculating the size of the grid control to be embedded, and add some style such as borders and scroll bar to have the control within the range.

 

The following code examples illustrate how to set the cell type to GridinCell.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].GridinCell);] |
|                                                                                                                                                                                                 |
| [gridControl1.BackColor = [Color].FromArgb(0xda, 0xe5, 0xf5);]                                                                      |
|                                                                                                                                                                                                 |
| [GridControl][ grid;]                                                                                   |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [this][.gridControl1\[3, 2\].CellType = [CustomCellTypes].GridinCell.ToString();]  |
|                                                                                                                                                                                                 |
| [this][.gridControl1.CoveredRanges.Add([GridRangeInfo].Cells(3, 2, 7, 4));]        |
|                                                                                                                                                                                                 |
| [grid = [new] [CellEmbeddedGrid]([this].gridControl1);]                                   |
|                                                                                                                                                                                                 |
| [grid.BackColor = [Color].FromArgb(0xb4, 0xe7, 0xf2);]                                                                              |
|                                                                                                                                                                                                 |
| [grid.RowCount = 10;]                                                                                                                                       |
|                                                                                                                                                                                                 |
| [grid.ColCount = 4;]                                                                                                                                        |
|                                                                                                                                                                                                 |
| [grid\[1, 1\].Text = [\"this is a 10x4 grid\"];]                                                                                    |
|                                                                                                                                                                                                 |
| [grid.ThemesEnabled = [true];]                                                                                                         |
|                                                                                                                                                                                                 |
| [this][.gridControl1\[3, 2\].Control = grid;]                                                              |
|                                                                                                                                                                                                 |
| [this][.gridControl1.Controls.Add(grid);]                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [RegisterCellModel.GridCellType([Me].gridControl1, CustomCellTypes.GridinCell)]                        |
|                                                                                                                                                                 |
| [Dim][ grid [As] GridControl]                         |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [Me][.gridControl1(3, 2).CellType = CustomCellTypes.GridinCell.ToString()] |
|                                                                                                                                                                 |
| [Me][.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(3, 2, 7, 4))]     |
|                                                                                                                                                                 |
| [grid = [New] CellEmbeddedGrid([Me].gridControl1)]                                |
|                                                                                                                                                                 |
| [grid.BackColor = Color.FromArgb(&HB4, &HE7, &HF2)]                                                                         |
|                                                                                                                                                                 |
| [grid.RowCount = 10]                                                                                                        |
|                                                                                                                                                                 |
| [grid.ColCount = 4]                                                                                                         |
|                                                                                                                                                                 |
| [grid(1, 1).Text = [\"this is a 10x4 grid\"]]                                                       |
|                                                                                                                                                                 |
| [grid.ThemesEnabled = [True]]                                                                          |
|                                                                                                                                                                 |
| [Me][.gridControl1(3, 2).Control = grid]                                   |
|                                                                                                                                                                 |
| [Me][.gridControl1.Controls.Add(grid)]                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][110][: \"GridInCell\" Cells]*

 

[]{#p99} 

 

[]{#related-topics}

