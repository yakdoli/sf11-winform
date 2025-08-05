---
title: selectingthedateandyearatruntime.md
original_path: WinForms_Docs/99_Uncategorized/selectingthedateandyearatruntime.md
created_at: 2025-08-05
---






#### Selecting the Date and Year at Run Time {#selecting-the-date-and-year-at-run-time style="tab-stops: 0pt"}

Selecting Date at Run Time

By setting the **AllowSelection** property to ***true***, you can enable user selection in CalendarEdit control at run time.[ ]This dependency property indicates whether the date selection is allowed during runtime. It returns a bool value indicating the state of this property.

 

For setting the AllowSelection property, use the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\--][ Adding calendar with allow selection of a date ][\--\>]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][AllowSelection][=]\"[True]\"[/\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| **[]**                                                              |
|                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                    |
|                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]          |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Allow selection of a date]                                       |
|                                                                                                                       |
| [calendarEdit.AllowSelection = [true];]                      |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding calendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

Figure 66: AllowSelection = \"True\"

[] 

Selecting Year at Run Time

By setting the **IsAllowYearSelection** property to ***true***, you can edit the year at run time. This is dependency property indicates whether the year can be edited at run time. It returns the bool value that indicates the state of this property.

 

To set the IsAllowYearSelection property, use the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<!\--][ Setting IsAllowYearSelection property][\--\>]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][IsAllowYearSelection][=]\"[True]\"[/\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [//Allow selection of year]                                         |
|                                                                                                                       |
| [calendarEdit.IsAllowYearSelection = [true];]                |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

Figure 67: IsAllowYearSelection = \"True\"

[] 

See Also[]

[]

 

[]{#related-topics}

