---
title: howtodisplaythechartareaalone1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtodisplaythechartareaalone1.md
created_at: 2025-07-03
---








  









## How to display the Chart Area alone {#how-to-display-the-chart-area-alone style="tab-stops: 0pt"}

 

This can be achieved by setting the **Legend.Visible** property of ChartControl to **False**, **ElementsSpacing** property of ChartControl to **Zero***,* and **Text** property of ChartControl to an Empty String.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| **[]**                                                                                                   |
|                                                                                                                                                            |
| [this][.chartControl1.Text = [\"\"];]         |
|                                                                                                                                                            |
| [this][.chartControl1.Legend.Visible = [false];] |
|                                                                                                                                                            |
| [this][.chartControl1.ElementsSpacing = 0;]                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [Me][.chartControl1.Text = [\"\"]]         |
|                                                                                                                                                         |
| [Me][.chartControl1.Legend.Visible = [False]] |
|                                                                                                                                                         |
| [Me][.chartControl1.ElementsSpacing = 0]                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p288} 

[]{#related-topics}

