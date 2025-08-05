---
title: whatisthedifferencebetweentextalignhorizontalalignmentandverticalalignment.md
original_path: WinForms_Docs/99_Uncategorized/whatisthedifferencebetweentextalignhorizontalalignmentandverticalalignment.md
created_at: 2025-08-05
---








  









### What is the Difference between TextAlign, HorizontalAlignment and VerticalAlignment? {#what-is-the-difference-between-textalign-horizontalalignment-and-verticalalignment style="tab-stops: 0pt"}

[] 

Introduction

[] 

**TextAlign** is set when the description of embedded controls are to be aligned to the left or right. **HorizontalAlignment** is set when the cell value is to be aligned either left or right or center of the cell. **VerticalAlignment** is set when the cell value is to be aligned either top or bottom or middle of the cell.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [// Right align the cell values of column 3 horizontally.]                                                                                 |
|                                                                                                                                                                                              |
| [this][.gridControl1.ColStyles\[3\].HorizontalAlignment = GridHorizontalAlignment.Right;] |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [// Right align the embedded controls in column 6. ]                                                                                       |
|                                                                                                                                                                                              |
| [this][.gridControl1.ColStyles\[6\].TextAlign = GridTextAlign.Right;]                     |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [// Align the cell values of column 8 at the bottom. ]                                                                                     |
|                                                                                                                                                                                              |
| [this][.gridControl1.ColStyles\[8\].VerticalAlignment = GridVerticalAlignment.Bottom;]    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [\' Right align the cell values of column 3 horizontally.]                                                                            |
|                                                                                                                                                                                         |
| [Me][.gridControl1.ColStyles(3).HorizontalAlignment = GridHorizontalAlignment.Right] |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [\' Right align the embedded controls in column 6.]                                                                                   |
|                                                                                                                                                                                         |
| [Me][.gridControl1.ColStyles(6).TextAlign = GridTextAlign.Right]                     |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [\' Align the cell values of column 8 at the bottom. ]                                                                                |
|                                                                                                                                                                                         |
| [Me][.gridControl1.ColStyles(8).VerticalAlignment = GridVerticalAlignment.Bottom]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p579} 

 

[]{#related-topics}

