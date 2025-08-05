---
title: rowsremovedandcolumnsremoved.md
original_path: WinForms_Docs/99_Uncategorized/rowsremovedandcolumnsremoved.md
created_at: 2025-08-05
---






#### RowsRemoved and ColumnsRemoved {#rowsremoved-and-columnsremoved style="tab-stops: 0pt"}

[] 

These events are triggered when a range of rows or columns are removed from the grid. Their event handlers receive an argument of type GridRangeRemovedEventArgs containing data related to these events. Following are the event argument properties that provide information about the rows or columns removal.

[] 


  ---------- --------------------------------------------------------
  Property   Description
  Count      The index of the last row or column that was removed.
  RemoveAt   The index of the first row or column that was removed.
  ---------- --------------------------------------------------------


[] 

Example

**[]** 

This event can be triggered using the following code:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                                              |
| [grid.Model.RowsRemoved += [new] [GridRangeRemovedEventHandler ](Model_RowsRemoved);]       |
|                                                                                                                                                                                              |
| [grid.Model.ColumnsRemoved += [new] [GridRangeRemovedEventHandler ](Model_ColumnsRemoved);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [void][ Model_RowsRemoved([object] sender, GridRangeRemovedEventArgs e)]    |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [    Console.WriteLine(e.RemoveAt + 1 - e.Count + [\" row(s) are removed from position \"] + e.RemoveAt);]                                |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [void][ Model_ColumnsRemoved([object] sender, GridRangeRemovedEventArgs e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [    Console.WriteLine(e.RemoveAt + 1 - e.Count + [\" column(s) are removed from position \"] + e.RemoveAt);]                             |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p207} 

 

[]{#related-topics}

