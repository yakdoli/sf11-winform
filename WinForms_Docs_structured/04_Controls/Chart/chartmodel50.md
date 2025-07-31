---
title: chartmodel50.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartmodel50.md
created_at: 2025-07-03
---






#### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

The steps to apply skins in any chart through ChartModel are as follows:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the SeriesType.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the **Skins** property to any ChartModel Skins IEnumerable.

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [        ][public][ [ActionResult] SimpleChart()]                                                         |
|                                                                                                                                                                                                                                                                         |
| [        {            ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [            [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [            [// Create chart series and add data points to it.]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [            ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [                        [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the series, add the points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]                       |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| **[chartModel.Skins = [ChartModelSkins].Office2007Blue;            ]**                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ] |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [            [return] View(); ]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[ASPX\]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| [\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]] |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View \[cshtml\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [@(][new][ [HtmlString]][(Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model).ToString())[)]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

7.   Build and run the code, to get the following output:

{border="0"}

Figure 306: Office 2007 Blue Skin

The following screenshots show the chart in different skins:

{border="0"}

Figure 307: Almond Skin

[] 

{border="0"}

Figure 308: Blend Skin

[] 

[]{#related-topics}

