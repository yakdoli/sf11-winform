---
title: howtodatabindaneditcontroltoadatasource.md
original_path: WinForms_Docs/03_Data_Binding/howtodatabindaneditcontroltoadatasource.md
created_at: 2025-08-05
---








  









## How To Data Bind an Edit Control To a Datasource {#how-to-data-bind-an-edit-control-to-a-datasource style="tab-stops: 0pt"}

 

The following code snippet illustrates how an Edit Control can be data-bound to a table in a DataSet.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [// Create a new DataSet.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [this][.dataset = [new] [DataSet]([\"MyDataSet\"]);]                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Create a new DataTable.]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [this][.table = [new] [DataTable]([\"MyDataTable\"]);]                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Create a new DataColumn and add it to the DataTable.]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                     |
| [this][.datacolumn = [new] [DataColumn]([\"Code\"], System.[Type].GetType([\"System.String\"]));] |
|                                                                                                                                                                                                                                                                                                     |
| [this][.table.Columns.Add([this].datacolumn);]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Create a new DataRow, and assign it to the specific column.]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| [// Assign a string value 'program' to that DataRow-DataColumn field.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [this][.datarow = [this].table.NewRow();]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [this][.datarow\[[this].datacolumn\] = program;]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Add this DataRow to the DataTable.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [this][.table.Rows.Add([this].datarow);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Add this DataTable to the DataSet.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [this][.dataset.Tables.Add([this].table);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [// Databinding EditControl.Text to the DataColumn \"Code\",]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [// where \"Code\" contains the program to be displayed in the EditControl.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [this][.editControl1.DataBindings.Add([\"Text\"], [this].dataset.Tables\[0\], [\"Code\"]);]                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [\' Create a new DataSet.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [Me][.dataset = [New] DataSet([\"MyDataSet\"])                                    ]                              |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [\' Create a new DataTable.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [Me][.table = [New] DataTable([\"MyDataTable\"]) ]                                                               |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [\' Create a new DataColumn and add it to the DataTable.]                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [Me][.datacolumn = [New] DataColumn([\"Code\"],System.Type.GetType([\"System.String\"]))] |
|                                                                                                                                                                                                                                                   |
| [Me][.table.Columns.Add([Me].datacolumn)]                                                                                               |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [\' Create a new DataRow, and assign it to the specific column.]                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [\' Assign a string value 'program' to that DataRow-DataColumn field.]                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [Me][.datarow = [Me].table.NewRow()]                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [Me][.datarow([Me].datacolumn) = program ]                                                                                              |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [\' Add this DataRow to the DataTable.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [Me][.table.Rows.Add([Me].datarow) ]                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [\' Add this DataTable to the DataSet.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [Me][.dataset.Tables.Add([Me].table)]                                                                                                   |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [\' Databinding EditControl.Text to the DataColumn \"Code\",]                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [\' where \"Code\" contains the program to be displayed in the EditControl.]                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [Me][.editControl1.DataBindings.Add([\"Text\"], [Me].dataset.Tables(0), [\"Code\"])]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p187} 

[]{#related-topics}

