---
title: enabletheondemandcal.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\enabletheondemandcal.md
created_at: 2025-07-03
---








  





## Enable the On-Demand Calculation in PivotGrid control {#enable-the-on-demand-calculation-in-pivotgrid-control style="TEXT-ALIGN: justify; LINE-HEIGHT: 115%; tab-stops: 0pt"}

The following code snippet illustrates how to enable the On-Demand calculation and to disable the auto-sizing option in the PivotGrid control for a better performance:

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| [pivotGridControl1.AutoSizeOption = [GridAutoSizeOption].None;]   |
|                                                                                                                               |
| [pivotGridControl1.PivotEngine.EnableOnDemandCalculations = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                     |
|                                                                                                                                                                      |
| [pivotGridControl1.AutoSizeOption = [GridAutoSizeOption].None]**[]** |
|                                                                                                                                                                      |
| [pivotGridControl1.PivotEngine.EnableOnDemandCalculations = [True]]                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

