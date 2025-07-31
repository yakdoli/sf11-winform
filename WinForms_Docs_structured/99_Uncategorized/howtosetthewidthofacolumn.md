---
title: howtosetthewidthofacolumn.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthewidthofacolumn.md
created_at: 2025-07-03
---








  









### How to Set the Width of a Column {#how-to-set-the-width-of-a-column style="tab-stops: 0pt"}

[] 

Introduction

[] 

Changing a column\'s width is simple whether you are using the designer or code. In the designer, use the **ColWidthsEntries** collection. In code, use the **GridControl.ColWidths** collection to specify the width of a column.

[] 

Example

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Set size of column 3 to 250.\                                                                                                                                                                 |
| ][this][.gridControl1.ColWidths\[3\] = 250;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [\' Set size of column 3 to 250.\                                                                                                                                                             |
| ][Me][.GridControl1.ColWidths(3) = 250 ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p569} 

 

[]{#related-topics}

