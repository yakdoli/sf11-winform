---
title: drawingwinlosssparklineinawebapplication.md
original_path: WinForms_Docs/99_Uncategorized/drawingwinlosssparklineinawebapplication.md
created_at: 2025-08-05
---






##### Drawing Win-Loss Sparkline in a web application {#drawing-win-loss-sparkline-in-a-web-application style="tab-stops: 0pt"}

The Win-loss type of Sparkline is similar to column type but all columns have equal length for data points. The vertical column direction represents the negative or positive value.

Refer to the following code snippets to draw the Win-Loss sparkline:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [//Set Sparkline points to source property]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [this][.sparkLine1.Source =[new] [double]\[\] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };] |
|                                                                                                                                                                                                                               |
| [//Set line type sparkline]                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [this][.sparkLine1.Type = [SparkLineType].WinLoss;]                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [Me][.sparkLine1.Type = [SparkLineType]. WinLoss]                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

{border="0"}

Figure 89: WinLoss SparkLine

[]{#related-topics}

