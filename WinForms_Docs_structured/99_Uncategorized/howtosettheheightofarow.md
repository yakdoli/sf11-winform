---
title: howtosettheheightofarow.md
original_path: WinForms_Docs/99_Uncategorized/howtosettheheightofarow.md
created_at: 2025-08-05
---








  









### How to Set the Height of a Row {#how-to-set-the-height-of-a-row style="tab-stops: 0pt"}

[] 

Introduction

[] 

Changing a row\'s height is simple whether you are using the designer or code. From the designer, use the **RowHeightEntries** collection. To explicitly set the height of the particular row from code, use the **GridControl.RowHeights** collection.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Set height of row 3 to 40.\                                                                                                                                                                    |
| ][this][.gridControl1.RowHeights\[3\] = 40; ] |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Set height of header row 30.]                                                                                                                |
|                                                                                                                                                                                                    |
| [this][.gridControl1.RowHeights\[0\] = 30; ]                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [\' Set height of row 3 to 40.\                                                                                                                                                               |
| ][Me][.GridControl1.RowHeights(3) = 40 ] |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [\' Set height of header row 30.]                                                                                                           |
|                                                                                                                                                                                               |
| [Me][.GridControl1.RowHeights(0) = 30 ]                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p566} 

 

[]{#related-topics}

