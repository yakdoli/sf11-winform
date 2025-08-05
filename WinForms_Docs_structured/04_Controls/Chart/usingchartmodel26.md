---
title: usingchartmodel26.md
original_path: WinForms_Docs/04_Controls/Chart/usingchartmodel26.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

The steps to customize a Symbol in chart through Builder are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Set the **Visible** property of Symbol to **True.**

[·      ]Set the ChartSeries, ChartArea, and ChartModel properties.

[·      ]Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [public] [ [ActionResult] SimpleChart()]                                                          |
|                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [            [ChartModel] model = [new][ChartModel]();]                                                            |
|                                                                                                                                                                                                                                          |
| [            model.Legend.Visible = [true];]                                                                                                                       |
|                                                                                                                                                                                                                                          |
| [            model.LegendPosition = [DockPosition].Bottom;]                                                                                                     |
|                                                                                                                                                                                                                                          |
| [             ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| [            [Series] series = [new][Series]([\"London\"]);]                               |
|                                                                                                                                                                                                                                          |
| [            model.Text = [\"Monthly Average Temperature\"];]                                                                                                   |
|                                                                                                                                                                                                                                          |
| [            model.Axes\[[\"PrimaryX\"]\].Title = [\"Month\"];]                                                                         |
|                                                                                                                                                                                                                                          |
| [            model.Axes\[[\"PrimaryY\"]\].Title = [\"Temperature\"];]                                                                   |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            [DateTime] dt = [new][DateTime](2010, 01, 01);]                                                       |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            model.Axes\[[\"PrimaryX\"]\].RangeType = [RangeType].Set;]                                                                 |
|                                                                                                                                                                                                                                          |
| [            model.Axes\[[\"PrimaryX\"]\].ValueType = [ChartAxisValueType].Double;]                                                     |
|                                                                                                                                                                                                                                          |
| [            model.Axes\[[\"PrimaryX\"]\].Range = [new][MinMaxInfo]() { Start = 1990, End = 2003, Interval = 1 };] |
|                                                                                                                                                                                                                                          |
| [            model.Axes\[[\"PrimaryX\"]\].DateFormat = [\"mmm\"];]                                                                      |
|                                                                                                                                                                                                                                          |
| [           ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [            model.Size = [new] System.Drawing.[Size](1000, 600);]                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            series.Points.Add(dt, 3.9);]                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [            series.Points.Add(dt.AddMonths(1), 5.3);           ]                                                                                                                       |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            series.Type = [SeriesType].Line;]                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [            model.Series.Add(series);]                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| **[            series.Symbol.Visible = [true];]**                                                                                                                  |
|                                                                                                                                                                                                                                          |
| **[            series.Symbol.Shape = [SymbolShape].Circle;]**                                                                                                   |
|                                                                                                                                                                                                                                          |
| **[            series.Symbol.Size =[new][Size](10,10);]**                                                                                  |
|                                                                                                                                                                                                                                          |
| **[            series.Symbol.Style.Border.Width = 2;]**                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| **[            [//Customize symbol for paritcular points]]**                                                                                                      |
|                                                                                                                                                                                                                                          |
| **[            series.Points\[1\].GetSymbol().Shape = [SymbolShape].Image;]**                                                                                   |
|                                                                                                                                                                                                                                          |
| **[            series.Points\[1\].GetSymbol().ImageUrl = [\"\~/Content/Images/hot.png\"];]**                                                                    |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            [Series] series1 = [new][Series]([\"Tokyo\"]);]                               |
|                                                                                                                                                                                                                                          |
| [            series1.Points.Add(dt, 3.9);]                                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [            series1.Points.Add(dt.AddMonths(2), 4.2);]                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [             ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            series1.Symbol.Visible = [true];]                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [            series1.Symbol.Shape = [SymbolShape].Circle;]                                                                                                      |
|                                                                                                                                                                                                                                          |
| [            series1.Type = [SeriesType].Line;]                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [            model.Series.Add(series1);]                                                                                                                                                |
|                                                                                                                                                                                                                                          |
| [            ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [            model.Legend.Visible = [true];]                                                                                                                       |
|                                                                                                                                                                                                                                          |
| [            model.Legend.Shape = [LegendShape].Rectangle;]                                                                                                     |
|                                                                                                                                                                                                                                          |
| [            model.ElementSpacing = 10;]                                                                                                                                                |
|                                                                                                                                                                                                                                          |
| [            series.Style.Border.Width = 3;]                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| [            ViewData\[[\"ChartModel\"]\] = model;]                                                                                                             |
|                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [          ] [ ] []                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| []                                                                                                                                                                                                                                                                                                                                                 |
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
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Build and run the code, to get the following output:

[] 

[ {border="0"} ] []

 

Figure 54: Symbol Customization

 

[]{#related-topics}

