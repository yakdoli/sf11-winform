---
title: howtoobtainthedatethatisclickedintheschedulecontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtoobtainthedatethatisclickedintheschedulecontrol.md
created_at: 2025-08-05
---








  









## How to obtain the date that is clicked in the ScheduleControl {#how-to-obtain-the-date-that-is-clicked-in-the-schedulecontrol style="tab-stops: 0pt"}

[] 

Clicked DateTime value of a Schedule Control can be obtained by handling the **ScheduleAppointmentClick** event as shown in the following code snippet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                                                                                                                    |
| \                                                                                                                                                                                                                                                                             |
| ]**[]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [// Subscribe to item click event.]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [this][.scheduleControl1.ScheduleAppointmentClick += [new] [ScheduleAppointmentClickEventHandler](scheduleControl1_ScheduleAppointmentClick);] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [// Sample event handler to catch clicks on the schedule control.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [private][ [void] scheduleControl1_ScheduleAppointmentClick([object] sender, [ScheduleAppointmentClickEventArgs] e)]      |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [Console][.WriteLine([\"scheduleControl1_ScheduleAppointmentClick: {0} {1}\"], e.ClickType, e.ClickDateTime);]                                                    |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]\                                                                                                                                                                                                                                                                                                                                                 |
| \                                                                                                                                                                                                                                                                                                                                                              |
| ]**[]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\' Subscribe to item click event]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [AddHandler][ scheduleControl1.ScheduleAppointmentClick, [AddressOf] scheduleControl1_ScheduleAppointmentClick]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\' Sample event handler to catch clicks on the schedule control.]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] scheduleControl1_ScheduleAppointmentClick([ByVal] sender [As] [Object], [ByVal] e [As] ScheduleAppointmentClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"scheduleControl1_ScheduleAppointmentClick: {0} {1}\"], e.ClickType, e.ClickDateTime)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

