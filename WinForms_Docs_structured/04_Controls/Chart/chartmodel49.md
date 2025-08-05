---
title: chartmodel49.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel49.md
created_at: 2025-08-05
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create legend customization in any chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the Legend related properties, as shown in the code snippet displayed below.

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.


\[C#\]            

[        ][public][ [ActionResult] SimpleChart()]

[        {            ]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            [// Create chart series and add data points to it.]]

[            ]

[                        [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the series, add the points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]

[] 

**[            chartModel.ShowLegend = [true];]**

**[            chartModel.LegendPosition = [ChartDock].Top;]**

**[            chartModel.LegendsPlacement = [ChartPlacement].Outside;]**

**[            chartModel.Legend.Alignment = [ChartAlignment].Center;]**

[            ]

[    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ]

[] 

[            ViewData.Model = chartModel;]

[            [return] View(); ]

[}]


[] 

6.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 


View \[ASPX\]

[] 

[\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]][]


[] 


View \[cshtml\]

[] 

[@(][new][ [HtmlString]][(Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model).ToString())[)]]

[] 


7.   Build and run the code, to get the following output:

 

{border="0"}

Figure 303: Legend Position Top, Alignment Center, and Placement as Outside

[]{#related-topics}

