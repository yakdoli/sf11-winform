---
title: byusingappointmentsproperty.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\byusingappointmentsproperty.md
created_at: 2025-07-03
---








  









### By Using Appointments Property {#by-using-appointments-property style="tab-stops: 0pt"}

You can add appointments directly to the Schedule control, by using the following code.

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][schedule][:][Schedule.Appointments][\>]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][schedule][:][ScheduleAppointmentCollection][\>]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\<][schedule][:][ScheduleAppointment][ ]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ StartTime][=\"1/18/2010 12:00:00 AM\"][ EndTime][=\"1/18/2010 8:00:00 AM\"][ ]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ Subject][=\"Meet the doc\"][ Location][=\"Hutchison road\"][ AllDay][=\"False\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\<][schedule][:][ScheduleAppointment][ ]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ StartTime][=\"1/19/2010 12:00:00 AM\"][ EndTime][=\"1/19/2010 4:00:00 AM\"]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ Subject][=\"Going to Park\"][ Location][=\"Park road\"][ AllDay][=\"False\"/\>]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\<][schedule][:][ScheduleAppointment]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ StartTime][=\"1/20/2010 12:00:00 AM\"][ EndTime][=\"1/20/2010 6:00:00 AM\"][ ]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ Subject][=\"Visit to Mary\'s house\"][ Location][=\"Hutchison road\"][ ]                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            AllDay][=\"False\"/\>]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\<][schedule][:][ScheduleAppointment]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ StartTime][=\"1/21/2010 12:00:00 AM\"][ EndTime][=\"1/21/2010 4:00:00 AM\"][ ]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][ Subject][=\"Meeting with William\"][ Location][=\"Park road \"][ ]                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            AllDay][=\"False\"/\>]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\</][schedule][:][ScheduleAppointmentCollection][\>]                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][schedule][:][Schedule.Appointments][\>]                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

