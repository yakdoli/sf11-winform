---
title: boxandwhiskerchart.md
original_path: WinForms_Docs/04_Controls/Chart/boxandwhiskerchart.md
created_at: 2025-08-05
---






#### Box and Whisker Chart {#box-and-whisker-chart style="tab-stops: 0pt"}

[] 

In 1977, John Tukey published an efficient method for displaying a five-number data summary. The graph is called a Box and Whisker plot (also known as BoxPlot) and summarizes the following statistical measures.

[] 

[·      ]median

[·      ]upper and lower quartiles (75 percentile to 25 percentile)

[·      ]minimum and maximum data values

[] 

The following is an example of a Box and Whisker plot.

[] 

{border="0"}

**[]** 

Figure 78: Box and Whisker Chart

[] 

The Box and Whisker plot is interpreted as follows.

[] 

[·      ]The box itself contains the middle 50% of the data. The upper edge (hinge) of the box indicates the 75th percentile of the data set and the lower hinge indicates the 25th percentile. The range of the middle two quartiles is known as the inter-quartile range.

[·      ]The line in the box indicates the median value of the data.

[·      ]Box and Whisker chart has two modes, Normal mode and Percentile mode.

[·      ]In Normal Mode, if the median line within the box is not equi-distant from the hinges, then the data is skewed. The ends of the vertical lines or \"whiskers\" indicate the minimum and maximum data values, unless outliers are present, in which case the whiskers extend to a maximum of 1.5 times the inter-quartile range.

[·      ]In Percentile Mode: \[Set **Series1.ConfigItems.BoxAndWhiskerItem.PercentileMode** property to ***true***\], the ends of the vertical lines or \"whiskers\" will be decided by the Series1.ConfigItems.BoxAndWhiskerItem.Percentile property value. For example, if the \'Percentile\' value is 0.15, then the minimum value will be the 15th percentile of the overall data set and the maximum value will be 85th percentile of the overall data set.


Note:


1.   The percentile value should lie between 0.0 to 0.25.

2.   It is not possible to set upper Percentile value. It is calculated automatically based on the Percentile value.

   

 For Ex:

          Percentile = 0.15

          Upper Percentile = 1 - Percentile = 0.85.

In Normal mode, Outliers are present in which case the whiskers extend to a maximum of 1.5 times the inter-quartile range. But in Percentile mode, Outliers will be calculated based on the Percentile value.

    

For example:

          Percentile = 0.15

Outliers are present in which case the whiskers extend to minimum and maximum of 15th and 85th percentile of overall data set, respectively. If \'Percentile\' value is Zero, then, there is no outliers in the Chart.

 

3.   The width of the Outliers can be adjusted by using this:

           \'Series1.ConfigItems.BoxAndWhiskerItem.OutLierWidth\' property.

        If it is zero, the width of the outlier will be calculated based on the data points range.

**[]** 

**[Chart Details]**

**[]** 


+---------------------------------------+--------------------------------------------------------------+
| **[]**                             |
|                                                                                                      |
| Details                                                                                              |
+---------------------------------------+--------------------------------------------------------------+
| Number of Y values per point          | 5 (minimum, lower quartile, median, upper quartile, maximum) |
+---------------------------------------+--------------------------------------------------------------+
| Number of Series                      | One or more                                                  |
+---------------------------------------+--------------------------------------------------------------+
| Cannot be Combined with               | Pie, Bar, Polar, Radar                                       |
+---------------------------------------+--------------------------------------------------------------+


[] 

Box and Whisker series can be added to the chart using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                |
| [// Create chart series and add data points into it.]                                                                                        |
|                                                                                                                                                                                                |
| [ChartSeries series1 = [this].[ChartWebControl1].Model.NewSeries(\"Series 1\",ChartSeriesType.BoxAndWhisker );] |
|                                                                                                                                                                                                |
| [series1.Points.Add(1, 5, 8 ,12, 15, 18);]                                                                                                                 |
|                                                                                                                                                                                                |
| [series1.Points.Add(2, 4, 6, 10, 12, 14);]                                                                                                                 |
|                                                                                                                                                                                                |
| [series1.Points.Add(3, 2, 4, 7, 14, 18);]                                                                                                                  |
|                                                                                                                                                                                                |
| [                        ]                                                                                                                                 |
|                                                                                                                                                                                                |
| [ChartSeries series2 = [this].[ChartWebControl1].Model.NewSeries(\"Series 2\",ChartSeriesType.BoxAndWhisker );] |
|                                                                                                                                                                                                |
| [series2.Points.Add(1, 6, 9, 15, 18, 20);]                                                                                                                 |
|                                                                                                                                                                                                |
| [series2.Points.Add(2, 7, 9, 13, 15, 16);]                                                                                                                 |
|                                                                                                                                                                                                |
| [series2.Points.Add(3, 6, 8, 10, 15, 19);]                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [// Add the series to the chart series collection.]                                                                                          |
|                                                                                                                                                                                                |
| [this][.[ChartWebControl1].Series.Add(series1);]                                    |
|                                                                                                                                                                                                |
| [this][.[ChartWebControl1].Series.Add(series2);]                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [\' Create chart series and add data points into it.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [Dim][ series1 [As] ChartSeries = [Me].[ChartWebControl1].Model.NewSeries(\"Series 1\",ChartSeriesType.BoxAndWhisker)] |
|                                                                                                                                                                                                                                                                             |
| [series1.Points.Add(1, 5, 8 ,12, 15, 18)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [series1.Points.Add(2, 4, 6, 10, 12, 14)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [series1.Points.Add(3, 2, 4, 7, 14, 18)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [Dim][ series2 [As] ChartSeries = [Me].[ChartWebControl1].Model.NewSeries(\"Series 2\",ChartSeriesType.BoxAndWhisker)] |
|                                                                                                                                                                                                                                                                             |
| [series2.Points.Add(1, 6, 9, 15, 18, 20)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [series2.Points.Add(2, 7, 9, 13, 15, 16)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [series2.Points.Add(3, 6, 8, 10, 15, 19)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [\' Add the series to the chart series collection.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [Me][.[ChartWebControl1].Series.Add(series1)]                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [Me][.[ChartWebControl1].Series.Add(series2)]                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#p68} 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Customization Options[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{.UGHyperlink}                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [, ]{.UGHyperlink} |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

