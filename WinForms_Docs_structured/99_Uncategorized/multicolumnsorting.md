---
title: multicolumnsorting.md
original_path: WinForms_Docs/99_Uncategorized/multicolumnsorting.md
created_at: 2025-08-05
---






##### Multicolumn Sorting {#multicolumn-sorting style="tab-stops: 0pt"}

To apply sorting on more than one column at run time, click the desired column headers by pressing the CTRL key.

 

Below is the code that sorts the grid by two columns:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][GridDataControl][ x][:][Name][=\"dataGrid\"][ [AutoPopulateColumns][=\"True\"] [AutoPopulateRelations][=\"False\"] [ItemsSource][=\"{][StaticResource][ customerSource][}\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<][syncfusion][:][GridDataControl.SortColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [         ][\<][syncfusion][:][GridDataSortColumn][ ColumnName][=\"CompanyName\"][ SortDirection][=\"Ascending\" /\>]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [         ][\<][syncfusion][:][GridDataSortColumn][ ColumnName][=\"ContactTitle\"][ SortDirection][=\"Descending\" /\>]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\</][syncfusion][:][GridDataControl.SortColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][GridDataControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: When the grid is sorted against multiple columns, the affected column headers will get painted with a number that starts from 0, 1 \... representing the sort order.


 

The following screen shot shows a multicolumn sorting enabled GDC:

 

{border="0"}

Figure 170: Sorting by two column, \"CompanyName\" and \"ContactTitle\"

***[]*** 

Multicolumn sorting feature is now enabled in GridData control.

 

[]{#related-topics}

