---
title: usingbuilder10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder10.md
created_at: 2025-07-03
---






#### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to handle node deletion through Builder.

1.   In the **view**, create an object for the **Node** class and set the **LabelVisibility** and **Label** properties.

2.   Invoke the **Diagram** helper with the control ID and set the **Nodes** property[.][ ]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [\<%][ ][Node][ node = [new] [Node]()] |
|                                                                                                                                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                             |
| [        Name = [\"EssentialDiagram\"],        ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                             |
| [        Shape = [Shapes].RoundedRectangle,]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                             |
| [        LabelVisibility = [true,]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                             |
| [        Label = [\"Essential Diagram\"]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [    };]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                             |
| [%\>][]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [\<%][{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                             |
|        .Nodes(nodes => nodes.Add(node))                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                             |
| [          .Width(900)]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [          .Height(500)]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                             |
| [          .DiagramMode(DiagramMode.SVG)          ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [          .Render();]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                             |
| [  }]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                             |
| [%\>][]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode. Change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

[] 

3.   Build and run the application.

 

[]{#related-topics}

