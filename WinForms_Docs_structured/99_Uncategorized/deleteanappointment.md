---
title: deleteanappointment.md
original_path: WinForms_Docs/99_Uncategorized/deleteanappointment.md
created_at: 2025-08-05
---








  









### [Delete an Appointment] {#delete-an-appointment style="LINE-HEIGHT: 150%; MARGIN-TOP: 0pt; tab-stops: 0pt"}

Essential Schedule provides two ways to delete an appointment at run time.

1.   Using AppointmentDoubleClick Event

2.   Using Context Menu[]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                           |
|                                                                                                                                                                                           |
| [    [\<%][=]Html.Syncfusion().Schedule()([\"DeleteAppointment\"])] |
|                                                                                                                                                                                           |
| [        .DataSource(Model)]                                                                                                                 |
|                                                                                                                                                                                           |
| [        .Skins([ScheduleSkins].Sandune)]                                                                            |
|                                                                                                                                                                                           |
| [        .BindList(columns =\>]                                                                                                              |
|                                                                                                                                                                                           |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                           |
| [           columns.IdField([\"AppId\"]);]                                                                           |
|                                                                                                                                                                                           |
| [           columns.SubjectField([\"Subject\"]);]                                                                    |
|                                                                                                                                                                                           |
| [           columns.LocationField([\"Location\"]);]                                                                  |
|                                                                                                                                                                                           |
| [           columns.StartTimeField([\"StartTime\"]);]                                                                |
|                                                                                                                                                                                           |
| [           columns.EndTimeField([\"EndTime\"]);]                                                                    |
|                                                                                                                                                                                           |
| [           columns.DescriptionField([\"Descrip\"]);]                                                                |
|                                                                                                                                                                                           |
| [           columns.OwnerField([\"Resource\"]);]                                                                     |
|                                                                                                                                                                                           |
| [        })]                                                                                                                                 |
|                                                                                                                                                                                           |
| [    [%\>]]                                                                                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                     |
|                                                                                                                                                                       |
| [    [@(] Html.Syncfusion().Schedule()([\"DeleteAppointment\"])] |
|                                                                                                                                                                       |
| [        .DataSource(Model)]                                                                                         |
|                                                                                                                                                                       |
| [        .Skins([ScheduleSkins].Sandune)]                                                    |
|                                                                                                                                                                       |
| [        .BindList(columns =\>]                                                                                      |
|                                                                                                                                                                       |
| [        {]                                                                                                          |
|                                                                                                                                                                       |
| [           columns.IdField([\"AppId\"]);]                                                   |
|                                                                                                                                                                       |
| [           columns.SubjectField([\"Subject\"]);]                                            |
|                                                                                                                                                                       |
| [           columns.LocationField([\"Location\"]);]                                          |
|                                                                                                                                                                       |
| [           columns.StartTimeField([\"StartTime\"]);]                                        |
|                                                                                                                                                                       |
| [           columns.EndTimeField([\"EndTime\"]);]                                            |
|                                                                                                                                                                       |
| [           columns.DescriptionField([\"Descrip\"]);]                                        |
|                                                                                                                                                                       |
| [           columns.OwnerField([\"Resource\"]);]                                             |
|                                                                                                                                                                       |
| [        })[)]]                                                                          |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| []                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

The Appointment dialog opens on double-clicking an appointment or selecting menuitem (Delete Appointment) from context menu to delete an appointment.

[] 

Properties

Table 9: Delete an Appointment - Properties

**[]** 


+------------------+-------------------------------------------------------------+----------------------+---------------------------------------------------+-------------+
| Property         | Description                                                 | Type of the property | Value it accepts                                  | Dependency  |
+==================+=============================================================+======================+===================================================+=============+
| AllowDelete      | Used to set enable/disable delete appointment.              | Boolean              | [True/False]              | NA          |
|                  |                                                             |                      |                                                   |             |
|                  |                                                             |                      |                                                   |             |
+------------------+-------------------------------------------------------------+----------------------+---------------------------------------------------+-------------+
| ContextMenuItems | Used to add context-menu item for deleting an  appointment. | List                 | [List\<ContextMenuItem\>] | NA          |
|                  |                                                             |                      |                                                   |             |
|                  |                                                             |                      |                                                   |             |
+------------------+-------------------------------------------------------------+----------------------+---------------------------------------------------+-------------+


 

More:





