---
title: formulacell.md
original_path: WinForms_Docs/99_Uncategorized/formulacell.md
created_at: 2025-08-05
---






##### Formula Cell {#formula-cell style="tab-stops: 0pt"}

[] 

The **FormulaCell** cell type allows you to add algebraic formulas to a cell that depends on other cells. The cell value should be a well-formed formula starting with an \'=\' and the **CellType** property set to *FormulaCell*. If a Formula Cell does not begin with an \'=\', the cell is treated as a text box cell. For details, see [Formula Support].

[] 

The following code example illustrates how to set the cell type to FormulaCell.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| []                                                                              |
|                                                                                                                                                   |
| [// Set Cell Type as Formula Cell.]                                             |
|                                                                                                                                                   |
| [gridControl1\[rowIndex, colIndex\].CellType = [\"FormulaCell\"];]    |
|                                                                                                                                                   |
| []                                                                                            |
|                                                                                                                                                   |
| [// Assign a Formula.]                                                          |
|                                                                                                                                                   |
| [gridControl1\[rowIndex, colIndex\].CellValue = [\"= (A1+A2) / 2\"];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                                |
| []                                                                           |
|                                                                                                                                                |
| [\' Set Cell Type as Formula Cell.]                                          |
|                                                                                                                                                |
| [gridControl1(rowIndex, colIndex).CellType = [\"FormulaCell\"]]    |
|                                                                                                                                                |
| []                                                                         |
|                                                                                                                                                |
| [\' Assign a Formula.]                                                       |
|                                                                                                                                                |
| [gridControl1(rowIndex, colIndex).CellValue = [\"= (A1+A2) / 2\"]] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 79: Formula Cells shown as Text Boxes

[] 

{border="0"}

[] 

Figure 80: Same Cells shown as Formula Cells

 

[]{#p56} 

 

[]{#related-topics}

