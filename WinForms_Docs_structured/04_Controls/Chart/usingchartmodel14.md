---
title: usingchartmodel14.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\usingchartmodel14.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

[] 

The following steps explain the addition of a dialog to an application using the Properties model.

1.   In the Controller, create an instance of the DialogModel, define the properties and pass the instance through **View Specific Data** to **View** as given below.**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [public] [ [ActionResult] SimpleChart()]                                                                   |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [            ChartModel] [ model = [new][ChartModel]();] |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [            [Series] series = [new][Series]([\"Series 1\"]);]            |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(1991, 3.9);]                                                                                                                            |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(1992, 5.3);]                                                                                                                            |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(1993, 8.8);]                                                                                                                            |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(1994, 15);]                                                                                                                             |
|                                                                                                                                                                                                                         |
| [            series.Points.Add(1995, 20.6);]                                                                                                                           |
|                                                                                                                                                                                                                         |
| [            series.Type = [SeriesType].Column;]                                                                                               |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [            model.Series.Add(series);]                                                                                                                                |
|                                                                                                                                                                                                                         |
| [            model.Size = [new][Size](500, 400);]                                                                         |
|                                                                                                                                                                                                                         |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                            |
|                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                    |
|                                                                                                                                                                                                                         |
| **[}]**                                                                                                                                                                             |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[ [] ]]{.underline}*  

[] 

2.   In **View**, create the dialog contents and invoke the dialog helper with the **View Data** key as the first argument.

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
| []                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the applicatiton.

 

The output is shown in the following screenshot.

[] 

[] 

{border="0"}

Figure 30: Chart control added to the application[]

[]{#related-topics}

