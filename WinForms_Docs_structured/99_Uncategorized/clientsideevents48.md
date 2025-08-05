---
title: clientsideevents48.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents48.md
created_at: 2025-08-05
---








  









## Client-Side Events {#client-side-events style="tab-stops: 0pt"}

Schedule control enables client side events to handle the following:

[·      ]Appointment selection

[·      ]Cell double-click

[] 

To enable client side scripting, you should set the EnableClientSideEvents as true.

**[]** 

Appointment Selection

A user can raise the **AppointmentSelection** event by selecting an appointment.

The event argument consists of the appointment details with the appointment ID.  The user specified appointment selection method receives the appointment details and displays it in the Customized Appointment Window.

[] 

Cell Double-click

A user can raise the **OnCellDoubleClick** event by double-clicking the cells.

When this event is raised, the event arguments consist of the  cell details such as date, start time, end time, and resource. The user specified method receives the cell details and uses it to create a new appointment by using the Customized Appointment Window.

If a user does not specify any method for appointment selection and cell double-click, then the Schedule's default appointment window will be displayed.

[] 

Properties

Table 20: Cell Double-click Properties

**[]** 


  Property                 Description                                      Type of the Property   Value it Accepts                       Dependency
  ------------------------ ------------------------------------------------ ---------------------- -------------------------------------- ------------
  EnableClientSideEvents   Used to set enable/disable client-side events.   Boolean                [True/False]   NA


[] 

Events

The client-side events of the Schedule control are given below.

 

Table 21:Cell Double-click Events

[] 


+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| Name                             | Description                                                                                                                               | Arguments                                                  |
+==================================+===========================================================================================================================================+============================================================+
| ClientSideOnAppointmentSelection | Specifies the client-side function to call when an appointment is selected.                                                               | Instance, Args(                                            |
|                                  |                                                                                                                                           |                                                            |
|                                  |                                                                                                                                           | ID: returns the Appointment ID                             |
|                                  |                                                                                                                                           |                                                            |
|                                  | The event handler receives an argument of type args containing data related to this event.                                                |                                                            |
|                                  |                                                                                                                                           |                                                            |
|                                  |                                                                                                                                           | CurrentItem: returns the selected appointment's details)   |
|                                  |                                                                                                                                           |                                                            |
|                                  | If the user does not specify any function for this event, the default appointment window is loaded with the selected appointment details. |                                                            |
|                                  |                                                                                                                                           |                                                            |
|                                  |                                                                                                                                           |                                                            |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| ClientSideOnCellDoubleClick      | Specifies the client-side function to call when a Schedule cell is double clicked.                                                        | Instance, Args(                                            |
|                                  |                                                                                                                                           |                                                            |
|                                  |                                                                                                                                           | SelectedDate: returns the selected cell's date.            |
|                                  |                                                                                                                                           |                                                            |
|                                  | The event handler receives an argument of type args containing data related to this event.                                                | SelectedStartTime: returns the selected cell's start time. |
|                                  |                                                                                                                                           |                                                            |
|                                  |                                                                                                                                           | SelectedEndTime: returns the selected cell's end time.     |
|                                  |                                                                                                                                           |                                                            |
|                                  | If the user does not specify any function for this event, the default appointment window is loaded with the selected cell details.        | SelectedResourceId: returns the selected cell's owner id.) |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+


[] 

More:





