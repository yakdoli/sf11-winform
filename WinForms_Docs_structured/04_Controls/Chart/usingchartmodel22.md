---
title: usingchartmodel22.md
original_path: WinForms_Docs/04_Controls/Chart/usingchartmodel22.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using ChartModel {#using-chartmodel style="tab-stops: 0pt"}

[] 

The steps to create a Pie chart through ChartModel are as follows:

1.   In Controller, create an instance of MVCChartModel.

[·      ]Create an instance of ChartSeries, and set the SeriesType to Pie.

2.   Set the ChartSeries, ChartArea, and ChartModel properties.

3.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]        ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [public] [ [ActionResult] SimpleChart()]                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [            [ChartModel] model = [new][ChartModel]();]                                                                                           |
|                                                                                                                                                                                                                                                                         |
| [            model.Text = [\"Product Development LifeCycle\"];]                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [            model.Font = [new][ChartFont]([\"Segoe UI\"], [\"14px\"], [ChartFontStyle].Normal);] |
|                                                                                                                                                                                                                                                                         |
| [            model.Size = [new][Size](600, 750);      ]                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            [Series] Series1 = [new][Series]([\"PieChart\"]);]                                                           |
|                                                                                                                                                                                                                                                                         |
| **[            Series1.Type = [SeriesType].Pie;]**                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points.Add(1, 20);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points.Add(2, 21);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points.Add(3, 40);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points.Add(4, 10);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points.Add(5, 9);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            model.Series.Add(Series1);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points\[0\].Text = [\"Analysis 20%\"];]                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points\[1\].Text = [\"Design 21%\"];]                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points\[2\].Text = [\"Code/Unit Test 40%\"];]                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points\[3\].Text = [\"Documentation 10%\"];]                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [            Series1.Points\[4\].Text = [\"Deployment 9%\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            Series1.DisplayText = [true];]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            Series1.TextColor = [Color].Red;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            Series1.ShowTicks = [true];]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [            model.Legend.Visible = [false];]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            model.LegendAlignment = [StringAlignment].Center;]                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [            model.LegendPosition = [DockPosition].Top;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [            model.ElementSpacing = 10;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            ViewData\[[\"ChartModel\"]\] = model;        ]                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[         ]

4.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[      ] []

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%] [=] [ Html.MobSyncfusion().Chart([\"]] [SimpleChart] [ \"] [, ([ChartModel])ViewData\[[\"ChartModel\"]\])[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

5.   Build and run the code, to get the following output:

 

{border="0"}

Figure 46: Pie-chart showing the Product development cycle

[] 

[]{#related-topics}

