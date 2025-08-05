---
title: builder8.md
original_path: WinForms_Docs/99_Uncategorized/builder8.md
created_at: 2025-08-05
---






##### Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Tornado chart through Builder:

1.   In Controller, return view to the corresponding **View** page.

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

2.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Tornado**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [      [\<%][=] Html.Chart([\"SimpleChart\"]).Series(series =\>{]                                                              |
|                                                                                                                                                                                                                                             |
| **[    series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Tornado)]**                                                                                           |
|                                                                                                                                                                                                                                             |
| [                .Text([\"Male\"])]                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [                .Points(points =\>]                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                    points.Add(1, -50, -12);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(2, -50, -91);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(3, -50, -397);]                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [                    points.Add(4, -50, -1072);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(5, -50, -2117);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(6, -50, -3094);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(7, -50, -3804);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(8, -50, -4712);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(9, -50, -6203);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(10, -50, -8415);]                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [                    points.Add(11, -50, -9771);]                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [                });]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Tornado)**]                                                                                           |
|                                                                                                                                                                                                                                             |
| [                .Text([\"Female\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [                .Points(points =\>]                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                    points.Add(1, 50, 58);]                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [                    points.Add(2, 50, 321);]                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [                    points.Add(3, 50, 1034);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(4, 50, 2135);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(5, 50, 3459);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(6, 50, 4282);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(7, 50, 4697);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(8, 50, 5412);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(9, 50, 6814);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(10, 50, 8944);]                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [                    points.Add(11, 50, 10212);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                });]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [            }).Skins([ChartModelSkins].Office2007Blue)]                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [              ][.ChartSeriesSkins([ChartSeriesSkins].Analog)]                                                                              |
|                                                                                                                                                                                                                                             |
| [              .Font([new] System.Drawing.[Font]([\"Verdana\"], 12, System.Drawing.[FontStyle].Bold))    ] |
|                                                                                                                                                                                                                                             |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                                               |
|                                                                                                                                                                                                                                             |
| [              .BorderAppearance(border =\>{]                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [                  border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                             |
|                                                                                                                                                                                                                                             |
| [              }).PrimaryYAxis(yaxis =\>{]                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [                  yaxis.Title([\"Age\"])]                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [                       .DrawGrid([false]);                      ]                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [              }).PrimaryXAxis(xaxis =\>{]                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [                  xaxis.Title([\"Population Projection\"])]                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                       .DrawGrid([false]);]                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [              }).Text([\"Year 2009 Population Projections by Gender and Age\"])]                                                                                               |
|                                                                                                                                                                                                                                             |
| [        ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [    [%\>]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\] ]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [\@{][ ][Html.Chart([\"SimpleChart\"]).Series(series =\>{]                          |
|                                                                                                                                                                                                                                             |
| **[    series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Tornado)]**                                                                                           |
|                                                                                                                                                                                                                                             |
| [                .Text([\"Male\"])]                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [                .Points(points =\>]                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                    points.Add(1, -50, -12);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(2, -50, -91);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(3, -50, -397);]                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [                    points.Add(4, -50, -1072);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(5, -50, -2117);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(6, -50, -3094);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(7, -50, -3804);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(8, -50, -4712);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(9, -50, -6203);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                    points.Add(10, -50, -8415);]                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [                    points.Add(11, -50, -9771);]                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [                });]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Tornado)**]                                                                                           |
|                                                                                                                                                                                                                                             |
| [                .Text([\"Female\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [                .Points(points =\>]                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [                    points.Add(1, 50, 58);]                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [                    points.Add(2, 50, 321);]                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [                    points.Add(3, 50, 1034);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(4, 50, 2135);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(5, 50, 3459);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(6, 50, 4282);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(7, 50, 4697);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(8, 50, 5412);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(9, 50, 6814);]                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| [                    points.Add(10, 50, 8944);]                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [                    points.Add(11, 50, 10212);]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                });]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [            }).Skins([ChartModelSkins].Office2007Blue)]                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [              ][.ChartSeriesSkins([ChartSeriesSkins].Analog)]                                                                              |
|                                                                                                                                                                                                                                             |
| [              .Font([new] System.Drawing.[Font]([\"Verdana\"], 12, System.Drawing.[FontStyle].Bold))    ] |
|                                                                                                                                                                                                                                             |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                                               |
|                                                                                                                                                                                                                                             |
| [              .BorderAppearance(border =\>{]                                                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [                  border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                             |
|                                                                                                                                                                                                                                             |
| [              }).PrimaryYAxis(yaxis =\>{]                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [                  yaxis.Title([\"Age\"])]                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [                       .DrawGrid([false]);                      ]                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [              }).PrimaryXAxis(xaxis =\>{]                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [                  xaxis.Title([\"Population Projection\"])]                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                       .DrawGrid([false]);]                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [              }).Text([\"Year 2009 Population Projections by Gender and Age\"])][         ]                                                |
|                                                                                                                                                                                                                                             |
| [              .Render();]                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [        ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [              [}]][                                      ][]             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 87: Chart Displaying Tornado Series

[]{#related-topics}

