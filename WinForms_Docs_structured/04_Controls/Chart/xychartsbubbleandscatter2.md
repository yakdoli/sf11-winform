---
title: xychartsbubbleandscatter2.md
original_path: WinForms_Docs/04_Controls/Chart/xychartsbubbleandscatter2.md
created_at: 2025-08-05
---






##### XY Charts (Bubble and Scatter)[]{#p100} {#xy-charts-bubble-and-scatter style="tab-stops: 0pt"}

###### 4.1.1.4.6.1 Scatter Chart {#scatter-chart style="tab-stops: 0pt"}

Scatter Charts, also known as XY Charts, are a plot of Y values and X values along two axes. The points are not joined together and can be customized using shapes or images to make them easily identifiable, usually independent of time.

 

The scatter graph lets you plot data points based on two independent variables. The variable that we seek to predict is called the dependent variable or Y-variable. The variable on which it depends is called the independent variable or the X-variable. Scatter graphs can chart multiple data sets, each represented by a different symbol and each having any number of data points.

 

It is used to display numerical data, either discrete or continuous. Scatter charts are commonly used for visualizing scientific data.

 

The following image shows a multi series Scatter Chart.

[] 

{border="0"}

Figure 140: Scatter Chart

 

Data Requirements

[] 

Table 81: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


**[]** 

Template

While setting template the following parameters can be used:

[] 

Table 82: Template Parameters


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x point coordinate
  Y          double        y point coordinate
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

A sample which demonstrates Scatter and Bubble Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Scatter And Bubble Chart Demo***

 

Fast Scatter chart Type

Fast Scatter charts are similar to Scatter Charts as they are a plot of Y values and X values along two axes. The points are not joined together and can be customized using shapes or images to make them easily identifiable, usually independent of time.

 

Fast Scatter charts can present multiple data sets, each represented by a different symbol and each having any number of data points. It is used to display numerical data, either discrete or continuous.

 

The following points mark the advantages of **Fast Scatter Charts** over **Scatter Charts**:

[] 

[·      ]The Fast Scatter Charts are rendered using drawing visuals.

[·      ]They load faster than the scattered charts.

[·      ]They ensure high performance for displaying data.

[·      ]They can be used as real time charts to render huge number of data points.

[] 

The Chart type Fast Scatter is added in the Enum of type **ChartTypes**.

[] 

{border="0"}

Figure 141: Fast Scatter Charts

[] 

Data Requirements

[] 

Table 83: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


**[]** 

Template

While setting template the following parameters can be used:

[] 

Table 84: Template Parameter


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x point coordinate
  Y          double        y point coordinate
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

The following code snippet illustrates the usage of Fast Scatter charts.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][ChartSeries][ Type][=\"FastScatter\"][ Name][=\"series1\"][ Stroke][=\"Black\"][ DataSource][=\"{][Binding][}\"/\>] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [ChartSeries][ series = ][new][ ][ChartSeries][();] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Type = ][ChartTypes][.FastScatter;]                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the sample.

[] 

A Fast Scatter chart is displayed.

[] 

{border="0"}

Figure 142: Fast Scatter Chart

[] 

A sample which demonstrates Fast Scatter Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\Essential Studio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Performance-\> Fast chart types***

 

See Also

]{.UGHyperlink}

[] 

###### 4.1.1.4.6.2 Bubble Chart {#bubble-chart style="tab-stops: 0pt"}

Bubble Chart is an extension of the Scatter Chart (or XY-chart) where each data marker is represented by a circle whose dimension forms a third variable. Consequently, bubble charts allow three-variable comparisons allowing for easy visualization of complex interdependencies that are not apparent in two-variable charts. Bubble charts are frequently used in market and product comparison studies.

 

Though it\'s called a bubble chart, the data marker can be rendered as either a circle, image or square using the **BubbleType** property.

 

The following image shows a multi series Bubble Chart.

[] 

{border="0"}

Figure 143: Bubble Chart

[] 

Data Requirements

[] 

Table 85: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | two         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


**[]** 

BubbleType Properties

[] 

Table 86: Property Table


  --------------------------- -------- ------------- -----------------------
  Name                        Type     Container     Description
  ChartBubbleType.MinRadius   double   ChartSeries   minimal figure radius
  ChartBubbleType.MaxRadius   double   ChartSeries   maximal figure radius
  --------------------------- -------- ------------- -----------------------


[] 

Template

While setting template the following parameters can be used:

[] 

Table 87: Template Parameter


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x column coordinate
  Y          double        y column coordinate
  Width      double        column width
  Height     double        column height
  Radius     double        figure radius
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

A sample which demonstrates Scatter and Bubble Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Scatter And Bubble Chart Demo***

**** 

See Also

[]{.UGHyperlink}

[] 

[]{#related-topics}

