---
title: builder4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder4.md
created_at: 2025-07-03
---






##### Builder {#builder style="tab-stops: 0pt"}

 

To create a Stacking Bar chart through Builder:

 

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

3.   Add the **Series** to the ChartModel and set the series type to **StackingBar**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[ASPX\]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [    ][\<%][=][ Html.Chart([\"SimpleChart\"]).Series(series =\>{] |
|                                                                                                                                                                                                                                                                                         |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StackingBar)**]                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [                                .Text([\"Server 1\"])]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [                                .Points(points =\>]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [                                {]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(15, 225);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(3, 325);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(7, 275);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(11, 350);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                                });]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StackingBar)**]                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [                                .Text([\"Server 2\"])]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [                                .Points(points =\>]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [                                {]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(15, 325);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(3, 355);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(7, 315);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                         |
| [                                    points.Add(11, 300);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                                });]                                                                                                                                                                                                               |
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
| [              }).PrimaryYAxis(yaxis =\>{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                  yaxis.Title([\"Peak Load (Hr)\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                         |
| [              }).PrimaryXAxis(xaxis =\>{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [                  xaxis.Title([\"Server Load (MB)\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [              }).Text([\"Peak Average Network Load\"])]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [        ]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                         |
| [    [%\>]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [\@{][ ][Html.Chart([\"SimpleChart\"]).Series(series =\>{]              |
|                                                                                                                                                                                                                                 |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StackingBar)**]                                                           |
|                                                                                                                                                                                                                                 |
| [                                .Text([\"Server 1\"])]                                                                                                             |
|                                                                                                                                                                                                                                 |
| [                                .Points(points =\>]                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [                                {]                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(15, 225);]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(3, 325);]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(7, 275);]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(11, 350);]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                                });]                                                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [                    **series.Add().Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].StackingBar)**]                                                           |
|                                                                                                                                                                                                                                 |
| [                                .Text([\"Server 2\"])]                                                                                                             |
|                                                                                                                                                                                                                                 |
| [                                .Points(points =\>]                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [                                {]                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(15, 325);]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(3, 355);]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(7, 315);]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [                                    points.Add(11, 300);]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                                });]                                                                                                                                                       |
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
| [              }).PrimaryYAxis(yaxis =\>{]                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                  yaxis.Title([\"Peak Load (Hr)\"]);]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [              }).PrimaryXAxis(xaxis =\>{]                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                  xaxis.Title([\"Server Load (MB)\"]);]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [              }).Text([\"Peak Average Network Load\"])][            ]                                                          |
|                                                                                                                                                                                                                                 |
| [              .Render();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [        ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [              [}]][                                      ][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application, to get the following output:

 

{border="0"}

Figure 79: Stacking Bar chart

[]{#related-topics}

