---
title: rowsmovedandcolumnsmoved.md
original_path: WinForms_Docs/99_Uncategorized/rowsmovedandcolumnsmoved.md
created_at: 2025-08-05
---






#### RowsMoved and ColumnsMoved {#rowsmoved-and-columnsmoved style="tab-stops: 0pt"}

[] 

These events are raised when a range of rows or columns are moved from one position to another. Their event handlers receive an argument of type GridRangeMovedEventArgs containing data related to these events. Following are the event argument properties information about the rows or columns migration.

[] 


  ---------- --------------------------------------------------------------------
  Property   Description
  Count      The index of the last row or column that was removed.
  InsertAt   The row or column index where the cells should be inserted before.
  RemoveAt   The index of the first row or column that was removed.
  ---------- --------------------------------------------------------------------


[] 

Example

**[]** 

This event can be triggered using the following code:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [grid.Model.RowsMoved += [new] [GridRangeMovedEventHandler](Model_RowsMoved);]        |
|                                                                                                                                                                        |
| [grid.Model.ColumnsMoved += [new] [GridRangeMovedEventHandler ](Model_ColumnsMoved);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [void][ Model_RowsMoved([object] sender, GridRangeMovedEventArgs e)]                                                    |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [    Console.WriteLine(e.RemoveAt + 1 - e.Count + [\" row(s) are moved from position \"] + e.RemoveAt + [\" to position \"] + e.InsertAt);]   |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [void][ Model_ColumnsMoved([object] sender, GridRangeMovedEventArgs e)]                                                 |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [    Console.WriteLine(e.RemoveAt+ 1 - e.Count + [\" column(s) are moved from position \"] + e.RemoveAt + [\" to position \"] + e.InsertAt);] |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p206} 

 

[]{#related-topics}

