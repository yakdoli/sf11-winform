---
title: chartmodel6.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel6.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Gantt chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the **SeriesType** to **Gantt**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding **View** page after setting the **ChartModel** to the **ViewData**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [     ][public][ [ActionResult] SimpleChart()]                                                          |
|                                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                           |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [// Create chart series and add data points to it.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| **[            [ChartSeries] Completion = [new] [ChartSeries]([\"Completion\"], [ChartSeriesType].Gantt);]** |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Points.Add(1, 0, 1);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Points.Add(4, 1, 2);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Points.Add(6, 3, 5);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Points.Add(8, 6, 9);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Points.Add(10, 10, 13);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Points.Add(12, 15, 18);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            Completion.Style.PointWidth = 0.3f;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            ][// Add the series to the chart series collection.][]                                                            |
|                                                                                                                                                                                                                                                                       |
| [            **chartModel.Series.Add(Completion);**]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [// Create chart series and add data points to it.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            **[ChartSeries] Task = [new] [ChartSeries]([\"Task\"], [ChartSeriesType].Gantt);**]             |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            Task.Points.Add(1, 0, 1);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            Task.Points.Add(4, 1, 3);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            Task.Points.Add(6, 3, 6);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            Task.Points.Add(8, 6, 10);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            Task.Points.Add(10, 10, 15);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            Task.Points.Add(12, 15, 20);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            Task.Style.PointWidth = 0.8f;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [// Add the series to the chart series collection.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            **chartModel.Series.Add(Task);**]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Refresh();]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Text = [\"Project Schedule\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Size = [new] [Size](500, 400);]                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryYAxis.DrawGrid = [false];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryXAxis.Range = [new] [MinMaxInfo](0, 20, 1);]                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryYAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryYAxis.Range = [new] [MinMaxInfo](0, 15, 1);]                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Series3D = [false];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryYAxis.Inversed = [true];]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.BorderStyle = System.Web.UI.WebControls.[BorderStyle].None;]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryXAxis.LabelRotate = [true];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryXAxis.LabelRotateAngle = 90;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.ChartArea.XAxesLayoutMode = [ChartAxesLayoutMode].Stacking;]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.ElementsSpacing = 0;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Font = [new] [Font]([\"Verdana\"], 12, [FontStyle].Bold);]                                                   |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Text = [\"Project Schedule\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryXAxis.Title = [\"Days\"];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.PrimaryYAxis.Title = [\"Task\"];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the **ViewData** to **MVCChartModel** and set it as the second argument.

[] 

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

 

6.   Build and run the code, to get the following output:

 

{border="0"}

Figure 84: Chart displaying Gantt Series

[]{#related-topics}

