---
title: chartmodel25.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel25.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a HiLoOpenClose chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **HiLoOpenClose**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the **ChartModel** to the **ViewData**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [        ][public][ [ActionResult] SimpleChart()]                                                           |
|                                                                                                                                                                                                                                                                           |
| [        {            ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [            [// Create chart series and add data points to it.]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            **[ChartSeries] series = [new] [ChartSeries]([\"HiLo Chart\"], [ChartSeriesType].HiLoOpenClose);**] |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            series.Text = series.Name;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [DateTime] start = [new] [DateTime](2006, 2, 12);]                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(0), 456, 214, 364, 386);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(1), 491, 234, 321, 378);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(2), 482, 193, 302, 352);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(3), 437, 243, 354, 391);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(4), 421, 223, 317, 367);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(5), 434, 263, 339, 385);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(6), 425, 245, 365, 396);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(7), 457, 234, 385, 398);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(8), 482, 267, 316, 389);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series.Points.Add(start.AddDays(9), 496, 285, 374, 399);]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Series.Add(series);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            ][chartModel.Text = [\"Candle Chart\"];]                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.Title = [\"Week Day\"];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryYAxis.Title = [\"Price (\$)\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.ValueType = [ChartValueType].DateTime;]                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.DrawGrid = [false];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.LabelRotate = [true];]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.LabelRotateAngle = 270;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryYAxis.DrawGrid = [false];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Indexed = [true];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.DateTimeFormat = [\"MMM/dd\"];]                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.HidePartialLabels = [true];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [}][]                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

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

[      ][]

[      ][]

6.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 130: Chart displaying HiLoOpenClose chart Series

 

[]{#related-topics}

