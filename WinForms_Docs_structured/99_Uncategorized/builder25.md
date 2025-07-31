---
title: builder25.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder25.md
created_at: 2025-07-03
---






##### Builder {#builder style="tab-stops: 0pt"}

 

To create a HiLoOpenClose chart through Builder:

1.   In Controller, return view to the corresponding View page.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                        |
|                                                                                                                                               |
| [        [public] [ActionResult] SimpleChart()] |
|                                                                                                                                               |
| [        {            ]                                                                      |
|                                                                                                                                               |
| [            [return] View();]                                          |
|                                                                                                                                               |
| [        }]                                                                                  |
|                                                                                                                                               |
| []                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **HiLoOpenClose**, and add the **Points** to the series and set the style.

4.   Set the **ChartModel** and **ChartArea** properties.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [   [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"HiLo Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| **[            series.Add()]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| [                  .Name([\"FT\"])]                                                                                                                          |
|                                                                                                                                                                                                                          |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].HiLoOpenClose)]**                                                                |
|                                                                                                                                                                                                                          |
| [                  .Points(points =\>]                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [                  {]                                                                                                                                                                |
|                                                                                                                                                                                                                          |
| [                      [DateTime] start = [new] [DateTime](2006, 2, 12);]                                       |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(0), 456, 214, 364, 386);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(1), 491, 234, 321, 378);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(2), 482, 193, 302, 352);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(3), 437, 243, 354, 391);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(4), 421, 223, 317, 367);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(5), 434, 263, 339, 385);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(6), 425, 245, 365, 396);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(7), 457, 234, 385, 398);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(8), 482, 267, 316, 389);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| **[                      points.Add(start.AddDays(9), 496, 285, 374, 399);]**                                                                                                        |
|                                                                                                                                                                                                                          |
| [                  });]                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [        }).BorderAppearance(border =\>]                                                                                                                                             |
|                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].][Pinned);]                          |
|                                                                                                                                                                                                                          |
| [        }).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                                                                               |
|                                                                                                                                                                                                                          |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                                            |
|                                                                                                                                                                                                                          |
| [              .Skins([ChartModelSkins].Office2007Blue)]                                                                                                     |
|                                                                                                                                                                                                                          |
| [              .ChartSeriesSkins([ChartSeriesSkins].Analog)]                                                                                                 |
|                                                                                                                                                                                                                          |
| [              .Indexed([true])]                                                                                                                                |
|                                                                                                                                                                                                                          |
| [              .PrimaryXAxis(xaxis =\>]                                                                                                                                              |
|                                                                                                                                                                                                                          |
| [              {]                                                                                                                                                                    |
|                                                                                                                                                                                                                          |
| [                  xaxis.Title([\"Week Day\"])]                                                                                                              |
|                                                                                                                                                                                                                          |
| [                       .ValueType(Syncfusion.Windows.Forms.Chart.[ChartValueType].DateTime)]                                                                |
|                                                                                                                                                                                                                          |
| [                       .DateTimeFormat([\"MMM/dd\"])]                                                                                                       |
|                                                                                                                                                                                                                          |
| [                       .DrawGrid([false])]                                                                                                                     |
|                                                                                                                                                                                                                          |
| [                       .LabelRotate([true])]                                                                                                                   |
|                                                                                                                                                                                                                          |
| [                       .LabelRotateAngle(270)]                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [                       .HidePartialLabels([true]);]                                                                                                            |
|                                                                                                                                                                                                                          |
| [              }).PrimaryYAxis(yaxis =\> {]                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [                  yaxis.Title([\"Price (\$)\"])]                                                                                                            |
|                                                                                                                                                                                                                          |
| [                       .DrawGrid([false]);]                                                                                                                    |
|                                                                                                                                                                                                                          |
| [              })   ]                                                                                                                                                                |
|                                                                                                                                                                                                                          |
| [    [%\>]][]                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**[]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [   [\@{] Html.Chart([\"chart_Model\"]).Text([\"HiLo Chart\"]).Series(series =\>] |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| **[            series.Add()]**                                                                                                                                |
|                                                                                                                                                                                                   |
| [                  .Name([\"FT\"])]                                                                                                   |
|                                                                                                                                                                                                   |
| **[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].HiLoOpenClose)]**                                         |
|                                                                                                                                                                                                   |
| [                  .Points(points =\>]                                                                                                                        |
|                                                                                                                                                                                                   |
| [                  {]                                                                                                                                         |
|                                                                                                                                                                                                   |
| [                      [DateTime] start = [new] [DateTime](2006, 2, 12);]                |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(0), 456, 214, 364, 386);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(1), 491, 234, 321, 378);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(2), 482, 193, 302, 352);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(3), 437, 243, 354, 391);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(4), 421, 223, 317, 367);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(5), 434, 263, 339, 385);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(6), 425, 245, 365, 396);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(7), 457, 234, 385, 398);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(8), 482, 267, 316, 389);]**                                                                                 |
|                                                                                                                                                                                                   |
| **[                      points.Add(start.AddDays(9), 496, 285, 374, 399);]**                                                                                 |
|                                                                                                                                                                                                   |
| [                  });]                                                                                                                                       |
|                                                                                                                                                                                                   |
| [        }).BorderAppearance(border =\>]                                                                                                                      |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                                   |
|                                                                                                                                                                                                   |
| [            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].][Pinned);]   |
|                                                                                                                                                                                                   |
| [        }).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                                                        |
|                                                                                                                                                                                                   |
| [              .Size([new] System.Drawing.[Size](500, 400))]                                                     |
|                                                                                                                                                                                                   |
| [              .Skins([ChartModelSkins].Office2007Blue)]                                                                              |
|                                                                                                                                                                                                   |
| [              .ChartSeriesSkins([ChartSeriesSkins].Analog)]                                                                          |
|                                                                                                                                                                                                   |
| [              .Indexed([true])]                                                                                                         |
|                                                                                                                                                                                                   |
| [              .PrimaryXAxis(xaxis =\>]                                                                                                                       |
|                                                                                                                                                                                                   |
| [              {]                                                                                                                                             |
|                                                                                                                                                                                                   |
| [                  xaxis.Title([\"Week Day\"])]                                                                                       |
|                                                                                                                                                                                                   |
| [                       .ValueType(Syncfusion.Windows.Forms.Chart.[ChartValueType].DateTime)]                                         |
|                                                                                                                                                                                                   |
| [                       .DateTimeFormat([\"MMM/dd\"])]                                                                                |
|                                                                                                                                                                                                   |
| [                       .DrawGrid([false])]                                                                                              |
|                                                                                                                                                                                                   |
| [                       .LabelRotate([true])]                                                                                            |
|                                                                                                                                                                                                   |
| [                       .LabelRotateAngle(270)]                                                                                                               |
|                                                                                                                                                                                                   |
| [                       .HidePartialLabels([true]);]                                                                                     |
|                                                                                                                                                                                                   |
| [              }).PrimaryYAxis(yaxis =\> {]                                                                                                                   |
|                                                                                                                                                                                                   |
| [                  yaxis.Title([\"Price (\$)\"])]                                                                                     |
|                                                                                                                                                                                                   |
| [                       .DrawGrid([false]);]                                                                                             |
|                                                                                                                                                                                                   |
| [              })    ]                                                                                                                                        |
|                                                                                                                                                                                                   |
| [           .Render();]                                                                                                                                       |
|                                                                                                                                                                                                   |
| [    [}]][]                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}[]

[] 

Figure 129: Chart displaying HiLoOpenClose chart Series

[] 

[]{#related-topics}

