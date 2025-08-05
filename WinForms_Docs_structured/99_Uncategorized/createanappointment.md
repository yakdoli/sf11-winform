---
title: createanappointment.md
original_path: WinForms_Docs/99_Uncategorized/createanappointment.md
created_at: 2025-08-05
---








  









### Create an Appointment {#create-an-appointment style="tab-stops: 0pt"}

Essential Schedule provides two ways to create a new appointment at run time. They are:

1.   Using CellDoubleClick Event and

2.   Using Context Menu

[] 

The Appointment dialog which opens on double-clicking the Schedule cells or selecting the menu item (New Appointment) from the Context menu, is used in creating a new appointment.It  provides options to set the subject, location, start and end time, and description. The auto format of the Appointment dialog will be automatically changed based on the auto format of the Schedule control.

[] 

Properties

Table 7: Create an Appointment -- Properties

**[]** 


+------------------+----------------------------------------------------------------+----------------------+---------------------------------------------------+-------------+
| Property         | Description                                                    | Type of the property | Value it accepts                                  | Dependency  |
+==================+================================================================+======================+===================================================+=============+
| AllowAddNew      | Used to set enable/disable for creating a  new appointment.    | Boolean              | [True/False]              | NA          |
|                  |                                                                |                      |                                                   |             |
|                  |                                                                |                      |                                                   |             |
+------------------+----------------------------------------------------------------+----------------------+---------------------------------------------------+-------------+
| ContextMenuItems | Used to add context-menu item for creating a  new appointment. | List                 | [List\<ContextMenuItem\>] | NA          |
|                  |                                                                |                      |                                                   |             |
|                  |                                                                |                      | []                        |             |
+------------------+----------------------------------------------------------------+----------------------+---------------------------------------------------+-------------+


 

More:





