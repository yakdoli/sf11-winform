---
title: steplinechart1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\steplinechart1.md
created_at: 2025-07-03
---






#### Step Line Chart {#step-line-chart style="tab-stops: 0pt"}

 

Step Line charts use horizontal and vertical lines to connect data points resulting in a step like progression.

Step Line chart can be created in two ways:[]

[·      ]Builder[]

[·      ]ChartModel[]

 

Chart Details

 


+------------------------------+------------------------------------------------------------------------+
| Details                                                                                               |
+------------------------------+------------------------------------------------------------------------+
| Number of Y values per point | 1                                                                      |
+------------------------------+------------------------------------------------------------------------+
| Number of Series             | One or more                                                            |
+------------------------------+------------------------------------------------------------------------+
| Cannot be Combined with      | Pie chart, Bar chart, Stacked Bar chart, Polar chart, and Radar chart. |
+------------------------------+------------------------------------------------------------------------+


[] 

Builder

 

To create a Step Line chart through Builder:

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
| [        }]                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the **View** page, invoke the **ChartBuilder** by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **StepLine**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[ASPX\]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [    ][\<%][=][ Html.Chart([\"SimpleChart\"]).Series(series =\>{] |
|                                                                                                                                                                                                                                                                                         |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StepLine)**]                                                                                                                      |
|                                                                                                                                                                                                                                                                                         |
| [                          .Text([\"Server 1\"])]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [                          .Points(point =\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [                          {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(1, 200);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(2, 500);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(3, 100);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(4, 400);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                          });]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StepLine)**]                                                                                                                      |
|                                                                                                                                                                                                                                                                                         |
| [                    .Text([\"Server 2\"])]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [                    .Points(point =\>]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [                    {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(1, 900);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(2, 700);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(3, 800);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                                    point.Add(4, 600);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                   });]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [            }).Skins([ChartModelSkins].Office2007Blue)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [              .ShowLegend([true])]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [              .LegendsPlacement(Syncfusion.Windows.Forms.Chart.[ChartPlacement].Outside)]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [              .LegendPosition(Syncfusion.Windows.Forms.Chart.[ChartDock].Top)]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [              .Legend(legend =\>{]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [                  legend.Alignment(Syncfusion.Windows.Forms.Chart.[ChartAlignment].Center);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [              }).Series3D([true])]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [              .BorderAppearance(border =\>{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [                  border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [              }).PrimaryXAxis(xaxis =\>{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                  xaxis.Title([\"Server Load(MegaBytes)\"]);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                         |
| [              }).Text([\"Daily Server Load\"])]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [        ]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [\@{][ ][Html.Chart([\"SimpleChart\"]).Series(series =\>{]              |
|                                                                                                                                                                                                                                 |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StepLine)**]                                                              |
|                                                                                                                                                                                                                                 |
| [                          .Text([\"Server 1\"])]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [                          .Points(point =\>]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [                          {]                                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(1, 200);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(2, 500);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(3, 100);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(4, 400);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                          });]                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StepLine)**]                                                              |
|                                                                                                                                                                                                                                 |
| [                    .Text([\"Server 2\"])]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [                    .Points(point =\>]                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [                    {]                                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(1, 900);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(2, 700);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(3, 800);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                                    point.Add(4, 600);]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                   });]                                                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            }).Skins([ChartModelSkins].Office2007Blue)]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [              .ShowLegend([true])]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [              .LegendsPlacement(Syncfusion.Windows.Forms.Chart.[ChartPlacement].Outside)]                                                                          |
|                                                                                                                                                                                                                                 |
| [              .LegendPosition(Syncfusion.Windows.Forms.Chart.[ChartDock].Top)]                                                                                     |
|                                                                                                                                                                                                                                 |
| [              .Legend(legend =\>{]                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [                  legend.Alignment(Syncfusion.Windows.Forms.Chart.[ChartAlignment].Center);]                                                                       |
|                                                                                                                                                                                                                                 |
| [              }).Series3D([true])]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                                   |
|                                                                                                                                                                                                                                 |
| [              .BorderAppearance(border =\>{]                                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [                  border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                 |
|                                                                                                                                                                                                                                 |
| [              }).PrimaryXAxis(xaxis =\>{]                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                  xaxis.Title([\"Server Load(MegaBytes)\"]);]                                                                                                      |
|                                                                                                                                                                                                                                 |
| [              }).Text([\"Daily Server Load\"])][             ]                                                                 |
|                                                                                                                                                                                                                                 |
| [              .Render();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [        ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [              [}]][                                      ][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 75: Step Line chart

ChartModel

[] 

To create a Step Line chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the **SeriesType** to **StepLine**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return **View** to the corresponding View page after setting the **ChartModel** to the **ViewData**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] SimpleChart()]                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [        {            ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [            [// Create chart series and add data points to it.]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| **[            [ChartSeries] series1 = [new] [ChartSeries]([\"Server1\"], [ChartSeriesType]. StepLine);]** |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series1.Points.Add(1, 200);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series1.Points.Add(2, 500);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| [           ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [            series1.Points.Add(3, 100);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series1.Points.Add(4, 400);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            [// Add the series to the chart series collection.]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| **[            chartModel.Series.Add(series1);]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                     |
| **[            [ChartSeries] series2 = [new] [ChartSeries]([\"Server2\"], [ChartSeriesType]. StepLine);]** |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series2.Points.Add(1, 900);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series2.Points.Add(2, 700);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series2.Points.Add(3, 800);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            series2.Points.Add(4, 600);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            [// Add the series to the chart series collection.]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| **[            chartModel.Series.Add(series2); ]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.Series3D = [true];]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.PrimaryYAxis.Title = [\"ServerLoad(MegaBytes)\"];            ]                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.Text = [\"Daily Server Load\"];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.ShowLegend = [true];]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.LegendPosition = [ChartDock].Top;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.LegendsPlacement = [ChartPlacement].Outside;]                                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.Legend.Alignment = [ChartAlignment].Center;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [            chartModel.Size = [new] System.Drawing.[Size](500, 400);]                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| [            [return] View(); ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [}][]                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument, and convert the **ViewData** to **MVCChartModel** and set it as the second argument.

[] 

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

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [@(][new][ [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

 

{border="0"}

Figure 76: Step Line chart

[]{#related-topics}

