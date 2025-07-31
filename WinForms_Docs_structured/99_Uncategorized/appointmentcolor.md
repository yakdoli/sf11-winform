---
title: appointmentcolor.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\appointmentcolor.md
created_at: 2025-07-03
---








  









### Appointment Color {#appointment-color style="tab-stops: 0pt"}

[] 

The color of an appointment can be changed by using the options provided by the **ScheduleWebAppointment Collection Editor**, invoked through the **Appointments** collection property.

[] 


  ---------------------- ----------------------------------------------------------------------------------
  Appointment Property   Description
  BackColor              Specifies the back color for the appointment.
  TimeSpanColor          Specifies the color to be applied to the handler to the left of the appointment.
  ---------------------- ----------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Appointments][\>]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Syncfusion][:][ScheduleWebAppointment][ [UniqueID][=\"1\"] [BackColor][=\"MistyRose\"] [TimeSpanColor][=\"Orchid\"\>]]         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Syncfusion][:][ScheduleWebAppointment][\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Syncfusion][:][ScheduleWebAppointment][ [UniqueID][=\"2\"] [BackColor][=\"AliceBlue\"] [TimeSpanColor][=\"CornflowerBlue\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Syncfusion][:][ScheduleWebAppointment][\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Appointments][\>]                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                        |
| []                                                                                 |
|                                                                                                                        |
| [// Appointment app1 = Scheduler1.Appointments\[0\];]                |
|                                                                                                                        |
| [app1.BackColor = System.Drawing.[Color].MistyRose;]          |
|                                                                                                                        |
| [app1.TimeSpanColor = System.Drawing.[Color].Orchid;]         |
|                                                                                                                        |
| []                                                                                 |
|                                                                                                                        |
| [app2.BackColor = System.Drawing.[Color].AliceBlue;]          |
|                                                                                                                        |
| [app2.TimeSpanColor = System.Drawing.[Color].CornflowerBlue;] |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                          |
|                                                                                                                                                           |
| []                                                                                                                    |
|                                                                                                                                                           |
| [\' Appointment app1 = Scheduler1.Appointments\[0\];]                                                   |
|                                                                                                                                                           |
| [Private][ app1.BackColor = System.Drawing.Color.MistyRoseColor]     |
|                                                                                                                                                           |
| [Private][ app1.TimeSpanColor = System.Drawing.Color.Orchid]         |
|                                                                                                                                                           |
| []                                                                                                                    |
|                                                                                                                                                           |
| [Private ][app2.BackColor = System.Drawing.Color.AliceBlue]          |
|                                                                                                                                                           |
| [Private ][app2.TimeSpanColor = System.Drawing.Color.CornflowerBlue] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

Figure 59

[]{#p42} 

[]{#related-topics}

