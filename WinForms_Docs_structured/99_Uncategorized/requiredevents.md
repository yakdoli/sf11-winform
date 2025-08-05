---
title: requiredevents.md
original_path: WinForms_Docs/99_Uncategorized/requiredevents.md
created_at: 2025-08-05
---






##### Required Events {#required-events style="tab-stops: 0pt"}

[] 

These are the three events that you should handle in order to implement a virtual grid. They provide the basic information about the number of rows, columns and the values for your data.

[] 

 

[]{#p305} 

###### 4.1.4.11.1.1        QueryRowCount Event {#queryrowcount-event style="tab-stops: 0pt"}

[] 

This event is used to return the row count on demand. Here is a sample handler.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [private][ [void] GridQueryRowCount([object] sender, [GridRowColCountEventArgs] e)] |
|                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [    [// Determine number of rows.]]                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [    e.Count = [this].numArrayRows;]                                                                                                                                              |
|                                                                                                                                                                                                                                            |
| [    e.Handled = [true];]                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private Sub][ GridQueryRowCount(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ GridRowColCountEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Determine number of rows.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [e.Count = ][Me][.numArrayRows]                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [e.Handled = ][True]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p306} 

 

###### 4.1.4.11.1.2        QueryColCount Event {#querycolcount-event style="tab-stops: 0pt"}

[] 

The **QueryColCount** event is used to return the column count on demand. Note that when you handle the event by assigning e.Count, you are setting the e.Handled property to true.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [private][ [void] GridQueryColCount([object] sender, [GridRowColCountEventArgs] e)] |
|                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [    [// Determine the number of columns.]]                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [    e.Count = [this].numArrayCols;]                                                                                                                                              |
|                                                                                                                                                                                                                                            |
| [    e.Handled = [true];]                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private Sub][ GridQueryColCount(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ GridRowColCountEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Determine the number of columns.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [e.Count = ][Me][.numArrayCols]                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [e.Handled = ][True]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p307} 

 

###### 4.1.4.11.1.3        QueryCellInfo Event {#querycellinfo-event style="tab-stops: 0pt"}

[] 

**QueryCellInfo** is the workhorse event. It is used to provide the **GridStyleInfo** object for a given cell. In your handler for this event, you would normally set the **CellValue** for the GridStyleInfo object passed in with the event arguments. But, you can also set other members of this GridStyleInfo object. For example, you can set the BackColor to change the cell background. All of this is done on a demand basis. The **BackColor** value is not stored in any grid storage. There is another event, **PrepareViewStyleInfo** that you can handle to make a transient adjustment to a style just before it is displayed. This event is discussed in more detail later in this section.

 

The **GridQueryCellInfoEventArgs** members, e.ColIndex and e.RowIndex, specify the column and row of the requested style. The e.Style member holds the GridStyleInfo object whose value this event should set provided it is a cell that you want to populate. It is possible that e.ColIndex and / or e.RowIndex may have the value of -1. A -1 indicating that a **rowstyle** or **columnstyle** is being requested. So, e.ColIndex = -1 and e.RowIndex = 4 indicates that the rowstyle for row 4 is being requested (GridControl.RowStyles\[4\]). Similarly, a positive column value with the row value = -1 would be a request for that particular columnstyle. If both values are -1, then the **TableStyle** property is being requested.

 

One last comment before we look at the code. Header rows and columns in an Essential Grid are treated the same as other rows and columns with respect to QueryCellInfo. If you have a single header row, then anytime e.ColIndex is 0, a row header is being requested. Similarly, if you have a single column header row, e.RowIndex = 0 is a request for the column header.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [private][ [void] GridQueryCellInfo([object] sender, [GridQueryCellInfoEventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [    [if](e.ColIndex \> 0 && e.RowIndex \> 0)]                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [        [// Using indexers, pass value to a cell from a given data source.]]                                                                                                      |
|                                                                                                                                                                                                                                              |
| [        e.Style.CellValue = [this].intArray\[e.RowIndex - 1, e.ColIndex - 1\];]                                                                                                    |
|                                                                                                                                                                                                                                              |
| [        e.Handled = [true];]                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] GridQueryCellInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridQueryCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                 |
| [If][ ((e.ColIndex \> 0) [AndAlso] (e.RowIndex \> 0)) [Then]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                 |
| [\' Using indexers, pass value to a cell from a given data source.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Style.CellValue = [Me].intArray(e.RowIndex - 1, e.ColIndex - 1)]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Handled = [True]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [If]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p308} 

 

[]{#related-topics}

