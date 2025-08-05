---
title: usingchartmodel21.md
original_path: WinForms_Docs/04_Controls/Chart/usingchartmodel21.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

[] 

The steps to create a Column chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Create an instance of ChartSeries, and set the SeriesType to Column.

[·      ]Set the ChartSeries, ChartArea, and ChartModel properties.

[·      ]Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [public] [ [ActionResult] SimpleChart()]                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            [ChartModel] model = [new][ChartModel]();]                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [            model.Legend.Visible = [false];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            [Random] ran = [new][Random]();]                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            [Series] series = [new][Series]([\"Toyoto\"]);]                                                         |
|                                                                                                                                                                                                                                                                    |
| [            model.Text = [\"Car Sales\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].Title = [\"Year\"];]                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryY\"]\].Title = [\"Sales(%)\"];]                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryY\"]\].MajorGridLines.Visible = [false];]                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].MajorGridLines.Visible = [false];]                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [            model.LegendPosition = [DockPosition].Bottom;]                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Font = [new][ChartFont]([\"Arial\"], [\"15pt\"], [ChartFontStyle].Bold);] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            [DateTime] dt = [new][DateTime](2011, 01, 01);]                                                                                 |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].RangeType = [RangeType].Set;]                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].ValueType = [ChartAxisValueType].Double;]                                                                               |
|                                                                                                                                                                                                                                                                    |
| [          model.Axes\[[\"PrimaryX\"]\].Range = [new][MinMaxInfo]() { Start = 1990, End = 2003, Interval = 3 };]                             |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            series.Points.Add(1991, 3.9);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            series.Points.Add(1992, 5.3);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            series.Points.Add(1993, 8.8);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [             . . .]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| **[            series.Type = [SeriesType].Column;]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [            model.Series.Add(series);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            ....]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Series.Add(series2);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [            model.ElementSpacing = 10;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [            model.Margin= [new][MarginInfo]() { Left = 0 };]                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            [return] View();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"]] [SimpleChart] [ \"] [, ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
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
|                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the code, to get the following output:

 

 

{border="0"}

Figure 44: Column chart showing car sales

 

[]{#related-topics}

