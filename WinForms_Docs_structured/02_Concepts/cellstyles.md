---
title: cellstyles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\cellstyles.md
created_at: 2025-07-03
---






#### Cell Styles {#cell-styles style="tab-stops: 0pt"}

[] 

The Essential Grid\'s cell style architecture plays an integral role in almost every aspect of Essential Grid. The display system hosts a powerful and complete Styles architecture. Settings can be specified at the cell level or at higher levels using parent styles that are referred to as Base Styles. Base Styles can affect a groups of cells. Cell level settings override any higher-level settings and enable easy customization to cell level. With this initial version, Syncfusion\'s core focus has been on the underlying architecture for displaying cells with virtualized cell editors to enable good performance characteristics.

 

Following are the two cell styles available:

[] 

Volatile Cell Styles

[] 

QueryCellInfo will be raised the first time you access the contents of a cell with a call to Grid.Model\[rowIndex, columnIndex\] or when the grid calls this indexer internally before painting cells. The indexer returns an object of type GridStyleInfo. After querying the cell contents they remain cached in a volatile cache that holds weak references to the cell styles. This ensures that this data is available for reuse when needed. At the same time it does not stand in the way of the garbage collector if memory needs to be freed. Once a style gets garbage collected it will be removed from the volatile cache. You can manually force QueryCellInfo to be called again when you call GridControl.InvalidateCell(cell) or GridModel.VolatileCellStyles.Clear(cell).

**[]** 

Render Cell Styles

[] 

Prior to display of a cell, the PrepareRenderCell event is raised. This event is not raised from the Model. Instead it is raised from the GridControlBase directly. This has the advantage that if you want multiple grids to display the same Model, individual grids can override the cell contents individually.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [// view specific cell color]                                                                                                                              |
|                                                                                                                                                                                                                              |
| [grid.PrepareRenderCell += [new] GridPrepareRenderCellEventHandler(grid_PrepareRenderCell);]                                                        |
|                                                                                                                                                                                                                              |
| [void][ grid_PrepareRenderCell([object] sender, GridPrepareRenderCellEventArgs e)] |
|                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [    [if] (e.Cell.RowIndex \> 0 && e.Cell.ColumnIndex \> 0)]                                                                                        |
|                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                  |
|                                                                                                                                                                                                                              |
| [        [if] (e.Cell.RowIndex % 2 == 0)]                                                                                                           |
|                                                                                                                                                                                                                              |
| [            e.Style.Background = [Brushes].LightSkyBlue;]                                                                                       |
|                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                  |
|                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

PrepareRenderCell is used to initialize the so called RenderStyles. RenderStyles are of type GridRenderStyleInfo and derive from GridStyleInfo. GridRenderStyleInfo are tied to a GridControlBase instance. The render style provides additional properties to obtain access to the associated GridControl , CellRenderer and the underlying ModelStyle instance from the volatile cells cache described earlier.

 

To access the render style for a cell you can call GridControlBase.GetRenderStyleInfo.

 

Render Styles are created only for the cells that are visible and will be discarded the moment a cell is scrolled out of view (with the exception being if the current cell is scrolled out of view; they are retained in such case alone).

 

In contrast, Volatile Cell Styles from the GridModel are often also created for cells outside the viewable area and can stay in the cache even when a cell is scrolled out of view.

 

A basic understanding of this layered cell style architecture will help you understand and learn grid behaviors. This is particularly important when you are trying to modify or extend some existing functionality.

[] 

See Also

[] 

More:







