---
title: howtodisplaythechartareaalone.md
original_path: WinForms_Docs/04_Controls/Chart/howtodisplaythechartareaalone.md
created_at: 2025-08-05
---








  









## How to display the Chart Area alone? {#how-to-display-the-chart-area-alone style="tab-stops: 0pt"}

[] 

This can be achieved by setting the **Legend.Visible** property of ChartControl to **False**, **ElementsSpacing** property of ChartControl to **Zero***,* and **Text** property of ChartControl to an Empty String.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [this][.ChartWebControl1.Text = [\"\"];]         |
|                                                                                                                                                               |
| [this][.ChartWebControl1.Legend.Visible = [false];] |
|                                                                                                                                                               |
| [this][.ChartWebControl1.ElementsSpacing = 0;]                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| **[]**                                                                                                   |
|                                                                                                                                                            |
| [Me][.ChartWebControl1.Text = [\"\"]]         |
|                                                                                                                                                            |
| [Me][.ChartWebControl1.Legend.Visible = [False]] |
|                                                                                                                                                            |
| [Me][.ChartWebControl1.ElementsSpacing = 0]                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p280} 

[]{#related-topics}

