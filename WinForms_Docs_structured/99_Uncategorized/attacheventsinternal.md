---
title: attacheventsinternal.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\attacheventsinternal.md
created_at: 2025-07-03
---






#### []{#_AttachEventsInternal}AttachEventsInternal

This method is used to attach the DOM events to the schedule. It takes the Boolean value as an argument.

If we pass the Boolean value as true then it will attach the DOM events to the schedule.  Otherwise, it detaches the events from the schedule.

The Boolean value is true in the InitBase method and false in the DisposeScheduleBase method.

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
| [             oScheduleobj.AttachEventsInternal([false]);        ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [         } ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In the above mentioned code, we have passed the  boolean value as false to the AttachEventstInternal method. Therefore, it will detach the DOM events from the schedule.

[]{#related-topics}

