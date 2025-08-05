---
title: serversideevents1.md
original_path: WinForms_Docs/99_Uncategorized/serversideevents1.md
created_at: 2025-08-05
---








  









### Server-side Events {#server-side-events style="tab-stops: 0pt"}

[] 

This section describes the list of server-side events.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------+
|                                   |                                                                                                    |
|                                   |                                                                                                    |
| Server-side Event                 | Description                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentAdding                 | Handled when you Add a Schedule appointment.                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentDeleting               | Handled when you Delete a Schedule appointment.                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentChanged                | Event that is handled when an appointment is changed.                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentChanging               | Event that is handled when a Schedule appointment is about to change.                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentClicked                | Event that is handled on a Schedule appointment click.                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentDragged                | Event that is handled on appointment drag.                                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| BlockedAppointmentOveridden       | Event that is handled when blocked appointment collides with appointment.                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| CallbackRefresh                   | Event that is handled on client Refresh method.                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| CheckVisibleDay                   | Event that is handled to obtain information on the day visibility.                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| ResourceIndexChanged              | Event that is handled when the resource start index is changed.                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| ScheduleClicked                   | Event that is handled on a Schedule cell click.                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| StartDateChanged                  | Event that is handled when the start date is changed.                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| AppointmentDraggedOut             | Event that is handled when a Schedule appointment is dragged onto an HTML control.                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataBinding                       | Event that is handled when data is bound to the Schedule  control from a data source.              |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataSourceControlAdding           | Occurs when an appointment is added into the Schedule control.                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataSourceControlAdded            | Occurs after an appointment is added into the Schedule control.                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataSourceControlUpdated          | Occurs when an appointment is updated.                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataSourceControlUpdating         | Occurs after an appointment is updated.                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataSourceControlDeleting         | Occurs when an appointment is deleted from the Schedule control.                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| DataSourceControlDeleted          | Occurs after an appointment is deleted from the Schedule control.                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| ExternalAppointmentDragging       | Event that is triggered when an appointment is dragged from an external control (Grid View, etc.). |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| RenderingAppointment              | Occurs on rendering an appointment.                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| ResourceIndexChanged              | Event that is triggered when the index of an appointment is changed.                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| SchedulePrintClicked              | Handled when Print Started.[]                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| ScheduleAfterPrint                | Handled After Print.[]                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| ScheduleMenuItemClick             | Event that is triggered when a Schedule menu item is clicked.                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| StartDateChanged                  | Event that is triggered when the start date of an appointment is changed.                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------+


[] 

 

 

AppointmentChanged Event

[] 

This is a server-side event that is handled when an appointment is changed.

 

The event handler receives an argument of type[ ]**ScheduleAppointmentEventArgs**[ ]containing data related to this event. The following ScheduleAppointmentEventArgs[ ]members provide information specific to this event.

[] 


  ------------- ----------------------------------------------------
  Member        Description
  Action        Specifies the action performed on the appointment.
  CurrentItem   Gets or sets the current item.
  ------------- ----------------------------------------------------


[] 

