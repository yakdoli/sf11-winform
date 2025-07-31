---
title: chartmodel7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel7.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Histogram chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Histogram**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding **View** page after setting the **ChartModel** to the **ViewData**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [     ][public][ [ActionResult] SimpleChart()]                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [            [Random] r = [new] [Random]();]                                                                                                                               |
|                                                                                                                                                                                                                                                                                     |
| [            [double]\[\] points = {   25.250,27.750,29.000,28.275,29.750,27.750,28.275,26.250,25.750,25.250,26.250,25.250,24.500,]                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [                                          25.625,25.500,26.625,26.275,26.250,26.875,27.250,26.875,26.500,27.125,26.275,25.875,26.625,]                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| [                                          27.125,26.250,27.000,27.250,27.500,28.500,29.500,28.875,28.500,29.000,28.500,28.500,29.000,]                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| [                                          29.000]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [                                      };]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| [            [double]\[\] points1 = {  23.000,26.500,27.750,25.025,26.500,26.500,28.025,29.250,26.750,27.250,26.250,25.250,24.500,]                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [                                           25.625,25.500,26.625,26.275,26.250,26.875,27.250,26.875,26.500,27.125,26.275,25.875,26.625,]                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [                                           27.125,26.250,27.000,27.250,27.500,28.500,29.500,28.875,28.500,29.000,28.500,28.500,29.000,]                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [                                           29.000]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [                                       };]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [            [DateTime] date = [DateTime].Today.AddDays(-points1.Length);]                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            [for] ([int] i = 1; i \<= 2; i++)]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [            {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            [// Create chart series and add data points to it.]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [                [ChartSeries] Histogram = [new] [ChartSeries]([\"Series\"] + i.ToString(), [ChartSeriesType].Histogram);] |
|                                                                                                                                                                                                                                                                                     |
| [                [for] ([int] j = 0; j \< 50; j++)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [                    Histogram.Points.Add(r.Next(10, 500), 1000);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [                Histogram.Text = Histogram.Name;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [                Histogram.ConfigItems.HistogramItem.NumberOfIntervals = 20;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [                Histogram.ConfigItems.HistogramItem.ShowNormalDistribution = [true];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            [// Add the series to the chart series collection.]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| [                chartModel.Series.Add(Histogram);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [            ][}]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.DropSeriesPoints = [true];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryYAxis.ForceZero = [true];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.ChartArea.XAxesLayoutMode = [ChartAxesLayoutMode].Stacking;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryXAxis.DrawGrid = [false];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryYAxis.DrawGrid = [false];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryXAxis.RangeType = [ChartAxisRangeType].Set;]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryXAxis.Range = [new] [MinMaxInfo](-100, 600, 100);]                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryYAxis.ValueType = [ChartValueType].Double;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryYAxis.RangeType = [ChartAxisRangeType].Auto;]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.BorderStyle = System.Web.UI.WebControls.[BorderStyle].None;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryXAxis.Title = [\"Number Of Users\"];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.Size = [new] [Size](500, 400);]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.Text = [\"Server Load Analysis\"];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.Font = [new] [Font]([\"Verdana\"], 12, [FontStyle].Bold);]                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryYAxis.Title = [\"Server Load (MB)\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [            chartModel.ElementsSpacing = 0;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| [            [return] View();]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument, and convert the **ViewData** to **MVCChartModel** and set it as the second argument.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| [    [@(][new] [HtmlString](Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model).ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

[] 

[] 

{border="0"}

Figure 86: Chart displaying Histogram Series

[] 

[]{#related-topics}

