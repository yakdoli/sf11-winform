---
title: delete2.md
original_path: WinForms_Docs/99_Uncategorized/delete2.md
created_at: 2025-08-05
---






#### []{#_Delete}Delete

This method is invoked when the user clicks the Delete ViewStrip on the schedule. It takes Delete ViewStrip object as argument and returns the Boolean value.

It internally invokes the GetAppointmentDataInternal method for getting the selected Appointment data from the schedule. Using the Appointment data, it enables the delete operation.

It always return false.

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
| [             oScheduleobj.Delete(oScheduleobj);        ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [        } ]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

