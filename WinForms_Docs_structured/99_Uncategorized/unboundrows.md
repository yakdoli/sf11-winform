---
title: unboundrows.md
original_path: WinForms_Docs/99_Uncategorized/unboundrows.md
created_at: 2025-08-05
---






#### UnboundRows {#unboundrows style="tab-stops: 0pt"}

Essential Grid supports addition of extra rows in the view which will not affect the DataSource. Such additional rows are called UnboundRows as they do not belong to the data source. These unbound fields can be used, when you want to add some additional or custom information for GridDataControl 

You can create an UnboundRow by just setting the UnboundRowCount. It contains a property named Format, which is used to specify a format for the UnboundRow. Given an UnboundRow we can check if this is an UnboundRow or not using IsInUnboundRow(int Rowindex) method in Grid Model.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    ][this][.grid.Model.UnboundRowsCount = 5;]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [    ][this][.grid.UnboundRowPosition = ][Position][.Top;] |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 164: [Unbound Rows at Top]

 

{border="0"}

Figure 165: [Unbound Rows at Bottom ]

 

Properties, Methods and Events tables

 

Properties

  Properties               Description                                                                Type Of Property   Acceptable Value   Reference Link
  ------------------------ -------------------------------------------------------------------------- ------------------ ------------------ ----------------
  **UnboundRowPosition**   Gets or sets a value, which represents the position of the Unbound Rows.   Position           Top/Bottom         NA

 

 

Methods

+-----------------------------------+--------------------------------------------------------------------------+----------------+-------------+-------------+
| Method                            | Description                                                              | Parameters     | Type        | Return Type |
+-----------------------------------+--------------------------------------------------------------------------+----------------+-------------+-------------+
| **IsInUnboundRows(int RowIndex)** | This method checks if the rows provided is an unbound row or not.        | (int RowIndex) | Integer     | Boolean     |
|                                   |                                                                          |                |             |             |
|                                   | This can be accessed from Grid Model as grid.Model.IsInUnboundRows(row); |                |             |             |
+===================================+==========================================================================+================+=============+=============+

 

[]{#related-topics}

