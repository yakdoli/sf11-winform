---
title: sortinginicollectionviewadv.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sortinginicollectionviewadv.md
created_at: 2025-07-03
---






##### Sorting in ICollectionViewAdv {#sorting-in-icollectionviewadv style="tab-stops: 0pt"}

[] 

Adding SortDescriptions to the ICollectionView would sort the internal data.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [var][ orders = northwind.Orders;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [var][ queryableCollectionView = [new] [QueryableCollectionView](orders);]                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [queryableCollectionView.SortDescriptions.Add([new] System.ComponentModel.[SortDescription]([\"CustomerID\"], System.ComponentModel.[ListSortDirection].Descending));] |
|                                                                                                                                                                                                                                                                                                         |
| [foreach][ ([var] record [in] queryableCollectionView.Records)]                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [    var][ order = ([Orders])record.Data;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [    [Console].WriteLine([\"OrderID - {0} / CustomerID - {1}\"], order.OrderID, order.CustomerID);]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Sorting with Grouping

**[]** 

The TopLevelGroup works in conjunction with the sort descriptions present in the ICollectionView. It would automatically sort the groups and its bottom level group (records).

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [var][ orders = northwind.Orders;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [var][ queryableCollectionView = [new] [QueryableCollectionView](orders);]                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [queryableCollectionView.SortDescriptions.Add([new] System.ComponentModel.[SortDescription]([\"CustomerID\"], System.ComponentModel.[ListSortDirection].Descending));] |
|                                                                                                                                                                                                                                                                                                         |
| [queryableCollectionView.GroupDescriptions.Add([new] [PropertyGroupDescription]([\"ShipCountry\"]));]                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [queryableCollectionView.GroupDescriptions.Add([new] [PropertyGroupDescription]([\"ShipCity\"]));]                                                                                             |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [foreach][ ([var] nodeEntry [in] queryableCollectionView.TopLevelGroup)]                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [    Console][.WriteLine(nodeEntry);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [foreach][ ([var] record [in] queryableCollectionView.Records)]                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [    var][ order = ([Orders])record.Data;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| [    Console][.WriteLine([\"OrderID - {0} / CustomerID - {1}\"], order.OrderID, order.CustomerID);]                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: When applying sorting with grouping, both the ICollectionViewAdv.TopLevelGroup and the ICollectionViewAdv.Records will be in sync.


 

[]{#p228} 

[]{#related-topics}

