---
title: calendar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\calendar.md
created_at: 2025-07-03
---








  









### Calendar {#calendar style="tab-stops: 0pt"}

[] 

When you click on a day or multiple days in the calendar, it will show the corresponding dates with appointments in the Schedule control.

 

Calendar can be placed to the left / right of the resources by using the below given property.

[] 


+-----------------------------------+--------------------------------------------------------------------------------+
|                                   |                                                                                |
|                                   |                                                                                |
| Schedule Property                 | Description                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| CalendarPosition                  | Gets / sets the position of the calendar. The options included are as follows: |
|                                   |                                                                                |
|                                   | [·      ]None                                     |
|                                   |                                                                                |
|                                   | [·      ]Left                                     |
|                                   |                                                                                |
|                                   | [·      ]Right                                    |
+-----------------------------------+--------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [CalendarPosition][=\"left\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][syncfusion][:][Schedule][ [\>]]                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                         |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [Schedule1.CalendarPosition = [ScheduleCalendarPosition].Left;] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                 |
|                                                                                                  |
| []                                                           |
|                                                                                                  |
| [Schedule1.CalendarPosition = ScheduleCalendarPosition.Left] |
+--------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Place the \"using Syncfusion.Web.UI.WebControls.Tools;\" namespace on top.


[] 

Schedule control lets you drag an appointment onto a date in the calendar, in order to move an appointment from one day to another. On drop, the control asks whether it should refresh it\'s view to show the \"dropped date\". If you choose *Yes*, it switches the view to the \"dropped date\".

[] 

{border="0"}[]

**[]** 

Figure 32: Calendar Position = \"Left\"

[] 

The number of months displayed in the calendar get varied according to the control height. Navigation buttons in the calendar will let you move to the \"next\" and \"previous\" months. The dates with appointments are highlighted in bold in order to differentiate them from the dates without appointments.

[]{#p28} 

More:





