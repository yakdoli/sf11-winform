---
title: cancelingtheprogressbar1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cancelingtheprogressbar1.md
created_at: 2025-07-03
---






#### Canceling the progress bar {#canceling-the-progress-bar style="tab-stops: 0pt"}

There are two methods to cancel a progress bar:

1.   Calling the **CancelProgressBar** method in **HierarchyNavigator**.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                                                          |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [HierarchyNavigator][ hierarchyNavigator = [new] [HierarchyNavigator]();] |
|                                                                                                                                                                                                                                          |
| [hierarchyNavigator.CancelProgressBar();]                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Passing an argument in the method to cancel the progress bar for a specified time span. The image below specifies a time span of 1000 ms.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                                                          |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [HierarchyNavigator][ hierarchyNavigator = [new] [HierarchyNavigator]();] |
|                                                                                                                                                                                                                                          |
| [hierarchyNavigator.OnCancelProgressBar([new] [TimeSpan](0, 0, 0, 0, 1000));]                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#related-topics}

