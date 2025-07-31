---
title: restrictautoresizingofrowheaderarea.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\restrictautoresizingofrowheaderarea.md
created_at: 2025-07-03
---








  









## Restrict Auto-Resizing of Row Header Area {#restrict-auto-resizing-of-row-header-area style="tab-stops: 0pt"}

PivotGrid provides support for restricting the row header items from being stretched when there are too many items in the computation area. When the computation button (**Show List** button) located at the DataHeaderArea of the grouping bar is clicked, the **Computation List** window appears with the computation fields.

Use Case Scenarios

This feature will restrict the row header items getting stretched and maintains its size with the fixed one, so that the user can view most of the data in the viewable area instead of scrolling to view the data.

Properties

Table 8: Property Table


  ------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ -----------
  Property                       Description                                                                                                                                                                                                            Type         Data Type
  AllowRowHeaderAreaAutoSizing   Shows the Computation Button (Show Field List Button) whose click event opens the Computation List Window with calculation fields of PivotGrid and restricts the stretching of row header items in the Grouping Bar.   Dependency   Boolean
  ------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ -----------


[] 

More:







