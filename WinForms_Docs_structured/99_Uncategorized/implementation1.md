---
title: implementation1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\implementation1.md
created_at: 2025-07-03
---






##### Implementation {#implementation style="tab-stops: 0pt"}

Polar chart or Radar chart with RadarType can be created through two ways:

[·      ]Builder

[·      ]ChartModel

###### 5.2.1.6.1.1 Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Polar chart or Radar chart with RadarType through Builder:

1.   In Controller, return view to the corresponding View page.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                           |
|                                                                                                                                  |
| [        [public] [ActionResult] SimpleChart()] |
|                                                                                                                                  |
| [        {            ]                                                                      |
|                                                                                                                                  |
| [            [return] View();]                                          |
|                                                                                                                                  |
| [        }][]                  |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Polar**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the RadarType property to Area, Symbol, or Line.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"ABS(Sin(3φ))\"]).Series(series =\>] |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| **[            series.Add()]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| **[                  .Name([\"Analysis\"])]**                                                                                                                   |
|                                                                                                                                                                                                                             |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Polar)]**                                                                           |
|                                                                                                                                                                                                                             |
| [                  .Points(points =\>]                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [                  {]                                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| **[                      [for] ([int] i = 0; i \<= 710; i++)]**                                                                               |
|                                                                                                                                                                                                                             |
| **[                      {]**                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| **[                          [double] x = [Math].Abs([Math].Sin(3 \* i));]**                                       |
|                                                                                                                                                                                                                             |
| **[                          points.Add(i, x);]**                                                                                                                                       |
|                                                                                                                                                                                                                             |
| **[                      }]**                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| [                  })]                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| **[                  .ConfigItems(configItems =\>]**                                                                                                                                    |
|                                                                                                                                                                                                                             |
| **[                  {]**                                                                                                                                                               |
|                                                                                                                                                                                                                             |
| **[                      configItems.RadarItem(item =\>]**                                                                                                                              |
|                                                                                                                                                                                                                             |
| **[                      {]**                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| **[                          item.Type(Syncfusion.Windows.Forms.Chart.[ChartRadarDrawType].Line);]**                                                            |
|                                                                                                                                                                                                                             |
| **[                      });]**                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| **[                  });]**                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [        })]                                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][]                                           |
|                                                                                                                                                                                                                             |
| [        [%\>]][]                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
| []                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [    [\@{] Html.Chart([\"chart_Model\"]).Text([\"ABS(Sin(3φ))\"]).Series(series =\>] |
|                                                                                                                                                                                                      |
| [        {]                                                                                                                                                      |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| **[            series.Add()]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| **[                  .Name([\"Analysis\"])]**                                                                                            |
|                                                                                                                                                                                                      |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Polar)]**                                                    |
|                                                                                                                                                                                                      |
| [                  .Points(points =\>]                                                                                                                           |
|                                                                                                                                                                                                      |
| [                  {]                                                                                                                                            |
|                                                                                                                                                                                                      |
| **[                      [for] ([int] i = 0; i \<= 710; i++)]**                                                        |
|                                                                                                                                                                                                      |
| **[                      {]**                                                                                                                                    |
|                                                                                                                                                                                                      |
| **[                          [double] x = [Math].Abs([Math].Sin(3 \* i));]**                |
|                                                                                                                                                                                                      |
| **[                          points.Add(i, x);]**                                                                                                                |
|                                                                                                                                                                                                      |
| **[                      }]**                                                                                                                                    |
|                                                                                                                                                                                                      |
| [                  })]                                                                                                                                           |
|                                                                                                                                                                                                      |
| **[                  .ConfigItems(configItems =\>]**                                                                                                             |
|                                                                                                                                                                                                      |
| **[                  {]**                                                                                                                                        |
|                                                                                                                                                                                                      |
| **[                      configItems.RadarItem(item =\>]**                                                                                                       |
|                                                                                                                                                                                                      |
| **[                      {]**                                                                                                                                    |
|                                                                                                                                                                                                      |
| **[                          item.Type(Syncfusion.Windows.Forms.Chart.[ChartRadarDrawType].Line);]**                                     |
|                                                                                                                                                                                                      |
| **[                      });]**                                                                                                                                  |
|                                                                                                                                                                                                      |
| **[                  });]**                                                                                                                                      |
|                                                                                                                                                                                                      |
| [        }).Render();]                                                                                                                                           |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][]                    |
|                                                                                                                                                                                                      |
| [        [}]][]                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 215: Polar chart with Drawtype as Line

[] 

###### 5.2.1.6.1.2 ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Polar chart or Radar chart with RadarType through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, set the SeriesType to **Bubble**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the ScatterConnectType property and the ScatterSplineTension property.

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [       ][public][ [ActionResult] SimpleChart()]                                                |
|                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [    ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                   |
|                                                                                                                                                                                                                                                               |
| [            [// Create chart series and add data points to it.]]                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [            [ChartSeries] series1 = [new] [ChartSeries]([\" System 1\"], [ChartSeriesType].Polar);] |
|                                                                                                                                                                                                                                                               |
| [            series1.Text = series1.Name;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            [for] ([int] i = 0; i \<= 710; i++)]                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [                [double] x = [Math].Abs([Math].Sin(3 \* i));]                                                                                       |
|                                                                                                                                                                                                                                                               |
| [                series1.Points.Add(i, x);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| **[            series1.ConfigItems.RadarItem.Type = [ChartRadarDrawType].Line;]**                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| **[            chartModel.Series.Add(series1);]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][]                                                                             |
|                                                                                                                                                                                                                                                               |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [        }][]                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                                                                                           |
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
| View \[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

7.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 216: Polar chart with Drawtype as Line

[]{#related-topics}

