---
title: selectionrange.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectionrange.md
created_at: 2025-07-03
---






#### Selection Range {#selection-range style="tab-stops: 0pt"}

You can set the selection range mode for CalendarEdit control in two different ways, using the **SelectionRangeMode** property. They are as follows.

[·      ]**CurrentMonth**: selects only days, belonging to the current month from the column

[·      ]**WholeColumn**: selects the whole column

 

For setting the selection range mode, use the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<!\--][ Adding CalendarEdit with selection range mode ][\--\>]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][SelectionRangeMode][=]\"[WholeColumn]\"[/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [//Sets selection range mode as whole column]                       |
|                                                                                                                       |
| [calendarEdit.SelectionRangeMode = SelectionRangeMode.WholeColumn;  ]             |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

 

[]{#p34} 

[]{#related-topics}

