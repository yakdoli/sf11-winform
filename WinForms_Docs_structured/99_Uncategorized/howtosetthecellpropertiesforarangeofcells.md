---
title: howtosetthecellpropertiesforarangeofcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthecellpropertiesforarangeofcells.md
created_at: 2025-07-03
---








  









### How to Set the Cell Properties for a Range of Cells {#how-to-set-the-cell-properties-for-a-range-of-cells style="tab-stops: 0pt"}

[] 

Introduction

[] 

Use the GridControl\'s[ ]**ChangeCells** method by passing it a [GridRangeInfo] object to change the appearance of a range of cells.

[] 

Example

 

To set the [backcolor] and **textcolor** for a range of cells, use the below given code snippet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Style settings.]                                                                                                                                |
|                                                                                                                                                                                                       |
| [GridStyleInfo style = ][new][ GridStyleInfo();] |
|                                                                                                                                                                                                       |
| [style.TextColor = Color.Red;]                                                                                                                      |
|                                                                                                                                                                                                       |
| [style.BackColor = Color.LightBlue;]                                                                                                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Modifying a range of cells.]                                                                                                                    |
|                                                                                                                                                                                                       |
| [gridControl1.ChangeCells(GridRangeInfo.Cells(1, 1, 4, 5), style);]                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [\' Style settings.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [Dim][ style ][As New][ GridStyleInfo()] |
|                                                                                                                                                                                                                                                |
| [style.TextColor = Color.Red]                                                                                                                                                                |
|                                                                                                                                                                                                                                                |
| [style.BackColor = Color.LightBlue]                                                                                                                                                          |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [\' Modifying a range of cells.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                |
| [GridControl1.ChangeCells(GridRangeInfo.Cells(1, 1, 4, 5), style)]                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p564} 

 

[]{#related-topics}

