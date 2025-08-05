---
title: builder61.md
original_path: WinForms_Docs/99_Uncategorized/builder61.md
created_at: 2025-08-05
---








  









### Builder {#builder style="tab-stops: 0pt"}

[] 

The steps to enable the printing feature in a chart through Builder are as follows:

 

Step 1:

View:

Add the code displayed below in the aspx file. The printing functionality can be enabled by using the **PrintButtonVisible** property. Also, the Print button can be draggable. This can be enabled by using the **PrintButtonDraggable** property.

 


[View\[ASPX\]]

[] 

[\<%][\--Rendering the Chart Control\--][%\>]

[  ]

[    [\<%][=]Html.Chart([\"chart_Model\"])]

[            [//Enabling the print button]]

**[        .PrintButtonVisible([true])]**

[            [//enabling the drag functionality of the print button]]

**[        .PrintButtonDraggable([true])]**

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

[         .ChartSeriesSkins([ChartSeriesSkins]. DefaultAlpha)]

[        .BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[        [%\>]][]


 


[View\[cshtml\]]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[  ]

[    [\@{] Html.Chart([\"chart_Model\"])]

[            [//Enabling the print button]]

**[        .PrintButtonVisible([true])]**

[            [//enabling the drag functionality of the print button]]

**[        .PrintButtonDraggable([true])]**

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

[         .ChartSeriesSkins([ChartSeriesSkins]. DefaultAlpha)]

[        .BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[.Render();]

[}][]


[        ]

Step 2:

Add the code displayed below in the Controller.

[] 


[public][ [ActionResult] Index()]

[        {]

[] 

[            [return] View();]

[        }][]


Step 3:

Run the code, to get the following output:

{border="0"}

Figure 347: Chart with Print button

[] 

Step 4:

Double-click the **Print** button, to print the chart.

[]{#related-topics}

