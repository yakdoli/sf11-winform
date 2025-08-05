---
title: linecharts5.md
original_path: WinForms_Docs/04_Controls/Chart/linecharts5.md
created_at: 2025-08-05
---






##### Line Charts[]{#p72} {#line-charts style="tab-stops: 0pt"}

###### 4.1.1.4.1.1 Line Chart {#line-chart style="tab-stops: 0pt"}

Line Charts join points on a plot using straight lines showing trends in data at equal intervals. Line charts treats the input as non-numeric, categorical information, equally spaced along the x-axis. This is appropriate for categorical data, such as text labels, but can produce unexpected results when the x values consist of numbers.

 

When rendered in 3D the plot looks like a ribbon and hence such types are also referred to as Ribbon or Strip Charts.

 

The appearance of the lines and the points can be configured with options such as the colors used, thickness of the lines and the symbols displayed.

 

{border="0"}

Figure 114: Line Chart

[] 

Data Requirements

The following are the details about Line Chart:

[] 

Table 21: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Template

While setting template the following parameters can be used.

[] 

Table 22: Template parameters


  ---------- ------------- ------------------------------
  Name       Type          Description
  X1         double        x-coordinate of first point
  Y1         double        y-coordinate of first point
  X2         double        x-coordinate of second point
  Y2         double        y-coordinate of second point
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ------------------------------


[] 

A sample which demonstrates Line Chart Types is available in the following sample installation path.

[] 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Line Chart Demo***

[] 

See Also

[]{.UGHyperlink}

