---
title: flattenedmode.md
original_path: WinForms_Docs/99_Uncategorized/flattenedmode.md
created_at: 2025-08-05
---








  









### Flattened Mode[] {#flattened-mode style="tab-stops: 0pt"}

[] 

Flattened mode is a simplified rendering mode. Background and contents (nodes) are rendered into a single image. This image will be cut to separate square images, if **OptimizedBackgroundRendering** mode is enabled.

 

This mode is useful when you do not have to perform any interactive operation with the node (selecting / dragging). It is designed especially for static documents. It is similar to the read-only mode.

 

This optimization mode reduces data transfer from the server to client. Also this optimization reduces loading time, when the document has many nodes.

 

***[Warning]***[:] Some interactive functionality won\'t work. For example, nodes dragging and selecting functionality.

 

You can turn on or off the Flattened mode by using the **Flattened** public property. The following code example illustrates how to set this property.

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                    |
| **[]**                                                         |
|                                                                                                    |
| [// Turn on]                                     |
|                                                                                                    |
| [DiagramWebControl1.Flattened = [true]; ] |
+----------------------------------------------------------------------------------------------------+

[] 


+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                            |                                                                                                                                                                                                           |
|                                            |                                                                                                                                                                                                           |
|                                            | Flattened Mode                                                                                                                                                                                            |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Server Memory Usage**                    | Default, except when OptimizedBackgroundRendering is activated. For details, see [Optimized Background Rendering Mode]{.UGHyperlink}.                                                                     |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Client Memory Usage**                    | Default, except when OptimizedBackgroundRendering is activated. For details, see [Optimized Background Rendering Mode]{.UGHyperlink}[.] |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Server HDD Space**                       | Default, except when OptimizedBackgroundRendering is activated. For details, see [Optimized Background Rendering Mode]{.UGHyperlink}.                                                                     |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Sever CPU Usage**                        | Default, except when OptimizedBackgroundRendering is activated. For details, see [Optimized Background Rendering Mode]{.UGHyperlink}.                                                                     |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Client CPU Usage**                       | May decrease when OptimizedBackgroundRendering is deactivated.                                                                                                                                            |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Interactive Ability**                    | No interaction -- only static view.                                                                                                                                                                       |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Interactive Speed**                      | Scrolling and panning will work faster when OptimizedBackgroundRendering is deactivated.                                                                                                                  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Initial Loading Time on Client Browser** | Decreases in most of cases.                                                                                                                                                                               |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Data Size from Server to Client**        | Decreases in most of cases.                                                                                                                                                                               |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

See Also

[] 

[Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Properties and Events for Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Background Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Content Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Optimization via HTML Elements]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Caching Modes]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event]{.UGHyperlink}[, ]{.UGHyperlink}[Optimization Customization]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

