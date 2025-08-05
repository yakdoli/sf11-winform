---
title: customizingappointmentsusingtemplates.md
original_path: WinForms_Docs/99_Uncategorized/customizingappointmentsusingtemplates.md
created_at: 2025-08-05
---








  









### Customizing Appointments Using Templates {#customizing-appointments-using-templates style="tab-stops: 0pt"}

 

Schedule control provides an option to customize the appointments. The appointments can be customized using Appointment Template. This feature is used to change the look and feel of the appointment and also include additional fields to make the application user friendly.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[ASPX\]]**[] |
|                                                                                                                                                         |
| [\<appointmenttemplate\>]                                                                                           |
|                                                                                                                                                         |
| [            \<div\>]                                                                                               |
|                                                                                                                                                         |
| [                    From]                                                                                          |
|                                                                                                                                                         |
| [                    [\<%]\# Container.StartTime [%\>]]     |
|                                                                                                                                                         |
| [                    till]                                                                                          |
|                                                                                                                                                         |
| [                    [\<%]\# Container.EndTime [%\>]]       |
|                                                                                                                                                         |
| [                    Subject:]                                                                                      |
|                                                                                                                                                         |
| [                    [\<%]\# Container.Subject [%\>]]       |
|                                                                                                                                                         |
| [            \</div\>]                                                                                              |
|                                                                                                                                                         |
| [\</appointmenttemplate\>]                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 81: Schedule with Customized Appointment

[] 

More:





