---
title: usingpropertiesmodel8.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel8.md
created_at: 2025-08-05
---






#### Using Properties Model {#using-properties-model style="PAGE-BREAK-AFTER: auto; tab-stops: 0pt"}

1.   In the **controller**, create an object for the **Node** class and set the **AllowResize** property.

2.   Create an object for the **DiagramPropertiesModel** class and set the Nodes property and pass this model class to the **view data**.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller ]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [DiagramPropertiesModel][ model = [new] [DiagramPropertiesModel]();]                                                                              |
|                                                                                                                                                                                                                                                                                                                          |
| [        [public] [ActionResult] FlatDiagram()]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                          |
| [Node][ node = [new] [Node]()]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [                Name = \"Node1\",                ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                          |
| [                 AllowResize=[true]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [            };]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                          |
| [            model.Nodes = [new NodesCollection()]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [                node1 ]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                          |
| [            };]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                          |
| [            model.Width = [Unit].Pixel(1100);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [            model.Height = [Unit].Pixel(500);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [            model.DiagramMode = ][DiagramMode][.SVG;][] |
|                                                                                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"FlatDiagram\"]\] = model;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

3.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.


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


[] 

4.   Build and run the application.

 

Resizing a node affects the node\'s **OffsetX**, **OffsetY**, **width**, and **height** properties. To resize a node:  

1.   Select the node that is to be resized.

2.   Move the pointer to the edge that you want to resize.

3.   The cursor will change to one with two arrows.

4.   Now drag the edge to the size you want. The node\'s **OffsetX**, **OffsetY**, **Height**, and **Width** properties will correspondingly change. 


Note: To resize both the width and height by the same factor, click and drag the corners of the resize adorner.


 

{border="0"}

Figure 43: Node Resizing Illustrated

 

 

[]{#related-topics}

