---
title: inbuiltdraganddropsupportforchartseries1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\inbuiltdraganddropsupportforchartseries1.md
created_at: 2025-07-03
---






##### Inbuilt Drag and Drop Support for Chart Series {#inbuilt-drag-and-drop-support-for-chart-series style="tab-stops: 0pt"}

Features

This feature helps the user to drag the Chart point from one location to another location within the Chart area and improves the user interaction by editing the under bound model's object at run time. This feature also maps the mouse coordinates to the coordinates of the ChartAxis and positions the data point. Hence, all the relevant properties like tooltip, series annotation, will be changed according to the new position.[]

[  ]

Use Case Scenarios

[·      ]Inbuilt Drag and Drop support for the Chart Series can be used in rescheduling the number of working days for any task assigned to employee.

[·      ]Reschedule the task start and end time using typical Gantt Chart type.

[·      ]It allows the user to modify the under bound data of segment dynamically by clicking and dragging the segment to the new position inside the Chart Area.

{border="0"}

 

Figure 250: Inbuilt Drag and Drop support[]

 

 

Tables for Properties, Methods, and Events

Properties

Table 160: Propert Table

  ---------------------- --------------------------------------------------------------------------------- --------------------- ----------- -----------------
  Property               Description                                                                       Type                  Data Type   Reference links
  AllowSegmentDragDrop   To set the Drag and Drop Support for the Chart Series[]   Dependency Property   Boolean     NA
  ---------------------- --------------------------------------------------------------------------------- --------------------- ----------- -----------------

[] 

Events

Table 161: ChartSegmentDragging Table

  Event                                            Description                                                      Arguments                                 Type                                      Reference links
  ------------------------------------------------ ---------------------------------------------------------------- ----------------------------------------- ----------------------------------------- ------------------------------
  ChartSegmentDragging[]   Triggered before dragging is started[]   ChartSegment[ ]   Routed Event[ ]   NA[]

[] 

[ ]Table 162: ChartSegmentDragged Table

  Event                                           Description                                                                           Arguments                                 Type                                      Reference links
  ----------------------------------------------- ------------------------------------------------------------------------------------- ----------------------------------------- ----------------------------------------- ------------------------------
  ChartSegmentDragged[]   Event is triggered immediately after dragging is started[ ]   ChartSegment[ ]   Routed Event[ ]   NA[]

[][] 

Table 163: ChartSegmentDropping Table

  Event                                            Description                                                         Arguments                                 Type                                      Reference links
  ------------------------------------------------ ------------------------------------------------------------------- ----------------------------------------- ----------------------------------------- ------------------------------
  ChartSegmentDropping[]   Triggered before dropping the segment[  ]   ChartSegment[ ]   Routed Event[ ]   NA[]

[] 

[ ]Table 164: ChartSegmentDropped Table

  Event                                           Description                                                                               Arguments                                 Type                                      Reference links
  ----------------------------------------------- ----------------------------------------------------------------------------------------- ----------------------------------------- ----------------------------------------- ------------------------------
  ChartSegmentDropped[]   Event is triggered immediately after the segment is dropped[. ]   ChartSegment[ ]   Routed Event[ ]   NA[]

[][] 

[][] 

Sample Link

To view sample:

1.   Open the WPF sample browser from the dashboard.

2.   Navigate to WPF Chart -\> User Interaction-\>Drag and Drop support demo[]

[] 

Adding Inbuilt Drag and Drop Support for Chart Series[ ]to an Application

**Inbuilt** Drag and Drop Support can be added to an Application using the following code snippet:

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                   |
| **[]**                                                                                                        |
|                                                                                                                                                   |
| [Chart1.Areas\[0\].AllowSegmentDragDrop = [true];][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        \<][sync][:][Chart][ x][:][Name][=\"Chart1\"\>][]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][sync][:][ChartArea][ AllowSegmentDragDrop][=\"True\"\>][                ][]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][sync][:][ChartSeries][ x][:][Name][=\"series1\"][ Type][=\"Bubble\"/\>][                              ][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\</][sync][:][ChartArea][\>][]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\</][sync][:][Chart][\>][                              ]                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[] 

[]{#related-topics}

