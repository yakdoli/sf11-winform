---
title: columncharts5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\columncharts5.md
created_at: 2025-07-03
---






##### Column Charts {#column-charts style="tab-stops: 0pt"}

###### 4.1.1.4.3.1 Column Chart {#column-chart style="tab-stops: 0pt"}

Column Charts are among the most common chart types that are being used. It uses vertical bars (called columns) to display different values of one or more items. It is similar to a bar chart except that here the bars are vertical and not horizontal. Points from adjacent series are drawn as bars next to each other. 

It is used for comparing the frequency, count, total or average of data in different categories. It is ideal for showing the variations in the value of an item over time.

 

The following image shows a multi series Column Chart.

[] 

{border="0"}

Figure 126: Column Chart

[] 

Data Requirements

**[]** 

Table 46: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Custom Properties

**[]** 

Table 47: Custom Property


+-------------------+-----------------+-----------------+--------------------------------------+
| Name              | Type            | Container       | Description                          |
+-------------------+-----------------+-----------------+--------------------------------------+
| ChartType.Spacing | double          | ChartArea       | sets the interval between columns    |
|                   |                 |                 |                                      |
|                   |                 |                 | Possible values lie between 0 and 1. |
+-------------------+-----------------+-----------------+--------------------------------------+


[] 

Template

While setting template the following parameters can be used:

[] 

Table 48: Template Parameter


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x column coordinate
  Y          double        y column coordinate
  Width      double        column width
  Height     double        column height
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

A sample which demonstrates Column Chart Types is available in the following sample installation path.

[] 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Column Chart Demo***

**** 

See Also

[]{.UGHyperlink}

