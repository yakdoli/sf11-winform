---
title: builder27.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder27.md
created_at: 2025-07-03
---






##### Builder {#builder style="tab-stops: 0pt"}

 

The steps to create a Point and Figure chart through Builder are as follows:

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

3.   Add the **Series** to the ChartModel and set the series type to **PointAndFigure**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

[] 


[ **View**]**\[ASPX\]**

[\<%][]

[    [double]\[\] points1 = {   35.250,37.750,39.000,38.275,37.750,37.750,37.275,36.250,35.750,35.250,36.250,35.250,34.500,]

[                                          35.625,35.500,36.625,36.275,36.250,36.875,37.250,36.875,36.500,37.125,36.275,35.875,36.625,]

[                                          27.125,26.250,27.000,27.250,37.500,38.500,39.500,38.875,38.500,39.000,38.500,28.500,29.000,]

[                                          29.000,40.000,29.875,29.875,28.875,28.500,28.250,28.875,29.275,29.275,29.750,29.500,29.275,]

[                                          28.500,27.750,27.625,27.500,26.500,25.000,26.625,26.000,25.875,25.000,25.250,25.125,25.050};]

[] 

[    [double]\[\] points2 = {   25,27.500,28.750,28.025,27.500,27.500,27.025,26.250,35.750,35.250,36.250,35.250,34.500,]

[                                           25.625,25.500,26.625,26.275,26.250,26.875,27.250,26.875,26.500,27.125,26.275,25.875,26.625,]

[                                           27.125,26.250,27.000,27.250,27.500,38.500,39.500,38.875,38.500,39.000,28.500,28.500,29.000,]

[                                           29.000,40.000,29.875,29.875,28.875,28.500,28.250,28.875,29.275,29.275,29.750,29.500,29.275,]

[                                           28.500,27.750,27.625,27.500,26.500,25.000,26.625,26.000,25.875,25.000,25.250,25.125,25.050};]

[] 

[] 

[    [DateTime] current = [new] [DateTime](2004, 01, 1);]

[    [int] numPoints = points1.Length;]

[%\>][]

