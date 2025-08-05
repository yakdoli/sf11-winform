---
title: abbreviatingnames.md
original_path: WinForms_Docs/99_Uncategorized/abbreviatingnames.md
created_at: 2025-08-05
---








  









### Abbreviating Names {#abbreviating-names style="tab-stops: 0pt"}

This section provides information about how to abbreviate day and month names. It has the following topics:

[]{#p55}Abbreviating Day Names

By default, the day names are displayed in an abbreviated form in the CalendarEdit control. They can also be displayed in an expanded form by setting **IsDayNameAbbreviated** property to false. This indicates whether the name of day is abbreviated or expanded. It returns the bool value.

To set this property, use the below code:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<!\--][ Adding calendar with day name expanded][\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][Width][=]\"[400]\"[ ][IsDayNamesAbbreviated][=]\"[False]\"[/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| []                                                                                |
|                                                                                                                       |
| [//Disable the DayNameAbbreviated]                                  |
|                                                                                                                       |
| [calendarEdit.IsDayNamesAbbreviated = [false]; ]             |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 83: IsDayNamesAbbreviated = \"False\"

 

[]{#p56}Abbreviating Month Names

By default, the MonthNames are displayed in an expanded form in the CalendarEdit control. They can also be displayed in an abbreviated form by setting **IsMonthNamesAbbreviated** property to ***true***. This dependency property indicates whether the name of month is abbreviated or expanded. It returns a bool value.

To set the IsMonthNamesAbbreviated property, use the following code.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<!\--][ Adding calendar with month name been abbreviated ][\--\>]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][IsMonthNameAbbreviated][=]\"[True]\"[/\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                                    |
|                                                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]                          |
|                                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                                       |
| [//Disable the DayNameAbbreviated]                                                  |
|                                                                                                                                                       |
| [calendarEdit.IsMonthNameAbbreviated = [true];]                              |
|                                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                                       |
| [//Adding CalendarEdit as window content]                                           |
|                                                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 84: IsMonthNameAbbreviated = \"True\"

 

[]{#p57} 

[]{#related-topics}

