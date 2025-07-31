---
title: usingchartmodel28.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\usingchartmodel28.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

The steps to show a Legend in chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Set the **ShowTooltips** property of chart model to **True ** and  set the **ChartModel.Calcregions** property to True.

[·      ]Set the ChartSeries, ChartArea, and ChartModel properties.

[·      ]Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                          |
|                                                                                                                                                                                                       |
| [public] [ [ActionResult] SimpleChart()]                       |
|                                                                                                                                                                                                       |
| [        {]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [            [ChartModel] model = [new][ChartModel]();]                         |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                       |
| [            series.Points.Add(1900, 100);]                                                                                                          |
|                                                                                                                                                                                                       |
| [            series.Points.Add(1920, 120);           ]                                                                                               |
|                                                                                                                                                                                                       |
| [            . . .]                                                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                       |
| [            series.Type = [SeriesType].Spline;]                                                                             |
|                                                                                                                                                                                                       |
| [            model.Series.Add(series);]                                                                                                              |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                       |
| [            series.Symbol.Visible = [true];]                                                                                   |
|                                                                                                                                                                                                       |
| [            series.Symbol.Shape = [SymbolShape].Star;]                                                                      |
|                                                                                                                                                                                                       |
| [] []                                                                                              |
|                                                                                                                                                                                                       |
| [           ] [//Enabling the tooltip support] [] |
|                                                                                                                                                                                                       |
| **[            model.ShowToolTip = [true];]**                                                                                   |
|                                                                                                                                                                                                       |
| **[            model.CalcRegion = [true];]**                                                                                    |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                                       |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                          |
|                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                       |
| [        }]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [          ] [ ] []                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"SimpleChart\"], ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
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

[] 

3.   Build and run the code, to get the following output:

[] 

[] 

{border="0"}

Figure 58: Chart Tooltip

 

 

 

 

 

[]{#related-topics}

