---
title: chartseries.md
original_path: WinForms_Docs/04_Controls/Chart/chartseries.md
created_at: 2025-08-05
---








  









## Chart Series {#chart-series style="tab-stops: 0pt"}

[] 

Provide data for the chart through the **ChartSeries**. ChartSeries acts as a wrapper around data that is to be displayed, and associates styles with the data. The data that is to be displayed is contained in either the **IChartSeriesModel** or the **IEditableChartSeriesModel** implementation. The style used to display the points is stored in a contained implementation of IChartSeriesStylesModel.

Here is some sample code to create a new series and add it to the chart.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [// 1) One way to create a series:]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [ChartSeries][ series = [new] [ChartSeries]([\"Sales Performance\"], [ChartSeriesType].Bar);] |
|                                                                                                                                                                                                                                                                          |
| [series.Points.Add(0,200);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series.Points.Add(1,300);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [// Remember to add the series to the chart.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [ChartWebControl1.Series.Add(series);]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [// 2) Another way to create a series]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [// This will automatically add the series to the chart]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| [ChartSeries][ series = ChartWebControl1.Model.NewSeries([\"Sales Performance\"], [ChartSeriesType].Bar);]                              |
|                                                                                                                                                                                                                                                                          |
| [series.Points.Add(0,200);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series.Points.Add(1,300);]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [\' 1) One way to create a series:]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [Dim][ series [As] ChartSeries = [New] ChartSeries([\"Sales Performance\"], ChartSeriesType.Bar)]              |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add(0,200)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add(1,300)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [\' Remember to add the series to the chart.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series.Add(series)]                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [\' 2) Another way to create a series]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [\' This will automatically add the series to the chart]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [ChartSeries][ series = [Me].ChartWebControl1.Model.NewSeries([\"Sales Performance\"], [ChartSeriesType].Bar)] |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add(0,200)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add(1,300)]                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note:[ ]Same ChartSeries object being added to more than one chart is not supported. It binds the series to the default primary axis always.


[] 

Chart Points

**[]** 

The **ChartPoint** class holds value information about a single point in a series (x and y values). The following table describes the kind of x and y values you can specify via a chart point.

[] 


  ------ ------------------ --------------------
  Axis   Number of Values   Value Types
  X      1                  double or DateTime
  Y      1 or more          double or DateTime
  ------ ------------------ --------------------


[] 

Here is some sample code that shows adding data points to the **Points** collection. You could also optionally create a ChartPoint instance first and then add it to the Points collection.

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                                 |
| []                                                                                        |
|                                                                                                                 |
| [// Option 1: 1 X double value; 2 double Y values in a point] |
|                                                                                                                 |
| [series1.Points.Add(0, 2.5, 3.5);]                                          |
|                                                                                                                 |
| []                                                                          |
|                                                                                                                 |
| [// Option 2: 1 X double value; 1 DateTime Y value]           |
|                                                                                                                 |
| [series2.Points.Add(1, DateTime.Now);]                                      |
|                                                                                                                 |
| []                                                                          |
|                                                                                                                 |
| [// Option 3: 1 X DateTime value; 1 double Y value]           |
|                                                                                                                 |
| [series1.Points.Add([DateTime].Now, 5.3);]             |
+-----------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                              |
|                                                                                                                 |
| []                                                                                        |
|                                                                                                                 |
| [\' Option 1: 1 X double value; 2 double Y values in a point] |
|                                                                                                                 |
| [series1.Points.Add(0, 2.5, 3.5)]                                           |
|                                                                                                                 |
| []                                                                          |
|                                                                                                                 |
| [\' Option 2: 1 X double value; 1 DateTime Y value]           |
|                                                                                                                 |
| [series2.Points.Add(1, DateTime.Now)]                                       |
|                                                                                                                 |
| []                                                                          |
|                                                                                                                 |
| [\' Option 3: 1 X DateTime value; 1 double Y value]           |
|                                                                                                                 |
| [series1.Points.Add([DateTime].Now, 5.3)]              |
+-----------------------------------------------------------------------------------------------------------------+

[] 

ValueType

**[]** 

Always use the **ChartAxis.ValueType** property to specify what kind of values you have added in the series data points for the corresponding axis.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                                |
|                                                                                                                                                                                         |
| [// To specify DateTime values in the X axis]                                                                                         |
|                                                                                                                                                                                         |
| [this][.ChartWebControl1.PrimaryXAxis.ValueType = [ChartValueType].DateTime;] |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [// To specify Double values]                                                                                                         |
|                                                                                                                                                                                         |
| [this][.ChartWebControl1.PrimaryXAxis.ValueType = [ChartValueType].Double;]   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                                             |
|                                                                                                                                                                                      |
| [\' To specify DateTime values in the X axis]                                                                                      |
|                                                                                                                                                                                      |
| [Me][.ChartWebControl1.PrimaryXAxis.ValueType = [ChartValueType].DateTime] |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [\' To specify Double values]                                                                                                      |
|                                                                                                                                                                                      |
| [Me][.ChartWebControl1.PrimaryXAxis.ValueType = [ChartValueType].Double]   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Note that to display the text right next to the data points, the  property of the data point\'s style should be set.

The Chart Series features are elaborated in more detail in the following sub-topics.

[]{#p78} 

More:











