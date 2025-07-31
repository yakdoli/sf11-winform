---
title: piecharts.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\piecharts.md
created_at: 2025-07-03
---






##### Pie Charts {#pie-charts style="tab-stops: 0pt"}

###### []{#p113}4.1.1.4.8.1 Pie Chart {#pie-chart style="tab-stops: 0pt"}

A Pie Chart renders Y values as slices in a pie. These slices are rendered in proportion to the whole which is simply the sum of all the Y values in the series. Consequently, Pie Charts are used to visualize the proportional contribution (in terms of percentage or fraction) of categories of data to the whole data set. The X values in the data series will only be treated as nominal (categorical, qualitative) data. The Pie Chart can display only one DataSeries at a time.

[] 

{border="0"}

Figure 154: Pie Chart

[] 

Data Requirements

[] 

Table 112: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

Pie Type Properties

[] 

Table 113: Pie Type Properties


  ---------------------------- -------- ----------- --------------------------------------------
  Name                         Type     Container   Description
  ChartPieType.ExplodedIndex   double   ChartArea   index of segment which should be leant out
  ---------------------------- -------- ----------- --------------------------------------------


[] 

Template

While setting template, the following parameters can be used.

[] 

Table 114: Template Parameter


+-----------------------+-----------------------+-------------------------------------------------------------------+
| Name                  | Type                  | Description                                                       |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| TickX                 | double                | x-coordinate of sector center                                     |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| TickY                 | double                | y-coordinate of sector center                                     |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| IsExploded            | double                | *true -* if segment is leant out                                  |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| ExplodRadius          | double                | radius to which the segment should be leant out                   |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| Geometry              | Geometry              | segment geometry                                                  |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| Interior              | Brush                 | column color                                                      |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| Series                | ChartSeries           | reference to series-owner                                         |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| AngleOfSliceRotation  | double                | specifies the angle (in radians) at which the segment is rendered |
|                       |                       |                                                                   |
|                       |                       | It is useful for creating animated templates.                     |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| StartAngle            | double                | specifies the angle (in radians) of one side of the pie           |
+-----------------------+-----------------------+-------------------------------------------------------------------+
| EndAngle              | double                | specifies the angle (in radians) of the other side of the pie     |
+-----------------------+-----------------------+-------------------------------------------------------------------+


[] 

A sample which demonstrates Pie Chart Types is available in the following sample installation path.

**** 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Pie Chart Demo***

 

See Also

[]

 

[]{#p114} 

###### 4.1.1.4.8.2 Doughnut Chart {#doughnut-chart style="tab-stops: 0pt"}

Doughnut charts are pie charts with a hole, whose value is specified as the doughnut coefficient. The Doughnut Chart is best suited for presenting data in proportions.

 

{border="0"}

Figure 155: Doughnut Chart

[] 

Data Requirements

[] 

Table 115: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


**[]** 

Doughnut Type Properties

[] 

Table 116: Doughnut Type Properties


  --------------------------------------- -------- ------------- -------------------------------------------------------------
  Name                                    Type     Container     Description
  ChartDoughnutType.ExplodedIndex         int      ChartSeries   index of segment which should be leant out
  ChartDoughnutType.DoughnutCoefficient   double   ChartSeries   number which shows relation of inner radius to outer radius
  --------------------------------------- -------- ------------- -------------------------------------------------------------


[] 

Template

While setting template the following parameters can be used:

[] 

Table 117: Template Parameters


  --------------------- ------------- ------------------------------------------------------
  Name                  Type          Description
  TickX                 double        x-coordinate of sector center
  TickY                 double        y-coordinate of sector center
  IsExploded            double        *true -* if segment is leant out
  DoughnutCoefficient   double        number which shows relation of inner radius to outer
  ExplodRadius          double        radius to which the segment should be leant out
  Geometry              Geometry      segment geometry
  Interior              Brush         column color
  Series                ChartSeries   reference to series-owner
  --------------------- ------------- ------------------------------------------------------


[] 

A sample which demonstrates Pie Chart Types is available in the following sample installation path.

**** 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Pie Chart Demo***

 

See Also

[]

[]{#p115} 

 

[]{#related-topics}

