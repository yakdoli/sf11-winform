---
title: howtochangethecurrentdisplaytoadesiredscheduleviewtype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethecurrentdisplaytoadesiredscheduleviewtype.md
created_at: 2025-07-03
---








  









## How to change the current display to a desired Schedule View Type {#how-to-change-the-current-display-to-a-desired-schedule-view-type style="tab-stops: 0pt"}

[] 

The current display of a ScheduleControl can be changed to a desired view type by invoking the **PerformSwitchToScheduleViewTypeClick** method and passing the desired view as parameter.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                  |
| \                                                                                                                                           |
| ]**[]                                   |
|                                                                                                                                             |
| [// Switches the display to Month View.]                                                  |
|                                                                                                                                             |
| [scheduleControl1.PerformSwitchToScheduleViewTypeClick([ScheduleViewType].Month);] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]\                                                                                                      |
| \                                                                                                                   |
| ]**[]           |
|                                                                                                                     |
| [\' Switches the display to Month View.]                          |
|                                                                                                                     |
| [scheduleControl1.PerformSwitchToScheduleViewTypeClick(ScheduleViewType.Month)] |
+---------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

