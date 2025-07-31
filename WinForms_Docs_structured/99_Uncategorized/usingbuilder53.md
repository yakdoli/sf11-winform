---
title: usingbuilder53.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder53.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using Builder {#using-builder style="tab-stops: 0pt"}

[] 

The steps to create a Combination chart through Builder are as follows:

1.   In Controller, return view to the corresponding View page.

 

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                          |
|                                                                                                                                                       |
| [public] [ [ActionResult] SimpleChart()] |
|                                                                                                                                                       |
| [{ ]                                                                                                              |
|                                                                                                                                                       |
| [return] [ View();]                                              |
|                                                                                                                                                       |
| [}]                                                                                                               |
|                                                                                                                                                       |
| []                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Line** and **Column**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [    [\<%][=] Html.MobSyncfusion().Chart(\"Chart\")  ]            |
|                                                                                                                                                                     |
| [              .Series(series =\>]                                                                                 |
|                                                                                                                                                                     |
| [              {]                                                                                                  |
|                                                                                                                                                                     |
| [                  series.Add().Name(\"John\")**.Type(SeriesType.Column).**Points(p =\>]                           |
|                                                                                                                                                                     |
| [                  {]                                                                                              |
|                                                                                                                                                                     |
| [                      p.Add(1, 3);]                                                                               |
|                                                                                                                                                                     |
| [                      p.Add(2, 2);]                                                                               |
|                                                                                                                                                                     |
| [                      p.Add(3, 1);]                                                                               |
|                                                                                                                                                                     |
| [                      p.Add(4, 2);]                                                                               |
|                                                                                                                                                                     |
| [                      p.Add(5, 5);]                                                                               |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [                  });                  ]                                                                          |
|                                                                                                                                                                     |
| [                  ]                                                                                               |
|                                                                                                                                                                     |
| [                  series.Add().Name(\"Average\")**.Type(SeriesType.Line).**Points(p =\>]                          |
|                                                                                                                                                                     |
| [                  {]                                                                                              |
|                                                                                                                                                                     |
| [                      p.Add(1, 3); ]                                                                              |
|                                                                                                                                                                     |
| [                      p.Add(2, 2.67);]                                                                            |
|                                                                                                                                                                     |
| [                      p.Add(3, 3); ]                                                                              |
|                                                                                                                                                                     |
| [                      p.Add(4, 6.33);]                                                                            |
|                                                                                                                                                                     |
| [                      p.Add(5, 3.33);]                                                                            |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [                  }).Style(style =\>]                                                                             |
|                                                                                                                                                                     |
| [                  {]                                                                                              |
|                                                                                                                                                                     |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                    |
|                                                                                                                                                                     |
| [                      style.Interior(new Syncfusion.Mvc.ChartAdv.GradientInfo(new ColorInfo(Color.Maroon)));    ] |
|                                                                                                                                                                     |
| [                  }).DisplayText(false).Symbol(symbol =\> symbol.Visible(true).Shape(SymbolShape.Diamond));    ]  |
|                                                                                                                                                                     |
| [               ]                                                                                                  |
|                                                                                                                                                                     |
| [              })]                                                                                                 |
|                                                                                                                                                                     |
| [                 ]                                                                                                |
|                                                                                                                                                                     |
| [%\>]                                                                                          |
|                                                                                                                                                                     |
| []                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                             |
|                                                                                                                                                                             |
| [\@{] [Html.MobSyncfusion().ChartAdv(\"ChartAdv\")  ] |
|                                                                                                                                                                             |
| [              .LegendPosition(DockPosition.Bottom)         ]                                                              |
|                                                                                                                                                                             |
| [              .Series(series =\>]                                                                                         |
|                                                                                                                                                                             |
| [              {]                                                                                                          |
|                                                                                                                                                                             |
| [                  series.Add().Name(\"John**\").Type(SeriesType.Column)**.Points(p =\>]                                   |
|                                                                                                                                                                             |
| [                  {]                                                                                                      |
|                                                                                                                                                                             |
| [                      p.Add(1, 3);]                                                                                       |
|                                                                                                                                                                             |
| [                      p.Add(2, 2);]                                                                                       |
|                                                                                                                                                                             |
| [                      p.Add(3, 1);]                                                                                       |
|                                                                                                                                                                             |
| [                      p.Add(4, 2);]                                                                                       |
|                                                                                                                                                                             |
| [                      p.Add(5, 5);]                                                                                       |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| [                  });                  ]                                                                                  |
|                                                                                                                                                                             |
| [                  series.Add().Name(\"Doss**\").Type(SeriesType.Line)**.Points(p =\>]                                     |
|                                                                                                                                                                             |
| [                  {]                                                                                                      |
|                                                                                                                                                                             |
| [                      p.Add(1, 3); ]                                                                                      |
|                                                                                                                                                                             |
| [                      p.Add(2, 2.67);]                                                                                    |
|                                                                                                                                                                             |
| [                      p.Add(3, 3); ]                                                                                      |
|                                                                                                                                                                             |
| [                      p.Add(4, 6.33);]                                                                                    |
|                                                                                                                                                                             |
| [                      p.Add(5, 3.33);]                                                                                    |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| [                  }).Style(style =\>]                                                                                     |
|                                                                                                                                                                             |
| [                  {]                                                                                                      |
|                                                                                                                                                                             |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                            |
|                                                                                                                                                                             |
| [                      style.Interior(new Syncfusion.Mvc.ChartAdv.GradientInfo(new ColorInfo(Color.Maroon)));    ]         |
|                                                                                                                                                                             |
| [                  }).DisplayText(false).Symbol(symbol =\> symbol.Visible(true).Shape(SymbolShape.Diamond));    ]          |
|                                                                                                                                                                             |
| [               ]                                                                                                          |
|                                                                                                                                                                             |
| [              }).Render();]                                                                                               |
|                                                                                                                                                                             |
| [}] []                                                |
|                                                                                                                                                                             |
|                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application, to get the following output:

 

{border="0"}

Figure 47: Combination Chart[]

 

[]{#related-topics}

