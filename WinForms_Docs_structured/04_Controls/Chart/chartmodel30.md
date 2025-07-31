---
title: chartmodel30.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel30.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

 

To create a Box and Whisker chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **BoxAndWhisker**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [       ][public][ [ActionResult] SimpleChart()] |
|                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [    ]                                                                                                                                                                     |
|                                                                                                                                                                                                                |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                    |
|                                                                                                                                                                                                                |
| [            [// Create chart series and add data points to it.]]                                                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| **[            [ChartSeries] series = [new] [ChartSeries]([\"Analysis\"]);]** |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                |
| **[            series.Points.Add(0, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150);]**                                                                                      |
|                                                                                                                                                                                                                |
| **[            series.Points.Add(1, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140);]**                                                                                       |
|                                                                                                                                                                                                                |
| **[            series.Points.Add(2, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130);]**                                                                                        |
|                                                                                                                                                                                                                |
| **[            series.Points.Add(3, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120);]**                                                                                         |
|                                                                                                                                                                                                                |
| **[            series.Points.Add(4, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110);]**                                                                                          |
|                                                                                                                                                                                                                |
| **[            series.Points.Add(5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100);]**                                                                                           |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                |
| **[            series.Type = [ChartSeriesType].BoxAndWhisker;]**                                                                                   |
|                                                                                                                                                                                                                |
| **[            series.Text = series.Name;]**                                                                                                                               |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                |
| **[            chartModel.Series.Add(series);]**                                                                                                                           |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [            chartModel.Text = [\"Box and Whisker Chart\"];]                                                                                       |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [            chartModel.Series3D = [true];]                                                                                                           |
|                                                                                                                                                                                                                |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                 |
|                                                                                                                                                                                                                |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                             |
|                                                                                                                                                                                                                |
| [            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]                                                       |
|                                                                                                                                                                                                                |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                               |
|                                                                                                                                                                                                                |
| [                                 ]                                                                                                                                        |
|                                                                                                                                                                                                                |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                        |
|                                                                                                                                                                                                                |
| [            ViewData.Model = chartModel;]                                                                                                                                 |
|                                                                                                                                                                                                                |
| [            [return] View();]                                                                                                                        |
|                                                                                                                                                                                                                |
| [        }][]                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[              ]

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
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                                         |
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

{border="0"}

Figure 140: Chart displaying Box and Whisker chart Series

[] 

[]{#related-topics}

