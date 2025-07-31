---
title: drawingcolumnsparkli.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drawingcolumnsparkli.md
created_at: 2025-07-03
---






##### Drawing Column Sparkline in  an Application {#drawing-column-sparkline-in-an-application style="tab-stops: 0pt"}

 

The column type of spark line represents each data point by a column. The vertical column direction represents the negative or positive value.

[] 

Refer to the following code snippets to draw the column sparkline:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [//Set Sparkline points to source property]**[]**                                                                                              |
|                                                                                                                                                                                                                                      |
| [this][.sparkLine1.ItemSource =[new] [double]\[\] { 30, -20, 80, 20, 40, -50, -30, 70,    -40, 50 };] |
|                                                                                                                                                                                                                                      |
| [//Set line type sparkline]**[]**                                                                                                              |
|                                                                                                                                                                                                                                      |
| [this][.sparkLine1.SparkLineType = [SparkLine].[SparkLineType].Column;]                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [\'Set Sparkline points to source property]                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [Me][.sparkLine1.ItemSource = [New] [Double]() {30, -20, 80, 20, 40, -50,-30, 70, -40, 50}]         |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [\'Set line type sparkline]                                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [Me][.sparkLine1.SparkLineType = [SparkLine].[SparkLineType]. Column[]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 280: Column SparkLine

 

[]{#related-topics}

