---
title: timeinterval.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\timeinterval.md
created_at: 2025-07-03
---








  









### Time Interval {#time-interval style="LINE-HEIGHT: 150%; tab-stops: 0pt"}

You can use the **TimeInterval** property to set the time interval for each time slot in the Schedule Control. Schedule control supports various time intervals ranging from five minutes to one hour. The following options are provided:

[·      ]FiveMin

[·      ]SixMin

[·      ]TenMin

[·      ]FifteenMin

[·      ]TwentyMin

[·      ]ThirtyMin

[·      ]OneHour

The user is free to choose the time interval and the view is updated automatically based on the interval. The Scroll bars are available to scroll up to the final hour of the day and the mouse wheel support is added for the scroll bars to move up and down the view easily.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][Schedule:Schedule][ ][x:Name][=][\"][schedule][\" ][TimeInterval][=\"FifteenMin\"/\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 38: TimeInteval is set to FifteenMin[]

[]{#related-topics}

