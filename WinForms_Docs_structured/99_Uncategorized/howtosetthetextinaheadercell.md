---
title: howtosetthetextinaheadercell.md
original_path: WinForms_Docs/99_Uncategorized/howtosetthetextinaheadercell.md
created_at: 2025-08-05
---








  









### How to Set the Text in a Header Cell {#how-to-set-the-text-in-a-header-cell style="tab-stops: 0pt"}

[] 

Introduction

 

In a **GridControl**, values in header cells are set just as in any other cell.

[] 

Example

[] 

Use an indexer on your GridControl with the row index set to 0.

[] 

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                              |
|                                                                                                             |
| **[]**                                                    |
|                                                                                                             |
| [// Setting Text property in the 5th column header cell.] |
|                                                                                                             |
| [gridControl1\[0, 5\].Text = \"HeaderTextForColumn5\";]   |
+-------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                          |
|                                                                                                             |
| **[]**                                                    |
|                                                                                                             |
| [\' Setting Text property in the 5th column header cell.] |
|                                                                                                             |
| [GridControl1(0, 5).Text = \"HeaderTextForColumn5\"]      |
+-------------------------------------------------------------------------------------------------------------+

 

[]{#p568} 

 

[]{#related-topics}

