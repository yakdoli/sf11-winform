---
title: selectionbordercolor.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectionbordercolor.md
created_at: 2025-07-03
---






#### Selection Border Color {#selection-border-color style="tab-stops: 0pt"}

Whenever a selection is made in the Calendar, the selected day grid will be associated with a border. The color of this selection border of the day grid can be customized using the **SelectionBorderBrush** property. This dependency property sets the brush value for the selection border brush of the day grid.

 

To set the SelectionBorderBrush property, use the below code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<!\--][ Adding calendar with selection border brush ][\--\>]                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[ ][SelectionBorderBrush][=]\"[Aqua]\"[/\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| []                                                                                                |
|                                                                                                                                                       |
| [//Setting the brush for the Selection day grid]                                    |
|                                                                                                                                                       |
| [calendarEdit.SelectionBorderBrush = Brushes.Aqua;    ]                                           |
|                                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                                       |
| [//Adding CalendarEdit as window content]                                           |
|                                                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 86: SelectionBorderBrush = \"Aqua\"

 

[]{#p62} 

[]{#related-topics}

