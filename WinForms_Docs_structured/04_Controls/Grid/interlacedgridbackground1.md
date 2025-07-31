---
title: interlacedgridbackground1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\interlacedgridbackground1.md
created_at: 2025-07-03
---








  









### Interlaced Grid Background {#interlaced-grid-background style="tab-stops: 0pt"}

 

Chart supports interlaced grid which draws alternative grid background in x-axis and y-axis. The color is also customizable.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [this][.chartControl1.PrimaryXAxis.InterlacedGrid = ][true][;\                                                                                |
| ][this][.chartControl1.PrimaryXAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(166, 184, 200);] |
|                                                                                                                                                                                                                                                                                                   |
| [this][.chartControl1.PrimaryYAxis.InterlacedGrid = ][True][;\                                                                                |
| this.chartControl1.PrimaryYAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(124, 144, 179));]                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [Me][.chartControl1.PrimaryXAxis.InterlacedGrid = ][True\                                                                                |
| Me][.chartControl1.PrimaryXAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(166, 184, 200)]  |
|                                                                                                                                                                                                                                             |
| [Me][.chartControl1.PrimaryYAxis.InterlacedGrid = ][True\                                                                                |
| Me][.chartControl1.PrimaryYAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(124, 144, 179))] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 327: Interlaced Grid

 

The preceding image illustrates interlaced grid background for the chart.

 

A sample which illustrates the Interlaced Grid for the Chart is available in the below sample installation location.

 

[\<Sample location\>\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Chart.Windows\\Samples\\2.0\\Chart Appearance\\Interlaced Grid]{.UGHyperlink}

[]{#p213} 

 

[]{#related-topics}

