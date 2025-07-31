---
title: todrawlinechartsinasparklinechart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\todrawlinechartsinasparklinechart.md
created_at: 2025-07-03
---






##### To draw line charts in a Sparkline Chart {#to-draw-line-charts-in-a-sparkline-chart style="tab-stops: 0pt"}

The line type of spark line represents a set of data points, connected by a line.

Refer to the following code snippets to draw the line Sparkline chart:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [//Set Sparkline points to source property]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [this][.sparkLine1.Source =[new] [double]\[\] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };] |
|                                                                                                                                                                                                                               |
| [//Set line type sparkline]                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [this][.sparkLine1.Type = [SparkLineType].Line;]                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [\'Set Sparkline points to source property]                                                                                                                          |
|                                                                                                                                                                                                                        |
| [Me][.sparkLine1.Source = [New] [Double]() {30, -20, 80, 20, 40, -50,-30, 70, -40, 50}] |
|                                                                                                                                                                                                                        |
| [\'Set line type sparkline]                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [Me][.sparkLine1.Type = [SparkLineType].Line]                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

{border="0"}

Figure 87: Line SparkLine

[]{#related-topics}

