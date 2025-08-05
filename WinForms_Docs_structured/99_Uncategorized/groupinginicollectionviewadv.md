---
title: groupinginicollectionviewadv.md
original_path: WinForms_Docs/99_Uncategorized/groupinginicollectionviewadv.md
created_at: 2025-08-05
---






##### Grouping in ICollectionViewAdv {#grouping-in-icollectionviewadv style="tab-stops: 0pt"}

[] 

To specify groups, add GroupDescriptions to ICollectionViewAdv.GroupDescriptions. The sample below is a code snippet that shows adding groups to Northwind database.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [var][ northwind = [new] [Northwind]([\"Data Source = Northwind.sdf\"]);] |
|                                                                                                                                                                                                                                     |
| [var][ orders = northwind.Orders;]                                                                                                             |
|                                                                                                                                                                                                                                     |
| [var][ queryableCollectionView = [new] [QueryableCollectionView](orders);]                        |
|                                                                                                                                                                                                                                     |
| [queryableCollectionView.GroupDescriptions.Add([new] [PropertyGroupDescription]([\"ShipCountry\"]));]                      |
|                                                                                                                                                                                                                                     |
| [queryableCollectionView.GroupDescriptions.Add([new] [PropertyGroupDescription]([\"ShipCity\"]));]                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[            ]

The grouping values are stored in a binary tree structure in the ICollectionViewAdv.TopLevelGroup. The visual graph of the TopLevelGroup is as follows:

[] 

{border="0"}

 

Figure 93: TopLevelGroup - Visual Graph

***[]*** 

The class diagram for the structure above is as follows:

[] 

{border="0"}

Figure 94: Class Diagram

[] 

[·      ]**NodeEntry** -- It is the base class for all the nodes in the binary tree.

[·      ]**GroupEntry** -- Contains a list of groups.

[·      ]**GroupRecordEntry** -- Contains a list of records.

[·      ]**Group** -- Extended Group entry that has implementation for populating and structuring the groups and its sub- groups. It can store both a list of Groups or Records. If the Group is a BottomLevelGroup then the Group.Details would contain the GroupRecordEntry.

[] 

Iterating through the whole structure

**[]** 

The TopLevelGroup is an extended Group class. Iteration through the whole structure can be performed by looping through the structure using a foreach loop, since the Group already has an Enumerator implemented.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [var][ northwind = [new] [Northwind]([\"Data Source = Northwind.sdf\"]);] |
|                                                                                                                                                                                                                                     |
| [var][ orders = northwind.Orders;]                                                                                                             |
|                                                                                                                                                                                                                                     |
| [var][ queryableCollectionView = [new] [QueryableCollectionView](orders);]                        |
|                                                                                                                                                                                                                                     |
| [queryableCollectionView.GroupDescriptions.Add([new] [PropertyGroupDescription]([\"ShipCountry\"]));]                      |
|                                                                                                                                                                                                                                     |
| [foreach][ ([var] nodeEntry [in] queryableCollectionView.TopLevelGroup)]                             |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [    [Console].WriteLine(nodeEntry);]                                                                                                                                   |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p226} 

 

[]{#related-topics}

