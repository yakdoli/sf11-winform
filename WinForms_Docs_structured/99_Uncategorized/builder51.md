---
title: builder51.md
original_path: WinForms_Docs/99_Uncategorized/builder51.md
created_at: 2025-08-05
---






#### Builder {#builder style="tab-stops: 0pt"}

[] 

To apply skins for the Chart series through Builder:

[] 

 

Step 1:

View:

 

Add the code displayed below in the Index.aspx file. The Chart Series Skins can be set by using the **ChartSeriesSkins** property.

[] 


[View \[ASPX\]]

[] 

[\<%][=][ Html.Chart([\"ChartModel\"])[]]

[//Applying the Chart Series Skins]

[    .ChartSeriesSkins([ChartSeriesSkins].Colorful)]

[] 

[    .Skins([ChartModelSkins].Office2007Blue)]

[            ]

[    .Series(series=\>{]

[        series.Add().Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 451 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 366 });]

[        }).Name([\"Saab\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[    series.Add().Points(points=\>{]

[        points.Add().X(1997).YValues([new] [double]\[\] { 556 });]

[        points.Add().X(1999).YValues([new] [double]\[\] { 491 });]

[        points.Add().X(2003).YValues([new] [double]\[\] { 737 });]

[] 

[    }).Name([\"Volvo\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[        series.Add().Points(points=\>{]

[            points.Add().X(1997).YValues([new] [double]\[\] { 156 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 100 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 537 });]

[        }).Name([\"Volvo1\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[    }).BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[        ]

[] 

[] 

[        [%\>]]


[] 


[View \[cshtml\]]

[] 

[\@{][ Html.Chart([\"ChartModel\"])[]]

[//Applying the Chart Series Skins]

[    .ChartSeriesSkins([ChartSeriesSkins].Colorful)]

[] 

[    .Skins([ChartModelSkins].Office2007Blue)]

[            ]

[    .Series(series=\>{]

[        series.Add().Points(points =\>]

[        {]

[            points.Add().X(1997).YValues([new] [double]\[\] { 437 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 451 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 366 });]

[        }).Name([\"Saab\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[    series.Add().Points(points=\>{]

[        points.Add().X(1997).YValues([new] [double]\[\] { 556 });]

[        points.Add().X(1999).YValues([new] [double]\[\] { 491 });]

[        points.Add().X(2003).YValues([new] [double]\[\] { 737 });]

[] 

[    }).Name([\"Volvo\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[        series.Add().Points(points=\>{]

[            points.Add().X(1997).YValues([new] [double]\[\] { 156 });]

[            points.Add().X(1999).YValues([new] [double]\[\] { 100 });]

[            points.Add().X(2003).YValues([new] [double]\[\] { 537 });]

[        }).Name([\"Volvo1\"]).Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column);]

[    }).BorderAppearance(border =\> border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Emboss))]

[.Render();]

[        ]

[}][]

[] 


[        ]

Step 2:

Controller:

Add the code displayed below in the HomeController.cs file.

[       ]


[        [public] [ActionResult] Index()]

[        {]

[            [return] View();]

[        }]

[        ]


[] 

Step 3:

Run the code, to get the following output.

[] 

{border="0"}

Figure 310: ChartSeries Skin-Colorful

 

[]{#related-topics}

