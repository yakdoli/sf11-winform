---
title: usingpropertiesmodel1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel1.md
created_at: 2025-07-03
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set **ShowHorizontalGridLine** and **ShowVerticalGridLine** properties. Pass this model class to **view data**.


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                       |
| [DiagramPropertiesModel][ model = [new] [DiagramPropertiesModel]()]                                                                            |
|                                                                                                                                                                                                                                                                                                                       |
| [            {]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [                ShowHorizontalGridLine = [true],]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                       |
| [                ShowVerticalGridLine = [true],]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                       |
| [                GridLineHorizontalOffset = 50,]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                       |
| [                GridLineVerticalOffset = 50,]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                       |
| [                DiagramMode = ][DiagramMode][.SVG][] |
|                                                                                                                                                                                                                                                                                                                       |
| [            };]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                       |
| [            ViewData\[[\"GridLines\"]\] = model;][]                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

**[]** 

2.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][]**                                                                  |
|                                                                                                                                                                        |
| [  [\<%]{]                                                                            |
|                                                                                                                                                                        |
| [              Html.Syncfusion().Diagram([\"GridLines\"])]                                |
|                                                                                                                                                                        |
| [                  .Render();]                                                                                    |
|                                                                                                                                                                        |
| [    }]                                                                                                           |
|                                                                                                                                                                        |
| [  [%\>]][ ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

3.   Build and run the application.

{border="0"}

Figure 140: Customized Gridline Offset

 

 

[]{#related-topics}

