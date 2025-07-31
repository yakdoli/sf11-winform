---
title: scheduleappointmentstatus.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scheduleappointmentstatus.md
created_at: 2025-07-03
---








  









### Schedule Appointment Status {#schedule-appointment-status style="tab-stops: 0pt"}

[] 

This feature helps you to define a set a status to the Schedule Appointments. The Schedule control has provision to set the appointment with different status. By default, the Essential Schedule control has a collection of Appointment status which includes Busy, Free, Out-of-office and Tentative. An appointment created in Schedule control will take "**Busy**" status by default. You can modify the status of the appointment through Appointment Editor Window or through code.

[] 

You can have their own collection of status in addition to or overriding the default set of status. These custom statuses are also available while editing the status of appointment through AppointmentEditor and through code. An appointment added to the Schedule control can take any one of the status in this collection of Appointment status.

[] 

Use Case Scenarios

[] 

In a call center application which uses Schedule control to record the calls, you may need to add your own custom status like "Process Over", "Processing", "Not to be processed", "Internal process" and etc. These statuses can be defined and set to Schedule appointments. The custom status added will be available in Appointment Editor of the Schedule control as shown in the below figure.

[] 

{border="0"}

 

Figure 30: Custom Appointment Status

 

Properties

 

+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------+---------------------------------------------------------------------------------------+
| Property                             | Description                                                                                                                                                                             | Type                | Data Type                           | Reference links                                                                       |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------+---------------------------------------------------------------------------------------+
| Schedule.AppointmentStatusCollection | It is a set of AppointmentStatus available in theSchedule control. Any appointment added to the Schedule control will have any one of the status from this AppointmentStatusCollection. | Dependency property | ScheduleAppointmentStatusCollection |                                                                                       |
|                                      |                                                                                                                                                                                         |                     |                                     |                                                                                       |
|                                      |                                                                                                                                                                                         |                     | .                                   |                                                                                       |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------+---------------------------------------------------------------------------------------+
| ScheduleAppointment.Status           | Holds information about the current status of appoinment                                                                                                                                | Dependency Property | ScheduleAppointmentStatus           | []  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------+---------------------------------------------------------------------------------------+

**[]** 

Adding Appointment Status to an Application

**[]** 

Setting a status to Appointment using Appointment Editor

**[]** 

[·      ]Open AppointmentEditor of the Schedule control by double clicking the time slot of DaysView / MonthView / ScheduleView for creating new appointment.

[·      ]Choose a status from ShowAs combo box available in the AppointmentEditor.

[·      ]The newly added appointment has status set to the status that is chosen in AppointmentEditor.

[·      ]If you want to edit existing appointment's status, just open the AppointmentEditor by double clicking the appointment.

[·      ]Initially the status of the appointment that is edited will be set in the AppointmentEditor's ShowAs combo box.

[·      ]Now choose new status for the appointment. Save and close the AppointmentEditor. New status will be set to the appointment.

**[]** 

Adding custom statuses to Schedule control

Adding a set of ScheduleAppointmentStatus to Schedule.AppointmentStatusCollection includes the custom ScheduleAppointmentStatus to the Schedule control in addition to the default statuses. The below code snippet shows how to add custom with default AppointmentStatus to the Schedule control.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][Schedule][ x][:][Name][=\"Schedule1\"][ ScheduleType][=\"Week\"][ CalendarVisibility][=\"Visible\"][ ItemsSource][=\"{][Binding][ Data][}\" \>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\<][syncfusion][:][Schedule.AppointmentStatusCollection][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][syncfusion][:][ScheduleAppointmentStatus][ Brush][=\"Green\"][ Status][=\"Process Over\" /\>][                    ][]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\</][syncfusion][:][Schedule.AppointmentStatusCollection][\>][                ][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [            ][\</][syncfusion][:][Schedule][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\[OR\]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Schedule1.AppointmentStatusCollection.Add([new] [ScheduleAppointmentStatus]() { Brush = [new] [SolidColorBrush]([Colors].Green), Status = [\"Process Over\"] });] |
|                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Assigning a new ScheduleAppointmentStatusCollection value to Schedule.AppointmentStatusCollection includes custom ScheduleAppointmentStatus to the Schedule control by removing the default status. The below code snippet shows how to add custom only AppointmentStatus to the Schedule control.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][Schedule.AppointmentStatusCollection][\>][]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    ][\<][syncfusion][:][ScheduleAppointmentStatusCollection][\>][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                        ][\<][syncfusion][:][ScheduleAppointmentStatus][ Brush][=\"Green\"][ Status][=\"Process Over\" /\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    ][\</][syncfusion][:][ScheduleAppointmentStatusCollection][\>][]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                ][\</][syncfusion][:][Schedule.AppointmentStatusCollection][\>][  ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\[OR\]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                           |
| [ScheduleAppointmentStatusCollection][ \_statusCollection = [new] [ScheduleAppointmentStatusCollection]();]                                                                                          |
|                                                                                                                                                                                                                                                                                                                                           |
| [            \_statusCollection.Add([new] [ScheduleAppointmentStatus]() { Brush = [new] [SolidColorBrush]([Colors].Green), Status = [\"Process Over\"] });] |
|                                                                                                                                                                                                                                                                                                                                           |
| [            Schedule1.AppointmentStatusCollection = \_statusCollection;]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

