---
title: howtosetthescheduleappointmentsasreadonly.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthescheduleappointmentsasreadonly.md
created_at: 2025-07-03
---








  









## How to set the schedule appointments as read-only {#how-to-set-the-schedule-appointments-as-read-only style="tab-stops: 0pt"}

[] 

You can achieve this by canceling the **ScheduleAppointmentClick** event of the ScheduleControl. Please refer the below code snippet which illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                                                                                                                    |
| \                                                                                                                                                                                                                                                                             |
| ]**[]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [// Handle the ScheduleAppointmentClick event.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [this][.scheduleControl1.ScheduleAppointmentClick += [new] [ScheduleAppointmentClickEventHandler](scheduleControl1_ScheduleAppointmentClick);] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [private][ [void] scheduleControl1_ScheduleAppointmentClick([object] sender, [ScheduleAppointmentClickEventArgs] e)]      |
|                                                                                                                                                                                                                                                                               |
| [{   ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [// Cancel the event.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [e.Cancel = [true];]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]\                                                                                                                                                                                                                                                                                                                                                 |
| \                                                                                                                                                                                                                                                                                                                                                              |
| ]**[]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\' Handle the ScheduleAppointmentClick event.]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                |
| [AddHandler][ ScheduleControl1.ScheduleAppointmentClick, [AddressOf] ScheduleControl1_ScheduleAppointmentClick]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] scheduleControl1_ScheduleAppointmentClick([ByVal] sender [As] [Object], [ByVal] e [As] ScheduleAppointmentClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\' Cancel the event.]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p30} 

 

 

[]{#related-topics}