[]{#p73} 

###### 4.1.1.4.1.2 Fast Line Chart {#fast-line-chart style="tab-stops: 0pt"}

Use a Fast Line chart instead of a Line chart when displaying a large number of data points in the chart. This chart type improves performance by foregoing some features in the Line chart.

[] 

{border="0"}

Figure 115: FastLine Chart

 

Data Requirements

The following are the details about Fast Line Chart:

[] 

Table 23: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | One         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

 

Template

While setting template the following parameters can be used:

[] 

Table 24: Template Parameter


  ---------- ------------- ------------------------------
  Name       Type          Description
  X1         Double        x-coordinate of first point
  Y1         Double        y-coordinate of first point
  X2         Double        x-coordinate of second point
  Y2         Double        y-coordinate of second point
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ------------------------------


[] 

A sample which demonstrates Line Chart Types is available in the following sample installation path.

[] 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Line Chart Demo***

**** 

**** 

Customization of FastLine

Essential Chart enables you to customize the look and feel of the Fastline chart.

Following types of lines are supported for FastLine chart:

[·      ]Dash line

[·      ]Dot line

[·      ]Dash-dot line

[·      ]Dash-dot-dot line

 

Property

Table 25: Property Table


  ---------- --------------------------------------------------------------- ------------------------------------------------ -------------------- --------------------------------------------------------------------------------------------------------------
  Property   Description                                                     Type                                             Data Type            Reference links
  Pen        Gets and sets various types of pen for drawing fastchat type.   Attached property for ChartFastSeriesPresenter   System.Drawing.Pen   [[Pen Class]{.UGHyperlink}](http://msdn.microsoft.com/en-us/library/system.drawing.pen.aspx)[]{.UGHyperlink}
  ---------- --------------------------------------------------------------- ------------------------------------------------ -------------------- --------------------------------------------------------------------------------------------------------------


 

Customizing Fastline

To customize the FastLine chart, use the *Pen* property of *ChartFastSeriesPresenter*.

 

The following code illustrates this:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][ChartSeries][ Name][=\"series\"][ Type][=\"FastLine\"][ IsIndexed][=\"True\"][ [ Interior][=\"LightBlue\" \>]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                            ][\<][syncfusion][:][ChartFastSeriesPresenter.Pen][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                                ][\<][Pen][ Brush][=\"Black\"][ DashCap][=\"Round\"][ DashStyle][=\"DashDot\"][ StartLineCap][=\"Round\"][ EndLineCap][=\"Round\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                            ][\</][syncfusion][:][ChartFastSeriesPresenter.Pen][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                        ][\</][syncfusion][:][ChartSeries][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 116: Customized Fastline

[] 

Sample Link

To view a sample

1.   Open the Syncfusion Dashboard.

2.   Select User Interface.

3.   Click the **WPF** drop-down list and select **Explore Samples**.

4.   Navigate to ***Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Customization\\ FastLine Customization Demo\\***

[] 

**** 

**** 

See Also

[]{.UGHyperlink}

[]{#p74} 

 

###### 4.1.1.4.1.3 Spline Chart {#spline-chart style="tab-stops: 0pt"}

Spline Chart is similar to a Line Chart except that it connects the different data points using splines instead of straight lines.

 

When rendered in 3D the plot looks like a ribbon and hence such types are also referred to as Ribbon or Strip Charts.

 

The appearance of the lines and the points can be configured with options such as the colors used, thickness of the lines and the symbols displayed.

[] 

{border="0"}

Figure 117: Spline Chart\
\

Data Requirements

[] 

The following are the details about Spline Chart:

[] 

Table 26: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Spline Settings

[] 

Table 27: Spline Setting


  ----------------------------------- -------- ------------- ---------------------------------------------------------------
  Name                                Type     Container     Description
  ChartSplineType.SplineCoefficient   double   ChartSeries   attached property which lets you control the spline curvature
  ----------------------------------- -------- ------------- ---------------------------------------------------------------


[] 

Template

While setting template the following parameters can be used.

[] 

Table 28L Template Parameter


  ---------- ------------- ------------------------------
  Name       Type          Description
  X1         double        x-coordinate of first point
  Y1         double        y-coordinate of first point
  X2         double        x-coordinate of second point
  Y2         double        y-coordinate of second point
  Geometry   Geometry      segment geometry
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ------------------------------


[] 

A sample which demonstrates Line Chart Types is available in the following sample installation path.

[] 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Line Chart Demo***

**** 

See Also

[]{.UGHyperlink}

[]{#p75} 

 

###### 4.1.1.4.1.4 Rotated Spline Chart {#rotated-spline-chart style="tab-stops: 0pt"}

A Rotated Spline Chart is similar to a Spline Chart. The only difference is that it would be rotated. It plots one or several series of data and joins each series by smooth, rotated spline curves instead of straight lines.

 

The following image shows a sample Rotated Spline Chart.

[] 

{border="0"}

Figure 118: Rotated Spline Chart

***[]*** 

Data Requirements

The following are the details about Rotated Spline Chart:

**[]** 

Table 29: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Rotated Spline Settings

[] 

Table 30: Rotated Spline Settings


  ----------------------------------- -------- ------------- ---------------------------------------------------------------
  Name                                Type     Container     Description
  ChartSplineType.SplineCoefficient   double   ChartSeries   attached property which lets you control the spline curvature
  ----------------------------------- -------- ------------- ---------------------------------------------------------------


[] 

A sample which demonstrates Line Chart Types is available in the following sample installation path.

[] 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Line Chart Demo***

***[]*** 

See Also

[]{.UGHyperlink}

[]{#p76} 

###### 4.1.1.4.1.5 Step Line Chart {#step-line-chart style="tab-stops: 0pt"}

Step Line Charts use horizontal and vertical lines to connect data points resulting in a step like progression.

[] 

{border="0"}

Figure 119: Step Line Chart

[] 

Data Requirements

The following are the details about Step Line Chart:

**[]** 

Table 31: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Template

While setting template the following parameters can be used:

[] 

Table 32: Template Parameter


  ---------- ----------------- ---------------------------------
  Name       Type              Description
  X1         double            x-coordinate of first point
  Y1         double            y-coordinate of first point
  X2         double            x-coordinate of second point
  Y2         double            y-coordinate of second point
  StepX      double            x-coordinate of transient point
  StepY      double            y-coordinate of transient point
  Points     PointCollection   collection of  segment points
  Interior   Brush             column color
  Series     ChartSeries       reference to series-owner
  ---------- ----------------- ---------------------------------


[] 

A sample which demonstrates Line Chart Types is available in the following sample installation path.

[] 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Line Chart Demo***

**** 

See Also

[]{.UGHyperlink}

 

[]{#related-topics}

