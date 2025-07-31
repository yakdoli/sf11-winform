---
title: enablesmigrationofnetgridtoesssentialgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\enablesmigrationofnetgridtoesssentialgrid.md
created_at: 2025-07-03
---






#### Enables Migration of .Net Grid to Esssential Grid {#enables-migration-of-.net-grid-to-esssential-grid style="tab-stops: 0pt"}

**[]** 

Look-up table that Enables Migration of .Net Grid to Esssential Grid

**[]** 

The following section contains document that enables users to migrate **.Net Grid** to **Esssential Grid**. Most of the properties, events, methods have common name in both the grid. So it is not included in the following table. Since the API of both the grid is different, following document contains only common features that can be implemented with single line of code.

 

**Equivalent Properties available**

**[]** 


+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| .Net Grid                 | Esssential Grid          | Description                                                                                                           |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| AllowDrop                 | AllowDrop                | Gets or sets a value indicating whether the control can accept data that                                              |
|                           |                          |                                                                                                                       |
|                           |                          | the user drags into it.                                                                                               |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| AllowUserToAddRows        | EnableAddNew             | Gets or sets a value indicating whether the option to add rows is displayed.                                          |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| AllowUserToDeleteRows     | EnableRemove             | Gets or sets a value indicating whether it allows delete the rows.                                                    |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| AllowUserToResizeColumns  | ResizeRowsBehavior       | Gets or sets a value indicating whether the it allows dragging of selected columns for rearranging.                   |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| AllowUserToResizeRows     | ResizeRowsBehavior       | Gets or sets a value indicating wheather row is resizable.                                                            |
|                           |                          |                                                                                                                       |
|                           |                          |                                                                                                                       |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ColumnCount               |  Model.ColCount          | Gets or sets the number of columns displayed                                                                          |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ColumnHeadersHeight       | Model.RowHeights\[0\]    | Gets or sets the width of the row.                                                                                    |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ColumnHeadersVisible      | Properties.ColHeaders    | Gets or sets a value indicating whether the column header row is displayed.                                           |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| HorizontalScrollingOffset | HScrollIncrement         | Gets or sets the number of pixels by which the control is scrolled horizontally.                                      |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| GridColor                 | Properties.GridLineColor | Gets or sets the color of the grid lines separating the cells.                                                        |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| MultiSelect               | AllowSelection           | Gets or sets a value indicating whether more than one cell, row, or column can be selected.                           |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| RowCount                  | Model.RowCount           | Gets or sets the number of rows displayed.                                                                            |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| RowHeadersVisible         | Properties.RowHeaders    | Gets or sets a value indicating whether the column that contains row headers is displayed.                            |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| RowHeadersWidth           | Model.ColWidths\[0\]     | Gets or sets the width of the column.                                                                                 |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| VerticalScrollingOffset   | VScrollIncrement         | Gets the number of pixels by which the control is scrolled vertically.                                                |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| IsCurrentCellInEditMode   | CurrentCell.IsEditing    | Gets a value indicating whether the currently active cell is being edited.                                            |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+
| RightToLeft               | RightToLeft              | Gets or sets a value indicating whether control\'s elements are aligned to support locales using right-to-left fonts. |
+---------------------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------+


[] 

[] 

[] 

Equivalent Events available

**[]** 


  ------------------------ -------------------------- -------------------------------------------------------------------------------------------
  .Net Grid                Esssential Grid            Description
  BackgroundColorChanged   BackColorChanged           Occurs when the value of the **System.Windows.Forms.Control.BackColor** property changes.
  CellMouseEnter           CellMouseHoverEnter        Occurs when the mouse pointer hovers over a cell.
  CellMouseLeave           CellMouseHoverLeave        Occurs when the mouse pointer leaves a cell.
  CellPainting             CellDrawn                  Occurs when a cell needs to be drawn.
  ColumnWidthChanged       Model.ColWidthsChanged     Occurs when column width changes.
  DataSourceChanged        Binder.DataSourceChanged   Occurs when the **DataSource** property is changed.
  RowsRemoved              Model.RowsRemoved          Occurs when a row/ rows are deleted.
  SelectionChanged         Model.SelectionChanged     Occurs when current selection changes.
  SelectionChanged         Model.RowHeightsChanged    Occurs when row height changes.
  ------------------------ -------------------------- -------------------------------------------------------------------------------------------


**[]** 

[] 

Methods

 


+-----------------------+-------------------------+-----------------------------------------------------------------+
| .Net Grid             | Esssential Grid         | Description                                                     |
+-----------------------+-------------------------+-----------------------------------------------------------------+
| ClearSelection()      | Selections.Clear()      | Clears the current selection by unselecting all selected cells. |
+-----------------------+-------------------------+-----------------------------------------------------------------+
| InvalidateCell()      | Model.InvalidateRange() | Invalidates the specified cell                                  |
|                       |                         |                                                                 |
|                       |                         | forcing it to be repainted.                                     |
+-----------------------+-------------------------+-----------------------------------------------------------------+
| InvalidateColumn()    | Model.InvalidateRange() | Invalidates the specified column                                |
|                       |                         |                                                                 |
|                       |                         | forcing it to be repainted.                                     |
+-----------------------+-------------------------+-----------------------------------------------------------------+
| InvalidateRow         | Model.InvalidateRange() | Invalidates the specified row                                   |
|                       |                         |                                                                 |
|                       |                         | forcing it to be repainted.                                     |
+-----------------------+-------------------------+-----------------------------------------------------------------+
| RefreshEdit           | CurrentCell.Refresh()   | Refreshes the value of the current cell                         |
+-----------------------+-------------------------+-----------------------------------------------------------------+


[] 

[] 

[]{#related-topics}

