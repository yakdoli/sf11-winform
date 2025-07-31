---
title: usingchartmodel23.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\usingchartmodel23.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

[] 

The steps to create a Combination chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Create an instance of ChartSeries, and set the SeriesType to Line and Column.

[·      ]Set the ChartSeries, ChartArea, and ChartModel properties.

[·      ]Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                            |
|                                                                                                                                                                                                                         |
| [public] [ [ActionResult] SimpleChart()]                                                                   |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [            ChartModel] [ model = [new][ChartModel]();] |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [            [Series] series = [new][Series]([\"John\"]);]                |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(1, 2);]                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(2, 3);]                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(3, 5);]                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(4, 7);]                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(5, 6);]                                                                                                                                 |
|                                                                                                                                                                                                                         |
| **[            series.Type = [SeriesType].Column;     ]**                                                                                      |
|                                                                                                                                                                                                                         |
| [            model.Series.Add(series);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [            [Series] series3 = [new][Series]([\"Doss\"]);]               |
|                                                                                                                                                                                                                         |
| [            series3.Points.Add(1, 3);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| [            series3.Points.Add(2, 2);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| [            series3.Points.Add(3, 3);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| [            series3.Points.Add(4, 6);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| [            series3.Points.Add(5, 3);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| **[            series3.Type = [SeriesType].Line;]**                                                                                            |
|                                                                                                                                                                                                                         |
| [            model.Series.Add(series3);]                                                                                                                               |
|                                                                                                                                                                                                                         |
| [            model.Size = [new][Size](500, 400);]                                                                         |
|                                                                                                                                                                                                                         |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                            |
|                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                    |
|                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[           ]

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ] []

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"]] [SimpleChart] [ \"] [, ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

[] 

{border="0"}

Figure 48: Combination Chart

 

[]{#related-topics}

