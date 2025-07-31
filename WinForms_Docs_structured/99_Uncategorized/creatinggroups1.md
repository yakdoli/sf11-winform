---
title: creatinggroups1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatinggroups1.md
created_at: 2025-07-03
---






##### Creating Groups {#creating-groups style="tab-stops: 0pt"}

[]{#p272}Grid groups can be created at design-time as well as run time. They are managed by the GroupedColumns collection which holds one entry for every grouped column. A group can be created programmatically by adding the desired column into this collection. The records are sorted in the ascending (default) or descending order of their Grouped Column values. The GroupedColumns collection can have more than one entry to form Nested Groups.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][GridDataControl][ x][:][Name][=\"dataGrid\"][ ShowAddNewRow][=\"False\"][ ShowFilters][=\"False\"][ AutoPopulateColumns][=\"True\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AutoPopulateRelations][=\"True\"][ ItemsSource][=\"{][StaticResource][ ordersSource][}\"][ ShowGroupDropArea][=\"True\"\>]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][GridDataControl.GroupedColumns][ \>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][GridDataGroupColumn][ ColumnName][=\"ShipCountry\"\>\</][syncfusion][:][GridDataGroupColumn][\>]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][GridDataControl.GroupedColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][GridDataControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                               |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [GridDataGroupColumn][ groupedCol = [new] [GridDataGroupColumn]();] |
|                                                                                                                                                                                                          |
| [groupedCol.ColumnName = [\"ShipCountry\"];]                                                                                                 |
|                                                                                                                                                                                                          |
| [dataGridControl.GroupedColumns.Add(groupedCol);]                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 166: Creating Groups by using GridData control

[] 

Run Time Grouping

 

Run time grouping is enabled by displaying the group drop area, a placeholder to store the current groups. Such groups can be created interactively through the drag-and-drop operation. For example, to group data against a particular column, drag the desired column header and drop it into the group drop area.

 

{border="0"}

Figure 167: Illustrates Run Time Grouping

[] 

 

See Also

 

Nested Groups and Custom Groups

 

 

[]{#related-topics}

