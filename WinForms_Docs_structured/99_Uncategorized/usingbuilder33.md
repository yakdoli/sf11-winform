---
title: usingbuilder33.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder33.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The steps to create a Step Line chart through Builder are as follows:

1.   In Controller, return view to the corresponding View page.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [  ] [public] [ [ActionResult] SimpleChart()] |
|                                                                                                                                                                                                                  |
| [   { ]                                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [       return] [ View();]                                                                                                  |
|                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                       |
|                                                                                                                                                                                                                  |
| [      []]                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **StepLine**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| [\<%] [=] [ Html.Syncfusion.Chart([\"Chart\"])] |
|                                                                                                                                                                                                                      |
| [          .LegendPosition([DockPosition].Bottom).Margin([new][MarginInfo]() { Left = 0 })]                 |
|                                                                                                                                                                                                                      |
| [              .Series(series =\>]                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [              {]                                                                                                                                                                |
|                                                                                                                                                                                                                      |
| [               series.Add().Name([\"Series 1\"]).**Type([SeriesType].StepLine**).Points(p =\>]                                  |
|                                                                                                                                                                                                                      |
| [                  {]                                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [                      p.Add(1, 75);]                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [                      p.Add(2, 82);]                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [                      p.Add(3, 87);]                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [                      . . .      ]                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [                  }).Style(style =\>]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [                  {]                                                                                                                                                            |
|                                                                                                                                                                                                                      |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                                                                  |
|                                                                                                                                                                                                                      |
| [                  }).DisplayText([true]);]                                                                                                                 |
|                                                                                                                                                                                                                      |
| [               ]                                                                                                                                                                |
|                                                                                                                                                                                                                      |
| [              })]                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [    [%\>]]                                                                                                                                          |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                    |
|                                                                                                                                    |
| [\@{Html.Syncfusion.Chart(\"Chart\")]                                                          |
|                                                                                                                                    |
| [           .LegendPosition(DockPosition.Bottom).Margin(new MarginInfo() { Left = 0 })]        |
|                                                                                                                                    |
| [           .Series(series =\>]                                                                |
|                                                                                                                                    |
| [              {]                                                                              |
|                                                                                                                                    |
| [                  series.Add().Name(\"Seires 1\").**Type(SeriesType.StepLine).**Points(p =\>] |
|                                                                                                                                    |
| [                  {]                                                                          |
|                                                                                                                                    |
| [                      p.Add(1, 75);]                                                          |
|                                                                                                                                    |
| [                      p.Add(2, 82);]                                                          |
|                                                                                                                                    |
| [                      p.Add(3, 87);]                                                          |
|                                                                                                                                    |
| [                      . . .]                                                                  |
|                                                                                                                                    |
| [                      ]                                                                       |
|                                                                                                                                    |
| [                  }).Style(style =\>]                                                         |
|                                                                                                                                    |
| [                  {]                                                                          |
|                                                                                                                                    |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                |
|                                                                                                                                    |
| [                  }).DisplayText(true);]                                                      |
|                                                                                                                                    |
| [              }).Render();]                                                                   |
|                                                                                                                                    |
| [        }] []                                    |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 30: Step-line chart

 

[]{#related-topics}

