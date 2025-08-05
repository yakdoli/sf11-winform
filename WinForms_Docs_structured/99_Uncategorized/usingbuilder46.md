---
title: usingbuilder46.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder46.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The steps to create a Line chart through Builder are as follows:

1.   In Controller, return view to the corresponding View page.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [   ] [public] [ [ActionResult] SimpleChart()] |
|                                                                                                                                                                                                              |
| [   { ]                                                                                                                                                                  |
|                                                                                                                                                                                                              |
| [       return] [ View();]                                                                                              |
|                                                                                                                                                                                                              |
| [   }]                                                                                                                                                                   |
|                                                                                                                                                                                                              |
| []                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Line**, and add the **Points** to the series and set the style.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"Chart\"])] |
|                                                                                                                                                                                                                                                                  |
| [           .LegendPosition([DockPosition].Bottom).Margin([new][MarginInfo]() { Left = 0 })]                                               |
|                                                                                                                                                                                                                                                                  |
| [              .Series(series =\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| [              {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| [                  series.Add().Name([\"LineSeries\"]).**Type([SeriesType].Line).**Points(p =\>]                                                                |
|                                                                                                                                                                                                                                                                  |
| [                  {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [                      p.Add(1, 75);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [                      p.Add(2, 82);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [                      p.Add(3, 87);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [                      p.Add(4, 84);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [                      . . .]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| [                  }).Style(style =\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [                  {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| [                  }).DisplayText([true]);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                  |
| [               ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| [              })    [%\>]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                  |
|                                                                                                                                                                                      |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                      |
| [\@{] [Html.MobSyncfusion().Chart(\"Chart\")                 ] |
|                                                                                                                                                                                      |
| [              .Series(series =\>]                                                                                                  |
|                                                                                                                                                                                      |
| [              {]                                                                                                                   |
|                                                                                                                                                                                      |
| [                  series.Add().Name(\"LineSeires**\").Type(SeriesType.Line)**.Points(p =\>]                                        |
|                                                                                                                                                                                      |
| [                  {]                                                                                                               |
|                                                                                                                                                                                      |
| [                      p.Add(1, 75);]                                                                                               |
|                                                                                                                                                                                      |
| [                      p.Add(2, 82);]                                                                                               |
|                                                                                                                                                                                      |
| [                      p.Add(3, 87);]                                                                                               |
|                                                                                                                                                                                      |
| [                      p.Add(4, 84);]                                                                                               |
|                                                                                                                                                                                      |
| [                      p.Add(5, 84);]                                                                                               |
|                                                                                                                                                                                      |
| [                         . . . ]                                                                                                   |
|                                                                                                                                                                                      |
| [                      ]                                                                                                            |
|                                                                                                                                                                                      |
| [                  }).Style(style =\>]                                                                                              |
|                                                                                                                                                                                      |
| [                  {]                                                                                                               |
|                                                                                                                                                                                      |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                     |
|                                                                                                                                                                                      |
| [                  }).DisplayText(true);]                                                                                           |
|                                                                                                                                                                                      |
| [              }).Render();]                                                                                                        |
|                                                                                                                                                                                      |
| [        [}]]                                                                                           |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application, to get the following output:

{border="0"}

Figure 31: Line Chart

 

[]{#related-topics}

