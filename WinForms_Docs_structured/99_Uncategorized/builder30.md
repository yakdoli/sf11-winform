---
title: builder30.md
original_path: WinForms_Docs/99_Uncategorized/builder30.md
created_at: 2025-08-05
---






##### Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Box and Whisker chart through Builder:

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

2.   In the **View** page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **BoxAndWhisker**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"Box and Whisker Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| **[            series.Add()]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| **[                  .Name([\"Analysis\"])]**                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].BoxAndWhisker)                  ]**                                                          |
|                                                                                                                                                                                                                                                   |
| **[                  .Points(points =\>]**                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| **[                  {                      ]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| **[                      points.Add(1, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140);]**                                                                                                          |
|                                                                                                                                                                                                                                                   |
| **[                      points.Add(2, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130);]**                                                                                                           |
|                                                                                                                                                                                                                                                   |
| **[                      points.Add(3, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120);]**                                                                                                            |
|                                                                                                                                                                                                                                                   |
| **[                      points.Add(4, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110);]**                                                                                                             |
|                                                                                                                                                                                                                                                   |
| **[                      points.Add(5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100);]**                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [                  });]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [        }).BorderAppearance(border =\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                                            |
|                                                                                                                                                                                                                                                   |
| [        }).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                                                                                           |
|                                                                                                                                                                                                                                                   |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                                        |
|                                                                                                                                                                                                                                                   |
| [              .Skins([ChartModelSkins].Office2007Blue)]                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [              .ChartSeriesSkins([ChartSeriesSkins].Analog) ]                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [              .Series3D([true])                          ]                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| [        [%\>][]]                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [    [\@{] Html.Chart([\"chart_Model\"]).Text([\"Box and Whisker Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                               |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                            |
| **[            series.Add()]**                                                                                                                                            |
|                                                                                                                                                                                                                            |
| **[                  .Name([\"Analysis\"])]**                                                                                                     |
|                                                                                                                                                                                                                            |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].BoxAndWhisker)                  ]**                                   |
|                                                                                                                                                                                                                            |
| **[                  .Points(points =\>]**                                                                                                                                |
|                                                                                                                                                                                                                            |
| **[                  {                      ]**                                                                                                                           |
|                                                                                                                                                                                                                            |
| **[                      points.Add(1, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140);]**                                                                                   |
|                                                                                                                                                                                                                            |
| **[                      points.Add(2, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130);]**                                                                                    |
|                                                                                                                                                                                                                            |
| **[                      points.Add(3, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120);]**                                                                                     |
|                                                                                                                                                                                                                            |
| **[                      points.Add(4, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110);]**                                                                                      |
|                                                                                                                                                                                                                            |
| **[                      points.Add(5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100);]**                                                                                       |
|                                                                                                                                                                                                                            |
| [                  });]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        }).BorderAppearance(border =\>]                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]                                                     |
|                                                                                                                                                                                                                            |
| [        }).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                                                                    |
|                                                                                                                                                                                                                            |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                 |
|                                                                                                                                                                                                                            |
| [              .Skins([ChartModelSkins].Office2007Blue)]                                                                                          |
|                                                                                                                                                                                                                            |
| [              .ChartSeriesSkins([ChartSeriesSkins].Analog) ]                                                                                     |
|                                                                                                                                                                                                                            |
| [             .Series3D([true])]                                                                                                                     |
|                                                                                                                                                                                                                            |
| [             .Render();                         ]                                                                                                                        |
|                                                                                                                                                                                                                            |
| [        [}][]]                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 139: Chart displaying Box and Whisker chart Series

[] 

[]{#related-topics}

