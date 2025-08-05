---
title: builder36.md
original_path: WinForms_Docs/99_Uncategorized/builder36.md
created_at: 2025-08-05
---






##### Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Bubble chart with BubbleType through Builder:

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

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [     ][\<%][            [string] accessFileLocation = Server.MapPath([\".\"]);] |
|                                                                                                                                                                                                                                                                            |
| [                  accessFileLocation += [@\"\\Content\\Bubble.png\"];]                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                  System.Drawing.[Bitmap] flower = [new] System.Drawing.[Bitmap](accessFileLocation);]                                                           |
|                                                                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>]                                    |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [//\-\-\-\-\-\-\-\-- Add the Series and set the styling properties that you want\-\-\-\-\--][]                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [            series.Add()]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [                  .Name([\"Technology CCC\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [    .Points(points =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                points.Add(500, 250, 5);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [                points.Add(1000, 391, 2);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [                points.Add(1500, 282, 4);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [                points.Add(2000, 387, 2);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [                points.Add(2500, 251, 4);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            }).Style(style =\>{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| **[                    style.Images(images =\>{]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| **[                            images.Add(flower);]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| **[                });]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [            }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| **[              .ConfigItems(items =\>{]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| **[                    items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Image));]**                                                                                  |
|                                                                                                                                                                                                                                                                            |
| **[                });]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][]                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [   ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [    [%\>]][]                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [     ][\@{][           [string] accessFileLocation = Server.MapPath([\".\"]);]            |
|                                                                                                                                                                                                                                                                                      |
| [                  accessFileLocation += [@\"\\Content\\Bubble.png\"];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [                  System.Drawing.[Bitmap] flower = [new] System.Drawing.[Bitmap](accessFileLocation);]                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [    [}]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [    [\@{] Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>]                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [//\-\-\-\-\-\-\-\-- Add the Series and set the styling properties that you want\-\-\-\-\--][]                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [            series.Add()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| [                  .Name([\"Technology CCC\"])                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [    .Points(points =\>]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [                points.Add(500, 250, 5);]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| [                points.Add(1000, 391, 2);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [                points.Add(1500, 282, 4);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [                points.Add(2000, 387, 2);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [                points.Add(2500, 251, 4);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [            }).Style(style =\>{]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                      |
| **[                    style.Images(images =\>{]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| **[                            images.Add(flower);]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| **[                });]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [            }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| **[              .ConfigItems(items =\>{]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| **[                    items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Image));]**                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| **[                });]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [            })]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [//\-\-\-\-\-\-\-\--Set the ChartModel and ChartArea Properties that you want\-\-\-\-\--][    [}]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 205: Chart displaying Bubble chart Series

[                                                ]

See also

[BubbleChart]

[]{#related-topics}

