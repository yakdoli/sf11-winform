---
title: axisrangeandintervals2.md
original_path: WinForms_Docs/99_Uncategorized/axisrangeandintervals2.md
created_at: 2025-08-05
---








  









### Axis Range and Intervals {#axis-range-and-intervals style="tab-stops: 0pt"}

 

Automatic Range Calculation

 

The range and intervals for an axis are automatically calculated by the built-in \"nice range calculation engine\", by default. This engine takes a raw data series and comes up with a nice human readable range of numbers in which to represent them. For example, if the data series contains points in the range 1.2 - 3.7, the engine would come up with a scale of 0 - 5 for the axis with 10 intervals of 0.5 each.

 

This default behavior is controlled by the **ChartAxis.RangeType** property which is set to **Auto** by default.

 

Specifying Custom Ranges

 

Sometimes the automatic range generation might not be good enough for you, in which case you can specify a custom range on the axis. You should start by setting the **ChartAxis.RangeType** property to **Set**. Then use one of the following properties to specify a custom range.

 


  -------------------- ---------------------- ---------------------- ---------------------------------------------------------------------------------------------------------------------
  ChartAxis Property   Applies to RangeType   Applies to ValueType   Description
  Range                Set                    Double                 Specifies the minimum, maximum and interval for the axis. Use this if the data points are of double type.
  DateTimeRange        Set                    DateTime               Specifies the start and end dates and interval time for the axis. Use this if the data points are of datetime type.
  -------------------- ---------------------- ---------------------- ---------------------------------------------------------------------------------------------------------------------


 

Here is some sample code that shows how this is done.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| [// Customize the X axis range and interval which has points of type DateTime]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryXAxis.ValueType = [ChartValueType].DateTime;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryXAxis.DateTimeRange = [new] [ChartDateTimeRange](baseDate.AddMonths(-1), baseDate.AddMonths(6), 1, [ChartDateTimeIntervalType].Months);] |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [// Customize the Y axis range and interval which has points of type double]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryYAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryYAxis.Range = [new] [MinMaxInfo](1, 20, 2);]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [// Customize the Y axis range and interval which has points of type double]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [this][.chartControl1.PrimaryXAxis.Range = [new] [MinMaxInfo](0, 6, 1);]                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [\' Customize the X axis range and interval which has points of type DateTime]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryXAxis.RangeType = [ChartAxisRangeType.Set]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryXAxis.ValueType = [ChartValueType.DateTime]]                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryXAxis.DateTimeRange = [New] [ChartDateTimeRange(baseDate.AddMonths(-1), baseDate.AddMonths(6), 1, ChartDateTimeIntervalType.Months)]] |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [\' Customize the Y axis range and interval which has points of type double]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryYAxis.RangeType = [ChartAxisRangeType.Set]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryYAxis.Range = [New] [MinMaxInfo(1, 20, 2)]]                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [\' Customize the x axis range and interval which has points of type double]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set]                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.PrimaryXAxis.Range = [New] [MinMaxInfo](0, 6, 1)]                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You can however tweak the ranges and intervals that get generated through these properties.

 

Changing Intervals

 

Use these properties to customize the intervals that get generated:

 


  -------------------- ---------------------- ---------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ChartAxis Property   Applies to RangeType   Applies to ValueType   Description
  DesiredIntervals     Auto                   Double, DateTime       A request for the nice-range calculation engine to come up with a nice range with so many intervals. The engine will only use this setting as a guidance. Default value is 6.
  IntervalType         Auto                   DateTime               Specifies whether the interval that gets calculated should be in Years, Months, Weeks, Days, Hours, Minutes, Seconds or Milliseconds. This setting is used only if the **ValueType** of the axis is set to **DateTime**. Default value is **Auto**.
  -------------------- ---------------------- ---------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

Changing Origin

 

Use these properties to customize the origin of the axes:

 


+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             |                      |                      |                                                                                                                                                                                                                                                                                                      |
|                             |                      |                      |                                                                                                                                                                                                                                                                                                      |
| ChartAxis Property          | Applies to RangeType | Applies to ValueType | Description                                                                                                                                                                                                                                                                                          |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PreferZero                  | Auto                 | Double               | Indicates whether one boundary of the calculated range should be tweaked to zero. Such tweaking will happen only if zero is within a reasonable distance from the calculated boundary. To ensure that one boundary is always zero, use the \"ForceZero\" setting instead. Default value is **true**. |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ForceZero                   | Auto                 | Double               | Indicates whether one boundary of the calculated range should always be tweaked to zero. Default value is **true**.                                                                                                                                                                                  |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CustomOrigin                | Auto and Set         | Double, DateTime     | Lets you use the properties Origin and OriginDate below. Default value is **false**.                                                                                                                                                                                                                 |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Origin                      | Auto and Set         | Double               | Lets you specify a custom origin (double value) for the axis. Use this property when the data points are of double type. The interval and range will then be calculated automatically. Remember to set CustomOrigin to **true**. Default value is **0**.**0**.                                       |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OriginDate                  | Auto and Set         | DateTime             | Lets you specify a custom origin (double value) for the axis. Use this property when the data points are of double type. The interval and range will then be calculated automatically. Remember to set CustomOrigin to **true**. Default value is **DateTime.MinValue**.                             |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Offset                      | Auto and Set         | Double and DateTime  | Specifies the offset that should be applied to the automatically calculated start of the range.                                                                                                                                                                                                      |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OffsetDateTime              | Auto                 | DateTime             | Specifies the offset that should be applied to the automatically calculated start of the range.                                                                                                                                                                                                      |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DateTimeInterval.Offset     | Set                  | DateTime             | Use this instead of Offset if you want to specify the OffsetType (see below).                                                                                                                                                                                                                        |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DateTimeInterval.OffsetType | Set                  | DateTime             | Specifies the type of offset specified above. Could be Auto, Years, Months, Weeks, Days, Hours, Minutes, Seconds or Milliseconds.                                                                                                                                                                    |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RangePaddingType            | Auto                 | Double and DateTime  | Specifies if there should be any padding applied between the points and the axes, before and after the datapoints.                                                                                                                                                                                   |
+-----------------------------+----------------------+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[]{#p179} 

 

[]{#related-topics}

