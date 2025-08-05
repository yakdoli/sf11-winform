---
title: floatingcells.md
original_path: WinForms_Docs/99_Uncategorized/floatingcells.md
created_at: 2025-08-05
---






#### Floating Cells {#floating-cells style="tab-stops: 0pt"}

[] 

Floating cells[ ]are those cells whose content floats over empty, adjacent cells. You can enable floating cells at the grid level by setting the **GridControl.FloatCellsMode**.

 

Setting this property to the GridFloatCellsMode.BeforeDisplayCalculation will force the floating cells to always be calculated just prior to being displayed. Setting the property to the GridFloatCellsMode.OnDemandCalculation will calculate the floating cells only if the cell contents or size changes. This latter option is more efficient.

 

You can control a cell whether or not it  floats over adjacent cells through the **FloatCell** property in the cell\'s **GridStyleInfo** object. You can also prevent a cell from being flooded by using its **GridStyleInfo.FloodCell** property. In the code given below, all three lines (1, 3, 5) hold the same text in column one. But, the floating cells in lines three and five are stopped short; line three by an occupied cell and line five by a **FloodCell** false settings.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [// Enable Float Cells.]                                                                                                                              |
|                                                                                                                                                                                                         |
| [this][.gridControl1.FloatCellsMode = [GridFloatCellsMode].OnDemandCalculation;]           |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [// Specify Cell Text.]                                                                                                                               |
|                                                                                                                                                                                                         |
| [this][.gridControl1\[1, 1\].Text = [\"This is a text that floats over several cells.\"];] |
|                                                                                                                                                                                                         |
| [this][.gridControl1\[3, 1\].Text = [\"This is a text that floats over several cells.\"];] |
|                                                                                                                                                                                                         |
| [this][.gridControl1\[5, 1\].Text = [\"This is a text that floats over several cells.\"];] |
|                                                                                                                                                                                                         |
| [this][.gridControl1\[3, 3\].Text = [\"3.14159\"];]                                        |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [// Code to prevent cell(5,2) from being flooded.]                                                                                                    |
|                                                                                                                                                                                                         |
| [this][.gridControl1\[5, 2\].FloodCell = [false];]                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [\' Enable Float Cells.]                                                                                                                         |
|                                                                                                                                                                                                    |
| [Me][.gridControl1.FloatCellsMode = GridFloatCellsMode.OnDemandCalculation]                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [\' Specify Cell Text.]                                                                                                                          |
|                                                                                                                                                                                                    |
| [Me][.gridControl1(1, 1).Text = [\"This is a text that floats over several cells.\"]] |
|                                                                                                                                                                                                    |
| [Me][.gridControl1(3, 1).Text = [\"This is a text that floats over several cells.\"]] |
|                                                                                                                                                                                                    |
| [Me][.gridControl1(5, 1).Text = [\"This is a text that floats over several cells.\"]] |
|                                                                                                                                                                                                    |
| [Me][.gridControl1(3, 3).Text = [\"3.14159\"]]                                        |
|                                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                                    |
| [\' Code to prevent cell(5,2) from being flooded.]                                                                                               |
|                                                                                                                                                                                                    |
| [Me][.gridControl1(5, 2).FloodCell = [False]]                                            |
|                                                                                                                                                                                                    |
| [Me][.gridControl1(2, 2).Font.Bold = [True]]                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][179][: Floating Cells]*

 

[]{#p337} 

 

[]{#related-topics}

