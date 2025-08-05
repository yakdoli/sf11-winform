---
title: cellstyle.md
original_path: WinForms_Docs/02_Concepts/cellstyle.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Cell Style {#cell-style style="tab-stops: 0pt"}

The following properties of a grid cell can be customized so that the grid appears in a custom style rather than the default one.

+---------------+---------------------------------------------------+-------------+------------------+----------------+
|               |                                                   |             |                  |                |
|               |                                                   |             |                  |                |
| Property Name | Description                                       | Type        | Value it Accepts | Reference link |
|               |                                                   |             |                  |                |
|               |                                                   |             |                  |                |
+---------------+---------------------------------------------------+-------------+------------------+----------------+
| Background    | Gets or sets the background color of a grid cell. | Brush       | \-               | \-             |
+---------------+---------------------------------------------------+-------------+------------------+----------------+
| FontFamily    | Gets or sets the font family of a grid cell.      | FontFamily  | \-               | \-             |
+---------------+---------------------------------------------------+-------------+------------------+----------------+
| FontSize      | Gets or sets the font size of a grid cell.        | int         | \-               | \-             |
+---------------+---------------------------------------------------+-------------+------------------+----------------+
| FontWeight    | Gets or sets the font weigh of a grid cell.       | FontWeight  | \-               | \-             |
+---------------+---------------------------------------------------+-------------+------------------+----------------+
| Foreground    | Gets or sets the foreground color of a grid cell. | Brush       | \-               | \-             |
+---------------+---------------------------------------------------+-------------+------------------+----------------+

[] 

Column, row, summary, and value cells of a grid can be formatted independently using the following properties:

[·      ] **ColumnHeaderCellStyle** -- Specifies the style for column headers.

[·      ] **RowHeaderCellStyle** -- Specifies the style for row headers.

[·      ] **SummaryCellStyle** -- Specifies the style for summary cells.

[·      ] **ValueCellStyle**  --  Specifies the style for value cells.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [            [// Specifying the Background color for Grid column header]]                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            [this].PivotGridControl1.ColumnHeaderCellStyle.Background = [new][SolidColorBrush]([Color].FromRgb(175, 209, 255));] |
|                                                                                                                                                                                                                                                                 |
| [            [// Specifying the Background color for Grid row header]]                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| [            [this].PivotGridControl1.RowHeaderCellStyle.Background = [new][SolidColorBrush]([Color].FromRgb(175, 209, 255));]    |
|                                                                                                                                                                                                                                                                 |
| [            [// Specifying the Background color for Grid summary cell]]                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [            [this].PivotGridControl1.SummaryCellStyle.Background = [new][SolidColorBrush]([Color].FromRgb(206, 225, 248)); ]     |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| [            [\' Specifying the Background color for Grid column header]]                                                                       |
|                                                                                                                                                                                                           |
| [            [Me].PivotGridControl1.ColumnHeaderCellStyle.Background = [New] SolidColorBrush(Color.FromRgb(175, 209, 255))] |
|                                                                                                                                                                                                           |
| [            [\' Specifying the Background color for Grid row header]]                                                                          |
|                                                                                                                                                                                                           |
| [            [Me].PivotGridControl1.RowHeaderCellStyle.Background = [New] SolidColorBrush(Color.FromRgb(175, 209, 255))]    |
|                                                                                                                                                                                                           |
| [            [\' Specifying the Background color for Grid summary cell]]                                                                        |
|                                                                                                                                                                                                           |
| [            [Me].PivotGridControl1.SummaryCellStyle.Background = [New] SolidColorBrush(Color.FromRgb(206, 225, 248))]      |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The formatting set in the above code generates the following PivotTable.

[] 

{border="0"}

 

Figure 10: Formatted PivotGrid

[]{#related-topics}

