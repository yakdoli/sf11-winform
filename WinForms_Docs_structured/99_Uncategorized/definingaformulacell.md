---
title: definingaformulacell.md
original_path: WinForms_Docs/99_Uncategorized/definingaformulacell.md
created_at: 2025-08-05
---






##### Defining a FormulaCell[] {#defining-a-formulacell style="tab-stops: 0pt"}

[] 

You can use FormulaCells for every cell in a grid or for just a few cells. Even if you assign a **CellType** FormulaCell to every cell in a grid, the default behavior is to treat such cells as text box cells unless you start the cell entry with an equal sign. If the cell value starts with an equal sign then, the cell is considered as a formula cell and its contents are treated as such.

 

To make all cells present in a grid as potential formula cells, you will have to set the CellType of the standard **BaseStyle** to a FormulaCell using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [// Set up a Formula Cell.]                                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [this][.gridControl1.BaseStylesMap\[[\"Standard\"]\].StyleInfo.CellType = [\"FormulaCell\"];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                          |
| ['Set up a Formula Cell.]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.GridControl1.BaseStylesMap(][\"Standard\"][). StyleInfo.CellType = ][\"FormulaCell\"] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p20} 

[]{#related-topics}

