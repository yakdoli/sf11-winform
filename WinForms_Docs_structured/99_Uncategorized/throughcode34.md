---
title: throughcode34.md
original_path: WinForms_Docs/99_Uncategorized/throughcode34.md
created_at: 2025-08-05
---






#### Through Code {#through-code style="tab-stops: 0pt"}

[] 

Here are some code samples that will create a DataTable and bind it a to Grid Data Bound Grid. Once you have a **DataTable** object populated you can use the **GridDataBoundGrid.DataSource** property to implement the binding.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [DataTable][ myDataTable = [new] [DataTable]([\"MyDataTable\"]);] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [// Declare the Data Column and Data Row variables.]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [DataColumn][ myDataColumn;]                                                                                                           |
|                                                                                                                                                                                                                                |
| [DataRow][ myDataRow;]                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [// Create a new Data Column, set the Data Type and Column Name and add to the Data Table.   ]                                                                               |
|                                                                                                                                                                                                                                |
| [myDataColumn = [new] [DataColumn]();]                                                                                                        |
|                                                                                                                                                                                                                                |
| [myDataColumn.DataType = System.[Type].GetType([\"System.Int32\"]);]                                                                       |
|                                                                                                                                                                                                                                |
| [myDataColumn.ColumnName = [\"id\"];]                                                                                                                              |
|                                                                                                                                                                                                                                |
| [myDataTable.Columns.Add(myDataColumn);]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [// Create a second column.]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [myDataColumn = [new] [DataColumn]();]                                                                                                        |
|                                                                                                                                                                                                                                |
| [myDataColumn.DataType = [Type].GetType([\"System.String\"]);]                                                                             |
|                                                                                                                                                                                                                                |
| [myDataColumn.ColumnName = [\"item\"];]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [myDataTable.Columns.Add(myDataColumn);]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [// Create new Data Row objects and add to the Data Table.    ]                                                                                                              |
|                                                                                                                                                                                                                                |
| [for][ ([int] i = 0; i \<= 10; i++)]                                                                                 |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [    myDataRow = myDataTable.NewRow();]                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [    myDataRow\[[\"id\"]\] = i;]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [    myDataRow\[[\"item\"]\] = [\"item \"] + i.ToString();]                                                                                |
|                                                                                                                                                                                                                                |
| [    myDataTable.Rows.Add(myDataRow);]                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [this][.GridDataBoundGrid1.DataSource = myDataTable;]                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [// Size the columns.]                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [this][.GridDataBoundGrid1.Model.ColWidths\[1\] = 30;]                                                                                    |
|                                                                                                                                                                                                                                |
| [this][.GridDataBoundGrid1.Model.ColWidths\[2\] = 50;]                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [Dim][ myDataTable [As] DataTable = [New] DataTable([\"MyDataTable\"])] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\' Declare the Data Column and Data Row variables.]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [Dim][ myDataColumn [As] DataColumn]                                                                                 |
|                                                                                                                                                                                                                                |
| [Dim][ myDataRow [As] DataRow]                                                                                       |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\' Create a new Data Column, set the Data Type and Column Name and add to the Data Table. ]                                                                                 |
|                                                                                                                                                                                                                                |
| [myDataColumn = [New] DataColumn()]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [myDataColumn.DataType = System.Type.GetType([\"System.Int32\"])]                                                                                                  |
|                                                                                                                                                                                                                                |
| [myDataColumn.ColumnName = [\"id\"]]                                                                                                                               |
|                                                                                                                                                                                                                                |
| [myDataTable.Columns.Add(myDataColumn)]                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\' Create a second column.]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [myDataColumn = [New] DataColumn()]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [myDataColumn.DataType = Type.GetType([\"System.String\"])]                                                                                                        |
|                                                                                                                                                                                                                                |
| [myDataColumn.ColumnName = [\"item\"]]                                                                                                                             |
|                                                                                                                                                                                                                                |
| [myDataTable.Columns.Add(myDataColumn)]                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\' Create new Data Row objects and add to the Data Table.    ]                                                                                                              |
|                                                                                                                                                                                                                                |
| [Dim][ i [As] [Integer]]                                                                        |
|                                                                                                                                                                                                                                |
| [For][ i = 0 [To] 10]                                                                                                |
|                                                                                                                                                                                                                                |
| [myDataRow = myDataTable.NewRow]                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [myDataRow([\"id\"]) = i]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [myDataRow([\"item\"]) = [\"item \"] & i]                                                                                                  |
|                                                                                                                                                                                                                                |
| [myDataTable.Rows.Add(myDataRow)]                                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [Next][ i]                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.DataSource = myDataTable]                                                                                        |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\' Size the columns.]                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.Model.ColWidths(1) = 30]                                                                                         |
|                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.Model.ColWidths(2) = 50]                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