[]{#p85} 

###### 4.1.1.4.3.2 Column Range Chart {#column-range-chart style="tab-stops: 0pt"}

Column Range Chart is similar to the Column Chart except that each column is rendered over a range. Therefore the user must specify the y-axis Starting and Ending values for each point.

 

The following figure shows a Column Range Chart.

[] 

{border="0"}

Figure 127: Column Range Chart

Data Requirements

[] 

Table 49: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | two         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Custom Properties

[] 

Table 50: Custom Property


+-------------------+-----------------+-----------------+--------------------------------------+
| Name              | Type            | Container       | Description                          |
+-------------------+-----------------+-----------------+--------------------------------------+
| ChartType.Spacing | double          | ChartArea       | sets the interval between columns    |
|                   |                 |                 |                                      |
|                   |                 |                 | Possible values lie between 0 and 1. |
+-------------------+-----------------+-----------------+--------------------------------------+


[] 

Template

While setting template the following parameters can be used:

[] 

Table 51: Template Parameter


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x column coordinate
  Y          double        y column coordinate
  Width      double        column width
  Height     double        column height
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

A sample which demonstrates Column Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Column Chart Demo***

 

See Also

[]{.UGHyperlink}

[]{#p86} 

###### 4.1.1.4.3.3 Stacking Column Chart {#stacking-column-chart style="tab-stops: 0pt"}

Stacking Column Charts are similar to regular column charts except that the Y values stack on top of each other in the specified series order. This helps visualize the relationship of parts to the whole.

 

The following image shows a sample Stacking Column Chart.

[] 

{border="0"}

Figure 128: Stacking Column Chart

[] 

Data Requirements

[] 

Table 52: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


**[]** 

**[]** 

Custom StackingColumn100 Properties

[] 

Table 53: Custom Stacking Column 100 Property


+---------------------------------------------------+-----------------+-----------------+-----------------------------------------------------------------------------+
| Name                                              | Type            | Container       | Description                                                                 |
+---------------------------------------------------+-----------------+-----------------+-----------------------------------------------------------------------------+
| ChartStackingColumn100Type.ShowValueAsProbability | bool            | ChartArea       | y-axis range is set between 0 and 100                                       |
|                                                   |                 |                 |                                                                             |
|                                                   |                 |                 | If true, the y-axis range is set between 0 and 1. Default value is *false*. |
+---------------------------------------------------+-----------------+-----------------+-----------------------------------------------------------------------------+


**[]** 

Template

While setting template, the following parameters can be used.

[] 

Table 54: Template Parameter


  ---------- ------------- ---------------------------------
  Name       Type          Description
  X          double        x column coordinate
  Y          double        y column coordinate
  Width      double        column width
  Height     double        column height
  Interior   Brush         column color
  IsUpper    bool          true -- if this is upper column
  IsLower    bool          true -- if this is lower column
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------------


[] 

Stacking Negative Series

When negative values are added, Stacking Column chart can be made to be stacked separately in the chart area, above and below the y-axis 0.

 

Below given code is used to do this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [ChartStackingColumnType.SetRequiresNegativeSeriesStack([this].chartArea2, [true]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample which demonstrates Column Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Column Chart Demo***

 

 

See Also

[]{.UGHyperlink}

###### []{#p87}4.1.1.4.3.4 Stacking Column 100 Chart {#stacking-column-100-chart style="tab-stops: 0pt"}

In the 100 % Stacked Column Chart, the cumulative proportion of each stacked element always totals 100%. This type of chart is great to visualize the relative contribution of each series values to the whole.

[] 

The following image shows a sample Stacking Column 100 Chart.

[] 

{border="0"}

Figure 129: Stacking Column 100 Chart

[] 

Data Requirements

**[]** 

Table 55: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


**[]** 

**[]** 

Spline Settings

[] 

Table 56: Spline Setting


+-----------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------+
| Name                                          | Type            | Container       | Description                                                        |
+-----------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------+
| ChartStackingColumn100.ShowValueAsProbability | bool            | ChartArea       | y-axis range is set from 0 - 100                                   |
|                                               |                 |                 |                                                                    |
|                                               |                 |                 | If true, y-axis range is set from 0 - 1. Default value is *false*. |
+-----------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------+


**[]** 

Template

While setting template, the following parameters can be used.

[] 

Table 57: Template parameters


  ------------ ------------- ----------------------------------------------
  Name         Type          Description
  X            double        x column coordinate
  Y            double        y column coordinate
  Width        double        column width
  Height       double        column height
  Interior     Brush         column color
  IsUpper      bool          *true* -- if this is upper column
  IsLower      bool          *true* -- if this is lower column
  Percentage   double        indicates the percentage this point takes up
  Series       ChartSeries   reference to series-owner
  ------------ ------------- ----------------------------------------------


[] 

A sample which demonstrates Column Chart Types is available in the following sample installation path.

**** 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Column Chart Demo***

**** 

See Also

[]{#p88}[]{.UGHyperlink}

###### 4.1.1.4.3.5 Histogram Chart {#histogram-chart style="tab-stops: 0pt"}

Histogram is a bar (column) chart of a frequency distribution in which the widths of the bars are proportional to the classes into which the variable has been divided and the heights of the bars are proportional to the class frequencies. The categories are usually specified as non overlapping intervals of some variable. The categories (bars) must be adjacent. In addition, the chart has the capability to draw a normal distribution curve.

 

Histograms are useful data summaries that convey the following information:

[] 

[·      ]The general shape of the frequency distribution. (normal, exponential, etc.)

[·      ]Symmetry of the distribution and whether it is skewed.

[·      ]Modality - unimodal, bimodal or multimodal.

[] 

The shape of the distribution conveys important information such as the probability distribution of the data.

[] 

{border="0"}

Figure 130: Histogram Chart

[] 

Data Requirements

**[]** 

Table 58: Data Requirement


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

Histogram Settings

**[]** 

Table 59: Histogram Setting


  ------------------------------------------- -------- ------------- --------------------------------------------------------------------------
  Name                                        Type     Container     Description
  ChartHistogramType.IntervalOfHistogram      double   ChartArea     attached property that specifies the Interval which leads for one column
  ChartHistogramType.DrawNormalDistribution   bool     ChartSeries   specifies whether to draw Normal Distribution Line
  ------------------------------------------- -------- ------------- --------------------------------------------------------------------------


[] 

Template

While setting template the following parameters can be used:

[] 

Table 60: Template Parameter


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x column coordinate
  Y          double        y column coordinate
  Width      double        column width
  Height     double        column height
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

See Also

[]{.UGHyperlink}

[]{#p89} 

###### 4.1.1.4.3.6 Fast Column Chart {#fast-column-chart style="tab-stops: 0pt"}

Fast Column Chart is similar to Column chart as it uses vertical bars (called columns) to display different values of one or more items. Points from adjacent series are drawn as bars next to each other. 

 

It is used for comparing the frequency, count, total or average of data in different categories. It is ideal for showing the variations in the value of an item over time.

 

The following points mark the advantages of **Fast Column** over **Column** charts:

[] 

[·      ]The Fast Column charts are rendered using drawing visuals.

[·      ]They load faster than the Column charts.

[·      ]They ensure high performance for displaying data.

[·      ]They can be used as real time charts to render huge number of data points.

[] 

The Chart type Fast Column is added in the Enum of type ChartTypes.

[] 

{border="0"}

Figure 131: Fast Column Chart

[] 

Data Requirements

**[]** 

Table 61: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Custom Properties

**[]** 

Table 62: Custom Property


+-------------------+-----------------+-----------------+--------------------------------------+
| Name              | Type            | Container       | Description                          |
+-------------------+-----------------+-----------------+--------------------------------------+
| ChartType.Spacing | double          | ChartArea       | sets the interval between columns    |
|                   |                 |                 |                                      |
|                   |                 |                 | Possible values lie between 0 and 1. |
+-------------------+-----------------+-----------------+--------------------------------------+


[] 

Template

While setting template the following parameters can be used:

[] 

Table 63: Template Parameter


  ---------- ------------- ---------------------------
  Name       Type          Description
  X          double        x column coordinate
  Y          double        y column coordinate
  Width      double        column width
  Height     double        column height
  Interior   Brush         column color
  Series     ChartSeries   reference to series-owner
  ---------- ------------- ---------------------------


[] 

A sample which demonstrates Fast Column Chart Type is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\Essential Studio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Performance-\> Fast chart types***

**** 

The following code snippet illustrate the usage of Fast Column charts.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][ChartSeries][ Type][=\"FastColumn\"][ Name][=\"series1\"][ Stroke][=\"Black\"][ DataSource][=\"{][Binding][}\"/\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [ChartSeries][ series = ][new][ ][ChartSeries][();] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Type = ][ChartTypes][.FastColumn;]                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the sample.

[] 

A Fast Column chart is displayed pertaining to the data source it is bound to.

[] 

{border="0"}

Figure 132: Fast Column Chart

[] 

See Also

[]{.UGHyperlink}

 

[]{#related-topics}

