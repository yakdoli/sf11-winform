---
title: filteroptimization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\filteroptimization.md
created_at: 2025-07-03
---






##### Filter Optimization {#filter-optimization style="tab-stops: 0pt"}

 

The filter can be optimized for the performance over large data in **GridGroupingControl**.

Set **OptimizeFilterPerformance** to **true** to optimize the filter.

This boolean property enables the grid to optimize the filtering of data by delegating the summary to filter the grid accordingly.

The **OptimizeFilterPerformance** property can be assigned directly from the **GridGroupingControl** and can apply to any type of filter bar specified to the grid.

 

The following code illustrates how to optimize the filter.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [        [private] [void] Form1_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                  |
| [        {]                                                                                                                                                  |
|                                                                                                                                                                                                  |
| [            [this].gridGroupingControl1.OptimizeFilterPerformance = [true];]                                      |
|                                                                                                                                                                                                  |
| [        }]                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [       [Private] [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                    |
| [            [Me].gridGroupingControl1.OptimizeFilterPerformance = [True]]                                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [        [End] [Sub]]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

*[Figure ][415][: Optimize Filter ]*

 

[]{#p484} 

 

[]{#related-topics}

