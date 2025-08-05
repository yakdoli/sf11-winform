---
title: usingchartmodel13.md
original_path: WinForms_Docs/04_Controls/Chart/usingchartmodel13.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

The steps to show a Legend in chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

2.   Set the **ShowTooltips** property of chart model to **True ** and  set the **ChartModel.Calcregions** property to True.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

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

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<%] [=] [ Html.Syncfusion.Chart([\"SimpleChart\"], ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [  ] [@] [(Html.Syncfusion.Chart(\"SimpleChart\", (ChartModel)ViewData\[\"ChartModel\"\]))]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

[] 

[] 

{border="0"}

Figure 27: Chart Tooltip

 

 

 

 

 

[]{#related-topics}

