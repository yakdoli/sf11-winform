---
title: settingsthedays1.md
original_path: WinForms_Docs/99_Uncategorized/settingsthedays1.md
created_at: 2025-08-05
---






#### Settings the Days {#settings-the-days style="tab-stops: 0pt"}

It is possible to hide the days of the next month and the previous month in the calendar, to enhance the appearance of the Calendar. This is done by disabling the ShowNextMonthDays and ShowPreviousMonthDays properties.

 

For setting these properties, use the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<!\--][ Adding calendar with next month day and previous month day Set to false ][\--\>]                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][ShowNextMonthDays][=]\"[False]\"[ ][ShowPreviousMonthDays][=]\"[False]\"[/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                    |
|                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]          |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [//Hide the next month days]                                        |
|                                                                                                                       |
| [calendarEdit.ShowNextMonthDays = [false];]                  |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Hide the previous month days]                                    |
|                                                                                                                       |
| [calendarEdit.ShowPreviousMonthDays = [false]; ]             |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 69: ShowNextMonthDays = \"False\"; ShowPreviousMonthDays = \"False\"

 

[]{#p39} 

[]{#related-topics}

