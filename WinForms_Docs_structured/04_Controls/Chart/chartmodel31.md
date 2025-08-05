---
title: chartmodel31.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel31.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Polar chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the **SeriesType** to **Polar**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the **ChartModel** to the **ViewData**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [       ][public][ [ActionResult] SimpleChart()]                                                |
|                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [    ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                   |
|                                                                                                                                                                                                                                                               |
| [            [// Create chart series and add data points to it.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            [ChartSeries] series1 = [new] [ChartSeries]([\" System 1\"], [ChartSeriesType].Polar);] |
|                                                                                                                                                                                                                                                               |
| [            series1.Text = series1.Name;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            [for] ([int] i = 0; i \<= 710; i++)]                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [                [double] x = [Math].Abs([Math].Sin(3 \* i));]                                                                                       |
|                                                                                                                                                                                                                                                               |
| [                series1.Points.Add(i, x);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [            series1.ConfigItems.RadarItem.Type = [ChartRadarDrawType].Area;]                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Series.Add(series1);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Text = [\"ABS(Sin(3φ))\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryYAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryXAxis.Range = [new] [MinMaxInfo](0, 360, 45);]                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryYAxis.Range = [new] [MinMaxInfo](0, 1.5, 0.5);]                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [                                 ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[         ]

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ]

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

[] 

6.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 144: Chart displaying Polar Series

[]{#related-topics}

