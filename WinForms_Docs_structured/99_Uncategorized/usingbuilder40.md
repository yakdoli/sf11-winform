---
title: usingbuilder40.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder40.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The steps to show a Legend in chart through Builder are as follows:

[1.   ]In Controller, return view to the corresponding View page.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| [   ] [public] [ [ActionResult] SimpleChart()] |
|                                                                                                                                                                                            |
| [   { ]                                                                                                                                                |
|                                                                                                                                                                                            |
| [       return] [ View();]                                                                            |
|                                                                                                                                                                                            |
| [   }]                                                                                                                                                 |
|                                                                                                                                                                                            |
| []                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Set the **Visible** property of Legend to **True .**

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [\<%] [=] [ Html.Syncfusion.Chart([\"Chart\"])] |
|                                                                                                                                                                                                                                                             |
| [           .LegendPosition([DockPosition].Bottom).Margin([new][MarginInfo]() { Left = 0 })]                                          |
|                                                                                                                                                                                                                                                             |
| [              .Series(series =\>]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [              {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [                  series.Add().Name([\"LineSeries\"]).Type([SeriesType].Line).Points(p =\>]                                                               |
|                                                                                                                                                                                                                                                             |
| [                  {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                      p.Add(1, 75);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                      p.Add(2, 82);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                      p.Add(3, 87);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                      p.Add(4, 84);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                      . . .]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [                  }).Style(style =\>]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [                  {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [                  }).DisplayText([true]);]                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [               ]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [              }).**Legend(legend =\> legend.Visible([true]).Shape([LegendShape]. Rectangle))**.ElementSpacing(10)]                                           |
|                                                                                                                                                                                                                                                             |
| [    [%\>]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                          |
|                                                                                                                                                              |
| **[]**                                                                                                                   |
|                                                                                                                                                              |
| [\@{] [Html.Syncfusion.Chart(\"Chart\")]                         |
|                                                                                                                                                              |
| [                  .LegendPosition(DockPosition.Bottom).Margin(new MarginInfo() { Left = 0 })]                           |
|                                                                                                                                                              |
| [              .Series(series =\>]                                                                                       |
|                                                                                                                                                              |
| [              {]                                                                                                        |
|                                                                                                                                                              |
| [                  series.Add().Name(\"LineSeires\").Type(SeriesType.Line).Points(p =\>]                                 |
|                                                                                                                                                              |
| [                  {]                                                                                                    |
|                                                                                                                                                              |
| [                      p.Add(1, 75);]                                                                                    |
|                                                                                                                                                              |
| [                      p.Add(2, 82);]                                                                                    |
|                                                                                                                                                              |
| [                      p.Add(3, 87);]                                                                                    |
|                                                                                                                                                              |
| [                      p.Add(4, 84);]                                                                                    |
|                                                                                                                                                              |
| [                      p.Add(5, 84);]                                                                                    |
|                                                                                                                                                              |
| [                      ]                                                                                                 |
|                                                                                                                                                              |
| [                  }).Style(style =\>]                                                                                   |
|                                                                                                                                                              |
| [                  {]                                                                                                    |
|                                                                                                                                                              |
| [                      style.Border(border =\> border.Width(3)).Opacity(0.8f);]                                          |
|                                                                                                                                                              |
| [                  }).DisplayText(true);]                                                                                |
|                                                                                                                                                              |
| [              }).**Legend(legend =\> legend.Visible(true).Shape(LegendShape.Rectangle))**.ElementSpacing(10).Render();] |
|                                                                                                                                                              |
| [        [}]]                                                                                |
|                                                                                                                                                              |
| []                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application, to get the following output:

{border="0"}

Figure 26: Chart Legend

 

[]{#related-topics}

