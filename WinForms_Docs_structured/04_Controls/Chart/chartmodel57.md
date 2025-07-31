---
title: chartmodel57.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel57.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

The steps to enable the ToolBar through ChartModel are as follows:

**[]** 

Step 1:

 

Controller:

Add the code displayed below in the Controller.

In the InitializeChart function, the chart data's are initialized. By setting the **ShowToolBar** property to true, the Toolbar can be enabled. The **ChartParams** class is used to get the post parameter values. For this, the **ChartParams** class is used as a parameter in the post action method and passed as a parameter to the **ChartActionResult** method. To get the updated chart, the **ChartActionResult** method is called.

 


[  ][public][ [ActionResult] Index()]

[        {]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            [//Rendering the chart]]

[            InitializeChart (chartModel);]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[            [return] View();]

[        }]

[] 

[        \[[AcceptVerbs]([HttpVerbs].Post)\]]

[        [public] [ActionResult] Index([MVCChartModel] chartModel, [ChartParams] param)]

[        {]

[            [//Rendering the chart]]

[            InitializeChart (chartModel);]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[            [//calling the ChartActionResult method to get the updated chart ]]

[            [return] chartModel.ChartActionResult(param);]

[] 

[] 

[        }]

[] 

[        [//Rendering the chart]]

[        [protected] [void] InitializeChart ([MVCChartModel] chartModel)]

[        {]

[            [//Enabling the ToolBar]]

[            **chartModel.ShowToolBar = [true];**]

[] 

[            [//Creating Chart series]]

[            [ChartSeries] series;]

[            series = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType].Column);]

[            series.Text = series.Name;]

[            series.Points.Add(1997, 437);]

[            series.Points.Add(1999, 311);]

[            series.Points.Add(2003, 466);]

[            chartModel.Series.Add(series);]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Colorful;]

[            chartModel.EnableXZooming = [true];]

[            chartModel.EnableYZooming = [true];]

[        }]**[]**


 

Step 2:

View:

Add the code displayed below in the view.


View \[ASPX\]

[] 

[\<%][\--Rendering the Chart Control\--][%\>]

[  ]

[        [\<%][=] Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]) [%\>]]**[]**


 


View \[cshtml\]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[] 

[@(][new][ [HtmlString]][(Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]).ToString())[)]]

[] 


**[]** 

 

Step 3:

** **Run the code, to get the following output:

[] 

{border="0"}

Figure 329: Chart - ToolBar

**[]** 

[]{#related-topics}

