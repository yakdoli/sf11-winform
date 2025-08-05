---
title: selectappointmentbase.md
original_path: WinForms_Docs/99_Uncategorized/selectappointmentbase.md
created_at: 2025-08-05
---






#### []{#_SelectAppointmentBase}SelectAppointmentBase

This method is invoked when the user selects an Appointment. It takes the Appointment object as argument and returns nothing.

The SelectAppointmentBase method is used to capture the selected Appointment data and store it in a separate variable that will be used later in case of deleting the Appointment.

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
| [             [var] oStartDate = [new] Date([\"Jan 3, 2011 07:00:00\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] oEndDate = [new] Date([\"Jan 31, 2011 10:00:00\"]);]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] oAppointments = oScheduleobj.GetAppointments(1, oStartDate, oEndDate);]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [             [for] ([var] i = 0; i \< oAppointments.length; i++)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [              oScheduleobj.SelectAppointmentBase(oAppointments\[i\].AppointmentEl);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [       } ]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

