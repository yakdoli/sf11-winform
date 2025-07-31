---
title: navigationcalendar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\navigationcalendar.md
created_at: 2025-07-03
---








  









### Navigation Calendar {#navigation-calendar style="tab-stops: 0pt"}

[] 

A GridControl-derived object that displays multiple calendars lets you select particular dates or data ranges to be displayed in the ScheduleControl.

[] 

Properties

[] 


  ----------------- --------------------------------------------------------------------------
  Name              Description
  CalendarGrid      Gets the grid control that is used to display the calendars.
  DateValue         Gets / sets the date value for the navigation calendar.
  SelectedDates     Gets the dates selected in the navigation calendar.
  ShowWeekNumbers   Indicates whether the week numbers should be displayed in the calendars.
  Today             Gets / sets the DateTime value for the current day.
  ----------------- --------------------------------------------------------------------------


[] 

[] 

Methods

[] 


  ------------------ -----------------------------------------------------------------------
  Name               Description
  FirstDayOfMonth    Returns the date of the first day of the month of the passed-in date.
  MondayBeforeDate   Returns the Monday before the given date.
  SundayAfterDate    Returns the Sunday after the given date.
  ------------------ -----------------------------------------------------------------------


[] 

[] 

Event

[] 


  ------------------ ---------------------------------------------------------------
  Name               Description
  DateValueChanged   Occurs when NavigationCalendar.DateValue property is changed.
  ------------------ ---------------------------------------------------------------


 

[]{#p26} 

[]{#related-topics}

