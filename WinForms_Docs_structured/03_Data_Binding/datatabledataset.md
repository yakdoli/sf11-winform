---
title: datatabledataset.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\datatabledataset.md
created_at: 2025-07-03
---








  









### DataTable / DataSet {#datatable-dataset style="tab-stops: 0pt"}

[] 

Binding to DataTable / DataSet

[] 

A DataTable can act as a data source to the GridGroupingControl. Columns can be added to the DataTable using DataColumn objects. To add a new row, access the **NewRow** method of DataSet.

Here is a code snippet to bind a single DataTable to the GridGroupingControl.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                           |
| [OleDbConnection][ MyOleDbConnection = [new] [OleDbConnection]([\"Provider=Microsoft.Jet.OLEDB.4.0; Data Source=\"] + Server.MapPath([\"\~/App_Data/Nwind.mdb\"]));] |
|                                                                                                                                                                                                                                                                                                                                                           |
| [OleDbDataAdapter][ MyOleDbDataAdapter = [new] [OleDbDataAdapter]();]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                           |
| [MyOleDbDataAdapter.SelectCommand = [new] [OleDbCommand]([\"SELECT TOP 10 CustomerID, CompanyName, ContactName FROM Customers\"],]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                           |
| [MyOleDbConnection);]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [DataTable][ myDataTable = [new] [DataTable]();]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [MyOleDbConnection.Open();]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                           |
| [try]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| [MyOleDbDataAdapter.Fill(myDataTable);]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| [finally]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| [MyOleDbConnection.Close();]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                           |
| [GridGroupingControl1.DataSource = myDataTable.DefaultView;]                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ MyOleDbConnection [As] [New] Data.OleDb.OleDbConnection([\"Provider=Microsoft.Jet.OLEDB.4.0; Data Source=\"] + Server.MapPath([\"\~/App_Data/Nwind.mdb\"]))] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ MyOleDbDataAdapter [As] [New] Data.OleDb.OleDbDataAdapter()]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [MyOleDbDataAdapter.SelectCommand = [New] OleDbCommand([\"SELECT TOP 10 CustomerID, CompanyName, ContactName FROM Customers\"], MyOleDbConnection) ]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ myDataTable [As] [New] Data.DataTable()]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [MyOleDbConnection.Open() ]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Try][ ]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [MyOleDbDataAdapter.Fill(myDataTable) ]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Finally][ ]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    MyOleDbConnection.Close() ]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Try]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                  |
| [GridGroupingControl1.DataSource = myDataTable.DefaultView]                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p29} 

[]{#related-topics}

