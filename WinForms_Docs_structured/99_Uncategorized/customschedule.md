---
title: customschedule.md
original_path: WinForms_Docs/99_Uncategorized/customschedule.md
created_at: 2025-08-05
---








  









## Custom Schedule {#custom-schedule style="tab-stops: 0pt"}

Essential Gantt provides the custom schedule support that allows you to define your own schedule for Gantt to track the progress of projects. You can define the schedule for any measurement unit or for different types of date time formats such as quarterly basis scale and so on, with this feature.

This feature will get information from users and draw the Gantt schedule with the obtained information. Custom schedule has been split into two types namely:

 

[·      ]Custom Numeric

[·      ]Custom DateTime

These types are included in the existing SchduleType enum.

 

Custom Numeric:

Custom Numeric schedule is to define your own schedule with any numeric measurement unit other than date time. With this schedule, you can track the progress of your projects based on your own measurement, and need not depend on Date Time. Two new API's are added to the Mapping attributes in order to support this schedule in GanttChart and GanttGrid.

 

Custom DateTime:

Custom DateTime schedule is to define your own date time schedule, which can match your current financial calendar. In case you need the schedule on quarterly basis, then you can use this schedule type to define the custom schedule.

In both the custom schedules, Gantt will get the information from the application to render the schedule. Gantt will accept the custom schedule information in the form of a collection of "GanttScheduleRowInfo" objects, and process it to draw the schedule.

 

GanttScheduleRowInfo class will have following fields:

**PixelsPerUnit** -- Gets the information about the pixel value equivalent to one unit in custom measurement.

 

**CellsPerUnit** -- Gets the information about a cell size of the preceding row in the schedule based on the immediate next row. In CustomDateTime Schedule, CellsPerUnit will be used to customize the cell. For example, in quarterly basis month cell, you need to draw a cell by consolidating three months. For this, you need to define the CellsPerUnit of that corresponding row as 3.

 

**TimeUnit** -- Gets the information about the type of row, when the schedule type is CustomDateTime. The Time unit can be any one of the following:

 

[·      ]Days -- represents the corresponding row as day's row

[·      ]Weeks -- represents the corresponding row as week's row

[·      ]Months -- represents the corresponding row as month's row

[·      ]Years -- represents the corresponding row as year's row

[**[]**]{.apple-style-span} 

Use Case Scenarios

[[This will be useful when users like to define their schedules with their own measurements or calendars.]]{.apple-style-span}

**Example 1:** Research organizations may follow different measurements to track their work progress. The measurements will depend on their products. In such a scenario, they can use CustomNumeric schedule to define schedules with their own measures.

 

**Example 2:** A very big construction project many have the time period of many years or months and so they need some customized way of date time schedule to track their progress. In this scenario, they can use the CustomDateTime schedule to customize their schedule.  The schedule can have the time scale on quarterly basis to track their progress.

[**[]**]{.apple-style-span} 

[Properties]{.apple-style-span}

Table 1: Properties Table


  ---------------------- ------------------------------------------------------ -------------------- -------------------------------
  Property               Description                                            Type                 Data Type
  CustomScheduleSource   Gets/Sets the custom schedule items Source of Gantt.   DependencyProperty   IList\<GanttScheduleRowInfo\>
  ---------------------- ------------------------------------------------------ -------------------- -------------------------------


[**[]**]{.apple-style-span} 

[Events]{.apple-style-span}

Table: ScheduleCellCrated Event Table


+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------+
| Event               | Description                                                                                                                                                  | Arguments                                                             | Type            |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------+
| ScheduleCellCreated | Whenever a schedule cell is created, this event is triggered. The handler of the event will have the newly created cell (GanttScheduleCell) in the argument. | ScheduleCellCreated(object sender, ScheduleCellCreatedEventArgs args) | Routed Event    |
|                     |                                                                                                                                                              |                                                                       |                 |
|                     | By handling this event, users can customize the appearance of the cell.                                                                                      |                                                                       |                 |
+=====================+==============================================================================================================================================================+=======================================================================+=================+


