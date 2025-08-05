---
title: getappointmentdatainternal.md
original_path: WinForms_Docs/03_Data_Binding/getappointmentdatainternal.md
created_at: 2025-08-05
---






#### []{#_GetAppointmentsDataInternal_1}GetAppointmentDataInternal

This method is used to get all the internal properties of an appointment. It has no arguments. It will return the properties collection as an object such as AllDay, StartMinutes, AllowDrag, StartHour, EndHour, TotalMinutes etc.

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
| [             oAppointments = oScheduleobj.GetAppointmentsDataInternal();]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [             [for] ([var] i = 0; i \< oAppointments.length; i++)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [             alert(oAppointments\[i\].AllDay);      ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [         } ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_Day} 

[]{#related-topics}

