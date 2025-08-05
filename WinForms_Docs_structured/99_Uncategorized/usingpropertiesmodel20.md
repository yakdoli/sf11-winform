---
title: usingpropertiesmodel20.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel20.md
created_at: 2025-08-05
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set the **HorizontalSpacing**, **Vertical Spacing**, and **SpaceBetweenSubTrees** properties. Pass this model class to the **view data**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [DiagramPropertiesModel][ diagramModel = [new] [DiagramPropertiesModel]();]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [            diagramModel.HorizontalSpacing = 100;]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [            diagramModel.VerticalSpacing = 50;]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [            diagramModel.SpaceBetweenSubTrees = 30;]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [           diagramModel][.DiagramMode = ][DiagramMode][.SVG;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

**[]** 

2.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.

 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [  [\<%]{]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [              Html.Syncfusion().Diagram([\"]][FlatDiagram\"][)] |
|                                                                                                                                                                                                                      |
| [                  .Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [  [%\>]][ ]                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

3.   Build and run the application.

 

The following screen shots illustrate the layout spacing.{border="0"}

Figure 101: Horizontal Spacing  

 

{border="0"}

Figure 102: Vertical Spacing

                                                                 

{border="0"}

Figure 103: Space between Sub-Trees

                                      * *

[]{#related-topics}