[[]]{.apple-style-span} 

GanttScheduleCell Class

The properties of the GanttScheduleCell class are as tabulated:

[**[]**]{.apple-style-span} 


+-----------------+------------------------------------------------------------------------------+---------------------+-----------------+
| Property        | Description                                                                  | Type                | Data Type       |
+-----------------+------------------------------------------------------------------------------+---------------------+-----------------+
| CellDate        | Gets/Sets the current schedule cell date in the datetime schedule.           | Dependency Property | DateTime        |
+-----------------+------------------------------------------------------------------------------+---------------------+-----------------+
|                 | Gets/Sets the current schedule cell tool tip.                                | Dependency Property | Object          |
|                 |                                                                              |                     |                 |
| CellToolTip     |                                                                              |                     |                 |
+-----------------+------------------------------------------------------------------------------+---------------------+-----------------+
| CellTimeUnit    | Gets/Sets the current schedule row time unit (like weeks, months and so on). | Dependency Property | TimeUnit (Enum) |
+-----------------+------------------------------------------------------------------------------+---------------------+-----------------+
| Content         | Gets/Sets the current schedule cell content                                  | Dependency Property | Object          |
+-----------------+------------------------------------------------------------------------------+---------------------+-----------------+


 

Adding Custom Schedule to an Application

To add CustomNumeric Schedule to an application:

1.   Define the Mapping for StartPointMapping and FinishPointMapping in TaskAttributeMapping.

2.   Set the Gantt Schedule type as CustomNumeric.

3.   Bind the GanttScheduleRowInfo collection to the **CustomScheduleSource** property of Gantt.

