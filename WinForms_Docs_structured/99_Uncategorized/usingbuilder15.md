---
title: usingbuilder15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder15.md
created_at: 2025-07-03
---






#### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps guide in handling the customization of connector labels through Builder.

1.   In the **view**, create an object for the **Connector** class and set the **LabelFontColor**, **LabelBorderColor**, etc., properties.

2.   Invoke the **Diagram** helper with the control ID and set the **Nodes** property.[ ]

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**[]                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [\<%][ Line[Connector] line = [new] Line[Connector] ()] |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                Name = \"line1\",]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                Label = \"Line's Label\",]                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [                HeadNode = node1,]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                TailNode = node2,]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                LabelBackground = \"#fcb\",]                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [                LabelBorderColor = \"#bcf\",]                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                LabelBorderWidth = 1,]                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [                LabelFontColor = \"#aad\",]                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [                LabelFontFamily = \"Arial\",]                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                LabelFontSize = 12,]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [                LabelHeight = 30,]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                LabelWidth = 100               ]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [%\>][]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [\<%][{]                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])]                                                                                                                          |
|                                                                                                                                                                                                                                                            |
|               .Connectors(conn => conn.Add(line))                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [          .Width(900)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [          .Height(500)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [          .DiagramMode(DiagramMode.SVG)          ]                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [          .Render();]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [  }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [%\>][]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

3.   Build and run the application.

[]{#related-topics}

