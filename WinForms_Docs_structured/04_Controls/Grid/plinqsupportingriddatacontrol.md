---
title: plinqsupportingriddatacontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\plinqsupportingriddatacontrol.md
created_at: 2025-07-03
---






#### PLINQ Support in GridDataControl {#plinq-support-in-griddatacontrol style="tab-stops: 0pt"}

[[PLINQ]{.UGHyperlink}](http://msdn.microsoft.com/en-us/library/dd997425.aspx) is the parallel implementation of the standard LINQ. GridDataControl uses a QueryableCollectionView that works on top of LINQ expressions for performing major operations such as Sorting, Filtering, Grouping and Summaries calculation. Since PLINQ works on top of LINQ expression trees, QueryableCollectionView now has a property UsePLINQ = true / false (this class implements *IParallelizableView* interface) that would add a AsParallel() to change it into a Parallel Query. Sorting, Grouping and Summary operations would be automatically done in parallel when this property is set.

 

{border="0"}

 

 

+----------------------------------------------------------------------------------------+
| [  \[XAML\]]                                       |
|                                                                                        |
| [\<syncfusion:GridDataControl]                     |
|                                                                                        |
| [                x:Name=\"grid\"  ]                |
|                                                                                        |
| [                AutoPopulateColumns=\"True\"    ] |
|                                                                                        |
| [                AutoPopulateRelations=\"False\"]  |
|                                                                                        |
| [                UsePLINQ=\"True\"]                |
|                                                                                        |
| [      VisualStyle=\"Office14Silver\"\>]           |
|                                                                                        |
| [    \</syncfusion:GridDataControl\>]              |
|                                                                                        |
| []                                                 |
|                                                                                        |
| []                                                 |
+----------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| *\[C#\]*                                                              |
|                                                                       |
|                                                                       |
|                                                                       |
| this.gridDataControl1.UsePLINQ = true;                                |
+-----------------------------------------------------------------------+

**** 


Note: This only works for strongly-typed collections and not for legacy object models like DataTable.


 

 

[]{#related-topics}

