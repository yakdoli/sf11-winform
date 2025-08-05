---
title: chartmodel19.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel19.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Funnel chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Funnel**.

3.   Set the **ChartSeries, ChartArea, and ChartModel** properties.

4.   Return view to the corresponding View page after setting the **ChartModel** to the **ViewData**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [        ][public][ [ActionResult] SimpleChart()]                                                       |
|                                                                                                                                                                                                                                                                       |
| [        {            ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            [// Creating chart series and adding data points to it.]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| **[            [ChartSeries] series1 = [new] [ChartSeries]([\"Funnel Chart\"], [ChartSeriesType].Funnel);]** |
|                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| **[            series1.Points.Add(0, 25);]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| **[            series1.Points.Add(1, 25);]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| **[            series1.Points.Add(2, 25);]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| **[            series1.Points.Add(3, 25);]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| **[            series1.Points.Add(4, 25);]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            series1.Style.DisplayText = [true];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [            series1.Styles\[0\].Text = [\"Oats\\n4.15%\"];]                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            series1.Styles\[1\].Text = [\"Barley\\n12.89%\"];]                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [            series1.Styles\[2\].Text = [\"Maize\\n21.62%\"];]                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [            series1.Styles\[3\].Text = [\"Rice\\n23.75%\"];]                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [            series1.Styles\[4\].Text = [\"Wheat\\n37.5%\"];]                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [            series1.ConfigItems.FunnelItem.LabelPlacement = [ChartAccumulationLabelPlacement].Right;]                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            series1.ConfigItems.FunnelItem.LabelStyle = [ChartAccumulationLabelStyle].OutsideInColumn;]                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            series1.ConfigItems.FunnelItem.FigureBase = [ChartFigureBase].Circle;]                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [            series1.ConfigItems.FunnelItem.GapRatio = 0;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [// Adding Chart Series to the Chart Model]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [            **chartModel.Series.Add(series1);**]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Text = [\"Product Comparision Chart\"];]                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument, and convert the **ViewData** to **MVCChartModel** and set it as the second argument.

[] 

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

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

6.   Build and run the code, to get the following output:

[] 

{border="0"}

[] 

Figure 114: Sample Funnel chart

 

[]{#related-topics}

