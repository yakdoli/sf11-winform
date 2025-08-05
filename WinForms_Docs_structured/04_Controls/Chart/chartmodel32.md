---
title: chartmodel32.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel32.md
created_at: 2025-08-05
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Radar chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Radar**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [       [public] [ActionResult] SimpleChart()]                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [    ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [            [// Create chart series and add data points to it.]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| **[            [ChartSeries] series1 = [new] [ChartSeries]([\" Allocated Budget\"], [ChartSeriesType].Radar);]** |
|                                                                                                                                                                                                                                                                           |
| **[            ][series1.Text = series1.Name;]**                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Points.Add(0, 40);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Points.Add(1, 20);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Points.Add(2, 33);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Points.Add(3, 25);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Points.Add(4, 60);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Points.Add(5, 20);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [            series1.ConfigItems.RadarItem.Type = [ChartRadarDrawType].Area;]                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| **[            [ChartSeries] series2 = [new] [ChartSeries]([\"Actual Spending\"], [ChartSeriesType].Radar);]**   |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Text = series2.Name;]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Points.Add(0, 50);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Points.Add(1, 22);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Points.Add(2, 25);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Points.Add(3, 20);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Points.Add(4, 20);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| **[            series2.Points.Add(5, 45);]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [            series2.ConfigItems.RadarItem.Type = [ChartRadarDrawType].Area;]                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            chartModel.Series.Add(series1);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| **[            chartModel.Series.Add(series2);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryYAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryYAxis.Range = [new] [MinMaxInfo](0, 60, 10);]                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.PrimaryXAxis.Range = [new] [MinMaxInfo](0, 6, 1);]                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Text = [\"Organization Budget\"];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [                        ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [                                 ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[             ]

5.   In the View page, invoke the ChartBuilder by using the control ID as first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ][]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                 |
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

[] 

[]{#_Pie_Chart}{border="0"}

Figure 147: Chart displaying Radar chart Series

[]{#related-topics}