In the below example, the modified Subject is displayed in the label element.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnAppointmentChanged] [=\"Schedule1_AppointmentChanged\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [protected][ [void] Schedule1_AppointmentChanged([object] sender, Syncfusion.Schedule.[ScheduleAppointmentEventArgs] e)] |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [  [ // Gets the current appointment\'s subject.]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [   Text1.Text = e.CurrentItem.Subject;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Protected][ [Sub] Schedule1_AppointmentChanged([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Schedule.ScheduleAppointmentEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Gets the current appointment\'s subject.]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [Text1.Text = e.CurrentItem.Subject]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

AppointmentChanging Event

[] 

This is a server-side event that is handled when a Schedule appointment is about to change. Also, when an appointment is deleted using the ViewStrip item, this event will be triggered before the AppointmentChanged event.

 

The event handler receives an argument of type[ ]**ScheduleAppointmentCancelEventArgs**[ ]containing data related to this event. The following ScheduleAppointmentCancelEventArgs[ ]members provide information specific to this event.

[] 


  -------------- -----------------------------------------------------------------------
  Member         Description
  Action         Specifies the action to be performed on the appointment.
  Cancel         Gets or sets a value indicating whether the event should be canceled.
  CurrentItem    Gets or sets the current item.
  ProposedItem   Gets or sets the proposed item.
  -------------- -----------------------------------------------------------------------


[] 

In the example given below, the subject of the CurrentItem and the ProposedItem are displayed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnAppointmentChanging] [=\"Schedule1_AppointmentChanging\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| [protected][ [void] Schedule1_AppointmentChanging([object] sender, Syncfusion.Schedule.[ScheduleAppointmentCancelEventArgs] e)] |
|                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| [   // Gets the appointment\'s current and proposed subjects.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                        |
| [   Text1.Text = e.CurrentItem.Subject + [\"is changing to\"] + e.ProposedItem.Subject;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                         |
| [Protected [Sub] Schedule1_AppointmentChanging([ByVal] sender [As] Object, [ByVal] e [As] [Syncfusion.Schedule.ScheduleAppointmentCancelEventArgs])] |
|                                                                                                                                                                                                                                                                                                                         |
| [\' Gets the appointment\'s current and proposed subjects.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                         |
| [Text1.Text = e.CurrentItem.Subject & [\"is changing to\"] & e.ProposedItem.Subject]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

AppointmentClicked Event

[] 

This is a server-side event that is handled on a Schedule appointment click.

 

The event handler receives an argument of type[ ]**AppointmentEventArgs**[ ]containing data related to this event. The following AppointmentEventArgs[ ]member provides information specific to this event.

[] 


  ------------- -------------------------------------------------
  Member        Description
  Appointment   Gets the appointment which generated the event.
  ------------- -------------------------------------------------



 

{border="0"}Note: AutoPostBackOnAppointmentClicked must be set to True to trigger the Appointment triggered event.


[] 

In the below example, the back color of the appointment will be changed and a message will be displayed on the label element.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnAppointmentClicked] [=\"Schedule1_AppointmentClicked\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [protected][ [void] Schedule1_AppointmentClicked([object] sender, [AppointmentEventArgs] e)] |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [   // When the appointment is clicked, appointment drag is enabled and back color of the appointment is changed.]                                                                             |
|                                                                                                                                                                                                                                                  |
| [e.Appointment.AllowDrag = [true];]                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [e.Appointment.BackColor = [Color].AliceBlue;]                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [Disp.Text = [\"AppointmentClicked event is fired and Appointment drag is enabled\"];]                                                                                                |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [Protected [Sub] Schedule1_AppointmentClicked([ByVal] sender [As] Object, [ByVal] e [As] AppointmentEventArgs)] |
|                                                                                                                                                                                                                                                              |
| [   [\' When the appointment is clicked, appointment drag is enabled and back color of the appointment is changed.]]                                                                               |
|                                                                                                                                                                                                                                                              |
| [e.Appointment.AllowDrag = [True]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [e.Appointment.BackColor = Color.AliceBlue]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [Disp.Text = [\"AppointmentClicked event is fired and Appointment drag is enabled\"]]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

AppointmentDragged Event

[] 

This is a server-side event that is handled on appointment drag.

 

The event handler receives an argument of type[ ]**AppointmentDraggedEventArgs**[ ]containing data related to this event. The following AppointmentDraggedEventArgs[ ]members provide information specific to this event.

[] 


  -------------- -------------------------------------------------
  Member         Description
  Appointment    Gets the appointment which generated the event.
  OldEndTime     Appointment\'s EndTime value before dragging.
  OldStartTime   Appointment\'s StartTime value before dragging.
  OldOwner       Appointment\'s Owner value before dragging.
  -------------- -------------------------------------------------


[] 

In the below example, the back color will be changed, and the start and end time before dragging the appointment and the new start and end time where the appointment is positioned, will be displayed.

[] 

Also, if the appointment is dragged between resources (checked using the if condition), the id of the old and the new resource where the appointment is placed, will be displayed on the label elements.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnAppointmentDragged][=\"Schedule1_AppointmentDragged\"] [runat][=\"server\"] [Height][=\"400\" ][Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [protected][ [void] Schedule1_AppointmentDragged([object] sender, [AppointmentDraggedEventArgs] e)]                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [// Schedule1.EnableCallbacks = false;]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [e.Appointment.BackColor = [Color].AliceBlue;]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [Disp.Value = [\"Appointment time is changed from\"] + e.OldStartTime + [\'\\n\'] + e.OldEndTime + [\"to\"] + e.Appointment.StartTime +[\"to\"]+ e.Appointment.EndTime;] |
|                                                                                                                                                                                                                                                                                                          |
| [if][(e.OldResourceID != e.Appointment.ResourceID)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [Text1.Text=[\"Appointment is moved from\"] + e.OldResourceID + [\"to\"] + e.Appointment.ResourceID;]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [Protected [Sub] Schedule1_AppointmentDragged([ByVal] sender [As] Object, [ByVal] e [As] AppointmentDraggedEventArgs)]                      |
|                                                                                                                                                                                                                                                                                          |
| [\' Schedule1.EnableCallbacks = False]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [e.Appointment.BackColor = Color.AliceBlue]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                          |
| [Disp.Value = [\"AppointmentDragged event is fired\"]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                          |
| [Disp.Value = [\"Appointment time is changed from\"] & e.OldStartTime + ControlChars.Lf + e.OldEndTime & [\"to\"] & e.Appointment.StartTime & [\"to\"] & e.Appointment.EndTime] |
|                                                                                                                                                                                                                                                                                          |
| [If][ e.OldResourceID \<\> e.Appointment.ResourceID [Then]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                          |
| [Text1.Text=[\"Appointment is moved from\"] & e.OldResourceID & [\"to\"] & e.Appointment.ResourceID]                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

BlockedAppointmentOverridden Event

[] 

This is a server-side event that is handled when blocked appointment collides with appointment.

 

The event handler receives an argument of type[ ]**BlockedAppointmentOverridenEventArgs**[ ]containing data related to this event. The following BlockedAppointmentOverridenEventArgs[ ]member provides information specific to this event.

[] 


  ------------- --------------------------------
  Member        Description
  Appointment   Gets the Schedule appointment.
  ------------- --------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnBlockedAppointmentOverridden][=\"Schedule1_BlockedAppointmentOverriden\"] [runat][=\"server\"] [Height][=\"400\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Width][=\"600\"][ [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [protected][ [void] Schedule1_BlockedAppointmentOverriden([object] sender, [BlockedAppointmentOverridenEventArgs] e)] |
|                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [   [// Unblocks the blocked appointment.]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [   e.Appointment.Blocked = [false];]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Protected][ [Sub] Schedule1_BlockedAppointmentOverriden([ByVal] sender [As] [Object], [ByVal] e [As] BlockedAppointmentOverridenEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Unblocks the blocked appointment.]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [e.Appointment.Blocked = [False]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CallbackRefresh Event

[] 

This is a server-side event that is handled on client Refresh method. Schedule control supports in-built AJAX feature, that enables to refresh the control avoiding postback. This can be performed by raising the **CallbackRefresh** event.

 

The event handler receives an argument of type[ ]**CallbackEventArgs**[ ]containing data related to this event. The following CallbackEventArgs[ ]member provides information specific to this event.

[] 


  ------------------ -----------------------------------
  Member             Description
  CallbackArgument   The arguments sent by the client.
  ------------------ -----------------------------------


[] 

In the following example, the CallbackRefresh event will be raised, adding a new resource to the control.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnCallbackRefresh] [=\"Schedule1_CallbackRefresh\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"] [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [protected][ [void] Schedule1_CallbackRefresh([object] sender, Syncfusion.Web.UI.WebControls.Shared.[CallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [   [// A new resource is added to the Schedule control.]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [Resource resource1 = [new] Resource();]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                    |
| [Schedule1.Resources.Add(resource1);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                    |
| [resource1.Name = [\"Added Resource\"];]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Protected][ [Sub] Schedule1_CallbackRefresh([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.Shared.CallbackEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' A new resource is added to the Schedule control.]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ resource1 [As] Resource = [New] Resource()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Schedule1.Resources.Add(resource1)]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [resource1.Name = [\"Added Resource\"]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CheckVisibleDay Event

[] 

This is a server-side event that is handled to obtain information on the day visibility.

The event handler receives an argument of type **CheckVisibleDayEventArgs** containing data related to this event. The following CheckVisibleDayEventArgs members provide information specific to this event. It returns the date based on the schedule type (30 visible days for month, 7 visible days for week, etc.). The calendar should be available for this.

[] 


  -------- -------------------------------------------------------------------
  Member   Description
  Date     Gets the date when the event is called.
  Hidden   Specifies whether or not the day should be shown in the Schedule.
  -------- -------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnCheckVisibleDay] [=\"Schedule1_CheckVisibleDay\" ][runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"] [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [protected][ [void] Schedule1_CheckVisibleDay([object] sender, CheckVisibleDayEventArgs e)] |
|                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [  [// Gets the current date in string format and display in the text box.]]                                                                                     |
|                                                                                                                                                                                                                            |
| [  Text1.text= e.Date.ToString();]                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [Protected][ [Sub] Schedule1_CheckVisibleDay([ByVal] sender [As] [Object], [ByVal] e [As] CheckVisibleDayEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [\' Gets the current date in string format and display in the text box.]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [Text1.text = e.Date.ToString()]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataSourceControlAdding Event

[] 

While adding the appointments to the Schedule control, an appointment object must be created for each appointment in the control. The DataSourceControlAdding event is handled when an appointment is added to the Schedule control. It enables us to provide an event handling method that performs a custom routine, such as, adding extra properties to an appointment, whenever this event occurs.

AppointmentDataEventArgs object is passed to the event handling method, which enables us to access the properties of the appointments that are added.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnDataSourceControlAdding] [=\"Schedule1_DataSourceControlAdding\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]   [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [protected][ [void] Schedule1_DataSourceControlAdding([object] sender, AppointmentDataEventArgs e)] |
|                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Protected][ [Sub] Schedule1_DataSourceControlAdding([ByVal] sender [As] [Object], [ByVal] e [As] AppointmentDataEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataSourceControlAdded Event

[] 

This event is handled after an appointment is added to the Schedule control. It enables us to provide an event handling method that performs a custom routine, such as, checking the result of the Add operation, whenever this event occurs.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnDataSourceControlAdded] [=\"Schedule1_DataSourceControlAdded\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [protected][ [void] Schedule1_DataSourceControlAdded([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [Protected][ [Sub] Schedule1_DataSourceControlAdded([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataSourceControlUpdating Event

[] 

This event is handled when an appointment in the Schedule control is updated. It enables us to provide an event handling method that performs a custom routine, such as, canceling the Update operation, whenever this event occurs.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnDataSourceControlUpdating] [=\"Schedule1_DataSourceControlUpdating\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]  [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [protected][ [void] Schedule1_DataSourceControlUpdating([object] sender, AppointmentDataEventArgs e)] |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [int][ id = e.Appointment.UniqueID;]                                                                                                            |
|                                                                                                                                                                                                                                      |
| [} ]                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Protected][ [Sub] Schedule1_DataSourceControlUpdating([ByVal] sender [As] [Object], [ByVal] e [As] AppointmentDataEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ id [As] [Integer] = e.Appointment.UniqueID]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataSourceControlUpdated Event

[] 

This event is handled after an appointment in the Schedule control is updated. It enables us to provide an event handling method that performs a custom routine, such as, checking the result of the Update operation, whenever this event occurs.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnDataSourceControlUpdated][=\"Schedule1_DataSourceControlUpdated\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]   [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [protected][ [void] Schedule1_DataSourceControlUpdated([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [Protected][ [Sub] Schedule1_DataSourceControlUpdated([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataSourceControlDeleting Event

[] 

This event is handled when an appointment in the Schedule control is deleted. It enables us to provide an event handling method that performs a custom routine, such as, canceling the Delete operation, whenever this event occurs.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnDataSourceControlDeleting] [=\"Schedule1_DataSourceControlDeleting\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]  [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [protected][ [void] Schedule1_DataSourceControlDeleting([object] sender, AppointmentDataEventArgs e)] |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [e.Cancel = [true];]                                                                                                                                                        |
|                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Protected][ [Sub] Schedule1_DataSourceControlDeleting([ByVal] sender [As] [Object], [ByVal] e [As] AppointmentDataEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataSourceControlDeleted Event

[] 

This event is handled after an appointment in the Schedule control is deleted. It enables us to provide an event handling method that performs a custom routine, such as, checking the results of the Delete operation, whenever this event occurs.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnDataSourceControlDeleted] [=\"Schedule1_DataSourceControlDeleted\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]   [MinDate][=\"2007-01-16\"] [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [protected][ [void] Schedule1_DataSourceControlDeleted([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [Protected][ [Sub] Schedule1_DataSourceControlDeleted([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ResourceIndexChanged Event

[] 

This is a server-side event that is handled when the resource start index is changed.

[] 

The event handler receives an argument of type[ ]**ResourceIndexChangedEventArgs** containing data related to this event. The following ResourceIndexChangedEventArgs[ ]member provides information specific to this event.

[] 


  ----------------------- --------------------------------------
  Member                  Description
  OldStartResourceIndex   Gets the old Schedule ResourceIndex.
  ----------------------- --------------------------------------


[] 

In the below example, the previous resource index and the new resource index will be displayed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnResourceIndexChanged] [=\"Schedule1_ResourceIndexChanged\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [protected][ [void] Schedule1_ResourceIndexChanged([object] sender, [ResourceIndexChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [  [ // Displays the old and new resource index.]]                                                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [   Disp.Text = [\"\"];]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [   Disp.Text = e.OldStartResourceIndex + [\"is changed to\"] + Schedule1.ResourceIndex;]                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [Protected [Sub] Schedule1_ResourceIndexChanged([ByVal] sender [As] Object, [ByVal] e [As] ResourceIndexChangedEventArgs)] |
|                                                                                                                                                                                                                                                                         |
| [\' Displays the old and new resource index.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [Disp.Text = [\"\"]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [Disp.Text = e.OldStartResourceIndex & [\"is changed to\"] & Schedule1.ResourceIndex]                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

SchedulePrintClicked

 

The SchedulePrintClicked event is triggered at the beginning of the server-side Print method.

This event is mainly used to change the appearance of the schedule before print.

 


  ----------------------------------- ----------------------------------------------------- -------------------------------------------------------------- ------------------------------------- --------------------------------------------
  **[Event]**   **[Description]**               **[Arguments]**                          **[Type]**      **[Reference link]**
  SchedulePrintClicked                Handled when Print Started.[]   [EventArgs][]   [Server-Side]   [NA]
  ----------------------------------- ----------------------------------------------------- -------------------------------------------------------------- ------------------------------------- --------------------------------------------


 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [\[C#\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [    [void] Schedule1_SchedulePrintClicked([object] sender, Syncfusion.Web.UI.WebControls.ScheduleControl.[ScheduleOnPrintClickEventArgs] e)] |
|                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [        [this].Schedule1.CalendarPosition = [ScheduleCalendarPosition].None;]                                                                                     |
|                                                                                                                                                                                                                                                     |
| [        [this].Schedule1.Height = [Unit].Percentage(100);]                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [\[VB\]]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [Protected] [Sub] Schedule1_SchedulePrintClicked([ByVal] sender [As] [Object], [ByVal] e [As] [ScheduleOnPrintClickEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [        [Me].Schedule1.CalendarPosition = [ScheduleCalendarPosition].None]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                     |
| [        [Me].Schedule1.Height = [Unit].Percentage(100)]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [End] [Sub]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The details of the Print method are tabulated below:


  Name of the method   Parameters of the method   Return type                  Descriptions
  -------------------- -------------------------- ---------------------------- ----------------------------------------------------------------------------------
  Print                NA                         [NA]   [This method is used to print Schedule in the server-side]


[] 

You can use this method as shown in the code snippets below:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\[C#\]]                                                                                                                                                    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [    [protected] [void] Print_click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                 |
| [    {]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| [        Schedule1.Print();]                                                                                                                                |
|                                                                                                                                                                                                 |
| [    }]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [\[VB\]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [    [Protected] [Sub] Print_click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                    |
| [        Schedule1.Print()]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| [    [End] [Sub]]                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

**ScheduleAfterPrint**

 

This server-side print event is triggered after the print is complete. This event is mainly used to change the appearance of the schedule after print.

The table below gives you the details of this event:

 


+--------------------+----------------------+--------------------------------------+-------------+----------------+
| Event              | Description          | Arguments                            | Type        | Reference link |
+--------------------+----------------------+--------------------------------------+-------------+----------------+
| ScheduleAfterPrint | Handled After Print. | EventArgs[] | Server-Side | NA             |
|                    |                      |                                      |             |                |
|                    |                      |                                      |             |                |
+--------------------+----------------------+--------------------------------------+-------------+----------------+


 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [\[C#\]]                                                                                                                                                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [    [void] Schedule1_ScheduleAfterPrint([object] sender, [ScheduleAfterPrintEventArgs] e)] |
|                                                                                                                                                                                                   |
| [    {]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| [        [this].Schedule1.CalendarPosition = [ScheduleCalendarPosition].Left;]                                   |
|                                                                                                                                                                                                   |
| [        [this].Schedule1.Height = 500;]                                                                                                 |
|                                                                                                                                                                                                   |
| [    }]                                                                                                                                                       |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                 |
| [\[VB\]]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [Protected] [Sub] Schedule1_ScheduleAfterPrint([ByVal] sender [As] [Object], [ByVal] e [As] [ScheduleAfterPrintEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        [Me].Schedule1.CalendarPosition = [ScheduleCalendarPosition].Left]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        [Me].Schedule1.Height = 500]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [End] [Sub]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The details of the Print method are tabulated in the description of **SchedulePrintClicked** event.[]

 

ScheduleClicked Event

[] 

This is a server-side event that is handled on a Schedule cell click.

 

The event handler receives an argument of type[ ]**ScheduleClickEventArgs**[ ]containing data related to this event. The following ScheduleClickEventArgs[ ]members provide information specific to this event.

[] 


  ---------- --------------------------------------------------
  Member     Description
  Date       Gets the date for which the event is called.
  Resource   Gets the resource for which the event is called.
  ---------- --------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnResourceIndexChanged] [=\"Schedule1_ResourceIndexChanged\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [protected][ [void] Schedule1_ScheduleClicked([object] sender, ScheduleClickEventArgs e)] |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [   [// Gets the date for which the event is called and adds the specified number of minutes to the to the value of this instance.]]                           |
|                                                                                                                                                                                                                          |
| [   this][.EndTime.Value = e.Date.AddMinutes(30);]                                                                                  |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [Protected][ [Sub] Schedule1_ScheduleClicked([ByVal] sender [As] [Object], [ByVal] e [As] ScheduleClickEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [\' Gets the date for which the event is called and adds the specified number of minutes to the to the value of this instance.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                       |
| [Me][.EndTime.Value = e.Date.AddMinutes(30)]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

StartDateChanged Event

[] 

This is a server-side event that is handled when the start date is changed.

 

The event handler receives an argument of type[ ]**StartDateChangedEventArgs**[ ]containing data related to this event. The following StartDateChangedEventArgs[ ]member provides information specific to this event.

[] 


+-----------------------------------+-----------------------------------+
|                                   |                                   |
|                                   |                                   |
| Member                            | Description                       |
+-----------------------------------+-----------------------------------+
| OldStartDate                      | Gets the Schedule old start date. |
+-----------------------------------+-----------------------------------+


\
In the below example, the previous and the current start dates are displayed.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnStartDateChanged] [=\"Schedule1_StartDateChanged\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [protected][ [void] Schedule1_StartDateChanged([object] sender, [StartDateChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [    [// Gets the previous and current start dates.]]                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [    Text1.Text = e.OldStartDate + [\"is changed to\"] + Schedule1.StartDate;]                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [Protected [Sub] Schedule1_StartDateChanged([ByVal] sender [As] Object, [ByVal] e [As] StartDateChangedEventArgs)] |
|                                                                                                                                                                                                                                                                 |
| [\' Gets the previous and current start dates.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [Text1.Text = e.OldStartDate & [\"is changed to\"] & Schedule1.StartDate]                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RenderingAppointment Event

[] 

This is a server-side event that is handled while an appointment is rendering.

 

The event handler receives an argument of type **RenderingAppointmentsEventArgs** containing data related to this event. The following RenderingAppointmentsEventArgs members provide information specific to this event.

[] 


  ------------- -----------------------------------------------------------------------------
  Member        Description
  Appointment   Gets or sets the rendering appointment.
  Handled       Boolean value that specifies whether to allow rendering appointment or not.
  ------------- -----------------------------------------------------------------------------


[] 

In the below example, the subject of the rendering appointment is displayed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnRenderingAppointment][=\"Schedule1_RenderingAppointment\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\"] [\....]]                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [protected][ [void] Schedule1_RenderingAppointment([object] sender, StartDateChangedEventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [// Get the details of the rendering appointment.]                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [Textbox1.Text=e.Appointment.Subject;]                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [e.Handled = [true];]                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [Protected][ [Sub] Schedule1_StartDateChanged([ByVal] sender [As] [Object], [ByVal] e [As] StartDateChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                           |
| [Textbox1.Text = e.Appointment.Subject]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                           |
| [e.Handled = [True]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ScheduleMenuItemClick Event

[] 

This is a server-side event that is handled when a Schedule menu item is clicked.

[] 

The event handler receives an argument of type **ScheduleMenuItemEventArgs** containing data related to this event. The following ScheduleMenuItemEventArgs member provides information specific to this event.

[] 


  ------------- ------------------------------------------------------------------------------------
  Member        Description
  Appointment   Gets or sets the appointment at the point where the schedule menu item is clicked.
  CommandName   Name of the menu item clicked.
  ------------- ------------------------------------------------------------------------------------


[] 

In the below example, the previous and the current start dates are displayed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][cc1][:][Schedule][ [ID][=\"Schedule1\"] [OnRenderingAppointment][=\"Schedule1_ScheduleMenuItemClick\"] [runat][=\"server\"] [Height][=\"400\"] [Width][=\"600\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [MinDate][=\"2007-01-16\"][ [MaxDate][=\"2007-01-18\"] [AutoFormat] [=\"Office2007Blue\" ][ShowContextMenu][=\"True\"] [\....]]                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: The ShowContextMenu property should be set to True in order to display the menu on the Schedule control.


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [protected][ [void] Schedule1_ScheduleMenuItemClick([object] sender, StartDateChangedEventArgs e)] |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [if][ (e.CommandName == [\"Edit\"])]                                                                                  |
|                                                                                                                                                                                                                                   |
| [e.Appointment.Subject = [\"New subject of the appointment\"];]                                                                                                        |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [Protected][ [Sub] Schedule1_ScheduleMenuItemClick([ByVal] sender [As] [Object], [ByVal] e [As] StartDateChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                |
| [    [If] e.CommandName = [\"Edit\"] [Then]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                |
| [        e.Appointment.Subject = [\"New subject of the appointment\"]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                |
| [    [End] [If]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

