---
title: axisrangeandintervals1.md
original_path: WinForms_Docs/99_Uncategorized/axisrangeandintervals1.md
created_at: 2025-08-05
---








  









### Axis Range and Intervals {#axis-range-and-intervals style="tab-stops: 0pt"}

 

Automatic Range Calculation

The range and intervals for an axis are automatically calculated by the built-in \"nice range calculation engine\", by default. This engine takes the raw data series and converts it to a readable range of numbers in which it will be represented. For example, if the data series has points between the range 1.2 to 3.7, then the engine will create a scale of 0 to 5 for the axis with ten intervals of 0.5 each.

This default behavior is controlled by the ChartAxis.RangeType property, which is set to Auto by default.

 

Specifying Custom Ranges

Sometimes the automatic range generation might not be suitable for you, in which case you can specify a custom range on the axis. You should start by setting the ChartAxis.RangeType property to Set. Then use one of the following properties to specify a custom range:

 


+--------------------+----------------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------+
| ChartAxis Property | Applies to RangeType | Applies to ValueType (Depenencies) | Description                                                                                                             | Property Type                                                     | Value it Accepts             |
|                    |                      |                                    |                                                                                                                         |                                                                   |                              |
|                    | (Dependencies)       |                                    |                                                                                                                         |                                                                   |                              |
+--------------------+----------------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------+
| Range              | Set                  | Double                             | Specifies the minimum, maximum, and interval for the axis. Use this if the data points are of the double type.          | MinMaxInfo                                                        | A MinMaxInfo object.         |
+--------------------+----------------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------+
| DateTimeRange      | Set                  | DateTime                           | Specifies the start and end dates and interval time for the axis. Use this if the data points are of the datetime type. | [ChartDateTimeRange] | A ChartDateTimeRange object. |
+--------------------+----------------------+------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------+


Axis Range and Intervals by using any chart can be created through two ways:

[·      ]Builder

[·      ]ChartModel

 

More:







