---
title: usingchartmodel5.md
original_path: WinForms_Docs/04_Controls/Chart/usingchartmodel5.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

[] 

The steps to create a Step Line chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

2.   Create an instance of ChartSeries, and set the SeriesType to **StepArea**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                    |
|                                                                                                                                                                                                 |
| [public] [ [ActionResult] SimpleChart()]                                           |
|                                                                                                                                                                                                 |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [            [ChartModel] model = [new][ChartModel]();]                                |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [            [Series] Series = [new][Series]([\"Series 1\"]);] |
|                                                                                                                                                                                                 |
| **[            Series.Type = [SeriesType].StepArea;]**                                                                              |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [            Series.Points.Add(1, 75);]                                                                                                                     |
|                                                                                                                                                                                                 |
| [            Series.Points.Add(2, 82);]                                                                                                                     |
|                                                                                                                                                                                                 |
| [            Series.Points.Add(3, 87);]                                                                                                                     |
|                                                                                                                                                                                                 |
| [             . . .]                                                                                                                                        |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                 |
|                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                         |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [        }]                                                                                                                                                 |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ASPX\]]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<%] [=] [ Html.Syncfusion.Chart([\"SimpleChart\"], ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [  ] [@] [(Html.Syncfusion.Chart(\"SimpleChart\", (ChartModel)ViewData\[\"ChartModel\"\]))] |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the code, to get the following output:

 

{border="0"}

Figure 37: Step-line area chart

 

[]{#related-topics}

