---
title: enabledrawingtools1.md
original_path: WinForms_Docs/99_Uncategorized/enabledrawingtools1.md
created_at: 2025-08-05
---






#### Enable Drawing Tools {#enable-drawing-tools style="tab-stops: 0pt"}

To enable DrawingTools set **EnableDrawingTools** property to **true**. Shapes and line connectors are enabled, when the **EnableDrawingTools** property is enabled. By default, the value is set to false.

 

DrawingTools can be enabled using two methods.

[·      ]Through XAML.

***[ ]***[The following code illustrates how to enable the DrawingTools][.]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][DiagramControl][ Name][=\"diagramControl\"][ ][]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][\<][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [         ][\<][syncfusion][:][DiagramModel][ x][:][Name][=\"diagramModel\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [         ][\</][syncfusion][:][DiagramModel][\>][  ]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][\</][syncfusion][:][DiagramControl.Model][\>][ ]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\<][syncfusion][:][DiagramControl.View][\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [       ][\<][syncfusion][:][DiagramView][ Name][=\"diagramView\" ][EnableDrawingTools[=\"True\"\>]]                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\</][syncfusion][:][DiagramView][\>]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][\</][syncfusion][:][DiagramControl.View][\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion][:][DiagramControl][\>][]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ][Through Code behind\[C#\]]

[] 

[The following code illustrates how to enable the DrawingTools][.]

***[]*** 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [       DiagramView][ diagramView = [new] [DiagramView]();][] |
|                                                                                                                                                                                                                                        |
| [       diagramView.][EnableDrawingTools = [true];]                                                                                       |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


***[]*** 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                  |
| [      ]                                                                                                                     |
|                                                                                                                                                                                  |
| [       [Dim] diagramView [As] [New] [DiagramView]()] |
|                                                                                                                                                                                  |
| [      diagramView.EnableDrawingTools = [True]]                                                                         |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


***[]*** 

***[Note:]***

***[When the ]**[EnableDrawingToolsis set to True, it has to be disabled manually, i.e. it cannot be disabled automatically.]**[ This will facilitate drawing shapes or lines continually until EnableDrawingTools is set to false manually.]***

[]{#related-topics}

