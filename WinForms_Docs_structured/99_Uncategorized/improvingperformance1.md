---
title: improvingperformance1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\improvingperformance1.md
created_at: 2025-07-03
---








  









## Improving Performance {#improving-performance style="tab-stops: 0pt"}

 

Properties and Methods used to improve chart performance

 


+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| Chart control                       | Description                                                                                                                                                                                                                     |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| Property                                                                                                                                                                                                                                                              |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| ChartControl.ImprovePerformance     | Instructs the chart to calculate the axes ranges only before painting and not at every series adding or moving. Performance of a Chart with large number of series will be improved significantly, if this property is enabled. |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     | By default this property is false.                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| CalcRegions                         | This property by default is **true**. This controls the Tooltips, Autohighlighting properties and RegionHit events. If these properties and events are not used, this property can be set to false for better performance.      |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| ChartSeries.EnableStyles            | Disabling this property will in turn disable the point symbols and point text which speeds up the chart.                                                                                                                        |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| ChartSeries.Style.DisplayShadow     | Setting this property to false will not render the series with shadow, which will increase the speed of the chart.                                                                                                              |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     | By default this property is set to **false**.                                                                                                                                                                                   |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| Indexed                             | The chart renders faster if the series is not indexed. This of course, may or may not be possible in all cases.                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
|                                     | By default this property is **false**.                                                                                                                                                                                          |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| BackInterior                        | The background style for the Chart control is specified using this property and if this property is not set with gradient or pattern style, will help improve the performance of the chart.                                     |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| ChartArea.BackInterior              | This property sets the back color for the chart area. If not set with gradient or pattern style, will help improve the performance of the chart.                                                                                |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| ChartInterior                       | If this property which fills the chart interior, not set with gradient or pattern style, will improve the performance of the chart.                                                                                             |
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| Method                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     |                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                 |
| BeginUpdate and EndUpdate           | Encapsulate your \"data points adding code\" within **BeginUpdate** and **EndUpdate** to improve Chart initialization speed. See the example below.                                                                             |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [// Improves the performance of the chart when a large number of series are used.]                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.ImprovePerformance = ][true][;] |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.CalcRegions = [false];]                                                                                                     |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].EnableStyles = [false];]                                                                                        |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Style.DisplayShadow = [false];]                                                                                 |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Indexed = [true];]                                                                                                          |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [//BeginUpdate and EndUpdate methods]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [private][ [DataModel] datamodel1;]                                                                                                               |
|                                                                                                                                                                                                                                                             |
| [ChartSeries][ series = [this].chartControl1.Model.NewSeries([\"Line 1\"], [ChartSeriesType].Line);]  |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.BeginUpdate();]                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [// Add a whole bunch of points to the series like this: series.Points.Add(1, 10), etc.]                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.EndUpdate();]                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [\' Improves the performance of the chart when a large number of series are used.]                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [Me][.chartControl1.ImprovePerformance = ][True]                                                               |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Me][.][chartControl1.CalcRegions = [False]]                                                           |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Me][.chartControl1.Series\[0\].EnableStyles = [False]]                                                                                                  |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Me][.chartControl1.Series\[0\].Style.DisplayShadow = [False]]                                                                                           |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Me][.chartControl1.Indexed = [True]]                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [\'BeginUpdate and EndUpdate methods]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [Private][ datamodel1 [As] DataModel]                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [Private][ series [As] ChartSeries = [Me].chartControl1.Model.NewSeries([\"Line 1\"], ChartSeriesType.Line)] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [Me][.chartControl1.BeginUpdate()]                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [\'Add a whole bunch of points to the series like this: series.Points.Add(1, 10), etc.]                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [Me][.chartControl1.EndUpdate()]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p26} 

 

[]{#related-topics}

