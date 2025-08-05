---
title: usingbuilder35.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder35.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

[] 

The steps to create a Spline Area chart through Builder are as follows:

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

3.   Add the **Series** to the ChartModel and set the series type to **SplineArea**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [\<%] [MinMaxInfo] [ ass = [new][MinMaxInfo](); [%\>]] |
|                                                                                                                                                                                                                                                                                 |
| [\<%] [ass.Start = [new][DateTime](2010,1,1).ToOADate(); [%\>]]                                            |
|                                                                                                                                                                                                                                                                                 |
| [\<%] [ass.End = [new][DateTime](2010, 12, 1).ToOADate(); [%\>]]                                           |
|                                                                                                                                                                                                                                                                                 |
| [\<%] [ass.Interval = 60; [%\>]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [   [\<%][=] Html.Syncfusion.Chart([\"Chart\"])]                                                                                                                   |
|                                                                                                                                                                                                                                                                                 |
| [                     .LegendPosition([DockPosition].Bottom).Margin([new][MarginInfo]() { Left = 0 })]                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [              .Series(series =\>]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [              {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [                  series.Add().Name([\"Jhon\"])**.Type([SeriesType].SplineArea).**Points(p =\>]                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [                  {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010,1,1), 400);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 2, 1), 900);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 3, 1), 700);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 4, 1), 550);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 5, 1), 800);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 6, 1), 480);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 7, 1), 650);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 8, 1), 620);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 9, 1), 600);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 10, 1), 530);]                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 11, 1), 540);]                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [                      p.Add([new][DateTime](2010, 12, 1), 380);]                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [                  }).Style(style =\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [                  {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [                  });]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [               ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [              })]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [    [%\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                |
|                                                                                                                                                                |
| [        [\@{]MinMaxInfo ass = new MinMaxInfo(); [}]]              |
|                                                                                                                                                                |
| [        [\@{]ass.Start = new DateTime(2010, 1, 1).ToOADate();[}]] |
|                                                                                                                                                                |
| [        [\@{]ass.End = new DateTime(2010, 12, 1).ToOADate();[}]]  |
|                                                                                                                                                                |
| [        [\@{]ass.Interval = 31;[}]]                               |
|                                                                                                                                                                |
| [        [\@{]Html.Syncfusion.Chart(\"ChartAdv\")]                                             |
|                                                                                                                                                                |
| [              .Series(series =\>]                                                                                         |
|                                                                                                                                                                |
| [              {]                                                                                                          |
|                                                                                                                                                                |
| [                  series.Add().Name(\"Newyork\")**.Type(SeriesType.SplineArea).**Points(p =\>]                            |
|                                                                                                                                                                |
| [                  {]                                                                                                      |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 1, 1), 400);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 2, 1), 900);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 3, 1), 700);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 4, 1), 550);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 5, 1), 800);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 6, 1), 480);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 7, 1), 650);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 8, 1), 620);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 9, 1), 600);]                                                              |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 10, 1), 530);]                                                             |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 11, 1), 540);]                                                             |
|                                                                                                                                                                |
| [                      p.Add(new DateTime(2010, 12, 1), 380);]                                                             |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [                  }).Style(style =\>]                                                                                     |
|                                                                                                                                                                |
| [                  {]                                                                                                      |
|                                                                                                                                                                |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                            |
|                                                                                                                                                                |
| [                  });]                                                                                                    |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [              }).Render();]                                                                                               |
|                                                                                                                                                                |
| [        [}]]                                                                                  |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| []                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application, to get the following output:

[] 

{border="0"}

Figure 34: Spline area chart

[]{#related-topics}

