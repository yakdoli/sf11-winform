---
title: disposeschedulebase.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\disposeschedulebase.md
created_at: 2025-07-03
---






#### []{#_DisposeScheduleBase}DisposeScheduleBase

This method is invoked only when the user closes the browser window of the schedule or refreshes the schedule control.

It will detach the entire DOM events attached in the schedule. It means that the Boolean value passed to the AttachEventsInternal method is false.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[JavaScript\]]**[]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [    \<][script][ [type][=\"text/javascript\"] [language][=\"javascript\"\>]] |
|                                                                                                                                                                                                                                                                                                          |
| [        [function] pageLoad()]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [         {]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [             var][ oScheduleobj = Scheduler;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [             oScheduleobj.DisposeScheduleBase();]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [         } ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

