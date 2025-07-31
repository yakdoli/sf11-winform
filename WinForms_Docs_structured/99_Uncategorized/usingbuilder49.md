---
title: usingbuilder49.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder49.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

[] 

The steps to create an Area chart through Builder are as follows:

1.   In Controller, return view to the corresponding View page.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                          |
|                                                                                                                                                       |
| [public] [ [ActionResult] SimpleChart()] |
|                                                                                                                                                       |
| [   { ]                                                                                                           |
|                                                                                                                                                       |
| [       return] [ View();]                                       |
|                                                                                                                                                       |
| [   }]                                                                                                            |
|                                                                                                                                                       |
| []                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Area**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [%] [MinMaxInfo] [ ass = [new][MinMaxInfo](); [%\>]] |
|                                                                                                                                                                                                                                                                                                                      |
| [\<%] [ass.Start =1940; [%\>]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [\<%] [ass.End = 2005; [%\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                      |
| [\<%] [ass.Interval = 15; [%\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [   [\<%][=] Html.MobSyncfusion().Chart([\"Chart\"]) ]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [           .LegendPosition([DockPosition].Bottom)             ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                      |
| [              .Series(series =\>]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                      |
| [              {]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [                  series.Add().Name([\"John\"])**.Type([SeriesType].Area).**Points(p =\>]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                      |
| [                  {]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [                      p.Add(1946, 0.011);]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                      |
| [                      p.Add(1945, 0.06);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                      |
| [                      p.Add(1947, 0.032);]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                      |
| [                      . . .]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [                     ]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| [                  }).Style(style =\>]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                      |
| [                  {]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [                  }).DisplayText([false]).Symbol(symbol =\> symbol.Visible([true]).Shape([SymbolShape].Star));]                                                                                  |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                      |
| [                  series.Add().Name([\"Andrew\"]).Type([SeriesType].Area).Points(p =\>]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                      |
| [                  {]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [                      p.Add(1950, 0.5);]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                      |
| [                      p.Add(1951, 0.25);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                      |
| [                      p.Add(1952, 0.50);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                      |
| [                      . . .      ]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [  ]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                      |
| [                  }).Style(style =\>]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                      |
| [                  {]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [                  }).DisplayText([false]);    ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [               ]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [              })]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                      |
| [    [%\>]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                     |
|                                                                                                                                                                     |
| [  [\@{]]                                                                              |
|                                                                                                                                                                     |
| [            MinMaxInfo ass = new MinMaxInfo();]                                                                   |
|                                                                                                                                                                     |
| [            ass.Start = 1940;]                                                                                    |
|                                                                                                                                                                     |
| [            ass.End = 2005;]                                                                                      |
|                                                                                                                                                                     |
| [            ass.Interval = 5;]                                                                                    |
|                                                                                                                                                                     |
| [            Html.MobSyncfusion().Chart(\"Chart\")]                                                                |
|                                                                                                                                                                     |
| [                   .LegendPosition(DockPosition.Bottom)]                                                          |
|                                                                                                                                                                     |
| [                      .Series(series =\>]                                                                         |
|                                                                                                                                                                     |
| [                      {]                                                                                          |
|                                                                                                                                                                     |
| [                          series.Add().Name(\"John**\").Type(SeriesType.Area)**.Points(p =\>]                     |
|                                                                                                                                                                     |
| [                          {]                                                                                      |
|                                                                                                                                                                     |
| [                              p.Add(1946, 0.011);]                                                                |
|                                                                                                                                                                     |
| [                              p.Add(1945, 0.06);]                                                                 |
|                                                                                                                                                                     |
| [                              p.Add(1947, 0.032);]                                                                |
|                                                                                                                                                                     |
| [                              . . .]                                                                              |
|                                                                                                                                                                     |
| [                          }).Style(style =\>]                                                                     |
|                                                                                                                                                                     |
| [                          {]                                                                                      |
|                                                                                                                                                                     |
| [                              style.Border(border =\> border.Width(3)).Opacity(0.8f);]                            |
|                                                                                                                                                                     |
| [                          }).DisplayText(false).Symbol(symbol =\> symbol.Visible(true).Shape(SymbolShape.Star));] |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [                          series.Add().Name(\"Andrew\").Type(SeriesType.Area).Points(p =\>]                       |
|                                                                                                                                                                     |
| [                          {]                                                                                      |
|                                                                                                                                                                     |
| [                              p.Add(1950, 0.5);]                                                                  |
|                                                                                                                                                                     |
| [                              p.Add(1951, 0.25);]                                                                 |
|                                                                                                                                                                     |
| [                              p.Add(1952, 0.50);]                                                                 |
|                                                                                                                                                                     |
| [                              . . .]                                                                              |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [                          }).Style(style =\>]                                                                     |
|                                                                                                                                                                     |
| [                          {]                                                                                      |
|                                                                                                                                                                     |
| [                              style.Border(border =\> border.Width(3)).Opacity(0.8f);]                            |
|                                                                                                                                                                     |
| [                          }).DisplayText(false);]                                                                 |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [                      }).Render();]                                                                               |
|                                                                                                                                                                     |
| [        [}]]                                                                          |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
|                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 37: Area Chart

 

 

[]{#related-topics}

