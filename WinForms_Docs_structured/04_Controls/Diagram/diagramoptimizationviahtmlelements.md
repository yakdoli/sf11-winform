---
title: diagramoptimizationviahtmlelements.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\diagramoptimizationviahtmlelements.md
created_at: 2025-07-03
---








  









### Diagram Optimization via HTML Elements[] {#diagram-optimization-via-html-elements style="tab-stops: 0pt"}

[] 

There are situations when you do not have to render diagram document background as an image. If the diagram document background is simple, you can activate the optimization via HTML elements, by using the public property, **UseHTMLBackground**.

[] 


{border="0"}[Note][: ]A simple diagram document background is one that does not have any textures, color gradients or fill hatch styles, and so on.


[] 

The main advantages are increased loading speed, increased rendering speed, small memory usage and high interactivity speed. Also this optimization is not sensitive to the document size.

 

***[Warning]***[:]***[ ]***Diagram border cannot be drawn in this mode.

 

You can turn on or off this mode by using the **UseHTMLBackground** public property. The following code example illustrates how to set this property.

[] 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                            |
| **[]**                                                                 |
|                                                                                                            |
| [// Turn on]                                             |
|                                                                                                            |
| [DiagramWebControl1.UseHTMLBackground = [true]; ] |
+------------------------------------------------------------------------------------------------------------+

[] 

[] 


+--------------------------------------------+-----------------------------------+
|                                            |                                   |
|                                            |                                   |
|                                            | UseHTMLBackground                 |
+--------------------------------------------+-----------------------------------+
| **Server Memory Usage**                    | Decreases                         |
+--------------------------------------------+-----------------------------------+
| **Client Memory Usage**                    | Decreases                         |
+--------------------------------------------+-----------------------------------+
| **Server HDD Space**                       | Default                           |
+--------------------------------------------+-----------------------------------+
| **Sever CPU Usage**                        | Decreases                         |
+--------------------------------------------+-----------------------------------+
| **Client CPU Usage**                       | Decreases                         |
+--------------------------------------------+-----------------------------------+
| **Interactive Ability**                    | All interactions are allowed.     |
+--------------------------------------------+-----------------------------------+
| **Interactive Speed**                      | Default                           |
+--------------------------------------------+-----------------------------------+
| **Initial Loading Time on Client Browser** | Decreases                         |
+--------------------------------------------+-----------------------------------+
| **Data Size from Server to Client**        | Decreases                         |
+--------------------------------------------+-----------------------------------+


[] 

See Also

[] 

[Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Properties and Events for Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Background Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Content Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Caching Modes]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event]{.UGHyperlink}[, ]{.UGHyperlink}[Optimization Customization]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

