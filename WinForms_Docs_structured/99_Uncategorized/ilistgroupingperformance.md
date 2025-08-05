---
title: ilistgroupingperformance.md
original_path: WinForms_Docs/99_Uncategorized/ilistgroupingperformance.md
created_at: 2025-08-05
---






##### IList Grouping Performance {#ilist-grouping-performance style="tab-stops: 0pt"}

[] 

The **IList** binded to the **GridGroupingControl** has been implemented with an optimization process for grouping columns to improve the performance.

 

Grouping a column which has Ilist binded reduces the time taken to refresh the control after grouping. The grouping performance has been improved with huge data loaded

 

Set **OptimizeIListGroupingPerformance** to **true** to enable grouping optimization over the **Ilist** data source.

 

The following code illustrates how to enable grouping optimization.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [        ][private][ [void] Form1_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| [            gridGroupingControl1.OptimizedListGrouping = [true];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [       [Private] [Sub] Form1_Load([ByVal] sender [As] System.Object, [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                             |
| [            GridGroupingControl1.OptimizedListGrouping = [true]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [       [End] [Sub]]                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Enable Real Time Updates

[] 

The OptimizeIListGroupingPerformance method has to be called to enable real time updates with the data source from the GridGroupingControl

 

The following code illustrates how to enable real time updates.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                               |
| [        void][ gridGroupingEmployee_SourceListListChanged([object] sender, [TableListChangedEventArgs] e)] |
|                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
| [            [this].gridGroupingEmployee.OptimizeIListGroupingPeformance(sender, e);]                                                                                                |
|                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [Private] [Sub] gridGroupingEmployee_SourceListListChanged([ByVal] sender [As] [Object], [ByVal] e [As] TableListChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [            [Me].gridGroupingEmployee.OptimizeIListGroupingPeformance(sender, e)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [End] [Sub]]                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

*[Figure ][261][: First Name Is Dragged to Add to Group.]*

***[]*** 

{border="0"}

*[Figure ][262][: Time Taken to Group the Records]*

***[]*** 

[] 

[] 

[] 

 

[]{#p403} 

 

[]{#related-topics}

