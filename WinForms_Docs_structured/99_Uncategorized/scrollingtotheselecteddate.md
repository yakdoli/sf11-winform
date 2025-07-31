---
title: scrollingtotheselecteddate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollingtotheselecteddate.md
created_at: 2025-07-03
---






#### Scrolling to the Selected Date {#scrolling-to-the-selected-date style="tab-stops: 0pt"}

CalendarEdit control enables the user to navigate to a particular date in the Calendar, by using the ScrollToDate option. To enable this, set the **ScrollToDateEnabled** property to ***true***. This dependency property indicates whether to scroll to the selected date.

Here is the code snippet for setting this property.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<!\--][ Adding calendar with scroll to date as true ][\--\>]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][ScrollToDateEnabled][=]\"[True]\"[/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                    |
|                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]          |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Enable scroll to date]                                           |
|                                                                                                                       |
| [calendarEdit.ScrollToDateEnabled = [true]; ]                |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

 

[]{#p48} 

[]{#related-topics}

