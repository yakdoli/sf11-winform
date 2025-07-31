---
title: accumulationcharts5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\accumulationcharts5.md
created_at: 2025-07-03
---






##### Accumulation Charts {#accumulation-charts style="tab-stops: 0pt"}

###### []{#p97}4.1.1.4.5.1 Funnel Chart {#funnel-chart style="tab-stops: 0pt"}

[] 

The Funnel chart is a single series chart representing the data as portions of 100%, and this chart does not use any axes. Funnel chart can be viewed as 2D or 3D.

 

Funnel charts are often used to represent stages in a sales process and show the amount of potential revenue for each stage. This type of chart can be useful also in identifying potential problem areas in an organization\'s sales processes, for example. A funnel chart is similar to a stacked percent bar chart.

 

{border="0"}

Figure 138: Funnel Chart

[] 

Data Requirements

[] 

Table 76: Data Requirement


+------------------------------+-------------+
| Details                                    |
+------------------------------+-------------+
| Number of y values per point | one         |
+------------------------------+-------------+
| Number of points             | one or more |
+------------------------------+-------------+
| Number of series             | one or more |
+------------------------------+-------------+


[] 

FunnelType Properties

[] 

Table 77: FunnelType Property


  ------------------------------- ----------------- ------------- ------------------------------------------------------
  Name                            Type              Container     Description
  ChartFunnelType.ExplodedIndex   int               ChartSeries   index of segment which should be leant out
  ChartFunnelType.GapRatio        double            ChartSeries   indicates relation of  inner interval to their width
  ChartFunnelType.FunnelMode      ChartFunnelMode   ChartSeries   method of data displaying
  ------------------------------- ----------------- ------------- ------------------------------------------------------


[] 

 

Template

While setting template the following parameters can be used:

[] 


  ---------------- ------------- -------------------------------------------------------
  Name             Type          Description
  GapRatio         double        indicates relation of  inner  interval to their width
  IsExploded       bool          *true* - if segment is leant out
  ExplodedOffset   double        displacement on which segment should be leant out
  MinWidth         double        minimal segment width
  Geometry         Geometry      segment geometry
  Interior         Brush         column color
  Series           ChartSeries   reference to series-owner
  ---------------- ------------- -------------------------------------------------------


[] 

A sample which demonstrates Accumulation Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Accumulation Chart Demo***

 

See Also

[]{.UGHyperlink}

[]{#p98} 

###### 4.1.1.4.5.2 Pyramid Chart {#pyramid-chart style="tab-stops: 0pt"}

Pyramid chart is similar to the funnel chart. It is often used for geographical purposes. The Pyramid Chart type displays the data which when totalled will be 100%. This type of chart is a single series chart representing the data as portions of 100%, and this chart does not use any axes. Pyramid chart can be viewed as 2D or 3D.

[] 

The following images are some sample Pyramid Charts.

[] 

{border="0"}

Figure 139: Pyramid Chart

[] 

Data Requirements

[] 

Table 78: Data Requirement


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

PyramidType Properties

[] 

Table 79: Property Table


  -------------------------------- ------------------ ------------- ------------------------------------------------------
  Name                             Type               Container     Description
  ChartPyramidType.ExplodedIndex   int                ChartSeries   index of segment which should be leant out
  ChartPyramidType.GapRatio        double             ChartSeries   indicates relation of inner  interval to their width
  ChartPyramidType.PyramidMode     ChartPyramidMode   ChartSeries   method of data displaying
  -------------------------------- ------------------ ------------- ------------------------------------------------------


[] 

Template

**[]** 

While setting template the following parameters can be used.

[] 

Table 80: Template Parameters


  ---------------- ------------- ------------------------------------------------------
  Name             Type          Description
  GapRatio         double        indicates relation of inner interval to their  width
  IsExploded       bool          *true* - if segment is leant out
  ExplodedOffset   double        displacement on which segment should be leant out
  Geometry         Geometry      segment geometry
  Interior         Brush         column color
  Series           ChartSeries   reference to series-owner
  ---------------- ------------- ------------------------------------------------------


[] 

A sample which demonstrates Accumulation Chart Types is available in the following sample installation path.

 

***..My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Chart.WPF\\Samples\\3.5\\WindowsSamples\\Chart Gallery\\Accumulation Chart Demo***

 

See Also

[]{.UGHyperlink}

[] 

 

 

[]{#related-topics}

