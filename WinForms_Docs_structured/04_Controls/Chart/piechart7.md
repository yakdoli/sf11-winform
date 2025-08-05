---
title: piechart7.md
original_path: WinForms_Docs/04_Controls/Chart/piechart7.md
created_at: 2025-08-05
---








  









### Pie Chart {#pie-chart style="tab-stops: 0pt"}

A pie chart renders the y values as slices in a pie. These slices are rendered in proportion to the whole, which is simply the sum of all the y values in the series. Consequently, pie charts are used to visualize the proportional contribution (in terms of percentage or fraction) of categories of data to the whole data set. The x values in the data series will only be treated as nominal (categorical and qualitative) data. The pie chart can display only one data series at a time.                      

Chart Details


  ---------------------------------- -----------------------
  **Number of Y values per point**   1
  **Number of Series         **      One
  **Cannot be Combined with   **     Any other chart type.
  ---------------------------------- -----------------------


[] 

Column series can be added to the chart using the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][      ][]**                                                           |
|                                                                                                                                                                                                           |
| [       [Series] Series1 = [new] [Series]([\"PieChart\"]);] |
|                                                                                                                                                                                                           |
| [        Series1.Type = [SeriesType].Pie;]                                                                                       |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(1, 20);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(2, 21);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(3, 40);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(4, 10);]                                                                                                                     |
|                                                                                                                                                                                                           |
| [        Series1.Points.Add(5, 9);]                                                                                                                      |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.Series.Add(Series1);]                                                                                     |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [        Series1.Points\[0\].Text = [\"Analysis 20%\"];]                                                                         |
|                                                                                                                                                                                                           |
| [        Series1.Points\[1\].Text = [\"Design 21%\"];]                                                                           |
|                                                                                                                                                                                                           |
| [        Series1.Points\[2\].Text = [\"Code/Unit Test 40%\"];]                                                                   |
|                                                                                                                                                                                                           |
| [        Series1.Points\[3\].Text = [\"Documentation 10%\"];]                                                                    |
|                                                                                                                                                                                                           |
| [        Series1.Points\[4\].Text = [\"Deployment 9%\"];]                                                                        |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [        Series1.DisplayText = [true];]                                                                                             |
|                                                                                                                                                                                                           |
| [        Series1.TextColor = [Color].Red;]                                                                                       |
|                                                                                                                                                                                                           |
| [        Series1.ShowTicks = [true];]                                                                                               |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.Legend.Visible = [false];]                                                           |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.LegendAlignment = [StringAlignment].Center;]                                      |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.LegendPosition = [DockPosition].Top;]                                             |
|                                                                                                                                                                                                           |
| [        [this].ChartAdv1.ElementSpacing = 10;]                                                                                     |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][      ][]**                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| [       Dim][ Series1 [As] [Series] = [New] [Series]([\"PieChart\"])] |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Type = [SeriesType].Pie]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points.Add(1, 20)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points.Add(2, 21)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points.Add(3, 40)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points.Add(4, 10)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points.Add(5, 9)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [        [Me].ChartAdv1.Series.Add(Series1)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points(0).Text = [\"Analysis 20%\"]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points(1).Text = [\"Design 21%\"]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points(2).Text = [\"Code/Unit Test 40%\"]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points(3).Text = [\"Documentation 10%\"]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.Points(4).Text = [\"Deployment 9%\"]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.DisplayText = [True]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.TextColor = [Color].Red]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| [        Series1.ShowTicks = [True]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [        [Me].ChartAdv1.Legend.Visible = [False]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [        [Me].ChartAdv1.LegendAlignment = [StringAlignment].Center]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                        |
| [        [Me].ChartAdv1.LegendPosition = [DockPosition].Top]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [        [Me].ChartAdv1.ElementSpacing = 10]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}{border="0"}

 

{border="0"}

Figure 16: Pie Chart Showing the Product Development Cycle

 

[]{#related-topics}

