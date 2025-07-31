---
title: getcalendarobjectidbase.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\getcalendarobjectidbase.md
created_at: 2025-07-03
---






#### []{#_GetCalendarObjectIDBase}GetCalendarObjectIDBase

This method is used to return the Calendar object only when the Calendar property is set for the schedule control. It takes no argument.

If the Calendar is not set for the schedule control, it will return Null. Otherwise, it returns the object of the Calendar.

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
| [             [var] oCalender= oScheduleobj.GetCalendarObjectIDBase();         ]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [         } ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

