---
title: usingpropertiesmodel21.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel21.md
created_at: 2025-07-03
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set the **Orientation** property. Pass this model class to the **view data**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller ]**                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [DiagramModel][ diagramModel = [new] [DiagramModel]();]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [diagramModel.Orientation = [TreeOrientation]. TopBottom;]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [diagramModel][.DiagramMode = ][DiagramMode][.SVG;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

2.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID, which is the same as the **view data** name.


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [  [\<%]{]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| [        Html.Syncfusion().Diagram([\"]][FlatDiagram\"][)] |
|                                                                                                                                                                                                                                                                   |
| [        .Render();]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [    }[%\>]][ ]                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


3.   Build and run the application.

The orientations are illustrated in the following figure.

 

{border="0"}

Figure 104: BottomTop Orientation

{border="0"}

Figure 105: TopBottom Orientation

 

{border="0"}

Figure 106: LeftRight Orientation

 

{border="0"}

Figure 107: RightLeft Orientation

 

[]{#related-topics}

