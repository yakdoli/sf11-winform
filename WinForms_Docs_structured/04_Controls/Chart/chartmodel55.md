---
title: chartmodel55.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel55.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

The steps to enable the ContextMenu through ChartModel are as follows:

 

Step 1:

Controller:

Add the code displayed below in the Controller.

In the InitializeChart function, the chart data's are initialized. By setting the **ShowContextMenu** property to true, the context menu can be enabled. The **ChartParams** class is used to get the post parameter values. For this, the **ChartParams** class is used as a parameter in the post action method and passed as a parameter to the **ChartActionResult** method. To get the updated chart, the **ChartActionResult** method is called.

 


[public][ [ActionResult] Index()]

[        {]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            [//Rendering the chart]]

[            ][InitializeChart(chartModel);]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[            [return] View();]

[        }]

[] 

[        \[[AcceptVerbs]([HttpVerbs].Post)\]]

[        [public] [ActionResult] Index([MVCChartModel] chartModel, [ChartParams] param)]

[        {]

[            [//Rendering the chart]]

[            ][InitializeChart(chartModel);]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[            [//calling the ChartActionResult method to get the updated chart ]]

[            [return] chartModel.ChartActionResult(param);]

[           ]

[] 

[        }]

[        ]

[        [//Rendering the chart]]

[        [protected] [void] InitializeChart ([MVCChartModel] chartModel)]

[        {]

[            [//Enabling the context menu]]

**[            chartModel.ShowContextMenu = [true];]**

[] 

[            [//Creating Chart series]]

[            [ChartSeries] series;]

[            series = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType]. Column);]

[            series.Text = series.Name;]

[            series.Points.Add(1997, 437);]

[            series.Points.Add(1999, 311);]

[            series.Points.Add(2003, 466);]

[            chartModel.Series.Add(series);]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[           ]

[        }]**[]**


Step 2:

View:

Add the code displayed below in the aspx file.

 


View \[ASPX\]

[] 

[\<%][\--Rendering the Chart COntrol\--][%\>]

[  ]

[        [\<%][=] Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]) [%\>]]**[]**


 


View \[cshtml\]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[@(][new][ [HtmlString]][  ][(Html.Chart([\"chart_Model\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]).ToString())[)]]

[] 


Step 3:

Run the code, to get the following output:

{border="0"}

Figure 325: Chart - ContextMenu

[] 

[]{#related-topics}

