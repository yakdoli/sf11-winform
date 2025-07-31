---
title: enabledrawingtoolsproperty.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\enabledrawingtoolsproperty.md
created_at: 2025-07-03
---






#### Enable DrawingTools Property {#enable-drawingtools-property style="tab-stops: 0pt"}

To enable DrawingTools set the *EnableDrawingTools* property to *true*. Shapes and line connectors are enabled, when the *EnableDrawingTools* property is enabled. By default, the value is set to false.

 

DrawingTools can be enabled using two methods:

[·      ]Through XAML.

 

The following code illustrates how to enable the DrawingTools:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][DiagramControl][ Name][=\"diagramControl\"][ ][]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][\<][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [         ][\<][syncfusion][:][DiagramModel][ x][:][Name][=\"diagramModel\"\>]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [         ][\</][syncfusion][:][DiagramModel][\>][  ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][\</][syncfusion][:][DiagramControl.Model][\>][ ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\<][syncfusion][:][DiagramControl.View][\>]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [       ][\<][syncfusion][:][DiagramView][ Name][=\"diagramView\" ][EnableDrawingTools][=\"True\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\</][syncfusion][:][DiagramView][\>]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][\</][syncfusion][:][DiagramControl.View][\>]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion][:][DiagramControl][\>][]                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[·      ]Through Code behind\[C#\]


**** 


The following code illustrates how to enable the DrawingTools:

[] 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| [        DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [       diagramView.][ EnableDrawingTools = [true];]                                                 |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



 

{border="0"}Note: When the EnableDrawingTools is set to True, it has to be disabled manually, i.e. it cannot be disabled automatically. This will facilitate drawing shapes or lines continually until EnableDrawingTools is set to false manually.


[]{#related-topics}

