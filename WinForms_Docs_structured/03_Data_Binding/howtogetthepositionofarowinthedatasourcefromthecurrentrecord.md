---
title: howtogetthepositionofarowinthedatasourcefromthecurrentrecord.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\howtogetthepositionofarowinthedatasourcefromthecurrentrecord.md
created_at: 2025-07-03
---






#### How to Get the Position of a Row in the DataSource from the Current Record {#how-to-get-the-position-of-a-row-in-the-datasource-from-the-current-record style="tab-stops: 0pt"}

[] 

From the row index, you can get the element displayed at that row. If it is a record row, then the element\'s parent record\'s unsorted position will give the underlying **DataRow** position.

[] 

Example

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [Table table = e.TableControl.Table;]                                                                                                                      |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Get the current display element.\                                                                                                                                                                        |
| ][Element el = table.DisplayElements\[e.rowIndex\];]                                                     |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Get the current record.\                                                                                                                                                                                 |
| ][Record r = el.ParentRecord;]                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Find its row position.\                                                                                                                                                                                  |
| ][int][ dataRowPos = table.UnsortedRecords.IndexOf(r);] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Retrieve the corresponding data row from the datasource.\                                                                                                                                                |
| ][CustomersDataRow row = dataSoure.Rows\[dataRowPos\];]                                                  |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// Access the CutomerId value of the current record.\                                                                                                                                                       |
| ][string][ id = row.CustomerId;]                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                               |
| [Dim][ table ][As Table][ = e.TableControl.Table ]                                                                      |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Get the current display element.\                                                                                                                                                                                                                                                                                         |
| ][Dim][ el ][As][ Element = table.DisplayElements(e.rowIndex)]        |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Get the current record.][\                                                                                                                                                                                                                                              |
| ][Dim][ r ][As][ Record = el.ParentRecord ]                           |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Find its row position.\                                                                                                                                                                                                                                                                                                   |
| ][Dim][ dataRowPos ][As Integer][ = table.UnsortedRecords.IndexOf(r)] |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Retrieve the corresponding data row from the datasource.][\                                                                                                                                                                                                             |
| ][Dim][ row ][As][ CustomersDataRow = dataSoure.Rows(dataRowPos)]     |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                               |
| [\' Access the CutomerId value of the current record.][\                                                                                                                                                                                                                    |
| ][Dim][ id ][As String][ = row.CustomerId]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p706} 

 

[]{#related-topics}

