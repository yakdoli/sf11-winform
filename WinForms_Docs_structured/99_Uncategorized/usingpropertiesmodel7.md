---
title: usingpropertiesmodel7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel7.md
created_at: 2025-07-03
---






##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

1.   In the **controller**, create object for Node class and set the **AllowMove** property.

2.   Create an object for the **DiagramPropertiesModel** class and set the **Nodes** property. Pass this model class to **view data**.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller ]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [DiagramPropertiesModel][ model = [new] [DiagramPropertiesModel]();] |
|                                                                                                                                                                                                                                             |
| [        [public] [ActionResult] FlatDiagram()]                                                                                           |
|                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [Node][ node = [new] [Node]()]                                       |
|                                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                Name = \"Node1\",                ]                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [                 **AllowMove=[true]**]                                                                                                                           |
|                                                                                                                                                                                                                                             |
| [            };]                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [            model.Nodes = [new NodesCollection()]]                                                                                                               |
|                                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [                node1 ]                                                                                                                                                               |
|                                                                                                                                                                                                                                             |
| [            };]                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [            model.Width = [Unit].Pixel(1100);]                                                                                                                |
|                                                                                                                                                                                                                                             |
| [            model.Height = [Unit].Pixel(500);]                                                                                                                |
|                                                                                                                                                                                                                                             |
| [            [model.DiagramMode = ][DiagramMode][.SVG;]]                                                           |
|                                                                                                                                                                                                                                             |
| [            ViewData\[[\"FlatDiagram\"]\] = model;]                                                                                                           |
|                                                                                                                                                                                                                                             |
| [            [return] View();]                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

3.   In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
| [  [\<%]{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                |
| [              Html.Syncfusion().Diagram([\"]][FlatDiagram][\"][)] |
|                                                                                                                                                                                                                                                                                                                                                |
| [                  .Render();]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| [  [%\>]][ ]                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


4.   Build and run the application.

 

5.   A node's location can be changed at run time by clicking and dragging the node.

 

[]{#related-topics}

