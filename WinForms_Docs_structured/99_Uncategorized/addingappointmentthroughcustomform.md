---
title: addingappointmentthroughcustomform.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingappointmentthroughcustomform.md
created_at: 2025-07-03
---








  









### Adding Appointment through Custom Form {#adding-appointment-through-custom-form style="tab-stops: 0pt"}

[] 

The **Add Appointment Window** dialog box can be customized with the required form for adding an appointment to the Schedule control. The Syncfusion Window control or any aspx page can be used to add an appointment. The **CustomizeAddNewAppointment** property adds an appointment to the Schedule control by using a customized form, and also raises a server-side event "AppointmentAdding", when set to *true*.

 

The following code snippet illustrates the customization of appointment forms:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][ScheduleMenu][ [CustomizeAddNewAppointment][=\"true\"] [ShowAddNewAppointmentMenuItem][=\"true\"] [ShowEditAppointmentMenuItem][=\"false\"\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [this][.Schedule1.ScheduleMenu.CustomizeAddNewAppointment = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                      |
| [Me][.Schedule1.ScheduleMenu.CustomizeAddNewAppointment = True] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following is the resultant output:

[] 

{border="0"}[]

***[]*** 

Figure 68: Custom Form to add an Appointment to the Edit Control

 

[]{#related-topics}

