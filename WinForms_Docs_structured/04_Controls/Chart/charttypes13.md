---
title: charttypes13.md
original_path: WinForms_Docs/04_Controls/Chart/charttypes13.md
created_at: 2025-08-05
---








  









## Chart Types {#chart-types style="tab-stops: 0pt"}

Essential Chart includes a comprehensive set of 8 basic chart types for all your business needs. Each one is highly and easily configurable with built-in support for creating stunning visual effects.

Chart types are specified on each chart series by using the **Type** property. All the chart types are required to have at least one X and one Y value. Certain chart types need more than one Y value.

The following table narrates the minimum and maximum number of series and number of Y values required by each type of chart supported by Essential Chart.


  Chart Type    Minimum Number of Series   Maximum Number of Series   Number of Y Values Required
  ------------- -------------------------- -------------------------- -----------------------------
  Area          1                          Unlimited                  1
  Column        1                          Unlimited                  1
  Combination   2                          Unlimited                  1
  Line          1                          Unlimited                  1
  Pie           1                          1                          1


[] 

Series Properties

+-------------+-------------------------------------+---------------+-----------------------+-------------+
| Name        | Description                         | Property Type | Value it accepts      | Dependency  |
+-------------+-------------------------------------+---------------+-----------------------+-------------+
| Type        | Gets or sets the chart series type. | SeriesType    | SeriesType.Line       | NA          |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.Spline     |             |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.StepLine   |             |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.Area       |             |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.StepArea   |             |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.SplineArea |             |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.Pie        |             |
|             |                                     |               |                       |             |
|             |                                     |               | SeriesType.Column     |             |
+-------------+-------------------------------------+---------------+-----------------------+-------------+

 

More:













