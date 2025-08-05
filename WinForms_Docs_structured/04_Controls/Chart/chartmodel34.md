---
title: chartmodel34.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel34.md
created_at: 2025-08-05
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a HeatMap chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **HeatMap**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [        ][public][ [ActionResult] SimpleChart()]                                                 |
|                                                                                                                                                                                                                                                                 |
| [        {            ]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [            [// Create chart series and add data points to it.]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| **[            [ChartSeries] Stocks = [new] [ChartSeries]([\"Stocks\"], [ChartSeriesType].HeatMap);]** |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(7, 4, 10000);]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(6, 3, 5541);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(5, 2, 6007);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(4, 2, 5022);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(3, 2.5, 6882);]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(2, 1.5, 6584);]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| **[            Stocks.Points.Add(1, 1, 2799);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[0\].Text = [\"US\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[1\].Text = [\"South Carolina\"];]                                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[2\].Text = [\"Florida\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[3\].Text = [\"Mexico\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[4\].Text = [\"Arizona\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[5\].Text = [\"North Carolina\"];]                                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Styles\[6\].Text = [\"Utah\"];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Style.DisplayText = [true];]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.Style.Font.Size = 9f;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.Series.Add(Stocks);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.ConfigItems.HeatMapItem.DisplayTitle = [true];]                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.ConfigItems.HeatMapItem.LowestValueColor = [Color].FromArgb(255, 23, 0);]                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.ConfigItems.HeatMapItem.HighestValueColor = [Color].FromArgb(81, 168, 0);]                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.ConfigItems.HeatMapItem.MiddleValueColor = [Color].Gold;]                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.ConfigItems.HeatMapItem.StartText = [\"US\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [            Stocks.ConfigItems.HeatMapItem.EndText = [\"Utah\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.ElementsSpacing = 5;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.Text = [\"Stocks- Sales and Expense details\"];]                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| [                                 ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ][]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
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

{border="0"}

Figure 150: Chart displaying HeatMap Series

[]{#related-topics}

