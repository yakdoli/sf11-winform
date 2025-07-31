---
title: builder22.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder22.md
created_at: 2025-07-03
---






##### Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Bubble chart through Builder:

1.   In Controller, return view to the corresponding View page.

[] 


\[C#\]

[        [public] [ActionResult] SimpleChart()]

[        {            ]

[            [return] View();]

[        }]


[] 

2.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the **ChartModel** and set the series type to **Bubble**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [    [\<%]            [string] accessFileLocation = Server.MapPath([\".\"]);]                                              |
|                                                                                                                                                                                                                                         |
| [                  accessFileLocation += [@\"\\Content\\Bubble.png\"];]                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                  System.Drawing.[Bitmap] flower = [new] System.Drawing.[Bitmap](accessFileLocation);]                        |
|                                                                                                                                                                                                                                         |
| [    ][%\>][]                                                                              |
|                                                                                                                                                                                                                                         |
| [    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                                         |
| [        {            **series.Add()**]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [                  .Name([\"Technology AAA\"])]                                                                                                                             |
|                                                                                                                                                                                                                                         |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]**                                                                                      |
|                                                                                                                                                                                                                                         |
| [                  .Points(points =\>{]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(500, 356, 3);]**                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(1000, 491, 4);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(1500, 382, 3);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(2000, 437, 3);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(2500, 351, 4);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                                           |
|                                                                                                                                                                                                                                         |
| [                  .ScatterSplineTension(0)]                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [                  .ConfigItems(items =\>{]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                        items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Circle));                  ]                            |
|                                                                                                                                                                                                                                         |
| [                  });         ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [            **series.Add()**]                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [                  .Name([\"Technology BBB\"])]                                                                                                                             |
|                                                                                                                                                                                                                                         |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]**                                                                                      |
|                                                                                                                                                                                                                                         |
| [                  .Points(points =\>{]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(500, 175, 4);]**                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(1000, 291, 3);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(1500, 182, 2);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(2000, 237, 4);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| **[                            points.Add(2500, 151, 4);]**                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                                           |
|                                                                                                                                                                                                                                         |
| [                  .ScatterSplineTension(0)]                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [                  .ConfigItems(items =\>{]                                                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [                    items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Circle));               ]                                   |
|                                                                                                                                                                                                                                         |
| [                });]                                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| **[            series.Add()]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [                  .Name([\"Technology CCC\"])]                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [                  **.Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble**)]                                                                                      |
|                                                                                                                                                                                                                                         |
| [    .Points(points =\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| **[                points.Add(500, 250, 5);]**                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| **[                points.Add(1000, 391, 2);]**                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| **[                points.Add(1500, 282, 4);]**                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| **[                points.Add(2000, 387, 2);]**                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| **[                points.Add(2500, 251, 4);]**                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [            }).Style(style =\>{]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                    style.Images(images =\>{]                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [                            images.Add(flower);]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                });]                                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [            }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                                               |
|                                                                                                                                                                                                                                         |
| [              .ConfigItems(items =\>{]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [                    items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Image));]                                                   |
|                                                                                                                                                                                                                                         |
| [                });]                                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [            }).BorderAppearance(border =\>{                    border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                            |
|                                                                                                                                                                                                                                         |
| [            ][}).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                                       |
|                                                                                                                                                                                                                                         |
| [              .ElementsSpacing(5)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [              .Size([new] System.Drawing.[Size](500,400))]                                                                                            |
|                                                                                                                                                                                                                                         |
| [              .Skins([ChartModelSkins].Office2007Blue)]                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [              .ChartSeriesSkins([ChartSeriesSkins].Analog)   ]                                                                                                             |
|                                                                                                                                                                                                                                         |
| [    [%\>]][]                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [    [\@{]            [string] accessFileLocation = Server.MapPath([\".\"]);]                       |
|                                                                                                                                                                                                                  |
| [                  accessFileLocation += [@\"\\Content\\Bubble.png\"];]                                                                              |
|                                                                                                                                                                                                                  |
| [                  System.Drawing.[Bitmap] flower = [new] System.Drawing.[Bitmap](accessFileLocation);] |
|                                                                                                                                                                                                                  |
| [    ][}][]                                                         |
|                                                                                                                                                                                                                  |
| [    [\@{] Html.Chart([\"chart_Model\"]).Text([\"Product Comparison Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                  |
| [        {]                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [            **series.Add()**]                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [                  .Name([\"Technology AAA\"])]                                                                                                      |
|                                                                                                                                                                                                                  |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]**                                                               |
|                                                                                                                                                                                                                  |
| [                  .Points(points =\>{]                                                                                                                                      |
|                                                                                                                                                                                                                  |
| **[                            points.Add(500, 356, 3);]**                                                                                                                   |
|                                                                                                                                                                                                                  |
| **[                            points.Add(1000, 491, 4);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| **[                            points.Add(1500, 382, 3);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| **[                            points.Add(2000, 437, 3);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| **[                            points.Add(2500, 351, 4);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                    |
|                                                                                                                                                                                                                  |
| [                  .ScatterSplineTension(0)]                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [                  .ConfigItems(items =\>{]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                        items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Circle));                  ]     |
|                                                                                                                                                                                                                  |
| [                  });         ]                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [            **series.Add()**]                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [                  .Name([\"Technology BBB\"])]                                                                                                      |
|                                                                                                                                                                                                                  |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble)]**                                                               |
|                                                                                                                                                                                                                  |
| [                  .Points(points =\>{]                                                                                                                                      |
|                                                                                                                                                                                                                  |
| **[                            points.Add(500, 175, 4);]**                                                                                                                   |
|                                                                                                                                                                                                                  |
| **[                            points.Add(1000, 291, 3);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| **[                            points.Add(1500, 182, 2);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| **[                            points.Add(2000, 237, 4);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| **[                            points.Add(2500, 151, 4);]**                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                    |
|                                                                                                                                                                                                                  |
| [                  .ScatterSplineTension(0)]                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [                  .ConfigItems(items =\>{]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [                    items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Circle));               ]            |
|                                                                                                                                                                                                                  |
| [                });]                                                                                                                                                        |
|                                                                                                                                                                                                                  |
| **[            series.Add()]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [                  .Name([\"Technology CCC\"])]                                                                                                      |
|                                                                                                                                                                                                                  |
| [                  **.Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Bubble**)]                                                               |
|                                                                                                                                                                                                                  |
| [    .Points(points =\>]                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [            {]                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| **[                points.Add(500, 250, 5);]**                                                                                                                               |
|                                                                                                                                                                                                                  |
| **[                points.Add(1000, 391, 2);]**                                                                                                                              |
|                                                                                                                                                                                                                  |
| **[                points.Add(1500, 282, 4);]**                                                                                                                              |
|                                                                                                                                                                                                                  |
| **[                points.Add(2000, 387, 2);]**                                                                                                                              |
|                                                                                                                                                                                                                  |
| **[                points.Add(2500, 251, 4);]**                                                                                                                              |
|                                                                                                                                                                                                                  |
| [            }).Style(style =\>{]                                                                                                                                            |
|                                                                                                                                                                                                                  |
| [                    style.Images(images =\>{]                                                                                                                               |
|                                                                                                                                                                                                                  |
| [                            images.Add(flower);]                                                                                                                            |
|                                                                                                                                                                                                                  |
| [                });]                                                                                                                                                        |
|                                                                                                                                                                                                                  |
| [            }).ScatterConnectType(Syncfusion.Windows.Forms.Chart.[ScatterConnectType].None)]                                                        |
|                                                                                                                                                                                                                  |
| [              .ConfigItems(items =\>{]                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [                    items.BubbleItem(item =\> item.BubbleType(Syncfusion.Windows.Forms.Chart.[ChartBubbleType].Image));]                            |
|                                                                                                                                                                                                                  |
| [                });]                                                                                                                                                        |
|                                                                                                                                                                                                                  |
| [            }).BorderAppearance(border =\>{                    border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]     |
|                                                                                                                                                                                                                  |
| [            ][}).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                |
|                                                                                                                                                                                                                  |
| [              .ElementsSpacing(5)]                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [              .Size([new] System.Drawing.[Size](500,400))]                                                                     |
|                                                                                                                                                                                                                  |
| [              .Skins([ChartModelSkins].Office2007Blue)]                                                                                             |
|                                                                                                                                                                                                                  |
| [              .ChartSeriesSkins([ChartSeriesSkins].Analog)    ]                                                                                     |
|                                                                                                                                                                                                                  |
| [           .Render();]                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [    [}]]                                                                                                                                        |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 123: Chart displaying Bubble chart Series

[                                ]

[]{#related-topics}

