---
title: sortingdatabycellvalues.md
original_path: WinForms_Docs/03_Data_Binding/sortingdatabycellvalues.md
created_at: 2025-08-05
---






#### Sorting Data by Cell Values {#sorting-data-by-cell-values style="tab-stops: 0pt"}

This is used to sort a range of cells dynamically, at runtime. This is explained in the following code snippets:

 

{border="0"}

Column "ID" is Sorted in Descending order.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **C#**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [//Creates the data sorter][]                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [IDataSort][ sorter = book.CreateDataSorter();]                                                                                             |
|                                                                                                                                                                                                                                                               |
| [//Range to sort][]                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [sorter.SortRange = range;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [//Adds the sort field with the column index, sort based on and order by attribute][]                                                         |
|                                                                                                                                                                                                                                                               |
| [ISortField][ sortField = sorter.SortFields.Add(0, [SortOn].Values, [OrderBy].Ascending);]  |
|                                                                                                                                                                                                                                                               |
| [//Adds another sort field][]                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [ISortField][ sortField2 = sorter.SortFields.Add(1, [SortOn].Values, [OrderBy].Ascending);] |
|                                                                                                                                                                                                                                                               |
| [//Sort based on the sort Field attribute][]                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [sorter.Sort();]                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **VB.Net**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
| [\'\'Creates the Data sorter][]                                                                       |
|                                                                                                                                                                                                                       |
| [Dim][ sorter [As] [IDataSort] = book.CreateDataSorter()] |
|                                                                                                                                                                                                                       |
| [\'\'Specifies the sort range][]                                                                      |
|                                                                                                                                                                                                                       |
| [sorter.SortRange = range]                                                                                                                                           |
|                                                                                                                                                                                                                       |
| [Dim][ field [As] [ISortField]]                           |
|                                                                                                                                                                                                                       |
| [\'\' Adds the sort field with column index, sort based on and order by attribute][]                  |
|                                                                                                                                                                                                                       |
| [field = sorter.SortFields.Add(2, [SortOn].Values, [OrderBy].OnTop)]                                                 |
|                                                                                                                                                                                                                       |
| [\'\' Adds the second sort field][]                                                                   |
|                                                                                                                                                                                                                       |
| [field = sorter.SortFields.Add(2,[SortOn].Values,[OrderBy].OnTop)]                                                   |
|                                                                                                                                                                                                                       |
| [\'\' Sorts the data with the sort field attribute][]                                                 |
|                                                                                                                                                                                                                       |
| [sorter.Sort()]                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

