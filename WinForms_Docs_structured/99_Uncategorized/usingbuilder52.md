---
title: usingbuilder52.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder52.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using Builder {#using-builder style="tab-stops: 0pt"}

[] 

The steps to create a Pie chart through Builder are as follows:

1.   In Controller, return view to the corresponding View page.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                          |
|                                                                                                                                                       |
| [public] [ [ActionResult] SimpleChart()] |
|                                                                                                                                                       |
| [{ ]                                                                                                              |
|                                                                                                                                                       |
| [   return] [ View();]                                           |
|                                                                                                                                                       |
| [}]                                                                                                               |
|                                                                                                                                                       |
| []                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View Page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the series type to **Pie**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"Chart\"])]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [              .Series(series =\>]                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [              {]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                  series.Add().Name([\"Series 1\"])**.Type([SeriesType].Pie).**Points(p =\>]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                  {]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                      p.Add(1, 20);]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                      p.Add(2, 21);]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                      p.Add(3, 40);]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                      p.Add(4, 10);]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                      p.Add(5, 9);]                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                  });]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [              }).Size([new] System.Drawing.[Size](600, 750)).Text([\"Product Development LifeCycle\"]).Font([new][ChartFont]([\"Arial\"], [\"15px\"], [ChartFontStyle].Bold)).ElementSpacing(10)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    [%\>]]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                |
| [  [\@{]Html.MobSyncfusion().Chart(\"ChartAdv\")]                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [                 .Series(series =\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [              {]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                |
| [                  series.Add().Name(\"Series 1\").Type(SeriesType.Pie).Points(p =\>]                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                  {]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                      p.Add(1, 20);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                      p.Add(2, 21);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                      p.Add(3, 40);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                      p.Add(4, 10);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [                      p.Add(5, 9);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                |
| [                  });]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                |
| [              }).Size(new System.Drawing.Size(600, 750)).Text(\"Product Development LifeCycle\").Font(new ChartFont(\"Arial\", \"15px\", ChartFontStyle.Bold)).ElementSpacing(10).Render();] |
|                                                                                                                                                                                                                                                |
| [        [}]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

5.   Build and run the application, to get the following output:

 

 

{border="0"}

Figure 45: Pie-chart showing the Product development cycle

[]{#related-topics}

