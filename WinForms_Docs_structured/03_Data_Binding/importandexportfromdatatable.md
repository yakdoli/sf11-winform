---
title: importandexportfromdatatable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\importandexportfromdatatable.md
created_at: 2025-07-03
---








  









### Import and Export from Data Table {#import-and-export-from-data-table style="tab-stops: 0pt"}

Spreadsheet offers some helper methods that enable you to import and export data form ADO.NET data sources very easily. The ImportDataTable and ExportDataTable methods allow you to use one line of code to import data from a Datatable to a SpreadSheet and export data from a SpreadSheet to a DataTable respectively.

{border="0"}

Figure 30: Importing from Data Table

 

Samples Link

The samples for Importing from data table are located at:

**Essential Studio Dashboard \> Spreadsheet \> Data Management \> Import Data Table.**

Refer to section 2.2 Samples and Location to access the samples location.

 

Methods


+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| Method              | Description                                                                                                                                                                                                                                                                                                                     | Parameters                                                                                                                         | Type        | Return Type |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| ImportFromDataTable | This method imports data from the DataTable into the Spreadsheet.                                                                                                                                                                                                                                                               |  ImportDataTable(DataTable dataTable)                                                                                              | N/A         | void        |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| ImportFromDataTable | This method imports data from a DataTable into a Spreadsheet with parameters Row and Column of the first cell, where DataTable should be imported.                                                                                                                                                                              | ImportFromDataTable(DataTable table, bool isFieldNameShow, int startRow, int startCol)                                             | N/A         | void        |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| ImportFromDataTable | This method imports data from a DataTable into a Spreadsheet with parameters  Row index and column index of SpreadSheet, where DataTable should be imported and preserve types  (This Indicates whether Spreadsheet should try to preserve types in DataTable)[] | ImportFromDataTable(DataTable table, bool isFieldNameShow, int startRow, int startCol, bool preserveTypes)                         | N/A         | void        |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| ImportFromDataTable | This method imports data from a DataTable into a Spreadsheet with parameters starting row index and column index and maximum number of rows and columns to import.[]                                                                                             | ImportFromDataTable(DataTable table, bool isFieldNameShow, int startRow, int startCol, int maxRow, int maxCol)                     | N/A         | void        |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------+
| ImportFromDataTable | This method imports data from a DataTable into a Spreadsheet with parameters starting row index and column index and maximum number of rows and columns to import and preserve types.[]                                                                          | ImportFromDataTable(DataTable table, bool isFieldNameShow, int startRow, int startCol, int maxRow, int maxCol, bool preserveTypes) | N/A         | void        |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
|                     |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |             |             |
+=====================+=================================================================================================================================================================================================================================================================================================================================+====================================================================================================================================+=============+=============+


 

More:







