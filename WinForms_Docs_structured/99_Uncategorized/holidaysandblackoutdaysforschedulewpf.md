---
title: holidaysandblackoutdaysforschedulewpf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\holidaysandblackoutdaysforschedulewpf.md
created_at: 2025-07-03
---








  









### Holidays and Blackout Days for Schedule WPF {#holidays-and-blackout-days-for-schedule-wpf style="tab-stops: 0pt"}

Holidays and blackout days for Schedule WPF enable you to add holidays as all-day appointments, reminding you when the next holiday occurs.

Creating Holidays & Blackout Days for the Schedule Control

Add holidays to the schedule control by using the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][schedule][:][Schedule.Holidays][ \>]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [    ][\<][schedule][:][ScheduleHolidaysCollection][\>]                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [      ][\<][schedule][:][ScheduleHolidays][ ]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][StartTime][=\"1/1/2010 12:00:00 AM\"][ EndTime][=\"1/1/2010 8:00:00 AM\"][ ]      |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][Subject][=\"New Year Day\"][ Location][=\"Hutchison road\" /\>]                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [      ][\<][schedule][:][ScheduleHolidays][ ]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][StartTime][=\"12/31/2009 12:00:00 AM\"][ EndTime][=\"12/31/2009 4:00:00 AM\"][ ]  |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][Subject][=\"New Year Evening\"][ Location][=\"Park road\" /\>]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [      ][\<][schedule][:][ScheduleHolidays][ ]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][StartTime][=\"12/25/2009 12:00:00 AM\"][ EndTime][=\"12/25/2009 6:00:00 AM\"][ ]  |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][Subject][=\"Christmas Day\"][ Location][=\"Hutchison road\" /\>]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [      ][\<][schedule][:][ScheduleHolidays][ ]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][StartTime][=\"12/24/2009 12:00:00 AM\"][ EndTime][=\"12/26/2009 4:00:00 AM\"][  ] |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [         ][Subject][=\"Christmas Evening\"][ Location][=\"Park road \" /\>]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [       ][\</][schedule][:][ScheduleHolidaysCollection][\>]                              |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][schedule][:][Schedule.Holidays][\>]                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

{border="0"}

Figure 20: Holidays As Appointment

[]{#p18} 

[]{#related-topics}

