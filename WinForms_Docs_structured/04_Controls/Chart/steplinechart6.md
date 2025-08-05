---
title: steplinechart6.md
original_path: WinForms_Docs/04_Controls/Chart/steplinechart6.md
created_at: 2025-08-05
---






#### Step Line Chart {#step-line-chart style="tab-stops: 0pt"}

Step line charts use horizontal and vertical lines to connect data points resulting in a step-like progression.

 

Chart Details


  ---------------------------------- -------------
  **Number of Y Values per Point**   1
  **Number of Series         **      One or more
  **Cannot be Combined with   **     Pie chart
  ---------------------------------- -------------


[] 

Step Line series can be added to the chart using the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| [       [Series] Series1 = [new] [Series]([\"Server 1\"]);] |
|                                                                                                                                                                                                           |
| [       Series1.Type = [SeriesType].StepLine;]                                                                                   |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(1, 75);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(2, 82);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(3, 87);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(4, 84);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(5, 84);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(6, 60);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(7, 55);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(8, 78);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(9, 90);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(10, 85);]                                                                                                                    |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.Series.Add(Series1);]                                                                                     |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [        Dim][ Series1 [As] [Series] = [New] [Series]([\"Server 1\"])] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Type = [SeriesType].StepLine]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(1, 75)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(2, 82)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(3, 87)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(4, 84)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(5, 84)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(6, 60)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(7, 55)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(8, 78)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(9, 90)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [        Series1.Points.Add(10, 85)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [        [Me].ChartAdv1.Series.Add(Series1)]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| [           ]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| [ ][ ][]                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 11: Step Line Chart

[]{#related-topics}

