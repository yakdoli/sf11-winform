---
title: excel2003.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\excel2003.md
created_at: 2025-07-03
---






#### Excel 2003 {#excel-2003 style="tab-stops: 0pt"}

**[]** 

XlsIO supports the usage of Pivot Tables in a Template file. It is even possible to dynamically refresh the data in a pivot table by using XlsIO. The following steps illustrate how to do this.

[] 

[·      ]Create the pivot table using MS Excel GUI.

[·      ]Specify the named range to be the data source of the pivot table.

[·      ]Make sure that the \"Refresh On Open\" option of the pivot table is selected.

[·      ]Dynamically refresh the data in the Named Range.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [// Change the range values that the Pivot Tables range refers to.]                                                     |
|                                                                                                                                                                           |
| [myWorkbook.Names\[[\"PivotRange\"]\].RefersToRange = mySheet.Range\[[\"A1:D27\"]\];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [\' Change the range values that the Pivot Tables range refers to.]                                                                                                         |
|                                                                                                                                                                                                                               |
| [Private][ myWorkbook.Names([\"PivotRange\"]).RefersToRange = mySheet.Range([\"A1:D27\"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

