---
title: directionformonthnavigation1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\directionformonthnavigation1.md
created_at: 2025-07-03
---






#### Direction for Month Navigation {#direction-for-month-navigation style="tab-stops: 0pt"}

In the CalendarEdit control, the direction of month navigation is horizontal by default. You can also change this direction to vertical by setting the **MonthChangeDirection** property to **Vertical**. This dependency property sets the month change direction. Following are the two month change directions.

[·      ]**Vertical**: Enables navigating through the months vertically

[·      ]**Horizontal**: Enables navigating through the months horizontally

 

For setting the MonthChangeDirection property, use the following code.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<!\--][ Adding calendar with month change direction as vertical ][\--\>]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][MonthChangeDirection][=]\"[Vertical]\"[/\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

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
| [//Month change direction as vertical]                              |
|                                                                                                                       |
| [calendarEdit.MonthChangeDirection = AnimationDirection.Vertical;]                |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

