---
title: rowsinsertedandcolumnsinserted.md
original_path: WinForms_Docs/99_Uncategorized/rowsinsertedandcolumnsinserted.md
created_at: 2025-08-05
---






#### RowsInserted and ColumnsInserted {#rowsinserted-and-columnsinserted style="tab-stops: 0pt"}

[] 

These events are triggered when one or more rows or columns are inserted. The event handler receives an argument of type **GridRangeInsertedEventArgs** containing data related to this event. The following **GridRangeInsertedEventArgs** properties provide information specific to these events.

[] 


  ---------- --------------------------------------------------------------------
  Property   Description
  Count      The number of rows or columns.
  InsertAt   The row or column index where the cells should be inserted before.
  ---------- --------------------------------------------------------------------


[] 

Example

[] 

This event can be triggered using the following code:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [grid.Model.RowsInserted += [new] [GridRangeInsertedEventHandler ](Model_RowsInserted);]       |
|                                                                                                                                                                                 |
| [grid.Model.ColumnsInserted += [new] [GridRangeInsertedEventHandler ](Model_ColumnsInserted);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [void][ Model_ColumnsInserted([object] sender, [GridRangeInsertedEventArgs] e)] |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [     [Console].WriteLine(e.Count + [\" columns are inserted at \"] + e.InsertAt);]                                           |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [void][ Model_RowsInserted([object] sender, [GridRangeInsertedEventArgs] e)]    |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [     [Console].WriteLine(e.Count + [\" rows are inserted at \"] + e.InsertAt);]                                              |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p205} 

 

[]{#related-topics}

