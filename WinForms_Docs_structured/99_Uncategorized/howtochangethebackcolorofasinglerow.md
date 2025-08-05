---
title: howtochangethebackcolorofasinglerow.md
original_path: WinForms_Docs/99_Uncategorized/howtochangethebackcolorofasinglerow.md
created_at: 2025-08-05
---








  









### How to Change the Backcolor of a Single Row {#how-to-change-the-backcolor-of-a-single-row style="tab-stops: 0pt"}

[] 

Introduction

[] 

The **GridControl.RowStyles** collection contains[ ]{.UGHyperlink}[GridStyleInfo]{.UGHyperlink} objects that provide row style settings for the GridControl. Changing the properties on a particular RowStyle will affect all the cells in that row (unless a particular cell has a more specific style setting, like a [cellstyle]{.UGHyperlink}, applied).\
\

Example

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                         |
|                                                                                                        |
| []                                                   |
|                                                                                                        |
| [// Setting the BackColor of the 3rd row.]           |
|                                                                                                        |
| [gridControl1.RowStyles\[3\].BackColor = Color.Red;] |
+--------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                  |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [\' Setting the BackColor of the 3rd row.]        |
|                                                                                                     |
| [GridControl1.RowStyles(3).BackColor = Color.Red] |
+-----------------------------------------------------------------------------------------------------+

 

[]{#p551} 

 

[]{#related-topics}

