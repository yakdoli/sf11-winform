---
title: usingbuilder28.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder28.md
created_at: 2025-08-05
---






#### Using Builder {#using-builder style="PAGE-BREAK-AFTER: auto; tab-stops: 0pt"}

1.   In the **view**, invoke the **Diagram** helper with the control ID and set the **HorizontalGridLineStyle** and **VerticalGridLineStyle** properties.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                 |
| [\<%][{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [      Html.Syncfusion().Diagram([\"GridLines\"])]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
| [          .ShowHorizontalGridLine([true])]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                 |
| [          .ShowVerticalGridLine([true])]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [          .HorizontalGridLineStyle([new] [GridLineStyle]() { GridLineColor =                   [\"#ccddff\"], GridLineThickness = 3.0 })]                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [          .VerticalGridLineStyle([new] [GridLineStyle]() { GridLineColor = [\"#cceeff\"], GridLineThickness = 3.0 })]                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [          .DiagramMode(][DiagramMode][.SVG)][] |
|                                                                                                                                                                                                                                                                                                                 |
| [          .Render();]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                 |
| [  }[%\>]][]                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.   Build and run the application.

{border="0"}

Figure 141: Custome Gridline Style

 

 

[]{#related-topics}

