---
title: usingbuilder20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder20.md
created_at: 2025-07-03
---






#### Using Builder {#using-builder style="tab-stops: 0pt"}

1.   In the **view**, invoke the **Diagram** helper with the control ID and set the **HorizontalSpacing**, **Vertical Spacing**, and **SpaceBetweenSubTrees** properties.

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[View ]**                                                                       |
|                                                                                                                                        |
| [\<%][{] |
|                                                                                                                                        |
| [      Html.Syncfusion().Diagram([\"FlatDiagram\"])]      |
|                                                                                                                                        |
| [             .HorizontalSpacing(50)]                                             |
|                                                                                                                                        |
| [             .VerticalSpacing(50)]                                               |
|                                                                                                                                        |
| [             .SpaceBetweenSubTrees(50)]                                          |
|                                                                                                                                        |
| [             .DiagramMode(DiagramMode.SVG)]                                      |
|                                                                                                                                        |
| [             .Render();]                                                         |
|                                                                                                                                        |
| [  }]                                                                             |
|                                                                                                                                        |
| [%\>][]  |
+----------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode,  change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.    Build and run the application.

[]{#related-topics}

