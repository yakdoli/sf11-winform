---
title: reminderserviceinterface.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\reminderserviceinterface.md
created_at: 2025-07-03
---








  









### Reminder Service Interface {#reminder-service-interface style="tab-stops: 0pt"}

[] 

The interface **IScheduleReminderService** is available in the Schedule assembly, which is used to cancel the reminder window for the schedule control. Users can add their code to be executed whenever the reminder is invoked.

1.   Creating class for implementing the interface

Creating a class called **ReminderServiceImpl** that implements **IScheduleReminderService**. The method displays all the appointments' subjects that are being reminded.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [public][ [class] [ReminderServiceImpl] : [IScheduleReminderService]] |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [     [#region] IScheduleReminderService Members]                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [       [public] [void] OnReminderInvoked([object] o, [ScheduleReminderEventArgs] e)]                |
|                                                                                                                                                                                                                                 |
| [       {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [          [foreach] ([ScheduleAppointment] appointment [in ]e.ReminderAppointments)                {]                    |
|                                                                                                                                                                                                                                 |
| [               [MessageBox].Show(appointment.Subject);]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [          }  ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [      #endregion]                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   Creating a static resource value for ReminderService

Creating instance or object for the ReminderServiceImpl defined in the above XAML.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][Grid.Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [     \<][local][:][ReminderServiceImpl][ x:Key=][\"Service\"\>\</][local][:][ReminderServiceImpl][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][Grid.Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Assigning it in Schedule's Property

Assigning the created object to schedule's property ReminderService in XAML.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][schedule][:][Schedule][ x][:][Name][=\"schedule\"][ DisplayReminder][=\"True\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [           ReminderService][=\"{][StaticResource][ Service][}\"][ ][/\>]                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

4.   Assigning the object of the class to ReminderService property

Creating an object or instance for the class ReminderServiceImpl and assigning the object to schedule's property ReminderService in C#.


{border="0"}Note: Set the DisplayReminder property to true to implement any functionality on Reminderservice.

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][]                                                                                               |
|                                                                                                                                                                                                           |
| [ReminderServiceImpl][ service = [new] [ReminderServiceImpl]();    ] |
|                                                                                                                                                                                                           |
| [Schedule ][schedule = new [Schedule]();]                                                 |
|                                                                                                                                                                                                           |
| [schedule][.ReminderService = service;]                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[                {border="0"}]Note: Users can either use Coding section 2 & 3 together if he uses XAML or Coding section 3 alone if he uses C#.  But Coding section 1 is mandatory for either case.

 


[]{#related-topics}

