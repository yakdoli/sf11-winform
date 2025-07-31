---
title: coloredit.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\coloredit.md
created_at: 2025-07-03
---






##### Color Edit {#color-edit style="tab-stops: 0pt"}

[] 

The **Color Edit** cell type allows you to pick colors and set a color object as the **CellValue**. To do this, you have to set the **CellType** property to *ColorEdit*.

[] 

The following code example illustrates how to set the cell type to ColorEdit.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                              |
| []                                                                         |
|                                                                                                                              |
| [// Set up a Color Edit control.]                                          |
|                                                                                                                              |
| [gridControl1\[rowIndex, colIndex\].CellType = [\"ColorEdit\"];] |
|                                                                                                                              |
| [gridControl1\[rowIndex, colIndex\].CellValue = [Color].Aqua;]   |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                        |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [\' Set up a Color Edit control.]                                       |
|                                                                                                                           |
| [gridControl1(rowIndex, colIndex).CellType = [\"ColorEdit\"]] |
|                                                                                                                           |
| [gridControl1(rowIndex, colIndex).CellValue = Color.Aqua]                             |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 75: Color Edit Cells

 

[]{#p52} 

 

[]{#related-topics}

