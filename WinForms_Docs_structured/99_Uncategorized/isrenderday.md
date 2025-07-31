---
title: isrenderday.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\isrenderday.md
created_at: 2025-07-03
---






#### []{#_IsRenderDay}IsRenderDay

This method is used to check whether the user passed Date is rendered in the schedule or not. It takes the day as argument and returns a Boolean value.

It returns true if the user specified day is rendered in the schedule, otherwise false.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**[]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [    \<][script][ [type][=\"text/javascript\"] [language][=\"javascript\"\>]] |
|                                                                                                                                                                                                                                                                                                          |
| [        [function] pageLoad()]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [         {]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [             var][ oScheduleobj = Scheduler;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] day = [new] Date([\"1/4/2011\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] brender=oScheduleobj.IsRenderDay(day);      ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [        } ]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

