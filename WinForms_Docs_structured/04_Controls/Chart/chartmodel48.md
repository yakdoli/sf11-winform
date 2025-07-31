---
title: chartmodel48.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel48.md
created_at: 2025-07-03
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create an Axis Title in any chart type through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Line**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [        [public] [ActionResult] SimpleChart()]                                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| [        {            ]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [            [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the series, add the points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]                              |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.Title = [\"XAxis\"];]**                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.TitleColor = [Color].Green;]**                                                                                                                                  |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.TitleAlignment = [StringAlignment].Center;]**                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.Font = [new] [Font]([\"Verdana\"], 10, System.Drawing.[FontStyle].Bold);]**                |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.Title = [\"YAxis\"];]**                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.TitleColor = [Color].Red;]**                                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| **[            chartModel.PrimaryXAxis.TitleAlignment = [StringAlignment].Center;]**                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-- Set needed properties to chartmodel to set skin, size, legend visibility and so on   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ] |
|                                                                                                                                                                                                                                                                    |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [            [return] View(); ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 


View \[ASPX\]

[] 

[\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]]

[] 


[] 

[] 


View \[cshtml\]

 

[@(][new][ [HtmlString]][(Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model).ToString())[)]]

[] 

[] 


[] 

[] 

6.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 277: Customized Axis Titles

[]{#related-topics}

