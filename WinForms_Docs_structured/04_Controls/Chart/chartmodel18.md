---
title: chartmodel18.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel18.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

 

To create a Range Area chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **RangeArea**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the **ChartModel** to the **ViewData**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [        ][public][ [ActionResult] SimpleChart()]                                                          |
|                                                                                                                                                                                                                                                                          |
| [        {            ]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [            [// Creating chart series and adding data points to it.]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| **[            [ChartSeries] series1 = [new] [ChartSeries]([\"Profit Range\"], [ChartSeriesType].RangeArea);]** |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(1, 20, 49);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(2, 18, 52);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(3, 20, 50);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(4, 18.5, 53);]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(5, 21, 51);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(6, 17.7, 54);]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| **[            series1.Points.Add(7, 19, 52);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            series1.Style.Symbol.Size = [new] [Size](7, 7);]                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| [            series1.Style.Symbol.Color = [Color].DarkBlue;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [            series1.Style.Symbol.Shape = [ChartSymbolShape].Circle;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            [// Adding Chart Series to the Chart Model]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [            **chartModel.Series.Add(series1);**]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [            ]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.PrimaryYAxis.Title = [\"Profit Range\"];]                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.PrimaryXAxis.Title = [\"Year\"];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.Text = [\"Profit Range Per Year\"];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.ShowLegend = [true];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.LegendPosition = [ChartDock].Top;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.LegendsPlacement = [ChartPlacement].Outside;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.Legend.Alignment = [ChartAlignment].Center;]                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]][] |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 108: Range Area chart

[] 

[]{#related-topics}

