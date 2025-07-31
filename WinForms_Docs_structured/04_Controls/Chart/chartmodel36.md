---
title: chartmodel36.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel36.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

 

To create a Bubble chart with BubbleType through ChartModel:

1.   In Controller, create an instance of MVCChartModel.

2.   Create an instance of ChartSeries, and set the SeriesType to Bubble.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] SimpleChart()]                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [        {            ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [        [string] accessFileLocation = Server.MapPath([\".\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            accessFileLocation += [@\"\\Content\\Bubble.png\"];]                                                                                                                                           |
|                                                                                                                                                                                                                                                                         |
| [            System.Drawing.[Bitmap] flower = [new] System.Drawing.[Bitmap](accessFileLocation);]                                                              |
|                                                                                                                                                                                                                                                                         |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [            [// Create chart series and add data points to it.]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [//\-\-\-\-\-\-\-\-- Add the Series and set the styling properties that you want\-\-\-\-\--][]                                                                                    |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| **[            [ChartSeries] series3 = [new] [ChartSeries]([\"Technology CCC\"], [ChartSeriesType].Bubble);]** |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| **[            series3.Points.Add(500, 250, 5);]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| **[            series3.Points.Add(1000, 391, 2);]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| **[            series3.Points.Add(1500, 282, 4);]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| **[            series3.Points.Add(2000, 387, 2);]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| **[            series3.Points.Add(2500, 251, 4);]**[]                                                                                                                                           |
|                                                                                                                                                                                                                                                                         |
| [            ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            series3.ScatterConnectType = [ScatterConnectType].None;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            series3.ScatterSplineTension = 0;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| **[            series3.ConfigItems.BubbleItem.BubbleType = [ChartBubbleType].Image;]**                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| **[            [// Adding Chart Series to the Chart Model]]**                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| **[            chartModel.Series.Add(series3);]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| **[            chartModel.Series\[2\].Style.Images = [new] [ChartImageCollection]();]**                                                                                                |
|                                                                                                                                                                                                                                                                         |
| **[            chartModel.Series\[2\].Style.Images.Add(flower);]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--][]                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [}][]                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [  [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

6.   Build and run the application, to get the following output:

{border="0"}

Figure 206: Chart displaying Bubble chart Series

See also

[BubbleChart]

[]{#related-topics}

