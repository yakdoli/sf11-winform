---
title: showingtheprogressbar1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\showingtheprogressbar1.md
created_at: 2025-07-03
---






#### Showing the progress bar {#showing-the-progress-bar style="tab-stops: 0pt"}

There are two methods to show the progress bar:

1.   Calling the **ShowProgressBar** method in **HierarchyNavigator**, which shows the progress bar with a time span of 500 ms.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                                                          |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [HierarchyNavigator][ hierarchyNavigator = [new] [HierarchyNavigator]();] |
|                                                                                                                                                                                                                                          |
| [hierarchyNavigator.ShowProgressBar();]                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Passing an argument in the method with a specified time span. The image below specifies a time span of 1000 ms.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                                                          |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [HierarchyNavigator][ hierarchyNavigator = [new] [HierarchyNavigator]();] |
|                                                                                                                                                                                                                                          |
| [hierarchyNavigator.ShowProgressBar([new] [TimeSpan](0, 0, 0, 0, 1000));]                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#related-topics}

