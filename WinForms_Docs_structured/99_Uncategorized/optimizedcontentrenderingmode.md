---
title: optimizedcontentrenderingmode.md
original_path: WinForms_Docs/99_Uncategorized/optimizedcontentrenderingmode.md
created_at: 2025-08-05
---








  









### Optimized Content Rendering Mode[] {#optimized-content-rendering-mode style="tab-stops: 0pt"}

[]{#p39}[] 

The **OptimizedContentRendering** mode affects only the diagram content.

 

It is useful to use this mode when the diagram document has many nodes, and it is not necessary to load all of them to the client. In this mode, only the required nodes will be rendered (depending on the view port size and diagram\'s magnification).

 

The nodes which are partly in view-port will be cropped (below image). If such node (nodes) is (are) dragged, it (they) will be rendered again, to show the new image (this operation is a bit slow).

[] 

{border="0"}

[] 

Figure 38: Cropped Node

[] 

When the magnification changes or the content scrolls (panning), the content will be reformed: nodes that are not necessary are deleted and new necessary nodes are created.

 

This mode is very useful when the diagram document has many nodes, and not all of them are in view-port at the same time. It is also useful when controls have to render large nodes (if sizes are equal to view-port or larger). The main advantage is that data transfer from the server to client machine is reduced, and also the memory usage on client is reduced.

[] 


{border="0"}[Note][: ]It is useless to use this mode, when all nodes are in the view-port. It will only decrease loading time and interaction speed.


[] 

***Warning***: Some interactive functionality will work slower: scrolling and panning of diagram. Dragging of the nodes will work slower too.

 

You can turn on or off the OptimizedContentRendering mode by using the **OptimizedContentRendering** public property. The following code example illustrates how to set this property.

[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                    |
| **[]**                                                                         |
|                                                                                                                    |
| [// Turn on]                                                     |
|                                                                                                                    |
| [DiagramWebControl1.OptimizedContentRendering = [true]; ] |
+--------------------------------------------------------------------------------------------------------------------+

[] 


+--------------------------------------------+--------------------------------------------------------------------------------------------------+
|                                            |                                                                                                  |
|                                            |                                                                                                  |
|                                            | Optimized Content Rendering Mode                                                                 |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Server Memory Usage**                    | Default.                                                                                         |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Client Memory Usage**                    | Decrease in most of cases.                                                                       |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Server HDD Space**                       | Default.                                                                                         |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Sever CPU Usage**                        | Default.                                                                                         |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Client CPU Usage**                       | Increases when scrolling, panning and dragging nodes.                                            |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Interactive Ability**                    | All interactions are allowed.                                                                    |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Interactive Speed**                      | Scrolling and panning will work slower, node dragging too.                                       |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Initial Loading Time on Client Browser** | Decrease when document has many nodes and not all of them are in the view-port at the same time. |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Data Size from Server to Client**        | Decrease in most of the cases.                                                                   |
+--------------------------------------------+--------------------------------------------------------------------------------------------------+


[] 

See Also

[] 

[Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Properties and Events for Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Background Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Flattened Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Optimization via HTML Elements]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Caching Modes]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event]{.UGHyperlink}[, ]{.UGHyperlink}[Optimization Customization]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

