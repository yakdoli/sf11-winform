---
title: linklabelcell.md
original_path: WinForms_Docs/99_Uncategorized/linklabelcell.md
created_at: 2025-08-05
---






##### Link Label Cell {#link-label-cell style="tab-stops: 0pt"}

[] 

The Link Label Cell cell type holds the link that has been provided in the **Tag** property. This displays ordinary text in the cell which links to the specified location.

 

The following code examples illustrate how to set the cell type to LinkLabelCell.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].LinkLabelCell);] |
|                                                                                                                                                                                                    |
| [int][ rowIndex = 5;]                                                                                         |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].CellType = [CustomCellTypes].LinkLabelCell.ToString();]                                                   |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].Text = [\"Syncfusion, Inc.\"];]                                                                           |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].Font.Bold = [true];]                                                                                         |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].Tag = [\"http://www.syncfusion.com\"];]                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.LinkLabelCell)]                                                  |
|                                                                                                                                                                    |
| [Dim][ rowIndex [As] [Integer] = 5] |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).CellType = CustomCellTypes.LinkLabelCell.ToString()]                                                |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).Text = [\"Syncfusion, Inc.\"]]                                              |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).Font.Bold = [True]]                                                            |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).Tag = [\"http://www.syncfusion.com\"]]                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][111][: \"Link Label Cell\" Cells]*

 

[]{#p100} 

 

[]{#related-topics}

