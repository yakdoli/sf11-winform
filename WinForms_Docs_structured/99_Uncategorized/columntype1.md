---
title: columntype1.md
original_path: WinForms_Docs/99_Uncategorized/columntype1.md
created_at: 2025-08-05
---






##### Column Type {#column-type style="tab-stops: 0pt"}

Column Type specifies whether the columns should be rendered as bars or cylinders.


+-------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Details                                                                                                                                         |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Possible values                     | Box - Renders the columns as boxes.\                                                                      |
|                                     | Cylinder - Renders the columns as cylinders.                                                              |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Default value                       | Box                                                                                                       |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+
| 2D/3D limitations                   | 3D only                                                                                                   |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Application to chart element        | All series                                                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Application to chart types          | Column chart, Column Range chart, Stacking Column chart, Candle chart, Bar chart, and Stacking Bar chart. |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+


[] 

Column chart with the Column Type property can be created in two ways:

[·      ]Builder

[·      ]ChartModel

 

###### 5.2.1.3.2.1 Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Column chart with the Column Type property through Builder:

1.   In Controller, return View to the Aspx page.

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

[] 

2.   In **View**, invoke the ChartBuilder with the control ID as the first argument.

3.   Create the **Series** and **Points**, and set the style for the chart.

4.   Set the **ColumnType** to **Cylinder**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[ASPX\]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                        |
| [    ][\<%][=][ Html.Chart([\"SimpleChart\"]).Series(series =\>] |
|                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| [    series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column)]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                        |
| [                .Text([\"Server 1\"])]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                        |
| [                .Points(point =\>]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| [                {]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| **[                    point.Add(1, [new] [double]\[\] { 200 });]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| **[                    point.Add(2, [new] [double]\[\] { 500 });]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| **[                    point.Add(3, [new] [double]\[\] { 100 });]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| **[                    point.Add(4, [new] [double]\[\] { 400 });]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| [                })]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| **[                .ConfigItems(configItems =\> {]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| **[                    configItems.ColumnItem(item =\> {                        item.ColumnType(Syncfusion.Windows.Forms.Chart.[ChartColumnType].Cylinder);]**                                                             |
|                                                                                                                                                                                                                                                                                        |
| **[                    });]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| **[                });]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| [})]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [// \-\-\-\-\-\-\-\-\-\-\-\-- Set all styling properties to ChartModel\-\-\-\--][                ]                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [        ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| [    [%\>]][]                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[cshtml\]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [   ][\@{][ Html.Chart([\"SimpleChart\"]).Series(series =\>] |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [    series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column)]                                                                                      |
|                                                                                                                                                                                                                                   |
| [                .Text([\"Server 1\"])]                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [                .Points(point =\>]                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [                {]                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| **[                    point.Add(1, [new] [double]\[\] { 200 });]**                                                                                 |
|                                                                                                                                                                                                                                   |
| **[                    point.Add(2, [new] [double]\[\] { 500 });]**                                                                                 |
|                                                                                                                                                                                                                                   |
| **[                    point.Add(3, [new] [double]\[\] { 100 });]**                                                                                 |
|                                                                                                                                                                                                                                   |
| **[                    point.Add(4, [new] [double]\[\] { 400 });]**                                                                                 |
|                                                                                                                                                                                                                                   |
| [                })]                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| **[                .ConfigItems(configItems =\> {]**                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| **[                    configItems.ColumnItem(item =\> {                        item.ColumnType(Syncfusion.Windows.Forms.Chart.[ChartColumnType].Cylinder);]**        |
|                                                                                                                                                                                                                                   |
| **[                    });]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                   |
| **[                });]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [}).Render();]                                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| [// \-\-\-\-\-\-\-\-\-\-\-\-- Set all styling properties to ChartModel\-\-\-\--][              ]                                            |
|                                                                                                                                                                                                                                   |
| [            [}]][]                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application.

###### 5.2.1.3.2.2 ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Column chart with the Column Type property through ChartModel:

1.   In Controller, create an instance for MVCChartModel.

2.   Create an instance for ChartSeries, add the Points, set any style, and add the Series to the ChartModel.

3.   Set the style for the chart.

4.   Set the ColumnType to Cylinder.

5.   Return the view by setting the ChartModel in the ViewData.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        ][public][ [ActionResult] SimpleChart()]                                              |
|                                                                                                                                                                                                                                                              |
| [        {            ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                 |
|                                                                                                                                                                                                                                                              |
| [            [// Create chart series and add data points to it.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [ChartSeries] series1 = [new] [ChartSeries]([\"Server1\"], [ChartSeriesType].Column);] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| **[            series1.Points.Add(1, 200);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| **[            series1.Points.Add(2, 500);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| **[            series1.Points.Add(3, 100);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| **[            series1.Points.Add(4, 400);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [            ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| **[            series1.ConfigItems.ColumnItem.ColumnType = [ChartColumnType].Cylinder;]**                                                                                                        |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [// Add the series to the chart series collection.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            chartModel.Series.Add(series1);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [// \-\-\-\-\-\-\-\-\-\-\-\-- Set all styling properties to the ChartModel\-\-\-\--][                                ViewData.Model = chartModel;]                     |
|                                                                                                                                                                                                                                                              |
| [                  [return] View();    ]                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [ }][]                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Invoke the ChartBuilder by using the control ID as the first argument, and convert the passed ViewData to **MVCChartModel** and pass it as the second argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[ASPX\]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]][] |
|                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View\[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [  [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

7.   Build and run the application. You will get the following output, now the ColumnType is cylinder.

[] 

{border="0"}

Figure 192: Cylinder Column Type

[] 

See Also

[Column Chart], [Column Range Chart],[ Stacking Column Chart],[ Candle Chart],[ Bar Chart],[ Stacking Bar Chart]

[]{#related-topics}

