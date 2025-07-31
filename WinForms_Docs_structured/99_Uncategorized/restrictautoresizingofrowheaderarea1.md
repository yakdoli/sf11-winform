---
title: restrictautoresizingofrowheaderarea1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\restrictautoresizingofrowheaderarea1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Restrict Auto-resizing of Row Header Area {#restrict-auto-resizing-of-row-header-area style="tab-stops: 0pt"}

The PivotGrid control provides support for restricting the row header items from being stretched when there are too many items in the computation area. When the **Computation** button (**Show List** button) located in the DataHeaderArea of the grouping bar is clicked, the **Computation List** window appears with the computation fields.

Use Case Scenarios

This feature will restrict the row header items from being stretched and maintains its size with the fixed one so that users can view most of the data in the viewable area instead of scrolling to view the data.

Properties

Table 4: Property Table


  ------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ -----------
  Property                       Description                                                                                                                                                                                                                   Type         Data Type
  AllowRowHeaderAreaAutoSizing   Shows the ComputationButton (Show Field List Button) whose click event opens the Computation List Window with the calculation fields of the PivotGrid and restricts the stretching of row header items in the grouping bar.   Dependency   Boolean
  ------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ -----------


[] 

More:







