---
title: chartmodel52.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel52.md
created_at: 2025-08-05
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

To customize the Watermark text through ChartModel:

[] 

Step 1:

View:

Add the code displayed below in the aspx file.

[] 


[View\[ASPX\]]

[] 

[\<%][\--Rendering the Chart Control\--][%\>]

[  ]

[        [\<%][=] Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]) [%\>]]**[]**


 


[View\[cshtml\]]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[] 

[@(][new][ [HtmlString]][(][Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\])][.ToString())[)]][  ]


[        ]

Step 2:

Controller:

The Watermark text can be set by using the **Text** property. The Watermark text can be positioned by using the **VerticalAlignment** and **VerticalAlignment** properties. The opacity of the text can be set by using the **Opacity** property. The **ZOrder** is used to set the display of the text, if the text can be displayed behind or over the ChartArea. The text appearance can be customized by using the **Font** and **TextColor** properties.

Add the code displayed below in the Controller.

**[]** 


[public][ [ActionResult] Index()]

[        {]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[] 

[            [//Setting the watermark text]]

[            chartModel.ChartArea.ChartArea.Watermark.Text = [\"Syncfusion\"];]

[            [//Setting the Zorder to display the text over the chart area]]

[            chartModel.ChartArea.ChartArea.Watermark.ZOrder = [ChartWaterMarkOrder].Over;]

[            [//setting the vertical alignment of the text]]

[            chartModel.ChartArea.ChartArea.Watermark.VerticalAlignment = [ChartAlignment].Center;]

[            [//setting the horizontal alignment of the text]]

[            chartModel.ChartArea.ChartArea.Watermark.HorizontalAlignment = [ChartAlignment].Center;]

[            [//setting the opacity]]

[            chartModel.ChartArea.ChartArea.Watermark.Opacity = 60f;]

[            [//setting the text color]]

[            chartModel.ChartArea.Watermark.TextColor = [Color].FromArgb(171, 153, 177);]

[            [//setting the font style]]

[            chartModel.ChartArea.ChartArea.Watermark.Font = [new] [Font]([\"Arial\"], 20);]

[       ]

[            [ChartSeries] series;]

[            series = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType].Column);]

[            series.Text = series.Name;]

[            series.Points.Add(1997, 437);]

[            series.Points.Add(1999, 311);]

[            series.Points.Add(2003, 466);]

[            chartModel.Series.Add(series);]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[            chartModel.ChartSeriesSkins = [ChartSeriesSkins].Pastel;]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[] 

[            [return] View();]

[        }]


**[]** 

Step 3:

Run the code, to get the following output.

[] 

{border="0"}

Figure 313: Chart - Watermark support

[]{#related-topics}

