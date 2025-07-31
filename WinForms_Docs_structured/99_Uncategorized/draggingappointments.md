---
title: draggingappointments.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\draggingappointments.md
created_at: 2025-07-03
---








  









### Dragging Appointments {#dragging-appointments style="tab-stops: 0pt"}

[] 

Appointments can be dragged between various resources and set for different time intervals. To perform the drag action, the **AllowAppointmentDrag** property must be set to **True**.

 

If you press ESC key before dropping an appointment, all the changes will be canceled, and the appointment will return to its initial position. In grouped view, where different resources are represented by different columns, dragging an appointment to another column automatically changes the associated resource.

[] 


  ---------------------- ------------------------------------------------------------------------------------------------
  Appointment Property   Description
  AllowAppointmentDrag   Gets / sets a value indicating whether appointments in the Schedule are allowed to be dragged.
  ---------------------- ------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][Syncfusion][:][schedule][ [id][=\"Schedule1\"] [runat][=\"server\"] [AllowAppointmentDrag][=\"True\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][Syncfusion][:][schedule][\>]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                     |
| []                                                              |
|                                                                                                     |
| [Schedule1.AllowAppointmentDrag = [true];] |
+-----------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                              |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [Private][ Schedule1.AllowAppointmentDrag = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

Figure 69[]

[] 

A sample which demonstrates the above feature is available in the below sample installation path.

[] 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\<Version Number\>\\Web\\Schedule.Web\\Samples\\2.0\\Scheduler-AdvancedFeatures\\ DragDropOptions

 

[]{#related-topics}

