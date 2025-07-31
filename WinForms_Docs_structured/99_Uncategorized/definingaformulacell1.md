---
title: definingaformulacell1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingaformulacell1.md
created_at: 2025-07-03
---






##### Defining a FormulaCell {#defining-a-formulacell style="tab-stops: 0pt"}

[] 

You can use Formula Cells for every cell in a grid or for just a few cells. Even if you set the **CellType** property to *FormulaCell* to every cell in a grid, the default behavior is to treat such cells as text box cells, unless you start the cell entry with an equal sign. If the cell value starts with an equal sign, then the cell is considered as a formula cell and its contents are treated as such.

[] 

To make all cells present in a grid as potential formula cells, you will have to set the cell type of the standard **BaseStyle** to FormulaCell by using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [// Set up a Formula Cell.]                                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [this][.gridControl1.BaseStylesMap\[[\"Standard\"]\].StyleInfo.CellType = [\"FormulaCell\"];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [\'  Set up a Formula Cell.]                                                                                                                                                |
|                                                                                                                                                                                                                               |
| [Me][.gridControl1.BaseStylesMap([\"Standard\"]).StyleInfo.CellType = [\"FormulaCell\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p116} 

 

[]{#related-topics}

