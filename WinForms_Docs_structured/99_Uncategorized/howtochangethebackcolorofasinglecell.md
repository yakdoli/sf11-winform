---
title: howtochangethebackcolorofasinglecell.md
original_path: WinForms_Docs/99_Uncategorized/howtochangethebackcolorofasinglecell.md
created_at: 2025-08-05
---








  









### How to Change the Backcolor of a Single Cell {#how-to-change-the-backcolor-of-a-single-cell style="tab-stops: 0pt"}

[] 

Introduction

[] 

The style object holds all the information that affects the cells appearance. One property contained in the style object is its [BackColor]{.UGHyperlink}. Use a two-parameter indexer (rowIndex, colIndex) on your GridControl object to get a reference to that particular cells style, a [GridStyleInfo]{.UGHyperlink} object.\
\

Example

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                        |
| []                                                                   |
|                                                                                                                        |
| [// Changing the BackColor of a cell in the 1st row and 3rd column.] |
|                                                                                                                        |
| [gridControl1\[1, 3\].BackColor = Color.Red;]                        |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                     |
|                                                                                                                        |
| []                                                                   |
|                                                                                                                        |
| [\' Changing the BackColor of a cell in the 1st row and 3rd column.] |
|                                                                                                                        |
| [GridControl1(1, 3).BackColor = Color.Red]                           |
+------------------------------------------------------------------------------------------------------------------------+

 

[]{#p550} 

 

[]{#related-topics}

