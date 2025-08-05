---
title: chartmodel38.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel38.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

The steps to create a Renko chart with ColorsMode, DarkLightPower, and ReversalAmount through ChartModel are as follows:

 

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Renko**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the ColorsMode, DarkLightPower, and ReversalAmount properties.

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [        [public] [ActionResult] SimpleChart()]                                                                              |
|                                                                                                                                                                                                               |
| [        {]                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [    ]                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                  |
|                                                                                                                                                                                                               |
| [            [// Create chart series and add data points into it.]]                                                                                 |
|                                                                                                                                                                                                               |
| [            [double]\[\] points1 = {   25.250,27.750,29.000,28.275,27.750,27.750,27.275,26.250,25.750,25.250,26.250,25.250,24.500,]                 |
|                                                                                                                                                                                                               |
| [                                          25.625,25.500,26.625,26.275,26.250,26.875,27.250,26.875,26.500,27.125,26.275,25.875,26.625,]                                   |
|                                                                                                                                                                                                               |
| [                                          27.125,26.250,27.000,27.250,27.500,28.500,29.500,28.875,28.500,29.000,28.500,28.500,29.000,]                                   |
|                                                                                                                                                                                                               |
| [                                          29.000,40.000,29.875,29.875,28.875,28.500,28.250,28.875,29.275,29.275,29.750,29.500,29.275,]                                   |
|                                                                                                                                                                                                               |
| [                                          28.500,27.750,27.625,27.500,26.500,25.000,26.625,26.000,25.875,25.000,25.250,25.125,25.050};]                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            [DateTime] current = [new] [DateTime](2004, 1, 1);]                                     |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            [ChartSeries] series = [new] [ChartSeries]([\"Series \"] + 0);] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            [for] ([int] day = 0; day \< points1.Length; day++)]                                                               |
|                                                                                                                                                                                                               |
| [            {]                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [                series.Points.Add(current.AddDays(day), points1\[day\]);]                                                                                                |
|                                                                                                                                                                                                               |
| [            }]                                                                                                                                                           |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            series.Type = [ChartSeriesType].Renko;]                                                                                              |
|                                                                                                                                                                                                               |
| [            series.Text = series.Name;]                                                                                                                                  |
|                                                                                                                                                                                                               |
| **[            series.ReversalAmount = 3.0;]**                                                                                                                            |
|                                                                                                                                                                                                               |
| **[            series.ConfigItems.FinancialItem.PriceUpColor = [Color].LightSkyBlue;]**                                                           |
|                                                                                                                                                                                                               |
| **[            series.ConfigItems.FinancialItem.PriceDownColor = [Color].FromArgb(33, 76, 129);]**                                                |
|                                                                                                                                                                                                               |
| **[            series.ConfigItems.FinancialItem.ColorsMode = [ChartFinancialColorMode].DarkLight;]**                                              |
|                                                                                                                                                                                                               |
| **[            series.ConfigItems.FinancialItem.DarkLightPower = 200;]**                                                                                                  |
|                                                                                                                                                                                                               |
| [            ]                                                                                                                                                            |
|                                                                                                                                                                                                               |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--][]                             |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            ViewData.Model = chartModel;]                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                                       |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [        }]                                                                                                                                                               |
|                                                                                                                                                                                                               |
| []                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[          ]

6.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ][]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\][]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[      ][]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 241: Renko chart with ReversalAmount 3.0, ColorsMode as DarkLight, and DarkLightPower as 200

**[]** 

[]{#related-topics}

