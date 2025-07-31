---
title: schedulecontrol1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\schedulecontrol1.md
created_at: 2025-07-03
---








  









## ScheduleControl {#schedulecontrol style="tab-stops: 0pt"}

[] 

It is a User Control that provides the basic scheduling functionality.

[] 

Properties

[] 


  ----------------- ----------------------------------------------------------------------------------------------------
  Name              Description
  Appearance        Gets / sets the ScheduleAppearance object that controls the visual aspects of the ScheduleControl.
  Calendar          Gets the navigation calendar.
  CaptionPanel      Gets the caption panel that holds the caption above the calendar.
  DataSource        Gets / sets the data source for the ScheduleControl.
  EnableAlerts      Indicates whether alerts should be raised as the appointment time approaches.
  NavigationPanel   Gets the navigation panel.
  ScheduleType      Gets / sets whether a daily, weekly or monthly schedule is displayed.
  ----------------- ----------------------------------------------------------------------------------------------------


[] 

[] 

Methods

[] 


  -------------------------------------- ----------------------------------------------------------------------------------------
  Name                                   Description
  AddControlToNavigationPanel            Adds the specified control to the navigation panel underneath the navigation calendar.
  AddSpanAppointment                     Adds a multiday span appointment to a data provider.
  PerformNewItemClick                    Displays a dialog box allowing you to add an item.
  PerformDeleteItemClick                 Displays a dialog box allowing you to delete an item.
  PerformEditItemClick                   Displays a dialog box allowing you to edit an item.
  PerformSwitchToScheduleViewTypeClick   Switches the display to the specified ScheduleView type.
  -------------------------------------- ----------------------------------------------------------------------------------------


[] 

[] 

Events

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Name                              | Description                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| ItemChanged                       | Notifies when an appointment is modified.                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| ScheduleAppointmentClick          | Occurs when an item is clicked / double-clicked.                                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
|                                   | Lets you either use a derived ScheduleGridControl or subscribe to the events on the ScheduleGridControl. |
|                                   |                                                                                                          |
| ScheduleGridCreated               |                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+


[]{#p23}[] 

[] 

More:









