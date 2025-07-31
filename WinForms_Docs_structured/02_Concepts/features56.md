---
title: features56.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\features56.md
created_at: 2025-07-03
---






##### Features {#features style="tab-stops: 0pt"}

###### 4.2.4.1.1.1 Entire Content {#entire-content style="tab-stops: 0pt"}

You can convert the entire content of a GridDataControl to an Excel Spreadsheet. You can also avail the option for specifying the version of the Excel file using the ExcelVersion  enum. The version can be one of the following:

 

[·      ]ExcelVersion.Excel97to2003  

[·      ]ExcelVersion.Excel2007

 

The following code illustrates the conversion of GridDataControl contents to an Excel Spreadsheet:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                            |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| [gridDataControl.ExportToExcel([\"Sample.xlsx\"], [ExcelVersion].Excel2007 );]    |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [(or)]                                                                                                                            |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [gridDataControl.ExportToExcel([\"Sample.xls\"], [ExcelVersion].Excel97to2003 );] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 236: GridDataControl

[] 

[] 

{border="0"}

Figure 237: GridDataControl content in an Excel Spreadsheet

***[]*** 

The above images shows how the entire content of the GridDataControl is exported to an Excel Spreadsheet.

[] 

###### 4.2.4.1.1.2 Selected Rows {#selected-rows style="tab-stops: 0pt"}

You can also avail the choice of converting the selected rows of GridDataControl to an Excel Spreadsheet.

 

The following code illustrates the conversion of selected rows of GridDataControl to an Excel Spreadsheet:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                         |
|                                                                                                                                                                    |
| []                                                                                                                |
|                                                                                                                                                                    |
| [grid.ExportToExcel(grid.Model.SelectedRanges.ActiveRange,[\"sample.xlsx\"], ExcelVersion.Excel2007);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

###### 4.2.4.1.1.3 GridDataControl with Nested Child {#griddatacontrol-with-nested-child style="tab-stops: 0pt"}

You can convert the content of a GridDataControl, with Nested Child to an Excel Spreadsheet. Parent and visible child content are exported to Excel Spreadsheet.

 

The following code illustrates the conversion of GridDataControl with Nested Child to an Excel Spreadsheet:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                            |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| [gridDataControl.ExportToExcel([\"Sample.xlsx\"], [ExcelVersion].Excel2007 );]    |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [(or)]                                                                                                                            |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [gridDataControl.ExportToExcel([\"Sample.xls\"], [ExcelVersion].Excel97to2003 );] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Only the visible child\'s contents will be exported.


[] 

{border="0"}

Figure 238: GridDataControl with NestedChild

***[]*** 

{border="0"}

Figure 239: GridDataControl with NestedChild content in an Excel Spreadsheet

 

The above images shows how the GridControl, with Nested Child is exported to an Excel Spreadsheet.

 

 

###### 4.2.4.1.1.4 GridDataControl with Grouping {#griddatacontrol-with-grouping style="tab-stops: 0pt"}

You can convert the content of a GridDataControl, with Grouping to an Excel Spreadsheet. The following code illustrates this feature:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                            |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| [gridDataControl.ExportToExcel([\"Sample.xlsx\"], [ExcelVersion].Excel2007 );]    |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [(or)]                                                                                                                            |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [gridDataControl.ExportToExcel([\"Sample.xls\"], [ExcelVersion].Excel97to2003 );] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note:[ ]Only the visible grouping contents will be exported.


[] 

{border="0"}

Figure 240: GridDataControl with Grouping

***[]*** 

{border="0"}

Figure 241: GridDataControl with Grouping content in an Excel spreadsheet

**[]** 

The above images shows how the GridControl, with Grouping is exported to an Excel Spreadsheet.

 

 

 

[]{#related-topics}

