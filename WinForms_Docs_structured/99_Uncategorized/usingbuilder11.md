---
title: usingbuilder11.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder11.md
created_at: 2025-07-03
---






#### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps guide in handling the customization of node labels through Builder.

1.   In the **view**, create an object for the **Node** class and set the **LabelFontColor, LabelBorderColor,** etc. properties.

2.   Invoke the **Diagram** helper with the control ID and set the **Nodes** property.[ ]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[]                                                                                                                  |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [\<%][ [Node] node = [new] [Node]()] |
|                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [                Name = Node1,]                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [                Label = Node1,]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [                LabelBackground = \"#fcb\",]                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| [                LabelBorderColor = \"#bcf\",]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                LabelBorderWidth = 1,]                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| [                LabelFontColor = \"#aad\",]                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [                LabelFontFamily = \"Arial\",]                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| [                LabelFontSize = 12,]                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [                LabelHeight = 30,]                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [                LabelWidth = 100,]                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [                LabelHorizontalAlignment = [Horizontal].Center,]                                                                                          |
|                                                                                                                                                                                                                                         |
| [                LabelVerticalAlignment = [Vertical].Middle,]                                                                                              |
|                                                                                                                                                                                                                                         |
| [                LabelFontColor = [\"red\"],]                                                                                                              |
|                                                                                                                                                                                                                                         |
| [                LabelFontSize = 16,]                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [                LabelFontFamily = [\"Times New Roman]]                                                                                                    |
|                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [%\>][]                                                                                                   |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [\<%][{]                                                                                                  |
|                                                                                                                                                                                                                                         |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])]                                                                                                       |
|                                                                                                                                                                                                                                         |
|               .Nodes(nodes => nodes.Add(node))                                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| [          .Width(900)]                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [          .Height(500)]                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [          .DiagramMode(DiagramMode.SVG)          ]                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [          .Render();]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [  }]                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [%\>][]                                                                                                   |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

3.   Build and run the application.

 

[]{#related-topics}

