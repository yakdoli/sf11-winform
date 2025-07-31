---
title: builder54.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder54.md
created_at: 2025-07-03
---






##### Builder {#builder style="tab-stops: 0pt"}

 

The steps to create a chart with the panning feature through Builder are as follows:

[] 

Step 1:

Controller:

Add the code displayed below in the HomeController.cs file.


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

[] 

[        [public] [ActionResult] Index()]

[        {]

[            [ChartParams] ChartParamsData = [new] [ChartParams]();]

[            ChartParamsData.EnablePanning = [true];]

[            ViewData\[[\"ChartParamsData\"]\] = ChartParamsData;]

[            [return] View();]

[        }]

[] 

[        \[[AcceptVerbs]([HttpVerbs].Post)\]]

[        [public] [ActionResult] Index([MVCChartModel] chartModel, [ChartParams] param, [bool] EnablePanning)]

[        {]

[] 

[            param.EnablePanning = EnablePanning;]

[            ViewData\[[\"ChartParamsData\"]\] = param;]

[            [return] PartialView([\"PartialView\"], [this].ViewData);]

[] 

[        }]

[] 

[        ]

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

[    Chart Zooming]

[\</][asp][:][Content][\>]

[\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]

[    [\<%][\--Rendering the Chart COntrol\--][%\>]]

[    [\<][div] [id][=\"Chart\"\>]]

[       [\<%]Html.RenderPartial([\"PartialView\"], [this].ViewData); [%\>]]

[    [\</][div][\>]]

[    [\<][div][\>]]

[    [\<%][using] (Ajax.BeginFormExt([\"Index\"], [new] [AjaxOptions]() { UpdateTargetId = [\"Chart\"]}))]

[      { [%\>]]

[    [\<%][=]Html.CheckBox([\"EnablePanning\"], [true])[%\>]]

[    [\<][input] [type][=\"submit\"] [value][=\"Reset\"] [/\>]]

[    [\<%]} [%\>]]

[    [\</][div][\>]]

[\</][asp][:][Content][\>]


[] 

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

[       [@\*][\--Rendering the Chart COntrol\--][\*@]]

[    [\<][div] [id][=\"Chart\"\>]]

[       [@]Html.RenderPartial([\"PartialView\"], [this].ViewData)[]]

[    [\</][div][\>]]

[\<][div][\>]

[    [@][using] (Ajax.BeginFormExt([\"Index\"], [new] [AjaxOptions]() { UpdateTargetId = [\"Chart\"]}))]

[      { []]

[    [@]Html.CheckBox([\"EnablePanning\"], [true])[]]

[    [\<][input] [type][=\"submit\"] [value][=\"Reset\"] [/\>]]

[    }[]]

[    [\</][div][\>]]

[] 

[\</][div][\>]


[] 

Step 3:

PartialView:

[] 

Create a Partial View named **"PartialView.ascx"**, and add the code displayed below in it.

[] 


[View\[ASPX\]]

[] 

[\<%][@][ [Control] [Language][=\"C#\"] [Inherits][=\"System.Web.Mvc.ViewUserControl\"] [%\>]]

[] 

[ [\<%][\--Rendering the Chart COntrol\--][%\>]]

[    [\<%][=]Html.Chart([\"chart_Model\"])]

[        [//Enabling x-axis and y-axis zooming]]

[    .EnableXZooming([true])]

[    .EnableYZooming([true])]

[    .ChartSeriesSkins([ChartSeriesSkins].Pastel)]

[        [//Adding the chart series points]]

[    .Series(series=\>{]

[        series.Add().Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 411 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 466 });]

[            points.Add().X(2005).YValues([new] [double]\[\] { 422 });]

[            points.Add().X(2009).YValues([new] [double]\[\] { 622 });]

[        }).Name([\"Saab\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Area);]

[  [//Getting the chart post parameter values for zooming from the controller]]

[    }).PrimaryXAxis(xaxis=\>{]

[        [ChartParams] ChartParams = [new] [ChartParams]();]

[        ChartParams = ([ChartParams])ViewData\[[\"ChartParamsData\"]\];]

[        xaxis]

[            .Range(range =\>]

[            {]

[                range.Max(2012).Min(1995).Interval(5);]

[            })]

[        .Title([\" Year \"]);]

[        [//Enabling and disabling panning for x-axis]]

[        [if] (ChartParams.EnablePanning)]

[        {]

[            xaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].Panning);]

[        }]

[        [else]]

[        {]

[            xaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].None);]

[        }]

[] 

[        xaxis.LineType(line =\> line.ForeColor(System.Drawing.[Color].DarkGray)).GridLineType(gridline =\> gridline.ForeColor(System.Drawing.[Color].DarkGray)).Title([\"Year\"]);]

[})]

[            [//Enabling and disabling panning for y-axis]]

[        .PrimaryYAxis(yaxis =\>]

[        {]

[            [ChartParams] ChartParams = [new] [ChartParams]();]

[            ChartParams = ([ChartParams])ViewData\[[\"ChartParamsData\"]\];]

[            [if] (ChartParams.EnablePanning)]

[            {]

[                yaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].Panning);]

[            }]

[            [else]]

[            {]

[                yaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].None);]

[            }]

[            yaxis.Title([\"Market Volume \"])]

[            .Range(range =\>]

[                {]

[                    range.Max(800).Min(0).Interval(500);]

[                });]

[] 

[            yaxis.LineType(line =\> line.ForeColor(System.Drawing.[Color].DarkGray)).GridLineType(gridline =\> gridline.ForeColor(System.Drawing.[Color].DarkGray)).Title([\"Market Volume\"]);]

[        })]

[        .ChartParamsArgs(([ChartParams])ViewData\[[\"ChartParamsData\"]\])]

[        .Text([\"Sales Volume Comparison\"])]

[        .Font([new] System.Drawing.[Font]([\"Verdana\"], 12, System.Drawing.[FontStyle].Bold))]

[        .BorderAppearance(ba =\> ba.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[        .Size([new] System.Drawing.[Size](450, 350))]

[        .Skins([ChartModelSkins].Office2007Blue)]

[        .ChartSeriesSkins([ChartSeriesSkins].GrayScale)]

[        ]

[        [%\>]][]


[] 

[] 


[View\[cshtml\][]]

[] 

[ [@\*][\--Rendering the Chart COntrol\--][\*@]]

[    [\@{][ ]Html.Chart([\"chart_Model\"])]

[        [//Enabling x-axis and y-axis zooming]]

[    .EnableXZooming([true])]

[    .EnableYZooming([true])]

[    .ChartSeriesSkins([ChartSeriesSkins].Pastel)]

[        [//Adding the chart series points]]

[    .Series(series=\>{]

[        series.Add().Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 411 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 466 });]

[            points.Add().X(2005).YValues([new] [double]\[\] { 422 });]

[            points.Add().X(2009).YValues([new] [double]\[\] { 622 });]

[        }).Name([\"Saab\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Area);]

[  [//Getting the chart post parameter values for zooming from the controller]]

[    }).PrimaryXAxis(xaxis=\>{]

[        [ChartParams] ChartParams = [new] [ChartParams]();]

[        ChartParams = ([ChartParams])ViewData\[[\"ChartParamsData\"]\];]

[        xaxis]

[            .Range(range =\>]

[            {]

[                range.Max(2012).Min(1995).Interval(5);]

[            })]

[        .Title([\" Year \"]);]

[        [//Enabling and disabling panning for x-axis]]

[        [if] (ChartParams.EnablePanning)]

[        {]

[            xaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].Panning);]

[        }]

[        [else]]

[        {]

[            xaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].None);]

[        }]

[] 

[        xaxis.LineType(line =\> line.ForeColor(System.Drawing.[Color].DarkGray)).GridLineType(gridline =\> gridline.ForeColor(System.Drawing.[Color].DarkGray)).Title([\"Year\"]);]

[})]

[            [//Enabling and disabling panning for y-axis]]

[        .PrimaryYAxis(yaxis =\>]

[        {]

[            [ChartParams] ChartParams = [new] [ChartParams]();]

[            ChartParams = ([ChartParams])ViewData\[[\"ChartParamsData\"]\];]

[            [if] (ChartParams.EnablePanning)]

[            {]

[                yaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].Panning);]

[            }]

[            [else]]

[            {]

[                yaxis.ZoomActions(Syncfusion.Windows.Forms.Chart.[ChartZoomingAction].None);]

[            }]

[            yaxis.Title([\"Market Volume \"])]

[            .Range(range =\>]

[                {]

[                    range.Max(800).Min(0).Interval(500);]

[                });]

[] 

[            yaxis.LineType(line =\> line.ForeColor(System.Drawing.[Color].DarkGray)).GridLineType(gridline =\> gridline.ForeColor(System.Drawing.[Color].DarkGray)).Title([\"Market Volume\"]);]

[        })]

[        .ChartParamsArgs(([ChartParams])ViewData\[[\"ChartParamsData\"]\])]

[        .Text([\"Sales Volume Comparison\"])]

[        .Font([new] System.Drawing.[Font]([\"Verdana\"], 12, System.Drawing.[FontStyle].Bold))]

[        .BorderAppearance(ba =\> ba.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[        .Size([new] System.Drawing.[Size](450, 350))]

[        .Skins([ChartModelSkins].Office2007Blue)]

[        .ChartSeriesSkins([ChartSeriesSkins].GrayScale)]

[        .Render();]

[        ]

[        [}]][]


[] 

Step 4:

Run the code, to get the following output:

{border="0"}

Figure 320: Before Zooming

[] 

[] 

[] 

{border="0"}

Figure 321: After Zooming - Panning Enabled


 

{border="0"}Note: To enable and disable panning, check and uncheck the PanningEnabled checkbox respectively, click Reset, to reset the chart, and zoom by selecting the area inside the chart.


[]{#related-topics}

