---
title: interlacedgridbackground.md
original_path: WinForms_Docs/04_Controls/Grid/interlacedgridbackground.md
created_at: 2025-08-05
---








  









### Interlaced Grid Background {#interlaced-grid-background style="tab-stops: 0pt"}

[] 

Chart supports interlaced grid which draws alternative grid background in x-axis and y-axis. The color is also customizable.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                     |
| [this][.ChartWebControl1.PrimaryXAxis.InterlacedGrid = ][true][;\                                                                               |
| ][this][.ChartWebControl1.PrimaryXAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(166, 184, 21);] |
|                                                                                                                                                                                                                                                                                                     |
| [this][.ChartWebControl1.PrimaryYAxis.InterlacedGrid = ][True][;\                                                                               |
| this.ChartWebControl1.PrimaryYAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(124, 144, 179));]                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.PrimaryXAxis.InterlacedGrid = ][True\                                                                                |
| Me][.ChartWebControl1.PrimaryXAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(166, 184, 21)]   |
|                                                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.PrimaryYAxis.InterlacedGrid = ][True\                                                                                |
| Me][.ChartWebControl1.PrimaryYAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(124, 144, 179))] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

A sample which illustrates the Interlaced Grid for the Chart is available in the below sample installation location.

\<sample installation location\>\\Syncfusion\\EssentialStudio\\***Version Number***\\Web\\chart.web\\Samples\\3.5\\Chart Appearance\\InterlacedGrid

[]{#p213} 

[]{#related-topics}