[    [\<%][=]Html.Chart([\"chart_Model\"]).Text([\"Point and Figure Chart\"]).Series(series =\>]

[        {]

[] 

**[            series.Add()]**

**[                  .Name([\"FT\"])]**

**[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].PointAndFigure)]**

[                  .ReversalAmount(0.0)]

[                  .Points(points =\>]

[                  {]

**[                      [for] ([int] j = 0; j \< numPoints; j++)]**

**[                          points.Add(current.AddDays(j), [new] [double]\[\] { points1\[j\], points2\[j\] });]**

[                  })]

[                  .ConfigItems(item =\>]

[                  {]

[                      item.FinancialItem(financialitem =\>]

[                      {]

[                          financialitem.PriceUpColor(System.Drawing.[Color].SkyBlue)]

[                                       .PriceDownColor(System.Drawing.[Color].FromArgb(33, 76, 129));]

[                      });]

[                  });]

[        }).BorderAppearance(border =\>]

[        {]

[            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]

[        }).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]

[              .Size([new] System.Drawing.[Size](500, 400))]

[              .Skins([ChartModelSkins].Office2007Blue)]

[              .ChartSeriesSkins([ChartSeriesSkins].Analog)                            ]

[              .PrimaryXAxis(xaxis =\>]

[              {]

[                  xaxis.Title([\"Week Day\"])]

[                       .ValueType(Syncfusion.Windows.Forms.Chart.[ChartValueType].DateTime)]

[                       .DateTimeFormat([\"MMM/dd\"])]

[                       .DateTimeRange([new] Syncfusion.Windows.Forms.Chart.[ChartDateTimeRange](current, current.AddDays(30), 10, Syncfusion.Windows.Forms.Chart.[ChartDateTimeIntervalType].Days))]

[                       .IntervalType(Syncfusion.Windows.Forms.Chart.[ChartDateTimeIntervalType].Months)                       ]

[              ][         .LabelRotate([true])]

[                       .LabelRotateAngle(270);                       ]

[              }).PrimaryYAxis(yaxis =\> {]

[                  yaxis.Title([\"Price (\$)\"]);                       ]

[              })]

[] 

[    ]

[    [%\>]]


 


[ **View**]**\[cshtml\]**

[\@{][]

[    [double]\[\] points1 = {   35.250,37.750,39.000,38.275,37.750,37.750,37.275,36.250,35.750,35.250,36.250,35.250,34.500,]

[                                          35.625,35.500,36.625,36.275,36.250,36.875,37.250,36.875,36.500,37.125,36.275,35.875,36.625,]

[                                          27.125,26.250,27.000,27.250,37.500,38.500,39.500,38.875,38.500,39.000,38.500,28.500,29.000,]

[                                          29.000,40.000,29.875,29.875,28.875,28.500,28.250,28.875,29.275,29.275,29.750,29.500,29.275,]

[                                          28.500,27.750,27.625,27.500,26.500,25.000,26.625,26.000,25.875,25.000,25.250,25.125,25.050};]

[] 

[    [double]\[\] points2 = {   25,27.500,28.750,28.025,27.500,27.500,27.025,26.250,35.750,35.250,36.250,35.250,34.500,]

[                                           25.625,25.500,26.625,26.275,26.250,26.875,27.250,26.875,26.500,27.125,26.275,25.875,26.625,]

[                                           27.125,26.250,27.000,27.250,27.500,38.500,39.500,38.875,38.500,39.000,28.500,28.500,29.000,]

[                                           29.000,40.000,29.875,29.875,28.875,28.500,28.250,28.875,29.275,29.275,29.750,29.500,29.275,]

[                                           28.500,27.750,27.625,27.500,26.500,25.000,26.625,26.000,25.875,25.000,25.250,25.125,25.050};]

[] 

[] 

[    [DateTime] current = [new] [DateTime](2004, 01, 1);]

[    [int] numPoints = points1.Length;]

[}][]

[    [\@{] Html.Chart([\"chart_Model\"]).Text([\"Point and Figure Chart\"]).Series(series =\>]

[        {]

[] 

**[            series.Add()]**

**[                  .Name([\"FT\"])]**

**[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].PointAndFigure)]**

[                  .ReversalAmount(0.0)]

[                  .Points(points =\>]

[                  {]

**[                      [for] ([int] j = 0; j \< numPoints; j++)]**

**[                          points.Add(current.AddDays(j), [new] [double]\[\] { points1\[j\], points2\[j\] });]**

[                  })]

[                  .ConfigItems(item =\>]

[                  {]

[                      item.FinancialItem(financialitem =\>]

[                      {]

[                          financialitem.PriceUpColor(System.Drawing.[Color].SkyBlue)]

[                                       .PriceDownColor(System.Drawing.[Color].FromArgb(33, 76, 129));]

[                      });]

[                  });]

[        }).BorderAppearance(border =\>]

[        {]

[            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]

[        }).SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]

[              .Size([new] System.Drawing.[Size](500, 400))]

[              .Skins([ChartModelSkins].Office2007Blue)]

[              .ChartSeriesSkins([ChartSeriesSkins].Analog)                            ]

[              .PrimaryXAxis(xaxis =\>]

[              {]

[                  xaxis.Title([\"Week Day\"])]

[                       .ValueType(Syncfusion.Windows.Forms.Chart.[ChartValueType].DateTime)]

[                       .DateTimeFormat([\"MMM/dd\"])]

[                       .DateTimeRange([new] Syncfusion.Windows.Forms.Chart.[ChartDateTimeRange](current, current.AddDays(30), 10, Syncfusion.Windows.Forms.Chart.[ChartDateTimeIntervalType].Days))]

[                       .IntervalType(Syncfusion.Windows.Forms.Chart.[ChartDateTimeIntervalType].Months)                       ]

[              ][         .LabelRotate([true])]

[                       .LabelRotateAngle(270);                       ]

[              }).PrimaryYAxis(yaxis =\> {]

[                  yaxis.Title([\"Price (\$)\"]);                       ]

[              })]

[           .Render();]

[    ]

[    [}]]


 

 

5.   [Build and run the application, to get the following output:]

[] 

[] 

{border="0"}

[] 

Figure 133: Chart displaying Point and Figure chart Series[ ]

**[]** 

[]{#related-topics}

