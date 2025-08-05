---
title: clientsidefunctionalities.md
original_path: WinForms_Docs/99_Uncategorized/clientsidefunctionalities.md
created_at: 2025-08-05
---








  









### Client Side Functionalities {#client-side-functionalities style="tab-stops: 0pt"}

The Client-side mouse events support for web chart allows easy interaction with the chart control in client side.

The client-side mouse events are used to get information from the chart region to customize the chart. []

**Events**


  ------------------------------------------------------ ------------------------------------------------------------------------------------------------------ -------------------------------------- --------------------------------------------
  Event                                                  Description[]                                                                 Arguments[]   Reference links[]
  ClientSideOnMouseClick[]      Specifies the client side function to call, when chart is clicked.                                     args                                   NA
  ClientSideOnMouseDblClick[]   Specifies the client side function to call, when chart is double clicked.[]   args[]        NA[]
  ClientSideOnMouseDown[]       Specifies the client side function to call, when mouse down on chart.[]       args[]        NA[]
  ClientSideOnMouseMove[]       Specifies the client side function to call, when mouse move on chart.[]       args[]        NA[]
   ClientSideOnMouseUp[]        Specifies the client side function to call, when mouse up on chart.[]         args[]        NA[]
  ------------------------------------------------------ ------------------------------------------------------------------------------------------------------ -------------------------------------- --------------------------------------------


[] 

