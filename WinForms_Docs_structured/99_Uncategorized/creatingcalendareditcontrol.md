---
title: creatingcalendareditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingcalendareditcontrol.md
created_at: 2025-07-03
---








  









### Creating CalendarEdit Control {#creating-calendaredit-control style="tab-stops: 0pt"}

There are two possible ways to create a simple CalendarEdit control.

1\. Through Designer

 

[To create the CalendarEdit control through designer, follow the below steps:]

1.   Drag the CalendarEdit control from the toolbox onto the design area.

2.   Set the properties for the CalendarEdit in design mode, by using the Smart Tag feature.

[] 

{border="0"}

Figure 63: Dragging CalendarEdit from the Toolbox

[] 

2\. Programmatically

To create the CalendarEdit control through code, use the following XAML or C# code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<!\--][ Adding CalendarEdit control ][\--\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion:CalendarEdit][ ][Name][=][\"[calendarEdit]\"[/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| []                                                                   |
|                                                                                                                       |
| [//Creating an instance of CalendarEdit control]                    |
|                                                                                                                       |
| [CalendarEdit calendarEdit = [new] CalendarEdit();]          |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [//Adding CalendarEdit as window content]                           |
|                                                                                                                       |
| [this][.Content = calendarEdit;] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 64: CalendarEdit Control

 

[]{#related-topics}

