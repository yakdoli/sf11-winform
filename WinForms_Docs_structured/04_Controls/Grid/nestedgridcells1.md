---
title: nestedgridcells1.md
original_path: WinForms_Docs/04_Controls/Grid/nestedgridcells1.md
created_at: 2025-08-05
---






##### Nested Grid Cells {#nested-grid-cells style="tab-stops: 0pt"}

Nested grids are an important component of the basic architecture of Essential Grid. They provide for the easy display of complex user interfaces using a flat grid. They also form the underpinnings for the display of hierarchical and grouped data. You can nest grids inside a row, column or covered range. When you nest a grid inside a covered range you can specify whether the rows or columns derive their state from the parent control. You have multiple independent options for both rows and columns.

 

API definition

GridCellNestedGridModel is the class to be used as model class for this cell type. Its constructor accepts two objects of type GridNestedAxisLayout enum, where the first parameter corresponds to row and second parameter corresponds to grid column. This  enum value determines whether to share the row layout or column layout or the rows and columns are independent of parent grid.

Nested Grid inside a Row of Parent Grid[]

In this case, the grid will maintain its own row heights. When you resize rows the grid will also notify the parent grid that its total height is changed. While scrolling you can scroll row by row through the nested grid. The nested grid will have no separate scrollbars. They are shared with the parent grid.

 

Example

