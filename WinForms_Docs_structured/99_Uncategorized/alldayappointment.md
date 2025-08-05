---
title: alldayappointment.md
original_path: WinForms_Docs/99_Uncategorized/alldayappointment.md
created_at: 2025-08-05
---








  









### AllDay Appointment {#allday-appointment style="tab-stops: 0pt"}

[] 

Appointments which extend for an entire day are termed as \"AllDay Appointments\".

[] 

{border="0"}[]

Figure 52[]

[] 

To set an appointment as an AllDay appointment, the **AllDay** property (in the ScheduleWebAppointment Collection Editor) for that appointment must be set to **True**.

[] 


+-----------------------------------+--------------------------------------------------------------------+
|                                   |                                                                    |
|                                   |                                                                    |
| Appointment Property              | Description                                                        |
+-----------------------------------+--------------------------------------------------------------------+
| AllDay                            | Specifies whether to mark an appointment as an allday appointment. |
+-----------------------------------+--------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [AllDay][=\"true\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][syncfusion][:][Schedule][\>]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------+
| **[\[C#\]]**                                 |
|                                                                                  |
| []                                           |
|                                                                                  |
| [app1.AllDay = [true];] |
+----------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                           |
|                                                                                                                                            |
| []                                                                                                     |
|                                                                                                                                            |
| [Private ][app1.AllDay = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Unlike the normal appointments, allday appointments will be displayed on the header below the resource text. Also, they can be displayed with different row styles using the **AllDayAppointmentRowStyle** property.

 

The **AllDayAppointmentRowVisible** property can be used to show / hide the allday appointments.

[] 


+-----------------------------------+--------------------------------------------------------------------+
|                                   |                                                                    |
|                                   |                                                                    |
| Schedule Property                 | Description                                                        |
+-----------------------------------+--------------------------------------------------------------------+
| AllDayAppointmentRowStyle         | Specifies styles for the allday appointment\'s rows.               |
+-----------------------------------+--------------------------------------------------------------------+
| AllDayAppointmentRowVisible       | Specifies whether a row containing allday appointments is visible. |
|                                   |                                                                    |
|                                   |                                                                    |
|                                   |                                                                    |
|                                   | The default value is set to True.                                  |
+-----------------------------------+--------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                |
| [Schedule1.AllDayAppointmentRowStyle.BackColor = System.Drawing.[Color].NavajoWhite;] |
|                                                                                                                                                |
| [Schedule1.AllDayAppointmentRowStyle.ForeColor = System.Drawing.[Color].Orange;]      |
|                                                                                                                                                |
| [Schedule1.AllDayAppointmentRowStyle.Font.Name = [\"TimesNewRoman\"];]              |
|                                                                                                                                                |
| [Schedule1.AllDayAppointmentRowStyle.Font.Size = 12;]                                                      |
|                                                                                                                                                |
| [Schedule1.AllDayAppointmentRowStyle.Font.Bold = [true];]                             |
|                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                |
| [Schedule1.AllDayAppointmentRowVisible = [true];]                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Private ][Schedule1.AllDayAppointmentRowStyle.BackColor = System.Drawing.Color.NavajoWhite]            |
|                                                                                                                                                                                              |
| [Private ][Schedule1.AllDayAppointmentRowStyle.ForeColor = System.Drawing.Color.Orange]                 |
|                                                                                                                                                                                              |
| [Private ][Schedule1.AllDayAppointmentRowStyle.Font.Name = [\"TimesNewRoman\"]] |
|                                                                                                                                                                                              |
| [Private ][Schedule1.AllDayAppointmentRowStyle.Font.Size = 12]                                          |
|                                                                                                                                                                                              |
| [Private ][Schedule1.AllDayAppointmentRowStyle.Font.Bold = [True]]                 |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [Private ][Schedule1.AllDayAppointmentRowVisible = [True]]                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

[] 

Figure 53: AllDayAppointmentRowVisible = \"True\" and AllDayAppointmentRowStyle - BackColor = \"NavajoWhite\"; ForeColor = Orange; FontName = \"TimesNewRoman\"; FontSize = \"12\"; FontBold = \"True\"

[]{#p36} 

[]{#related-topics}

