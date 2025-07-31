---
title: howtochangetheappearanceofasingleheadercell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\howtochangetheappearanceofasingleheadercell.md
created_at: 2025-07-03
---








  









### How to Change the Appearance of a Single Header Cell {#how-to-change-the-appearance-of-a-single-header-cell style="tab-stops: 0pt"}

[] 

Introduction

 

To make changes to individual cells (header cells or otherwise), use an indexer on the GridControl. In a GridControl with  the default headers, the column headers are row zero and the row headers are column zero. Given below is the code that will change a column header.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                      |
| [// Changing the font properties of the header cell.]                                                                                              |
|                                                                                                                                                                                                      |
| [gridControl1\[0, 3\].Font.Italic = ][true][; ] |
|                                                                                                                                                                                                      |
| [gridControl1\[0, 3\].Font.Bold = ][true][; ]   |
|                                                                                                                                                                                                      |
| [gridControl1\[0, 3\].Font.Orientation = 270;]                                                                                                     |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [// Changing the Text Color and Text of the header cell. ]                                                                                         |
|                                                                                                                                                                                                      |
| [gridControl1\[0, 3\].TextColor = Color.Red; ]                                                                                                     |
|                                                                                                                                                                                                      |
| [gridControl1\[0, 3\].Text = \"Sales\";]                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                           |
|                                                                                                                                              |
| []                                                                                                                     |
|                                                                                                                                              |
| [// Changing the font properties of the header cell.]                                      |
|                                                                                                                                              |
| [GridControl1(0, 3).Font.Italic = ][True] |
|                                                                                                                                              |
| [GridControl1(0, 3).Font.Bold = ][True]   |
|                                                                                                                                              |
| [GridControl1(0, 3).Font.Orientation = 270]                                                |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [// Changing the Text Color and Text of the header cell.]                                  |
|                                                                                                                                              |
| [GridControl1(0, 3).TextColor = Color.Red]                                                 |
|                                                                                                                                              |
| [GridControl1(0, 3).Text = \"Sales\"]                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][499][: GridControl Showing Modified Header Cell]*

 

[]{#p548} 

 

[]{#related-topics}

