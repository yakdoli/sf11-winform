---
title: usingbuilder1.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder1.md
created_at: 2025-08-05
---






#### Using Builder {#using-builder style="PAGE-BREAK-AFTER: auto; tab-stops: 0pt"}

1.   In the **view**, invoke the **Diagram** helper with control ID and set the **GridLineHorizontalOffset** and **GridLineVerticalOffset** properties.


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| [        [\<%]{]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [              Html.Syncfusion().Diagram([\"GridLines\"])]                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [                  .ShowHorizontalGridLine([true])]                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [                  .ShowVerticalGridLine([true])]                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [                  .GridLineHorizontalOffset(50)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                     |
| [                  .GridLineVerticalOffset(50)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [                  .DiagramMode(][DiagramMode][.SVG)][] |
|                                                                                                                                                                                                                                                     |
| [                  .Render();]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [          }[%\>]][]                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.   Build and run the application.

{border="0"}

Figure 139: Customized Gridline Offset

 

[]{#related-topics}

