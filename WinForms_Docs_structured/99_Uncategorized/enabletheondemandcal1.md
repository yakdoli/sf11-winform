---
title: enabletheondemandcal1.md
original_path: WinForms_Docs/99_Uncategorized/enabletheondemandcal1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  





## Enable the On-Demand Calculation in PivotGrid Control {#enable-the-on-demand-calculation-in-pivotgrid-control style="TEXT-ALIGN: justify; LINE-HEIGHT: 115%; tab-stops: 0pt"}

The following code snippet illustrates how to enable the On-Demand calculation and to disable the auto-sizing option in the PivotGrid control for a better performance:

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| [pivotGridControl1.AutoSizeOption = [GridAutoSizeOption].None;]   |
|                                                                                                                               |
| [pivotGridControl1.PivotEngine.EnableOnDemandCalculations = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                      |
|                                                                                                                                                                       |
| [pivotGridControl1.AutoSizeOption = [GridAutoSizeOption].None] **[]** |
|                                                                                                                                                                       |
| [pivotGridControl1.PivotEngine.EnableOnDemandCalculations = [True]]                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

