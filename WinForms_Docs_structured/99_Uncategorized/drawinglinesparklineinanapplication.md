---
title: drawinglinesparklineinanapplication.md
original_path: WinForms_Docs/99_Uncategorized/drawinglinesparklineinanapplication.md
created_at: 2025-08-05
---






##### Drawing Line Sparkline in an Application {#drawing-line-sparkline-in-an-application style="tab-stops: 0pt"}

The line type of spark line represents a set of data points, connected by a line.

 

Refer to the following code snippets to draw  the line sparkline.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                      |
| [//Set Sparkline points to source property]**[]**                                                                                              |
|                                                                                                                                                                                                                                      |
| [this][.sparkLine1.ItemSource =[new] [double]\[\] { 30, -20, 80, 20, 40, -50, -30, 70,    -40, 50 };] |
|                                                                                                                                                                                                                                      |
| [//Set line type sparkline]**[]**                                                                                                              |
|                                                                                                                                                                                                                                      |
| [this][.sparkLine1.SparkLineType = [SparkLine].[SparkLineType].Line;]                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [\'Set Sparkline points to source property]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [Me][.sparkLine1.ItemSource = [New] [Double]() {30, -20, 80, 20, 40, -50,-30, 70, -40, 50}]      |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [\'Set line type sparkline]                                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [Me][.sparkLine1.SparkLineType = [SparkLine].[SparkLineType].Line[]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 279: Line SparkLine[]

[] 

[] 

[]{#related-topics}

