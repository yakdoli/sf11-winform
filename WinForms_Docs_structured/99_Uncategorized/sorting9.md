---
title: sorting9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sorting9.md
created_at: 2025-07-03
---






#### Sorting {#sorting style="tab-stops: 0pt"}

You can enable sorting in the GridTree control by using GridTreeControl.AllowSort property. When this property is set to true, you can perform sorting on a column by clicking on the column header of the respective column. In addition, Grid Tree provides support to perform MultiColumn Sorting by holding down CTRL key and clicking the left mouse button.

 

The GridTreeControl.InternalGrid.SortTree method is used to sort a column in the Grid Tree programmatically. There are two overloads:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [public][ [void] SortTree([string] colName, [ListSortDirection] dir)]                                        |
|                                                                                                                                                                                                                                                                     |
| [public][ [void] SortTree([string] colName, [ListSortDirection] dir, [bool] clearSort)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The first signature sorts the given column in the given direction clearing any existing sorting. The second signature gives you the option of not clearing the existing sorts, which enables multi-column sorting.

 

Here are additional members of GridTreeControlImpl that allows you to access sort information and provide support for customized sorting.

 

[public] [bool] IsPropertySorted([string] propertyName, [out] [SortState] state)--determines whether a particular column has been sorted.

[public] [IComparer]\<[GridTreeNode]\> SortComparer--Allows customized sorting. The default implementation assumes the underlying node items implement IComparable and uses that implementation for the sorting comparisons within the columns. If your objects are not IComparable, then you need to provide a SortComparer that properly sorts the GridNodes depending upon the SortProperty value of GridNode.Item.

[public] [string] SortProperty-string that holds the column name to be sorted. You can specify a SortDirection by appending a space followed by either ASC or DESC. In addition, you can specify multicolumn sorts by passing several columns separated by commas. For example, \"Price ASC, Weight DESC\", which will indicate to first sort in ascending order by the Price column, and then sort in descending order by the Weight column.

[public] [List]\<[SortState]\> SortStates-is the list of the SortStates for the columns currently sorted in the GridTree control. The SortState class contains information regarding the direction and the property sorted, and it exposes static helper methods, which takes care of the changes between SortStates and the SortProperty.

 

 

 

[]{#related-topics}

