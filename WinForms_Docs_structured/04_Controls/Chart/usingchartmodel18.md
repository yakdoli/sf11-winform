---
title: usingchartmodel18.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\usingchartmodel18.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

 

The steps to create an Area chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Create an instance of ChartSeries, and set the SeriesType to **Area.**

[·      ]Set the ChartSeries, ChartArea, and ChartModel properties.

[·      ]Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]        ]                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [public] [ [ActionResult] SimpleChart()]                               |
|                                                                                                                                                                                                               |
| [        {]                                                                                                                                                  |
|                                                                                                                                                                                                               |
| [            [ChartModel] model = [new][ChartModel]();]                                 |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [            [Series] Series = [new][Series]([\"Series 1\"]);]  |
|                                                                                                                                                                                                               |
| **[            Series.Type = [SeriesType].Area;]**                                                                                   |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [            Series.Points.Add(1945, 0.01);]                                                                                                                 |
|                                                                                                                                                                                                               |
| [            Series.Points.Add(1950, 0.06);]                                                                                                                 |
|                                                                                                                                                                                                               |
| [            Series.Points.Add(1955, 0.11);]                                                                                                                 |
|                                                                                                                                                                                                               |
| [             . . .]                                                                                                                                         |
|                                                                                                                                                                                                               |
| [            model.Series.Add(Series);]                                                                                                                      |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [            [Series] Series1 = [new][Series]([\"Series 2\"]);] |
|                                                                                                                                                                                                               |
| **[            Series1.Type = [SeriesType].Area;]**                                                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [            Series1.Points.Add(1945, 0.5);]                                                                                                                 |
|                                                                                                                                                                                                               |
| [            Series1.Points.Add(1950, 0.25);]                                                                                                                |
|                                                                                                                                                                                                               |
| [            Series1.Points.Add(1955, 0.50);]                                                                                                                |
|                                                                                                                                                                                                               |
| [             . . .]                                                                                                                                         |
|                                                                                                                                                                                                               |
| [            model.Series.Add(Series1);]                                                                                                                     |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                  |
|                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                          |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [        }]                                                                                                                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In the View page, invoke the ChartBuilder by using control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"SimpleChart\"], ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [  ] [@] [(Html.MobSyncfusion().Chart(\"SimpleChart\", (ChartModel)ViewData\[\"ChartModel\"\]))] |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the code, to get the following output:

 

{border="0"}

Figure 38: Area Chart

[]{#related-topics}

