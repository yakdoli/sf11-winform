---
title: exporttoexcel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exporttoexcel.md
created_at: 2025-07-03
---








  









### Export to Excel {#export-to-excel style="tab-stops: 0pt"}

[] 

The Export feature allows us to export the Grid data into a Microsoft Excel file. This can be done through server-side**[ ]Export** method.

[] 

Class Model

[] 

The new Export feature contains the following structure of Class Model.

[] 

[·      ]**GridBaseExcelExport** - common base class for Excel export.

[·      ]**GridExcelExport** - class which has been inherited from the base class, initializes the Excel file and exports the data with styles.

[·      ]**GridExportHelperUtils** - defines the AutoFormat colors.

[] 

Features

[] 

[·      ]Exporting the Grouped tables.

[·      ]Exporting the Nested tables.

[·      ]A grid with a MultiRow record can be exported.

[·      ]Summary rows can be exported.

[·      ]The styles applied for the grid can also be exported to the Excel file.

[] 

Export Method

**[]** 

The Export method is present inside the GridExcelExport class. Export method should be called using the GridExcelExport class objects.

[] 

Excel Export

**[]** 

The GridExcelExport class constructors accept the following as arguments.

[] 

1.   The Grid object, which is going to be exported.

2.   Name of the file to which the data is going to be exported.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [GridExcelExport][ excel = [new] [GridExcelExport]([this].GridGroupingControl1, [\"excel.xls\"]);] |
|                                                                                                                                                                                                                                                                               |
| [excel.ExportNestedTable = [true];]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                               |
| [excel.Export();]                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [Dim][ excel [As] [New] GridExcelExport([Me].GridGroupingControl1, [\"excel.xls\"])] |
|                                                                                                                                                                                                                                                                 |
| [excel.ExportNestedTable = [True] ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [excel.Export()]                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Public APIs

[] 

Properties

[] 


  --------------------- ------------------------------------------------------------------------------- ---------------------
  Name                  Description                                                                     Return Type
  AutoFormat            Return the \"AutoFormat\" applied to the Grid.                                  string
  UseAutoFormat         Return True if AutoFormat is set to the Grid else False.                        bool
  ExportNestedTable     If it is set to False Nestedtables can\'t be exported. By default it is True.   bool
  FileName              Return the name of the exported file.                                           string
  GridGroupingControl   Return the reference of the Grid object, which is going to be exported.         GridGroupingControl
  --------------------- ------------------------------------------------------------------------------- ---------------------


[] 

Method

[] 


  -------- ---------------------------------------
  Name     Description
  Export   Export the Grid data into Excel file.
  -------- ---------------------------------------


[]{#related-topics}

