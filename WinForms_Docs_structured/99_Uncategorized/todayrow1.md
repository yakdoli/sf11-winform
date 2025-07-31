---
title: todayrow1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\todayrow1.md
created_at: 2025-07-03
---






#### Today Row {#today-row style="tab-stops: 0pt"}

To know the details of current date in a CalendarEdit control, you need to enable Today Row. Set the **TodayRowIsVisible** property to ***true*** to display today\'s details. This dependency property indicates whether the today bar is visible or collapsed.

 

For setting this property, use the below code snippet.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<!\--][ Adding Calendar with today row ][\--\>]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][TodayRowIsVisible][=]\"[True]\"[/\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| []                                                                  |
|                                                                                                                       |
| [//Enable the today row]                                            |
|                                                                                                                       |
| [calendarEdit.TodayRowIsVisible = [true]; ]                  |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 70: TodayRowIsVisible = \"True\"

 

 

[]{#related-topics}

