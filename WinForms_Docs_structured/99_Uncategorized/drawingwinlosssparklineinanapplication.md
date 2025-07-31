---
title: drawingwinlosssparklineinanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drawingwinlosssparklineinanapplication.md
created_at: 2025-07-03
---






##### Drawing WinLoss Sparkline in an Application {#drawing-winloss-sparkline-in-an-application style="tab-stops: 0pt"}

The Winloss type of spark line is similar to column type but all columns have equal length for data points.   The vertical column direction represents the negative or positive value.

 

Refer to the following code snippets to draw  the  WinLoss sparkline:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [//Set Sparkline points to source property]**[]**                                                                                              |
|                                                                                                                                                                                                                                      |
| [this][.sparkLine1.ItemSource =[new] [double]\[\] { 30, -20, 80, 20, 40, -50, -30, 70,    -40, 50 };] |
|                                                                                                                                                                                                                                      |
| [//Set line type sparkline]**[]**                                                                                                              |
|                                                                                                                                                                                                                                      |
| [this][.sparkLine1.SparkLineType = [SparkLine].[SparkLineType].WinLoss;]                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [\'Set Sparkline points to source property]                                                                                                                                       |
|                                                                                                                                                                                                                                     |
| [Me][.sparkLine1.ItemSource = [New] [Double]() {30, -20, 80, 20, 40, -50,-30, 70, -40, 50}]          |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [\'Set line type sparkline]                                                                                                                                                       |
|                                                                                                                                                                                                                                     |
| [Me][.sparkLine1.SparkLineType = [SparkLine].[SparkLineType]. WinLoss[]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

{border="0"}

Figure 281: WinLoss SparkLine

**** 

[]{#related-topics}

