---
title: howtodisablethedragbehaviorofscheduleappointmentsintheschedulecontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodisablethedragbehaviorofscheduleappointmentsintheschedulecontrol.md
created_at: 2025-07-03
---








  









## How to disable the drag behavior of schedule appointments in the ScheduleControl {#how-to-disable-the-drag-behavior-of-schedule-appointments-in-the-schedulecontrol style="tab-stops: 0pt"}

[] 

You can do this by invoking the **ItemChanging** event of the ScheduleControl, and canceling the **ItemDrag** action, as shown in the below code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                                                                                                                        |
| \                                                                                                                                                                                                                                                                                 |
| ]**[]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                   |
| [// Handle the ItemChanging event.]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [this][.scheduleControl1.ItemChanging += [new] [ScheduleAppointmentChangingEventHandler](scheduleControl1_ItemChanging); ]                         |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [private][ [void] scheduleControl1_ItemChanging([object] sender, Syncfusion.Schedule.[ScheduleAppointmentCancelEventArgs] e)] |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [   [// Cancel the ItemDrag action.]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [if][ (e.Action == [ItemAction].ItemDrag)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [{  ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                   |
| [e.Cancel = [true];]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]\                                                                                                                                                                                                                                                                                                                                                          |
| \                                                                                                                                                                                                                                                                                                                                                                       |
| ]**[]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Handle the ItemChanging event.]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [AddHandler][ [Me].scheduleControl1.ItemChanging, [AddressOf] scheduleControl1_ItemChanging]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] scheduleControl1_ItemChanging([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Schedule.ScheduleAppointmentCancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [   [\' Cancel the ItemDrag action.]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [If][ e.Action = ItemAction.ItemDrag [Then]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [If]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p29} 

 

 

[]{#related-topics}

