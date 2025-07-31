---
title: chartmodel53.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel53.md
created_at: 2025-07-03
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a chart with the zooming feature through ChartModel:

[] 

Step 1:

Controller:

Add the code displayed below in the Home Controller.cs file.

[] 


[using][ System;]

[using][ System.Collections.Generic;]

[using][ System.Linq;]

[using][ System.Web;]

[using][ System.Web.Mvc;]

[using][ Syncfusion.Mvc.Shared;]

[using][ Syncfusion.Mvc.Chart;]

[using][ Syncfusion.Windows.Forms.Chart;]

[using][ Syncfusion.Drawing;]

[using][ System.Drawing;]

[] 

[namespace][ Sample.Controllers]

[{]

[    \[[HandleError]\]]

[    [public] [class] [HomeController] : [Controller]]

[    {]

[        [public] [ActionResult] Index()]

[        {]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            InitializeChart(chartModel);]

[            CustomizeChartAppearance(chartModel);]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[            [return] View();]

[        }]

[] 

[        \[[AcceptVerbs]([\"Post\"])\]]

[        [public] [ActionResult] Index([MVCChartModel] chartModel, [ChartParams] param)]

[        {]

[            InitializeChart(chartModel);]

[            CustomizeChartAppearance(chartModel);]

[           [return] chartModel.ChartActionResult(param);]

[        }]

[] 

[        [///][ ][\<summary\>]]

[        [///][ Initializes the chart data and enables zooming.]]

[        [///][ ][\</summary\>]]

[        [///][ ][\<param name=\"chartModel\"\>][The chart model.][\</param\>]]

[        [protected] [void] InitializeChart([MVCChartModel] chartModel)]

[        {]

[            chartModel.Series.Clear();]

[            chartModel.Size = [new] [Size](450, 350);]

[] 

[            [//Enabling X-Axis and Y-Axis Zooming]]

[            **chartModel.EnableXZooming = [true];**]

**[            chartModel.EnableYZooming = [true];]**

[] 

[            [//Creating Chart series]]

[            [ChartSeries] series;]

[            series = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType].Area);]

[            series.Text = series.Name;]

[] 

[            [//Adding Chart Series Points]]

[            series.Points.Add(1997, 437);]

[            series.Points.Add(1999, 411);]

[            series.Points.Add(2003, 466);]

[            series.Points.Add(2005, 422);]

[            series.Points.Add(2009, 622);]

[] 

[            [//Adding the chart series in the chart model]]

[            chartModel.Series.Add(series);]

[            chartModel.PrimaryYAxis.GridLineType.ForeColor = [Color].DarkGray;]

[            chartModel.PrimaryXAxis.LineType.ForeColor = [Color].DarkGray;]

[] 

[            [//Specifying the chart x-axis and y-axis titles]]

[            chartModel.PrimaryXAxis.Title = [\" Year \"];]

[            chartModel.PrimaryYAxis.Title = [\"Market Volume \"];]

[            [//Adding title for the chart]]

[            chartModel.Text = [\"Sales Volume Comparison\"];]

[            chartModel.Font = [new] [Font]([\"Verdana\"], 12, [FontStyle].Bold);]

[] 

[            [//Setting the maximum and minimum range values for x-axis and y-axis]]

[            chartModel.PrimaryYAxis.Range = [new] [MinMaxInfo](0, 800, 500);]

[            chartModel.PrimaryXAxis.Range = [new] [MinMaxInfo](1995, 2012, 5);]

[] 

[        }]

[] 

[        [///][ ][\<summary\>]]

[        [///][ Customizing the chart appearance]]

[        [///][ ][\</summary\>]]

[        [///][ ][\<param name=\"chartModel\"\>][The chart model.][\</param\>]]

[        [private] [void] CustomizeChartAppearance([MVCChartModel] chartModel)]

[        {]

[            [//Setting the border appearance]]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]

[            [//Setting the skins]]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[            [//Setting the series skins]]

[            chartModel.ChartSeriesSkins = [ChartSeriesSkins].GrayScale;]

[            ]

[        }]

[    }]

[}]


[] 

Step 2:

View:

Add the code displayed below in the Index.aspx file.

[] 


[View\[ASPX\]]

[] 

[\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]

[] 

[\<][asp][:][Content][ [ID][=\"Content1\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]]

[   Chart Zooming]

[\</][asp][:][Content][\>]

[] 

[\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]

[] 

[\<%][\--Rendering the Chart Control\--][%\>]

[    ]

[    [\<%][=] Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]) [%\>]]

[] 

[\</][asp][:][Content][\>]


[] 


[View\[cshtml\]]

[] 

[\@{]

[] 

[Layout=\"\~/Views/Shared/\_Layout.cshtml\";]

[ViewBag.Title=" Chart Zooming";]

[}]

[] 

[\<][div][\>]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[    ]

[    [@(]][new][ [HtmlString]][(Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]).ToString())[)]]

[] 

[\</][div][\>]


 

Step 3:

Run the code, to get the following output.

[] 

{border="0"}

Figure 318: Before Zooming

[] 

{border="0"}

Figure 319: After Zooming

[] 

[]{#related-topics}

