---
title: builder59.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\builder59.md
created_at: 2025-07-03
---






#### Builder {#builder style="tab-stops: 0pt"}

[] 

The steps to add the Interactive Cursor to the ChartModel through Builder are as follows:

Step 1:

View:

Add the code displayed below in the aspx file. The Interactive cursors can be enabled by setting the **ShowInteractiveCursors** property to true. The Interactive cursors can be customized by using the **InteractiveCursors** mapper.

[] 


[View\[ASPX\]]

[] 

[\<%][\--Rendering the Chart COntrol\--][%\>]

[    [\<%][=]Html.Chart([\"chart_Model\"])]

[        [//Enabling the Interactive cursors]]

**[                .ShowInteractiveCursors([true])]**

[    .Series(series=\>{]

[        series.Add()]

[            .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Line)]

[       .Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 137 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 211 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 766 });]

[        });]

[        series.Add()]

[      .Points(points =\>]

[      {]

[          points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[          points.Add().X(1999).YValues([new] [double]\[\] { 311 });]

[          points.Add().X(2003).YValues([new] [double]\[\] { 466 });]

[      })]

[        .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Line);]

[    })]

[        [//Customizing the Interactive cursors]]

[     .ChartArea(area =\>]

[            area]

**[.InteractiveCursors(intercursors =\>]**

**[            {]**

**[               intercursors.Add(0).Color(System.Drawing.[Color].Red);]**

**[               intercursors.Add(1).Color(System.Drawing.[Color].Blue).XPosition(6);]**

**[            }))]**

[        .Skins([ChartModelSkins].Office2007Blue)]

[         .ChartSeriesSkins([ChartSeriesSkins].DefaultAlpha)]

[        .BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[] 

[    [%\>]][]


[] 


[View\[cshtml\]]

[] 

[@\*][\--Rendering the Chart COntrol\--][\*@]

[    [\@{] Html.Chart([\"chart_Model\"])]

[        [//Enabling the Interactive cursors]]

**[                .ShowInteractiveCursors([true])]**

[    .Series(series=\>{]

[        series.Add()]

[            .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Line)]

[       .Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 137 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 211 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 766 });]

[        });]

[        series.Add()]

[      .Points(points =\>]

[      {]

[          points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[          points.Add().X(1999).YValues([new] [double]\[\] { 311 });]

[          points.Add().X(2003).YValues([new] [double]\[\] { 466 });]

[      })]

[        .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Line);]

[    })]

[        [//Customizing the Interactive cursors]]

[     .ChartArea(area =\>]

[            area]

**[.InteractiveCursors(intercursors =\>]**

**[            {]**

**[               intercursors.Add(0).Color(System.Drawing.[Color].Red);]**

**[               intercursors.Add(1).Color(System.Drawing.[Color].Blue).XPosition(6);]**

**[            }))]**

[        .Skins([ChartModelSkins].Office2007Blue)]

[         .ChartSeriesSkins([ChartSeriesSkins].DefaultAlpha)]

[        .BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[.Render();]

[] 

[    [}]][]


 

Step 2:

Add the code displayed below in the Controller.

[] 


[public][ [ActionResult] Index()]

[        {]

[            [return] View();]

[] 

[        }][]


Step 3:

Run the code, to get the following output:

[] 

{border="0"}

Figure 338: Chart - Interactive Cursor

[] 

[]{#related-topics}