The code below implements a nested scroll grid. The GridCellNestedScrollGridModel is the model class to be used.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                     |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [// Add Nested Scroll Grid cell model.]                                                                      |
|                                                                                                                                                                |
| [GridCellNestedScrollGridModel scrollGridModel = [new] GridCellNestedScrollGridModel();]              |
|                                                                                                                                                                |
| [Model.CellModels.Add([\"ScrollGrid\"], scrollGridModel);]                                         |
|                                                                                                                                                                |
| [Model\[40, 2\].CellType = [\"ScrollGrid\"];]                                                      |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [// Create scroll nested grid.]                                                                              |
|                                                                                                                                                                |
| [GridModel nestedGrid = [new] GridModel();]                                                           |
|                                                                                                                                                                |
| [nestedGrid.Options.AllowSelection = GridSelectionFlags.Cell;]                                                             |
|                                                                                                                                                                |
| [nestedGrid.RowHeights.DefaultLineSize = 20;]                                                                              |
|                                                                                                                                                                |
| [nestedGrid.RowCount = 50;]                                                                                                |
|                                                                                                                                                                |
| [nestedGrid.ColumnWidths.DefaultLineSize = 50;]                                                                            |
|                                                                                                                                                                |
| [nestedGrid.ColumnCount = 12;]                                                                                             |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [Brush headerBrush = ColorHelper.CreateFrozenSolidColorBrush(128, Colors.DarkGray);]                                       |
|                                                                                                                                                                |
| [nestedGrid.BaseStylesMap\[[\"Header\"]\].StyleInfo.Background = headerBrush;]                     |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [for][ ([int] n = 0; n \< nestedGrid.RowCount; n++)] |
|                                                                                                                                                                |
| [{]                                                                                                                        |
|                                                                                                                                                                |
| [    [for] ([int] c = 0; c \< nestedGrid.ColumnCount; c++)]                      |
|                                                                                                                                                                |
| [    {]                                                                                                                    |
|                                                                                                                                                                |
| [        GridStyleInfo ci = [new] GridStyleInfo();]                                                   |
|                                                                                                                                                                |
| [        ci.CellType = [\"TextBox\"];]                                                             |
|                                                                                                                                                                |
| [        ci.CellValue = String.Format([\"Scroll{0}:{1}\"], n, c);]                                 |
|                                                                                                                                                                |
| [        nestedGrid.Data\[n, c\] = ci.Store;]                                                                              |
|                                                                                                                                                                |
| [    }]                                                                                                                    |
|                                                                                                                                                                |
| [}]                                                                                                                        |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [Model\[40, 2\].CellValue = nestedGrid;]                                                                                   |
|                                                                                                                                                                |
| [CoveredCells.Add([new] CoveredCellInfo(40, 2, 49, 5));]                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 35: Nested Grid

 

The same way you can nest a grid inside a complete row you can also nest a grid inside a whole column.

Nested Grid Inside a Covered Range with its Rows Tied to the Rows of the Parent Grid

In this case, the grid will have its own unique column widths but the row heights are shared with the parent grid. When scrolling through rows in the nested grid you also scroll the rows in the parent grid to keep them in sync. The nested grid will have no separate scrollbars. They are shared with the parent grid. When you resize rows they will also be resized in the parent grid and vice versa.

 

Example

The codes below show a grid whose cell contains a nested grid, which again contains a nested grid in its cell, and this second nested grid again contains a nested grid in its cell and thus forming four grids nested within one another.

 

To specify shared row layout, use Shared option of GridNestedAxisLayout enum in the first parameter.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// Add appropriate Nested Grid cell model.]                                                                                          |
|                                                                                                                                                                                         |
| [GridCellNestedGridModel shareRow = [new] GridCellNestedGridModel (GridNestedAxisLayout.Shared, GridNestedAxisLayout.Normal);] |
|                                                                                                                                                                                         |
| [Model.CellModels.Add([\"ShareRowLayoutGrid\"], shareRow);]                                                                 |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// Setup nested grid with shared row layout]                                                                                         |
|                                                                                                                                                                                         |
| [Model\[100, 2\].CellType = [\"ShareRowLayoutGrid\"];]                                                                      |
|                                                                                                                                                                                         |
| [Model\[100, 2\].BorderMargins.Top = 0;]                                                                                                            |
|                                                                                                                                                                                         |
| [Model\[100, 2\].BorderMargins.Left = 0;]                                                                                                           |
|                                                                                                                                                                                         |
| [Model\[100, 2\].BorderMargins.Right = 0;]                                                                                                          |
|                                                                                                                                                                                         |
| [Model\[100, 2\].BorderMargins.Bottom = 0;]                                                                                                         |
|                                                                                                                                                                                         |
| [Model\[100, 2\].Background = SystemColors.InactiveCaptionBrush;]                                                                                   |
|                                                                                                                                                                                         |
| [GridModel nestedGridWithSharedRowsModel = GetNestedGridWithSharedRowsModel();]                                                                     |
|                                                                                                                                                                                         |
| [Model\[100, 2\].CellValue = nestedGridWithSharedRowsModel;]                                                                                        |
|                                                                                                                                                                                         |
| [CoveredCells.Add([new] CoveredCellInfo(100, 2, 100 + nestedGridWithSharedRowsModel.RowCount - 1, 5));]                        |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// Setup the top level(parent) nested grid]                                                                                          |
|                                                                                                                                                                                         |
| [private][ GridModel GetNestedGridWithSharedRowsModel()]                                           |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [GridModel model = [new] GridModel();]                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Pen gridLinePen = [new] Pen(Brushes.DarkGray, 1);]                                                                            |
|                                                                                                                                                                                         |
| [gridLinePen.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [model.Options.AllowSelection = GridSelectionFlags.Cell;]                                                                                           |
|                                                                                                                                                                                         |
| [model.ColumnWidths.DefaultLineSize = 50;]                                                                                                          |
|                                                                                                                                                                                         |
| [model.ColumnWidths.HeaderLineCount = 1;]                                                                                                           |
|                                                                                                                                                                                         |
| [model.ColumnCount = 12;]                                                                                                                           |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [model.RowHeights.HeaderLineCount = 1;]                                                                                                             |
|                                                                                                                                                                                         |
| [model.RowHeights.FooterLineCount = 1;]                                                                                                             |
|                                                                                                                                                                                         |
| [model.RowCount = 601; ]                                                                                                                            |
|                                                                                                                                                                                         |
| [Color clr = Color.FromArgb(128, 0, 0, 0);]                                                                                                         |
|                                                                                                                                                                                         |
| [Brush headerBrush = [new] SolidColorBrush(clr);]                                                                              |
|                                                                                                                                                                                         |
| [headerBrush.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Color clr2 = Color.FromArgb(128, 128, 0, 0);]                                                                                                      |
|                                                                                                                                                                                         |
| [Brush footerBrush = [new] SolidColorBrush(clr2);]                                                                             |
|                                                                                                                                                                                         |
| [footerBrush.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [for][ ([int] n = 0; n \< model.RowCount; n++)]                               |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [    [for] ([int] c = 0; c \< model.ColumnCount; c++)]                                                    |
|                                                                                                                                                                                         |
| [    {]                                                                                                                                             |
|                                                                                                                                                                                         |
| [        GridStyleInfo ci = [new] GridStyleInfo();]                                                                            |
|                                                                                                                                                                                         |
| [        ci.CellType = [\"TextBox\"];]                                                                                      |
|                                                                                                                                                                                         |
| [        ci.CellValue = String.Format([\"{0}:{1}\"], n, c);]                                                                |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Top = gridLinePen.Thickness;]                                                                                             |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Left = gridLinePen.Thickness;]                                                                                            |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Right = gridLinePen.Thickness / 2;]                                                                                       |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Bottom = gridLinePen.Thickness / 2;]                                                                                      |
|                                                                                                                                                                                         |
| [        ci.Borders.Right = gridLinePen;]                                                                                                           |
|                                                                                                                                                                                         |
| [        ci.Background = [null];[// Brushes.White;]]                                                     |
|                                                                                                                                                                                         |
| [        ci.Borders.Bottom = gridLinePen;]                                                                                                          |
|                                                                                                                                                                                         |
| [        model.Data\[n, c\] = ci.Store;]                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [if] (c == 0 \|\| n == 0)]                                                                                            |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            ci.CellType = [\"Static\"];]                                                                                   |
|                                                                                                                                                                                         |
| [            ci.Background = headerBrush;]                                                                                                          |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [if] (n == model.RowCount - 1)]                                                                                       |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            ci.CellType = [\"Static\"];]                                                                                   |
|                                                                                                                                                                                         |
| [            ci.Background = footerBrush;]                                                                                                          |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| [    }]                                                                                                                                             |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [GridModel nestedGridWithSharedRowsModel = GetSecondNestedGridWithSharedRowsModel();]                                                               |
|                                                                                                                                                                                         |
| [model\[10, 2\].CellType = [\"ShareRowLayoutGrid\"];]                                                                       |
|                                                                                                                                                                                         |
| [model\[10, 2\].BorderMargins.Top = 0;]                                                                                                             |
|                                                                                                                                                                                         |
| [model\[10, 2\].BorderMargins.Left = 0;]                                                                                                            |
|                                                                                                                                                                                         |
| [model\[10, 2\].BorderMargins.Right = 0;]                                                                                                           |
|                                                                                                                                                                                         |
| [model\[10, 2\].BorderMargins.Bottom = 0;]                                                                                                          |
|                                                                                                                                                                                         |
| [model\[10, 2\].Background = SystemColors.InactiveCaptionBrush;]                                                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// Creates a nested grid for second level.]                                                                                          |
|                                                                                                                                                                                         |
| [model\[10, 2\].CellValue = nestedGridWithSharedRowsModel;]                                                                                         |
|                                                                                                                                                                                         |
| [model.CoveredCells.Add([new] CoveredCellInfo(10, 2, 10 + nestedGridWithSharedRowsModel.RowCount - 1, 7));]                    |
|                                                                                                                                                                                         |
| [model.SelectedCells = GridRangeInfo.Empty;]                                                                                                        |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [return][ model;]                                                                                  |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// Setup the second level nested grid]                                                                                               |
|                                                                                                                                                                                         |
| [private][ GridModel GetSecondNestedGridWithSharedRowsModel()]                                     |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [GridModel model = [new] GridModel();]                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Pen gridLinePen = [new] Pen(Brushes.DarkGray, 1);]                                                                            |
|                                                                                                                                                                                         |
| [gridLinePen.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [model.Options.AllowSelection = GridSelectionFlags.Cell;]                                                                                           |
|                                                                                                                                                                                         |
| [model.ColumnWidths.DefaultLineSize = 40;]                                                                                                          |
|                                                                                                                                                                                         |
| [model.ColumnWidths.HeaderLineCount = 1;]                                                                                                           |
|                                                                                                                                                                                         |
| [model.ColumnCount = 8;]                                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [model.RowHeights.HeaderLineCount = 1;]                                                                                                             |
|                                                                                                                                                                                         |
| [model.RowHeights.FooterLineCount = 1;]                                                                                                             |
|                                                                                                                                                                                         |
| [model.RowCount = 121; [// make sure this matched covered cell size \...]]                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [Color clr = Color.FromArgb(128, 0, 0,128);]                                                                                                        |
|                                                                                                                                                                                         |
| [Brush headerBrush = [new] SolidColorBrush(clr);]                                                                              |
|                                                                                                                                                                                         |
| [headerBrush.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Color clr2 = Color.FromArgb(128, 0, 128, 0);]                                                                                                      |
|                                                                                                                                                                                         |
| [Brush footerBrush = [new] SolidColorBrush(clr2);]                                                                             |
|                                                                                                                                                                                         |
| [footerBrush.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [for][ ([int] n = 0; n \< model.RowCount; n++)]                               |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [    [for] ([int] c = 0; c \< model.ColumnCount; c++)]                                                    |
|                                                                                                                                                                                         |
| [    {]                                                                                                                                             |
|                                                                                                                                                                                         |
| [        GridStyleInfo ci = [new] GridStyleInfo();]                                                                            |
|                                                                                                                                                                                         |
| [        ci.CellType = [\"TextBox\"];]                                                                                      |
|                                                                                                                                                                                         |
| [        ci.CellValue = String.Format([\"{0}:{1}\"], n, c);]                                                                |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Top = gridLinePen.Thickness;]                                                                                             |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Left = gridLinePen.Thickness;]                                                                                            |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Right = gridLinePen.Thickness / 2;]                                                                                       |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Bottom = gridLinePen.Thickness / 2;]                                                                                      |
|                                                                                                                                                                                         |
| [        ci.Borders.Right = gridLinePen;]                                                                                                           |
|                                                                                                                                                                                         |
| [        ci.Background = [null];[// Brushes.White;]]                                                     |
|                                                                                                                                                                                         |
| [        ci.Borders.Bottom = gridLinePen;]                                                                                                          |
|                                                                                                                                                                                         |
| [        model.Data\[n, c\] = ci.Store;]                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [if] (c == 0 \|\| n == 0)]                                                                                            |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            ci.CellType = [\"Static\"];]                                                                                   |
|                                                                                                                                                                                         |
| [            ci.Background = headerBrush;]                                                                                                          |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [if] (n == model.RowCount - 1)]                                                                                       |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            ci.CellType = [\"Static\"];]                                                                                   |
|                                                                                                                                                                                         |
| [            ci.Background = footerBrush;]                                                                                                          |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| [    }]                                                                                                                                             |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [GridModel nestedGridWithSharedRowsModel = GetThirdNestedGridWithSharedRowsModel();]                                                                |
|                                                                                                                                                                                         |
| [model\[15, 2\].CellType = [\"ShareRowLayoutGrid\"];]                                                                       |
|                                                                                                                                                                                         |
| [model\[15, 2\].BorderMargins.Top = 0;]                                                                                                             |
|                                                                                                                                                                                         |
| [model\[15, 2\].BorderMargins.Left = 0;]                                                                                                            |
|                                                                                                                                                                                         |
| [model\[15, 2\].BorderMargins.Right = 0;]                                                                                                           |
|                                                                                                                                                                                         |
| [model\[15, 2\].BorderMargins.Bottom = 0;]                                                                                                          |
|                                                                                                                                                                                         |
| [model\[15, 2\].Background = Brushes.Wheat;]                                                                                                        |
|                                                                                                                                                                                         |
| [// Creates a nested grid for third level.]                                                                                           |
|                                                                                                                                                                                         |
| [model\[15, 2\].CellValue = nestedGridWithSharedRowsModel;]                                                                                         |
|                                                                                                                                                                                         |
| [model.CoveredCells.Add([new] CoveredCellInfo(15, 2, 15 + nestedGridWithSharedRowsModel.RowCount - 1, 5));]                    |
|                                                                                                                                                                                         |
| [model.SelectedCells = GridRangeInfo.Empty;]                                                                                                        |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [return][ model;]                                                                                  |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// Setup the third level nested grid]                                                                                                |
|                                                                                                                                                                                         |
| [private][ GridModel GetThirdNestedGridWithSharedRowsModel()]                                      |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [GridModel model = [new] GridModel();]                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Pen gridLinePen = [new] Pen(Brushes.DarkGray, 1);]                                                                            |
|                                                                                                                                                                                         |
| [gridLinePen.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [model.Options.AllowSelection = GridSelectionFlags.Cell;]                                                                                           |
|                                                                                                                                                                                         |
| [model.ColumnWidths.DefaultLineSize = 35;]                                                                                                          |
|                                                                                                                                                                                         |
| [model.ColumnWidths.HeaderLineCount = 1;]                                                                                                           |
|                                                                                                                                                                                         |
| [model.ColumnCount = 4;]                                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [model.RowHeights.HeaderLineCount = 1;]                                                                                                             |
|                                                                                                                                                                                         |
| [model.RowHeights.FooterLineCount = 1;]                                                                                                             |
|                                                                                                                                                                                         |
| [model.RowCount = 31; [// make sure this matched covered cell size \...]]                                                     |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [Color clr = Color.FromArgb(128, 0, 128, 128);]                                                                                                     |
|                                                                                                                                                                                         |
| [Brush headerBrush = [new] SolidColorBrush(clr);]                                                                              |
|                                                                                                                                                                                         |
| [headerBrush.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Color clr2 = Color.FromArgb(128, 128, 128, 0);]                                                                                                    |
|                                                                                                                                                                                         |
| [Brush footerBrush = [new] SolidColorBrush(clr2);]                                                                             |
|                                                                                                                                                                                         |
| [footerBrush.Freeze();]                                                                                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [for][ ([int] n = 0; n \< model.RowCount; n++)]                               |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [    [for] ([int] c = 0; c \< model.ColumnCount; c++)]                                                    |
|                                                                                                                                                                                         |
| [    {]                                                                                                                                             |
|                                                                                                                                                                                         |
| [        GridStyleInfo ci = [new] GridStyleInfo();]                                                                            |
|                                                                                                                                                                                         |
| [        ci.CellType = [\"TextBox\"];]                                                                                      |
|                                                                                                                                                                                         |
| [        ci.CellValue = String.Format([\"{0}:{1}\"], n, c);]                                                                |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Top = gridLinePen.Thickness;]                                                                                             |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Left = gridLinePen.Thickness;]                                                                                            |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Right = gridLinePen.Thickness / 2;]                                                                                       |
|                                                                                                                                                                                         |
| [        ci.BorderMargins.Bottom = gridLinePen.Thickness / 2;]                                                                                      |
|                                                                                                                                                                                         |
| [        ci.Borders.Right = gridLinePen;]                                                                                                           |
|                                                                                                                                                                                         |
| [        ci.Background = [null];[// Brushes.White;]]                                                     |
|                                                                                                                                                                                         |
| [        ci.Borders.Bottom = gridLinePen;]                                                                                                          |
|                                                                                                                                                                                         |
| [        model.Data\[n, c\] = ci.Store;]                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [if] (c == 0 \|\| n == 0)]                                                                                            |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            ci.CellType = [\"Static\"];]                                                                                   |
|                                                                                                                                                                                         |
| [            ci.Background = headerBrush;]                                                                                                          |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [        [if] (n == model.RowCount - 1)]                                                                                       |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            ci.CellType = [\"Static\"];]                                                                                   |
|                                                                                                                                                                                         |
| [            ci.Background = footerBrush;]                                                                                                          |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| [    }]                                                                                                                                             |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [model.SelectedCells = GridRangeInfo.Empty;]                                                                                                        |
|                                                                                                                                                                                         |
| [return][ model;]                                                                                  |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 36: Nested Grid-Rows tied to the Parent Grid Rows

 

Nested Grid Inside a Covered Range with its Columns Tied to the Columns of the Parent Grid

In this case the grid will have its own unique row height but the column widths are shared with the parent grid. When scrolling through columns in the nested grid you also scroll the columns in the parent grid to keep them in sync. The nested grid will have no scrollbars. They are shared with the parent grid. When you resize columns they will also be resized in parent grid and vice versa.

 

Example

To specify shared column layout, use Shared option of GridNestedAxisLayout enum in the second parameter.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                 |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Add the appropriate nested grid cell model.]                                                                                         |
|                                                                                                                                                                                            |
| [GridCellNestedGridModel shareColumn = [new] GridCellNestedGridModel (GridNestedAxisLayout.Normal, GridNestedAxisLayout.Shared);] |
|                                                                                                                                                                                            |
| [Model.CellModels.Add([\"ShareColumn\"], shareColumnLayoutGridModel);]                                                         |
|                                                                                                                                                                                            |
| [Model\[60, 1\].CellType = [\"ShareColumnLayoutGrid\"];]                                                                       |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [Model\[60, 1\].BorderMargins.Top = 0;]                                                                                                                |
|                                                                                                                                                                                            |
| [Model\[60, 1\].BorderMargins.Left = 0;]                                                                                                               |
|                                                                                                                                                                                            |
| [Model\[60, 1\].BorderMargins.Right = 0;]                                                                                                              |
|                                                                                                                                                                                            |
| [Model\[60, 1\].BorderMargins.Bottom = 0;]                                                                                                             |
|                                                                                                                                                                                            |
| [Model\[60, 1\].Background = SystemColors.InactiveCaptionBrush;]                                                                                       |
|                                                                                                                                                                                            |
| [GridModel nestedGridWithSharedColumnsModel = GetNestedGridWithSharedColumnsModel();]                                                                  |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Creates a nested grid with shared column layout.]                                                                                    |
|                                                                                                                                                                                            |
| [Model\[60, 1\].CellValue = nestedGridWithSharedColumnsModel;]                                                                                         |
|                                                                                                                                                                                            |
| [CoveredCells.Add([new] CoveredCellInfo(60, 1, 80, 1 + nestedGridWithSharedColumnsModel.ColumnCount - 1));]                       |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Sets up a nested grid with column layout shared]                                                                                     |
|                                                                                                                                                                                            |
| [private][ GridModel GetNestedGridWithSharedColumnsModel()]                                           |
|                                                                                                                                                                                            |
| [{]                                                                                                                                                    |
|                                                                                                                                                                                            |
| [    GridModel model = [new] GridModel();]                                                                                        |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    Pen gridLinePen = [new] Pen(Brushes.DarkGray, 1);]                                                                           |
|                                                                                                                                                                                            |
| [    gridLinePen.Freeze();]                                                                                                                            |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    model.Options.AllowSelection = GridSelectionFlags.Cell;]                                                                                          |
|                                                                                                                                                                                            |
| [    model.ColumnWidths.HeaderLineCount = 1;]                                                                                                          |
|                                                                                                                                                                                            |
| [    model.ColumnCount = 10;]                                                                                                                          |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    model.RowHeights.HeaderLineCount = 1;]                                                                                                            |
|                                                                                                                                                                                            |
| [    model.RowHeights.FooterLineCount = 1;]                                                                                                            |
|                                                                                                                                                                                            |
| [    model.RowCount = 13;]                                                                                                                             |
|                                                                                                                                                                                            |
| [    model.RowHeights.DefaultLineSize = 30;]                                                                                                           |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    Color clr = Color.FromArgb(128, 0, 0, 0);]                                                                                                        |
|                                                                                                                                                                                            |
| [    Brush headerBrush = [new] SolidColorBrush(clr);]                                                                             |
|                                                                                                                                                                                            |
| [    headerBrush.Freeze();]                                                                                                                            |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    Color clr2 = Color.FromArgb(128, 128, 0, 0);]                                                                                                     |
|                                                                                                                                                                                            |
| [    Brush footerBrush = [new] SolidColorBrush(clr2);]                                                                            |
|                                                                                                                                                                                            |
| [    footerBrush.Freeze();]                                                                                                                            |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    [for] ([int] n = 0; n \< model.RowCount; n++)]                                                          |
|                                                                                                                                                                                            |
| [    {]                                                                                                                                                |
|                                                                                                                                                                                            |
| [        [for] ([int] c = 0; c \< model.ColumnCount; c++)]                                                   |
|                                                                                                                                                                                            |
| [        {]                                                                                                                                            |
|                                                                                                                                                                                            |
| [            GridStyleInfo ci = [new] GridStyleInfo();]                                                                           |
|                                                                                                                                                                                            |
| [            ci.CellType = [\"TextBox\"];]                                                                                     |
|                                                                                                                                                                                            |
| [            ci.CellValue = String.Format([\"{0}:{1}\"], n, c);]                                                               |
|                                                                                                                                                                                            |
| [            ci.BorderMargins.Top = gridLinePen.Thickness;]                                                                                            |
|                                                                                                                                                                                            |
| [            ci.BorderMargins.Left = gridLinePen.Thickness;]                                                                                           |
|                                                                                                                                                                                            |
| [            ci.BorderMargins.Right = gridLinePen.Thickness / 2;]                                                                                      |
|                                                                                                                                                                                            |
| [            ci.BorderMargins.Bottom = gridLinePen.Thickness / 2;]                                                                                     |
|                                                                                                                                                                                            |
| [            ci.Borders.Right = gridLinePen;]                                                                                                          |
|                                                                                                                                                                                            |
| [            ci.Background = [null];[// Brushes.White;]]                                                    |
|                                                                                                                                                                                            |
| [            ci.Borders.Bottom = gridLinePen;]                                                                                                         |
|                                                                                                                                                                                            |
| [            model.Data\[n, c\] = ci.Store;]                                                                                                           |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [            [if] (c == 0 \|\| n == 0)]                                                                                           |
|                                                                                                                                                                                            |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                            |
| [                ci.CellType = [\"Static\"];]                                                                                  |
|                                                                                                                                                                                            |
| [                ci.Background = headerBrush;]                                                                                                         |
|                                                                                                                                                                                            |
| [            }]                                                                                                                                        |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [            [if] (c == 3 \|\| n == 3)]                                                                                           |
|                                                                                                                                                                                            |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                            |
| [                ci.CellType = [\"CheckBox\"];]                                                                                |
|                                                                                                                                                                                            |
| [                ci.CellValue = [false];]                                                                                         |
|                                                                                                                                                                                            |
| [            }]                                                                                                                                        |
|                                                                                                                                                                                            |
| [            [if] (c == 4 \|\| n == 4)]                                                                                           |
|                                                                                                                                                                                            |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                            |
| [                ci.CellType = [\"Static\"];]                                                                                  |
|                                                                                                                                                                                            |
| [                ci.CellValue = [\"Static\"];]                                                                                 |
|                                                                                                                                                                                            |
| [            }]                                                                                                                                        |
|                                                                                                                                                                                            |
| [            [if] (n == model.RowCount - 1)]                                                                                      |
|                                                                                                                                                                                            |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                            |
| [                ci.CellType = [\"Static\"];]                                                                                  |
|                                                                                                                                                                                            |
| [                ci.Background = footerBrush;]                                                                                                         |
|                                                                                                                                                                                            |
| [            }]                                                                                                                                        |
|                                                                                                                                                                                            |
| [        }]                                                                                                                                            |
|                                                                                                                                                                                            |
| [    }]                                                                                                                                                |
|                                                                                                                                                                                            |
| [    model.SelectedCells = GridRangeInfo.Empty;]                                                                                                       |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [    [return] model;]                                                                                                             |
|                                                                                                                                                                                            |
| [}]                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 37: Nested Grid-Columns tied to the Parent Grid Columns

 

Nested Grid Inside a Covered Range with its Rows and Columns Independent of Parent Grid

In this case, the nested grid maintains its own row heights and column widths. You can scroll through this grid without scrolling the parent grid. Resizing rows and columns in this grid will also not affect the parent grid.

 

Example

To make rows and columns independent of parent grid, the GridNestedAxisLayout enum must be set to Normal in both the parameters.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                          |
| [// Add Nested Grid cell model.]                                                                                                       |
|                                                                                                                                                                                          |
| [GridCellNestedGridModel gridModel = [new] GridCellNestedGridModel (GridNestedAxisLayout.Normal, GridNestedAxisLayout.Normal);] |
|                                                                                                                                                                                          |
| [Model.CellModels.Add([\"Grid\"], gridModel);]                                                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [CoveredCells.Add([new] CoveredCellInfo(6, 2, 8, 4));]                                                                          |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [Model\[6, 2\].CellType = [\"Grid\"];]                                                                                       |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Create a simple nested grid.]                                                                                                      |
|                                                                                                                                                                                          |
| [GridModel model = [new] GridModel();]                                                                                          |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [model.Options.AllowSelection = GridSelectionFlags.Cell;]                                                                                            |
|                                                                                                                                                                                          |
| [model.RowHeights.DefaultLineSize = 20;]                                                                                                             |
|                                                                                                                                                                                          |
| [model.RowCount = 20;]                                                                                                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [model.ColumnWidths.DefaultLineSize = 50;]                                                                                                           |
|                                                                                                                                                                                          |
| [model.ColumnCount = 8;]                                                                                                                             |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [model.HeaderRows = 0;]                                                                                                                              |
|                                                                                                                                                                                          |
| [model.FrozenRows = 0;]                                                                                                                              |
|                                                                                                                                                                                          |
| [model.HeaderColumns = 1;]                                                                                                                           |
|                                                                                                                                                                                          |
| [model.FrozenColumns = 1;]                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [for][ ([int] n = 0; n \< model.RowCount; n++)]                                |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [    [for] ([int] c = 0; c \< model.ColumnCount; c++)]                                                     |
|                                                                                                                                                                                          |
| [    {]                                                                                                                                              |
|                                                                                                                                                                                          |
| [        GridStyleInfo ci = [new] GridStyleInfo();]                                                                             |
|                                                                                                                                                                                          |
| [        ci.CellType = [\"TextBox\"];]                                                                                       |
|                                                                                                                                                                                          |
| [        ci.CellValue = String.Format([\"{0}:{1}\"], n, c);]                                                                 |
|                                                                                                                                                                                          |
| [        [//ci.Background =  transparentBlanchedAlmond;]]                                                                      |
|                                                                                                                                                                                          |
| [        model.Data\[n, c\] = ci.Store;]                                                                                                             |
|                                                                                                                                                                                          |
| [    }]                                                                                                                                              |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                  |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [Model\[6, 2\].CellValue = model;]                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 38: Nested Grid-Rows and Columns Independent of Parent Grid


{border="0"}Note: For complete code, please refer to the following browser sample.


*[]* 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Nested Grid Demo***

**** 

[]{#related-topics}

