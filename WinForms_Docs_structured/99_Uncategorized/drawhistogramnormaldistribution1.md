---
title: drawhistogramnormaldistribution1.md
original_path: WinForms_Docs/99_Uncategorized/drawhistogramnormaldistribution1.md
created_at: 2025-08-05
---






#### DrawHistogramNormalDistribution {#drawhistogramnormaldistribution style="tab-stops: 0pt"}

 

The normal distribution curve is drawn by setting this property of the ChartSeries class to **true**.

 


+------------------------------+-----------------+
| Details                                        |
+------------------------------+-----------------+
| **Possible Values**          | True or False   |
+------------------------------+-----------------+
| **Default Value    **        | **False**       |
+------------------------------+-----------------+
| **2D / 3D Limitations**      | No              |
+------------------------------+-----------------+
| **Applies to Chart Element** | All series      |
+------------------------------+-----------------+
| **Applies to Chart Types**   | Histogram Chart |
+------------------------------+-----------------+


 

Here is some sample code.

 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                              |
| **[]**                                                                     |
|                                                                                                                              |
| [// This draws the normal distribution curve for the histogram chart.]     |
|                                                                                                                              |
| [series2.DrawHistogramNormalDistribution = [true];]                 |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| [// Set the desired number of intervals required for the histogram chart.] |
|                                                                                                                              |
| [series2.NumberOfHistogramIntervals = 10;]                                               |
+------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| **[]**                                                                                              |
|                                                                                                                                                       |
| [\' This draws the normal distribution curve for the histogram chart.]                              |
|                                                                                                                                                       |
| [series2.DrawHistogramNormalDistribution = ][True] |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [\' Set the desired number of intervals required for the histogram chart.]                          |
|                                                                                                                                                       |
| [series2.NumberOfHistogramIntervals = 10]                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 119: Histogram Chart with Normal Distribution Curve

[] 

See Also

[] 

[Histogram Chart]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p92} 

[]{#related-topics}

