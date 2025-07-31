---
title: howtochangethelookofacolumnsborder.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethelookofacolumnsborder.md
created_at: 2025-07-03
---








  









### How to Change the Look of a Column\'s Border {#how-to-change-the-look-of-a-columns-border style="tab-stops: 0pt"}

[] 

Introduction

[] 

You can use the **Borders** property of the **GridStyleInfo** to change the style and the appearance of the grid cell\'s border. Each border side of the cell can be configured individually with a **GridBorder** value. There is a **BorderMargins** property to control the margins on all four sides. In a GridDataBoundGrid, you can set the style properties column by column using GridDataBoundGrid.GridBoundColumns or GridDataBoundGrid.Binder.InternalColumns depending upon whether you had explicitly added the **GridBoundColumns** or not.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [// Borders on all four sides of the cell.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [GridStyleInfo style = ][this][.gridDataBoundGrid1.GridBoundColumns\[1\].StyleInfo;]                                  |
|                                                                                                                                                                                                                                                                            |
| [style.Borders.All = ][new][ GridBorder(GridBorderStyle.Solid, Color.Red, GridBorderWeight.Thin);]                    |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [style = ][this][.gridDataBoundGrid1.GridBoundColumns\[2\].StyleInfo;]                                                |
|                                                                                                                                                                                                                                                                            |
| [style.Borders.Right = ][new][ GridBorder(GridBorderStyle.Dotted, Color.LightBlue, GridBorderWeight.ExtraThick);]     |
|                                                                                                                                                                                                                                                                            |
| [style.Borders.Bottom = ][new][ GridBorder(GridBorderStyle.Solid, Color.Pink, GridBorderWeight.Medium);]              |
|                                                                                                                                                                                                                                                                            |
| [style.Borders.Left = ][new][ GridBorder(GridBorderStyle.DashDot, Color.LightGreen, GridBorderWeight.ExtraThick);]    |
|                                                                                                                                                                                                                                                                            |
| [style.Borders.Top = ][new][ GridBorder(GridBorderStyle.DashDotDot, Color.Purple, GridBorderWeight.ExtraExtraThick);] |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [// Border Margins]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [this][.gridDataBoundGrid1.GridBoundColumns\[4\].StyleInfo.BorderMargins.Right = 20;]                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [this][.gridDataBoundGrid1.GridBoundColumns\[4\].StyleInfo.BorderMargins.Left = 22;]                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [this][.gridDataBoundGrid1.GridBoundColumns\[4\].StyleInfo.BorderMargins.Top = 24;]                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [this][.gridDataBoundGrid1.GridBoundColumns\[4\].StyleInfo.BorderMargins.Bottom = 26;]                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Borders on all four sides of the cell.]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ style ][As][ GridStyleInfo = ][Me][.gridDataBoundGrid1.GridBoundColumns(1).StyleInfo] |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.Borders.All = ][New][ GridBorder(GridBorderStyle.Solid, Color.Red, GridBorderWeight.Thin)]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style = ][Me][.gridDataBoundGrid1.GridBoundColumns(2).StyleInfo]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.Borders.Right = ][New][ GridBorder(GridBorderStyle.Dotted, Color.LightBlue, GridBorderWeight.ExtraThick)]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.Borders.Bottom = ][New][ GridBorder(GridBorderStyle.Solid, Color.Pink, GridBorderWeight.Medium)]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.Borders.Left = ][New][ GridBorder(GridBorderStyle.DashDot, Color.LightGreen, GridBorderWeight.ExtraThick)]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.Borders.Top = ][New][ GridBorder(GridBorderStyle.DashDotDot, Color.Purple, GridBorderWeight.ExtraExtraThick)]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Bordermargins]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridDataBoundGrid1.GridBoundColumns(4).StyleInfo.BorderMargins.Right = 20]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridDataBoundGrid1.GridBoundColumns(4).StyleInfo.BorderMargins.Left = 22]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridDataBoundGrid1.GridBoundColumns(4).StyleInfo.BorderMargins.Top = 24]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridDataBoundGrid1.GridBoundColumns(4).StyleInfo.BorderMargins.Bottom = 26]                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p587} 

 

[]{#related-topics}

