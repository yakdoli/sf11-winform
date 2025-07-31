---
title: changeanappointment.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\changeanappointment.md
created_at: 2025-07-03
---








  









### [Change an Appointment] {#change-an-appointment style="LINE-HEIGHT: 150%; MARGIN-TOP: 0pt; tab-stops: 0pt"}

Essential Schedule provides two ways to change an existing appointment at run time.

1.   Using AppointmentDoubleClick Event

2.   Using Context Menu

The Appointment dialog that opens on double-clicking an appointment or selecting menuitem (Open Appointment) from context menu with existing appointment details, provides options to change the subject, location, start time and end time, and description and so on.

[] 

**[]** 

**[]** 

Properties

Table 8: Change an Appointment - Properties

**[]** 


+------------------+---------------------------------------------------------+----------------------+---------------------------------------------------+-------------+
| Property         | Description                                             | Type of the property | Value it accepts                                  | Dependency  |
+==================+=========================================================+======================+===================================================+=============+
| AllowEdit        | Used to set enable/disable update appointment.          | Boolean              | [True/False]              | NA          |
|                  |                                                         |                      |                                                   |             |
|                  |                                                         |                      |                                                   |             |
+------------------+---------------------------------------------------------+----------------------+---------------------------------------------------+-------------+
| ContextMenuItems | Used to add context-menu item for updating appointment. | List                 | [List\<ContextMenuItem\>] |             |
|                  |                                                         |                      |                                                   |             |
|                  |                                                         |                      |                                                   |             |
+------------------+---------------------------------------------------------+----------------------+---------------------------------------------------+-------------+


 

More:





