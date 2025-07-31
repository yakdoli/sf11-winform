---
title: pivotitem1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pivotitem1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### PivotItem {#pivotitem style="tab-stops: 0pt"}

 

A pivot item is an item in a PivotTable field. PivotItem provides the information needed to define a pivot item for either a row or column pivot. It consists of the following fields.

+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------+----------------+
|                  |                                                                                                                                                                |             |                  |                |
|                  |                                                                                                                                                                |             |                  |                |
| Property Name    | Description                                                                                                                                                    | Type        | Value it Accepts | Reference link |
|                  |                                                                                                                                                                |             |                  |                |
|                  |                                                                                                                                                                |             |                  |                |
+==================+================================================================================================================================================================+=============+==================+================+
| Comparer         | Gets or sets the IComparer object used for sorting. If this value is null, then sorting will be performed under the assumption that this field is IComparable. | IComparer   | \-               | \-             |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------+----------------+
| FieldHeader      | Gets or sets the title you want to see in the header for this pivot item.                                                                                      | string      | \-               | \-             |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------+----------------+
| FieldMappingName | Gets or sets the property\'s mapping name.                                                                                                                     | string      | \-               | \-             |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------+----------------+
| Format           | Gets or sets the format item for the specified field.                                                                                                          | string      | \-               | \-             |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------+----------------+
| TotalHeader      | Gets or sets the string you want appended to the pivot item\'s summary cells.                                                                                  | string      | \-               | \-             |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------+----------------+

 

More:







