---
title: invertedaxis.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\invertedaxis.md
created_at: 2025-07-03
---








  









### Inverted Axis {#inverted-axis style="tab-stops: 0pt"}

[] 

Essential Chart provides support for inverting the values in an axis. Data on an inverted axis is plotted in the opposite direction - top to bottom for y-axis and right to left for x-axis. To enable this behavior, set the **ChartAxis.Inversed** to**[ ]true**.

[] 


  ----------------------- ------------------------------------------------
  Chart Axis Properties   Description
  Inversed                Indicates whether the axis should be reversed.
  ----------------------- ------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| **[]**                                                                                                            |
|                                                                                                                                                                     |
| [   ][// This inverts the specified chart axis.]                                            |
|                                                                                                                                                                     |
| [this][.ChartWebControl1.PrimaryXAxis.Inversed = [true];] |
|                                                                                                                                                                     |
| [this][.ChartWebControl1.PrimaryYAxis.Inversed = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [   ][\' This inverts the specified chart axis.]                                         |
|                                                                                                                                                                  |
| [Me][.ChartWebControl1.PrimaryXAxis.Inversed = [True]] |
|                                                                                                                                                                  |
| [Me][.ChartWebControl1.PrimaryYAxis.Inversed = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows a chart whose x and y axes have been reversed.

[] 

{border="0"}

**[]** 

Figure 242: Chart with Both Axes Reversed

 

[]{#related-topics}

