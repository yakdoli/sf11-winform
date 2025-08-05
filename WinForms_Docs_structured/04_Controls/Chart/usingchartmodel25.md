---
title: usingchartmodel25.md
original_path: WinForms_Docs/04_Controls/Chart/usingchartmodel25.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

The steps to show a Legend in chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Set the **Visible** property of Legend to **True.**

[·      ]Set the ChartSeries, ChartArea, and ChartModel properties.

[·      ]Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [public] [ [ActionResult] SimpleChart()]                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            [ChartModel] model = [new][ChartModel]();]                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [            DateTime] [ dt = [new][DateTime](2010, 01, 01);]                                       |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Legend.Visible = [true];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| [            model.LegendPosition = [DockPosition].Bottom;]                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].MajorGridLines.Visible = [false];]                                                                                         |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            [Series] series = [new][Series]([\"Banana\"]);]                                                         |
|                                                                                                                                                                                                                                                                    |
| [            model.Text = [\"Fruits Production Statistics\"];]                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].Title = [\"Year\"];]                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryY\"]\].Title = [\"Sales(%)\"];]                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Font = [new][ChartFont]([\"Arial\"], [\"15pt\"], [ChartFontStyle].Bold);] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].RangeType = [RangeType].Set;]                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].ValueType = [ChartAxisValueType].Double;]                                                                               |
|                                                                                                                                                                                                                                                                    |
| [            model.Axes\[[\"PrimaryX\"]\].Range = [new][MinMaxInfo]() { Start = 1990, End = 2003, Interval = 3 };]                           |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            series.Points.Add(1991, 3.9);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            series.Points.Add(1992, 5.3);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            series.Points.Add(1993, 8.8);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            \...]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            series.Symbol.Visible = [true];]                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            series.Symbol.Shape = [SymbolShape].Triangle;]                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            series.Type = [SeriesType].Line;]                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [            model.Series.Add(series);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            [Series] series1 = [new][Series]([\"Apple\"]);]                                                         |
|                                                                                                                                                                                                                                                                    |
| [            series1.Points.Add(1991, 3.9);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [            series1.Points.Add(1992, 4.2);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [            series1.Points.Add(1993, 5.7);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [             . . .]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            series1.Symbol.Visible = [true];]                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [            series1.Symbol.Shape = [SymbolShape].Diamond;]                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [            series1.Type = [SeriesType].Line;]                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [            model.Series.Add(series1);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [            **model.Legend.Visible = [true];**]                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [            model.Legend.Shape = [LegendShape].Rectangle;]                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [            model.ElementSpacing = 10;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [            model.Margin = [new][MarginInfo]() { Left = 0 };]                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            series.Style.Border.Width = 3;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            [return] View();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [          ] [ ] []                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

[] 

3.   Build and run the code, to get the following output:

[] 

[] 

{border="0"}

Figure 52: Chart Legend

 

 

[]{#related-topics}

