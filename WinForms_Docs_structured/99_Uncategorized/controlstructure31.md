---
title: controlstructure31.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\controlstructure31.md
created_at: 2025-07-03
---








  









## Control Structure {#control-structure style="tab-stops: 0pt"}

[] 

The following screen shot shows the structure of the ScheduleControl.

[] 

{border="0"}

 

Figure 8: Structure of ScheduleControl

[] 

[] 

**Essential Schedule** primarily consists of a **UserControl derived class** named ***ScheduleControl***.

 This section discusses the main properties of the ScheduleControl. The data for the ScheduleControl comes from any object that implements IScheduleDataProvider. The following discussions elaborate on the concrete implementation of the IScheduleDataProvider, based on an ArrayList-derived object that serializes to a disk file.

[] 

The above screen shot shows a ScheduleControl displaying a Month view. The four marked areas are actually Control-derived objects (two Panels and two GridControls). These controls have been added to the **ScheduleControl.Controls** collection. Any of the four controls except the ScheduleGrid can be hidden through the property settings. Here is a short description of each of the 4 labeled areas:

 

**CaptionPanel**: This is a Panel that displays a caption at the top of the ScheduleControl. There are also two button objects on this panel that will navigate the Schedule forward and backward. You can hide this panel by using the ScheduleControl.Appearance.ShowCaption property. This panel is docked at the top of the ScheduleControl client area.

**[]** 

**NavigationPanel**: This is a Panel where you can place additional controls and make them appear adjacent to the ScheduleControl. This can be optionally docked to the left or right side of the ScheduleControl. You can also hide this panel. The ScheduleControl.Calendar which is a NavigationCalendar object is docked at the top of this panel. There is also a Splitter docked under the NavigationCalendar that allows you to display more or fewer calendars in the NavigationCalendar. The default setting displays two such calendars. The picture below displays three. You can easily put your own controls under the NavigationCalendar using code similar to these snippets.

[       ]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [Panel][ p = [new] [Panel]();]                                        |
|                                                                                                                                                                                                      |
| [p.BackColor = [Color].Blue;]                                                                                                               |
|                                                                                                                                                                                                      |
| [p.Dock = [DockStyle].Fill;]                                                                                                                |
|                                                                                                                                                                                                      |
| [p.BackgroundImage = [Image].FromFile([\"..\\\\..\\\\sync.png\"]);]                                                  |
|                                                                                                                                                                                                      |
| [p.BackgroundImageLayout = [ImageLayout].Tile;]                                                                                             |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [this][.ScheduleControl1.AddControlToNavigationPanel(p);][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

**NavigationCalendar**: This is a GridControl-derived object that displays multiple calendars allowing you to select the dates displayed in the ScheduleControl. The NavigationCalendar is docked at the top of the NavigationPanel. The number of calendars displayed in the NavigationCalendar is determined by its client height. Enlarging the height of the NavigationCalendar, will display more calendars. This can be facilitated by using the Splitter docked under the NavigationCalendar.

 

**ScheduleGrid**: This is a GridControl-derived object that displays the actual schedule content, i.e., the appointments for the various dates. The actual look of this GridControl is determined by the ScheduleViewType which is set by using the ScheduleControl.ScheduleType property.

 

Here is a Day view that shows a panel added under the NavigationCalendar by using the **ScheduleControl1.AddControlToNavigationPanel** code mentioned above.

You can dock any control under the NavigationCalendar by using this method.

[] 

{border="0"}

 

Figure 9: ScheduleControl Day View showing a Special Control added under the NavigationCalendar

[] 

[] 

In addition to the Month view, the ScheduleControl can also display Day, WorkWeek, Week and Custom views.

A Custom view is one where you can display up to eight individual days in the ScheduleGrid. You can easily switch views by using the**ScheduleControl.PerformSwitchToScheduleViewTypeClick** method.

Here are a series of screen shots illustrating these different views.

[] 

{border="0"}

 

Figure 10: ScheduleControl Day View

[] 

[] 

Notice in the WorkWeek view snapshot below, there is a Vacation entry at the top of 10/31/2006.

This entry is an All-Day entry which has no specific time assigned to it. It is simply associated with the particular date. For the Day, WorkWeek and Custom views, All-Day entries are displayed in a frozen row at the top of the ScheduleGrid. For Week and Month views, All-Day entries are listed with the time entries.

[] 

{border="0"}

 

Figure 11: ScheduleControl showing a WorkWeek View

[] 

Here is a Week view snapshot.

Notice in the NavigationCalendar on the left, week numbers appear on the left side of each week in the NavigationCalendar. You can optionally turn these numbers off using the **ScheduleControl.Calendar.ShowWeekNumbers** property.

[] 

{border="0"}

[] 

Figure 12: ScheduleControl showing a Week View

[] 

[] 

The snapshot below shows a ScheduleControl displaying three days. You can select any combination of up to either dates (either contiguous or not) to be displayed in this manner in a Custom view.

[] 

{border="0"}

[] 

Figure 13: ScheduleControl showing a Custom View

 

[]{#p10} 

[]{#related-topics}

