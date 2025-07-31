---
title: events2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\events2.md
created_at: 2025-07-03
---








  









### Events {#events style="tab-stops: 0pt"}

This section lists the server-side and client-side events of the Grid Grouping control.[]{#p115}

Server-side Events[]

The server-side events are listed in the below table with descriptions:

[] 


  ------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Event Name                     Description
  QueryCellStyleInfo             It occurs for each cell before it gets rendered. Using this event you can customize the contents of the cell.
  QueryCoveredRange              Occurs to determine if the cell belongs to a covered range and returns the covered range of the cell.
  CurrentRecordContextChanged    Occurs before and after the status of the current record is changed. Using the CurrentRecordContextChangeEventArgs.Action you can get information on which record, state was changed.
  DataSourceControlRowAdding     Occurs before adding a new record in the bound DataSourceControl.
  DataSourceControlRowUpdating   Occurs before updating a record in the bound DataSourceControl.
  DataSourceControlRowDeleting   Occurs before deleting a record in the bound DataSourceControl.
  RowDataBound                   Occurs when a data row is bound to data in a GridGroupingControl.
  GroupedColumnsChanged          Occurs when a column is added or removed from the GroupedColumns collection.
  SortedColumnsChanged           Occurs when a column is added or removed from the SortedColumns collection.
  SearchDataSourceEvent          Occurs after the search button is clicked in the SearchTextBox.
  RecordDoubleClicked            Occurs after the record is double clicked.
  ------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

Client-side Events

[] 

The client-side events are listed in the below table with description.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------+
| Event Name                        | Description                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnRecordClick           | Specifies the client side function to call, when record is clicked.                            |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnSelectionChanged      | Specifies the client side function to call, when the selection of records are getting changed. |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideColumnResizing          | Specifies the client side function to call, when the columns are getting resized.              |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnBeginDragRows         | Specifies the client side function to call, when rows are dragged.                             |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnCellValidate          | Specifies the client side function to call, when cell is clicked in the ExcelEditMode.         |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnRowMouseOut           | Specifies the client side function to call, when record is hovered out.                        |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnRowMouseOver          | Specifies the client side function to call, when record is hovered.                            |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnRowsDropping          | Specifies the client side function to call, when rows are dropped.                             |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| ClientSideOnRowDoubleClick        | Specifies the client side function to call, when record is double clicked                      |
|                                   |                                                                                                |
|                                   |                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------+


 

 

[]{#related-topics}

