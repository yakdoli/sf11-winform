---
title: chartmodel59.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel59.md
created_at: 2025-07-03
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

The steps to add the Interactive Cursor to the ChartModel through ChartModel are as follows:

Step 1:

Add the code displayed below in the view.

 


View \[ASPX\]

[] 

[\<%][\--Rendering the Chart COntrol\--][%\>]

[  ]

[        [\<%][=] Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]) [%\>]]**[]**


 


View \[cshtml\]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[] 

[@(][new][ [HtmlString]][(Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]).ToString())[)]]

[] 


 

 

**[]** 

Step 2:

Controller:

The Interactive cursors can be enabled by setting the **ShowInteractiveCursors** property to true. The Interactive cursors can be customized by using the [ChartInteractiveCursor ]class properties and it is added to the ChartModel.

Add the code displayed below in the Controller.


[public][ [ActionResult] Index()]

[        {]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            InitializeChart(chartModel);]

[] 

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[           ]

[] 

[            [return] View();]

[] 

[        }]

[] 

[        [void] InitializeChart([MVCChartModel] chartModel)]

[        {]

[] 

[            [ChartSeries] series1, series2;]

[] 

[            series1 = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType].Line);]

[            series1.Text = series1.Name;]

[            series1.Points.Add(1997, 137);]

[            series1.Points.Add(1999, 211);]

[] 

[            series1.Points.Add(2003, 766);]

[] 

[            series2 = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType].Line);]

[            series2.Text = series2.Name;]

[            series2.Points.Add(1997, 437);]

[            series2.Points.Add(1999, 311);]

[] 

[            series2.Points.Add(2003, 466);]

[] 

[            chartModel.Series.Add(series1);]

[            chartModel.Series.Add(series2);]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[            chartModel.ChartSeriesSkins = [ChartSeriesSkins].WarmCold;]

[] 

[            [//Enabling the Interactive cursors]]

**[            chartModel.ShowInteractiveCursors = [true];]**

[] 

[            [//Customizing the Interactive cursors]]

[            [ChartInteractiveCursor] cursor1 = [new] [ChartInteractiveCursor](chartModel.Series\[0\]);]

[            chartModel.ChartArea.InteractiveCursors.Add(cursor1);]

[            [ChartInteractiveCursor] cursor2 = [new] [ChartInteractiveCursor](chartModel.Series\[1\]);]

[            cursor2.XPosition = 6;]

[            cursor2.Color = [Color].Blue;]

[            chartModel.ChartArea.InteractiveCursors.Add(cursor2);]

[] 

[] 

[        }][]


Step 3:

Run the code, to get the following output:

[] 

{border="0"}

Figure 339: Chart - Interactive Cursor

[] 

[]{#related-topics}

