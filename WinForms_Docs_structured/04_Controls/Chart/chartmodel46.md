---
title: chartmodel46.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel46.md
created_at: 2025-08-05
---






##### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Custom Axis Size in any chart through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType to **Line**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] SimpleChart()]                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [        {            ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [            [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the remaining points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]                                         |
|                                                                                                                                                                                                                                                                         |
| **[                  chartModel.PrimaryYAxis.AutoSize]**[ **= [false];**]                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| **[                  chartModel.PrimaryYAxis.Size]**[ **= [new] System.Drawing.[Size](26,100);**]                                                  |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ] |
|                                                                                                                                                                                                                                                                         |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [            [return] View(); ]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\][]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\][]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [@(][new][ [HtmlString](Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model).ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 268: Custom YAxis Size

[] 

[]{#related-topics}

