---
title: headerrowsandcolumns.md
original_path: WinForms_Docs/99_Uncategorized/headerrowsandcolumns.md
created_at: 2025-08-05
---






##### Header Rows and Columns {#header-rows-and-columns style="tab-stops: 0pt"}

[] 

As we have seen in the previous section, it is possible to hide both the row and column headers. We can also have more than one header row and / or more than one header column. The properties that control the number of header rows and columns is **GridControl.Rows.HeaderCount** and **GridControl.Cols.HeaderCount**. This **HeaderCount** property is the index of the last header row or column. So, to have a total of three column header rows, set **Rows.HeaderCount** to two.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [// Total of three column header rows.    ][    ] |
|                                                                                                                                                       |
| [this][.gridControl1.Rows.HeaderCount = 2;]        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [\' Total of three column header rows.     ][   ] |
|                                                                                                                                                       |
| [Me][.GridControl1.Cols.Rows.HeaderCount = 2  ]    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][172][: Grid With Three Column Header Rows]*

 

[]{#p327} 

 

[]{#related-topics}

