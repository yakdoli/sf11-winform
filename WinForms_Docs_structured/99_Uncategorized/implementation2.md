---
title: implementation2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\implementation2.md
created_at: 2025-07-03
---






##### Implementation {#implementation style="tab-stops: 0pt"}

[] 

Funnel or Pyramid charts with the above properties can be created through two ways:

[·      ]Builder

[·      ]ChartModel

[] 

###### 5.2.1.8.6.1 Builder {#builder style="tab-stops: 0pt"}

[] 

The steps to create Funnel or Pyramid charts with the above properties through Builder are as follows:

1.   In Controller, return view to the corresponding View page.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        ][public][ [ActionResult] SimpleChart()] |
|                                                                                                                                                                                                                 |
| [        {            ]                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                                         |
|                                                                                                                                                                                                                 |
| [        }][]                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Funnel** or **Pyramid**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the Funnel Config items properties.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                |
| [    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>][] |
|                                                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                |
| [            series.Add().Name([\"Funnel Chart\"]).Name([\"Pyramid Chart\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Pyramid).Points(points =\>]                     |
|                                                                                                                                                                                                                                                                                                |
| [           {]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| **[               points.Add(0, 20.6);]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| **[               points.Add(1, 25.3);]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| **[               points.Add(2, 45.7);]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| **[               points.Add(3, 97.3);]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| **[               points.Add(4, 125.8);]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [           }).ConfigItems(items =\>]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                |
| [           {]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| **[               items.FunnelItem(item =\>]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| **[               {]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| **[                   item.LabelStyle(Syncfusion.Windows.Forms.Chart.[ChartAccumulationLabelStyle].OutsideInColumn)]**                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| **[                       .LabelPlacement(Syncfusion.Windows.Forms.Chart.[ChartAccumulationLabelPlacement].Center)]**                                                                                                              |
|                                                                                                                                                                                                                                                                                                |
| **[                       .FigureBase(Syncfusion.Windows.Forms.Chart.[ChartFigureBase].Square)]**                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| **[                       .GapRatio(0.2f)]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| **[                       .FunnelMode(Syncfusion.Windows.Forms.Chart.[ChartFunnelMode].YIsWidth);]**                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| **[               });]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                |
| **[           });]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [//\-\-\-\-\-\-\-\-- Add the Series and set the styling properties that you want\-\-\-\-\--][]                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                |
| [            })]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [    [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| [    [%\>]][]                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [    [\@{] Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>][]    |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            series.Add().Name([\"Funnel Chart\"]).Name([\"Pyramid Chart\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Pyramid).Points(points =\>] |
|                                                                                                                                                                                                                                                                            |
| [           {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| **[               points.Add(0, 20.6);]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| **[               points.Add(1, 25.3);]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| **[               points.Add(2, 45.7);]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| **[               points.Add(3, 97.3);]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| **[               points.Add(4, 125.8);]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [           }).ConfigItems(items =\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [           {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| **[               items.FunnelItem(item =\>]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| **[               {]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| **[                   item.LabelStyle(Syncfusion.Windows.Forms.Chart.[ChartAccumulationLabelStyle].OutsideInColumn)]**                                                                                         |
|                                                                                                                                                                                                                                                                            |
| **[                       .LabelPlacement(Syncfusion.Windows.Forms.Chart.[ChartAccumulationLabelPlacement].Center)]**                                                                                          |
|                                                                                                                                                                                                                                                                            |
| **[                       .FigureBase(Syncfusion.Windows.Forms.Chart.[ChartFigureBase].Square)]**                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| **[                       .GapRatio(0.2f)]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| **[                       .FunnelMode(Syncfusion.Windows.Forms.Chart.[ChartFunnelMode].YIsWidth);]**                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| **[               });]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| **[           });]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [//\-\-\-\-\-\-\-\-- Add the series and set the styling properties that you want\-\-\-\-\--][]                                                                                       |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [            }).Render();]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [    [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--]]                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [    [}]][]                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   [Build and run the application, to get the following output:]

[] 

{border="0"}[]

[] 

Figure 231:: Funnel chart with LabelStyle outsideinColumn, LabelPlacement center, FunnelMode YIsWidth, FigureBase Square, and GapRatio 0.2f

[] 

###### 5.2.1.8.6.2 ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create Funnel or Pyramid charts with the above properties through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Funnel** or **Pyramid**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the Funnel ConfigItem properties.

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [       ][public][ [ActionResult] SimpleChart()]                                                    |
|                                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [    ]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                       |
|                                                                                                                                                                                                                                                                   |
| [            [// Create chart series and add data points to it.]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [            [ChartSeries] series1 = [new] [ChartSeries]([\"Funnel Chart\"], [ChartSeriesType].Funnel);] |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [            series1.Points.Add(0, 20.6);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [            series1.Points.Add(1, 25.3);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [            series1.Points.Add(2, 45.7);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [            series1.Points.Add(3, 97.3);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [            series1.Points.Add(4, 125.8);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//\-\-\-\-\-\-\-\-- Add the series and set the styling properties that you want\-\-\-\-\--][]                                                                              |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| **[            series1.ConfigItems.FunnelItem.LabelPlacement = [ChartAccumulationLabelPlacement].Center;]**                                                                                           |
|                                                                                                                                                                                                                                                                   |
| **[            series1.ConfigItems.FunnelItem.LabelStyle = [ChartAccumulationLabelStyle].OutsideInColumn;]**                                                                                          |
|                                                                                                                                                                                                                                                                   |
| **[            series1.ConfigItems.FunnelItem.FigureBase = [ChartFigureBase].Square;]**                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| **[            series1.ConfigItems.FunnelItem.GapRatio = 0.2f;]**                                                                                                                                                             |
|                                                                                                                                                                                                                                                                   |
| **[            series1.ConfigItems.FunnelItem.FunnelMode = [ChartFunnelMode].YIsWidth;]**                                                                                                             |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [            [// Adding Chart Series to the Chart Model]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [            chartModel.Series.Add(series1);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--]                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [            [return] View();]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [        }][]                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[ASPX\]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

7.   Build and run the application, to get the following output:

[] 

{border="0"}[]

[] 

Figure 232: Funnel chart with LabelStyle outsideinColumn, LabelPlacement center, FunnelMode YIsWidth, FigureBase Square, and GapRatio 0.2f

[]{#related-topics}

