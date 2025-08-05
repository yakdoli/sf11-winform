---
title: implementation.md
original_path: WinForms_Docs/99_Uncategorized/implementation.md
created_at: 2025-08-05
---






##### Implementation {#implementation style="tab-stops: 0pt"}

 

Scatter chart with the ScatterConnectType and ScatterSplineTension properties can be created through two ways:

[·      ]Builder

[·      ]ChartModel

[] 

###### 5.2.1.5.3.1 Builder {#builder style="tab-stops: 0pt"}

[] 

The steps to create a Scatter chart with the ScatterConnectType and ScatterSplineTension properties through Builder are as follows:

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
| [        }]                                                                                  |
|                                                                                                                                  |
| []                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Bubble**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the ScatterConnectType property and ScatterSplineTension property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                         |
| [    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [//\-\-\-\-\-\-\-\-- Add the Series and set the styling properties that you want\-\-\-\-\--][]                                                    |
|                                                                                                                                                                                                                                         |
| [            series.Add()]                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| [                  .Name([\"Technology CCC\"])]                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]                                                                                          |
|                                                                                                                                                                                                                                         |
| [    .Points(points =\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                points.Add(500, 250, 5);]                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| [                points.Add(1000, 391, 2);]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                points.Add(1500, 282, 4);]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                points.Add(2000, 387, 2);]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                points.Add(2500, 251, 4);]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                **}).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].Spline)**]                                                                     |
|                                                                                                                                                                                                                                         |
| **[              .ScatterSplineTension(2);]**                                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [})]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][]                                                       |
|                                                                                                                                                                                                                                         |
| [    ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [    [%\>]][]                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [    [\@{] Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [//\-\-\-\-\-\-\-\-- Add the Series and set the styling properties that you want\-\-\-\-\--][]                             |
|                                                                                                                                                                                                                  |
| [            series.Add()]                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| [                  .Name([\"Technology CCC\"])]                                                                                                      |
|                                                                                                                                                                                                                  |
| [                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]                                                                   |
|                                                                                                                                                                                                                  |
| [    .Points(points =\>]                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [            {]                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [                points.Add(500, 250, 5);]                                                                                                                                   |
|                                                                                                                                                                                                                  |
| [                points.Add(1000, 391, 2);]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                points.Add(1500, 282, 4);]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                points.Add(2000, 387, 2);]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                points.Add(2500, 251, 4);]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                **}).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].Spline)**]                                              |
|                                                                                                                                                                                                                  |
| **[              .ScatterSplineTension(2);]**                                                                                                                                |
|                                                                                                                                                                                                                  |
| [}).Render();]                                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea properties that you want\-\-\-\-\--][]                                |
|                                                                                                                                                                                                                  |
| [        [}]][]                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 211: Scatter chart with ScatterConnectType as Spline and ScatterSplineTension as 2

 

See also

[Scatter Chart]

[                                ]

###### 5.2.1.5.3.2 ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Scatter chart with the ScatterConnectType and ScatterSplineTension properties through ChartModel:

1.   In Controller, create an instance of MVCChartModel.

2.   Create an instance of ChartSeries, and set the SeriesType to Bubble.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the ScatterConnectType property and ScatterSplineTension property.

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [        ][public][ [ActionResult] SimpleChart()]                                                         |
|                                                                                                                                                                                                                                                                         |
| [        {            ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [            [// Create chart series and add data points to it.]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
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
| **[            series3.Points.Add(2500, 251, 4);]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [            ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            series3.ScatterConnectType = [ScatterConnectType].Spline;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            series3.ScatterSplineTension = 2;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| **[            [// Adding Chart Series to the Chart Model]]**                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| **[            chartModel.Series.Add(series3);]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][]                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel**, and set it as the second argument.

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
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

7.   Build and run the application, to get the following output:

 

{border="0"}

Figure 212: Scatter chart with ScatterConnectType as Spline and ScatterSplineTension as 2

 

See also

[Scatter Chart]

 

[]{#related-topics}

