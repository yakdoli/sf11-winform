---
title: textbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textbox.md
created_at: 2025-07-03
---






##### Text Box {#text-box style="tab-stops: 0pt"}

[] 

A **Text Box** cell type displays text and images that can be edited in place.

[] 

The following code example illustrates how to set the cell type to TextBox.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                  |
|                                                                                                                                                 |
| []                                                                            |
|                                                                                                                                                 |
| [gridControl1\[rowIndex,colIndex\].Text = [\"TextBox\"];]           |
|                                                                                                                                                 |
| [gridControl1\[rowIndex,colIndex\].CellType = [\"TextBox\"];]       |
|                                                                                                                                                 |
| []                                                                                          |
|                                                                                                                                                 |
| [// Text box with image - assumes ImageList set the same Static sample code.] |
|                                                                                                                                                 |
| [gridControl1\[rowIndex,colIndex + 1\].Text = [\"TextBox/Image\"];] |
|                                                                                                                                                 |
| [gridControl1\[rowIndex,colIndex\].CellType = [\"TextBox\"];]       |
|                                                                                                                                                 |
| [gridControl1\[rowIndex,colIndex + 1\].ImageIndex = 1;]                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                              |
|                                                                                                                                                 |
| []                                                                            |
|                                                                                                                                                 |
| [gridControl1(rowIndex, colIndex).Text = [\"TextBox\"]]             |
|                                                                                                                                                 |
| [gridControl1(rowIndex, colIndex).CellType = [\"TextBox\"]]         |
|                                                                                                                                                 |
| []                                                                          |
|                                                                                                                                                 |
| [\' Text box with image - assumes ImageList set the same Static sample code.] |
|                                                                                                                                                 |
| [gridControl1(rowIndex, colIndex + 1).Text = [\"TextBox/Image\"]]   |
|                                                                                                                                                 |
| [gridControl1(rowIndex, colIndex).CellType = [\"TextBox\"]]         |
|                                                                                                                                                 |
| [gridControl1(rowIndex, colIndex + 1).ImageIndex = 1]                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][91][: Text Box Cells]*

 

[]{#p67} 

 

[]{#related-topics}

