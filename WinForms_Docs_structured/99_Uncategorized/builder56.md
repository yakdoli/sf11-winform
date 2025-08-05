---
title: builder56.md
original_path: WinForms_Docs/99_Uncategorized/builder56.md
created_at: 2025-08-05
---






##### Builder {#builder style="tab-stops: 0pt"}

The steps to customize the ContextMenu through Builder are as follows:

Step 1:

View:

Add the code displayed below in the view.


View \[ASPX\]

 

[\<%][\--Rendering the Chart through partial view\--][%\>]

[] 

[    [\<%] Html.RenderPartial([\"PartialView\"], [this].ViewData); [%\>]]


**[]** 

 


View \[cshtml\]

[] 

[@\*][\--Rendering the Chart through partial view\--][\*@]

[] 

[    [@]Html.RenderPartial([\"PartialView\"], [this].ViewData)[]]

[] 

[] 


**[]** 

Step 2:

PartialView:

Add the code displayed below in the Partial View. The specified context menu items can be added by using the **AddContextMenuItem** property. The ChartParams values can be got by using the **ChartParamsArgs** property. To get the updated chart, the chart parameter values are used.

[] 


View \[ASPX\]

[] 

[\<%][\--Rendering the Chart Control\--][%\>]

[    [\<%][=]Html.Chart([\"chart_Model\"])]

[        [//Enabling the Context Menu ]]

**[      .ShowContextMenu([true])]**

[          ]

[          [//Adding the particular context menu items]]

**[      .AddContextMenuItem([ContextMenuItem].ChartTypes)]**

**[      .AddContextMenuItem([ContextMenuItem].Enable3D)]**

[       [//Getting the chart post parameter values from the controller]]

[     .ChartParamsArgs(([ChartParams])ViewData\[[\"ChartParamsData\"]\])]

[    .Series(series=\>{]

[        series.Add().Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 311 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 466 });]

[        })]

[        .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[    })]

[] 

[        .Skins([ChartModelSkins].Office2007Blue)]

[        .BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[        [%\>]]**[]**


[] 


View \[cshtml\]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[    [\@{] Html.Chart([\"chart_Model\"])]

[        [//Enabling the Context Menu ]]

**[      .ShowContextMenu([true])]**

[          ]

[          [//Adding the particular context menu items]]

**[      .AddContextMenuItem([ContextMenuItem].ChartTypes)]**

**[      .AddContextMenuItem([ContextMenuItem].Enable3D)]**

[       [//Getting the chart post parameter values from the controller]]

[     .ChartParamsArgs(([ChartParams])ViewData\[[\"ChartParamsData\"]\])]

[    .Series(series=\>{]

[        series.Add().Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 311 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 466 });]

[        })]

[        .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[    })]

[] 

[        .Skins([ChartModelSkins].Office2007Blue)]

[        .BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[.Render();]

[        [}]]**[]**


 

Step 3:

Controller:

Add the code displayed below in the Controller. The **ChartParams** class is used to get the post parameter values. The post parameter values will be passed to the view through the ViewData.

 


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

[       ]

[        [string] BorderSkin = [\"Emboss\"];]

[        [public] [ActionResult] Index()]

[        {]

[            [MVCChartModel] c = [new] [MVCChartModel]();]

[            [ChartParams] ChartParamsData = [new] [ChartParams]();]

[            ViewData\[[\"ChartParamsData\"]\] = ChartParamsData;]

[            [return] View();]

[        }]

[] 

[        \[[AcceptVerbs]([\"Post\"])\]]

[        [public] [ActionResult] Index([MVCChartModel] chartModel, [ChartParams] param)]

[        {]

[] 

[            ViewData\[[\"ChartParamsData\"]\] = param;]

[            [return] PartialView([\"PartialView\"], [this].ViewData);]

[] 

[        }]

[    }]

[}]**[]**


 

Step 4:

Run the code, to get the following output:

{border="0"}

Figure 326: Customized ContextMenu

**[]** 


{border="0"}Note: If you add the contextmenu items by using the AddContextMenuItem property, then it will override the default context menu items.


[]{#related-topics}

