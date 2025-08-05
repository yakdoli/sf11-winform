---
title: chartmodel40.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel40.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a HiLoOpenClose chart with OpenCloseDrawMode through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **HiLoOpenClose**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

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
| [     **series1.ConfigItems.HiLoOpenCloseItem.DrawMode = [ChartOpenCloseDrawMode].Open;**]                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            chartModel.Series.Add(series);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--]                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]][] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                          |
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

Figure 250: HiLoOpenClose chart with OpenCloseDrawMode as Open

[]{#related-topics}

