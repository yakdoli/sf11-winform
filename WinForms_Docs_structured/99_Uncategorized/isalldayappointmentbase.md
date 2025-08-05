---
title: isalldayappointmentbase.md
original_path: WinForms_Docs/99_Uncategorized/isalldayappointmentbase.md
created_at: 2025-08-05
---






#### []{#_IsAllDayAppointmentBase}IsAllDayAppointmentBase

This is an explicit method to check whether the Appointment type is AllDayAppointment or not. It will be triggered implicitly by the IsAppointmentBase method.

It takes Appointment object as argument and returns a Boolean value.

It returns true for AllDayAppointment and false for other appointments.

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
| [             [var] bApp = oScheduleobj.IsAllDayAppointmentBase(oAppointments\[i\].AppointmentEl);                           } ]                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