You can handle these client-side events as shown in the following code snippets:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][ChartWebControl][ [ID][=\"ChartWebControl1\"] [runat][=\"server\"] [ClientSideOnMouseClick] [=\"OnMouseClick\"] [ClientSideOnMouseDblClick] [=\"OnMouseDblClick\"] [ClientSideOnMouseDown] [=\"OnMouseDown\"] [ClientSideOnMouseMove] [=\"OnMouseMove\"] [ClientSideOnMouseUp] [=\"OnMouseUp\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][syncfusion][:][ChartWebControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

For JavaScript, define the handlers:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\] ]**[]                                                                                                        |
|                                                                                                                                                                                                        |
| [\<[script] [type]=\"text/javascript\"\>]                                                                               |
|                                                                                                                                                                                                        |
| [function][ ][OnMouseDown][ (args) {]     |
|                                                                                                                                                                                                        |
| [//args:][]                                                                                                  |
|                                                                                                                                                                                                        |
| [//RegionIndex- Specifies the index of this region]                                                                                                  |
|                                                                                                                                                                                                        |
| [//SeriesIndex-Specifies the type of region.]                                                                                                        |
|                                                                                                                                                                                                        |
| [//PointIndex-Specifies the point index of region.    ]                                                                                              |
|                                                                                                                                                                                                        |
| [//IsChartPoint-Indicates whether the region is a Chart Point in the ChartSeries.  ]                                                                 |
|                                                                                                                                                                                                        |
| [//ToolTip-Specifies the series name for this region.]                                                                                               |
|                                                                                                                                                                                                        |
| [//Type-Specifies the type of region. ][]                                                                        |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [function][ ][OnMouseUp][ (args) {]       |
|                                                                                                                                                                                                        |
| [//args:][]                                                                                                  |
|                                                                                                                                                                                                        |
| [//RegionIndex- Specifies the index of this region]                                                                                                  |
|                                                                                                                                                                                                        |
| [//SeriesIndex-Specifies the type of region.]                                                                                                        |
|                                                                                                                                                                                                        |
| [//PointIndex-Specifies the point index of region.    ]                                                                                              |
|                                                                                                                                                                                                        |
| [//IsChartPoint-Indicates whether the region is a Chart Point in the ChartSeries.  ]                                                                 |
|                                                                                                                                                                                                        |
| [//ToolTip-Specifies the series name for this region.]                                                                                               |
|                                                                                                                                                                                                        |
| [//Type-Specifies the type of region. ][]                                                                        |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [function][ ][OnMouseDblClick][ (args) {] |
|                                                                                                                                                                                                        |
| [//args:][]                                                                                                  |
|                                                                                                                                                                                                        |
| [//RegionIndex- Specifies the index of this region]                                                                                                  |
|                                                                                                                                                                                                        |
| [//SeriesIndex-Specifies the type of region.]                                                                                                        |
|                                                                                                                                                                                                        |
| [//PointIndex-Specifies the point index of region.    ]                                                                                              |
|                                                                                                                                                                                                        |
| [//IsChartPoint-Indicates whether the region is a Chart Point in the ChartSeries.  ]                                                                 |
|                                                                                                                                                                                                        |
| [//ToolTip-Specifies the series name for this region.]                                                                                               |
|                                                                                                                                                                                                        |
| [//Type-Specifies the type of region. ][]                                                                        |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [function][ ][OnMouseMove][ (args) {]     |
|                                                                                                                                                                                                        |
| [ //args:][]                                                                                                 |
|                                                                                                                                                                                                        |
| [//RegionIndex- Specifies the index of this region]                                                                                                  |
|                                                                                                                                                                                                        |
| [//SeriesIndex-Specifies the type of region.]                                                                                                        |
|                                                                                                                                                                                                        |
| [//PointIndex-Specifies the point index of region.    ]                                                                                              |
|                                                                                                                                                                                                        |
| [//IsChartPoint-Indicates whether the region is a Chart Point in the ChartSeries.  ]                                                                 |
|                                                                                                                                                                                                        |
| [//ToolTip-Specifies the series name for this region.]                                                                                               |
|                                                                                                                                                                                                        |
| [//Type-Specifies the type of region. ][]                                                                        |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [function][ ][OnMouseClick][ (args) {]    |
|                                                                                                                                                                                                        |
| [//args:][]                                                                                                  |
|                                                                                                                                                                                                        |
| [//RegionIndex- Specifies the index of this region]                                                                                                  |
|                                                                                                                                                                                                        |
| [//SeriesIndex-Specifies the type of region.]                                                                                                        |
|                                                                                                                                                                                                        |
| [//PointIndex-Specifies the point index of region.    ]                                                                                              |
|                                                                                                                                                                                                        |
| [//IsChartPoint-Indicates whether the region is a Chart Point in the ChartSeries.  ]                                                                 |
|                                                                                                                                                                                                        |
| [//ToolTip-Specifies the series name for this region.]                                                                                               |
|                                                                                                                                                                                                        |
| [//Type-Specifies the type of region. ][]                                                                        |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [][]                                                                                                              |
|                                                                                                                                                                                                        |
| [\</[script]\> ]                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following properties are enabled when the CalcRegions property is enabled, and they become the arguments for the above mentioned client-side events:


+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| ChartRegion Property | Description                                                                                                                      | Type of Property | Value it accepts                                                                                       | Dependencies                                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| RegionIndex          | A index of this region.                                                                                                          | int              | Any integer                                                                                            | CalcRegions property---enabled when the CalcRegions property is true. |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Type                 | Specifies the type of region.                                                                                                    | ChartRegionType  | Possible values:                                                                                       | CalcRegions property---enabled when the CalcRegions property is true. |
|                      |                                                                                                                                  |                  |                                                                                                        |                                                                       |
|                      |                                                                                                                                  |                  | [·      ]SeriesPoint - interacts on a data point.                         |                                                                       |
|                      |                                                                                                                                  |                  |                                                                                                        |                                                                       |
|                      |                                                                                                                                  |                  | [·      ]HorAxisLabel - interacts on a horizontal axis                    |                                                                       |
|                      |                                                                                                                                  |                  |                                                                                                        |                                                                       |
|                      |                                                                                                                                  |                  | [·      ]VerAxisLabel - interacts on a vertical axis                      |                                                                       |
|                      |                                                                                                                                  |                  |                                                                                                        |                                                                       |
|                      |                                                                                                                                  |                  | [·      ]ChartCustom - interacts with a region that is none of the above. |                                                                       |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| IsChartPoint         | Indicates whether the region is a Chart Point in the ChartSeries. This simply checks if the above mentioned Type is SeriesPoint. | bool             | [·      ]True                                                             | CalcRegions property---enabled when the CalcRegions property is true. |
|                      |                                                                                                                                  |                  |                                                                                                        |                                                                       |
|                      |                                                                                                                                  |                  | [·      ]False                                                            |                                                                       |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| SeriesIndex          | The index into the Series array of the Chart in which this point occurs. If the Type is SeriesPoint.                             | Int              | Any integer                                                                                            | CalcRegions property---enabled when the CalcRegions property is true. |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| PointIndex           | The index into the Points array of the ChartSeries in which this point occurs. If the Type is SeriesPoint.                       | Int              | Any integer                                                                                            | CalcRegions property---enabled when the CalcRegions property is true. |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| ToolTip              | Specifies the tooltip for this region.                                                                                           | String           | Any string                                                                                             | CalcRegions property---enabled when the CalcRegions property is true. |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+


[] 


Note: The CalcRegions property must be set to true for the Events to work.


 

[]{#related-topics}

