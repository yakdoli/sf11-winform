---
title: chartmodel3.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel3.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

To create a Bar chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the **SeriesType** to **Bar**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the **ChartModel** to the ViewData.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [     ][public][ [ActionResult] SimpleChart()]                                                  |
|                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                  |
|                                                                                                                                                                                                                                                               |
| [            [// Create a chart series and add data points to it.]]                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| **[            [ChartSeries] series1 = [new] [ChartSeries]([\"Server1\"], [ChartSeriesType].Bar);]** |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            series1.Points.Add(15, 225);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            series1.Points.Add(3, 325);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [            series1.Points.Add(7, 275);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [            series1.Points.Add(11, 350);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            [// Add the series to the chart series collection.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| **[            chartModel.Series.Add(series1);]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| **[            [ChartSeries] series2 = [new] [ChartSeries]([\"Server2\"], [ChartSeriesType].Bar);]** |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            series2.Points.Add(15, 325);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            series2.Points.Add(3, 355);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [            series2.Points.Add(7, 315);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [            series2.Points.Add(11, 300);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            [// Add the series to the chart series collection.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            **chartModel.Series.Add(series2);**]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Series3D = [true];]                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryYAxis.Title = [\"Peak Load (Hr)\"];]                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryXAxis.Title = [\"Server Load (MB)\"];]                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Text = [\"Peak Average Network Load\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [            chartModel.ShowLegend = [true];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            chartModel.LegendPosition = [ChartDock].Top;]                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            chartModel.LegendsPlacement = [ChartPlacement].Outside;]                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Legend.Alignment = [ChartAlignment].Center;]                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryYAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryYAxis.Range = [new] [MinMaxInfo](0, 20, 10);]                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [            chartModel.PrimaryXAxis.Range.Min = 0;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the **ViewData** to **MVCChartModel** and set it as the second argument.

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [@(][new][ [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the code, to get the following output:

[] 

[] 

{border="0"}

Figure 78: Bar Chart

 

[]{#related-topics}

