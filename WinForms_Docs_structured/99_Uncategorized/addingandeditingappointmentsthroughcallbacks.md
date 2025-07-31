---
title: addingandeditingappointmentsthroughcallbacks.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingandeditingappointmentsthroughcallbacks.md
created_at: 2025-07-03
---








  









### Adding and Editing Appointments through Callbacks {#adding-and-editing-appointments-through-callbacks style="tab-stops: 0pt"}

[] 

This section discusses how appointments can be directly added and edited in the Schedule control through callbacks.

[] 

Adding Appointments

[] 

Appointments can be added through callbacks by double-clicking on the Schedule cells at run time. The **Add Appointment** dialog box that opens on double-clicking the Schedule cells, provides options to set the subject, start time and end time. Also, an appointment can be set as an \"allday\" appointment by checking the \'All Day\' check box provided. Now it is also possible to add recurring appointments through callbacks. The auto format of the Add pop-up window will be automatically changed based on the auto format of the Schedule control.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                      |
|                                   |                                                                                                                                      |
| Schedule Property                 | Description                                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| AllowAddingAppointByCallBack      | Gets or sets the value that indicates whether adding appointments through callbacks should be allowed. Default value is set to True. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][Syncfusion][:][schedule][ [id][=\"Schedule1\"] [runat][=\"server\"] [AllowAddingAppointByCallBack][=\"True\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][Syncfusion][:][schedule][\>]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                             |
| []                                                                      |
|                                                                                                             |
| [Schedule1.AllowAddingAppointByCallBack = [true];] |
+-------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                      |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [Private ][Schedule1.AllowAddingAppointByCallBack = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

Figure 63[]

Editing Appointments

[] 

Schedule control provides two ways to edit an appointment.

[] 

[·      ]Using Context Menu

[·      ]Using AppointmentClicked Event

[] 

**[]** 

Using Context Menu

[] 

Essential Schedule provides support for editing an appointment on clicking the **Edit Appointment** menu item in the context menu. The Edit Appointment pop-up window contains all the details of the appointment. After making changes to an appointment, click the **Update** button in the pop-up window to reflect the changes made to the appointment. The auto format of the Edit Appointment pop-up window will be automatically changed based on the auto format of the Schedule control. To show the context menu on the Schedule control, you must set the **ShowContextMenu** property to **True**.

[] 

{border="0"}[]

Figure 64[]

[] 

Select **Edit Appointment** from the context menu in order to open the Edit Appointment pop-up window. The Edit Appointment pop-up window will be displayed as shown below.

[] 

{border="0"}[]

[] 

Figure 65[]

Using AppointmentClicked Event

[] 

On clicking an appointment, the AppointmentClicked event is handled on the server-side, which allows to edit the appointment. The arguments of the AppointmentClicked event return all the details of the appointment to the server-side. Here you can override the values as per your needs. To know more about the AppointmentClicked event, see [AppointmentClicked Event]{.UGHyperlink}.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [Schedule1.AppointmentClicked += [new] Schedule.AppointmentClickedEventHandler(Schedule1_AppointmentClicked);]                                            |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [void][ Schedule1_AppointmentClicked([object] sender, AppointmentEventArgs e)]                           |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [e.Appointment.Subject = [\"This is Edited Appointment\"];]                                                                                             |
|                                                                                                                                                                                                                    |
| [e.Appointment.LocationValue = [\"Enter the text\"];]                                                                                                   |
|                                                                                                                                                                                                                    |
| [e.Appointment.StartTime = [DateTime].Now;]                                                                                                               |
|                                                                                                                                                                                                                    |
| [e.Appointment.EndTime = [DateTime].Now.AddHours(2);]                                                                                                     |
|                                                                                                                                                                                                                    |
| [e.Appointment.AllDay = [true];]                                                                                                                          |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [Protected][ [Sub] Scheduler1_AppointmentClicked([ByVal] sender [As] [Object], [ByVal] e [As] AppointmentEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [e.Appointment.Subject = [\"This is Edited Appointment\"]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [e.Appointment.LocationValue = [\"Enter the text\"]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [e.Appointment.StartTime = DateTime.Now]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [e.Appointment.EndTime = DateTime.Now.AddHours(2)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [e.Appointment.AllDay = [True]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

**[]** 

Figure 66: Editing an Appointment using the AppointmentClicked Event

[] 

A sample which demonstrates the Editing feature is available in the below sample installation path.

[] 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\<Version Number\>\\Web\\Schedule.Web\\Samples\\2.0\\Scheduler-Localization\\Localization

[] 

See Also

[] 

Edit or Delete Appointment

[]{#p47}[] 

[]{#related-topics}

