---
title: selectadrawingtool.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectadrawingtool.md
created_at: 2025-07-03
---






#### Select a DrawingTool {#select-a-drawingtool style="tab-stops: 0pt"}

DrawingTools consist of different shapes and line connectors. You can choose one of the DrawingTools at a time. By default, it is set to Ellipse.

 

The DrawingTool selection in Diagram View can be set in two methods:

[·      ]Through XAML.

       

The following code illustrates how to select a DrawingTool:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][DiagramControl][ Name][=\"diagramControl\"\>]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [       ][\<][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][syncfusion][:][DiagramModel][ x][:][Name][=\"diagramModel\"\>]                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\</][syncfusion][:][DiagramModel][\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\</][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [       ][\<][syncfusion][:][DiagramControl.View][\>]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][syncfusion][:][DiagramView][ Name][=\"diagramView\" ][DrawingTool][=\"Polygon\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][syncfusion][:][DiagramView.Page][\>]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\</][syncfusion][:][DiagramView][\>]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\</][syncfusion][:][DiagramControl.View][\>]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\</][syncfusion][:][DiagramControl][\>]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[·      ]Through Code behind\[C#\]

 

The following code illustrates how to select a DrawingTool:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| [        DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                   |
| ```                                                                                                                                                                    |
|        diagramView.DrawingTool = DrawingTools.Rectangle;                                                                                                                                          |
| ```                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

[]{#related-topics}

