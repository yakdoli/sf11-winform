---
title: chartmodel35.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel35.md
created_at: 2025-08-05
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Combination chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Line** and **Column**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        ][public][ [ActionResult] SimpleChart()]                                              |
|                                                                                                                                                                                                                                                              |
| [        {            ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                 |
|                                                                                                                                                                                                                                                              |
| [            [// Create chart series and add data points to it.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [ChartSeries] series1 = [new] [ChartSeries]([\"Server1\"], [ChartSeriesType].Line);]   |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series1.Points.Add(1, 200);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series1.Points.Add(2, 500);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [           ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [            series1.Points.Add(3, 100);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series1.Points.Add(4, 400);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [// Add the series to the chart series collection.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Series.Add(series1);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [            [ChartSeries] series2 = [new] [ChartSeries]([\"Server2\"], [ChartSeriesType].Column);] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series2.Points.Add(1, 900);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series2.Points.Add(2, 700);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series2.Points.Add(3, 800);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            series2.Points.Add(4, 600);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [// Add the series to the chart series collection.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Series.Add(series2); ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [     chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Series3D = [true];]                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            chartModel.PrimaryYAxis.Title = [\"ServerLoad(MegaBytes)\"];            ]                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Text = [\"Daily Server Load\"];]                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            chartModel.ShowLegend = [true];]                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            chartModel.LegendPosition = [ChartDock].Top;]                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            chartModel.LegendsPlacement = [ChartPlacement].Outside;]                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Legend.Alignment = [ChartAlignment].Center;]                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [            ViewData.Model = chartModel;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [            [return] View(); ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [}][]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[           ]

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ][]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  ]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

[] 

{border="0"}[]

Figure 152: Chart displaying a combination of Line and Column chart Series

 

[]{#related-topics}

