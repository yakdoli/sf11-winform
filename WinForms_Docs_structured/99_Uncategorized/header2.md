---
title: header2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\header2.md
created_at: 2025-07-03
---






##### Header {#header style="tab-stops: 0pt"}

[] 

The **Header** cell type displays static text similar to the static **CellType**. But the Header cell type, in addition, has a button-like border that can have a depressed state.

[] 

The following code example illustrates how to set the cell type to Header.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [// Set Cell Type as \"Header\".]                                                          |
|                                                                                                                                              |
| [gridControl1\[rowIndex,colIndex\].Text = [\"HeaderText\"];]                     |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [// Set Formatting properties.]                                                            |
|                                                                                                                                              |
| [gridControl1\[rowIndex,colIndex\].CellType = [\"Header\"];]                     |
|                                                                                                                                              |
| [gridControl1\[rowIndex,colIndex\].BackColor = [Color].FromArgb(208, 208, 208);] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                     |
|                                                                                                                        |
| []                                                                   |
|                                                                                                                        |
| [\' Set Cell Type as \"Header\".]                                    |
|                                                                                                                        |
| [gridControl1(rowIndex, colIndex).Text = [\"HeaderText\"]] |
|                                                                                                                        |
| []                                                                 |
|                                                                                                                        |
| [\' Set Formatting properties.]                                      |
|                                                                                                                        |
| [gridControl1(rowIndex, colIndex).CellType = [\"Header\"]] |
|                                                                                                                        |
| [gridControl1(rowIndex, colIndex).BackColor = Color.FromArgb(208, 208, 208)]       |
+------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][82][: Header Cells]*

 

[]{#p58} 

 

[]{#related-topics}

