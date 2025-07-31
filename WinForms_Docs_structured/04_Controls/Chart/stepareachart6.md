---
title: stepareachart6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\stepareachart6.md
created_at: 2025-07-03
---






#### Step Area Chart {#step-area-chart style="tab-stops: 0pt"}

Step area charts use horizontal and vertical lines to connect data points resulting in a step-like progression. The area under the step line contains the data shown by this type of chart.

Chart Details


  ---------------------------------- -------------
  **Number of Y Values per Point**   1
  **Number of Series         **      One or more
  **Cannot be Combined with   **     Pie chart
  ---------------------------------- -------------


[] 

Step area series can be added to the chart using the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][      ][]**                                                           |
|                                                                                                                                                                                                           |
| [        [Series] series = [new] [Series]([\"System 1\"]);] |
|                                                                                                                                                                                                           |
| [        [  ]]                                                                                                                      |
|                                                                                                                                                                                                           |
| [        series.Points.Add(1, 75);]                                                                                                                      |
|                                                                                                                                                                                                           |
| [        series.Points.Add(2, 82);]                                                                                                                      |
|                                                                                                                                                                                                           |
| [        series.Points.Add(3, 87);]                                                                                                                      |
|                                                                                                                                                                                                           |
| [         ]                                                                                                                                              |
|                                                                                                                                                                                                           |
| [         . . .]                                                                                                                                         |
|                                                                                                                                                                                                           |
| [        series.Style.Border.Width = 3;]                                                                                                                 |
|                                                                                                                                                                                                           |
| [        series.Style.Opacity = 0.8f;]                                                                                                                   |
|                                                                                                                                                                                                           |
| [        series.Type = [SeriesType].StepArea;]                                                                                   |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.Series.Add(series);]                                                                                      |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][  ][]**                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [        [Dim] series [As] [Series] = [New] [Series]([\"System 1\"])] |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(1, 75)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(2, 82)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(3, 87)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        . . .]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series.Style.Border.Width = 3]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [        series.Style.Opacity = 0.8F]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [        series.Type = [SeriesType].StepArea]                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [        [Me].ChartAdv1.Series.Add(series)]                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 14: Step Area Chart

 

[]{#related-topics}

