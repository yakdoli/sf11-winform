---
title: customizingaddeditappointmentwindow.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizingaddeditappointmentwindow.md
created_at: 2025-07-03
---








  









### Customizing Add/Edit Appointment Window {#customizing-addedit-appointment-window style="tab-stops: 0pt"}

[] 

The Add/Edit Appointment window can be customized using templates. This feature is used to change the look and feel of Appointment window and also include additional fields to make the application user friendly.

[] 

Properties

[] 

The following table lists more information on the property available.

[] 


  ----------------------------------- ------------------ --------------------------------------------------------------------
  Name of the Property                Value it accepts   Description
  CustomizeAddEditAppointmentWindow   Boolean            Specifies whether the Appointment window can be customized or not.
  ----------------------------------- ------------------ --------------------------------------------------------------------


[] 

The following code snippet illustrates the usage of the property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion][:][Schedule][ [ClientObjectId][=\"\_sfScheduler\"] [ClientSideOnScheduleClick][=\"fun1(this)\"]]                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [ID][=\"Schedule1\"] [CustomizeAddEditAppointmentWindow][=\"true\"] [runat][=\"server\"] [Width][=\"965px\"]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [Height][=\"500px\"] [VisibleDays][=\"2\"] [ShowContextMenu][=\"true\"] [StartDate][=\"2007-04-21\"]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [AutoFormat][=\"Office2007Blue\"] [ScheduleType][=\"day\"] [ViewStrip][=\"true\"] [autopostbackonschedulecellclick][=\"true\"\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][AppointmentAddEditTemplate][\>]]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [ [\<][table][\>]]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                        [\<][tr][\>]]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                            [\<][td] [style][=\"][padding-left]: [15px]; [padding-top]: [50px\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                [\<][asp][:][Label] [ID][=\"Label1\"] [runat][=\"server\"] [Text][=\"Description\"\>\</][asp][:][Label][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                            [\</][td][\>]]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                            [\<][td] [style][=\"][padding-left]: [15px]; [padding-top]: [50px\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                [\<][input] [type][=\"text\"] [id][=\"Subject\"] [style][=\"][height]: [70px]; [width]: [500px];[\"] [/\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                            [\</][td][\>]]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                        [\</][tr][\>]]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][table][\>]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][AppointmentAddEditTemplate][\>]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][syncfusion][:][Schedule][\>]                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [this][.Schedule2.CustomizeAddEditAppointmentWindow = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                      |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [Me][.Schedule2.CustomizeAddEditAppointmentWindow = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the code. The following output is displayed.

[] 

{border="0"}[]

Figure 67: Add/Edit Appointment Window

[]{#p48} 

[]{#related-topics}

