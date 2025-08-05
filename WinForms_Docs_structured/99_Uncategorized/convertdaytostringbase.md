---
title: convertdaytostringbase.md
original_path: WinForms_Docs/99_Uncategorized/convertdaytostringbase.md
created_at: 2025-08-05
---






#### []{#_ConvertDayToStringBase}ConvertDayToStringBase

This method is used to convert the Day object to String. It takes the Date object as argument and returns the String. Day object does not have hours, minutes, and seconds property. Therefore, the Date argument contains only the specific Day.

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
| [             [var] dtDate = [new] Date([\"1/5/2011\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] sDay = oScheduleobj.ConvertDayToStringBase(dtDate);         ]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [         } ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

