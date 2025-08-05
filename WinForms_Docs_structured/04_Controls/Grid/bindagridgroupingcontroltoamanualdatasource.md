---
title: bindagridgroupingcontroltoamanualdatasource.md
original_path: WinForms_Docs/04_Controls/Grid/bindagridgroupingcontroltoamanualdatasource.md
created_at: 2025-08-05
---






##### Bind a Grid Grouping Control to a Manual Data Source {#bind-a-grid-grouping-control-to-a-manual-data-source style="tab-stops: 0pt"}

[] 

Here are some code samples that will create a **DataTable** and bind it to a Grid Grouping control. Once you have a DataTable object populated you can use the **GridGroupingControl.DataSource** property to implement the binding.

[] 

1.   Include the required namespace.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                                |
| [using ][Synctusion.Windows.Forms.Grid.Grouping[;]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                      |
|                                                                                                                                         |
| []                                                                                  |
|                                                                                                                                         |
| [Imports ][Synctusion.Windows.Forms.Grid.Grouping] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of Grid Grouping control and specify its size.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [private][ Syncfusion.Windows.Forms.Grid.Grouping.[GridGroupingControl] gridGroupingControl1;]                             |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [this][.gridGroupingControl1 = [new] Syncfusion.Windows.Forms.Grid.Grouping.[GridGroupingControl]();] |
|                                                                                                                                                                                                                                         |
| [this][.gridGroupingControl1.Size = [new] System.Drawing.[Size](160, 200 );]                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [Private][ gridGroupingControl1 [As] Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl] |
|                                                                                                                                                                                                            |
| []                                                                                                                                                        |
|                                                                                                                                                                                                            |
| [Me][.gridGroupingControl1 = [New] Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl()] |
|                                                                                                                                                                                                            |
| [Me][.gridGroupingControl1.Size = [New] System.Drawing.Size(160, 200 )]                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Set up the Data Source.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
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
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
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
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Bind the grid grouping control to this data table by setting its **DataSource** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                      |
|                                                                                                                                                             |
| [this][.gridGroupingControl1.DataSource = myDataTable; ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| []                                                                                                  |
|                                                                                                                                                         |
| [Me][.GridGroupingControl1.DataSource = myDataTable] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Finally, add the grid grouping control to the form.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [this][.Controls.Add(][this][.gridGroupingControl1); ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [Me][.Controls.Add(][Me][.GridGroupingControl1)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   When you run the application, the grid will look like the one in the following image. You will be able to sort the data by clicking the header of the column you want to sort.

[] 

{border="0"}

*[Figure ][232][: Binding a Grid Grouping control to a Manual Data Source]*

 

[]{#p394} 

 

[]{#related-topics}

