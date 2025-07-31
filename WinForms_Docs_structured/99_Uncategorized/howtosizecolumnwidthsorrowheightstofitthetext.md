---
title: howtosizecolumnwidthsorrowheightstofitthetext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosizecolumnwidthsorrowheightstofitthetext.md
created_at: 2025-07-03
---








  









### How to Size Column Widths or Row Heights to Fit the Text {#how-to-size-column-widths-or-row-heights-to-fit-the-text style="tab-stops: 0pt"}

[] 

Introduction

[] 

To size columns so that all the text is visible, use the **grid.Model.ColWidths.ResizeToFit** method. This method will take two arguments, a **GridRangeInfo** object that will specify the cells that are to be resized and a **GridResizeToFitOptions** setting that will specify certain behaviors. The second setting controls whether you\'ll allow the cell to shrink when it is resized and whether you want to include any header cells in the resizing.\
\
There is also a **grid.Model.RowHeights.ResizeToFit** method to size row heights.\
\

Example

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [// AutoFit RowHeights.]                                                                       |
|                                                                                                                                                  |
| [grid.Model.RowHeights.ResizeToFit(GridRangeInfo.Table, GridResizeToFitOptions.NoShrinkSize);] |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [// AutoFit ColumnWidths.]                                                                     |
|                                                                                                                                                  |
| [grid.Model.ColWidths.ResizeToFit(GridRangeInfo.Col(2), GridResizeToFitOptions.NoShrinkSize);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                              |
|                                                                                                                                                 |
| []                                                                                            |
|                                                                                                                                                 |
| [\' AutoFit RowHeights.]                                                                      |
|                                                                                                                                                 |
| [grid.Model.RowHeights.ResizeToFit(GridRangeInfo.Table, GridResizeToFitOptions.NoShrinkSize)] |
|                                                                                                                                                 |
| []                                                                                            |
|                                                                                                                                                 |
| [\' AutoFit ColumnWidths. ]                                                                   |
|                                                                                                                                                 |
| [grid.Model.ColWidths.ResizeToFit(GridRangeInfo.Col(2), GridResizeToFitOptions.NoShrinkSize)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Resizing the entire grid for very large grids can be time consuming. To only resize the visible area of the grid, you can  set the range argument to grid.ViewLayout.VisibleCellsRange.


 

[]{#p639} 

 

[]{#related-topics}

