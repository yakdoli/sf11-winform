---
title: holidaysandblackoutdays.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\holidaysandblackoutdays.md
created_at: 2025-07-03
---








  









### Holidays and Blackout Days {#holidays-and-blackout-days style="tab-stops: 0pt"}

The feature for holidays and blackout days in Essential Schedule enables you to add a holiday to a calendar the same way you would add an appointment.

Creating Holidays and Blackout days for the Schedule Control

You can add holidays and blackout days to the schedule control by using the Holidays property, as demonstrated in the following code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[XAML\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][schedule][:][Schedule.Holidays][ \>]                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][schedule][:][ScheduleHolidaysCollection][\>]     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [           \<][schedule][:][ScheduleHolidays][ ]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [            StartTime][=\"1/1/2010 12:00:00 AM\"][ EndTime][=\"1/1/2010 8:00:00 AM\"][ ]                                            |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [            [Subject][=\"New Year Day\"/\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [       ][\</][schedule][:][ScheduleHolidaysCollection][\>] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][schedule][:][Schedule.Holidays][\>]                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the above code runs, you should see the output in the schedule control similar to the following figure.

 

{border="0"}

 

Figure 26: Holidays

[]{#related-topics}