The following code illustrates this:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   ][ \<][sync][:][GanttControl][ Grid.Row][=\"1\"][ [ScheduleType][=\"CustomNumeric\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [              [ x][:][Name][=\"Gantt\"][ VisualStyle][=\"Office2010Black\"\>]]                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                ][\<][sync][:][GanttControl.TaskAttributeMapping][\>][]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                    ][\<][sync][:][TaskAttributeMapping][ ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ TaskIdMapping][=\"Id\"]                                            ]                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ TaskNameMapping][=\"Name\"]                                        ]                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ StartPointMapping][=\"Start\"]                                               ]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ FinishPointMapping][=\"End\"]                                            ]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ ChildMapping][=\"ChildTask\"]                                                ]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ ProgressMapping][=\"Complete\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                       [ ResourceInfoMapping][=\"Resource\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                    ][\</][sync][:][TaskAttributeMapping][\>][]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                ][\</][sync][:][GanttControl.TaskAttributeMapping][\>]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [  ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [   // Assigning the custom schedule Items Source]**[]**                                                                 |
|                                                                                                                                                                                                                                          |
| [   this][.Gantt.CustomScheduleSource = [this].GetInfo();   ]                                        |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [   [///][ Gets the Numeric Schedule Items Info]        ]                                                                                    |
|                                                                                                                                                                                                                                          |
| [   [private] [ObservableCollection]\<[GanttScheduleRowInfo]\> GetInfo()]                                          |
|                                                                                                                                                                                                                                          |
| [   {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [       [// Creating a new collection]]                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [       [ObservableCollection]\<[GanttScheduleRowInfo]\> RowInfo = [new]]                                          |
|                                                                                                                                                                                                                                          |
| [                                         ObservableCollection][\<[GanttScheduleRowInfo]\>();] |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [       [// Defining the top most row of the schedule ]]                                                                                                          |
|                                                                                                                                                                                                                                          |
| [       RowInfo.Add([new] [GanttScheduleRowInfo]() { CellsPerUnit = 3 });]                                                                 |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [       [// Defining the consecutive rows of the schedule]]                                                                                                       |
|                                                                                                                                                                                                                                          |
| [       RowInfo.Add([new] [GanttScheduleRowInfo]() { CellsPerUnit = 2 });]                                                                 |
|                                                                                                                                                                                                                                          |
| [       RowInfo.Add([new] [GanttScheduleRowInfo]() { CellsPerUnit = 5 });]                                                                 |
|                                                                                                                                                                                                                                          |
| [       ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [       [// Defining the bottom most row of the schedule]]                                                                                                        |
|                                                                                                                                                                                                                                          |
| [       [// Here we are setting the cell width in pixels]]                                                                                                        |
|                                                                                                                                                                                                                                          |
| [       RowInfo.Add([new] [GanttScheduleRowInfo]() { PixelsPerUnit = 30d });]                                                              |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [       [return] RowInfo;]                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| [   }   ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 28

**[]** 

Samples

To view samples:

1.   Select **Start** -\> **Programs** -\> **Syncfusion** -\> **Essential Studio x.x.xx** -\> **Dashboard**.

2.   Click[[ ]]{.apple-converted-space}**Run Samples**[[ ]]{.apple-converted-space}for WPF under **User Interface Edition** panel.

3.   Select[[ ]]{.apple-converted-space}**Gantt**.

4.   Expand the **Custom Schedule** item in the **Sample Browser**.

5.   Choose the **Custom Numeric Schedule** sample to launch.

[] 

Adding CustomDateTime Schedule to an Application

To add CustomDateTime Schedule to an application:

1.   Define the **Gantt Schedule** type as **CustomDateTime**.

2.   Bind the **GanttScheduleRowInfo** collection to the **CustomScheduleSource** property of the Gantt.

The following code illustrates this:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [   ][ \<][sync][:][GanttControl][ Grid.Row][=\"1\"][ ]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                x][:][Name][=\"Gantt\"][ ScheduleType][=\"CustomDateTime\"][ [                                                                                                              ]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                VisualStyle][=\"Office2010Black\"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ItemsSource][=\"{][Binding][ GanttItemSource][}\"][ ShowChartLines][=\"False\"]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [               ][ ShowNonWorkingHoursBackground][=\"False\"]                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [               ][ ToolTipTemplate][=\"{][StaticResource][ toolTipTemplate][}\"][\>]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][sync][:][GanttControl.TaskAttributeMapping][\>][]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\<][sync][:][TaskAttributeMapping][ TaskIdMapping][=\"Id\"][]                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ TaskNameMapping][=\"Name\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ StartDateMapping][=\"StDate\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ ChildMapping][=\"ChildTask\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ FinishDateMapping][=\"EndDate\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ DurationMapping][=\"Duration\"]                                            ]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ ProgressMapping][=\"Complete\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ ResourceInfoMapping][=\"Resource\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ PredecessorMapping][=\"Predecessor\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                                           [ \>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\</][sync][:][TaskAttributeMapping][\>][]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\</][sync][:][GanttControl.TaskAttributeMapping][\>][]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\</][sync][:][GanttControl][\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [   // Assigning the custom schedule Items Source.]**[]**                                                                                                          |
|                                                                                                                                                                                                                                                                                    |
| [   this][.Gantt.CustomScheduleSource = [this].GetCustomScheduleSource();  ]                                                                   |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [   // Hooks the Schedulecell created event to customize the schedule cell appearance.][]                                                                          |
|                                                                                                                                                                                                                                                                                    |
| [   this][.Gantt.ScheduleCellCreated+=[new] [GanttControl].[ScheduleCellCreatedEventHandler ]] |
|                                                                                                                                                                                                                                                                                    |
| [                                                        (Gantt_ScheduleCellCreated);           ]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| [         ]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [   [///][ Gets the Custom DateTime Schedule Items Info]        ]                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [   public][  [IList]\<[GanttScheduleRowInfo]\> GetCustomScheduleSource()]                                          |
|                                                                                                                                                                                                                                                                                    |
| [   {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [       [List]\<[GanttScheduleRowInfo]\> RowInfo = [new] [List]\<[GanttScheduleRowInfo]\>();]                |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [       [// Defining the top most row of the schedule]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [       [// Here we need the Year Schedule in this row. So we are defining the TimeUnit as years.]]                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [       RowInfo.Add([new] [GanttScheduleRowInfo]() { TimeUnit = [TimeUnit].Years, ]                                                                          |
|                                                                                                                                                                                                                                                                                    |
| [                  CellsPerUnit = 1, HorizontalAlignment = [HorizontalAlignment].Left });]                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [       [// Defining the bottom most row of the schedule]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                    |
| [       [// Here we need to display the three months in a cell. So we are defining TimeUnit in  months, and setting cells per unit to 3. ]]                                                                 |
|                                                                                                                                                                                                                                                                                    |
| [       // The bottom most row should consist information about the pixels per unit, so we define the pixels per unit as 15 (here this is a one month width).][]   |
|                                                                                                                                                                                                                                                                                    |
| [       RowInfo.Add([new] [GanttScheduleRowInfo]() { TimeUnit = [TimeUnit].Months, ]                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [                  CellsPerUnit = 3, PixelsPerUnit = 15 });]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [            [return] RowInfo;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [    ///][ Handles the Schedule cell Created Event of the Gantt][ ]                                  |
|                                                                                                                                                                                                                                                                                    |
| [    void][ Gantt_ScheduleCellCreated([object] sender, [ScheduleCellCreatedEventArgs] args)]                           |
|                                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [            [DateTime] currentDate = args.CurrentCell.CellDate;                ]                                                                                                                         |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [            [if] (args.CurrentCell.CellTimeUnit == [TimeUnit].Months)]                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [                 args.CurrentCell.Foreground = [new] [SolidColorBrush]([Colors].White);]                                                                    |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [                [// Quarter 1 dates contain months below 3as we are checking the      ]]                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [                                     cell date and changing the content of the cell.][]                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [                [if] (currentDate.Month \<= 3)]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Content = [\"Q 1\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.CellToolTip = [\"Quarter 1\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Background = [new] [SolidColorBrush]([Colors].DarkGray);]                                                              |
|                                                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [                [// Quarter 2 dates contain months between 4 - 6as we are checking the cell dates and changing the content of the cell.]]                                                                  |
|                                                                                                                                                                                                                                                                                    |
| [                [else] [if] (currentDate.Month \> 3 && currentDate.Month \<= 6)]                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Content = [\"Q 2\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.CellToolTip = [\"Quarter 2\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Background =[new ][SolidColorBrush]([Colors].LightGray);]                                                              |
|                                                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [                [// Quarter 3 dates contain months between 6 - 9as we are checking the cell date and changing the content of the cell.]]                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [                                   ][]                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [                [else] [if] (currentDate.Month \> 6 && currentDate.Month \<= 9)]                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Content = [\"Q 3\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.CellToolTip = [\"Quarter 3\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Background = [new] [SolidColorBrush]([Colors].DarkGray);]                                                              |
|                                                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [                [// Quarter 4 dates contain months between 9 - 12. So we are checking]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
| [                                   the cell date and changing the content of the cell.][]                                                                         |
|                                                                                                                                                                                                                                                                                    |
| [                [else] [if] (currentDate.Month \> 9 && currentDate.Month \<= 12)]                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [                {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Content = [\"Q 4\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.CellToolTip = [\"Quarter 4\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| [                    args.CurrentCell.Background =[new] [SolidColorBrush]([Colors].LightGray);]                                                              |
|                                                                                                                                                                                                                                                                                    |
| [                }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 29

Samples Link

To view samples:

1.   Select **Start** -\> **Programs** -\> **Syncfusion** -\> **Essential Studio x.x.xx** -\> **Dashboard**.

2.   Click[[ ]]{.apple-converted-space}**Run Samples**[[ ]]{.apple-converted-space}for Silverlight under **User Interface Edition** panel.

3.   Select[[ ]]{.apple-converted-space}**Gantt**.

4.   Expand the **Custom Schedule** item in the **Sample Browser**.

5.   Choose the **Customized Schedule Appearance** sample to launch.

 

ScheduleCellCreatedEventArgs Class

The ScheduleCellCreatedEventArgs consists of the current schedule cell in the name of "CurrentCell". It is the "GanttScheduleCell" type.

 

[]{#related-topics}

