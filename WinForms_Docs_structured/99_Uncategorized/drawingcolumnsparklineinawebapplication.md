---
title: drawingcolumnsparklineinawebapplication.md
original_path: WinForms_Docs/99_Uncategorized/drawingcolumnsparklineinawebapplication.md
created_at: 2025-08-05
---






##### Drawing Column Sparkline in a web application {#drawing-column-sparkline-in-a-web-application style="tab-stops: 0pt"}

The column type of spark line represents each data point by a column. The vertical column direction represents the negative or positive value.

Refer to the following code snippets to draw the column Sparkline:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [//Set Sparkline points to source property]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [this][.sparkLine1.Source =[new] [double]\[\] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };] |
|                                                                                                                                                                                                                               |
| [//Set line type sparkline]                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [this][.sparkLine1.Type = [SparkLineType].Column;]                                                               |
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
| [Me][.sparkLine1.Type = [SparkLineType]. Column]                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

{border="0"}

Figure 88: Column SparkLine

 

[]{#related-topics}

