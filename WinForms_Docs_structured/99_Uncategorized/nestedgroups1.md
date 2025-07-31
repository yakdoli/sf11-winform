---
title: nestedgroups1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nestedgroups1.md
created_at: 2025-07-03
---






##### Nested Groups {#nested-groups style="tab-stops: 0pt"}

When you have the grid data grouped against more than one column, the groups will be nested in different levels forming a hierarchical, multilevel structure. You can expand or collapse the underlying groups and records from a parent group by clicking the PlusMinus button preceding its group caption.

 

MultiColumn (Nested) groups can be easily created by simply adding multiple columns into the GroupedColumns collection. You can also generate multilevel groups by just dragging multiple column headers into the group drop area.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [GridDataGroupColumn][ groupedCol1 = [new] [GridDataGroupColumn]();] |
|                                                                                                                                                                                                           |
| [groupedCol1.ColumnName = [\"ShipCountry\"];]                                                                                                 |
|                                                                                                                                                                                                           |
| [dataGrid.GroupedColumns.Add(groupedCol1);]                                                                                                                           |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [GridDataGroupColumn][ groupedCol2 = [new] [GridDataGroupColumn]();] |
|                                                                                                                                                                                                           |
| [groupedCol2.ColumnName = [\"EmployeeID\"];]                                                                                                  |
|                                                                                                                                                                                                           |
| [dataGrid.GroupedColumns.Add(groupedCol2);]                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 168: Nested Group created in Grid

***[]*** 

See Also

***[]*** 

Creating Groups

 

 

[]{#related-topics}

