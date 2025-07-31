---
title: howtochangethebackcolorofacolumn.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethebackcolorofacolumn.md
created_at: 2025-07-03
---








  









### How to Change the Backcolor of a Column {#how-to-change-the-backcolor-of-a-column style="tab-stops: 0pt"}

[] 

Introduction

[] 

[The GridControl.ColStyles collection contains ][GridStyleInfo]{.UGHyperlink}[ objects that provide column style settings for the GridControl. Changing the properties on a particular column style will affect all the cells in that row (unless a particular cell has a more specific style setting, like a ][cell style]{.UGHyperlink}[, applied).\
\
]

Example

[      ]

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                         |
|                                                                                                        |
| []                                                   |
|                                                                                                        |
| [// Setting the BackColor for the third column.]     |
|                                                                                                        |
| [gridControl1.ColStyles\[3\].BackColor = Color.Red;] |
+--------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                  |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [\' Setting the BackColor for the third column.]  |
|                                                                                                     |
| [GridControl1.ColStyles(3).BackColor = Color.Red] |
+-----------------------------------------------------------------------------------------------------+

 

[]{#p549} 

 

[]{#related-topics}

