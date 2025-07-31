---
title: invertedaxis2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\invertedaxis2.md
created_at: 2025-07-03
---








  









### Inverted Axis {#inverted-axis style="tab-stops: 0pt"}

 

Essential Chart provides support for inverting the values in an axis. Data on an inverted axis is plotted in the opposite direction - top to bottom for y-axis and right to left for x-axis. To enable this behavior, set the **ChartAxis.Inversed** to**[ ]true**.

 


  --------------------- ------------------------------------------------
  Chart Axis Property   Description
  Inversed              Indicates whether the axis should be reversed.
  --------------------- ------------------------------------------------


 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [   ][// This inverts the specified chart axis.]                        |
|                                                                                                                                                                  |
| [this][.chartControl1.PrimaryXAxis.Inversed = [true];] |
|                                                                                                                                                                  |
| [this][.chartControl1.PrimaryYAxis.Inversed = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [   ][\' This inverts the specified chart axis.]                     |
|                                                                                                                                                               |
| [Me][.chartControl1.PrimaryXAxis.Inversed = [True]] |
|                                                                                                                                                               |
| [Me][.chartControl1.PrimaryYAxis.Inversed = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following image shows a chart whose x and y axes have been reversed.

 

{border="0"}

 

 Figure 248: Chart with both Axes Reversed

[]{#p175} 

[]{#related-topics}

