---
title: icollectionviewadv.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\icollectionviewadv.md
created_at: 2025-07-03
---






#### ICollectionViewAdv {#icollectionviewadv style="tab-stops: 0pt"}

[] 

The ICollectionViewAdv interface is an extended ICollectionView interface that includes support for the following:

[] 

[·      ]Grouping structure -- Binary tree data structure to maintain the groups.

[·      ]Group summaries -- Collection to specify group summaries.

[·      ]Caption summary -- Specifies caption summary row.

[·      ]Records structure -- Flat data structure to maintain the list of internal records.

[·      ]Table summaries -- Collection to specify table summaries.

[·      ]Filter definitions -- Collection to specify filter descriptors.

[] 

ICollectionViewAdv interface implements the following:

[] 

{border="0"}

[] 

Figure 91: ICollectionViewAdv Interface

[] 

ICollectionViewAdv is implemented as two parts in Syncfusion.Linq.Base library, as shown below:

[] 

{border="0"}

 

Figure 92: CollectionViewAdv

[] 

The CollectionViewAdv is an abstract class implementing ICollectionViewAdv. By sub-classing the CollectionViewAdv, the specific actions for the following can be defined:

[] 

[·      ]Sorting

[·      ]Filtering

[·      ]Grouping

[·      ]Summaries

[] 

**QueryableCollectionView** - Implements an IQueryable way to provide Sorting, Filtering, Grouping and Summaries.

**DataTableCollectionView** -- Uses the DataView to provide Sorting/Filtering and uses custom logics to implement grouping and calculating summaries.

[]{#p225} 

 

More:









