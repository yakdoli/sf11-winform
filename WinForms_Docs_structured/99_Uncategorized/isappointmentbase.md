---
title: isappointmentbase.md
original_path: WinForms_Docs/99_Uncategorized/isappointmentbase.md
created_at: 2025-08-05
---






#### []{#_IsAppointmentBase}IsAppointmentBase

This method is used to check whether the appointment is a normal Appointment or AllDayAppointment. It implicitly invokes the AllDayAppointement method to check whether the appointment is AllDay or not.

It takes the Appointment object as argument and returns a Boolean value.

Before calling this method, we have to invoke either GetAppointments or GetAllDayAppointment method. Based on the method invoked, it will return either true or false.

If the GetAppointment fucntion is used, it will return true for normal Appointment and false for AllDayAppointment.

If GetAllDayAppointment fucntion is used, it will return true for AllDayAppointment and false for normal appointment.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**[]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [    \<][script][ [type][=\"text/javascript\"] [language][=\"javascript\"\>]] |
|                                                                                                                                                                                                                                                                                                          |
| [        [function] pageLoad()]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [         {]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [        ][ [var] oScheduleobj = Scheduler;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [        [var] oStartDate = [new] Date([\"Jan 3, 2011 07:00:00\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [        [var] oEndDate = [new] Date([\"Jan 31, 2011 10:00:00\"]);]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [       [var] oAppointments = oScheduleobj.GetAppointments(1, oStartDate, oEndDate);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [       [for] ([var] i = 0; i \< oAppointments.length; i++)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [       [var] bApp = oScheduleobj.IsAppointmentBase(oAppointments\[i\].AppointmentEl);         ]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [        } ]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

