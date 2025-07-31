---
title: sortbydisplaymember.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sortbydisplaymember.md
created_at: 2025-07-03
---






#### Sort by DisplayMember {#sort-by-displaymember style="tab-stops: 0pt"}

[] 

By default, sorting is done in a Grid Data Bound Grid through the **IBindingList**.

[] 


{border="0"}Note: IBindingList interface provides the features required to support both complex and simple scenarios when binding to a data source.


[] 

**Sort** method relies on the data source for the grid and by default, sorting is done based on the value members present in the data source and not based on the display member. We can implement Sort By DisplayMember feature in Grid Data Bound Grid. The code for foreign key column can be added to the View of the data table so that the sort behavior can be redirected to use the foreign key column linked to the combo box column, when the user sorts the combo box column.

[] 

Example:

[] 

The following code example implements a solution for sorting a column by its display member instead of its value member. Here the foreign key column is added to the View of the data to redirect the sort behavior to use the foreign key column.

 

To accomplish this, two handlers-the **CellClick** event and the **QueryCellInfo** event have been used. In the CellClick event, the display member is set to the existing mapping name in the sortName (which will be the value member) so that the sorting is done by display member.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [string][ sortName = column.MappingName;]                                                           |
|                                                                                                                                                                                          |
| [if][ (column.MappingName == [\"SupplierID\"])]                             |
|                                                                                                                                                                                          |
| [    sortName = [\"CompanyName\"];]                                                                                          |
|                                                                                                                                                                                          |
| [else][ [if] (column.MappingName == [\"CategoryID\"])] |
|                                                                                                                                                                                          |
| [    sortName = [\"CategoryName\"];]                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [Dim][ sortName [As] [String] = column.MappingName]        |
|                                                                                                                                                                                           |
| [If][ column.MappingName = [\"SupplierID\"] [Then]]     |
|                                                                                                                                                                                           |
| [sortName = [\"CompanyName\"]]                                                                                                |
|                                                                                                                                                                                           |
| [ElseIf][ column.MappingName = [\"CategoryID\"] [Then]] |
|                                                                                                                                                                                           |
| [sortName = [\"CategoryName\"]]                                                                                               |
|                                                                                                                                                                                           |
| [End][ [If]]                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A DataView is created by using the **List** property under the **CurrencyManager** class.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [CurrencyManager][ cm = BindingContext\[grid.DataSource, grid.DataMember\] [as] [CurrencyManager];] |
|                                                                                                                                                                                                                                          |
| [DataView][ dv = cm.List [as] [DataView];]                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [Dim][ cm [As] CurrencyManager = [TryCast](BindingContext(Grid.DataSource, Grid.DataMember), CurrencyManager)] |
|                                                                                                                                                                                                                                               |
| [Dim][ dv [As] DataView = [TryCast](cm.List, DataView)]                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The DataView sort is applied to this with the sortName.

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                                   |
| []                                                              |
|                                                                                                                   |
| [if][ (dv.Sort == sortName)] |
|                                                                                                                   |
| [{]                                                                           |
|                                                                                                                   |
| [    dv.Sort = sortName + [\" DESC\"];]               |
|                                                                                                                   |
| [}]                                                                           |
|                                                                                                                   |
| [else]                                                           |
|                                                                                                                   |
| [    dv.Sort = sortName;]                                                     |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                         |
|                                                                                                                                            |
| []                                                                                       |
|                                                                                                                                            |
| [If][ dv.Sort = sortName [Then]] |
|                                                                                                                                            |
| [dv.Sort = sortName & [\" DESC\"]]                                             |
|                                                                                                                                            |
| [Else]                                                                                    |
|                                                                                                                                            |
| [dv.Sort = sortName]                                                                                   |
|                                                                                                                                            |
| [End][ [If]]                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: CurrencyManager manages a list of binding objects when the data source uses the IBindingList interface.


[] 

In the QueryCellInfo handler, the sorting icon is drawn with respect to sorting

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                |
|                                                                                                                                                                                     |
| [if][ (dv.Sort == sortName)]                                                                   |
|                                                                                                                                                                                     |
| [    e.Style.Tag = [ListSortDirection].Ascending;]                                                                      |
|                                                                                                                                                                                     |
| [else][ [if] (dv.Sort == sortName + [\" DESC\"])] |
|                                                                                                                                                                                     |
| [    e.Style.Tag = [ListSortDirection].Descending;]                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [If][ dv.Sort = sortName [Then]]                                           |
|                                                                                                                                                                                                                      |
| [e.Style.Tag = ListSortDirection.Ascending]                                                                                                                      |
|                                                                                                                                                                                                                      |
| [ElseIf][ dv.Sort = sortName & [\" DESC\"] [Then]] |
|                                                                                                                                                                                                                      |
| [e.Style.Tag = ListSortDirection.Descending]                                                                                                                     |
|                                                                                                                                                                                                                      |
| [End][ [If]]                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][214][: Sort by Display Member]*

[] 

A sample demonstrating this feature is available under the following sample installation path.

 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Data Bound\\Sort By DisplayMember Demo***

 

[]{#p377} 

 

[]{#related-topics}

