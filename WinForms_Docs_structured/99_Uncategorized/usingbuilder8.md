---
title: usingbuilder8.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder8.md
created_at: 2025-08-05
---






#### Using Builder {#using-builder style="PAGE-BREAK-AFTER: auto; tab-stops: 0pt"}

 

1.   In the **view**, create an object for the **Node** class and set the **AllowResize** property.

2.   Invoke the **Diagram** helper with the control ID and set the **AllowResize** property.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [\<%][ [Node] node1 = [new] [Node]()]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [   {]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [       Name = [\"Node1\"],]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [       **AllowResize=[true]**]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [  };]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [%\>][]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [\<%][{]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [          .Nodes(nodes =\> nodes.Add(node1))]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [          .Width([Unit].Pixel(1100))]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [          .Height([Unit].Pixel(900))]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [          ][.DiagramMode(][DiagramMode][.SVG)][] |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [          .Render();]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [  }]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [%\>][]                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

3.    Build and run the application.

[]{#related-topics}

