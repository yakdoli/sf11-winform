---
title: builder18.md
original_path: WinForms_Docs/99_Uncategorized/builder18.md
created_at: 2025-08-05
---






##### Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Range Area chart through Builder:

1.   In Controller, return view to the corresponding **View** page.

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

3.   Add the **Series** to the ChartModel and set the series type to **RangeArea**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [    ][\<%][=][ Html.Chart([\"SimpleChart\"]).Series(series =\>{] |
|                                                                                                                                                                                                                                                                                         |
| **[    series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].RangeArea)]**                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [                .Text([\"Profit Range\"])]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [                .Style(style =\> {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [                    style.Symbol(symbol =\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [                    {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [                        symbol.Shape(Syncfusion.Windows.Forms.Chart.[ChartSymbolShape].Circle)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                              .Size([new] System.Drawing.[Size](7, 7))]                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [                              .Color(System.Drawing.[Color].DarkBlue);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [                    });]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [                             ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [              }).Points(points =\>]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [                {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(1, 20, 49);]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(2, 18, 52);]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(3, 20, 50);]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(4, 18.5, 53);]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(5, 21, 51);]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(6, 17.7, 54);]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| **[                    points.Add(7, 19, 52);]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [                });]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [            }).Skins([ChartModelSkins].Office2007Blue)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [                  .ChartSeriesSkins([ChartSeriesSkins].Analog)]                                                                                                                                                            |
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
| [            ][}).Size([new] System.Drawing.[Size](500, 400))]                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [              .BorderAppearance(border =\>{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [                  border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [              }).PrimaryYAxis(yaxis =\>{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                  yaxis.Title([\"Profit Range\"]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [              }).PrimaryXAxis(xaxis =\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [              {]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [                  xaxis.Title([\"Year\"]);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [              }).Text([\"Profit Range Per Year\"])        ]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [    [%\>]][]                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                        |
| [    ][\@{][ ][Html.Chart([\"SimpleChart\"]).Series(series =\>{] |
|                                                                                                                                                                                                                                                                                        |
| **[    series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].RangeArea)]**                                                                                                                                    |
|                                                                                                                                                                                                                                                                                        |
| [                .Text([\"Profit Range\"])]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| [                .Style(style =\> {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [                    style.Symbol(symbol =\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| [                    {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                        |
| [                        symbol.Shape(Syncfusion.Windows.Forms.Chart.[ChartSymbolShape].Circle)]                                                                                                                           |
|                                                                                                                                                                                                                                                                                        |
| [                              .Size([new] System.Drawing.[Size](7, 7))]                                                                                                                              |
|                                                                                                                                                                                                                                                                                        |
| [                              .Color(System.Drawing.[Color].DarkBlue);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [                    });]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                        |
| [                             ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                        |
| [              }).Points(points =\>]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [                {]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(1, 20, 49);]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(2, 18, 52);]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(3, 20, 50);]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(4, 18.5, 53);]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(5, 21, 51);]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(6, 17.7, 54);]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| **[                    points.Add(7, 19, 52);]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [                });]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                        |
| [            }).Skins([ChartModelSkins].Office2007Blue)]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                        |
| [                  .ChartSeriesSkins([ChartSeriesSkins].Analog)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                        |
| [              .ShowLegend([true])]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                        |
| [              .LegendsPlacement(Syncfusion.Windows.Forms.Chart.[ChartPlacement].Outside)]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| [              .LegendPosition(Syncfusion.Windows.Forms.Chart.[ChartDock].Top)]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                        |
| [              .Legend(legend =\>{]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                        |
| [                  legend.Alignment(Syncfusion.Windows.Forms.Chart.[ChartAlignment].Center);]                                                                                                                              |
|                                                                                                                                                                                                                                                                                        |
| [            ][}).Size([new] System.Drawing.[Size](500, 400))]                                                                                                    |
|                                                                                                                                                                                                                                                                                        |
| [              .BorderAppearance(border =\>{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                        |
| [                  border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                                                                        |
|                                                                                                                                                                                                                                                                                        |
| [              }).PrimaryYAxis(yaxis =\>{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                        |
| [                  yaxis.Title([\"Profit Range\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                        |
| [              }).PrimaryXAxis(xaxis =\>]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                        |
| [              {]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                        |
| [                  xaxis.Title([\"Year\"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [              }).Text([\"Profit Range Per Year\"])]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                        |
| [             .Render();        ]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                        |
| [    [}]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

[] 

Figure 107: Range Area chart

[] 

[]{#related-topics}

