---
title: usingpropertiesmodel10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel10.md
created_at: 2025-07-03
---






#### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps guide on adding a label to the node through the properties model.

1.   In the **controller**, create an object for the **Node** class and set the **Label** and **LabelVisibility** properties.

2.  Create an object for the **DiagramPropertiesModel** class and set the **Nodes** property. Pass this model class to the **view data**.


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    [Node] node = [new] [Node]()]                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [        Name = [\"EssentialDiagram\"],]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [        Shape = [Shapes].RoundedRectangle,]                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [        LabelVisibility = [true,]]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [        Label = [\"Essential Diagram\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    };]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][DiagramPropertiesModel][ diagramModel = ][new][ ][DiagramPropertiesModel][()] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [         Width =  750,]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [         Height =  500,]                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [         DiagramMode = ][DiagramMode][.SVG,]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|              Nodes = new NodesCollection(){ node }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    };]**[]**                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

3.   In the **view**, invoke the diagram helper with the control ID which is the same as the **view data** name.

 

+---------------------------------------------------------------------------------------+
| **[View]**[ ] |
|                                                                                       |
| ```                                                      |
| <%{                                                                                   |
| ```                                                                                   |
|                                                                                       |
| ```                                                      |
|       Html.Syncfusion().Diagram("FlatDiagram")                                        |
| ```                                                                                   |
|                                                                                       |
| [          .Render();]                            |
|                                                                                       |
| ```                                                      |
|   }                                                                                   |
| ```                                                                                   |
|                                                                                       |
| [%\>][] |
+---------------------------------------------------------------------------------------+

 

4.   Build and run the application.

 

 

{border="0"}                           {border="0"}

Figure 46: Node Label(in Canvas Mode)                 Figure 47: Node Label(in SVG Mode)[]

 

[Label Editing][]

Create a diagram with a single node and the node\'s label can be edited at run time by setting the **IsLabelEditable** property to **True**.

 

 

To specify a label at run:

1.   Double-click on a node. A text box will appear with the cursor at the beginning.

2.   Now type the label name and press ENTER. The label will be displayed on the node.

 

{border="0"}                                      {border="0"}

Figure 48: Label Editor(in Canvas Mode)                              Figure 49: Label Editor(in SVG Mode)

 

[]{#related-topics}

