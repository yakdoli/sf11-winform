---
title: viewstriptoolbar1.md
original_path: WinForms_Docs/99_Uncategorized/viewstriptoolbar1.md
created_at: 2025-08-05
---








  









## ViewStrip Toolbar {#viewstrip-toolbar style="tab-stops: 0pt"}

The ViewStrip toolbar provides options to view the day, workweek, week, and month schedule. It also provides options to move the Schedule to 'today's date' and print a schedule.

[] 

[·      ]Day: This view displays the most detailed view of appointments for a single day

[·      ]Workweek: This view displays the appointments for the working days in a particular week

[·      ]Week: This view displays the appointments for all the days in a week

[·      ]Month: This view displays the appointments for the entire month

[·      ]Today: Displays the present day's appointments

[·      ]Print: Prints a schedule

[] 

[] 

Properties

Table 6: ViewStrip Toolbar - Properties

**[]** 


+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| Property                                                                                         | Description                       | Type of the property | Value it accepts                                    | Dependency  |
+==================================================================================================+===================================+======================+=====================================================+=============+
| *[CurrentView]*      | Used to set the active view type. | Enum                 | [ScheduleViewMode].Day      | NA          |
|                                                                                                  |                                   |                      |                                                     |             |
|                                                                                                  |                                   |                      | [ScheduleViewMode].Week     |             |
|                                                                                                  |                                   |                      |                                                     |             |
|                                                                                                  |                                   |                      | [ScheduleViewMode].WorkWeek |             |
|                                                                                                  |                                   |                      |                                                     |             |
|                                                                                                  |                                   |                      | [ScheduleViewMode].Month    |             |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| *[ShowDayView]*      | Used to enable the Day view.      | Boolean              | [True/false]                | NA          |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| *[ShowWeekView]*     | Used to enable the Week view.     | Boolean              | [True/false]                | NA          |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| *[ShowWorkWeekView]* | Used to enable the Workweek view. | Boolean              | [True/false]                | NA          |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| *[ShowMonthView]*    | Used to enable the Month view.    | Boolean              | [True/false]                | NA          |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| *[ShowTodayView]*    | Used to enable the Today view.    | Boolean              | [True/false]                | NA          |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+
| *[ShowPrint]*        | Used to enable the Print icon.    | Boolean              | [True/false]                | NA          |
+--------------------------------------------------------------------------------------------------+-----------------------------------+----------------------+-----------------------------------------------------+-------------+


 

More:





