---
title: howtogetthenearestgridpointonadiagram.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtogetthenearestgridpointonadiagram.md
created_at: 2025-07-03
---








  









## How to Get the Nearest Grid Point on a Diagram {#how-to-get-the-nearest-grid-point-on-a-diagram style="tab-stops: 0pt"}

The **GetNearestGridPoint method** can be used to get the nearest grid point on a diagram based on a given point.

This method has the following two parameters:

[·      ]**Point** - specifies the location which calculates the nearest grid point.

[·      ]**Int** - specifies the ruler height.

 

The following code snippet illustrates the implementation of **GetNearestGridPoint** method:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                                       |
| **[]**                                                                                                              |
|                                                                                                                                                                                       |
| [//Current mouse position]                                                                                          |
|                                                                                                                                                                                       |
| [Point][ ptMouse = [new] [Point](e.X, e.Y);]     |
|                                                                                                                                                                                       |
| [int][ rulerHeight = (diagram1.ShowRulers) ? diagram1.RulersHeight : 0;]                         |
|                                                                                                                                                                                       |
| [//Nearest grid point][]                                                                        |
|                                                                                                                                                                                       |
| [PointF][ ptGridNearestPoint = diagram1.View.Grid.GetNearestGridPoint(ptMouse, rulerHeight);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [Current mouse position][ ]                                                                                            |
|                                                                                                                                                                                                                                           |
| [Dim][ ptMouse [As] [Point] = [New] [Point] (e.X, e.Y)]    |
|                                                                                                                                                                                                                                           |
| [Dim][ rulerHeight [As] [Integer]]                                                                         |
|                                                                                                                                                                                                                                           |
| [rulerHeight = [If]((diagram1.ShowRulers), diagram1.RulersHeight, 0)]                                                                                                            |
|                                                                                                                                                                                                                                           |
| [\'Nearest grid point][]                                                                                                                            |
|                                                                                                                                                                                                                                           |
| [Dim][ ptGridNearestPoint [As] [PointF] = diagram1.View.Grid.GetNearestGridPoint(ptMouse, rulerHeight)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

