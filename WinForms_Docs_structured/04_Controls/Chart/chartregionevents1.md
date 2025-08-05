---
title: chartregionevents1.md
original_path: WinForms_Docs/04_Controls/Chart/chartregionevents1.md
created_at: 2025-08-05
---








  









### Chart Region Events {#chart-region-events style="tab-stops: 0pt"}

 

The Chart handles the following mouse related events when the user interacts with the Chart using mouse, on certain specific regions in the Chart - Axis Labels, Chart Points or a custom region.

 

[·      ]ChartRegionClick Event

[·      ]ChartRegionMouseEnter Event

[·      ]ChartRegionMouseHover Event

[·      ]ChartRegionMouseMove Event

[·      ]ChartRegionMouseLeave Event

[·      ]ChartRegionMouseUp Event

[·      ]ChartRegionMouseDown Event

[·      ]ChartRegionDoubleClick Event

 

The above events are raised with a **ChartRegionMouseEventArgs** that contain the following properties.

 


  ------------------------------------ -------------------------------------------------------
  ChartRegionMouseEventArgs Property   Description
  Point                                Represents the client point where the event occurred.
  Region (Expanded below)              Returns the region associated with this event.
  Button                               Returns the right mouse button actions.
  ------------------------------------ -------------------------------------------------------


 

The **Region** property above includes several useful information about the kind of region the user is currently interacting with:

 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ChartRegion Property              | Description                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Description                       | A text description of this region.                                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Type                              | Specifies the type of region. Possible values:                                                                                   |
|                                   |                                                                                                                                  |
|                                   | [·      ]**SeriesPoint -** interacted on a data point.                                              |
|                                   |                                                                                                                                  |
|                                   | [·      ]**HorAxisLabel -** interacted on a horizontal axis                                         |
|                                   |                                                                                                                                  |
|                                   | [·      ]**VerAxisLabel -** interacted on a vertical axis                                           |
|                                   |                                                                                                                                  |
|                                   | [·      ]**ChartCustom -** interacted with a region that is none of the above.                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| IsChartPoint                      | Indicates whether the region is a Chart Point in the ChartSeries. This simply checks if the above mentioned Type is SeriesPoint. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| SeriesIndex                       | The index into the **Series** array of the Chart in which this point occurs. If the Type is SeriesPoint.                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| PointIndex                        | The index into the **Points** array of the ChartSeries in which this point occurs. If the Type is SeriesPoint.                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Region                            | The client region that represents this logical region.                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ToolTip                           | Specifies the tooltip for this region.                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+


 

ChartRegionDoubleClick and ChartRegionMouseDown Events

 

[]{#related-topics}

