---
title: chartmodel8.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel8.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

 

To create a Tornado chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the **SeriesType** to **Tornado**.

3.   Set the **ChartSeries**, **ChartArea**, and **ChartModel** properties.

4.   Return view to the corresponding View page after setting the **ChartModel** to the **ViewData**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [     ][public][ [ActionResult] SimpleChart()]                                                   |
|                                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                   |
|                                                                                                                                                                                                                                                                |
| [            [// Creating the Chart Series and added points to the series.]]                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| **[            [ChartSeries] Task1 = [new] [ChartSeries]([\"Male\"], [ChartSeriesType].Tornado);]**   |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(1, -50, -12);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(2, -50, -91);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(3, -50, -397);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(4, -50, -1072);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(5, -50, -2117);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(6, -50, -3094);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(7, -50, -3804);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(8, -50, -4712);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(9, -50, -6203);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(10, -50, -8415);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [            Task1.Points.Add(11, -50, -9771);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            [// Adding Series to the ChartModel]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [            **chartModel.Series.Add(Task1);**]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            [// Creating the Chart Series and added points to the series.]]                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            **[ChartSeries] Task2 = [new] [ChartSeries]([\"Female\"], [ChartSeriesType].Tornado);**] |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(1, 50, 58);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(2, 50, 321);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(3, 50, 1034);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(4, 50, 2135);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(5, 50, 3459);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(6, 50, 4282);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(7, 50, 4697);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(8, 50, 5412);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(9, 50, 6814);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(10, 50, 8944);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [            Task2.Points.Add(11, 50, 10212);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            [// Adding Series to the ChartModel]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| **[            chartModel.Series.Add(Task2);]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            chartModel.Text = [\"Year 2009 Population Projections by Gender and Age\"];]                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [            chartModel.Font = [new] [Font]([\"Verdana\"], 10, [FontStyle].Bold);]                                            |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            chartModel.Size = [new] [Size](500, 400);]                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Analog;]                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            chartModel.Skins = [ChartModelSkins].Office2007Blue;]                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]                                                                                                               |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            chartModel.PrimaryXAxis.DrawGrid = [false];]                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            chartModel.PrimaryYAxis.DrawGrid = [false];]                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            chartModel.Indexed = [true];            ]                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            chartModel.PrimaryXAxis.Title = [\"Population Projection\"];]                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            chartModel.PrimaryYAxis.Title = [\"Age\"];]                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [            [return] View();]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the **View** page, invoke the **ChartBuilder** by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [@(][new] [HtmlString](][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 88: Chart displaying Tornado Series

[]{#related-topics}

