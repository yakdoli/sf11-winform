---
title: charttypes17.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\charttypes17.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Chart Types {#chart-types style="tab-stops: 0pt"}

Essential Chart includes a comprehensive set of more than 35 Chart types for all your business needs. Each one is highly and easily configurable with built-in support for creating stunning visual effects.

Chart types are specified on each ChartSeries by using the Type property. All the chart types are required to have at least one X and one Y value. Certain chart types need more than one Y value.

The following table narrates the minimum and maximum number of series and number of Y values required by each type of chart supported by Essential Chart:


  Chart Type           Minimum Number of Series   Maximum Number of Series   Number of Y Values Required
  -------------------- -------------------------- -------------------------- -----------------------------
  Area charts          1                          Unlimited                  1
  Column charts        1                          Unlimited                  1
  Combination charts   2                          Unlimited                  1
  Line charts          1                          Unlimited                  1
  Pie charts           1                          1                          1


[] 

Series Properties

+-------------+---------------------------------------------------+----------------------+-----------------------+-------------+
| Name        | Description                                       | Type of the property | Value it accepts      | Dependency  |
+-------------+---------------------------------------------------+----------------------+-----------------------+-------------+
| Type        | This property gets or sets the chart series type. | SeriesType           | SeriesType.Line       | NA          |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.Spline     |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.StepLine   |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.Area       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.StepArea   |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.SplineArea |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.Pie        |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      | SeriesType.Column     |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
|             |                                                   |                      |                       |             |
+-------------+---------------------------------------------------+----------------------+-----------------------+-------------+

[] 

[] 

More:













