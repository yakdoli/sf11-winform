---
title: howtocreateflowchartcontrolsdecisionboxandcircleprogrammatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtocreateflowchartcontrolsdecisionboxandcircleprogrammatically.md
created_at: 2025-07-03
---








  









## How to create Flow Chart controls, Decision Box and Circle, programmatically?[] {#how-to-create-flow-chart-controls-decision-box-and-circle-programmatically style="tab-stops: 0pt"}

[] 

You can create a **Decision Box** by rotating a rectangle to 45 degrees, and a **Circle** by specifying the same height and width for an ellipse. This is demonstrated in the below given code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [//Decision Box]                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [Syncfusion.Windows.Forms.Diagram.[Rectangle] decision = [new] Syncfusion.Windows.Forms.Diagram.[Rectangle](100, 200, 60, 60);] |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [//Rotate to make a decision box]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [decision.RotationAngle = 45;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [decision.Visible = [true];]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [//Specify the same height and width to get a circle.]                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [Syncfusion.Windows.Forms.Diagram.[Ellipse] ellipse = [new] [Ellipse](40, 50, 60, 60);]                                         |
|                                                                                                                                                                                                                                    |
| [ellipse.FillStyle.Color = [Color].Black; ]                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [\'Decision Box]                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| [Dim][ decision [As] [New] Syncfusion.Windows.Forms.Diagram.Rectangle(100, 200, 60, 60)] |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [\'Rotate to make a decision box]                                                                                                                                     |
|                                                                                                                                                                                                                         |
| [decision.RotationAngle = 45]                                                                                                                                                       |
|                                                                                                                                                                                                                         |
| [decision.Visible = [True]]                                                                                                                                    |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [\'Specify the same height and width to get a circle.]                                                                                                                |
|                                                                                                                                                                                                                         |
| [Dim][ ellipse = [New] Ellipse(40, 50, 60, 60)]                                                               |
|                                                                                                                                                                                                                         |
| [ellipse.FillStyle.Color = Color.Black]                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

