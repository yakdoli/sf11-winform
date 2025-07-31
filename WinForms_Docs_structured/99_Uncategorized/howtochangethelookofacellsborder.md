---
title: howtochangethelookofacellsborder.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethelookofacellsborder.md
created_at: 2025-07-03
---








  









### How to Change the Look of a Cell\'s Border {#how-to-change-the-look-of-a-cells-border style="tab-stops: 0pt"}

[] 

Introduction

[] 

Use the **Borders** property of [GridStyleInfo]{.UGHyperlink} to change the style and the appearance of the grid cells border. Each border side of the cell can be configured individually with a GridBorder value. There is a BorderMargins property to control the margins on all four sides.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                          |
| [// Borders on all four sides of the cell.]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                          |
| [GridStyleInfo style = ][this][.gridControl1.RowStyles\[1\];]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridControl1.RowStyles\[1\].Borders.All = ][new][ GridBorder(GridBorderStyle.Solid, Color.Red, GridBorderWeight.Thin);]                    |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridControl1.RowStyles\[2\].Borders.Right = ][new][ GridBorder(GridBorderStyle.Dotted, Color.LightBlue, GridBorderWeight.ExtraThick);]     |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridControl1.RowStyles\[3\].Borders.Bottom = ][new][ GridBorder(GridBorderStyle.Solid, Color.Pink, GridBorderWeight.Medium);]              |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridControl1.RowStyles\[4\].Borders.Left = ][new][ GridBorder(GridBorderStyle.DashDot, Color.LightGreen, GridBorderWeight.ExtraThick);]    |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.gridControl1.RowStyles\[5\].Borders.Top = ][new][ GridBorder(GridBorderStyle.DashDotDot, Color.Purple, GridBorderWeight.ExtraExtraThick);] |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                          |
| [// Bordermargins]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                          |
| [    ][this][.gridControl1.RowStyles\[1\].BorderMargins.Right = 20;]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                          |
| [    ][this][.gridControl1.RowStyles\[2\].BorderMargins.Left = 22;]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                          |
| [    ][this][.gridControl1.RowStyles\[3\].BorderMargins.Top = 24;]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                          |
| [    ][this][.gridControl1.RowStyles\[4\].BorderMargins.Bottom = 26;]                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\' Borders on all four sides of the cell.]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(1).Borders.All = ][New][ GridBorder(GridBorderStyle.Solid, Color.Red, GridBorderWeight.Thin)]                    |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(2).Borders.Right = ][New][ GridBorder(GridBorderStyle.Dotted, Color.LightBlue, GridBorderWeight.ExtraThick)]     |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(3).Borders.Bottom = ][New][ GridBorder(GridBorderStyle.Solid, Color.Pink, GridBorderWeight.Medium)]              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(4).Borders.Left = ][New][ GridBorder(GridBorderStyle.DashDot, Color.LightGreen, GridBorderWeight.ExtraThick)]    |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(5).Borders.Top = ][New][ GridBorder(GridBorderStyle.DashDotDot, Color.Purple, GridBorderWeight.ExtraExtraThick)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\' Bordermargins]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(1).BorderMargins.Right = 20]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(2).BorderMargins.Left = 22]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(3).BorderMargins.Top = 24]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.GridControl1.RowStyles(4).BorderMargins.Bottom = 26]                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p553} 

 

[]{#related-topics}

