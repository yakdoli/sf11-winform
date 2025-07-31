---
title: getclienteventresourcedatainternal.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\getclienteventresourcedatainternal.md
created_at: 2025-07-03
---






#### []{#_GetClientEventResourceDataInternal}GetClientEventResourceDataInternal

This method is used to return the ResourceID and Resource name of the corresponding Appointment. It takes the Appointment object as argument and returns resource property object.

It implicitly invokes the GetResourceData method for accessing the resource properties for the specific appointment.

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
| [             [var] oStartDate = [new] Date([\"Jan 3, 2011 07:00:00\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] oEndDate = [new] Date([\"Jan 31, 2011 10:00:00\"]);]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [             [var] oAppointments = oScheduleobj.GetAppointments(1, oStartDate, oEndDate);]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [             [for] ([var] i = 0; i \< oAppointments.length; i++)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [                 [var] oRes =      oScheduleobj.GetClientEventResourceDataInternal(oAppointments\[i\].AppointmentEl);]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [         } ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [     [\</][script][\>]]                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

