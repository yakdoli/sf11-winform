---
title: improvetheperformanc.md
original_path: WinForms_Docs/99_Uncategorized/improvetheperformanc.md
created_at: 2025-08-05
---








  





## Improve the Performance of Loading & Scrolling in PivotGrid {#improve-the-performance-of-loading-scrolling-in-pivotgrid style="TEXT-ALIGN: justify; tab-stops: 0pt"}

The performance of the PivotGrid control can be improved by enabling the On-Demand calculations on the value cells and disabling the auto-sizing option. This refreshes the calculation only while loading or scrolling the PivotGrid control.[]

Properties

Table 12: Property Table

  ---------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ --------- ----------- -----------------
  Property                     Description                                                                                                                                            Type      Data Type   Reference links
  EnableOnDemandCalculations   Gets of sets whether the calculations are postponed until the value is requested through the Indexer on the PivotEngine. The default value is false.   **CLR**   Boolean     \-
  ---------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ --------- ----------- -----------------

[] 

[] 

[]{#related-topics}

