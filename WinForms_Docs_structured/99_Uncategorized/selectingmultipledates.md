---
title: selectingmultipledates.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectingmultipledates.md
created_at: 2025-07-03
---






#### Selecting Multiple Dates {#selecting-multiple-dates style="tab-stops: 0pt"}

CalendarEdit control allows the user to select multiple dates, by setting the **AllowMultiplySelection** property to ***true***. The following code snippet illustrates this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<!\--][ Adding CalendarEdit with multiple selection feature][\--\>]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][AllowMultiplySelection][=]\"[True]\"[/\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [//Allow multiple selection of date]                                |
|                                                                                                                       |
| [calendarEdit.AllowMultiplySelection = [true]; ]             |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 65: AllowMultiplySelection = \"True\"

**[]** 

See Also

[]

 

[]{#related-topics}

