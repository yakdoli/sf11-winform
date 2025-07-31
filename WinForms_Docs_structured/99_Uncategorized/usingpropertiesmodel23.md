---
title: usingpropertiesmodel23.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel23.md
created_at: 2025-07-03
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps show you how to handle the addition of a symbol palette group through the properties model.

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class. Assign this model class to **view data**. 

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller ]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [DiagramPropertiesModel][ diagramModel = [new] [DiagramPropertiesModel]()][;]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [diagramModel.IsPageEditable = [true];]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [diagramModel.BoundaryConstraintsEnabled=[false];            ]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[diagramModel.IsSymbolPaletteEnabled = [true];]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [diagramModel.SymbolPaletteWidth = 151;]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [diagramModel][.DiagramMode = ][DiagramMode][.Canvas;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **view**, invoke the **Diagram** helper with the **view data key** as the control ID.

 

+-----------------------------------------------------------------------------+
| **[View]**             |
|                                                                             |
| **[]**                 |
|                                                                             |
| ```                         |
| <%{                                                                         |
| ```                                                                         |
|                                                                             |
| ```                         |
|       Html.Syncfusion().Diagram("FlatDiagram")                              |
| ```                                                                         |
|                                                                             |
| [          .Render();] |
|                                                                             |
| ```                         |
|   }                                                                         |
| ```                                                                         |
|                                                                             |
| ```                         |
| %>                                                                          |
| ```                                                                         |
+-----------------------------------------------------------------------------+

 

3.   Build and run the application.

                           

[]{#related-topics}

