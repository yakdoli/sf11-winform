---
title: reminderappointments.md
original_path: WinForms_Docs/99_Uncategorized/reminderappointments.md
created_at: 2025-08-05
---








  









### Reminder Appointments {#reminder-appointments style="tab-stops: 0pt"}

 

Schedule control provides support for Reminder Appointments. This feature is used to show Reminder Dialog when the Reminder Time of an appointment is reached or when the appointment start time is reached.  Schedule Reminder also supports Recurrence Appointment and all-day appointments.

 

 Use Case Scenarios

Reminder Appointmnets help the Users to:

[·      ]Design a Reminder Dialog like Outlook Reminder

[·      ]Open the Reminder Dialog when Reminder time of an appointment is reached

[·      ]Reminder Support for all types of Recurrence appointment

[·      ][We can postpone the Reminder time for the due-in appointments by using Snooze]

[·      ][For overdue Appointments we can postpone the reminder after the Chosen snooze time]

[·      ]Dismiss and Dismiss All should Remove Reminder for selected and all appointment respectively.

[·      ]Open Item should display Add/Edit Appointment Window of the selected appointment.

 

Adding Reminder Appointment

[·      ]Through Code

To add a Reminder Appointment through code use **Reminder** and **ReminderValue** Properties.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Appointments][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            [\<][syncfusion][:][ScheduleWebAppointment]  [Reminder] [=] [\"true\"] [ReminderValue] [=] [\"15\"] [StartTime][=\"02/26/2010 01:00:00\"] [EndTime][=\"02/26/2010 02:00:00\"] [Subject][=\"Training\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Appointments][\>][]                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                      |
|                                                                                                                                                                                                         |
| [ScheduleWebAppointment][ app = [new] [ScheduleWebAppointment]();] |
|                                                                                                                                                                                                         |
| [Schedule1.Appointments.Add(app);]                                                                                                                                  |
|                                                                                                                                                                                                         |
| [app.Reminder = [true];]                                                                                                                       |
|                                                                                                                                                                                                         |
| [app.ReminderValue = 5;][]                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[VB\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [Private][ app [As] Syncfusion.Web.UI.WebControls.ScheduleControl.ScheduleWebAppointment = [New] ScheduleWebAppointment()] |
|                                                                                                                                                                                                                                                           |
| [Scheduler1.Appointments.Add(app1)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [app.Reminder = [true]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [app.ReminderValue = 15][]                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[   ][]

[·      ]Through Callback

 

It is also possible to add reminder Appointment through CallBack by double-clicking the schedule cells. Add/Edit Appointment dialog will pop-up as shown below.

 

{border="0"}

Figure 76:Add/Edit Appointment Dialog

 

Properties

Table 2: Reminder Properties


  --------------- -------------------------------------- ------------- ----------- -----------------
  Property        Description                            Type          Data Type   Reference links
  Reminder        Denotes the Reminder Appointment       Server-Side   Boolean     NA
  ReminderValue   Denotes the Reminder Time in minutes   Server-Side   Integer     NA
  --------------- -------------------------------------- ------------- ----------- -----------------


**[]** 

[]{#_Freeze_Panes}Reminder Support

Reminder Feature also supports for recurrence appointment and All-day Appointment.

 

Table 3: Reminder Dialog Feature


  ---------------------------------------------------- -------------------------------------------------------------------------
  Reminder Dialog Features                             Description
  Open Item / On Double Click an appointment in list   It will open the Edit Appointment Dialog for selected Appointment.
  Snooze for due in Appointments                       We can postpone the reminder time for the due In appointments
  Snooze for overdue Appointments                      We can postpone the reminder to show after the Chosen snooze time
  Dismiss                                              Dismiss is used to remove the reminder for selected appointment
  DismissAll                                           DismissAll is used to Remove Reminder for all the reminder appointments
  ---------------------------------------------------- -------------------------------------------------------------------------


 

Reminder for Recurrence Appointment

Reminder Feature also supports Recurrence Appointment. The Reminder Dialog will show when the next recurrence appointment reminder time is reached, till then the Reminder Dialog will have the last overdue appointment in the list.

{border="0"}

Figure 77: Reminder for Recurrence Appointment

**[]** 

Reminder for All-Day Appointment

Reminder Feature also supports All-Day Appointments.

 

{border="0"}

Figure 78: Reminder For All-Day Appointment

 

Appearance

Initially the Reminder dialog appears as shown below when the reminder time reached. The dialog title contains the number of reminder appointment in due time.

 

 

{border="0"}

Figure 79: Reminder Dialog before selecting Appointment

 

On clicking the Appointment in the list it should display **Subject, Start Time, Resource name and Location** of the selected appointment on top as shown below.

 

{border="0"}

Figure 80: Reminder Dialog after selecting Appointment

 

Sample Link

To access a Toolbar Customization sample:

1.   Open the Syncfusion Dashboard.

2.   Select User Interface.

3.   Click the ASP.NET drop-down list and select Explore Samples.

[4.    ]Navigate to **Schedule.Web** -\> **Basic Features -\> Reminder Demo.**[]

 

[]{#related-topics}

